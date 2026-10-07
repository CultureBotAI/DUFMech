from __future__ import annotations

import json
from pathlib import Path

import httpx
import pytest

from dufmech.example_candidates import (
    PROTEIN_TRAITS_GAP,
    TRAITMECH_NAMED,
    TRAITMECH_RENAMED,
    ExampleCandidateError,
    UniProtExampleClient,
    candidate_row,
    select_target_families,
)
from dufmech.example_candidates_snapshot import write_example_candidates_snapshot
from dufmech.provenance import check_manifest


def _cross(pfam, mech, section, accession="", mentioned=None):
    return {
        "pfam_id": pfam, "source_mech": mech, "source_section": section,
        "uniprot_accession": accession, "family_mentioned_in_record": mentioned,
    }


CROSS_ROWS = [
    # TraitMech names PF00001 without a protein: a target.
    _cross("PF00001", "TraitMech", "record_text"),
    # TraitMech names PF00002 and cites a protein carrying it: not a target.
    _cross("PF00002", "TraitMech", "record_text"),
    _cross("PF00002", "TraitMech", "uniprot_accession", "P11111", False),
    # TraitMech names PF00003; ProteinTraitsMech has an example carrying it: not a target.
    _cross("PF00003", "TraitMech", "record_text"),
    _cross("PF00003", "ProteinTraitsMech", "canonical_examples", "P22222", False),
    _cross("PF00003", "ProteinTraitsMech", "trait_identifier"),
    _cross("PF00003", "ProteinTraitsMech", "canonical_examples", "P22223", True),
    # ProteinTraitsMech trait record with examples that never carry the family: a gap.
    _cross("PF00004", "ProteinTraitsMech", "trait_identifier"),
    _cross("PF00004", "ProteinTraitsMech", "canonical_examples", "P33333", False),
    # Unlisted names have no Pfam ID and are never targets.
    _cross("", "TraitMech", "record_text"),
]


def test_select_target_families_reasons() -> None:
    targets = select_target_families(CROSS_ROWS, renamed_traitmech_families=["PF14337", "PF00001"])
    assert targets == {
        "PF00001": {TRAITMECH_NAMED, TRAITMECH_RENAMED},
        "PF00004": {PROTEIN_TRAITS_GAP},
        "PF14337": {TRAITMECH_RENAMED},
    }


def _entry(accession, *, reviewed=False, score=1.0, length=100):
    return {
        "primaryAccession": accession,
        "entryType": "UniProtKB reviewed (Swiss-Prot)" if reviewed else "UniProtKB unreviewed (TrEMBL)",
        "annotationScore": score,
        "proteinDescription": {"recommendedName": {"fullName": {"value": f"Protein {accession}"}}},
        "organism": {"taxonId": 562, "scientificName": "Escherichia coli"},
        "sequence": {"length": length},
    }


def test_candidate_row_normalizes_entry() -> None:
    row = candidate_row(_entry("P0A8M6", reviewed=True, score=5.0), "PF04363", 1, 40, ["x"])
    assert row is not None
    assert (row.reviewed, row.annotation_score, row.length) == (True, 5.0, 100)
    assert row.taxon_id == "NCBITaxon:562"
    assert row.tsv_row()["reviewed"] == "true"
    assert candidate_row({}, "PF04363", 1, 40, ["x"]) is None


def test_client_queries_each_family_and_retries_transient_errors() -> None:
    calls: list[httpx.URL] = []
    sleeps: list[float] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.url)
        query = request.url.params["query"]
        assert request.url.params["sort"] == "annotation_score desc,accession asc"
        assert request.url.params["size"] == "2"
        if query == "xref:pfam-PF00001" and len(calls) == 1:
            return httpx.Response(503)
        headers = {"X-Total-Results": "7", "X-UniProt-Release": "2026_03"}
        if query == "xref:pfam-PF00004":
            return httpx.Response(200, json={"results": []}, headers=headers)
        return httpx.Response(
            200,
            json={"results": [_entry("A1", reviewed=True, score=5.0), _entry("A2")]},
            headers=headers,
        )

    client = UniProtExampleClient(
        per_family=2, transport=httpx.MockTransport(handler), sleep=sleeps.append
    )
    run = client.collect({"PF00004": {PROTEIN_TRAITS_GAP}, "PF00001": {TRAITMECH_NAMED}})

    assert sleeps == [2.0]
    assert run.families_queried == 2
    assert run.families_without_members == ["PF00004"]
    assert run.uniprot_releases == {"2026_03"}
    assert [(row.pfam_id, row.rank, row.uniprot_accession) for row in run.rows] == [
        ("PF00001", 1, "A1"),
        ("PF00001", 2, "A2"),
    ]
    assert run.rows[0].family_members == 7


