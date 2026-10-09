"""Website adapter contracts, with validated record/history loader boundaries mocked."""

from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from unittest.mock import ANY, Mock

import pytest
import yaml
from bs4 import BeautifulSoup

from dufmech import history, records, reviews
from dufmech.pages import render_site
from dufmech.report import ReportError
from dufmech.site_data import source_link
from dufmech.site_metadata import load_review_site_metadata, load_site_metadata
from dufmech.site_sources import REPOSITORY
from tests.test_report import worklist_row
from tests.test_reviews import legacy_review_fixture, make_root, review_payload


@pytest.fixture
def adapter(tmp_path, monkeypatch):
    def sidecar(pfam, hour, *, kind="record", second_event=False):
        session_id = f"2026-10-07T{hour:02d}0000Z-fixture"
        directory = "records" if kind == "record" else "infrastructure"
        events = [{
            "type": "AUDIT", "outcome": "no_change", "summary": f"Inspected {pfam} at {hour}.",
            "details": f"Full {pfam} fixture details at {hour}; no functional claim was assessed.",
        }]
        if second_event:
            events.append({
                "type": "REVIEW", "outcome": "needs_followup", "summary": "Checked source references.",
                "details": "Second event details, not the first event's details.\nReference retained below.",
                "sections": ["provenance"],
            })
        return {
            "history_version": 1,
            "path": f"history/{directory}/{pfam}/{session_id}.yaml",
            "target": {"kind": kind, "slug": pfam, "path": f"data/families/{pfam}.yaml"},
            "session": {
                "id": session_id, "timestamp": f"2026-10-07T{hour:02d}:00:00Z",
                "actors": [
                    {"type": "human", "name": "Fixture curator"},
                    {"type": "ai_agent", "name": "Fixture assistant",
                     "model": "fixture-model", "agent_tool": "fixture-harness"},
                ],
            },
            "events": events,
            "links": {"issues": [f"{REPOSITORY}/issues/100"]},
        }

    canonical = [sidecar("PF00001", 2, second_event=True), sidecar("PF00002", 1),
                 sidecar("PF00001", 1), sidecar("PF00001", 3, kind="infrastructure"),
                 sidecar("PF00999", 1)]
    projected = []
    files = {"src/dufmech/schema/dufmech.yaml": b"title: Fixture schema\n"}
    for pfam in ("PF00001", "PF00002", "PF00003"):
        record = {"pfam_id": pfam, "curation_status": "SEEDED",
                  "provenance": {"snapshot_id": "frozen"}}
        events = history._project_curation_events([
            item for item in canonical
            if item["target"]["kind"] == "record" and item["target"]["slug"] == pfam
        ])
        if events:
            record["curation_events"] = events
        projected.append(record)
        files[f"data/families/{pfam}.yaml"] = records._encoded(record)
    for item in canonical:
        files[item["path"]] = yaml.safe_dump({
            key: value for key, value in item.items() if key != "path"
        }).encode("utf-8")
    pins = {}
    for path, content in files.items():
        target = tmp_path / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
        pins[path] = {"repository": REPOSITORY, "commit": "a" * 40, "path": path,
                      "sha256": hashlib.sha256(content).hexdigest()}
    record_loader = Mock(return_value=projected)
    history_loader = Mock(return_value=canonical)

    def capture_history(root, *, source_bytes):
        source_bytes.update({item["path"]: files[item["path"]] for item in canonical})
        return history_loader.return_value

    history_loader.side_effect = capture_history
    real_history_loader = history.load_history_metadata
    monkeypatch.setattr(records, "load_records", record_loader)
    monkeypatch.setattr(history, "load_history_metadata", history_loader)
    monkeypatch.setattr(reviews, "load_review_metadata", Mock(return_value=[]))
    return {"root": tmp_path, "records": projected, "canonical": canonical, "pins": pins,
            "history_loader": history_loader, "record_loader": record_loader, "files": files,
            "real_history_loader": real_history_loader}


