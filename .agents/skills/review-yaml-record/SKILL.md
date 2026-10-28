---
name: review-yaml-record
description: Review one DUFMech Pfam family projection, curated overlay, or verified snapshot row and retain an append-only record report. Use for a requested family review, not bulk source ingestion.
---

# Review a DUFMech Record

Read [the retained-review contract](../../../docs/reviews.md) before saving. Resolve
the exact Pfam accession with `uv run dufmech-review inspect record PFxxxxx`.
The command verifies the frozen snapshot and includes a projection and curation
overlay when present. If only a JSON row exists, keep its row locator; do not
invent a YAML record or call a seed scientifically reviewed.

Assess the requested scope against the actual input: identity and Pfam/InterPro
grounding, available assertions and evidence quotations, source provenance,
validation, completeness, and remaining gaps. Separate experimental evidence from
predictions, source metadata, and seed heuristics. Report which checks ran and
their results; unavailable checks remain unavailable. Absence claims require a
search that includes ignored/hidden files.

Retain exactly one report for the completed review session with the inspection's
source and targets, real UTC start/end, actual reviewer, explicit scientific-review boolean,
native/common verdicts, and substantive domain assessments. Use `SEED_ONLY`
or `NEEDS_FOLLOWUP` when appropriate. Scope-limited audits are useful results;
their completion does not establish scientific characterization.

Write the content with `dufmech-review save --content PATH`; `inspect` alone is
not a saved review. Run `dufmech-review check` and confirm `git check-ignore` does
not exclude the report. Cite its path and summarize unresolved findings in the
final response. Never amend an earlier retained report; a correction is a new
artifact that identifies the previous report in its notes.

Curate overlays only when that work is requested; generated `data/families/`
records are projections. A `REVIEWED` overlay additionally requires the exact
passing-report/current-content-digest/linked-history gate in the contract. Record
actual history with [the history command](../../../docs/history.md), preserving
the distinction between a scoped audit and scientific evidence review. Do not
add fake history events or change a status simply to make coverage look complete.

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
