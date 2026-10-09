# Retained Reviews

New reviews use the common YAML and derived Markdown contract in
[record-reviews.md](record-reviews.md), with DUF-specific commands and rubrics in
[record-review-profile.md](record-review-profile.md). The authoritative path is
`reviews/structured/<timestamp>-<slug>/review.yaml`; the sibling `review.md`
is generated, never an independently editable verdict.

## Inspect, Review, Save

```bash
uv run --locked dufmech-review inspect record PF04149
uv run --locked dufmech-review inspect category two-seeds --members PF04149 PF19054 --selection 'Explicit two-family metadata audit.'
uv run --locked dufmech-review inspect repo dufmech --scope-path src/dufmech/reviews.py
uv run --locked dufmech-review save --content /absolute/session/completed-review.yaml
just reviews-check
uv run --locked dufmech-review list --pfam-id PF04149
```

The optional global `--repo-root PATH` precedes the subcommand. Inspection returns
`status: inspection_only`, native context and available records, rubric headings,
and `structured` source/target fields. `--snapshot-id` pins a verified frozen
snapshot; otherwise the latest is verified. Inspection neither saves a review
nor performs science. Read the actual evidence and complete the common schema,
preserving these captured fields, native verdict, scope and scientific-review
boolean. Keep experimental, computational, contextual and seed evidence separate.

`save` (alias `finalize`) accepts only the new common document. It recomputes the
native frozen snapshot/projection context and semantic digest, then uses the
shared validator and atomic saver. Changed inputs require fresh inspection and
reassessment. No auto-conversion invents evidence, check results or assessments
from the old prose envelope. Categories and batches retain exact Pfam selection;
repository inspection maps native `repo` to common `repository`.

A passing common verdict requires a positive, evidence-linked assessment for
every reviewed target; passing checks or an empty findings list are insufficient.
Plain `pass` cannot retain unknown or concerning assessments. Terminal findings
must concern targets actually reviewed and assessed, with nonfailed completion.
Preserve all affected targets of each superseded finding, even when recording
a partial observation. A terminal finding is not automatically current: use the
shared currentness/planning views and retain their stale or unverified warnings.

The native reader verifies retained source Git provenance as well as the YAML
and derived Markdown pair. Historical Git inputs must match the retained commit;
working-tree snapshots must retain their input hashes and a verifiable base.
This proves what was inspected, not the scientific correctness of its claims.

The historical Markdown directories `reports/yaml_record_review/`,
`reports/yaml_category_review/` and `reports/repo_review/` remain read-only
inputs. Their existing strict frontmatter/body, path, digest and status semantics
remain supported; current records and history need no migration. Both formats
are checked, including ignored/hidden files. Shared checks reject modification or
deletion of previously committed structured bundles against `RECORD_REVIEW_BASE`
(HEAD locally; trusted event base in PR/merge-group/push CI).

Exit 0 means the requested command succeeded, not that science was established.
Validation/I/O failures return 1 and argparse errors 2. Correct a saved observation
with a new review that cites its predecessor; never rewrite retained evidence.

## The REVIEWED Contract

`curation_status: REVIEWED` means a completed **scoped** per-record review with a
passing verdict exists for the current effective record. It is not a scientific
endorsement. `scientific_review` remains explicit report metadata and must not be
inferred from the curation status, the existence of a report, or passing schema QC.

The curation overlay's `review_id` is the repository-relative retained report path.
`reviews.require_completed_review(root, pfam_id, review_id, record)` must succeed
after the overlay is merged into the effective `FamilyRecord`. The helper checks:

1. A saved per-record `PASS` report for exactly this Pfam accession. For new
   bundles this also requires explicit native `PASS`, common `pass`, completed
   status, full scope and the named `dufmech-record-content-v1` digest.
2. A SHA-256 digest matching the current record's content, excluding only
   `curation_status`, `review_id`, and the generated-only `curation_events` audit
   index to avoid circular bookkeeping. The stable `curation_history` pointer
   and all claim/evidence/provenance content remain in the digest.
3. A canonical-schema-valid history event targeting `data/families/PFxxxxx.yaml`,
   with `type: REVIEW` and `outcome: changed` or `no_change`.
4. That event's `links.urls` includes `reviews.review_report_url(review_id)`, a
   stable GitHub `blob/main/` URL for the append-only report, and its UTC session
   timestamp is no earlier than the review start.

Generate the `IN_PROGRESS` projection before inspecting it. Finalize the review,
write the real linked history event, then set the overlay's `review_id` and
`curation_status`. Regenerating projections after those bookkeeping changes leaves
the reviewed content digest unchanged. Appending history refreshes the read-only
audit index without invalidating that semantic digest; full projection validation
must still reject stale or forged audit indexes. A changed claim, evidence, provenance,
dataset, discussion, or source counter requires a new review. Row-only reviews
remain useful but cannot satisfy the projection digest gate. Category/repository
reviews and `SEED_ONLY`/`NEEDS_FOLLOWUP` verdicts cannot promote a record.

## Pages Integration

`reviews.load_review_metadata(root, pfam_id=None)` returns sorted validated
metadata for both formats, including `path`, `href`, `context`, `finished_utc`, `verdict`,
`review_scope`, and `scientific_review`. With a Pfam argument it includes its record
and category reports. Load all reports once per site render and index membership
in memory; do not run a repository scan for every generated family page.

`href` is URL-encoded **relative to the repository root**, not a Pages page. Link it
under a pinned GitHub repository URL or copy the validated artifact into the site
and link that destination. Escape displayed text. Never concatenate an unvalidated
overlay path into HTML. The generated-only `curation_events` index references
canonical sidecars by repository-relative path and zero-based event index; use
those sidecars for full details. Curated records retain the stable history directory
pointer described in [history.md](history.md). `review_id` identifies a specific
finalized report. No invented event or generation-time clock enters either index.

Repository skills live in `.claude/skills/review-yaml-record/`,
`.claude/skills/review-yaml-category/`, and `.claude/skills/review-repo/`.
The matching `.agents/skills/` entries point to those maintained instructions.

For structured bundles `path` is the authoritative YAML pointer and
`markdown_path` identifies the derived report. The optional `source_bytes`
sink captures both validated byte strings. Pages copies and pins both without
reopening either pathname; the status predicate uses that same validated capture.
