"""Command-line interface for Pfam-to-UniProtKB member expansion."""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Mapping
from pathlib import Path

from dufmech.protein_members import (
    InterProPfamProteinClient,
    collect_family_members,
    render_members_json,
    render_members_tsv,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Expand Pfam worklist rows to UniProtKB protein members."
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
        "--limit-members-per-family",
        type=int,
        help="stop after the first N normalized members for each Pfam family",
    )
    parser.add_argument(
        "--page-size",
        type=int,
        default=200,
        help="InterPro page size, max 200 (default: 200)",
    )
    parser.add_argument(
        "--format",
        choices=("tsv", "json"),
        default="tsv",
        help="output format (default: tsv)",
    )
    parser.add_argument("--out", type=Path, help="write here instead of stdout")
    args = parser.parse_args(argv)

    if args.page_size < 1 or args.page_size > 200:
        parser.error("--page-size must be between 1 and 200")
    if args.limit_families is not None and args.limit_families < 1:
        parser.error("--limit-families must be positive")
    if args.limit_members_per_family is not None and args.limit_members_per_family < 1:
        parser.error("--limit-members-per-family must be positive")
    if not args.input_json and not args.pfam_id:
        parser.error("provide --input-json or at least one --pfam-id")

    pfam_ids = list(args.pfam_id)
    if args.input_json:
        payload = json.loads(args.input_json.read_text(encoding="utf-8"))
        pfam_ids.extend(load_seed_pfam_ids(payload))
    if args.limit_families is not None:
        pfam_ids = pfam_ids[: args.limit_families]

    rows = collect_family_members(
        pfam_ids,
        InterProPfamProteinClient(),
        page_size=args.page_size,
        limit_members_per_family=args.limit_members_per_family,
    )
    output = (
        render_members_json(rows) if args.format == "json" else render_members_tsv(rows)
    )

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(output + "\n", encoding="utf-8")
        print(f"wrote {args.out} ({len(rows)} rows)", file=sys.stderr)
    else:
        print(output)
    return 0


def load_seed_pfam_ids(payload: object) -> list[str]:
    """Load ordered, unique Pfam accessions from a frozen worklist JSON payload."""

    if not isinstance(payload, list):
        raise TypeError("expected a frozen InterPro/Pfam worklist row list")

    pfam_ids: list[str] = []
    seen: set[str] = set()
    for row in payload:
        if not isinstance(row, Mapping):
            continue
        pfam_id = _string(row.get("pfam_id"))
        if pfam_id and pfam_id not in seen:
            seen.add(pfam_id)
            pfam_ids.append(pfam_id)
    return pfam_ids


def _string(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""


if __name__ == "__main__":
    raise SystemExit(main())
