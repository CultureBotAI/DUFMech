"""Command-line interface for frozen MGnify Proteins snapshots."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from dufmech.member_cli import load_seed_pfam_ids
from dufmech.mgnify_snapshot import (
    collect_mgnify_snapshot_rows,
    write_mgnify_snapshot,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Freeze a Pfam-to-MGnify Proteins representative snapshot."
    )
    parser.add_argument(
        "--input-json",
        type=Path,
        help="read Pfam IDs from a frozen InterPro/Pfam worklist JSON file",
    )
    parser.add_argument(
        "--pfam-id",
        action="append",
        default=[],
        help="fetch one Pfam accession; can be supplied more than once",
    )
    parser.add_argument(
        "--limit-families",
        type=int,
        help="stop after the first N Pfam families from the seed list",
    )
    parser.add_argument(
        "--limit-proteins-per-family",
        type=int,
        default=50,
        help="MGnify search limit per Pfam family, max 1000 (default: 50)",
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

    if args.limit_families is not None and args.limit_families < 1:
        parser.error("--limit-families must be positive")
    if args.limit_proteins_per_family < 1 or args.limit_proteins_per_family > 1000:
        parser.error("--limit-proteins-per-family must be between 1 and 1000")
    if args.snapshot_date:
        try:
            date.fromisoformat(args.snapshot_date)
        except ValueError:
            parser.error("--snapshot-date must be an ISO date")
    if not args.input_json and not args.pfam_id:
        parser.error("provide --input-json or at least one --pfam-id")

    pfam_ids = list(args.pfam_id)
    seed_snapshot_id = ""
    if args.input_json:
        payload = json.loads(args.input_json.read_text(encoding="utf-8"))
        pfam_ids.extend(load_seed_pfam_ids(payload))
        seed_snapshot_id = args.input_json.stem
    if args.limit_families is not None:
        pfam_ids = pfam_ids[: args.limit_families]

    rows = collect_mgnify_snapshot_rows(
        pfam_ids,
        limit_proteins_per_family=args.limit_proteins_per_family,
    )
    manifest = write_mgnify_snapshot(
        rows,
        args.out_dir,
        snapshot_date=args.snapshot_date,
        seed_snapshot_id=seed_snapshot_id,
        limit_proteins_per_family=args.limit_proteins_per_family,
    )
    print(
        f"wrote {manifest['snapshot']['id']} "
        f"({manifest['rows']['total']} rows) to {args.out_dir}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
