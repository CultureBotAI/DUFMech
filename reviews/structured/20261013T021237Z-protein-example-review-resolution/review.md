# PR 192 adversarial self-review and remediation

- Review: 20261013T021237Z-protein-example-review-resolution
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-13T02:05:23Z
- Finished UTC: 2026-10-13T02:12:37Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

The scoped implementation review found two reproducible defects, tracked as issues 193 and 194, and verified their fixes. Manifest-owned acquisition checkpoints can no longer be appended to, and retained examples and rejected candidates require immutable origin provenance with consistent registry status. All 128 focused tests pass; the 19 new negative cases produce 18 failures against the original module. Full publication QC, source retention and regenerated Pages remain required after this report is saved.

## Scope And Provenance

Read the four selected protein acquisition, validation, rendering and regression files. Assess immutable input handling, sequence origin semantics, all-family coverage and presentation of membership versus functional claims.

Selection: PR 192 sequence-example pipeline and its direct renderer integration; targeted negative tests for ordinary resume and malformed provenance.
Coverage: full; 4 reviewed / 4 in the declared population.
Source: working_tree at Git base 9053fcf725d527056db22c676ce84791f705ee6c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| src/dufmech/pages.py | src/dufmech/pages.py | source | src/dufmech/pages.py |
| src/dufmech/protein_examples.py | src/dufmech/protein_examples.py | source | src/dufmech/protein_examples.py |
| src/dufmech/site.py | src/dufmech/site.py | source | src/dufmech/site.py |
| tests/test_protein_examples.py | tests/test_protein_examples.py | source | tests/test_protein_examples.py |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused acquisition, source-pin, writer, renderer and command-boundary tests | passed | True | src/dufmech/pages.py, src/dufmech/protein_examples.py, src/dufmech/site.py, tests/test_protein_examples.py | 128 passed in 63.79 seconds. The retained-checkpoint tests verify unchanged bytes and no request when missing entries would require mutation. Valid offline replay and changed-registry versions remain accepted. |
| New negative cases exercised against the original committed module | passed | True | src/dufmech/protein_examples.py, tests/test_protein_examples.py | Expected failing baseline: 18 failed, 1 passed, 23 deselected. One checksum mismatch case was already rejected. This is red-phase evidence, not a passing baseline implementation. |
| All retained manifest and sequence-row integrity | passed | True | src/dufmech/protein_examples.py | 14 manifests validated, including both unmodified sequence-example snapshots under the stricter provenance rules. |
| Ruff and whitespace | passed | True | src/dufmech/pages.py, src/dufmech/protein_examples.py, src/dufmech/site.py, tests/test_protein_examples.py | Both commands were run separately and exited zero. |
| Final publication gates | unavailable | False | src/dufmech/pages.py, src/dufmech/protein_examples.py, src/dufmech/site.py, tests/test_protein_examples.py | Not yet run for a final published source ledger and generated site. Required before merging; this scoped report does not certify release readiness. |

## Scientific And Domain Assessments

### Frozen checkpoint mutation guard

ownership: supported. Targets: src/dufmech/protein_examples.py, tests/test_protein_examples.py.

The explicit acquisition command still resumes staging files, but rejects a missing-entry append when a companion manifest owns that checkpoint, before constructing the request. Complete frozen replay remains read-only. Parent symlinks are rejected.

### Immutable origin and registry consistency

provenance: supported. Targets: src/dufmech/protein_examples.py, tests/test_protein_examples.py.

Both example and unresolved candidate origins require internally consistent immutable links and identifying fields. Sequence origin must agree with registry status; mirrors and differences carry valid registry commit/path/blob hash/version/release metadata and consistent sequence comparison.

### Membership references do not promote functional claims

scope: supported. Targets: src/dufmech/pages.py, src/dufmech/site.py.

The rendering and loader integration preserves gap reporting, rejects unpinned native source files and supplies complete JSON/FASTA rather than silently truncating to ten displayed examples. Explicit membership and domain-boundary caveats remain. Functional assertions and canonical family projections are not changed.

## Findings

