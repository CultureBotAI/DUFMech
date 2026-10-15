# PR 211 PF01976 graphless assessment adversarial publication audit

- Review: 20261015T045541Z-pr-211-pf01976-publication
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-15T04:46:36Z
- Finished UTC: 2026-10-15T04:55:41Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

The reproduced stale-pin publication blocker is tracked in issue 212. Candidate retention, native rendering, responsive checks, evidence-boundary rechecks and corpus preservation pass. No additional blocking defect was established in this bounded same-agent review. Final audit-bearing capture, full QC, exact-head CI and deployment remain subsequent release gates. Scientific issues 213-215 remain open.

## Scope And Provenance

Twelve changed source/artifact paths plus the source-pin ledger and canonical PF01976 page. Check graphless evidence boundaries, exact reference/domain attribution, source ownership, append-only history/reviews, corpus preservation and candidate publication.

Selection: Explicit PR changed-source set plus two publication surfaces, not a random sample or corpus-wide scientific review.
Coverage: full; 14 reviewed / 14 in the declared population.
Source: working_tree at Git base 13b3b6b3058c22af38a792ecf6aafd436ea91dcd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| conf/site_source_pins.json | conf/site_source_pins.json | source | conf/site_source_pins.json |
| curation/families/PF01976.yaml | curation/families/PF01976.yaml | source | curation/families/PF01976.yaml |
| data/families/PF01976.yaml | data/families/PF01976.yaml | source | data/families/PF01976.yaml |
| data/families/manifest.json | data/families/manifest.json | source | data/families/manifest.json |
| docs/causal-graphs.md | docs/causal-graphs.md | source | docs/causal-graphs.md |
| evidence/PF01976/causal-evidence-assessment.txt | evidence/PF01976/causal-evidence-assessment.txt | source | evidence/PF01976/causal-evidence-assessment.txt |
| exports/kgx/nodes.tsv | exports/kgx/nodes.tsv | source | exports/kgx/nodes.tsv |
| exports/sssom/dufmech.sssom.tsv | exports/sssom/dufmech.sssom.tsv | source | exports/sssom/dufmech.sssom.tsv |
| history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml | history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml | source | history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml |
| history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml | history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml | source | history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml |
| pages/families/PF01976.html | pages/families/PF01976.html | source | pages/families/PF01976.html |
| reports/causal_graphs/inventory.json | reports/causal_graphs/inventory.json | source | reports/causal_graphs/inventory.json |
| reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md | reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md | source | reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md |
| reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml | reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml | source | reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| integrity | passed | True | conf/site_source_pins.json, curation/families/PF01976.yaml, data/families/PF01976.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01976/causal-evidence-assessment.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml, history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml, pages/families/PF01976.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md, reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml | All 8296 manifest hashes match. Only PF01976 changes; three OPEN discussions, zero graphs/assertions, two canonical events, exact scientific digest. Imported fields, frozen worklists, other records, prior reports, schemas and code are preserved. Exports change only PF01976 status; association edges are unchanged. |
| native | passed | True | conf/site_source_pins.json, curation/families/PF01976.yaml, data/families/PF01976.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01976/causal-evidence-assessment.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml, history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml, pages/families/PF01976.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md, reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml | 8296 schema-valid records and zero drift; 313 history records, four review-contract tests, 162 structured bundles and 170 native reports validate. Schema reproduction has zero differences. |
| regressions | passed | True | conf/site_source_pins.json, curation/families/PF01976.yaml, data/families/PF01976.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01976/causal-evidence-assessment.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml, history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml, pages/families/PF01976.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md, reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml | All 52 focused graph/QC regression tests passed in 26.85 seconds with the pinned CLAW runtime. |
| retention | passed | True | conf/site_source_pins.json, curation/families/PF01976.yaml, data/families/PF01976.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01976/causal-evidence-assessment.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml, history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml, pages/families/PF01976.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md, reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml | All 9126 candidate source files match the canonical remote commit 13b3b6b3058c22af38a792ecf6aafd436ea91dcd, retained by annotated source/dufmech-pr-211-candidate. |
| render | passed | True | conf/site_source_pins.json, curation/families/PF01976.yaml, data/families/PF01976.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01976/causal-evidence-assessment.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml, history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml, pages/families/PF01976.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md, reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml | Canonical Pages regenerated through the native writer, without manual HTML or source-hash changes. |
| browser | passed | True | conf/site_source_pins.json, curation/families/PF01976.yaml, data/families/PF01976.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01976/causal-evidence-assessment.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml, history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml, pages/families/PF01976.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md, reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml | 1440px and 390px checks preserve the graphless absence disclaimer, three OPEN questions, mappings, evidence references, IN PROGRESS display and pinned record link. No document overflow or JavaScript errors; selected screenshots visually inspected and browser/server closed. Initial assertion expected the raw IN_PROGRESS enum rather than the existing human-readable label; only the scratch test was corrected, not application code. |
| governed | passed | True | conf/site_source_pins.json, curation/families/PF01976.yaml, data/families/PF01976.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01976/causal-evidence-assessment.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml, history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml, pages/families/PF01976.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md, reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml | All 22 governed artifacts match the published CLAW pin. A separate structured archive comparison verifies all 148 runtime/source/lock files against the cached official adce6ce0d1720635f11268465003cf78f35b2acf archive with no differences. |

