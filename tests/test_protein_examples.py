from __future__ import annotations

import copy
import json

import httpx
import pytest
from bs4 import BeautifulSoup

from dufmech.cross_mech import MechSource, SourceRecord
from dufmech.pages import render_site
from dufmech.protein_examples import (
    acquire,
    build_rows,
    digest,
    direct_family_candidates,
    load_snapshot,
    normalize_entry,
    read_registry,
    registry_candidates,
    sequence_valid,
    validate_rows,
    write_snapshot,
)
from tests.test_report import worklist_row


def entry(accession="P0A8M6", pfam="PF04363"):
    return {"primaryAccession": accession, "entryType": "UniProtKB reviewed (Swiss-Prot)",
            "entryAudit": {"sequenceVersion": 1},
            "sequence": {"value": "MACDEFGHIK", "length": 10},
            "organism": {"taxonId": 83333, "scientificName": "Escherichia coli"},
            "proteinDescription": {"recommendedName": {"fullName": {"value": "TmaR"}}},
            "uniProtKBCrossReferences": [{"database": "Pfam", "id": pfam}]}


def fixture_rows():
    families = [worklist_row(pfam, proteins=1) for pfam in ("PF04363", "PF00001", "PF00002")]
    candidate = {"pfam_id": "PF04363", "uniprot_accession": "P0A8M6",
                 "source_mech": "CellStructureMech", "source_record_id": "local:TmaR",
                 "source_path": "data/structures/tmar.yaml", "source_section": "proteins",
                 "link_basis": ["uniprot_pfam_xref"]}
    sources = {"CellStructureMech": {"commit": "a" * 40,
                                    "repository": "https://github.com/test/CellStructureMech"}}
    protein = normalize_entry(entry(), "2026_03")
    candidates = [candidate, copy.deepcopy(candidate),
                  {**candidate, "pfam_id": "PF00001"}]
    return families, candidates, sources, {"P0A8M6": protein}


def built():
    families, candidates, sources, entries = fixture_rows()
    registry = {"P0A8M6": entries["P0A8M6"]}
    return families, build_rows(families, candidates, sources, entries, registry, registry_source())


def registry_source():
    return {"commit": "a" * 40, "path": "data/grounding/protein_registry.jsonl",
            "repository": "https://github.com/test/ptm", "sha256": "b" * 64,
            "url": "https://github.com/test/ptm/blob/" + "a" * 40
                   + "/data/grounding/protein_registry.jsonl"}


def test_audit_accounts_for_all_families_and_does_not_promote_unmatched_claim():
    families, rows = built()
    validate_rows(rows, families)
    by_id = {r["pfam_id"]: r for r in rows}
    assert by_id["PF00002"]["status"] == "NO_SIBLING_CANDIDATE"
    assert by_id["PF00001"]["status"] == "UNRESOLVED_CANDIDATES"
    assert by_id["PF00001"]["unresolved"][0]["reason"] == "PFAM_NOT_IN_CURRENT_ENTRY"
    example = by_id["PF04363"]["examples"][0]
    assert example["sequence_origin"] == "PTM_REGISTRY_MIRROR"
    assert len(example["origins"]) == 1
    assert example["evidence_scope"] == "FAMILY_MEMBERSHIP_NOT_FUNCTION"


@pytest.mark.parametrize("accession,reason", [
    ("P0A8M6-2", "ISOFORM_OR_INVALID_ACCESSION"),
    ("P12345", "NO_EXACT_CURRENT_ENTRY"),
])
def test_missing_and_isoform_ids_never_resolve_by_prefix(accession, reason):
    families, candidates, sources, entries = fixture_rows()
    rows = build_rows(families, [{**candidates[0], "uniprot_accession": accession}],
                      sources, entries, {}, {})
    row = next(r for r in rows if r["pfam_id"] == "PF04363")
    assert row["examples"] == []
    assert row["unresolved"][0]["reason"] == reason


def test_registry_mismatch_is_not_called_a_mirror():
    families, candidates, sources, entries = fixture_rows()
    old = {**entries["P0A8M6"], "sequence_version": 2}
    rows = build_rows(families, candidates, sources, entries, {"P0A8M6": old}, registry_source())
    validate_rows(rows, families)
    example = next(r for r in rows if r["pfam_id"] == "PF04363")["examples"][0]
    assert example["sequence_origin"] == "UNIPROT_FETCH"
    assert example["registry_status"] == "DIFFERENT_SEQUENCE_OR_VERSION"


