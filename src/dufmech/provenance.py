"""Verify frozen DUFMech snapshot manifests."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

from dufmech.worklist_lineage import verify_worklist_parent_rows

SHA256_RE = re.compile(r"[0-9a-f]{64}")


@dataclass(frozen=True)
class ManifestIssue:
    """One manifest integrity problem."""

    manifest: str
    message: str

    def render(self) -> str:
        return f"{self.manifest}: {self.message}"


def worklist_manifest_paths(directory: Path) -> list[Path]:
    """Return sorted worklist manifest paths."""

    return sorted(directory.rglob("*.manifest.json"))


def check_worklist_manifests(directory: Path) -> list[ManifestIssue]:
    """Validate every worklist manifest under ``directory``."""

    paths = worklist_manifest_paths(directory)
    issues: list[ManifestIssue] = []
    if not paths:
        issues.append(ManifestIssue(str(directory), "no manifest files found"))
    for path in paths:
        issues.extend(check_manifest(path))
    # Path traversal includes dotfiles and ignored artifacts, unlike git-based inventories.
    for path in sorted(directory.rglob("*")):
        if path.is_symlink():
            issues.append(_issue(path, "snapshot paths must not be symlinks"))
        elif path.suffix in {".json", ".tsv"} and not path.name.endswith(".manifest.json"):
            manifest = path.with_suffix(".manifest.json")
            if manifest not in paths:
                issues.append(_issue(path, "artifact has no manifest"))
    return issues


def check_manifest(manifest_path: Path) -> list[ManifestIssue]:
    """Validate one snapshot manifest."""

    if manifest_path.is_symlink():
        return [_issue(manifest_path, "manifest must not be a symlink")]
    try:
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    except OSError as exc:
        return [_issue(manifest_path, f"could not read manifest: {exc}")]
    except (ValueError, UnicodeError) as exc:
        return [_issue(manifest_path, f"invalid JSON: {exc}")]

    if not isinstance(payload, Mapping):
        return [_issue(manifest_path, "manifest must be a JSON object")]

    snapshot = _mapping(payload.get("snapshot"))
    snapshot_id = _string(snapshot.get("id"))
    issues: list[ManifestIssue] = []
    expected_id = manifest_path.name.removesuffix(".manifest.json")
    if not snapshot_id or snapshot_id != expected_id:
        issues.append(_issue(manifest_path, "snapshot.id must match the manifest filename"))
    snapshot_date = _string(snapshot.get("date"))
    try:
        if date.fromisoformat(snapshot_date).isoformat() != snapshot_date:
            raise ValueError
        if not snapshot_id.endswith(f"-{snapshot_date}"):
            raise ValueError
    except ValueError:
        issues.append(_issue(manifest_path, "snapshot.date must be an ISO date matching snapshot.id"))
    try:
        timestamp = datetime.fromisoformat(
            _string(snapshot.get("generated_at")).replace("Z", "+00:00")
        )
        if timestamp.tzinfo is None:
            raise ValueError
    except ValueError:
        issues.append(_issue(manifest_path, "snapshot.generated_at must include a timezone"))
    if snapshot_id.startswith("duf-characterization-scores-"):
        if not _string(_mapping(snapshot.get("input_snapshot_ids")).get("worklist")):
            issues.append(_issue(manifest_path, "snapshot.input_snapshot_ids.worklist is required"))
    else:
        source = _mapping(payload.get("source"))
        if not _string(source.get("name")) or not _string(source.get("url")):
            issues.append(_issue(manifest_path, "source.name and source.url are required"))

    files = _mapping(payload.get("files"))
    for label in ("json", "tsv"):
        if _mapping(files.get(label)).get("path") != f"{expected_id}.{label}":
            issues.append(_issue(manifest_path, f"files.{label}.path must be {expected_id}.{label}"))
    file_issues: list[ManifestIssue] = []
    for label, entry in sorted(files.items()):
        file_issues.extend(_check_file_entry(manifest_path, str(label), _mapping(entry)))
    issues.extend(file_issues)
    if not file_issues and all(
        _mapping(files.get(label)).get("path") == f"{expected_id}.{label}"
        for label in ("json", "tsv")
    ):
        issues.extend(_check_rows(manifest_path, payload, expected_id))
    return issues


def sha256(path: Path) -> str:
    """Return a file's sha256 digest."""

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _check_file_entry(
    manifest_path: Path,
    label: str,
    entry: Mapping[str, Any],
) -> list[ManifestIssue]:
    issues: list[ManifestIssue] = []
    raw_path = _string(entry.get("path"))
    expected_bytes = entry.get("bytes")
    expected_sha256 = _string(entry.get("sha256"))

    if not raw_path:
        issues.append(_issue(manifest_path, f"files.{label}.path is required"))
    elif Path(raw_path).name != raw_path:
        issues.append(_issue(manifest_path, f"files.{label}.path must be a filename"))

    if type(expected_bytes) is not int or expected_bytes < 0:
        issues.append(_issue(manifest_path, f"files.{label}.bytes must be a non-negative integer"))
    if not SHA256_RE.fullmatch(expected_sha256):
        issues.append(_issue(manifest_path, f"files.{label}.sha256 must be 64 lowercase hex characters"))

    if issues or not raw_path:
        return issues

    path = manifest_path.parent / raw_path
    if path.is_symlink():
        return [_issue(manifest_path, f"files.{label}.path must not be a symlink")]
    if not path.is_file():
        return [_issue(manifest_path, f"files.{label}.path is missing: {raw_path}")]

    try:
        if path.stat().st_size != expected_bytes:
            issues.append(_issue(manifest_path, f"files.{label}.bytes differs for {raw_path}"))
        if sha256(path) != expected_sha256:
            issues.append(_issue(manifest_path, f"files.{label}.sha256 differs for {raw_path}"))
    except OSError as exc:
        issues.append(_issue(manifest_path, f"could not read {raw_path}: {exc}"))
    return issues


