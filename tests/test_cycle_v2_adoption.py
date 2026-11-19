"""Contract and preservation checks for DUFMech adoption issue #399."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
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


EXPECTED_CI_SUCCESSOR = {
    "schema_version": "1.0.0",
    "record_type": "bounded_ci_successor",
    "prepared_on": "2026-11-16",
    "issues": [
        "https://github.com/CultureBotAI/DUFMech/issues/466",
        "https://github.com/CultureBotAI/DUFMech/issues/467"
    ],
    "historical_source": {
        "repository": "CultureBotAI/DUFMech",
        "revision": "a030cca0dae2771e961ae12474c24c47a32b1363"
    },
    "reviewed_source": {
        "repository": "CultureBotAI/DUFMech",
        "revision": "397a28bfd597a1142feb1cf23c0cf3c69bc1b323",
        "retention": {
            "ref": "refs/tags/source/dufmech-review-queue-ci-20261116",
            "object": "0f567927303e5a69f2bb069986b4308c5a9b5a09",
            "type": "tag",
            "target": "397a28bfd597a1142feb1cf23c0cf3c69bc1b323",
            "target_type": "commit"
        }
    },
    "original_evidence": {
        "reviews/workflow/adoption/2026-11-07-cycle-v2/inputs.json": "807ef730d156d06d96a019d1411f75aad70771b6dd92dd718972564cb0dfad36",
        "reviews/workflow/adoption/2026-11-07-cycle-v2/migration-review.md": "ef8551648db871f6bbaa7e15dcffa60eca3525b788abf8d277c6ba7d3ad44f1a"
    },
    "changes": {
        ".github/workflows/validate.yaml": {
            "before_sha256": "2c014c50fc76025d6349db367d58df63c0ca85d38f692e5d045b36dfe7c51f15",
            "after_sha256": "a34bd89df2b77d653a761ac9dc406b093d92117ce2163572de3b27d17bbded3e"
        }
    },
    "runtime_activation": "NOT PERFORMED",
    "runtime_change": "NONE",
    "migration_hold": "UNCHANGED",
    "adoption_issue": "https://github.com/CultureBotAI/DUFMech/issues/399",
    "assessment": {
        "path": "reviews/workflow/adoption/2026-11-16-ci-scratch-successor/review.md",
        "sha256": "68c21f68203536047e51191277ea7e5a65277d5a8f7c52bd88437af47eea1e33"
    }
}

CI_SUCCESSOR = Path("reviews/workflow/adoption/2026-11-16-ci-scratch-successor")
CI_PATH = ".github/workflows/validate.yaml"
HISTORICAL_SOURCE = "a030cca0dae2771e961ae12474c24c47a32b1363"
REVIEWED_CI_SOURCE = "397a28bfd597a1142feb1cf23c0cf3c69bc1b323"


def git_output(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def published_input(revision, path):
    return git_output("show", f"{revision}:{path}")


def unique_object(pairs):
    result = dict(pairs)
    assert len(result) == len(pairs), "duplicate receipt keys"
    return result


def assert_adoption_input_lineage(root):
    """Preserve historical evidence and admit only the exact reviewed CI successor."""
    for path, expected in EXPECTED_CI_SUCCESSOR["original_evidence"].items():
        retained = published_input(HISTORICAL_SOURCE, path)
        assert hashlib.sha256(retained).hexdigest() == expected, path
        assert (root / path).read_bytes() == retained, path
    metadata = json.loads((root / REVIEW.relative_to(ROOT) / "inputs.json").read_text())
    assert metadata["release"]["commit"] == RELEASE
    assert metadata["lane_pr"] == "https://github.com/CultureBotAI/culturebotai-claw/pull/924"
    assert metadata["runtime_activation"] == "NOT PERFORMED"
    successor = json.loads((root / CI_SUCCESSOR / "inputs.json").read_text(),
                           object_pairs_hook=unique_object)
    assert successor == EXPECTED_CI_SUCCESSOR, "only the exact bounded CI successor is admitted"
    retention = successor["reviewed_source"]["retention"]
    assert git_output("rev-parse", retention["ref"]).decode().strip() == retention["object"]
    assert git_output("cat-file", "-t", retention["object"]).decode().strip() == retention["type"]
    headers = git_output("cat-file", "-p", retention["object"]).splitlines()[:2]
    assert headers == [f"object {retention['target']}".encode(),
                       f"type {retention['target_type']}".encode()]
    assert retention["target"] == REVIEWED_CI_SOURCE
    assessment = successor["assessment"]
    assert hashlib.sha256((root / assessment["path"]).read_bytes()).hexdigest() == assessment["sha256"]

    assert len(metadata["candidate_inputs"]) == 8
    for path, expected in metadata["candidate_inputs"].items():
        retained = published_input(HISTORICAL_SOURCE, path)
        assert hashlib.sha256(retained).hexdigest() == expected, path
        current = (root / path).read_bytes()
        if path == CI_PATH:
            change = successor["changes"][CI_PATH]
            assert change["before_sha256"] == expected
            reviewed = published_input(REVIEWED_CI_SOURCE, path)
            assert hashlib.sha256(reviewed).hexdigest() == change["after_sha256"]
            assert current == reviewed, "current CI differs from the reviewed source blob"
            assert hashlib.sha256(current).hexdigest() == change["after_sha256"]
        else:
            assert current == retained, path
    helper = metadata["helper"]
    retained = published_input(HISTORICAL_SOURCE, helper["path"])
    assert hashlib.sha256(retained).hexdigest() == helper["sha256"]
    assert (root / helper["path"]).read_bytes() == retained


def test_adoption_inputs_remain_hash_bound_and_do_not_claim_activation():
    assert_adoption_input_lineage(ROOT)


@pytest.mark.parametrize("change", [
    "original-receipt", "original-review", "current-profile", "current-helper",
    "current-ci-scratch", "current-ci-pin", "successor-extra-field", "successor-missing-field",
    "successor-extra-path", "successor-missing-path", "successor-historical-source",
    "successor-reviewed-source", "successor-activation", "successor-review", "assessment",
    "duplicate-key", "historical-input", "reviewed-ci-input",
    "retention-ref", "retention-type", "retention-target",
])
def test_bounded_ci_successor_rejects_unreviewed_drift(tmp_path, monkeypatch, change):
    metadata = json.loads((REVIEW / "inputs.json").read_text())
    paths = (set(metadata["candidate_inputs"]) | {metadata["helper"]["path"]}
             | set(EXPECTED_CI_SUCCESSOR["original_evidence"])
             | {str(CI_SUCCESSOR / "inputs.json"), str(CI_SUCCESSOR / "review.md")})
    for path in paths:
        target = tmp_path / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((ROOT / path).read_bytes())
    assert_adoption_input_lineage(tmp_path)  # Each negative starts from a proven valid fixture.
    if change in {"historical-input", "reviewed-ci-input"}:
        original = published_input
        corrupt_revision = HISTORICAL_SOURCE if change == "historical-input" else REVIEWED_CI_SOURCE

        def corrupted(revision, path):
            value = original(revision, path)
            if revision == corrupt_revision and path == CI_PATH:
                return value + b"\n# corrupted retained input\n"
            return value

        monkeypatch.setattr(sys.modules[__name__], "published_input", corrupted)
    elif change.startswith("retention-"):
        original_git = git_output
        retention = EXPECTED_CI_SUCCESSOR["reviewed_source"]["retention"]

        def corrupted_tag(*args):
            if change == "retention-ref" and args == ("rev-parse", retention["ref"]):
                return b"0" * 40 + b"\n"
            if change == "retention-type" and args == ("cat-file", "-t", retention["object"]):
                return b"commit\n"
            if change == "retention-target" and args == ("cat-file", "-p", retention["object"]):
                return b"object " + b"0" * 40 + b"\ntype commit\n"
            return original_git(*args)

        monkeypatch.setattr(sys.modules[__name__], "git_output", corrupted_tag)
    elif change.startswith("successor-"):
        path = tmp_path / CI_SUCCESSOR / "inputs.json"
        value = json.loads(path.read_text())
        if change == "successor-extra-field":
            value["waiver"] = True
        elif change == "successor-missing-field":
            del value["migration_hold"]
        elif change == "successor-extra-path":
            value["changes"]["workflow/mech-workflow.yaml"] = value["changes"][CI_PATH]
        elif change == "successor-missing-path":
            value["changes"] = {}
        elif change == "successor-historical-source":
            value["historical_source"]["revision"] = "0" * 40
        elif change == "successor-reviewed-source":
            value["reviewed_source"]["revision"] = "0" * 40
        elif change == "successor-activation":
            value["runtime_activation"] = "PERFORMED"
        elif change == "successor-review":
            value["assessment"]["sha256"] = "0" * 64
        path.write_text(json.dumps(value))
    elif change == "duplicate-key":
        path = tmp_path / CI_SUCCESSOR / "inputs.json"
        text = path.read_text()
        path.write_text(text.replace("{", '{"runtime_activation":"PERFORMED",', 1))
    else:
        path = {
            "original-receipt": REVIEW.relative_to(ROOT) / "inputs.json",
            "original-review": REVIEW.relative_to(ROOT) / "migration-review.md",
            "current-profile": Path("workflow/mech-workflow.yaml"),
            "current-helper": Path(metadata["helper"]["path"]),
            "current-ci-scratch": Path(CI_PATH),
            "current-ci-pin": Path(CI_PATH),
            "assessment": CI_SUCCESSOR / "review.md",
        }[change]
        target = tmp_path / path
        if change == "current-ci-pin":
            target.write_text(target.read_text().replace(RELEASE, "0" * 40))
        elif change == "original-receipt":
            target.write_bytes(target.read_bytes() + b"\n")
        else:
            target.write_bytes(target.read_bytes() + b"\n# unreviewed drift\n")
    with pytest.raises(AssertionError):
        assert_adoption_input_lineage(tmp_path)


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
