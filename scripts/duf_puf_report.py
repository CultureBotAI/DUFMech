"""Print a DUFMech corpus report from frozen snapshots."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def main(argv: list[str] | None = None) -> int:
    sys.path.insert(0, str(REPO_ROOT / "src"))

    from dufmech.report import (
        build_report,
        load_latest_rows,
        render_report_text,
    )

    parser = argparse.ArgumentParser(
        description="Print a DUFMech corpus report from frozen snapshots."
    )
    parser.add_argument("--worklists-dir", type=Path, default=Path("data/worklists"))
    parser.add_argument("--worklist-json", type=Path)
    parser.add_argument("--score-json", type=Path)
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args(argv)

    if args.top < 0:
        parser.error("--top must be non-negative")
    worklist_rows, score_rows, input_ids = load_latest_rows(
        args.worklists_dir, worklist_json=args.worklist_json, score_json=args.score_json
    )

    report = build_report(worklist_rows, score_rows, top_n=args.top)
    print(render_report_text(report, input_ids=input_ids))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
