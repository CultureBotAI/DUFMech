from __future__ import annotations

import sys

from dufmech.qc import QualityCommand, run_quality_commands


def test_run_quality_commands_stops_at_first_failure(tmp_path, capsys) -> None:
    code = run_quality_commands(
        [
            QualityCommand(
                "ok",
                (sys.executable, "-c", "print('ok')"),
                "passes",
            ),
            QualityCommand(
                "bad",
                (sys.executable, "-c", "raise SystemExit(7)"),
                "fails",
            ),
            QualityCommand(
                "later",
                (sys.executable, "-c", "raise SystemExit(99)"),
                "should not run",
            ),
        ],
        cwd=tmp_path,
    )
    captured = capsys.readouterr()

    assert code == 7
    assert "=== qc: ok ===" in captured.out
    assert "=== qc: bad ===" in captured.out
    assert "=== qc: later ===" not in captured.out
    assert "qc stopped: bad failed with exit code 7" in captured.err
