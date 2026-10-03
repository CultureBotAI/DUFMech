"""Run the DUFMech quality gate."""

from __future__ import annotations

import argparse
import subprocess
import sys
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class QualityCommand:
    """One named quality gate command."""

    name: str
    command: tuple[str, ...]
    rationale: str


COMMANDS = (
    QualityCommand(
        "lint",
        (sys.executable, "-m", "ruff", "check", "src", "scripts", "tests"),
        "Fail fast on syntax, import, and style defects.",
    ),
    QualityCommand(
        "tests",
        (sys.executable, "-m", "pytest"),
        "Exercise parser, snapshot, scoring, report, and rendering invariants.",
    ),
    QualityCommand(
        "documentation",
        (sys.executable, "scripts/check_docs.py", "--check"),
        "The README current-corpus block must match frozen snapshots.",
    ),
    QualityCommand(
        "provenance",
        (sys.executable, "scripts/check_provenance.py"),
        "Every frozen snapshot must match its manifest checksums.",
    ),
    QualityCommand(
        "corpus report",
        (sys.executable, "scripts/duf_puf_report.py"),
        "Exercise cross-snapshot DUF/PUF summary metrics.",
    ),
    QualityCommand(
        "generated site",
        (sys.executable, "scripts/render_pages.py", "--check"),
        "The committed dashboard must not drift from frozen data.",
    ),
)


def run_quality_commands(
    commands: Iterable[QualityCommand] = COMMANDS,
    *,
    cwd: Path = REPO_ROOT,
) -> int:
    """Run each quality command in order, stopping at the first failure."""

    for item in commands:
        print(f"\n=== qc: {item.name} ===", flush=True)
        print(f"why: {item.rationale}", flush=True)
        completed = subprocess.run(item.command, cwd=cwd, check=False)
        if completed.returncode:
            print(
                f"qc stopped: {item.name} failed with exit code {completed.returncode}",
                file=sys.stderr,
            )
            return completed.returncode
    print("\nAll DUFMech quality gates passed.")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """Run DUFMech QC."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)
    return run_quality_commands()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
