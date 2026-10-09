"""Inspect inputs and retain explicit, append-only DUFMech review reports."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import secrets
import stat
import subprocess
import sys
from collections.abc import Callable, Sequence
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any
from urllib.parse import quote

import yaml

from dufmech.report import latest_snapshot_path, load_json_rows, verified_manifest
from dufmech.snapshot import WORKLIST_STEM

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_DIRS = {
    "record": "reports/yaml_record_review",
    "category": "reports/yaml_category_review",
    "repo": "reports/repo_review",
}
COMMON_SECTIONS = (
    "Validation", "Identity and Grounding", "Evidence", "Completeness", "Findings",
    "Recommended Edits", "Follow-up Checks", "Additional Notes",
)
SECTIONS = {
    "record": ("Target", *COMMON_SECTIONS),
    "category": (
        "Target Category", "Selection and Membership", "Validation", "Lump and Split Review",
        "Identity and Grounding", "Evidence Patterns", "Completeness Patterns", "Findings",
        "Recommended Edits", "Follow-up Checks", "Additional Notes",
    ),
    "repo": ("Target Repository", "Scope and Selection", *COMMON_SECTIONS),
}
VERDICTS = ("SEED_ONLY", "NEEDS_FOLLOWUP", "BLOCKED", "FAIL", "PASS")
PFAM = re.compile(r"PF\d{5}")
TOKEN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,159}")
PLACEHOLDER = re.compile(
    r"(?:TODO|TBD|FIXME)(?:\s*[:\-].*)?[.!]?|placeholder[.!]?"
    r"|<[^>\n]+>|\[(?:fill|insert)[^]\n]*\]", re.IGNORECASE | re.DOTALL
)


class _UniqueKeyLoader(yaml.SafeLoader):
    """Do not silently replace an earlier review verdict or history event field."""


def _yaml_mapping(loader: _UniqueKeyLoader, node: yaml.MappingNode) -> dict:
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node)
    return result


_UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _yaml_mapping)


def read_yaml(text: str) -> Any:
    return yaml.load(text, Loader=_UniqueKeyLoader)


def token(value: Any, label: str = "slug") -> str:
    if not isinstance(value, str) or not TOKEN.fullmatch(value):
        raise ValueError(f"{label} must be a filename-safe token beginning with a letter or digit")
    return value


def actual_text(value: Any, label: str) -> str:
    """Reject empty/scaffold content; substantive correctness still needs a reviewer."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} requires actual non-placeholder content")
    lines = [line.strip() for line in value.splitlines() if line.strip()]
    if PLACEHOLDER.fullmatch(value.strip()) or all(
        PLACEHOLDER.fullmatch(line) or line.lower() in {"...", "n/a", "none", "pending", "not reviewed"}
        for line in lines
    ):
        raise ValueError(f"{label} requires actual non-placeholder content")
    return value.strip()


def _single_line(value: Any, label: str) -> str:
    value = actual_text(value, label)
    if any(ord(c) < 32 for c in value):
        raise ValueError(f"{label} must be a single line")
    return value


def utc_timestamp(value: Any) -> datetime:
    if not isinstance(value, str):
        raise TypeError("timestamps must be quoted ISO-8601 UTC strings")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("timestamps must be ISO-8601 UTC strings") from exc
    if parsed.tzinfo is None or parsed.utcoffset() != timedelta(0):
        raise ValueError("timestamps must explicitly use UTC (Z or +00:00)")
    return parsed


def relative_path(value: Any) -> Path:
    """Only accept unambiguous repository-relative paths, never URL syntax."""
    if (not isinstance(value, str) or not value or "\\" in value
            or any(ord(c) < 32 for c in value) or any(c in value for c in ":%?#")
            or value.startswith("/") or any(p in {"", ".", ".."} for p in value.split("/"))):
        raise ValueError(f"unsafe repository-relative path: {value!r}")
    return Path(value)


