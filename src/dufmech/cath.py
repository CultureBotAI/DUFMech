"""Fetch CATH-Gene3D FunFam assignments for UniProt accessions."""

from __future__ import annotations

import csv
import io
import json
import re
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from typing import Any

import httpx

CATH_BASE_URL = "https://www.cathdb.info"
CATH_VERSION = "v4_4_0"
CATH_UNIPROT_TO_FUNFAM_URL = (
    f"{CATH_BASE_URL}/version/{{version}}/api/rest/uniprot_to_funfam/{{accession}}"
)

CATH_TSV_FIELDNAMES = [
    "uniprot_accession",
    "cath_uniprot_accession",
    "member_id",
    "member_accession",
    "member_start",
    "member_end",
    "uniprot_start",
    "superfamily_id",
    "funfam_number",
    "sequence_md5",
    "confidence",
    "taxon_id",
    "species_name",
    "taxon_division_id",
    "taxon_division_name",
    "gene_id",
    "gene_name",
    "description",
    "source_url",
]

MEMBER_RANGE_RE = re.compile(r"^(?P<accession>[^/]+)/(?P<start>\d+)-(?P<end>\d+)$")


class CathClientError(RuntimeError):
    """Raised when CATH-Gene3D returns an invalid or failing response."""


@dataclass(frozen=True)
class CathFunFamRow:
    """One CATH-Gene3D FunFam assignment for a UniProt accession."""

    uniprot_accession: str
    cath_uniprot_accession: str
    member_id: str
    member_accession: str
    member_start: int | None
    member_end: int | None
    uniprot_start: int | None
    superfamily_id: str
    funfam_number: str
    sequence_md5: str
    confidence: str
    taxon_id: str
    species_name: str
    taxon_division_id: str
    taxon_division_name: str
    gene_id: str
    gene_name: str
    description: str
    cath_version: str = CATH_VERSION

    @property
    def source_url(self) -> str:
        return CATH_UNIPROT_TO_FUNFAM_URL.format(
            version=self.cath_version,
            accession=self.uniprot_accession,
        )

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row.pop("cath_version")
        row["source_url"] = self.source_url
        return row


class CathClient:
    """Small client for the CATH-Gene3D UniProt-to-FunFam API."""

    def __init__(
        self,
        *,
        version: str = CATH_VERSION,
        timeout: float = 30.0,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self.version = version
        self.timeout = timeout
        self.transport = transport

    def uniprot_to_funfam(self, accession: str) -> Iterable[Mapping[str, Any]]:
        url = CATH_UNIPROT_TO_FUNFAM_URL.format(
            version=self.version,
            accession=accession,
        )
        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=True,
            transport=self.transport,
        ) as client:
            response = client.get(url, params={"content-type": "application/json"})
            if response.status_code == 404:
                return
            try:
                response.raise_for_status()
                payload = response.json()
            except (httpx.HTTPError, ValueError) as exc:
                raise CathClientError(
                    f"could not fetch CATH FunFam assignments for {accession}"
                ) from exc

        if not isinstance(payload, Mapping):
            raise CathClientError(
                f"CATH FunFam assignments for {accession} were not a JSON object"
            )
        data = payload.get("data")
        if not isinstance(data, list):
            raise CathClientError(
                f"CATH FunFam assignments for {accession} had no data list"
            )
        for row in data:
            if isinstance(row, Mapping):
                yield row


def collect_cath_rows(
    accessions: Iterable[str],
    client: CathClient,
) -> list[CathFunFamRow]:
    """Collect CATH FunFam rows for ordered, unique UniProt accessions."""

    rows: list[CathFunFamRow] = []
    seen_accessions: set[str] = set()
    seen_rows: set[tuple[str, str, str, str]] = set()
    for accession in accessions:
        accession = _string(accession)
        if not accession or accession in seen_accessions:
            continue
        seen_accessions.add(accession)
        for record in client.uniprot_to_funfam(accession):
            row = row_from_cath_record(
                accession,
                record,
                cath_version=client.version,
            )
            if row is None:
                continue
            key = (
                row.uniprot_accession,
                row.member_id,
                row.superfamily_id,
                row.funfam_number,
            )
            if key in seen_rows:
                continue
            seen_rows.add(key)
            rows.append(row)

    return sorted(
        rows,
        key=lambda row: (
            row.uniprot_accession,
            row.superfamily_id,
            _int(row.funfam_number) or 0,
            row.member_id,
        ),
    )


def row_from_cath_record(
    accession: str,
    record: Mapping[str, Any],
    *,
    cath_version: str = CATH_VERSION,
) -> CathFunFamRow | None:
    """Return a normalized CATH FunFam assignment, or ``None`` if malformed."""

    member_id = _string(record.get("member_id"))
    superfamily_id = _string(record.get("superfamily_id"))
    funfam_number = _string(record.get("funfam_number"))
    if not member_id or not superfamily_id or not funfam_number:
        return None

    member_accession, member_start, member_end = _member_range(member_id)

    return CathFunFamRow(
        uniprot_accession=accession,
        cath_uniprot_accession=_string(record.get("uniprot_acc")),
        member_id=member_id,
        member_accession=member_accession,
        member_start=member_start,
        member_end=member_end,
        uniprot_start=_int(record.get("uni_start")),
        superfamily_id=superfamily_id,
        funfam_number=funfam_number,
        sequence_md5=_string(record.get("sequence_md5")),
        confidence=_string(record.get("confidence")),
        taxon_id=_string(record.get("taxon_id")),
        species_name=_string(record.get("species_name")),
        taxon_division_id=_string(record.get("taxon_division_id")),
        taxon_division_name=_string(record.get("taxon_division_name")),
        gene_id=_string(record.get("gene_id")),
        gene_name=_string(record.get("gene_name")),
        description=_string(record.get("description")),
        cath_version=cath_version,
    )


def render_cath_tsv(rows: Iterable[CathFunFamRow]) -> str:
    """Render CATH FunFam rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=CATH_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_cath_json(rows: Iterable[CathFunFamRow]) -> str:
    """Render CATH FunFam rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def _member_range(member_id: str) -> tuple[str, int | None, int | None]:
    match = MEMBER_RANGE_RE.match(member_id)
    if match is None:
        return (member_id, None, None)
    return (
        match.group("accession"),
        int(match.group("start")),
        int(match.group("end")),
    )


def _int(value: object) -> int | None:
    try:
        if isinstance(value, str) and value:
            return int(value)
        if isinstance(value, int) and not isinstance(value, bool):
            return value
    except ValueError:
        return None
    return None


def _string(value: object) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, int):
        return str(value)
    return ""
