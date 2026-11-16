"""Offline adversarial regressions for DUFMech closure issues #461/#462."""
from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).parents[1] / "scripts/adhoc"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("close_review_queue", SCRIPTS /
                                              "close_consolidated_reviews_20261116.py")
assert spec and spec.loader
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class FakeGitHub:
    def __init__(self, journal):
        self.journal = journal
        self.pr = {"number": 289, "head": {"sha": "a" * 40, "ref": "review/batch-001",
                   "repo": {"full_name": m.REPO}},
                   "base": {"sha": "b" * 40, "ref": "main", "repo": {"full_name": m.REPO}},
                   "state": "open", "draft": True, "merged": False, "closed_at": None,
                   "updated_at": "2026-11-16T01:00:00Z", "title": "Original title",
                   "body": "Original instructions", "comments": 0, "review_comments": 0,
                   "labels": [], "assignees": [], "requested_reviewers": [], "requested_teams": [],
                   "milestone": None, "maintainer_can_modify": True, "locked": False,
                   "active_lock_reason": None}
        self.calls = []
        self.comments = []
        self.on_close = {}
        self.fail_post_read = False
        self.comment_failure = None
        self.create_before_failure = False
        self.race_fresh_change = None
        self.other_owner_closes_before_patch = False
        self.after_close_reads = 0
        self.trace = []

    def __call__(self, endpoint, payload=None, *, method=None):
        self.calls.append((endpoint, copy.deepcopy(payload), method))
        if payload is not None:
            kind = "comment" if method == "POST" else payload["state"]
            self.trace.append("mutation:" + kind)
            events = [json.loads(line) for line in self.journal.path.read_text().splitlines()]
            intent = "comment_intent" if method == "POST" else (
                "close_intent" if payload["state"] == "closed" else "reopen_intent")
            assert events[-1]["event"] == intent, "mutation preceded its durable intent"
        if endpoint == "git/ref/heads/review/batch-001":
            return {"object": {"sha": "a" * 40}}
        if endpoint == "pulls/289":
            if payload:
                if payload["state"] == "closed" and self.other_owner_closes_before_patch:
                    self.pr.update(state="closed", closed_at="2026-11-16T01:59:59Z",
                                   updated_at="2026-11-16T01:59:59Z",
                                   body="Another owner closed this independently")
                    return copy.deepcopy(self.pr)  # successful no-op PATCH
                self.pr["state"] = payload["state"]
                self.pr["updated_at"] = "2026-11-16T02:00:00Z"
                self.pr["closed_at"] = ("2026-11-16T02:00:00Z"
                                        if payload["state"] == "closed" else None)
                if payload["state"] == "closed":
                    self.pr.update(copy.deepcopy(self.on_close))
                return copy.deepcopy(self.pr)
            if self.pr["state"] == "closed":
                self.after_close_reads += 1
                if self.fail_post_read:
                    self.fail_post_read = False
                    raise RuntimeError("readback network failure")
                if self.race_fresh_change and self.after_close_reads == 2:
                    self.pr.update(copy.deepcopy(self.race_fresh_change))
            return copy.deepcopy(self.pr)
        if endpoint.startswith("issues/289/comments?"):
            return copy.deepcopy(self.comments)
        if endpoint.startswith("issues/comments/"):
            number = int(endpoint.rsplit("/", 1)[1])
            return copy.deepcopy(next(x for x in self.comments if x["id"] == number))
        if endpoint == "issues/289/comments" and method == "POST":
            comment = {"id": 100 + len(self.comments), "body": payload["body"], "user": {"id": 77},
                       "html_url": "https://github.com/CultureBotAI/DUFMech/pull/289#issuecomment-100"}
            failure = self.comment_failure
            if failure is None or self.create_before_failure:
                self.comments.append(comment)
                self.pr["comments"] += 1
                self.pr["updated_at"] = "2026-11-16T03:00:00Z"
            if failure is not None:
                self.comment_failure = None
                raise m.APIError("comment request failed", rejected=failure == "rejected")
            return copy.deepcopy(comment)
        raise AssertionError((endpoint, payload, method))

    def mutation_count(self, state=None, method=None):
        return sum(payload is not None and (method is None or actual_method == method)
                   and (state is None or payload.get("state") == state)
                   for _, payload, actual_method in self.calls)


@pytest.fixture
def scenario(tmp_path, monkeypatch):
    binding = {"version": 1, "repository": m.REPO, "replacement": "c" * 40,
               "replacement_branch": "replacement", "index_sha256": "d" * 64,
               "audit_sha256": "e" * 64, "base_main": "b" * 40, "actor_id": 77}
    journal = m.Journal(tmp_path / "operation.jsonl", binding)
    fake = FakeGitHub(journal)
    monkeypatch.setattr(m, "api", fake)
    row = {"number": 289, "head": "a" * 40, "base": "b" * 40}
    original = {"head_ref": "review/batch-001",
                "source_snapshot_updated_at": fake.pr["updated_at"]}

    def run(*, reload=False, apply=True):
        if reload:
            fake.journal = m.Journal(journal.path, binding)
        m.process_pr(row, original, fake.journal, lambda: None, apply=apply)

    return fake, journal, run


def test_unchanged_close_and_explanation_are_idempotent(scenario):
    fake, journal, run = scenario
    run()
    run(reload=True)
    assert fake.pr["state"] == "closed" and len(fake.comments) == 1
    assert fake.mutation_count(state="closed") == 1
    assert fake.mutation_count(method="POST") == 1
    events = [x["event"] for x in fake.journal.events]
    assert events.index("close_intent") < events.index("close_response") < events.index("closed_verified")
    assert events.index("comment_intent") < events.index("comment_response")
    assert journal.events[-1]["event"] == "comment_verified"


