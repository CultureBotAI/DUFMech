"""Check or refresh README.md's generated DUFMech corpus block."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def main(argv: list[str] | None = None) -> int:
    sys.path.insert(0, str(REPO_ROOT / "src"))

    from dufmech.docs import check_or_write_readme, render_block_from_paths

    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="refresh README.md")
    mode.add_argument(
        "--check",
        action="store_true",
        help="fail if README.md is stale",
    )
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    parser.add_argument("--worklists-dir", type=Path, default=Path("data/worklists"))
    parser.add_argument("--worklist-json", type=Path)
    parser.add_argument("--score-json", type=Path)
    args = parser.parse_args(argv)

    block = render_block_from_paths(
        worklists_dir=args.worklists_dir,
        worklist_json=args.worklist_json,
        score_json=args.score_json,
    )
    if check_or_write_readme(args.readme, block=block, write=args.write):
        print("README.md corpus block refreshed" if args.write else "README.md corpus block is current")
        return 0

    print("README.md corpus block is stale; run `just docs-stats`", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
