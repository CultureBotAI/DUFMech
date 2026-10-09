"""New review bundles preserve native digest, history and publication contracts."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy

import pytest
import yaml
from test_history import save_event
from test_reviews import legacy_review_fixture, make_root, review_payload

from dufmech import history, records, reviews, structured_reviews
from dufmech.report import ReportError
from dufmech.site_metadata import load_review_site_metadata, load_site_metadata
from dufmech.site_sources import source_path


def test_profile_skill_local_links_resolve_inside_repository():
    root = structured_reviews.ROOT
    profile = yaml.safe_load((root / "conf/record_review.yaml").read_text())
    for name in profile["skills"]:
        skill = root / name
        for link in re.findall(r"\]\(([^)]+)\)", skill.read_text()):
            if "://" in link or link.startswith("#"):
                continue
            target = (skill.parent / link.split("#", 1)[0]).resolve()
            assert target.is_relative_to(root), (name, link)
            assert target.is_file(), (name, link)


@pytest.fixture
def root(tmp_path, monkeypatch):
    root = make_root(tmp_path.resolve())
    for args in (
        ("init",), ("config", "user.name", "Synthetic fixture"),
        ("config", "user.email", "fixture@example.invalid"),
        ("remote", "add", "origin", "https://github.com/CultureBotAI/DUFMech.git"),
        ("add", "README.md"),
        ("-c", "commit.gpgsign=false", "-c", "core.hooksPath=/dev/null",
         "commit", "-m", "Synthetic fixture"),
    ):
        subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True)
    validator = history.history_validator(history.REPO_ROOT)
    monkeypatch.setattr(history, "history_validator", lambda _: validator)
    return root


def payload(root, kind="record", *, projection=False):
    if projection:
        records.write_records(root, records.build_records(root), apply=True)
    inspection = reviews.inspect_review(
        root, "category" if kind == "batch" else kind,
        "PF04149" if kind == "record" else "fixture",
        **({"members": ["PF04149", "PF19054"], "selection": "Both fixture families."}
           if kind in {"category", "batch"} else {}),
    )
    targets = [item["target_id"] for item in inspection["structured"]["targets"]]
    value = {
        **inspection["structured"], "schema_version": "1.0.0",
        "review_id": f"20261007T010400Z-{kind}-fixture", "title": "Synthetic native review",
        "started_at": "2026-10-07T01:00:00Z", "finished_at": "2026-10-07T01:04:00Z",
        "reviewer": {"identity": "test-reviewer", "kind": "human",
                     "independence": "self_review", "independence_basis": "Synthetic fixture."},
        "skill": ".claude/skills/review-yaml-record/SKILL.md",
        "completion": "completed", "verdict": "pass", "native_verdict": "PASS",
        "scientific_review": False, "summary": "Inspected synthetic metadata only.",
        "scope": {"description": "Metadata audit without literature reassessment.",
                  "selection": "Both fixture families." if kind in {"category", "batch"}
                  else "Explicit fixture targets.",
                  "coverage": "full", "population_size": len(targets),
                  "reviewed_target_ids": targets},
        "checks": [{"check_id": "fixture", "name": "Fixture inspection", "status": "passed",
                    "required": True, "summary": "Inspected the fixture source.",
                    "target_ids": targets}],
        "evidence": [{"evidence_id": "fixture", "kind": "record_content",
                      "reference": inspection["structured"]["targets"][0]["path"],
                      "accessed_at": "2026-10-07T01:00:00Z", "support": "supports",
                      "summary": "Read synthetic metadata only."}],
        "assessments": [{"assessment_id": "identity", "area": "identity", "topic": "Pfam identity",
                         "outcome": "supported", "summary": "Fixture identifiers match.",
                         "target_ids": targets, "evidence_ids": ["fixture"]}],
        "findings": [], "actions": [], "limitations": ["No biological evidence was assessed."],
    }
    if kind == "category":
        value["boundary_decisions"] = [{
            "action": "retain", "target_ids": targets, "rationale": "Distinct fixture accessions.",
            "evidence_ids": ["fixture"],
        }]
    if kind == "batch":
        value["kind"] = "batch"
        value["scope"].update(coverage="sampled", population_size=10,
                              sampling_method="Explicit deterministic fixture selection",
                              sampling_seed="fixture")
    return value


def pin_bytes(captured):
    return {path: {"repository": "https://github.com/CultureBotAI/DUFMech", "commit": "a" * 40,
                   "path": path, "sha256": hashlib.sha256(raw).hexdigest()}
            for path, raw in captured.items()}


@pytest.mark.parametrize("kind", ["record", "category", "repo", "batch"])
def test_inspect_save_load_scopes_and_immutable_common_pair(root, kind):
    value = payload(root, kind)
    path = reviews.save_review(root, value)
    assert path.relative_to(root).as_posix().startswith("reviews/structured/")
    assert path.name == "review.yaml"
    common = structured_reviews.common()
    assert common.read_review(root, path.relative_to(root).as_posix()) == value
    with pytest.raises(ValueError, match="immutable"):
        reviews.save_review(root, value)
    captured = {}
    loaded = reviews.load_review_metadata(root, source_bytes=captured)
    assert len(loaded) == 1
    assert loaded[0]["scientific_review"] is False
    assert loaded[0]["context"]["kind"] == kind
    assert set(captured) == {path.relative_to(root).as_posix(),
                             path.with_name("review.md").relative_to(root).as_posix()}
    assert all(source_path(name) for name in captured)
    native = loaded[0]
    assert native["context"]["source_files"] == {
        item["path"]: item["sha256"] for item in value["source"]["inputs"]
    }
    if kind == "repo":
        assert value["kind"] == "repository"
        assert not reviews.load_review_metadata(root, "PF04149")
    else:
        assert reviews.load_review_metadata(root, "PF04149")
        assert not native["context"]["record_digests"]
        assert value["targets"][0]["selector"] == "pfam_id=PF04149"


def test_row_only_pass_cannot_promote_projection(root):
    value = payload(root)
    path = reviews.save_review(root, value)
    records.write_records(root, records.build_records(root), apply=True)
    record = records.load_records(root)[0]
    with pytest.raises(ValueError, match="content changed"):
        reviews.require_completed_review(root, "PF04149", path.relative_to(root).as_posix(), record)


def test_new_cli_rejects_legacy_envelope_and_roundtrips_common_document(root, capsys):
    content = root / "content.yaml"
    content.write_text(yaml.safe_dump(review_payload(root)))
    args = ["--repo-root", str(root)]
    assert reviews.main([*args, "save", "--content", str(content)]) == 1
    assert "structured contract" in capsys.readouterr().err
    assert reviews.main([*args, "inspect", "record", "PF04149"]) == 0
    assert json.loads(capsys.readouterr().out)["structured"]["targets"]
    content.write_text(json.dumps(payload(root)))
    assert reviews.main([*args, "finalize", "--content", str(content)]) == 0
    assert "review.yaml" in capsys.readouterr().out
    assert reviews.main([*args, "check"]) == 0
    assert json.loads(capsys.readouterr().out)["valid_reports"] == 1
    assert reviews.main([*args, "list", "--pfam-id", "PF04149"]) == 0
    assert json.loads(capsys.readouterr().out)[0]["review_version"] == 2


def test_historical_and_common_metadata_coexist_without_migrating_bytes(root):
    old = legacy_review_fixture(root, review_payload(root))
    retained = old.read_bytes()
    new = reviews.save_review(root, payload(root))
    metadata = reviews.load_review_metadata(root, "PF04149")
    assert {item["path"] for item in metadata} == {
        old.relative_to(root).as_posix(), new.relative_to(root).as_posix(),
    }
    assert old.read_bytes() == retained


@pytest.mark.parametrize("change", ["overlay", "projection", "snapshot", "digest", "selector", "revision"])
def test_native_saver_rechecks_inputs_targets_and_semantic_digest(root, change):
    value = payload(root, projection=change != "selector")
    if change == "overlay":
        overlay = root / "curation/families/PF04149.yaml"
        overlay.parent.mkdir(parents=True)
        overlay.write_text("pfam_id: PF04149\ncuration_status: IN_PROGRESS\n")
    elif change == "projection":
        path = root / "data/families/PF04149.yaml"
        record = yaml.safe_load(path.read_text())
        record["description"] = "Changed inspected input."
        path.write_text(yaml.safe_dump(record))
    elif change == "snapshot":
        path = next((root / "data/worklists").glob("*.tsv"))
        path.write_text(path.read_text() + "\n")
    elif change == "digest":
        value["targets"][0]["semantic_digest"]["sha256"] = "a" * 64
    elif change == "selector":
        value["targets"][0]["selector"] = "pfam_id=PF19054"
    else:
        value["source"]["git_revision"] = "a" * 40
    with pytest.raises((ValueError, RuntimeError)):
        reviews.save_review(root, value)
    assert not (root / "reviews").exists()


@pytest.mark.parametrize("change", [
    lambda v: v.update(native_verdict="PASS", verdict="seed_only"),
    lambda v: v["targets"][0]["semantic_digest"].update(algorithm="unknown"),
    lambda v: v["targets"][0].update(path="README.md"),
    lambda v: v.update(repository="Example/Foreign"),
    lambda v: v.update(summary="TODO"),
    lambda v: v["checks"][0].update(status="failed"),
    lambda v: v["reviewer"].update(kind="deterministic"),
])
def test_invalid_or_false_scientific_pass_never_saves(root, change):
    value = payload(root, projection=True)
    value["scientific_review"] = True
    change(value)
    with pytest.raises(ValueError):
        reviews.save_review(root, value)
    assert not (root / "reviews").exists()


def test_completed_pass_gate_records_history_and_pages_consume_same_bundle(root):
    records.write_records(root, records.build_records(root), apply=True)
    overlay = root / "curation/families/PF04149.yaml"
    overlay.parent.mkdir(parents=True)
    curated = {"pfam_id": "PF04149", "curation_status": "IN_PROGRESS",
               "curation_history": "history/records/PF04149"}
    overlay.write_text(yaml.safe_dump(curated))
    save_event(root, event="EDIT", outcome="changed", timestamp="2026-10-07T00:50:00Z",
               target_path="curation/families/PF04149.yaml")
    value = payload(root, projection=True)
    value["scientific_review"] = True
    path = reviews.save_review(root, value)
    review_id = path.relative_to(root).as_posix()
    curated.update(review_id=review_id, curation_status="REVIEWED")
    overlay.write_text(yaml.safe_dump(curated))
    with pytest.raises(records.RecordError, match="canonical REVIEW event"):
        records.build_records(root)
    event_path = save_event(root, event="REVIEW", outcome="no_change",
                            target_path="data/families/PF04149.yaml",
                            urls=[reviews.review_report_url(review_id)])
    projected = records.build_records(root)
    record = projected["PF04149.yaml"]
    result = reviews.require_completed_review(root, "PF04149", review_id, record)
    assert result["scientific_review"] is True
    records.write_records(root, projected, apply=True)
    schema = root / "src/dufmech/schema/dufmech.yaml"
    schema.parent.mkdir(parents=True)
    schema.write_bytes(records.SCHEMA.read_bytes())
    metadata, _, copies = load_site_metadata(
        root, {"worklist": value["source"]["snapshot_id"]}, source_pins={},
    )
    assert metadata["PF04149"]["curation_status"] == "REVIEWED"
    assert copies[f"source/{review_id}"] == path.read_text()
    md = path.with_name("review.md").relative_to(root).as_posix()
    assert copies[f"source/{md}"] == path.with_name("review.md").read_text()
    save_event(root, event="AUDIT", outcome="no_change", target_path="data/families/PF04149.yaml")
    refreshed = records.build_records(root)["PF04149.yaml"]
    assert reviews.record_content_digest(record) == reviews.record_content_digest(refreshed)
    with pytest.raises(records.RecordError, match="curation_events differ"):
        records.validate_record(record, root)
    for field in ("description", "provenance", "curation_history"):
        changed = {**refreshed, field: "changed"}
        with pytest.raises(ValueError, match="content changed"):
            reviews.require_completed_review(root, "PF04149", review_id, changed)
    history_record = yaml.safe_load(event_path.read_text())
    history_record["links"]["urls"] = ["https://example.org/unrelated"]
    event_path.write_text(yaml.safe_dump(history_record))
    with pytest.raises(ValueError, match="canonical REVIEW event"):
        reviews.require_completed_review(root, "PF04149", review_id, refreshed)


@pytest.mark.parametrize("change", ["partial", "sampled", "no-native", "category", "batch", "repo"])
def test_other_common_reviews_cannot_promote_records(root, change):
    value = payload(root, change if change in {"category", "batch", "repo"} else "record",
                    projection=True)
    if change == "partial":
        value.update(completion="partial", verdict="not_assessed", native_verdict="BLOCKED")
        value["checks"][0]["status"] = "unavailable"
    elif change == "sampled":
        value["scope"].update(coverage="sampled", sampling_method="Explicit one-record sample")
    elif change == "no-native":
        del value["native_verdict"]
    path = reviews.save_review(root, value)
    record = records.load_records(root)[0]
    with pytest.raises(ValueError, match="PASS"):
        reviews.require_completed_review(root, "PF04149", path.relative_to(root).as_posix(), record)


def test_validated_pair_capture_survives_replacement_and_pins_require_both_bytes(root, monkeypatch):
    path = reviews.save_review(root, payload(root))
    relative = path.relative_to(root).as_posix()
    captured = {}
    reviews.load_review_metadata(root, source_bytes=captured)
    original_reader = reviews.read_source_bytes

    def replace_after_capture(base, name):
        raw = original_reader(base, name)
        if name.startswith("reviews/structured/"):
            (base / name).write_bytes(b"Unvalidated replacement\n")
        return raw

    monkeypatch.setattr(reviews, "read_source_bytes", replace_after_capture)
    metadata, _, copies = load_review_site_metadata(
        root, {"PF04149"}, source_pins=pin_bytes(captured),
    )
    assert metadata["PF04149"]["reviews"][0]["scientific_review"] is False
    assert copies == {f"source/{name}": raw.decode() for name, raw in captured.items()}
    monkeypatch.setattr(reviews, "read_source_bytes", original_reader)
    with pytest.raises(ValueError):
        reviews.load_review_metadata(root)
    for name, raw in captured.items():
        (root / name).write_bytes(raw)
    pins = pin_bytes(captured)
    pins.pop(path.with_name("review.md").relative_to(root).as_posix())
    with pytest.raises(ReportError, match="pin bytes differ"):
        load_review_site_metadata(root, {"PF04149"}, source_pins=pins)
    assert relative in captured


@pytest.mark.parametrize("ancestor", ["reviews", "reviews/structured"])
def test_native_output_symlink_is_refused(root, tmp_path_factory, ancestor):
    outside = tmp_path_factory.mktemp("outside")
    link = root / ancestor
    link.parent.mkdir(parents=True, exist_ok=True)
    link.symlink_to(outside, target_is_directory=True)
    with pytest.raises((ValueError, OSError)):
        reviews.save_review(root, payload(root))
    assert not list(outside.iterdir())


def test_git_visibility_and_hidden_invalid_bundle_are_enforced(root):
    value = payload(root)
    (root / ".gitignore").write_text("reviews/\n")
    with pytest.raises(ValueError, match="ignored"):
        reviews.save_review(root, value)
    (root / ".gitignore").write_text("")
    path = reviews.save_review(root, value)
    (path.parent / ".draft").write_text("Unfinished artifact")
    with pytest.raises(ValueError, match="incomplete"):
        reviews.load_review_metadata(root)


def test_concurrent_shared_saves_publish_one_pair_per_unique_id(root):
    value = payload(root)
    def save(number):
        content = deepcopy(value)
        content["review_id"] += f"-{number}"
        return reviews.save_review(root, content)
    with ThreadPoolExecutor(max_workers=4) as pool:
        paths = list(pool.map(save, range(8)))
    assert len(set(paths)) == len(reviews.load_review_metadata(root)) == 8


def test_common_direct_save_still_cannot_bypass_native_digest_algorithm(root):
    value = payload(root, projection=True)
    value["targets"][0]["semantic_digest"]["algorithm"] = "raw-file-hash"
    path = structured_reviews.common().save_review(root, json.loads(json.dumps(value)))
    with pytest.raises(ValueError, match="semantic digest algorithm"):
        reviews.read_review(root, path)


def test_native_capture_rejects_unverified_or_forged_committed_provenance(root):
    value = payload(root, projection=True)
    path = reviews.save_review(root, value)
    shared = structured_reviews.common()
    for state, revision in (("working_tree", "a" * 40),
                            ("git_commit", value["source"]["git_revision"])):
        altered = json.loads(json.dumps(value))
        altered["source"].update(state=state, git_revision=revision)
        path.write_text(yaml.safe_dump(altered, sort_keys=False))
        path.with_name("review.md").write_text(shared.render_markdown(altered))
        captured = {}
        with pytest.raises(ValueError, match="source provenance"):
            reviews.load_review_metadata(root, source_bytes=captured)
        assert captured == {}
