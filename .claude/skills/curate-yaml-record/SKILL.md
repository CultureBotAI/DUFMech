---
name: curate-yaml-record
description: Curate one DUFMech Pfam family's evidence-backed overlay, append actual canonical history, and regenerate its family projection. Use for a requested record correction or evidence addition, not review-only work or bulk source ingestion.
---

# Curate a DUFMech Family

Use this skill only inside DUFMech. Resolve one exact Pfam accession before
editing. A family, a subfamily and a tested protein are different claim scopes.
For review-only requests, use the maintained
[record-review skill](../review-yaml-record/SKILL.md); save its timestamped report
without treating the request as permission to change scientific content.

Read the [record contract](../../../docs/records.md),
[history contract](../../../docs/history.md), and the
[field/evidence checklist](references/review-checklist.md) for the target.
The [schema](../../../src/dufmech/schema/dufmech.yaml) is authoritative.

## Authoring Boundaries

- Edit the human-owned `curation/families/PFxxxxx.yaml` overlay. It conforms to
  `FamilyCuration`, not `FamilyRecord`. Use a narrow text-preserving patch and
  retain unrelated fields; do not serialize the generated record into an overlay.
- Preserve immutable `data/worklists/` snapshots. Imported identity, labels,
  counters, seed classification and score provenance cannot be overridden in
  the overlay. A source correction needs its own explicitly scoped source workflow.
- Never hand-edit `data/families/`, its ownership manifest, generated schemas,
  `curation_events`, or Pages. `just records` previews the native builder and
  `just records --apply` performs its validated, guarded publication.
- Keep appropriately licensed minimal source extracts in `evidence/`. Each
  assertion needs its exact scope, evidence kind, reference, source URL, quotation,
  explanation, cache path and SHA-256. Inspect the source itself; predictions or
  associations do not establish experimental function across the whole family.

Use an isolated worktree and the repository's coordination/authorization rules.
Search ignored and hidden files before declaring a record or supporting evidence
absent. No paid provider call, source adoption, or GitHub publication is implied
by a request to curate a record.

## Native Write and History Sequence

1. Inspect the current family and any overlay, source snapshot, retained reviews
   and sidecars. Run `just records-check` to establish the baseline; explain any
   existing failure before editing. Resolve contradictory evidence rather than
   silently dropping it or assigning a stronger status.
2. Apply the requested evidence-backed change to the overlay, initially using
   `IN_PROGRESS` for substantive curation. Do not carry an old `review_id` forward
   as approval of changed content. Preserve existing evidence and attribution.
3. Append a real canonical CREATE or EDIT event with `just new-history`, targeting
   the existing overlay or projection for this Pfam accession. Follow the history
   contract's required arguments: actual UTC session start, actual actor/tool/model,
   event, outcome, and a summary/details describing this work. The stable pointer is
   `history/records/PFxxxxx`. Do not attribute the agent's work to the user or invent
   an event to satisfy validation. If history creation fails, keep the unpublished
   worktree for repair; do not force the projection through.
4. Run `just records` and inspect the proposed changes, then `just records --apply`.
   Run `just validate-all validate-schema`; unrelated family projections should
   remain unchanged. Edited/unowned generated files or recovery-journal conflicts
   require reconciliation, not deletion of the guard or recovery copies.

## Review and Publication

A completed review is a separate append-only structured YAML/Markdown bundle,
not an implicit effect of editing or regeneration. Follow the
[retained-review contract](../../../docs/reviews.md) and record-review skill:
inspect the effective projection, perform the stated review, supply its unchanged
source and targets and real UTC start/end, then save the completed content through
`just review save --content PATH`. Verify the saved path with `just reviews-check`.

Do not promote a seed because schema checks passed. `REVIEWED` requires a retained
per-record PASS for the exact semantic digest and a linked canonical REVIEW event
targeting `data/families/PFxxxxx.yaml`. Create that actual event after the review
starts, with its report URL; only then set the overlay's status/review pointer and
regenerate. A scoped PASS is not necessarily scientific review or human endorsement:
read `review_scope`, `scientific_review`, and reviewer identity. Changed scientific
content requires a fresh review; history-index bookkeeping is separately validated.

Before an authorized publication, run `just qc` and inspect the full diff. Changes
to source bytes can invalidate the website source-pin ledger: the supported Pages
workflow first publishes an authorized source checkpoint, then captures that exact
commit with `uv run --locked python -m dufmech.site_sources capture --commit FULL_SHA`, regenerates
with `just render`, and reruns QC. Never invent a pin or weaken a check. If publishing
was not authorized, retain the local changes and report that remaining publication
step instead of committing or pushing to make a gate pass.

Report the changed authoring inputs, generated outputs, actual history/report paths,
checks run, supported conclusions, and unresolved or genuinely unknown findings.

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

For an audit-only request, use this same structured output route without
editing the overlay, regenerating records or appending curation history.