def load(adapter):
    return load_site_metadata(adapter["root"], {"worklist": "frozen"}, source_pins=adapter["pins"])


@pytest.mark.parametrize("pinned", [True, False])
def test_record_index_is_used_for_ui_details_and_full_source_links(adapter, pinned, monkeypatch):
    class AccessedEntry(dict):
        def __getitem__(self, key):
            accessed.append(key)
            return super().__getitem__(key)

    class SinglePassHistory(list):
        scans = 0

        def __iter__(self):
            self.scans += 1
            assert self.scans == 1, "canonical history must be grouped in a single pass"
            return super().__iter__()

    if not pinned:
        adapter["pins"] = {}
    histories = SinglePassHistory(adapter["canonical"])
    adapter["history_loader"].return_value = histories
    accessed = []
    record = adapter["records"][0]
    encoded = records._encoded(record)
    encoder = records._encoded
    # Keep the validated payload while instrumenting the returned mapping's lookups.
    monkeypatch.setattr(records, "_encoded", lambda value: encoded if value is record else encoder(value))
    record["curation_events"] = [AccessedEntry(entry) for entry in record["curation_events"]]
    metadata, provenance, copies = load(adapter)
    adapter["record_loader"].assert_called_once_with(adapter["root"])
    adapter["history_loader"].assert_called_once_with(adapter["root"], source_bytes=ANY)
    assert histories.scans == 1
    assert accessed.count("history_record") == 3
    assert accessed.count("event_index") == 3
    assert metadata["PF00001"]["record"] is record
    entries = metadata["PF00001"]["history"]
    assert [entry["event_index"] for entry in entries] == [0, 0, 1]
    canonical = {item["path"]: item for item in adapter["canonical"]}
    for entry, index in zip(entries, record["curation_events"], strict=True):
        assert {key: entry[key] for key in index} == index
        path = entry["history_record"]
        source = canonical[path]
        assert entry["description"] == source["events"][entry["event_index"]]["details"]
        assert entry["agent"] == "Fixture curator, Fixture assistant"
        assert entry["llm_assisted"] is True
        assert entry["url"] == (source_link(REPOSITORY, "a" * 40, path) if pinned else "")
        assert entry["source_path"] == path
        assert entry["local_source"] == f"source/{path}"
        assert copies[f"source/{path}"] == (adapter["root"] / path).read_text()
        assert yaml.safe_load(copies[f"source/{path}"])["links"] == source["links"]
    assert len(metadata["PF00002"]["history"]) == 1
    assert "history" not in metadata["PF00003"]
    assert "PF00999" not in metadata

    out = adapter["root"] / "site"
    render_site([worklist_row(pfam, proteins=1) for pfam in metadata], [], input_ids={"worklist": "frozen"},
                out_dir=out, family_metadata=metadata, provenance=provenance, extra_artifacts=copies)
    page = BeautifulSoup((out / "families/PF00001.html").read_text(), "html.parser")
    section = next(heading.parent for heading in page.select("h2")
                   if heading.get_text() == "Curation history and reviews")
    assert len(section.select("ol > li")) == 3
    for entry in entries:
        assert entry["description"] in section.get_text()
        href = entry["url"] if pinned else f"../{entry['local_source']}"
        assert section.select_one(f'a[href="{href}"]')
        assert (out / entry["local_source"]).read_text() == copies[entry["local_source"]]
    empty = BeautifulSoup((out / "families/PF00003.html").read_text(), "html.parser")
    assert "No retained curation events supplied." in empty.get_text()


