"""Shared OAK validation of labels against DUF's verified frozen Pfam source."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

from dufmech.records import _publish, _writer_lock, load_yaml, safe_path
from dufmech.report import latest_snapshot_path
from dufmech.score_inputs import load_score_input
from dufmech.snapshot import WORKLIST_STEM

REPO_ROOT = Path(__file__).resolve().parents[2]
INDEX = "conf/id_labels/pfam.obo"
PROVENANCE = "conf/id_labels/provenance.json"
CONFIG_PATH = "conf/id_label_targets.yaml"
VALIDATOR = "scripts/validate_id_label_correspondence.py"
SELECTOR = "simpleobo:" + INDEX
CONFIG = {
    "adapters": {"Pfam": SELECTOR},
    "ignored_prefixes": [],
    "synonym_scope": "exact",
    "targets": [{
        "name": "frozen-pfam-family-labels", "kind": "yaml",
        "glob": "data/families/*.yaml", "pairs": [["id", "name"]],
        "policy": "canonical", "required": True, "severity": "error",
    }],
}


class IdLabelError(ValueError):
    """The frozen reference or shared correspondence check could not be trusted."""


def _sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _json_bytes(value: dict) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def _source(root: Path):
    directory = safe_path(root, "data/worklists")
    path = latest_snapshot_path(directory, WORKLIST_STEM)
    assert path is not None
    safe_path(root, path.relative_to(root).as_posix())
    for suffix in (".manifest.json", ".tsv"):
        safe_path(root, path.with_suffix(suffix).relative_to(root).as_posix())
    source = load_score_input(path, "worklist")
    if not source.rows:
        raise IdLabelError("frozen Pfam source must contain at least one family")
    return path, source


def build_artifacts(root: Path) -> dict[str, bytes]:
    """Derive a label-only OBO index from source rows, never curated records."""
    root = root.absolute()
    path, source = _source(root)
    labels = {}
    for row in source.rows:
        pfam = row.get("pfam_id")
        label = row.get("name")
        if not isinstance(pfam, str) or not re.fullmatch(r"PF[0-9]{5}", pfam):
            raise IdLabelError("source contains an invalid Pfam accession")
        if (not isinstance(label, str) or not label.strip() or label != label.strip()
                or any(ord(char) < 32 or char in "\\!{}" for char in label)):
            raise IdLabelError(f"{pfam}: source label is empty or unsafe for the label-only OBO subset")
        curie = "Pfam:" + pfam
        if curie in labels:
            raise IdLabelError(f"duplicate source identifier: {curie}")
        labels[curie] = label
    # This deliberately narrow OBO subset has no escapes, comments or modifiers.
    # The separate OAK regression checks exact adapter round trips, not a local parser.
    payload = ("format-version: 1.2\n\n" + "".join(
        f"[Term]\nid: {curie}\nname: {labels[curie]}\n\n" for curie in sorted(labels)
    )).rstrip("\n").encode("utf-8") + b"\n"
    metadata = {
        "format_version": 1,
        "kind": "derived_frozen_pfam_label_index",
        "scope": "Frozen Pfam ID/name correspondence; not live ontology or scientific validation.",
        "source_path": path.relative_to(root).as_posix(),
        "source": source.provenance,
        "index": {"path": INDEX, "selector": SELECTOR, "sha256": _sha(payload),
                  "bytes": len(payload), "entities": len(labels)},
        "derivation": "Sorted Pfam IDs and verbatim source names only; no relationships or inferred labels.",
    }
    return {INDEX: payload, PROVENANCE: _json_bytes(metadata)}


def write_index(root: Path) -> list[str]:
    """Explicitly regenerate only the two derived reference artifacts."""
    root = root.absolute()
    with _writer_lock(root):
        artifacts = build_artifacts(root)
        paths = {name: safe_path(root, name) for name in artifacts}
        changed = []
        for name, content in artifacts.items():
            path = paths[name]
            if not path.exists() or path.read_bytes() != content:
                _publish(root, path, content)
                changed.append(name)
    return changed


def _reference(root: Path) -> tuple[dict, dict[str, bytes]]:
    artifacts = build_artifacts(root)
    for name, expected in artifacts.items():
        path = safe_path(root, name)
        if not path.is_file() or path.read_bytes() != expected:
            raise IdLabelError(f"stale or missing {name}; regenerate the derived label index")
    if load_yaml(safe_path(root, CONFIG_PATH)) != CONFIG:
        raise IdLabelError("id-label configuration must enforce the complete frozen Pfam target")
    return json.loads(artifacts[PROVENANCE]), artifacts


def _record_paths(root: Path, expected: set[str]) -> list[Path]:
    directory = safe_path(root, "data/families")
    paths = sorted(directory.glob("*.yaml"))
    if {path.name for path in paths} != expected:
        raise IdLabelError("family record inventory differs from the complete frozen Pfam source")
    for path in paths:
        safe_path(root, path.relative_to(root).as_posix())
        record = load_yaml(path)
        if record.get("id") != "Pfam:" + path.stem:
            raise IdLabelError(f"{path.name}: root id must match its Pfam filename")
    return paths


def _fingerprints(root: Path, paths: list[Path]) -> dict[str, str]:
    return {path.relative_to(root).as_posix(): _sha(
        safe_path(root, path.relative_to(root).as_posix()).read_bytes()) for path in paths}


def _preflight(root: Path) -> tuple[dict, dict[str, str], set[str]]:
    root = root.absolute()
    metadata, artifacts = _reference(root)
    source_path, source = _source(root)
    if source.provenance != metadata["source"]:
        raise IdLabelError("frozen source changed while checking the reference")
    expected_names = {row["pfam_id"] + ".yaml" for row in source.rows}
    records = _record_paths(root, expected_names)
    paths = records + [safe_path(root, name) for name in (
        *artifacts, CONFIG_PATH, VALIDATOR, "scripts/chem_formula.py")]
    paths += [source_path, source_path.with_suffix(".manifest.json"),
              source_path.with_suffix(".tsv")]
    before = _fingerprints(root, paths)
    if any(before[name] != _sha(payload) for name, payload in artifacts.items()):
        raise IdLabelError("reference changed during preflight")
    return metadata, before, expected_names


def check_index(root: Path) -> dict:
    """Verify native inputs only; this is not an OAK correspondence PASS."""
    metadata, _, names = _preflight(root.absolute())
    return {"status": "REFERENCE_VERIFIED", "expected_pairs": len(names),
            "source_sha256": metadata["source"]["sha256"],
            "index_sha256": metadata["index"]["sha256"], "scope": metadata["scope"]}


def check(root: Path, claw_root: Path, *, timeout: int = 180) -> dict:
    """Run the shared CLI in CLAW's locked runtime, never import OAK into DUF."""
    root = root.absolute()
    claw_root = claw_root.absolute()
    for name in ("pyproject.toml", "uv.lock"):
        if not (claw_root / name).is_file():
            raise IdLabelError(f"CLAW runtime is missing {name}")
    metadata, before, expected_names = _preflight(root)
    command = ["uv", "run", "--project", str(claw_root), "--locked", "--offline",
               "python", "-I", "-B", str(safe_path(root, VALIDATOR)),
               "-c", str(safe_path(root, CONFIG_PATH))]
    runtime_lock = _sha((claw_root / "uv.lock").read_bytes())
    environment = {key: value for key, value in os.environ.items()
                   if key not in {"VIRTUAL_ENV", "UV_PROJECT_ENVIRONMENT", "PYTHONPATH", "PYTHONHOME"}}
    done = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=timeout,
                          check=False, env={**environment, "PYTHONDONTWRITEBYTECODE": "1"})
    if _sha((claw_root / "uv.lock").read_bytes()) != runtime_lock:
        raise IdLabelError("CLAW runtime lock changed during validation")
    _, after, after_names = _preflight(root)
    if after != before or after_names != expected_names:
        raise IdLabelError("validation inputs changed during the shared CLI check")
    counts = {key: int(value) for key, value in re.findall(
        r"^\s+([A-Z_]+): (\d+)\s*$", done.stdout, re.MULTILINE)}
    if done.returncode != 0 or counts != {"OK_CANONICAL": len(expected_names)}:
        detail = (done.stdout + "\n" + done.stderr).strip()
        raise IdLabelError(f"shared OAK validation failed or skipped pairs: {detail}")
    return {
        "status": "PASS", "scope": metadata["scope"], "checked_pairs": len(expected_names),
        "verdicts": counts, "adapter": SELECTOR,
        "source_sha256": metadata["source"]["sha256"],
        "index_sha256": metadata["index"]["sha256"],
        "validator_sha256": before[VALIDATOR],
        "config_sha256": before[CONFIG_PATH],
        "claw_lock_sha256": runtime_lock,
        "command": command, "cwd": str(root),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--claw-root", type=Path, default=os.environ.get("CLAW_ROOT"),
                        help="published CLAW checkout with its locked OAK runtime")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="validate without writing (default)")
    mode.add_argument("--apply", action="store_true", help="regenerate the two derived index files")
    mode.add_argument("--check-index", action="store_true", help="native reference check, not OAK")
    args = parser.parse_args(argv)
    try:
        if args.apply:
            result = {"changed": write_index(args.repo_root)}
        elif args.check_index:
            result = check_index(args.repo_root)
        elif args.claw_root is None:
            raise IdLabelError("--check requires --claw-root or CLAW_ROOT for the isolated runtime")
        else:
            result = check(args.repo_root, args.claw_root)
    except (OSError, ValueError, RuntimeError, ImportError, subprocess.SubprocessError) as error:
        print(f"id-label validation: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
