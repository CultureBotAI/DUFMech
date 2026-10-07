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
        "family records and schema",
        (sys.executable, "-m", "dufmech.records", "--check"),
        "Closed schemas, frozen identity/labels, evidence quotes and projections must agree.",
    ),
    QualityCommand(
        "offline research profile",
        (sys.executable, "-m", "dufmech.research", "check"),
        "Validate the shared planning profile; no provider availability or execution is claimed.",
    ),
    QualityCommand(
        "KGX and SSSOM exports",
        (sys.executable, "-m", "dufmech.exports", "--check"),
        "Verified native records must reproduce every committed export byte without writing.",
    ),
    QualityCommand(
        "isolated OAK ID/label correspondence",
        (sys.executable, "-m", "dufmech.id_labels", "--check"),
        "Require complete canonical Pfam matches in CLAW_ROOT's separate locked offline runtime.",
    ),
    QualityCommand(
        "source governance",
        (sys.executable, "-m", "dufmech.source_governance"),
        "The source catalogue, adoption queue and native writer inventory must remain valid.",
    ),
    QualityCommand(
        "retained review reports",
        (sys.executable, "-m", "dufmech.reviews", "check"),
        "Review artifacts retain timestamps, source hashes, scope and actual findings.",
    ),
    QualityCommand(
        "curation history",
        (sys.executable, "-m", "dufmech.history", "check"),
        "Append-only events must conform to the canonical history schema.",
    ),
    QualityCommand(
        "cross-Mech report",
        (sys.executable, "scripts/cross_mech_report.py", "--check"),
        "The committed cross-Mech report must match the frozen snapshot.",
    ),
    QualityCommand(
        "generated site",
        (sys.executable, "scripts/render_pages.py", "--check"),
        "The committed dashboard must not drift from frozen data.",
    ),
    QualityCommand(
        "site contract and budgets",
        (sys.executable, "-m", "dufmech.site_contract"),
        "Site links, full-corpus reachability, contrast tokens and byte limits are checked offline.",
    ),
    QualityCommand(
        "browser regression tests",
        ("npm", "run", "test:browser"),
        "Playwright verifies catalogue controls, static fallback, themes and responsive layout.",
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