def safe_path(root: Path, relative: str, *, must_exist: bool = True) -> Path:
    root = root.resolve(strict=True)
    path = root
    for component in relative_path(relative).parts:
        path = path / component
        if path.is_symlink():
            raise ValueError(f"symlink paths are forbidden: {relative}")
    if must_exist and not path.exists():
        raise ValueError(f"missing repository path: {relative}")
    return path


def internal_href(root: Path, relative: str) -> str:
    """A validated, encoded link relative to the repository root (not the Pages root)."""
    safe_path(root, relative)
    return quote(relative, safe="/._-")


def read_source_bytes(root: Path, relative: str, *, max_bytes: int | None = None) -> bytes:
    """Capture one regular file without following symlinks in any path component."""
    root = root.absolute()
    if ".." in root.parts:
        raise ValueError("source root must not contain parent traversal")
    parts = (*root.parts[1:], *relative_path(relative).parts)
    directory = os.open(root.anchor, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        for component in parts[:-1]:
            child = os.open(component, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=directory)
            os.close(directory)
            directory = child
        descriptor = os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=directory)
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            os.close(descriptor)
            raise ValueError(f"source must be a regular file: {relative}")
        with os.fdopen(descriptor, "rb") as handle:
            raw = handle.read() if max_bytes is None else handle.read(max_bytes + 1)
            if max_bytes is not None and len(raw) > max_bytes:
                raise ValueError(f"source exceeds the {max_bytes} byte limit: {relative}")
            return raw
    finally:
        os.close(directory)


def append_document(
    root: Path, directory: str, stem: str, suffix: str, render: Callable[[str], str]
) -> Path:
    """Atomically publish a complete file without overwrites or symlink traversal.

    Directory descriptors keep creation pinned even if another writer renames a
    parent. Hard-link publication is exclusive; colliding names get numeric suffixes.
    """
    root = root.resolve(strict=True)
    token(stem, "artifact stem")
    if suffix not in {".md", ".yaml"}:
        raise ValueError("unsupported artifact extension")
    parts = relative_path(directory).parts
    fd = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        for component in parts:
            try:
                os.mkdir(component, dir_fd=fd)
            except FileExistsError:
                pass
            child = os.open(component, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = child
        for collision in range(10000):
            candidate = stem + (f"-{collision + 1:02d}" if collision else "")
            name = candidate + suffix
            try:
                entry = os.stat(name, dir_fd=fd, follow_symlinks=False)
            except FileNotFoundError:
                entry = None
            if entry is not None:
                if not stat.S_ISREG(entry.st_mode):
                    raise ValueError(f"artifact collision is not a regular file: {name}")
                continue
            content = render(candidate).encode("utf-8")
            temporary = f".append-{secrets.token_hex(12)}"
            temp_fd = os.open(
                temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644, dir_fd=fd
            )
            try:
                with os.fdopen(temp_fd, "wb") as handle:
                    handle.write(content)
                    handle.flush()
                    os.fsync(handle.fileno())
                try:
                    os.link(temporary, name, src_dir_fd=fd, dst_dir_fd=fd, follow_symlinks=False)
                except FileExistsError:
                    if not stat.S_ISREG(os.stat(name, dir_fd=fd, follow_symlinks=False).st_mode):
                        raise ValueError(f"artifact collision is not a regular file: {name}")
                    continue
                return root / directory / name
            finally:
                os.unlink(temporary, dir_fd=fd)
        raise ValueError("too many timestamp collisions")
    finally:
        os.close(fd)


def artifact_paths(root: Path, directory: str, suffixes: set[str]) -> list[Path]:
    """Inventory all files, including hidden/ignored entries; refuse any symlink."""
    base = safe_path(root, directory, must_exist=False)
    if not base.exists():
        return []
    if not base.is_dir():
        raise ValueError(f"artifact directory is not a directory: {directory}")
    found = []
    for path in sorted(base.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"symlink paths are forbidden: {path.relative_to(root.resolve())}")
        if path.is_file() and path.suffix in suffixes:
            found.append(path)
    return found


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def record_content_digest(record: dict[str, Any]) -> str:
    """Hash effective content, excluding review bookkeeping and the derived audit index."""
    content = {key: value for key, value in record.items()
               if key not in {"curation_status", "review_id", "curation_events"}}
    return hashlib.sha256(json.dumps(
        content, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False
    ).encode("utf-8")).hexdigest()


def _revision(root: Path) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True, check=True
    )
    revision = result.stdout.strip()
    if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", revision):
        raise ValueError("git HEAD did not resolve to a full revision")
    return revision


