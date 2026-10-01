"""Fetch RCSB PDB experimental structure evidence for UniProt accessions."""

from __future__ import annotations

import csv
import io
import json
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from typing import Any

import httpx

RCSB_SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v2/query"
RCSB_GRAPHQL_URL = "https://data.rcsb.org/graphql"

RCSB_POLYMER_ENTITY_QUERY = """
query($ids:[String!]!) {
  polymer_entities(entity_ids:$ids) {
    rcsb_id
    rcsb_polymer_entity_container_identifiers {
      entry_id
      entity_id
      auth_asym_ids
      reference_sequence_identifiers {
        database_name
        database_accession
      }
    }
    entity_poly {
      pdbx_strand_id
      rcsb_entity_polymer_type
      rcsb_sample_sequence_length
    }
    rcsb_entity_source_organism {
      ncbi_taxonomy_id
      ncbi_scientific_name
    }
    rcsb_polymer_entity_name_com {
      name
    }
    entry {
      rcsb_entry_info {
        experimental_method
        resolution_combined
      }
    }
  }
}
"""

RCSB_TSV_FIELDNAMES = [
    "uniprot_accession",
    "pdb_id",
    "entity_id",
    "rcsb_id",
    "experimental_method",
    "resolution",
    "polymer_type",
    "sequence_length",
    "chain_ids",
    "taxon_id",
    "organism",
    "entity_names",
    "reference_accessions",
    "source_url",
]


class RcsbPdbClientError(RuntimeError):
    """Raised when RCSB PDB returns an invalid or failing response."""


@dataclass(frozen=True)
class RcsbPdbRow:
    """One RCSB PDB polymer entity cross-referenced to a UniProt accession."""

    uniprot_accession: str
    pdb_id: str
    entity_id: str
    rcsb_id: str
    experimental_method: str
    resolution: float | None
    polymer_type: str
    sequence_length: int | None
    chain_ids: tuple[str, ...]
    taxon_id: str
    organism: str
    entity_names: tuple[str, ...]
    reference_accessions: tuple[str, ...]

    @property
    def source_url(self) -> str:
        return f"https://www.rcsb.org/structure/{self.pdb_id}"

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["chain_ids"] = ";".join(self.chain_ids)
        row["entity_names"] = ";".join(self.entity_names)
        row["reference_accessions"] = ";".join(self.reference_accessions)
        row["source_url"] = self.source_url
        return row


class RcsbPdbClient:
    """Small client for RCSB Search and Data APIs."""

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
    ) -> list[str]:
        body = {
            "query": {
                "type": "terminal",
                "service": "text",
                "parameters": {
                    "attribute": (
                        "rcsb_polymer_entity_container_identifiers."
                        "reference_sequence_identifiers.database_accession"
                    ),
                    "operator": "exact_match",
                    "value": accession,
                },
            },
            "return_type": "polymer_entity",
            "request_options": {
                "paginate": {
                    "start": 0,
                    "rows": limit,
                }
            },
        }
        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=True,
            transport=self.transport,
        ) as client:
            response = client.post(RCSB_SEARCH_URL, json=body)
            if response.status_code in (204, 404):
                return []
            try:
                response.raise_for_status()
                payload = response.json()
            except (httpx.HTTPError, ValueError) as exc:
                raise RcsbPdbClientError(
                    f"could not search RCSB PDB for {accession}"
                ) from exc

        if not isinstance(payload, Mapping):
            raise RcsbPdbClientError(
                f"RCSB PDB search for {accession} was not a JSON object"
            )
        result_set = payload.get("result_set")
        if not isinstance(result_set, list):
            return []

        entity_ids: list[str] = []
        for result in result_set:
            if not isinstance(result, Mapping):
                continue
            entity_id = _string(result.get("identifier"))
            if entity_id:
                entity_ids.append(entity_id)
        return entity_ids

    def fetch_polymer_entities(
        self,
        entity_ids: Iterable[str],
    ) -> Iterable[Mapping[str, Any]]:
        ids = list(entity_ids)
        if not ids:
            return

        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=True,
            transport=self.transport,
        ) as client:
            response = client.post(
                RCSB_GRAPHQL_URL,
                json={
                    "query": RCSB_POLYMER_ENTITY_QUERY,
                    "variables": {"ids": ids},
                },
            )
            try:
                response.raise_for_status()
                payload = response.json()
            except (httpx.HTTPError, ValueError) as exc:
                raise RcsbPdbClientError(
                    "could not fetch RCSB PDB polymer entities"
                ) from exc
        if not isinstance(payload, Mapping):
            raise RcsbPdbClientError("RCSB PDB GraphQL result was not a JSON object")
        errors = payload.get("errors")
        if isinstance(errors, list) and errors:
            raise RcsbPdbClientError("; ".join(str(error) for error in errors))
        data = payload.get("data")
        if not isinstance(data, Mapping):
            raise RcsbPdbClientError("RCSB PDB GraphQL result had no data object")
        entities = data.get("polymer_entities")
        if not isinstance(entities, list):
            raise RcsbPdbClientError(
                "RCSB PDB GraphQL result had no polymer_entities list"
            )
        for entity in entities:
            if isinstance(entity, Mapping):
                yield entity


