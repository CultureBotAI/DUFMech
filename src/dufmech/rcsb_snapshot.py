"""Write versioned RCSB PDB evidence snapshots."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Iterable
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.rcsb import (
    RCSB_GRAPHQL_URL,
    RCSB_SEARCH_URL,
    RCSB_TSV_FIELDNAMES,
    RcsbPdbClient,
    RcsbPdbRow,
    collect_rcsb_pdb_rows,
    render_rcsb_pdb_json,
    render_rcsb_pdb_tsv,
)

RCSB_STEM = "uniprot-rcsb-pdb"


def collect_rcsb_snapshot_rows(
    accessions: Iterable[str],
    *,
    client: RcsbPdbClient | None = None,
    limit_entities_per_accession: int = 50,
) -> list[RcsbPdbRow]:
    """Collect RCSB PDB rows with the default live client."""

    return collect_rcsb_pdb_rows(
        accessions,
        client or RcsbPdbClient(),
        limit_entities_per_accession=limit_entities_per_accession,
    )


def write_rcsb_snapshot(
    rows: Iterable[RcsbPdbRow],
    out_dir: Path,
    *,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    seed_snapshot_id: str = "",
    limit_entities_per_accession: int = 50,
) -> dict[str, Any]:
    """Write date-stamped RCSB PDB JSON, TSV, and manifest files."""

    rows = sorted(rows, key=lambda row: (row.uniprot_accession, row.pdb_id, row.entity_id))
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = _snapshot_date_text(snapshot_date)

    out_dir.mkdir(parents=True, exist_ok=True)

    snapshot_id = f"{RCSB_STEM}-{snapshot_date}"
    json_path = out_dir / f"{snapshot_id}.json"
    tsv_path = out_dir / f"{snapshot_id}.tsv"
    manifest_path = out_dir / f"{snapshot_id}.manifest.json"

    json_text = render_rcsb_pdb_json(rows) + "\n"
    tsv_text = render_rcsb_pdb_tsv(rows) + "\n"

    json_path.write_text(json_text, encoding="utf-8")
    tsv_path.write_text(tsv_text, encoding="utf-8")

    manifest = build_rcsb_manifest(
        rows,
        snapshot_id=snapshot_id,
        snapshot_date=snapshot_date,
        generated_at=generated_at,
        json_path=json_path,
        json_text=json_text,
        tsv_path=tsv_path,
        tsv_text=tsv_text,
        seed_snapshot_id=seed_snapshot_id,
        limit_entities_per_accession=limit_entities_per_accession,
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def build_rcsb_manifest(
    rows: Iterable[RcsbPdbRow],
    *,
    snapshot_id: str,
    snapshot_date: str,
    generated_at: datetime,
    json_path: Path,
    json_text: str,
    tsv_path: Path,
    tsv_text: str,
    seed_snapshot_id: str = "",
    limit_entities_per_accession: int = 50,
) -> dict[str, Any]:
    """Build provenance and checksum metadata for an RCSB PDB snapshot."""

    rows = list(rows)
    method_counts = Counter(row.experimental_method or "UNKNOWN" for row in rows)

    return {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
            "seed_snapshot_id": seed_snapshot_id,
        },
        "source": {
            "name": "RCSB PDB Search and Data APIs",
            "search_url": RCSB_SEARCH_URL,
            "graphql_url": RCSB_GRAPHQL_URL,
            "limit_entities_per_accession": limit_entities_per_accession,
        },
        "schema": {
            "tsv_fieldnames": RCSB_TSV_FIELDNAMES,
        },
        "rows": {
            "total": len(rows),
            "unique_uniprot_accessions": len(
                {row.uniprot_accession for row in rows}
            ),
            "unique_pdb_entries": len({row.pdb_id for row in rows}),
            "unique_rcsb_entities": len({row.rcsb_id for row in rows}),
            "by_experimental_method": dict(sorted(method_counts.items())),
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
