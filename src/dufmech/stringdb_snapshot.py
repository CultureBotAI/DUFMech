"""Write versioned STRING interaction snapshots."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Iterable
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.stringdb import (
    STRING_API_URL,
    STRING_CALLER_IDENTITY,
    STRING_TSV_FIELDNAMES,
    StringDbClient,
    StringDbInteractionRow,
    StringDbSeed,
    collect_stringdb_rows,
    render_stringdb_json,
    render_stringdb_tsv,
)

STRINGDB_STEM = "uniprot-string"


def collect_stringdb_snapshot_rows(
    seeds: Iterable[StringDbSeed],
    *,
    client: StringDbClient | None = None,
    limit_partners_per_protein: int = 10,
    required_score: int = 400,
) -> list[StringDbInteractionRow]:
    """Collect STRING rows with the default live client."""

    return collect_stringdb_rows(
        seeds,
        client or StringDbClient(),
        limit_partners_per_protein=limit_partners_per_protein,
        required_score=required_score,
    )


def write_stringdb_snapshot(
    rows: Iterable[StringDbInteractionRow],
    out_dir: Path,
    *,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    seed_snapshot_id: str = "",
    limit_partners_per_protein: int = 10,
    required_score: int = 400,
) -> dict[str, Any]:
    """Write date-stamped STRING JSON, TSV, and manifest files."""

    rows = sorted(
        rows,
        key=lambda row: (row.uniprot_accession, row.string_id, row.partner_string_id),
    )
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = _snapshot_date_text(snapshot_date)

    out_dir.mkdir(parents=True, exist_ok=True)

    snapshot_id = f"{STRINGDB_STEM}-{snapshot_date}"
    json_path = out_dir / f"{snapshot_id}.json"
    tsv_path = out_dir / f"{snapshot_id}.tsv"
    manifest_path = out_dir / f"{snapshot_id}.manifest.json"

    json_text = render_stringdb_json(rows) + "\n"
    tsv_text = render_stringdb_tsv(rows) + "\n"

    json_path.write_text(json_text, encoding="utf-8")
    tsv_path.write_text(tsv_text, encoding="utf-8")

    manifest = build_stringdb_manifest(
        rows,
        snapshot_id=snapshot_id,
        snapshot_date=snapshot_date,
        generated_at=generated_at,
        json_path=json_path,
        json_text=json_text,
        tsv_path=tsv_path,
        tsv_text=tsv_text,
        seed_snapshot_id=seed_snapshot_id,
        limit_partners_per_protein=limit_partners_per_protein,
        required_score=required_score,
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def build_stringdb_manifest(
    rows: Iterable[StringDbInteractionRow],
    *,
    snapshot_id: str,
    snapshot_date: str,
    generated_at: datetime,
    json_path: Path,
    json_text: str,
    tsv_path: Path,
    tsv_text: str,
    seed_snapshot_id: str = "",
    limit_partners_per_protein: int = 10,
    required_score: int = 400,
) -> dict[str, Any]:
    """Build provenance and checksum metadata for a STRING snapshot."""

    rows = list(rows)
    taxon_counts = Counter(row.string_taxon_id or "UNKNOWN" for row in rows)

    return {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
            "seed_snapshot_id": seed_snapshot_id,
        },
        "source": {
            "name": "STRING v12.0 API",
            "api_url": STRING_API_URL,
            "caller_identity": STRING_CALLER_IDENTITY,
            "limit_partners_per_protein": limit_partners_per_protein,
            "required_score": required_score,
        },
        "schema": {
            "tsv_fieldnames": STRING_TSV_FIELDNAMES,
        },
        "rows": {
            "total": len(rows),
            "unique_uniprot_accessions": len(
                {row.uniprot_accession for row in rows}
            ),
            "unique_query_string_ids": len({row.string_id for row in rows}),
            "unique_partner_string_ids": len(
                {row.partner_string_id for row in rows}
            ),
            "by_taxon": dict(sorted(taxon_counts.items())),
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
