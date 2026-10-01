from __future__ import annotations

import csv
import json
from io import StringIO
from typing import Any

import httpx

from dufmech.rcsb import (
    RcsbPdbClient,
    collect_rcsb_pdb_rows,
    render_rcsb_pdb_json,
    render_rcsb_pdb_tsv,
    row_from_rcsb_pdb_entity,
)


def rcsb_search_result(entity_id: str = "1A00_2") -> dict:
    return {
        "query_id": "query-1",
        "result_type": "polymer_entity",
        "total_count": 1,
        "result_set": [{"identifier": entity_id, "score": 1.0}],
    }


def rcsb_entity(
    *,
    pdb_id: str = "1A00",
    entity_id: str = "2",
    resolution: float = 2.0,
) -> dict[str, Any]:
    return {
        "rcsb_id": f"{pdb_id}_{entity_id}",
        "rcsb_polymer_entity_container_identifiers": {
            "entry_id": pdb_id,
            "entity_id": entity_id,
            "auth_asym_ids": ["B", "D"],
            "reference_sequence_identifiers": [
                {"database_name": "UniProt", "database_accession": "P68871"},
                {"database_name": "GenBank", "database_accession": "AAA16334"},
            ],
        },
        "entity_poly": {
            "pdbx_strand_id": "B,D",
            "rcsb_entity_polymer_type": "Protein",
            "rcsb_sample_sequence_length": 146,
        },
        "rcsb_entity_source_organism": [
            {
                "ncbi_taxonomy_id": 9606,
                "ncbi_scientific_name": "Homo sapiens",
            }
        ],
        "rcsb_polymer_entity_name_com": [
            {
                "name": "Hemoglobin subunit beta",
            }
        ],
        "entry": {
            "rcsb_entry_info": {
                "experimental_method": "X-ray",
                "resolution_combined": [resolution],
            }
        },
    }


def test_row_from_rcsb_pdb_entity_normalizes_experimental_metadata() -> None:
    row = row_from_rcsb_pdb_entity("P68871", rcsb_entity())

    assert row is not None
    assert row.uniprot_accession == "P68871"
    assert row.pdb_id == "1A00"
    assert row.entity_id == "2"
    assert row.rcsb_id == "1A00_2"
    assert row.experimental_method == "X-ray"
    assert row.resolution == 2.0
    assert row.polymer_type == "Protein"
    assert row.sequence_length == 146
    assert row.chain_ids == ("B", "D")
    assert row.taxon_id == "9606"
    assert row.organism == "Homo sapiens"
    assert row.entity_names == ("Hemoglobin subunit beta",)
    assert row.reference_accessions == ("P68871",)
    assert row.source_url.endswith("/1A00")


def test_rcsb_client_searches_and_hydrates_entities() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.host == "search.rcsb.org":
            payload = json.loads(request.read().decode("utf-8"))
            assert payload["query"]["parameters"]["value"] == "P68871"
            assert payload["request_options"]["paginate"]["rows"] == 2
            return httpx.Response(
                200,
                json={
                    "result_set": [
                        {"identifier": "1A00_2"},
                        {"identifier": "1A01_2"},
                    ]
                },
            )

        payload = json.loads(request.read().decode("utf-8"))
        assert payload["variables"]["ids"] == ["1A00_2", "1A01_2"]
        return httpx.Response(
            200,
            json={
                "data": {
                    "polymer_entities": [
                        rcsb_entity(pdb_id="1A00", resolution=2.0),
                        rcsb_entity(pdb_id="1A01", resolution=1.8),
                    ]
                }
            },
        )

    client = RcsbPdbClient(transport=httpx.MockTransport(handler))

    rows = collect_rcsb_pdb_rows(
        ["P68871"],
        client,
        limit_entities_per_accession=2,
    )

    assert [(row.pdb_id, row.resolution) for row in rows] == [
        ("1A00", 2.0),
        ("1A01", 1.8),
    ]


def test_rcsb_client_treats_204_search_as_no_evidence() -> None:
    client = RcsbPdbClient(
        transport=httpx.MockTransport(
            lambda request: httpx.Response(204)
            if request.url.host == "search.rcsb.org"
            else httpx.Response(500)
        )
    )

    assert collect_rcsb_pdb_rows(["P68871"], client) == []


def test_render_rcsb_pdb_tsv_and_json_are_stable() -> None:
    client = RcsbPdbClient(
        transport=httpx.MockTransport(
            lambda request: httpx.Response(
                200,
                json=(
                    {
                        "result_set": [
                            {"identifier": "1A01_2"},
                            {"identifier": "1A00_2"},
                        ]
                    }
                    if request.url.host == "search.rcsb.org"
                    else {
                        "data": {
                            "polymer_entities": [
                                rcsb_entity(pdb_id="1A01", resolution=1.8),
                                rcsb_entity(pdb_id="1A00", resolution=2.0),
                            ]
                        }
                    }
                ),
            )
        )
    )
    rows = collect_rcsb_pdb_rows(["P68871"], client, limit_entities_per_accession=2)

    tsv = render_rcsb_pdb_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert [row["pdb_id"] for row in parsed] == ["1A00", "1A01"]
    assert parsed[0]["chain_ids"] == "B;D"
    assert parsed[0]["reference_accessions"] == "P68871"

    payload = json.loads(render_rcsb_pdb_json(rows))
    assert payload[0]["source_url"].endswith("/1A00")
