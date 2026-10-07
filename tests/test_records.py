from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import pytest
import yaml

from dufmech import history
from dufmech import records as records_module
from dufmech.records import (
    RecordError,
    build_records,
    load_records,
    load_yaml,
    safe_path,
    validate_record,
    write_records,
    write_schema_artifacts,
)
from dufmech.score_inputs import load_score_input
from dufmech.scoring_snapshot import write_score_snapshot
from dufmech.snapshot import write_worklist_snapshot
from dufmech.worklist import DufFamilyRow
from tests.test_report import worklist_row
from tests.test_scoring_snapshot import score_row


@pytest.fixture
def corpus(tmp_path):
    root = tmp_path.resolve()
    row = worklist_row("PF00001", proteins=10)
    row["interpro_id"] = "IPR000001"
    del row["source_url"]
    write_worklist_snapshot([DufFamilyRow(**row)], root / "data/worklists",
                           snapshot_date="2026-10-01")
    return root


@pytest.fixture
def history_corpus(corpus, monkeypatch):
    canonical = history.history_validator(history.REPO_ROOT)
    monkeypatch.setattr(history, "history_validator", lambda _: canonical)
    write_records(corpus, build_records(corpus), apply=True)
    return corpus


def append_family_audit(root, timestamp="2026-10-07T12:00:00Z"):
    return history.new_history(
        root, kind="record", slug="PF00001", target_path="data/families/PF00001.yaml",
        timestamp=timestamp, summary="Checked fixture source identity.",
        details="Compared the generated fixture identity with its frozen source row.",
        actor_name="fixture-curator", actor_type="human", event="REVIEW", outcome="no_change",
    )


def test_deterministic_identity_projection_dry_run_apply_and_check(corpus):
    records = build_records(corpus)
    record = records["PF00001.yaml"]
    assert record["id"] == "Pfam:PF00001"
    assert record["name"] == "Domain of unknown function PF00001"
    assert record["curation_status"] == "SEEDED"
    assert record["characterization_status"] == "UNSCORED"
    assert record["interpro_id"] == "InterPro:IPR000001"
    assert "curation_events" not in record
    assert write_records(corpus, records) == ["PF00001.yaml", "manifest.json"]
    assert not (corpus / "data/families").exists()
    with pytest.raises(RecordError, match="stale"):
        write_records(corpus, records, check=True)
    write_records(corpus, records, apply=True)
    assert load_records(corpus) == [record]
    assert write_records(corpus, build_records(corpus), check=True) == []


def test_history_export_replays_real_sidecars_without_promoting_seed(history_corpus):
    path = append_family_audit(history_corpus)
    record = build_records(history_corpus)["PF00001.yaml"]
    assert record["curation_status"] == "SEEDED"
    assert "curation_history" not in record
    assert record["curation_events"] == [{
        "timestamp": "2026-10-07T12:00:00Z", "curator": "fixture-curator",
        "action": "REVIEW", "outcome": "no_change", "summary": "Checked fixture source identity.",
        "history_record": path.relative_to(history_corpus).as_posix(),
        "event_index": 0, "llm_assisted": False,
    }]
    validate_record(record, history_corpus)
    write_records(history_corpus, {"PF00001.yaml": record}, apply=True)
    assert load_records(history_corpus) == [record]
    from dufmech.datamodel.dufmech import FamilyRecord

    model = FamilyRecord(**record)
    assert model.curation_events[0].history_record == record["curation_events"][0]["history_record"]


@pytest.mark.parametrize("timestamp", [
    "2000-01-01T00:00:00Z", "2026-10-07T12:00:00Z", "2026-10-07T12:00:00+00:00",
    "2026-10-07T12:00:00.123456789Z", "2099-12-31T23:59:59.123456789+00:00",
])
def test_history_export_preserves_model_serialization_round_trip(history_corpus, timestamp):
    from linkml_runtime.dumpers import json_dumper, yaml_dumper

    from dufmech.datamodel.dufmech import FamilyRecord

    append_family_audit(history_corpus, timestamp)
    record = build_records(history_corpus)["PF00001.yaml"]
    model = FamilyRecord(**record)
    restored = (
        json.loads(json_dumper.dumps(model, inject_type=False)),
        yaml.safe_load(yaml_dumper.dumps(model)),
    )
    for result in restored:
        assert result == record
        assert result["curation_events"][0]["timestamp"] == timestamp
        validate_record(result, history_corpus)


