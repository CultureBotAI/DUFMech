"""Verify frozen DUFMech snapshot manifest checksums."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def main(argv: list[str] | None = None) -> int:
    sys.path.insert(0, str(REPO_ROOT / "src"))

    from dufmech.provenance import (
        check_worklist_manifests,
        worklist_manifest_paths,
    )

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--worklists-dir", type=Path, default=Path("data/worklists"))
    parser.add_argument("--protein-examples-dir", type=Path, default=Path("data/protein_examples"))
    parser.add_argument(
        "--cross-mech-dir",
        type=Path,
        default=Path("data/cross_mech"),
        help="checked when present; cross-Mech snapshots are optional",
    )
    args = parser.parse_args(argv)

    directories = [args.worklists_dir]
    if args.cross_mech_dir.exists():
        directories.append(args.cross_mech_dir)
    if args.protein_examples_dir.exists():
        directories.append(args.protein_examples_dir)
    issues = [issue for directory in directories for issue in check_worklist_manifests(directory)]
    if issues:
        print(
            "DUFMech provenance check failed:\n  "
            + "\n  ".join(issue.render() for issue in issues),
            file=sys.stderr,
        )
        return 1

    from dufmech.protein_examples import load_snapshot
    from dufmech.report import load_json_rows, verified_manifest

    for path in args.protein_examples_dir.glob("duf-protein-examples-*.json"):
        if path.name.endswith(".manifest.json"):
            continue
        manifest = verified_manifest(path)
        worklist_id = manifest["snapshot"]["input_snapshot_ids"]["worklist"]
        if Path(worklist_id).name != worklist_id:
            raise ValueError("protein-example worklist ID must be a filename stem")
        worklist = args.worklists_dir / f"{worklist_id}.json"
        verified_manifest(worklist)
        load_snapshot(path, list(load_json_rows(worklist)), worklist_id)

    count = sum(len(worklist_manifest_paths(directory)) for directory in directories)
    print(f"validated {count} DUFMech snapshot manifest(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
