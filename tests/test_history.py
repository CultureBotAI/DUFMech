from __future__ import annotations

import copy
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


@pytest.mark.parametrize("timestamp", [
    "2000-01-01T00:00:00Z", "2000-02-29T12:34:56Z", "2099-12-31T23:59:59Z",
    "2026-10-07T01:05:00.125+00:00",
])
def test_history_year_boundaries_are_valid_and_timestamps_are_retained(root, timestamp):
    path = save_event(root, timestamp=timestamp)
    assert history.load_history_metadata(root, "PF04149")[0]["session"]["timestamp"] == timestamp
    projected = history.project_curation_events(root, "PF04149")
    assert projected[0]["timestamp"] == timestamp
    assert projected[0]["history_record"] == path.relative_to(root).as_posix()


@pytest.mark.parametrize("timestamp", [
    "1999-12-31T23:59:59Z", "2100-01-01T00:00:00Z", "2206-08-22T12:00:00Z",
    "2026-02-30T00:00:00Z", "2026-10-07T01:05:00+01:00", "2026-10-07",
    "not a timestamp", datetime(2026, 10, 7, tzinfo=timezone.utc),
])
def test_invalid_history_timestamp_never_creates_an_artifact(root, timestamp):
    with pytest.raises((ValueError, TypeError)):
        save_event(root, timestamp=timestamp)
    assert not (root / "history").exists()


@pytest.mark.parametrize("year", [1999, 2100, 2206])
def test_retained_history_year_guard_cannot_be_bypassed_by_matching_filename(root, year):
    path = save_event(root)
    record = yaml.safe_load(path.read_text())
    record["session"]["timestamp"] = f"{year}-10-07T01:05:00Z"
    record["session"]["id"] = str(year) + record["session"]["id"][4:]
    changed = path.with_name(record["session"]["id"] + ".yaml")
    path.rename(changed)
    changed.write_text(yaml.safe_dump(record))
    for load in (history.load_history_metadata, history.project_curation_events):
        with pytest.raises(ValueError, match="between 2000 and 2099"):
            load(root, "PF04149")
    assert history.main(["--repo-root", str(root), "check"]) == 1


@pytest.mark.parametrize("timestamp", ["2026-02-30T01:05:00Z", "2026-10-07T01:05:00+01:00"])
def test_retained_history_invalid_calendar_or_non_utc_timestamp_is_rejected(root, timestamp):
    path = save_event(root)
    record = yaml.safe_load(path.read_text())
    record["session"]["timestamp"] = timestamp
    path.write_text(yaml.safe_dump(record))
    with pytest.raises(ValueError, match="timestamps"):
        history.project_curation_events(root, "PF04149")


def test_curation_event_projection_is_exact_ordered_read_only_and_uses_canonical_references(root, monkeypatch):
    later = save_event(root, timestamp="2026-10-07T02:00:00.125+00:00")
    first = save_event(root)
    second = save_event(root)
    save_event(root, slug="PF19054")
    record = yaml.safe_load(later.read_text())
    record["session"]["actors"].append({
        "name": "fixture-assistant", "type": "ai_agent", "model": "fixture-model",
        "agent_tool": "fixture-harness",
    })
    record["events"].append({
        "type": "REVIEW", "outcome": "no_change", "summary": "Checked a second fixture observation.",
        "details": "This second fixture event preserves its own position in the canonical session.",
    })
    later.write_text(yaml.safe_dump(record))
    before = {path.relative_to(root).as_posix(): path.read_bytes() for path in root.rglob("*") if path.is_file()}
    records = history.load_history_metadata(root, "PF04149")
    original = copy.deepcopy(records)
    projected = history.project_curation_events(root, "PF04149")
    expected_paths = [path.relative_to(root).as_posix() for path in sorted((first, second))]
    assert [event["history_record"] for event in projected] == [
        *expected_paths, later.relative_to(root).as_posix(), later.relative_to(root).as_posix(),
    ]
    assert [event["event_index"] for event in projected] == [0, 0, 0, 1]
    for event in projected:
        canonical = yaml.safe_load((root / event["history_record"]).read_text())
        source = canonical["events"][event["event_index"]]
        assert event == {
            "timestamp": canonical["session"]["timestamp"],
            "curator": ", ".join(actor["name"] for actor in canonical["session"]["actors"]),
            "action": source["type"], "outcome": source["outcome"], "summary": source["summary"],
            "history_record": event["history_record"], "event_index": event["event_index"],
            "llm_assisted": any(actor["type"] == "ai_agent" for actor in canonical["session"]["actors"]),
        }
    assert projected[-1]["curator"] == "test-curator, fixture-assistant"
    assert [event["llm_assisted"] for event in projected] == [False, False, True, True]
    assert projected[-1]["timestamp"] == "2026-10-07T02:00:00.125+00:00"
    with pytest.raises(ValueError, match="actual canonical event"):
        history.require_record_history(root, "PF04149", "history/records/PF04149")
    assert before == {path.relative_to(root).as_posix(): path.read_bytes()
                      for path in root.rglob("*") if path.is_file()}
    monkeypatch.setattr(history, "load_history_metadata", lambda *args: pytest.fail("unexpected reload"))
    assert history._project_curation_events(list(reversed(records))) == projected
    assert records == original


