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
    args = parser.parse_args(argv)

    issues = check_worklist_manifests(args.worklists_dir)
    if issues:
        print(
            "DUFMech provenance check failed:\n  "
            + "\n  ".join(issue.render() for issue in issues),
            file=sys.stderr,
        )
        return 1

    count = len(worklist_manifest_paths(args.worklists_dir))
    print(f"validated {count} DUFMech worklist manifest(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
