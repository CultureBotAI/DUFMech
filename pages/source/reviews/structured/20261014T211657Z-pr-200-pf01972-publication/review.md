# PR 200 PF01972 adversarial publication audit

- Review: 20261014T211657Z-pr-200-pf01972-publication
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-14T21:08:39Z
- Finished UTC: 2026-10-14T21:16:57Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

The initial source-pin failure was reproduced and tracked as GitHub issue 201. The inspected candidate now has a published annotated checkpoint, verified source bytes and regenerated canonical PF01972 graphs with distinct experimental/hypothetical labels. Source preservation, projection/review/inventory agreement and status-only export changes pass. No additional blocking defect was found in this scoped same-agent audit. Final audit-bearing checkpoint, whole-repository QC and exact-head CI remain release gates after this report is retained; no scientific coverage finding is retired.

## Scope And Provenance

Inspect all 15 initial PF01972 change paths plus candidate source ledger and canonical family page; challenge unsupported mechanistic transfer, immutable-source changes, generated drift and publication readiness.

Selection: Explicit PR 200 changed-source set and publication surfaces; no random sampling.
Coverage: full; 17 reviewed / 17 in the declared population.
Source: working_tree at Git base b6793ba2005e4429f0cef96a31a328825e655a00.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| conf/site_source_pins.json | conf/site_source_pins.json | source | conf/site_source_pins.json |
| curation/families/PF01972.yaml | curation/families/PF01972.yaml | source | curation/families/PF01972.yaml |
| data/families/PF01972.yaml | data/families/PF01972.yaml | source | data/families/PF01972.yaml |
| data/families/manifest.json | data/families/manifest.json | source | data/families/manifest.json |
| docs/causal-graphs.md | docs/causal-graphs.md | source | docs/causal-graphs.md |
| evidence/PF01972/ammelburg-2011-casein.txt | evidence/PF01972/ammelburg-2011-casein.txt | source | evidence/PF01972/ammelburg-2011-casein.txt |
| evidence/PF01972/coverage-and-exclusions.txt | evidence/PF01972/coverage-and-exclusions.txt | source | evidence/PF01972/coverage-and-exclusions.txt |
| evidence/PF01972/member-mapping.txt | evidence/PF01972/member-mapping.txt | source | evidence/PF01972/member-mapping.txt |
| evidence/PF01972/pandit-2004-prediction.txt | evidence/PF01972/pandit-2004-prediction.txt | source | evidence/PF01972/pandit-2004-prediction.txt |
| exports/kgx/nodes.tsv | exports/kgx/nodes.tsv | source | exports/kgx/nodes.tsv |
| exports/sssom/dufmech.sssom.tsv | exports/sssom/dufmech.sssom.tsv | source | exports/sssom/dufmech.sssom.tsv |
| history/records/PF01972/2026-10-14T204247Z-codex-3b40ac.yaml | history/records/PF01972/2026-10-14T204247Z-codex-3b40ac.yaml | source | history/records/PF01972/2026-10-14T204247Z-codex-3b40ac.yaml |
| history/records/PF01972/2026-10-14T204946Z-codex-4713e3.yaml | history/records/PF01972/2026-10-14T204946Z-codex-4713e3.yaml | source | history/records/PF01972/2026-10-14T204946Z-codex-4713e3.yaml |
| pages/families/PF01972.html | pages/families/PF01972.html | source | pages/families/PF01972.html |
| reports/causal_graphs/inventory.json | reports/causal_graphs/inventory.json | source | reports/causal_graphs/inventory.json |
| reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.md | reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.md | source | reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.md |
| reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.yaml | reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.yaml | source | reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.yaml |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Projection and export blast-radius audit | passed | True | data/families/PF01972.yaml, data/families/manifest.json, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, reports/causal_graphs/inventory.json | Native record validation passed; all 8296 manifest hashes verified; only PF01972 differs from main; frozen fields, overlay equivalence, semantic review/inventory digests and status-only exports verified. |
| Focused native graph and QC regressions | passed | True | curation/families/PF01972.yaml, reports/causal_graphs/inventory.json | 52 tests passed in 19.82 seconds. This does not certify biological causality. |
| Candidate source-pin verification | passed | True | conf/site_source_pins.json | 9098 source pins match local bytes at candidate b6793ba2005e4429f0cef96a31a328825e655a00. |
| Canonical online checkpoint retention | passed | True | conf/site_source_pins.json | All 9098 candidate source files verified against the canonical remote and annotated source/dufmech-pr-200-candidate tag. |
| Canonical PF01972 desktop and mobile rendering | passed | True | pages/families/PF01972.html | 1440px and 390px: two graphs, two edges, explicit support/scope labels, working evidence disclosures, no page overflow or JavaScript errors. Screenshots inspected. |

