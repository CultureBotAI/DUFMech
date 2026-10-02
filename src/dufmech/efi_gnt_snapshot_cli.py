"""Command-line interface for frozen EFI-GNT Pfam-neighbor snapshots."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from dufmech.efi_gnt_snapshot import (
    collect_efi_gnt_snapshot_rows,
    write_efi_gnt_snapshot,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Freeze an EFI-GNT Pfam Neighbor Mapping Table TSV snapshot."
    )
    parser.add_argument(
        "--pfam-neighbors-tsv",
        type=Path,
        required=True,
        help="read a saved EFI-GNT Pfam Neighbor Mapping Table TSV",
    )
    parser.add_argument(
        "--seed-snapshot-id",
        default="",
        help="upstream snapshot identifier used to generate EFI-GNT inputs",
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

    rows = collect_efi_gnt_snapshot_rows(args.pfam_neighbors_tsv)
    manifest = write_efi_gnt_snapshot(
        rows,
        args.out_dir,
        snapshot_date=args.snapshot_date,
        seed_snapshot_id=args.seed_snapshot_id,
        pfam_neighbors_path=args.pfam_neighbors_tsv,
    )
    print(
        f"wrote {manifest['snapshot']['id']} "
        f"({manifest['rows']['total']} rows) to {args.out_dir}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
