"""Command-line interface for frozen RCSB PDB evidence snapshots."""

from __future__ import annotations

import argparse
import json
from collections.abc import Mapping
from datetime import date
from pathlib import Path

from dufmech.rcsb_snapshot import collect_rcsb_snapshot_rows, write_rcsb_snapshot


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Freeze a UniProt accession to RCSB PDB evidence snapshot."
    )
    parser.add_argument(
        "--input-json",
        type=Path,
        help="read UniProt accessions from a member snapshot JSON file",
    )
    parser.add_argument(
        "--uniprot-accession",
        action="append",
        default=[],
        help="fetch one UniProt accession; can be supplied more than once",
    )
    parser.add_argument(
        "--limit-accessions",
        type=int,
        help="stop after the first N UniProt accessions",
    )
    parser.add_argument(
        "--limit-entities-per-accession",
        type=int,
        default=50,
        help="RCSB search result limit per UniProt accession (default: 50)",
    )
    parser.add_argument(
        "--snapshot-date",
        help="ISO snapshot date for generated filenames (default: today in UTC)",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("data/worklists"),
        help="directory for JSON, TSV, and manifest files (default: data/worklists)",
    )
    args = parser.parse_args(argv)

    if args.limit_accessions is not None and args.limit_accessions < 1:
        parser.error("--limit-accessions must be positive")
    if args.limit_entities_per_accession < 1:
        parser.error("--limit-entities-per-accession must be positive")
    if args.snapshot_date:
        try:
            date.fromisoformat(args.snapshot_date)
        except ValueError:
            parser.error("--snapshot-date must be an ISO date")
    if not args.input_json and not args.uniprot_accession:
        parser.error("provide --input-json or at least one --uniprot-accession")

    accessions = list(args.uniprot_accession)
    seed_snapshot_id = ""
    if args.input_json:
        payload = json.loads(args.input_json.read_text(encoding="utf-8"))
        accessions.extend(load_member_uniprot_accessions(payload))
        seed_snapshot_id = args.input_json.stem
    if args.limit_accessions is not None:
        accessions = accessions[: args.limit_accessions]

    rows = collect_rcsb_snapshot_rows(
        accessions,
        limit_entities_per_accession=args.limit_entities_per_accession,
    )
    manifest = write_rcsb_snapshot(
        rows,
        args.out_dir,
        snapshot_date=args.snapshot_date,
        seed_snapshot_id=seed_snapshot_id,
        limit_entities_per_accession=args.limit_entities_per_accession,
    )
    print(
        f"wrote {manifest['snapshot']['id']} "
        f"({manifest['rows']['total']} rows) to {args.out_dir}"
    )
    return 0


def load_member_uniprot_accessions(payload: object) -> list[str]:
    """Load ordered, unique UniProt accessions from a member JSON payload."""

    if not isinstance(payload, list):
        raise TypeError("expected a member snapshot row list")

    accessions: list[str] = []
    seen: set[str] = set()
    for row in payload:
        if not isinstance(row, Mapping):
            continue
        accession = _string(row.get("uniprot_accession"))
        if accession and accession not in seen:
            seen.add(accession)
            accessions.append(accession)
    return accessions


def _string(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""


if __name__ == "__main__":
    raise SystemExit(main())