def test_unscanned_is_not_absence_and_merged_identifiers_need_review():
    families, candidates, sources, entries = fixture_rows()
    candidate = {**candidates[0], "cited_uniprot_accession": "P99999"}
    rows = build_rows(families, [candidate], sources, entries, {}, {},
                      unscanned={"PF00002"})
    validate_rows(rows, families)
    by_id = {row["pfam_id"]: row for row in rows}
    assert by_id["PF00002"]["status"] == "NOT_SCANNED"
    assert by_id["PF04363"]["examples"] == []
    assert by_id["PF04363"]["unresolved"][0]["reason"] == "RESOLVED_ACCESSION_REQUIRES_REVIEW"


@pytest.mark.parametrize("change", [
    {"sequence": "M-A"}, {"sequence_length": 9}, {"sequence_length": True},
    {"sequence_sha256": "0" * 64}, {"sequence_version": 0},
    {"sequence_version": True}, {"uniprot_release": "unknown"},
])
def test_sequence_validation_rejects_malformed_metadata(change):
    with pytest.raises(ValueError):
        sequence_valid({**normalize_entry(entry(), "2026_03"), **change})


def test_lookup_checkpoint_resumes_without_network_and_does_not_follow_secondary_ids(tmp_path):
    checkpoint = tmp_path / "lookups.jsonl"
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(200, json={"results": [entry()]},
                              headers={"x-uniprot-release": "2026_03"})

    ids = ["P0A8M6", "P12345", "P0A8M6-2"]
    rows = acquire(ids, checkpoint, transport=httpx.MockTransport(handler))
    assert len(calls) == 1
    assert rows["P12345"] is None
    assert rows["P0A8M6-2"] is None
    assert acquire(ids, checkpoint, offline=True) == rows
    assert len(calls) == 1
    with pytest.raises(ValueError, match="offline checkpoint"):
        acquire(["P99999"], checkpoint, offline=True)


def test_lookup_rejects_missing_release_pagination_and_malformed_results(tmp_path):
    for headers, payload, message in [
        ({}, {"results": []}, "no release"),
        ({"x-uniprot-release": "2026_03", "link": '<https://rest.uniprot.org/x>; rel="next"'},
         {"results": []}, "pagination"),
        ({"x-uniprot-release": "2026_03"}, {}, "lacks results"),
    ]:
        with pytest.raises((ValueError, TypeError), match=message):
            acquire(["P0A8M6"], tmp_path / "checkpoint", transport=httpx.MockTransport(
                lambda request, h=headers, p=payload: httpx.Response(200, headers=h, json=p)))
    assert not (tmp_path / "checkpoint").exists()


def test_lookup_rejects_release_drift_on_resume(tmp_path):
    checkpoint = tmp_path / "checkpoint"
    acquire(["P0A8M6"], checkpoint, transport=httpx.MockTransport(
        lambda request: httpx.Response(200, headers={"x-uniprot-release": "2026_03"},
                                      json={"results": [entry()]})))
    before = checkpoint.read_bytes()
    with pytest.raises(ValueError, match="release changed"):
        acquire(["P12345"], checkpoint, transport=httpx.MockTransport(
            lambda request: httpx.Response(200, headers={"x-uniprot-release": "2026_04"},
                                          json={"results": []})))
    assert checkpoint.read_bytes() == before


def test_lookup_never_appends_to_frozen_checkpoint(tmp_path):
    checkpoint = tmp_path / "staging.jsonl"
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(200, headers={"x-uniprot-release": "2026_03"},
                              json={"results": [entry()]})

    transport = httpx.MockTransport(handler)
    acquire(["P0A8M6"], checkpoint, transport=transport)
    families, rows = built()
    path = write_snapshot(rows, tmp_path / "frozen", families=families,
                          snapshot_date="2026-10-12", worklist_id="test",
                          source={"name": "fixture", "url": "https://example.org"},
                          checkpoint=checkpoint.read_bytes())
    retained = path.with_suffix(".queries.jsonl")
    before = retained.read_bytes()
    assert acquire(["P0A8M6"], retained, offline=True)["P0A8M6"]
    assert acquire(["P0A8M6"], retained, transport=transport)["P0A8M6"]
    with pytest.raises(ValueError, match="immutable snapshot"):
        acquire(["P0A8M6", "P12345"], retained, transport=transport)
    assert len(calls) == 1
    assert retained.read_bytes() == before
    assert load_snapshot(path, families, "test")[0] == rows