### checkpoint-mutation: Resuming acquisition could mutate a retained snapshot checkpoint

major / resolved / confirmed; issue key: DUFMech-193.

The baseline appended new observations to manifest-owned .queries.jsonl files, invalidating historical evidence. The corrected code checks sibling manifests before network access and refuses the write.

Disposition: Reproduced on the original commit; corrected implementation passes no-request and unchanged-byte assertions and complete replay checks.

### unvalidated-provenance: Row validation accepted mutable and unsupported origin provenance

major / resolved / confirmed; issue key: DUFMech-194.

The baseline checked nonempty origins and only conditionally compared mirror hashes. The corrected validator enforces immutable origin URLs and commits plus consistent acquisition and registry metadata.

Disposition: Mutable links, unsupported origins and invalid registry metadata now reject; both real datasets and valid mismatch examples pass.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| checkpoint-probe | https://github.com/CultureBotAI/DUFMech/issues/193; acquire at 9053fcf72 and test_lookup_never_appends_to_frozen_checkpoint | supports | A temporary valid snapshot checkpoint was resumed with a new mocked accession. Its bytes changed and verified_manifest raised byte/checksum mismatches. No production artifact was changed. |
| origin-probe | https://github.com/CultureBotAI/DUFMech/issues/194; validate_rows at 9053fcf72 and provenance_validation regression cases | supports | A fixture with commit main, blob/main URL and unsupported sequence_origin UNVERIFIED passed the baseline row validator. |
| regressions | tests/test_protein_examples.py; test_lookup_never_appends_to_frozen_checkpoint, test_lookup_rejects_symlinked_parent_before_network, provenance_validation parameter sets and valid registry mismatch test | supports | Negative cases now reject manifest-owned checkpoint appends before network I/O, parent symlinks, mutable or inconsistent origins, unsupported origin/status pairs and malformed registry proof. Existing frozen data passes unchanged. |
| implementation | src/dufmech/protein_examples.py; acquire, build_rows, validate_rows, write_snapshot; pages.render_from_paths; site.protein_examples_section and FASTA rendering | supports | Coverage accounts for each worklist family; examples require exact current Pfam membership, preserve whole-protein sequences, and do not claim functional evidence. The renderer keeps all examples in JSON/FASTA, displays a bounded table and attribution, and requires native source pins. |

## Limits And Additional Notes

- Self-review, not independent approval or exhaustive adversarial filesystem/concurrency analysis.
- Full just qc, exact-head GitHub checks and retained source publication remain required after this report is committed. Their outcomes belong in PR 192, not a retroactive edit to this report.
- 5,190 family gaps, 15 rejected pairings and 114 unresolved discovery accession leads remain research work, not evidence of biological absence.
- The discovery manifest and pinned sibling commits are retained; full offline reproduction still needs the separately staged, verified discovery JSON input described in the provenance report.
- Source governance reports zero errors and 16 existing unresolved-license warnings. This review does not relicense the older combined cross-Mech bundle.
- No online source availability check or new scientific functional review was performed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T021237Z-protein-example-review-resolution
kind: repository
repository: CultureBotAI/DUFMech
title: PR 192 adversarial self-review and remediation
started_at: '2026-10-13T02:05:23Z'
finished_at: '2026-10-13T02:12:37Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: The implementing agent challenged checkpoint mutation and provenance
    validation with baseline reproductions and regression tests. No independent reviewer
    approval is claimed.
skill: .claude/skills/review-repo/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: false
summary: The scoped implementation review found two reproducible defects, tracked
  as issues 193 and 194, and verified their fixes. Manifest-owned acquisition checkpoints
  can no longer be appended to, and retained examples and rejected candidates require
  immutable origin provenance with consistent registry status. All 128 focused tests
  pass; the 19 new negative cases produce 18 failures against the original module.
  Full publication QC, source retention and regenerated Pages remain required after
  this report is saved.
