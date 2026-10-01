from __future__ import annotations

import csv
import json
from io import StringIO

import httpx

from dufmech.uniparc import (
    UNIPARC_TARGET,
    collect_uniparc_mappings,
    render_uniparc_json,
    render_uniparc_tsv,
    row_from_uniparc_mapping,
)
from dufmech.uniref import UniProtIdMappingClient


def uniparc_result(
    *,
    source: str = "P75259",
    uniparc_id: str = "UPI000013A20F",
) -> dict:
    return {
        "from": source,
        "to": {
            "uniParcId": uniparc_id,
            "crossReferenceCount": 181,
            "commonTaxons": [
                {
                    "topLevel": "cellular organisms",
                    "commonTaxon": "Mycoplasmoides pneumoniae",
                    "commonTaxonId": 2104,
                }
            ],
            "uniProtKBAccessions": [
                "B2BDZ4",
                "A0A7U4SLB0.1",
                "P75259.1",
                "P75259",
            ],
            "sequence": {
                "value": "MKEKIPFYNEKEFHDMVKKTKK",
                "length": 163,
                "molWeight": 19116,
                "crc64": "0D8AF31CEC157FAD",
                "md5": "0BB3B8E600BB8B2AC3C92B70609AA020",
            },
            "sequenceFeatures": [
                {
                    "database": "Gene3D",
                    "databaseId": "G3DSA:6.10.250.40",
                    "locations": [{"start": 54, "end": 154}],
                },
                {
                    "database": "Pfam",
                    "databaseId": "PF01519",
                    "interproGroup": {
                        "id": "IPR002862",
                        "name": "Domain of unknown function DUF16",
                    },
                    "locations": [{"start": 39, "end": 154}],
                },
            ],
        },
    }


def test_row_from_uniparc_mapping_normalizes_sequence_archive_metadata() -> None:
    row = row_from_uniparc_mapping(uniparc_result())

    assert row is not None
    assert row.uniprot_accession == "P75259"
    assert row.uniparc_id == "UPI000013A20F"
    assert row.cross_reference_count == 181
    assert row.sequence_length == 163
    assert row.molecular_weight == 19116
    assert row.crc64 == "0D8AF31CEC157FAD"
    assert row.md5 == "0BB3B8E600BB8B2AC3C92B70609AA020"
    assert row.common_taxon_ids == ("2104",)
    assert row.common_taxon_names == ("Mycoplasmoides pneumoniae",)
    assert row.common_taxon_top_levels == ("cellular organisms",)
    assert row.uniprotkb_accessions == (
        "B2BDZ4",
        "A0A7U4SLB0.1",
        "P75259.1",
        "P75259",
    )
    assert row.interpro_ids == ("IPR002862",)
    assert row.pfam_ids == ("PF01519",)
    assert row.gene3d_ids == ("G3DSA:6.10.250.40",)
    assert row.sequence_feature_count == 2
    assert row.source_url.endswith("/UPI000013A20F")


def test_collect_uniparc_mappings_deduplicates_and_sorts_rows() -> None:
    rows = collect_uniparc_mappings(
        [
            uniparc_result(source="P75259", uniparc_id="UPI000013A20F"),
            uniparc_result(source="B2BDZ3", uniparc_id="UPI000013A20E"),
            uniparc_result(source="P75259", uniparc_id="UPI000013A20F"),
        ]
    )

    assert [(row.uniparc_id, row.uniprot_accession) for row in rows] == [
        ("UPI000013A20E", "B2BDZ3"),
        ("UPI000013A20F", "P75259"),
    ]


def test_collect_uniparc_mappings_uses_uniparc_id_mapping_target() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/idmapping/run":
            payload = request.read().decode("utf-8")
            assert "from=UniProtKB_AC-ID" in payload
            assert "to=UniParc" in payload
            assert "ids=P75259" in payload
            return httpx.Response(200, json={"jobId": "job-1"})
        assert request.url.path == "/idmapping/status/job-1"
        return httpx.Response(200, json={"results": [uniparc_result()]})

    client = UniProtIdMappingClient(
        poll_interval=0,
        transport=httpx.MockTransport(handler),
    )

    rows = collect_uniparc_mappings(
        client.map_accessions(["P75259"], target=UNIPARC_TARGET)
    )

    assert [row.uniparc_id for row in rows] == ["UPI000013A20F"]


def test_render_uniparc_tsv_and_json_are_stable() -> None:
    rows = collect_uniparc_mappings(
        [
            uniparc_result(source="P75259", uniparc_id="UPI000013A20F"),
            uniparc_result(source="B2BDZ3", uniparc_id="UPI000013A20E"),
        ]
    )

    tsv = render_uniparc_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert [row["uniparc_id"] for row in parsed] == [
        "UPI000013A20E",
        "UPI000013A20F",
    ]
    assert parsed[0]["common_taxon_ids"] == "2104"
    assert parsed[0]["pfam_ids"] == "PF01519"

    payload = json.loads(render_uniparc_json(rows))
    assert payload[0]["source_url"].endswith("/UPI000013A20E")
