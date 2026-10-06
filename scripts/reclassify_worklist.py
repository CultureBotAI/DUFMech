"""Reclassify a frozen worklist without fetching or changing its source metadata.

Dry-run by default. A new date and --apply are required to publish new local files;
an existing snapshot is never overwritten.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from dufmech.reclassify import prepare_reclassification
from dufmech.report import ReportError
from dufmech.snapshot import write_snapshot_artifacts


def reclassify(source: Path, out: Path, snapshot_date: str, *, apply: bool = False) -> dict:
    try:
        prepared = prepare_reclassification(source, snapshot_date=snapshot_date)
    except ReportError as exc:
        raise ValueError(str(exc)) from exc
    if any((out / name).exists() or (out / name).is_symlink() for name in prepared.artifacts):
        raise ValueError("Refusing to overwrite an existing snapshot")
    if apply:
        write_snapshot_artifacts(out, prepared.artifacts)
    return prepared.summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--out", type=Path, default=Path("data/worklists"))
    parser.add_argument("--snapshot-date", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    try:
        result = reclassify(args.source, args.out, args.snapshot_date, apply=args.apply)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"reclassification failed: {exc}\n")
    print(json.dumps({key: value for key, value in result.items() if key != "changes"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
