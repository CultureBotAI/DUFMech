---
name: review-yaml-category
description: Review a selected DUFMech family cohort, including membership and lump/split reasoning, and retain an append-only category report. Use for cross-family category audits, not an individual-family review or an automatic whole-corpus certification.
---

# Review a DUFMech Category

Read [the retained-review contract](../../../docs/reviews.md). Define a reproducible
selection rule, category slug, and exact unique Pfam member list. Run
`uv run dufmech-review inspect category SLUG --members PFxxxxx PFyyyyy --selection 'RULE'`.
Keep the verified snapshot ID, source revision, member locators, and input hashes
from the returned context. A sampled cohort must say how it was sampled and which
families it includes; it cannot silently stand for every family in the repository.

Evaluate identity consistency, evidence patterns, validation, completeness, and
cross-member findings within the requested scope. In the lump/split section,
explain whether the evidence supports preserving distinct records, merging a
concept, or splitting a heterogeneous concept. Shared unknown-function labels,
model availability, or a seed category alone do not justify biological merging.
Distinguish source snapshots and predictions from primary experimental evidence.
Search ignored and hidden files before asserting evidence or records are absent.

Supply actual text for every category section, including selection/membership,
lump/split reasoning, findings, recommended edits, follow-ups, and flexible notes.
Retain exactly one completed scoped category report using `dufmech-review save
--content PATH`, then run `dufmech-review check` and verify the artifact is not
gitignored. Use honest limits and a `SEED_ONLY` or `NEEDS_FOLLOWUP` verdict when
scientific review is incomplete; never save an empty inspection as a review.

A category report does not mark its members `REVIEWED`. Individual promotions
require each member's passing retained record review and linked canonical history
event for its unchanged content. Review-driven curation or publication follows
the user's authorized scope. Report the retained artifact and remaining work;
append a new report for later corrections rather than changing the old one.
