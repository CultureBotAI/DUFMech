# PR 220 PF01977 AnFdc adversarial publication audit

- Review: 20261015T070720Z-pr-220-pf01977-publication
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-15T06:52:27Z
- Finished UTC: 2026-10-15T07:07:20Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

No additional blocking scientific defect was established in the bounded PR recheck. The stale source-pin failure was reproduced locally and in initial CI, tracked as issue 216, then corrected for the retained candidate through native source capture and rendering. Scientific findings 217-219 remain open. The final audit-bearing checkpoint, full QC and exact-head CI are subsequent mandatory release gates.

## Scope And Provenance

All thirteen candidate changed paths plus source pins and the canonical PF01977 page. Review evidence boundaries, native ownership, projection and export integrity, candidate source retention and responsive graph rendering.

Selection: Explicit PR source/artifact set plus its two publication surfaces, not a random sample or complete family literature review.
Coverage: full; 15 reviewed / 15 in the declared population.
Source: working_tree at Git base f2b12dd9f59d877f0869f185c281f887471e63be.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| conf/site_source_pins.json | conf/site_source_pins.json | source | conf/site_source_pins.json |
| curation/families/PF01977.yaml | curation/families/PF01977.yaml | source | curation/families/PF01977.yaml |
| data/families/PF01977.yaml | data/families/PF01977.yaml | source | data/families/PF01977.yaml |
| data/families/manifest.json | data/families/manifest.json | source | data/families/manifest.json |
| docs/causal-graphs.md | docs/causal-graphs.md | source | docs/causal-graphs.md |
| evidence/PF01977/anfdc-primary-assays.txt | evidence/PF01977/anfdc-primary-assays.txt | source | evidence/PF01977/anfdc-primary-assays.txt |
| evidence/PF01977/member-mapping.txt | evidence/PF01977/member-mapping.txt | source | evidence/PF01977/member-mapping.txt |
| exports/kgx/nodes.tsv | exports/kgx/nodes.tsv | source | exports/kgx/nodes.tsv |
| exports/sssom/dufmech.sssom.tsv | exports/sssom/dufmech.sssom.tsv | source | exports/sssom/dufmech.sssom.tsv |
| history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml | history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml | source | history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml |
| history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml | history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml | source | history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml |
| pages/families/PF01977.html | pages/families/PF01977.html | source | pages/families/PF01977.html |
| reports/causal_graphs/inventory.json | reports/causal_graphs/inventory.json | source | reports/causal_graphs/inventory.json |
| reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md | reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md | source | reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md |
| reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml | reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml | source | reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| records | passed | True | conf/site_source_pins.json, curation/families/PF01977.yaml, data/families/PF01977.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01977/anfdc-primary-assays.txt, evidence/PF01977/member-mapping.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml, history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml, pages/families/PF01977.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml | 8296 schema-valid records; zero generated drift. |
| integrity | passed | True | conf/site_source_pins.json, curation/families/PF01977.yaml, data/families/PF01977.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01977/anfdc-primary-assays.txt, evidence/PF01977/member-mapping.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml, history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml, pages/families/PF01977.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml | All 8296 manifest hashes match; only PF01977 changes. Ten graphs, 26 edges, 14 DIRECT and 12 UNRESOLVED directness, three OPEN discussions and two canonical events. Imported fields, other records, old reviews/history, source snapshots and code preserved; exports change only PF01977 status. |
| regressions | passed | True | conf/site_source_pins.json, curation/families/PF01977.yaml, data/families/PF01977.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01977/anfdc-primary-assays.txt, evidence/PF01977/member-mapping.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml, history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml, pages/families/PF01977.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml | 52 tests passed in 31.64 seconds. |
| quotes | passed | True | conf/site_source_pins.json, curation/families/PF01977.yaml, data/families/PF01977.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01977/anfdc-primary-assays.txt, evidence/PF01977/member-mapping.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml, history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml, pages/families/PF01977.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml | All 26 edge quotations occur in the hash-matching retained cache and inspected primary XML. No raw full text is added to the repository. |
| history | passed | True | conf/site_source_pins.json, curation/families/PF01977.yaml, data/families/PF01977.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01977/anfdc-primary-assays.txt, evidence/PF01977/member-mapping.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml, history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml, pages/families/PF01977.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml | 316 canonical history files validate. |
| schema | passed | True | conf/site_source_pins.json, curation/families/PF01977.yaml, data/families/PF01977.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01977/anfdc-primary-assays.txt, evidence/PF01977/member-mapping.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml, history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml, pages/families/PF01977.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml | Schema reproduction has zero differences. |
| governed | passed | True | conf/site_source_pins.json, curation/families/PF01977.yaml, data/families/PF01977.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01977/anfdc-primary-assays.txt, evidence/PF01977/member-mapping.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml, history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml, pages/families/PF01977.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml | 22 governed artifacts match the immutable published CLAW revision. |
| retention | passed | True | conf/site_source_pins.json, curation/families/PF01977.yaml, data/families/PF01977.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01977/anfdc-primary-assays.txt, evidence/PF01977/member-mapping.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml, history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml, pages/families/PF01977.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml | 9134 source files verified against canonical remote commit f2b12dd9f59d877f0869f185c281f887471e63be retained by annotated source/dufmech-pr-220-candidate. |
| render | passed | True | conf/site_source_pins.json, curation/families/PF01977.yaml, data/families/PF01977.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01977/anfdc-primary-assays.txt, evidence/PF01977/member-mapping.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml, history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml, pages/families/PF01977.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml | Canonical Pages regenerated through the native writer; no hand-edited HTML or source hashes. |
| browser | passed | True | conf/site_source_pins.json, curation/families/PF01977.yaml, data/families/PF01977.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01977/anfdc-primary-assays.txt, evidence/PF01977/member-mapping.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml, history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml, pages/families/PF01977.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml | 1440px and 390px retain all ten graphs, 26 edges, evidence disclosures, directness labels, three OPEN discussions and current pinned record link. No document overflow or JavaScript errors. Selected screenshots visually inspected; browser and local server closed. |

