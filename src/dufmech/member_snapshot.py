"""Write versioned Pfam member / UniRef snapshots."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Iterable
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.member_uniref import (
    MEMBER_UNIREF_TSV_FIELDNAMES,
    PfamMemberUniRefRow,
    join_members_to_uniref,
    render_member_uniref_json,
    render_member_uniref_tsv,
)
from dufmech.protein_members import (
    INTERPRO_PFAM_PROTEINS_URL,
    InterProPfamProteinClient,
    PfamProteinMemberRow,
    collect_family_members,
)
from dufmech.uniprotkb import (
    UNIPROTKB_SEARCH_URL,
    UniProtKbMetadataClient,
    collect_uniprotkb_metadata,
)
from dufmech.uniref import (
    DEFAULT_UNIREF_TARGET,
    UNIPROT_ID_MAPPING_URL,
    UniProtIdMappingClient,
    collect_uniref_mappings,
)

MEMBER_UNIREF_STEM = "pfam-uniprot"


def collect_member_uniref_rows(
    pfam_ids: Iterable[str],
    *,
    member_client: InterProPfamProteinClient | None = None,
    metadata_client: UniProtKbMetadataClient | None = None,
    uniref_client: UniProtIdMappingClient | None = None,
    page_size: int = 200,
    limit_members_per_family: int | None = None,
    uniref_target: str = DEFAULT_UNIREF_TARGET,
) -> list[PfamMemberUniRefRow]:
    """Collect Pfam members, UniProtKB metadata, and UniRef mappings."""

    member_client = member_client or InterProPfamProteinClient()
    metadata_client = metadata_client or UniProtKbMetadataClient()
    uniref_client = uniref_client or UniProtIdMappingClient()

    members = collect_family_members(
        pfam_ids,
        member_client,
        page_size=page_size,
        limit_members_per_family=limit_members_per_family,
    )
    accessions = _member_accessions(members)
    metadata = collect_uniprotkb_metadata(metadata_client.iter_metadata(accessions))
    mappings = collect_uniref_mappings(
        uniref_client.map_uniref(accessions, target=uniref_target)
    )

    return join_members_to_uniref(members, mappings, metadata)


def write_member_uniref_snapshot(
    rows: Iterable[PfamMemberUniRefRow],
    out_dir: Path,
    *,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    seed_snapshot_id: str = "",
    page_size: int = 200,
    uniref_target: str = DEFAULT_UNIREF_TARGET,
) -> dict[str, Any]:
    """Write date-stamped Pfam member / UniRef JSON, TSV, and manifest files."""

    rows = sorted(rows, key=lambda row: (row.pfam_id, row.uniprot_accession))
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = _snapshot_date_text(snapshot_date)

    out_dir.mkdir(parents=True, exist_ok=True)

    snapshot_id = f"{MEMBER_UNIREF_STEM}-{uniref_target.lower()}-{snapshot_date}"
    json_path = out_dir / f"{snapshot_id}.json"
    tsv_path = out_dir / f"{snapshot_id}.tsv"
    manifest_path = out_dir / f"{snapshot_id}.manifest.json"

    json_text = render_member_uniref_json(rows) + "\n"
    tsv_text = render_member_uniref_tsv(rows) + "\n"

    json_path.write_text(json_text, encoding="utf-8")
    tsv_path.write_text(tsv_text, encoding="utf-8")

    manifest = build_member_uniref_manifest(
        rows,
        snapshot_id=snapshot_id,
        snapshot_date=snapshot_date,
        generated_at=generated_at,
        json_path=json_path,
        json_text=json_text,
        tsv_path=tsv_path,
        tsv_text=tsv_text,
        seed_snapshot_id=seed_snapshot_id,
        page_size=page_size,
        uniref_target=uniref_target,
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def build_member_uniref_manifest(
    rows: Iterable[PfamMemberUniRefRow],
    *,
    snapshot_id: str,
    snapshot_date: str,
    generated_at: datetime,
    json_path: Path,
    json_text: str,
    tsv_path: Path,
    tsv_text: str,
    seed_snapshot_id: str = "",
    page_size: int = 200,
    uniref_target: str = DEFAULT_UNIREF_TARGET,
) -> dict[str, Any]:
    """Build provenance and checksum metadata for a Pfam member snapshot."""

    rows = list(rows)
    uniref_counts = Counter(row.uniref_type or "UNMAPPED" for row in rows)

    return {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
            "seed_snapshot_id": seed_snapshot_id,
        },
        "source": {
            "name": "InterPro Pfam members, UniProtKB and UniRef",
            "url": "https://www.ebi.ac.uk/interpro/api/protein/UniProt/",
            "interpro_pfam_proteins_url": INTERPRO_PFAM_PROTEINS_URL,
            "uniprotkb_search_url": UNIPROTKB_SEARCH_URL,
            "uniprot_id_mapping_url": UNIPROT_ID_MAPPING_URL,
            "uniref_target": uniref_target,
            "page_size": page_size,
        },
        "schema": {
            "tsv_fieldnames": MEMBER_UNIREF_TSV_FIELDNAMES,
        },
        "rows": {
            "total": len(rows),
            "unique_pfam_families": len({row.pfam_id for row in rows}),
            "unique_uniprot_accessions": len(
                {row.uniprot_accession for row in rows}
            ),
            "unique_uniref_clusters": len(
                {row.uniref_id for row in rows if row.uniref_id}
            ),
            "with_uniprot_metadata": sum(1 for row in rows if row.uniprot_id),
            "with_proteome_ids": sum(1 for row in rows if row.proteome_ids),
            "with_uniref": sum(1 for row in rows if row.uniref_id),
            "by_uniref_type": dict(sorted(uniref_counts.items())),
        },
        "files": {
            "json": _file_manifest(json_path, json_text),
            "tsv": _file_manifest(tsv_path, tsv_text),
        },
    }


def _member_accessions(rows: Iterable[PfamProteinMemberRow]) -> list[str]:
    accessions: list[str] = []
    seen: set[str] = set()
    for row in rows:
        if row.uniprot_accession in seen:
            continue
        seen.add(row.uniprot_accession)
        accessions.append(row.uniprot_accession)
    return accessions


def _file_manifest(path: Path, text: str) -> dict[str, Any]:
    data = text.encode("utf-8")
    return {
        "path": path.name,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def _snapshot_date_text(value: str | date) -> str:
    if isinstance(value, date):
        return value.isoformat()
    return date.fromisoformat(value).isoformat()


def _datetime_text(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
