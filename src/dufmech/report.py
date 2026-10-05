"""Summarize frozen DUF/PUF worklist and score snapshots."""

from __future__ import annotations

import json
import re
from collections import Counter
from collections.abc import Iterable, Mapping
from datetime import date
from pathlib import Path
from typing import Any

from dufmech.provenance import check_manifest
from dufmech.scoring import PARTIALLY_CHARACTERIZED
from dufmech.scoring_snapshot import SCORE_STEM
from dufmech.worklist import KNOWN_HISTORICAL_DUF, PFAM_RE, STATUS_ORDER, UNKNOWN_CANDIDATE

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
    for path in paths:
        try:
            date.fromisoformat(path.stem[-10:])
        except ValueError as exc:
            raise ReportError(f"invalid snapshot date in {path}") from exc
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
    except (ValueError, UnicodeError) as exc:
        raise ReportError(f"{path} is not valid JSON") from exc

    if not isinstance(payload, list):
        raise ReportError(f"expected a JSON row list in {path}")
    if any(not isinstance(row, Mapping) for row in payload):
        raise ReportError(f"every row in {path} must be an object")
    return payload


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
    verified_manifest(worklist_path)
    input_ids = {"worklist": worklist_path.stem}
    worklist_rows = load_json_rows(worklist_path)
    score_rows: list[Mapping[str, Any]] = []
    if score_path is not None:
        manifest = verified_manifest(score_path)
        score_input = _mapping(manifest["snapshot"].get("input_snapshot_ids")).get("worklist")
        if score_input != worklist_path.stem:
            raise ReportError(
                f"{score_path.name} was scored against {score_input}, not {worklist_path.stem}; "
                "select matching --worklist-json/--score-json snapshots or regenerate scores"
            )
        input_ids["scores"] = score_path.stem
        score_rows = load_json_rows(score_path)
    family_index(worklist_rows, score_rows)
    return (worklist_rows, score_rows, input_ids)


def verified_manifest(path: Path) -> dict[str, Any]:
    """Return a snapshot manifest after checking its files and row counts."""

    manifest_path = path.with_suffix(".manifest.json")
    issues = check_manifest(manifest_path)
    if issues:
        raise ReportError("; ".join(issue.render() for issue in issues))
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def family_index(
    worklist_rows: Iterable[Mapping[str, Any]],
    score_rows: Iterable[Mapping[str, Any]] = (),
) -> list[dict[str, Any]]:
    """Join worklist families to score rows and return a stable display index."""

    worklist = _rows_by_pfam(worklist_rows, "worklist")
    scores = _rows_by_pfam(score_rows, "scores")
    extra = scores.keys() - worklist.keys()
    if extra:
        raise ReportError(f"score families absent from worklist: {', '.join(sorted(extra))}")
    families: list[dict[str, Any]] = []
    for pfam_id, row in worklist.items():
        score = scores.get(pfam_id, {})
        seed_status = row.get("unknown_status")
        characterization_status = score.get("characterization_status")
        if not isinstance(seed_status, str) or seed_status not in STATUS_ORDER:
            raise ReportError(f"{pfam_id}: invalid unknown_status")
        if score and (
            not isinstance(characterization_status, str)
            or characterization_status not in {
                UNKNOWN_CANDIDATE, KNOWN_HISTORICAL_DUF, PARTIALLY_CHARACTERIZED
            }
        ):
            raise ReportError(f"{pfam_id}: invalid characterization_status")
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
                **{
                    field: _optional_count(row.get(field), pfam_id, field)
                    for field in (
                        "proteins", "matches", "proteomes", "taxa", "structures",
                        "alphafold_models", "domain_architectures",
                    )
                },
                **{
                    field: _optional_count(score.get(field), pfam_id, field)
                    for field in (
                        "known_evidence_count", "partial_evidence_count", "context_evidence_count",
                    )
                },
                "description": _string(row.get("description")),
                "source_url": _string(row.get("source_url")),
            }
        )

    return sorted(
        families,
        key=lambda row: (row["proteins"] is None, -(row["proteins"] or 0), row["pfam_id"]),
    )


def build_report(
    worklist_rows: Iterable[Mapping[str, Any]],
    score_rows: Iterable[Mapping[str, Any]] = (),
    *,
    top_n: int = 10,
) -> dict[str, Any]:
    """Build corpus summary metrics for DUF/PUF snapshots."""

    if type(top_n) is not int or top_n < 0:
        raise ReportError("top_n must be a non-negative integer")
    families = family_index(worklist_rows, score_rows)
    return {
        "families": {
            "total": len(families),
            "with_interpro_id": sum(1 for row in families if row["interpro_id"]),
            "with_structures": sum(1 for row in families if (row["structures"] or 0) > 0),
            "with_alphafold_models": sum(
                1 for row in families if (row["alphafold_models"] or 0) > 0
            ),
            "with_domain_architectures": sum(
                1 for row in families if (row["domain_architectures"] or 0) > 0
            ),
            "interpro_proteins": sum(row["proteins"] or 0 for row in families),
            "interpro_matches": sum(row["matches"] or 0 for row in families),
            "missing_protein_counts": sum(row["proteins"] is None for row in families),
            "missing_match_counts": sum(row["matches"] is None for row in families),
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
            f"{_int(families.get('interpro_proteins'))} summed per-family InterPro protein counts",
            f"{_int(families.get('interpro_matches'))} summed per-family InterPro match counts",
            "Per-family sums are not counts of unique proteins or matches.",
            f"{_int(families.get('missing_protein_counts'))} families lack protein counts",
            f"{_int(families.get('missing_match_counts'))} families lack match counts",
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
    top_rows = report.get("top_by_proteins", [])
    if top_rows:
        lines.extend(["", "Top families by protein count:"])
        for row in top_rows:
            proteins = "Not available" if row["proteins"] is None else f"{row['proteins']:,}"
            lines.append(f"  {row['pfam_id']}  {proteins:>13s}  {row['short_name']}")
    return "\n".join(lines)


def _rows_by_pfam(
    rows: Iterable[Mapping[str, Any]], label: str
) -> dict[str, Mapping[str, Any]]:
    indexed: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        if not isinstance(row, Mapping):
            raise ReportError(f"every {label} row must be an object")
        pfam_id = row.get("pfam_id")
        if not isinstance(pfam_id, str) or not PFAM_RE.fullmatch(pfam_id):
            raise ReportError(f"invalid {label} pfam_id: {pfam_id!r}")
        if pfam_id in indexed:
            raise ReportError(f"duplicate {label} pfam_id: {pfam_id}")
        indexed[pfam_id] = row
    return indexed


def _optional_count(value: object, pfam_id: str, field: str) -> int | None:
    if value is None:
        return None
    if type(value) is not int or value < 0:
        raise ReportError(f"{pfam_id}: {field} must be a non-negative integer or null")
    return value


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
