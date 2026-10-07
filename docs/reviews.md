# Retained Reviews

Reviews are append-only Markdown artifacts under `reports/yaml_record_review/`,
`reports/yaml_category_review/`, and `reports/repo_review/`. The fleet-compatible
`yaml` directory names also support a Pfam row in a verified frozen JSON snapshot
when its family projection is not present. These Markdown paths are not excluded
by the repository's `reports/*.tsv` and `reports/*.json` ignore rules.

## Inspect, Review, Save

Run commands from the repository root with `uv run dufmech-review`, or use
`uv run python -m dufmech.reviews`. The optional global `--repo-root PATH` precedes
the subcommand.

```bash
uv run dufmech-review inspect record PF04149
uv run dufmech-review inspect category two-seeds --members PF04149 PF19054 --selection 'Explicit two-family metadata audit.'
uv run dufmech-review inspect repo dufmech --scope-path src/dufmech/reviews.py --scope-path src/dufmech/history.py
uv run dufmech-review save --content /absolute/path/to/completed-review.yaml
uv run dufmech-review check
uv run dufmech-review list --pfam-id PF04149
```

`inspect` returns deterministic JSON containing `status: inspection_only`, an
exact `context`, available snapshot/projection/curation data, and required section
headings. It neither writes a report nor performs scientific review. An optional
`--snapshot-id interpro-pfam-duf-YYYY-MM-DD` pins the inspected snapshot; otherwise
the latest snapshot is selected and verified through the existing manifest gate.

Perform the review before constructing a YAML or JSON content mapping. Supply:

- `context`: the complete unmodified object returned by inspection.
- `started_utc`, `finished_utc`: quoted UTC ISO-8601 strings; end must not precede start.
- `reviewer`: the actual reviewing person or agent, including model when known.
- `review_scope`: what was assessed and its limits.
- `scientific_review`: an explicit boolean, usually `false` for seed/infrastructure audits.
- `verdict`: `SEED_ONLY`, `NEEDS_FOLLOWUP`, `BLOCKED`, `FAIL`, or `PASS`.
- `sections`: a mapping from every returned section heading to actual review prose.

`save` (alias `finalize`) refuses missing, empty, or known scaffold content. Notes
can contain arbitrary prose and level-three subheadings. Explain why a check is
unavailable instead of inserting an empty field. Input context is recomputed at
save time, so changed source files or a changed base Git revision require a fresh
inspection and reassessment. The command prints the appended absolute path.

Each artifact contains machine-readable YAML frontmatter and the shared fleet
sections: target, validation, identity/grounding, evidence, completeness, findings,
recommended edits, follow-up checks, and additional notes. Categories additionally
retain their selection rule, exact members, and lump/split reasoning. Repository
reviews retain their selected source paths and scope.

`source_revision` is the real Git HEAD at inspection, not a claim that uncommitted
work was already published. `source_state: working_tree` and exact source SHA-256
hashes describe the inspected input bytes, including overlays. Snapshot ID and
record locators distinguish a YAML projection from a JSON row. Report timestamps
are supplied once and preserved; no generation-time clock enters family records.

Reports use `<finished-UTC>-<slug>.md`, with `-02`, `-03`, and subsequent suffixes
on collisions. Publication is exclusive and atomic. There is no overwrite option;
corrections require a new report referencing the previous artifact in its notes.
Paths cannot escape the repository or traverse symlinks. `check` includes ignored
and hidden reports and verifies metadata, sections, timestamps, filenames, and
internal paths. It does not repeat biological research or invalidate an old review
merely because its source content has since changed. Exit 0 means the requested
operation succeeded; content/validation/I/O failures return 1, argparse errors 2.

## The REVIEWED Contract

`curation_status: REVIEWED` means a completed **scoped** per-record review with a
passing verdict exists for the current effective record. It is not a scientific
endorsement. `scientific_review` remains explicit report metadata and must not be
inferred from the curation status, the existence of a report, or passing schema QC.

The curation overlay's `review_id` is the repository-relative retained report path.
`reviews.require_completed_review(root, pfam_id, review_id, record)` must succeed
after the overlay is merged into the effective `FamilyRecord`. The helper checks:

1. A saved per-record `PASS` report for exactly this Pfam accession.
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
metadata, including `path`, `href`, `context`, `finished_utc`, `verdict`,
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
