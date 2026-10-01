"""Write versioned 3D-Beacons structural coverage snapshots."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Iterable
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.threedbeacons import (
    THREEDBEACONS_API_URL,
    THREEDBEACONS_TSV_FIELDNAMES,
    ThreeDBeaconsClient,
    ThreeDBeaconsStructureRow,
    collect_threedbeacons_rows,
    render_threedbeacons_json,
    render_threedbeacons_tsv,
)

THREEDBEACONS_STEM = "uniprot-3dbeacons"


def collect_threedbeacons_snapshot_rows(
    accessions: Iterable[str],
    *,
    client: ThreeDBeaconsClient | None = None,
) -> list[ThreeDBeaconsStructureRow]:
    """Collect 3D-Beacons rows with the default live client."""

    return collect_threedbeacons_rows(accessions, client or ThreeDBeaconsClient())


def write_threedbeacons_snapshot(
    rows: Iterable[ThreeDBeaconsStructureRow],
    out_dir: Path,
    *,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    seed_snapshot_id: str = "",
) -> dict[str, Any]:
    """Write date-stamped 3D-Beacons JSON, TSV, and manifest files."""

    rows = sorted(
        rows,
        key=lambda row: (
            row.uniprot_accession,
            row.provider,
            row.model_identifier,
            row.uniprot_start or 0,
            row.uniprot_end or 0,
        ),
    )
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = _snapshot_date_text(snapshot_date)

    out_dir.mkdir(parents=True, exist_ok=True)

    snapshot_id = f"{THREEDBEACONS_STEM}-{snapshot_date}"
    json_path = out_dir / f"{snapshot_id}.json"
    tsv_path = out_dir / f"{snapshot_id}.tsv"
    manifest_path = out_dir / f"{snapshot_id}.manifest.json"

    json_text = render_threedbeacons_json(rows) + "\n"
    tsv_text = render_threedbeacons_tsv(rows) + "\n"

    json_path.write_text(json_text, encoding="utf-8")
    tsv_path.write_text(tsv_text, encoding="utf-8")

    manifest = build_threedbeacons_manifest(
        rows,
        snapshot_id=snapshot_id,
        snapshot_date=snapshot_date,
        generated_at=generated_at,
        json_path=json_path,
        json_text=json_text,
        tsv_path=tsv_path,
        tsv_text=tsv_text,
        seed_snapshot_id=seed_snapshot_id,
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def build_threedbeacons_manifest(
    rows: Iterable[ThreeDBeaconsStructureRow],
    *,
    snapshot_id: str,
    snapshot_date: str,
    generated_at: datetime,
    json_path: Path,
    json_text: str,
    tsv_path: Path,
    tsv_text: str,
    seed_snapshot_id: str = "",
) -> dict[str, Any]:
    """Build provenance and checksum metadata for a 3D-Beacons snapshot."""

    rows = list(rows)
    provider_counts = Counter(row.provider or "UNKNOWN" for row in rows)
    category_counts = Counter(row.model_category or "UNKNOWN" for row in rows)

    return {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
            "seed_snapshot_id": seed_snapshot_id,
        },
        "source": {
            "name": "3D-Beacons Network UniProt summary API",
            "api_url": THREEDBEACONS_API_URL,
        },
        "schema": {
            "tsv_fieldnames": THREEDBEACONS_TSV_FIELDNAMES,
        },
        "rows": {
            "total": len(rows),
            "unique_uniprot_accessions": len(
                {row.uniprot_accession for row in rows}
            ),
            "unique_models": len(
                {(row.provider, row.model_identifier) for row in rows}
            ),
            "by_provider": dict(sorted(provider_counts.items())),
            "by_model_category": dict(sorted(category_counts.items())),
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
