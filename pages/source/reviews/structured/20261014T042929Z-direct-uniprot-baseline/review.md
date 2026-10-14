# PR 195 direct UniProt adversarial baseline

- Review: 20261014T042929Z-direct-uniprot-baseline
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-14T04:23:00Z
- Finished UTC: 2026-10-14T04:29:29Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

Historical assessment of committed baseline 05737a0ea. Newly authored negative tests reproduced two implementation gaps before fixes: cross-family sequence contradictions and checkpoint ownership changes during network requests. The new tests are reproduction evidence, not baseline test content.

## Scope And Provenance

Six committed baseline implementation and test files for direct UniProt discovery, parent validation and renderer integration; new negative probes were run before fixes.

Selection: Changed ingestion and presentation boundaries in PR 195.
Coverage: full; 6 reviewed / 6 in the declared population.
Source: git_commit at Git base 05737a0eaecdfe4263d61150fcdd17ac62cb0da7.
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
| New adversarial tests reproduce baseline defects | passed | True | src/dufmech/protein_discovery.py, src/dufmech/protein_examples.py, tests/test_protein_discovery.py | Three expected failing tests reproduced both defects. This is red-phase evidence, not a passing implementation. |
| Ruff | passed | True | src/dufmech/example_candidates.py, src/dufmech/pages.py, src/dufmech/protein_discovery.py, src/dufmech/protein_examples.py, src/dufmech/site.py, tests/test_protein_discovery.py | All checks passed before the added negative cases. |

## Scientific And Domain Assessments

### Sequence consistency and append-time ownership

provenance: concern. Targets: src/dufmech/protein_discovery.py, src/dufmech/protein_examples.py, tests/test_protein_discovery.py.

Per-row validation and pre-request ownership checks do not enforce the two reproduced cross-boundary invariants.

### Membership-only query and rendering contract

scope: supported. Targets: src/dufmech/example_candidates.py, src/dufmech/pages.py, src/dufmech/site.py.

The client retains explicit fields, bounded sample ranking and provider retry delays. Pages retains parent data, exposes FASTA and query provenance, and does not infer function or domain coordinates.

## Findings

### sequence-conflict: Same-release protein sequences can contradict across families

major / open / confirmed; issue key: DUFMech-196.

A combined snapshot can contain different sequence versions or hashes for the same primary accession and release. Production data was previously checked manually; enforce the invariant in validation.

### checkpoint-ownership: Checkpoint ownership is not rechecked after network requests

major / open / confirmed; issue key: DUFMech-197.

A hard-link alias created during a request is appended through the still-open staging inode. Recheck descriptor/path/link and manifest ownership before appends and use no-follow opening.

## Recommended Actions And Acceptance Checks

### fix-sequence-conflict

A combined snapshot can contain different sequence versions or hashes for the same primary accession and release. Production data was previously checked manually; enforce the invariant in validation.

- Reject same-accession same-release sequence/version conflicts, including parent overlaps.
- Permit different releases and verify the frozen production snapshot unchanged.

### fix-checkpoint-ownership

A hard-link alias created during a request is appended through the still-open staging inode. Recheck descriptor/path/link and manifest ownership before appends and use no-follow opening.

- Refuse hard-link, path replacement and newly manifest-owned checkpoints at append boundaries.
- Retain bounded, resumable acquisition and byte-identical retained data.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| probes | tests/test_protein_discovery.py; test_checkpoint_linked_during_request_is_not_appended and test_same_release_protein_cannot_have_conflicting_sequences | supports | All three new cases failed with DID NOT RAISE. Temporary fixtures only; no production artifact was modified. |
| inspection | src/dufmech/protein_discovery.py; discover, validate_observation, verify_derivation; related parent validator, client and Pages integration | supports | Reviewed the six selected files. Direct queries retain raw data, bounded sampling, exact membership and parent replay; sequence consistency and post-request ownership were not enforced. |

## Limits And Additional Notes

- Adversarial self-review, not independent approval or a scientific literature review.
- This assessment does not certify final source publication, generated Pages or exact-head CI.
- Append guards are advisory against cooperating writers, not protection from arbitrary concurrent inode mutation.
- Baseline source is historical; the added negative-test harness was run before implementation edits and is not represented as committed baseline content.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T042929Z-direct-uniprot-baseline
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
    sha256: c58e63ccfe7e0060008f2614f4befe41c7d94670ee8aec3989573c38a1f3d08d
  - path: src/dufmech/protein_examples.py
    role: target
    sha256: 799b287582b9639716faf4509b15c38869672a7e06fe1d41143970c6d37aaabb
  - path: src/dufmech/site.py
    role: target
    sha256: db216b3353cdf4542cd83f21beaa31182fc04352a74c69694b35c916264e0f9b
  - path: tests/test_protein_discovery.py
    role: target
    sha256: 735e8d1410297cf4f9b95423e11bb89ceaee11a0ec2af8b4a046c78a0a58253f
  snapshot_id: interpro-pfam-duf-2026-10-10
  state: git_commit
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
title: PR 195 direct UniProt adversarial baseline
started_at: '2026-10-14T04:23:00Z'
finished_at: '2026-10-14T04:29:29Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: The implementing agent challenged the committed implementation
    with new negative tests. No independent approval is claimed.
