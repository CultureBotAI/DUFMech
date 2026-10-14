# PR 199 causal-graph adversarial baseline

- Review: 20261014T195205Z-causal-graph-pr-baseline
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-14T19:45:05Z
- Finished UTC: 2026-10-14T19:52:05Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

The committed baseline preserves graph scope, evidence validation and review digests, but the retained structural inventory is outside QC. Issue 198 tracks this confirmed reporting-drift gap. Publication and full QC remain separate release gates.

## Scope And Provenance

Nine selected implementation, schema, rendering, test and inventory paths after integrating current main.

Selection: Graph data contract, projection/evidence validation, renderer integration and coverage verification boundaries.
Coverage: full; 9 reviewed / 9 in the declared population.
Source: git_commit at Git base 48012e1f00b385d0f387c3c04789a5d9fcad133f.
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
| Initial graph, records and exports regression suite | passed | True | src/dufmech/records.py, tests/test_causal_graphs.py | 132 passed before integrating the two existing main commits; this is not final exact-head QC. |
| Retained inventory check is unavailable in baseline | passed | True | src/dufmech/causal_graphs.py, src/dufmech/qc.py, tests/test_causal_graphs.py, tests/test_qc.py, reports/causal_graphs/inventory.json | Argparse rejects --check; static inspection confirms the committed report has no QC consumer. This is reproduction evidence, not a successful inventory gate. |

## Scientific And Domain Assessments

### Retained structural coverage reproducibility

provenance: concern. Targets: src/dufmech/causal_graphs.py, src/dufmech/qc.py, tests/test_causal_graphs.py, tests/test_qc.py, reports/causal_graphs/inventory.json.

The inventory content is explicitly structural, but no native command or QC gate detects stale counts, membership or semantic digests.

### Graph evidence and publication semantics

scope: supported. Targets: src/dufmech/records.py, src/dufmech/schema/dufmech.yaml, src/dufmech/site.py, tests/site_browser.cjs.

Closed-schema projection and evidence checks preserve graph scope, support labels and direction; status promotion remains gated separately. Renderer integration retains both graphs and protein examples. Browser coverage for the combined page is a follow-up release check.

## Findings

### inventory-drift: Retained causal coverage inventory can become stale without a failing gate

minor / open / confirmed; issue key: DUFMech-198.

The generated report records counts and semantic digests, but main only prints a newly computed inventory and QC never compares it with the saved artifact. Later graph curation can therefore publish stale coverage metadata.

## Recommended Actions And Acceptance Checks

### guard-inventory

Add read-only --check, explicit guarded --apply, QC wiring and regression coverage.

- Missing or byte-stale inventory fails without writes.
- All 8,296 current semantic digests match; regeneration never promotes scientific status.
- Symlink destinations and concurrent report edits are not overwritten.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| tests | tests/test_causal_graphs.py; Graph builder/model round-trip, malformed evidence, graph scope, cycles and rendering tests; records/export suite | supports | 132 tests passed in 103.32 seconds. Graph changes affect the semantic digest; invalid graph structure, quotes and hashes fail closed. |
| inspection | src/dufmech/causal_graphs.py; validate_graphs, inventory, main; records._validate_family_record; schema CausalGraph; site.curated_graphs and family-page integration | supports | Read the nine selected paths. Recomputed 130 overlays, 124 graph-bearing families, 747 graphs and 1,598 edges. All current overlays remain IN_PROGRESS; the 8,296-member inventory explicitly disclaims scientific completion. Main integration preserves protein examples alongside the graph section. |
| drift | src/dufmech/qc.py; COMMANDS and causal_graphs.main; ignored/hidden-inclusive search of src, scripts, tests, conf, justfile and .github | supports | No retained-inventory path or --check consumer is present in the searched directories, including ignored and hidden files. The report can diverge after an otherwise valid record regeneration. |

## Limits And Additional Notes

- Adversarial self-review, not independent approval.
- No fresh paper-by-paper reassessment of the 1,598 edges; existing scientific review scope and open follow-ups remain authoritative.
- Historical committed source; remediation and final publication must be assessed separately.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T195205Z-causal-graph-pr-baseline
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
    sha256: adcc562b3872e6715ddee8fbe70482ee0a87603c43438e8dd29989e70ac74023
  - path: src/dufmech/qc.py
    role: target
    sha256: a593c447d9314323efa664aa36695026f345f12c9865740b109aeae022ed5851
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
    sha256: 1acb8acdb308f1adba69b0bff293990ae2c9726f4aca5d1923890fb7e1ff8473
  - path: tests/test_causal_graphs.py
    role: target
    sha256: 6e2b7a7943c77af5a4da31e86e6aa4bcaa72b4521a68e1e035d9009707b7395b
  - path: tests/test_qc.py
    role: target
    sha256: 6923d9cc880a9595d17dab5e346c2a26925e17a9b9e4d7b947a371b77509b769
  snapshot_id: interpro-pfam-duf-2026-10-10
  state: git_commit
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
title: PR 199 causal-graph adversarial baseline
started_at: '2026-10-14T19:45:05Z'
finished_at: '2026-10-14T19:52:05Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: The publishing agent inspected existing implementation and challenged
    validation and publication boundaries. No independent approval is claimed.
skill: .claude/skills/review-repo/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: FAIL
scientific_review: false
summary: The committed baseline preserves graph scope, evidence validation and review
  digests, but the retained structural inventory is outside QC. Issue 198 tracks this
  confirmed reporting-drift gap. Publication and full QC remain separate release gates.
