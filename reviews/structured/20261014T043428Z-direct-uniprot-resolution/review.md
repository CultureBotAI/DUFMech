# PR 195 adversarial review remediation

- Review: 20261014T043428Z-direct-uniprot-resolution
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-14T04:29:29Z
- Finished UTC: 2026-10-14T04:34:28Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Both reproduced findings are resolved in the inspected working tree. Combined rows reject same-release sequence contradictions, and direct discovery uses descriptor-bound opening with ownership checks before each append. All 214 focused tests pass (one expected skip); the unchanged 8,296-family snapshot validates. Final publication and exact-head CI remain separate required release gates.

## Scope And Provenance

Read and reassessed the six selected current files after remediation, including checkpoint ownership transitions, combined sequence identity, raw replay and presentation.

Selection: Changed ingestion and presentation boundaries in PR 195.
Coverage: full; 6 reviewed / 6 in the declared population.
Source: working_tree at Git base 05737a0eaecdfe4263d61150fcdd17ac62cb0da7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| src/dufmech/example_candidates.py | src/dufmech/example_candidates.py | source | src/dufmech/example_candidates.py |
| src/dufmech/pages.py | src/dufmech/pages.py | source | src/dufmech/pages.py |
| src/dufmech/protein_discovery.py | src/dufmech/protein_discovery.py | source | src/dufmech/protein_discovery.py |
| src/dufmech/protein_examples.py | src/dufmech/protein_examples.py | source | src/dufmech/protein_examples.py |
| src/dufmech/site.py | src/dufmech/site.py | source | src/dufmech/site.py |
| tests/test_protein_discovery.py | tests/test_protein_discovery.py | source | tests/test_protein_discovery.py |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused discovery, parent, client, renderer and governance tests | passed | True | src/dufmech/example_candidates.py, src/dufmech/pages.py, src/dufmech/protein_discovery.py, src/dufmech/protein_examples.py, src/dufmech/site.py, tests/test_protein_discovery.py | 214 passed, 1 expected empty-parameter skip in 65.85 seconds. An intermediate new fixture lacked its required source URL; correcting the fixture enabled its intended conflict test. |
| Load and replay unchanged full direct snapshot | passed | True | src/dufmech/protein_discovery.py, src/dufmech/protein_examples.py | 8,296 rows, 8,290 covered, six empty, 24,886 examples and 23,836 distinct proteins. Parent/raw replay and stricter sequence checks pass. |
| Ruff | passed | True | src/dufmech/example_candidates.py, src/dufmech/pages.py, src/dufmech/protein_discovery.py, src/dufmech/protein_examples.py, src/dufmech/site.py, tests/test_protein_discovery.py | All checks passed. |
| Final release gates | unavailable | False | src/dufmech/example_candidates.py, src/dufmech/pages.py, src/dufmech/protein_discovery.py, src/dufmech/protein_examples.py, src/dufmech/site.py, tests/test_protein_discovery.py | The initial draft CI failed at the missing new source pin, as expected. Publication checkpoint, source retention, native rendering, full QC and exact-head CI must pass before merge; they are outside this scoped remediation review. |

## Scientific And Domain Assessments

### Sequence consistency and checkpoint ownership

provenance: supported. Targets: src/dufmech/protein_discovery.py, src/dufmech/protein_examples.py, tests/test_protein_discovery.py.

New tests exercise rejected ownership transitions and conflicting identities. Valid staging resumption, release distinctions, unchanged production parent replay and explicit empty responses remain accepted.

### Provider query and membership-only publication

scope: supported. Targets: src/dufmech/example_candidates.py, src/dufmech/pages.py, src/dufmech/site.py.

Focused client and renderer tests pass. Direct query origins and parent replay are preserved without functional promotion; publication still requires the explicit pin ledger and native gates.

## Findings

### sequence-conflict: Same-release protein sequences can contradict across families

major / resolved / confirmed; issue key: DUFMech-196.

A combined snapshot can contain different sequence versions or hashes for the same primary accession and release. Production data was previously checked manually; enforce the invariant in validation.

Disposition: Reproduced two baseline failures; validation now rejects contradictory same-release hashes/versions across parent and direct families, while accepting different releases and the unchanged production snapshot.

### checkpoint-ownership: Checkpoint ownership is not rechecked after network requests

major / resolved / confirmed; issue key: DUFMech-197.

A hard-link alias created during a request is appended through the still-open staging inode. Recheck descriptor/path/link and manifest ownership before appends and use no-follow opening.

