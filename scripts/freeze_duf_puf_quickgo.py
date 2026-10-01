"""Freeze a UniProt / QuickGO molecular-function snapshot."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def main(argv: list[str] | None = None) -> int:
    sys.path.insert(0, str(REPO_ROOT / "src"))
    from dufmech.quickgo_snapshot_cli import main as run

    return run(argv)


if __name__ == "__main__":
    raise SystemExit(main())
