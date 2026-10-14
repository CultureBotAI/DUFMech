# PR 202 PF01973 adversarial publication audit

- Review: 20261014T230556Z-pr-202-pf01973-publication
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-14T22:55:45Z
- Finished UTC: 2026-10-14T23:05:56Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Initial source-pin drift was reproduced locally and in CI and tracked as issue 203. Candidate source capture, canonical rendering, source retention, integrity checks and responsive graph checks now pass. No additional blocking defect was found in this bounded adversarial self-review. Final audit-bearing checkpoint, full QC and exact-head CI remain subsequent release gates. Research findings remain open as issues 204 and 205.

## Scope And Provenance

Review all 15 initial PF01973 change paths and the candidate source ledger and canonical family page for unsupported claim transfer, provenance drift, output ownership and release readiness.

Selection: Explicit initial PR 202 changed-source set plus two publication surfaces; not random sampling.
Coverage: full; 17 reviewed / 17 in the declared population.
Source: working_tree at Git base bf3279f826a5fbb982f962dba292a3f033f1a288.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| conf/site_source_pins.json | conf/site_source_pins.json | source | conf/site_source_pins.json |
| curation/families/PF01973.yaml | curation/families/PF01973.yaml | source | curation/families/PF01973.yaml |
| data/families/PF01973.yaml | data/families/PF01973.yaml | source | data/families/PF01973.yaml |
| data/families/manifest.json | data/families/manifest.json | source | data/families/manifest.json |
| docs/causal-graphs.md | docs/causal-graphs.md | source | docs/causal-graphs.md |
| evidence/PF01973/coverage-and-exclusions.txt | evidence/PF01973/coverage-and-exclusions.txt | source | evidence/PF01973/coverage-and-exclusions.txt |
| evidence/PF01973/crecy-2012-mpte.txt | evidence/PF01973/crecy-2012-mpte.txt | source | evidence/PF01973/crecy-2012-mpte.txt |
| evidence/PF01973/member-mapping.txt | evidence/PF01973/member-mapping.txt | source | evidence/PF01973/member-mapping.txt |
| evidence/PF01973/sulzenbacher-2018-maf.txt | evidence/PF01973/sulzenbacher-2018-maf.txt | source | evidence/PF01973/sulzenbacher-2018-maf.txt |
| exports/kgx/nodes.tsv | exports/kgx/nodes.tsv | source | exports/kgx/nodes.tsv |
| exports/sssom/dufmech.sssom.tsv | exports/sssom/dufmech.sssom.tsv | source | exports/sssom/dufmech.sssom.tsv |
| history/records/PF01973/2026-10-14T222220Z-codex-7efd01.yaml | history/records/PF01973/2026-10-14T222220Z-codex-7efd01.yaml | source | history/records/PF01973/2026-10-14T222220Z-codex-7efd01.yaml |
| history/records/PF01973/2026-10-14T223424Z-codex-efe5ea.yaml | history/records/PF01973/2026-10-14T223424Z-codex-efe5ea.yaml | source | history/records/PF01973/2026-10-14T223424Z-codex-efe5ea.yaml |
| pages/families/PF01973.html | pages/families/PF01973.html | source | pages/families/PF01973.html |
| reports/causal_graphs/inventory.json | reports/causal_graphs/inventory.json | source | reports/causal_graphs/inventory.json |
| reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.md | reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.md | source | reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.md |
| reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.yaml | reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.yaml | source | reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.yaml |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Projection and export blast-radius audit | passed | True | data/families/PF01973.yaml, data/families/manifest.json, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, reports/causal_graphs/inventory.json | All 8296 manifest hashes verified; only PF01973 changes; frozen fields, evidence hashes/quotes, semantic digests and status-only export changes pass. |
| Graph and QC regression tests | passed | True | curation/families/PF01973.yaml, reports/causal_graphs/inventory.json | 52 tests passed in 21.98 seconds; not a scientific validation of all family members. |
| Candidate source-byte and canonical online retention verification | passed | True | conf/site_source_pins.json | All 9106 candidate source files match local bytes and canonical Git blobs retained by the annotated candidate tag. |
| Native canonical site regeneration | passed | True | pages/families/PF01973.html | Canonical site regenerated from the retained candidate checkpoint without hand edits. |
| Desktop/mobile canonical PF01973 graph checks | passed | True | pages/families/PF01973.html | 1440px and 390px checks pass eight graphs, sixteen edges, uncertainty labels, evidence disclosure, no document overflow and no JavaScript errors. Six screenshots inspected; temporary server closed. |

