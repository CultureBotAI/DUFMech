"""Parse EFI-GNT Pfam-neighbor mapping tables."""

from __future__ import annotations

import csv
import io
import json
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass

EFI_GNT_URL = "https://efi.igb.illinois.edu/efi-gnt/"

EFI_GNT_TSV_FIELDNAMES = [
    "query_id",
    "neighbor_id",
    "neighbor_pfam",
    "ssn_query_cluster_number",
    "ssn_query_cluster_color",
    "query_neighbor_distance",
    "query_neighbor_direction",
    "source_url",
]

EFI_GNT_REQUIRED_COLUMNS = {
    "Query ID",
    "Neighbor ID",
    "Neighbor Pfam",
    "SSN Query Cluster #",
    "SSN Query Cluster Color",
    "Query-Neighbor Distance",
    "Query-Neighbor Directions",
}


class EfiGntError(RuntimeError):
    """Raised when an EFI-GNT Pfam-neighbor table is invalid."""


@dataclass(frozen=True)
class EfiGntNeighborRow:
    """One normalized EFI-GNT query-to-neighbor relationship."""

    query_id: str
    neighbor_id: str
    neighbor_pfam: str
    ssn_query_cluster_number: str
    ssn_query_cluster_color: str
    query_neighbor_distance: int | None
    query_neighbor_direction: str

    @property
    def source_url(self) -> str:
        return EFI_GNT_URL

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["source_url"] = self.source_url
        return row


def parse_pfam_neighbor_table(text: str) -> list[EfiGntNeighborRow]:
    """Parse an EFI-GNT Pfam Neighbor Mapping Table TSV."""

    reader = csv.DictReader(io.StringIO(text), dialect="excel-tab")
    _require_columns(reader.fieldnames or [])

    rows: list[EfiGntNeighborRow] = []
    seen: set[tuple[object, ...]] = set()
    for record in reader:
        row = row_from_pfam_neighbor_record(record)
        if row is None:
            continue
        key = (
            row.query_id,
            row.neighbor_id,
            row.neighbor_pfam,
            row.ssn_query_cluster_number,
            row.query_neighbor_distance,
            row.query_neighbor_direction,
        )
        if key in seen:
            continue
        seen.add(key)
        rows.append(row)

    return sort_efi_gnt_rows(rows)


def row_from_pfam_neighbor_record(
    record: Mapping[str, str | None],
) -> EfiGntNeighborRow | None:
    """Return a normalized EFI-GNT Pfam-neighbor row, or ``None`` if empty."""

    query_id = _string(record.get("Query ID"))
    neighbor_id = _string(record.get("Neighbor ID"))
    neighbor_pfam = _string(record.get("Neighbor Pfam"))
    if not query_id or not neighbor_id or not neighbor_pfam:
        return None

    return EfiGntNeighborRow(
        query_id=query_id,
        neighbor_id=neighbor_id,
        neighbor_pfam=neighbor_pfam,
        ssn_query_cluster_number=_string(record.get("SSN Query Cluster #")),
        ssn_query_cluster_color=_string(record.get("SSN Query Cluster Color")),
        query_neighbor_distance=_optional_int(
            record.get("Query-Neighbor Distance"),
            column="Query-Neighbor Distance",
        ),
        query_neighbor_direction=_string(record.get("Query-Neighbor Directions")),
    )


def render_efi_gnt_tsv(rows: Iterable[EfiGntNeighborRow]) -> str:
    """Render EFI-GNT rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=EFI_GNT_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_efi_gnt_json(rows: Iterable[EfiGntNeighborRow]) -> str:
    """Render EFI-GNT rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def sort_efi_gnt_rows(rows: Iterable[EfiGntNeighborRow]) -> list[EfiGntNeighborRow]:
    """Sort EFI-GNT rows by every stable, normalized key field."""

    return sorted(
        rows,
        key=lambda row: (
            row.query_id,
            row.neighbor_pfam,
            row.neighbor_id,
            row.ssn_query_cluster_number,
            _distance_sort_key(row.query_neighbor_distance),
            row.query_neighbor_direction,
        ),
    )


def _require_columns(fieldnames: Iterable[str]) -> None:
    missing = EFI_GNT_REQUIRED_COLUMNS.difference(fieldnames)
    if missing:
        missing_text = ", ".join(sorted(missing))
        raise EfiGntError(f"EFI-GNT Pfam-neighbor table missing columns: {missing_text}")


def _optional_int(value: str | None, *, column: str) -> int | None:
    text = _string(value)
    if not text:
        return None
    try:
        return int(text)
    except ValueError as exc:
        raise EfiGntError(f"EFI-GNT {column} must be an integer") from exc


def _distance_sort_key(value: int | None) -> tuple[int, int]:
    if value is None:
        return (1, 0)
    return (0, value)


def _string(value: object) -> str:
    if not isinstance(value, str):
        return ""
    text = value.strip()
    return "" if text == "-" else text
