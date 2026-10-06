"""Version a seed-classification correction from verified, frozen metadata."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from dataclasses import dataclass, fields
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.provenance import check_manifest
from dufmech.report import ReportError, family_index
from dufmech.snapshot import WORKLIST_STEM, build_worklist_manifest, write_snapshot_artifacts
from dufmech.worklist import (
    CLASSIFIER_POLICY,
    DufFamilyRow,
    reclassify_worklist,
    render_json,
    render_tsv,
)


@dataclass(frozen=True)
class PreparedReclassification:
    """Verified correction artifacts and a dry-run summary, with no files written."""

    manifest: dict[str, Any]
    artifacts: dict[str, str]
    summary: dict[str, Any]


def prepare_reclassification(
    input_json: Path,
    *,
    snapshot_date: str,
    generated_at: datetime | None = None,
) -> PreparedReclassification:
    """Validate frozen input and prepare complete correction provenance without writing."""

    manifest_path = input_json.with_suffix(".manifest.json")
    issues = check_manifest(manifest_path)
    if issues:
        raise ReportError("; ".join(issue.render() for issue in issues))
    manifest_bytes = manifest_path.read_bytes()
    parent = json.loads(manifest_bytes)
    if input_json.name != parent["files"]["json"]["path"]:
        raise ReportError("input must be the JSON artifact declared by its manifest")
    if not parent["snapshot"]["id"].startswith(f"{WORKLIST_STEM}-"):
        raise ReportError("input must be an InterPro/Pfam worklist snapshot")
    day = date.fromisoformat(snapshot_date)
    if day <= date.fromisoformat(parent["snapshot"]["date"]):
        raise ReportError(
            "reclassification needs a newer snapshot date, later than the input snapshot date"
        )
    input_bytes = input_json.read_bytes()
    if (
        hashlib.sha256(input_bytes).hexdigest() != parent["files"]["json"]["sha256"]
        or len(input_bytes) != parent["files"]["json"]["bytes"]
    ):
        raise ReportError("input JSON changed after manifest validation")
    payload = json.loads(input_bytes)
    family_index(payload)
    row_fields = {field.name for field in fields(DufFamilyRow)}
    rows = []
    for row in payload:
        if set(row) != row_fields | {"source_url"}:
            raise ReportError(f"{row['pfam_id']}: unexpected or missing worklist fields")
        if not isinstance(row["candidate_reasons"], list) or any(
            not isinstance(reason, str) for reason in row["candidate_reasons"]
        ):
            raise ReportError(f"{row['pfam_id']}: candidate_reasons must be a string list")
        for field in ("short_name", "name", "interpro_id", "description", "source_url"):
            if not isinstance(row[field], str):
                raise ReportError(f"{row['pfam_id']}: {field} must be a string")
        normalized = DufFamilyRow(**{key: row[key] for key in row_fields})
        if row["source_url"] != normalized.source_url:
            raise ReportError(f"{row['pfam_id']}: cannot preserve a noncanonical source_url")
        rows.append(normalized)
    corrected = reclassify_worklist(rows)
    snapshot_id = f"{WORKLIST_STEM}-{day.isoformat()}"
    texts = {
        f"{snapshot_id}.json": render_json(corrected) + "\n",
        f"{snapshot_id}.tsv": render_tsv(corrected) + "\n",
    }
    manifest = build_worklist_manifest(
        corrected,
        snapshot_id=snapshot_id,
        snapshot_date=day.isoformat(),
        generated_at=generated_at or datetime.now(timezone.utc),
        json_path=Path(f"{snapshot_id}.json"),
        json_text=texts[f"{snapshot_id}.json"],
        tsv_path=Path(f"{snapshot_id}.tsv"),
        tsv_text=texts[f"{snapshot_id}.tsv"],
    )
    original = {row.pfam_id: row for row in rows}
    transitions = Counter(
        f"{original[row.pfam_id].unknown_status} -> {row.unknown_status}"
        for row in corrected
        if row.unknown_status != original[row.pfam_id].unknown_status
    )
    manifest["source"] = parent["source"]
    manifest["snapshot"]["input_snapshot_ids"] = {"worklist": parent["snapshot"]["id"]}
    manifest["derivation"] = {
        "method": "reclassify_saved_worklist",
        "classifier_policy": CLASSIFIER_POLICY,
        "input_snapshot_generated_at": parent["snapshot"]["generated_at"],
        "input_files": {
            **parent["files"],
            "manifest": {
                "path": manifest_path.name,
                "bytes": len(manifest_bytes),
                "sha256": hashlib.sha256(manifest_bytes).hexdigest(),
            },
        },
        "changed_fields": ["unknown_status", "candidate_reasons"],
        "changed_status_rows": sum(transitions.values()),
        "changed_reason_rows": sum(
            tuple(row.candidate_reasons) != tuple(original[row.pfam_id].candidate_reasons)
            for row in corrected
        ),
        "status_transitions": dict(sorted(transitions.items())),
        "fetched_live": False,
    }
    changes = [
        {
            "pfam_id": row.pfam_id,
            "before": original[row.pfam_id].unknown_status,
            "after": row.unknown_status,
            "before_reasons": list(original[row.pfam_id].candidate_reasons),
            "after_reasons": list(row.candidate_reasons),
        }
        for row in corrected
        if row.unknown_status != original[row.pfam_id].unknown_status
        or tuple(row.candidate_reasons) != tuple(original[row.pfam_id].candidate_reasons)
    ]
    summary = {
        "source_snapshot": parent["snapshot"]["id"],
        "source_sha256": parent["files"]["json"]["sha256"],
        "policy": CLASSIFIER_POLICY,
        "rows": len(corrected),
        "changed_statuses": sum(transitions.values()),
        "by_unknown_status": manifest["rows"]["by_unknown_status"],
        "changes": changes,
    }
    texts[f"{snapshot_id}.manifest.json"] = json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    return PreparedReclassification(manifest, texts, summary)


def reclassify_snapshot(
    input_json: Path,
    out_dir: Path,
    *,
    snapshot_date: str,
    generated_at: datetime | None = None,
) -> dict[str, Any]:
    """Create a new, non-overwriting JSON/TSV/manifest snapshot without fetching data."""

    prepared = prepare_reclassification(
        input_json, snapshot_date=snapshot_date, generated_at=generated_at
    )
    write_snapshot_artifacts(out_dir, prepared.artifacts)
    return prepared.manifest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-json", type=Path, required=True)
    parser.add_argument("--snapshot-date", required=True, help="new ISO date, later than the input")
    parser.add_argument("--out-dir", type=Path, default=Path("data/worklists"))
    args = parser.parse_args(argv)
    try:
        manifest = reclassify_snapshot(
            args.input_json, args.out_dir, snapshot_date=args.snapshot_date
        )
    except (ReportError, OSError, ValueError) as exc:
        parser.exit(1, f"reclassification failed: {exc}\n")
    print(
        f"wrote {manifest['snapshot']['id']} ({manifest['rows']['total']} families; "
        f"{manifest['derivation']['changed_status_rows']} seed statuses changed; no live fetch)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