## Scientific And Domain Assessments

### Ownership, evidence scope and uninflated coverage

scope: supported. Targets: curation/families/PF01973.yaml, data/families/PF01973.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01973/coverage-and-exclusions.txt, evidence/PF01973/crecy-2012-mpte.txt, evidence/PF01973/member-mapping.txt, evidence/PF01973/sulzenbacher-2018-maf.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01973/2026-10-14T222220Z-codex-7efd01.yaml, history/records/PF01973/2026-10-14T223424Z-codex-efe5ea.yaml, reports/causal_graphs/inventory.json, reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.md, reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.yaml.

Sources and derived status/count changes are scoped to PF01973. Minimal evidence, append-only history/reviews, protein/domain distinctions and uncertainty are preserved. No kinase/glycosyltransferase transfer across the family, isolated-domain sufficiency or experimentally resolved residue chemistry is asserted.

### Retained candidate provenance and rendered uncertainty

provenance: supported. Targets: conf/site_source_pins.json, pages/families/PF01973.html.

The candidate ledger resolves to a canonical annotated checkpoint and its page correctly separates observed effects from hypotheses. Issue 203 is implemented for this candidate; closure waits for final audit-bearing source capture, full QC and exact-head CI.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| integrity | data/families/manifest.json; All 8296 manifests; structured YAML/JSON/TSV comparisons against c6a4d055de0a9ef0edc74f5c61cbbacfd8822904 | supports | Only PF01973 changes among family projections. Its overlay, review and inventory agree; all evidence hashes/quotes validate; two canonical history events remain. Exports change only its status, association edges stay unchanged, and frozen worklists are preserved. |
| scope | curation/families/PF01973.yaml; Eight graphs, sixteen edges, three discussions, four evidence ledgers, history, saved review and progress documentation | supports | Protein-specific archaeal chemistry, heterologous growth, Maf deletion/rescue and independent substitutions remain separate. Fourteen observed effects are distinct from two computational hypotheses. Spot checks of MptE Figure 4 caption and Maf Results pages 9/14/15 plus original Figure 5 confirm the bounded interpretations, including N491A. The original family review remains partial and IN_PROGRESS. |
| publication | https://github.com/CultureBotAI/DUFMech/issues/203; Initial source-pin exit 1; CI run 38650949208; candidate native capture, canonical online retention and browser checks | supports | Annotated source/dufmech-pr-202-candidate retains bf3279f826a5fbb982f962dba292a3f033f1a288. All 9106 candidate pins match canonical Git blobs. The canonical PF01973 page exposes eight graphs and sixteen edges with support labels and working evidence disclosures at 1440px and 390px. Final audit-bearing publication remains a separate check. |
| followups | reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.yaml; findings mpte-contexts and maf-contexts; GitHub issues 204 and 205 | supports | The saved source findings are preserved without closure. Issues 204/205 carry explicit acceptance criteria for exact archaeal constructs and later Maf/GlfM/Clostridium contexts, including the corrected 2024 supplement. Retrieval is not adoption. |

## Limits And Additional Notes