## Scientific And Domain Assessments

### Context and evidence boundaries

graph: supported. Targets: conf/site_source_pins.json, curation/families/PF01977.yaml, data/families/PF01977.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01977/anfdc-primary-assays.txt, evidence/PF01977/member-mapping.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml, history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml, pages/families/PF01977.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml.

The adopted scope distinguishes whole enzyme from PF01977 sufficiency, substrate-specific adduct endpoints from turnover, observed perturbations from atomic mechanism, and displayed traces from reported text. IN_PROGRESS and explicit exclusions prevent family-wide overstatement.

### Maintained ownership and append-only artifacts

provenance: supported. Targets: conf/site_source_pins.json, curation/families/PF01977.yaml, data/families/PF01977.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01977/anfdc-primary-assays.txt, evidence/PF01977/member-mapping.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml, history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml, pages/families/PF01977.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml.

Scientific edits reside in the overlay and minimal evidence ledgers. Native generation, actual history and the retained partial scientific review agree; no unrelated record or frozen source is rewritten.

### Candidate publication and rendering

other: supported. Targets: conf/site_source_pins.json, curation/families/PF01977.yaml, data/families/PF01977.yaml, data/families/manifest.json, docs/causal-graphs.md, evidence/PF01977/anfdc-primary-assays.txt, evidence/PF01977/member-mapping.txt, exports/kgx/nodes.tsv, exports/sssom/dufmech.sssom.tsv, history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml, history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml, pages/families/PF01977.html, reports/causal_graphs/inventory.json, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md, reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml.

Native capture, retained remote source bytes and responsive canonical graph rendering agree for the candidate. The audit itself must be included in a new retained checkpoint before final full release validation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| integrity | data/families/manifest.json; Executed native checks and structured comparison to base 9531391dd98c6ac48e6d0f9393659c7da2241b80 | supports | Projection ownership, graph counts, semantic digest, export deltas and preservation are checked separately from scientific completeness. |
| primary | https://doi.org/10.1074/jbc.RA117.000881; Original Figures 2 and 7 re-viewed; primary XML Results for light response, isotope exchange, apparent kinetics and R173A four-hour text; Bailey2019 cycloadduct Results; all 26 quoted snippets checked against the three primary XML sources | supports | Displayed and reported-only observations remain distinct. Residual activity, occupancy confounding, out-of-domain substitutions and separate mutant/analogue contexts are explicit. PMC HTML returned a challenge; retained public primary XML and original figures were used, not search snippets. |
| publication | https://github.com/CultureBotAI/DUFMech/issues/216; Initial CI 38695395198, Verify published source checkpoint retention; subsequent native capture, fresh remote check, canonical rendering and responsive browser test | supports | The initial CI failed for stale PF01977 source bytes. The retained candidate corrects that prerequisite. Audit-source recapture and final release checks remain required. |
| followups | reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml; Three open scientific findings and matching native discussions, tracked in issues 217, 218 and 219 | supports | This publication audit does not supersede, resolve or close the earlier scientific findings. |