def _check_rows(
    manifest_path: Path, payload: Mapping[str, Any], snapshot_id: str
) -> list[ManifestIssue]:
    total = _mapping(payload.get("rows")).get("total")
    fields = _mapping(payload.get("schema")).get("tsv_fieldnames")
    issues: list[ManifestIssue] = []
    if type(total) is not int or total < 0:
        issues.append(_issue(manifest_path, "rows.total must be a non-negative integer"))
    if (
        not isinstance(fields, list)
        or not fields
        or any(not isinstance(field, str) or not field for field in fields)
        or len(fields) != len(set(fields))
    ):
        issues.append(_issue(manifest_path, "schema.tsv_fieldnames must be unique nonempty strings"))
        return issues
    try:
        rows = json.loads((manifest_path.parent / f"{snapshot_id}.json").read_text("utf-8"))
        if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
            issues.append(_issue(manifest_path, "JSON artifact must be a list of objects"))
        elif len(rows) != total:
            issues.append(_issue(manifest_path, "JSON row count differs from rows.total"))
        with (manifest_path.parent / f"{snapshot_id}.tsv").open(
            encoding="utf-8", newline=""
        ) as handle:
            reader = csv.reader(handle, delimiter="\t", strict=True)
            if next(reader, None) != fields:
                issues.append(_issue(manifest_path, "TSV header differs from schema.tsv_fieldnames"))
            count = 0
            invalid_width = False
            for row in reader:
                count += 1
                invalid_width |= len(row) != len(fields)
            if invalid_width:
                issues.append(_issue(manifest_path, "TSV row width differs from schema.tsv_fieldnames"))
            if count != total:
                issues.append(_issue(manifest_path, "TSV row count differs from rows.total"))
        if not issues:
            verify_worklist_parent_rows(manifest_path, payload, rows)
    except (OSError, ValueError, UnicodeError, csv.Error) as exc:
        issues.append(_issue(manifest_path, f"could not parse snapshot rows: {exc}"))
    return issues


def _issue(manifest_path: Path, message: str) -> ManifestIssue:
    return ManifestIssue(manifest_path.name, message)


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _string(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""
