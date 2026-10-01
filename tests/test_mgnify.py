from __future__ import annotations

import csv
import json
from io import StringIO

import httpx

from dufmech.mgnify import (
    MGnifyProteinClient,
    collect_pfam_mgnify_rows,
    render_mgnify_json,
    render_mgnify_tsv,
    row_from_mgnify_protein,
)


def search_hit(mgyp: str = "MGYP000000000166") -> dict:
    return {
        "mgyp": mgyp,
        "full_length": True,
        "cluster_size": 3,
    }


def protein_detail(mgyp: str = "MGYP000000000166") -> dict:
    return {
        "mgyp": mgyp,
        "sequence": "MPEPTIDE",
        "full_length": True,
        "cluster_size": 3,
        "biomes": [
            {
                "id": 132,
                "name": "root:Environmental:Aquatic:Marine",
                "count": 2,
            },
            {
                "id": 433,
                "name": "root:Engineered:Wastewater",
                "count": 1,
            },
        ],
        "pfam_annotations": [
            {
                "accession": "PF01519",
                "name": "DUF16",
                "env_start": 2,
                "env_end": 7,
            },
            {
                "accession": "PF00005",
                "name": "ABC transporter",
                "env_start": 1,
                "env_end": 8,
            },
        ],
    }


def test_row_from_mgnify_protein_normalizes_environmental_metadata() -> None:
    row = row_from_mgnify_protein("PF01519", search_hit(), protein_detail())

    assert row is not None
    assert row.pfam_id == "PF01519"
    assert row.mgyp == "MGYP000000000166"
    assert row.full_length is True
    assert row.cluster_size == 3
    assert row.sequence_length == 8
    assert row.biome_ids == (132, 433)
    assert row.biome_names == (
        "root:Environmental:Aquatic:Marine",
        "root:Engineered:Wastewater",
    )
    assert row.biome_counts == (2, 1)
    assert row.pfam_match_count == 1
    assert row.pfam_match_ranges == ("2-7",)
    assert row.source_url.endswith("/MGYP000000000166")


def test_mgnify_client_searches_pfam_and_fetches_details() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/protein/search"):
            assert request.url.params["pfam_accession"] == "PF01519"
            assert request.url.params["limit"] == "2"
            return httpx.Response(
                200,
                json=[search_hit("MGYP000000000166"), search_hit("MGYP000000000617")],
            )
        if request.url.path.endswith("/protein/MGYP000000000166"):
            return httpx.Response(200, json=protein_detail("MGYP000000000166"))
        assert request.url.path.endswith("/protein/MGYP000000000617")
        return httpx.Response(200, json=protein_detail("MGYP000000000617"))

    client = MGnifyProteinClient(transport=httpx.MockTransport(handler))
    rows = collect_pfam_mgnify_rows(
        ["PF01519"],
        client,
        limit_proteins_per_family=2,
    )

    assert [(row.pfam_id, row.mgyp) for row in rows] == [
        ("PF01519", "MGYP000000000166"),
        ("PF01519", "MGYP000000000617"),
    ]


def test_render_mgnify_tsv_and_json_are_stable() -> None:
    client = MGnifyProteinClient(
        transport=httpx.MockTransport(
            lambda request: httpx.Response(
                200,
                json=(
                    [
                        search_hit("MGYP000000000617"),
                        search_hit("MGYP000000000166"),
                    ]
                    if request.url.path.endswith("/protein/search")
                    else protein_detail(request.url.path.rsplit("/", 1)[-1])
                ),
            )
        )
    )
    rows = collect_pfam_mgnify_rows(["PF01519"], client, limit_proteins_per_family=2)

    tsv = render_mgnify_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert [row["mgyp"] for row in parsed] == [
        "MGYP000000000166",
        "MGYP000000000617",
    ]
    assert parsed[0]["biome_ids"] == "132;433"
    assert parsed[0]["pfam_match_ranges"] == "2-7"

    payload = json.loads(render_mgnify_json(rows))
    assert payload[0]["source_url"].endswith("/MGYP000000000166")
