"""Close byte-preserved review PRs for DUFMech #460; repairs #461/#462, 2026-11-16.

Inputs: committed public index/audit, exact replacement branch/SHA, durable journal.
Output: fsynced append-only mutation intent, response, verification and failure
receipts. Default mode observes only. --apply closes frozen draft PRs and retains
their branches. Recovery may finish a receipt-owned explanation, never reclose an
unrelated PR. No automatic reopen occurs: a successful close response cannot
prove exclusive ownership of the transition. Detected races stop the batch.
Authorization, reviewed replacement/QC and the repository lock belong to the
caller. REST does not provide an atomic compare-and-swap here; detected races and
uncertain outcomes stop. No merge, branch deletion, workflow or provider call.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import re
import stat
import subprocess
import uuid
from datetime import datetime, timezone
from pathlib import Path

from consolidate_review_queue_20261116 import git, load_inventory, no_symlinks, require

REPO = "CultureBotAI/DUFMech"


class APIError(RuntimeError):
    """Carry only a proven HTTP rejection; all other mutation failures are uncertain."""

    def __init__(self, message: str, *, rejected: bool = False):
        super().__init__(message)
        self.rejected = rejected


def api(endpoint: str, payload: dict | None = None, *, method: str | None = None):
    route = endpoint.lstrip("/") if endpoint.startswith("/") else "repos/" + REPO + "/" + endpoint
    args = ["gh", "api", route]
    if payload is not None:
        args += ["--method", method or "PATCH", "--input", "-"]
    result = subprocess.run(args, input=json.dumps(payload) if payload is not None else None,
                            text=True, capture_output=True, check=False)
    if result.returncode:
        rejected = re.search(r"\(HTTP (400|401|403|404|405|409|410|422|429)\)", result.stderr)
        raise APIError(result.stderr.strip(), rejected=bool(rejected))
    return json.loads(result.stdout)


class Journal:
    """A single operation binding; no legacy adoption, truncation or rewriting."""

    def __init__(self, path: Path, binding: dict):
        require(path.is_absolute() and path.parent.is_dir(), "journal needs a durable absolute path")
        no_symlinks(path)
        require(not str(path).startswith(("/tmp/", "/private/tmp/", "/private/var/folders/")),
                "system temporary journals are forbidden")
        if path.exists():
            require(stat.S_ISREG(path.stat().st_mode), "journal must be a regular file")
        self.path = path
        self.events: list[dict] = []
        if path.exists():
            raw = path.read_bytes()
            require(raw.endswith(b"\n"), "incomplete journal; reconcile its uncertain outcome")
            self.events = [json.loads(line) for line in raw.splitlines()]
            require(self.events and self.events[0].get("event") == "binding"
                    and self.events[0].get("binding") == binding,
                    "journal binding differs; do not reuse another operation's receipts")
        else:
            self.add("binding", binding=binding)
        self.binding = binding

    def add(self, event: str, **details) -> dict:
        entry = {"at": datetime.now(timezone.utc).isoformat(), "event": event, **details}
        no_symlinks(self.path)
        fd = os.open(self.path, os.O_WRONLY | os.O_APPEND | os.O_CREAT | os.O_NOFOLLOW, 0o600)
        try:
            require(stat.S_ISREG(os.fstat(fd).st_mode), "journal must be a regular file")
            raw = (json.dumps(entry, sort_keys=True) + "\n").encode()
            with os.fdopen(fd, "ab", closefd=False) as handle:
                handle.write(raw)
                handle.flush()
                os.fsync(handle.fileno())  # intent is durable before its mutation is attempted
            directory = os.open(self.path.parent, os.O_RDONLY)
            try:
                os.fsync(directory)
            finally:
                os.close(directory)
        finally:
            os.close(fd)
        self.events.append(entry)
        return entry

    def for_pr(self, number: int) -> list[dict]:
        return [entry for entry in self.events if entry.get("number") == number]


def identity(pr: dict) -> list:
    return [pr["head"]["sha"], pr["head"]["ref"], pr["head"]["repo"]["full_name"],
            pr["base"]["sha"], pr["base"]["ref"], pr["base"]["repo"]["full_name"]]


def owner_metadata(pr: dict) -> dict:
    """Freeze owner-sensitive fields; omit only server lifecycle/mergeability fields."""
    fields = ("draft", "title", "body", "comments", "review_comments", "maintainer_can_modify",
              "locked", "active_lock_reason", "milestone")
    result = {key: pr.get(key) for key in fields}
    for key in ("labels", "assignees", "requested_reviewers", "requested_teams"):
        result[key] = sorted(
            [{k: value[k] for k in ("id", "name", "login", "slug") if k in value}
             for value in pr.get(key, [])], key=lambda value: json.dumps(value, sort_keys=True))
    return result


def same_owner_metadata(before: dict, after: dict, *, own_comments: int = 0) -> bool:
    expected = owner_metadata(before)
    if own_comments:
        require(type(expected["comments"]) is int, "missing original comment counter")
        expected["comments"] += own_comments
    return owner_metadata(after) == expected


def same_closure(left: dict, right: dict) -> bool:
    return (left.get("number") == right.get("number") and identity(left) == identity(right)
            and left["state"] == right["state"] == "closed"
            and not left["merged"] and not right["merged"]
            and isinstance(left.get("closed_at"), str) and bool(left["closed_at"])
            and left["closed_at"] == right.get("closed_at"))


def comment_body(row: dict, replacement: str, index_digest: str) -> str:
    marker = hashlib.sha256(f"{row['number']}:{row['head']}:{replacement}:{index_digest}".encode())
    return (f"<!-- dufmech-review-consolidation-v1:{marker.hexdigest()} -->\n"
            f"Consolidated under #460. The exact 20-file historical review payload from `{row['head']}` "
            f"is retained byte-for-byte in [the replacement commit](https://github.com/{REPO}/commit/{replacement}). "
            "The committed consolidation index records every source PR, Git blob and SHA256. "
            "Original branch and review evidence are retained. This closes a replaced publication request; "
            "it does not mean the reviews were merged, scientifically approved, deployed or restamped. "
            "The replacement PR will be linked from #460 after the queue has shrunk. No merge was performed.")


def matching_comment(number: int, body: str, actor: int) -> dict | None:
    marker = body.splitlines()[0]
    found = []
    for page in range(1, 101):
        comments = api(f"issues/{number}/comments?per_page=100&page={page}")
        require(isinstance(comments, list), "invalid comment inventory")
        found.extend(comment for comment in comments if marker in comment.get("body", ""))
        if len(comments) < 100:
            break
    else:
        raise RuntimeError("comment inventory limit reached; do not assume absence")
    require(len(found) <= 1, "duplicate explanation markers require reconciliation")
    if found:
        require(found[0].get("body") == body and found[0].get("user", {}).get("id") == actor,
                "explanation marker is not owned by this operation's authenticated actor")
        return found[0]
    return None


def mutation(journal: Journal, number: int, kind: str, endpoint: str,
             payload: dict, *, method: str = "PATCH", **context) -> dict:
    operation = uuid.uuid4().hex
    journal.add(kind + "_intent", number=number, operation=operation, payload=payload, **context)
    try:
        response = api(endpoint, payload, method=method)
    except Exception as exc:
        journal.add(kind + "_failure", number=number, operation=operation,
                    outcome="rejected" if isinstance(exc, APIError) and exc.rejected else "unknown",
                    error=str(exc))
        raise
    journal.add(kind + "_response", number=number, operation=operation, response=response)
    return response


def finish_comment(journal: Journal, number: int, body: str, actor: int,
                   existing: dict | None, *, apply: bool) -> None:
    events = journal.for_pr(number)
    intents = [entry for entry in events if entry["event"] == "comment_intent"]
    verified = [entry for entry in events if entry["event"] == "comment_verified"]
    if existing:
        require(bool(intents), "matching comment has no owned intent; reconcile before claiming it")
        if verified:
            require(existing["id"] == verified[-1]["comment_id"], "verified comment identity changed")
        response = api(f"issues/comments/{existing['id']}")
        require(response.get("body") == body and response.get("user", {}).get("id") == actor,
                "explanation readback differs")
        if apply and not verified:
            journal.add("comment_verified", number=number, comment_id=response["id"],
                        url=response["html_url"], recovered=True)
        return
    require(not verified, "previously verified comment disappeared; do not silently recreate it")
    if intents:
        last = intents[-1]["operation"]
        replies = [event for event in events if event.get("operation") == last
                   and event["event"] in {"comment_response", "comment_failure"}]
        require(replies and replies[-1]["event"] == "comment_failure"
                and replies[-1].get("outcome") == "rejected",
                "comment outcome is uncertain or receipt-owned comment disappeared; stop")
    if not apply:
        return
    comment = mutation(journal, number, "comment", f"issues/{number}/comments", {"body": body},
                       method="POST", body_sha256=hashlib.sha256(body.encode()).hexdigest())
    require(comment.get("body") == body and comment.get("user", {}).get("id") == actor,
            "comment response does not establish ownership")
    readback = api(f"issues/comments/{comment['id']}")
    require(readback.get("body") == body and readback.get("user", {}).get("id") == actor,
            "comment readback differs")
    journal.add("comment_verified", number=number, comment_id=comment["id"],
                url=readback["html_url"], recovered=False)


def process_pr(row: dict, original: dict, journal: Journal, remote_guard, *, apply: bool) -> None:
    number = row["number"]
    expected = [row["head"], original["head_ref"], REPO, row["base"], "main", REPO]
    actor = journal.binding["actor_id"]
    body = comment_body(row, journal.binding["replacement"], journal.binding["index_sha256"])

    def branch_guard():
        require(api("git/ref/heads/" + original["head_ref"])["object"]["sha"] == row["head"],
                f"PR {number} original branch changed or disappeared")

    events = journal.for_pr(number)
    require(not any(event["event"] in {"race_detected", "reopen_intent"} for event in events),
            f"PR {number} has a prior race; coordinator reconciliation is required")
    intents = [event for event in events if event["event"] == "close_intent"]
    receipts = [event for event in events if event["event"] == "close_response"]
    if intents:
        intent = intents[-1]
        require(receipts and receipts[-1]["operation"] == intent["operation"],
                f"PR {number} close outcome is uncertain; no automatic repeat")
        receipt = receipts[-1]["response"]
        before = intent["before"]
        current = api(f"pulls/{number}")
        require(identity(current) == expected and same_closure(receipt, current),
                f"PR {number} is not this journal's still-current closed unmerged PR")
        remote_guard()
        branch_guard()
        existing = matching_comment(number, body, actor)
        if not same_owner_metadata(before, current, own_comments=int(existing is not None)):
            journal.add("recovery_failure", number=number, observation=current,
                        error="owner metadata changed during recovery")
            raise RuntimeError(f"PR {number} owner metadata changed during recovery; stopped")
        if apply and not any(event["event"] == "closed_verified" for event in events):
            journal.add("closed_verified", number=number, observation=current,
                        close_operation=intent["operation"], recovered=True,
                        original_branch_retained=True)
        finish_comment(journal, number, body, actor, existing, apply=apply)
        return

    before = api(f"pulls/{number}")
    require(identity(before) == expected, f"PR {number} identity changed")
    require(before["state"] == "open" and before["draft"] and not before["merged"],
            f"PR {number} is no longer an open unmerged draft")
    require(before["updated_at"] == original["source_snapshot_updated_at"],
            f"PR {number} changed since the audit; rereview before closure")
    branch_guard()
    journal.add("preflight", number=number, observation=before, apply=apply)
    if not apply:
        return
    remote_guard()
    latest = api(f"pulls/{number}")
    require(identity(latest) == expected and latest["updated_at"] == before["updated_at"]
            and latest["state"] == "open" and not latest["merged"]
            and same_owner_metadata(before, latest), f"PR {number} changed immediately before closure")
    response = mutation(journal, number, "close", f"pulls/{number}", {"state": "closed"},
                        before=latest)
    try:
        after = api(f"pulls/{number}")
        require(response["state"] == "closed" and same_closure(response, after),
                f"PR {number} close response/readback mismatch")
        if (identity(after) != expected or not same_owner_metadata(before, response)
                or not same_owner_metadata(before, after)):
            journal.add("race_detected", number=number, before=before, response=response, after=after)
            raise RuntimeError(f"PR {number} changed during closure; no automatic reopen; stopped")
        branch_guard()
        journal.add("closed_verified", number=number, observation=after,
                    original_branch_retained=True)
        existing = matching_comment(number, body, actor)
        finish_comment(journal, number, body, actor, existing, apply=True)
    except Exception as exc:
        journal.add("post_close_failure", number=number, error=str(exc),
                    outcome="known_close_response_retained")
        raise


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--replacement-branch", required=True)
    parser.add_argument("--replacement-sha", required=True)
    parser.add_argument("--journal", type=Path, required=True)
    parser.add_argument("--pr", type=int, action="append")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)
    require(re.fullmatch(r"[0-9a-f]{40}", args.replacement_sha) is not None,
            "replacement requires a full commit SHA")
    index, digest = load_inventory(args.inventory)
    audit_bytes = args.audit.read_bytes()
    audit = json.loads(gzip.decompress(audit_bytes))
    originals = {pr["number"]: pr for pr in audit["prs"]}
    selected = [pr for pr in index["prs"] if args.pr is None or pr["number"] in args.pr]
    require(selected and (args.pr is None or set(args.pr) == {p["number"] for p in selected}),
            "requested PR is outside the frozen consolidation")
    root = args.root.resolve(strict=True)
    for path, raw in ((args.inventory, args.inventory.read_bytes()), (args.audit, audit_bytes)):
        relative = path.resolve(strict=True).relative_to(root).as_posix()
        require(git(root, "show", args.replacement_sha + ":" + relative) == raw,
                "input is not byte-identical to the replacement's committed " + relative)
    tree = {}
    for row in git(root, "ls-tree", "-rz", args.replacement_sha, "--",
                   "reviews/structured").split(b"\0"):
        if row:
            meta, path = row.split(b"\t", 1)
            tree[path.decode()] = meta.decode().split()
    for pr in index["prs"]:
        require(pr["head"] == originals[pr["number"]]["head"], "audit and source heads differ")
        for item in pr["files"]:
            require(tree.get(item["path"]) == [item["mode"], "blob", item["blob"]],
                    "replacement does not retain " + item["path"])

    def remote_guard():
        require(api("git/ref/heads/main")["object"]["sha"] == index["base_main"],
                "published main advanced; stop and reassess")
        require(api("git/ref/heads/" + args.replacement_branch)["object"]["sha"] == args.replacement_sha,
                "published replacement head changed")

    actor = api("/user")["id"]
    require(type(actor) is int and actor > 0, "authenticated actor ID unavailable")
    binding = {"version": 1, "repository": REPO, "index_sha256": digest,
               "audit_sha256": hashlib.sha256(audit_bytes).hexdigest(),
               "replacement": args.replacement_sha, "replacement_branch": args.replacement_branch,
               "base_main": index["base_main"], "actor_id": actor}
    journal = Journal(args.journal, binding)
    remote_guard()
    for row in selected:
        process_pr(row, originals[row["number"]], journal, remote_guard, apply=args.apply)
    print(json.dumps({"mode": "apply" if args.apply else "dry_run", "prs": len(selected),
                      "replacement": args.replacement_sha, "source_index_sha256": digest}))


if __name__ == "__main__":
    main()
