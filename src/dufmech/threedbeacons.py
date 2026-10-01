"""Fetch 3D-Beacons structural coverage summaries for UniProt accessions."""

from __future__ import annotations

import csv
import io
import json
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from typing import Any

import httpx

THREEDBEACONS_API_URL = (
    "https://www.ebi.ac.uk/pdbe/pdbe-kb/3dbeacons/api/uniprot/summary"
)

THREEDBEACONS_TSV_FIELDNAMES = [
    "uniprot_accession",
    "uniprot_id",
    "uniprot_checksum",
    "sequence_length",
    "segment_start",
    "segment_end",
    "model_identifier",
    "model_category",
    "provider",
    "model_format",
    "model_type",
    "model_url",
    "model_page_url",
    "created",
    "sequence_identity",
    "uniprot_start",
    "uniprot_end",
    "coverage",
    "experimental_method",
    "resolution",
    "confidence_type",
    "confidence_version",
    "confidence_avg_local_score",
    "oligomeric_state",
    "preferred_assembly_id",
    "polymer_identifiers",
    "non_polymer_identifiers",
    "source_url",
]


class ThreeDBeaconsClientError(RuntimeError):
    """Raised when 3D-Beacons returns an invalid or failing response."""


@dataclass(frozen=True)
class ThreeDBeaconsStructureRow:
    """One 3D-Beacons model or structure summary for a UniProt accession."""

    uniprot_accession: str
    uniprot_id: str
    uniprot_checksum: str
    sequence_length: int | None
    segment_start: int | None
    segment_end: int | None
    model_identifier: str
    model_category: str
    provider: str
    model_format: str
    model_type: str
    model_url: str
    model_page_url: str
    created: str
    sequence_identity: float | None
    uniprot_start: int | None
    uniprot_end: int | None
    coverage: float | None
    experimental_method: str
    resolution: float | None
    confidence_type: str
    confidence_version: str
    confidence_avg_local_score: float | None
    oligomeric_state: str
    preferred_assembly_id: str
    polymer_identifiers: tuple[str, ...]
    non_polymer_identifiers: tuple[str, ...]

    @property
    def source_url(self) -> str:
        return self.model_page_url or self.model_url

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["polymer_identifiers"] = ";".join(self.polymer_identifiers)
        row["non_polymer_identifiers"] = ";".join(self.non_polymer_identifiers)
        row["source_url"] = self.source_url
        return row


class ThreeDBeaconsClient:
    """Small client for the 3D-Beacons Network UniProt summary API."""

    def __init__(
        self,
        *,
        timeout: float = 30.0,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self.timeout = timeout
        self.transport = transport

    def summary(self, accession: str) -> Mapping[str, Any]:
        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=True,
            transport=self.transport,
        ) as client:
            response = client.get(f"{THREEDBEACONS_API_URL}/{accession}.json")
            if response.status_code == 404:
                return {"structures": []}
            try:
                response.raise_for_status()
                payload = response.json()
            except (httpx.HTTPError, ValueError) as exc:
                raise ThreeDBeaconsClientError(
                    f"could not fetch 3D-Beacons summary for {accession}"
                ) from exc

        if not isinstance(payload, Mapping):
            raise ThreeDBeaconsClientError(
                f"3D-Beacons summary for {accession} was not a JSON object"
            )
        return payload


def collect_threedbeacons_rows(
    accessions: Iterable[str],
    client: ThreeDBeaconsClient,
) -> list[ThreeDBeaconsStructureRow]:
    """Collect 3D-Beacons rows for ordered, unique UniProt accessions."""

    rows: list[ThreeDBeaconsStructureRow] = []
    seen_accessions: set[str] = set()
    seen_rows: set[tuple[str, str, str, int | None, int | None]] = set()
    for accession in accessions:
        accession = _string(accession)
        if not accession or accession in seen_accessions:
            continue
        seen_accessions.add(accession)
        for row in rows_from_threedbeacons_payload(accession, client.summary(accession)):
            key = (
                row.uniprot_accession,
                row.provider,
                row.model_identifier,
                row.uniprot_start,
                row.uniprot_end,
            )
            if key in seen_rows:
                continue
            seen_rows.add(key)
            rows.append(row)

    return sorted(
        rows,
        key=lambda row: (
            row.uniprot_accession,
            row.provider,
            row.model_identifier,
            row.uniprot_start or 0,
            row.uniprot_end or 0,
        ),
    )