Disposition: Reproduced baseline alias mutation; descriptor-bound opening and append-time checks now reject tested ownership transitions while preserving preexisting bytes and valid resume behavior.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| regressions | tests/test_protein_discovery.py; sequence consistency, raw-conflict freeze, different-release acceptance, append-time hard-link/manifest/path/size/parent tests and FIFO refusal | supports | All scoped tests pass. New cases reject contradictions across parent/direct and direct/direct examples and reject ownership changes without additional checkpoint writes. Legitimate cross-release changes remain accepted. |
| implementation | src/dufmech/protein_discovery.py; _checkpoint_writer, _check_append, discover; protein_examples.validate_rows and renderer integration | supports | No-follow descriptor-relative checkpoint open, append-boundary identity/link/size/manifest checks, and one sequence identity per accession/release in combined row validation. Query scope and presentation remain membership-only. |
| production | data/protein_examples/duf-protein-examples-direct-2026-10-13.json; load_snapshot over complete corpus, including parent and raw-query replay | supports | The unchanged production snapshot loaded successfully and retains the expected full coverage counts. |
| publication | https://github.com/CultureBotAI/DUFMech/actions/runs/38511518386; qc generated-site gate | context_only | Initial draft CI passed earlier gates then failed because the new direct snapshot has no source pin yet. No bypass is proposed. |

## Limits And Additional Notes

- Adversarial self-review, not independent approval or a functional scientific review.
- Checkpoint guards and flock are advisory; no exhaustive defense against noncooperating concurrent same-inode writes is claimed.
- Final full QC, native Pages regeneration, canonical source retention, exact-head CI and merge-queue CI remain required before merge and will be recorded in PR 195.
- Six successful empty searches remain research gaps; no biological-absence conclusion is drawn.
- Existing unresolved license warnings for other sources are not resolved or relicensed by this work.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T043428Z-direct-uniprot-resolution
kind: repository
repository: CultureBotAI/DUFMech
source:
  git_revision: 05737a0eaecdfe4263d61150fcdd17ac62cb0da7
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
  - path: src/dufmech/example_candidates.py
    role: target
    sha256: fcde2a7927daf4b4bc4b3ff04f32fff7889b4ff4c4720f5bdadf5da5345c712e
  - path: src/dufmech/pages.py
    role: target
    sha256: c77c649c0e2908d78cd114ee03932195dc7ecb3db35d22422375a5884531e804
  - path: src/dufmech/protein_discovery.py
    role: target
    sha256: 23ea5328c0e5786f414b3a529ed06cc8a8c3dbfa5b707f960ea7c35d43a64b2d
  - path: src/dufmech/protein_examples.py
    role: target
    sha256: ab3fe87b17c4dc7ec43bf95d141a6173f9de901d28d4d8f6d4436f3193f9ce75
  - path: src/dufmech/site.py
    role: target
    sha256: db216b3353cdf4542cd83f21beaa31182fc04352a74c69694b35c916264e0f9b
  - path: tests/test_protein_discovery.py
    role: target
    sha256: ea04800564d90b9934c0f38fe2151be6256275fa1b2b818a80dd47abcbd3afc3
  snapshot_id: interpro-pfam-duf-2026-10-10
  state: working_tree
targets:
- kind: source
  label: src/dufmech/example_candidates.py
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: src/dufmech/example_candidates.py
  target_id: src/dufmech/example_candidates.py
- kind: source
  label: src/dufmech/pages.py
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: src/dufmech/pages.py
  target_id: src/dufmech/pages.py
- kind: source
  label: src/dufmech/protein_discovery.py
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: src/dufmech/protein_discovery.py
  target_id: src/dufmech/protein_discovery.py
- kind: source
  label: src/dufmech/protein_examples.py
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: src/dufmech/protein_examples.py
  target_id: src/dufmech/protein_examples.py
- kind: source
  label: src/dufmech/site.py
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: src/dufmech/site.py
  target_id: src/dufmech/site.py
- kind: source
  label: tests/test_protein_discovery.py
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: tests/test_protein_discovery.py
  target_id: tests/test_protein_discovery.py
title: PR 195 adversarial review remediation
started_at: '2026-10-14T04:29:29Z'
finished_at: '2026-10-14T04:34:28Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: The implementing agent challenged the committed implementation
    with new negative tests. No independent approval is claimed.
skill: .claude/skills/review-repo/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: false
summary: Both reproduced findings are resolved in the inspected working tree. Combined
  rows reject same-release sequence contradictions, and direct discovery uses descriptor-bound
  opening with ownership checks before each append. All 214 focused tests pass (one
  expected skip); the unchanged 8,296-family snapshot validates. Final publication
  and exact-head CI remain separate required release gates.
