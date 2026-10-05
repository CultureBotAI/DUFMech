"""Write versioned snapshots of DUF/PUF examples found in sibling Mechs."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.cross_mech import (
    CROSS_MECH_TSV_FIELDNAMES,
    GITHUB_ORG_URL,
    UNIPROTKB_SEARCH_URL,
    ScanResult,
    render_cross_mech_json,
    render_cross_mech_tsv,
)

CROSS_MECH_STEM = "cross-mech-duf-examples"
CROSS_MECH_DIR = Path("data/cross_mech")


def write_cross_mech_snapshot(
    result: ScanResult,
    out_dir: Path,
    *,
    worklist_snapshot_id: str,
    source_ref: str,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
) -> dict[str, Any]:
    """Write date-stamped cross-Mech JSON, TSV, and manifest files."""

    rows = sorted(result.rows, key=lambda row: row.sort_key())
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = (
        snapshot_date.isoformat()
        if isinstance(snapshot_date, date)
        else date.fromisoformat(snapshot_date).isoformat()
    )
    snapshot_id = f"{CROSS_MECH_STEM}-{snapshot_date}"
    out_dir.mkdir(parents=True, exist_ok=True)
    json_text = render_cross_mech_json(rows) + "\n"
    tsv_text = render_cross_mech_tsv(rows) + "\n"
    (out_dir / f"{snapshot_id}.json").write_text(json_text, encoding="utf-8")
    (out_dir / f"{snapshot_id}.tsv").write_text(tsv_text, encoding="utf-8")

    proteins = {row.uniprot_accession for row in rows if row.uniprot_accession}
    manifest = {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
            "input_snapshot_ids": {"worklist": worklist_snapshot_id},
            "source_ref": source_ref,
        },
        "source": {
            "name": "Curated YAML records in sibling CultureBotAI Mech repositories",
            "url": GITHUB_ORG_URL,
            "mechs": result.mechs,
            "uniprotkb_url": UNIPROTKB_SEARCH_URL,
            "uniprotkb_accessions_requested": result.uniprot_requested,
            "uniprotkb_accessions_resolved": result.uniprot_resolved,
        },
        "schema": {"tsv_fieldnames": CROSS_MECH_TSV_FIELDNAMES},
        "rows": {
            "total": len(rows),
            "unique_pfam_ids": len({row.pfam_id for row in rows if row.pfam_id}),
            "unlisted_short_names": len({row.short_name for row in rows if not row.pfam_id}),
            "unique_uniprot_accessions": len(proteins),
            "by_source_mech": _counts(row.source_mech for row in rows),
            "by_source_section": _counts(row.source_section for row in rows),
            "by_unknown_status": _counts(row.unknown_status for row in rows),
            "pfam_ids_by_source_mech": {
                mech: len({row.pfam_id for row in rows if row.source_mech == mech and row.pfam_id})
                for mech in sorted({row.source_mech for row in rows})
            },
        },
        "files": {
            "json": _file_manifest(f"{snapshot_id}.json", json_text),
            "tsv": _file_manifest(f"{snapshot_id}.tsv", tsv_text),
        },
    }
    (out_dir / f"{snapshot_id}.manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return manifest


def _counts(values: Any) -> dict[str, int]:
    return dict(sorted(Counter(values).items()))


def _file_manifest(name: str, text: str) -> dict[str, Any]:
    data = text.encode("utf-8")
    return {"path": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def _datetime_text(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
