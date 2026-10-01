"""Fetch Rhea reaction evidence for UniProt accessions."""

from __future__ import annotations

import csv
import io
import json
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass

import httpx

RHEA_URL = "https://www.rhea-db.org/rhea/"
RHEA_COLUMNS = ("rhea-id", "equation", "chebi-id", "ec", "go", "pubmed")
RHEA_RESPONSE_FIELDNAMES = [
    "Reaction identifier",
    "Equation",
    "ChEBI identifier",
    "EC number",
    "Gene Ontology",
    "PubMed",
]

RHEA_TSV_FIELDNAMES = [
    "uniprot_accession",
    "rhea_id",
    "equation",
    "chebi_ids",
    "ec_numbers",
    "go_terms",
    "pubmed_ids",
    "source_url",
]


class RheaClientError(RuntimeError):
    """Raised when Rhea returns an invalid or failing response."""


@dataclass(frozen=True)
class RheaReactionRow:
    """One Rhea reaction associated with a UniProt accession."""

    uniprot_accession: str
    rhea_id: str
    equation: str
    chebi_ids: tuple[str, ...]
    ec_numbers: tuple[str, ...]
    go_terms: tuple[str, ...]
    pubmed_ids: tuple[str, ...]

    @property
    def source_url(self) -> str:
        return f"{RHEA_URL}{self.rhea_id.removeprefix('RHEA:')}"

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["chebi_ids"] = ";".join(self.chebi_ids)
        row["ec_numbers"] = ";".join(self.ec_numbers)
        row["go_terms"] = ";".join(self.go_terms)
        row["pubmed_ids"] = ";".join(self.pubmed_ids)
        row["source_url"] = self.source_url
        return row


class RheaClient:
    """Small client for the Rhea reaction table API."""

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
    ) -> Iterable[Mapping[str, str]]:
        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=True,
            transport=self.transport,
        ) as client:
            response = client.get(
                RHEA_URL,
                params={
                    "query": f"uniprot:{accession}",
                    "columns": ",".join(RHEA_COLUMNS),
                    "format": "tsv",
                    "limit": str(limit),
                },
            )
            try:
                response.raise_for_status()
            except httpx.HTTPError as exc:
                raise RheaClientError(
                    f"could not search Rhea reactions for {accession}"
                ) from exc

        yield from parse_rhea_tsv(response.text)


def collect_rhea_rows(
    accessions: Iterable[str],
    client: RheaClient,
    *,
    limit_reactions_per_accession: int = 50,
) -> list[RheaReactionRow]:
    """Collect Rhea reactions for ordered, unique UniProt accessions."""

    rows: list[RheaReactionRow] = []
    seen_accessions: set[str] = set()
    seen_rows: set[tuple[str, str]] = set()
    for accession in accessions:
        if not accession or accession in seen_accessions:
            continue
        seen_accessions.add(accession)
        for record in client.search_uniprot(
            accession,
            limit=limit_reactions_per_accession,
        ):
            row = row_from_rhea_record(accession, record)
            if row is None:
                continue
            key = (row.uniprot_accession, row.rhea_id)
            if key in seen_rows:
                continue
            seen_rows.add(key)
            rows.append(row)

    return sorted(rows, key=lambda row: (row.uniprot_accession, row.rhea_id))


def parse_rhea_tsv(text: str) -> list[Mapping[str, str]]:
    """Parse a Rhea TSV response into records."""

    reader = csv.DictReader(io.StringIO(text), dialect="excel-tab")
    if reader.fieldnames != RHEA_RESPONSE_FIELDNAMES:
        raise RheaClientError("Rhea search result had unexpected TSV fieldnames")
    return [
        {key: value or "" for key, value in row.items() if key is not None}
        for row in reader
    ]


def row_from_rhea_record(
    accession: str,
    record: Mapping[str, str],
) -> RheaReactionRow | None:
    """Return a normalized Rhea reaction row, or ``None`` if malformed."""

    rhea_id = _string(record.get("Reaction identifier"))
    if not rhea_id:
        return None

    return RheaReactionRow(
        uniprot_accession=accession,
        rhea_id=rhea_id,
        equation=_string(record.get("Equation")),
        chebi_ids=_split(record.get("ChEBI identifier")),
        ec_numbers=_split(record.get("EC number")),
        go_terms=_split(record.get("Gene Ontology")),
        pubmed_ids=_split(record.get("PubMed")),
    )


def render_rhea_tsv(rows: Iterable[RheaReactionRow]) -> str:
    """Render Rhea rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=RHEA_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_rhea_json(rows: Iterable[RheaReactionRow]) -> str:
    """Render Rhea rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def _split(value: object) -> tuple[str, ...]:
    if not isinstance(value, str):
        return ()
    return tuple(part.strip() for part in value.split(";") if part.strip())


def _string(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""
