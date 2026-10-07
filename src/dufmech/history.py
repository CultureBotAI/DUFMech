"""Write and validate append-only sidecar events using the governed history schema."""

from __future__ import annotations

import argparse
import json
import re
import secrets
import sys
from collections.abc import Sequence
from functools import lru_cache
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import yaml

from dufmech.reviews import (
    PFAM,
    REPO_ROOT,
    actual_text,
    append_document,
    artifact_paths,
    internal_href,
    read_yaml,
    safe_path,
    token,
    utc_timestamp,
)

SCHEMA_PATH = "src/dufmech/schema/history.yaml"
# Directory semantics from kg_microbe_history.scaffold; enum authority is the schema.
KIND_DIRS = {
    "record": "records", "schema": "schema", "mapping": "mappings", "report": "reports",
    "infrastructure": "infrastructure", "other": "other",
}


@lru_cache(maxsize=4)
def _validator(schema_path: str, schema_text: str):
    from linkml.validator import Validator
    from linkml.validator.plugins import JsonschemaValidationPlugin

    # The text is part of the cache key so a governed sync cannot leave stale validation.
    return Validator(schema=schema_path, validation_plugins=[JsonschemaValidationPlugin(closed=True)],
                     strict=True)


def history_validator(root: Path):
    """Load only the fleet-synchronized canonical file; never provide a local substitute."""
    try:
        path = safe_path(root, SCHEMA_PATH)
    except ValueError as exc:
        raise ValueError(
            f"canonical history schema unavailable at {SCHEMA_PATH}; run supported fleet sync"
        ) from exc
    return _validator(str(path), path.read_text(encoding="utf-8"))


def _validate_record(root: Path, record: Any, *, path: Path | None = None) -> None:
    validator = history_validator(root)
    if not isinstance(record, dict):
        raise TypeError("history record must be a mapping")
    report = validator.validate(record, target_class="HistoryRecord")
    if report.results:
        raise ValueError("history schema validation failed: " + "; ".join(
            str(result.message) for result in report.results
        ))
    if record["history_version"] != 1:
        raise ValueError("unsupported history_version")
    target, session = record["target"], record["session"]
    token(target.get("slug"))
    safe_path(root, target["path"], must_exist=path is None)
    timestamp = utc_timestamp(session["timestamp"])
    token(session["id"], "session.id")
    prefix = timestamp.strftime("%Y-%m-%dT%H%M%SZ-")
    if not session["id"].startswith(prefix):
        raise ValueError("session.id must begin with its UTC timestamp")
    for actor in session["actors"]:
        actual_text(actor["name"], "actor.name")
        for key in ("model", "agent_tool", "agent_version"):
            if key in actor:
                actual_text(actor[key], f"actor.{key}")
        if actor["type"] == "ai_agent" and (not actor.get("model") or not actor.get("agent_tool")):
            raise ValueError("AI history actors must identify model and agent_tool")
    for event in record["events"]:
        actual_text(event["summary"], "event.summary")
        actual_text(event["details"], "event.details")
    for urls in record.get("links", {}).values():
        for url in urls:
            parsed = urlsplit(url)
            if (parsed.scheme not in {"https", "http"} or not parsed.hostname
                    or parsed.username or parsed.password or any(ord(c) < 32 for c in url)):
                raise ValueError("history links must be public HTTP(S) URLs without credentials")
    if path is not None:
        expected = root.resolve() / "history" / KIND_DIRS[target["kind"]] / target["slug"]
        if path.parent != expected or path.stem != session["id"]:
            raise ValueError("history path must match target kind/slug and session.id")


def new_history(
    root: Path, *, kind: str, slug: str, target_path: str, timestamp: str,
    summary: str, details: str, actor_name: str, actor_type: str, event: str, outcome: str,
    model: str | None = None, agent_tool: str | None = None, agent_version: str | None = None,
    sections: Sequence[str] = (), issues: Sequence[str] = (), prs: Sequence[str] = (),
    urls: Sequence[str] = (),
) -> Path:
    """Create a completed, validated event about actual work; no default/fake events."""
    root = root.resolve(strict=True)
    if kind not in KIND_DIRS:
        raise ValueError(f"kind must be one of {tuple(KIND_DIRS)}")
    token(slug)
    actual_text(summary, "summary")
    actual_text(details, "details")
    actual_text(actor_name, "actor_name")
    safe_path(root, target_path)
    when = utc_timestamp(timestamp)
    actor = {"type": actor_type, "name": actor_name}
    for key, value in (("model", model), ("agent_tool", agent_tool), ("agent_version", agent_version)):
        if value is not None:
            actor[key] = value
    event_record: dict[str, Any] = {
        "type": event, "outcome": outcome, "summary": summary.strip(), "details": details,
    }
    if sections:
        event_record["sections"] = list(sections)
    actor_slug = re.sub(r"[^a-z0-9]+", "-", actor_name.lower()).strip("-") or "actor"
    stem = f"{when.strftime('%Y-%m-%dT%H%M%SZ')}-{actor_slug[:80]}-{secrets.token_hex(3)}"
    record = {
        "history_version": 1,
        "target": {"kind": kind, "slug": slug, "path": target_path},
        "session": {"id": stem, "timestamp": timestamp, "actors": [actor]},
        "events": [event_record],
    }
    links = {key: list(value) for key, value in (("issues", issues), ("prs", prs), ("urls", urls))
             if value}
    if links:
        record["links"] = links
    _validate_record(root, record)

    def render(session_id: str) -> str:
        record["session"]["id"] = session_id
        return yaml.safe_dump(record, sort_keys=False, allow_unicode=True)

    return append_document(root, f"history/{KIND_DIRS[kind]}/{slug}", stem, ".yaml", render)