## Limits And Additional Notes

- No independent expert review, raw diffraction refinement, physical plasmid resequencing, experimental replication or complete family literature census.
- Scientific follow-ups 217-219 remain open; no absence or full-corpus completion claim.
- All final release gates must run after the audit-bearing source capture. This candidate audit does not certify future results.
- Issue 216 is fixed for the candidate but remains open until final release verification. The initial failed check is retained as historical failure, not misreported as a pass.
- During verification the original temporary worktree lost its .git pointer and tracked test files, causing just id-labels-oak-test to exit 1 with a missing-file error. Cause not established. Recovered the published candidate into a fresh locked worktree, preserved local docs/pins byte-for-byte and repeated responsive checks. The old UV cache also had missing metadata; locked dependencies and the pinned CLAW runtime were rebuilt with a fresh cache. Final full QC and isolated OAK checks must use the recovered worktree; no failing run is counted as passing.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T070720Z-pr-220-pf01977-publication
repository: CultureBotAI/DUFMech
kind: repository
source:
  git_revision: f2b12dd9f59d877f0869f185c281f887471e63be
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: conf/site_source_pins.json
    sha256: 183021fd7f5639f0a86739a6d4a00c8835204a08dc4af6ddb1373fc26993324d
    role: target
  - path: curation/families/PF01977.yaml
    sha256: 7406b60fef3e567fb787c7346e91c417a29d98a33ba9f7ffc8dca955a8835138
    role: target
  - path: data/families/PF01977.yaml
    sha256: 17f8398c330c559d701e8e9c9f5b64db2654ef82d7c83e6a1a93d6eb85fcf46c
    role: target
  - path: data/families/manifest.json
    sha256: 9cfcbc3df1953a583834b859d367cdf97baee8c225812f5e282fd63d27e17de6
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
    sha256: eb89317820019bd045a2625f6472f9bf0ece0cd06e38d1c77ce667e23ac7804e
    role: target
  - path: evidence/PF01977/anfdc-primary-assays.txt
    sha256: 403f6306f44f138f074dee8c6bdd5faa29d49dc25e4dd2f2346070d512f5db1a
    role: target
  - path: evidence/PF01977/member-mapping.txt
    sha256: 465125d46c286a9be91a1c44ca15e99f0b2e65b9868ce529fdb886fed89f5264
    role: target
  - path: exports/kgx/nodes.tsv
    sha256: b94e961dd3ce96f8f1654c25caa1b44f0b8b9355ac461a8f3d2c4c520d1e24ab
    role: target
  - path: exports/sssom/dufmech.sssom.tsv
    sha256: 572b7799e5e5ecd1be16d1b92f3716ce7fc483f8eaed6b3aedff386212032a27
    role: target
  - path: history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
    sha256: d2ab2e2ecdf5fde67e2f7f4a37a80a6c8edbcba29525f8f46b21ec31fc3e41f7
    role: target
  - path: history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
    sha256: 9dc8d84790b363bc47c398563a208e28df46d0c1d36a4795e88580d5e5b49a5b
    role: target
  - path: pages/families/PF01977.html
    sha256: 14b5c0d36f614fa77dc3d47a41039d24123d93528adf411529bd8eec408cbbdb
    role: target
  - path: reports/causal_graphs/inventory.json
    sha256: 92b9f382102f0b11a7fe01ef14737f772cc05c64e861f7eb7fb8a45f59f2fc5e
    role: target
  - path: reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
    sha256: 4585a4b31eee6d15747f62b553b847a4acffac6353e23306e2fee8c211c966f1
    role: target
  - path: reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
    sha256: 69e96fd2ea14f7d6b0186b7511c0ed0a9644e19fbfe52c561869f22f75494535
    role: target
