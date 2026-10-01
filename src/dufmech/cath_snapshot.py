"""Write versioned CATH-Gene3D FunFam snapshots."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Iterable
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.cath import (
    CATH_TSV_FIELDNAMES,
    CATH_UNIPROT_TO_FUNFAM_URL,
    CATH_VERSION,
    CathClient,
    CathFunFamRow,
    collect_cath_rows,
    render_cath_json,
    render_cath_tsv,
)

CATH_STEM = "uniprot-cath-funfam"


def collect_cath_snapshot_rows(
    accessions: Iterable[str],
    *,
    client: CathClient | None = None,
) -> list[CathFunFamRow]:
    """Collect CATH rows with the default live client."""

    return collect_cath_rows(accessions, client or CathClient())


def write_cath_snapshot(
    rows: Iterable[CathFunFamRow],
    out_dir: Path,
    *,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    seed_snapshot_id: str = "",
    cath_version: str = CATH_VERSION,
) -> dict[str, Any]:
    """Write date-stamped CATH FunFam JSON, TSV, and manifest files."""

    rows = sorted(
        rows,
        key=lambda row: (
            row.uniprot_accession,
            row.superfamily_id,
            int(row.funfam_number) if row.funfam_number.isdigit() else 0,
            row.member_id,
        ),
    )
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = _snapshot_date_text(snapshot_date)

    out_dir.mkdir(parents=True, exist_ok=True)

    snapshot_id = f"{CATH_STEM}-{cath_version}-{snapshot_date}"
    json_path = out_dir / f"{snapshot_id}.json"
    tsv_path = out_dir / f"{snapshot_id}.tsv"
    manifest_path = out_dir / f"{snapshot_id}.manifest.json"

    json_text = render_cath_json(rows) + "\n"
    tsv_text = render_cath_tsv(rows) + "\n"

    json_path.write_text(json_text, encoding="utf-8")
    tsv_path.write_text(tsv_text, encoding="utf-8")

    manifest = build_cath_manifest(
        rows,
        snapshot_id=snapshot_id,
        snapshot_date=snapshot_date,
        generated_at=generated_at,
        json_path=json_path,
        json_text=json_text,
        tsv_path=tsv_path,
        tsv_text=tsv_text,
        seed_snapshot_id=seed_snapshot_id,
        cath_version=cath_version,
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def build_cath_manifest(
    rows: Iterable[CathFunFamRow],
    *,
    snapshot_id: str,
    snapshot_date: str,
    generated_at: datetime,
    json_path: Path,
    json_text: str,
    tsv_path: Path,
    tsv_text: str,
    seed_snapshot_id: str = "",
    cath_version: str = CATH_VERSION,
) -> dict[str, Any]:
    """Build provenance and checksum metadata for a CATH FunFam snapshot."""

    rows = list(rows)
    superfamily_counts = Counter(row.superfamily_id for row in rows)

    return {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
            "seed_snapshot_id": seed_snapshot_id,
        },
        "source": {
            "name": "CATH-Gene3D UniProt to FunFam API",
            "api_url": CATH_UNIPROT_TO_FUNFAM_URL,
            "cath_version": cath_version,
        },
        "schema": {
            "tsv_fieldnames": CATH_TSV_FIELDNAMES,
        },
        "rows": {
            "total": len(rows),
            "unique_uniprot_accessions": len(
                {row.uniprot_accession for row in rows}
            ),
            "unique_superfamilies": len({row.superfamily_id for row in rows}),
            "unique_funfams": len(
                {(row.superfamily_id, row.funfam_number) for row in rows}
            ),
            "by_superfamily": dict(sorted(superfamily_counts.items())),
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
