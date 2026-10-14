# PR 199 causal-graph inventory remediation

- Review: 20261014T195307Z-causal-graph-pr-resolution
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-14T19:48:26Z
- Finished UTC: 2026-10-14T19:53:07Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Issue 198 is resolved in the inspected working tree. The native inventory command now checks every current family against retained bytes without writing, and explicit refresh uses the established locked, no-follow, concurrent-edit-preserving writer. QC invokes the read-only gate. Focused tests pass and all 8,296 real inventory rows verify. Final source retention, Pages, full QC and exact-head CI remain required release checks.

## Scope And Provenance

Reassessed the same nine implementation, test and inventory targets after the issue-198 fix, including combined graph/protein-example rendering and new browser test construction.

Selection: Graph data contract, projection/evidence validation, renderer integration and coverage verification boundaries.
Coverage: full; 9 reviewed / 9 in the declared population.
Source: working_tree at Git base 48012e1f00b385d0f387c3c04789a5d9fcad133f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| reports/causal_graphs/inventory.json | reports/causal_graphs/inventory.json | source | reports/causal_graphs/inventory.json |
| src/dufmech/causal_graphs.py | src/dufmech/causal_graphs.py | source | src/dufmech/causal_graphs.py |
| src/dufmech/qc.py | src/dufmech/qc.py | source | src/dufmech/qc.py |
| src/dufmech/records.py | src/dufmech/records.py | source | src/dufmech/records.py |
| src/dufmech/schema/dufmech.yaml | src/dufmech/schema/dufmech.yaml | source | src/dufmech/schema/dufmech.yaml |
| src/dufmech/site.py | src/dufmech/site.py | source | src/dufmech/site.py |
| tests/site_browser.cjs | tests/site_browser.cjs | source | tests/site_browser.cjs |
| tests/test_causal_graphs.py | tests/test_causal_graphs.py | source | tests/test_causal_graphs.py |
| tests/test_qc.py | tests/test_qc.py | source | tests/test_qc.py |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Graph and QC regression suite | passed | True | reports/causal_graphs/inventory.json, src/dufmech/causal_graphs.py, src/dufmech/qc.py, src/dufmech/records.py, src/dufmech/schema/dufmech.yaml, src/dufmech/site.py, tests/site_browser.cjs, tests/test_causal_graphs.py, tests/test_qc.py | 52 passed in 32.53 seconds. |
| Retained production inventory | passed | True | reports/causal_graphs/inventory.json, src/dufmech/causal_graphs.py | Verified 8,296 family inventory rows without regenerating the already-current report. |
| Ruff source validation | passed | True | reports/causal_graphs/inventory.json, src/dufmech/causal_graphs.py, src/dufmech/qc.py, src/dufmech/records.py, src/dufmech/schema/dufmech.yaml, src/dufmech/site.py, tests/site_browser.cjs, tests/test_causal_graphs.py, tests/test_qc.py | All checks passed. |
| Source and writer governance | passed | True | src/dufmech/causal_graphs.py | Zero errors; 16 existing source-license warnings remain, unrelated to the new writer. |

## Scientific And Domain Assessments

### Inventory regeneration and verification

provenance: supported. Targets: reports/causal_graphs/inventory.json, src/dufmech/causal_graphs.py, src/dufmech/qc.py, src/dufmech/records.py, src/dufmech/schema/dufmech.yaml, src/dufmech/site.py, tests/site_browser.cjs, tests/test_causal_graphs.py, tests/test_qc.py.

The concrete stale-inventory failure is covered by a read-only check in QC and guarded explicit regeneration. Scope, evidence and review-status semantics remain unchanged; rendered page integration retains both feature sets.

## Findings

### inventory-drift: Retained causal coverage inventory can become stale without a failing gate

minor / resolved / confirmed; issue key: DUFMech-198.

The generated report records counts and semantic digests, but main only prints a newly computed inventory and QC never compares it with the saved artifact. Later graph curation can therefore publish stale coverage metadata.

