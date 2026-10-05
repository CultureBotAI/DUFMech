"""Write versioned DUF/Pfam worklist snapshots."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Iterable, Mapping
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.worklist import (
    EXTRA_FIELDS,
    INTERPRO_PFAM_URL,
    TSV_FIELDNAMES,
    DufFamilyRow,
    render_json,
    render_tsv,
)

WORKLIST_STEM = "interpro-pfam-duf"


def write_worklist_snapshot(
    rows: Iterable[DufFamilyRow],
    out_dir: Path,
    *,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    search: str = "DUF",
    page_size: int = 200,
    include_false_positives: bool = False,
) -> dict[str, Any]:
    """Write a date-stamped JSON/TSV worklist and manifest."""

    rows = list(rows)
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = _snapshot_date_text(snapshot_date)

    snapshot_id = f"{WORKLIST_STEM}-{snapshot_date}"
    json_path = out_dir / f"{snapshot_id}.json"
    tsv_path = out_dir / f"{snapshot_id}.tsv"
    manifest_path = out_dir / f"{snapshot_id}.manifest.json"

    json_text = render_json(rows) + "\n"
    tsv_text = render_tsv(rows) + "\n"

    manifest = build_worklist_manifest(
        rows,
        snapshot_id=snapshot_id,
        snapshot_date=snapshot_date,
        generated_at=generated_at,
        json_path=json_path,
        json_text=json_text,
        tsv_path=tsv_path,
        tsv_text=tsv_text,
        search=search,
        page_size=page_size,
        include_false_positives=include_false_positives,
    )
    write_snapshot_artifacts(
        out_dir,
        {
            json_path.name: json_text,
            tsv_path.name: tsv_text,
            manifest_path.name: json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        },
    )
    return manifest


def write_snapshot_artifacts(out_dir: Path, artifacts: Mapping[str, str]) -> None:
    """Write a complete new worklist artifact set, never overwriting existing files."""

    if any(not name or Path(name).name != name or name in {".", ".."} for name in artifacts):
        raise ValueError("snapshot artifact names must be filenames")
    encoded = {name: text.encode("utf-8") for name, text in artifacts.items()}
    for name in encoded:
        target = out_dir / name
        if target.exists() or target.is_symlink():
            raise FileExistsError(f"snapshot artifact already exists: {target}")
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    try:
        for name, data in encoded.items():
            target = out_dir / name
            # Exclusive creation also protects against a target appearing after preflight.
            with target.open("xb") as handle:
                written.append(target)
                handle.write(data)
    except OSError:
        for target in written:
            target.unlink()
        raise


def build_worklist_manifest(
    rows: Iterable[DufFamilyRow],
    *,
    snapshot_id: str,
    snapshot_date: str,
    generated_at: datetime,
    json_path: Path,
    json_text: str,
    tsv_path: Path,
    tsv_text: str,
    search: str = "DUF",
    page_size: int = 200,
    include_false_positives: bool = False,
) -> dict[str, Any]:
    """Build provenance and checksum metadata for a worklist snapshot."""

    rows = list(rows)
    status_counts = Counter(row.unknown_status for row in rows)
    reason_counts = Counter(
        reason for row in rows for reason in row.candidate_reasons
    )

    return {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
        },
        "source": {
            "name": "InterPro Pfam API",
            "url": INTERPRO_PFAM_URL,
            "search": search,
            "page_size": page_size,
            "extra_fields": EXTRA_FIELDS,
            "include_false_positives": include_false_positives,
        },
        "schema": {
            "tsv_fieldnames": TSV_FIELDNAMES,
        },
        "rows": {
            "total": len(rows),
            "by_unknown_status": dict(sorted(status_counts.items())),
            "by_candidate_reason": dict(sorted(reason_counts.items())),
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
