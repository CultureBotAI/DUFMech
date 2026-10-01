from __future__ import annotations

import csv
import json
from io import StringIO

import httpx

from dufmech.protein_members import (
    InterProPfamProteinClient,
    collect_family_members,
    collect_members,
    render_members_json,
    render_members_tsv,
    row_from_interpro_protein,
)


def interpro_protein(
    *,
    accession: str = "B2BDZ3",
    name: str = "DUF16 domain-containing protein",
    taxon_id: str = "2104",
    organism: str = "Mycoplasmoides pneumoniae",
    gene: str = "MPN138/MPN137",
    start: int = 39,
    end: int = 140,
    fragments: list[dict] | None = None,
) -> dict:
    fragments = fragments or [
        {
            "start": start,
            "end": end,
            "dc-status": "CONTINUOUS",
        }
    ]
    return {
        "metadata": {
            "accession": accession,
            "name": name,
            "source_database": "unreviewed",
            "length": 191,
            "source_organism": {
                "taxId": taxon_id,
                "scientificName": organism,
                "fullName": organism,
            },
            "gene": gene,
            "in_alphafold": True,
        },
        "entries": [
            {
                "accession": "PF01519",
                "entry_protein_locations": [
                    {
                        "fragments": fragments,
                        "representative": False,
                        "model": "PF01519",
                        "score": 1.6e-31,
                    }
                ],
                "protein_length": 191,
                "source_database": "pfam",
                "entry_type": "coiled_coil",
                "entry_integrated": "ipr002862",
            }
        ],
    }


def test_row_from_interpro_protein_normalizes_member_metadata() -> None:
    row = row_from_interpro_protein("PF01519", interpro_protein())

    assert row is not None
    assert row.pfam_id == "PF01519"
    assert row.uniprot_accession == "B2BDZ3"
    assert row.name == "DUF16 domain-containing protein"
    assert row.source_database == "unreviewed"
    assert row.length == 191
    assert row.taxon_id == "2104"
    assert row.organism == "Mycoplasmoides pneumoniae"
    assert row.gene == "MPN138/MPN137"
    assert row.in_alphafold is True
    assert row.match_count == 1
    assert row.match_ranges == ("39-140",)
    assert row.source_url.endswith("/B2BDZ3/")


def test_discontinuous_fragments_are_one_match() -> None:
    row = row_from_interpro_protein(
        "PF01519",
        interpro_protein(
            fragments=[
                {"start": 39, "end": 80, "dc-status": "N_TERMINAL_DISC"},
                {"start": 90, "end": 140, "dc-status": "C_TERMINAL_DISC"},
            ]
        ),
    )

    assert row is not None
    assert row.match_count == 1
    assert row.match_ranges == ("39-80", "90-140")


def test_collect_members_deduplicates_and_sorts_accessions() -> None:
    rows = collect_members(
        "PF01519",
        [
            interpro_protein(accession="B2BDZ4", start=39, end=154),
            interpro_protein(accession="B2BDZ3"),
            interpro_protein(accession="B2BDZ4", start=50, end=120),
        ],
    )

    assert [row.uniprot_accession for row in rows] == ["B2BDZ3", "B2BDZ4"]
    assert rows[1].match_ranges == ("39-154",)


def test_interpro_protein_client_follows_pagination() -> None:
    first = {
        "count": 2,
        "next": (
            "https://www.ebi.ac.uk/interpro/api/protein/UniProt/entry/"
            "pfam/PF01519/?cursor=next"
        ),
        "results": [interpro_protein(accession="B2BDZ3")],
    }
    second = {
        "count": 2,
        "next": None,
        "results": [interpro_protein(accession="B2BDZ4")],
    }

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.params.get("cursor") == "next":
            return httpx.Response(200, json=second)
        assert request.url.path.endswith("/api/protein/UniProt/entry/pfam/PF01519/")
        assert request.url.params["page_size"] == "200"
        return httpx.Response(200, json=first)

    client = InterProPfamProteinClient(transport=httpx.MockTransport(handler))

    rows = collect_members("PF01519", client.iter_proteins("PF01519"))

    assert [row.uniprot_accession for row in rows] == ["B2BDZ3", "B2BDZ4"]


def test_collect_family_members_expands_stable_pfam_list() -> None:
    pages = {
        "/interpro/api/protein/UniProt/entry/pfam/PF01519/": {
            "count": 1,
            "next": None,
            "results": [interpro_protein(accession="B2BDZ4", start=39, end=154)],
        },
        "/interpro/api/protein/UniProt/entry/pfam/PF01579/": {
            "count": 1,
            "next": None,
            "results": [interpro_protein(accession="O44526", start=21, end=148)],
        },
    }

    def handler(request: httpx.Request) -> httpx.Response:
        payload = pages[request.url.path]
        assert request.url.params["page_size"] == "50"
        return httpx.Response(200, json=payload)

    client = InterProPfamProteinClient(transport=httpx.MockTransport(handler))

    rows = collect_family_members(
        ["PF01579", "PF01519", "PF01579"],
        client,
        page_size=50,
        limit_members_per_family=1,
    )

    assert [(row.pfam_id, row.uniprot_accession) for row in rows] == [
        ("PF01519", "B2BDZ4"),
        ("PF01579", "O44526"),
    ]


def test_render_member_tsv_and_json_are_stable() -> None:
    rows = collect_members(
        "PF01519",
        [
            interpro_protein(accession="B2BDZ4", start=39, end=154),
            interpro_protein(accession="B2BDZ3"),
        ],
    )

    tsv = render_members_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert [row["uniprot_accession"] for row in parsed] == ["B2BDZ3", "B2BDZ4"]
    assert parsed[0]["match_ranges"] == "39-140"

    payload = json.loads(render_members_json(rows))
    assert payload[0]["source_url"].endswith("/B2BDZ3/")