scope:
  description: Nine selected implementation, schema, rendering, test and inventory
    paths after integrating current main.
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
- check_id: baseline-tests
  name: Initial graph, records and exports regression suite
  status: passed
  required: true
  target_ids:
  - src/dufmech/records.py
  - tests/test_causal_graphs.py
  command: PYTHONPATH=src:/private/tmp/dufmech-protein-claw/src .venv/bin/python -m
    pytest -q tests/test_causal_graphs.py tests/test_records.py tests/test_exports.py
  exit_code: 0
  summary: 132 passed before integrating the two existing main commits; this is not
    final exact-head QC.
  evidence_ids:
  - tests
- check_id: inventory-probe
  name: Retained inventory check is unavailable in baseline
  status: passed
  required: true
  target_ids:
  - src/dufmech/causal_graphs.py
  - src/dufmech/qc.py
  - tests/test_causal_graphs.py
  - tests/test_qc.py
  - reports/causal_graphs/inventory.json
  command: PYTHONPATH=src .venv/bin/python -m dufmech.causal_graphs --check
  exit_code: 2
  expected_exit_code: 2
  summary: Argparse rejects --check; static inspection confirms the committed report
    has no QC consumer. This is reproduction evidence, not a successful inventory
    gate.
  evidence_ids:
  - drift
evidence:
- evidence_id: tests
  kind: validation
  reference: tests/test_causal_graphs.py
  locator: Graph builder/model round-trip, malformed evidence, graph scope, cycles
    and rendering tests; records/export suite
  accessed_at: '2026-10-14T19:52:05Z'
  support: supports
  summary: 132 tests passed in 103.32 seconds. Graph changes affect the semantic digest;
    invalid graph structure, quotes and hashes fail closed.
- evidence_id: inspection
  kind: record_content
  reference: src/dufmech/causal_graphs.py
  locator: validate_graphs, inventory, main; records._validate_family_record; schema
    CausalGraph; site.curated_graphs and family-page integration
  accessed_at: '2026-10-14T19:52:05Z'
  support: supports
  summary: Read the nine selected paths. Recomputed 130 overlays, 124 graph-bearing
    families, 747 graphs and 1,598 edges. All current overlays remain IN_PROGRESS;
    the 8,296-member inventory explicitly disclaims scientific completion. Main integration
    preserves protein examples alongside the graph section.
- evidence_id: drift
  kind: validation
  reference: src/dufmech/qc.py
  locator: COMMANDS and causal_graphs.main; ignored/hidden-inclusive search of src,
    scripts, tests, conf, justfile and .github
  accessed_at: '2026-10-14T19:52:05Z'
  support: supports
  summary: No retained-inventory path or --check consumer is present in the searched
    directories, including ignored and hidden files. The report can diverge after
    an otherwise valid record regeneration.
assessments:
- assessment_id: coverage-drift
  area: provenance
  topic: Retained structural coverage reproducibility
  outcome: concern
  target_ids:
  - src/dufmech/causal_graphs.py
  - src/dufmech/qc.py
  - tests/test_causal_graphs.py
  - tests/test_qc.py
  - reports/causal_graphs/inventory.json
  evidence_ids:
  - drift
  - inspection
  summary: The inventory content is explicitly structural, but no native command or
    QC gate detects stale counts, membership or semantic digests.
- assessment_id: native-contract
  area: scope
  topic: Graph evidence and publication semantics
  outcome: supported
  target_ids:
  - src/dufmech/records.py
  - src/dufmech/schema/dufmech.yaml
  - src/dufmech/site.py
  - tests/site_browser.cjs
  evidence_ids:
  - inspection
  - tests
  summary: Closed-schema projection and evidence checks preserve graph scope, support
    labels and direction; status promotion remains gated separately. Renderer integration
    retains both graphs and protein examples. Browser coverage for the combined page
    is a follow-up release check.
findings:
- finding_id: inventory-drift
  issue_key: DUFMech-198
  category: provenance
  severity: minor
  status: open
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
  - drift
  ownership_note: Fix native causal_graphs CLI, QC wiring and regression tests; do
    not alter scientific records to fit an old inventory.
  external_issues:
  - https://github.com/CultureBotAI/DUFMech/issues/198
actions:
- action_id: guard-inventory
  description: Add read-only --check, explicit guarded --apply, QC wiring and regression
    coverage.
  finding_ids:
  - inventory-drift
  target_ids:
  - src/dufmech/causal_graphs.py
  - src/dufmech/qc.py
  - tests/test_causal_graphs.py
  - tests/test_qc.py
  - reports/causal_graphs/inventory.json
  ownership_note: Native structural inventory module, QC and tests.
  acceptance_checks:
  - Missing or byte-stale inventory fails without writes.
  - All 8,296 current semantic digests match; regeneration never promotes scientific
    status.
  - Symlink destinations and concurrent report edits are not overwritten.
limitations:
- Adversarial self-review, not independent approval.
- No fresh paper-by-paper reassessment of the 1,598 edges; existing scientific review
  scope and open follow-ups remain authoritative.
- Historical committed source; remediation and final publication must be assessed
  separately.
links:
- https://github.com/CultureBotAI/DUFMech/pull/199
tags:
- causal-graphs
- adversarial-review
```
