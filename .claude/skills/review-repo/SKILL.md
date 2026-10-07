---
name: review-repo
description: Perform a scoped DUFMech repository audit and retain a timestamped report of validation, provenance, coverage, findings, and follow-ups. Use for repository quality or workflow review, not automatic scientific review of every family.
---

# Review the DUFMech Repository

Read [the review contract](../../../docs/reviews.md). Identify the repository
revision and audit scope, then inspect with `uv run dufmech-review inspect repo
SLUG --scope-path PATH`, repeating `--scope-path` for the files actually assessed.
Inspection is read-only and verifies the current frozen worklist. Choose the
scope from the user's request; a tooling audit does not imply literature review.

Read the scoped code, records, schemas, tests, and previous audit evidence. Run
relevant available checks and report exact outcomes. Separate source integrity,
schema/evidence validation, retained reviews/history, rendering, and scientific
completeness. Do not report a test as passed because its command exists. Before
absence claims, include ignored/hidden files and state any search exclusions.

Retain exactly one report through `dufmech-review save --content PATH` after
performing the audit. Include real UTC start/end, reviewer, unchanged inspected
context, declared scope, explicit scientific-review boolean, verdict, and actual
text for every returned section. Name unverified areas and specific follow-ups.
Run `dufmech-review check`, verify the report is not ignored, and link it in the
final response. Reports are append-only; later corrections reference earlier
artifacts instead of replacing them.

Repository audit completion is not family scientific review. It cannot promote
records to `REVIEWED`. Record actual implementation/audit activity, when warranted,
with the canonical [history workflow](../../../docs/history.md) against the
appropriate infrastructure/report target. Follow the user's existing authorization
for fixes or publication; do not expand an audit into unrelated changes.
