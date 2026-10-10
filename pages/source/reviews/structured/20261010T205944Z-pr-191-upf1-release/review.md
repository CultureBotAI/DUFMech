# PR 191 adversarial audit: retained PF18141 migration and release

- Review: 20261010T205944Z-pr-191-upf1-release
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-10T20:32:33Z
- Finished UTC: 2026-10-10T20:59:44Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

The scoped issue 165 refresh preserves all 8295 parent worklist rows and adds only PF18141. The identical pinned Pfam gzip produces exactly one normalized flag correction; cross-Mech evidence and acquisition provenance are unchanged. Issue 190 tracks the corrected stale-baseline regression. No unresolved correctness finding remains in the selected release inputs; cross-Mech terms and scientific interpretation remain explicitly outside this approval.

## Scope And Provenance

Release-input audit of the selected frozen snapshots, PF18141 seed projection, corpus manifest, exports, ID labels, source governance and regression tests. Deterministic comparisons cover every inherited worklist row and projection, not scientific review of every family.

Selection: Explicit 18-file source, projection, export and regression surface for PR 191.
Coverage: full; 18 reviewed / 18 in the declared population.
Source: working_tree at Git base 2a9a930b2b5b73c88f7d2d570f9f49c45d3f48c2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| conf/id_labels/pfam.obo | conf/id_labels/pfam.obo | source | conf/id_labels/pfam.obo |
| conf/id_labels/provenance.json | conf/id_labels/provenance.json | source | conf/id_labels/provenance.json |
| curation/source_queue.tsv | curation/source_queue.tsv | source | curation/source_queue.tsv |
| data/cross_mech/cross-mech-duf-examples-2026-10-10.json | data/cross_mech/cross-mech-duf-examples-2026-10-10.json | source | data/cross_mech/cross-mech-duf-examples-2026-10-10.json |
| data/cross_mech/cross-mech-duf-examples-2026-10-10.manifest.json | data/cross_mech/cross-mech-duf-examples-2026-10-10.manifest.json | source | data/cross_mech/cross-mech-duf-examples-2026-10-10.manifest.json |
| data/families/PF18141.yaml | data/families/PF18141.yaml | source | data/families/PF18141.yaml |
| data/families/manifest.json | data/families/manifest.json | source | data/families/manifest.json |
| data/worklists/interpro-pfam-duf-2026-10-10.json | data/worklists/interpro-pfam-duf-2026-10-10.json | source | data/worklists/interpro-pfam-duf-2026-10-10.json |
| data/worklists/interpro-pfam-duf-2026-10-10.manifest.json | data/worklists/interpro-pfam-duf-2026-10-10.manifest.json | source | data/worklists/interpro-pfam-duf-2026-10-10.manifest.json |
| data/worklists/pfam-previous-unknown-names-2026-10-10.json | data/worklists/pfam-previous-unknown-names-2026-10-10.json | source | data/worklists/pfam-previous-unknown-names-2026-10-10.json |
| data/worklists/pfam-previous-unknown-names-2026-10-10.manifest.json | data/worklists/pfam-previous-unknown-names-2026-10-10.manifest.json | source | data/worklists/pfam-previous-unknown-names-2026-10-10.manifest.json |
| download.yaml | download.yaml | source | download.yaml |
| exports/kgx/edges.tsv | exports/kgx/edges.tsv | source | exports/kgx/edges.tsv |
| exports/kgx/nodes.tsv | exports/kgx/nodes.tsv | source | exports/kgx/nodes.tsv |
| exports/sssom/dufmech.sssom.tsv | exports/sssom/dufmech.sssom.tsv | source | exports/sssom/dufmech.sssom.tsv |
| tests/test_exports.py | tests/test_exports.py | source | tests/test_exports.py |
| tests/test_pfam_history.py | tests/test_pfam_history.py | source | tests/test_pfam_history.py |
| tests/test_upf1_migration_release.py | tests/test_upf1_migration_release.py | source | tests/test_upf1_migration_release.py |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Migration and lineage regressions | passed | True | data/cross_mech/cross-mech-duf-examples-2026-10-10.json, data/cross_mech/cross-mech-duf-examples-2026-10-10.manifest.json, data/families/PF18141.yaml, data/families/manifest.json, data/worklists/interpro-pfam-duf-2026-10-10.json, data/worklists/interpro-pfam-duf-2026-10-10.manifest.json, data/worklists/pfam-previous-unknown-names-2026-10-10.json, data/worklists/pfam-previous-unknown-names-2026-10-10.manifest.json, tests/test_exports.py, tests/test_pfam_history.py, tests/test_upf1_migration_release.py | 112 tests passed in 29.01 seconds. |
| Complete local quality gate | passed | True | conf/id_labels/pfam.obo, conf/id_labels/provenance.json, curation/source_queue.tsv, data/cross_mech/cross-mech-duf-examples-2026-10-10.json, data/cross_mech/cross-mech-duf-examples-2026-10-10.manifest.json, data/families/PF18141.yaml, data/families/manifest.json, data/worklists/interpro-pfam-duf-2026-10-10.json, data/worklists/interpro-pfam-duf-2026-10-10.manifest.json, data/worklists/pfam-previous-unknown-names-2026-10-10.json, data/worklists/pfam-previous-unknown-names-2026-10-10.manifest.json, download.yaml, exports/kgx/edges.tsv, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, tests/test_exports.py, tests/test_pfam_history.py, tests/test_upf1_migration_release.py | All local gates passed: 1284 Python tests passed and 3 skipped; lint, frozen provenance, records/schema, exports, offline OAK, governance, history/reviews, report reproducibility, generated site, site contracts and browser regressions succeeded. The 16 source-governance warnings remain visible. |
| Fresh canonical source retention | passed | True | data/cross_mech/cross-mech-duf-examples-2026-10-10.json, data/cross_mech/cross-mech-duf-examples-2026-10-10.manifest.json, data/families/PF18141.yaml, data/families/manifest.json, data/worklists/interpro-pfam-duf-2026-10-10.json, data/worklists/interpro-pfam-duf-2026-10-10.manifest.json, data/worklists/pfam-previous-unknown-names-2026-10-10.json, data/worklists/pfam-previous-unknown-names-2026-10-10.manifest.json | The canonical remote retained 8356 exact source files at 2a9a930b2b5b73c88f7d2d570f9f49c45d3f48c2 via annotated source/dufmech-pr-191-data. |
| Isolated real OAK rejection controls | passed | True | conf/id_labels/pfam.obo, conf/id_labels/provenance.json, exports/kgx/edges.tsv, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv | PASS: 8296 OK_CANONICAL pairs and seven negative/control cases behaved as expected. OAK 0.7.4 ran with networking denied and without importing native DUF modules. |

