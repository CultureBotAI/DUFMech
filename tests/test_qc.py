from __future__ import annotations

import sys

import pytest

from dufmech.qc import QualityCommand, main, run_quality_commands


@pytest.mark.parametrize(("args", "code"), [(["--help"], 0), (["--unknown"], 2)])
def test_qc_arguments_do_not_run_commands(args, code, monkeypatch) -> None:
    def unexpected_run():
        pytest.fail("QC must not execute for help or invalid arguments")

    monkeypatch.setattr("dufmech.qc.run_quality_commands", unexpected_run)
    with pytest.raises(SystemExit) as exc:
        main(args)
    assert exc.value.code == code


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
