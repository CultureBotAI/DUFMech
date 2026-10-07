"""Command-line interface for frozen DUF characterization scores."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Mapping
from datetime import date
from pathlib import Path
from typing import Any

from dufmech.score_inputs import ScoreInputError, load_score_input
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
        "--allow-ad-hoc-inputs",
        action="store_true",
        help="allow inputs without companion manifests; never bypass an invalid existing manifest",
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

    paths = {"worklist": args.worklist_json}
    if args.member_json:
        paths["members"] = args.member_json
    for flag in EVIDENCE_FLAGS:
        path = getattr(args, f"{flag.name}_json")
        if path:
            paths[flag.name] = path
    try:
        inputs = {role: load_score_input(path, role, allow_ad_hoc=args.allow_ad_hoc_inputs)
                  for role, path in paths.items()}
        evidence = EvidenceBundle(**{flag.name: inputs[flag.name].rows for flag in EVIDENCE_FLAGS
                                     if flag.name in inputs})
        rows = score_families(
            inputs["worklist"].rows,
            member_rows=inputs["members"].rows if "members" in inputs else (), evidence=evidence,
        )
        manifest = write_score_snapshot(
            rows, args.out_dir, snapshot_date=args.snapshot_date,
            input_snapshot_ids={role: value.provenance["snapshot_id"] for role, value in inputs.items()},
            input_provenance={role: value.provenance for role, value in inputs.items()},
        )
    except (OSError, ScoreInputError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
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
    EvidenceFlag("efi_gnt", "efi-gnt", "EFI-GNT"),
    EvidenceFlag("eggnog", "eggnog", "eggNOG-mapper"),
    EvidenceFlag("jgi_img", "jgi-img", "JGI IMG"),
    EvidenceFlag("mgnify", "mgnify", "MGnify Proteins"),
    EvidenceFlag("ncbifam", "ncbifam", "NCBIFAM"),
    EvidenceFlag("pdbe_kb", "pdbe-kb", "PDBe-KB"),
    EvidenceFlag("quickgo", "quickgo", "QuickGO"),
    EvidenceFlag("rcsb", "rcsb", "RCSB PDB"),
    EvidenceFlag("rhea", "rhea", "Rhea"),
    EvidenceFlag("stringdb", "string", "STRING"),
    EvidenceFlag("threedbeacons", "threedbeacons", "3D-Beacons"),
)


def load_json_rows(
    path: Path, *, role: str = "worklist", allow_ad_hoc: bool = False,
) -> list[Mapping[str, Any]]:
    """Compatibility entrypoint with the same strict policy as the scoring CLI."""
    return list(load_score_input(path, role, allow_ad_hoc=allow_ad_hoc).rows)


if __name__ == "__main__":
    raise SystemExit(main())