@pytest.mark.parametrize("change", [
    lambda record: record.pop("curation_events"),
    lambda record: record.update(curation_events=[]),
    lambda record: record["curation_events"].reverse(),
    lambda record: record["curation_events"][0].update(event_index=1),
    lambda record: record["curation_events"][0].update(history_record="history/records/stale.yaml"),
    lambda record: record["curation_events"][0].update(summary="Invented event summary"),
    lambda record: record["curation_events"][0].update(curator="Invented curator"),
    lambda record: record["curation_events"][0].update(llm_assisted=False),
    lambda record: record["curation_events"].append(deepcopy(record["curation_events"][0])),
])
def test_wrong_or_stale_record_index_is_rejected(adapter, change):
    adapter["pins"] = {}
    change(adapter["records"][0])
    with pytest.raises(ReportError, match="PF00001: curation_events differ from canonical history"):
        load(adapter)


def test_canonical_change_after_record_validation_is_rejected(adapter):
    def load_then_change_history(root):
        adapter["canonical"][0]["events"].append({
            "type": "AUDIT", "outcome": "no_change", "summary": "A new canonical event.",
            "details": "Arrived after the record projection was validated.",
        })
        return adapter["records"]

    adapter["record_loader"].side_effect = load_then_change_history
    with pytest.raises(ReportError, match="curation_events differ from canonical history"):
        load(adapter)
    adapter["history_loader"].assert_called_once_with(adapter["root"], source_bytes=ANY)


def test_no_canonical_history_cannot_acquire_an_invented_event(adapter):
    adapter["pins"] = {}
    adapter["records"][2]["curation_events"] = deepcopy(adapter["records"][0]["curation_events"])
    with pytest.raises(ReportError, match="PF00003: curation_events differ from canonical history"):
        load(adapter)


def test_explicit_empty_index_does_not_invent_events(adapter):
    adapter["pins"] = {}
    adapter["records"][2]["curation_events"] = []
    metadata, _, _ = load(adapter)
    assert "history" not in metadata["PF00003"]


def test_duplicate_sidecar_identity_is_rejected(adapter):
    adapter["canonical"].append(deepcopy(adapter["canonical"][0]))
    with pytest.raises(ReportError, match="duplicate canonical history record"):
        load(adapter)


@pytest.fixture
def publication(tmp_path, monkeypatch):
    root = make_root(tmp_path / "repository")
    canonical_validator = history.history_validator(history.REPO_ROOT)
    monkeypatch.setattr(history, "history_validator", lambda _: canonical_validator)
    monkeypatch.setattr(reviews, "_revision", lambda _: "a" * 40)
    records.write_records(root, records.build_records(root), apply=True)
    schema = root / "src/dufmech/schema/dufmech.yaml"
    schema.parent.mkdir(parents=True)
    schema.write_bytes(b"title: Fixture schema\n")
    return root


def publication_source(root, kind):
    if kind == "history":
        path = history.new_history(
            root, kind="record", slug="PF04149", target_path="data/families/PF04149.yaml",
            timestamp="2026-10-07T12:00:00Z", summary="Inspected fixture source identity.",
            details="Full captured details; no scientific claim was assessed.", actor_name="Fixture curator",
            actor_type="human", event="AUDIT", outcome="no_change",
            urls=[f"{REPOSITORY}/issues/106"],
        )
        records.write_records(root, records.build_records(root), apply=True)
    elif kind == "review":
        path = legacy_review_fixture(root, review_payload(root))
    else:
        path = root / "data/families/PF04149.yaml"
    return path.relative_to(root).as_posix()


def publication_pins(root):
    return {path.relative_to(root).as_posix(): {
        "repository": REPOSITORY, "commit": "a" * 40,
        "path": path.relative_to(root).as_posix(), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    } for path in root.rglob("*") if path.is_file()}


def replace_source(path, mode, outside):
    outside.mkdir()
    replacement = outside / path.name
    replacement.write_bytes(b"PRIVATEFIXTURE: replacement must never be published\n")
    if mode == "parent_symlink":
        path.parent.rename(path.parent.with_name(path.parent.name + "-captured"))
        path.parent.symlink_to(outside, target_is_directory=True)
    elif mode == "symlink":
        path.unlink()
        path.symlink_to(replacement)
    else:
        replacement.replace(path)


