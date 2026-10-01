"""Map UniProtKB accessions to permanent UniParc sequence IDs."""

from __future__ import annotations

import csv
import io
import json
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from typing import Any

UNIPARC_TARGET = "UniParc"

UNIPARC_TSV_FIELDNAMES = [
    "uniprot_accession",
    "uniparc_id",
    "cross_reference_count",
    "sequence_length",
    "molecular_weight",
    "crc64",
    "md5",
    "uniprotkb_accessions",
    "common_taxon_ids",
    "common_taxon_names",
    "common_taxon_top_levels",
    "interpro_ids",
    "pfam_ids",
    "gene3d_ids",
    "sequence_feature_count",
    "source_url",
]


@dataclass(frozen=True)
class UniParcMappingRow:
    """One UniProtKB accession mapped to a UniParc sequence archive row."""

    uniprot_accession: str
    uniparc_id: str
    cross_reference_count: int | None
    sequence_length: int | None
    molecular_weight: int | None
    crc64: str
    md5: str
    uniprotkb_accessions: tuple[str, ...]
    common_taxon_ids: tuple[str, ...]
    common_taxon_names: tuple[str, ...]
    common_taxon_top_levels: tuple[str, ...]
    interpro_ids: tuple[str, ...]
    pfam_ids: tuple[str, ...]
    gene3d_ids: tuple[str, ...]
    sequence_feature_count: int

    @property
    def source_url(self) -> str:
        return f"https://rest.uniprot.org/uniparc/{self.uniparc_id}"

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["uniprotkb_accessions"] = ";".join(self.uniprotkb_accessions)
        row["common_taxon_ids"] = ";".join(self.common_taxon_ids)
        row["common_taxon_names"] = ";".join(self.common_taxon_names)
        row["common_taxon_top_levels"] = ";".join(self.common_taxon_top_levels)
        row["interpro_ids"] = ";".join(self.interpro_ids)
        row["pfam_ids"] = ";".join(self.pfam_ids)
        row["gene3d_ids"] = ";".join(self.gene3d_ids)
        row["source_url"] = self.source_url
        return row


def collect_uniparc_mappings(
    mapping_results: Iterable[Mapping[str, Any]],
) -> list[UniParcMappingRow]:
    """Normalize UniProt ID Mapping results into sorted UniParc rows."""

    rows: list[UniParcMappingRow] = []
    seen: set[tuple[str, str]] = set()
    for result in mapping_results:
        row = row_from_uniparc_mapping(result)
        if row is None:
            continue
        key = (row.uniprot_accession, row.uniparc_id)
        if key in seen:
            continue
        seen.add(key)
        rows.append(row)
    return sorted(rows, key=lambda row: (row.uniparc_id, row.uniprot_accession))


def row_from_uniparc_mapping(result: Mapping[str, Any]) -> UniParcMappingRow | None:
    """Return a normalized UniParc mapping row, or ``None`` if malformed."""

    uniprot_accession = _string(result.get("from"))
    uniparc = _mapping(result.get("to"))
    uniparc_id = _string(uniparc.get("uniParcId"))
    if not uniprot_accession or not uniparc_id:
        return None

    sequence = _mapping(uniparc.get("sequence"))
    features = _mappings(uniparc.get("sequenceFeatures"))

    return UniParcMappingRow(
        uniprot_accession=uniprot_accession,
        uniparc_id=uniparc_id,
        cross_reference_count=_int(uniparc.get("crossReferenceCount")),
        sequence_length=_int(sequence.get("length")),
        molecular_weight=_int(sequence.get("molWeight")),
        crc64=_string(sequence.get("crc64")),
        md5=_string(sequence.get("md5")),
        uniprotkb_accessions=_unique_string_list(uniparc.get("uniProtKBAccessions")),
        common_taxon_ids=_common_taxon_strings(uniparc, "commonTaxonId"),
        common_taxon_names=_common_taxon_strings(uniparc, "commonTaxon"),
        common_taxon_top_levels=_common_taxon_strings(uniparc, "topLevel"),
        interpro_ids=_interpro_ids(features),
        pfam_ids=_database_ids(features, "Pfam"),
        gene3d_ids=_database_ids(features, "Gene3D"),
        sequence_feature_count=len(features),
    )


def render_uniparc_tsv(rows: Iterable[UniParcMappingRow]) -> str:
    """Render UniParc mapping rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=UNIPARC_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_uniparc_json(rows: Iterable[UniParcMappingRow]) -> str:
    """Render UniParc mapping rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def _common_taxon_strings(uniparc: Mapping[str, Any], key: str) -> tuple[str, ...]:
    return _unique_strings(taxon.get(key) for taxon in _mappings(uniparc.get("commonTaxons")))


def _interpro_ids(features: Iterable[Mapping[str, Any]]) -> tuple[str, ...]:
    return _unique_strings(
        _mapping(feature.get("interproGroup")).get("id") for feature in features
    )


def _database_ids(
    features: Iterable[Mapping[str, Any]],
    database: str,
) -> tuple[str, ...]:
    return _unique_strings(
        feature.get("databaseId")
        for feature in features
        if feature.get("database") == database
    )


def _unique_string_list(value: object) -> tuple[str, ...]:
    return _unique_strings(value if isinstance(value, list) else ())


def _unique_strings(values: Iterable[object]) -> tuple[str, ...]:
    unique: list[str] = []
    seen: set[str] = set()
    for value in values:
        text = _string(value)
        if text and text not in seen:
            seen.add(text)
            unique.append(text)
    return tuple(unique)


def _mappings(value: object) -> list[Mapping[str, Any]]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, Mapping)]


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _int(value: object) -> int | None:
    return value if type(value) is int else None


def _string(value: object) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, int):
        return str(value)
    return ""
