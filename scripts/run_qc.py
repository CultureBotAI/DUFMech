"""Run the DUFMech quality gate."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def main(argv: list[str] | None = None) -> int:
    sys.path.insert(0, str(REPO_ROOT / "src"))
    from dufmech.qc import main as run

    return run(argv)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