def test_lookup_rejects_symlinked_parent_before_network(tmp_path):
    real = tmp_path / "real"
    real.mkdir()
    link = tmp_path / "link"
    link.symlink_to(real, target_is_directory=True)
    with pytest.raises(ValueError, match="symlinks"):
        acquire(["P0A8M6"], link / "checkpoint.jsonl", transport=httpx.MockTransport(
            lambda request: pytest.fail("must not send a request")))
    assert not list(real.iterdir())


@pytest.mark.parametrize("bucket", ["examples", "unresolved"])
@pytest.mark.parametrize("change", [
    {"commit": "main"}, {"url": "https://example.org/blob/main/record.yaml"},
    {"path": "other.yaml"}, {"record_id": ""},
])
def test_provenance_validation_rejects_unpinned_or_inconsistent_origins(bucket, change):
    families, rows = built()
    candidate = next(r for r in rows if r[bucket])[bucket][0]
    candidate["origins"][0].update(change)
    with pytest.raises(ValueError, match="provenance"):
        validate_rows(rows, families)


@pytest.mark.parametrize("change", [
    {"sequence_origin": "UNVERIFIED"}, {"registry_status": "NOT_IN_REGISTRY"},
    {"registry_source": None},
])
def test_provenance_validation_rejects_unsupported_sequence_origin(change):
    families, rows = built()
    next(r for r in rows if r["examples"])["examples"][0].update(change)
    with pytest.raises((ValueError, TypeError), match="origin|provenance"):
        validate_rows(rows, families)


@pytest.mark.parametrize("change", [
    {"commit": "main"}, {"sha256": "unknown"}, {"sequence_sha256": "0" * 64},
    {"sequence_version": True}, {"uniprot_release": "unknown"},
    {"url": "https://example.org/registry"},
])
def test_provenance_validation_rejects_invalid_registry_proof(change):
    families, rows = built()
    next(r for r in rows if r["examples"])["examples"][0]["registry_source"].update(change)
    with pytest.raises(ValueError, match="provenance"):
        validate_rows(rows, families)


def test_snapshot_roundtrip_coverage_tamper_and_exclusive_publish(tmp_path):
    families, rows = built()
    kwargs = {"families": families, "snapshot_date": "2026-10-12", "worklist_id": "worklist-1",
              "source": {"name": "UniProt", "url": "https://rest.uniprot.org"}}
    path = write_snapshot(rows, tmp_path, checkpoint=b'{"fixture":true}\n', **kwargs)
    assert load_snapshot(path, families, "worklist-1")[0] == rows
    before = {p.name: p.read_bytes() for p in tmp_path.iterdir()}
    with pytest.raises(FileExistsError):
        write_snapshot(rows, tmp_path, **kwargs)
    assert before == {p.name: p.read_bytes() for p in tmp_path.iterdir()}
    with pytest.raises(ValueError, match="every worklist family"):
        validate_rows(rows[:-1], families)
    path.write_text("[]")
    with pytest.raises(Exception, match="sha256|bytes"):
        load_snapshot(path, families, "worklist-1")


def test_snapshot_rejects_symlink_output(tmp_path):
    families, rows = built()
    link = tmp_path / "link"
    link.symlink_to(tmp_path, target_is_directory=True)
    with pytest.raises(ValueError, match="symlink"):
        write_snapshot(rows, link / "child", families=families, snapshot_date="2026-10-12",
                       worklist_id="test", source={})


def test_snapshot_rejects_inflated_coverage_counts(tmp_path):
    families, rows = built()
    path = write_snapshot(rows, tmp_path, families=families, snapshot_date="2026-10-12",
                          worklist_id="test", source={"name": "fixture", "url": "https://example.org"})
    manifest = path.with_suffix(".manifest.json")
    data = json.loads(manifest.read_text())
    data["rows"]["proteins"] = 999
    manifest.write_text(json.dumps(data))
    with pytest.raises(ValueError, match="coverage differs"):
        load_snapshot(path, families, "test")


