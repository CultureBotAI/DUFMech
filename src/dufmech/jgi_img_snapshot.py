"""Write versioned JGI IMG gene-neighborhood snapshots."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Iterable
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.jgi_img import (
    JGI_IMG_TSV_FIELDNAMES,
    JGI_IMG_URL,
    JgiImgNeighborRow,
    parse_gene_neighborhood_table,
    render_jgi_img_json,
    render_jgi_img_tsv,
    sort_jgi_img_rows,
)

JGI_IMG_STEM = "jgi-img-gene-neighborhoods"


def collect_jgi_img_snapshot_rows(path: Path) -> list[JgiImgNeighborRow]:
    """Collect JGI IMG rows from a saved gene-neighborhood TSV."""

    return parse_gene_neighborhood_table(path.read_text(encoding="utf-8"))


def write_jgi_img_snapshot(
    rows: Iterable[JgiImgNeighborRow],
    out_dir: Path,
    *,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    seed_snapshot_id: str = "",
    gene_neighbors_path: Path | None = None,
) -> dict[str, Any]:
    """Write date-stamped JGI IMG JSON, TSV, and manifest files."""

    rows = sort_jgi_img_rows(rows)
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = _snapshot_date_text(snapshot_date)

    out_dir.mkdir(parents=True, exist_ok=True)

    snapshot_id = f"{JGI_IMG_STEM}-{snapshot_date}"
    json_path = out_dir / f"{snapshot_id}.json"
    tsv_path = out_dir / f"{snapshot_id}.tsv"
    manifest_path = out_dir / f"{snapshot_id}.manifest.json"

    json_text = render_jgi_img_json(rows) + "\n"
    tsv_text = render_jgi_img_tsv(rows) + "\n"

    json_path.write_text(json_text, encoding="utf-8")
    tsv_path.write_text(tsv_text, encoding="utf-8")

    manifest = build_jgi_img_manifest(
        rows,
        snapshot_id=snapshot_id,
        snapshot_date=snapshot_date,
        generated_at=generated_at,
        json_path=json_path,
        json_text=json_text,
        tsv_path=tsv_path,
        tsv_text=tsv_text,
        seed_snapshot_id=seed_snapshot_id,
        gene_neighbors_path=gene_neighbors_path,
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def build_jgi_img_manifest(
    rows: Iterable[JgiImgNeighborRow],
    *,
    snapshot_id: str,
    snapshot_date: str,
    generated_at: datetime,
    json_path: Path,
    json_text: str,
    tsv_path: Path,
    tsv_text: str,
    seed_snapshot_id: str = "",
    gene_neighbors_path: Path | None = None,
) -> dict[str, Any]:
    """Build provenance and checksum metadata for a JGI IMG snapshot."""

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
            "name": "JGI IMG gene-neighborhood table",
            "url": JGI_IMG_URL,
            "gene_neighbors_path": (
                "" if gene_neighbors_path is None else gene_neighbors_path.name
            ),
        },
        "schema": {
            "tsv_fieldnames": JGI_IMG_TSV_FIELDNAMES,
        },
        "rows": {
            "total": len(rows),
            "unique_queries": len({row.query_id for row in rows}),
            "unique_img_genomes": len(
                {row.img_genome_id for row in rows if row.img_genome_id}
            ),
            "unique_query_genes": len(
                {row.query_gene_oid for row in rows if row.query_gene_oid}
            ),
            "unique_neighbor_genes": len({row.neighbor_gene_oid for row in rows}),
            "unique_neighbor_pfams": len({row.neighbor_pfam for row in rows}),
            "unique_scaffolds": len({row.scaffold_id for row in rows if row.scaffold_id}),
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
