---
context:
  kind: repo
  members: []
  record_digests: {}
  scope_paths:
  - docs/records.md
  - src/dufmech/cross_mech_report.py
  - src/dufmech/cross_mech_snapshot.py
  - src/dufmech/provenance.py
  - src/dufmech/score_inputs.py
  - src/dufmech/worklist_lineage.py
  - tests/test_cross_mech_lineage.py
  - tests/test_exduf_apply.py
  - tests/test_worklist_lineage.py
  selection: ''
  slug: worklist-parent-and-alias-provenance
  snapshot_id: interpro-pfam-duf-2026-10-08
  source_files:
    data/worklists/interpro-pfam-duf-2026-10-08.json: 9f0992961c30c5d92343a92aab000cd20b6c4213952b4c68408c3065779a46ec
    data/worklists/interpro-pfam-duf-2026-10-08.manifest.json: 5929010740007a44480dac1fe804840b5885e131bceccc3043dbcb9146e991d5
    data/worklists/interpro-pfam-duf-2026-10-08.tsv: 3d873968fcb87babafe59c01722c0d914f4ddc45de28cb8de4595477c353f91b
    docs/records.md: 40ef5a2322143c112290c47c6b541d9c1ce60a5d82927ff84dea6322b71e2d78
    src/dufmech/cross_mech_report.py: 36480cd2747caca579fd8698be9ef5dfe64aeb6832bb37cab941e90cdfb13399
    src/dufmech/cross_mech_snapshot.py: 5cd0085781d625a7c7feddd0252cbc6cadb0fa27974113fd8b26e336e64297ad
    src/dufmech/provenance.py: b86cf7b26beef9e1a200fd3c8969ebcadaf62e728fdf2fb4f0ef426b0d9d8c1d
    src/dufmech/score_inputs.py: 74aa066d61d443133f48554fbbcebecd7f46d68650d88c7f1b6de53ac87ef342
    src/dufmech/worklist_lineage.py: a6a198d3019596fd8873137a6d1573a114be6cf84f4df6da2dec2af58154b2c0
    tests/test_cross_mech_lineage.py: 89fe4cc5a170be11e74007c6c37601b0743c399c5f5ff5f3e1195a8712564aa6
    tests/test_exduf_apply.py: 6d5ddb532b3f9d617b63d6ed4bb05aab4e58f60e1cdef2af821ffdc44aebf906
    tests/test_worklist_lineage.py: d922c4888087708b35aa165e6d4382b8f7deb3a504c4bf5bd4079caa137ebb15
  source_revision: 58aff1a53041689fba79c872c35fbb6c57f87458
  source_state: working_tree
  targets:
  - id: docs/records.md
    locator: docs/records.md
  - id: src/dufmech/cross_mech_report.py
    locator: src/dufmech/cross_mech_report.py
  - id: src/dufmech/cross_mech_snapshot.py
    locator: src/dufmech/cross_mech_snapshot.py
  - id: src/dufmech/provenance.py
    locator: src/dufmech/provenance.py
  - id: src/dufmech/score_inputs.py
    locator: src/dufmech/score_inputs.py
  - id: src/dufmech/worklist_lineage.py
    locator: src/dufmech/worklist_lineage.py
  - id: tests/test_cross_mech_lineage.py
    locator: tests/test_cross_mech_lineage.py
  - id: tests/test_exduf_apply.py
    locator: tests/test_exduf_apply.py
  - id: tests/test_worklist_lineage.py
    locator: tests/test_worklist_lineage.py
started_utc: '2026-10-08T07:42:45Z'
finished_utc: '2026-10-08T07:54:22Z'
verdict: PASS
reviewer: Codex
review_scope: 'Adversarial implementation review of local fixes for DUFMech #156 and
  #176: parent-row verification in scoring/report loaders and preservation of former-name
  provenance across cross-Mech derivations. No scientific family review, new source
  ingestion, or corpus adoption.'
scientific_review: false
review_version: 1
status: saved
---

# Repository Review: worklist-parent-and-alias-provenance

- Repository: CultureBotAI/DUFMech
- Repo: worklist-parent-and-alias-provenance
- Source revision: `58aff1a53041689fba79c872c35fbb6c57f87458` (working-tree hashes in metadata)
- Snapshot ID: `interpro-pfam-duf-2026-10-08`
- Started UTC: 2026-10-08T07:42:45Z
- Finished UTC: 2026-10-08T07:54:22Z
- Verdict: PASS
- Scientific review: false
- Reviewer: Codex
- Review scope: Adversarial implementation review of local fixes for DUFMech #156 and #176: parent-row verification in scoring/report loaders and preservation of former-name provenance across cross-Mech derivations. No scientific family review, new source ingestion, or corpus adoption.
- Record locator: `docs/records.md`
- Record locator: `src/dufmech/cross_mech_report.py`
- Record locator: `src/dufmech/cross_mech_snapshot.py`
- Record locator: `src/dufmech/provenance.py`
- Record locator: `src/dufmech/score_inputs.py`
- Record locator: `src/dufmech/worklist_lineage.py`
- Record locator: `tests/test_cross_mech_lineage.py`
- Record locator: `tests/test_exduf_apply.py`
- Record locator: `tests/test_worklist_lineage.py`

## Target Repository

