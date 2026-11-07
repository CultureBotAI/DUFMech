"""Contract and preservation checks for DUFMech adoption issue #399."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
from datetime import datetime
from pathlib import Path

import pytest
import yaml
from kg_microbe_skills.catalogue import canonical_regions, render_adapter
from kg_microbe_workflows import (
    LEGACY_PARENT_PATH,
    LEGACY_SCHEMA_PATH,
    WorkflowError,
    load_effective_workflow,
)

ROOT = Path(__file__).resolve().parents[1]
RELEASE = "c26f3a0906916f9641a5f82b004b5541ae5fbe52"
BASE = "5642a645349854802748ae387c0e2df121c5e83f"
REVIEW = ROOT / "reviews/workflow/adoption/2026-11-07-cycle-v2"
PROFILE = ROOT / "workflow/mech-workflow.yaml"
PARENT = ROOT / "workflow/parent/mech-cycle.yaml"
SCHEMA = ROOT / "workflow/parent/workflow.yaml"


def document(path):
    return yaml.safe_load(path.read_text())


def effective(profile=PROFILE):
    return load_effective_workflow(PARENT, profile, "dufmech", schema_path=SCHEMA)


def claw_root():
    value = os.environ.get("CLAW_ROOT", "")
    assert value, "The workflow canary checks need the explicit reviewed CLAW_ROOT"
    root = Path(value)
    assert root.is_absolute() and root.is_dir()
    assert subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=root, text=True,
    ).strip() == RELEASE
    return root


def test_release_pin_snapshots_and_ci_runtime_are_the_same_reviewed_commit():
    claw = claw_root()
    assert (ROOT / "scripts/.vendored_canon_ref").read_text().strip() == RELEASE
    assert document(PROFILE)["parent"]["revision"] == RELEASE
    for local, canonical in (
        (PARENT, "src/kg_microbe_workflows/templates/mech-cycle.yaml"),
        (SCHEMA, "src/kg_microbe_workflows/schema/workflow.yaml"),
    ):
        assert local.read_bytes() == (claw / canonical).read_bytes()
    steps = document(ROOT / ".github/workflows/validate.yaml")["jobs"]["qc"]["steps"]
    runtime = next(step for step in steps if step["name"] == "Check out published shared adapter runtime")
    assert runtime["with"]["repository"] == "CultureBotAI/culturebotai-claw"
    assert runtime["with"]["ref"] == RELEASE


def test_v2_inserts_triage_and_preserves_all_six_existing_goal_contracts():
    current = effective()
    old = load_effective_workflow(
        LEGACY_PARENT_PATH, ROOT / "workflow/legacy/mech-workflow-v1.yaml", "dufmech",
        schema_path=LEGACY_SCHEMA_PATH,
    )
    assert old["parent_version"] == "1.0.0" and current["parent_version"] == "2.0.0"
    assert [stage["stage"] for stage in current["stages"]] == list(range(1, 8))
    assert current["stages"][0]["key"] == "open_issue_triage"
    for previous, candidate in zip(old["stages"], current["stages"][1:], strict=True):
        assert {k: v for k, v in previous.items() if k != "stage"} == {
            k: v for k, v in candidate.items() if k != "stage"}
    for policy in ("infrastructure_policy", "review_policy", "closure_policy"):
        assert current[policy] == old[policy]
    policy = current["issue_triage_policy"]
    assert policy["required_severities"] == ["critical", "high"]
    assert policy["deferred_budget_seconds"] == 14400
    assert policy["budget_clock"] == "shared_wall_clock"
    assert policy["min_deferred_groups"] == 1 and policy["max_deferred_groups"] == 2
    assert policy["budget_after_required_resolution"] is True


def test_legacy_profile_is_the_exact_previous_published_input():
    archived = ROOT / "workflow/legacy/mech-workflow-v1.yaml"
    previous = subprocess.check_output(
        ["git", "show", f"{BASE}:workflow/mech-workflow.yaml"], cwd=ROOT,
    )
    assert archived.read_bytes() == previous
    metadata = json.loads((REVIEW / "inputs.json").read_text())
    assert metadata["previous_profile"]["sha256"] == hashlib.sha256(previous).hexdigest()


def test_rendered_managed_regions_and_declared_skill_paths_match_release():
    claw = claw_root()
    for name, target in (
        ("evolve-mech-workflow", "dufmech-evolve-workflow"),
        ("triage-and-resolve-issues", "triage-and-resolve-issues"),
    ):
        canonical = (claw / f"src/kg_microbe_skills/canonical/{name}.md").read_text()
        local = (ROOT / f".claude/skills/{target}/SKILL.md").read_text()
        assert canonical_regions(local) == canonical_regions(render_adapter(canonical, "dufmech"))
    for stage in effective()["stages"]:
        for path in stage["skill_paths"]:
            assert (ROOT / path).is_file()
    previous = subprocess.check_output(
        ["git", "show", f"{BASE}:.claude/skills/dufmech-evolve-workflow/SKILL.md"],
        cwd=ROOT, text=True,
    )
    current = (ROOT / ".claude/skills/dufmech-evolve-workflow/SKILL.md").read_text()
    assert previous.split("## Repository-specific adaptation\n", 1)[1] == current.split(
        "## Repository-specific adaptation\n", 1,
    )[1]


def test_dated_backlog_context_does_not_replace_future_supervisor_freeze():
    context = json.loads((REVIEW / "backlog-context.json").read_text())
    assert datetime.fromisoformat(context["issues_observed_at"]).tzinfo is not None
    assert len(context["issues"]) == 65 and len(context["open_prs"]) == 47
    numbers = {row["number"] for row in context["issues"]}
    assert len(numbers) == 65 and 399 not in numbers
    assert {96, 143, 145, 154, 353, 369, 397} <= numbers
    assert 387 in {row["number"] for row in context["open_prs"]}
    assert "never the future stage-1 frozen inventory" in context["purpose"]
    goal = document(PROFILE)["stages"][0]["goal_text"]
    assert "supervisor-frozen" in goal and "65" not in goal
    assert "exact protein/construct/residue scope" in goal
    assert "one or two largest" in goal and "single shared four-hour" in goal


def test_adoption_inputs_remain_hash_bound_and_do_not_claim_activation():
    metadata = json.loads((REVIEW / "inputs.json").read_text())
    assert metadata["release"]["commit"] == RELEASE
    assert metadata["lane_pr"] == "https://github.com/CultureBotAI/culturebotai-claw/pull/924"
    assert metadata["runtime_activation"] == "NOT PERFORMED"
    for path, expected in metadata["candidate_inputs"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected, path
    helper = metadata["helper"]
    assert hashlib.sha256((ROOT / helper["path"]).read_bytes()).hexdigest() == helper["sha256"]


@pytest.mark.parametrize("change", ["old-schema", "wrong-pin", "missing-stage", "wrong-repository"])
def test_native_loader_rejects_partial_or_misbound_adoption(tmp_path, change):
    candidate = document(PROFILE)
    if change == "old-schema":
        candidate["schema_version"] = "1.0.0"
    elif change == "wrong-pin":
        candidate["parent"]["sha256"] = "0" * 64
    elif change == "missing-stage":
        candidate["stages"].pop(0)
    else:
        candidate["repository_key"] = "traitmech"
    path = tmp_path / "profile.yaml"
    path.write_text(yaml.safe_dump(candidate, sort_keys=False))
    with pytest.raises(WorkflowError):
        effective(path)



def test_preparation_safety_in_locked_claw_runtime():
    """The operational helper uses CLAW's adapters and its separate locked runtime."""
    environment = {key: value for key, value in os.environ.items()
                   if key not in {"VIRTUAL_ENV", "UV_PROJECT_ENVIRONMENT", "PYTHONPATH", "PYTHONHOME"}}
    result = subprocess.run(
        ["uv", "run", "--project", str(claw_root()), "--locked", "--offline",
         "python", "-I", str(ROOT / "tests/cycle_v2_preparation_contract.py")],
        cwd=ROOT, env=environment, text=True, capture_output=True, timeout=120, check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Ran 6 tests" in result.stderr
