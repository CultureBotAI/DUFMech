"""Summarize frozen DUF/PUF worklist and score snapshots."""

from __future__ import annotations

import json
import re
from collections import Counter
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

from dufmech.scoring_snapshot import SCORE_STEM

WORKLIST_STEM = "interpro-pfam-duf"


class ReportError(RuntimeError):
    """Raised when a report input cannot be loaded."""


def latest_snapshot_path(directory: Path, stem: str, *, required: bool = True) -> Path | None:
    """Return the latest date-stamped JSON snapshot with ``stem`` under a directory."""

    pattern = re.compile(rf"^{re.escape(stem)}-\d{{4}}-\d{{2}}-\d{{2}}\.json$")
    paths = sorted(
        path
        for path in directory.glob(f"{stem}-*.json")
        if pattern.fullmatch(path.name)
    )
    if paths:
        return paths[-1]
    if required:
        raise ReportError(f"no {stem} JSON snapshots found under {directory}")
    return None


def load_json_rows(path: Path) -> list[Mapping[str, Any]]:
    """Load a frozen JSON row list."""

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ReportError(f"could not read {path}") from exc
    except json.JSONDecodeError as exc:
        raise ReportError(f"{path} is not valid JSON") from exc

    if not isinstance(payload, list):
        raise ReportError(f"expected a JSON row list in {path}")
    return [row for row in payload if isinstance(row, Mapping)]


def load_latest_rows(
    worklists_dir: Path,
    *,
    worklist_json: Path | None = None,
    score_json: Path | None = None,
) -> tuple[list[Mapping[str, Any]], list[Mapping[str, Any]], dict[str, str]]:
    """Load the requested or latest worklist and optional score snapshots."""

    worklist_path = worklist_json or latest_snapshot_path(worklists_dir, WORKLIST_STEM)
    score_path = score_json or latest_snapshot_path(worklists_dir, SCORE_STEM, required=False)

    assert worklist_path is not None
    input_ids = {"worklist": worklist_path.stem}
    worklist_rows = load_json_rows(worklist_path)
    score_rows: list[Mapping[str, Any]] = []
    if score_path is not None:
        input_ids["scores"] = score_path.stem
        score_rows = load_json_rows(score_path)
    return (worklist_rows, score_rows, input_ids)


def family_index(
    worklist_rows: Iterable[Mapping[str, Any]],
    score_rows: Iterable[Mapping[str, Any]] = (),
) -> list[dict[str, Any]]:
    """Join worklist families to score rows and return a stable display index."""

    scores = {
        _string(row.get("pfam_id")): row
        for row in score_rows
        if isinstance(row, Mapping) and _string(row.get("pfam_id"))
    }
    families: list[dict[str, Any]] = []
    for row in worklist_rows:
        if not isinstance(row, Mapping):
            continue
        pfam_id = _string(row.get("pfam_id"))
        if not pfam_id:
            continue
        score = scores.get(pfam_id, {})
        families.append(
            {
                "pfam_id": pfam_id,
                "short_name": _string(row.get("short_name")),
                "name": _string(row.get("name")),
                "interpro_id": _string(row.get("interpro_id")),
                "unknown_status": _string(row.get("unknown_status")),
                "characterization_status": _string(
                    score.get("characterization_status")
                ),
                "candidate_reasons": _string_list(row.get("candidate_reasons")),
                "demotion_reasons": _string_list(score.get("demotion_reasons")),
                "proteins": _int(row.get("proteins")),
                "matches": _int(row.get("matches")),
                "proteomes": _int(row.get("proteomes")),
                "taxa": _int(row.get("taxa")),
                "structures": _int(row.get("structures")),
                "alphafold_models": _int(row.get("alphafold_models")),
                "domain_architectures": _int(row.get("domain_architectures")),
                "known_evidence_count": _int(score.get("known_evidence_count")),
                "partial_evidence_count": _int(score.get("partial_evidence_count")),
                "context_evidence_count": _int(score.get("context_evidence_count")),
                "description": _string(row.get("description")),
                "source_url": _string(row.get("source_url")),
            }
        )

    return sorted(families, key=lambda row: (-row["proteins"], row["pfam_id"]))


def build_report(
    worklist_rows: Iterable[Mapping[str, Any]],
    score_rows: Iterable[Mapping[str, Any]] = (),
    *,
    top_n: int = 10,
) -> dict[str, Any]:
    """Build corpus summary metrics for DUF/PUF snapshots."""

    families = family_index(worklist_rows, score_rows)
    return {
        "families": {
            "total": len(families),
            "with_interpro_id": sum(1 for row in families if row["interpro_id"]),
            "with_structures": sum(1 for row in families if row["structures"] > 0),
            "with_alphafold_models": sum(
                1 for row in families if row["alphafold_models"] > 0
            ),
            "with_domain_architectures": sum(
                1 for row in families if row["domain_architectures"] > 0
            ),
            "interpro_proteins": sum(row["proteins"] for row in families),
            "interpro_matches": sum(row["matches"] for row in families),
        },
        "by_unknown_status": dict(
            _sorted_counter(row["unknown_status"] or "UNKNOWN" for row in families)
        ),
        "by_characterization_status": dict(
            sorted(
                Counter(
                    row["characterization_status"] or "UNSCORED"
                    for row in families
                ).items()
            )
        ),
        "by_candidate_reason": dict(
            _sorted_counter(
                reason
                for row in families
                for reason in row["candidate_reasons"]
            )
        ),
        "by_demotion_reason": dict(
            _sorted_counter(
                reason
                for row in families
                for reason in row["demotion_reasons"]
            )
        ),
        "top_by_proteins": families[:top_n],
    }


def render_report_text(report: Mapping[str, Any], *, input_ids: Mapping[str, str]) -> str:
    """Render a human-readable DUF/PUF corpus report."""

    families = _mapping(report.get("families"))
    lines = [
        "DUFMech corpus report",
        "",
        "Inputs:",
    ]
    for key, value in sorted(input_ids.items()):
        lines.append(f"  {key:8s} {value}")

    lines.extend(
        [
            "",
            f"{_int(families.get('total'))} DUF/Pfam worklist families",
            f"{_int(families.get('with_interpro_id'))} with InterPro integration",
            f"{_int(families.get('with_structures'))} with InterPro structure counters",
            (
                f"{_int(families.get('with_alphafold_models'))} with AlphaFold DB "
                "model counters"
            ),
            f"{_int(families.get('interpro_proteins'))} InterPro proteins",
            f"{_int(families.get('interpro_matches'))} InterPro matches",
        ]
    )

    _append_counter(lines, "Unknown-function seed status", report.get("by_unknown_status"))
    _append_counter(
        lines,
        "Characterization status",
        report.get("by_characterization_status"),
    )
    _append_counter(lines, "Candidate reasons", report.get("by_candidate_reason"))
    _append_counter(lines, "Demotion reasons", report.get("by_demotion_reason"))
    return "\n".join(lines)


def _append_counter(lines: list[str], title: str, payload: object) -> None:
    rows = _mapping(payload)
    if not rows:
        return
    lines.extend(["", f"{title}:"])
    for key, value in rows.items():
        lines.append(f"  {key:36s} {_int(value):6d}")


def _sorted_counter(values: Iterable[str]) -> list[tuple[str, int]]:
    return sorted(Counter(values).items())


def _int(value: object) -> int:
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    return 0


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _string(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""


def _string_list(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, str) and item]
