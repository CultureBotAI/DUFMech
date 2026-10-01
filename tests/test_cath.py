from __future__ import annotations

import csv
import json
from io import StringIO

import httpx

from dufmech.cath import (
    CathClient,
    CathClientError,
    collect_cath_rows,
    render_cath_json,
    render_cath_tsv,
)


def cath_payload() -> dict:
    return {
        "data": [
            {
                "uniprot_acc": "P68871",
                "member_id": "P68871/2-147",
                "sequence_md5": "209d686939d0b8d1ea089368150140e2",
                "uni_start": None,
                "taxon_division_id": "5",
                "taxon_division_name": "Primates",
                "superfamily_id": "1.10.490.10",
                "funfam_number": "1",
                "confidence": "1",
                "taxon_id": "9606",
                "species_name": "Homo sapiens",
                "description": "Hemoglobin subunit beta",
                "gene_id": "HBB_HUMAN",
                "gene_name": "HBB",
            },
            {
                "uniprot_acc": "P68871",
                "member_id": "P68873/2-147",
                "sequence_md5": "209d686939d0b8d1ea089368150140e2",
                "taxon_division_id": "5",
                "taxon_division_name": "Primates",
                "superfamily_id": "1.10.490.10",
                "funfam_number": "1",
                "confidence": "1",
                "taxon_id": "9606",
                "species_name": "Homo sapiens",
                "description": "Hemoglobin subunit beta",
                "gene_id": "HBB_HUMAN",
                "gene_name": "HBB",
            },
        ],
        "total_records": 2,
        "query": {"cath_version": "v4_4_0", "uniprot_acc": "P68871"},
    }


def test_cath_client_fetches_and_normalizes_funfams() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path.endswith("/v4_4_0/api/rest/uniprot_to_funfam/P68871")
        assert request.url.params["content-type"] == "application/json"
        return httpx.Response(200, json=cath_payload())

    rows = collect_cath_rows(
        ["P68871", "P68871"],
        CathClient(transport=httpx.MockTransport(handler)),
    )

    assert len(rows) == 2
    assert rows[0].uniprot_accession == "P68871"
    assert rows[0].cath_uniprot_accession == "P68871"
    assert rows[0].member_id == "P68871/2-147"
    assert rows[0].member_accession == "P68871"
    assert rows[0].member_start == 2
    assert rows[0].member_end == 147
    assert rows[0].uniprot_start is None
    assert rows[0].superfamily_id == "1.10.490.10"
    assert rows[0].funfam_number == "1"
    assert rows[0].confidence == "1"
    assert rows[0].taxon_id == "9606"
    assert rows[0].source_url.endswith("/P68871")


def test_cath_404_is_no_evidence() -> None:
    rows = collect_cath_rows(
        ["MISSING"],
        CathClient(transport=httpx.MockTransport(lambda request: httpx.Response(404))),
    )

    assert rows == []


def test_cath_client_raises_on_http_failure() -> None:
    client = CathClient(transport=httpx.MockTransport(lambda request: httpx.Response(500)))

    try:
        collect_cath_rows(["P68871"], client)
    except CathClientError as exc:
        assert "could not fetch CATH FunFam assignments for P68871" in str(exc)
    else:
        raise AssertionError("expected CathClientError")


def test_cath_client_raises_on_invalid_payload() -> None:
    client = CathClient(
        transport=httpx.MockTransport(lambda request: httpx.Response(200, json={}))
    )

    try:
        collect_cath_rows(["P68871"], client)
    except CathClientError as exc:
        assert "had no data list" in str(exc)
    else:
        raise AssertionError("expected CathClientError")


def test_render_cath_tsv_and_json_are_stable() -> None:
    rows = collect_cath_rows(
        ["P68871"],
        CathClient(
            transport=httpx.MockTransport(
                lambda request: httpx.Response(200, json=cath_payload())
            )
        ),
    )

    tsv = render_cath_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert [row["member_id"] for row in parsed] == [
        "P68871/2-147",
        "P68873/2-147",
    ]
    assert parsed[0]["superfamily_id"] == "1.10.490.10"

    payload = json.loads(render_cath_json(rows))
    assert payload[0]["source_url"].endswith("/P68871")
