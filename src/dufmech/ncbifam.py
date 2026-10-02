"""Parse saved NCBI Protein Family Model HMM hit tables."""

from __future__ import annotations

import csv
import io
import json
import re
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass

NCBIFAM_HMM_FTP_URL = "https://ftp.ncbi.nih.gov/hmm/current"
NCBIFAM_EVIDENCE_URL = "https://www.ncbi.nlm.nih.gov/genome/annotation_prok/evidence"

NCBIFAM_TSV_FIELDNAMES = [
    "query_id",
    "ncbifam_accession",
    "source_accession",
    "model_name",
    "product_name",
    "gene_symbol",
    "ec_numbers",
    "go_terms",
    "query_start",
    "query_end",
    "e_value",
    "bitscore",
    "source_url",
]

NCBIFAM_REQUIRED_COLUMNS = {
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
}


class NcbifamError(RuntimeError):
    """Raised when a NCBIFAM HMM hit table is invalid."""


@dataclass(frozen=True)
class NcbifamHitRow:
    """One normalized query-to-NCBIFAM HMM hit relationship."""

    query_id: str
    ncbifam_accession: str
    source_accession: str
    model_name: str
    product_name: str
    gene_symbol: str
    ec_numbers: tuple[str, ...]
    go_terms: tuple[str, ...]
    query_start: int | None
    query_end: int | None
    e_value: float | None
    bitscore: float | None

    @property
    def source_url(self) -> str:
        return f"{NCBIFAM_EVIDENCE_URL}/{self.ncbifam_accession}/"

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["ec_numbers"] = ";".join(self.ec_numbers)
        row["go_terms"] = ";".join(self.go_terms)
        row["source_url"] = self.source_url
        return row


def parse_ncbifam_hits(text: str) -> list[NcbifamHitRow]:
    """Parse a saved NCBIFAM HMM hit TSV."""

    reader = csv.DictReader(io.StringIO(text), dialect="excel-tab")
    _require_columns(reader.fieldnames or [])

    rows: list[NcbifamHitRow] = []
    seen: set[NcbifamHitRow] = set()
    for record in reader:
        row = row_from_ncbifam_record(record)
        if row is None:
            continue
        if row in seen:
            continue
        seen.add(row)
        rows.append(row)

    return sort_ncbifam_rows(rows)


def row_from_ncbifam_record(record: Mapping[str, str | None]) -> NcbifamHitRow | None:
    """Return a normalized NCBIFAM HMM hit row, or ``None`` if empty."""

    query_id = _string(record.get("Query ID"))
    ncbifam_accession = _string(record.get("NCBIFAM Accession")).upper()
    if not query_id or not ncbifam_accession:
        return None

    return NcbifamHitRow(
        query_id=query_id,
        ncbifam_accession=ncbifam_accession,
        source_accession=_string(record.get("Source Accession")),
        model_name=_string(record.get("Model Name")),
        product_name=_string(record.get("Product Name")),
        gene_symbol=_string(record.get("Gene Symbol")),
        ec_numbers=_split_terms(record.get("EC Numbers")),
        go_terms=_split_terms(record.get("GO Terms")),
        query_start=_optional_int(record.get("Query Start"), column="Query Start"),
        query_end=_optional_int(record.get("Query End"), column="Query End"),
        e_value=_optional_float(record.get("E-Value"), column="E-Value"),
        bitscore=_optional_float(record.get("Bitscore"), column="Bitscore"),
    )


def render_ncbifam_tsv(rows: Iterable[NcbifamHitRow]) -> str:
    """Render NCBIFAM rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=NCBIFAM_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_ncbifam_json(rows: Iterable[NcbifamHitRow]) -> str:
    """Render NCBIFAM rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def sort_ncbifam_rows(rows: Iterable[NcbifamHitRow]) -> list[NcbifamHitRow]:
    """Sort NCBIFAM rows by every stable, normalized key field."""

    return sorted(
        rows,
        key=lambda row: (
            row.query_id,
            row.ncbifam_accession,
            row.source_accession,
            row.model_name,
            row.product_name,
            row.gene_symbol,
            row.ec_numbers,
            row.go_terms,
            _int_sort_key(row.query_start),
            _int_sort_key(row.query_end),
            _float_sort_key(row.e_value),
            _float_sort_key(row.bitscore),
        ),
    )


def _require_columns(fieldnames: Iterable[str]) -> None:
    missing = NCBIFAM_REQUIRED_COLUMNS.difference(fieldnames)
    if missing:
        missing_text = ", ".join(sorted(missing))
        raise NcbifamError(f"NCBIFAM HMM hit table missing columns: {missing_text}")


def _optional_int(value: str | None, *, column: str) -> int | None:
    text = _string(value)
    if not text:
        return None
    try:
        return int(text)
    except ValueError as exc:
        raise NcbifamError(f"NCBIFAM {column} must be an integer") from exc


def _optional_float(value: str | None, *, column: str) -> float | None:
    text = _string(value)
    if not text:
        return None
    try:
        return float(text)
    except ValueError as exc:
        raise NcbifamError(f"NCBIFAM {column} must be a number") from exc


def _split_terms(value: str | None) -> tuple[str, ...]:
    terms: list[str] = []
    seen: set[str] = set()
    for term in re.split(r"[;,]", _string(value)):
        term = term.strip()
        if not term or term in seen:
            continue
        seen.add(term)
        terms.append(term)
    return tuple(terms)


def _int_sort_key(value: int | None) -> tuple[int, int]:
    if value is None:
        return (1, 0)
    return (0, value)


def _float_sort_key(value: float | None) -> tuple[int, float]:
    if value is None:
        return (1, 0.0)
    return (0, value)


def _string(value: object) -> str:
    if not isinstance(value, str):
        return ""
    text = value.strip()
    return "" if text == "-" else text
