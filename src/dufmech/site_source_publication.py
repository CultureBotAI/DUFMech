"""Explicit online gate for canonical retention of the website source checkpoint."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import tempfile
from pathlib import Path

from dufmech.report import ReportError
from dufmech.site_sources import REPOSITORY, SOURCE_ROOTS, load_source_pins, source_bytes

PUBLICATION_URL = REPOSITORY + ".git"
RETAINED_TAGS = "refs/tags/source/dufmech-*"


def _git(root: Path, *args: str, allowed: tuple[int, ...] = (0,)) -> subprocess.CompletedProcess:
    # Never let checkout refs, replacement objects, templates, or URL rewrites supply proof.
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
               GIT_TERMINAL_PROMPT="0", GIT_NO_REPLACE_OBJECTS="1")
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "-c", f"core.hooksPath={os.devnull}", *args],
            env=env, capture_output=True, timeout=180, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ReportError(f"cannot verify published site sources: git {args[0]} failed") from exc
    if result.returncode not in allowed:
        raise ReportError(f"cannot verify published site sources: git {args[0]} failed "
                          f"(exit {result.returncode}); check canonical repository access")
    return result


def check_published_source_pins(root: Path) -> dict:
    """Check fresh canonical refs and pinned blobs, without changing the checkout.

    An annotated source tag must point directly to the checkpoint. This observes
    current retention, not a promise that a maintainer can never delete the tag.
    """
    root = root.resolve()
    pins = load_source_pins(root, required=True)
    commit = next(iter(pins.values()))["commit"]
    with tempfile.TemporaryDirectory(prefix="dufmech-source-publication-") as directory:
        remote = Path(directory)
        _git(remote, "init", "--bare", "--template=")
        _git(remote, "fetch", "--filter=blob:none", "--no-tags", "--no-recurse-submodules",
             "--no-write-fetch-head", PUBLICATION_URL,
             "+refs/heads/main:refs/heads/main", f"+{RETAINED_TAGS}:{RETAINED_TAGS}")
        retained_by = None
        kind = _git(remote, "cat-file", "-t", commit, allowed=(0, 128))
        if kind.returncode == 0 and kind.stdout.strip() == b"commit":
            ancestor = _git(remote, "merge-base", "--is-ancestor", commit, "refs/heads/main",
                            allowed=(0, 1))
            if ancestor.returncode == 0:
                retained_by = "refs/heads/main"
            else:
                tags = _git(remote, "for-each-ref",
                            "--format=%(refname) %(objecttype) %(*objecttype) %(*objectname)",
                            RETAINED_TAGS).stdout.decode().splitlines()
                for tag in tags:
                    parts = tag.split()
                    if len(parts) == 4 and parts[1:] == ["tag", "commit", commit]:
                        retained_by = parts[0]
                        break
        if retained_by is None:
            raise ReportError(
                f"site source checkpoint {commit} is not retained on canonical main or by a "
                "published annotated source/dufmech-* tag pointing directly to it; "
                "publish and retain the checkpoint before merging"
            )

        tree = _git(remote, "ls-tree", "-rz", commit, "--", *SOURCE_ROOTS).stdout
        blobs = {}
        for entry in tree.split(b"\0"):
            if entry:
                info, name = entry.split(b"\t", 1)
                mode, kind, digest = info.split()
                if kind == b"blob" and mode in {b"100644", b"100755"}:
                    blobs[name.decode("utf-8")] = digest.decode("ascii")
        for relative, pin in pins.items():
            content = source_bytes(root, relative)
            blob_id = hashlib.sha1(f"blob {len(content)}\0".encode() + content).hexdigest()
            if (hashlib.sha256(content).hexdigest() != pin["sha256"]
                    or blobs.get(relative) != blob_id):
                raise ReportError(f"published source checkpoint bytes differ: {relative}")
    return {"repository": REPOSITORY, "commit": commit, "retained_by": retained_by,
            "files": len(pins)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args(argv)
    try:
        result = check_published_source_pins(args.root)
    except ReportError as exc:
        parser.exit(1, f"{exc}\n")
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