def test_curation_event_projection_is_empty_without_history_and_rejects_unsafe_inputs(root):
    before = sorted(path.relative_to(root) for path in root.rglob("*"))
    assert history.project_curation_events(root, "PF04149") == []
    assert before == sorted(path.relative_to(root) for path in root.rglob("*"))
    for pfam in (None, "PF04149/../PF19054", "Pfam:PF04149", "PF1234"):
        with pytest.raises(ValueError, match="exact Pfam"):
            history.project_curation_events(root, pfam)
    path = save_event(root)
    path.write_text("history_version: 1\nevents: []\n")
    with pytest.raises(ValueError, match="schema validation"):
        history.project_curation_events(root, "PF04149")


def test_curation_event_projection_rejects_symlinked_canonical_sidecars(root):
    path = save_event(root)
    original = path.with_suffix(".original")
    path.rename(original)
    path.symlink_to(original)
    with pytest.raises(ValueError, match="symlink"):
        history.project_curation_events(root, "PF04149")


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
    {"details": "TODO\nTBD"}, {"details": "<protein_id>\n<source_url>"},
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
    approved = {**record, "curation_status": "REVIEWED", "review_id": review_id,
                "curation_events": history.project_curation_events(root, "PF04149")}
    status = reviews.require_completed_review(root, "PF04149", review_id, approved)
    assert status["scientific_review"] is False
    assert len(status["history_paths"]) == 1
    digest = reviews.record_content_digest(approved)
    save_event(root, event="AUDIT", outcome="no_change", target_path="data/families/PF04149.yaml")
    approved["curation_events"] = history.project_curation_events(root, "PF04149")
    assert len(approved["curation_events"]) == 2
    assert reviews.record_content_digest(approved) == digest
    assert reviews.require_completed_review(root, "PF04149", review_id, approved)
    approved["assertions"] = [{"statement": "A changed functional claim"}]
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
    refreshed = build_records(root)
    assert refreshed["PF04149.yaml"]["curation_events"] != reviewed["PF04149.yaml"]["curation_events"]
    assert (reviews.record_content_digest(refreshed["PF04149.yaml"])
            == reviews.record_content_digest(reviewed["PF04149.yaml"]))
    with pytest.raises(RecordError, match="stale generated"):
        write_records(root, refreshed, check=True)
    write_records(root, refreshed, apply=True)
    assert write_records(root, refreshed, check=True) == []
    changed = dict(refreshed["PF04149.yaml"], name="Changed reviewed identity")
    with pytest.raises(RecordError, match="content changed"):
        validate_record(changed, root)


@pytest.mark.parametrize("family_count", [4, 8])
def test_family_history_build_and_write_validation_stays_linear(root, monkeypatch, family_count):
    from dufmech.records import build_records, write_records

    source = json.loads((root / "data/worklists/interpro-pfam-duf-2026-10-05.json").read_text())[0]
    del source["source_url"]
    pfams = [f"PF{1000 + number:05d}" for number in range(family_count)]
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
    # Build and write each validate the view and the authoritative pointer gate.
    assert calls == Counter({pfam: 4 for pfam in pfams})
    assert sum(calls.values()) == 4 * family_count
    calls.clear()
    assert len(history.load_history_metadata(root)) == family_count
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


