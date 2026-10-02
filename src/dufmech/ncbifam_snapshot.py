"""Write versioned NCBIFAM HMM hit snapshots."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Iterable
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.ncbifam import (
    NCBIFAM_HMM_FTP_URL,
    NCBIFAM_TSV_FIELDNAMES,
    NcbifamHitRow,
    parse_ncbifam_hits,
    render_ncbifam_json,
    render_ncbifam_tsv,
    sort_ncbifam_rows,
)

NCBIFAM_STEM = "uniprot-ncbifam"


def collect_ncbifam_snapshot_rows(path: Path) -> list[NcbifamHitRow]:
    """Collect NCBIFAM rows from a saved HMM hit TSV."""

    return parse_ncbifam_hits(path.read_text(encoding="utf-8"))


def write_ncbifam_snapshot(
    rows: Iterable[NcbifamHitRow],
    out_dir: Path,
    *,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    seed_snapshot_id: str = "",
    hmm_hits_path: Path | None = None,
) -> dict[str, Any]:
    """Write date-stamped NCBIFAM JSON, TSV, and manifest files."""

    rows = sort_ncbifam_rows(rows)
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = _snapshot_date_text(snapshot_date)

    out_dir.mkdir(parents=True, exist_ok=True)

    snapshot_id = f"{NCBIFAM_STEM}-{snapshot_date}"
    json_path = out_dir / f"{snapshot_id}.json"
    tsv_path = out_dir / f"{snapshot_id}.tsv"
    manifest_path = out_dir / f"{snapshot_id}.manifest.json"

    json_text = render_ncbifam_json(rows) + "\n"
    tsv_text = render_ncbifam_tsv(rows) + "\n"

    json_path.write_text(json_text, encoding="utf-8")
    tsv_path.write_text(tsv_text, encoding="utf-8")

    manifest = build_ncbifam_manifest(
        rows,
        snapshot_id=snapshot_id,
        snapshot_date=snapshot_date,
        generated_at=generated_at,
        json_path=json_path,
        json_text=json_text,
        tsv_path=tsv_path,
        tsv_text=tsv_text,
        seed_snapshot_id=seed_snapshot_id,
        hmm_hits_path=hmm_hits_path,
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def build_ncbifam_manifest(
    rows: Iterable[NcbifamHitRow],
    *,
    snapshot_id: str,
    snapshot_date: str,
    generated_at: datetime,
    json_path: Path,
    json_text: str,
    tsv_path: Path,
    tsv_text: str,
    seed_snapshot_id: str = "",
    hmm_hits_path: Path | None = None,
) -> dict[str, Any]:
    """Build provenance and checksum metadata for a NCBIFAM snapshot."""

    rows = list(rows)
    model_counts = Counter(row.ncbifam_accession for row in rows)

    return {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
            "seed_snapshot_id": seed_snapshot_id,
        },
        "source": {
            "name": "NCBI Protein Family Model HMMs",
            "url": NCBIFAM_HMM_FTP_URL,
            "hmm_hits_path": "" if hmm_hits_path is None else hmm_hits_path.name,
        },
        "schema": {
            "tsv_fieldnames": NCBIFAM_TSV_FIELDNAMES,
        },
        "rows": {
            "total": len(rows),
            "unique_queries": len({row.query_id for row in rows}),
            "unique_ncbifam_accessions": len(
                {row.ncbifam_accession for row in rows}
            ),
            "with_product_name": sum(1 for row in rows if row.product_name),
            "with_gene_symbol": sum(1 for row in rows if row.gene_symbol),
            "with_ec_numbers": sum(1 for row in rows if row.ec_numbers),
            "with_go_terms": sum(1 for row in rows if row.go_terms),
            "by_ncbifam_accession": dict(sorted(model_counts.items())),
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