def swap_after_capture(monkeypatch, kind, root, path, mode, outside):
    module = {"record": records, "history": history, "review": reviews}[kind]
    name = {"record": "load_records", "history": "load_history_metadata", "review": "load_review_metadata"}[kind]
    original = getattr(module, name)
    swaps = []

    def load_then_replace(*args, **kwargs):
        result = original(*args, **kwargs)
        # Records replay history too; replace only after the adapter's own capture.
        if kind == "record" or kwargs.get("source_bytes") is not None:
            assert not swaps
            swaps.append(path)
            replace_source(root / path, mode, outside)
        return result

    monkeypatch.setattr(module, name, load_then_replace)
    return swaps


@pytest.mark.parametrize("kind", ["record", "history", "review"])
@pytest.mark.parametrize("mode", ["regular", "symlink", "parent_symlink"])
@pytest.mark.parametrize("pinned", [True, False])
def test_postcapture_replacement_never_changes_published_bytes(
    publication, tmp_path, monkeypatch, kind, mode, pinned,
):
    root = publication
    path = publication_source(root, kind)
    original = (root / path).read_bytes()
    pins = publication_pins(root) if pinned else {}
    swaps = swap_after_capture(monkeypatch, kind, root, path, mode, tmp_path / "outside")
    metadata, provenance, copies = load_site_metadata(
        root, {"worklist": "interpro-pfam-duf-2026-10-05"}, source_pins=pins,
    )
    assert swaps == [path]
    assert copies[f"source/{path}"].encode("utf-8") == original
    assert "PRIVATEFIXTURE" not in json.dumps([metadata, provenance, copies])
    if kind == "record":
        assert records._encoded(metadata["PF04149"]["record"]) == original
    elif kind == "history":
        event = metadata["PF04149"]["history"][0]
        canonical = yaml.safe_load(original)
        assert event["summary"] == canonical["events"][0]["summary"]
        assert event["description"] == canonical["events"][0]["details"]
        assert yaml.safe_load(copies[f"source/{path}"])["links"] == canonical["links"]
    else:
        assert metadata["PF04149"]["reviews"][0]["scientific_review"] is False
        assert "## Evidence" in copies[f"source/{path}"]
    if pinned:
        assert hashlib.sha256(copies[f"source/{path}"].encode()).hexdigest() == pins[path]["sha256"]


@pytest.mark.parametrize("kind", ["record", "history", "review"])
def test_source_pin_must_match_captured_bytes_not_replacement(publication, tmp_path, monkeypatch, kind):
    root = publication
    path = publication_source(root, kind)
    pins = publication_pins(root)
    pins[path]["sha256"] = hashlib.sha256(
        b"PRIVATEFIXTURE: replacement must never be published\n"
    ).hexdigest()
    swaps = swap_after_capture(monkeypatch, kind, root, path, "regular", tmp_path / "outside")
    with pytest.raises(ReportError, match="site source pin bytes differ from captured source"):
        load_site_metadata(root, {"worklist": "interpro-pfam-duf-2026-10-05"}, source_pins=pins)
    assert swaps == [path]


@pytest.mark.parametrize("shared", [True, False])
@pytest.mark.parametrize("mode", ["regular", "symlink"])
def test_schema_description_and_download_use_same_confined_capture(adapter, tmp_path, monkeypatch, shared, mode):
    filename = "mech_shared.yaml" if shared else "dufmech.yaml"
    path = f"src/dufmech/schema/{filename}"
    original = b"title: Original captured schema\n"
    (adapter["root"] / path).write_bytes(original)
    adapter["pins"][path] = {"repository": REPOSITORY, "commit": "a" * 40,
                             "path": path, "sha256": hashlib.sha256(original).hexdigest()}
    reader = reviews.read_source_bytes
    captures = []

    def read_then_replace(root, relative):
        raw = reader(root, relative)
        if relative == path:
            captures.append(relative)
            replace_source(root / relative, mode, tmp_path / "outside-schema")
        return raw

    monkeypatch.setattr(reviews, "read_source_bytes", read_then_replace)
    _, provenance, copies = load(adapter)
    assert captures == [path]
    assert copies[f"schema/{filename}"].encode() == original
    if not shared:
        assert provenance["schema"]["document"]["title"] == "Original captured schema"


