from __future__ import annotations

import csv
import json
from io import StringIO

import httpx

from dufmech.uniref import (
    UniProtIdMappingClient,
    UniProtIdMappingError,
    collect_uniref_mappings,
    render_uniref_json,
    render_uniref_tsv,
    row_from_uniref_mapping,
)


def uniref_result(
    *,
    source: str = "B2BDZ4",
    cluster_id: str = "UniRef90_P75259",
    entry_type: str = "UniRef90",
    representative_accessions: list[str] | None = None,
) -> dict:
    return {
        "from": source,
        "to": {
            "id": cluster_id,
            "name": "Cluster: UPF0134 protein MPN_139",
            "updated": "2026-06-10",
            "entryType": entry_type,
            "commonTaxon": {
                "scientificName": "Mycoplasmoides pneumoniae",
                "taxonId": 2104,
            },
            "memberCount": 2,
            "organismCount": 2,
            "representativeMember": {
                "memberId": "Y139_MYCPN",
                "organismTaxId": 272634,
                "sequenceLength": 163,
                "proteinName": "UPF0134 protein MPN_139",
                "accessions": representative_accessions or ["P75259"],
            },
            "seedId": "P75259",
        },
    }


def test_row_from_uniref_mapping_normalizes_cluster_metadata() -> None:
    row = row_from_uniref_mapping(uniref_result())

    assert row is not None
    assert row.uniprot_accession == "B2BDZ4"
    assert row.uniref_id == "UniRef90_P75259"
    assert row.uniref_type == "UniRef90"
    assert row.name == "Cluster: UPF0134 protein MPN_139"
    assert row.updated == "2026-06-10"
    assert row.member_count == 2
    assert row.organism_count == 2
    assert row.common_taxon_id == "2104"
    assert row.common_taxon_name == "Mycoplasmoides pneumoniae"
    assert row.representative_accession == "P75259"
    assert row.representative_member_id == "Y139_MYCPN"
    assert row.representative_protein_name == "UPF0134 protein MPN_139"
    assert row.representative_taxon_id == "272634"
    assert row.representative_length == 163
    assert row.seed_id == "P75259"
    assert row.source_url.endswith("/UniRef90_P75259")


def test_collect_uniref_mappings_deduplicates_and_sorts_rows() -> None:
    rows = collect_uniref_mappings(
        [
            uniref_result(source="B2BDZ4", cluster_id="UniRef90_P75259"),
            uniref_result(source="B2BDZ3", cluster_id="UniRef90_B2BDZ3"),
            uniref_result(source="B2BDZ4", cluster_id="UniRef90_P75259"),
        ]
    )

    assert [(row.uniref_id, row.uniprot_accession) for row in rows] == [
        ("UniRef90_B2BDZ3", "B2BDZ3"),
        ("UniRef90_P75259", "B2BDZ4"),
    ]


def test_uniprot_mapping_client_submits_and_polls_mapping_job() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/idmapping/run":
            payload = request.read().decode("utf-8")
            assert "from=UniProtKB_AC-ID" in payload
            assert "to=UniRef90" in payload
            assert "ids=B2BDZ3%2CB2BDZ4" in payload
            return httpx.Response(200, json={"jobId": "job-1"})
        assert request.url.path == "/idmapping/status/job-1"
        return httpx.Response(
            200,
            json={
                "results": [
                    uniref_result(source="B2BDZ3", cluster_id="UniRef90_B2BDZ3"),
                    uniref_result(source="B2BDZ4", cluster_id="UniRef90_P75259"),
                ]
            },
        )

    client = UniProtIdMappingClient(
        poll_interval=0,
        transport=httpx.MockTransport(handler),
    )

    rows = collect_uniref_mappings(client.map_uniref(["B2BDZ3", "B2BDZ4"]))

    assert [row.uniprot_accession for row in rows] == ["B2BDZ3", "B2BDZ4"]


def test_uniprot_mapping_client_reports_failed_ids() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/idmapping/run":
            return httpx.Response(200, json={"jobId": "job-1"})
        return httpx.Response(200, json={"failedIds": ["B2BDZ3"]})

    client = UniProtIdMappingClient(
        poll_interval=0,
        transport=httpx.MockTransport(handler),
    )

    try:
        list(client.map_uniref(["B2BDZ3"]))
    except UniProtIdMappingError as exc:
        assert "B2BDZ3" in str(exc)
    else:
        raise AssertionError("expected UniProtIdMappingError")


def test_uniprot_mapping_client_waits_for_results() -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        if request.url.path == "/idmapping/run":
            return httpx.Response(200, json={"jobId": "job-1"})

        attempts += 1
        if attempts == 1:
            return httpx.Response(200, json={"jobStatus": "RUNNING"})
        return httpx.Response(200, json={"results": [uniref_result()]})

    client = UniProtIdMappingClient(
        poll_interval=0,
        transport=httpx.MockTransport(handler),
    )

    rows = collect_uniref_mappings(client.map_uniref(["B2BDZ4"]))

    assert len(rows) == 1
    assert attempts == 2


def test_uniprot_mapping_client_follows_results_pagination() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/idmapping/run":
            return httpx.Response(200, json={"jobId": "job-1"})
        if request.url.params.get("cursor") == "next":
            return httpx.Response(
                200,
                json={
                    "results": [
                        uniref_result(
                            source="B2BDZ4",
                            cluster_id="UniRef90_P75259",
                        )
                    ]
                },
            )
        return httpx.Response(
            200,
            headers={
                "Link": (
                    "<https://rest.uniprot.org/idmapping/uniref/results/"
                    'job-1?cursor=next>; rel="next"'
                )
            },
            json={
                "results": [
                    uniref_result(
                        source="B2BDZ3",
                        cluster_id="UniRef90_B2BDZ3",
                    )
                ]
            },
        )

    client = UniProtIdMappingClient(
        poll_interval=0,
        transport=httpx.MockTransport(handler),
    )

    rows = collect_uniref_mappings(client.map_uniref(["B2BDZ3", "B2BDZ4"]))

    assert [row.uniprot_accession for row in rows] == ["B2BDZ3", "B2BDZ4"]


def test_render_uniref_tsv_and_json_are_stable() -> None:
    rows = collect_uniref_mappings(
        [
            uniref_result(source="B2BDZ3", cluster_id="UniRef90_B2BDZ3"),
            uniref_result(source="B2BDZ4", cluster_id="UniRef90_P75259"),
        ]
    )

    tsv = render_uniref_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert [row["uniref_id"] for row in parsed] == [
        "UniRef90_B2BDZ3",
        "UniRef90_P75259",
    ]
    assert parsed[0]["source_url"] == (
        "https://rest.uniprot.org/uniref/UniRef90_B2BDZ3"
    )

    payload = json.loads(render_uniref_json(rows))
    assert payload[0]["source_url"].endswith("/UniRef90_B2BDZ3")