@pytest.mark.parametrize("change", [
    {"draft": False}, {"body": "New owner instructions"}, {"title": "Owner changed title"},
    {"labels": [{"id": 9, "name": "hold"}]}, {"requested_reviewers": [{"id": 12, "login": "reviewer"}]},
    {"comments": 1}, {"review_comments": 1},
])
def test_owner_metadata_race_stops_without_reopening(scenario, change):
    fake, journal, run = scenario
    fake.on_close = change
    with pytest.raises(RuntimeError, match="no automatic reopen"):
        run()
    assert fake.pr["state"] == "closed"
    assert fake.mutation_count(state="closed") == 1 and fake.mutation_count(state="open") == 0
    assert not fake.comments
    assert any(x["event"] == "race_detected" for x in journal.events)
    with pytest.raises(ValueError, match="prior race"):
        run(reload=True)
    assert fake.mutation_count(state="closed") == 1


def test_another_owners_noop_close_is_never_reopened(scenario):
    fake, journal, run = scenario
    fake.other_owner_closes_before_patch = True
    with pytest.raises(RuntimeError, match="no automatic reopen"):
        run()
    assert fake.pr["state"] == "closed"
    assert fake.pr["body"] == "Another owner closed this independently"
    assert fake.mutation_count(state="open") == 0 and not fake.comments
    assert not any(entry["event"] == "closed_verified" for entry in journal.events)


def test_known_patch_response_survives_readback_failure_and_resumes(scenario):
    fake, journal, run = scenario
    fake.fail_post_read = True
    with pytest.raises(RuntimeError, match="readback network"):
        run()
    assert fake.pr["state"] == "closed"
    assert [x["event"] for x in journal.events][-2:] == ["close_response", "post_close_failure"]
    run(reload=True)
    recovered = [entry for entry in fake.journal.events if entry["event"] == "closed_verified"]
    assert len(recovered) == 1 and recovered[0]["recovered"] is True
    assert recovered[0]["observation"]["state"] == "closed"
    assert fake.mutation_count(state="closed") == 1
    assert len(fake.comments) == 1


def test_rejected_comment_resumes_once_without_reclosing(scenario):
    fake, _, run = scenario
    fake.comment_failure = "rejected"
    with pytest.raises(m.APIError):
        run()
    run(reload=True)
    run(reload=True)
    assert fake.mutation_count(state="closed") == 1
    assert fake.mutation_count(method="POST") == 2
    assert len(fake.comments) == 1


def test_unknown_comment_without_marker_stops_without_retry(scenario):
    fake, _, run = scenario
    fake.comment_failure = "unknown"
    with pytest.raises(m.APIError):
        run()
    with pytest.raises(ValueError, match="outcome is uncertain"):
        run(reload=True)
    assert fake.mutation_count(method="POST") == 1
    assert not fake.comments


def test_unknown_comment_with_owned_marker_recovers_without_duplicate(scenario):
    fake, _, run = scenario
    fake.comment_failure = "unknown"
    fake.create_before_failure = True
    with pytest.raises(m.APIError):
        run()
    run(reload=True)
    assert len(fake.comments) == 1 and fake.mutation_count(method="POST") == 1


def test_unrelated_closed_pr_is_never_adopted_or_reopened(scenario):
    fake, _, run = scenario
    fake.pr.update(state="closed", closed_at="2026-11-16T00:00:00Z")
    with pytest.raises(ValueError, match="no longer an open"):
        run()
    assert fake.mutation_count() == 0


def test_missing_patch_response_is_uncertain_and_never_retried(scenario, monkeypatch):
    fake, journal, run = scenario
    original = fake.__call__

    def lose_response(endpoint, payload=None, *, method=None):
        response = original(endpoint, payload, method=method)
        if payload == {"state": "closed"}:
            raise m.APIError("response lost", rejected=False)
        return response

    monkeypatch.setattr(m, "api", lose_response)
    with pytest.raises(m.APIError):
        run()
    assert journal.events[-1]["event"] == "close_failure"
    with pytest.raises(ValueError, match="close outcome is uncertain"):
        run(reload=True)
    assert fake.mutation_count(state="closed") == 1


def test_fsync_orders_intents_before_mutations_and_persists_responses(scenario, monkeypatch):
    fake, journal, run = scenario
    original_add = journal.add

    def add(event, **details):
        fake.trace.append("journal:" + event)
        return original_add(event, **details)

    monkeypatch.setattr(journal, "add", add)
    monkeypatch.setattr(m.os, "fsync", lambda _fd: fake.trace.append("fsync"))
    run()
    for kind, mutation in [("close", "closed"), ("comment", "comment")]:
        position = fake.trace.index("mutation:" + mutation)
        assert fake.trace[position - 3:position] == ["journal:" + kind + "_intent", "fsync", "fsync"]
        assert fake.trace[position + 1:position + 4] == [
            "journal:" + kind + "_response", "fsync", "fsync"]


def test_journal_rejects_incomplete_file_symlink_and_wrong_binding(tmp_path):
    path = tmp_path / "journal.jsonl"
    path.write_text('{"event":"close_intent"')
    with pytest.raises(ValueError, match="incomplete journal"):
        m.Journal(path, {"scope": 1})
    path.unlink()
    original = tmp_path / "original.jsonl"
    m.Journal(original, {"scope": 1})
    path.symlink_to(original)
    with pytest.raises(ValueError, match="symlink"):
        m.Journal(path, {"scope": 1})
    with pytest.raises(ValueError, match="binding differs"):
        m.Journal(original, {"scope": 2})
