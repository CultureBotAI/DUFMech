"""Write versioned QuickGO molecular-function snapshots."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Iterable
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.quickgo import (
    QUICKGO_ANNOTATION_URL,
    QUICKGO_ASPECT,
    QUICKGO_TSV_FIELDNAMES,
    QuickGoAnnotationRow,
    QuickGoClient,
    collect_quickgo_rows,
    render_quickgo_json,
    render_quickgo_tsv,
)

QUICKGO_STEM = "uniprot-quickgo-mf"


def collect_quickgo_snapshot_rows(
    accessions: Iterable[str],
    *,
    client: QuickGoClient | None = None,
    limit_annotations_per_accession: int = 50,
    aspect: str = QUICKGO_ASPECT,
) -> list[QuickGoAnnotationRow]:
    """Collect QuickGO rows with the default live client."""

    return collect_quickgo_rows(
        accessions,
        client or QuickGoClient(),
        limit_annotations_per_accession=limit_annotations_per_accession,
        aspect=aspect,
    )


def write_quickgo_snapshot(
    rows: Iterable[QuickGoAnnotationRow],
    out_dir: Path,
    *,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    seed_snapshot_id: str = "",
    limit_annotations_per_accession: int = 50,
    aspect: str = QUICKGO_ASPECT,
) -> dict[str, Any]:
    """Write date-stamped QuickGO JSON, TSV, and manifest files."""

    rows = sorted(rows, key=lambda row: (row.uniprot_accession, row.annotation_id))
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = _snapshot_date_text(snapshot_date)

    out_dir.mkdir(parents=True, exist_ok=True)

    snapshot_id = f"{QUICKGO_STEM}-{snapshot_date}"
    json_path = out_dir / f"{snapshot_id}.json"
    tsv_path = out_dir / f"{snapshot_id}.tsv"
    manifest_path = out_dir / f"{snapshot_id}.manifest.json"

    json_text = render_quickgo_json(rows) + "\n"
    tsv_text = render_quickgo_tsv(rows) + "\n"

    json_path.write_text(json_text, encoding="utf-8")
    tsv_path.write_text(tsv_text, encoding="utf-8")

    manifest = build_quickgo_manifest(
        rows,
        snapshot_id=snapshot_id,
        snapshot_date=snapshot_date,
        generated_at=generated_at,
        json_path=json_path,
        json_text=json_text,
        tsv_path=tsv_path,
        tsv_text=tsv_text,
        seed_snapshot_id=seed_snapshot_id,
        limit_annotations_per_accession=limit_annotations_per_accession,
        aspect=aspect,
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def build_quickgo_manifest(
    rows: Iterable[QuickGoAnnotationRow],
    *,
    snapshot_id: str,
    snapshot_date: str,
    generated_at: datetime,
    json_path: Path,
    json_text: str,
    tsv_path: Path,
    tsv_text: str,
    seed_snapshot_id: str = "",
    limit_annotations_per_accession: int = 50,
    aspect: str = QUICKGO_ASPECT,
) -> dict[str, Any]:
    """Build provenance and checksum metadata for a QuickGO snapshot."""

    rows = list(rows)
    evidence_counts = Counter(row.evidence_code or "UNKNOWN" for row in rows)
    assigned_by_counts = Counter(row.assigned_by or "UNKNOWN" for row in rows)

    return {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
            "seed_snapshot_id": seed_snapshot_id,
        },
        "source": {
            "name": "QuickGO annotation search API",
            "url": QUICKGO_ANNOTATION_URL,
            "aspect": aspect,
            "limit_annotations_per_accession": limit_annotations_per_accession,
        },
        "schema": {
            "tsv_fieldnames": QUICKGO_TSV_FIELDNAMES,
        },
        "rows": {
            "total": len(rows),
            "unique_uniprot_accessions": len(
                {row.uniprot_accession for row in rows}
            ),
            "unique_go_terms": len({row.go_id for row in rows}),
            "by_evidence_code": dict(sorted(evidence_counts.items())),
            "by_assigned_by": dict(sorted(assigned_by_counts.items())),
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
