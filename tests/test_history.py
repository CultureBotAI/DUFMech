from __future__ import annotations

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml
from test_reviews import make_root, review_payload

from dufmech import history, reviews
from dufmech.snapshot import write_worklist_snapshot
from dufmech.worklist import DufFamilyRow


@pytest.fixture
def root(tmp_path, monkeypatch):
    root = make_root(tmp_path)
    monkeypatch.setattr(reviews, "_revision", lambda _: "a" * 40)
    # Validate test events against the actual synchronized schema, never a test copy.
    validator = history.history_validator(history.REPO_ROOT)
    monkeypatch.setattr(history, "history_validator", lambda _: validator)
    return root


def save_event(root: Path, **kwargs) -> Path:
    values = {
        "kind": "record", "slug": "PF04149",
        "target_path": "data/worklists/interpro-pfam-duf-2026-10-05.json",
        "timestamp": "2026-10-07T01:05:00Z", "summary": "Inspected fixture provenance.",
        "details": "Verified the fixture manifest; no biological assertion was evaluated.",
        "actor_name": "test-curator", "actor_type": "human", "event": "AUDIT",
        "outcome": "needs_followup",
    }
    values.update(kwargs)
    return history.new_history(root, **values)


def test_actual_sidecar_passes_canonical_schema_and_roundtrips(root):
    path = save_event(root)
    record = yaml.safe_load(path.read_text())
    assert not history.history_validator(root).validate(record, "HistoryRecord").results
    assert record["session"]["id"] == path.stem
    assert record["session"]["timestamp"] == "2026-10-07T01:05:00Z"
    assert path.parent.relative_to(root).as_posix() == "history/records/PF04149"
    records = history.load_history_metadata(root, "PF04149")
    assert records == history.load_history_metadata(root, "PF04149")
    assert records[0]["target_href"].startswith("data/worklists/")
    assert history.load_history_metadata(root, "PF19054") == []


def test_same_timestamp_and_shortid_collision_never_overwrites(root, monkeypatch):
    monkeypatch.setattr(history.secrets, "token_hex", lambda n: "abc123" if n == 3 else "temporary")
    first = save_event(root)
    original = first.read_bytes()
    second = save_event(root)
    assert second.stem == first.stem + "-02"
    assert first.read_bytes() == original
    assert yaml.safe_load(second.read_text())["session"]["id"] == second.stem
    assert len(history.load_history_metadata(root)) == 2


@pytest.mark.parametrize("kwargs", [
    {"details": "TODO: replace this placeholder"}, {"summary": ""}, {"actor_name": "TBD"},
    {"actor_type": "invented"}, {"event": "SCIENCE_COMPLETE"}, {"outcome": "reviewed"},
    {"slug": "../escape"}, {"target_path": "../README.md"},
    {"target_path": "/etc/passwd"}, {"target_path": "https://example.org"},
    {"timestamp": "2026-10-07T01:05:00"}, {"actor_type": "ai_agent"},
    {"urls": ["javascript:alert(1)"]},
])
def test_invalid_event_is_not_written(root, kwargs):
    with pytest.raises((ValueError, TypeError)):
        save_event(root, **kwargs)
    assert not (root / "history").exists()


def test_missing_canonical_schema_fails_without_writing(tmp_path):
    root = make_root(tmp_path)
    with pytest.raises(ValueError, match="supported fleet sync"):
        save_event(root)
    assert not (root / "history").exists()


@pytest.mark.parametrize("relative", ["history", "history/records", "history/records/PF04149"])
def test_symlink_history_directory_is_refused(root, relative, tmp_path_factory):
    outside = tmp_path_factory.mktemp("outside")
    link = root / relative
    link.parent.mkdir(parents=True, exist_ok=True)
    link.symlink_to(outside, target_is_directory=True)
    with pytest.raises((ValueError, OSError)):
        save_event(root)
    assert not list(outside.iterdir())


def test_symlink_target_is_refused(root):
    (root / "target.md").symlink_to(root / "README.md")
    with pytest.raises(ValueError, match="symlink"):
        save_event(root, target_path="target.md")


