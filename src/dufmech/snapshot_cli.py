"""Command-line interface for versioned DUFMech snapshots."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from dufmech.snapshot import write_worklist_snapshot
from dufmech.worklist import (
    InterProPfamClient,
    collect_worklist,
    load_interpro_fixture,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Freeze an InterPro/Pfam DUF-family snapshot."
    )
    parser.add_argument(
        "--search",
        default="DUF",
        help="InterPro Pfam search term (default: DUF)",
    )
    parser.add_argument(
        "--page-size",
        type=int,
        default=200,
        help="InterPro page size, max 200 (default: 200)",
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
    parser.add_argument(
        "--include-false-positives",
        action="store_true",
        help="include Pfam search hits whose metadata does not look DUF-like",
    )
    parser.add_argument(
        "--input-json",
        type=Path,
        help="read a saved InterPro page or result list instead of fetching live",
    )
    args = parser.parse_args(argv)

    if args.page_size < 1 or args.page_size > 200:
        parser.error("--page-size must be between 1 and 200")
    if args.snapshot_date:
        try:
            date.fromisoformat(args.snapshot_date)
        except ValueError:
            parser.error("--snapshot-date must be an ISO date")

    if args.input_json:
        payload = json.loads(args.input_json.read_text(encoding="utf-8"))
        entries = load_interpro_fixture(payload)
    else:
        entries = InterProPfamClient().iter_entries(
            search=args.search,
            page_size=args.page_size,
        )

    rows = collect_worklist(
        entries,
        include_false_positives=args.include_false_positives,
    )
    try:
        manifest = write_worklist_snapshot(
            rows,
            args.out_dir,
            snapshot_date=args.snapshot_date,
            search=args.search,
            page_size=args.page_size,
            include_false_positives=args.include_false_positives,
        )
    except (OSError, ValueError) as exc:
        parser.exit(1, f"worklist freeze failed: {exc}\n")
    print(
        f"wrote {manifest['snapshot']['id']} "
        f"({manifest['rows']['total']} rows) to {args.out_dir}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