source:
  git_revision: 9053fcf725d527056db22c676ce84791f705ee6c
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
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
  - path: src/dufmech/pages.py
    role: target
    sha256: 7911a9a50e741496d90cd89a27d8926a8fe82ca1448888fa9cd7f403be4c0db8
  - path: src/dufmech/protein_examples.py
    role: target
    sha256: 729aef4d6205813947492f7fd815a8da6f27e0166f91f1503234cf956b459d57
  - path: src/dufmech/site.py
    role: target
    sha256: 4efdc2e9e8479f56e6daec71834867c98201a8d74957feff5ec42621f0e5a9f1
  - path: tests/test_protein_examples.py
    role: target
    sha256: 586095b0f5937b027de77eedf85b53eb377a662d0f1e2ee6c49564a4e0ca161e
targets:
- kind: source
  label: src/dufmech/pages.py
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: src/dufmech/pages.py
  target_id: src/dufmech/pages.py
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
  label: tests/test_protein_examples.py
  ownership_note: Inspect the selected source's ownership before proposing an edit.
  path: tests/test_protein_examples.py
  target_id: tests/test_protein_examples.py
scope:
  description: Read the four selected protein acquisition, validation, rendering and
    regression files. Assess immutable input handling, sequence origin semantics,
    all-family coverage and presentation of membership versus functional claims.
  selection: PR 192 sequence-example pipeline and its direct renderer integration;
    targeted negative tests for ordinary resume and malformed provenance.
  coverage: full
  population_size: 4
  reviewed_target_ids:
  - src/dufmech/pages.py
  - src/dufmech/protein_examples.py
  - src/dufmech/site.py
  - tests/test_protein_examples.py
  exclusions:
  - target: Family scientific curation
    reason: No literature or experimental functional assertions are evaluated or promoted.
  - target: Separate causal-graph branch and other Mechs
    reason: Not part of this PR or remediation.
checks:
- check_id: focused
  name: Focused acquisition, source-pin, writer, renderer and command-boundary tests
  status: passed
  required: true
  target_ids:
  - src/dufmech/pages.py
  - src/dufmech/protein_examples.py
  - src/dufmech/site.py
  - tests/test_protein_examples.py
  command: env PYTHONPATH=src:/private/tmp/dufmech-protein-claw/src CLAW_SRC=/private/tmp/dufmech-protein-claw/src
    CLAW_ROOT=/private/tmp/dufmech-protein-claw .venv/bin/python -m pytest tests/test_protein_examples.py
    tests/test_site_sources.py tests/test_site_writes.py tests/test_pages.py tests/test_just_curation.py
    -q
  exit_code: 0
  expected_exit_code: 0
  summary: 128 passed in 63.79 seconds. The retained-checkpoint tests verify unchanged
    bytes and no request when missing entries would require mutation. Valid offline
    replay and changed-registry versions remain accepted.
  evidence_ids:
  - regressions
- check_id: baseline-red
  name: New negative cases exercised against the original committed module
  status: passed
  required: true
  target_ids:
  - src/dufmech/protein_examples.py
  - tests/test_protein_examples.py
  command: env PYTHONPATH=src .venv/bin/python -c 'import subprocess; import dufmech.protein_examples
    as m; import pytest; exec(compile(subprocess.check_output(["git","show","9053fcf72:src/dufmech/protein_examples.py"]),
    "baseline-protein-examples.py", "exec"), m.__dict__); raise SystemExit(pytest.main(["tests/test_protein_examples.py",
    "-q", "--tb=no", "-k", "never_appends or symlinked_parent or provenance_validation"]))'
  exit_code: 1
  expected_exit_code: 1
  summary: 'Expected failing baseline: 18 failed, 1 passed, 23 deselected. One checksum
    mismatch case was already rejected. This is red-phase evidence, not a passing
    baseline implementation.'
  evidence_ids:
  - regressions
  - checkpoint-probe
  - origin-probe
- check_id: snapshots
  name: All retained manifest and sequence-row integrity
  status: passed
  required: true
  target_ids:
  - src/dufmech/protein_examples.py
  command: env PYTHONPATH=src .venv/bin/python scripts/check_provenance.py
  exit_code: 0
  expected_exit_code: 0
  summary: 14 manifests validated, including both unmodified sequence-example snapshots
    under the stricter provenance rules.
  evidence_ids:
  - regressions
