"""Command-line interface for frozen DUF characterization scores."""

from __future__ import annotations

import argparse
import json
from collections.abc import Mapping
from datetime import date
from pathlib import Path
from typing import Any

from dufmech.scoring import EvidenceBundle, score_families
from dufmech.scoring_snapshot import write_score_snapshot


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Score frozen DUF/Pfam families with evidence snapshots."
    )
    parser.add_argument(
        "--worklist-json",
        type=Path,
        required=True,
        help="read frozen InterPro/Pfam worklist JSON rows",
    )
    parser.add_argument(
        "--member-json",
        type=Path,
        help="read frozen Pfam member / UniRef JSON rows",
    )
    for flag in EVIDENCE_FLAGS:
        parser.add_argument(
            f"--{flag.cli_name}-json",
            dest=f"{flag.name}_json",
            type=Path,
            help=f"read frozen {flag.label} JSON rows",
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

    worklist_rows = load_json_rows(args.worklist_json)
    member_rows = load_json_rows(args.member_json) if args.member_json else []
    evidence = EvidenceBundle(
        **{
            flag.name: tuple(load_json_rows(getattr(args, f"{flag.name}_json")))
            for flag in EVIDENCE_FLAGS
            if getattr(args, f"{flag.name}_json")
        }
    )
    rows = score_families(worklist_rows, member_rows=member_rows, evidence=evidence)

    input_snapshot_ids = {"worklist": args.worklist_json.stem}
    if args.member_json:
        input_snapshot_ids["members"] = args.member_json.stem
    for flag in EVIDENCE_FLAGS:
        path = getattr(args, f"{flag.name}_json")
        if path:
            input_snapshot_ids[flag.name] = path.stem

    manifest = write_score_snapshot(
        rows,
        args.out_dir,
        snapshot_date=args.snapshot_date,
        input_snapshot_ids=input_snapshot_ids,
    )
    print(
        f"wrote {manifest['snapshot']['id']} "
        f"({manifest['rows']['total']} rows) to {args.out_dir}"
    )
    return 0


class EvidenceFlag:
    def __init__(self, name: str, cli_name: str, label: str) -> None:
        self.name = name
        self.cli_name = cli_name
        self.label = label


EVIDENCE_FLAGS = (
    EvidenceFlag("alphafold", "alphafold", "AlphaFold DB"),
    EvidenceFlag("cath", "cath", "CATH-Gene3D"),
    EvidenceFlag("cdsearch", "cdsearch", "NCBI Batch CD-Search"),
    EvidenceFlag("eggnog", "eggnog", "eggNOG-mapper"),
    EvidenceFlag("mgnify", "mgnify", "MGnify Proteins"),
    EvidenceFlag("pdbe_kb", "pdbe-kb", "PDBe-KB"),
    EvidenceFlag("quickgo", "quickgo", "QuickGO"),
    EvidenceFlag("rcsb", "rcsb", "RCSB PDB"),
    EvidenceFlag("rhea", "rhea", "Rhea"),
    EvidenceFlag("stringdb", "string", "STRING"),
    EvidenceFlag("threedbeacons", "threedbeacons", "3D-Beacons"),
)


def load_json_rows(path: Path) -> list[Mapping[str, Any]]:
    """Load one frozen JSON row list."""

    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise TypeError(f"expected a JSON row list in {path}")
    return [row for row in payload if isinstance(row, Mapping)]


if __name__ == "__main__":
    raise SystemExit(main())
