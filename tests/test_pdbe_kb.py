from __future__ import annotations

import csv
import json
from io import StringIO
from typing import Any

import httpx

from dufmech.pdbe_kb import (
    PdbeKbClient,
    PdbeKbSeed,
    collect_pdbe_kb_rows,
    render_pdbe_kb_json,
    render_pdbe_kb_tsv,
    rows_from_pdbe_kb_payload,
)


def pdbe_uniprot_mapping_payload() -> dict[str, Any]:
    return {
        "1a00": {
            "sequence": "MHL",
            "length": 3,
            "dataType": "UNIPROT MAPPING",
            "data": [
                {
                    "name": "HBB_HUMAN",
                    "accession": "P68871",
                    "dataType": "UniProt",
                    "additionalData": {
                        "bestChainId": "D",
                        "entityId": 2,
                    },
                    "residues": [
                        {
                            "startIndex": 1,
                            "unpStartIndex": 2,
                            "endIndex": 146,
                            "unpEndIndex": 147,
                            "startCode": "MET",
                            "endCode": "HIS",
                            "indexType": "PDB",
                        },
                        {
                            "startIndex": 37,
                            "unpStartIndex": 38,
                            "endIndex": 37,
                            "unpEndIndex": 38,
                            "startCode": "TRP",
                            "endCode": "TRP",
                            "indexType": "UNIPROT",
                            "mutation": True,
                            "pdbCode": "TYR",
                        },
                    ],
                }
            ],
        }
    }


def pdbe_domains_payload() -> dict[str, Any]:
    return {
        "1a00": {
            "sequence": "MHL",
            "length": 3,
            "dataType": "DOMAINS",
            "data": [
                {
                    "name": "CATH domains",
                    "accession": "CATH domains",
                    "dataType": "CATH",
                    "additionalData": {
                        "bestChainId": "D",
                        "entityId": 2,
                    },
                    "residues": [
                        {
                            "startIndex": 1,
                            "endIndex": 146,
                            "startCode": "MET",
                            "endCode": "HIS",
                            "indexType": "PDB",
                            "additionalData": {
                                "domainId": "1.10.490.10",
                                "domain": "1a00D00",
                                "domainName": "Globins",
                                "resourceUrl": "https://www.cathdb.info/",
                            },
                        }
                    ],
                }
            ],
        }
    }


def test_rows_from_pdbe_kb_payload_flattens_residue_annotations() -> None:
    rows = rows_from_pdbe_kb_payload(
        PdbeKbSeed("P68871", "1A00", "2"),
        "uniprot_mapping",
        pdbe_uniprot_mapping_payload(),
    )

    assert len(rows) == 2
    assert rows[0].seed_uniprot_accession == "P68871"
    assert rows[0].pdb_id == "1A00"
    assert rows[0].entity_id == "2"
    assert rows[0].page_data_type == "UNIPROT MAPPING"
    assert rows[0].annotation_data_type == "UniProt"
    assert rows[0].annotation_accession == "P68871"
    assert rows[0].best_chain_id == "D"
    assert rows[0].start_index == 1
    assert rows[0].uniprot_start == 2
    assert rows[0].uniprot_end == 147
    assert rows[1].mutation is True
    assert rows[1].pdb_code == "TYR"


def test_rows_from_pdbe_kb_payload_preserves_endpoint_additional_data() -> None:
    rows = rows_from_pdbe_kb_payload(
        PdbeKbSeed("P68871", "1A00", "2"),
        "domains",
        pdbe_domains_payload(),
    )

    assert len(rows) == 1
    assert rows[0].annotation_data_type == "CATH"
    assert rows[0].detail_id == "1.10.490.10"
    assert rows[0].resource_url == "https://www.cathdb.info/"
    assert json.loads(rows[0].residue_additional_data) == {
        "domain": "1a00D00",
        "domainId": "1.10.490.10",
        "domainName": "Globins",
        "resourceUrl": "https://www.cathdb.info/",
    }


def test_pdbe_kb_client_fetches_selected_entity_endpoints() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path in {
            "/pdbe/api/pdb/entry/uniprot_mapping/1a00/2",
            "/pdbe/api/pdb/entry/domains/1a00/2",
        }
        return httpx.Response(
            200,
            json=(
                pdbe_domains_payload()
                if request.url.path.endswith("/domains/1a00/2")
                else pdbe_uniprot_mapping_payload()
            ),
        )

    client = PdbeKbClient(transport=httpx.MockTransport(handler))

    rows = collect_pdbe_kb_rows(
        [PdbeKbSeed("P68871", "1A00", "2")],
        client,
        endpoints=("uniprot_mapping", "domains"),
    )

    assert [(row.endpoint, row.annotation_data_type) for row in rows] == [
        ("domains", "CATH"),
        ("uniprot_mapping", "UniProt"),
        ("uniprot_mapping", "UniProt"),
    ]


def test_pdbe_kb_client_treats_empty_message_as_no_evidence() -> None:
    client = PdbeKbClient(
        transport=httpx.MockTransport(
            lambda request: httpx.Response(
                200,
                json={"message": "Requested endpoint does not contain any data"},
            )
        )
    )

    assert collect_pdbe_kb_rows([PdbeKbSeed("P68871", "1A00", "2")], client) == []


def test_render_pdbe_kb_tsv_and_json_are_stable() -> None:
    rows = rows_from_pdbe_kb_payload(
        PdbeKbSeed("P68871", "1A00", "2"),
        "uniprot_mapping",
        pdbe_uniprot_mapping_payload(),
    )

    tsv = render_pdbe_kb_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert [row["start_index"] for row in parsed] == ["1", "37"]
    assert parsed[1]["mutation"] == "True"

    payload = json.loads(render_pdbe_kb_json(rows))
    assert payload[0]["source_url"].endswith("/uniprot_mapping/1a00/2")