- Same-agent adversarial audit, not independent approval or a new completed family scientific review.
- The initial local full-QC attempt was interrupted after its reproduced pin failure: 288 passed, 1 failed in 223.19 seconds before interruption; this is not a full-suite result.
- The initial CI run 38650949208 failed at source retention before QC. Candidate fixes do not imply final full QC or deployment has already passed.
- Original pf01973-mpte-mechanistic-coverage and pf01973-maf-mechanism-and-member-coverage findings remain open, tracked in issues 204/205; this audit does not supersede them or any earlier family finding.
- Web-tool opens of the founding source URLs failed in this audit; previously retrieved hash-anchored XML/PDF originals were used for source spot checks.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T230556Z-pr-202-pf01973-publication
repository: CultureBotAI/DUFMech
kind: repository
source:
  git_revision: bf3279f826a5fbb982f962dba292a3f033f1a288
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: conf/site_source_pins.json
    sha256: b01ed94db854d7e995e5a6ed8bf6dc33f8ffd150096f41d6a975702b9bf55a92
    role: target
  - path: curation/families/PF01973.yaml
    sha256: 4c1e8d7477449e3df78434fa95769716be29edecf5cc016222d22ced0845123c
    role: target
  - path: data/families/PF01973.yaml
    sha256: 163fe50e3cf91f1f44457ae2eb5adc47f5341a5e5c2154ed56bcdc27352ef146
    role: target
  - path: data/families/manifest.json
    sha256: 654417fafff037e15665187b2480e9d01dc6d5c82a51b9de785e9f821e719369
    role: target
  - path: data/worklists/interpro-pfam-duf-2026-10-10.json
    sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383
    role: context
  - path: data/worklists/interpro-pfam-duf-2026-10-10.manifest.json
    sha256: 31c07ffb6a169c851ea0e6e9dd527a10c04028eafeb29187bd62dc2ae848696e
    role: context
  - path: data/worklists/interpro-pfam-duf-2026-10-10.tsv
    sha256: be023c8dd9d8d3864926b5032d6f7e87a884b1a567391696822dbbecc692dae7
    role: context
  - path: docs/causal-graphs.md
    sha256: 61f58331e3b60292a11ac217edb093b99d3dccfd858482d069d632d6a3f5de2a
    role: target
  - path: evidence/PF01973/coverage-and-exclusions.txt
    sha256: e8dfb09903c1b9c048feb162607bf73b70e1345f6f39a44aab93d2edcf694f54
    role: target
  - path: evidence/PF01973/crecy-2012-mpte.txt
    sha256: 601d231b6582bd80d75b93e37b0302e9364aacdf550993699782873891ce1492
    role: target
  - path: evidence/PF01973/member-mapping.txt
    sha256: 4391c8d7b3988527c816d37bc1101a4aea43562a283610afd7260a506ceeaada
    role: target
  - path: evidence/PF01973/sulzenbacher-2018-maf.txt
    sha256: d386fe9982f5703ceec75be5306af2e3ddee108f8a9be1fae34bf2b6bc7bb16b
    role: target
  - path: exports/kgx/nodes.tsv
    sha256: 11aa0eb965fed408b0f652def482b6ccc4531e27facbf84ef828a7c89dbc2acc
    role: target
  - path: exports/sssom/dufmech.sssom.tsv
    sha256: 8c9060d2c072a5375ca02c98a1585d155b0393379de85123347d22077940be8d
    role: target
  - path: history/records/PF01973/2026-10-14T222220Z-codex-7efd01.yaml
    sha256: 9a43d8d2a7bedb3447573ff233d7977ab94f32b9793de595ec74da82e0d13312
    role: target
  - path: history/records/PF01973/2026-10-14T223424Z-codex-efe5ea.yaml
    sha256: 1d8ea7ac9e0b75ec79b312ad65be0cde447143b801e5fbd099e46b483172f03f
    role: target
  - path: pages/families/PF01973.html
    sha256: a7e2ec7df40758ac4aaea1da75a17219785dc998889b2e54d5666242a9d165b7
    role: target
  - path: reports/causal_graphs/inventory.json
    sha256: b6294f4c7380f7b40e3aa1234fb1889a6a0cea12c29d2e0af759206e0990ea2b
    role: target
  - path: reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.md
    sha256: f103d53d225b283e53e2fd93049cbaee9e1bf99bf2f145f6463be2eeba7bbc37
    role: target
  - path: reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.yaml
    sha256: 5fb590581c4b3ffd77b53d62e79ed8fc31d738b6198d1d7ee4fab799405c3248
    role: target
  - path: src/dufmech/site_sources.py
    role: context
    sha256: bad39b4cb1d578ddec9c8ee5b415411110391e6f290b9e96651c550ef5738d65
  - path: src/dufmech/qc.py
    role: context
    sha256: e75e5080000578ef5b794147fbd138810de552da9eb241d2cb7612322c093d6e
