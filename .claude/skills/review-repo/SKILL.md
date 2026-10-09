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
source and targets, declared scope, explicit scientific-review boolean, verdict, and actual
domain assessments. Name unverified areas and specific follow-ups.
Run `dufmech-review check`, verify the report is not ignored, and link it in the
final response. Reports are append-only; later corrections reference earlier
artifacts instead of replacing them.

Repository audit completion is not family scientific review. It cannot promote
records to `REVIEWED`. Record actual implementation/audit activity, when warranted,
with the canonical [history workflow](../../../docs/history.md) against the
appropriate infrastructure/report target. Follow the user's existing authorization
for fixes or publication; do not expand an audit into unrelated changes.

## Structured Review Output

Follow [docs/record-reviews.md](../../../docs/record-reviews.md) and the
[DUFMech profile](../../../docs/record-review-profile.md) for every new review.
Use the native inspection's `structured.source` and `structured.targets`;
author the common schema with actual checks, evidence-linked domain assessments,
findings/actions, coverage and limits, then run `just review save --content PATH`.
New output is `reviews/structured/<timestamp>-<slug>/review.yaml` plus its
derived `review.md`. Link both; run `just reviews-check`. Historical reports
remain read-only. Preserve the scientific-review flag, native verdict,
snapshot identity, exact row selector and named semantic digest.
Map seed-only, follow-up, blocked, failing and passing native verdicts using
the profile. Never label an inspection, deterministic scan, provider draft
or seed metadata as a completed scientific review. Native status and history
requirements still apply independently of common schema validity.

Use common `kind: repository`; native inspection still accepts `repo`.
