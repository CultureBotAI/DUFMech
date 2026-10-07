"""Write versioned DUF characterization score snapshots."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Iterable, Mapping
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.score_inputs import ScoreInputError, score_input_validation
from dufmech.scoring import (
    SCORE_TSV_FIELDNAMES,
    FamilyScoreRow,
    render_scores_json,
    render_scores_tsv,
)
from dufmech.snapshot import write_snapshot_artifacts

SCORE_STEM = "duf-characterization-scores"


def write_score_snapshot(
    rows: Iterable[FamilyScoreRow],
    out_dir: Path,
    *,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    input_snapshot_ids: Mapping[str, str] | None = None,
    input_provenance: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Write date-stamped DUF characterization JSON, TSV, and manifest files."""

    rows = sorted(rows, key=lambda row: (row.characterization_status, row.pfam_id))
    if len({row.pfam_id for row in rows}) != len(rows):
        raise ScoreInputError("duplicate score family identifiers")
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = _snapshot_date_text(snapshot_date)

    snapshot_id = f"{SCORE_STEM}-{snapshot_date}"
    json_path = out_dir / f"{snapshot_id}.json"
    tsv_path = out_dir / f"{snapshot_id}.tsv"
    manifest_path = out_dir / f"{snapshot_id}.manifest.json"

    json_text = render_scores_json(rows) + "\n"
    tsv_text = render_scores_tsv(rows) + "\n"

    manifest = build_score_manifest(
        rows,
        snapshot_id=snapshot_id,
        snapshot_date=snapshot_date,
        generated_at=generated_at,
        json_path=json_path,
        json_text=json_text,
        tsv_path=tsv_path,
        tsv_text=tsv_text,
        input_snapshot_ids=input_snapshot_ids or {},
        input_provenance=input_provenance or {},
    )
    write_snapshot_artifacts(
        out_dir,
        {json_path.name: json_text, tsv_path.name: tsv_text,
         manifest_path.name: json.dumps(manifest, indent=2, sort_keys=True) + "\n"},
    )
    return manifest


def build_score_manifest(
    rows: Iterable[FamilyScoreRow],
    *,
    snapshot_id: str,
    snapshot_date: str,
    generated_at: datetime,
    json_path: Path,
    json_text: str,
    tsv_path: Path,
    tsv_text: str,
    input_snapshot_ids: Mapping[str, str] | None = None,
    input_provenance: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build provenance and checksum metadata for a score snapshot."""

    rows = list(rows)
    status_counts = Counter(row.characterization_status for row in rows)
    demotion_counts = Counter(reason for row in rows for reason in row.demotion_reasons)
    input_ids = dict(sorted((input_snapshot_ids or {}).items()))
    provenance = dict(sorted((input_provenance or {}).items()))
    validation = score_input_validation(input_ids, provenance)

    return {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
            "input_snapshot_ids": input_ids,
        },
        "input_provenance_version": 1,
        "input_validation": validation,
        "input_provenance": provenance,
        "schema": {
            "tsv_fieldnames": SCORE_TSV_FIELDNAMES,
        },
        "rows": {
            "total": len(rows),
            "by_characterization_status": dict(sorted(status_counts.items())),
            "by_demotion_reason": dict(sorted(demotion_counts.items())),
            "with_known_evidence": sum(1 for row in rows if row.known_evidence_count),
            "with_partial_evidence": sum(
                1 for row in rows if row.partial_evidence_count
            ),
            "with_context_evidence": sum(
                1 for row in rows if row.context_evidence_count
            ),
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
