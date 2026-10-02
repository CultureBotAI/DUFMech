from __future__ import annotations

import csv
import json
from io import StringIO

from dufmech.efi_gnt import (
    EfiGntError,
    parse_pfam_neighbor_table,
    render_efi_gnt_json,
    render_efi_gnt_tsv,
    row_from_pfam_neighbor_record,
)


def tsv_line(*cells: str) -> str:
    return "\t".join(cells)


EFI_GNT_HEADER = tsv_line(
    "Query ID",
    "Neighbor ID",
    "Neighbor Pfam",
    "SSN Query Cluster #",
    "SSN Query Cluster Color",
    "Query-Neighbor Distance",
    "Query-Neighbor Directions",
)


def efi_gnt_line(
    query_id: str = "P75259",
    neighbor_id: str = "Q11111",
    *,
    distance: str = "2",
) -> str:
    return tsv_line(
        query_id,
        neighbor_id,
        "PF00005",
        "1",
        "#1f77b4",
        distance,
        "same",
    )


def test_row_from_pfam_neighbor_record_normalizes_mapping_metadata() -> None:
    row = row_from_pfam_neighbor_record(
        dict(zip(EFI_GNT_HEADER.split("\t"), efi_gnt_line().split("\t")))
    )

    assert row is not None
    assert row.query_id == "P75259"
    assert row.neighbor_id == "Q11111"
    assert row.neighbor_pfam == "PF00005"
    assert row.ssn_query_cluster_number == "1"
    assert row.ssn_query_cluster_color == "#1f77b4"
    assert row.query_neighbor_distance == 2
    assert row.query_neighbor_direction == "same"
    assert row.source_url == "https://efi.igb.illinois.edu/efi-gnt/"


def test_parse_pfam_neighbor_table_deduplicates_and_sorts() -> None:
    rows = parse_pfam_neighbor_table(
        "\n".join(
            [
                EFI_GNT_HEADER,
                efi_gnt_line("P75259", "Q11111"),
                efi_gnt_line("B2BDZ3", "Q33333"),
                efi_gnt_line("P75259", "Q11111"),
            ]
        )
    )

    assert [(row.query_id, row.neighbor_id) for row in rows] == [
        ("B2BDZ3", "Q33333"),
        ("P75259", "Q11111"),
    ]


def test_parse_pfam_neighbor_table_sorts_missing_distance_after_zero() -> None:
    rows = parse_pfam_neighbor_table(
        "\n".join(
            [
                EFI_GNT_HEADER,
                efi_gnt_line(distance=""),
                efi_gnt_line(distance="0"),
            ]
        )
    )

    assert [row.query_neighbor_distance for row in rows] == [0, None]


def test_parse_pfam_neighbor_table_rejects_missing_columns() -> None:
    try:
        parse_pfam_neighbor_table("Query ID\tNeighbor ID\nP75259\tQ11111\n")
    except EfiGntError as exc:
        assert "Neighbor Pfam" in str(exc)
    else:
        raise AssertionError("expected EfiGntError")


def test_parse_pfam_neighbor_table_rejects_invalid_distance() -> None:
    try:
        parse_pfam_neighbor_table(
            f"{EFI_GNT_HEADER}\n"
            f"{tsv_line('P75259', 'Q11111', 'PF00005', '1', '#1f77b4', 'near', 'same')}"
        )
    except EfiGntError as exc:
        assert "Distance" in str(exc)
    else:
        raise AssertionError("expected EfiGntError")


def test_render_efi_gnt_tsv_and_json_are_stable() -> None:
    rows = parse_pfam_neighbor_table(f"{EFI_GNT_HEADER}\n{efi_gnt_line()}")

    tsv = render_efi_gnt_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert parsed[0]["query_id"] == "P75259"
    assert parsed[0]["neighbor_pfam"] == "PF00005"
    assert parsed[0]["query_neighbor_distance"] == "2"

    payload = json.loads(render_efi_gnt_json(rows))
    assert payload[0]["query_id"] == "P75259"
    assert payload[0]["query_neighbor_distance"] == 2
