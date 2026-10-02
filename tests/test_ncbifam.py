from __future__ import annotations

import csv
import json
from io import StringIO

from dufmech.ncbifam import (
    NcbifamError,
    parse_ncbifam_hits,
    render_ncbifam_json,
    render_ncbifam_tsv,
    row_from_ncbifam_record,
)


def tsv_line(*cells: str) -> str:
    return "\t".join(cells)


NCBIFAM_HEADER = tsv_line(
    "Query ID",
    "NCBIFAM Accession",
    "Source Accession",
    "Model Name",
    "Product Name",
    "Gene Symbol",
    "EC Numbers",
    "GO Terms",
    "Query Start",
    "Query End",
    "E-Value",
    "Bitscore",
)


def ncbifam_line(
    query_id: str = "P75259",
    ncbifam_accession: str = "NF002448",
    *,
    start: str = "39",
    end: str = "154",
    e_value: str = "1e-80",
    bitscore: str = "250.5",
) -> str:
    return tsv_line(
        query_id,
        ncbifam_accession,
        "TIGR00001",
        "UPF0134 protein family",
        "UPF0134 protein",
        "upf0134",
        "1.2.3.4, 5.6.7.8",
        "GO:0003674;GO:0008150",
        start,
        end,
        e_value,
        bitscore,
    )


def test_row_from_ncbifam_record_normalizes_model_metadata() -> None:
    row = row_from_ncbifam_record(
        dict(zip(NCBIFAM_HEADER.split("\t"), ncbifam_line().split("\t")))
    )

    assert row is not None
    assert row.query_id == "P75259"
    assert row.ncbifam_accession == "NF002448"
    assert row.source_accession == "TIGR00001"
    assert row.model_name == "UPF0134 protein family"
    assert row.product_name == "UPF0134 protein"
    assert row.gene_symbol == "upf0134"
    assert row.ec_numbers == ("1.2.3.4", "5.6.7.8")
    assert row.go_terms == ("GO:0003674", "GO:0008150")
    assert row.query_start == 39
    assert row.query_end == 154
    assert row.e_value == 1e-80
    assert row.bitscore == 250.5
    assert row.source_url == (
        "https://www.ncbi.nlm.nih.gov/genome/annotation_prok/evidence/NF002448/"
    )


def test_parse_ncbifam_hits_deduplicates_and_sorts() -> None:
    rows = parse_ncbifam_hits(
        "\n".join(
            [
                NCBIFAM_HEADER,
                ncbifam_line("P75259", "NF002448"),
                ncbifam_line("B2BDZ3", "NF009946"),
                ncbifam_line("P75259", "NF002448"),
            ]
        )
    )

    assert [(row.query_id, row.ncbifam_accession) for row in rows] == [
        ("B2BDZ3", "NF009946"),
        ("P75259", "NF002448"),
    ]


def test_parse_ncbifam_hits_skips_missing_core_identifiers() -> None:
    rows = parse_ncbifam_hits(
        "\n".join(
            [
                NCBIFAM_HEADER,
                ncbifam_line(),
                ncbifam_line(query_id=""),
                ncbifam_line(ncbifam_accession=""),
            ]
        )
    )

    assert [(row.query_id, row.ncbifam_accession) for row in rows] == [
        ("P75259", "NF002448")
    ]


def test_parse_ncbifam_hits_sorts_missing_start_after_zero() -> None:
    rows = parse_ncbifam_hits(
        "\n".join(
            [
                NCBIFAM_HEADER,
                ncbifam_line(start=""),
                ncbifam_line(start="0"),
            ]
        )
    )

    assert [row.query_start for row in rows] == [0, None]


def test_parse_ncbifam_hits_rejects_missing_columns() -> None:
    try:
        parse_ncbifam_hits("Query ID\tNCBIFAM Accession\nP75259\tNF002448\n")
    except NcbifamError as exc:
        assert "Bitscore" in str(exc)
    else:
        raise AssertionError("expected NcbifamError")


def test_parse_ncbifam_hits_rejects_invalid_coordinate() -> None:
    try:
        parse_ncbifam_hits(f"{NCBIFAM_HEADER}\n{ncbifam_line(start='near')}")
    except NcbifamError as exc:
        assert "Query Start" in str(exc)
    else:
        raise AssertionError("expected NcbifamError")


def test_parse_ncbifam_hits_rejects_invalid_score() -> None:
    try:
        parse_ncbifam_hits(f"{NCBIFAM_HEADER}\n{ncbifam_line(bitscore='strong')}")
    except NcbifamError as exc:
        assert "Bitscore" in str(exc)
    else:
        raise AssertionError("expected NcbifamError")


def test_render_ncbifam_tsv_and_json_are_stable() -> None:
    rows = parse_ncbifam_hits(f"{NCBIFAM_HEADER}\n{ncbifam_line()}")

    tsv = render_ncbifam_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert parsed[0]["query_id"] == "P75259"
    assert parsed[0]["ncbifam_accession"] == "NF002448"
    assert parsed[0]["ec_numbers"] == "1.2.3.4;5.6.7.8"

    payload = json.loads(render_ncbifam_json(rows))
    assert payload[0]["query_id"] == "P75259"
    assert payload[0]["ec_numbers"] == ["1.2.3.4", "5.6.7.8"]