## Scientific And Domain Assessments

### Bounded source migration without scientific promotion

provenance: supported. Targets: data/cross_mech/cross-mech-duf-examples-2026-10-10.json, data/cross_mech/cross-mech-duf-examples-2026-10-10.manifest.json, data/families/PF18141.yaml, data/families/manifest.json, data/worklists/interpro-pfam-duf-2026-10-10.json, data/worklists/interpro-pfam-duf-2026-10-10.manifest.json, data/worklists/pfam-previous-unknown-names-2026-10-10.json, data/worklists/pfam-previous-unknown-names-2026-10-10.manifest.json.

The retained inputs support precisely the intended PF18141 naming-history correction. Parent rows, source counters and all existing scientific projection fields are conserved; cross-Mech coverage remains explicitly unscanned for the new family.

### Reproducible graph exports and canonical Pfam labels

consistency: supported. Targets: conf/id_labels/pfam.obo, conf/id_labels/provenance.json, exports/kgx/edges.tsv, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv.

Native checks reproduce the complete exports and ID-label artifacts from verified records. The extra family and its InterPro mapping account for the census increase; no curated assertions were invented.

### Historical invariants without blocking future curation

consistency: supported. Targets: tests/test_exports.py, tests/test_pfam_history.py, tests/test_upf1_migration_release.py.

