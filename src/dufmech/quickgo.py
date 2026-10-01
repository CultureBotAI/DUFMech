"""Fetch QuickGO molecular-function annotations for UniProt accessions."""

from __future__ import annotations

import csv
import io
import json
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from typing import Any

import httpx

QUICKGO_ANNOTATION_URL = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
QUICKGO_ASPECT = "molecular_function"

QUICKGO_TSV_FIELDNAMES = [
    "uniprot_accession",
    "annotation_id",
    "gene_product_id",
    "qualifier",
    "go_id",
    "go_name",
    "go_evidence",
    "go_aspect",
    "evidence_code",
    "reference",
    "with_from",
    "taxon_id",
    "taxon_name",
    "assigned_by",
    "target_sets",
    "symbol",
    "date",
    "extensions",
    "source_url",
]


class QuickGoClientError(RuntimeError):
    """Raised when QuickGO returns an invalid or failing response."""


@dataclass(frozen=True)
class QuickGoAnnotationRow:
    """One QuickGO annotation associated with a UniProt accession."""

    uniprot_accession: str
    annotation_id: str
    gene_product_id: str
    qualifier: str
    go_id: str
    go_name: str
    go_evidence: str
    go_aspect: str
    evidence_code: str
    reference: str
    with_from: tuple[str, ...]
    taxon_id: str
    taxon_name: str
    assigned_by: str
    target_sets: tuple[str, ...]
    symbol: str
    date: str
    extensions: str

    @property
    def source_url(self) -> str:
        return (
            "https://www.ebi.ac.uk/QuickGO/annotations?"
            f"geneProductId={self.gene_product_id}"
        )

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["with_from"] = ";".join(self.with_from)
        row["target_sets"] = ";".join(self.target_sets)
        row["source_url"] = self.source_url
        return row


class QuickGoClient:
    """Small client for the QuickGO annotation search API."""

    def __init__(
        self,
        *,
        timeout: float = 30.0,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self.timeout = timeout
        self.transport = transport

    def search_uniprot(
        self,
        accession: str,
        *,
        limit: int = 50,
        aspect: str = QUICKGO_ASPECT,
    ) -> Iterable[Mapping[str, Any]]:
        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=True,
            transport=self.transport,
        ) as client:
            response = client.get(
                QUICKGO_ANNOTATION_URL,
                headers={"Accept": "application/json"},
                params={
                    "geneProductId": f"UniProtKB:{accession}",
                    "aspect": aspect,
                    "limit": str(limit),
                },
            )
            try:
                response.raise_for_status()
                payload = response.json()
            except (httpx.HTTPError, ValueError) as exc:
                raise QuickGoClientError(
                    f"could not search QuickGO annotations for {accession}"
                ) from exc

        if not isinstance(payload, Mapping):
            raise QuickGoClientError(
                f"QuickGO annotations for {accession} were not a JSON object"
            )
        results = payload.get("results")
        if not isinstance(results, list):
            raise QuickGoClientError(
                f"QuickGO annotations for {accession} had no results list"
            )
        for result in results:
            if isinstance(result, Mapping):
                yield result


def collect_quickgo_rows(
    accessions: Iterable[str],
    client: QuickGoClient,
    *,
    limit_annotations_per_accession: int = 50,
    aspect: str = QUICKGO_ASPECT,
) -> list[QuickGoAnnotationRow]:
    """Collect QuickGO annotations for ordered, unique UniProt accessions."""

    rows: list[QuickGoAnnotationRow] = []
    seen_accessions: set[str] = set()
    seen_rows: set[tuple[str, str]] = set()
    for accession in accessions:
        if not accession or accession in seen_accessions:
            continue
        seen_accessions.add(accession)
        for annotation in client.search_uniprot(
            accession,
            limit=limit_annotations_per_accession,
            aspect=aspect,
        ):
            row = row_from_quickgo_annotation(accession, annotation)
            if row is None:
                continue
            key = (row.uniprot_accession, row.annotation_id)
            if key in seen_rows:
                continue
            seen_rows.add(key)
            rows.append(row)

    return sorted(rows, key=lambda row: (row.uniprot_accession, row.annotation_id))


def row_from_quickgo_annotation(
    accession: str,
    annotation: Mapping[str, Any],
) -> QuickGoAnnotationRow | None:
    """Return a normalized QuickGO annotation row, or ``None`` if malformed."""

    annotation_id = _string(annotation.get("id"))
    gene_product_id = _string(annotation.get("geneProductId"))
    go_id = _string(annotation.get("goId"))
    if not annotation_id or not gene_product_id or not go_id:
        return None

    return QuickGoAnnotationRow(
        uniprot_accession=accession,
        annotation_id=annotation_id,
        gene_product_id=gene_product_id,
        qualifier=_string(annotation.get("qualifier")),
        go_id=go_id,
        go_name=_string(annotation.get("goName")),
        go_evidence=_string(annotation.get("goEvidence")),
        go_aspect=_string(annotation.get("goAspect")),
        evidence_code=_string(annotation.get("evidenceCode")),
        reference=_string(annotation.get("reference")),
        with_from=_with_from(annotation.get("withFrom")),
        taxon_id=_string(annotation.get("taxonId")),
        taxon_name=_string(annotation.get("taxonName")),
        assigned_by=_string(annotation.get("assignedBy")),
        target_sets=_strings(annotation.get("targetSets")),
        symbol=_string(annotation.get("symbol")),
        date=_string(annotation.get("date")),
        extensions=_compact_json(annotation.get("extensions")),
    )


def render_quickgo_tsv(rows: Iterable[QuickGoAnnotationRow]) -> str:
    """Render QuickGO rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=QUICKGO_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_quickgo_json(rows: Iterable[QuickGoAnnotationRow]) -> str:
    """Render QuickGO rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def _as_list(value: object) -> list[Any]:
    return value if isinstance(value, list) else []


def _compact_json(value: object) -> str:
    if value is None:
        return ""
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def _string(value: object) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, int):
        return str(value)
    return ""


def _strings(value: object) -> tuple[str, ...]:
    return tuple(_string(item) for item in _as_list(value) if _string(item))


def _with_from(value: object) -> tuple[str, ...]:
    groups: list[str] = []
    for group in _as_list(value):
        if not isinstance(group, Mapping):
            continue
        xrefs: list[str] = []
        for xref in _as_list(group.get("connectedXrefs")):
            if not isinstance(xref, Mapping):
                continue
            db = _string(xref.get("db"))
            xref_id = _string(xref.get("id"))
            if db and xref_id:
                xrefs.append(f"{db}:{xref_id}")
        if xrefs:
            groups.append(",".join(xrefs))
    return tuple(groups)