targets:
- target_id: conf/site_source_pins.json
  path: conf/site_source_pins.json
  label: conf/site_source_pins.json
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: curation/families/PF01977.yaml
  path: curation/families/PF01977.yaml
  label: curation/families/PF01977.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: data/families/PF01977.yaml
  path: data/families/PF01977.yaml
  label: data/families/PF01977.yaml
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
- target_id: evidence/PF01977/anfdc-primary-assays.txt
  path: evidence/PF01977/anfdc-primary-assays.txt
  label: evidence/PF01977/anfdc-primary-assays.txt
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: evidence/PF01977/member-mapping.txt
  path: evidence/PF01977/member-mapping.txt
  label: evidence/PF01977/member-mapping.txt
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
- target_id: history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
  path: history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
  label: history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
  path: history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
  label: history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: pages/families/PF01977.html
  path: pages/families/PF01977.html
  label: pages/families/PF01977.html
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: reports/causal_graphs/inventory.json
  path: reports/causal_graphs/inventory.json
  label: reports/causal_graphs/inventory.json
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
  path: reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
  label: reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  path: reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  label: reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
title: PR 220 PF01977 AnFdc adversarial publication audit
started_at: '2026-10-15T06:52:27Z'
finished_at: '2026-10-15T07:07:20Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent adversarially rechecked its curation, primary excerpts
    and selected original figures; not independent expert approval.
skill: .claude/skills/review-repo/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: false
summary: No additional blocking scientific defect was established in the bounded PR
  recheck. The stale source-pin failure was reproduced locally and in initial CI,
  tracked as issue 216, then corrected for the retained candidate through native source
  capture and rendering. Scientific findings 217-219 remain open. The final audit-bearing
  checkpoint, full QC and exact-head CI are subsequent mandatory release gates.
scope:
  description: All thirteen candidate changed paths plus source pins and the canonical
    PF01977 page. Review evidence boundaries, native ownership, projection and export
    integrity, candidate source retention and responsive graph rendering.
  selection: Explicit PR source/artifact set plus its two publication surfaces, not
    a random sample or complete family literature review.
  coverage: full
  population_size: 15
  reviewed_target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01977.yaml
  - data/families/PF01977.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01977/anfdc-primary-assays.txt
  - evidence/PF01977/member-mapping.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
  - history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
  - pages/families/PF01977.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  exclusions:
  - target: Complete PF01977 and corpus science
    reason: Other members, remaining AnFdc assays and missing raw construct/assay
      details remain tracked by the unchanged scientific review and issues 217-219.
  - target: Final audit-bearing source checkpoint, full QC, exact-head CI and deployment
    reason: This append-only report must be retained before final source capture and
      release verification. No future check is asserted passed.
checks:
- check_id: records
  name: records
  command: just records-check
  status: passed
  required: true
  exit_code: 0
  summary: 8296 schema-valid records; zero generated drift.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01977.yaml
  - data/families/PF01977.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01977/anfdc-primary-assays.txt
  - evidence/PF01977/member-mapping.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
  - history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
  - pages/families/PF01977.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  evidence_ids:
  - integrity
- check_id: integrity
  name: integrity
  command: uv run --locked python /private/tmp/duf-pf01977-check.py --review --inventory
    --exports --publication
  status: passed
  required: true
  exit_code: 0
  summary: All 8296 manifest hashes match; only PF01977 changes. Ten graphs, 26 edges,
    14 DIRECT and 12 UNRESOLVED directness, three OPEN discussions and two canonical
    events. Imported fields, other records, old reviews/history, source snapshots
    and code preserved; exports change only PF01977 status.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01977.yaml
  - data/families/PF01977.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01977/anfdc-primary-assays.txt
  - evidence/PF01977/member-mapping.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
  - history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
  - pages/families/PF01977.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  evidence_ids:
  - integrity
- check_id: regressions
  name: regressions
  command: uv run --locked python -m pytest -q tests/test_causal_graphs.py tests/test_qc.py
  status: passed
  required: true
  exit_code: 0
  summary: 52 tests passed in 31.64 seconds.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01977.yaml
  - data/families/PF01977.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01977/anfdc-primary-assays.txt
  - evidence/PF01977/member-mapping.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
  - history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
  - pages/families/PF01977.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  evidence_ids:
  - integrity