Disposition: The check now rejects absent/stale bytes, runs in QC and verifies all production digests. Regression tests demonstrate no-write check behavior and safe explicit refresh.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| regressions | tests/test_causal_graphs.py; Inventory CLI, missing/stale bytes, semantic-digest changes, no-write check, symlinks, directory destinations, conflicting modes and concurrent edits; tests/test_qc.py inventory wiring | supports | 52 focused tests pass. Default output and --check do not write; explicit apply preserves displaced concurrent content and rejects unsafe paths. |
| production | reports/causal_graphs/inventory.json; All 8,296 rows and aggregate graph_states | supports | The report matches freshly validated native records byte-for-byte: 124 PRESENT and 8,172 ABSENT. Those are structural states, not scientific review completion. |
| implementation | src/dufmech/causal_graphs.py; write_inventory/main, qc.COMMANDS, closed schema and evidence validation, site.curated_graphs and new browser scenario | supports | Reviewed explicit mode selection, native validation, safe-path and writer-lock reuse, atomic publication with recovery, QC ordering, graph evidence and scope labels, and simultaneous graph/protein-example sections. Browser execution and final publication remain release gates. |

## Limits And Additional Notes

- Adversarial self-review, not an independent approval or a new literature review of all graph edges.
- All 130 curated families remain IN_PROGRESS. Six are scoped graphless assessments; another 8,166 families have not received this curation. Existing per-family scientific follow-ups remain open.
- Full QC, browser execution, source checkpoint retention, generated Pages and exact-head CI are separate release gates still pending at this review timestamp.
- Advisory writer locking and recovery protect cooperating writers and observed concurrent edits, not every malicious filesystem race.
- Sixteen pre-existing source-governance license warnings remain visible; no new source acquisition or blanket licensing claim was made.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T195307Z-causal-graph-pr-resolution
kind: repository
repository: CultureBotAI/DUFMech
source:
  git_revision: 48012e1f00b385d0f387c3c04789a5d9fcad133f
  inputs:
  - path: data/worklists/interpro-pfam-duf-2026-10-10.json
    role: context
    sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383
  - path: data/worklists/interpro-pfam-duf-2026-10-10.manifest.json
    role: context
    sha256: 31c07ffb6a169c851ea0e6e9dd527a10c04028eafeb29187bd62dc2ae848696e
  - path: data/worklists/interpro-pfam-duf-2026-10-10.tsv
    role: context
    sha256: be023c8dd9d8d3864926b5032d6f7e87a884b1a567391696822dbbecc692dae7
  - path: reports/causal_graphs/inventory.json
    role: target
    sha256: 7ddc0359fb29851656e67c46785ba94bd863dc9ef9254f6da129a5f600b1b18f
  - path: src/dufmech/causal_graphs.py
    role: target
    sha256: 720765571fda119ed7ec971a0fb9f49270c348d908aa210f31bb35089f893a9b
  - path: src/dufmech/qc.py
    role: target
    sha256: e75e5080000578ef5b794147fbd138810de552da9eb241d2cb7612322c093d6e
  - path: src/dufmech/records.py
    role: target
    sha256: 929362c8289eaeb0098ffd23d668e25305d9df83bf1154f3f5919e8d3103ba5c
  - path: src/dufmech/schema/dufmech.yaml
    role: target
    sha256: 5ca9b9cd1fdefdbe8066b08c319b5144a5f2631710f2271e84dc346283b608e9
  - path: src/dufmech/site.py
    role: target
    sha256: 3d60ee72f88ca48153148a155a454c21b5da663d2ffd8931d7d00e948bd6cbfb
  - path: tests/site_browser.cjs
    role: target
    sha256: 81f8a7476c20e172ef140d1a75dc925347f42fe7e8b986ff24858a15c417868d
  - path: tests/test_causal_graphs.py
    role: target
    sha256: 2fe4e7e91fd1aa73d755d64f7e6398bc53ec8a6400eedc8318da190f079f3cef
  - path: tests/test_qc.py
    role: target
    sha256: 2207d06775011e0b60ff8d989aef1056cb2ae8b8a3f7318587c9618a7e5e2edf
  snapshot_id: interpro-pfam-duf-2026-10-10
  state: working_tree
targets:
- kind: source
  label: reports/causal_graphs/inventory.json
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: reports/causal_graphs/inventory.json
  target_id: reports/causal_graphs/inventory.json
- kind: source
  label: src/dufmech/causal_graphs.py
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: src/dufmech/causal_graphs.py
  target_id: src/dufmech/causal_graphs.py
- kind: source
  label: src/dufmech/qc.py
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: src/dufmech/qc.py
  target_id: src/dufmech/qc.py
- kind: source
  label: src/dufmech/records.py
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: src/dufmech/records.py
  target_id: src/dufmech/records.py