targets:
- target_id: conf/site_source_pins.json
  path: conf/site_source_pins.json
  label: conf/site_source_pins.json
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: curation/families/PF01973.yaml
  path: curation/families/PF01973.yaml
  label: curation/families/PF01973.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: data/families/PF01973.yaml
  path: data/families/PF01973.yaml
  label: data/families/PF01973.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: data/families/manifest.json
  path: data/families/manifest.json
  label: data/families/manifest.json
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: docs/causal-graphs.md
  path: docs/causal-graphs.md
  label: docs/causal-graphs.md
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: evidence/PF01973/coverage-and-exclusions.txt
  path: evidence/PF01973/coverage-and-exclusions.txt
  label: evidence/PF01973/coverage-and-exclusions.txt
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: evidence/PF01973/crecy-2012-mpte.txt
  path: evidence/PF01973/crecy-2012-mpte.txt
  label: evidence/PF01973/crecy-2012-mpte.txt
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: evidence/PF01973/member-mapping.txt
  path: evidence/PF01973/member-mapping.txt
  label: evidence/PF01973/member-mapping.txt
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: evidence/PF01973/sulzenbacher-2018-maf.txt
  path: evidence/PF01973/sulzenbacher-2018-maf.txt
  label: evidence/PF01973/sulzenbacher-2018-maf.txt
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: exports/kgx/nodes.tsv
  path: exports/kgx/nodes.tsv
  label: exports/kgx/nodes.tsv
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: exports/sssom/dufmech.sssom.tsv
  path: exports/sssom/dufmech.sssom.tsv
  label: exports/sssom/dufmech.sssom.tsv
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: history/records/PF01973/2026-10-14T222220Z-codex-7efd01.yaml
  path: history/records/PF01973/2026-10-14T222220Z-codex-7efd01.yaml
  label: history/records/PF01973/2026-10-14T222220Z-codex-7efd01.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: history/records/PF01973/2026-10-14T223424Z-codex-efe5ea.yaml
  path: history/records/PF01973/2026-10-14T223424Z-codex-efe5ea.yaml
  label: history/records/PF01973/2026-10-14T223424Z-codex-efe5ea.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: pages/families/PF01973.html
  path: pages/families/PF01973.html
  label: pages/families/PF01973.html
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: reports/causal_graphs/inventory.json
  path: reports/causal_graphs/inventory.json
  label: reports/causal_graphs/inventory.json
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.md
  path: reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.md
  label: reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.md
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.yaml
  path: reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.yaml
  label: reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
title: PR 202 PF01973 adversarial publication audit
started_at: '2026-10-14T22:55:45Z'
finished_at: '2026-10-14T23:05:56Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: The publishing agent challenged the source claims, generated
    scope and release readiness. No separate reviewer or independent scientific approval
    is claimed.
skill: .claude/skills/review-repo/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: false
summary: Initial source-pin drift was reproduced locally and in CI and tracked as
  issue 203. Candidate source capture, canonical rendering, source retention, integrity
  checks and responsive graph checks now pass. No additional blocking defect was found
  in this bounded adversarial self-review. Final audit-bearing checkpoint, full QC
  and exact-head CI remain subsequent release gates. Research findings remain open
  as issues 204 and 205.
