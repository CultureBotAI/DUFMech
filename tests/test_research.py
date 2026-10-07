"""Exercise the actual shared contract offline, not a substitute provider runner."""

import base64
import hashlib
import json
import socket
import subprocess
import sys
from copy import deepcopy
from pathlib import Path

import kg_microbe_research as shared
import pytest

from dufmech import research

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def root(tmp_path):
    (tmp_path / "conf").mkdir()
    (tmp_path / research.PROFILE).write_bytes((ROOT / research.PROFILE).read_bytes())
    target = tmp_path / "data/families/PF04149.yaml"
    target.parent.mkdir(parents=True)
    target.write_bytes((ROOT / "data/families/PF04149.yaml").read_bytes())
    return tmp_path


@pytest.fixture(autouse=True)
def offline(monkeypatch):
    def refused(*args, **kwargs):
        raise AssertionError("Network access attempted")

    monkeypatch.setattr(socket.socket, "connect", refused)
    monkeypatch.setattr(socket, "create_connection", refused)


def build(root, **kwargs):
    return research.scaffold_result(
        root, pfam_id="PF04149", question="Which identity provenance needs checking?",
        simulate=True, **kwargs,
    )


def test_profile_and_nonvacuous_shared_ranking(root):
    loaded = research.profile(root)
    assert loaded.mech == "DUFMech"
    assert set(loaded.focuses) == {"identity_provenance", "functional_evidence"}
    assert loaded.source_sha256 == hashlib.sha256((root / research.PROFILE).read_bytes()).hexdigest()
    reports = []
    for focus in loaded.focuses:
        report = research.triage(root, focus=focus)
        assert report == research.triage(root, focus=focus)
        assert len(report["stages"]) == 3
        for stage in report["stages"]:
            assert {row["provider"] for row in stage["ranking"]} == set(shared.PROVIDERS)
            assert stage["recommended_available"] is None
        reports.append(report)
    assert reports[0]["stages"][0]["ranking"] != reports[1]["stages"][0]["ranking"]


def test_no_ambient_credentials_or_discovery(root, monkeypatch):
    from kg_microbe_research import providers

    original = providers.credential_status
    seen = []

    def guarded(name, environ=None, probe=None):
        assert environ == {}
        assert isinstance(probe, shared.StaticProbe)
        seen.append(name)
        return original(name, environ, probe)

    monkeypatch.setattr(providers, "credential_status", guarded)
    monkeypatch.setenv("ASTA_API_KEY", "dummy-canary-never-read")
    monkeypatch.setenv("ENABLE_MOCK_PROVIDER", "true")
    text = json.dumps(research.triage(root))
    assert seen and "dummy-canary" not in text
    assert all(row["status"] != "available" for row in research.triage(root)["stages"][0]["ranking"])


def test_shared_result_replay_reads_no_credentials_and_calls_no_tools(root, monkeypatch):
    from kg_microbe_research import providers

    original = providers.credential_status
    replay_lookups = []

    def guarded(name, environ=None, probe=None):
        assert environ == {}
        return original(name, environ, probe)

    def lookup(self, name):
        replay_lookups.append(name)
        return False

    monkeypatch.setattr(providers, "credential_status", guarded)
    monkeypatch.setattr(shared.SystemProbe, "which", lookup)
    monkeypatch.setattr(shared.SystemProbe, "has_module", lookup)
    record = build(root)
    path = research.retain_result(root, record)
    research.validate_result(root, str(path.relative_to(root)), verify_snapshots=True)
    assert set(replay_lookups) == {"claude"}  # Cyberian is blocked before lookup in b815.
    assert all(run["provider_called"] is False for run in record["runs"])


def test_positive_dry_run_policy_is_not_execution(root):
    decision = research.authorize(root, stage="discovery", simulate=True)
    assert decision["mode"] == "dry-run"
    assert decision["provider"] == "claude_code"
    assert decision["execution_authorized"] is False
    assert research.SIMULATION in decision["scope"]
    plan = shared.plan_stage(research.profile(root), "discovery", **research._context(True))
    # A meaningful contrast: canonical policy can grant a simulated live decision,
    # but the DUF adapter rejects it before evaluating that request.
    assert shared.authorize(plan, apply=True, acknowledge_usage=True).live is True
    with pytest.raises(shared.PolicyError, match="execution is disabled"):
        research.authorize(root, stage="discovery", simulate=True, apply=True,
                           acknowledge_usage=True, override_reason="Cannot waive offline boundary")


