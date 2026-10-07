from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
import yaml

from dufmech import history
from dufmech import knowledge_gaps as gaps
from dufmech.records import RecordError, build_records, load_yaml, write_records
from dufmech.snapshot import write_worklist_snapshot
from dufmech.worklist import DufFamilyRow
from tests.test_report import worklist_row


@pytest.fixture
def corpus(tmp_path, monkeypatch):
    canonical = history.history_validator(history.REPO_ROOT)
    monkeypatch.setattr(history, "history_validator", lambda _: canonical)
    root = tmp_path.resolve()
    (root / "conf").mkdir()
    source = Path(__file__).resolve().parents[1] / gaps.CONFIG
    (root / gaps.CONFIG).write_bytes(source.read_bytes())
    rows = []
    for pfam in ("PF00001", "PF00002"):
        row = worklist_row(pfam, proteins=10)
        row["short_name"] = "DUF" + pfam[-1]
        row["interpro_id"] = "IPR0" + pfam[2:]
        del row["source_url"]
        rows.append(DufFamilyRow(**row))
    write_worklist_snapshot(rows, root / "data/worklists", snapshot_date="2026-10-01")
    write_records(root, build_records(root), apply=True)
    (root / "evidence/knowledge_gaps").mkdir(parents=True)
    source = {
        "version": 1, "source_url": "https://example.org/fixture-abstracts",
        "retrieved_at": "2026-10-07T10:00:00Z",
        "results": [{"reference": "PMID:1", "title": "Synthetic test fixture, not evidence",
                     "abstract": "The DUF1 substrate remains unknown. Further studies of DUF1 "
                                 "are needed to determine substrate specificity."}],
    }
    (root / "evidence/knowledge_gaps/fixture.json").write_text(json.dumps(source))
    return root


def packet(root):
    return gaps.scan(root, "evidence/knowledge_gaps/fixture.json", limit=2)


def reviewed(root):
    p, report = gaps.retain(root, packet(root), "2026-10-07T11:00:00Z")
    audit = history.new_history(
        root, kind="record", slug="PF00001", target_path="data/families/PF00001.yaml",
        timestamp="2026-10-07T12:00:00Z", summary="Reviewed synthetic gap proposal.",
        details=f"Fixture-only approval of {p.relative_to(root)}; not real scientific evidence.",
        actor_name="fixture-curator", actor_type="human", event="REVIEW", outcome="no_change",
    )
    return p.relative_to(root).as_posix(), audit.relative_to(root).as_posix(), report


def accept(root, p, audit, **kwargs):
    return gaps.accept(root, p, "PF00001", audit, actor_name="fixture-curator",
                       actor_type="human", **kwargs)


def test_offline_shared_scoring_is_deterministic_and_does_not_call_network(corpus, monkeypatch):
    import urllib.request

    monkeypatch.setattr(urllib.request, "urlopen", lambda *a, **kw: pytest.fail("network"))
    before = (corpus / "data/families/PF00001.yaml").read_bytes()
    result = packet(corpus)
    assert result == packet(corpus)
    assert result["records_scanned"] == 2
    assert [r["record_id"] for r in result["scanned_records"]] == ["Pfam:PF00001", "Pfam:PF00002"]
    assert len(result["results"]) == 1
    proposed = result["results"][0]
    assert proposed["record_id"] == "Pfam:PF00001"
    assert proposed["status"] == "proposed"
    assert proposed["score"] >= 5
    assert proposed["discussion"]["kind"] == "KNOWLEDGE_GAP"
    assert proposed["discussion"]["evidence"][0]["supports"] == "NO_EVIDENCE"
    assert (corpus / "data/families/PF00001.yaml").read_bytes() == before
    assert not (corpus / "curation/families/PF00001.yaml").exists()


def test_windows_wrap_and_do_not_create_spurious_proposals(corpus):
    assert gaps.scan(corpus, "evidence/knowledge_gaps/fixture.json", offset=1, limit=1)["results"] == []
    assert gaps.scan(corpus, "evidence/knowledge_gaps/fixture.json", offset=2, limit=1)["results"]


@pytest.mark.parametrize("offset,limit", [(-1, 1), (0, 0), (0, 101), (True, 1), (0, True)])
def test_invalid_windows_fail_closed(corpus, offset, limit):
    with pytest.raises(RecordError, match="offset"):
        gaps.scan(corpus, "evidence/knowledge_gaps/fixture.json", offset=offset, limit=limit)


def test_retained_reports_timestamp_collisions_and_preservation(corpus):
    result = packet(corpus)
    first, report = gaps.retain(corpus, result, "2026-10-07T11:00:00Z")
    second, _ = gaps.retain(corpus, result, "2026-10-07T11:00:00Z")
    assert first != second
    assert load_yaml(first)["created_at"] == "2026-10-07T11:00:00Z"
    text = report.read_text()
    assert first.relative_to(corpus).as_posix() in text
    assert "## Findings" in text and "## Limitations" in text and "## Next Actions" in text
    assert "no record changed" in text


def test_accept_preview_then_apply_preserves_native_history_and_regeneration(corpus):
    p, audit, _ = reviewed(corpus)
    result = accept(corpus, p, audit)
    assert result["apply"] is False
    assert not (corpus / "curation/families/PF00001.yaml").exists()
    result = accept(corpus, p, audit, apply=True)
    assert (corpus / result["change_history"]).is_file()
    overlay = load_yaml(corpus / "curation/families/PF00001.yaml")
    assert overlay["curation_status"] == "IN_PROGRESS"
    assert len(overlay["discussions"]) == 1
    records = build_records(corpus)
    assert records["PF00001.yaml"]["characterization_status"] == "UNSCORED"
    assert records["PF00001.yaml"]["discussions"] == overlay["discussions"]
    assert len(records["PF00001.yaml"]["curation_events"]) == 2
    write_records(corpus, records, apply=True)
    assert packet(corpus)["results"][0]["status"] == "already_filed"
    with pytest.raises(RecordError, match="stale"):
        accept(corpus, p, audit, apply=True)