def rows_from_threedbeacons_payload(
    accession: str,
    payload: Mapping[str, Any],
) -> list[ThreeDBeaconsStructureRow]:
    """Return normalized 3D-Beacons rows from one UniProt summary payload."""

    structures = payload.get("structures")
    if not isinstance(structures, list):
        raise ThreeDBeaconsClientError(
            f"3D-Beacons summary for {accession} had no structures list"
        )

    entry = _mapping(payload.get("uniprot_entry"))
    rows: list[ThreeDBeaconsStructureRow] = []
    for structure in structures:
        if not isinstance(structure, Mapping):
            continue
        summary = _mapping(structure.get("summary"))
        row = row_from_threedbeacons_summary(accession, entry, summary)
        if row is not None:
            rows.append(row)
    return rows


def row_from_threedbeacons_summary(
    accession: str,
    entry: Mapping[str, Any],
    summary: Mapping[str, Any],
) -> ThreeDBeaconsStructureRow | None:
    """Return one normalized structure summary, or ``None`` if malformed."""

    model_identifier = _string(summary.get("model_identifier"))
    provider = _string(summary.get("provider"))
    if not model_identifier or not provider:
        return None

    entities = summary.get("entities")

    return ThreeDBeaconsStructureRow(
        uniprot_accession=accession,
        uniprot_id=_string(entry.get("id")),
        uniprot_checksum=_string(entry.get("uniprot_checksum")),
        sequence_length=_int(entry.get("sequence_length")),
        segment_start=_int(entry.get("segment_start")),
        segment_end=_int(entry.get("segment_end")),
        model_identifier=model_identifier,
        model_category=_string(summary.get("model_category")),
        provider=provider,
        model_format=_string(summary.get("model_format")),
        model_type=_string(summary.get("model_type")),
        model_url=_string(summary.get("model_url")),
        model_page_url=_string(summary.get("model_page_url")),
        created=_string(summary.get("created")),
        sequence_identity=_float(summary.get("sequence_identity")),
        uniprot_start=_int(summary.get("uniprot_start")),
        uniprot_end=_int(summary.get("uniprot_end")),
        coverage=_float(summary.get("coverage")),
        experimental_method=_string(summary.get("experimental_method")),
        resolution=_float(summary.get("resolution")),
        confidence_type=_string(summary.get("confidence_type")),
        confidence_version=_string(summary.get("confidence_version")),
        confidence_avg_local_score=_float(
            summary.get("confidence_avg_local_score")
        ),
        oligomeric_state=_string(summary.get("oligomeric_state")),
        preferred_assembly_id=_string(summary.get("preferred_assembly_id")),
        polymer_identifiers=_entity_identifiers(entities, "POLYMER"),
        non_polymer_identifiers=_entity_identifiers(entities, "NON-POLYMER"),
    )


def render_threedbeacons_tsv(rows: Iterable[ThreeDBeaconsStructureRow]) -> str:
    """Render 3D-Beacons rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=THREEDBEACONS_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_threedbeacons_json(rows: Iterable[ThreeDBeaconsStructureRow]) -> str:
    """Render 3D-Beacons rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def _entity_identifiers(value: object, entity_type: str) -> tuple[str, ...]:
    if not isinstance(value, list):
        return ()

    identifiers: list[str] = []
    seen: set[str] = set()
    for entity in value:
        if not isinstance(entity, Mapping):
            continue
        if _string(entity.get("entity_type")) != entity_type:
            continue

        category = _string(entity.get("identifier_category")) or entity_type
        identifier = _string(entity.get("identifier")) or _string(
            entity.get("description")
        )
        if not identifier:
            continue
        label = f"{category}:{identifier}"
        if label in seen:
            continue
        seen.add(label)
        identifiers.append(label)

    return tuple(identifiers)


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _int(value: object) -> int | None:
    return value if isinstance(value, int) and not isinstance(value, bool) else None


def _float(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int | float):
        return float(value)
    return None


def _string(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""
