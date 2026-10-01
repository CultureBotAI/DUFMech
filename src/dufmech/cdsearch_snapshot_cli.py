"""Command-line interface for frozen NCBI Batch CD-Search snapshots."""

from __future__ import annotations

import argparse
import json
from collections.abc import Mapping
from datetime import date
from pathlib import Path

from dufmech.cdsearch import (
    DEFAULT_CDSEARCH_BATCH_SIZE,
    DEFAULT_CDSEARCH_DB,
    DEFAULT_CDSEARCH_MODE,
)
from dufmech.cdsearch_snapshot import (
    collect_cdsearch_snapshot_rows,
    write_cdsearch_snapshot,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Freeze UniProt accessions to NCBI Batch CD-Search snapshots."
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
        "--batch-size",
        type=int,
        default=DEFAULT_CDSEARCH_BATCH_SIZE,
        help=(
            "number of UniProt accessions per Batch CD-Search job "
            f"(default: {DEFAULT_CDSEARCH_BATCH_SIZE})"
        ),
    )
    parser.add_argument(
        "--db",
        default=DEFAULT_CDSEARCH_DB,
        help=f"Batch CD-Search database selector (default: {DEFAULT_CDSEARCH_DB})",
    )
    parser.add_argument(
        "--mode",
        default=DEFAULT_CDSEARCH_MODE,
        help=f"Batch CD-Search hit mode (default: {DEFAULT_CDSEARCH_MODE})",
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
    if args.batch_size < 1:
        parser.error("--batch-size must be positive")
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

    rows = collect_cdsearch_snapshot_rows(
        accessions,
        db=args.db,
        mode=args.mode,
        batch_size=args.batch_size,
    )
    manifest = write_cdsearch_snapshot(
        rows,
        args.out_dir,
        snapshot_date=args.snapshot_date,
        seed_snapshot_id=seed_snapshot_id,
        db=args.db,
        mode=args.mode,
        batch_size=args.batch_size,
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