The regression suite verifies the single-row correction and all inherited-row invariants. The issue 190 baseline fix removes the date-dependent false failure, and the isolated PF18141 projection avoids constraining future live scientific curation.

### Source inventory and licensing scope

provenance: supported. Targets: curation/source_queue.tsv, download.yaml.

New artifacts are registered only for their corresponding pipelines. Cross-Mech licensing and acquisition scope are not promoted by an offline compatibility derivation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| lineage | tests/test_upf1_migration_release.py; Four retained-artifact regression tests | supports | The new Pfam table keeps 1834 rows and changes only PF18141 currently_unknown_name. Worklist comparison preserves all 8295 parent rows and adds PF18141. All 16298 cross-Mech rows and original source metadata are identical; PF18141 alone joins the unscanned set. The isolated seed projection remains SEEDED/UNSCORED with no assertions or review pointer. |
| projection-delta | data/families/manifest.json; Parsed comparison of every inherited YAML with git archive 67083dfc2 data/families | supports | 8295 inherited projections match exactly after removing only snapshot_id, path, sha256 and generated_at from provenance. PF18141 is the only added projection. Existing tracked snapshots, histories and reviews have no modified or deleted paths against 67083dfc2. |
| test-fix | tests/test_pfam_history.py; test_report_can_pin_a_pfam_snapshot; GitHub issue 190 | supports | The test now captures the verified current baseline before adding a synthetic next-day snapshot. Both mismatch-by-default and reproducibility-by-explicit-pin assertions pass. Export census expectations match the new 8296-family release; the new seed test builds isolated frozen inputs so future live curation remains possible. |
| local-qc | src/dufmech/qc.py; All COMMANDS executed through just qc; local log /private/tmp/dufmech-pr191-qc.log | supports | The full local run passed against the data checkpoint and first regenerated site. Exports reproduce 16534 nodes and 8238 associations; OAK checks all 8296 Pfam pairs. Browser checks exercise desktop/mobile layouts and source-backed navigation. A separate Chromium check found PF18141 in the EX_DUF catalogue, verified its unscanned label and opened its page without overflow at 1440px and 390px; both screenshots were inspected. |
| governance | curation/source_queue.tsv; interpro_pfam, pfam_previous_ids and cross_mech rows; corresponding download.yaml entries | supports | Only the three relevant source rows adopt new manifests. Cross-Mech remains BLOCKED with UNVERIFIED terms and retains the original scan date; no new scan, relicensing or evidence-of-absence claim is made. Native source governance passes with 16 disclosed warnings. |
| retention | src/dufmech/site_source_publication.py; Fresh canonical check for source/dufmech-pr-191-data | supports | The online gate fetched the fixed canonical repository into a temporary bare clone and verified direct annotated-tag retention plus exact source blobs. The first draft CI failure was the expected old-ledger rejection, not an ignored final check. |

## Limits And Additional Notes

