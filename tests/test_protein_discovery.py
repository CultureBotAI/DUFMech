from __future__ import annotations

import copy
import json
import os

import httpx
import pytest
from bs4 import BeautifulSoup

from dufmech.protein_discovery import (
    DIRECT_STEM,
    discover,
    enrich_rows,
    freeze_discovery,
    parse_checkpoint,
    query_settings,
    query_url,
    validate_observation,
)
from dufmech.protein_examples import (
    digest,
    latest_protein_snapshot,
    load_snapshot,
    validate_rows,
    write_snapshot,
)
from dufmech.report import ReportError
from dufmech.site import protein_examples_section
from tests.test_protein_examples import built, entry


def observation(pfam="PF00002", *, empty=False):
    settings = query_settings()
    return {"pfam_id": pfam, "settings": settings, "url": query_url(pfam, settings),
            "fetched_at": "2026-10-13T03:00:00+00:00", "release": "2026_03",
            "total": 0 if empty else 1,
            "results": [] if empty else [{**entry(pfam=pfam), "annotationScore": 5}]}


def transport(*, empty=False, release="2026_03", calls=None):
    def handler(request):
        if calls is not None:
            calls.append(request)
        pfam = request.url.params["query"].removeprefix("xref:pfam-")
        row = observation(pfam, empty=empty)
        return httpx.Response(200, json={"results": row["results"]},
                              headers={"x-uniprot-release": release,
                                       "x-total-results": str(row["total"])})
    return httpx.MockTransport(handler)


def test_full_sequences_and_empty_searches_are_distinct_from_failures(tmp_path):
    calls = []
    checkpoint = tmp_path / "queries.jsonl"
    rows = discover({"PF00001", "PF00002"}, checkpoint, workers=2,
                    transport=transport(calls=calls))
    assert len(calls) == 2
    assert all("sequence_version" in request.url.params["fields"] for request in calls)
    before = checkpoint.read_bytes()
    assert discover(set(rows), checkpoint, offline=True) == rows
    assert checkpoint.read_bytes() == before
    assert len(calls) == 2
    empty = discover({"PF00003"}, tmp_path / "empty", transport=transport(empty=True))
    assert empty["PF00003"]["total"] == 0
    with pytest.raises(ValueError, match="lacks 1 families"):
        discover({*rows, "PF00003"}, checkpoint, offline=True)


@pytest.mark.parametrize("change", [
    {"release": ""}, {"release": "2026"}, {"total": None}, {"total": True},
    {"total": -1}, {"total": 10}, {"results": []}, {"results": None},
    {"url": "https://untrusted.example/search"}, {"pfam_id": "PF00003"},
    {"fetched_at": "2026-10-13T03:00:00"},
])
def test_malformed_observation_is_not_accepted(change):
    with pytest.raises((ValueError, TypeError)):
        validate_observation({**observation(), **change}, query_settings())


@pytest.mark.parametrize("change", [
    {"annotationScore": None}, {"annotationScore": True}, {"annotationScore": 6},
    {"annotationScore": float("nan")}, {"annotationScore": float("inf")},
    {"primaryAccession": "P0A8M6-2"}, {"entryAudit": {}},
    {"sequence": {"value": "MA-X", "length": 4}},
    {"uniProtKBCrossReferences": [{"database": "Pfam", "id": "PF99999"}]},
])
def test_invalid_sequence_or_membership_fails_closed(change):
    row = observation()
    row["results"][0].update(change)
    with pytest.raises((ValueError, TypeError)):
        validate_observation(row, query_settings())


def test_checkpoint_rejects_torn_duplicate_mixed_or_changed_contracts(tmp_path):
    row = observation()
    line = json.dumps(row) + "\n"
    settings = query_settings()
    for content in (line.rstrip(), line + line,
                    line + json.dumps({**observation("PF00003"), "release": "2026_04"}) + "\n"):
        with pytest.raises(ValueError):
            parse_checkpoint(content, settings)
    with pytest.raises(ValueError, match="contract"):
        parse_checkpoint(line, query_settings(1))
    checkpoint = tmp_path / "queries.jsonl"
    checkpoint.write_text(line)
    with pytest.raises(ValueError, match="outside"):
        discover({"PF00003"}, checkpoint, transport=transport())
    assert checkpoint.read_text() == line