def inspect_review(
    root: Path, kind: str, slug: str, *, members: Sequence[str] = (), selection: str = "",
    snapshot_id: str | None = None, scope_paths: Sequence[str] = (),
) -> dict[str, Any]:
    """Return stable provenance and available data; never create a completed review."""
    root = root.resolve(strict=True)
    if kind not in REPORT_DIRS:
        raise ValueError("review kind must be record, category, or repo")
    token(slug)
    if kind == "record":
        members = [slug]
    elif kind == "category":
        _single_line(selection, "selection")
        if not members or len(set(members)) != len(members):
            raise ValueError("categories require explicit, unique member IDs")
    elif members:
        raise ValueError("repo reviews use scope_paths, not member IDs")
    if any(not isinstance(pfam, str) or not PFAM.fullmatch(pfam) for pfam in members):
        raise ValueError("members must be exact Pfam accessions (PF plus five digits)")
    worklists = safe_path(root, "data/worklists")
    if snapshot_id:
        token(snapshot_id, "snapshot_id")
        path = safe_path(root, f"data/worklists/{snapshot_id}.json")
    else:
        path = latest_snapshot_path(worklists, WORKLIST_STEM)
        assert path is not None
    manifest_path = safe_path(root, f"data/worklists/{path.stem}.manifest.json")
    manifest = json.loads(manifest_path.read_text())
    if not isinstance(manifest, dict) or not isinstance(manifest.get("files"), dict):
        raise TypeError("manifest must contain a files mapping")
    for entry in manifest.get("files", {}).values():
        if not isinstance(entry, dict):
            raise TypeError("manifest file entry must be a mapping")
        filename = entry.get("path")
        if not isinstance(filename, str) or Path(filename).name != filename:
            raise ValueError("manifest file entries must be filenames")
        safe_path(root, f"data/worklists/{filename}")
    verified_manifest(path)
    files = {str(manifest_path.relative_to(root)): _sha(manifest_path)}
    for entry in manifest["files"].values():
        name = f"data/worklists/{entry['path']}"
        files[name] = _sha(safe_path(root, name))
    rows = load_json_rows(path)
    indexed = {}
    for row in rows:
        pfam = row.get("pfam_id")
        if pfam in indexed:
            raise ValueError(f"duplicate snapshot Pfam identity: {pfam}")
        indexed[pfam] = row
    targets, records, record_digests = [], {}, {}
    for pfam in sorted(members):
        if pfam not in indexed:
            raise ValueError(f"{pfam} is absent from verified snapshot {path.stem}")
        locator = f"data/worklists/{path.name}#pfam_id={pfam}"
        record: dict[str, Any] = {"snapshot_row": indexed[pfam]}
        for label, directory in (("projection", "data/families"), ("curation", "curation/families")):
            relative = f"{directory}/{pfam}.yaml"
            candidate = safe_path(root, relative, must_exist=False)
            if candidate.exists():
                value = read_yaml(candidate.read_text())
                if not isinstance(value, dict):
                    raise ValueError(f"{relative} must contain a mapping")
                record[label] = value
                files[relative] = _sha(candidate)
                if label == "projection":
                    if value.get("pfam_id") != pfam or value.get("id") != f"Pfam:{pfam}":
                        raise ValueError(f"projection identity disagrees with filename: {relative}")
                    locator = relative
                    record_digests[pfam] = record_content_digest(value)
        targets.append({"id": pfam, "locator": locator})
        records[pfam] = record
    if kind == "repo":
        for relative in sorted(set(scope_paths or ("README.md", "pyproject.toml"))):
            files[relative] = _sha(safe_path(root, relative))
            targets.append({"id": relative, "locator": relative})
    context = {
        "kind": kind, "slug": slug, "source_revision": _revision(root),
        "source_state": "working_tree", "snapshot_id": path.stem,
        "source_files": dict(sorted(files.items())), "targets": targets,
        "members": sorted(members), "selection": selection if kind == "category" else "",
        "scope_paths": sorted(t["locator"] for t in targets) if kind == "repo" else [],
        "record_digests": record_digests,
    }
    from dufmech.structured_reviews import inspected_fields

    return {"status": "inspection_only", "context": context,
            "required_sections": list(SECTIONS[kind]), "records": records,
            "structured": inspected_fields(context)}


