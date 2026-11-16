"""Copy original review blobs for DUFMech issues #459/#460, 2026-11-16.

Purpose: consolidate 95 review PRs without parsing/restamping their 1,900 files.
Input: public docs/provenance/review-queue-20261116.json and exact Git objects.
Output: only the indexed reviews/structured pairs and a JSON stdout receipt.
Default is a read-only dry run; --verify requires every output to exist.
The caller owns authorization, RepositorySettings validation and the repository
LockManager lease. No fetch, tag, commit, merge or provider call occurs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

REPOSITORY = "CultureBotAI/DUFMech"
PR_COUNT = 95
FILES_PER_PR = 20
FILE_COUNT = PR_COUNT * FILES_PER_PR
HEX40 = re.compile(r"[0-9a-f]{40}\Z")
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
REVIEW_PATH = re.compile(r"reviews/structured/[A-Za-z0-9][A-Za-z0-9._-]*/review\.(yaml|md)\Z")


class ConsolidationError(ValueError):
    """An input or destination cannot safely participate in consolidation."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ConsolidationError(message)


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def no_symlinks(path: Path) -> None:
    for component in (path, *path.parents):
        require(not component.is_symlink(), f"symlink path refused: {component}")


def git(root: Path, *args: str, input_bytes: bytes | None = None) -> bytes:
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    result = subprocess.run(
        ["git", "--no-replace-objects", "-C", str(root), *args], input=input_bytes,
        capture_output=True, check=False, env=env,
    )
    require(result.returncode == 0, f"git {args[0]} failed: {result.stderr.decode().strip()}")
    return result.stdout


def load_inventory(path: Path) -> tuple[dict, str]:
    no_symlinks(path)
    raw = path.read_bytes()
    payload = json.loads(raw, object_pairs_hook=unique_object)
    expected = {"schema_version", "repository", "date", "issues", "base_main",
                "expected_pr_count", "expected_file_count", "prs"}
    require(isinstance(payload, dict) and set(payload) == expected, "invalid inventory keys")
    require(type(payload["schema_version"]) is int and payload["schema_version"] == 1,
            "unsupported inventory version")
    require(payload["repository"] == REPOSITORY and payload["date"] == "2026-11-16",
            "wrong repository or inventory date")
    require(payload["issues"] == [459, 460], "wrong issue scope")
    require(type(payload["expected_pr_count"]) is int
            and payload["expected_pr_count"] == PR_COUNT
            and type(payload["expected_file_count"]) is int
            and payload["expected_file_count"] == FILE_COUNT, "unexpected inventory counts")
    require(isinstance(payload["base_main"], str)
            and bool(HEX40.fullmatch(payload["base_main"])), "invalid main base")
    require(isinstance(payload["prs"], list) and len(payload["prs"]) == PR_COUNT,
            "incorrect PR count")
    numbers, paths = set(), set()
    for pr in payload["prs"]:
        require(isinstance(pr, dict) and set(pr) == {"number", "head", "base", "merge_base",
                                                    "files"}, "invalid PR keys")
        number = pr["number"]
        require(type(number) is int and number > 0 and number not in numbers,
                "invalid or duplicate PR number")
        numbers.add(number)
        for field in ("head", "base", "merge_base"):
            require(isinstance(pr[field], str) and bool(HEX40.fullmatch(pr[field])),
                    f"invalid {field} for PR {number}")
        require(isinstance(pr["files"], list) and len(pr["files"]) == FILES_PER_PR,
                f"incorrect file count for PR {number}")
        pairs: dict[str, set[str]] = {}
        for item in pr["files"]:
            require(isinstance(item, dict) and set(item) == {
                "path", "status", "mode", "blob", "sha256", "size"}, "invalid file keys")
            name = item["path"]
            require(isinstance(name, str) and bool(REVIEW_PATH.fullmatch(name))
                    and name not in paths, "unsafe or duplicate review path")
            paths.add(name)
            require(item["status"] == "A" and item["mode"] == "100644",
                    f"only added regular review files are allowed: {name}")
            require(isinstance(item["blob"], str) and bool(HEX40.fullmatch(item["blob"]))
                    and isinstance(item["sha256"], str)
                    and bool(HEX64.fullmatch(item["sha256"])), f"invalid hashes: {name}")
            require(type(item["size"]) is int and item["size"] > 0, f"invalid byte count: {name}")
            parent, leaf = name.rsplit("/", 1)
            pairs.setdefault(parent, set()).add(leaf)
        require(all(leaves == {"review.yaml", "review.md"} for leaves in pairs.values()),
                f"missing YAML/Markdown partner in PR {number}")
    require(len(paths) == FILE_COUNT, "incorrect unique file count")
    return payload, hashlib.sha256(raw).hexdigest()