- kind: source
  label: src/dufmech/schema/dufmech.yaml
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: src/dufmech/schema/dufmech.yaml
  target_id: src/dufmech/schema/dufmech.yaml
- kind: source
  label: src/dufmech/site.py
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: src/dufmech/site.py
  target_id: src/dufmech/site.py
- kind: source
  label: tests/site_browser.cjs
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: tests/site_browser.cjs
  target_id: tests/site_browser.cjs
- kind: source
  label: tests/test_causal_graphs.py
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: tests/test_causal_graphs.py
  target_id: tests/test_causal_graphs.py
- kind: source
  label: tests/test_qc.py
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: tests/test_qc.py
  target_id: tests/test_qc.py
title: PR 199 causal-graph inventory remediation
started_at: '2026-10-14T19:48:26Z'
finished_at: '2026-10-14T19:53:07Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: The publishing agent inspected existing implementation and challenged
    validation and publication boundaries. No independent approval is claimed.
skill: .claude/skills/review-repo/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: false
summary: Issue 198 is resolved in the inspected working tree. The native inventory
  command now checks every current family against retained bytes without writing,
  and explicit refresh uses the established locked, no-follow, concurrent-edit-preserving
  writer. QC invokes the read-only gate. Focused tests pass and all 8,296 real inventory
  rows verify. Final source retention, Pages, full QC and exact-head CI remain required
  release checks.
scope:
  description: Reassessed the same nine implementation, test and inventory targets
    after the issue-198 fix, including combined graph/protein-example rendering and
    new browser test construction.
  selection: Graph data contract, projection/evidence validation, renderer integration
    and coverage verification boundaries.
  coverage: full
  population_size: 9
  reviewed_target_ids:
  - reports/causal_graphs/inventory.json
  - src/dufmech/causal_graphs.py
  - src/dufmech/qc.py
  - src/dufmech/records.py
  - src/dufmech/schema/dufmech.yaml
  - src/dufmech/site.py
  - tests/site_browser.cjs
  - tests/test_causal_graphs.py
  - tests/test_qc.py
  exclusions:
  - target: Scientific literature for 8,296 families
    reason: This implementation audit does not repeat or replace the retained per-family
      scientific reviews.
  - target: Final publication artifacts and CI
    reason: Source checkpoint, final Pages and exact-head checks must follow remediation.
checks:
- check_id: focused
  name: Graph and QC regression suite
  status: passed
  required: true
  target_ids:
  - reports/causal_graphs/inventory.json
  - src/dufmech/causal_graphs.py
  - src/dufmech/qc.py
  - src/dufmech/records.py
  - src/dufmech/schema/dufmech.yaml
  - src/dufmech/site.py
  - tests/site_browser.cjs
  - tests/test_causal_graphs.py
  - tests/test_qc.py
  command: PYTHONPATH=src:/private/tmp/dufmech-protein-claw/src .venv/bin/python -m
    pytest -q tests/test_causal_graphs.py tests/test_qc.py
  exit_code: 0
  summary: 52 passed in 32.53 seconds.
  evidence_ids:
  - regressions
- check_id: production
  name: Retained production inventory
  status: passed
  required: true
  target_ids:
  - reports/causal_graphs/inventory.json
  - src/dufmech/causal_graphs.py
  command: PYTHONPATH=src .venv/bin/python -m dufmech.causal_graphs --check
  exit_code: 0
  summary: Verified 8,296 family inventory rows without regenerating the already-current
    report.
  evidence_ids:
  - production
- check_id: lint
  name: Ruff source validation
  status: passed
  required: true
  target_ids:
  - reports/causal_graphs/inventory.json
  - src/dufmech/causal_graphs.py
  - src/dufmech/qc.py
  - src/dufmech/records.py
  - src/dufmech/schema/dufmech.yaml
  - src/dufmech/site.py
  - tests/site_browser.cjs
  - tests/test_causal_graphs.py
  - tests/test_qc.py
  command: .venv/bin/python -m ruff check src scripts tests
  exit_code: 0
  summary: All checks passed.
  evidence_ids:
  - implementation
- check_id: writer-policy
  name: Source and writer governance
  status: passed
  required: true
  target_ids:
  - src/dufmech/causal_graphs.py
  command: PYTHONPATH=src .venv/bin/python -m dufmech.source_governance
  exit_code: 0
  summary: Zero errors; 16 existing source-license warnings remain, unrelated to the
    new writer.
  evidence_ids:
  - implementation
