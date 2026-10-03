"""Print a DUFMech corpus report from frozen snapshots."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def main(argv: list[str] | None = None) -> int:
    sys.path.insert(0, str(REPO_ROOT / "src"))

    from dufmech.report import (
        WORKLIST_STEM,
        build_report,
        latest_snapshot_path,
        load_json_rows,
        render_report_text,
    )
    from dufmech.scoring_snapshot import SCORE_STEM

    parser = argparse.ArgumentParser(
        description="Print a DUFMech corpus report from frozen snapshots."
    )
    parser.add_argument("--worklists-dir", type=Path, default=Path("data/worklists"))
    parser.add_argument("--worklist-json", type=Path)
    parser.add_argument("--score-json", type=Path)
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args(argv)

    worklist_path = args.worklist_json or latest_snapshot_path(
        args.worklists_dir, WORKLIST_STEM
    )
    score_path = args.score_json or latest_snapshot_path(
        args.worklists_dir, SCORE_STEM, required=False
    )
    assert worklist_path is not None

    input_ids = {"worklist": worklist_path.stem}
    worklist_rows = load_json_rows(worklist_path)
    score_rows = []
    if score_path is not None:
        input_ids["scores"] = score_path.stem
        score_rows = load_json_rows(score_path)

    report = build_report(worklist_rows, score_rows, top_n=args.top)
    print(render_report_text(report, input_ids=input_ids))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
