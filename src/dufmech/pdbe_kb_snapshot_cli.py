"""Command-line interface for frozen PDBe-KB annotation snapshots."""

from __future__ import annotations

import argparse
import json
from collections.abc import Mapping
from datetime import date
from pathlib import Path

from dufmech.pdbe_kb import PDBE_KB_ENDPOINTS, PdbeKbSeed
from dufmech.pdbe_kb_snapshot import (
    collect_pdbe_kb_snapshot_rows,
    write_pdbe_kb_snapshot,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Freeze a UniProt/RCSB PDB to PDBe-KB annotation snapshot."
    )
    parser.add_argument(
        "--input-json",
        type=Path,
        help="read PDB entities from an RCSB snapshot JSON file",
    )
    parser.add_argument(
        "--pdb-entity",
        action="append",
        default=[],
        metavar="UNIPROT:PDB:ENTITY",
        help="fetch one UniProt/PDB/entity tuple; can be supplied more than once",
    )
    parser.add_argument(
        "--endpoint",
        action="append",
        choices=PDBE_KB_ENDPOINTS,
        help="PDBe-KB entity endpoint to fetch; can be supplied more than once",
    )
    parser.add_argument(
        "--limit-structures",
        type=int,
        help="stop after the first N PDB entities",
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

    if args.limit_structures is not None and args.limit_structures < 1:
        parser.error("--limit-structures must be positive")
    if args.snapshot_date:
        try:
            date.fromisoformat(args.snapshot_date)
        except ValueError:
            parser.error("--snapshot-date must be an ISO date")
    if not args.input_json and not args.pdb_entity:
        parser.error("provide --input-json or at least one --pdb-entity")

    try:
        seeds = [parse_pdb_entity_seed(value) for value in args.pdb_entity]
    except argparse.ArgumentTypeError as exc:
        parser.error(str(exc))
    seed_snapshot_id = ""
    if args.input_json:
        payload = json.loads(args.input_json.read_text(encoding="utf-8"))
        seeds.extend(load_rcsb_pdb_seeds(payload))
        seed_snapshot_id = args.input_json.stem
    if args.limit_structures is not None:
        seeds = seeds[: args.limit_structures]

    endpoints = tuple(args.endpoint or PDBE_KB_ENDPOINTS)
    rows = collect_pdbe_kb_snapshot_rows(seeds, endpoints=endpoints)
    manifest = write_pdbe_kb_snapshot(
        rows,
        args.out_dir,
        snapshot_date=args.snapshot_date,
        seed_snapshot_id=seed_snapshot_id,
        endpoints=endpoints,
    )
    print(
        f"wrote {manifest['snapshot']['id']} "
        f"({manifest['rows']['total']} rows) to {args.out_dir}"
    )
    return 0


def parse_pdb_entity_seed(value: str) -> PdbeKbSeed:
    """Parse one ``UNIPROT:PDB:ENTITY`` seed value."""

    parts = value.split(":")
    if len(parts) != 3 or any(not part.strip() for part in parts):
        raise argparse.ArgumentTypeError(
            "PDB entity seeds must use UNIPROT:PDB:ENTITY"
        )
    return PdbeKbSeed(
        uniprot_accession=parts[0].strip(),
        pdb_id=parts[1].strip(),
        entity_id=parts[2].strip(),
    )


def load_rcsb_pdb_seeds(payload: object) -> list[PdbeKbSeed]:
    """Load ordered, unique PDB entities from an RCSB JSON payload."""

    if not isinstance(payload, list):
        raise TypeError("expected an RCSB PDB snapshot row list")

    seeds: list[PdbeKbSeed] = []
    seen: set[tuple[str, str, str]] = set()
    for row in payload:
        if not isinstance(row, Mapping):
            continue
        seed = PdbeKbSeed(
            uniprot_accession=_string(row.get("uniprot_accession")),
            pdb_id=_string(row.get("pdb_id")),
            entity_id=_string(row.get("entity_id")),
        )
        if (
            not seed.uniprot_accession
            or not seed.pdb_id
            or not seed.entity_id
            or seed.key in seen
        ):
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