def test_response_order_and_duplicate_primary_ids_are_checked():
    row = observation()
    row["results"] *= 2
    row["total"] = 2
    with pytest.raises(ValueError, match="ranked"):
        validate_observation(row, query_settings())
    row["results"] = [{**entry("P99999", "PF00002"), "annotationScore": 5},
                      {**entry("P0A8M6", "PF00002"), "annotationScore": 5}]
    with pytest.raises(ValueError, match="ranked"):
        validate_observation(row, query_settings())


def test_frozen_checkpoint_cannot_be_extended_and_release_drift_cannot_append(tmp_path):
    checkpoint = tmp_path / "queries.jsonl"
    discover({"PF00001"}, checkpoint, transport=transport())
    before = checkpoint.read_bytes()
    with pytest.raises(ValueError, match="release changed"):
        discover({"PF00001", "PF00002"}, checkpoint, transport=transport(release="2026_04"))
    assert checkpoint.read_bytes() == before
    manifest = tmp_path / "snapshot.manifest.json"
    manifest.write_text(json.dumps({"files": {"queries": {"path": checkpoint.name}}}))
    with pytest.raises(ValueError, match="immutable"):
        discover({"PF00001", "PF00002"}, checkpoint, transport=transport())
    assert checkpoint.read_bytes() == before
    assert discover({"PF00001"}, checkpoint, offline=True)


def test_bad_response_and_http_errors_never_become_empty_families(tmp_path):
    for index, response in enumerate([
        httpx.Response(400, json={"results": []}),
        httpx.Response(200, json={"results": []},
                       headers={"x-uniprot-release": "2026_03", "x-total-results": "99"}),
        httpx.Response(200, json={"results": []}, headers={"x-total-results": "0"}),
        httpx.Response(200, json={"results": []}, headers={"x-uniprot-release": "2026_03"}),
    ]):
        checkpoint = tmp_path / f"bad-{index}"
        with pytest.raises((ValueError, RuntimeError)):
            discover({"PF00002"}, checkpoint,
                     transport=httpx.MockTransport(lambda request, result=response: result))
        assert checkpoint.read_bytes() == b""


def test_symlink_checkpoint_and_parent_are_rejected(tmp_path):
    target = tmp_path / "target"
    target.mkdir()
    alias = tmp_path / "alias"
    alias.symlink_to(target, target_is_directory=True)
    with pytest.raises(ValueError, match="symlink"):
        discover({"PF00002"}, alias / "queries", transport=transport())
    checkpoint = target / "checkpoint"
    checkpoint.write_text("")
    alias_file = tmp_path / "queries"
    alias_file.symlink_to(checkpoint)
    with pytest.raises(ValueError, match="symlink"):
        discover({"PF00002"}, alias_file, offline=True)


def test_hard_link_alias_cannot_mutate_a_retained_checkpoint(tmp_path):
    checkpoint = tmp_path / "checkpoint"
    checkpoint.write_text(json.dumps(observation()) + "\n")
    alias = tmp_path / "alias"
    os.link(checkpoint, alias)
    before = checkpoint.read_bytes()
    with pytest.raises(ValueError, match="hard-link"):
        discover({"PF00002", "PF00003"}, alias, transport=transport())
    assert checkpoint.read_bytes() == before


def test_checkpoint_linked_during_request_is_not_appended(tmp_path):
    checkpoint = tmp_path / "checkpoint"
    checkpoint.write_text(json.dumps(observation()) + "\n")
    retained = tmp_path / "retained.jsonl"
    before = checkpoint.read_bytes()

    def handler(request):
        os.link(checkpoint, retained)
        row = observation("PF00003")
        return httpx.Response(200, json={"results": row["results"]},
                              headers={"x-uniprot-release": "2026_03", "x-total-results": "1"})

    with pytest.raises(ValueError, match="hard-link"):
        discover({"PF00002", "PF00003"}, checkpoint, transport=httpx.MockTransport(handler))
    assert retained.read_bytes() == before
    assert checkpoint.read_bytes() == before


