"""Write versioned MGnify Proteins snapshots."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Iterable
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.mgnify import (
    MGNIFY_PROTEIN_SEARCH_URL,
    MGNIFY_TSV_FIELDNAMES,
    MGnifyProteinClient,
    MgnifyProteinRow,
    collect_pfam_mgnify_rows,
    render_mgnify_json,
    render_mgnify_tsv,
)

MGNIFY_STEM = "pfam-mgnify-proteins"


def collect_mgnify_snapshot_rows(
    pfam_ids: Iterable[str],
    *,
    client: MGnifyProteinClient | None = None,
    limit_proteins_per_family: int = 50,
) -> list[MgnifyProteinRow]:
    """Collect MGnify representatives with the default live client."""

    return collect_pfam_mgnify_rows(
        pfam_ids,
        client or MGnifyProteinClient(),
        limit_proteins_per_family=limit_proteins_per_family,
    )


def write_mgnify_snapshot(
    rows: Iterable[MgnifyProteinRow],
    out_dir: Path,
    *,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    seed_snapshot_id: str = "",
    limit_proteins_per_family: int = 50,
) -> dict[str, Any]:
    """Write date-stamped MGnify JSON, TSV, and manifest files."""

    rows = sorted(rows, key=lambda row: (row.pfam_id, row.mgyp))
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = _snapshot_date_text(snapshot_date)

    out_dir.mkdir(parents=True, exist_ok=True)

    snapshot_id = f"{MGNIFY_STEM}-{snapshot_date}"
    json_path = out_dir / f"{snapshot_id}.json"
    tsv_path = out_dir / f"{snapshot_id}.tsv"
    manifest_path = out_dir / f"{snapshot_id}.manifest.json"

    json_text = render_mgnify_json(rows) + "\n"
    tsv_text = render_mgnify_tsv(rows) + "\n"

    json_path.write_text(json_text, encoding="utf-8")
    tsv_path.write_text(tsv_text, encoding="utf-8")

    manifest = build_mgnify_manifest(
        rows,
        snapshot_id=snapshot_id,
        snapshot_date=snapshot_date,
        generated_at=generated_at,
        json_path=json_path,
        json_text=json_text,
        tsv_path=tsv_path,
        tsv_text=tsv_text,
        seed_snapshot_id=seed_snapshot_id,
        limit_proteins_per_family=limit_proteins_per_family,
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def build_mgnify_manifest(
    rows: Iterable[MgnifyProteinRow],
    *,
    snapshot_id: str,
    snapshot_date: str,
    generated_at: datetime,
    json_path: Path,
    json_text: str,
    tsv_path: Path,
    tsv_text: str,
    seed_snapshot_id: str = "",
    limit_proteins_per_family: int = 50,
) -> dict[str, Any]:
    """Build provenance and checksum metadata for a MGnify snapshot."""

    rows = list(rows)
    length_counts = Counter(_length_status(row) for row in rows)

    return {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
            "seed_snapshot_id": seed_snapshot_id,
        },
        "source": {
            "name": "MGnify Proteins API",
            "search_url": MGNIFY_PROTEIN_SEARCH_URL,
            "limit_proteins_per_family": limit_proteins_per_family,
        },
        "schema": {
            "tsv_fieldnames": MGNIFY_TSV_FIELDNAMES,
        },
        "rows": {
            "total": len(rows),
            "unique_pfam_families": len({row.pfam_id for row in rows}),
            "unique_mgyp_accessions": len({row.mgyp for row in rows}),
            "by_length_status": dict(sorted(length_counts.items())),
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


def _length_status(row: MgnifyProteinRow) -> str:
    if row.full_length is True:
        return "full_length"
    if row.full_length is False:
        return "fragment"
    return "unknown"


def _snapshot_date_text(value: str | date) -> str:
    if isinstance(value, date):
        return value.isoformat()
    return date.fromisoformat(value).isoformat()


def _datetime_text(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
