from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

import pytest
import yaml

from dufmech import exports, source_governance
from dufmech.qc import COMMANDS, QualityCommand, main, run_quality_commands
from tests.test_exports import inventory, make_corpus

ROOT = Path(__file__).resolve().parents[1]


def adapter_command(module):
    return next(item for item in COMMANDS if item.command[1:3] == ("-m", module))


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


@pytest.mark.parametrize("module", ["dufmech.research", "dufmech.exports"])
def test_qc_runs_real_adapter_checks_and_rejects_invalid_inputs(tmp_path, monkeypatch, module):
    monkeypatch.setenv("PYTHONPATH", str(ROOT / "src") + os.pathsep
                       + os.environ.get("PYTHONPATH", ""))
    command = adapter_command(module)
    if module == "dufmech.research":
        root = tmp_path / "research"
        (root / "conf").mkdir(parents=True)
        target = root / "conf/deep_research_provider.yaml"
        shutil.copyfile(ROOT / "conf/deep_research_provider.yaml", target)
        assert command.command[-1] == "check"
    else:
        root = make_corpus(tmp_path / "exports")
        exports.write_exports(root, apply=True)
        target = root / exports.KGX_EDGES
        assert command.command[-1] == "--check"
    before = inventory(root)
    assert run_quality_commands([command], cwd=root) == 0
    assert inventory(root) == before
    target.write_text("invalid: fixture\n")
    before = inventory(root)
    assert run_quality_commands([command], cwd=root) == 1
    assert inventory(root) == before


def test_qc_full_oak_gate_requires_explicit_isolated_runtime(monkeypatch, tmp_path):
    monkeypatch.delenv("CLAW_ROOT", raising=False)
    monkeypatch.setenv("PYTHONPATH", str(ROOT / "src") + os.pathsep
                       + os.environ.get("PYTHONPATH", ""))
    command = adapter_command("dufmech.id_labels")
    assert command.command[-1] == "--check"
    assert "--check-index" not in command.command
    assert run_quality_commands([command], cwd=tmp_path) == 1
    assert not list(tmp_path.iterdir())


def test_adapter_writer_declarations_match_real_helpers():
    rows, findings = source_governance.writer_inventory(ROOT)
    assert not [finding for finding in findings if finding.severity == "error"]
    config = yaml.safe_load((ROOT / "conf/writer_audit.yaml").read_text())
    assert config["helpers"]["retain_result"]["required_calls"] == [
        "_shared", "_result_path", "new_result_path", "write_result",
    ]
    assert config["helpers"]["write_exports"]["apply_default"] is False
    by_function = {(row["path"], row["function"]): row for row in rows}
    assert "helper:retain_result" in by_function[
        ("src/dufmech/research.py", "main")
    ]["write_evidence"]
    assert config["helpers"]["write_exports"]["formats"] == ["tsv"]
    assert "tsv" in by_function[("src/dufmech/exports.py", "write_exports")]["formats"]
    assert by_function[("src/dufmech/id_labels.py", "write_index")]["policy"] == (
        "frozen-reference-derived-explicit-cli-apply"
    )
