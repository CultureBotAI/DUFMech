"""Fetch accession-keyed UniProtKB metadata."""

from __future__ import annotations

import csv
import io
import json
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import asdict, dataclass
from typing import Any

import httpx

UNIPROTKB_SEARCH_URL = "https://rest.uniprot.org/uniprotkb/search"

UNIPROTKB_METADATA_TSV_FIELDNAMES = [
    "uniprot_accession",
    "uniprot_id",
    "reviewed",
    "protein_name",
    "taxon_id",
    "organism",
    "proteome_ids",
    "source_url",
]


class UniProtKbMetadataError(RuntimeError):
    """Raised when UniProtKB returns an invalid or failing response."""


@dataclass(frozen=True)
class UniProtKbMetadataRow:
    """UniProtKB metadata keyed by a primary accession."""

    uniprot_accession: str
    uniprot_id: str
    reviewed: bool | None
    protein_name: str
    taxon_id: str
    organism: str
    proteome_ids: tuple[str, ...]

    @property
    def source_url(self) -> str:
        return f"https://rest.uniprot.org/uniprotkb/{self.uniprot_accession}"

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["proteome_ids"] = ";".join(self.proteome_ids)
        row["source_url"] = self.source_url
        return row


class UniProtKbMetadataClient:
    """Small client for accession-keyed UniProtKB search pages."""

    def __init__(
        self,
        *,
        timeout: float = 30.0,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self.timeout = timeout
        self.transport = transport

    def iter_metadata(
        self,
        accessions: Iterable[str],
        *,
        batch_size: int = 100,
        page_size: int = 500,
    ) -> Iterable[Mapping[str, Any]]:
        if batch_size < 1:
            raise ValueError("batch_size must be positive")
        if page_size < 1 or page_size > 500:
            raise ValueError("page_size must be between 1 and 500")

        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=True,
            transport=self.transport,
        ) as client:
            for batch in _chunked(_unique_accessions(accessions), batch_size):
                next_url: str | None = UNIPROTKB_SEARCH_URL
                params: dict[str, str] | None = {
                    "query": " OR ".join(f"accession:{accession}" for accession in batch),
                    "size": str(page_size),
                }
                while next_url:
                    response = client.get(next_url, params=params)
                    try:
                        response.raise_for_status()
                        payload = response.json()
                    except (httpx.HTTPError, ValueError) as exc:
                        raise UniProtKbMetadataError(
                            f"could not fetch UniProtKB metadata page {next_url}"
                        ) from exc
                    if not isinstance(payload, Mapping):
                        raise UniProtKbMetadataError(
                            f"UniProtKB metadata page {next_url} was not a JSON object"
                        )
                    results = payload.get("results")
                    if not isinstance(results, list):
                        raise UniProtKbMetadataError(
                            f"UniProtKB metadata page {next_url} had no results list"
                        )
                    for result in results:
                        if isinstance(result, Mapping):
                            yield result
                    next_url = _next_link(response)
                    params = None


def collect_uniprotkb_metadata(
    entries: Iterable[Mapping[str, Any]],
) -> list[UniProtKbMetadataRow]:
    """Normalize UniProtKB entries into sorted accession-keyed metadata rows."""

    rows: list[UniProtKbMetadataRow] = []
    seen: set[str] = set()
    for entry in entries:
        row = row_from_uniprotkb_entry(entry)
        if row is None or row.uniprot_accession in seen:
            continue
        seen.add(row.uniprot_accession)
        rows.append(row)
    return sorted(rows, key=lambda row: row.uniprot_accession)


def row_from_uniprotkb_entry(
    entry: Mapping[str, Any],
) -> UniProtKbMetadataRow | None:
    """Return normalized UniProtKB metadata, or ``None`` if malformed."""

    accession = _string(entry.get("primaryAccession"))
    if not accession:
        return None

    organism = _mapping(entry.get("organism"))

    return UniProtKbMetadataRow(
        uniprot_accession=accession,
        uniprot_id=_string(entry.get("uniProtkbId")),
        reviewed=_reviewed(entry.get("entryType")),
        protein_name=_protein_name(entry.get("proteinDescription")),
        taxon_id=_string(organism.get("taxonId")),
        organism=_string(organism.get("scientificName")),
        proteome_ids=_proteome_ids(entry.get("uniProtKBCrossReferences")),
    )


def render_uniprotkb_metadata_tsv(rows: Iterable[UniProtKbMetadataRow]) -> str:
    """Render UniProtKB metadata rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=UNIPROTKB_METADATA_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_uniprotkb_metadata_json(rows: Iterable[UniProtKbMetadataRow]) -> str:
    """Render UniProtKB metadata rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def _protein_name(value: object) -> str:
    description = _mapping(value)
    recommended_name = _mapping(description.get("recommendedName"))
    full_name = _mapping(recommended_name.get("fullName"))
    name = _string(full_name.get("value"))
    if name:
        return name

    submission_names = description.get("submissionNames")
    if isinstance(submission_names, list):
        for submission_name in submission_names:
            full_name = _mapping(_mapping(submission_name).get("fullName"))
            name = _string(full_name.get("value"))
            if name:
                return name
    return ""


def _proteome_ids(value: object) -> tuple[str, ...]:
    if not isinstance(value, list):
        return ()

    proteome_ids: list[str] = []
    seen: set[str] = set()
    for cross_reference in value:
        if not isinstance(cross_reference, Mapping):
            continue
        if cross_reference.get("database") != "Proteomes":
            continue
        proteome_id = _string(cross_reference.get("id"))
        if proteome_id and proteome_id not in seen:
            seen.add(proteome_id)
            proteome_ids.append(proteome_id)
    return tuple(proteome_ids)


def _reviewed(value: object) -> bool | None:
    entry_type = _string(value).lower()
    if "unreviewed" in entry_type:
        return False
    if "reviewed" in entry_type:
        return True
    return None


def _next_link(response: httpx.Response) -> str | None:
    next_link = response.links.get("next")
    if not isinstance(next_link, Mapping):
        return None
    next_url = next_link.get("url")
    return next_url if isinstance(next_url, str) and next_url else None


def _unique_accessions(accessions: Iterable[str]) -> list[str]:
    unique: list[str] = []
    seen: set[str] = set()
    for accession in accessions:
        if not accession or accession in seen:
            continue
        seen.add(accession)
        unique.append(accession)
    return unique


def _chunked(items: Sequence[str], size: int) -> Iterable[list[str]]:
    for offset in range(0, len(items), size):
        yield list(items[offset : offset + size])


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _string(value: object) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, int):
        return str(value)
    return ""