def test_history_source_sink_preserves_exact_validated_bytes_after_replacement(root, monkeypatch):
    path = save_event(root)
    relative = path.relative_to(root).as_posix()
    original = path.read_bytes().replace(b"\n", b"\r\n")
    path.write_bytes(original)
    capture = history.read_source_bytes
    calls = []

    def replace_after_capture(base, name):
        calls.append(name)
        raw = capture(base, name)
        (base / name).write_text("history_version: 1\nevents: []\n")
        return raw

    monkeypatch.setattr(history, "read_source_bytes", replace_after_capture)
    captured = {relative: b"untrusted sink entry is not input"}
    metadata = history.load_history_metadata(root, "PF04149", source_bytes=captured)
    assert calls == [relative]
    assert captured == {relative: original}
    assert metadata[0]["events"][0]["summary"] == "Inspected fixture provenance."
    assert "source_bytes" not in metadata[0]
    json.dumps(metadata)
    failed_capture = {}
    with pytest.raises(ValueError, match="schema validation"):
        history.load_history_metadata(root, "PF04149", source_bytes=failed_capture)
    assert failed_capture == {}


def test_history_source_sink_only_contains_requested_family(root):
    selected = save_event(root)
    save_event(root, slug="PF19054")
    captured = {}
    metadata = history.load_history_metadata(root, "PF04149", source_bytes=captured)
    assert [item["path"] for item in metadata] == [selected.relative_to(root).as_posix()]
    assert captured == {selected.relative_to(root).as_posix(): selected.read_bytes()}


def captured_review_fixture(root):
    record = {"id": "Pfam:PF04149", "pfam_id": "PF04149", "name": "DUF397",
              "curation_status": "IN_PROGRESS", "assertions": []}
    target = root / "data/families/PF04149.yaml"
    target.parent.mkdir()
    target.write_text(yaml.safe_dump(record))
    payload = review_payload(root)
    payload["verdict"] = "PASS"
    report_path = reviews.save_review(root, payload)
    review_id = report_path.relative_to(root).as_posix()
    history_path = save_event(
        root, event="REVIEW", outcome="no_change", target_path="data/families/PF04149.yaml",
        urls=[reviews.review_report_url(review_id)],
    )
    approved = {**record, "curation_status": "REVIEWED", "review_id": review_id}
    return approved, report_path, history_path


def test_review_predicate_uses_exact_validated_captures_and_public_gate_stays_fresh(root):
    record, report_path, _ = captured_review_fixture(root)
    review_id = record["review_id"]
    review_bytes, history_bytes = {}, {}
    captured_report = reviews.load_review_metadata(root, source_bytes=review_bytes)[0]
    captured_history = history.load_history_metadata(root, "PF04149", source_bytes=history_bytes)
    expected = reviews.require_completed_review(root, "PF04149", review_id, record)
    assert reviews._require_completed_review_from_metadata(
        "PF04149", review_id, record, captured_report, captured_history,
    ) == expected
    changed = reviews.read_review(root, report_path)
    changed["verdict"] = "SEED_ONLY"
    report_path.write_text(reviews._render_report(changed))
    replacement = reviews.load_review_metadata(root)[0]
    assert replacement["verdict"] == "SEED_ONLY"
    assert report_path.read_bytes() != review_bytes[review_id]
    with pytest.raises(ValueError, match="explicit PASS"):
        reviews._require_completed_review_from_metadata("PF04149", review_id, record, replacement, captured_history)
    with pytest.raises(ValueError, match="explicit PASS"):
        reviews.require_completed_review(root, "PF04149", review_id, record)
    assert reviews._require_completed_review_from_metadata(
        "PF04149", review_id, record, captured_report, captured_history,
    ) == expected