def collect_rcsb_pdb_rows(
    accessions: Iterable[str],
    client: RcsbPdbClient,
    *,
    limit_entities_per_accession: int = 50,
) -> list[RcsbPdbRow]:
    """Collect RCSB PDB polymer entities for ordered, unique UniProt accessions."""

    rows: list[RcsbPdbRow] = []
    seen_accessions: set[str] = set()
    seen_rows: set[tuple[str, str]] = set()
    for accession in accessions:
        if not accession or accession in seen_accessions:
            continue
        seen_accessions.add(accession)
        entity_ids = client.search_uniprot(
            accession,
            limit=limit_entities_per_accession,
        )
        for entity in client.fetch_polymer_entities(entity_ids):
            row = row_from_rcsb_pdb_entity(accession, entity)
            if row is None:
                continue
            key = (row.uniprot_accession, row.rcsb_id)
            if key in seen_rows:
                continue
            seen_rows.add(key)
            rows.append(row)
    return sorted(rows, key=lambda row: (row.uniprot_accession, row.pdb_id, row.entity_id))


def row_from_rcsb_pdb_entity(
    accession: str,
    entity: Mapping[str, Any],
) -> RcsbPdbRow | None:
    """Return normalized RCSB PDB entity metadata, or ``None`` if malformed."""

    identifiers = _mapping(entity.get("rcsb_polymer_entity_container_identifiers"))
    rcsb_id = _string(entity.get("rcsb_id"))
    pdb_id = _string(identifiers.get("entry_id"))
    entity_id = _string(identifiers.get("entity_id"))
    if not rcsb_id or not pdb_id or not entity_id:
        return None

    entry = _mapping(entity.get("entry"))
    entry_info = _mapping(entry.get("rcsb_entry_info"))
    entity_poly = _mapping(entity.get("entity_poly"))
    source_organism = _first_mapping(entity.get("rcsb_entity_source_organism"))

    return RcsbPdbRow(
        uniprot_accession=accession,
        pdb_id=pdb_id,
        entity_id=entity_id,
        rcsb_id=rcsb_id,
        experimental_method=_string(entry_info.get("experimental_method")),
        resolution=_first_float(entry_info.get("resolution_combined")),
        polymer_type=_string(entity_poly.get("rcsb_entity_polymer_type")),
        sequence_length=_int(entity_poly.get("rcsb_sample_sequence_length")),
        chain_ids=_strings(identifiers.get("auth_asym_ids")),
        taxon_id=_string(source_organism.get("ncbi_taxonomy_id")),
        organism=_string(source_organism.get("ncbi_scientific_name")),
        entity_names=_entity_names(entity.get("rcsb_polymer_entity_name_com")),
        reference_accessions=_reference_accessions(
            identifiers.get("reference_sequence_identifiers")
        ),
    )


def render_rcsb_pdb_tsv(rows: Iterable[RcsbPdbRow]) -> str:
    """Render RCSB PDB rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=RCSB_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_rcsb_pdb_json(rows: Iterable[RcsbPdbRow]) -> str:
    """Render RCSB PDB rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def _entity_names(value: object) -> tuple[str, ...]:
    names: list[str] = []
    seen: set[str] = set()
    for item in _as_list(value):
        if not isinstance(item, Mapping):
            continue
        name = _string(item.get("name"))
        if name and name not in seen:
            seen.add(name)
            names.append(name)
    return tuple(names)


def _reference_accessions(value: object) -> tuple[str, ...]:
    accessions: list[str] = []
    seen: set[str] = set()
    for item in _as_list(value):
        if not isinstance(item, Mapping):
            continue
        if item.get("database_name") != "UniProt":
            continue
        accession = _string(item.get("database_accession"))
        if accession and accession not in seen:
            seen.add(accession)
            accessions.append(accession)
    return tuple(accessions)


def _as_list(value: object) -> list[Any]:
    return value if isinstance(value, list) else []


def _first_float(value: object) -> float | None:
    for item in _as_list(value):
        if type(item) in (float, int):
            return float(item)
    return None


def _first_mapping(value: object) -> Mapping[str, Any]:
    for item in _as_list(value):
        if isinstance(item, Mapping):
            return item
    return {}


def _int(value: object) -> int | None:
    return value if type(value) is int else None


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _string(value: object) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, int):
        return str(value)
    return ""


def _strings(value: object) -> tuple[str, ...]:
    strings: list[str] = []
    seen: set[str] = set()
    for item in _as_list(value):
        text = _string(item)
        if text and text not in seen:
            seen.add(text)
            strings.append(text)
    return tuple(strings)