- Same-agent adversarial review, not independent approval or family-level scientific review.
- Cross-Mech licensing remains unverified. Its existing retained data was derived offline without new acquisition, and governance retains 16 warnings.
- Inherited rows were not reclassified under the v3 text classifier. That is a separate later-dated snapshot operation, not part of issue 165 closure.
- The completed local gate predates saving this report. This immutable report needs a final retained checkpoint and Pages regeneration. Final exact-head CI, merge-queue QC and Pages deployment remain release gates; no future success is asserted here.
- Three command-frontmatter parameterizations were skipped because their command-file parameter set is empty (confirmed with pytest -q -rs tests/test_skill_frontmatter.py). No data-validation gate was skipped for that reason. No paid research, new evidence scoring or literature validation was performed.
- Issue 190 records the concrete regression found and corrected during this release. It is linked for PR closure; no speculative cleanup issue was created. Earlier immutable review bundles and source checkpoints remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
kind: repository
repository: CultureBotAI/DUFMech
source:
  git_revision: 2a9a930b2b5b73c88f7d2d570f9f49c45d3f48c2
  inputs:
  - path: conf/id_labels/pfam.obo
    role: target
    sha256: 9abdbbea9bf9497a00d52843e8a00fcd3fcddcef9eabb126a28478b79b79177c
  - path: conf/id_labels/provenance.json
    role: target
    sha256: 1fa8d0890cb9f7d846abbc3336ec0eed5f3833b9e3365ee78a1a6f8a9b1dc2d8
  - path: curation/source_queue.tsv
    role: target
    sha256: 359b2fe7e42974f78c33de209c966d5bf9865451ee714ad226c28eb170a7263e
  - path: data/cross_mech/cross-mech-duf-examples-2026-10-10.json
    role: target
    sha256: 2881f5619286145456b97e4f4df5d032188344d0fad33259b3bbe22ef2dbf99d
  - path: data/cross_mech/cross-mech-duf-examples-2026-10-10.manifest.json
    role: target
    sha256: 6d249ce688aa2166167292b58195e532d573ca1df1cf7af62d4be93351a2029c
  - path: data/families/PF18141.yaml
    role: target
    sha256: 501a5bce46fb02e3f024515f345afb325325750227e7987d1944e246c117ac88
  - path: data/families/manifest.json
    role: target
    sha256: 4860e4371e84861292af75c9c53748afd11fcda6bd48f6dbefe52ce57ed50d56
  - path: data/worklists/interpro-pfam-duf-2026-10-10.json
    role: target
    sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383
  - path: data/worklists/interpro-pfam-duf-2026-10-10.manifest.json
    role: target
    sha256: 31c07ffb6a169c851ea0e6e9dd527a10c04028eafeb29187bd62dc2ae848696e
  - path: data/worklists/interpro-pfam-duf-2026-10-10.tsv
    role: context
    sha256: be023c8dd9d8d3864926b5032d6f7e87a884b1a567391696822dbbecc692dae7
  - path: data/worklists/pfam-previous-unknown-names-2026-10-10.json
    role: target
    sha256: a9f70f265bfe7039f5abf8e8a4545f389b66636edaf8e102c7e1a08ca1c1c10e
  - path: data/worklists/pfam-previous-unknown-names-2026-10-10.manifest.json
    role: target
    sha256: 6cdae618189b4c17a179097754eb81a2daf84b5a21705336f5119481ca0d65e0
  - path: download.yaml
    role: target
    sha256: 0da08721be900a9bfb9b3f707a800ccb352ff9693a1e1fb6ab6daab7c9e11bb9
  - path: exports/kgx/edges.tsv
    role: target
    sha256: 7c5ac1162eb92d57843e10f05f0ee95dcbd83d93a4ce1478628536f914e74679
  - path: exports/kgx/nodes.tsv
    role: target
    sha256: d45edebaef2f1d7d9a0505c89cf37cbd64722f25f9a99ae2fb8aad44af64ecfc
  - path: exports/sssom/dufmech.sssom.tsv
    role: target
    sha256: bcac6604769e2924ba3396d9251ff5ca49ff966cd6187e88a6895fdd9ff1cf59
  - path: tests/test_exports.py
    role: target
    sha256: e9d85d94950863ce9930cb3d402aa972a86ad0523e4e7e852fd91c502571041b
  - path: tests/test_pfam_history.py
    role: target
    sha256: be01b124ecaa0452fa072f41756d1b3fd2c482b5bb2866446235533e68bc3358
  - path: tests/test_upf1_migration_release.py
    role: target
    sha256: b68af44ec295f59374d0fd9af3b67268e5361738efa828ee2500d66a4c6c231f
  snapshot_id: interpro-pfam-duf-2026-10-10
  state: working_tree
targets:
- kind: source
  label: conf/id_labels/pfam.obo
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: conf/id_labels/pfam.obo
  target_id: conf/id_labels/pfam.obo
- kind: source
  label: conf/id_labels/provenance.json
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: conf/id_labels/provenance.json
  target_id: conf/id_labels/provenance.json