@pytest.mark.parametrize("change", [
    lambda record: record.pop("links"),
    lambda record: record["links"].update(urls=["https://example.org/different-review"]),
    lambda record: record["events"][0].update(type="AUDIT"),
    lambda record: record["events"][0].update(outcome="needs_followup"),
    lambda record: record["target"].update(path="data/worklists/interpro-pfam-duf-2026-10-05.json"),
])
def test_review_predicate_rejects_later_valid_history_without_matching_review(root, change):
    record, _, path = captured_review_fixture(root)
    review_id = record["review_id"]
    captured_report = reviews.load_review_metadata(root)[0]
    original = history.load_history_metadata(root, "PF04149")
    assert reviews.require_completed_review(root, "PF04149", review_id, record)
    altered = yaml.safe_load(path.read_text())
    change(altered)
    path.write_text(yaml.safe_dump(altered))
    captured_later = history.load_history_metadata(root, "PF04149")
    with pytest.raises(ValueError, match="canonical REVIEW event"):
        reviews._require_completed_review_from_metadata("PF04149", review_id, record, captured_report, captured_later)
    with pytest.raises(ValueError, match="canonical REVIEW event"):
        reviews.require_completed_review(root, "PF04149", review_id, record)
    assert reviews._require_completed_review_from_metadata(
        "PF04149", review_id, record, captured_report, original,
    )


def test_captured_review_predicate_binds_path_content_and_time_without_io(root, monkeypatch):
    record, _, path = captured_review_fixture(root)
    review_id = record["review_id"]
    captured_report = reviews.load_review_metadata(root)[0]
    captured_history = history.load_history_metadata(root, "PF04149")
    altered = yaml.safe_load(path.read_text())
    altered["session"]["timestamp"] = "2026-10-07T00:59:59Z"
    altered["session"]["id"] = "2026-10-07T005959Z-older-session"
    old_path = path.with_name(altered["session"]["id"] + ".yaml")
    path.unlink()
    old_path.write_text(yaml.safe_dump(altered))
    older_history = history.load_history_metadata(root, "PF04149")
    monkeypatch.setattr(reviews, "read_review", lambda *args, **kwargs: pytest.fail("unexpected report reload"))
    monkeypatch.setattr(history, "load_history_metadata", lambda *args, **kwargs: pytest.fail("unexpected history reload"))
    with pytest.raises(ValueError, match="canonical REVIEW event"):
        reviews._require_completed_review_from_metadata("PF04149", review_id, record, captured_report, older_history)
    with pytest.raises(ValueError, match="artifact path"):
        reviews._require_completed_review_from_metadata(
            "PF04149", "reports/yaml_record_review/another.md", record, captured_report, captured_history,
        )
    with pytest.raises(ValueError, match="content changed"):
        reviews._require_completed_review_from_metadata(
            "PF04149", review_id, {**record, "assertions": [{"statement": "changed claim"}]},
            captured_report, captured_history,
        )
    assert reviews._require_completed_review_from_metadata(
        "PF04149", review_id, record, captured_report, captured_history,
    )["scientific_review"] is False


def test_captured_history_pointer_rejects_snapshot_retarget_with_identical_event_index(root, monkeypatch):
    _, _, path = captured_review_fixture(root)
    pointer = "history/records/PF04149"
    captured = history.load_history_metadata(root, "PF04149")
    assert history.require_record_history(root, "PF04149", pointer) == captured
    altered = yaml.safe_load(path.read_text())
    altered["target"]["path"] = "data/worklists/interpro-pfam-duf-2026-10-05.json"
    path.write_text(yaml.safe_dump(altered))
    later = history.load_history_metadata(root, "PF04149")
    assert history._project_curation_events(captured) == history._project_curation_events(later)
    with pytest.raises(ValueError, match="actual canonical event"):
        history.require_record_history(root, "PF04149", pointer)
    monkeypatch.setattr(history, "load_history_metadata", lambda *args, **kwargs: pytest.fail("unexpected history reload"))
    with pytest.raises(ValueError, match="actual canonical event"):
        history._require_record_history_from_metadata("PF04149", pointer, later)
    with pytest.raises(ValueError, match="exact Pfam"):
        history._require_record_history_from_metadata("PF04149", "history/records/PF19054", captured)
    with pytest.raises(ValueError, match="actual canonical event"):
        history._require_record_history_from_metadata("PF19054", "history/records/PF19054", captured)
    assert history._require_record_history_from_metadata("PF04149", pointer, captured) == captured
