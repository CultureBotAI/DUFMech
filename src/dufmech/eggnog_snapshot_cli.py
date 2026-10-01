"""Command-line interface for frozen eggNOG-mapper annotation snapshots."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from dufmech.eggnog_snapshot import (
    collect_eggnog_snapshot_rows,
    write_eggnog_snapshot,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Freeze an eggNOG-mapper annotations TSV snapshot."
    )
    parser.add_argument(
        "--annotations-tsv",
        type=Path,
        required=True,
        help="read standard eggNOG-mapper .emapper.annotations TSV rows",
    )
    parser.add_argument(
        "--seed-snapshot-id",
        default="",
        help="upstream snapshot identifier used to generate eggNOG inputs",
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

    if args.snapshot_date:
        try:
            date.fromisoformat(args.snapshot_date)
        except ValueError:
            parser.error("--snapshot-date must be an ISO date")

    rows = collect_eggnog_snapshot_rows(args.annotations_tsv)
    manifest = write_eggnog_snapshot(
        rows,
        args.out_dir,
        snapshot_date=args.snapshot_date,
        seed_snapshot_id=args.seed_snapshot_id,
        annotations_path=args.annotations_tsv,
    )
    print(
        f"wrote {manifest['snapshot']['id']} "
        f"({manifest['rows']['total']} rows) to {args.out_dir}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