def source_blobs(root: Path, payload: dict) -> dict[str, bytes]:
    """Prove each complete PR delta and blob before looking at any destination."""
    origin = git(root, "remote", "get-url", "origin").decode().strip().removesuffix(".git")
    require(origin in {f"https://github.com/{REPOSITORY}", f"git@github.com:{REPOSITORY}"},
            "unexpected origin identity")
    require(Path(git(root, "rev-parse", "--show-toplevel").decode().strip()) == root,
            "root is not the repository top level")
    git(root, "merge-base", "--is-ancestor", payload["base_main"], "HEAD")
    files = {}
    for pr in payload["prs"]:
        base = git(root, "merge-base", pr["base"], pr["head"]).decode().strip()
        require(base == pr["merge_base"], f"changed merge base for PR {pr['number']}")
        delta = git(root, "diff-tree", "-r", "--no-commit-id", "--raw", "-z",
                    "--no-abbrev", "--no-renames", "--no-ext-diff", base, pr["head"], "--")
        fields = delta.split(b"\0")
        require(fields[-1] == b"" and len(fields) % 2 == 1, "invalid Git delta encoding")
        actual = {}
        for index in range(0, len(fields) - 1, 2):
            old_mode, mode, old_blob, blob, status = fields[index].decode().split()
            name = fields[index + 1].decode()
            require(old_mode == ":000000" and old_blob == "0" * 40 and status == "A",
                    f"PR {pr['number']} includes a non-addition: {name}")
            actual[name] = (mode, blob, status)
        expected = {item["path"]: (item["mode"], item["blob"], item["status"])
                    for item in pr["files"]}
        require(actual == expected, f"PR {pr['number']} delta differs from inventory")
        files.update({item["path"]: item for item in pr["files"]})
    ids = sorted({item["blob"] for item in files.values()})
    stream = git(root, "cat-file", "--batch", input_bytes=("\n".join(ids) + "\n").encode())
    offset, blobs = 0, {}
    for oid in ids:
        end = stream.index(b"\n", offset)
        header = stream[offset:end].decode().split()
        require(len(header) == 3 and header[0] == oid and header[1] == "blob",
                f"unavailable source blob: {oid}")
        size = int(header[2])
        raw = stream[end + 1:end + 1 + size]
        require(len(raw) == size and stream[end + 1 + size:end + 2 + size] == b"\n",
                f"incomplete source blob: {oid}")
        require(hashlib.sha1(f"blob {size}\0".encode() + raw).hexdigest() == oid,
                f"Git blob digest mismatch: {oid}")
        blobs[oid] = raw
        offset = end + 2 + size
    require(offset == len(stream), "unexpected trailing Git output")
    output = {}
    for name, item in files.items():
        raw = blobs[item["blob"]]
        require(len(raw) == item["size"] and hashlib.sha256(raw).hexdigest() == item["sha256"],
                f"source byte proof differs: {name}")
        output[name] = raw
    return output


def inspect_destinations(root: Path, output: dict[str, bytes]) -> list[str]:
    missing = []
    for name, raw in output.items():
        path = root / name
        no_symlinks(path)
        for parent in path.parents:
            if parent == root:
                break
            require(not parent.exists() or parent.is_dir(), f"non-directory parent: {name}")
        if not path.exists():
            missing.append(name)
            continue
        mode = path.stat().st_mode
        require(stat.S_ISREG(mode) and not mode & 0o111,
                f"destination is not a regular nonexecutable file: {name}")
        require(path.read_bytes() == raw, f"existing destination bytes differ: {name}")
    return missing


def publish(root: Path, output: dict[str, bytes], missing: list[str]) -> None:
    """Stage all bytes, then exclusively create files; roll back only owned inodes."""
    scratch = root / ".temp"
    no_symlinks(scratch)
    git(root, "check-ignore", "-q", ".temp/")
    scratch.mkdir(exist_ok=True)
    created: list[tuple[Path, int]] = []
    with tempfile.TemporaryDirectory(prefix="review-queue-stage-", dir=scratch) as temporary:
        stage = Path(temporary)
        for index, name in enumerate(missing):
            path = stage / str(index)
            path.write_bytes(output[name])
            path.chmod(0o644)
            require(path.read_bytes() == output[name], f"staged bytes differ: {name}")
        require(inspect_destinations(root, output) == missing, "destinations changed after preflight")
        try:
            for index, name in enumerate(missing):
                path = root / name
                no_symlinks(path)
                path.parent.mkdir(parents=True, exist_ok=True)
                no_symlinks(path)
                os.link(stage / str(index), path)  # exclusive creation, never overwrite
                created.append((path, path.stat().st_ino))
            require(not inspect_destinations(root, output), "post-write verification incomplete")
        except (OSError, ConsolidationError):
            for path, inode in reversed(created):
                if (path.is_file() and not path.is_symlink() and path.stat().st_ino == inode
                        and path.read_bytes() == output[path.relative_to(root).as_posix()]):
                    path.unlink()
            raise


def consolidate(root: Path, inventory: Path, *, apply: bool = False, verify: bool = False) -> dict:
    require(root.is_absolute() and root.is_dir(), "--root must be an existing absolute directory")
    no_symlinks(root)
    require(not (apply and verify), "--apply and --verify are mutually exclusive")
    payload, index_digest = load_inventory(inventory)
    output = source_blobs(root, payload)
    missing = inspect_destinations(root, output)
    if verify:
        require(not missing, f"verification failed: {len(missing)} indexed files are missing")
    if apply and missing:
        publish(root, output, missing)
    return {"mode": "verify" if verify else "apply" if apply else "dry_run",
            "repository": REPOSITORY, "source_index_sha256": index_digest,
            "pull_requests": len(payload["prs"]), "files": len(output),
            "bytes": sum(map(len, output.values())), "already_present": len(output) - len(missing),
            "missing_before": len(missing), "created": len(missing) if apply else 0}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--inventory", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--verify", action="store_true")
    args = parser.parse_args(argv)
    try:
        result = consolidate(args.root, args.inventory, apply=args.apply, verify=args.verify)
    except (ConsolidationError, OSError, ValueError, TypeError, KeyError) as exc:
        print(f"review consolidation refused: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