## Scientific And Domain Assessments

### Evidence boundaries, preserved corpus and maintained ownership

scope: supported. Targets: conf/site_source_pins.json, curation/families/PF01976.yaml, data/families/PF01976.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01976/causal-evidence-assessment.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml, history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml, pages/families/PF01976.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md, reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml.

The bounded graphless assessment avoids treating predictions, automated names or a multi-mutant association as observed domain mechanisms. Native history/review and generated artifacts agree; all prior family content is preserved. Canonical display exposes the uncertainty and source provenance.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| integrity | data/families/manifest.json; Structured comparison against d53afef37b7e7f0667511c3e919a44c1270631a4 and fresh native checks | supports | Only PF01976 changes among 8296 families. Its semantic digest remains 9b7bc79ac8aed0744b99795e721badc52fc8b5ae5a6d4dfc34002190ec4ce868. Inventory retains 791 graphs/1680 edges across 126 families, 8170 graphless and 133 IN_PROGRESS; these are not scientific completion counts. |
| primary | evidence/PF01976/causal-evidence-assessment.txt; Makarova2015 full section 3.6 and adjacent family boundaries; Zhou2017 mutation/growth text and original Table 1 continuation; four retained InterPro mapping responses | supports | Redox is a comparative proposal, not a measured reaction. D5SS13 has separate PF01976 and PF00348 domains. The original DVU3364 row records a one-C deletion and predicted 145-aa loss within a multi-mutant strain, not isolated allele causality. Reference mappings and source hashes reproduce the ledger; no experimental construct identity is inferred. Current web access to the Zhou page returned a challenge; the previously retrieved hash-matching HTML and table image were inspected locally. |
| publication | https://github.com/CultureBotAI/DUFMech/issues/212; Initial local source-pin exit 1 and CI run 38683378652; candidate native capture/remote retention and canonical browser checks | supports | The preceding ledger rejected changed PF01976 bytes; candidate capture fixes that mismatch. Final audit-bearing retention and release checks remain required before closure. |
| runtime | .github/workflows/validate.yaml; Published CLAW pin adce6ce0d1720635f11268465003cf78f35b2acf; governed checker and structured archive comparison | supports | All 22 governed artifacts and 148 configured runtime/source/lock files match their official pinned source. |
| followups | reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml; Three OPEN findings, now tracked by GitHub issues 213, 214 and 215 | supports | The prior scientific review and all three native questions are preserved. Publication does not resolve redox/member evidence, prenyl-domain attribution or DVU3364 allele causality, and cannot promote REVIEWED. |

## Limits And Additional Notes

