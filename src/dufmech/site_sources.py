"""Explicit, content-verified website source pins, independent of checkout history."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path, PurePosixPath

from dufmech.report import ReportError

REPOSITORY = "https://github.com/CultureBotAI/DUFMech"
LEDGER = Path("conf/site_source_pins.json")
SOURCE_ROOTS = (
    "data/worklists", "data/cross_mech", "data/families", "curation/families", "history",
    "reports/yaml_record_review", "reports/yaml_category_review", "reports/repo_review",
    "reviews/structured",
    "src/dufmech/schema",
)


def source_path(value: str) -> bool:
    path = PurePosixPath(value)
    return (bool(re.fullmatch(r"[A-Za-z0-9_./-]+", value))
            and not path.is_absolute() and ".." not in path.parts
            and path.as_posix() == value
            and any(value.startswith(prefix + "/") for prefix in SOURCE_ROOTS))


def source_bytes(root: Path, relative: str) -> bytes:
    path = root / relative
    for component in (path, *path.parents):
        if component == root:
            break
        if component.is_symlink():
            raise ReportError(f"source pin cannot follow a symlink: {relative}")
    try:
        return path.read_bytes()
    except OSError as exc:
        raise ReportError(f"cannot read pinned site source: {relative}") from exc


def load_source_pins(root: Path, *, required: bool = False) -> dict[str, dict[str, str]]:
    """Check the committed ledger against actual bytes, with no Git or network calls."""
    root = root.resolve()
    ledger = root / LEDGER
    if ledger.is_symlink() or ledger.parent.is_symlink():
        raise ReportError("site source pin ledger must not be a symlink")
    if not ledger.exists() and not required:
        return {}
    try:
        payload = json.loads(ledger.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ReportError(f"cannot read site source pin ledger: {LEDGER}") from exc
    if (not isinstance(payload, dict) or set(payload) != {"version", "repository", "commit", "files"}
            or type(payload["version"]) is not int or payload["version"] != 1
            or payload["repository"] != REPOSITORY
            or not isinstance(payload["commit"], str)
            or not re.fullmatch(r"[0-9a-f]{40}", payload["commit"])
            or not isinstance(payload["files"], dict) or not payload["files"]):
        raise ReportError("invalid site source pin ledger")
    result = {}
    for relative, digest in sorted(payload["files"].items()):
        if (not source_path(relative) or not isinstance(digest, str)
                or not re.fullmatch(r"[0-9a-f]{64}", digest)):
            raise ReportError(f"invalid site source pin: {relative}")
        if hashlib.sha256(source_bytes(root, relative)).hexdigest() != digest:
            raise ReportError(f"site source pin bytes differ: {relative}; capture a new source checkpoint")
        result[relative] = {"repository": REPOSITORY, "commit": payload["commit"],
                            "path": relative, "sha256": digest}
    return result


def capture_source_pins(root: Path, commit: str) -> dict:
    """Verify an operator-supplied published commit locally before writing its ledger.

    This offline operation cannot establish remote reachability; publication of the
    supplied checkpoint is the operator's prerequisite, not a claim made by rendering.
    """
    root = root.resolve()
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ReportError("source checkpoint must be an explicit full lowercase commit SHA")
    try:
        kind = subprocess.run(["git", "-C", str(root), "cat-file", "-t", commit],
                              check=True, capture_output=True, text=True).stdout.strip()
        if kind != "commit":
            raise ReportError("source checkpoint must identify a commit")
        tree = subprocess.run(
            ["git", "-C", str(root), "ls-tree", "-rz", commit, "--", *SOURCE_ROOTS],
            check=True, capture_output=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError) as exc:
        raise ReportError("source checkpoint is not available in the local Git object database") from exc
    blobs = {}
    for entry in tree.split(b"\0"):
        if not entry:
            continue
        info, name = entry.split(b"\t", 1)
        mode, kind, digest = info.split()
        if kind == b"blob" and mode in {b"100644", b"100755"}:
            blobs[name.decode("utf-8")] = digest.decode()
    files = {}
    # rglob intentionally includes ignored files: no local source may silently escape capture.
    for prefix in SOURCE_ROOTS:
        directory = root / prefix
        if directory.is_symlink():
            raise ReportError(f"source pin cannot follow a symlink: {prefix}")
        for path in sorted(directory.rglob("*")):
            if path.is_symlink():
                raise ReportError(f"source pin cannot follow a symlink: {path.relative_to(root)}")
            if not path.is_file():
                continue
            relative = path.relative_to(root).as_posix()
            if not source_path(relative):
                raise ReportError(f"invalid site source path: {relative}")
            content = source_bytes(root, relative)
            blob_id = hashlib.sha1(f"blob {len(content)}\0".encode() + content).hexdigest()
            if blobs.get(relative) != blob_id:
                raise ReportError(f"source checkpoint does not match local bytes: {relative}")
            files[relative] = hashlib.sha256(content).hexdigest()
    if not files:
        raise ReportError("no website source files available to pin")
    payload = {"version": 1, "repository": REPOSITORY, "commit": commit, "files": files}
    ledger = root / LEDGER
    if ledger.is_symlink() or ledger.parent.is_symlink():
        raise ReportError("site source pin ledger must not be a symlink")
    ledger.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=ledger.parent, delete=False) as handle:
        staged = Path(handle.name)
        handle.write(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    try:
        os.replace(staged, ledger)
    finally:
        staged.unlink(missing_ok=True)
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    capture = sub.add_parser("capture", help="pin a previously published source checkpoint, offline")
    capture.add_argument("--commit", required=True, help="full SHA of the published source commit")
    capture.add_argument("--root", type=Path, default=Path("."))
    check = sub.add_parser("check", help="verify ledger content hashes without consulting Git")
    check.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args(argv)
    try:
        if args.command == "capture":
            result = capture_source_pins(args.root, args.commit)
            print(f"pinned {len(result['files'])} source files at {result['commit']} in {LEDGER}")
        else:
            result = load_source_pins(args.root, required=True)
            print(f"verified {len(result)} site source pins")
    except ReportError as exc:
        parser.exit(1, f"{exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