def test_loader_checks_hidden_yml_and_closed_schema(root):
    path = save_event(root)
    record = yaml.safe_load(path.read_text())
    record["unsupported"] = "must fail"
    path.write_text(yaml.safe_dump(record))
    with pytest.raises(ValueError, match="schema validation"):
        history.load_history_metadata(root)
    path.unlink()
    (path.parent / ".hidden.yml").write_text("events: []\n")
    with pytest.raises(ValueError, match="schema validation"):
        history.load_history_metadata(root)


def test_loader_rejects_filename_disagreement_and_handles_removed_target(root):
    path = save_event(root, target_path="README.md")
    (root / "README.md").unlink()
    assert history.load_history_metadata(root)[0]["target_href"] is None
    renamed = path.with_name("moved.yaml")
    path.rename(renamed)
    with pytest.raises(ValueError, match="path must match"):
        history.load_history_metadata(root)


def test_completed_review_gate_binds_event_report_and_current_record(root):
    record = {"id": "Pfam:PF04149", "pfam_id": "PF04149", "name": "DUF397",
              "curation_status": "IN_PROGRESS", "assertions": []}
    target = root / "data/families/PF04149.yaml"
    target.parent.mkdir()
    target.write_text(yaml.safe_dump(record))
    payload = review_payload(root)
    seed = reviews.save_review(root, payload)
    with pytest.raises(ValueError, match="PASS"):
        reviews.require_completed_review(root, "PF04149", seed.relative_to(root).as_posix(), record)
    payload["verdict"] = "PASS"
    report = reviews.save_review(root, payload)
    review_id = report.relative_to(root).as_posix()
    with pytest.raises(ValueError, match="canonical REVIEW event"):
        reviews.require_completed_review(root, "PF04149", review_id, record)
    save_event(root, event="REVIEW", outcome="no_change", target_path="data/families/PF04149.yaml",
               urls=[reviews.review_report_url(review_id)])
    approved = {**record, "curation_status": "REVIEWED", "review_id": review_id}
    status = reviews.require_completed_review(root, "PF04149", review_id, approved)
    assert status["scientific_review"] is False
    assert len(status["history_paths"]) == 1
    approved["name"] = "A changed claim"
    with pytest.raises(ValueError, match="content changed"):
        reviews.require_completed_review(root, "PF04149", review_id, approved)


def test_cli_new_history_check_and_list(root, capsys):
    base = ["--repo-root", str(root)]
    assert history.main([
        *base, "new-history", "--kind", "record", "--slug", "PF04149", "--path", "README.md",
        "--timestamp", "2026-10-07T01:05:00Z", "--summary", "Inspected repository metadata.",
        "--details", "Read README contents and identified remaining documentation gaps.",
        "--actor-name", "reviewer", "--actor-type", "human", "--event", "AUDIT",
        "--outcome", "needs_followup",
    ]) == 0
    capsys.readouterr()
    assert history.main([*base, "check"]) == 0
    assert '"valid_history": 1' in capsys.readouterr().out
    assert history.main([*base, "list", "--pfam-id", "PF19054"]) == 0
    assert capsys.readouterr().out.strip() == "[]"


def test_stable_curation_history_pointer_requires_actual_family_event(root):
    pointer = "history/records/PF04149"
    with pytest.raises(ValueError, match="missing"):
        history.require_record_history(root, "PF04149", pointer)
    save_event(root, target_path="README.md")
    with pytest.raises(ValueError, match="actual canonical event"):
        history.require_record_history(root, "PF04149", pointer)
    target = root / "curation/families/PF04149.yaml"
    target.parent.mkdir(parents=True)
    target.write_text("pfam_id: PF04149\ncuration_status: IN_PROGRESS\n")
    save_event(root, event="EDIT", outcome="changed", target_path=target.relative_to(root).as_posix())
    assert len(history.require_record_history(root, "PF04149", pointer)) == 1
    with pytest.raises(ValueError, match="exact Pfam"):
        history.require_record_history(root, "PF19054", pointer)


