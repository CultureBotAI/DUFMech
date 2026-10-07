"""Offline gap proposals from retained abstracts; acceptance is a separate review."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

import yaml

from dufmech.history import load_history_metadata, new_history
from dufmech.records import (
    RecordError,
    UniqueKeyLoader,
    _encoded,
    _publish_projection,
    _writer_lock,
    build_records,
    load_records,
    load_yaml,
    safe_path,
    validate_record,
)
from dufmech.reviews import (
    append_document,
    read_source_bytes,
    record_content_digest,
    utc_timestamp,
)

ROOT = Path(__file__).resolve().parents[2]
CONFIG = "conf/kgscan_config.yaml"
REFERENCE = re.compile(r"(?:PMID:[0-9]+|DOI:10\.[0-9]{4,9}/\S+)\Z")


def _unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise RecordError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise RecordError(f"{name} must be nonempty text")
    return value


def _config(root):
    cfg = load_yaml(safe_path(root, CONFIG))
    expected = {
        "repo_name": "DUFMech", "record_glob": "../data/families/*.yaml",
        "id_field": "id", "name_fields": ["short_name", "name"],
        "discussions_field": "discussions", "require_topic_in_sentence": True,
        "topic_token_min_matches": 0,
    }
    if set(cfg) != {*expected, "min_score"} or any(
        type(cfg[k]) is not type(v) or cfg[k] != v for k, v in expected.items()
    ):
        raise RecordError("kgscan config does not match the native precision contract")
    if type(cfg["min_score"]) is not int or cfg["min_score"] < 1:
        raise RecordError("min_score must be a positive integer")
    return cfg


def _abstracts(root, relative):
    if not relative.startswith("evidence/knowledge_gaps/") or not relative.endswith(".json"):
        raise RecordError("abstracts must be retained under evidence/knowledge_gaps/*.json")
    safe_path(root, relative)
    raw = read_source_bytes(root, relative, max_bytes=10_000_000)
    data = json.loads(raw, object_pairs_hook=_unique)
    if not isinstance(data, dict) or set(data) != {"version", "source_url", "retrieved_at", "results"}:
        raise RecordError("invalid retained abstract envelope")
    if type(data["version"]) is not int or data["version"] != 1:
        raise RecordError("unsupported abstract version")
    url = urlsplit(_text(data["source_url"], "source_url"))
    if url.scheme != "https" or not url.hostname or url.username or url.password:
        raise RecordError("source_url must be public HTTPS without credentials")
    utc_timestamp(data["retrieved_at"])
    rows = data["results"]
    if not isinstance(rows, list) or not 1 <= len(rows) <= 1000:
        raise RecordError("retain between 1 and 1000 abstracts per cache")
    references = set()
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"reference", "title", "abstract"}:
            raise RecordError("invalid retained abstract row")
        if not REFERENCE.fullmatch(_text(row["reference"], "reference")):
            raise RecordError("abstract reference must be PMID or DOI")
        if row["reference"] in references:
            raise RecordError("duplicate abstract reference")
        references.add(row["reference"])
        _text(row["title"], "title")
        _text(row["abstract"], "abstract")
    return data, hashlib.sha256(raw).hexdigest()


def scan(root: Path, abstracts: str, *, offset: int = 0, limit: int = 25,
         records: list[dict] | None = None) -> dict:
    """Reuse shared sentence scoring and Discussion shape without any network call."""
    try:
        from kg_microbe_kgscan import scan as shared_scan
        from kg_microbe_kgscan.scan import (
            build_discussion,
            extract_gap_signals,
            prompt_key,
            signal_score,
        )
    except ModuleNotFoundError as exc:
        raise RecordError("Shared gap scanner unavailable; set CLAW_SRC to the published "
                          "CLAW src directory and use just knowledge-gap-scan") from exc

    if type(offset) is not int or offset < 0 or type(limit) is not int or not 1 <= limit <= 100:
        raise RecordError("offset must be nonnegative and limit must be between 1 and 100")
    cfg = _config(root)
    cache, digest = _abstracts(root, abstracts)
    corpus = load_records(root) if records is None else records
    corpus = sorted(corpus, key=lambda r: r["id"])
    if not corpus:
        raise RecordError("cannot scan an empty corpus")
    owners = {}
    for record in corpus:
        for discussion in record.get("discussions", []):
            for evidence in discussion.get("evidence", []):
                key = prompt_key({"evidence": [evidence]})
                if key:
                    owners.setdefault(key, set()).add(record["id"])
    start = offset % len(corpus)
    window = (corpus[start:] + corpus[:start])[:limit]
    proposed = []
    for record in window:
        terms = list(dict.fromkeys([record["short_name"], record["name"], record["pfam_id"]]))
        matches = []
        for article in cache["results"]:
            signals = extract_gap_signals(article["abstract"], max_signals=8,
                                          topic_terms=terms, require_topic=True)
            if signals:
                matches.append({"reference": article["reference"], "title": article["title"],
                                "signals": signals, "score": signal_score(signals)})
        matches.sort(key=lambda item: (-item["score"], item["reference"]))
        score = sum(item["score"] for item in matches)
        if score < cfg["min_score"]:
            continue
        discussion = build_discussion(record["id"], {"name": record["short_name"], "matches": matches})
        discussion["rationale"] = (
            f"Surfaced by offline gap-signal scoring of retained abstracts from "
            f"{cache['source_url']} (retrieved {cache['retrieved_at']}; SHA-256 {digest}). "
            "The quotation and family scope require curator review; this is not functional evidence."
        )
        keys = {prompt_key({"evidence": [e]}) for e in discussion.get("evidence", [])}
        keys.discard(None)
        proposed.append({"record_id": record["id"], "pfam_id": record["pfam_id"],
                         "record_sha256": record_content_digest(record), "score": score,
                         "discussion": discussion, "sentence_keys": keys})
    selected = set()
    for candidate in sorted(proposed, key=lambda p: (-p["score"], p["record_id"])):
        keys = candidate["sentence_keys"]
        existing = set().union(*(owners.get(key, set()) for key in keys))
        candidate["existing_owners"] = sorted(existing)
        candidate["status"] = (
            "already_filed" if existing else
            "cross_record_duplicate" if keys & selected else "proposed"
        )
        if candidate["status"] == "proposed":
            selected.update(keys)
    results = []
    for candidate in sorted(proposed, key=lambda p: p["record_id"]):
        candidate.pop("sentence_keys")
        results.append(candidate)
    return {"version": 1, "repo_name": "DUFMech", "engine": "retained-abstracts-offline",
            "engine_sha256": hashlib.sha256(Path(shared_scan.__file__).read_bytes()).hexdigest(),
            "abstracts": abstracts, "abstracts_sha256": digest,
            "source_url": cache["source_url"], "retrieved_at": cache["retrieved_at"],
            "config_sha256": hashlib.sha256(safe_path(root, CONFIG).read_bytes()).hexdigest(),
            "offset": offset, "limit": limit, "records_scanned": len(window),
            "scanned_records": [{"record_id": r["id"], "sha256": record_content_digest(r)}
                                for r in window],
            "min_score": cfg["min_score"], "results": results}


def retain(root: Path, packet: dict, timestamp: str) -> tuple[Path, Path]:
    """Retain complete, timestamped proposals; never change scientific records."""
    when = utc_timestamp(timestamp)
    packet = {**packet, "created_at": timestamp}
    stem = when.strftime("%Y%m%dT%H%M%SZ") + "-knowledge-gaps"
    path = append_document(root, "reports/knowledge_gap_scan", stem, ".yaml",
                           lambda _: yaml.safe_dump(packet, sort_keys=False, allow_unicode=True))
    lines = ["# DUFMech Knowledge-Gap Proposals", "", f"- Timestamp: {timestamp}",
             f"- Packet: `{path.relative_to(root).as_posix()}`",
             f"- Abstract cache SHA-256: `{packet['abstracts_sha256']}`",
             f"- Records scanned: {packet['records_scanned']}",
             "- Method: offline shared sentence scoring over retained abstracts.",
             "- Status: proposals only; no record changed or scientific review claimed.", "",
             "## Findings", ""]
    for candidate in packet["results"]:
        lines.extend([f"### {candidate['record_id']}", "",
                      f"- Disposition: {candidate['status']}; score: {candidate['score']}",
                      candidate["discussion"]["prompt"], ""])
    if not packet["results"]:
        lines.extend(["No sentences passed the configured gates in this window.", ""])
    lines.extend(["## Limitations", "",
                  ("A matching sentence is not verified functional evidence. The retained source, "
                   "quotation, family scope and interpretation require curator review."), "",
                  "## Next Actions", "",
                  "Review selected proposals and record a canonical family audit before acceptance.", ""])
    report = append_document(root, "reports/knowledge_gap_scan", stem, ".md",
                             lambda _: "\n".join(lines))
    return path, report


def _packet_bytes(root: Path, packet_path: str) -> bytes:
    if not packet_path.startswith("reports/knowledge_gap_scan/") or not packet_path.endswith(".yaml"):
        raise RecordError("acceptance requires a retained proposal packet")
    return read_source_bytes(root, packet_path, max_bytes=10_000_000)


def approval_details(root: Path, packet_path: str, pfam: str, rationale: str) -> str:
    """Render an explicit decision for a curator to retain in canonical event details."""
    if not re.fullmatch(r"PF[0-9]{5}", pfam):
        raise RecordError("expected exact Pfam accession")
    return json.dumps({
        "contract": "dufmech-gap-approval-v1", "decision": "ACCEPT", "pfam_id": pfam,
        "packet": packet_path, "packet_sha256": hashlib.sha256(_packet_bytes(root, packet_path)).hexdigest(),
        "rationale": _text(rationale, "rationale"),
    }, sort_keys=True)


def _approved(event: dict, packet_path: str, digest: str, pfam: str) -> bool:
    if event["type"] != "REVIEW" or event["outcome"] != "no_change":
        return False
    try:
        decision = json.loads(event["details"], object_pairs_hook=_unique)
        if not isinstance(decision, dict):
            return False
        rationale = decision.pop("rationale")
        _text(rationale, "rationale")
    except (ValueError, KeyError, TypeError):
        return False
    return decision == {
        "contract": "dufmech-gap-approval-v1", "decision": "ACCEPT", "pfam_id": pfam,
        "packet": packet_path, "packet_sha256": digest,
    }


def accept(root: Path, packet_path: str, pfam: str, history_path: str, *, apply=False,
           actor_name: str, actor_type: str, model: str | None = None,
           agent_tool: str | None = None) -> dict:
    """Preview, then explicitly accept one reviewed proposal into its native overlay."""
    if not re.fullmatch(r"PF[0-9]{5}", pfam):
        raise RecordError("expected exact Pfam accession")
    _text(actor_name, "actor_name")
    if actor_type not in {"human", "ai_agent"}:
        raise RecordError("actor_type must be human or ai_agent")
    if actor_type == "ai_agent" and (not model or not agent_tool):
        raise RecordError("AI actors require model and agent_tool")
    with _writer_lock(root):
        raw_packet = _packet_bytes(root, packet_path)
        packet = yaml.load(raw_packet, Loader=UniqueKeyLoader)
        if not isinstance(packet, dict):
            raise RecordError("proposal packet must be an object")
        utc_timestamp(packet.get("created_at"))
        destination = safe_path(root, f"curation/families/{pfam}.yaml")
        try:
            before = read_source_bytes(root, destination.relative_to(root).as_posix(),
                                       max_bytes=10_000_000)
        except FileNotFoundError:
            before = None
        corpus = list(build_records(root).values())
        replay = scan(root, packet["abstracts"], offset=packet["offset"], limit=packet["limit"],
                      records=corpus)
        if {k: v for k, v in packet.items() if k != "created_at"} != replay:
            raise RecordError("proposal packet is stale or differs from retained-source replay")
        candidate = next((r for r in replay["results"] if r["pfam_id"] == pfam), None)
        if candidate is None or candidate["status"] != "proposed":
            raise RecordError("no unfiled proposal for this family")
        audits = load_history_metadata(root, pfam)
        audit = next((a for a in audits if history_path ==
                      f"history/records/{pfam}/{a['session']['id']}.yaml"), None)
        if audit is None or audit["target"]["path"] not in {
            f"data/families/{pfam}.yaml", f"curation/families/{pfam}.yaml",
        }:
            raise RecordError("need a canonical REVIEW/no_change audit targeting this exact family")
        if utc_timestamp(audit["session"]["timestamp"]) < utc_timestamp(packet["created_at"]):
            raise RecordError("review must not predate the proposal packet")
        digest = hashlib.sha256(raw_packet).hexdigest()
        if not any(_approved(e, packet_path, digest, pfam) for e in audit["events"]):
            raise RecordError("need a canonical REVIEW/no_change affirmative approval bound to packet SHA-256 and family")
        current = list(build_records(root).values())
        if [record_content_digest(r) for r in current] != [record_content_digest(r) for r in corpus]:
            raise RecordError("corpus changed during proposal replay")
        prior = (yaml.load(before, Loader=UniqueKeyLoader) if before is not None else
                 {"pfam_id": pfam, "curation_status": "SEEDED"})
        overlay = copy.deepcopy(prior)
        overlay["curation_status"] = "IN_PROGRESS"
        overlay.pop("review_id", None)
        overlay["curation_history"] = f"history/records/{pfam}"
        overlay.setdefault("discussions", []).append(candidate["discussion"])
        validate_record(overlay, root, target="FamilyCuration")
        result = {"pfam_id": pfam, "apply": apply, "overlay": overlay,
                  "review_history": history_path, "packet": packet_path}
        if apply:
            _publish_projection(root, destination, _encoded(overlay), before)
            try:
                event = new_history(
                    root, kind="record", slug=pfam,
                    target_path=f"curation/families/{pfam}.yaml",
                    timestamp=datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                    summary="Accepted a reviewed knowledge-gap proposal; function remains unscored.",
                    details=f"Accepted {packet_path} (SHA-256 {digest}) after review in {history_path}; "
                            f"abstract cache SHA-256 {packet['abstracts_sha256']}.",
                    actor_name=actor_name, actor_type=actor_type, model=model,
                    agent_tool=agent_tool, event="EDIT", outcome="changed",
                    sections=["discussions"],
                )
            except BaseException:
                # Keep a visible recovery trail; never discard a concurrently edited overlay.
                _publish_projection(root, destination, before or _encoded(prior), _encoded(overlay))
                raise
            result["change_history"] = event.relative_to(root).as_posix()
        return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    commands = parser.add_subparsers(dest="command", required=True)
    propose = commands.add_parser("scan")
    propose.add_argument("--abstracts", required=True)
    propose.add_argument("--offset", type=int, default=0)
    propose.add_argument("--limit", type=int, default=25)
    decision = commands.add_parser("approval")
    decision.add_argument("--packet", required=True)
    decision.add_argument("--pfam", required=True)
    decision.add_argument("--rationale", required=True)
    approve = commands.add_parser("accept")
    approve.add_argument("--packet", required=True)
    approve.add_argument("--pfam", required=True)
    approve.add_argument("--history", required=True)
    approve.add_argument("--apply", action="store_true")
    approve.add_argument("--actor-name", required=True)
    approve.add_argument("--actor-type", choices=["human", "ai_agent"], required=True)
    approve.add_argument("--model")
    approve.add_argument("--agent-tool")
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve(strict=True)
        if args.command == "scan":
            packet = scan(root, args.abstracts, offset=args.offset, limit=args.limit)
            timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
            for path in retain(root, packet, timestamp):
                print(path.relative_to(root))
        elif args.command == "approval":
            print(approval_details(root, args.packet, args.pfam, args.rationale))
        else:
            print(json.dumps(accept(root, args.packet, args.pfam, args.history,
                                    apply=args.apply, actor_name=args.actor_name,
                                    actor_type=args.actor_type, model=args.model,
                                    agent_tool=args.agent_tool), indent=2))
        return 0
    except (ValueError, OSError, KeyError, TypeError, ImportError) as exc:
        print(f"knowledge-gap adapter: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
