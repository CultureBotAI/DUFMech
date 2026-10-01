"""Fetch PDBe-KB structure annotations for RCSB PDB polymer entities."""

from __future__ import annotations

import csv
import io
import json
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import asdict, dataclass
from typing import Any

import httpx

PDBE_KB_BASE_URL = "https://www.ebi.ac.uk/pdbe/api/pdb/entry"
PDBE_KB_ENDPOINTS = (
    "uniprot_mapping",
    "binding_sites",
    "interfaces",
    "domains",
    "annotations",
)
PDBE_KB_ENDPOINT_URL = PDBE_KB_BASE_URL + "/{endpoint}/{pdb_id}/{entity_id}"

PDBE_KB_TSV_FIELDNAMES = [
    "seed_uniprot_accession",
    "pdb_id",
    "entity_id",
    "endpoint",
    "page_data_type",
    "annotation_data_type",
    "annotation_name",
    "annotation_accession",
    "best_chain_id",
    "start_index",
    "end_index",
    "uniprot_start",
    "uniprot_end",
    "start_code",
    "end_code",
    "index_type",
    "group_label",
    "detail_id",
    "bound_molecule_id",
    "resource_url",
    "confidence_level",
    "confidence_score",
    "raw_score",
    "mutation",
    "pdb_code",
    "group_additional_data",
    "residue_additional_data",
    "source_url",
]


class PdbeKbClientError(RuntimeError):
    """Raised when PDBe-KB returns an invalid or failing response."""


@dataclass(frozen=True)
class PdbeKbSeed:
    """One PDB polymer entity from a UniProt/RCSB PDB snapshot."""

    uniprot_accession: str
    pdb_id: str
    entity_id: str

    @property
    def key(self) -> tuple[str, str, str]:
        return (self.uniprot_accession, self.pdb_id.lower(), self.entity_id)


@dataclass(frozen=True)
class PdbeKbAnnotationRow:
    """One PDBe-KB annotation residue span for a PDB polymer entity."""

    seed_uniprot_accession: str
    pdb_id: str
    entity_id: str
    endpoint: str
    page_data_type: str
    annotation_data_type: str
    annotation_name: str
    annotation_accession: str
    best_chain_id: str
    start_index: int | None
    end_index: int | None
    uniprot_start: int | None
    uniprot_end: int | None
    start_code: str
    end_code: str
    index_type: str
    group_label: str
    detail_id: str
    bound_molecule_id: str
    resource_url: str
    confidence_level: str
    confidence_score: float | None
    raw_score: float | None
    mutation: bool | None
    pdb_code: str
    group_additional_data: str
    residue_additional_data: str

    @property
    def source_url(self) -> str:
        return PDBE_KB_ENDPOINT_URL.format(
            endpoint=self.endpoint,
            pdb_id=self.pdb_id.lower(),
            entity_id=self.entity_id,
        )

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["source_url"] = self.source_url
        return row


class PdbeKbClient:
    """Small client for PDBe API entity annotation endpoints."""

    def __init__(
        self,
        *,
        timeout: float = 30.0,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self.timeout = timeout
        self.transport = transport

    def fetch_entity_endpoint(
        self,
        pdb_id: str,
        entity_id: str,
        endpoint: str,
    ) -> Mapping[str, Any]:
        url = PDBE_KB_ENDPOINT_URL.format(
            endpoint=endpoint,
            pdb_id=pdb_id.lower(),
            entity_id=entity_id,
        )
        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=True,
            transport=self.transport,
        ) as client:
            response = client.get(url)
            if response.status_code in (204, 404):
                return {}
            try:
                response.raise_for_status()
                payload = response.json()
            except (httpx.HTTPError, ValueError) as exc:
                raise PdbeKbClientError(
                    f"could not fetch PDBe-KB {endpoint} for {pdb_id}/{entity_id}"
                ) from exc

        if not isinstance(payload, Mapping):
            raise PdbeKbClientError(
                f"PDBe-KB {endpoint} for {pdb_id}/{entity_id} "
                "was not a JSON object"
            )
        return payload


def collect_pdbe_kb_rows(
    seeds: Iterable[PdbeKbSeed],
    client: PdbeKbClient,
    *,
    endpoints: Sequence[str] = PDBE_KB_ENDPOINTS,
) -> list[PdbeKbAnnotationRow]:
    """Collect PDBe-KB annotation rows for ordered, unique PDB entities."""

    rows: list[PdbeKbAnnotationRow] = []
    seen_seeds: set[tuple[str, str, str]] = set()
    seen_rows: set[tuple[object, ...]] = set()
    for seed in seeds:
        if not seed.pdb_id or not seed.entity_id or seed.key in seen_seeds:
            continue
        seen_seeds.add(seed.key)
        for endpoint in endpoints:
            payload = client.fetch_entity_endpoint(
                seed.pdb_id,
                seed.entity_id,
                endpoint,
            )
            for row in rows_from_pdbe_kb_payload(seed, endpoint, payload):
                key = tuple(row.tsv_row().values())
                if key in seen_rows:
                    continue
                seen_rows.add(key)
                rows.append(row)

    return sorted(
        rows,
        key=lambda row: (
            row.seed_uniprot_accession,
            row.pdb_id,
            row.entity_id,
            row.endpoint,
            row.annotation_data_type,
            row.annotation_accession,
            row.start_index or 0,
            row.end_index or 0,
            row.group_label,
            row.bound_molecule_id,
            row.detail_id,
        ),
    )


