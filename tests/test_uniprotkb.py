from __future__ import annotations

import csv
import json
from io import StringIO

import httpx

from dufmech.uniprotkb import (
    UniProtKbMetadataClient,
    collect_uniprotkb_metadata,
    render_uniprotkb_metadata_json,
    render_uniprotkb_metadata_tsv,
    row_from_uniprotkb_entry,
)


def uniprotkb_entry(
    *,
    accession: str = "B2BDZ4",
    uniprot_id: str = "A0A0H3MNP5_MYCPU",
    entry_type: str = "UniProtKB unreviewed (TrEMBL)",
) -> dict:
    return {
        "primaryAccession": accession,
        "uniProtkbId": uniprot_id,
        "entryType": entry_type,
        "proteinDescription": {
            "recommendedName": {
                "fullName": {
                    "value": "UPF0134 protein MPN_139",
                },
            },
        },
        "organism": {
            "taxonId": 2104,
            "scientificName": "Mycoplasmoides pneumoniae",
        },
        "uniProtKBCrossReferences": [
            {
                "database": "Proteomes",
                "id": "UP000000808",
            },
            {
                "database": "Proteomes",
                "id": "UP000000808",
            },
            {
                "database": "AlphaFoldDB",
                "id": "B2BDZ4",
            },
        ],
    }


def test_row_from_uniprotkb_entry_normalizes_proteome_metadata() -> None:
    row = row_from_uniprotkb_entry(uniprotkb_entry())

    assert row is not None
    assert row.uniprot_accession == "B2BDZ4"
    assert row.uniprot_id == "A0A0H3MNP5_MYCPU"
    assert row.reviewed is False
    assert row.protein_name == "UPF0134 protein MPN_139"
    assert row.taxon_id == "2104"
    assert row.organism == "Mycoplasmoides pneumoniae"
    assert row.proteome_ids == ("UP000000808",)
    assert row.source_url.endswith("/B2BDZ4")


def test_collect_uniprotkb_metadata_deduplicates_and_sorts_rows() -> None:
    rows = collect_uniprotkb_metadata(
        [
            uniprotkb_entry(accession="B2BDZ4"),
            uniprotkb_entry(
                accession="B2BDZ3",
                uniprot_id="A0A0H3ML47_MYCPU",
                entry_type="UniProtKB reviewed (Swiss-Prot)",
            ),
            uniprotkb_entry(accession="B2BDZ4"),
        ]
    )

    assert [(row.uniprot_accession, row.reviewed) for row in rows] == [
        ("B2BDZ3", True),
        ("B2BDZ4", False),
    ]


def test_uniprotkb_metadata_client_follows_pagination() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/uniprotkb/search"
        if request.url.params.get("cursor") == "next":
            return httpx.Response(
                200,
                json={"results": [uniprotkb_entry(accession="B2BDZ4")]},
            )

        assert request.url.params["query"] == "accession:B2BDZ3 OR accession:B2BDZ4"
        assert request.url.params["size"] == "50"
        return httpx.Response(
            200,
            headers={
                "Link": (
                    "<https://rest.uniprot.org/uniprotkb/search?"
                    'cursor=next>; rel="next"'
                )
            },
            json={"results": [uniprotkb_entry(accession="B2BDZ3")]},
        )

    client = UniProtKbMetadataClient(transport=httpx.MockTransport(handler))

    rows = collect_uniprotkb_metadata(
        client.iter_metadata(
            ["B2BDZ3", "B2BDZ4", "B2BDZ3"],
            page_size=50,
        )
    )

    assert [row.uniprot_accession for row in rows] == ["B2BDZ3", "B2BDZ4"]


def test_render_uniprotkb_metadata_tsv_and_json_are_stable() -> None:
    rows = collect_uniprotkb_metadata(
        [
            uniprotkb_entry(accession="B2BDZ4"),
            uniprotkb_entry(accession="B2BDZ3"),
        ]
    )

    tsv = render_uniprotkb_metadata_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert [row["uniprot_accession"] for row in parsed] == ["B2BDZ3", "B2BDZ4"]
    assert parsed[0]["proteome_ids"] == "UP000000808"

    payload = json.loads(render_uniprotkb_metadata_json(rows))
    assert payload[0]["source_url"].endswith("/B2BDZ3")
