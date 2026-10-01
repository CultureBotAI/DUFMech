"""Write versioned NCBI Batch CD-Search snapshots."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Iterable
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.cdsearch import (
    CDSEARCH_TSV_FIELDNAMES,
    CDSEARCH_URL,
    DEFAULT_CDSEARCH_BATCH_SIZE,
    DEFAULT_CDSEARCH_DB,
    DEFAULT_CDSEARCH_MODE,
    CdSearchClient,
    CdSearchDomainRow,
    collect_cdsearch_rows,
    render_cdsearch_json,
    render_cdsearch_tsv,
)

CDSEARCH_STEM = "uniprot-cdsearch"


def collect_cdsearch_snapshot_rows(
    accessions: Iterable[str],
    *,
    client: CdSearchClient | None = None,
    db: str = DEFAULT_CDSEARCH_DB,
    mode: str = DEFAULT_CDSEARCH_MODE,
    batch_size: int = DEFAULT_CDSEARCH_BATCH_SIZE,
) -> list[CdSearchDomainRow]:
    """Collect NCBI Batch CD-Search rows with the default live client."""

    return collect_cdsearch_rows(
        accessions,
        client or CdSearchClient(),
        db=db,
        mode=mode,
        batch_size=batch_size,
    )


def write_cdsearch_snapshot(
    rows: Iterable[CdSearchDomainRow],
    out_dir: Path,
    *,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    seed_snapshot_id: str = "",
    db: str = DEFAULT_CDSEARCH_DB,
    mode: str = DEFAULT_CDSEARCH_MODE,
    batch_size: int = DEFAULT_CDSEARCH_BATCH_SIZE,
) -> dict[str, Any]:
    """Write date-stamped NCBI Batch CD-Search JSON, TSV, and manifest files."""

    rows = sorted(
        rows,
        key=lambda row: (
            row.uniprot_accession,
            row.start or 0,
            row.end or 0,
            row.cdd_accession,
            row.hit_type,
        ),
    )
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = _snapshot_date_text(snapshot_date)

    out_dir.mkdir(parents=True, exist_ok=True)

    snapshot_id = f"{CDSEARCH_STEM}-{snapshot_date}"
    json_path = out_dir / f"{snapshot_id}.json"
    tsv_path = out_dir / f"{snapshot_id}.tsv"
    manifest_path = out_dir / f"{snapshot_id}.manifest.json"

    json_text = render_cdsearch_json(rows) + "\n"
    tsv_text = render_cdsearch_tsv(rows) + "\n"

    json_path.write_text(json_text, encoding="utf-8")
    tsv_path.write_text(tsv_text, encoding="utf-8")

    manifest = build_cdsearch_manifest(
        rows,
        snapshot_id=snapshot_id,
        snapshot_date=snapshot_date,
        generated_at=generated_at,
        json_path=json_path,
        json_text=json_text,
        tsv_path=tsv_path,
        tsv_text=tsv_text,
        seed_snapshot_id=seed_snapshot_id,
        db=db,
        mode=mode,
        batch_size=batch_size,
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def build_cdsearch_manifest(
    rows: Iterable[CdSearchDomainRow],
    *,
    snapshot_id: str,
    snapshot_date: str,
    generated_at: datetime,
    json_path: Path,
    json_text: str,
    tsv_path: Path,
    tsv_text: str,
    seed_snapshot_id: str = "",
    db: str = DEFAULT_CDSEARCH_DB,
    mode: str = DEFAULT_CDSEARCH_MODE,
    batch_size: int = DEFAULT_CDSEARCH_BATCH_SIZE,
) -> dict[str, Any]:
    """Build provenance and checksum metadata for a Batch CD-Search snapshot."""

    rows = list(rows)
    hit_type_counts = Counter(row.hit_type or "UNKNOWN" for row in rows)

    return {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
            "seed_snapshot_id": seed_snapshot_id,
        },
        "source": {
            "name": "NCBI Batch CD-Search",
            "url": CDSEARCH_URL,
            "db": db,
            "mode": mode,
            "batch_size": batch_size,
            "tdata": "hits",
            "useid1": True,
        },
        "schema": {
            "tsv_fieldnames": CDSEARCH_TSV_FIELDNAMES,
        },
        "rows": {
            "total": len(rows),
            "unique_uniprot_accessions": len(
                {row.uniprot_accession for row in rows}
            ),
            "unique_cdd_accessions": len({row.cdd_accession for row in rows}),
            "unique_superfamilies": len(
                {row.superfamily_accession for row in rows if row.superfamily_accession}
            ),
            "by_hit_type": dict(sorted(hit_type_counts.items())),
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