## Scientific And Domain Assessments

### Curation ownership, evidence classes and uninflated coverage

scope: supported. Targets: curation/families/PF01972.yaml, data/families/PF01972.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01972/ammelburg-2011-casein.txt, evidence/PF01972/coverage-and-exclusions.txt, evidence/PF01972/member-mapping.txt, evidence/PF01972/pandit-2004-prediction.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01972/2026-10-14T204247Z-codex-3b40ac.yaml, history/records/PF01972/2026-10-14T204946Z-codex-4713e3.yaml, reports/causal_graphs/inventory.json, reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.md, reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.yaml.

The source changes are limited to PF01972 and its derived counts/statuses. Human overlay ownership, canonical history and retained scientific limitations are preserved; no untested SDH microstep, defense phenotype or family-wide experimental characterization is asserted.

### Retained candidate bytes and rendered uncertainty

provenance: supported. Targets: conf/site_source_pins.json, pages/families/PF01972.html.

Candidate pins resolve to an annotated canonical tag and match actual bytes. The generated page retains observation/hypothesis distinctions and evidence. Publication fix 201 is implemented for the inspected candidate, but issue closure waits for final QC and exact-head CI.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| integrity | data/families/manifest.json; All 8296 hashes compared with actual files; prior main 2da6c366b06615fbb6c34379318771fe09f4cfda; structured YAML/JSON/TSV comparison | supports | Only PF01972 changes scientific projection content. The retained review and inventory bind the same semantic digest; KGX and SSSOM change only its curation-status representation; association edges are unchanged. Both history events and the existing review are preserved. |
| scope | curation/families/PF01972.yaml; Both causal graphs, all three open discussions and four evidence extracts; docs progress and continuation checkpoint | supports | The assay-level observation and computational hypothesis remain separate and UNRESOLVED in directness. Missing controls, historical clone identity, catalytic proof and broader coverage remain explicit; IN_PROGRESS is not promoted. Reinspected thesis pages 90-91 and original Figure24 plus founding-paper Methods text; no new experimental claim was added. |
| publication | https://github.com/CultureBotAI/DUFMech/issues/201; Initial source-pin exit 1 and initial CI run 38638205011; candidate source capture, online retention result and canonical browser checks | supports | Initial CI failed at the same stale PF01972 source-pin check reproduced locally. Native capture from the published annotated candidate fixes byte agreement. Canonical rendering and responsive graph disclosure checks now pass. The source tag must be preserved after branch deletion; final exact-head checks are still required. |

## Limits And Additional Notes