@pytest.mark.parametrize("kwargs,exception", [
    ({}, shared.PolicyError),
    ({"simulate": True, "no_paid": True}, shared.PolicyError),
    ({"simulate": True, "provider": "falcon", "override_reason": "not a bypass"}, shared.PolicyError),
    ({"simulate": True, "allow": ["typo"]}, shared.PolicyInputError),
    ({"simulate": True, "focus": "missing"}, shared.ProfileError),
    ({"simulate": True, "max_cost": "invalid"}, shared.PolicyError),
    ({"simulate": True, "max_cost": "low", "acknowledge_usage": True}, shared.PolicyError),
    ({"simulate": True, "allow": ["asta"]}, shared.PolicyError),
])
def test_negative_policy(root, kwargs, exception):
    with pytest.raises(exception):
        research.authorize(root, stage="discovery", **kwargs)


@pytest.mark.parametrize("mutation", ["unknown", "weight", "duplicate", "wrong-mech"])
def test_profile_rejects_invalid_data(root, mutation):
    path = root / research.PROFILE
    content = path.read_text()
    if mutation == "unknown":
        content += "execution_enabled: true\n"
    elif mutation == "weight":
        content = content.replace("cost_weight: 1", "cost_weight: true")
    elif mutation == "duplicate":
        content += "mech: DUFMech\n"
    else:
        content = content.replace("mech: DUFMech", "mech: OtherMech")
    path.write_text(content)
    with pytest.raises(shared.ProfileError):
        research.profile(root)


def test_retained_result_binds_actual_profile_target_and_query(root):
    record = build(root)
    assert record["status"] == "DRY_RUN"
    assert record["assessment_status"] == "NOT_ASSESSED"
    assert record["plan"]["authority"] == "audit_only"
    assert len(record["plan"]["provider_evaluations"]) == 3 * len(shared.PROVIDERS)
    assert len(record["runs"]) == 3
    assert not record.get("findings") and not record.get("citations")
    for run in record["runs"]:
        assert run["provider_called"] is False and run["live_authorized"] is False
        assert research.SIMULATION in run["provider_status_reason"]
        assert research.SIMULATION in run["rendered_query"]
        assert run["query_sha256"] == hashlib.sha256(run["rendered_query"].encode()).hexdigest()
    for artifact, original in zip(record["artifacts"], [research.PROFILE, Path("data/families/PF04149.yaml")]):
        raw = base64.b64decode(artifact["content_base64"])
        assert raw == (root / original).read_bytes()
        assert artifact["sha256"] == hashlib.sha256(raw).hexdigest()
    path = research.retain_result(root, record)
    assert research.validate_result(root, str(path.relative_to(root)), verify_snapshots=True) == record
    before = path.read_bytes()
    with pytest.raises(FileExistsError):
        research.retain_result(root, record)
    assert path.read_bytes() == before


@pytest.mark.parametrize("kind", ["unknown-field", "query", "snapshot", "live", "finding"])
def test_shared_schema_and_provenance_reject_tampering(root, kind):
    record = deepcopy(build(root))
    if kind == "unknown-field":
        record["made_up"] = "not in canonical schema"
    elif kind == "query":
        record["runs"][0]["rendered_query"] += " modified"
    elif kind == "snapshot":
        record["artifacts"][1]["content_base64"] = base64.b64encode(b"changed target").decode()
    elif kind == "live":
        record["runs"][0]["provider_called"] = True
    else:
        record["findings"] = [{"finding_id": "f1", "statement": "Invented finding"}]
    with pytest.raises(shared.ResearchRecordError):
        research.retain_result(root, record)
    assert not (root / "research").exists()


def test_historical_bytes_validate_but_current_snapshot_drift_fails(root):
    record = build(root)
    path = research.retain_result(root, record).relative_to(root).as_posix()
    (root / "data/families/PF04149.yaml").write_text("pfam_id: PF00001\n")
    research.validate_result(root, path)
    with pytest.raises(shared.ResearchRecordError):
        research.validate_result(root, path, verify_snapshots=True)


@pytest.mark.parametrize("output", ["../escape.yaml", "/tmp/escape.yaml", "data/families/new.yaml", "research/runs/../escape.yaml"])
def test_retention_paths_are_bounded(root, output):
    with pytest.raises(ValueError):
        research.retain_result(root, build(root), output=output)