@pytest.mark.parametrize("timestamp", [
    "1999-12-31T23:59:59Z", "2100-01-01T00:00:00Z", "2026-10-07",
    "2026-13-07T12:00:00Z", "2026-02-30T12:00:00Z", "2026-10-07T12:00:00",
])
def test_history_export_schema_retains_century_and_datetime_validation(history_corpus, timestamp):
    append_family_audit(history_corpus)
    record = build_records(history_corpus)["PF00001.yaml"]
    record["curation_events"][0]["timestamp"] = timestamp
    errors = list(records_module.validator().iter_errors(record))
    assert any(list(error.path) == ["curation_events", 0, "timestamp"] for error in errors)


@pytest.mark.parametrize("mutation", [
    lambda r: r.pop("curation_events"),
    lambda r: r.update(curation_events=[]),
    lambda r: r["curation_events"][0].update(summary="Fabricated audit summary"),
    lambda r: r["curation_events"][0].update(event_index=1),
    lambda r: r["curation_events"][0].update(llm_assisted=True),
    lambda r: r["curation_events"][0].update(
        history_record="history/records/PF00002/2026-10-07T120000Z-other.yaml"),
])
def test_history_export_rejects_forged_or_missing_views(history_corpus, mutation):
    append_family_audit(history_corpus)
    record = build_records(history_corpus)["PF00001.yaml"]
    mutation(record)
    with pytest.raises(RecordError, match="curation_events"):
        validate_record(record, history_corpus)
    original = (history_corpus / "data/families/PF00001.yaml").read_bytes()
    with pytest.raises(RecordError, match="curation_events"):
        write_records(history_corpus, {"PF00001.yaml": record}, apply=True)
    assert (history_corpus / "data/families/PF00001.yaml").read_bytes() == original


def test_appended_history_requires_projection_refresh(history_corpus):
    append_family_audit(history_corpus)
    first = build_records(history_corpus)
    write_records(history_corpus, first, apply=True)
    append_family_audit(history_corpus, "2026-10-07T12:01:00Z")
    with pytest.raises(RecordError, match="curation_events"):
        validate_record(first["PF00001.yaml"], history_corpus)
    with pytest.raises(RecordError):
        load_records(history_corpus)
    refreshed = build_records(history_corpus)
    assert len(refreshed["PF00001.yaml"]["curation_events"]) == 2
    write_records(history_corpus, refreshed, apply=True)
    assert load_records(history_corpus) == [refreshed["PF00001.yaml"]]


def test_history_export_is_not_an_overlay_authoring_surface(history_corpus):
    append_family_audit(history_corpus)
    record = build_records(history_corpus)["PF00001.yaml"]
    overlay = {key: record[key] for key in ("pfam_id", "curation_status", "curation_events")}
    with pytest.raises(RecordError, match="Additional properties"):
        validate_record(overlay, history_corpus, target="FamilyCuration")


def test_builder_loads_one_validated_history_index(history_corpus, monkeypatch):
    append_family_audit(history_corpus)
    original = history.load_history_metadata
    loads = []

    def tracked(root, pfam_id=None):
        loads.append(pfam_id)
        return original(root, pfam_id)

    monkeypatch.setattr(history, "load_history_metadata", tracked)
    build_records(history_corpus)
    assert loads == [None]


def test_derived_scores_retain_distinct_provenance(corpus):
    source = corpus / "data/worklists/interpro-pfam-duf-2026-10-01.json"
    write_score_snapshot([score_row()], corpus / "data/worklists",
                         snapshot_date="2026-10-02",
                         input_snapshot_ids={"worklist": source.stem},
                         input_provenance={"worklist": load_score_input(source, "worklist").provenance})
    record = build_records(corpus)["PF00001.yaml"]
    assert record["characterization_status"] != "UNSCORED"
    assert record["score_provenance"]["snapshot_id"] == "duf-characterization-scores-2026-10-02"
    assert "source_url" not in record["score_provenance"]
    assert record["provenance"]["snapshot_id"] == "interpro-pfam-duf-2026-10-01"


def test_legacy_unverified_scores_cannot_be_promoted_to_family_records(corpus):
    write_score_snapshot([score_row()], corpus / "data/worklists",
                         snapshot_date="2026-10-02",
                         input_snapshot_ids={"worklist": "interpro-pfam-duf-2026-10-01"})
    with pytest.raises(ValueError, match="verified score inputs"):
        build_records(corpus)


@pytest.mark.parametrize("mutation", [
    lambda r: r.update(unknown_field="no"),
    lambda r: r.update(id="Pfam:PF99999"),
    lambda r: r["counters"].update(proteins=-1),
    lambda r: r["counters"].update(proteins=True),
    lambda r: r["counters"].update(unrecognized=1),
    lambda r: r["provenance"].update(sha256="bad"),
    lambda r: r.update(curation_status="DONE"),
    lambda r: r.update(interpro_id="InterPro:IPR1"),
])
def test_closed_record_schema_rejects_invalid_fields(corpus, mutation):
    record = build_records(corpus)["PF00001.yaml"]
    mutation(record)
    with pytest.raises(RecordError):
        validate_record(record, corpus)