- kind: source
  label: curation/source_queue.tsv
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: curation/source_queue.tsv
  target_id: curation/source_queue.tsv
- kind: source
  label: data/cross_mech/cross-mech-duf-examples-2026-10-10.json
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: data/cross_mech/cross-mech-duf-examples-2026-10-10.json
  target_id: data/cross_mech/cross-mech-duf-examples-2026-10-10.json
- kind: source
  label: data/cross_mech/cross-mech-duf-examples-2026-10-10.manifest.json
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: data/cross_mech/cross-mech-duf-examples-2026-10-10.manifest.json
  target_id: data/cross_mech/cross-mech-duf-examples-2026-10-10.manifest.json
- kind: source
  label: data/families/PF18141.yaml
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: data/families/PF18141.yaml
  target_id: data/families/PF18141.yaml
- kind: source
  label: data/families/manifest.json
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: data/families/manifest.json
  target_id: data/families/manifest.json
- kind: source
  label: data/worklists/interpro-pfam-duf-2026-10-10.json
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: data/worklists/interpro-pfam-duf-2026-10-10.json
  target_id: data/worklists/interpro-pfam-duf-2026-10-10.json
- kind: source
  label: data/worklists/interpro-pfam-duf-2026-10-10.manifest.json
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: data/worklists/interpro-pfam-duf-2026-10-10.manifest.json
  target_id: data/worklists/interpro-pfam-duf-2026-10-10.manifest.json
- kind: source
  label: data/worklists/pfam-previous-unknown-names-2026-10-10.json
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: data/worklists/pfam-previous-unknown-names-2026-10-10.json
  target_id: data/worklists/pfam-previous-unknown-names-2026-10-10.json
- kind: source
  label: data/worklists/pfam-previous-unknown-names-2026-10-10.manifest.json
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: data/worklists/pfam-previous-unknown-names-2026-10-10.manifest.json
  target_id: data/worklists/pfam-previous-unknown-names-2026-10-10.manifest.json
- kind: source
  label: download.yaml
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: download.yaml
  target_id: download.yaml
- kind: source
  label: exports/kgx/edges.tsv
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: exports/kgx/edges.tsv
  target_id: exports/kgx/edges.tsv
- kind: source
  label: exports/kgx/nodes.tsv
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: exports/kgx/nodes.tsv
  target_id: exports/kgx/nodes.tsv
- kind: source
  label: exports/sssom/dufmech.sssom.tsv
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: exports/sssom/dufmech.sssom.tsv
  target_id: exports/sssom/dufmech.sssom.tsv
- kind: source
  label: tests/test_exports.py
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: tests/test_exports.py
  target_id: tests/test_exports.py
- kind: source
  label: tests/test_pfam_history.py
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: tests/test_pfam_history.py
  target_id: tests/test_pfam_history.py
- kind: source
  label: tests/test_upf1_migration_release.py
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: tests/test_upf1_migration_release.py
  target_id: tests/test_upf1_migration_release.py
schema_version: 1.0.0
review_id: 20261010T205944Z-pr-191-upf1-release
title: 'PR 191 adversarial audit: retained PF18141 migration and release'
started_at: '2026-10-10T20:32:33Z'
finished_at: '2026-10-10T20:59:44Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: The implementing agent rechecked source deltas, provenance,
    regressions and rendered behavior. No independent reviewer or approval is claimed.
skill: .claude/skills/review-repo/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: false
summary: The scoped issue 165 refresh preserves all 8295 parent worklist rows and
  adds only PF18141. The identical pinned Pfam gzip produces exactly one normalized
  flag correction; cross-Mech evidence and acquisition provenance are unchanged. Issue
  190 tracks the corrected stale-baseline regression. No unresolved correctness finding
  remains in the selected release inputs; cross-Mech terms and scientific interpretation
  remain explicitly outside this approval.
