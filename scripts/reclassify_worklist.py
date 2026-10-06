"""Reclassify a frozen worklist without fetching or changing its source metadata.

Dry-run by default. A new date and --apply are required to publish new local files;
an existing snapshot is never overwritten.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from dataclasses import fields
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from dufmech.provenance import check_manifest
from dufmech.snapshot import write_worklist_snapshot
from dufmech.worklist import DufFamilyRow, _candidate_reasons, _unknown_status


def reclassify(source: Path, out: Path, snapshot_date: str, *, apply: bool = False) -> dict:
    source_manifest = source.with_suffix(".manifest.json")
    errors = check_manifest(source_manifest)
    if errors:
        raise ValueError("; ".join(error.render() for error in errors))
    original = json.loads(source_manifest.read_text())
    if date.fromisoformat(snapshot_date) <= date.fromisoformat(original["snapshot"]["date"]):
        raise ValueError("Reclassification needs a newer snapshot date; preserve the frozen source")
    snapshot_id = "interpro-pfam-duf-" + snapshot_date
    if any((out / (snapshot_id + suffix)).exists() for suffix in (".json", ".tsv", ".manifest.json")):
        raise ValueError("Refusing to overwrite an existing snapshot")
    source_rows = json.loads(source.read_text())
    rows, changes = [], []
    names = {field.name for field in fields(DufFamilyRow)}
    for entry in source_rows:
        values = {key: entry[key] for key in names}
        values["candidate_reasons"] = _candidate_reasons(
            entry["short_name"], entry["name"], entry["description"]
        )
        values["unknown_status"] = _unknown_status(values["candidate_reasons"])
        row = DufFamilyRow(**values)
        if row.source_url != entry["source_url"]:
            raise ValueError("Unexpected source URL; reclassification must preserve metadata")
        rows.append(row)
        if (row.unknown_status != entry["unknown_status"] or
                list(row.candidate_reasons) != entry["candidate_reasons"]):
            changes.append({"pfam_id": row.pfam_id, "before": entry["unknown_status"],
                            "after": row.unknown_status,
                            "before_reasons": entry["candidate_reasons"],
                            "after_reasons": list(row.candidate_reasons)})
    summary = {
        "source_snapshot": original["snapshot"]["id"],
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "policy": "Recognize explicit unknown-function names and family/families descriptions; "
                  "seed status is a metadata classification, not experimental evidence.",
        "rows": len(rows),
        "changed_statuses": sum(x["before"] != x["after"] for x in changes),
        "by_unknown_status": dict(sorted(Counter(row.unknown_status for row in rows).items())),
        "changes": changes,
    }
    if apply:
        manifest = write_worklist_snapshot(rows, out, snapshot_date=snapshot_date)
        manifest["snapshot"]["input_snapshot_ids"] = {"worklist": original["snapshot"]["id"]}
        manifest["source"] = {
            **original["source"],
            "name": "Reclassification of frozen InterPro Pfam API metadata",
            "original_generated_at": original["snapshot"]["generated_at"],
            "note": "No new API retrieval; all names, descriptions, identifiers and counters "
                    "are copied unchanged from the source snapshot.",
        }
        manifest["reclassification"] = summary
        (out / (snapshot_id + ".manifest.json")).write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n"
        )
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--out", type=Path, default=Path("data/worklists"))
    parser.add_argument("--snapshot-date", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    result = reclassify(args.source, args.out, args.snapshot_date, apply=args.apply)
    print(json.dumps({key: value for key, value in result.items() if key != "changes"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
