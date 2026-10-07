import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def workflow(name):
    return yaml.safe_load((ROOT / ".github/workflows" / name).read_text())


def test_required_qc_runs_unconditionally_on_event_commit_and_queue():
    document = workflow("validate.yaml")
    events = document.get("on", document.get(True))
    assert {"pull_request", "push", "workflow_dispatch", "merge_group"} <= events.keys()
    assert events["merge_group"] == {"types": ["checks_requested"]}
    assert events["pull_request"] is None
    assert "github.run_id" in document["concurrency"]["group"]
    assert document["concurrency"]["cancel-in-progress"] == "${{ github.event_name == 'pull_request' }}"
    qc = document["jobs"]["qc"]
    assert "if" not in qc and not qc.get("continue-on-error")
    steps = qc["steps"]
    checkout = next(step for step in steps if step.get("uses", "").startswith("actions/checkout@"))
    assert "ref" not in checkout.get("with", {})
    assert checkout["with"]["persist-credentials"] is False
    assert {step.get("run") for step in steps} >= {"just qc", "npm ci", "uv sync --locked --extra dev"}


def test_pages_uses_successful_main_validation_and_serialized_current_main_guards():
    document = workflow("pages.yaml")
    events = document.get("on", document.get(True))
    assert set(events) == {"workflow_run"}
    assert events["workflow_run"] == {
        "workflows": ["Validate DUFMech"], "types": ["completed"], "branches": ["main"],
    }
    assert document["concurrency"] == {
        "group": "publish-pages", "queue": "max", "cancel-in-progress": False,
    }
    build = document["jobs"]["build"]
    for clause in (
        "conclusion == 'success'", "head_branch == 'main'",
        "head_repository.full_name == github.repository", "event == 'push'",
    ):
        assert clause in build["if"]
    checkout = next(s for s in build["steps"] if s.get("uses", "").startswith("actions/checkout@"))
    assert checkout["with"]["ref"] == "${{ github.event.workflow_run.head_sha }}"
    assert checkout["if"] == "steps.current.outputs.publish == 'true'"
    assert document["permissions"] == {"contents": "read"}
    assert document["jobs"]["deploy"]["needs"] == "build"
    for job in (build, document["jobs"]["deploy"]):
        guard = next(s for s in job["steps"] if s.get("id") == "current")
        assert guard["env"]["CANDIDATE_SHA"] == "${{ github.event.workflow_run.head_sha }}"
        assert 'git/ref/heads/main' in guard["run"]
        assert '"$CANDIDATE_SHA" = "$current_sha"' in guard["run"]


@pytest.mark.parametrize("job", ["build", "deploy"])
@pytest.mark.parametrize("current,expected", [("a" * 40, "true"), ("b" * 40, "false")])
def test_actual_pages_guards_reject_late_validation_of_superseded_main(tmp_path, job, current, expected):
    steps = workflow("pages.yaml")["jobs"][job]["steps"]
    guard = next(step for step in steps if step.get("id") == "current")
    gh = tmp_path / "gh"
    gh.write_text('#!/bin/sh\nprintf "%s\\n" "$TEST_CURRENT_MAIN"\n')
    gh.chmod(0o755)
    output = tmp_path / "outputs"
    env = {**os.environ, "PATH": str(tmp_path) + os.pathsep + os.environ["PATH"],
           "TEST_CURRENT_MAIN": current, "CANDIDATE_SHA": "a" * 40,
           "GITHUB_OUTPUT": str(output), "GH_REPO": "CultureBotAI/DUFMech"}
    subprocess.run(["bash", "-e", "-c", guard["run"]], env=env, check=True, capture_output=True)
    assert output.read_text().strip() == f"publish={expected}"


def test_pages_freshness_guard_immediately_precedes_deploy_and_reports_actual_revision():
    job = workflow("pages.yaml")["jobs"]["deploy"]
    assert job["timeout-minutes"] > 10
    steps = job["steps"]
    deploy = next(index for index, step in enumerate(steps) if step.get("id") == "deployment")
    assert steps[deploy - 1]["id"] == "current"
    assert steps[deploy]["if"] == "steps.current.outputs.publish == 'true'"
    report = steps[deploy + 1]
    assert report["if"] == "steps.deployment.outcome == 'success'"
    assert report["env"]["CANDIDATE_SHA"] == "${{ github.event.workflow_run.head_sha }}"
    assert 'git/ref/heads/main' in report["run"]


def test_native_workflow_actions_are_immutable_and_no_secrets_reach_pr_code():
    for name in ("validate.yaml", "pages.yaml"):
        raw = (ROOT / ".github/workflows" / name).read_text()
        assert "secrets." not in raw
        for job in workflow(name)["jobs"].values():
            for step in job["steps"]:
                if "uses" in step:
                    assert re.fullmatch(r"[\w-]+/[\w-]+@[a-f0-9]{40}", step["uses"])