CultureBotAI/DUFMech, base revision 58aff1a53041689fba79c872c35fbb6c57f87458. Implementation worktree /private/tmp/dufmech-classification-release-guards, branch fix/classification-release-guards. This report is retained in the separate sparse audit worktree /private/tmp/dufmech-classification-audit. All 16 changed implementation files, including the three new modules/test files and the preceding classification batch, were compared byte-for-byte with the audit copy. The nine paths listed in context are this review's scope.

## Scope and Selection

Reviewed issue https://github.com/CultureBotAI/DUFMech/issues/156 and https://github.com/CultureBotAI/DUFMech/issues/176 against their native producers, verified-input consumers, manifest checks, ancestor traversal, report rendering, regression fixtures and frozen data. Read the changed code and surrounding exduf/reclassification/report behavior. Searched src, tests and docs for alias-provenance consumers with rg --no-ignore --hidden, including ignored files within those directories. This is a scoped tooling audit, not certification of unrelated repository behavior.

## Validation

The complete just qc command passed all sixteen gates: lint, tests, documentation, nine frozen snapshot manifests, corpus report, 8,295 schema-valid records with zero generated-file drift, offline research profile, byte-reproducible KGX/SSSOM exports, isolated OAK correspondence for all 8,295 Pfam ID/name pairs, source governance, five existing review reports, two existing history records, cross-Mech report, generated site, site contract/budgets and all six Playwright browser tests. The full Python run passed 1,178 tests with three existing empty-parameter skips and one upstream SSSOM/LinkML deprecation warning. A final malformed-snapshot guard was added after that suite began; all 193 affected tests were then rerun on the final source and passed, including the six new malformed-input cases. Final Ruff and git diff --check passed. Source governance retains zero errors and 15 existing licensing/adoption warnings. The existing cross-Mech report remains byte-current. QC ran with localhost permission for Playwright and the separately locked pinned CLAW runtime; no gate was bypassed.

## Identity and Grounding

The shared worklist validator reads only safe, date-shaped direct-parent filenames, rejects symlinks and non-regular files, and verifies byte size and SHA-256 before comparing the captured rows. Reclassification preserves exactly the parent's family membership and non-classification metadata and checks its change summary. Migration verifies retained membership, metadata, declared additions, carries, refreshes, live-new families and before/after changes against the available original/live parents. Tests alter child metadata and recompute its own hashes to prove that self-consistent child manifests do not evade the parent comparison.

## Evidence

Cross-Mech chains preserve the inherited alias-to-Pfam mapping and the original previous-name snapshot ID and hash, whether the next derivation omits or repeats --previous-names-json. Legacy single-source manifests normalize without changing the retained corpus. Multiple contributing Pfam snapshots retain separate source records and the report cites the contributing snapshots without falsely assigning old resolutions to a newer release. Mapping/count discrepancies, missing inherited mappings, conflicting maps and reuse of a snapshot identity with different bytes stop before writing a new derivation. Ambiguity history is retained per source while resolved names leave the active ambiguity list.

## Completeness

The local code addresses the two scoped provenance defects. All 41 new parametrized tests in test_worklist_lineage.py and test_cross_mech_lineage.py are covered by the final 193-test rerun. Portability remains intentional: absent parent JSON cannot be content-compared, and a declared but unavailable live parent limits refresh replay. Direct-parent validation does not require every grandparent; existing lazy ancestry tests still pass. Added/carried rows that were explicitly fetched are not misrepresented as copied parent metadata. This does not re-execute scientific classification, authenticate external assertions, or recover an alias already lost by an earlier malformed artifact.

## Findings

No remaining blocking defect found in the reviewed scope. The adversarial pass found a raw-exception regression for a malformed non-object snapshot field in the new shared validator; the guard was corrected and null/list/string snapshot and parent-ID cases now return validation errors through both consumers. The prior review's #156/#176 follow-ups are addressed locally by this batch, but the GitHub issues remain open until publication. Existing source licensing/adoption warnings and source-pin workflow limitations are outside this fix.

## Recommended Edits

Keep the fixes scoped to provenance validation, deterministic chain bookkeeping, focused regression tests and rollout documentation. Preserve the frozen snapshots, generated family records, exports and Pages. Retain this append-only audit separately until publication can use a reachable source checkpoint and correct site pins; do not change the old report or bypass the pin gates.

## Follow-up Checks

Commit and publish only under the user's shipping workflow, with fresh checks and PR review before merge. A later corpus update still needs a newly frozen Pfam previous-name table, migration and v3 reclassification using actual acquisition dates; each worklist derivation must be later than its parent. Regenerate compatible cross-Mech artifacts and review the changes before publishing scores, records, exports and Pages. The evidence-backed 10-20-family pilot remains future scientific work. Missing external parents and provider availability were not certified.

## Additional Notes

This report supplements reports/repo_review/20261008T071432Z-classification-release-guards.md; it does not rewrite that historical assessment or promote any family to REVIEWED. The corpus remains 8,295 SEEDED/UNSCORED families, with no new ingestion or curated claims in this batch. The original shared checkout and its unrelated untracked .claude/hooks and .claude/settings.json were preserved. No commit, push, PR, merge, issue closure or branch deletion was performed. Source hashes describe actual uncommitted working-tree bytes, not a published revision.