scope:
  description: Review all 15 initial PF01973 change paths and the candidate source
    ledger and canonical family page for unsupported claim transfer, provenance drift,
    output ownership and release readiness.
  selection: Explicit initial PR 202 changed-source set plus two publication surfaces;
    not random sampling.
  coverage: full
  population_size: 17
  reviewed_target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01973.yaml
  - data/families/PF01973.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01973/coverage-and-exclusions.txt
  - evidence/PF01973/crecy-2012-mpte.txt
  - evidence/PF01973/member-mapping.txt
  - evidence/PF01973/sulzenbacher-2018-maf.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01973/2026-10-14T222220Z-codex-7efd01.yaml
  - history/records/PF01973/2026-10-14T223424Z-codex-efe5ea.yaml
  - pages/families/PF01973.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.md
  - reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.yaml
  exclusions:
  - target: Independent scientific review and full PF01973/corpus characterization
    reason: Primary spot checks challenge the declared scope; later members, exact
      historical constructs and unresolved molecular controls remain follow-ups.
  - target: Final audit-bearing publication revision and deployment
    reason: This retained report requires its own source checkpoint and regeneration.
      Final full QC, exact-head CI and deployment checks occur after retention.
checks:
- check_id: integrity
  name: Projection and export blast-radius audit
  command: PYTHONPATH=src:/private/tmp/dufmech-protein-claw/src .venv/bin/python /private/tmp/duf-pf01973-integrity.py
  status: passed
  required: true
  exit_code: 0
  summary: All 8296 manifest hashes verified; only PF01973 changes; frozen fields,
    evidence hashes/quotes, semantic digests and status-only export changes pass.
  target_ids:
  - data/families/PF01973.yaml
  - data/families/manifest.json
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - reports/causal_graphs/inventory.json
  evidence_ids:
  - integrity
- check_id: regressions
  name: Graph and QC regression tests
  command: PYTHONPATH=src:/private/tmp/dufmech-protein-claw/src .venv/bin/python -m
    pytest -q tests/test_causal_graphs.py tests/test_qc.py
  status: passed
  required: true
  exit_code: 0
  summary: 52 tests passed in 21.98 seconds; not a scientific validation of all family
    members.
  target_ids:
  - curation/families/PF01973.yaml
  - reports/causal_graphs/inventory.json
  evidence_ids:
  - integrity
- check_id: retention
  name: Candidate source-byte and canonical online retention verification
  command: just site-sources-published
  status: passed
  required: true
  exit_code: 0
  summary: All 9106 candidate source files match local bytes and canonical Git blobs
    retained by the annotated candidate tag.
  target_ids:
  - conf/site_source_pins.json
  evidence_ids:
  - publication
- check_id: render
  name: Native canonical site regeneration
  command: just render
  status: passed
  required: true
  exit_code: 0
  summary: Canonical site regenerated from the retained candidate checkpoint without
    hand edits.
  target_ids:
  - pages/families/PF01973.html
  evidence_ids:
  - publication
- check_id: browser
  name: Desktop/mobile canonical PF01973 graph checks
  command: node /private/tmp/duf-pf01973-browser.cjs
  status: passed
  required: true
  exit_code: 0
  summary: 1440px and 390px checks pass eight graphs, sixteen edges, uncertainty labels,
    evidence disclosure, no document overflow and no JavaScript errors. Six screenshots
    inspected; temporary server closed.
  target_ids:
  - pages/families/PF01973.html
  evidence_ids:
  - publication
evidence:
- evidence_id: integrity
  kind: validation
  reference: data/families/manifest.json
  locator: All 8296 manifests; structured YAML/JSON/TSV comparisons against c6a4d055de0a9ef0edc74f5c61cbbacfd8822904
  accessed_at: '2026-10-14T23:05:56Z'
  support: supports
  summary: Only PF01973 changes among family projections. Its overlay, review and
    inventory agree; all evidence hashes/quotes validate; two canonical history events
    remain. Exports change only its status, association edges stay unchanged, and
    frozen worklists are preserved.
