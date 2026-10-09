"""Adapt validated family projections and retained artifacts to the website."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import yaml

from dufmech.report import ReportError
from dufmech.site_data import source_link
from dufmech.site_sources import REPOSITORY, load_source_pins, source_path


def _captured_source(path: str, raw: bytes | None, pins: dict) -> tuple[str, dict]:
    """Bind an immutable source link to the exact validated bytes being published."""
    if not source_path(path) or not isinstance(raw, bytes):
        raise ReportError(f"missing validated site source capture: {path}")
    pinned = pins.get(path, {})
    if pins and (pinned.get("path") != path
                 or pinned.get("sha256") != hashlib.sha256(raw).hexdigest()):
        raise ReportError(f"site source pin bytes differ from captured source: {path}")
    try:
        return raw.decode("utf-8"), dict(pinned)
    except UnicodeError as exc:
        raise ReportError(f"site source is not UTF-8: {path}") from exc


def metadata_from_records(records: list[dict], *, input_ids: dict, sources: dict) -> dict:
    """Keep source identities in the snapshots; attach actual curated content separately."""
    result = {}
    for record in records:
        pfam = record["pfam_id"]
        if pfam in result:
            raise ReportError(f"duplicate family record: {pfam}")
        if record["provenance"]["snapshot_id"] != input_ids["worklist"]:
            raise ReportError(f"{pfam}: family record and worklist snapshot disagree")
        result[pfam] = {
            "curation_status": record["curation_status"],
            "record": record,
            **({"source": sources[f"data/families/{pfam}.yaml"]}
               if f"data/families/{pfam}.yaml" in sources else {}),
        }
    return result


def load_review_site_metadata(
    root: Path, family_ids: set[str], *, source_pins: dict | None = None,
) -> tuple[dict, dict, dict]:
    """Retained reviews can accompany snapshot-only builds without certifying records."""
    from dufmech.reviews import load_review_metadata

    source_pins = load_source_pins(root) if source_pins is None else source_pins
    source_bytes: dict[str, bytes] = {}
    review_records = load_review_metadata(root, source_bytes=source_bytes)
    return _review_site_metadata(review_records, source_bytes, family_ids, source_pins)


def _review_site_metadata(
    review_records: list[dict], source_bytes: dict[str, bytes], family_ids: set[str], source_pins: dict,
) -> tuple[dict, dict, dict]:
    """Adapt one validated capture shared with the curation-status qualification."""
    metadata: dict[str, dict] = {}
    summaries, copies = [], {}
    for review in review_records:
        path = review["path"]
        if f"source/{path}" in copies:
            raise ReportError(f"duplicate captured review: {path}")
        content, pinned = _captured_source(path, source_bytes.get(path), source_pins)
        copies[f"source/{path}"] = content
        markdown_path = review.get("markdown_path")
        if markdown_path:
            markdown, _ = _captured_source(
                markdown_path, source_bytes.get(markdown_path), source_pins,
            )
            copies[f"source/{markdown_path}"] = markdown
        reference = {
            "url": source_link(pinned.get("repository", REPOSITORY), pinned.get("commit", ""), path),
            "local_source": f"source/{path}",
            "label": f"{review['finished_utc']}: {review['verdict']} by {review['reviewer']}",
            "scope": review["review_scope"], "scientific_review": review["scientific_review"],
        }
        summaries.append(reference)
        for pfam in review["context"]["members"]:
            if pfam in family_ids:
                metadata.setdefault(pfam, {}).setdefault("reviews", []).append(reference)
    return metadata, {"retained_reviews": summaries}, copies


def load_site_metadata(
    root: Path, input_ids: dict, *, source_pins: dict | None = None,
) -> tuple[dict, dict, dict[str, str]]:
    """Read parent-owned APIs once. Copies preserve uncommitted artifact access locally."""
    from dufmech.history import (
        _project_curation_events,
        _require_record_history_from_metadata,
        load_history_metadata,
    )
    from dufmech.records import _encoded, load_records
    from dufmech.reviews import (
        _require_completed_review_from_metadata,
        load_review_metadata,
        read_source_bytes,
    )

    root = root.resolve()
    records = load_records(root)
    source_pins = load_source_pins(root) if source_pins is None else source_pins
    sources = {}
    copies: dict[str, str] = {}
    for record in records:
        path = f"data/families/{record['pfam_id']}.yaml"
        # load_records verifies files against this exact deterministic serialization.
        # Publish that checked payload, never reopen a potentially replaced pathname.
        content, source = _captured_source(path, _encoded(record), source_pins)
        copies[f"source/{path}"] = content
        if source:
            sources[path] = source
    metadata = metadata_from_records(records, input_ids=input_ids, sources=sources)
    for record in records:
        pfam = record["pfam_id"]
        metadata[pfam]["local_source"] = f"source/data/families/{pfam}.yaml"

    history_bytes: dict[str, bytes] = {}
    history_by_family: dict[str, dict[str, dict]] = {}
    for history_record in load_history_metadata(root, source_bytes=history_bytes):
        target = history_record["target"]
        if target["kind"] != "record" or target["slug"] not in metadata:
            continue
        family_history = history_by_family.setdefault(target["slug"], {})
        path = history_record["path"]
        if path in family_history:
            raise ReportError(f"duplicate canonical history record: {path}")
        family_history[path] = history_record
    history_sources: dict[str, str] = {}
    for record in records:
        pfam = record["pfam_id"]
        family_history = history_by_family.get(pfam, {})
        indexed_events = record.get("curation_events", [])
        # Recheck after loading records to catch a sidecar change during the build.
        if indexed_events != _project_curation_events(list(family_history.values())):
            raise ReportError(f"{pfam}: curation_events differ from canonical history; regenerate records")
        if record.get("curation_history"):
            try:
                _require_record_history_from_metadata(
                    pfam, record["curation_history"], list(family_history.values()),
                )
            except ValueError as exc:
                raise ReportError(f"{pfam}: captured curation history is invalid: {exc}") from exc
        for entry in indexed_events:
            path = entry["history_record"]
            event = family_history[path]["events"][entry["event_index"]]
            if path not in history_sources:
                content, pinned = _captured_source(path, history_bytes.get(path), source_pins)
                copies[f"source/{path}"] = content
                history_sources[path] = source_link(
                    pinned.get("repository", REPOSITORY), pinned.get("commit", ""), path,
                )
            metadata[pfam].setdefault("history", []).append({
                **entry, "agent": entry["curator"], "description": event["details"],
                "url": history_sources[path], "source_path": path, "local_source": f"source/{path}",
            })
    review_bytes: dict[str, bytes] = {}
    captured_reviews = load_review_metadata(root, source_bytes=review_bytes)
    reviews, review_provenance, review_copies = _review_site_metadata(
        captured_reviews, review_bytes, set(metadata), source_pins,
    )
    reviews_by_path = {review["path"]: review for review in captured_reviews}
    for record in records:
        if record["curation_status"] != "REVIEWED":
            continue
        pfam, review_id = record["pfam_id"], record.get("review_id")
        if review_id not in reviews_by_path:
            raise ReportError(f"{pfam}: REVIEWED requires its captured review: {review_id}")
        try:
            _require_completed_review_from_metadata(
                pfam, review_id, record, reviews_by_path[review_id],
                list(history_by_family.get(pfam, {}).values()),
            )
        except ValueError as exc:
            raise ReportError(f"{pfam}: captured artifacts do not qualify REVIEWED: {exc}") from exc
    for pfam, fields in reviews.items():
        metadata[pfam].update(fields)
    copies.update(review_copies)
    schema_path = "src/dufmech/schema/dufmech.yaml"
    schema_text, schema_source = _captured_source(
        schema_path, read_source_bytes(root, schema_path), source_pins,
    )
    schema = yaml.safe_load(schema_text)
    copies["schema/dufmech.yaml"] = schema_text
    provenance = {**review_provenance, "schema": {
        **schema_source, "label": schema.get("title", "DUFMech LinkML schema"),
        "document": schema,
    }, "record_count": len(records)}
    shared_path = "src/dufmech/schema/mech_shared.yaml"
    try:
        shared_bytes = read_source_bytes(root, shared_path)
    except FileNotFoundError:
        if shared_path in source_pins:
            raise ReportError(f"pinned shared schema is missing: {shared_path}") from None
    else:
        shared_text, shared_source = _captured_source(shared_path, shared_bytes, source_pins)
        copies["schema/mech_shared.yaml"] = shared_text
        provenance["shared_schema"] = shared_source
    # Fail early if an adapter returns values that cannot be published as deterministic JSON.
    json.dumps([metadata, provenance])
    return metadata, provenance, copies