- Same-agent adversarial self-review, not independent approval or full family/corpus scientific completion.
- Issue 212 requires final audit-bearing source retention and final full QC/CI/deployment after this immutable report.
- Scientific issues 213-215 remain open. No new allele reconstruction, biochemical experiment or inaccessible supplement assessment is claimed.
- Primary originals and temporary check scripts remain outside the repository. Minimal retained evidence, source hashes and explicit methods/limits remain in the ledger.
- All-page link-pin fanout is generated; detailed responsive inspection is scoped to PF01976, with full site/browser regression gates required subsequently.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T045541Z-pr-211-pf01976-publication
repository: CultureBotAI/DUFMech
kind: repository
source:
  git_revision: 13b3b6b3058c22af38a792ecf6aafd436ea91dcd
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: conf/site_source_pins.json
    sha256: ec7327c9bfb9ad949a481119c83d292250b6797561b69ba75b5ba6a21c494365
    role: target
  - path: curation/families/PF01976.yaml
    sha256: 50deb1b5f922fa75493b5f350a4e50218d1aa23ed5be966a0d11af8cd4b2939e
    role: target
  - path: data/families/PF01976.yaml
    sha256: 55f321f327ec48706267d0dd36bb2bdb084fad254be32ed641f78615b4615f37
    role: target
  - path: data/families/manifest.json
    sha256: d1d3a1c57e32e56e060931539434228fff4caa1cfba8b1f3239b0b200ee2b059
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
    sha256: 9842c0a849a81aaf12cab40af367f0608aa7f9c9f13b332038dae434bad04496
    role: target
  - path: evidence/PF01976/causal-evidence-assessment.txt
    sha256: e32c344814267c69667710fc2305cee68c9a1a32bc6315cb41411367c29cc271
    role: target
  - path: exports/kgx/nodes.tsv
    sha256: 4f489542085bcd6fe82b8d891b79c2bd12ad6d87458f6c738dc6b6f40828fca2
    role: target
  - path: exports/sssom/dufmech.sssom.tsv
    sha256: 1b61371e584c44a123101e38e77788feb053a1684f9933bda1a42d8db41813fc
    role: target
  - path: history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml
    sha256: 5e79e4600218491656d55cb4f2ea4d08ba6d4cf52048b1ca53bbd2824e959dbe
    role: target
  - path: history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml
    sha256: b9ed55692caede24ca320f85f04b5d8e50dff8d3cfbad226aed1d501e50e66a2
    role: target
  - path: pages/families/PF01976.html
    sha256: 003b3820c592a23fbc8b04f941e5f1a8e5557d19b6d8ffb3e3e8538a25c76c18
    role: target
  - path: reports/causal_graphs/inventory.json
    sha256: c42b59684036195b18fcce46743d233d1dd78640ba01d00abe81f6bba5057d92
    role: target
  - path: reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md
    sha256: b3e4542e8adbadf0c30a09cac3519b5048eaf492f9ad9a019ac0abf6aee3c316
    role: target
  - path: reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml
    sha256: 7483ea20253579eb52b7580c45046668be13bcc4c11de2dd5f8ac5d1ed4a9fc2
    role: target
  - path: src/dufmech/site_sources.py
    role: context
    sha256: bad39b4cb1d578ddec9c8ee5b415411110391e6f290b9e96651c550ef5738d65
  - path: src/dufmech/qc.py
    role: context
    sha256: e75e5080000578ef5b794147fbd138810de552da9eb241d2cb7612322c093d6e
  - path: .github/workflows/validate.yaml
    role: context
    sha256: 88da10d07212b66c1882b077cd02847037ecc88042432ebbae928356d4c9c4e5
targets:
- target_id: conf/site_source_pins.json
  path: conf/site_source_pins.json
  label: conf/site_source_pins.json
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: curation/families/PF01976.yaml
  path: curation/families/PF01976.yaml
  label: curation/families/PF01976.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: data/families/PF01976.yaml
  path: data/families/PF01976.yaml
  label: data/families/PF01976.yaml
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
- target_id: evidence/PF01976/causal-evidence-assessment.txt
  path: evidence/PF01976/causal-evidence-assessment.txt
  label: evidence/PF01976/causal-evidence-assessment.txt
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
- target_id: history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml
  path: history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml
  label: history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml
  path: history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml
  label: history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: pages/families/PF01976.html
  path: pages/families/PF01976.html
  label: pages/families/PF01976.html
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: reports/causal_graphs/inventory.json
  path: reports/causal_graphs/inventory.json
  label: reports/causal_graphs/inventory.json
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md
  path: reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md
  label: reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml
  path: reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml
  label: reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
title: PR 211 PF01976 graphless assessment adversarial publication audit
started_at: '2026-10-15T04:46:36Z'
finished_at: '2026-10-15T04:55:41Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same-agent adversarial recheck of evidence interpretation, maintained
    ownership and publication surfaces; not independent expert approval.
skill: .claude/skills/review-repo/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: false
summary: The reproduced stale-pin publication blocker is tracked in issue 212. Candidate
  retention, native rendering, responsive checks, evidence-boundary rechecks and corpus
  preservation pass. No additional blocking defect was established in this bounded
  same-agent review. Final audit-bearing capture, full QC, exact-head CI and deployment
  remain subsequent release gates. Scientific issues 213-215 remain open.
