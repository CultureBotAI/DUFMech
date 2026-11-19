"""Execute actual CI scratch configuration with native journals (#466, 2026-11-16)."""
from __future__ import annotations

import json
import os
import shlex
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
STEP_NAME = "Set up durable validation scratch"


def test_ci_scratch_exports_drive_real_pytest_and_durable_journal(tmp_path):
    workflow = yaml.safe_load((ROOT / ".github/workflows/validate.yaml").read_text())
    steps = workflow["jobs"]["qc"]["steps"]
    configured = [step for step in steps if step.get("name") == STEP_NAME]
    assert len(configured) == 1, "CI must configure durable scratch before validation"
    step = configured[0]
    setup_index = steps.index(step)
    for index, candidate in enumerate(steps):
        if index != setup_index and any(token in candidate.get("run", "") for token in (
            "pytest", "just qc", "dufmech.site_source_publication", "check_vendored_sync",
        )):
            assert setup_index < index, "scratch must precede every validation command"
    assert step["shell"] == "bash"

    # Only child environments receive this isolated runner home; real HOME is untouched.
    home = tmp_path / "runner home"
    workspace = tmp_path / "checkout"
    home.mkdir()
    workspace.mkdir()
    probe = workspace / "test_journal_probe.py"
    probe.write_text('''
import json
import os
from pathlib import Path
import sys
import tempfile

sys.path.insert(0, os.environ["DUFMECH_PROBE_SCRIPTS"])
from close_consolidated_reviews_20261116 import Journal


def test_native_journal_accepts_configured_pytest_fixture(tmp_path):
    expected = Path(os.environ["DUFMECH_PROBE_ROOT"]).resolve()
    assert tmp_path.resolve().is_relative_to(expected / "pytest")
    assert Path(tempfile.gettempdir()).resolve() == expected / "tmp"
    journal = Journal(tmp_path / "journal.jsonl", {"issue": 466})
    journal.add("scratch_probe", purpose="offline workflow regression")
    assert journal.events[-1]["event"] == "scratch_probe"
    Path(os.environ["DUFMECH_PROBE_RECEIPT"]).write_text(json.dumps({
        "fixture": str(tmp_path.resolve()),
        "journal": str(journal.path),
        "events": [row["event"] for row in journal.events],
    }))
''')
    roots = set()
    receipts = []
    for run_id, attempt in (("43951441717", "1"), ("43951441717", "2"), ("43951441718", "1")):
        env_file = tmp_path / f"github-env-{run_id}-{attempt}"
        env_file.touch()
        child_env = dict(os.environ)
        for name in ("TMPDIR", "TMP", "TEMP", "PYTEST_ADDOPTS"):
            child_env.pop(name, None)
        child_env.update(HOME=str(home), GITHUB_WORKSPACE=str(workspace),
                         GITHUB_RUN_ID=run_id, GITHUB_RUN_ATTEMPT=attempt,
                         GITHUB_ENV=str(env_file))
        result = subprocess.run(
            ["bash", "--noprofile", "--norc", "-e", "-o", "pipefail", "-c", step["run"]],
            cwd=workspace, env=child_env, capture_output=True, text=True, check=False,
        )
        assert result.returncode == 0, result.stderr
        lines = env_file.read_text().splitlines()
        exports = dict(line.split("=", 1) for line in lines)
        assert len(lines) == len(exports) == 4
        assert set(exports) == {"TMPDIR", "TMP", "TEMP", "PYTEST_ADDOPTS"}
        expected = (home / "agent-work/DUFMech" / f"ci-{run_id}-{attempt}").resolve()
        assert expected not in roots, "run IDs and attempts need isolated scratch"
        roots.add(expected)
        assert not expected.is_relative_to(workspace.resolve())
        for name in ("TMPDIR", "TMP", "TEMP"):
            assert Path(exports[name]).resolve() == expected / "tmp"
            assert Path(exports[name]).is_dir()
        assert shlex.split(exports["PYTEST_ADDOPTS"]) == [f"--basetemp={expected / 'pytest'}"]

        receipt = tmp_path / f"receipt-{run_id}-{attempt}.json"
        child_env.update(exports)
        child_env.update(DUFMECH_PROBE_SCRIPTS=str(ROOT / "scripts/adhoc"),
                         DUFMECH_PROBE_ROOT=str(expected), DUFMECH_PROBE_RECEIPT=str(receipt))
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", str(probe)],
            cwd=workspace, env=child_env, capture_output=True, text=True, check=False,
        )
        assert result.returncode == 0, result.stdout + result.stderr
        proof = json.loads(receipt.read_text())
        assert proof["events"][-1] == "scratch_probe"
        receipts.append(proof)
    assert all(Path(row["journal"]).is_file() for row in receipts), "later runs erased earlier scratch"
