---
context:
  kind: category
  slug: two-seed-provenance
  source_revision: 0793aeb9d6770d4f1fb12120efb9c8baa08d262f
  source_state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-05
  source_files:
    data/worklists/interpro-pfam-duf-2026-10-05.json: 4c70383682228942940565906d83c8289fdd2e67f1841504ff280c30c4efac10
    data/worklists/interpro-pfam-duf-2026-10-05.manifest.json: 23d9d926caade8c9886d782e8e7cf7369598a64d4df61c64e2c7366c3949a36e
    data/worklists/interpro-pfam-duf-2026-10-05.tsv: 2a2e441c3a76c06ad33e30c12cd253dc50b72f9858d58be6c33a24f53dc23d4d
  targets:
  - id: PF04149
    locator: data/worklists/interpro-pfam-duf-2026-10-05.json#pfam_id=PF04149
  - id: PF19054
    locator: data/worklists/interpro-pfam-duf-2026-10-05.json#pfam_id=PF19054
  members:
  - PF04149
  - PF19054
  selection: Explicit PF04149 and PF19054 metadata sample; not a biological grouping.
  scope_paths: []
  record_digests: {}
started_utc: '2026-10-07T07:20:40Z'
finished_utc: '2026-10-07T07:24:23.895662Z'
verdict: SEED_ONLY
reviewer: Codex (GPT-6), scoped implementation audit
review_scope: 'Two explicitly selected frozen rows: identity, evidence categories,
  and lump/split triage.'
scientific_review: false
review_version: 1
status: saved
---

# YAML Category Review: two-seed-provenance

- Repository: CultureBotAI/DUFMech
- Category: two-seed-provenance
- Source revision: `0793aeb9d6770d4f1fb12120efb9c8baa08d262f` (working-tree hashes in metadata)
- Snapshot ID: `interpro-pfam-duf-2026-10-05`
- Started UTC: 2026-10-07T07:20:40Z
- Finished UTC: 2026-10-07T07:24:23.895662Z
- Verdict: SEED_ONLY
- Scientific review: false
- Reviewer: Codex (GPT-6), scoped implementation audit
- Review scope: Two explicitly selected frozen rows: identity, evidence categories, and lump/split triage.
- Selection Rule: Explicit PF04149 and PF19054 metadata sample; not a biological grouping.
- Member IDs: PF04149, PF19054
- Record locator: `data/worklists/interpro-pfam-duf-2026-10-05.json#pfam_id=PF04149`
- Record locator: `data/worklists/interpro-pfam-duf-2026-10-05.json#pfam_id=PF19054`

## Target Category

A two-family metadata sample comprising PF04149 (DUF397) and PF19054 (DUF5753), selected for this implementation audit only.

## Selection and Membership

The complete selection is the explicit Pfam list PF04149 and PF19054, both resolved in interpro-pfam-duf-2026-10-05. It is neither a random sample nor a biological functional class and does not represent the remainder of the worklist.

## Validation

Ran category inspection against the frozen worklist. Both IDs resolve uniquely, and existing manifest validation accepted JSON/TSV bytes, hashes, and row counts. The report retains exact member locators and input hashes.

## Lump and Split Review

Preserve separate records. The families have distinct Pfam and InterPro identifiers, and an unknown-function label supplies no evidence for merging them. No member-level sequence or experimental evidence was assessed to justify splitting either family.

## Identity and Grounding

PF04149 maps in the snapshot to DUF397/IPR007278; PF19054 maps to DUF5753/IPR043917. Source URLs name their respective Pfam IDs. Live identifier/label freshness is unverified.

## Evidence Patterns

Both rows are UNKNOWN_CANDIDATE and report zero structures. Their AlphaFold model counts are 19,000 and 19,007 respectively. PF19054's description proposes a ligand-binding domain in transcription regulators, whereas PF04149's description says its function is unknown. This difference is descriptive source metadata, not independently checked experimental proof.

## Completeness Patterns

The sample has source identity and coverage counters but no primary-study support reviewed during this session. Model counts and descriptions cannot supply missing assay, organism, or mechanism scope.

## Findings

The current metadata supports two separate research leads. The sample cannot establish scientific completion, family equivalence, or whole-corpus evidence coverage.

## Recommended Edits

Retain separate seeds. Investigate the proposed PF19054 activity as a claim requiring evidence and distinguish it from the source's broad unknown-candidate classification.

## Follow-up Checks

For each family, resolve live identity and inspect primary literature, then assess whether any characterized member supports a family-wide claim. Record narrower organism/member scope when extrapolation is unsupported.

## Additional Notes

No per-family REVIEWED flag or scientific history event was created. This retained category audit documents the selection and its limits only.
