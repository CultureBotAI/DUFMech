"""Expand Pfam families to MGnify Proteins representatives."""

from __future__ import annotations

import csv
import io
import json
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from typing import Any

import httpx

MGNIFY_PROTEINS_BASE_URL = "https://www.ebi.ac.uk/metagenomics/proteins/api/v1"
MGNIFY_PROTEIN_SEARCH_URL = f"{MGNIFY_PROTEINS_BASE_URL}/protein/search"
MGNIFY_PROTEIN_URL = f"{MGNIFY_PROTEINS_BASE_URL}/protein/{{mgyp}}"

MGNIFY_TSV_FIELDNAMES = [
    "pfam_id",
    "mgyp",
    "full_length",
    "cluster_size",
    "sequence_length",
    "biome_ids",
    "biome_names",
    "biome_counts",
    "pfam_match_count",
    "pfam_match_ranges",
    "source_url",
]


class MGnifyProteinClientError(RuntimeError):
    """Raised when MGnify Proteins returns an invalid or failing response."""


@dataclass(frozen=True)
class MgnifyProteinRow:
    """One MGnify cluster representative carrying a Pfam family."""

    pfam_id: str
    mgyp: str
    full_length: bool | None
    cluster_size: int | None
    sequence_length: int | None
    biome_ids: tuple[int, ...]
    biome_names: tuple[str, ...]
    biome_counts: tuple[int, ...]
    pfam_match_count: int
    pfam_match_ranges: tuple[str, ...]

    @property
    def source_url(self) -> str:
        return MGNIFY_PROTEIN_URL.format(mgyp=self.mgyp)

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["biome_ids"] = ";".join(str(item) for item in self.biome_ids)
        row["biome_names"] = ";".join(self.biome_names)
        row["biome_counts"] = ";".join(str(item) for item in self.biome_counts)
        row["pfam_match_ranges"] = ";".join(self.pfam_match_ranges)
        row["source_url"] = self.source_url
        return row


class MGnifyProteinClient:
    """Small client for the MGnify Proteins Pfam search API."""

    def __init__(
        self,
        *,
        timeout: float = 30.0,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self.timeout = timeout
        self.transport = transport

    def search_pfam(
        self,
        pfam_id: str,
        *,
        limit: int = 50,
    ) -> Iterable[Mapping[str, Any]]:
        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=True,
            transport=self.transport,
        ) as client:
            response = client.get(
                MGNIFY_PROTEIN_SEARCH_URL,
                params={"pfam_accession": pfam_id, "limit": str(limit)},
            )
            try:
                response.raise_for_status()
                payload = response.json()
            except (httpx.HTTPError, ValueError) as exc:
                raise MGnifyProteinClientError(
                    f"could not search MGnify Proteins for {pfam_id}"
                ) from exc
            if not isinstance(payload, list):
                raise MGnifyProteinClientError(
                    f"MGnify Proteins search for {pfam_id} was not a JSON list"
                )
            for hit in payload:
                if isinstance(hit, Mapping):
                    yield hit

    def fetch_protein(self, mgyp: str) -> Mapping[str, Any]:
        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=True,
            transport=self.transport,
        ) as client:
            response = client.get(MGNIFY_PROTEIN_URL.format(mgyp=mgyp))
            try:
                response.raise_for_status()
                payload = response.json()
            except (httpx.HTTPError, ValueError) as exc:
                raise MGnifyProteinClientError(
                    f"could not fetch MGnify Proteins representative {mgyp}"
                ) from exc
            if not isinstance(payload, Mapping):
                raise MGnifyProteinClientError(
                    f"MGnify Proteins representative {mgyp} was not a JSON object"
                )
            return payload


def collect_pfam_mgnify_rows(
    pfam_ids: Iterable[str],
    client: MGnifyProteinClient,
    *,
    limit_proteins_per_family: int = 50,
) -> list[MgnifyProteinRow]:
    """Collect MGnify Proteins representatives for a stable Pfam family list."""

    rows: list[MgnifyProteinRow] = []
    seen_pfams: set[str] = set()
    seen_rows: set[tuple[str, str]] = set()
    for pfam_id in pfam_ids:
        if pfam_id in seen_pfams:
            continue
        seen_pfams.add(pfam_id)
        for hit in client.search_pfam(pfam_id, limit=limit_proteins_per_family):
            mgyp = _string(hit.get("mgyp"))
            if not mgyp:
                continue
            row = row_from_mgnify_protein(pfam_id, hit, client.fetch_protein(mgyp))
            if row is None or (row.pfam_id, row.mgyp) in seen_rows:
                continue
            seen_rows.add((row.pfam_id, row.mgyp))
            rows.append(row)
    return sorted(rows, key=lambda row: (row.pfam_id, row.mgyp))


def row_from_mgnify_protein(
    pfam_id: str,
    hit: Mapping[str, Any],
    protein: Mapping[str, Any],
) -> MgnifyProteinRow | None:
    """Return a normalized MGnify representative row, or ``None`` if malformed."""

    mgyp = _string(protein.get("mgyp")) or _string(hit.get("mgyp"))
    if not mgyp:
        return None

    sequence = protein.get("sequence")
    biomes = _biomes(protein.get("biomes"))
    match_ranges = _pfam_match_ranges(pfam_id, protein.get("pfam_annotations"))

    return MgnifyProteinRow(
        pfam_id=pfam_id,
        mgyp=mgyp,
        full_length=_bool(protein.get("full_length"), hit.get("full_length")),
        cluster_size=_int(protein.get("cluster_size"), hit.get("cluster_size")),
        sequence_length=len(sequence) if isinstance(sequence, str) else None,
        biome_ids=tuple(biome[0] for biome in biomes),
        biome_names=tuple(biome[1] for biome in biomes),
        biome_counts=tuple(biome[2] for biome in biomes),
        pfam_match_count=len(match_ranges),
        pfam_match_ranges=match_ranges,
    )


def render_mgnify_tsv(rows: Iterable[MgnifyProteinRow]) -> str:
    """Render MGnify representative rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=MGNIFY_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_mgnify_json(rows: Iterable[MgnifyProteinRow]) -> str:
    """Render MGnify representative rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def _biomes(value: object) -> tuple[tuple[int, str, int], ...]:
    if not isinstance(value, list):
        return ()

    rows: list[tuple[int, str, int]] = []
    for biome in value:
        if not isinstance(biome, Mapping):
            continue
        biome_id = _int(biome.get("id"))
        biome_name = _string(biome.get("name"))
        biome_count = _int(biome.get("count"))
        if biome_id is not None and biome_name and biome_count is not None:
            rows.append((biome_id, biome_name, biome_count))
    return tuple(rows)


def _pfam_match_ranges(pfam_id: str, value: object) -> tuple[str, ...]:
    if not isinstance(value, list):
        return ()

    ranges: list[str] = []
    for annotation in value:
        if not isinstance(annotation, Mapping):
            continue
        if annotation.get("accession") != pfam_id:
            continue
        start = _int(annotation.get("env_start"))
        end = _int(annotation.get("env_end"))
        if start is not None and end is not None:
            ranges.append(f"{start}-{end}")
    return tuple(ranges)


def _bool(*values: object) -> bool | None:
    for value in values:
        if type(value) is bool:
            return value
    return None


def _int(*values: object) -> int | None:
    for value in values:
        if type(value) is int:
            return value
    return None


def _string(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""