- Same-agent adversarial audit, not independent approval or a new full family scientific review.
- The existing pf01972-causal-context-coverage finding and earlier corpus follow-ups remain open; this repository review does not supersede them.
- No claim that full QC, final CI, merge or deployment has already passed. These are checked separately against the final audit-bearing revision.
- Initial temporary integrity-helper import and digest-key mistakes were corrected before its successful run; no repository application code changed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T211657Z-pr-200-pf01972-publication
repository: CultureBotAI/DUFMech
kind: repository
source:
  git_revision: b6793ba2005e4429f0cef96a31a328825e655a00
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: conf/site_source_pins.json
    sha256: 33b0a14f593809f0bb64f6925b8d88ff1fa22937b7c146822aa46ad8790b8e79
    role: target
  - path: curation/families/PF01972.yaml
    sha256: 9c0fa29bdb7cb5678deaec4e25fcf62b31cda52076f9493d5dc65d67089c8262
    role: target
  - path: data/families/PF01972.yaml
    sha256: 8590809e3b2af2e158466642eb3660cd81f845fe3fec5c69c1c7db64b78fa8f2
    role: target
  - path: data/families/manifest.json
    sha256: 444d3638697e389314096ab985636a9009c23bde76101bd341346390a53f8c5d
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
    sha256: 3dc4319ea142554ea1d05b1ec9b1f2ad2e3144930567dca98fd4480d60fbc29f
    role: target
  - path: evidence/PF01972/ammelburg-2011-casein.txt
    sha256: 37e12d65ba5695e667e9c08bbb231cf2de389925112f2f95f5b1e031b510d856
    role: target
  - path: evidence/PF01972/coverage-and-exclusions.txt
    sha256: ed3e8a17b0feba6bacdd3d3affa0e00d6962fc321edeba5c3d02bbc9e57d9eb3
    role: target
  - path: evidence/PF01972/member-mapping.txt
    sha256: 9c81e76b1590a5b3c25336a41aba9bdaf3ec5fd74036370a5ea3c19cf04dfbe2
    role: target
  - path: evidence/PF01972/pandit-2004-prediction.txt
    sha256: 9a52c87650b016af7f97fd3ffc98ea0874c394470cfd0785da3fc38e50413c49
    role: target
  - path: exports/kgx/nodes.tsv
    sha256: 3c035a18d83ba797c89bf2e31fd3fe29f9be9b75e9a1617371ad5b6e4a6d422e
    role: target
  - path: exports/sssom/dufmech.sssom.tsv
    sha256: 6140c4a77cc5a394380e9e14877ac18ff9b15caaed29caf5f71bd68dfcd9c4d3
    role: target
  - path: history/records/PF01972/2026-10-14T204247Z-codex-3b40ac.yaml
    sha256: 15ca61f7b91b401e424f586ef4989307ac249ce5d6cdc1343939f1ee300cbf40
    role: target
  - path: history/records/PF01972/2026-10-14T204946Z-codex-4713e3.yaml
    sha256: dda9fc58d7f9b1d97219b35d4ed761456a2c3a25861b21ab3f7a86a0c746b49e
    role: target
  - path: pages/families/PF01972.html
    sha256: ca477ee70e159b89c56c8efdbcb7c8f7f157e91e9c6819c335f229b42c41279e
    role: target
  - path: reports/causal_graphs/inventory.json
    sha256: 9e8a6bc342ffdaf26ad0fd0e60ae191fadff3f22f6d408ba006cfa055e495168
    role: target
  - path: reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.md
    sha256: 01093fb05ab9a9b1762489f13ce2c9f1113dcd43f1fb9e8be2a1059253d51b65
    role: target
  - path: reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.yaml
    sha256: 01216b5533b71e0d63463bd933d6a66f4099d0cf3c3ad35055fc9267f7b7941f
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
- target_id: curation/families/PF01972.yaml
  path: curation/families/PF01972.yaml
  label: curation/families/PF01972.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: data/families/PF01972.yaml
  path: data/families/PF01972.yaml
  label: data/families/PF01972.yaml
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
- target_id: evidence/PF01972/ammelburg-2011-casein.txt
  path: evidence/PF01972/ammelburg-2011-casein.txt
  label: evidence/PF01972/ammelburg-2011-casein.txt
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: evidence/PF01972/coverage-and-exclusions.txt
  path: evidence/PF01972/coverage-and-exclusions.txt
  label: evidence/PF01972/coverage-and-exclusions.txt
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: evidence/PF01972/member-mapping.txt
  path: evidence/PF01972/member-mapping.txt
  label: evidence/PF01972/member-mapping.txt
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: evidence/PF01972/pandit-2004-prediction.txt
  path: evidence/PF01972/pandit-2004-prediction.txt
  label: evidence/PF01972/pandit-2004-prediction.txt
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
- target_id: history/records/PF01972/2026-10-14T204247Z-codex-3b40ac.yaml
  path: history/records/PF01972/2026-10-14T204247Z-codex-3b40ac.yaml
  label: history/records/PF01972/2026-10-14T204247Z-codex-3b40ac.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: history/records/PF01972/2026-10-14T204946Z-codex-4713e3.yaml
  path: history/records/PF01972/2026-10-14T204946Z-codex-4713e3.yaml
  label: history/records/PF01972/2026-10-14T204946Z-codex-4713e3.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: pages/families/PF01972.html
  path: pages/families/PF01972.html
  label: pages/families/PF01972.html
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: reports/causal_graphs/inventory.json
  path: reports/causal_graphs/inventory.json
  label: reports/causal_graphs/inventory.json
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.md
  path: reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.md
  label: reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.md
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.yaml
  path: reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.yaml
  label: reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