- check_id: lint
  name: Ruff and whitespace
  status: passed
  required: true
  target_ids:
  - src/dufmech/pages.py
  - src/dufmech/protein_examples.py
  - src/dufmech/site.py
  - tests/test_protein_examples.py
  command: .venv/bin/ruff check src scripts tests; git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Both commands were run separately and exited zero.
  evidence_ids:
  - implementation
- check_id: publication
  name: Final publication gates
  status: unavailable
  required: false
  target_ids:
  - src/dufmech/pages.py
  - src/dufmech/protein_examples.py
  - src/dufmech/site.py
  - tests/test_protein_examples.py
  summary: Not yet run for a final published source ledger and generated site. Required
    before merging; this scoped report does not certify release readiness.
  evidence_ids:
  - implementation
evidence:
- evidence_id: checkpoint-probe
  kind: validation
  reference: https://github.com/CultureBotAI/DUFMech/issues/193
  locator: acquire at 9053fcf72 and test_lookup_never_appends_to_frozen_checkpoint
  accessed_at: '2026-10-13T02:09:23Z'
  support: supports
  summary: A temporary valid snapshot checkpoint was resumed with a new mocked accession.
    Its bytes changed and verified_manifest raised byte/checksum mismatches. No production
    artifact was changed.
- evidence_id: origin-probe
  kind: validation
  reference: https://github.com/CultureBotAI/DUFMech/issues/194
  locator: validate_rows at 9053fcf72 and provenance_validation regression cases
  accessed_at: '2026-10-13T02:09:23Z'
  support: supports
  summary: A fixture with commit main, blob/main URL and unsupported sequence_origin
    UNVERIFIED passed the baseline row validator.
- evidence_id: regressions
  kind: validation
  reference: tests/test_protein_examples.py
  locator: test_lookup_never_appends_to_frozen_checkpoint, test_lookup_rejects_symlinked_parent_before_network,
    provenance_validation parameter sets and valid registry mismatch test
  accessed_at: '2026-10-13T02:09:23Z'
  support: supports
  summary: Negative cases now reject manifest-owned checkpoint appends before network
    I/O, parent symlinks, mutable or inconsistent origins, unsupported origin/status
    pairs and malformed registry proof. Existing frozen data passes unchanged.
- evidence_id: implementation
  kind: record_content
  reference: src/dufmech/protein_examples.py
  locator: acquire, build_rows, validate_rows, write_snapshot; pages.render_from_paths;
    site.protein_examples_section and FASTA rendering
  accessed_at: '2026-10-13T02:09:23Z'
  support: supports
  summary: Coverage accounts for each worklist family; examples require exact current
    Pfam membership, preserve whole-protein sequences, and do not claim functional
    evidence. The renderer keeps all examples in JSON/FASTA, displays a bounded table
    and attribution, and requires native source pins.
assessments:
- assessment_id: retention
  area: ownership
  topic: Frozen checkpoint mutation guard
  outcome: supported
  summary: The explicit acquisition command still resumes staging files, but rejects
    a missing-entry append when a companion manifest owns that checkpoint, before
    constructing the request. Complete frozen replay remains read-only. Parent symlinks
    are rejected.
  target_ids:
  - src/dufmech/protein_examples.py
  - tests/test_protein_examples.py
  evidence_ids:
  - checkpoint-probe
  - regressions
- assessment_id: provenance
  area: provenance
  topic: Immutable origin and registry consistency
  outcome: supported
  summary: Both example and unresolved candidate origins require internally consistent
    immutable links and identifying fields. Sequence origin must agree with registry
    status; mirrors and differences carry valid registry commit/path/blob hash/version/release
    metadata and consistent sequence comparison.
  target_ids:
  - src/dufmech/protein_examples.py
  - tests/test_protein_examples.py
  evidence_ids:
  - origin-probe
  - regressions