skill: .claude/skills/review-repo/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: FAIL
scientific_review: false
summary: 'Historical assessment of committed baseline 05737a0ea. Newly authored negative
  tests reproduced two implementation gaps before fixes: cross-family sequence contradictions
  and checkpoint ownership changes during network requests. The new tests are reproduction
  evidence, not baseline test content.'
scope:
  description: Six committed baseline implementation and test files for direct UniProt
    discovery, parent validation and renderer integration; new negative probes were
    run before fixes.
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
- check_id: negative-probes
  name: New adversarial tests reproduce baseline defects
  status: passed
  required: true
  target_ids:
  - src/dufmech/protein_discovery.py
  - src/dufmech/protein_examples.py
  - tests/test_protein_discovery.py
  command: .venv/bin/pytest -q tests/test_protein_discovery.py -k 'linked_during_request
    or conflicting_sequences'
  exit_code: 1
  expected_exit_code: 1
  summary: Three expected failing tests reproduced both defects. This is red-phase
    evidence, not a passing implementation.
  evidence_ids:
  - probes
- check_id: ruff
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
  command: .venv/bin/ruff check .
  exit_code: 0
  summary: All checks passed before the added negative cases.
  evidence_ids:
  - inspection
evidence:
- evidence_id: probes
  kind: validation
  reference: tests/test_protein_discovery.py
  locator: test_checkpoint_linked_during_request_is_not_appended and test_same_release_protein_cannot_have_conflicting_sequences
  accessed_at: '2026-10-14T04:29:29Z'
  support: supports
  summary: All three new cases failed with DID NOT RAISE. Temporary fixtures only;
    no production artifact was modified.
- evidence_id: inspection
  kind: record_content
  reference: src/dufmech/protein_discovery.py
  locator: discover, validate_observation, verify_derivation; related parent validator,
    client and Pages integration
  accessed_at: '2026-10-14T04:29:29Z'
  support: supports
  summary: Reviewed the six selected files. Direct queries retain raw data, bounded
    sampling, exact membership and parent replay; sequence consistency and post-request
    ownership were not enforced.
assessments:
- assessment_id: integrity
  area: provenance
  topic: Sequence consistency and append-time ownership
  outcome: concern
  summary: Per-row validation and pre-request ownership checks do not enforce the
    two reproduced cross-boundary invariants.
  target_ids:
  - src/dufmech/protein_discovery.py
  - src/dufmech/protein_examples.py
  - tests/test_protein_discovery.py
  evidence_ids:
  - probes
  - inspection
- assessment_id: integration
  area: scope
  topic: Membership-only query and rendering contract
  outcome: supported
  summary: The client retains explicit fields, bounded sample ranking and provider
    retry delays. Pages retains parent data, exposes FASTA and query provenance, and
    does not infer function or domain coordinates.
  target_ids:
  - src/dufmech/example_candidates.py
  - src/dufmech/pages.py
  - src/dufmech/site.py
  evidence_ids:
  - inspection
findings:
- finding_id: sequence-conflict
  issue_key: DUFMech-196
  category: provenance
  severity: major
  status: open
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
  - probes
  ownership_note: Fix native row validation and tests; do not rewrite frozen evidence.
  external_issues:
  - https://github.com/CultureBotAI/DUFMech/issues/196
- finding_id: checkpoint-ownership
  issue_key: DUFMech-197
  category: ownership
  severity: major
  status: open
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
  - probes
  ownership_note: Fix direct discovery writer and regression tests.
  external_issues:
  - https://github.com/CultureBotAI/DUFMech/issues/197
actions:
- action_id: fix-sequence-conflict
  description: A combined snapshot can contain different sequence versions or hashes
    for the same primary accession and release. Production data was previously checked
    manually; enforce the invariant in validation.
  finding_ids:
  - sequence-conflict
  target_ids:
  - src/dufmech/protein_examples.py
  - tests/test_protein_discovery.py
  ownership_note: Fix native row validation and tests; do not rewrite frozen evidence.
  acceptance_checks:
  - Reject same-accession same-release sequence/version conflicts, including parent
    overlaps.
  - Permit different releases and verify the frozen production snapshot unchanged.
- action_id: fix-checkpoint-ownership
  description: A hard-link alias created during a request is appended through the
    still-open staging inode. Recheck descriptor/path/link and manifest ownership
    before appends and use no-follow opening.
  finding_ids:
  - checkpoint-ownership
  target_ids:
  - src/dufmech/protein_discovery.py
  - tests/test_protein_discovery.py
  ownership_note: Fix direct discovery writer and regression tests.
  acceptance_checks:
  - Refuse hard-link, path replacement and newly manifest-owned checkpoints at append
    boundaries.
  - Retain bounded, resumable acquisition and byte-identical retained data.
limitations:
- Adversarial self-review, not independent approval or a scientific literature review.
- This assessment does not certify final source publication, generated Pages or exact-head
  CI.
- Append guards are advisory against cooperating writers, not protection from arbitrary
  concurrent inode mutation.
- Baseline source is historical; the added negative-test harness was run before implementation
  edits and is not represented as committed baseline content.
links:
- https://github.com/CultureBotAI/DUFMech/pull/195
tags:
- direct-uniprot
- adversarial-review
```