- evidence_id: scope
  kind: record_content
  reference: curation/families/PF01973.yaml
  locator: Eight graphs, sixteen edges, three discussions, four evidence ledgers,
    history, saved review and progress documentation
  accessed_at: '2026-10-14T23:05:56Z'
  support: supports
  summary: Protein-specific archaeal chemistry, heterologous growth, Maf deletion/rescue
    and independent substitutions remain separate. Fourteen observed effects are distinct
    from two computational hypotheses. Spot checks of MptE Figure 4 caption and Maf
    Results pages 9/14/15 plus original Figure 5 confirm the bounded interpretations,
    including N491A. The original family review remains partial and IN_PROGRESS.
- evidence_id: publication
  kind: validation
  reference: https://github.com/CultureBotAI/DUFMech/issues/203
  locator: Initial source-pin exit 1; CI run 38650949208; candidate native capture,
    canonical online retention and browser checks
  accessed_at: '2026-10-14T23:05:56Z'
  support: supports
  summary: Annotated source/dufmech-pr-202-candidate retains bf3279f826a5fbb982f962dba292a3f033f1a288.
    All 9106 candidate pins match canonical Git blobs. The canonical PF01973 page
    exposes eight graphs and sixteen edges with support labels and working evidence
    disclosures at 1440px and 390px. Final audit-bearing publication remains a separate
    check.
- evidence_id: followups
  kind: record_content
  reference: reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.yaml
  locator: findings mpte-contexts and maf-contexts; GitHub issues 204 and 205
  accessed_at: '2026-10-14T23:05:56Z'
  support: supports
  summary: The saved source findings are preserved without closure. Issues 204/205
    carry explicit acceptance criteria for exact archaeal constructs and later Maf/GlfM/Clostridium
    contexts, including the corrected 2024 supplement. Retrieval is not adoption.
assessments:
- assessment_id: bounded-curation
  area: scope
  topic: Ownership, evidence scope and uninflated coverage
  outcome: supported
  target_ids:
  - curation/families/PF01973.yaml
  - data/families/PF01973.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01973/coverage-and-exclusions.txt
  - evidence/PF01973/crecy-2012-mpte.txt
  - evidence/PF01973/member-mapping.txt
  - evidence/PF01973/sulzenbacher-2018-maf.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01973/2026-10-14T222220Z-codex-7efd01.yaml
  - history/records/PF01973/2026-10-14T223424Z-codex-efe5ea.yaml
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.md
  - reviews/structured/20261014T223640Z-pf01973-mpte-and-maf-contexts/review.yaml
  evidence_ids:
  - integrity
  - scope
  - followups
  summary: Sources and derived status/count changes are scoped to PF01973. Minimal
    evidence, append-only history/reviews, protein/domain distinctions and uncertainty
    are preserved. No kinase/glycosyltransferase transfer across the family, isolated-domain
    sufficiency or experimentally resolved residue chemistry is asserted.
- assessment_id: candidate-publication
  area: provenance
  topic: Retained candidate provenance and rendered uncertainty
  outcome: supported
  target_ids:
  - conf/site_source_pins.json
  - pages/families/PF01973.html
  evidence_ids:
  - publication
  summary: The candidate ledger resolves to a canonical annotated checkpoint and its
    page correctly separates observed effects from hypotheses. Issue 203 is implemented
    for this candidate; closure waits for final audit-bearing source capture, full
    QC and exact-head CI.
findings: []
actions: []
limitations:
- Same-agent adversarial audit, not independent approval or a new completed family
  scientific review.
- 'The initial local full-QC attempt was interrupted after its reproduced pin failure:
  288 passed, 1 failed in 223.19 seconds before interruption; this is not a full-suite
  result.'
- The initial CI run 38650949208 failed at source retention before QC. Candidate fixes
  do not imply final full QC or deployment has already passed.
- Original pf01973-mpte-mechanistic-coverage and pf01973-maf-mechanism-and-member-coverage
  findings remain open, tracked in issues 204/205; this audit does not supersede them
  or any earlier family finding.
- Web-tool opens of the founding source URLs failed in this audit; previously retrieved
  hash-anchored XML/PDF originals were used for source spot checks.
tags:
- adversarial-self-review
- pr-202
- pf01973
- publication
```
