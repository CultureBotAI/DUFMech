"""Write versioned UniParc sequence archive snapshots."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Iterable
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.uniparc import (
    UNIPARC_TARGET,
    UNIPARC_TSV_FIELDNAMES,
    UniParcMappingRow,
    collect_uniparc_mappings,
    render_uniparc_json,
    render_uniparc_tsv,
)
from dufmech.uniref import UNIPROT_ID_MAPPING_URL, UniProtIdMappingClient

UNIPARC_STEM = "uniprot-uniparc"


def collect_uniparc_snapshot_rows(
    accessions: Iterable[str],
    *,
    client: UniProtIdMappingClient | None = None,
    batch_size: int = 100_000,
) -> list[UniParcMappingRow]:
    """Collect UniParc rows with the default live UniProt ID Mapping client."""

    client = client or UniProtIdMappingClient()
    return collect_uniparc_mappings(
        client.map_accessions(
            accessions,
            batch_size=batch_size,
            target=UNIPARC_TARGET,
        )
    )


def write_uniparc_snapshot(
    rows: Iterable[UniParcMappingRow],
    out_dir: Path,
    *,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    seed_snapshot_id: str = "",
    batch_size: int = 100_000,
) -> dict[str, Any]:
    """Write date-stamped UniParc JSON, TSV, and manifest files."""

    rows = sorted(rows, key=lambda row: (row.uniparc_id, row.uniprot_accession))
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = _snapshot_date_text(snapshot_date)

    out_dir.mkdir(parents=True, exist_ok=True)

    snapshot_id = f"{UNIPARC_STEM}-{snapshot_date}"
    json_path = out_dir / f"{snapshot_id}.json"
    tsv_path = out_dir / f"{snapshot_id}.tsv"
    manifest_path = out_dir / f"{snapshot_id}.manifest.json"

    json_text = render_uniparc_json(rows) + "\n"
    tsv_text = render_uniparc_tsv(rows) + "\n"

    json_path.write_text(json_text, encoding="utf-8")
    tsv_path.write_text(tsv_text, encoding="utf-8")

    manifest = build_uniparc_manifest(
        rows,
        snapshot_id=snapshot_id,
        snapshot_date=snapshot_date,
        generated_at=generated_at,
        json_path=json_path,
        json_text=json_text,
        tsv_path=tsv_path,
        tsv_text=tsv_text,
        seed_snapshot_id=seed_snapshot_id,
        batch_size=batch_size,
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def build_uniparc_manifest(
    rows: Iterable[UniParcMappingRow],
    *,
    snapshot_id: str,
    snapshot_date: str,
    generated_at: datetime,
    json_path: Path,
    json_text: str,
    tsv_path: Path,
    tsv_text: str,
    seed_snapshot_id: str = "",
    batch_size: int = 100_000,
) -> dict[str, Any]:
    """Build provenance and checksum metadata for a UniParc snapshot."""

    rows = list(rows)
    top_level_counts = Counter(
        top_level for row in rows for top_level in row.common_taxon_top_levels
    )

    return {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
            "seed_snapshot_id": seed_snapshot_id,
        },
        "source": {
            "name": "UniProt ID Mapping UniParc target",
            "uniprot_id_mapping_url": UNIPROT_ID_MAPPING_URL,
            "target": UNIPARC_TARGET,
            "batch_size": batch_size,
        },
        "schema": {
            "tsv_fieldnames": UNIPARC_TSV_FIELDNAMES,
        },
        "rows": {
            "total": len(rows),
            "unique_uniprot_accessions": len(
                {row.uniprot_accession for row in rows}
            ),
            "unique_uniparc_ids": len({row.uniparc_id for row in rows}),
            "with_sequence_checksum": sum(1 for row in rows if row.crc64 or row.md5),
            "with_common_taxon": sum(1 for row in rows if row.common_taxon_ids),
            "with_pfam_features": sum(1 for row in rows if row.pfam_ids),
            "with_gene3d_features": sum(1 for row in rows if row.gene3d_ids),
            "by_common_taxon_top_level": dict(sorted(top_level_counts.items())),
        },
        "files": {
            "json": _file_manifest(json_path, json_text),
            "tsv": _file_manifest(tsv_path, tsv_text),
        },
    }


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