- check_id: quotes
  name: quotes
  command: Structured XML/YAML comparison of all edge evidence snippets and cache
    SHA256 values
  status: passed
  required: true
  exit_code: 0
  summary: All 26 edge quotations occur in the hash-matching retained cache and inspected
    primary XML. No raw full text is added to the repository.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01977.yaml
  - data/families/PF01977.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01977/anfdc-primary-assays.txt
  - evidence/PF01977/member-mapping.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
  - history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
  - pages/families/PF01977.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  evidence_ids:
  - primary
- check_id: history
  name: history
  command: just history-check
  status: passed
  required: true
  exit_code: 0
  summary: 316 canonical history files validate.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01977.yaml
  - data/families/PF01977.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01977/anfdc-primary-assays.txt
  - evidence/PF01977/member-mapping.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
  - history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
  - pages/families/PF01977.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  evidence_ids:
  - integrity
- check_id: schema
  name: schema
  command: just validate-schema
  status: passed
  required: true
  exit_code: 0
  summary: Schema reproduction has zero differences.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01977.yaml
  - data/families/PF01977.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01977/anfdc-primary-assays.txt
  - evidence/PF01977/member-mapping.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
  - history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
  - pages/families/PF01977.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  evidence_ids:
  - integrity
- check_id: governed
  name: governed
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  exit_code: 0
  summary: 22 governed artifacts match the immutable published CLAW revision.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01977.yaml
  - data/families/PF01977.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01977/anfdc-primary-assays.txt
  - evidence/PF01977/member-mapping.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
  - history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
  - pages/families/PF01977.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  evidence_ids:
  - integrity
- check_id: retention
  name: retention
  command: uv run --locked python -m dufmech.site_source_publication
  status: passed
  required: true
  exit_code: 0
  summary: 9134 source files verified against canonical remote commit f2b12dd9f59d877f0869f185c281f887471e63be
    retained by annotated source/dufmech-pr-220-candidate.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01977.yaml
  - data/families/PF01977.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01977/anfdc-primary-assays.txt
  - evidence/PF01977/member-mapping.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
  - history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
  - pages/families/PF01977.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  evidence_ids:
  - publication
- check_id: render
  name: render
  command: just render
  status: passed
  required: true
  exit_code: 0
  summary: Canonical Pages regenerated through the native writer; no hand-edited HTML
    or source hashes.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01977.yaml
  - data/families/PF01977.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01977/anfdc-primary-assays.txt
  - evidence/PF01977/member-mapping.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
  - history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
  - pages/families/PF01977.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  evidence_ids:
  - publication
- check_id: browser
  name: browser
  command: DUF_CANONICAL=1 node /private/tmp/duf-pf01977-browser.cjs
  status: passed
  required: true
  exit_code: 0
  summary: 1440px and 390px retain all ten graphs, 26 edges, evidence disclosures,
    directness labels, three OPEN discussions and current pinned record link. No document
    overflow or JavaScript errors. Selected screenshots visually inspected; browser
    and local server closed.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01977.yaml
  - data/families/PF01977.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01977/anfdc-primary-assays.txt
  - evidence/PF01977/member-mapping.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
  - history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
  - pages/families/PF01977.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  evidence_ids:
  - publication
evidence:
- evidence_id: integrity
  kind: validation
  reference: data/families/manifest.json
  locator: Executed native checks and structured comparison to base 9531391dd98c6ac48e6d0f9393659c7da2241b80
  accessed_at: '2026-10-15T07:07:20Z'
  support: supports
  summary: Projection ownership, graph counts, semantic digest, export deltas and
    preservation are checked separately from scientific completeness.
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1074/jbc.RA117.000881
  locator: Original Figures 2 and 7 re-viewed; primary XML Results for light response,
    isotope exchange, apparent kinetics and R173A four-hour text; Bailey2019 cycloadduct
    Results; all 26 quoted snippets checked against the three primary XML sources
  accessed_at: '2026-10-15T07:07:20Z'
  support: supports
  summary: Displayed and reported-only observations remain distinct. Residual activity,
    occupancy confounding, out-of-domain substitutions and separate mutant/analogue
    contexts are explicit. PMC HTML returned a challenge; retained public primary
    XML and original figures were used, not search snippets.
