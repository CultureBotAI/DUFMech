---
context:
  kind: repo
  members: []
  record_digests: {}
  scope_paths:
  - docs/records.md
  - src/dufmech/pfam_history.py
  - src/dufmech/reclassify.py
  - src/dufmech/score_inputs.py
  - src/dufmech/worklist.py
  - tests/test_duf_puf_worklist.py
  - tests/test_pfam_history.py
  - tests/test_reclassify.py
  - tests/test_score_inputs.py
  selection: ''
  slug: classification-release-guards
  snapshot_id: interpro-pfam-duf-2026-10-08
  source_files:
    data/worklists/interpro-pfam-duf-2026-10-08.json: 9f0992961c30c5d92343a92aab000cd20b6c4213952b4c68408c3065779a46ec
    data/worklists/interpro-pfam-duf-2026-10-08.manifest.json: 5929010740007a44480dac1fe804840b5885e131bceccc3043dbcb9146e991d5
    data/worklists/interpro-pfam-duf-2026-10-08.tsv: 3d873968fcb87babafe59c01722c0d914f4ddc45de28cb8de4595477c353f91b
    docs/records.md: 8e041d6af543c68fdec2ed1798f2c339b74c14006cb8402185b7c4350ec781b2
    src/dufmech/pfam_history.py: 657e533ae7fc1e1c9ea3b5ee9468698ca18c07d23e03ac7e25f74834b12d3703
    src/dufmech/reclassify.py: 8f399730d68e65e63aa81e958a11d25bb2c6bbbef2c2e0b6f3b81382668a5009
    src/dufmech/score_inputs.py: 181da8d3ae231bed2fd8ad6f3bcd8a6bc5de630709c57fa5e6b3b185865a75bd
    src/dufmech/worklist.py: 6ff68c3e9b456989ed10ca97bd1a0c6dba0cc23026ff22386744d6772ddffc8b
    tests/test_duf_puf_worklist.py: cc0086df0d64afed7a335450ab079ca80106887bd479b5d5296f1301c5985a14
    tests/test_pfam_history.py: cc622918ac156b7612f9fbd7b53a46f25e975be986794ab982fa4981d3ab4731
    tests/test_reclassify.py: 97a3303ec5088584eac8cb1ccd966e171335f6ed63166e944b1bb453e8ad9345
    tests/test_score_inputs.py: 4ec31d0dae0b3bd27ac5ab3b0bab03544a1d5bb299c9f59422e14e0599864698
  source_revision: 58aff1a53041689fba79c872c35fbb6c57f87458
  source_state: working_tree
  targets:
  - id: docs/records.md
    locator: docs/records.md
  - id: src/dufmech/pfam_history.py
    locator: src/dufmech/pfam_history.py
  - id: src/dufmech/reclassify.py
    locator: src/dufmech/reclassify.py
  - id: src/dufmech/score_inputs.py
    locator: src/dufmech/score_inputs.py
  - id: src/dufmech/worklist.py
    locator: src/dufmech/worklist.py
  - id: tests/test_duf_puf_worklist.py
    locator: tests/test_duf_puf_worklist.py
  - id: tests/test_pfam_history.py
    locator: tests/test_pfam_history.py
  - id: tests/test_reclassify.py
    locator: tests/test_reclassify.py
  - id: tests/test_score_inputs.py
    locator: tests/test_score_inputs.py
started_utc: '2026-10-08T06:57:46Z'
finished_utc: '2026-10-08T07:14:32Z'
verdict: PASS
reviewer: Codex
review_scope: 'Implementation audit of the local classification-release-guards patch
  for DUFMech issues #165 and #173: Pfam unknown-name parsing, historical naming versus
  current unknown-function reasons, policy-versioned reclassification and verified
  input compatibility. No scientific family curation, source adoption or corpus migration.'
scientific_review: false
review_version: 1
status: saved
---

# Repository Review: classification-release-guards

- Repository: CultureBotAI/DUFMech
- Repo: classification-release-guards
- Source revision: `58aff1a53041689fba79c872c35fbb6c57f87458` (working-tree hashes in metadata)
- Snapshot ID: `interpro-pfam-duf-2026-10-08`
- Started UTC: 2026-10-08T06:57:46Z
- Finished UTC: 2026-10-08T07:14:32Z
- Verdict: PASS
- Scientific review: false
- Reviewer: Codex
- Review scope: Implementation audit of the local classification-release-guards patch for DUFMech issues #165 and #173: Pfam unknown-name parsing, historical naming versus current unknown-function reasons, policy-versioned reclassification and verified input compatibility. No scientific family curation, source adoption or corpus migration.
- Record locator: `docs/records.md`
- Record locator: `src/dufmech/pfam_history.py`
- Record locator: `src/dufmech/reclassify.py`
- Record locator: `src/dufmech/score_inputs.py`
- Record locator: `src/dufmech/worklist.py`
- Record locator: `tests/test_duf_puf_worklist.py`
- Record locator: `tests/test_pfam_history.py`
- Record locator: `tests/test_reclassify.py`
- Record locator: `tests/test_score_inputs.py`