def test_overlay_cannot_replace_source_identity_and_orphans_fail(corpus):
    directory = corpus / "curation/families"
    directory.mkdir(parents=True)
    overlay = directory / "PF00001.yaml"
    overlay.write_text("pfam_id: PF00001\ncuration_status: IN_PROGRESS\nname: invented\n")
    with pytest.raises(RecordError, match="Additional properties"):
        build_records(corpus)
    overlay.write_text("pfam_id: PF00001\ncuration_status: SEEDED\n")
    assert build_records(corpus)["PF00001.yaml"]["curation_status"] == "SEEDED"
    overlay.rename(directory / "PF99999.yaml")
    with pytest.raises(RecordError, match="orphan"):
        build_records(corpus)


def test_reviewed_cannot_be_set_without_a_completed_report(corpus):
    record = build_records(corpus)["PF00001.yaml"]
    record["curation_status"] = "REVIEWED"
    with pytest.raises(RecordError, match="review_id"):
        validate_record(record, corpus)
    record["review_id"] = "reports/yaml_record_review/absent.md"
    with pytest.raises(RecordError, match="missing"):
        validate_record(record, corpus)


def test_duplicate_keys_are_not_silently_replaced(tmp_path):
    path = tmp_path / "duplicate.yaml"
    path.write_text("pfam_id: PF00001\npfam_id: PF00002\n")
    with pytest.raises(RecordError, match="duplicate YAML key"):
        load_yaml(path)