- evidence_id: publication
  kind: validation
  reference: https://github.com/CultureBotAI/DUFMech/issues/216
  locator: Initial CI 38695395198, Verify published source checkpoint retention; subsequent
    native capture, fresh remote check, canonical rendering and responsive browser
    test
  accessed_at: '2026-10-15T07:07:20Z'
  support: supports
  summary: The initial CI failed for stale PF01977 source bytes. The retained candidate
    corrects that prerequisite. Audit-source recapture and final release checks remain
    required.
- evidence_id: followups
  kind: prior_review
  reference: reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  locator: Three open scientific findings and matching native discussions, tracked
    in issues 217, 218 and 219
  accessed_at: '2026-10-15T07:07:20Z'
  support: supports
  summary: This publication audit does not supersede, resolve or close the earlier
    scientific findings.
assessments:
- assessment_id: boundaries
  area: graph
  topic: Context and evidence boundaries
  outcome: supported
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01977.yaml
  - data/families/PF01977.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01977/anfdc-primary-assays.txt
  - evidence/PF01977/member-mapping.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
  - history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
  - pages/families/PF01977.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  evidence_ids:
  - primary
  - followups
  summary: The adopted scope distinguishes whole enzyme from PF01977 sufficiency,
    substrate-specific adduct endpoints from turnover, observed perturbations from
    atomic mechanism, and displayed traces from reported text. IN_PROGRESS and explicit
    exclusions prevent family-wide overstatement.
- assessment_id: ownership
  area: provenance
  topic: Maintained ownership and append-only artifacts
  outcome: supported
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01977.yaml
  - data/families/PF01977.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01977/anfdc-primary-assays.txt
  - evidence/PF01977/member-mapping.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
  - history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
  - pages/families/PF01977.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  evidence_ids:
  - integrity
  summary: Scientific edits reside in the overlay and minimal evidence ledgers. Native
    generation, actual history and the retained partial scientific review agree; no
    unrelated record or frozen source is rewritten.
- assessment_id: publication
  area: other
  topic: Candidate publication and rendering
  outcome: supported
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01977.yaml
  - data/families/PF01977.yaml
  - data/families/manifest.json
  - docs/causal-graphs.md
  - evidence/PF01977/anfdc-primary-assays.txt
  - evidence/PF01977/member-mapping.txt
  - exports/kgx/nodes.tsv
  - exports/sssom/dufmech.sssom.tsv
  - history/records/PF01977/2026-10-15T060707Z-codex-18c546.yaml
  - history/records/PF01977/2026-10-15T063259Z-codex-ee021b.yaml
  - pages/families/PF01977.html
  - reports/causal_graphs/inventory.json
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.md
  - reviews/structured/20261015T063259Z-pf01977-anfdc-causal-evidence/review.yaml
  evidence_ids:
  - publication
  summary: Native capture, retained remote source bytes and responsive canonical graph
    rendering agree for the candidate. The audit itself must be included in a new
    retained checkpoint before final full release validation.
findings: []
actions: []
limitations:
- No independent expert review, raw diffraction refinement, physical plasmid resequencing,
  experimental replication or complete family literature census.
- Scientific follow-ups 217-219 remain open; no absence or full-corpus completion
  claim.
- All final release gates must run after the audit-bearing source capture. This candidate
  audit does not certify future results.
notes:
- Issue 216 is fixed for the candidate but remains open until final release verification.
  The initial failed check is retained as historical failure, not misreported as a
  pass.
- During verification the original temporary worktree lost its .git pointer and tracked
  test files, causing just id-labels-oak-test to exit 1 with a missing-file error.
  Cause not established. Recovered the published candidate into a fresh locked worktree,
  preserved local docs/pins byte-for-byte and repeated responsive checks. The old
  UV cache also had missing metadata; locked dependencies and the pinned CLAW runtime
  were rebuilt with a fresh cache. Final full QC and isolated OAK checks must use
  the recovered worktree; no failing run is counted as passing.
tags:
- adversarial-review
- self-review
- pr-220
- pf01977
- publication
```
