"""Verify frozen DUFMech snapshot manifests."""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

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

    return sorted(directory.glob("*.manifest.json"))


def check_worklist_manifests(directory: Path) -> list[ManifestIssue]:
    """Validate every worklist manifest under ``directory``."""

    paths = worklist_manifest_paths(directory)
    if not paths:
        return [ManifestIssue(str(directory), "no manifest files found")]

    issues: list[ManifestIssue] = []
    for path in paths:
        issues.extend(check_manifest(path))
    return issues


def check_manifest(manifest_path: Path) -> list[ManifestIssue]:
    """Validate one snapshot manifest."""

    try:
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    except OSError as exc:
        return [_issue(manifest_path, f"could not read manifest: {exc}")]
    except json.JSONDecodeError as exc:
        return [_issue(manifest_path, f"invalid JSON: {exc}")]

    if not isinstance(payload, Mapping):
        return [_issue(manifest_path, "manifest must be a JSON object")]

    snapshot = _mapping(payload.get("snapshot"))
    snapshot_id = _string(snapshot.get("id"))
    if not snapshot_id:
        return [_issue(manifest_path, "snapshot.id is required")]

    files = _mapping(payload.get("files"))
    if not files:
        return [_issue(manifest_path, "files is required")]

    issues: list[ManifestIssue] = []
    for label, entry in sorted(files.items()):
        issues.extend(_check_file_entry(manifest_path, str(label), _mapping(entry)))
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

    if not isinstance(expected_bytes, int) or expected_bytes < 0:
        issues.append(_issue(manifest_path, f"files.{label}.bytes must be a non-negative integer"))
    if not SHA256_RE.fullmatch(expected_sha256):
        issues.append(_issue(manifest_path, f"files.{label}.sha256 must be 64 lowercase hex characters"))

    if issues or not raw_path:
        return issues

    path = manifest_path.parent / raw_path
    if not path.is_file():
        return [_issue(manifest_path, f"files.{label}.path is missing: {raw_path}")]

    if path.stat().st_size != expected_bytes:
        issues.append(_issue(manifest_path, f"files.{label}.bytes differs for {raw_path}"))
    if sha256(path) != expected_sha256:
        issues.append(_issue(manifest_path, f"files.{label}.sha256 differs for {raw_path}"))
    return issues


def _issue(manifest_path: Path, message: str) -> ManifestIssue:
    return ManifestIssue(manifest_path.name, message)


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _string(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""