@pytest.mark.parametrize("field,value", [("sequence_version", 2), ("sequence", "AAAAAAAAAA")])
def test_same_release_protein_cannot_have_conflicting_sequences(field, value):
    families, parent = built()
    rows = enrich_rows(parent, {"PF00002": observation()})
    direct = next(row for row in rows if row["pfam_id"] == "PF00002")
    example = direct["examples"][0]
    example[field] = value
    example["sequence_sha256"] = digest(example["sequence"].encode())
    with pytest.raises(ValueError, match="conflicting sequence"):
        validate_rows(rows, families)


def test_same_protein_may_change_between_releases():
    families, parent = built()
    row = observation()
    row["release"] = "2026_04"
    row["results"][0]["entryAudit"]["sequenceVersion"] = 2
    rows = enrich_rows(parent, {"PF00002": row})
    validate_rows(rows, families)


def test_conflicting_raw_responses_cannot_be_frozen(tmp_path):
    families, parent = built()
    path = write_snapshot(parent, tmp_path, families=families, snapshot_date="2026-10-13",
                          worklist_id="test-worklist",
                          source={"name": "fixture", "url": "https://rest.uniprot.org"})
    row = observation()
    row["results"][0]["entryAudit"]["sequenceVersion"] = 2
    checkpoint = tmp_path / "staging.jsonl"
    checkpoint.write_text(json.dumps(row) + "\n")
    with pytest.raises(ValueError, match="conflicting sequence"):
        freeze_discovery(path, checkpoint, tmp_path, families=families,
                         worklist_id="test-worklist", snapshot_date="2026-10-13")
    assert not list(tmp_path.glob(f"{DIRECT_STEM}*"))


def test_independent_direct_queries_must_agree_on_same_release_sequence():
    families, parent = built()
    empty = next(row for row in parent if row["pfam_id"] == "PF00001")
    empty.update(status="NO_SIBLING_CANDIDATE", candidate_count=0, unresolved=[])
    first, second = observation("PF00001"), observation("PF00002")
    second["results"][0]["entryAudit"]["sequenceVersion"] = 2
    rows = enrich_rows(parent, {"PF00001": first, "PF00002": second})
    with pytest.raises(ValueError, match="conflicting sequence"):
        validate_rows(rows, families)


@pytest.mark.parametrize("change", ["manifest", "replace", "symlink", "append", "parent"])
def test_checkpoint_changed_during_request_is_preserved(tmp_path, change):
    directory = tmp_path / "staging"
    directory.mkdir()
    checkpoint = directory / "checkpoint"
    before = json.dumps(observation()) + "\n"
    checkpoint.write_text(before)
    replacement = "replacement data\n"

    def handler(request):
        if change == "manifest":
            (directory / "new.manifest.json").write_text(
                json.dumps({"files": {"queries": {"path": checkpoint.name}}}))
        elif change == "append":
            checkpoint.write_text(before + replacement)
        elif change == "parent":
            directory.rename(tmp_path / "retained")
            directory.mkdir()
            checkpoint.write_text(replacement)
        else:
            checkpoint.rename(directory / "retained")
            if change == "replace":
                checkpoint.write_text(replacement)
            else:
                checkpoint.symlink_to(directory / "retained")
        row = observation("PF00003")
        return httpx.Response(200, json={"results": row["results"]},
                              headers={"x-uniprot-release": "2026_03", "x-total-results": "1"})

    with pytest.raises((ValueError, ReportError)):
        discover({"PF00002", "PF00003"}, checkpoint, transport=httpx.MockTransport(handler))
    if change == "parent":
        assert (tmp_path / "retained/checkpoint").read_text() == before
    elif change in {"replace", "symlink"}:
        assert (directory / "retained").read_text() == before
    assert checkpoint.read_text() == (replacement if change in {"replace", "parent"} else
                                     before + replacement if change == "append" else before)


def test_nonregular_checkpoint_is_rejected_without_blocking(tmp_path):
    checkpoint = tmp_path / "fifo"
    os.mkfifo(checkpoint)
    with pytest.raises(ValueError, match="regular file"):
        discover({"PF00002"}, checkpoint, transport=transport())


@pytest.mark.parametrize("workers,per_family", [(0, 3), (5, 3), (True, 3), (2, 0), (2, 26), (2, True)])
def test_invalid_scope_is_rejected_before_requests(tmp_path, workers, per_family):
    calls = []
    with pytest.raises((ValueError, TypeError)):
        discover({"PF00002"}, tmp_path / "queries", workers=workers, per_family=per_family,
                 transport=transport(calls=calls))
    assert calls == []


