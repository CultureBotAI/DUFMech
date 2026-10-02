"""Parse saved JGI IMG gene-neighborhood tables."""

from __future__ import annotations

import csv
import io
import json
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass

JGI_IMG_URL = "https://img.jgi.doe.gov/"

JGI_IMG_TSV_FIELDNAMES = [
    "query_id",
    "img_genome_id",
    "query_gene_oid",
    "neighbor_gene_oid",
    "neighbor_pfam",
    "scaffold_id",
    "neighbor_locus_tag",
    "neighbor_product",
    "query_neighbor_distance",
    "query_neighbor_direction",
    "source_url",
]

JGI_IMG_REQUIRED_COLUMNS = {
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
}


class JgiImgError(RuntimeError):
    """Raised when a JGI IMG gene-neighborhood table is invalid."""


@dataclass(frozen=True)
class JgiImgNeighborRow:
    """One normalized JGI IMG query-to-neighbor relationship."""

    query_id: str
    img_genome_id: str
    query_gene_oid: str
    neighbor_gene_oid: str
    neighbor_pfam: str
    scaffold_id: str
    neighbor_locus_tag: str
    neighbor_product: str
    query_neighbor_distance: int | None
    query_neighbor_direction: str

    @property
    def source_url(self) -> str:
        return JGI_IMG_URL

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["source_url"] = self.source_url
        return row


def parse_gene_neighborhood_table(text: str) -> list[JgiImgNeighborRow]:
    """Parse a saved JGI IMG gene-neighborhood TSV."""

    reader = csv.DictReader(io.StringIO(text), dialect="excel-tab")
    _require_columns(reader.fieldnames or [])

    rows: list[JgiImgNeighborRow] = []
    seen: set[tuple[object, ...]] = set()
    for record in reader:
        row = row_from_gene_neighborhood_record(record)
        if row is None:
            continue
        key = (
            row.query_id,
            row.img_genome_id,
            row.query_gene_oid,
            row.neighbor_gene_oid,
            row.neighbor_pfam,
            row.scaffold_id,
            row.neighbor_locus_tag,
            row.neighbor_product,
            row.query_neighbor_distance,
            row.query_neighbor_direction,
        )
        if key in seen:
            continue
        seen.add(key)
        rows.append(row)

    return sort_jgi_img_rows(rows)


def row_from_gene_neighborhood_record(
    record: Mapping[str, str | None],
) -> JgiImgNeighborRow | None:
    """Return a normalized JGI IMG gene-neighbor row, or ``None`` if empty."""

    query_id = _string(record.get("Query ID"))
    neighbor_gene_oid = _string(record.get("Neighbor Gene OID"))
    neighbor_pfam = _string(record.get("Neighbor Pfam"))
    if not query_id or not neighbor_gene_oid or not neighbor_pfam:
        return None

    return JgiImgNeighborRow(
        query_id=query_id,
        img_genome_id=_string(record.get("IMG Genome ID")),
        query_gene_oid=_string(record.get("Query Gene OID")),
        neighbor_gene_oid=neighbor_gene_oid,
        neighbor_pfam=neighbor_pfam,
        scaffold_id=_string(record.get("Scaffold ID")),
        neighbor_locus_tag=_string(record.get("Neighbor Locus Tag")),
        neighbor_product=_string(record.get("Neighbor Product")),
        query_neighbor_distance=_optional_int(
            record.get("Query-Neighbor Distance"),
            column="Query-Neighbor Distance",
        ),
        query_neighbor_direction=_string(record.get("Query-Neighbor Direction")),
    )


def render_jgi_img_tsv(rows: Iterable[JgiImgNeighborRow]) -> str:
    """Render JGI IMG rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=JGI_IMG_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_jgi_img_json(rows: Iterable[JgiImgNeighborRow]) -> str:
    """Render JGI IMG rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def sort_jgi_img_rows(rows: Iterable[JgiImgNeighborRow]) -> list[JgiImgNeighborRow]:
    """Sort JGI IMG rows by every stable, normalized key field."""

    return sorted(
        rows,
        key=lambda row: (
            row.query_id,
            row.neighbor_pfam,
            row.neighbor_gene_oid,
            row.img_genome_id,
            row.query_gene_oid,
            row.scaffold_id,
            row.neighbor_locus_tag,
            row.neighbor_product,
            _distance_sort_key(row.query_neighbor_distance),
            row.query_neighbor_direction,
        ),
    )


def _require_columns(fieldnames: Iterable[str]) -> None:
    missing = JGI_IMG_REQUIRED_COLUMNS.difference(fieldnames)
    if missing:
        missing_text = ", ".join(sorted(missing))
        raise JgiImgError(f"JGI IMG gene-neighborhood table missing columns: {missing_text}")


def _optional_int(value: str | None, *, column: str) -> int | None:
    text = _string(value)
    if not text:
        return None
    try:
        return int(text)
    except ValueError as exc:
        raise JgiImgError(f"JGI IMG {column} must be an integer") from exc


def _distance_sort_key(value: int | None) -> tuple[int, int]:
    if value is None:
        return (1, 0)
    return (0, value)


def _string(value: object) -> str:
    if not isinstance(value, str):
        return ""
    text = value.strip()
    return "" if text == "-" else text
