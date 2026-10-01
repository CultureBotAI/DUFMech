"""Write versioned PDBe-KB annotation snapshots."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Iterable, Sequence
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.pdbe_kb import (
    PDBE_KB_BASE_URL,
    PDBE_KB_ENDPOINTS,
    PDBE_KB_TSV_FIELDNAMES,
    PdbeKbAnnotationRow,
    PdbeKbClient,
    PdbeKbSeed,
    collect_pdbe_kb_rows,
    render_pdbe_kb_json,
    render_pdbe_kb_tsv,
)

PDBE_KB_STEM = "uniprot-pdbe-kb"


def collect_pdbe_kb_snapshot_rows(
    seeds: Iterable[PdbeKbSeed],
    *,
    client: PdbeKbClient | None = None,
    endpoints: Sequence[str] = PDBE_KB_ENDPOINTS,
) -> list[PdbeKbAnnotationRow]:
    """Collect PDBe-KB rows with the default live client."""

    return collect_pdbe_kb_rows(
        seeds,
        client or PdbeKbClient(),
        endpoints=endpoints,
    )


def write_pdbe_kb_snapshot(
    rows: Iterable[PdbeKbAnnotationRow],
    out_dir: Path,
    *,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    seed_snapshot_id: str = "",
    endpoints: Sequence[str] = PDBE_KB_ENDPOINTS,
) -> dict[str, Any]:
    """Write date-stamped PDBe-KB JSON, TSV, and manifest files."""

    rows = sorted(
        rows,
        key=lambda row: (
            row.seed_uniprot_accession,
            row.pdb_id,
            row.entity_id,
            row.endpoint,
            row.annotation_data_type,
            row.annotation_accession,
            row.start_index or 0,
        ),
    )
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = _snapshot_date_text(snapshot_date)

    out_dir.mkdir(parents=True, exist_ok=True)

    snapshot_id = f"{PDBE_KB_STEM}-{snapshot_date}"
    json_path = out_dir / f"{snapshot_id}.json"
    tsv_path = out_dir / f"{snapshot_id}.tsv"
    manifest_path = out_dir / f"{snapshot_id}.manifest.json"

    json_text = render_pdbe_kb_json(rows) + "\n"
    tsv_text = render_pdbe_kb_tsv(rows) + "\n"

    json_path.write_text(json_text, encoding="utf-8")
    tsv_path.write_text(tsv_text, encoding="utf-8")

    manifest = build_pdbe_kb_manifest(
        rows,
        snapshot_id=snapshot_id,
        snapshot_date=snapshot_date,
        generated_at=generated_at,
        json_path=json_path,
        json_text=json_text,
        tsv_path=tsv_path,
        tsv_text=tsv_text,
        seed_snapshot_id=seed_snapshot_id,
        endpoints=endpoints,
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def build_pdbe_kb_manifest(
    rows: Iterable[PdbeKbAnnotationRow],
    *,
    snapshot_id: str,
    snapshot_date: str,
    generated_at: datetime,
    json_path: Path,
    json_text: str,
    tsv_path: Path,
    tsv_text: str,
    seed_snapshot_id: str = "",
    endpoints: Sequence[str] = PDBE_KB_ENDPOINTS,
) -> dict[str, Any]:
    """Build provenance and checksum metadata for a PDBe-KB snapshot."""

    rows = list(rows)
    endpoint_counts = Counter(row.endpoint for row in rows)
    annotation_counts = Counter(row.annotation_data_type or "UNKNOWN" for row in rows)

    return {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
            "seed_snapshot_id": seed_snapshot_id,
        },
        "source": {
            "name": "PDBe API entity annotation endpoints",
            "base_url": PDBE_KB_BASE_URL,
            "endpoints": list(endpoints),
        },
        "schema": {
            "tsv_fieldnames": PDBE_KB_TSV_FIELDNAMES,
        },
        "rows": {
            "total": len(rows),
            "unique_seed_uniprot_accessions": len(
                {row.seed_uniprot_accession for row in rows}
            ),
            "unique_pdb_entries": len({row.pdb_id for row in rows}),
            "unique_pdb_entities": len({(row.pdb_id, row.entity_id) for row in rows}),
            "by_endpoint": dict(sorted(endpoint_counts.items())),
            "by_annotation_data_type": dict(sorted(annotation_counts.items())),
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
