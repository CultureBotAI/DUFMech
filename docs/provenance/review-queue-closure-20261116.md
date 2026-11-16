# Review queue closure helper, 2026-11-16

[Issue #461](https://github.com/CultureBotAI/DUFMech/issues/461) tracks concurrent
owner changes during closure. [Issue #462](https://github.com/CultureBotAI/DUFMech/issues/462)
tracks durable mutation receipts and recovery. The bounded helper is
`scripts/adhoc/close_consolidated_reviews_20261116.py`; the consolidation scope
remains [issue #460](https://github.com/CultureBotAI/DUFMech/issues/460).

Inputs are the committed public source index and compressed audit, exact
replacement branch/SHA, an explicit durable private JSONL journal, and optional
in-scope PR numbers. The helper verifies the index/audit bytes against that
replacement commit and every original review blob against its tree. The journal
binds their hashes, replacement, frozen main and authenticated actor ID. Keep the
journal private: API observations can contain user identities and full PR text.
Never replace, truncate or publish its contents as repository documentation.

The default command makes GitHub GET requests and records local observations.
Only `--apply` mutates GitHub. The caller must first authorize the bounded action,
validate the repository, acquire its CLAW lock, complete independent review and
bind passing native/publication/hosted checks to the exact replacement. The
helper does not establish those scientific or workflow approvals.

Before closing, the helper freezes source identity, draft/title/body, issue and
review-comment counts, labels, assignees, reviewer/team requests and other
owner-sensitive PR fields. It compares the final preflight, PATCH response and
fresh readback. State and server lifecycle timestamps are the intended changes;
mergeability cache fields are not treated as owner input. REST has no atomic
compare-and-swap in this implementation, so a final-request race remains possible.

A detected race stops the batch and retains the response, observation and failure
receipt. The helper never automatically reopens a PR. A successful close PATCH
can be a no-op if another owner closed it after the final GET; without an atomic
compare-and-swap, the helper cannot prove exclusive ownership of that transition.
The actual current state remains for coordinator reconciliation. A later invocation
never automatically reopens an earlier operation or recloses a user-reopened PR.

Each mutation gets an append-only, file-and-directory-fsynced intent before the
request and a response receipt immediately afterward. Exceptions retain an
explicit failure/outcome record. Partial or differently bound journals are
refused. A known closure response can recover from a failed later read; after fresh
identity, source-branch and metadata checks it appends an explicit recovered
closed-verification receipt. A close intent without a response cannot be silently
adopted as success.

Explanations use a deterministic HTML marker and require the exact body and
authenticated actor identity. Recovery reconciles the full comment inventory
before finishing an owned missing explanation. A definite HTTP rejection can be
retried. An uncertain comment request can be recovered if its unique matching
comment exists; if absent, the helper stops rather than risk a duplicate.
Verified comments are read back and never recreated merely because they vanish.

Offline tests mock every API call and cover normal/idempotent closure, changed
draft/body/title/labels/requests/counters, another owner's successful no-op closure,
readback outages, rejected and uncertain comment requests, missing closure
responses, fsync ordering and invalid journal paths/bindings. Mutation controls
run against private copies in fresh Python processes. These tests make no live
closure, reopen, comment, merge or deployment request.