title: PR 200 PF01972 adversarial publication audit
started_at: '2026-10-14T21:08:39Z'
finished_at: '2026-10-14T21:16:57Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: The publishing agent challenged the existing curation, source
    boundaries, generated scope and release readiness. No separate reviewer or independent
    expert approval is claimed.
skill: .claude/skills/review-repo/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: false
summary: The initial source-pin failure was reproduced and tracked as GitHub issue
  201. The inspected candidate now has a published annotated checkpoint, verified
  source bytes and regenerated canonical PF01972 graphs with distinct experimental/hypothetical
  labels. Source preservation, projection/review/inventory agreement and status-only
  export changes pass. No additional blocking defect was found in this scoped same-agent
  audit. Final audit-bearing checkpoint, whole-repository QC and exact-head CI remain
  release gates after this report is retained; no scientific coverage finding is retired.
scope:
  description: Inspect all 15 initial PF01972 change paths plus candidate source ledger
    and canonical family page; challenge unsupported mechanistic transfer, immutable-source
    changes, generated drift and publication readiness.
  selection: Explicit PR 200 changed-source set and publication surfaces; no random
    sampling.
  coverage: full
  population_size: 17
  reviewed_target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01972.yaml
  - data/families/PF01972.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01972/ammelburg-2011-casein.txt
  - evidence/PF01972/coverage-and-exclusions.txt
  - evidence/PF01972/member-mapping.txt
  - evidence/PF01972/pandit-2004-prediction.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01972/2026-10-14T204247Z-codex-3b40ac.yaml
  - history/records/PF01972/2026-10-14T204946Z-codex-4713e3.yaml
  - pages/families/PF01972.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.md
  - reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.yaml
  exclusions:
  - target: Independent scientific review and corpus-wide experiments
    reason: Primary source spot checks assess the declared limits, not every family
      or the unresolved historical construct, controls, products, residue chemistry
      and later structural-study experiments.
  - target: Final audit-bearing publication revision and GitHub deployment
    reason: This report must itself be retained in a new source checkpoint. Recapture,
      deterministic regeneration, full QC and exact-head CI are mandatory subsequent
      release checks.
checks:
- check_id: integrity
  name: Projection and export blast-radius audit
  command: PYTHONPATH=src .venv/bin/python /private/tmp/duf-pr200-integrity.py
  status: passed
  required: true
  exit_code: 0
  summary: Native record validation passed; all 8296 manifest hashes verified; only
    PF01972 differs from main; frozen fields, overlay equivalence, semantic review/inventory
    digests and status-only exports verified.
  target_ids:
  - data/families/PF01972.yaml
  - data/families/manifest.json
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - reports/causal_graphs/inventory.json
  evidence_ids:
  - integrity
- check_id: regressions
  name: Focused native graph and QC regressions
  command: PYTHONPATH=src:/private/tmp/dufmech-protein-claw/src .venv/bin/python -m
    pytest -q tests/test_causal_graphs.py tests/test_qc.py
  status: passed
  required: true
  exit_code: 0
  summary: 52 tests passed in 19.82 seconds. This does not certify biological causality.
  target_ids:
  - curation/families/PF01972.yaml
  - reports/causal_graphs/inventory.json
  evidence_ids:
  - integrity
- check_id: source-bytes
  name: Candidate source-pin verification
  command: PYTHONPATH=src .venv/bin/python -m dufmech.site_sources check
  status: passed
  required: true
  exit_code: 0
  summary: 9098 source pins match local bytes at candidate b6793ba2005e4429f0cef96a31a328825e655a00.
  target_ids:
  - conf/site_source_pins.json
  evidence_ids:
  - publication
- check_id: retention
  name: Canonical online checkpoint retention
  command: just site-sources-published
  status: passed
  required: true
  exit_code: 0
  summary: All 9098 candidate source files verified against the canonical remote and
    annotated source/dufmech-pr-200-candidate tag.
  target_ids:
  - conf/site_source_pins.json
  evidence_ids:
  - publication