scope:
  description: Release-input audit of the selected frozen snapshots, PF18141 seed
    projection, corpus manifest, exports, ID labels, source governance and regression
    tests. Deterministic comparisons cover every inherited worklist row and projection,
    not scientific review of every family.
  selection: Explicit 18-file source, projection, export and regression surface for
    PR 191.
  coverage: full
  population_size: 18
  reviewed_target_ids:
  - conf/id_labels/pfam.obo
  - conf/id_labels/provenance.json
  - curation/source_queue.tsv
  - data/cross_mech/cross-mech-duf-examples-2026-10-10.json
  - data/cross_mech/cross-mech-duf-examples-2026-10-10.manifest.json
  - data/families/PF18141.yaml
  - data/families/manifest.json
  - data/worklists/interpro-pfam-duf-2026-10-10.json
  - data/worklists/interpro-pfam-duf-2026-10-10.manifest.json
  - data/worklists/pfam-previous-unknown-names-2026-10-10.json
  - data/worklists/pfam-previous-unknown-names-2026-10-10.manifest.json
  - download.yaml
  - exports/kgx/edges.tsv
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - tests/test_exports.py
  - tests/test_pfam_history.py
  - tests/test_upf1_migration_release.py
checks:
- check_id: focused
  name: Migration and lineage regressions
  command: .venv/bin/python -m pytest -q tests/test_pfam_history.py tests/test_exduf.py
    tests/test_exduf_apply.py tests/test_worklist_lineage.py tests/test_cross_mech_lineage.py
    tests/test_upf1_migration_release.py
  summary: 112 tests passed in 29.01 seconds.
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - data/cross_mech/cross-mech-duf-examples-2026-10-10.json
  - data/cross_mech/cross-mech-duf-examples-2026-10-10.manifest.json
  - data/families/PF18141.yaml
  - data/families/manifest.json
  - data/worklists/interpro-pfam-duf-2026-10-10.json
  - data/worklists/interpro-pfam-duf-2026-10-10.manifest.json
  - data/worklists/pfam-previous-unknown-names-2026-10-10.json
  - data/worklists/pfam-previous-unknown-names-2026-10-10.manifest.json
  - tests/test_exports.py
  - tests/test_pfam_history.py
  - tests/test_upf1_migration_release.py
  evidence_ids:
  - lineage
  - test-fix
- check_id: qc
  name: Complete local quality gate
  command: CLAW_SRC=/private/tmp/dufmech-classification-claw/src CLAW_ROOT=/private/tmp/dufmech-classification-claw
    UV_CACHE_DIR=/private/tmp/dufmech-uv-cache PLAYWRIGHT_BROWSERS_PATH=/private/tmp/dufmech-playwright-browsers
    just qc
  summary: 'All local gates passed: 1284 Python tests passed and 3 skipped; lint,
    frozen provenance, records/schema, exports, offline OAK, governance, history/reviews,
    report reproducibility, generated site, site contracts and browser regressions
    succeeded. The 16 source-governance warnings remain visible.'
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - conf/id_labels/pfam.obo
  - conf/id_labels/provenance.json
  - curation/source_queue.tsv
  - data/cross_mech/cross-mech-duf-examples-2026-10-10.json
  - data/cross_mech/cross-mech-duf-examples-2026-10-10.manifest.json
  - data/families/PF18141.yaml
  - data/families/manifest.json
  - data/worklists/interpro-pfam-duf-2026-10-10.json
  - data/worklists/interpro-pfam-duf-2026-10-10.manifest.json
  - data/worklists/pfam-previous-unknown-names-2026-10-10.json
  - data/worklists/pfam-previous-unknown-names-2026-10-10.manifest.json
  - download.yaml
  - exports/kgx/edges.tsv
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - tests/test_exports.py
  - tests/test_pfam_history.py
  - tests/test_upf1_migration_release.py
  evidence_ids:
  - local-qc