@pytest.mark.parametrize("empty", [False, True])
def test_enrichment_preserves_covered_and_rejected_rows(empty):
    families, parent = built()
    before = copy.deepcopy(parent)
    rows = enrich_rows(parent, {"PF00002": observation(empty=empty)})
    validate_rows(rows, families)
    assert parent == before
    assert [r for r in rows if r["pfam_id"] != "PF00002"] == [
        r for r in parent if r["pfam_id"] != "PF00002"]
    direct = next(r for r in rows if r["pfam_id"] == "PF00002")
    assert direct["status"] == ("NO_UNIPROT_MEMBERS" if empty else "HAS_SEQUENCE_EXAMPLE")
    html = BeautifulSoup(protein_examples_section(direct), "html.parser")
    assert "sibling references" not in html.get_text()
    assert "not a representative or reviewed-only sample" in html.get_text()
    if empty:
        assert "zero members" in html.get_text()
    else:
        assert direct["examples"][0]["registry_status"] == "NOT_CHECKED"
        assert html.find("a", string="UniProt family search, rank 1")
    with pytest.raises(ValueError, match="exactly"):
        enrich_rows(parent, {})


@pytest.mark.parametrize("field,value", [
    ("rank", 2), ("rank", True), ("kind", "SIBLING_RECORD"), ("annotation_score", True),
    ("url", "https://uniprot.org"), ("fetched_at", "2026-10-14T00:00:00Z"),
    ("uniprot_release", "2026_04"),
])
def test_direct_origin_tampering_is_rejected(field, value):
    families, parent = built()
    rows = enrich_rows(parent, {"PF00002": observation()})
    direct = next(r for r in rows if r["pfam_id"] == "PF00002")
    direct["examples"][0]["origins"][0][field] = value
    with pytest.raises(ValueError):
        validate_rows(rows, families)


def test_only_direct_rows_can_claim_unchecked_registry():
    families, rows = built()
    example = next(r for r in rows if r["examples"])["examples"][0]
    example.update(registry_status="NOT_CHECKED", sequence_origin="UNIPROT_FETCH")
    with pytest.raises(ValueError, match="direct query"):
        validate_rows(rows, families)


def test_sibling_origin_cannot_masquerade_as_a_direct_query():
    families, rows = built()
    example = next(r for r in rows if r["examples"])["examples"][0]
    example["origins"][0]["kind"] = "UNIPROT_FAMILY_SEARCH"
    with pytest.raises(ValueError, match="requires direct discovery"):
        validate_rows(rows, families)


def frozen(tmp_path):
    families, parent = built()
    path = write_snapshot(parent, tmp_path, families=families, snapshot_date="2026-10-13",
                          worklist_id="test-worklist",
                          source={"name": "test UniProt fixture", "url": "https://rest.uniprot.org"})
    checkpoint = tmp_path / "staging.jsonl"
    checkpoint.write_text(json.dumps(observation()) + "\n")
    direct = freeze_discovery(path, checkpoint, tmp_path, families=families,
                              worklist_id="test-worklist", snapshot_date="2026-10-13")
    return families, path, direct, checkpoint


def test_frozen_snapshot_replays_and_latest_prefers_same_day_successor(tmp_path):
    families, parent, direct, checkpoint = frozen(tmp_path)
    _, manifest = load_snapshot(direct, families, "test-worklist")
    assert manifest["source"]["families_queried"] == 1
    assert manifest["source"]["parent"]["sha256"] == digest(parent.read_bytes())
    assert latest_protein_snapshot(tmp_path) == direct
    with pytest.raises(FileExistsError):
        freeze_discovery(parent, checkpoint, tmp_path, families=families,
                         worklist_id="test-worklist", snapshot_date="2026-10-13")
    later = tmp_path / "replay"
    later.mkdir()
    for path in tmp_path.glob(f"{parent.stem}.*"):
        (later / path.name).write_bytes(path.read_bytes())
    replay = freeze_discovery(parent, checkpoint, later, families=families,
                              worklist_id="test-worklist", snapshot_date="2026-10-13")
    assert replay.read_bytes() == direct.read_bytes()
    assert replay.with_suffix(".tsv").read_bytes() == direct.with_suffix(".tsv").read_bytes()