def rows_from_pdbe_kb_payload(
    seed: PdbeKbSeed,
    endpoint: str,
    payload: Mapping[str, Any],
) -> list[PdbeKbAnnotationRow]:
    """Return normalized PDBe-KB rows from an entity endpoint payload."""

    entry = _pdb_entry_payload(seed.pdb_id, payload)
    page_data_type = _string(entry.get("dataType"))
    rows: list[PdbeKbAnnotationRow] = []
    for annotation in _as_list(entry.get("data")):
        if not isinstance(annotation, Mapping):
            continue

        group_additional = _mapping(annotation.get("additionalData"))
        annotation_name = _string(annotation.get("name"))
        annotation_accession = _string(annotation.get("accession"))
        annotation_data_type = _string(annotation.get("dataType"))
        best_chain_id = _string(group_additional.get("bestChainId"))
        group_additional_data = _compact_json(group_additional)

        for residue in _as_list(annotation.get("residues")):
            if not isinstance(residue, Mapping):
                continue
            residue_additional = _mapping(residue.get("additionalData"))
            rows.append(
                PdbeKbAnnotationRow(
                    seed_uniprot_accession=seed.uniprot_accession,
                    pdb_id=seed.pdb_id.upper(),
                    entity_id=seed.entity_id,
                    endpoint=endpoint,
                    page_data_type=page_data_type,
                    annotation_data_type=annotation_data_type,
                    annotation_name=annotation_name,
                    annotation_accession=annotation_accession,
                    best_chain_id=best_chain_id,
                    start_index=_int(residue.get("startIndex")),
                    end_index=_int(residue.get("endIndex")),
                    uniprot_start=_int(residue.get("unpStartIndex")),
                    uniprot_end=_int(residue.get("unpEndIndex")),
                    start_code=_string(residue.get("startCode")),
                    end_code=_string(residue.get("endCode")),
                    index_type=_string(residue.get("indexType")),
                    group_label=_string(residue_additional.get("groupLabel")),
                    detail_id=_detail_id(residue_additional),
                    bound_molecule_id=_string(
                        residue_additional.get("boundMoleculeId")
                    ),
                    resource_url=_string(residue_additional.get("resourceUrl")),
                    confidence_level=_string(
                        residue_additional.get("confidenceLevel")
                    ),
                    confidence_score=_float(
                        residue_additional.get("confidenceScore")
                    ),
                    raw_score=_float(residue_additional.get("rawScore")),
                    mutation=_bool(residue.get("mutation")),
                    pdb_code=_string(residue.get("pdbCode")),
                    group_additional_data=group_additional_data,
                    residue_additional_data=_compact_json(residue_additional),
                )
            )

    return rows


def render_pdbe_kb_tsv(rows: Iterable[PdbeKbAnnotationRow]) -> str:
    """Render PDBe-KB rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=PDBE_KB_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_pdbe_kb_json(rows: Iterable[PdbeKbAnnotationRow]) -> str:
    """Render PDBe-KB rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def _pdb_entry_payload(
    pdb_id: str,
    payload: Mapping[str, Any],
) -> Mapping[str, Any]:
    for key in (pdb_id.lower(), pdb_id.upper(), pdb_id):
        entry = payload.get(key)
        if isinstance(entry, Mapping):
            return entry
    for key, entry in payload.items():
        if isinstance(key, str) and key.lower() == pdb_id.lower():
            return _mapping(entry)
    return {}


def _detail_id(additional_data: Mapping[str, Any]) -> str:
    for key in ("domainId", "domain", "cofactorId", "ordinalId"):
        detail = _string(additional_data.get(key))
        if detail:
            return detail
    return ""


def _as_list(value: object) -> list[Any]:
    return value if isinstance(value, list) else []


def _bool(value: object) -> bool | None:
    return value if type(value) is bool else None


def _compact_json(value: Mapping[str, Any]) -> str:
    if not value:
        return ""
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def _float(value: object) -> float | None:
    return float(value) if type(value) in (float, int) else None


def _int(value: object) -> int | None:
    return value if type(value) is int else None


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _string(value: object) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, int | float):
        return str(value)
    return ""