def load_history_metadata(root: Path, pfam_id: str | None = None) -> list[dict[str, Any]]:
    """Return schema-validated events and repository-relative links for Pages.

    A removed historical target has target_href=None. Unsafe/symlinked targets
    still fail validation rather than becoming links outside the repository.
    """
    root = root.resolve(strict=True)
    directory = "history"
    if pfam_id is not None:
        if not isinstance(pfam_id, str) or not PFAM.fullmatch(pfam_id):
            raise ValueError("pfam_id must be an exact Pfam accession")
        # Per-record validation must not revalidate every other family's events.
        # The global check calls without an ID and still checks the complete tree.
        directory = f"history/records/{pfam_id}"
    paths = artifact_paths(root, directory, {".yaml", ".yml"})
    if paths:
        history_validator(root)
    result = []
    for path in paths:
        relative = path.relative_to(root).as_posix()
        record = read_yaml(safe_path(root, relative).read_text(encoding="utf-8"))
        _validate_record(root, record, path=path)
        if pfam_id is not None and not (
            record["target"]["kind"] == "record" and record["target"]["slug"] == pfam_id
        ):
            continue
        target = safe_path(root, record["target"]["path"], must_exist=False)
        result.append({
            **record, "path": relative, "href": internal_href(root, relative),
            "target_href": internal_href(root, record["target"]["path"]) if target.exists() else None,
        })
    return sorted(result, key=lambda item: (utc_timestamp(item["session"]["timestamp"]), item["path"]))


def require_record_history(root: Path, pfam_id: str, history_path: str) -> list[dict[str, Any]]:
    """Validate a stable curation_history directory backed by real family events."""
    if not PFAM.fullmatch(pfam_id) or history_path != f"history/records/{pfam_id}":
        raise ValueError("curation_history must be history/records/<exact Pfam accession>")
    directory = safe_path(root, history_path)
    if not directory.is_dir():
        raise ValueError("curation_history must identify a directory")
    targets = {f"data/families/{pfam_id}.yaml", f"curation/families/{pfam_id}.yaml"}
    events = [record for record in load_history_metadata(root, pfam_id)
              if record["target"]["path"] in targets]
    if not events:
        raise ValueError("curation_history requires an actual canonical event for this family")
    return events


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    commands = parser.add_subparsers(dest="command", required=True)
    new = commands.add_parser("new-history", aliases=["new"], help="save actual completed work")
    for name in ("kind", "slug", "path", "timestamp", "summary", "actor-name", "actor-type",
                 "event", "outcome"):
        new.add_argument(f"--{name}", required=True)
    detail = new.add_mutually_exclusive_group(required=True)
    detail.add_argument("--details")
    detail.add_argument("--details-file", type=Path)
    for name in ("model", "agent-tool", "agent-version"):
        new.add_argument(f"--{name}")
    for name in ("section", "issue", "pr", "url"):
        new.add_argument(f"--{name}", action="append", default=[])
    commands.add_parser("check", aliases=["validate"], help="validate the canonical schema and sidecars")
    listing = commands.add_parser("list", help="emit validated history metadata as JSON")
    listing.add_argument("--pfam-id")
    args = parser.parse_args(argv)
    try:
        if args.command in {"new-history", "new"}:
            if args.details_file is not None and args.details_file.is_symlink():
                raise ValueError("details input must not be a symlink")
            details = args.details_file.read_text() if args.details_file else args.details
            path = new_history(
                args.repo_root, kind=args.kind, slug=args.slug, target_path=args.path,
                timestamp=args.timestamp, summary=args.summary, details=details,
                actor_name=args.actor_name, actor_type=args.actor_type, event=args.event,
                outcome=args.outcome, model=args.model, agent_tool=args.agent_tool,
                agent_version=args.agent_version, sections=args.section, issues=args.issue,
                prs=args.pr, urls=args.url,
            )
            print(path)
        else:
            if getattr(args, "pfam_id", None) is not None and not PFAM.fullmatch(args.pfam_id):
                raise ValueError("pfam-id must be an exact Pfam accession")
            if args.command in {"check", "validate"}:
                history_validator(args.repo_root)
            records = load_history_metadata(args.repo_root, getattr(args, "pfam_id", None))
            print(json.dumps(records if args.command == "list" else {"valid_history": len(records)},
                             indent=2, sort_keys=True))
    except (TypeError, ValueError, OSError, RuntimeError, yaml.YAMLError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