def test_raw_derivation_detects_rehashed_tampering(tmp_path):
    families, _parent, direct, _checkpoint = frozen(tmp_path)
    data = json.loads(direct.read_text())
    row = next(r for r in data if r["pfam_id"] == "PF00002")
    row["examples"][0]["protein_name"] = "unjustified change"
    direct.write_text(json.dumps(data))
    manifest_path = direct.with_suffix(".manifest.json")
    manifest = json.loads(manifest_path.read_text())
    manifest["files"]["json"].update(sha256=digest(direct.read_bytes()), bytes=direct.stat().st_size)
    manifest_path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match="reproduce"):
        load_snapshot(direct, families, "test-worklist")


def test_parent_pin_cannot_be_changed_or_traverse_directories(tmp_path):
    families, _parent, direct, _checkpoint = frozen(tmp_path)
    manifest_path = direct.with_suffix(".manifest.json")
    manifest = json.loads(manifest_path.read_text())
    for change in ({"sha256": "0" * 64}, {"path": "../outside.json"}):
        updated = copy.deepcopy(manifest)
        updated["source"]["parent"].update(change)
        manifest_path.write_text(json.dumps(updated))
        with pytest.raises(ValueError):
            load_snapshot(direct, families, "test-worklist")


def test_selector_ignores_auxiliaries_and_uses_dates_before_kind(tmp_path):
    assert latest_protein_snapshot(tmp_path) is None
    old = tmp_path / f"{DIRECT_STEM}-2026-10-13.json"
    old.touch()
    (tmp_path / f"{DIRECT_STEM}-2026-10-14.manifest.json").touch()
    invalid = tmp_path / f"{DIRECT_STEM}-2026-13-99.json"
    invalid.touch()
    with pytest.raises(ReportError, match="invalid snapshot date"):
        latest_protein_snapshot(tmp_path)
    invalid.unlink()
    assert latest_protein_snapshot(tmp_path) == old
    newer = tmp_path / "duf-protein-examples-2026-10-14.json"
    newer.touch()
    assert latest_protein_snapshot(tmp_path) == newer


def test_pages_retain_parent_and_raw_queries_for_portable_replay(tmp_path, monkeypatch):
    from dufmech.pages import render_from_paths

    inputs = tmp_path / "inputs"
    inputs.mkdir()
    families, parent, direct, _checkpoint = frozen(inputs)
    monkeypatch.setattr("dufmech.pages.load_latest_rows",
                        lambda *a, **kw: (families, [], {"worklist": "test-worklist"}))
    monkeypatch.setattr("dufmech.pages.tracked_source", lambda *a, **kw: {})
    out = tmp_path / "site"
    render_from_paths(out_dir=out, worklists_dir=inputs,
                      worklist_json=inputs / "worklist.json", protein_examples_json=direct,
                      cross_mech_dir=inputs / "no-cross")
    for path in inputs.glob("duf-protein-examples*.*"):
        assert (out / "datasets" / path.name).read_bytes() == path.read_bytes()
    copied, _ = load_snapshot(out / "datasets" / direct.name, families, "test-worklist")
    row = next(r for r in copied if r["pfam_id"] == "PF00002")
    payload = json.loads((out / "families/PF00002.json").read_text())
    assert payload["protein_examples"] == row
    assert "MACDEFGHIK" in (out / "families/PF00002.fasta").read_text()
    assert (out / "datasets" / parent.name).exists()


def test_failed_derivation_rolls_back_only_new_snapshot(tmp_path):
    families, _parent, direct, _checkpoint = frozen(tmp_path)
    rows, manifest = load_snapshot(direct, families, "test-worklist")
    before = {path.name: path.read_bytes() for path in tmp_path.iterdir()}
    source = copy.deepcopy(manifest["source"])
    source["parent"]["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="parent checksum"):
        write_snapshot(rows, tmp_path, families=families, snapshot_date="2026-10-14",
                       worklist_id="test-worklist", source=source, stem=DIRECT_STEM,
                       checkpoint=direct.with_suffix(".queries.jsonl").read_bytes())
    assert {path.name: path.read_bytes() for path in tmp_path.iterdir()} == before