def test_missing_history_capture_never_falls_back_to_a_path_read(adapter):
    adapter["history_loader"].side_effect = None
    with pytest.raises(ReportError, match="missing validated site source capture"):
        load(adapter)


def test_missing_review_capture_never_falls_back_to_a_path_read(adapter, monkeypatch):
    path = "reports/yaml_record_review/missing-capture.md"
    monkeypatch.setattr(reviews, "load_review_metadata", Mock(return_value=[{"path": path}]))
    with pytest.raises(ReportError, match="missing validated site source capture"):
        load_review_site_metadata(adapter["root"], {"PF00001"}, source_pins={})


@pytest.fixture
def progress_publication(publication):
    root = publication
    overlay = root / "curation/families/PF04149.yaml"
    overlay.parent.mkdir(parents=True)
    overlay.write_text(yaml.safe_dump({
        "pfam_id": "PF04149", "curation_status": "IN_PROGRESS",
        "curation_history": "history/records/PF04149",
    }))
    history.new_history(
        root, kind="record", slug="PF04149", target_path="data/families/PF04149.yaml",
        timestamp="2026-10-07T00:50:00Z", summary="Opened fixture curation.",
        details="Inspected fixture identity without assessing a functional claim.",
        actor_name="Fixture curator", actor_type="human", event="EDIT", outcome="changed",
    )
    records.write_records(root, records.build_records(root), apply=True)
    return root


@pytest.fixture
def reviewed_publication(progress_publication):
    root = progress_publication
    payload = review_payload(root)
    payload["verdict"] = "PASS"
    report = legacy_review_fixture(root, payload)
    review_id = report.relative_to(root).as_posix()
    overlay = root / "curation/families/PF04149.yaml"
    curated = yaml.safe_load(overlay.read_text())
    curated.update(curation_status="REVIEWED", review_id=review_id)
    overlay.write_text(yaml.safe_dump(curated))
    event = history.new_history(
        root, kind="record", slug="PF04149", target_path="data/families/PF04149.yaml",
        timestamp="2026-10-07T01:02:00Z", summary="Reviewed fixture identity.",
        details="The scoped fixture review does not assert scientific characterization.",
        actor_name="Fixture reviewer", actor_type="human", event="REVIEW", outcome="no_change",
        urls=[reviews.review_report_url(review_id)],
    )
    records.write_records(root, records.build_records(root), apply=True)
    return {"root": root, "report": report, "event": event, "review_id": review_id}


@pytest.mark.parametrize("change,expected", [
    ("seed_only", "explicit PASS per-record review"),
    ("seed_only_with_other_pass", "explicit PASS per-record review"),
    ("missing_with_other_pass", "requires its captured review"),
    ("digest", "record content changed"),
    ("later_review_start", "canonical REVIEW event"),
    ("history_url", "canonical REVIEW event"),
    ("history_target", "canonical REVIEW event"),
])
@pytest.mark.parametrize("pinned", [True, False])
def test_reviewed_requalifies_exact_later_captures(reviewed_publication, monkeypatch, change, expected, pinned):
    root = reviewed_publication["root"]
    report, event = reviewed_publication["report"], reviewed_publication["event"]
    pins = publication_pins(root) if pinned else {}
    native_load = records.load_records

    def load_then_change(*args, **kwargs):
        result = native_load(*args, **kwargs)
        assert next(record for record in result if record["pfam_id"] == "PF04149")["curation_status"] == "REVIEWED"
        if change.startswith("history_"):
            value = yaml.safe_load(event.read_text())
            if change == "history_url":
                value.pop("links")
            else:
                value["target"]["path"] = "curation/families/PF04149.yaml"
            event.write_text(yaml.safe_dump(value))
        else:
            value = reviews.read_review(root, report)
            if change.endswith("with_other_pass"):
                report.with_name(report.stem + "-02.md").write_bytes(report.read_bytes())
            if change == "missing_with_other_pass":
                report.unlink()
            else:
                if change.startswith("seed_only"):
                    value["verdict"] = "SEED_ONLY"
                elif change == "digest":
                    value["context"]["record_digests"]["PF04149"] = "0" * 64
                else:
                    value["started_utc"] = "2026-10-07T01:03:00Z"
                report.write_text(reviews._render_report(value))
        if pinned:
            # Matching byte pins cannot turn a nonqualifying captured report into PASS.
            pins.update(publication_pins(root))
        return result

    monkeypatch.setattr(records, "load_records", load_then_change)
    with pytest.raises(ReportError, match=expected):
        load_site_metadata(root, {"worklist": "interpro-pfam-duf-2026-10-05"}, source_pins=pins)


