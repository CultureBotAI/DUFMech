"""Command-line interface for frozen STRING interaction snapshots."""

from __future__ import annotations

import argparse
import json
from collections.abc import Mapping
from datetime import date
from pathlib import Path

from dufmech.stringdb import StringDbSeed
from dufmech.stringdb_snapshot import (
    collect_stringdb_snapshot_rows,
    write_stringdb_snapshot,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Freeze UniProt accessions to STRING interaction snapshots."
    )
    parser.add_argument(
        "--input-json",
        type=Path,
        help="read UniProt accessions and taxa from a member snapshot JSON file",
    )
    parser.add_argument(
        "--uniprot-taxon",
        action="append",
        default=[],
        metavar="UNIPROT:TAXON",
        help="fetch one UniProt/taxon tuple; can be supplied more than once",
    )
    parser.add_argument(
        "--limit-seeds",
        type=int,
        help="stop after the first N UniProt/taxon pairs",
    )
    parser.add_argument(
        "--limit-partners-per-protein",
        type=int,
        default=10,
        help="STRING interaction partner limit per protein (default: 10)",
    )
    parser.add_argument(
        "--required-score",
        type=int,
        default=400,
        help="STRING required score threshold from 0 to 1000 (default: 400)",
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

    if args.limit_seeds is not None and args.limit_seeds < 1:
        parser.error("--limit-seeds must be positive")
    if args.limit_partners_per_protein < 1:
        parser.error("--limit-partners-per-protein must be positive")
    if args.required_score < 0 or args.required_score > 1000:
        parser.error("--required-score must be between 0 and 1000")
    if args.snapshot_date:
        try:
            date.fromisoformat(args.snapshot_date)
        except ValueError:
            parser.error("--snapshot-date must be an ISO date")
    if not args.input_json and not args.uniprot_taxon:
        parser.error("provide --input-json or at least one --uniprot-taxon")

    try:
        seeds = [parse_uniprot_taxon_seed(value) for value in args.uniprot_taxon]
    except argparse.ArgumentTypeError as exc:
        parser.error(str(exc))

    seed_snapshot_id = ""
    if args.input_json:
        payload = json.loads(args.input_json.read_text(encoding="utf-8"))
        seeds.extend(load_member_stringdb_seeds(payload))
        seed_snapshot_id = args.input_json.stem
    if args.limit_seeds is not None:
        seeds = seeds[: args.limit_seeds]

    rows = collect_stringdb_snapshot_rows(
        seeds,
        limit_partners_per_protein=args.limit_partners_per_protein,
        required_score=args.required_score,
    )
    manifest = write_stringdb_snapshot(
        rows,
        args.out_dir,
        snapshot_date=args.snapshot_date,
        seed_snapshot_id=seed_snapshot_id,
        limit_partners_per_protein=args.limit_partners_per_protein,
        required_score=args.required_score,
    )
    print(
        f"wrote {manifest['snapshot']['id']} "
        f"({manifest['rows']['total']} rows) to {args.out_dir}"
    )
    return 0


def parse_uniprot_taxon_seed(value: str) -> StringDbSeed:
    """Parse one ``UNIPROT:TAXON`` seed value."""

    parts = value.split(":")
    if len(parts) != 2 or any(not part.strip() for part in parts):
        raise argparse.ArgumentTypeError(
            "STRING seeds must use UNIPROT:TAXON"
        )
    return StringDbSeed(
        uniprot_accession=parts[0].strip(),
        taxon_id=parts[1].strip(),
    )


def load_member_stringdb_seeds(payload: object) -> list[StringDbSeed]:
    """Load ordered, unique UniProt/taxon seeds from a member JSON payload."""

    if not isinstance(payload, list):
        raise TypeError("expected a member snapshot row list")

    seeds: list[StringDbSeed] = []
    seen: set[tuple[str, str]] = set()
    for row in payload:
        if not isinstance(row, Mapping):
            continue
        seed = StringDbSeed(
            uniprot_accession=_string(row.get("uniprot_accession")),
            taxon_id=_string(row.get("uniprot_taxon_id"))
            or _string(row.get("taxon_id")),
        )
        if not seed.uniprot_accession or not seed.taxon_id or seed.key in seen:
            continue
        seen.add(seed.key)
        seeds.append(seed)
    return seeds


def _string(value: object) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, int):
        return str(value)
    return ""


if __name__ == "__main__":
    raise SystemExit(main())