def test_requires_specific_canonical_review(corpus):
    p, audit, _ = reviewed(corpus)
    with pytest.raises(RecordError, match="canonical REVIEW"):
        accept(corpus, p, "history/records/PF00002/not-real.yaml", apply=True)
    doc = load_yaml(corpus / audit)
    doc["events"][0]["details"] = "Unrelated review without packet identity."
    (corpus / audit).write_text(yaml.safe_dump(doc))
    with pytest.raises(RecordError, match="canonical REVIEW"):
        accept(corpus, p, audit)


@pytest.mark.parametrize("mutation", [
    lambda p: p["results"][0]["discussion"].update(prompt="Invented conclusion"),
    lambda p: p.update(abstracts_sha256="0" * 64),
    lambda p: p.update(extra="ignored field"),
])
def test_tampered_packets_fail_before_writes(corpus, mutation):
    p, audit, _ = reviewed(corpus)
    doc = load_yaml(corpus / p)
    mutation(doc)
    (corpus / p).write_text(yaml.safe_dump(doc))
    with pytest.raises(RecordError, match="differs"):
        accept(corpus, p, audit, apply=True)
    assert not (corpus / "curation/families/PF00001.yaml").exists()


def test_missing_shared_runtime_has_actionable_cli_failure(corpus, monkeypatch, capsys):
    monkeypatch.setattr(gaps, "scan", lambda *a, **kw: (_ for _ in ()).throw(
        ImportError("kg_microbe_kgscan: set CLAW_SRC to the published CLAW src directory")))
    assert gaps.main(["--root", str(corpus), "scan", "--abstracts",
                      "evidence/knowledge_gaps/fixture.json"]) == 2
    assert "CLAW_SRC" in capsys.readouterr().err


def test_duplicate_and_invalid_abstracts_rejected(corpus):
    source = corpus / "evidence/knowledge_gaps/fixture.json"
    original = json.loads(source.read_text())
    changed = copy.deepcopy(original)
    changed["results"].append(changed["results"][0])
    source.write_text(json.dumps(changed))
    with pytest.raises(RecordError, match="duplicate abstract"):
        packet(corpus)
    source.write_text('{"version": 1, "version": 1}')
    with pytest.raises(RecordError, match="duplicate JSON"):
        packet(corpus)


def test_symlink_cache_and_output_are_rejected(corpus, tmp_path):
    source = corpus / "evidence/knowledge_gaps/fixture.json"
    outside = tmp_path / "elsewhere.json"
    source.rename(outside)
    source.symlink_to(outside)
    with pytest.raises(RecordError, match="symlink"):
        packet(corpus)


def test_failed_history_restores_unaccepted_overlay_content(corpus, monkeypatch):
    p, audit, _ = reviewed(corpus)
    monkeypatch.setattr(gaps, "new_history", lambda *a, **kw: (_ for _ in ()).throw(OSError("disk")))
    with pytest.raises(OSError, match="disk"):
        accept(corpus, p, audit, apply=True)
    overlay = load_yaml(corpus / "curation/families/PF00001.yaml")
    assert overlay == {"pfam_id": "PF00001", "curation_status": "SEEDED"}
    assert not build_records(corpus)["PF00001.yaml"].get("discussions")


def test_cross_record_duplicate_and_corpus_wide_existing_owner(corpus):
    source = corpus / "evidence/knowledge_gaps/fixture.json"
    data = json.loads(source.read_text())
    data["results"][0]["abstract"] = (
        "The DUF1 and DUF2 substrate remains unknown and further studies are needed."
    )
    source.write_text(json.dumps(data))
    result = packet(corpus)
    assert [r["status"] for r in result["results"]] == ["proposed", "cross_record_duplicate"]
    records = list(build_records(corpus).values())
    records[0]["discussions"] = [result["results"][0]["discussion"]]
    second = gaps.scan(corpus, "evidence/knowledge_gaps/fixture.json", offset=1, limit=1,
                       records=records)
    assert second["results"][0]["status"] == "already_filed"
    assert second["results"][0]["existing_owners"] == ["Pfam:PF00001"]


def test_review_must_not_predate_packet(corpus):
    p, audit, _ = reviewed(corpus)
    data = load_yaml(corpus / p)
    data["created_at"] = "2026-10-07T13:00:00Z"
    (corpus / p).write_text(yaml.safe_dump(data))
    with pytest.raises(RecordError, match="predate"):
        accept(corpus, p, audit)


def test_configuration_is_strict_and_duplicate_keys_are_rejected(corpus):
    path = corpus / gaps.CONFIG
    data = load_yaml(path)
    data["require_topic_in_sentence"] = 1
    path.write_text(yaml.safe_dump(data))
    with pytest.raises(RecordError, match="precision contract"):
        packet(corpus)


def test_output_symlink_is_not_followed(corpus, tmp_path):
    result = packet(corpus)
    outside = tmp_path / "outside"
    outside.mkdir()
    (corpus / "reports").symlink_to(outside, target_is_directory=True)
    with pytest.raises((ValueError, OSError)):
        gaps.retain(corpus, result, "2026-10-07T11:00:00Z")
    assert not list(outside.iterdir())
