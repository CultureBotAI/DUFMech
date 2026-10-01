"""Expand Pfam families to UniProtKB protein members."""

from __future__ import annotations

import csv
import io
import json
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from typing import Any

import httpx

INTERPRO_PFAM_PROTEINS_URL = (
    "https://www.ebi.ac.uk/interpro/api/protein/UniProt/entry/pfam/{pfam_id}/"
)

MEMBER_TSV_FIELDNAMES = [
    "pfam_id",
    "uniprot_accession",
    "name",
    "source_database",
    "length",
    "taxon_id",
    "organism",
    "gene",
    "in_alphafold",
    "match_count",
    "match_ranges",
    "source_url",
]


class InterProProteinClientError(RuntimeError):
    """Raised when InterPro returns an invalid or failing protein response."""


@dataclass(frozen=True)
class PfamProteinMemberRow:
    """One UniProtKB protein member matched to a Pfam family."""

    pfam_id: str
    uniprot_accession: str
    name: str
    source_database: str
    length: int | None
    taxon_id: str
    organism: str
    gene: str
    in_alphafold: bool | None
    match_count: int
    match_ranges: tuple[str, ...]

    @property
    def source_url(self) -> str:
        return f"https://www.ebi.ac.uk/interpro/protein/UniProt/{self.uniprot_accession}/"

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["match_ranges"] = ";".join(self.match_ranges)
        row["source_url"] = self.source_url
        return row


class InterProPfamProteinClient:
    """Small client for InterPro Pfam-to-UniProt member pages."""

    def __init__(
        self,
        *,
        timeout: float = 30.0,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self.timeout = timeout
        self.transport = transport

    def iter_proteins(
        self,
        pfam_id: str,
        *,
        page_size: int = 200,
    ) -> Iterable[Mapping[str, Any]]:
        next_url: str | None = INTERPRO_PFAM_PROTEINS_URL.format(pfam_id=pfam_id)
        params: dict[str, str] | None = {"page_size": str(page_size)}

        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=True,
            transport=self.transport,
        ) as client:
            while next_url:
                response = client.get(next_url, params=params)
                try:
                    response.raise_for_status()
                    payload = response.json()
                except (httpx.HTTPError, ValueError) as exc:
                    raise InterProProteinClientError(
                        f"could not fetch InterPro protein page {next_url}"
                    ) from exc
                if not isinstance(payload, dict):
                    raise InterProProteinClientError(
                        f"InterPro protein page {next_url} was not a JSON object"
                    )
                results = payload.get("results")
                if not isinstance(results, list):
                    raise InterProProteinClientError(
                        f"InterPro protein page {next_url} had no results list"
                    )
                for result in results:
                    if isinstance(result, Mapping):
                        yield result
                raw_next = payload.get("next")
                next_url = raw_next if isinstance(raw_next, str) and raw_next else None
                params = None


def collect_members(
    pfam_id: str,
    proteins: Iterable[Mapping[str, Any]],
    *,
    limit: int | None = None,
) -> list[PfamProteinMemberRow]:
    """Normalize InterPro proteins into sorted Pfam-to-UniProt rows."""

    rows: list[PfamProteinMemberRow] = []
    seen: set[str] = set()
    for protein in proteins:
        row = row_from_interpro_protein(pfam_id, protein)
        if row is None or row.uniprot_accession in seen:
            continue
        seen.add(row.uniprot_accession)
        rows.append(row)
        if limit is not None and len(rows) >= limit:
            break
    return sorted(rows, key=lambda row: row.uniprot_accession)


def row_from_interpro_protein(
    pfam_id: str,
    protein: Mapping[str, Any],
) -> PfamProteinMemberRow | None:
    """Return a normalized UniProtKB member row, or ``None`` if malformed."""

    metadata = _mapping(protein.get("metadata"))
    accession = _string(metadata.get("accession"))
    if not accession:
        return None

    organism = _mapping(metadata.get("source_organism"))
    organism_name = _string(organism.get("scientificName")) or _string(
        organism.get("fullName")
    )
    match_count, match_ranges = _match_summary(pfam_id, protein.get("entries"))

    return PfamProteinMemberRow(
        pfam_id=pfam_id,
        uniprot_accession=accession,
        name=_string(metadata.get("name")),
        source_database=_string(metadata.get("source_database")),
        length=_int(metadata.get("length")),
        taxon_id=_string(organism.get("taxId")),
        organism=organism_name,
        gene=_string(metadata.get("gene")),
        in_alphafold=_bool(metadata.get("in_alphafold")),
        match_count=match_count,
        match_ranges=match_ranges,
    )


def render_members_tsv(rows: Iterable[PfamProteinMemberRow]) -> str:
    """Render member rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=MEMBER_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_members_json(rows: Iterable[PfamProteinMemberRow]) -> str:
    """Render member rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def _match_summary(pfam_id: str, entries: object) -> tuple[int, tuple[str, ...]]:
    if not isinstance(entries, list):
        return (0, ())

    match_count = 0
    ranges: list[str] = []
    for entry in entries:
        if not isinstance(entry, Mapping) or entry.get("accession") != pfam_id:
            continue
        locations = entry.get("entry_protein_locations")
        if not isinstance(locations, list):
            continue
        for location in locations:
            if not isinstance(location, Mapping):
                continue
            fragments = location.get("fragments")
            if not isinstance(fragments, list):
                continue
            location_ranges: list[str] = []
            for fragment in fragments:
                start, end = _fragment_bounds(fragment)
                if start is not None and end is not None:
                    location_ranges.append(f"{start}-{end}")
            if location_ranges:
                match_count += 1
                ranges.extend(location_ranges)
    return (match_count, tuple(ranges))


def _fragment_bounds(fragment: object) -> tuple[int | None, int | None]:
    if not isinstance(fragment, Mapping):
        return (None, None)
    return (_int(fragment.get("start")), _int(fragment.get("end")))


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _int(value: object) -> int | None:
    return value if type(value) is int else None


def _bool(value: object) -> bool | None:
    return value if type(value) is bool else None


def _string(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""