def assertion(root):
    path = root / "evidence/test.txt"
    path.parent.mkdir()
    path.write_text("The tested protein bound the substrate in this experiment.\n")
    return {
        "assertion_id": "test-claim", "statement": "Fixture claim only",
        "evidence_kind": "EXPERIMENTAL", "scope": "One tested protein, not the family",
        "evidence": [{
            "reference": "https://example.org/study", "source_url": "https://example.org/study",
            "snippet": "The tested protein bound the substrate", "explanation": "Fixture support",
            "cache_path": "evidence/test.txt", "cache_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }],
    }


def test_assertions_require_checked_local_quotes_not_just_urls(corpus):
    record = build_records(corpus)["PF00001.yaml"]
    record["assertions"] = [assertion(corpus)]
    overlay = {key: record[key] for key in ("pfam_id", "curation_status", "assertions")}
    validate_record(overlay, corpus, target="FamilyCuration")
    with pytest.raises(RecordError, match="curation_history"):
        validate_record(record, corpus)
    evidence = record["assertions"][0]["evidence"][0]
    evidence["snippet"] = "Fabricated claim"
    with pytest.raises(RecordError, match="quotation"):
        validate_record(overlay, corpus, target="FamilyCuration")
    evidence["snippet"] = "The tested protein"
    evidence["cache_sha256"] = "0" * 64
    with pytest.raises(RecordError, match="hash mismatch"):
        validate_record(overlay, corpus, target="FamilyCuration")


@pytest.mark.parametrize("path", ["evidence/../../outside.txt", "/tmp/outside.txt"])
def test_cache_paths_cannot_escape(corpus, path):
    with pytest.raises(RecordError, match="unsafe"):
        safe_path(corpus, path)


def test_generated_writer_preserves_manual_edits_and_unknown_files(corpus):
    records = build_records(corpus)
    write_records(corpus, records, apply=True)
    target = corpus / "data/families/PF00001.yaml"
    target.write_text(target.read_text() + "# human edit\n")
    with pytest.raises(RecordError, match="edited/unowned"):
        write_records(corpus, records, apply=True)
    assert target.read_text().endswith("# human edit\n")
    extra = target.parent / "notes.md"
    extra.write_text("preserve this")
    with pytest.raises(RecordError, match="refusing to delete"):
        write_records(corpus, records, apply=True)
    assert extra.read_text() == "preserve this"


def test_generator_rejects_symlinks_even_when_content_matches(corpus, tmp_path):
    records = build_records(corpus)
    write_records(corpus, records, apply=True)
    target = corpus / "data/families/PF00001.yaml"
    saved = tmp_path / "saved.yaml"
    target.rename(saved)
    target.symlink_to(saved)
    with pytest.raises(RecordError, match="symlink"):
        write_records(corpus, records, apply=True)


def test_batch_validation_precedes_any_write(corpus):
    records = build_records(corpus)
    other = copy.deepcopy(records["PF00001.yaml"])
    other.update(id="Pfam:PF00002", pfam_id="PF00002", unknown=True)
    records["PF00002.yaml"] = other
    with pytest.raises(RecordError):
        write_records(corpus, records, apply=True)
    assert not (corpus / "data/families").exists()


def test_generated_schema_docs_are_checked(corpus):
    assert len(write_schema_artifacts(corpus)) == 4
    assert not (corpus / "schema").exists()
    write_schema_artifacts(corpus, apply=True)
    assert write_schema_artifacts(corpus, check=True) == []
    assert not (corpus / "docs/schema.md").read_bytes().endswith(b"\n\n")
    schema = json.loads((corpus / "schema/FamilyRecord.schema.json").read_text())
    assert schema["additionalProperties"] is False
    (corpus / "docs/schema.md").write_text("stale")
    with pytest.raises(RecordError, match="stale"):
        write_schema_artifacts(corpus, check=True)


def test_generated_python_model_accepts_validated_projection(corpus):
    from dufmech.datamodel.dufmech import FamilyRecord

    record = build_records(corpus)["PF00001.yaml"]
    model = FamilyRecord(**record)
    assert str(model.id) == record["id"]
    assert model.pfam_id == record["pfam_id"]
    assert str(model.curation_status) == "SEEDED"
    assert model.provenance.sha256 == record["provenance"]["sha256"]


def test_generated_identity_tampering_is_detected_against_snapshot(corpus):
    records = build_records(corpus)
    write_records(corpus, records, apply=True)
    target = corpus / "data/families/PF00001.yaml"
    record = yaml.safe_load(target.read_text())
    record["name"] = "Invented name"
    target.write_text(yaml.safe_dump(record))
    with pytest.raises(RecordError):
        write_records(corpus, build_records(corpus), check=True)
    with pytest.raises(RecordError):
        load_records(corpus)


def test_concurrent_edit_after_preflight_is_preserved(corpus, monkeypatch):
    records = build_records(corpus)
    first = records["PF00001.yaml"]
    second = copy.deepcopy(first)
    second.update(pfam_id="PF00002", id="Pfam:PF00002")
    records["PF00002.yaml"] = second
    write_records(corpus, records, apply=True)
    changed = copy.deepcopy(records)
    changed["PF00001.yaml"]["name"] = "new source label 1"
    changed["PF00002.yaml"]["name"] = "new source label 2"
    publish = records_module._publish_projection
    target = corpus / "data/families/PF00002.yaml"
    edited = target.read_bytes() + b"# concurrent human edit\n"

    def interleave(root, path, payload, expected):
        publish(root, path, payload, expected)
        if path.name == "PF00001.yaml":
            target.write_bytes(edited)

    monkeypatch.setattr(records_module, "_publish_projection", interleave)
    with pytest.raises(RecordError, match="concurrent edit"):
        write_records(corpus, changed, apply=True)
    assert target.read_bytes() == edited
    recovered = list((corpus / ".dufmech/record-recovery").glob("*/PF00002.yaml"))
    assert any(path.read_bytes() == edited for path in recovered)


def test_competing_creation_is_never_overwritten(corpus, monkeypatch):
    records = build_records(corpus)
    publish = records_module._publish_projection
    target = corpus / "data/families/PF00001.yaml"

    def interleave(root, path, payload, expected):
        if path == target:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("concurrent file")
        publish(root, path, payload, expected)

    monkeypatch.setattr(records_module, "_publish_projection", interleave)
    with pytest.raises(RecordError, match="publication conflict"):
        write_records(corpus, records, apply=True)
    assert target.read_text() == "concurrent file"


@pytest.mark.parametrize("projection", [True, False])
def test_parent_directory_swap_cannot_redirect_publication(corpus, monkeypatch, projection):
    target = corpus / "data/families/PF00001.yaml"
    target.parent.mkdir(parents=True)
    target.write_bytes(b"original")
    outside = corpus / "outside"
    outside.mkdir()
    (outside / target.name).write_bytes(b"outside human data")
    moved = corpus / "saved-families"
    stage = records_module._stage_file

    def swap(directory, payload):
        name = stage(directory, payload)
        target.parent.rename(moved)
        target.parent.symlink_to(outside, target_is_directory=True)
        return name

    monkeypatch.setattr(records_module, "_stage_file", swap)
    if projection:
        records_module._publish_projection(corpus, target, b"generated", b"original")
    else:
        records_module._publish(corpus, target, b"generated")
    assert (outside / target.name).read_bytes() == b"outside human data"
    assert (moved / target.name).read_bytes() == b"generated"
    assert list(outside.iterdir()) == [outside / target.name]


def test_staging_failure_does_not_displace_existing_record(corpus, monkeypatch):
    records = build_records(corpus)
    write_records(corpus, records, apply=True)
    target = corpus / "data/families/PF00001.yaml"
    original = target.read_bytes()
    records["PF00001.yaml"]["name"] = "changed source"

    def fail(directory, payload):
        raise OSError("simulated staging failure")

    monkeypatch.setattr(records_module, "_stage_file", fail)
    with pytest.raises(OSError, match="staging failure"):
        write_records(corpus, records, apply=True)
    assert target.read_bytes() == original


def test_failed_publication_restores_displaced_record(corpus, monkeypatch):
    records = build_records(corpus)
    write_records(corpus, records, apply=True)
    target = corpus / "data/families/PF00001.yaml"
    original = target.read_bytes()
    records["PF00001.yaml"]["name"] = "changed source"
    link = records_module.os.link

    def fail_generated(source, destination, **kwargs):
        if source.startswith(".dufmech-"):
            raise OSError("simulated publication failure")
        return link(source, destination, **kwargs)

    monkeypatch.setattr(records_module.os, "link", fail_generated)
    with pytest.raises(RecordError, match="publication conflict"):
        write_records(corpus, records, apply=True)
    assert target.read_bytes() == original
    assert not list(target.parent.glob(".dufmech-*"))


@pytest.mark.parametrize("cancellation", [KeyboardInterrupt, SystemExit])
@pytest.mark.parametrize("point", ["publication", "after_rename"])
def test_cancellation_restores_displaced_record_and_propagates(corpus, monkeypatch,
                                                             cancellation, point):
    records = build_records(corpus)
    write_records(corpus, records, apply=True)
    target = corpus / "data/families/PF00001.yaml"
    original = target.read_bytes()
    records["PF00001.yaml"]["name"] = "changed source"
    operation = records_module.os.link if point == "publication" else records_module.os.rename

    def interrupt(source, destination, **kwargs):
        if point == "after_rename":
            operation(source, destination, **kwargs)
            raise cancellation("cancelled after displacement")
        if source.startswith(".dufmech-"):
            raise cancellation("cancelled before publication")
        return operation(source, destination, **kwargs)

    monkeypatch.setattr(records_module.os, "link" if point == "publication" else "rename", interrupt)
    with pytest.raises(cancellation, match="cancelled"):
        write_records(corpus, records, apply=True)
    assert target.read_bytes() == original
    assert not list(target.parent.glob(".dufmech-*"))


def test_cancelled_publication_preserves_competing_creation(corpus, monkeypatch):
    records = build_records(corpus)
    write_records(corpus, records, apply=True)
    target = corpus / "data/families/PF00001.yaml"
    original = target.read_bytes()
    records["PF00001.yaml"]["name"] = "changed source"
    link = records_module.os.link

    def interrupt(source, destination, **kwargs):
        if source.startswith(".dufmech-"):
            target.write_bytes(b"concurrent creation")
            raise KeyboardInterrupt
        return link(source, destination, **kwargs)

    monkeypatch.setattr(records_module.os, "link", interrupt)
    with pytest.raises(KeyboardInterrupt):
        write_records(corpus, records, apply=True)
    assert target.read_bytes() == b"concurrent creation"
    assert any(path.read_bytes() == original
               for path in (corpus / ".dufmech/record-recovery").glob("*/PF00001.yaml"))


def test_source_labels_are_preserved_verbatim(corpus):
    row = worklist_row("PF00001", proteins=10)
    row["interpro_id"] = "IPR000001"
    row["name"] = "  frozen source label  "
    row["short_name"] = " DUF1 "
    del row["source_url"]
    write_worklist_snapshot([DufFamilyRow(**row)], corpus / "data/worklists",
                           snapshot_date="2026-10-02")
    record = build_records(corpus)["PF00001.yaml"]
    assert record["name"] == row["name"]
    assert record["short_name"] == row["short_name"]


def test_source_label_types_cannot_be_normalized_into_empty_strings(corpus):
    row = worklist_row("PF00001", proteins=10)
    row["interpro_id"] = "IPR000001"
    row["name"] = 42
    del row["source_url"]
    write_worklist_snapshot([DufFamilyRow(**row)], corpus / "data/worklists",
                           snapshot_date="2026-10-02")
    with pytest.raises(RecordError, match="source name must be a string"):
        build_records(corpus)


def test_package_schema_is_shipped():
    assert (Path(__file__).parents[1] / "src/dufmech/schema/dufmech.yaml").is_file()