def _validate_context(root: Path, context: Any) -> None:
    if not isinstance(context, dict) or context.get("kind") not in REPORT_DIRS:
        raise ValueError("context requires a supported review kind")
    kind = context["kind"]
    keys = {"kind", "slug", "source_revision", "source_state", "snapshot_id", "source_files",
            "targets", "members", "selection", "scope_paths", "record_digests"}
    if set(context) != keys:
        raise ValueError("review context fields do not match inspection output")
    token(context.get("slug"))
    if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", str(context.get("source_revision", ""))):
        raise ValueError("source_revision must be a full Git revision")
    token(context.get("snapshot_id"), "snapshot_id")
    if context.get("source_state") != "working_tree":
        raise ValueError("source_state must identify the inspected working_tree")
    files = context.get("source_files")
    if not isinstance(files, dict) or not files:
        raise ValueError("context.source_files must contain input hashes")
    for relative, sha in files.items():
        safe_path(root, relative)
        if not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{64}", sha):
            raise ValueError("input hashes must be SHA-256")
    targets = context.get("targets")
    if not isinstance(targets, list) or not targets:
        raise ValueError("context.targets is required")
    ids = []
    for target in targets:
        if not isinstance(target, dict) or not isinstance(target.get("locator"), str):
            raise TypeError("invalid target locator")
        locator, sep, fragment = target["locator"].partition("#")
        if locator not in files:
            raise ValueError("target locator must be a hashed source file")
        safe_path(root, locator)
        if sep and (kind == "repo" or fragment != f"pfam_id={target.get('id')}"):
            raise ValueError("invalid snapshot row locator")
        ids.append(target.get("id"))
    members = context.get("members")
    if not isinstance(members, list) or not isinstance(context["scope_paths"], list):
        raise TypeError("members and scope_paths must be lists")
    if kind != "repo":
        if (not members or any(not isinstance(p, str) or not PFAM.fullmatch(p) for p in members)
                or members != sorted(set(members))
                or ids != members):
            raise ValueError("target IDs must match sorted, unique Pfam members")
        if kind == "record" and members != [context["slug"]]:
            raise ValueError("record slug must match its member")
    if kind == "category":
        _single_line(context.get("selection"), "selection")
    elif context["selection"] != "":
        raise ValueError("only category reviews carry a selection rule")
    if kind == "repo":
        if members or context["scope_paths"] != sorted(target["locator"] for target in targets):
            raise ValueError("repo scope_paths must match target locators")
    elif context["scope_paths"]:
        raise ValueError("only repo reviews carry scope_paths")
    digests = context.get("record_digests")
    if not isinstance(digests, dict) or any(
        key not in context.get("members", []) or not isinstance(value, str)
        or not re.fullmatch(r"[0-9a-f]{64}", value) for key, value in digests.items()
    ):
        raise ValueError("record_digests must map member IDs to SHA-256 content digests")