scope:
  description: Twelve changed source/artifact paths plus the source-pin ledger and
    canonical PF01976 page. Check graphless evidence boundaries, exact reference/domain
    attribution, source ownership, append-only history/reviews, corpus preservation
    and candidate publication.
  selection: Explicit PR changed-source set plus two publication surfaces, not a random
    sample or corpus-wide scientific review.
  coverage: full
  population_size: 14
  reviewed_target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01976.yaml
  - data/families/PF01976.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01976/causal-evidence-assessment.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml
  - history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml
  - pages/families/PF01976.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml
  exclusions:
  - target: Full family/member science, raw sequencing, historical evolved allele
      and inaccessible supplements
    reason: Rechecked inspected sources and explicit exclusions; no experimental replication
      or newly completed evidence gap.
  - target: Final audit-bearing checkpoint, full QC, exact-head CI and deployed Pages
    reason: This immutable review must first be committed, retained and captured;
      final release checks follow it.
checks:
- check_id: integrity
  name: integrity
  command: uv run --locked python /private/tmp/duf-pf01976-check.py --exports --review
    --inventory --publication
  status: passed
  required: true
  exit_code: 0
  summary: All 8296 manifest hashes match. Only PF01976 changes; three OPEN discussions,
    zero graphs/assertions, two canonical events, exact scientific digest. Imported
    fields, frozen worklists, other records, prior reports, schemas and code are preserved.
    Exports change only PF01976 status; association edges are unchanged.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01976.yaml
  - data/families/PF01976.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01976/causal-evidence-assessment.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml
  - history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml
  - pages/families/PF01976.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml
  evidence_ids:
  - integrity
- check_id: native
  name: native
  command: just validate-all validate-schema
  status: passed
  required: true
  exit_code: 0
  summary: 8296 schema-valid records and zero drift; 313 history records, four review-contract
    tests, 162 structured bundles and 170 native reports validate. Schema reproduction
    has zero differences.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01976.yaml
  - data/families/PF01976.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01976/causal-evidence-assessment.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml
  - history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml
  - pages/families/PF01976.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml
  evidence_ids:
  - integrity
- check_id: regressions
  name: regressions
  command: PYTHONPATH=src:/private/tmp/dufmech-protein-claw/src uv run --locked --extra
    dev pytest -q tests/test_causal_graphs.py tests/test_qc.py
  status: passed
  required: true
  exit_code: 0
  summary: All 52 focused graph/QC regression tests passed in 26.85 seconds with the
    pinned CLAW runtime.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01976.yaml
  - data/families/PF01976.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01976/causal-evidence-assessment.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml
  - history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml
  - pages/families/PF01976.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml
  evidence_ids:
  - runtime
- check_id: retention
  name: retention
  command: just site-sources-published
  status: passed
  required: true
  exit_code: 0
  summary: All 9126 candidate source files match the canonical remote commit 13b3b6b3058c22af38a792ecf6aafd436ea91dcd,
    retained by annotated source/dufmech-pr-211-candidate.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01976.yaml
  - data/families/PF01976.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01976/causal-evidence-assessment.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml
  - history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml
  - pages/families/PF01976.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml
  evidence_ids:
  - publication
- check_id: render
  name: render
  command: just render
  status: passed
  required: true
  exit_code: 0
  summary: Canonical Pages regenerated through the native writer, without manual HTML
    or source-hash changes.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01976.yaml
  - data/families/PF01976.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01976/causal-evidence-assessment.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml
  - history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml
  - pages/families/PF01976.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml
  evidence_ids:
  - publication
- check_id: browser
  name: browser
  command: DUF_CANONICAL=1 node /private/tmp/duf-pf01976-browser.cjs
  status: passed
  required: true
  exit_code: 0
  summary: 1440px and 390px checks preserve the graphless absence disclaimer, three
    OPEN questions, mappings, evidence references, IN PROGRESS display and pinned
    record link. No document overflow or JavaScript errors; selected screenshots visually
    inspected and browser/server closed. Initial assertion expected the raw IN_PROGRESS
    enum rather than the existing human-readable label; only the scratch test was
    corrected, not application code.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01976.yaml
  - data/families/PF01976.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01976/causal-evidence-assessment.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml
  - history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml
  - pages/families/PF01976.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml
  evidence_ids:
  - publication
- check_id: governed
  name: governed
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  exit_code: 0
  summary: All 22 governed artifacts match the published CLAW pin. A separate structured
    archive comparison verifies all 148 runtime/source/lock files against the cached
    official adce6ce0d1720635f11268465003cf78f35b2acf archive with no differences.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01976.yaml
  - data/families/PF01976.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01976/causal-evidence-assessment.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml
  - history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml
  - pages/families/PF01976.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml
  evidence_ids:
  - runtime
