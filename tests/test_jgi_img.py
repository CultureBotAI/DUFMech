from __future__ import annotations

import csv
import json
from io import StringIO

from dufmech.jgi_img import (
    JgiImgError,
    parse_gene_neighborhood_table,
    render_jgi_img_json,
    render_jgi_img_tsv,
    row_from_gene_neighborhood_record,
)


def tsv_line(*cells: str) -> str:
    return "\t".join(cells)


JGI_IMG_HEADER = tsv_line(
    "Query ID",
    "IMG Genome ID",
    "Query Gene OID",
    "Neighbor Gene OID",
    "Neighbor Pfam",
    "Scaffold ID",
    "Neighbor Locus Tag",
    "Neighbor Product",
    "Query-Neighbor Distance",
    "Query-Neighbor Direction",
)


def jgi_img_line(
    query_id: str = "P75259",
    neighbor_gene_oid: str = "3300049538",
    *,
    distance: str = "2",
) -> str:
    return tsv_line(
        query_id,
        "3300000123",
        "3300049500",
        neighbor_gene_oid,
        "PF00005",
        "Ga0123456_101",
        "DUF_0001",
        "ABC transporter ATP-binding protein",
        distance,
        "downstream",
    )


def test_row_from_gene_neighborhood_record_normalizes_mapping_metadata() -> None:
    row = row_from_gene_neighborhood_record(
        dict(zip(JGI_IMG_HEADER.split("\t"), jgi_img_line().split("\t")))
    )

    assert row is not None
    assert row.query_id == "P75259"
    assert row.img_genome_id == "3300000123"
    assert row.query_gene_oid == "3300049500"
    assert row.neighbor_gene_oid == "3300049538"
    assert row.neighbor_pfam == "PF00005"
    assert row.scaffold_id == "Ga0123456_101"
    assert row.neighbor_locus_tag == "DUF_0001"
    assert row.neighbor_product == "ABC transporter ATP-binding protein"
    assert row.query_neighbor_distance == 2
    assert row.query_neighbor_direction == "downstream"
    assert row.source_url == "https://img.jgi.doe.gov/"


def test_parse_gene_neighborhood_table_deduplicates_and_sorts() -> None:
    rows = parse_gene_neighborhood_table(
        "\n".join(
            [
                JGI_IMG_HEADER,
                jgi_img_line("P75259", "3300049538"),
                jgi_img_line("B2BDZ3", "3300049555"),
                jgi_img_line("P75259", "3300049538"),
            ]
        )
    )

    assert [(row.query_id, row.neighbor_gene_oid) for row in rows] == [
        ("B2BDZ3", "3300049555"),
        ("P75259", "3300049538"),
    ]


def test_parse_gene_neighborhood_table_skips_missing_core_identifiers() -> None:
    rows = parse_gene_neighborhood_table(
        "\n".join(
            [
                JGI_IMG_HEADER,
                jgi_img_line(),
                jgi_img_line(query_id=""),
                tsv_line(
                    "P75259",
                    "3300000123",
                    "3300049500",
                    "",
                    "PF00005",
                    "Ga0123456_101",
                    "DUF_0001",
                    "ABC transporter ATP-binding protein",
                    "2",
                    "downstream",
                ),
            ]
        )
    )

    assert [(row.query_id, row.neighbor_gene_oid) for row in rows] == [
        ("P75259", "3300049538")
    ]


def test_parse_gene_neighborhood_table_sorts_missing_distance_after_zero() -> None:
    rows = parse_gene_neighborhood_table(
        "\n".join(
            [
                JGI_IMG_HEADER,
                jgi_img_line(distance=""),
                jgi_img_line(distance="0"),
            ]
        )
    )

    assert [row.query_neighbor_distance for row in rows] == [0, None]


def test_parse_gene_neighborhood_table_rejects_missing_columns() -> None:
    try:
        parse_gene_neighborhood_table("Query ID\tNeighbor Gene OID\nP75259\t3300049538\n")
    except JgiImgError as exc:
        assert "Neighbor Pfam" in str(exc)
    else:
        raise AssertionError("expected JgiImgError")


def test_parse_gene_neighborhood_table_rejects_invalid_distance() -> None:
    invalid_line = tsv_line(
        "P75259",
        "3300000123",
        "3300049500",
        "3300049538",
        "PF00005",
        "Ga0123456_101",
        "DUF_0001",
        "ABC transporter ATP-binding protein",
        "near",
        "downstream",
    )

    try:
        parse_gene_neighborhood_table(f"{JGI_IMG_HEADER}\n{invalid_line}")
    except JgiImgError as exc:
        assert "Distance" in str(exc)
    else:
        raise AssertionError("expected JgiImgError")


def test_render_jgi_img_tsv_and_json_are_stable() -> None:
    rows = parse_gene_neighborhood_table(f"{JGI_IMG_HEADER}\n{jgi_img_line()}")

    tsv = render_jgi_img_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert parsed[0]["query_id"] == "P75259"
    assert parsed[0]["neighbor_pfam"] == "PF00005"
    assert parsed[0]["query_neighbor_distance"] == "2"

    payload = json.loads(render_jgi_img_json(rows))
    assert payload[0]["query_id"] == "P75259"
    assert payload[0]["query_neighbor_distance"] == 2
