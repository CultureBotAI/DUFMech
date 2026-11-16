"""Close byte-preserved review PRs for DUFMech #460 (2026-11-16).

Inputs: the committed public consolidation index and original audit ledger,
replacement branch/full SHA, and an explicit durable JSONL journal path.
Output: append-only GitHub pre/post observations; default mode is read-only.
--apply closes only frozen draft PRs and retains all original Git branches.
The caller owns authorization and the shared repository lock. No merge,
branch deletion, workflow dispatch, provider call or scientific judgement occurs.
"""
from __future__ import annotations

import argparse
import gzip
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from consolidate_review_queue_20261116 import git, load_inventory, require

REPO = "CultureBotAI/DUFMech"


def api(endpoint: str, payload: dict | None = None) -> dict:
    args = ["gh", "api", "repos/" + REPO + "/" + endpoint]
    if payload is not None:
        args += ["--method", "PATCH", "--input", "-"]
    result = subprocess.run(args, input=json.dumps(payload) if payload is not None else None,
                            text=True, capture_output=True, check=True)
    return json.loads(result.stdout)


def record(path: Path, event: str, **details: object) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps({"at": datetime.now(timezone.utc).isoformat(),
                                 "event": event, **details}, sort_keys=True) + "\n")
        handle.flush()


def identity(pr: dict) -> tuple:
    return (pr["head"]["sha"], pr["head"]["ref"], pr["head"]["repo"]["full_name"],
            pr["base"]["sha"], pr["base"]["ref"], pr["base"]["repo"]["full_name"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--replacement-branch", required=True)
    parser.add_argument("--replacement-sha", required=True)
    parser.add_argument("--journal", type=Path, required=True)
    parser.add_argument("--pr", type=int, action="append")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    require(re.fullmatch(r"[0-9a-f]{40}", args.replacement_sha) is not None,
            "replacement requires a full commit SHA")
    require(args.journal.is_absolute() and args.journal.parent.is_dir()
            and not args.journal.is_symlink(), "journal must be an explicit durable regular path")
    require(not str(args.journal.resolve()).startswith(("/tmp/", "/private/tmp/", "/private/var/folders/")),
            "system temporary journals are forbidden")
    index, digest = load_inventory(args.inventory)
    audit = json.loads(gzip.decompress(args.audit.read_bytes()))
    originals = {pr["number"]: pr for pr in audit["prs"]}
    selected = [pr for pr in index["prs"] if args.pr is None or pr["number"] in args.pr]
    require(selected and (args.pr is None or set(args.pr) == {p["number"] for p in selected}),
            "requested PR is outside the frozen consolidation")
    tree = {}
    for row in git(args.root, "ls-tree", "-rz", args.replacement_sha, "--", "reviews/structured").split(b"\0"):
        if row:
            meta, path = row.split(b"\t", 1)
            tree[path.decode()] = meta.decode().split()
    for pr in index["prs"]:
        require(pr["head"] == originals[pr["number"]]["head"], "audit and source heads differ")
        for item in pr["files"]:
            require(tree.get(item["path"]) == [item["mode"], "blob", item["blob"]],
                    "replacement does not retain " + item["path"])

    def remote_guard() -> None:
        require(api("git/ref/heads/main")["object"]["sha"] == index["base_main"],
                "published main advanced; stop and reassess")
        require(api("git/ref/heads/" + args.replacement_branch)["object"]["sha"] == args.replacement_sha,
                "published replacement head changed")

    remote_guard()
    for row in selected:
        number = row["number"]
        original = originals[number]
        before = api(f"pulls/{number}")
        expected = (row["head"], original["head_ref"], REPO, row["base"], "main", REPO)
        require(identity(before) == expected, f"PR {number} identity changed")
        require(before["state"] == "open" and before["draft"] and not before["merged"],
                f"PR {number} is no longer an open unmerged draft")
        require(before["updated_at"] == original["source_snapshot_updated_at"],
                f"PR {number} changed since the audit; rereview before closure")
        require(api("git/ref/heads/" + original["head_ref"])["object"]["sha"] == row["head"],
                f"PR {number} original branch changed or disappeared")
        record(args.journal, "preflight", number=number, head=row["head"],
               updated_at=before["updated_at"], index_sha256=digest,
               replacement=args.replacement_sha, apply=args.apply)
        if not args.apply:
            continue
        remote_guard()
        latest = api(f"pulls/{number}")
        require(identity(latest) == expected and latest["updated_at"] == before["updated_at"]
                and latest["state"] == "open" and latest["draft"],
                f"PR {number} changed immediately before closure")
        api(f"pulls/{number}", {"state": "closed"})
        after = api(f"pulls/{number}")
        if identity(after) != expected or after["merged"]:
            record(args.journal, "race_detected", number=number, actual=identity(after))
            if not after["merged"]:
                reopened = api(f"pulls/{number}", {"state": "open"})
                record(args.journal, "reopened_after_race", number=number, state=reopened["state"])
            raise RuntimeError(f"PR {number} changed during closure; stopped batch")
        require(after["state"] == "closed", f"PR {number} closure did not persist")
        require(api("git/ref/heads/" + original["head_ref"])["object"]["sha"] == row["head"],
                f"PR {number} branch retention check failed")
        record(args.journal, "closed_verified", number=number, head=row["head"],
               replacement=args.replacement_sha, merged=False, original_branch_retained=True)
        body = (f"Consolidated under #460. The exact 20-file historical review payload from `{row['head']}` "
                f"is retained byte-for-byte in [the replacement commit](https://github.com/{REPO}/commit/{args.replacement_sha}). "
                "The committed consolidation index records every source PR, Git blob and SHA256. "
                "Original branch and review evidence are retained. This closes a replaced publication request; "
                "it does not mean the reviews were merged, scientifically approved, deployed or restamped. "
                "The replacement PR will be linked from #460 after the queue has shrunk. No merge was performed.")
        result = subprocess.run(["gh", "api", "repos/" + REPO + f"/issues/{number}/comments",
                                 "--method", "POST", "--input", "-"],
                                input=json.dumps({"body": body}), text=True, capture_output=True, check=True)
        comment = json.loads(result.stdout)
        record(args.journal, "comment_verified", number=number, url=comment["html_url"])
    print(json.dumps({"mode": "apply" if args.apply else "dry_run", "prs": len(selected),
                      "replacement": args.replacement_sha, "source_index_sha256": digest}))


if __name__ == "__main__":
    main()