def _validate_content(root: Path, payload: Any) -> None:
    if not isinstance(payload, dict):
        raise TypeError("review content must be a mapping")
    _validate_context(root, payload.get("context"))
    start = utc_timestamp(payload.get("started_utc"))
    end = utc_timestamp(payload.get("finished_utc"))
    if end < start:
        raise ValueError("finished_utc precedes started_utc")
    if payload.get("verdict") not in VERDICTS:
        raise ValueError(f"verdict must be one of {VERDICTS}")
    _single_line(payload.get("reviewer"), "reviewer")
    _single_line(payload.get("review_scope"), "review_scope")
    if type(payload.get("scientific_review")) is not bool:
        raise ValueError("scientific_review must explicitly be true or false")
    if payload["verdict"] == "SEED_ONLY" and payload["scientific_review"]:
        raise ValueError("SEED_ONLY cannot certify scientific review")
    sections = payload.get("sections")
    if not isinstance(sections, dict):
        raise TypeError("sections must map fleet section headings to actual review text")
    required = SECTIONS[payload["context"]["kind"]]
    if set(sections) != set(required):
        raise ValueError(f"sections must be exactly: {', '.join(required)}")
    for heading, content in sections.items():
        actual_text(content, heading)
        if re.search(r"^#{1,2}\s", content, flags=re.MULTILINE):
            raise ValueError("section text may use level-three headings, not report-level headings")


def _render_report(payload: dict[str, Any]) -> str:
    context = payload["context"]
    kind = context["kind"]
    metadata = {k: v for k, v in payload.items() if k != "sections"}
    titles = {"record": "YAML Record Review", "category": "YAML Category Review",
              "repo": "Repository Review"}
    lines = ["---", yaml.safe_dump(metadata, sort_keys=False).rstrip(), "---", "",
             f"# {titles[kind]}: {context['slug']}", "",
             "- Repository: CultureBotAI/DUFMech",
             f"- {kind.title()}: {context['slug']}",
             f"- Source revision: `{context['source_revision']}` (working-tree hashes in metadata)",
             f"- Snapshot ID: `{context['snapshot_id']}`",
             f"- Started UTC: {payload['started_utc']}",
             f"- Finished UTC: {payload['finished_utc']}",
             f"- Verdict: {payload['verdict']}",
             f"- Scientific review: {str(payload['scientific_review']).lower()}",
             f"- Reviewer: {payload['reviewer']}",
             f"- Review scope: {payload['review_scope']}"]
    if kind == "category":
        lines.extend([f"- Selection Rule: {context['selection']}",
                      f"- Member IDs: {', '.join(context['members'])}"])
    for target in context["targets"]:
        lines.append(f"- Record locator: `{target['locator']}`")
    for heading in SECTIONS[kind]:
        lines.extend(["", f"## {heading}", "", payload["sections"][heading].strip()])
    return "\n".join(lines) + "\n"


def save_review(root: Path, payload: dict[str, Any]) -> Path:
    """Save new common bundles; legacy Markdown is supported only for reading."""
    from dufmech.structured_reviews import save

    return save(root, payload)