scope:
  description: Read and reassessed the six selected current files after remediation,
    including checkpoint ownership transitions, combined sequence identity, raw replay
    and presentation.
  selection: Changed ingestion and presentation boundaries in PR 195.
  coverage: full
  population_size: 6
  reviewed_target_ids:
  - src/dufmech/example_candidates.py
  - src/dufmech/pages.py
  - src/dufmech/protein_discovery.py
  - src/dufmech/protein_examples.py
  - src/dufmech/site.py
  - tests/test_protein_discovery.py
  exclusions:
  - target: Scientific function and current provider content
    reason: Sequence membership is not experimental characterization; no new provider
      calls.
  - target: Final generated publication
    reason: Source checkpoint and regenerated Pages remain a separate release gate.
checks:
- check_id: focused
  name: Focused discovery, parent, client, renderer and governance tests
  status: passed
  required: true
  target_ids:
  - src/dufmech/example_candidates.py
  - src/dufmech/pages.py
  - src/dufmech/protein_discovery.py
  - src/dufmech/protein_examples.py
  - src/dufmech/site.py
  - tests/test_protein_discovery.py
  command: .venv/bin/pytest -q tests/test_protein_discovery.py tests/test_protein_examples.py
    tests/test_example_candidates.py tests/test_pages.py tests/test_site.py tests/test_source_governance.py
  exit_code: 0
  summary: 214 passed, 1 expected empty-parameter skip in 65.85 seconds. An intermediate
    new fixture lacked its required source URL; correcting the fixture enabled its
    intended conflict test.
  evidence_ids:
  - regressions
- check_id: production
  name: Load and replay unchanged full direct snapshot
  status: passed
  required: true
  target_ids:
  - src/dufmech/protein_discovery.py
  - src/dufmech/protein_examples.py
  command: .venv/bin/python -c 'from pathlib import Path; from dufmech.protein_examples
    import load_snapshot; from dufmech.report import load_json_rows; p=Path("data/protein_examples/duf-protein-examples-direct-2026-10-13.json");
    rows,m=load_snapshot(p,list(load_json_rows(Path("data/worklists/interpro-pfam-duf-2026-10-10.json"))),"interpro-pfam-duf-2026-10-10");
    print(m["rows"])'
  exit_code: 0
  summary: 8,296 rows, 8,290 covered, six empty, 24,886 examples and 23,836 distinct
    proteins. Parent/raw replay and stricter sequence checks pass.
  evidence_ids:
  - production
- check_id: lint
  name: Ruff
  status: passed
  required: true
  target_ids:
  - src/dufmech/example_candidates.py
  - src/dufmech/pages.py
  - src/dufmech/protein_discovery.py
  - src/dufmech/protein_examples.py
  - src/dufmech/site.py
  - tests/test_protein_discovery.py
  command: .venv/bin/ruff check src scripts tests
  exit_code: 0
  summary: All checks passed.
  evidence_ids:
  - implementation
- check_id: publication
  name: Final release gates
  status: unavailable
  required: false
  target_ids:
  - src/dufmech/example_candidates.py
  - src/dufmech/pages.py
  - src/dufmech/protein_discovery.py
  - src/dufmech/protein_examples.py
  - src/dufmech/site.py
  - tests/test_protein_discovery.py
  summary: The initial draft CI failed at the missing new source pin, as expected.
    Publication checkpoint, source retention, native rendering, full QC and exact-head
    CI must pass before merge; they are outside this scoped remediation review.
  evidence_ids:
  - publication
evidence:
- evidence_id: regressions
  kind: validation
  reference: tests/test_protein_discovery.py
  locator: sequence consistency, raw-conflict freeze, different-release acceptance,
    append-time hard-link/manifest/path/size/parent tests and FIFO refusal
  accessed_at: '2026-10-14T04:34:28Z'
  support: supports
  summary: All scoped tests pass. New cases reject contradictions across parent/direct
    and direct/direct examples and reject ownership changes without additional checkpoint
    writes. Legitimate cross-release changes remain accepted.
- evidence_id: implementation
  kind: record_content
  reference: src/dufmech/protein_discovery.py
  locator: _checkpoint_writer, _check_append, discover; protein_examples.validate_rows
    and renderer integration
  accessed_at: '2026-10-14T04:34:28Z'
  support: supports
  summary: No-follow descriptor-relative checkpoint open, append-boundary identity/link/size/manifest
    checks, and one sequence identity per accession/release in combined row validation.
    Query scope and presentation remain membership-only.
