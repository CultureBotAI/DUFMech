"""Write versioned eggNOG-mapper annotation snapshots."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Iterable
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.eggnog import (
    EGGNOG_MAPPER_URL,
    EGGNOG_TSV_FIELDNAMES,
    EggNogAnnotationRow,
    parse_emapper_annotations,
    render_eggnog_json,
    render_eggnog_tsv,
)

EGGNOG_STEM = "eggnog-mapper"


def collect_eggnog_snapshot_rows(path: Path) -> list[EggNogAnnotationRow]:
    """Collect eggNOG-mapper rows from a saved annotations TSV."""

    return parse_emapper_annotations(path.read_text(encoding="utf-8"))


def write_eggnog_snapshot(
    rows: Iterable[EggNogAnnotationRow],
    out_dir: Path,
    *,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    seed_snapshot_id: str = "",
    annotations_path: Path | None = None,
) -> dict[str, Any]:
    """Write date-stamped eggNOG JSON, TSV, and manifest files."""

    rows = sorted(rows, key=lambda row: row.query_id)
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = _snapshot_date_text(snapshot_date)

    out_dir.mkdir(parents=True, exist_ok=True)

    snapshot_id = f"{EGGNOG_STEM}-{snapshot_date}"
    json_path = out_dir / f"{snapshot_id}.json"
    tsv_path = out_dir / f"{snapshot_id}.tsv"
    manifest_path = out_dir / f"{snapshot_id}.manifest.json"

    json_text = render_eggnog_json(rows) + "\n"
    tsv_text = render_eggnog_tsv(rows) + "\n"

    json_path.write_text(json_text, encoding="utf-8")
    tsv_path.write_text(tsv_text, encoding="utf-8")

    manifest = build_eggnog_manifest(
        rows,
        snapshot_id=snapshot_id,
        snapshot_date=snapshot_date,
        generated_at=generated_at,
        json_path=json_path,
        json_text=json_text,
        tsv_path=tsv_path,
        tsv_text=tsv_text,
        seed_snapshot_id=seed_snapshot_id,
        annotations_path=annotations_path,
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def build_eggnog_manifest(
    rows: Iterable[EggNogAnnotationRow],
    *,
    snapshot_id: str,
    snapshot_date: str,
    generated_at: datetime,
    json_path: Path,
    json_text: str,
    tsv_path: Path,
    tsv_text: str,
    seed_snapshot_id: str = "",
    annotations_path: Path | None = None,
) -> dict[str, Any]:
    """Build provenance and checksum metadata for an eggNOG snapshot."""

    rows = list(rows)
    cog_counts = Counter(row.cog_category or "UNKNOWN" for row in rows)

    return {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
            "seed_snapshot_id": seed_snapshot_id,
        },
        "source": {
            "name": "eggNOG-mapper annotations",
            "url": EGGNOG_MAPPER_URL,
            "annotations_path": "" if annotations_path is None else annotations_path.name,
        },
        "schema": {
            "tsv_fieldnames": EGGNOG_TSV_FIELDNAMES,
        },
        "rows": {
            "total": len(rows),
            "unique_queries": len({row.query_id for row in rows}),
            "with_eggnog_ogs": sum(1 for row in rows if row.eggnog_ogs),
            "with_go_terms": sum(1 for row in rows if row.go_terms),
            "with_ec_numbers": sum(1 for row in rows if row.ec_numbers),
            "with_pfams": sum(1 for row in rows if row.pfams),
            "with_preferred_name": sum(1 for row in rows if row.preferred_name),
            "by_cog_category": dict(sorted(cog_counts.items())),
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