- assessment_id: scope
  area: scope
  topic: Membership references do not promote functional claims
  outcome: supported
  summary: The rendering and loader integration preserves gap reporting, rejects unpinned
    native source files and supplies complete JSON/FASTA rather than silently truncating
    to ten displayed examples. Explicit membership and domain-boundary caveats remain.
    Functional assertions and canonical family projections are not changed.
  target_ids:
  - src/dufmech/pages.py
  - src/dufmech/site.py
  evidence_ids:
  - implementation
  - regressions
findings:
- finding_id: checkpoint-mutation
  issue_key: DUFMech-193
  category: ownership
  severity: major
  status: resolved
  certainty: confirmed
  title: Resuming acquisition could mutate a retained snapshot checkpoint
  description: The baseline appended new observations to manifest-owned .queries.jsonl
    files, invalidating historical evidence. The corrected code checks sibling manifests
    before network access and refuses the write.
  target_ids:
  - src/dufmech/protein_examples.py
  - tests/test_protein_examples.py
  field_paths:
  - acquire
  evidence_ids:
  - checkpoint-probe
  - regressions
  native_severity: high
  normalization_reason: Mapped to major because an ordinary resume could corrupt retained
    source evidence.
  ownership_note: Fix belongs to the native acquisition module and its focused tests,
    not frozen snapshots.
  disposition_reason: Reproduced on the original commit; corrected implementation
    passes no-request and unchanged-byte assertions and complete replay checks.
  external_issues:
  - https://github.com/CultureBotAI/DUFMech/issues/193
  previous_occurrences:
  - repository: CultureBotAI/DUFMech
    review_id: 20261013T021059Z-protein-example-baseline-review
    finding_id: checkpoint-mutation
- finding_id: unvalidated-provenance
  issue_key: DUFMech-194
  category: provenance
  severity: major
  status: resolved
  certainty: confirmed
  title: Row validation accepted mutable and unsupported origin provenance
  description: The baseline checked nonempty origins and only conditionally compared
    mirror hashes. The corrected validator enforces immutable origin URLs and commits
    plus consistent acquisition and registry metadata.
  target_ids:
  - src/dufmech/protein_examples.py
  - tests/test_protein_examples.py
  field_paths:
  - validate_rows
  evidence_ids:
  - origin-probe
  - regressions
  native_severity: medium
  normalization_reason: Mapped to major because accepted imported data is presented
    as verified, although no current production-row corruption was demonstrated.
  ownership_note: Fix belongs to the native row validator and regression fixtures;
    no frozen evidence rewrite is appropriate.
  disposition_reason: Mutable links, unsupported origins and invalid registry metadata
    now reject; both real datasets and valid mismatch examples pass.
  external_issues:
  - https://github.com/CultureBotAI/DUFMech/issues/194
  previous_occurrences:
  - repository: CultureBotAI/DUFMech
    review_id: 20261013T021059Z-protein-example-baseline-review
    finding_id: unvalidated-provenance
actions: []
limitations:
- Self-review, not independent approval or exhaustive adversarial filesystem/concurrency
  analysis.
- Full just qc, exact-head GitHub checks and retained source publication remain required
  after this report is committed. Their outcomes belong in PR 192, not a retroactive
  edit to this report.
- 5,190 family gaps, 15 rejected pairings and 114 unresolved discovery accession leads
  remain research work, not evidence of biological absence.
- The discovery manifest and pinned sibling commits are retained; full offline reproduction
  still needs the separately staged, verified discovery JSON input described in the
  provenance report.
- Source governance reports zero errors and 16 existing unresolved-license warnings.
  This review does not relicense the older combined cross-Mech bundle.
- No online source availability check or new scientific functional review was performed.
links:
- https://github.com/CultureBotAI/DUFMech/pull/192
- https://github.com/CultureBotAI/DUFMech/issues/193
- https://github.com/CultureBotAI/DUFMech/issues/194
tags:
- protein-examples
- adversarial-review
- provenance
related_reviews:
- repository: CultureBotAI/DUFMech
  review_id: 20261013T021059Z-protein-example-baseline-review
  relationship: Resolves both baseline findings after reproduced failures and regression-tested
    fixes.
```