def test_client_gives_up_after_retries() -> None:
    client = UniProtExampleClient(
        transport=httpx.MockTransport(lambda _: httpx.Response(503)),
        retries=1,
        sleep=lambda _: None,
    )
    with pytest.raises(ExampleCandidateError):
        client.collect({"PF00001": {TRAITMECH_NAMED}})


def test_snapshot_manifest_validates_and_is_exclusive(tmp_path: Path) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={"results": [_entry("A1", reviewed=True, score=5.0)]},
            headers={"X-Total-Results": "1", "X-UniProt-Release": "2026_03"},
        )

    targets = {"PF00001": {TRAITMECH_NAMED}}
    run = UniProtExampleClient(transport=httpx.MockTransport(handler)).collect(targets)
    out = tmp_path / "worklists"
    manifest = write_example_candidates_snapshot(
        run, targets, out, per_family=3,
        input_snapshot_ids={"worklist": "w", "cross_mech": "c"}, snapshot_date="2026-10-07",
    )
    path = out / "uniprot-duf-example-candidates-2026-10-07.manifest.json"
    assert check_manifest(path) == []
    assert manifest["rows"]["families_with_reviewed_candidate"] == 1
    assert manifest["targets"]["by_reason"] == {TRAITMECH_NAMED: 1}
    rows = json.loads((out / "uniprot-duf-example-candidates-2026-10-07.json").read_text("utf-8"))
    assert rows[0]["selection_reasons"] == [TRAITMECH_NAMED]
    with pytest.raises(FileExistsError):
        write_example_candidates_snapshot(
            run, targets, out, per_family=3, input_snapshot_ids={}, snapshot_date="2026-10-07"
        )


def test_checkpoint_resumes_without_requerying(tmp_path: Path) -> None:
    calls: list[str] = []
    fail_on = {"PF00004"}

    def handler(request: httpx.Request) -> httpx.Response:
        pfam = request.url.params["query"].removeprefix("xref:pfam-")
        calls.append(pfam)
        if pfam in fail_on:
            return httpx.Response(400)
        return httpx.Response(
            200,
            json={"results": [_entry(f"A{pfam[-1]}")]},
            headers={"X-Total-Results": "1", "X-UniProt-Release": "2026_03"},
        )

    targets = {"PF00001": {TRAITMECH_NAMED}, "PF00004": {PROTEIN_TRAITS_GAP}}
    checkpoint = tmp_path / "raw" / "checkpoint.jsonl"
    client = UniProtExampleClient(transport=httpx.MockTransport(handler), sleep=lambda _: None)

    with pytest.raises(ExampleCandidateError):
        client.collect(targets, checkpoint=checkpoint)
    assert calls == ["PF00001", "PF00004"]
    # A torn final line from a crash is tolerated.
    checkpoint.write_text(checkpoint.read_text() + '{"pfam_id": "PF0', encoding="utf-8")

    fail_on.clear()
    run = client.collect(targets, checkpoint=checkpoint)
    assert calls == ["PF00001", "PF00004", "PF00004"]
    assert [row.uniprot_accession for row in run.rows] == ["A1", "A4"]

    # A different per_family setting does not reuse the checkpoint.
    other = UniProtExampleClient(
        per_family=2, transport=httpx.MockTransport(handler), sleep=lambda _: None
    )
    other.collect(targets, checkpoint=checkpoint)
    assert calls[-2:] == ["PF00001", "PF00004"]