def test_effective_family_record_progress_review_and_history_integration(root):
    from dufmech.records import RecordError, build_records, validate_record, write_records

    write_records(root, build_records(root), apply=True)
    overlay = root / "curation/families/PF04149.yaml"
    overlay.parent.mkdir(parents=True)
    curated = {"pfam_id": "PF04149", "curation_status": "IN_PROGRESS",
               "curation_history": "history/records/PF04149"}
    overlay.write_text(yaml.safe_dump(curated))
    with pytest.raises(RecordError, match="missing"):
        build_records(root)
    save_event(
        root, event="EDIT", outcome="changed", timestamp="2026-10-07T00:50:00Z",
        target_path="curation/families/PF04149.yaml",
        summary="Opened the fixture's scoped curation overlay.",
        details="Created an IN_PROGRESS overlay and its stable history directory pointer.",
    )
    progress = build_records(root)
    assert progress["PF04149.yaml"]["curation_status"] == "IN_PROGRESS"
    validate_record(progress["PF04149.yaml"], root)
    write_records(root, progress, apply=True)
    payload = review_payload(root)
    payload["verdict"] = "PASS"
    path = reviews.save_review(root, payload)
    review_id = path.relative_to(root).as_posix()
    # A pointer while IN_PROGRESS is allowed and is not a completed-review claim.
    curated["review_id"] = review_id
    overlay.write_text(yaml.safe_dump(curated))
    assert build_records(root)["PF04149.yaml"]["curation_status"] == "IN_PROGRESS"
    curated["curation_status"] = "REVIEWED"
    overlay.write_text(yaml.safe_dump(curated))
    with pytest.raises(RecordError, match="canonical REVIEW event"):
        build_records(root)
    save_event(
        root, event="REVIEW", outcome="no_change", target_path="data/families/PF04149.yaml",
        urls=[reviews.review_report_url(review_id)],
        details="Completed the scoped fixture metadata review with no scientific endorsement.",
    )
    reviewed = build_records(root)
    assert reviewed["PF04149.yaml"]["curation_status"] == "REVIEWED"
    assert (reviews.record_content_digest(progress["PF04149.yaml"])
            == reviews.record_content_digest(reviewed["PF04149.yaml"]))
    write_records(root, reviewed, apply=True)
    save_event(root, event="AUDIT", outcome="no_change", target_path="data/families/PF04149.yaml")
    assert write_records(root, build_records(root), check=True) == []
    changed = dict(reviewed["PF04149.yaml"], name="Changed reviewed identity")
    with pytest.raises(RecordError, match="content changed"):
        validate_record(changed, root)


def test_eight_families_build_and_write_validate_sixteen_events_not_128(root, monkeypatch):
    from dufmech.records import build_records, write_records

    source = json.loads((root / "data/worklists/interpro-pfam-duf-2026-10-05.json").read_text())[0]
    del source["source_url"]
    pfams = [f"PF{1000 + number:05d}" for number in range(8)]
    rows = [DufFamilyRow(**{**source, "pfam_id": pfam}) for pfam in pfams]
    write_worklist_snapshot(
        rows, root / "data/worklists", snapshot_date="2026-10-06",
        generated_at=datetime(2026, 10, 6, tzinfo=timezone.utc),
    )
    write_records(root, build_records(root), apply=True)
    directory = root / "curation/families"
    directory.mkdir(parents=True)
    for pfam in pfams:
        target = f"curation/families/{pfam}.yaml"
        (root / target).write_text(yaml.safe_dump({
            "pfam_id": pfam, "curation_status": "IN_PROGRESS",
            "curation_history": f"history/records/{pfam}",
        }))
        save_event(root, slug=pfam, target_path=target, event="EDIT", outcome="changed")
    original = history._validate_record
    calls = Counter()

    def counted(root, record, *, path=None):
        calls[record["target"]["slug"]] += 1
        return original(root, record, path=path)

    monkeypatch.setattr(history, "_validate_record", counted)
    write_records(root, build_records(root), apply=True)
    assert calls == Counter({pfam: 2 for pfam in pfams})
    assert sum(calls.values()) == 16
    calls.clear()
    assert len(history.load_history_metadata(root)) == 8
    assert calls == Counter({pfam: 1 for pfam in pfams})


def test_scoped_history_is_fresh_and_global_check_still_detects_other_invalid_family(root):
    first = save_event(root)
    second = save_event(root, slug="PF19054")
    second.write_text("history_version: 1\nevents: []\n")
    assert len(history.load_history_metadata(root, "PF04149")) == 1
    with pytest.raises(ValueError, match="schema validation"):
        history.load_history_metadata(root)
    first.write_text("history_version: 1\nevents: []\n")
    with pytest.raises(ValueError, match="schema validation"):
        history.load_history_metadata(root, "PF04149")