## Target Repository

CultureBotAI/DUFMech at base 58aff1a53041689fba79c872c35fbb6c57f87458. Implementation worktree: /private/tmp/dufmech-classification-release-guards, branch fix/classification-release-guards. This report is retained in a separate sparse audit worktree with byte-identical copies of all nine scoped changed files, avoiding unpublished source pins in the generated website.

## Scope and Selection

Reviewed the diff and surrounding parser, reclassification, scoring and lineage behavior, plus regression tests and rollout documentation for issues https://github.com/CultureBotAI/DUFMech/issues/165 and https://github.com/CultureBotAI/DUFMech/issues/173. Inspected the retained October 8 worklist and October 7 Pfam previous-name snapshot with structured JSON parsing. This is not a whole-repository correctness certification.

## Validation

The full Python suite completed with 1,143 passed, three empty-parameter-set skips in the governed skill-frontmatter tests, and one upstream SSSOM/LinkML deprecation warning. The strengthened final reclassification tests were rerun separately: 20 passed. Ruff and git diff --check passed. All non-browser just qc gates passed: documentation, nine snapshot manifests, corpus report, 8,295 schema-valid records with zero drift, offline research profile, KGX/SSSOM exports, isolated OAK correspondence, source governance, five existing reviews, two existing history records, cross-Mech report, generated site, and site contract/budgets. The initial qc invocation stopped at the final browser gate because the sandbox denied binding 127.0.0.1 (EPERM). Rerunning just browser-test with the required localhost permission passed all six tests. No failing behavioral gate was bypassed. Separate just id-labels-oak-test passed the full 8,295-pair corpus and all malformed-input cases with network denied. All 18 vendored governance artifacts matched the immutable published CLAW pin. Source governance retains zero errors and 15 existing license/adoption warnings. Module, script, installed entrypoint and just-wrapper reclassification --help checks passed.

## Identity and Grounding

The parser now accepts four-digit UPF family identifiers, retaining existing DUF compound-name support, without treating UPF1/UPF2/UPF3 gene labels as unknown-function family labels. Checking all 1,834 retained previous-name rows preserved every recorded previous_unknown_names identifier; PF18141 UPF1_1B_dom was the sole changed currently_unknown_name flag in memory. The UPF1 gene identity is corroborated by https://www.ncbi.nlm.nih.gov/gene/5976; an example of the distinct UPF0001 family label is https://prosite.expasy.org/PS01211. These checks do not introduce a new family record or establish its experimentally demonstrated function.

## Evidence

Historical numbered labels are removed only from the internal classification text; original names, descriptions, identifiers, counters and source URLs are preserved. Separate present-tense unknown statements still produce unknown reasons, including function remains unknown and function is still unknown. The real-corpus regression changes prospective scoring for exactly ten families: PF05647, PF10862 and PF14298 cease treating explicit former names as current unknown-function claims; PF10015, PF10912, PF11503, PF13907, PF14934, PF16392 and PF16404 retain unknown status from explicit current uncertainty. No new experimental evidence is inferred; known_evidence_count remains zero in these metadata-only checks.

## Completeness

Classifier policy unknown-function-metadata-v3 is the default. The Python reclassification API retains explicit v2 replay, verified-input loading accepts both policies, and the published October 5 rows reproduce under v2 without modifying snapshots. Frozen artifacts, family projections, exports and Pages remain unchanged. Issue #165 still needs a newly frozen previous-name table and an actual migration; #173's retained corpus needs a new v3 derivation before publishing corrected scores. Neither issue should be described as fully adopted merely because this code patch passes.

## Findings

No remaining blocking defect found in the scoped code changes. Adversarial checks exposed a converse risk in ignoring former labels: explicit function remains unknown/function is still unknown must survive. The v3 policy and regression tests now handle that case. Existing worklist parent-row replay limitations (#156), chained historical-name provenance loss (#176), source licensing warnings and publication-pin workflow limitations (#179) remain outside this patch and are not certified as resolved.

## Recommended Edits

Keep this patch limited to classifier behavior, backwards-compatible replay, tests and rollout documentation. Do not manually edit immutable snapshots or generated family records. Retain the explicit distinction among seed classification, automated scoring and scientific curation.

## Follow-up Checks

Address the outstanding provenance safeguards before the scored release. Freeze a new Pfam previous-name snapshot, migrate the current worklist using actual acquisition dates, and reclassify the migrated worklist under v3; each derivation needs a later date than its parent. Do not overwrite October 8 artifacts or fabricate a future run. Rebuild compatible cross-Mech artifacts and review all changes before generating records, scores, exports and Pages. Publish this review only with a reachable source checkpoint and compatible site pins. The planned 10-20-family evidence-backed pilot remains future work.

## Additional Notes

This report has scientific_review false and does not promote any family to REVIEWED. No providers were ingested, no curated overlays/history were fabricated, no GitHub issues were closed, and no PR was opened or merged for this batch. Original shared checkout main and its untracked .claude/hooks and .claude/settings.json were preserved. Native review validation applies to this retained report; exact source hashes identify the reviewed working-tree bytes.