- evidence_id: production
  kind: validation
  reference: data/protein_examples/duf-protein-examples-direct-2026-10-13.json
  locator: load_snapshot over complete corpus, including parent and raw-query replay
  accessed_at: '2026-10-14T04:34:28Z'
  support: supports
  summary: The unchanged production snapshot loaded successfully and retains the expected
    full coverage counts.
- evidence_id: publication
  kind: validation
  reference: https://github.com/CultureBotAI/DUFMech/actions/runs/38511518386
  locator: qc generated-site gate
  accessed_at: '2026-10-14T04:34:28Z'
  support: context_only
  summary: Initial draft CI passed earlier gates then failed because the new direct
    snapshot has no source pin yet. No bypass is proposed.
assessments:
- assessment_id: integrity
  area: provenance
  topic: Sequence consistency and checkpoint ownership
  outcome: supported
  summary: New tests exercise rejected ownership transitions and conflicting identities.
    Valid staging resumption, release distinctions, unchanged production parent replay
    and explicit empty responses remain accepted.
  target_ids:
  - src/dufmech/protein_discovery.py
  - src/dufmech/protein_examples.py
  - tests/test_protein_discovery.py
  evidence_ids:
  - regressions
  - implementation
  - production
- assessment_id: integration
  area: scope
  topic: Provider query and membership-only publication
  outcome: supported
  summary: Focused client and renderer tests pass. Direct query origins and parent
    replay are preserved without functional promotion; publication still requires
    the explicit pin ledger and native gates.
  target_ids:
  - src/dufmech/example_candidates.py
  - src/dufmech/pages.py
  - src/dufmech/site.py
  evidence_ids:
  - regressions
  - implementation
findings:
- finding_id: sequence-conflict
  issue_key: DUFMech-196
  category: provenance
  severity: major
  status: resolved
  certainty: confirmed
  title: Same-release protein sequences can contradict across families
  description: A combined snapshot can contain different sequence versions or hashes
    for the same primary accession and release. Production data was previously checked
    manually; enforce the invariant in validation.
  target_ids:
  - src/dufmech/protein_examples.py
  - tests/test_protein_discovery.py
  field_paths:
  - validate_rows
  evidence_ids:
  - regressions
  - implementation
  - production
  ownership_note: Fix native row validation and tests; do not rewrite frozen evidence.
  external_issues:
  - https://github.com/CultureBotAI/DUFMech/issues/196
  disposition_reason: Reproduced two baseline failures; validation now rejects contradictory
    same-release hashes/versions across parent and direct families, while accepting
    different releases and the unchanged production snapshot.
  previous_occurrences:
  - repository: CultureBotAI/DUFMech
    review_id: 20261014T042929Z-direct-uniprot-baseline
    finding_id: sequence-conflict
- finding_id: checkpoint-ownership
  issue_key: DUFMech-197
  category: ownership
  severity: major
  status: resolved
  certainty: confirmed
  title: Checkpoint ownership is not rechecked after network requests
  description: A hard-link alias created during a request is appended through the
    still-open staging inode. Recheck descriptor/path/link and manifest ownership
    before appends and use no-follow opening.
  target_ids:
  - src/dufmech/protein_discovery.py
  - tests/test_protein_discovery.py
  field_paths:
  - discover
  evidence_ids:
  - regressions
  - implementation
  - production
  ownership_note: Fix direct discovery writer and regression tests.
  external_issues:
  - https://github.com/CultureBotAI/DUFMech/issues/197
  disposition_reason: Reproduced baseline alias mutation; descriptor-bound opening
    and append-time checks now reject tested ownership transitions while preserving
    preexisting bytes and valid resume behavior.
  previous_occurrences:
  - repository: CultureBotAI/DUFMech
    review_id: 20261014T042929Z-direct-uniprot-baseline
    finding_id: checkpoint-ownership
actions: []
limitations:
- Adversarial self-review, not independent approval or a functional scientific review.
- Checkpoint guards and flock are advisory; no exhaustive defense against noncooperating
  concurrent same-inode writes is claimed.
- Final full QC, native Pages regeneration, canonical source retention, exact-head
  CI and merge-queue CI remain required before merge and will be recorded in PR 195.
- Six successful empty searches remain research gaps; no biological-absence conclusion
  is drawn.
- Existing unresolved license warnings for other sources are not resolved or relicensed
  by this work.
links:
- https://github.com/CultureBotAI/DUFMech/pull/195
tags:
- direct-uniprot
- adversarial-review
related_reviews:
- repository: CultureBotAI/DUFMech
  review_id: 20261014T042929Z-direct-uniprot-baseline
  relationship: Resolves both reproduced findings with native validator and writer
    fixes and regression checks.
```