def test_registry_reads_pinned_blob_not_dirty_worktree(tmp_path, monkeypatch):
    protein = {**normalize_entry(entry(), "2026_03"), "protein_id": "UniProtKB:P0A8M6"}
    content = (json.dumps(protein) + "\n").encode()
    calls = []

    def show(args):
        calls.append(args)
        return content

    monkeypatch.setattr("dufmech.protein_examples.subprocess.check_output", show)
    registry, provenance = read_registry(tmp_path, {"commit": "a" * 40,
                                        "repository": "https://github.com/test/ptm"})
    assert calls[0][-1] == "a" * 40 + ":data/grounding/protein_registry.jsonl"
    assert provenance["sha256"] == digest(content)
    assert registry["P0A8M6"]["sequence"] == "MACDEFGHIK"


def test_direct_pfam_examples_keep_qualified_and_legacy_entries_without_classifications(
    tmp_path, monkeypatch,
):
    candidate = {"pfam_id": "PF04363", "source_mech": "ProteinTraitsMech",
                 "source_section": "trait_identifier", "source_record_id": "Pfam:PF04363",
                 "source_path": "data/traits/tmar.yaml"}
    calls = []
    record = SourceRecord(MechSource("proteintraitsmech", "data/traits"), "a" * 40,
                          candidate["source_path"], """identifier: Pfam:PF04363
canonical_examples:
- protein_id: UniProtKB:P0A8M6
  qualification_status: QUALIFIED
- protein_id: UniProtKB:P12345
""")

    def iterate(root, mech, **kwargs):
        calls.append(kwargs)
        return "a" * 40, iter([record])

    monkeypatch.setattr("dufmech.protein_examples.iter_mech_records", iterate)
    rows, scope = direct_family_candidates(tmp_path / "proteintraitsmech",
                                          {"commit": "a" * 40, "data_dir": "data/traits"},
                                          [candidate])
    assert calls == [{"ref": "a" * 40, "paths": {"data/traits/tmar.yaml"}}]
    assert [r["uniprot_accession"] for r in rows] == ["P0A8M6", "P12345"]
    assert scope["qualification_statuses"] == {"QUALIFIED": 1, "LEGACY_OR_UNSPECIFIED": 1}


def test_direct_source_adds_qualification_without_duplicate_origins():
    families, candidates, sources, entries = fixture_rows()
    direct = {**candidates[0], "qualification_status": "QUALIFIED",
              "link_basis": ["ptm_own_pfam_record_example"]}
    rows = build_rows(families, candidates + [direct], sources, entries, {}, {})
    example = next(r for r in rows if r["pfam_id"] == "PF04363")["examples"][0]
    assert len(example["origins"]) == 1
    assert example["origins"][0]["qualification_status"] == "QUALIFIED"
    assert set(example["origins"][0]["link_basis"]) == {
        "ptm_own_pfam_record_example", "uniprot_pfam_xref"}


def test_registry_discovery_finds_unlinked_carriers_and_accounts_for_missing_entries():
    families, _, _, entries = fixture_rows()
    entries["P12345"] = normalize_entry(entry("P12345", "PF99999"), "2026_03")
    rows, scope = registry_candidates(
        {"P0A8M6": {}, "P12345": {}, "Q99999": {}}, entries, families)
    assert len(rows) == 1
    assert rows[0]["pfam_id"] == "PF04363"
    assert rows[0]["qualification_status"] == "NOT_ASSESSED_FOR_THIS_FAMILY"
    assert scope == {"proteins_checked": 3, "family_protein_pairs": 1,
                     "no_exact_current_entry": ["Q99999"], "without_target_family_count": 1}


def test_site_retains_sequence_and_fasta_without_claiming_function(tmp_path):
    families, rows = built()
    render_site(families, [], input_ids={}, out_dir=tmp_path, protein_examples=rows)
    html = BeautifulSoup((tmp_path / "families/PF04363.html").read_text(), "html.parser")
    section = html.select_one("#protein-examples")
    assert "TmaR" in section.get_text()
    assert "not functional evidence" in section.get_text()
    assert section.select_one('a[href="PF04363.fasta"]')
    assert "MACDEFGHIK" in (tmp_path / "families/PF04363.fasta").read_text()
    payload = json.loads((tmp_path / "families/PF04363.json").read_text())
    assert payload["protein_examples"]["examples"][0]["sequence_sha256"] == digest(b"MACDEFGHIK")
    gap = BeautifulSoup((tmp_path / "families/PF00002.html").read_text(), "html.parser")
    assert "No sibling protein candidate" in gap.select_one("#protein-examples").get_text()