evidence:
- evidence_id: regressions
  kind: validation
  reference: tests/test_causal_graphs.py
  locator: Inventory CLI, missing/stale bytes, semantic-digest changes, no-write check,
    symlinks, directory destinations, conflicting modes and concurrent edits; tests/test_qc.py
    inventory wiring
  accessed_at: '2026-10-14T19:53:07Z'
  support: supports
  summary: 52 focused tests pass. Default output and --check do not write; explicit
    apply preserves displaced concurrent content and rejects unsafe paths.
- evidence_id: production
  kind: validation
  reference: reports/causal_graphs/inventory.json
  locator: All 8,296 rows and aggregate graph_states
  accessed_at: '2026-10-14T19:53:07Z'
  support: supports
  summary: 'The report matches freshly validated native records byte-for-byte: 124
    PRESENT and 8,172 ABSENT. Those are structural states, not scientific review completion.'
- evidence_id: implementation
  kind: record_content
  reference: src/dufmech/causal_graphs.py
  locator: write_inventory/main, qc.COMMANDS, closed schema and evidence validation,
    site.curated_graphs and new browser scenario
  accessed_at: '2026-10-14T19:53:07Z'
  support: supports
  summary: Reviewed explicit mode selection, native validation, safe-path and writer-lock
    reuse, atomic publication with recovery, QC ordering, graph evidence and scope
    labels, and simultaneous graph/protein-example sections. Browser execution and
    final publication remain release gates.
assessments:
- assessment_id: coverage
  area: provenance
  topic: Inventory regeneration and verification
  outcome: supported
  target_ids:
  - reports/causal_graphs/inventory.json
  - src/dufmech/causal_graphs.py
  - src/dufmech/qc.py
  - src/dufmech/records.py
  - src/dufmech/schema/dufmech.yaml
  - src/dufmech/site.py
  - tests/site_browser.cjs
  - tests/test_causal_graphs.py
  - tests/test_qc.py
  evidence_ids:
  - regressions
  - production
  - implementation
  summary: The concrete stale-inventory failure is covered by a read-only check in
    QC and guarded explicit regeneration. Scope, evidence and review-status semantics
    remain unchanged; rendered page integration retains both feature sets.
findings:
- finding_id: inventory-drift
  issue_key: DUFMech-198
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Retained causal coverage inventory can become stale without a failing gate
  description: The generated report records counts and semantic digests, but main
    only prints a newly computed inventory and QC never compares it with the saved
    artifact. Later graph curation can therefore publish stale coverage metadata.
  target_ids:
  - src/dufmech/causal_graphs.py
  - src/dufmech/qc.py
  - tests/test_causal_graphs.py
  - tests/test_qc.py
  - reports/causal_graphs/inventory.json
  field_paths:
  - main
  - COMMANDS
  - families[].record_digest
  evidence_ids:
  - regressions
  - production
  - implementation
  ownership_note: Fix native causal_graphs CLI, QC wiring and regression tests; do
    not alter scientific records to fit an old inventory.
  external_issues:
  - https://github.com/CultureBotAI/DUFMech/issues/198
  disposition_reason: The check now rejects absent/stale bytes, runs in QC and verifies
    all production digests. Regression tests demonstrate no-write check behavior and
    safe explicit refresh.
  previous_occurrences:
  - repository: CultureBotAI/DUFMech
    review_id: 20261014T195205Z-causal-graph-pr-baseline
    finding_id: inventory-drift
actions: []
limitations:
- Adversarial self-review, not an independent approval or a new literature review
  of all graph edges.
- All 130 curated families remain IN_PROGRESS. Six are scoped graphless assessments;
  another 8,166 families have not received this curation. Existing per-family scientific
  follow-ups remain open.
- Full QC, browser execution, source checkpoint retention, generated Pages and exact-head
  CI are separate release gates still pending at this review timestamp.
- Advisory writer locking and recovery protect cooperating writers and observed concurrent
  edits, not every malicious filesystem race.
- Sixteen pre-existing source-governance license warnings remain visible; no new source
  acquisition or blanket licensing claim was made.
links:
- https://github.com/CultureBotAI/DUFMech/pull/199
- https://github.com/CultureBotAI/DUFMech/issues/198
tags:
- causal-graphs
- adversarial-review
```
