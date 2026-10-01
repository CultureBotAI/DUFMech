from __future__ import annotations

import csv
from io import StringIO

import httpx

from dufmech.rhea import (
    RheaClient,
    RheaClientError,
    collect_rhea_rows,
    parse_rhea_tsv,
    render_rhea_json,
    render_rhea_tsv,
)

RHEA_TSV = """Reaction identifier\tEquation\tChEBI identifier\tEC number\tGene Ontology\tPubMed
RHEA:10012\t(R)-6-hydroxynicotine + O2 + H2O = 6-hydroxypseudooxynicotine + H2O2\tCHEBI:58413;CHEBI:15379\tEC:1.5.3.6\tGO:0018530 (R)-6-hydroxynicotine oxidase activity\t16095622;2680607
RHEA:46988\t(R)-6-hydroxynicotine + O2 = 6-hydroxy-N-methylmyosmine + H2O2\tCHEBI:58413;CHEBI:15379\t\t\t16095622;2680607
"""


def test_parse_rhea_tsv_normalizes_multivalue_fields() -> None:
    rows = collect_rhea_rows(
        ["P08159"],
        RheaClient(transport=httpx.MockTransport(lambda request: rhea_response())),
        limit_reactions_per_accession=2,
    )

    assert [row.rhea_id for row in rows] == ["RHEA:10012", "RHEA:46988"]
    assert rows[0].chebi_ids == ("CHEBI:58413", "CHEBI:15379")
    assert rows[0].ec_numbers == ("EC:1.5.3.6",)
    assert rows[0].go_terms == (
        "GO:0018530 (R)-6-hydroxynicotine oxidase activity",
    )
    assert rows[0].pubmed_ids == ("16095622", "2680607")
    assert rows[0].source_url.endswith("/10012")
    assert rows[1].go_terms == ()


def test_rhea_client_searches_by_uniprot_accession() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.params["query"] == "uniprot:P08159"
        assert request.url.params["columns"] == "rhea-id,equation,chebi-id,ec,go,pubmed"
        assert request.url.params["format"] == "tsv"
        assert request.url.params["limit"] == "2"
        return rhea_response()

    rows = collect_rhea_rows(
        ["P08159", "P08159"],
        RheaClient(transport=httpx.MockTransport(handler)),
        limit_reactions_per_accession=2,
    )

    assert len(rows) == 2


def test_parse_rhea_tsv_raises_on_unexpected_fieldnames() -> None:
    try:
        parse_rhea_tsv("<html>not tsv</html>")
    except RheaClientError as exc:
        assert "unexpected TSV fieldnames" in str(exc)
    else:
        raise AssertionError("expected RheaClientError")


def test_rhea_client_treats_header_only_tsv_as_no_evidence() -> None:
    rows = collect_rhea_rows(
        ["A0A_DOES_NOT_EXIST"],
        RheaClient(
            transport=httpx.MockTransport(
                lambda request: httpx.Response(
                    200,
                    text=(
                        "Reaction identifier\tEquation\tChEBI identifier\t"
                        "EC number\tGene Ontology\tPubMed\n"
                    ),
                )
            )
        ),
    )

    assert rows == []


def test_render_rhea_tsv_and_json_are_stable() -> None:
    rows = collect_rhea_rows(
        ["P08159"],
        RheaClient(transport=httpx.MockTransport(lambda request: rhea_response())),
        limit_reactions_per_accession=2,
    )

    tsv = render_rhea_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert [row["rhea_id"] for row in parsed] == ["RHEA:10012", "RHEA:46988"]
    assert parsed[0]["chebi_ids"] == "CHEBI:58413;CHEBI:15379"

    assert '"source_url": "https://www.rhea-db.org/rhea/10012"' in render_rhea_json(
        rows
    )


def rhea_response() -> httpx.Response:
    return httpx.Response(200, text=RHEA_TSV)