def read_review(
    root: Path, path: Path, *, source_bytes: dict[str, bytes] | None = None,
) -> dict[str, Any]:
    """Validate a captured report; optionally retain those exact bytes in an output sink."""
    relative = path.relative_to(root.absolute()).as_posix()
    raw = read_source_bytes(root, relative)
    if relative.startswith("reviews/structured/"):
        from dufmech.structured_reviews import common, metadata

        markdown_path = path.with_name("review.md").relative_to(root.absolute()).as_posix()
        markdown = read_source_bytes(root, markdown_path)
        review = common().parse_review_bundle(relative, raw, markdown)
        provenance = common().source_provenance(root, review)
        if provenance["status"] in {"invalid", "unverified"}:
            raise ValueError(f"source provenance {provenance['status']}: {provenance['reason']}")
        payload = metadata(review)
        if source_bytes is not None:
            source_bytes.update({relative: raw, markdown_path: markdown})
        return payload
    text = raw.decode("utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError(f"{relative}: missing review metadata")
    front, body = text[4:].split("\n---\n", 1)
    payload = read_yaml(front)
    if not isinstance(payload, dict) or payload.get("review_version") != 1:
        raise ValueError(f"{relative}: unsupported review metadata")
    if payload.get("status") != "saved":
        raise ValueError(f"{relative}: only explicitly saved reviews belong in reports")
    sections = {}
    chunks = re.split(r"^## (.+)\n", body, flags=re.MULTILINE)
    for i in range(1, len(chunks), 2):
        if chunks[i] in sections:
            raise ValueError(f"{relative}: duplicate review section")
        sections[chunks[i]] = chunks[i + 1].strip()
    payload["sections"] = sections
    _validate_content(root, payload)
    context = payload["context"]
    timestamp = utc_timestamp(payload["finished_utc"]).strftime("%Y%m%dT%H%M%SZ")
    expected = re.escape(f"{timestamp}-{context['slug']}") + r"(?:-[0-9]{2,})?\.md"
    if (path.parent != root.resolve() / REPORT_DIRS[context["kind"]]
            or not re.fullmatch(expected, path.name)):
        raise ValueError(f"{relative}: filename/directory disagrees with review metadata")
    if text != _render_report(payload):
        raise ValueError(f"{relative}: report body and metadata disagree")
    if source_bytes is not None:
        source_bytes[relative] = raw
    return payload


def load_review_metadata(
    root: Path, pfam_id: str | None = None, *, source_bytes: dict[str, bytes] | None = None,
) -> list[dict[str, Any]]:
    """Read validated reports and optionally capture their source bytes for publication.

    ``source_bytes`` is output-only; existing entries never substitute for a read.
    Hrefs remain relative to the repository root; source bytes are not metadata.
    """
    root = root.absolute()
    result = []
    from dufmech.structured_reviews import common

    groups = [artifact_paths(root, directory, {".md"}) for directory in REPORT_DIRS.values()]
    groups.append([root / name for name in common().review_paths(root)])
    for paths in groups:
        for path in paths:
            captured = {} if source_bytes is not None else None
            review = read_review(root, path, source_bytes=captured)
            if pfam_id is not None and pfam_id not in review["context"]["members"]:
                continue
            item = {k: v for k, v in review.items() if k != "sections"}
            item["path"] = path.relative_to(root).as_posix()
            item["href"] = internal_href(root, item["path"])
            if item["review_version"] == 2:
                item["markdown_path"] = path.with_name("review.md").relative_to(root).as_posix()
            result.append(item)
            if source_bytes is not None:
                source_bytes.update(captured)
    return sorted(result, key=lambda item: (utc_timestamp(item["finished_utc"]), item["path"]))


def review_report_url(review_id: str) -> str:
    """Stable append-only report URL used by canonical HistoryLinks.urls."""
    relative_path(review_id)
    return "https://github.com/CultureBotAI/DUFMech/blob/main/" + quote(review_id, safe="/._-")


def require_completed_review(
    root: Path, pfam_id: str, review_id: str, record: dict[str, Any],
) -> dict[str, Any]:
    """Gate REVIEWED on a current PASS report and a canonical linked REVIEW event.

    PASS applies only to the declared review_scope. scientific_review remains an
    independent explicit assertion, never inferred from curation_status.
    """
    from dufmech.history import load_history_metadata

    if not PFAM.fullmatch(pfam_id) or record.get("pfam_id") != pfam_id:
        raise ValueError("review target must match the effective FamilyRecord")
    path = safe_path(root, review_id)
    review = {**read_review(root, path), "path": review_id}
    history_records = load_history_metadata(root, pfam_id)
    return _require_completed_review_from_metadata(pfam_id, review_id, record, review, history_records)


def _require_completed_review_from_metadata(
    pfam_id: str, review_id: str, record: dict[str, Any], review: dict[str, Any],
    history_records: Sequence[dict[str, Any]],
) -> dict[str, Any]:
    """Apply the REVIEWED predicate to internally validated captured artifacts.

    This pure helper never loads or validates external input. Public callers use
    ``require_completed_review``; publication adapters pass the exact validated
    report and history metadata whose captured source bytes they publish.
    """
    if not PFAM.fullmatch(pfam_id) or record.get("pfam_id") != pfam_id:
        raise ValueError("review target must match the effective FamilyRecord")
    if review.get("path") != review_id:
        raise ValueError("review artifact path does not match review_id")
    context = review["context"]
    if (context["kind"] != "record" or context["members"] != [pfam_id]
            or review["verdict"] != "PASS"):
        raise ValueError("REVIEWED requires an explicit PASS per-record review")
    if review.get("review_version") == 2 and (
        review["native_verdict"] != "PASS" or review["common_verdict"] != "pass"
        or review["completion"] != "completed" or review["coverage"] != "full"
    ):
        raise ValueError("REVIEWED requires a completed full-scope structured PASS")
    if context["record_digests"].get(pfam_id) != record_content_digest(record):
        raise ValueError("reviewed record content changed or no projection was reviewed")
    expected_url = review_report_url(review_id)
    matches = []
    for history in history_records:
        if (history["target"]["kind"] == "record" and history["target"].get("slug") == pfam_id
                and history["target"]["path"] == f"data/families/{pfam_id}.yaml"
                and expected_url in history.get("links", {}).get("urls", [])
                and utc_timestamp(history["session"]["timestamp"])
                >= utc_timestamp(review["started_utc"])
                and any(event["type"] == "REVIEW" and event["outcome"] in {"changed", "no_change"}
                        for event in history["events"])):
            matches.append(history["path"])
    if not matches:
        raise ValueError("REVIEWED requires a canonical REVIEW event linked to this report URL")
    return {"review_id": review_id, "history_paths": sorted(matches),
            "review_scope": review["review_scope"], "scientific_review": review["scientific_review"],
            "record_digest": context["record_digests"][pfam_id]}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    commands = parser.add_subparsers(dest="command", required=True)
    inspect = commands.add_parser("inspect", help="read-only context; never a completed review")
    inspect.add_argument("kind", choices=REPORT_DIRS)
    inspect.add_argument("slug")
    inspect.add_argument("--members", nargs="+", default=[])
    inspect.add_argument("--selection", default="")
    inspect.add_argument("--snapshot-id")
    inspect.add_argument("--scope-path", action="append", default=[])
    save = commands.add_parser("save", aliases=["finalize"], help="append supplied actual content")
    save.add_argument("--content", type=Path, required=True)
    commands.add_parser("check", help="validate retained reports, including ignored/hidden files")
    listing = commands.add_parser("list", help="emit validated Pages metadata as JSON")
    listing.add_argument("--pfam-id")
    args = parser.parse_args(argv)
    try:
        if args.command == "inspect":
            result = inspect_review(
                args.repo_root, args.kind, args.slug, members=args.members, selection=args.selection,
                snapshot_id=args.snapshot_id, scope_paths=args.scope_path,
            )
            print(json.dumps(result, indent=2, sort_keys=True))
        elif args.command in {"save", "finalize"}:
            if args.content.is_symlink():
                raise ValueError("content input must not be a symlink")
            from dufmech.structured_reviews import common

            print(save_review(args.repo_root, common().load_document(args.content.read_bytes())))
        else:
            records = load_review_metadata(args.repo_root, getattr(args, "pfam_id", None))
            print(json.dumps(records if args.command == "list" else {"valid_reports": len(records)},
                             indent=2, sort_keys=True))
    except (TypeError, ValueError, OSError, RuntimeError, yaml.YAMLError,
            subprocess.CalledProcessError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