- check_id: retention
  name: Fresh canonical source retention
  command: just site-sources-published
  summary: The canonical remote retained 8356 exact source files at 2a9a930b2b5b73c88f7d2d570f9f49c45d3f48c2
    via annotated source/dufmech-pr-191-data.
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - data/cross_mech/cross-mech-duf-examples-2026-10-10.json
  - data/cross_mech/cross-mech-duf-examples-2026-10-10.manifest.json
  - data/families/PF18141.yaml
  - data/families/manifest.json
  - data/worklists/interpro-pfam-duf-2026-10-10.json
  - data/worklists/interpro-pfam-duf-2026-10-10.manifest.json
  - data/worklists/pfam-previous-unknown-names-2026-10-10.json
  - data/worklists/pfam-previous-unknown-names-2026-10-10.manifest.json
  evidence_ids:
  - retention
- check_id: oak-controls
  name: Isolated real OAK rejection controls
  command: CLAW_ROOT=/private/tmp/dufmech-classification-claw UV_CACHE_DIR=/private/tmp/dufmech-uv-cache
    just id-labels-oak-test
  summary: 'PASS: 8296 OK_CANONICAL pairs and seven negative/control cases behaved
    as expected. OAK 0.7.4 ran with networking denied and without importing native
    DUF modules.'
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - conf/id_labels/pfam.obo
  - conf/id_labels/provenance.json
  - exports/kgx/edges.tsv
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  evidence_ids:
  - local-qc
evidence:
- evidence_id: lineage
  kind: validation
  reference: tests/test_upf1_migration_release.py
  locator: Four retained-artifact regression tests
  accessed_at: '2026-10-10T20:59:44Z'
  support: supports
  summary: The new Pfam table keeps 1834 rows and changes only PF18141 currently_unknown_name.
    Worklist comparison preserves all 8295 parent rows and adds PF18141. All 16298
    cross-Mech rows and original source metadata are identical; PF18141 alone joins
    the unscanned set. The isolated seed projection remains SEEDED/UNSCORED with no
    assertions or review pointer.
- evidence_id: projection-delta
  kind: validation
  reference: data/families/manifest.json
  locator: Parsed comparison of every inherited YAML with git archive 67083dfc2 data/families
  accessed_at: '2026-10-10T20:59:44Z'
  support: supports
  summary: 8295 inherited projections match exactly after removing only snapshot_id,
    path, sha256 and generated_at from provenance. PF18141 is the only added projection.
    Existing tracked snapshots, histories and reviews have no modified or deleted
    paths against 67083dfc2.
- evidence_id: test-fix
  kind: record_content
  reference: tests/test_pfam_history.py
  locator: test_report_can_pin_a_pfam_snapshot; GitHub issue 190
  accessed_at: '2026-10-10T20:59:44Z'
  support: supports
  summary: The test now captures the verified current baseline before adding a synthetic
    next-day snapshot. Both mismatch-by-default and reproducibility-by-explicit-pin
    assertions pass. Export census expectations match the new 8296-family release;
    the new seed test builds isolated frozen inputs so future live curation remains
    possible.
- evidence_id: local-qc
  kind: validation
  reference: src/dufmech/qc.py
  locator: All COMMANDS executed through just qc; local log /private/tmp/dufmech-pr191-qc.log
  accessed_at: '2026-10-10T20:59:44Z'
  support: supports
  summary: The full local run passed against the data checkpoint and first regenerated
    site. Exports reproduce 16534 nodes and 8238 associations; OAK checks all 8296
    Pfam pairs. Browser checks exercise desktop/mobile layouts and source-backed navigation.
    A separate Chromium check found PF18141 in the EX_DUF catalogue, verified its
    unscanned label and opened its page without overflow at 1440px and 390px; both
    screenshots were inspected.
- evidence_id: governance
  kind: record_content
  reference: curation/source_queue.tsv
  locator: interpro_pfam, pfam_previous_ids and cross_mech rows; corresponding download.yaml
    entries
  accessed_at: '2026-10-10T20:59:44Z'
  support: supports
  summary: Only the three relevant source rows adopt new manifests. Cross-Mech remains
    BLOCKED with UNVERIFIED terms and retains the original scan date; no new scan,
    relicensing or evidence-of-absence claim is made. Native source governance passes
    with 16 disclosed warnings.