@pytest.mark.parametrize("status", ["IN_PROGRESS", "REVIEWED"])
@pytest.mark.parametrize("pinned", [True, False])
def test_curation_history_pointer_uses_captured_target_not_only_event_index(
    request, monkeypatch, status, pinned,
):
    if status == "REVIEWED":
        root = request.getfixturevalue("reviewed_publication")["root"]
    else:
        root = request.getfixturevalue("progress_publication")
    pins = publication_pins(root) if pinned else {}
    native_load = records.load_records

    def load_then_retarget(*args, **kwargs):
        result = native_load(*args, **kwargs)
        record = next(item for item in result if item["pfam_id"] == "PF04149")
        assert record["curation_status"] == status
        for path in (root / "history/records/PF04149").glob("*.yaml"):
            value = yaml.safe_load(path.read_text())
            value["target"]["path"] = "data/worklists/interpro-pfam-duf-2026-10-05.json"
            path.write_text(yaml.safe_dump(value))
        assert history.project_curation_events(root, "PF04149") == record["curation_events"]
        if pinned:
            pins.update(publication_pins(root))
        return result

    monkeypatch.setattr(records, "load_records", load_then_retarget)
    with pytest.raises(ReportError, match="captured curation history is invalid.*actual canonical event"):
        load_site_metadata(root, {"worklist": "interpro-pfam-duf-2026-10-05"}, source_pins=pins)


@pytest.mark.parametrize("pinned", [True, False])
def test_reviewed_qualification_never_reopens_postcapture_artifacts(reviewed_publication, monkeypatch, pinned):
    root = reviewed_publication["root"]
    report, event = reviewed_publication["report"], reviewed_publication["event"]
    original_report, original_event = report.read_bytes(), event.read_bytes()
    pins = publication_pins(root) if pinned else {}
    native_load = reviews.load_review_metadata
    calls = []

    def capture_then_change(*args, **kwargs):
        result = native_load(*args, **kwargs)
        calls.append(kwargs["source_bytes"])
        value = reviews.read_review(root, report)
        value["verdict"] = "SEED_ONLY"
        report.write_text(reviews._render_report(value))
        value = yaml.safe_load(event.read_text())
        value.pop("links")
        event.write_text(yaml.safe_dump(value))
        return result

    monkeypatch.setattr(reviews, "load_review_metadata", capture_then_change)
    metadata, _, copies = load_site_metadata(
        root, {"worklist": "interpro-pfam-duf-2026-10-05"}, source_pins=pins,
    )
    assert len(calls) == 1
    assert metadata["PF04149"]["curation_status"] == "REVIEWED"
    reference = metadata["PF04149"]["reviews"][0]
    assert ": PASS by " in reference["label"]
    assert reference["scientific_review"] is False
    assert copies[f"source/{report.relative_to(root)}"].encode() == original_report
    assert copies[f"source/{event.relative_to(root)}"].encode() == original_event