evidence:
- evidence_id: integrity
  kind: validation
  reference: data/families/manifest.json
  locator: Structured comparison against d53afef37b7e7f0667511c3e919a44c1270631a4
    and fresh native checks
  accessed_at: '2026-10-15T04:55:41Z'
  support: supports
  summary: Only PF01976 changes among 8296 families. Its semantic digest remains 9b7bc79ac8aed0744b99795e721badc52fc8b5ae5a6d4dfc34002190ec4ce868.
    Inventory retains 791 graphs/1680 edges across 126 families, 8170 graphless and
    133 IN_PROGRESS; these are not scientific completion counts.
- evidence_id: primary
  kind: primary_source
  reference: evidence/PF01976/causal-evidence-assessment.txt
  locator: Makarova2015 full section 3.6 and adjacent family boundaries; Zhou2017
    mutation/growth text and original Table 1 continuation; four retained InterPro
    mapping responses
  accessed_at: '2026-10-15T04:55:41Z'
  support: supports
  summary: Redox is a comparative proposal, not a measured reaction. D5SS13 has separate
    PF01976 and PF00348 domains. The original DVU3364 row records a one-C deletion
    and predicted 145-aa loss within a multi-mutant strain, not isolated allele causality.
    Reference mappings and source hashes reproduce the ledger; no experimental construct
    identity is inferred. Current web access to the Zhou page returned a challenge;
    the previously retrieved hash-matching HTML and table image were inspected locally.
- evidence_id: publication
  kind: validation
  reference: https://github.com/CultureBotAI/DUFMech/issues/212
  locator: Initial local source-pin exit 1 and CI run 38683378652; candidate native
    capture/remote retention and canonical browser checks
  accessed_at: '2026-10-15T04:55:41Z'
  support: supports
  summary: The preceding ledger rejected changed PF01976 bytes; candidate capture
    fixes that mismatch. Final audit-bearing retention and release checks remain required
    before closure.
- evidence_id: runtime
  kind: validation
  reference: .github/workflows/validate.yaml
  locator: Published CLAW pin adce6ce0d1720635f11268465003cf78f35b2acf; governed checker
    and structured archive comparison
  accessed_at: '2026-10-15T04:55:41Z'
  support: supports
  summary: All 22 governed artifacts and 148 configured runtime/source/lock files
    match their official pinned source.
- evidence_id: followups
  kind: prior_review
  reference: reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml
  locator: Three OPEN findings, now tracked by GitHub issues 213, 214 and 215
  accessed_at: '2026-10-15T04:55:41Z'
  support: supports
  summary: The prior scientific review and all three native questions are preserved.
    Publication does not resolve redox/member evidence, prenyl-domain attribution
    or DVU3364 allele causality, and cannot promote REVIEWED.
assessments:
- assessment_id: bounded-assessment
  area: scope
  topic: Evidence boundaries, preserved corpus and maintained ownership
  outcome: supported
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01976.yaml
  - data/families/PF01976.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01976/causal-evidence-assessment.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01976/2026-10-15T041826Z-codex-0441fd.yaml
  - history/records/PF01976/2026-10-15T042712Z-codex-3918bc.yaml
  - pages/families/PF01976.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.md
  - reviews/structured/20261015T042712Z-pf01976-causal-evidence-boundaries/review.yaml
  evidence_ids:
  - integrity
  - primary
  - followups
  - runtime
  - publication
  summary: The bounded graphless assessment avoids treating predictions, automated
    names or a multi-mutant association as observed domain mechanisms. Native history/review
    and generated artifacts agree; all prior family content is preserved. Canonical
    display exposes the uncertainty and source provenance.
findings: []
actions: []
limitations:
- Same-agent adversarial self-review, not independent approval or full family/corpus
  scientific completion.
- Issue 212 requires final audit-bearing source retention and final full QC/CI/deployment
  after this immutable report.
- Scientific issues 213-215 remain open. No new allele reconstruction, biochemical
  experiment or inaccessible supplement assessment is claimed.
- Primary originals and temporary check scripts remain outside the repository. Minimal
  retained evidence, source hashes and explicit methods/limits remain in the ledger.
- All-page link-pin fanout is generated; detailed responsive inspection is scoped
  to PF01976, with full site/browser regression gates required subsequently.
related_reviews:
- repository: CultureBotAI/DUFMech
  review_id: 20261015T042712Z-pf01976-causal-evidence-boundaries
  relationship: Publication audit; does not supersede or close prior scientific findings.
tags:
- adversarial-self-review
- pr-211
- pf01976
- publication
```