def test_retention_rejects_symlink_and_unlabelled_result(root, tmp_path):
    record = build(root)
    outside = tmp_path / "outside"
    outside.mkdir()
    (root / "research").symlink_to(outside, target_is_directory=True)
    with pytest.raises((ValueError, shared.ResearchRecordError)):
        research.retain_result(root, record)
    assert not list(outside.iterdir())
    record["status"] = "COMPLETED"
    with pytest.raises(ValueError, match="dummy DRY_RUN"):
        research.retain_result(root, record)


def test_scaffold_requires_simulation_and_matching_target(root):
    with pytest.raises(shared.PolicyError):
        research.scaffold_result(root, pfam_id="PF04149", question="Identity?")
    with pytest.raises(ValueError, match="Pfam accession"):
        research.scaffold_result(root, pfam_id="../../secrets", question="Identity?", simulate=True)
    (root / "data/families/PF04149.yaml").write_text("pfam_id: PF00001\n")
    with pytest.raises(ValueError, match="Retained target snapshot"):
        build(root)


def test_missing_profile_or_target_is_not_an_empty_success(root):
    target = root / "data/families/PF04149.yaml"
    target.unlink()
    with pytest.raises(shared.ResearchRecordError):
        build(root)
    (root / research.PROFILE).unlink()
    with pytest.raises(shared.ProfileError):
        research.triage(root)


def test_cli_default_is_no_write_and_retention_is_explicit(root, capsys):
    args = ["scaffold-result", "--root", str(root), "--simulate", "--pfam-id", "PF04149",
            "--question", "Why this family? --apply is quoted text, not an option."]
    assert research.main(args) == 0
    record = json.loads(capsys.readouterr().out)
    assert "--apply is quoted text" in record["plan"]["question"]["text"]
    assert not (root / "research").exists()
    assert research.main([*args, "--output", "research/runs/demo.yaml"]) == 1
    capsys.readouterr()
    assert research.main([*args, "--retain", "--output", "research/runs/demo.yaml"]) == 0
    capsys.readouterr()
    assert research.main(["validate-result", "--root", str(root), "--verify-snapshots",
                          "research/runs/demo.yaml"]) == 0


def test_cli_argv_exit_codes_and_repeated_allow(root, capsys, monkeypatch):
    common = ["--root", str(root), "--simulate", "--stage", "discovery"]
    assert research.main(["authorize", *common, "--allow", "claude-code", "--allow", "claude_code"]) == 3
    assert json.loads(capsys.readouterr().out)["execution_authorized"] is False
    assert research.main(["authorize", *common, "--apply", "--acknowledge-usage"]) == 2
    capsys.readouterr()
    assert research.main(["triage", "--root", str(root), "--no-paid"]) == 1
    assert "no_paid_unsatisfiable" in json.loads(capsys.readouterr().out)
    for argv in (["authorize", *common, "--sim"], ["triage", "--bogus"], []):
        with pytest.raises(SystemExit) as exc:
            research.main(argv)
        assert exc.value.code == 1
    capsys.readouterr()
    monkeypatch.setattr(sys, "argv", ["dufmech-research", "check", "--root", str(root)])
    assert research.main() == 0
    assert json.loads(capsys.readouterr().out)["execution_enabled"] is False


def test_module_cli_forwards_process_arguments(root):
    pythonpath = f"{ROOT / 'src'}:{Path(shared.__file__).resolve().parents[1]}"
    result = subprocess.run(
        [sys.executable, "-B", "-m", "dufmech.research", "authorize", "--root", str(root),
         "--stage", "discovery", "--simulate", "--allow=claude-code"],
        env={"PYTHONPATH": pythonpath, "PYTHONDONTWRITEBYTECODE": "1"},
        capture_output=True, text=True, timeout=60, check=False,
    )
    assert result.returncode == 3, result.stderr
    assert json.loads(result.stdout)["execution_authorized"] is False


def test_missing_shared_package_fails_closed(root, monkeypatch, capsys):
    def missing(name):
        raise ImportError(name)

    monkeypatch.setattr(research.importlib, "import_module", missing)
    assert research.main(["check", "--root", str(root)]) == 1
    assert "CLAW_SRC" in json.loads(capsys.readouterr().out)["error"]
