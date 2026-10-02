"""Write versioned EFI-GNT Pfam-neighbor snapshots."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Iterable
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.efi_gnt import (
    EFI_GNT_TSV_FIELDNAMES,
    EFI_GNT_URL,
    EfiGntNeighborRow,
    parse_pfam_neighbor_table,
    render_efi_gnt_json,
    render_efi_gnt_tsv,
    sort_efi_gnt_rows,
)

EFI_GNT_STEM = "efi-gnt-pfam-neighbors"


def collect_efi_gnt_snapshot_rows(path: Path) -> list[EfiGntNeighborRow]:
    """Collect EFI-GNT rows from a saved Pfam Neighbor Mapping Table TSV."""

    return parse_pfam_neighbor_table(path.read_text(encoding="utf-8"))


def write_efi_gnt_snapshot(
    rows: Iterable[EfiGntNeighborRow],
    out_dir: Path,
    *,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    seed_snapshot_id: str = "",
    pfam_neighbors_path: Path | None = None,
) -> dict[str, Any]:
    """Write date-stamped EFI-GNT JSON, TSV, and manifest files."""

    rows = sort_efi_gnt_rows(rows)
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = _snapshot_date_text(snapshot_date)

    out_dir.mkdir(parents=True, exist_ok=True)

    snapshot_id = f"{EFI_GNT_STEM}-{snapshot_date}"
    json_path = out_dir / f"{snapshot_id}.json"
    tsv_path = out_dir / f"{snapshot_id}.tsv"
    manifest_path = out_dir / f"{snapshot_id}.manifest.json"

    json_text = render_efi_gnt_json(rows) + "\n"
    tsv_text = render_efi_gnt_tsv(rows) + "\n"

    json_path.write_text(json_text, encoding="utf-8")
    tsv_path.write_text(tsv_text, encoding="utf-8")

    manifest = build_efi_gnt_manifest(
        rows,
        snapshot_id=snapshot_id,
        snapshot_date=snapshot_date,
        generated_at=generated_at,
        json_path=json_path,
        json_text=json_text,
        tsv_path=tsv_path,
        tsv_text=tsv_text,
        seed_snapshot_id=seed_snapshot_id,
        pfam_neighbors_path=pfam_neighbors_path,
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def build_efi_gnt_manifest(
    rows: Iterable[EfiGntNeighborRow],
    *,
    snapshot_id: str,
    snapshot_date: str,
    generated_at: datetime,
    json_path: Path,
    json_text: str,
    tsv_path: Path,
    tsv_text: str,
    seed_snapshot_id: str = "",
    pfam_neighbors_path: Path | None = None,
) -> dict[str, Any]:
    """Build provenance and checksum metadata for an EFI-GNT snapshot."""

    rows = list(rows)
    pfam_counts = Counter(row.neighbor_pfam for row in rows)

    return {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
            "seed_snapshot_id": seed_snapshot_id,
        },
        "source": {
            "name": "EFI-GNT Pfam Neighbor Mapping Table",
            "url": EFI_GNT_URL,
            "pfam_neighbors_path": (
                "" if pfam_neighbors_path is None else pfam_neighbors_path.name
            ),
        },
        "schema": {
            "tsv_fieldnames": EFI_GNT_TSV_FIELDNAMES,
        },
        "rows": {
            "total": len(rows),
            "unique_queries": len({row.query_id for row in rows}),
            "unique_neighbors": len({row.neighbor_id for row in rows}),
            "unique_neighbor_pfams": len({row.neighbor_pfam for row in rows}),
            "unique_ssn_query_clusters": len(
                {
                    row.ssn_query_cluster_number
                    for row in rows
                    if row.ssn_query_cluster_number
                }
            ),
            "with_distance": sum(
                1 for row in rows if row.query_neighbor_distance is not None
            ),
            "by_neighbor_pfam": dict(sorted(pfam_counts.items())),
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