- check_id: browser
  name: Canonical PF01972 desktop and mobile rendering
  command: DUF_SITE_ROOT=/private/tmp/dufmech-causal-graphs/pages node /private/tmp/duf-pf01972-browser.cjs
  status: passed
  required: true
  exit_code: 0
  summary: '1440px and 390px: two graphs, two edges, explicit support/scope labels,
    working evidence disclosures, no page overflow or JavaScript errors. Screenshots
    inspected.'
  target_ids:
  - pages/families/PF01972.html
  evidence_ids:
  - publication
evidence:
- evidence_id: integrity
  kind: validation
  reference: data/families/manifest.json
  locator: All 8296 hashes compared with actual files; prior main 2da6c366b06615fbb6c34379318771fe09f4cfda;
    structured YAML/JSON/TSV comparison
  accessed_at: '2026-10-14T21:16:57Z'
  support: supports
  summary: Only PF01972 changes scientific projection content. The retained review
    and inventory bind the same semantic digest; KGX and SSSOM change only its curation-status
    representation; association edges are unchanged. Both history events and the existing
    review are preserved.
- evidence_id: scope
  kind: record_content
  reference: curation/families/PF01972.yaml
  locator: Both causal graphs, all three open discussions and four evidence extracts;
    docs progress and continuation checkpoint
  accessed_at: '2026-10-14T21:16:57Z'
  support: supports
  summary: The assay-level observation and computational hypothesis remain separate
    and UNRESOLVED in directness. Missing controls, historical clone identity, catalytic
    proof and broader coverage remain explicit; IN_PROGRESS is not promoted. Reinspected
    thesis pages 90-91 and original Figure24 plus founding-paper Methods text; no
    new experimental claim was added.
- evidence_id: publication
  kind: validation
  reference: https://github.com/CultureBotAI/DUFMech/issues/201
  locator: Initial source-pin exit 1 and initial CI run 38638205011; candidate source
    capture, online retention result and canonical browser checks
  accessed_at: '2026-10-14T21:16:57Z'
  support: supports
  summary: Initial CI failed at the same stale PF01972 source-pin check reproduced
    locally. Native capture from the published annotated candidate fixes byte agreement.
    Canonical rendering and responsive graph disclosure checks now pass. The source
    tag must be preserved after branch deletion; final exact-head checks are still
    required.
assessments:
- assessment_id: bounded-curation
  area: scope
  topic: Curation ownership, evidence classes and uninflated coverage
  outcome: supported
  target_ids:
  - curation/families/PF01972.yaml
  - data/families/PF01972.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01972/ammelburg-2011-casein.txt
  - evidence/PF01972/coverage-and-exclusions.txt
  - evidence/PF01972/member-mapping.txt
  - evidence/PF01972/pandit-2004-prediction.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01972/2026-10-14T204247Z-codex-3b40ac.yaml
  - history/records/PF01972/2026-10-14T204946Z-codex-4713e3.yaml
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.md
  - reviews/structured/20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis/review.yaml
  evidence_ids:
  - scope
  - integrity
  summary: The source changes are limited to PF01972 and its derived counts/statuses.
    Human overlay ownership, canonical history and retained scientific limitations
    are preserved; no untested SDH microstep, defense phenotype or family-wide experimental
    characterization is asserted.
- assessment_id: candidate-publication
  area: provenance
  topic: Retained candidate bytes and rendered uncertainty
  outcome: supported
  target_ids:
  - conf/site_source_pins.json
  - pages/families/PF01972.html
  evidence_ids:
  - publication
  summary: Candidate pins resolve to an annotated canonical tag and match actual bytes.
    The generated page retains observation/hypothesis distinctions and evidence. Publication
    fix 201 is implemented for the inspected candidate, but issue closure waits for
    final QC and exact-head CI.
findings: []
actions: []
limitations:
- Same-agent adversarial audit, not independent approval or a new full family scientific
  review.
- The existing pf01972-causal-context-coverage finding and earlier corpus follow-ups
  remain open; this repository review does not supersede them.
- No claim that full QC, final CI, merge or deployment has already passed. These are
  checked separately against the final audit-bearing revision.
- Initial temporary integrity-helper import and digest-key mistakes were corrected
  before its successful run; no repository application code changed.
tags:
- adversarial-self-review
- pr-200
- pf01972
- publication
```
