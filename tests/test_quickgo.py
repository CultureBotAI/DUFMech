from __future__ import annotations

import csv
import json
from io import StringIO
from typing import Any

import httpx

from dufmech.quickgo import (
    QuickGoClient,
    QuickGoClientError,
    collect_quickgo_rows,
    render_quickgo_json,
    render_quickgo_tsv,
    row_from_quickgo_annotation,
)


def quickgo_annotation_payload() -> dict[str, Any]:
    return {
        "numberOfHits": 1,
        "results": [
            {
                "id": "UniProtKB:P08159!447048181",
                "geneProductId": "UniProtKB:P08159",
                "qualifier": "enables",
                "goId": "GO:0018530",
                "goName": "oxidase activity",
                "goEvidence": "IEA",
                "goAspect": "molecular_function",
                "evidenceCode": "ECO:0000501",
                "reference": "GO_REF:0000120",
                "withFrom": [
                    {"connectedXrefs": [{"db": "RHEA", "id": "10012"}]},
                    {"connectedXrefs": [{"db": "EC", "id": "1.5.3.6"}]},
                ],
                "taxonId": 29320,
                "taxonName": "Arthrobacter nicotinovorans",
                "assignedBy": "UniProt",
                "extensions": [{"connectedXrefs": [{"db": "FOO", "id": "1"}]}],
                "targetSets": ["UniProt"],
                "symbol": "6-hdno",
                "date": "20260727",
            }
        ],
        "pageInfo": {"resultsPerPage": 10, "current": 1, "total": 1},
    }


def test_row_from_quickgo_annotation_normalizes_cross_references() -> None:
    row = row_from_quickgo_annotation(
        "P08159",
        quickgo_annotation_payload()["results"][0],
    )

    assert row is not None
    assert row.uniprot_accession == "P08159"
    assert row.annotation_id == "UniProtKB:P08159!447048181"
    assert row.gene_product_id == "UniProtKB:P08159"
    assert row.qualifier == "enables"
    assert row.go_id == "GO:0018530"
    assert row.evidence_code == "ECO:0000501"
    assert row.with_from == ("RHEA:10012", "EC:1.5.3.6")
    assert row.taxon_id == "29320"
    assert row.target_sets == ("UniProt",)
    assert json.loads(row.extensions) == [
        {"connectedXrefs": [{"db": "FOO", "id": "1"}]}
    ]


def test_quickgo_client_searches_by_uniprot_accession() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.params["geneProductId"] == "UniProtKB:P08159"
        assert request.url.params["aspect"] == "molecular_function"
        assert request.url.params["limit"] == "1"
        assert request.headers["accept"] == "application/json"
        return httpx.Response(200, json=quickgo_annotation_payload())

    rows = collect_quickgo_rows(
        ["P08159", "P08159"],
        QuickGoClient(transport=httpx.MockTransport(handler)),
        limit_annotations_per_accession=1,
    )

    assert len(rows) == 1


def test_quickgo_client_treats_empty_results_as_no_evidence() -> None:
    rows = collect_quickgo_rows(
        ["A0A_DOES_NOT_EXIST"],
        QuickGoClient(
            transport=httpx.MockTransport(
                lambda request: httpx.Response(
                    200,
                    json={"numberOfHits": 0, "results": []},
                )
            )
        ),
    )

    assert rows == []


def test_quickgo_client_raises_on_http_failure() -> None:
    client = QuickGoClient(
        transport=httpx.MockTransport(lambda request: httpx.Response(500))
    )

    try:
        collect_quickgo_rows(["P08159"], client)
    except QuickGoClientError as exc:
        assert "could not search QuickGO annotations for P08159" in str(exc)
    else:
        raise AssertionError("expected QuickGoClientError")


def test_render_quickgo_tsv_and_json_are_stable() -> None:
    rows = collect_quickgo_rows(
        ["P08159"],
        QuickGoClient(
            transport=httpx.MockTransport(
                lambda request: httpx.Response(
                    200,
                    json=quickgo_annotation_payload(),
                )
            )
        ),
    )

    tsv = render_quickgo_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert parsed[0]["with_from"] == "RHEA:10012;EC:1.5.3.6"
    assert parsed[0]["target_sets"] == "UniProt"

    payload = json.loads(render_quickgo_json(rows))
    assert payload[0]["source_url"].endswith(
        "/annotations?geneProductId=UniProtKB:P08159"
    )
