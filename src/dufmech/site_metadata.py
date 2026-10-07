"""Adapt validated family projections and retained artifacts to the website."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from dufmech.report import ReportError
from dufmech.site_data import source_link, tracked_source
from dufmech.site_sources import REPOSITORY, load_source_pins


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
    metadata: dict[str, dict] = {}
    summaries, copies = [], {}
    for review in load_review_metadata(root):
        path = review["path"]
        copies[f"source/{path}"] = (root / path).read_text(encoding="utf-8")
        pinned = tracked_source(root / path, root, pins=source_pins)
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
    from dufmech.history import load_history_metadata
    from dufmech.records import load_records

    root = root.resolve()
    records = load_records(root)
    source_pins = load_source_pins(root) if source_pins is None else source_pins
    sources = {}
    for record in records:
        path = f"data/families/{record['pfam_id']}.yaml"
        source = tracked_source(root / path, root, pins=source_pins)
        if source:
            sources[path] = source
    metadata = metadata_from_records(records, input_ids=input_ids, sources=sources)
    copies: dict[str, str] = {}
    for record in records:
        pfam = record["pfam_id"]
        # A local copy remains truthful during integration before a new source commit exists.
        path = f"data/families/{pfam}.yaml"
        copies[f"source/{path}"] = (root / path).read_text(encoding="utf-8")
        metadata[pfam]["local_source"] = f"source/{path}"

    def artifact(path: str) -> str:
        copies[f"source/{path}"] = (root / path).read_text(encoding="utf-8")
        pinned = tracked_source(root / path, root, pins=source_pins)
        return source_link(pinned.get("repository", REPOSITORY), pinned.get("commit", ""), path)

    for history in load_history_metadata(root):
        target = history["target"]
        if target["kind"] != "record" or target["slug"] not in metadata:
            continue
        url = artifact(history["path"])
        for event in history["events"]:
            metadata[target["slug"]].setdefault("history", []).append({
                "timestamp": history["session"]["timestamp"],
                "agent": ", ".join(actor["name"] for actor in history["session"]["actors"]),
                "action": event["type"], "summary": event["summary"],
                "description": event["details"], "outcome": event["outcome"],
                "url": url, "source_path": history["path"], "local_source": f"source/{history['path']}",
            })
    reviews, review_provenance, review_copies = load_review_site_metadata(
        root, set(metadata), source_pins=source_pins,
    )
    for pfam, fields in reviews.items():
        metadata[pfam].update(fields)
    copies.update(review_copies)
    schema_path = root / "src/dufmech/schema/dufmech.yaml"
    schema = yaml.safe_load(schema_path.read_text(encoding="utf-8"))
    copies["schema/dufmech.yaml"] = schema_path.read_text(encoding="utf-8")
    shared = root / "src/dufmech/schema/mech_shared.yaml"
    if shared.is_file():
        copies["schema/mech_shared.yaml"] = shared.read_text(encoding="utf-8")
    schema_source = tracked_source(schema_path, root, pins=source_pins)
    provenance = {**review_provenance, "schema": {
        **schema_source, "label": schema.get("title", "DUFMech LinkML schema"),
        "document": schema,
    }, "record_count": len(records)}
    if shared.is_file():
        provenance["shared_schema"] = tracked_source(shared, root, pins=source_pins)
    # Fail early if an adapter returns values that cannot be published as deterministic JSON.
    json.dumps([metadata, provenance])
    return metadata, provenance, copies
