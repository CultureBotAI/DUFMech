#!/usr/bin/env python3
"""Read-only Git-tree archive accounting, retained for DUFMech #463 (2026-11-16).

Inputs: repository, exact base/head commits, site prefix, optional preserved-source
index (a files list or prs[].files), and optional repository-relative budget JSON.
Output: complete changed-file accounting JSON, optionally fixed-mtime gzip.
No fetch, provider call, Git mutation, source rewriting or guard change occurs.
"""
from __future__ import annotations

import argparse
import collections
import datetime
import gzip
import hashlib
import json
import os
import subprocess
from pathlib import Path


def git(root: Path, *args: str, data: bytes | None = None) -> bytes:
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    return subprocess.check_output(
        ["git", "--no-replace-objects", "-C", str(root), *args], input=data, env=env,
    )


def tree(root: Path, revision: str) -> dict[str, dict]:
    result = {}
    for raw in git(root, "ls-tree", "-r", "-l", "-z", revision).split(b"\0"):
        if not raw:
            continue
        metadata, path = raw.split(b"\t", 1)
        mode, kind, oid, size = metadata.decode().split()
        result[path.decode()] = {"mode": mode, "oid": oid,
                                 "size": int(size) if kind == "blob" else None}
    return result


def account(base: dict[str, dict], head: dict[str, dict], prefix: str,
            preserved: set[str]) -> dict:
    before = {name: item for name, item in base.items() if name.startswith(prefix)}
    after = {name: item for name, item in head.items() if name.startswith(prefix)}
    if any(item["size"] is None for item in [*before.values(), *after.values()]):
        raise ValueError("site tree contains a non-blob Git entry")
    changed = []
    groups: dict[str, dict] = {}
    for name in sorted(set(before) | set(after)):
        old, new = before.get(name), after.get(name)
        if old == new:
            continue
        status = "added" if old is None else "deleted" if new is None else "modified"
        old_size, new_size = old["size"] if old else 0, new["size"] if new else 0
        relative = name.removeprefix(prefix)
        parent = relative.split("/", 1)[0] if "/" in relative else "root"
        group = "preserved_source_downloads" if name in preserved else parent + Path(name).suffix
        row = {"path": name, "status": status, "base": old, "head": new,
               "delta_bytes": new_size - old_size, "group": group}
        changed.append(row)
        item = groups.setdefault(group, {"added": 0, "deleted": 0, "modified": 0,
                                        "base_bytes": 0, "head_bytes": 0, "delta_bytes": 0})
        item[status] += 1
        item["base_bytes"] += old_size
        item["head_bytes"] += new_size
        item["delta_bytes"] += new_size - old_size
    base_bytes, head_bytes = sum(x["size"] for x in before.values()), sum(x["size"] for x in after.values())
    counts = collections.Counter(row["status"] for row in changed)
    assert sum(row["delta_bytes"] for row in changed) == head_bytes - base_bytes
    assert counts["added"] - counts["deleted"] == len(after) - len(before)
    return {"base": {"files": len(before), "bytes": base_bytes},
            "head": {"files": len(after), "bytes": head_bytes},
            "delta": {"files": len(after) - len(before), "bytes": head_bytes - base_bytes},
            "changed_counts": {key: counts[key] for key in ("added", "modified", "deleted")},
            "unchanged_files": len(set(before) & set(after)) - counts["modified"],
            "unchanged_bytes": sum(before[name]["size"] for name in before if before[name] == after.get(name)),
            "groups": groups, "changed_files": changed}


def preserved_sources(root: Path, head: dict[str, dict], prefix: str, index: Path) -> dict:
    raw_index = index.read_bytes()
    payload = json.loads(raw_index)
    entries = payload["files"] if "files" in payload else [item for pr in payload["prs"] for item in pr["files"]]
    assert len({entry["path"] for entry in entries}) == len(entries), "duplicate preserved path"
    ids = sorted({entry["blob"] for entry in entries})
    stream = git(root, "cat-file", "--batch", data=("\n".join(ids) + "\n").encode())
    offset, hashes = 0, {}
    for oid in ids:
        end = stream.index(b"\n", offset)
        actual, kind, length = stream[offset:end].decode().split()
        assert actual == oid and kind == "blob", "missing source blob"
        size = int(length)
        raw = stream[end + 1:end + 1 + size]
        assert len(raw) == size and stream[end + 1 + size:end + 2 + size] == b"\n"
        hashes[oid] = {"sha256": hashlib.sha256(raw).hexdigest(), "size": size}
        offset = end + 2 + size
    assert offset == len(stream)
    proofs = []
    for entry in entries:
        destination = prefix + "source/" + entry["path"]
        expected = {"mode": entry["mode"], "oid": entry["blob"], "size": entry["size"]}
        assert head.get(entry["path"]) == expected, "original source differs: " + entry["path"]
        assert head.get(destination) == expected, "published source differs: " + destination
        assert hashes[entry["blob"]] == {"sha256": entry["sha256"], "size": entry["size"]}
        proofs.append({"source": entry["path"], "destination": destination,
                       "blob": entry["blob"], "sha256": entry["sha256"], "size": entry["size"]})
    return {"source_index_sha256": hashlib.sha256(raw_index).hexdigest(), "files": len(proofs),
            "bytes": sum(item["size"] for item in proofs), "proofs": proofs}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    parser.add_argument("--site-prefix", default="pages/")
    parser.add_argument("--preserved-source-index", type=Path)
    parser.add_argument("--budgets-relative")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assert args.site_prefix and not args.site_prefix.startswith("/") and args.site_prefix.endswith("/")
    assert ".." not in Path(args.site_prefix).parts
    base = git(args.repo, "rev-parse", args.base + "^{commit}").decode().strip()
    head = git(args.repo, "rev-parse", args.head + "^{commit}").decode().strip()
    base_tree, head_tree = tree(args.repo, base), tree(args.repo, head)
    preserved = (preserved_sources(args.repo, head_tree, args.site_prefix, args.preserved_source_index)
                 if args.preserved_source_index else {"files": 0, "bytes": 0, "proofs": []})
    accounting = account(base_tree, head_tree, args.site_prefix,
                         {item["destination"] for item in preserved["proofs"]})
    report = {"version": 1, "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "base_commit": base, "head_commit": head, "site_prefix": args.site_prefix,
              "helper_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "repository_origin": git(args.repo, "remote", "get-url", "origin").decode().strip(),
              "accounting": accounting, "preserved_sources": preserved}
    if args.budgets_relative:
        report["base_budgets"] = json.loads(git(args.repo, "show", base + ":" + args.budgets_relative))
        report["head_budgets"] = json.loads(git(args.repo, "show", head + ":" + args.budgets_relative))
    raw = (json.dumps(report, indent=2, sort_keys=True) + "\n").encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(gzip.compress(raw, mtime=0) if args.output.suffix == ".gz" else raw)
    print(json.dumps({key: accounting[key] for key in ["base", "head", "delta", "changed_counts", "unchanged_files", "groups"]}, indent=2))


if __name__ == "__main__":
    main()
