"""Write versioned snapshots of DUF/PUF examples found in sibling Mechs."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Mapping, Sequence
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
from dufmech.report import ReportError, load_json_rows, verified_manifest

CROSS_MECH_STEM = "cross-mech-duf-examples"
CROSS_MECH_DIR = Path("data/cross_mech")


def load_cross_mech_snapshot(
    path: Path,
    *,
    worklist_rows: Sequence[Mapping[str, Any]],
    worklist_snapshot_id: str,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Verify cross-Mech evidence against the selected worklist for every consumer."""

    manifest = verified_manifest(path)
    worklist_input = manifest["snapshot"].get("input_snapshot_ids", {}).get("worklist")
    if worklist_input != worklist_snapshot_id:
        raise ReportError(
            f"{path.name} was built against {worklist_input}, "
            f"not {worklist_snapshot_id}; regenerate the cross-Mech snapshot"
        )
    rows = [dict(row) for row in load_json_rows(path)]
    families = {row["pfam_id"]: row for row in worklist_rows}
    extra = {row["pfam_id"] for row in rows if row["pfam_id"]} - families.keys()
    if extra:
        raise ReportError(f"cross-Mech families absent from worklist: {', '.join(sorted(extra))}")
    for row in rows:
        if row["pfam_id"] and any(
            row[key] != families[row["pfam_id"]][key] for key in ("short_name", "unknown_status")
        ):
            raise ReportError(
                f"{path.name}: {row['pfam_id']} metadata differs from {worklist_snapshot_id}; "
                "regenerate the cross-Mech snapshot"
            )
    return rows, manifest


def write_cross_mech_snapshot(
    result: ScanResult,
    out_dir: Path,
    *,
    worklist_snapshot_id: str,
    source_ref: str,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
) -> dict[str, Any]:
    """Write new date-stamped artifacts, refusing to replace any existing evidence."""

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
    json_text = render_cross_mech_json(rows) + "\n"
    tsv_text = render_cross_mech_tsv(rows) + "\n"

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
            "uniprotkb_accessions_unresolved": result.uniprot_unresolved,
            "uniprotkb_lookup": result.uniprot_lookup,
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
    # Encode the complete set before opening anything. Exclusive creation also
    # protects against a destination appearing after the existence check.
    artifacts = {
        out_dir / f"{snapshot_id}.json": json_text.encode("utf-8"),
        out_dir / f"{snapshot_id}.tsv": tsv_text.encode("utf-8"),
        out_dir / f"{snapshot_id}.manifest.json": (
            json.dumps(manifest, indent=2, sort_keys=True) + "\n"
        ).encode("utf-8"),
    }
    for path in artifacts:
        if path.exists() or path.is_symlink():
            raise FileExistsError(f"snapshot artifact already exists: {path}")
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    try:
        for path, data in artifacts.items():
            with path.open("xb") as handle:
                written.append(path)
                handle.write(data)
    except OSError:
        for path in written:
            path.unlink()
        raise
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
