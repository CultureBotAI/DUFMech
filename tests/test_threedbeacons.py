from __future__ import annotations

import csv
import json
from io import StringIO

import httpx

from dufmech.threedbeacons import (
    ThreeDBeaconsClient,
    ThreeDBeaconsClientError,
    collect_threedbeacons_rows,
    render_threedbeacons_json,
    render_threedbeacons_tsv,
    rows_from_threedbeacons_payload,
)


def threedbeacons_payload() -> dict:
    return {
        "uniprot_entry": {
            "ac": "P75259",
            "id": "Y139_MYCPN",
            "uniprot_checksum": "0D8AF31CEC157FAD",
            "sequence_length": 163,
            "segment_start": 52,
            "segment_end": 158,
        },
        "structures": [
            {
                "summary": {
                    "model_identifier": "P75259_52-158:7n9f.1.9",
                    "model_category": "TEMPLATE-BASED",
                    "model_url": (
                        "https://swissmodel.expasy.org/3d-beacons/uniprot/"
                        "P75259.cif?range=52-158&template=7n9f.1.9"
                    ),
                    "model_format": "MMCIF",
                    "model_type": "ATOMIC",
                    "model_page_url": (
                        "https://swissmodel.expasy.org/repository/uniprot/"
                        "P75259?range=52-158&template=7n9f.1.9"
                    ),
                    "provider": "SWISS-MODEL",
                    "created": "2026-09-27",
                    "sequence_identity": 1.0,
                    "uniprot_start": 52,
                    "uniprot_end": 158,
                    "coverage": 0.656,
                    "confidence_type": "QMEANDisCo",
                    "confidence_version": "4.6.0",
                    "confidence_avg_local_score": 0.526,
                    "oligomeric_state": "MONOMER",
                    "entities": [
                        {
                            "entity_type": "POLYMER",
                            "entity_poly_type": "POLYPEPTIDE(L)",
                            "identifier": "P75259",
                            "identifier_category": "UNIPROT",
                            "description": "UPF0134 protein MPN_139",
                            "chain_ids": ["A"],
                        },
                        {
                            "entity_type": "NON-POLYMER",
                            "identifier": "NA",
                            "identifier_category": "CCD",
                            "description": "SODIUM ION",
                            "chain_ids": ["B"],
                        },
                    ],
                },
            },
            {
                "summary": {
                    "model_identifier": "AF-P75259-F1",
                    "model_category": "AB-INITIO",
                    "model_url": "https://alphafold.ebi.ac.uk/files/AF-P75259-F1.cif",
                    "model_format": "MMCIF",
                    "model_page_url": "https://alphafold.ebi.ac.uk/entry/AF-P75259-F1",
                    "provider": "AlphaFold DB",
                    "created": "2025-08-01T00:00:00Z",
                    "sequence_identity": 1.0,
                    "uniprot_start": 1,
                    "uniprot_end": 163,
                    "coverage": 1.0,
                    "confidence_type": "pLDDT",
                    "confidence_avg_local_score": 83.88,
                    "oligomeric_state": "MONOMER",
                    "entities": [
                        {
                            "entity_type": "POLYMER",
                            "identifier": "P75259",
                            "identifier_category": "UNIPROT",
                            "description": "UPF0134 protein MPN_139",
                            "chain_ids": ["A"],
                        },
                    ],
                },
            },
        ],
    }


def test_threedbeacons_client_fetches_and_normalizes_summaries() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path.endswith("/uniprot/summary/P75259.json")
        return httpx.Response(200, json=threedbeacons_payload())

    rows = collect_threedbeacons_rows(
        ["P75259", "P75259"],
        ThreeDBeaconsClient(transport=httpx.MockTransport(handler)),
    )

    assert len(rows) == 2
    assert rows[0].uniprot_accession == "P75259"
    assert rows[0].uniprot_id == "Y139_MYCPN"
    assert rows[0].provider == "AlphaFold DB"
    assert rows[0].confidence_type == "pLDDT"
    assert rows[0].confidence_avg_local_score == 83.88
    assert rows[1].provider == "SWISS-MODEL"
    assert rows[1].sequence_length == 163
    assert rows[1].segment_start == 52
    assert rows[1].segment_end == 158
    assert rows[1].model_type == "ATOMIC"
    assert rows[1].uniprot_start == 52
    assert rows[1].uniprot_end == 158
    assert rows[1].coverage == 0.656
    assert rows[1].confidence_version == "4.6.0"
    assert rows[1].polymer_identifiers == ("UNIPROT:P75259",)
    assert rows[1].non_polymer_identifiers == ("CCD:NA",)
    assert rows[1].source_url.endswith("template=7n9f.1.9")


def test_threedbeacons_404_is_no_evidence() -> None:
    rows = collect_threedbeacons_rows(
        ["MISSING"],
        ThreeDBeaconsClient(
            transport=httpx.MockTransport(lambda request: httpx.Response(404))
        ),
    )

    assert rows == []


def test_threedbeacons_client_raises_on_http_failure() -> None:
    client = ThreeDBeaconsClient(
        transport=httpx.MockTransport(lambda request: httpx.Response(500))
    )

    try:
        collect_threedbeacons_rows(["P75259"], client)
    except ThreeDBeaconsClientError as exc:
        assert "could not fetch 3D-Beacons summary for P75259" in str(exc)
    else:
        raise AssertionError("expected ThreeDBeaconsClientError")


def test_rows_from_threedbeacons_payload_raises_without_structures() -> None:
    try:
        rows_from_threedbeacons_payload("P75259", {})
    except ThreeDBeaconsClientError as exc:
        assert "had no structures list" in str(exc)
    else:
        raise AssertionError("expected ThreeDBeaconsClientError")


def test_render_threedbeacons_tsv_and_json_are_stable() -> None:
    rows = rows_from_threedbeacons_payload("P75259", threedbeacons_payload())

    tsv = render_threedbeacons_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert [row["provider"] for row in parsed] == ["SWISS-MODEL", "AlphaFold DB"]
    assert parsed[0]["polymer_identifiers"] == "UNIPROT:P75259"
    assert parsed[0]["non_polymer_identifiers"] == "CCD:NA"

    payload = json.loads(render_threedbeacons_json(rows))
    assert payload[0]["source_url"].endswith("template=7n9f.1.9")