- evidence_id: retention
  kind: validation
  reference: src/dufmech/site_source_publication.py
  locator: Fresh canonical check for source/dufmech-pr-191-data
  accessed_at: '2026-10-10T20:59:44Z'
  support: supports
  summary: The online gate fetched the fixed canonical repository into a temporary
    bare clone and verified direct annotated-tag retention plus exact source blobs.
    The first draft CI failure was the expected old-ledger rejection, not an ignored
    final check.
assessments:
- assessment_id: data-integrity
  area: provenance
  topic: Bounded source migration without scientific promotion
  outcome: supported
  summary: The retained inputs support precisely the intended PF18141 naming-history
    correction. Parent rows, source counters and all existing scientific projection
    fields are conserved; cross-Mech coverage remains explicitly unscanned for the
    new family.
  target_ids:
  - data/cross_mech/cross-mech-duf-examples-2026-10-10.json
  - data/cross_mech/cross-mech-duf-examples-2026-10-10.manifest.json
  - data/families/PF18141.yaml
  - data/families/manifest.json
  - data/worklists/interpro-pfam-duf-2026-10-10.json
  - data/worklists/interpro-pfam-duf-2026-10-10.manifest.json
  - data/worklists/pfam-previous-unknown-names-2026-10-10.json
  - data/worklists/pfam-previous-unknown-names-2026-10-10.manifest.json
  evidence_ids:
  - lineage
  - projection-delta
- assessment_id: export-integrity
  area: consistency
  topic: Reproducible graph exports and canonical Pfam labels
  outcome: supported
  summary: Native checks reproduce the complete exports and ID-label artifacts from
    verified records. The extra family and its InterPro mapping account for the census
    increase; no curated assertions were invented.
  target_ids:
  - conf/id_labels/pfam.obo
  - conf/id_labels/provenance.json
  - exports/kgx/edges.tsv
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  evidence_ids:
  - local-qc
  - projection-delta
- assessment_id: regression-safety
  area: consistency
  topic: Historical invariants without blocking future curation
  outcome: supported
  summary: The regression suite verifies the single-row correction and all inherited-row
    invariants. The issue 190 baseline fix removes the date-dependent false failure,
    and the isolated PF18141 projection avoids constraining future live scientific
    curation.
  target_ids:
  - tests/test_exports.py
  - tests/test_pfam_history.py
  - tests/test_upf1_migration_release.py
  evidence_ids:
  - lineage
  - test-fix
  - local-qc
- assessment_id: source-boundaries
  area: provenance
  topic: Source inventory and licensing scope
  outcome: supported
  summary: New artifacts are registered only for their corresponding pipelines. Cross-Mech
    licensing and acquisition scope are not promoted by an offline compatibility derivation.
  target_ids:
  - curation/source_queue.tsv
  - download.yaml
  evidence_ids:
  - governance
findings: []
actions: []
limitations:
- Same-agent adversarial review, not independent approval or family-level scientific
  review.
- Cross-Mech licensing remains unverified. Its existing retained data was derived
  offline without new acquisition, and governance retains 16 warnings.
- Inherited rows were not reclassified under the v3 text classifier. That is a separate
  later-dated snapshot operation, not part of issue 165 closure.
- The completed local gate predates saving this report. This immutable report needs
  a final retained checkpoint and Pages regeneration. Final exact-head CI, merge-queue
  QC and Pages deployment remain release gates; no future success is asserted here.
- Three command-frontmatter parameterizations were skipped because their command-file
  parameter set is empty (confirmed with pytest -q -rs tests/test_skill_frontmatter.py).
  No data-validation gate was skipped for that reason. No paid research, new evidence
  scoring or literature validation was performed.
notes:
- Issue 190 records the concrete regression found and corrected during this release.
  It is linked for PR closure; no speculative cleanup issue was created. Earlier immutable
  review bundles and source checkpoints remain unchanged.
links:
- https://github.com/CultureBotAI/DUFMech/pull/191
- https://github.com/CultureBotAI/DUFMech/issues/165
- https://github.com/CultureBotAI/DUFMech/issues/190
tags:
- migration
- provenance
- release
- self-review
```
