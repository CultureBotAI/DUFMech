# PR 258 CofC adversarial publication review

- Review: 20261016T041512Z-pr-258-publication
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-16T04:05:38Z
- Finished UTC: 2026-10-16T04:15:12Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

The reproduced source-pin mismatch in issue259 is repaired on a retained candidate checkpoint. Seven graphs and18 relations preserve their scientific scope and exact record digest. Scientific issues260-262 remain open. Final audit-bearing source capture, full QC and exact-head CI are still required before merge.

## Scope And Provenance

Scoped adversarial audit of PF01983 publication, evidence qualifiers and immutable-source preservation.

Selection: All three affected maintained overlay, source-ledger and canonical family-page surfaces. Prior-review discovery included ignored/hidden files; GitHub PF01983 issue search returned no existing duplicate before filing259-262.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 7207aae4a61efb550445799612cdd277cb45791e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| conf/site_source_pins.json | conf/site_source_pins.json | source | conf/site_source_pins.json |
| curation/families/PF01983.yaml | curation/families/PF01983.yaml | source | curation/families/PF01983.yaml |
| pages/families/PF01983.html | pages/families/PF01983.html | source | pages/families/PF01983.html |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| focused | passed | True | conf/site_source_pins.json, curation/families/PF01983.yaml, pages/families/PF01983.html | 56 focused tests passed. |
| native | passed | True | conf/site_source_pins.json, curation/families/PF01983.yaml, pages/families/PF01983.html | 8296 records, zero projection drift,349 history files,199 structured bundles/207 retained reports and schema checks pass. |
| retention | passed | True | conf/site_source_pins.json, curation/families/PF01983.yaml, pages/families/PF01983.html | 9242 pins match and are retained by the published annotated candidate tag. |
| render | passed | True | conf/site_source_pins.json, curation/families/PF01983.yaml, pages/families/PF01983.html | Native full-corpus rendering and site contracts/budgets pass. |
| integrity | passed | True | conf/site_source_pins.json, curation/families/PF01983.yaml, pages/families/PF01983.html | All8296 manifest hashes; all8295 other families unchanged; old evidence/history/reviews and science unchanged; all18 source anchors match; copied sources and PF01983 JSON exact. |
| mapping | passed | True | conf/site_source_pins.json, curation/families/PF01983.yaml, pages/families/PF01983.html | Exact Mrhiz+5/Mjan+6/Msmeg0 reference mappings and B3 pMH43-to-7P97 translation are reproduced; B3 is209/216 identical to Mrhiz, not the same sequence. |
| browser | passed | True | conf/site_source_pins.json, curation/families/PF01983.yaml, pages/families/PF01983.html | Desktop1440px/mobile390px: seven graphs,18 working disclosures,2 direct/16 unresolved labels, local source links HTTP200, no document overflow or JS errors; screenshots inspected. |

## Scientific And Domain Assessments

### Candidate checkpoint and canonical publication

provenance: supported. Targets: conf/site_source_pins.json, curation/families/PF01983.yaml, pages/families/PF01983.html.

Published annotated source retention and native regeneration repair the reproduced stale publication without weakening gates.

### Claim scope and edge evidence remain intact

graph: supported. Targets: conf/site_source_pins.json, curation/families/PF01983.yaml, pages/families/PF01983.html.

Publication preserves the exact scientific digest and explicit unresolved mechanisms, partner contexts and reference offsets; primary figure re-reading did not support stronger claims.

### Maintained owners and prior artifacts

representation: supported. Targets: conf/site_source_pins.json, curation/families/PF01983.yaml, pages/families/PF01983.html.

Only the new family curation and derived publication surfaces change; all prior evidence/review/history bytes and8295 other records remain intact.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| release | https://github.com/CultureBotAI/DUFMech/commit/7207aae4a61efb550445799612cdd277cb45791e; source/dufmech-pr-258-candidate; native capture, online retention, full-corpus rendering, integrity and browser checks | supports | 9242 source files are retained by a canonical annotated tag; canonical family JSON and all copied sources match. |
| failure | https://github.com/CultureBotAI/DUFMech/issues/259; Initial site_sources check exit1 and CI38848873301 Verify published source checkpoint retention | supports | The initial gate failed on data/families/PF01983.yaml stale bytes; no gate was disabled or bypassed. |
| science | reviews/structured/20261016T035526Z-pf01983-cofc-coupled-assay-contexts/review.yaml; Partial scientific review; three open findings now tracked in issues260-262 | supports | The record remains IN_PROGRESS with no approval pointer; all seven graph IDs and18 relations retain their qualifiers. |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC8764529/; Hash-verified cached XML s2-4/s2-8/s4-5; visually re-inspected Figures3/6; reference comparison and pMH43 translation | supports | The source supports distinct coupled relative-product effects, not a directly observed binding or channeling mechanism. |
| paired | https://pmc.ncbi.nlm.nih.gov/articles/PMC6450877/; Hash-verified cached XML Sec3/Sec12; Figure2 visually re-inspected | supports | Two paired reactions produce the measured product; downstream partner choice and missing intermediate observation constrain transfer. |

## Limits And Additional Notes

- Same-agent review, not independent approval or experimental replication. This repository audit is not a new full-family scientific review.
- Only the two complete paired-enzyme reactions are DIRECT;16 mutation/partner relations remain UNRESOLVED. Relative fractions are not intrinsic affinity or absolute rates.
- Issues260-262 preserve the saved scientific findings: physical constructs/assay details, quantitative/atomic mechanisms, and primary-source/member coverage. None is closed by publishing this batch.
- Primary figures and selected XML Methods/Results were re-read; exact cached reference mappings and B3 translation were rerun. No new full-source or additional-member coverage is claimed.
- The live Hasan PMC page returned a browser verification challenge. The existing hash-verified primary XML and images were used, without bypassing the challenge.
- Unrecovered supplements, printed Fo units and unauthenticated physical inserts remain explicit limitations. Original2008/earlier2019 source access is not resolved by metadata or search snippets.
- This candidate review itself needs a final retained source checkpoint and re-render. Full release QC, final PR/merge-group CI and deployment are subsequent gates, not claimed complete in this artifact.
- Issue259 was recorded in GitHub before this audit bundle existed. This bundle verifies its candidate repair in the publication assessment; it does not fabricate a predecessor structured finding or supersede the scientific review.
- All8296 records remain the corpus denominator; graph presence in132 families is not corpus-wide scientific completion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
repository: CultureBotAI/DUFMech
kind: repository
source:
  git_revision: 7207aae4a61efb550445799612cdd277cb45791e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: conf/site_source_pins.json
    sha256: a8c6056d5e54a9d9222be4266bb3f7bb575914c2025a9a13678eb189fa10b569
    role: target
  - path: curation/families/PF01983.yaml
    sha256: ca8b26e4f406f0f9e4bf2e2b4a6788c10570c5a7f61350d888e205ecb9c667ee
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
  - path: pages/families/PF01983.html
    sha256: 86dfd1c98b3250901115c2ea43c83f9cb040a5b0c69912f23320ff98dd56de3e
    role: target
  - path: reviews/structured/20261016T035526Z-pf01983-cofc-coupled-assay-contexts/review.yaml
    role: context
    sha256: d4e4fa089abfebf1a04019df8a7a822ac315bed71c1e4551ff093eeed7d9c062
  - path: data/families/PF01983.yaml
    role: context
    sha256: 7721b3ae4d296a58002b177c3848b16ab672708ff17c1dd21c58819eb3d10977
  - path: reports/causal_graphs/inventory.json
    role: context
    sha256: 7c7e65daeaa15b74203b58e52478f2823ea0f6d7a282d3fa2c2015875edc3b76
  - path: src/dufmech/site_sources.py
    role: context
    sha256: bad39b4cb1d578ddec9c8ee5b415411110391e6f290b9e96651c550ef5738d65
  - path: src/dufmech/site_source_publication.py
    role: context
    sha256: 401f34614494bb898c21b61d5085038bd71c898cd10017b7c1655ae51118aa6e
  - path: src/dufmech/qc.py
    role: context
    sha256: e75e5080000578ef5b794147fbd138810de552da9eb241d2cb7612322c093d6e
  - path: scripts/render_pages.py
    role: context
    sha256: b3f2a86f2a6c362914493670c9ca6473544e5945ed0db2af21b9449fb9672399
  - path: evidence/PF01983/bashiri-2019.txt
    role: context
    sha256: 54a354e96fad787ba8de16b92c0d49516a921b8b7de993fff702e2c91b7bd9d9
  - path: evidence/PF01983/coverage-and-gaps.txt
    role: context
    sha256: a2f196ae4de943ef8744c7a23cafb252074f69966a4eefb8a2189bc7ee01c420
  - path: evidence/PF01983/hasan-2022.txt
    role: context
    sha256: f2e8f6026258575874f3561fb0f6508c6f072df21e71d0d7dc28e5be640c9adf
  - path: evidence/PF01983/identity-and-coordinates.txt
    role: context
    sha256: 5d9b1b72cba6afa147eeddd6b023be7493bd6765c3d4c56958cc55f918419a84
targets:
- target_id: conf/site_source_pins.json
  path: conf/site_source_pins.json
  label: conf/site_source_pins.json
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: curation/families/PF01983.yaml
  path: curation/families/PF01983.yaml
  label: curation/families/PF01983.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: pages/families/PF01983.html
  path: pages/families/PF01983.html
  label: pages/families/PF01983.html
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
schema_version: 1.0.0
review_id: 20261016T041512Z-pr-258-publication
title: PR 258 CofC adversarial publication review
started_at: '2026-10-16T04:05:38Z'
finished_at: '2026-10-16T04:15:12Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same-agent adversarial review of publication and claim preservation;
    not independent scientific approval.
skill: .claude/skills/review-repo/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: false
summary: The reproduced source-pin mismatch in issue259 is repaired on a retained
  candidate checkpoint. Seven graphs and18 relations preserve their scientific scope
  and exact record digest. Scientific issues260-262 remain open. Final audit-bearing
  source capture, full QC and exact-head CI are still required before merge.
scope:
  description: Scoped adversarial audit of PF01983 publication, evidence qualifiers
    and immutable-source preservation.
  selection: All three affected maintained overlay, source-ledger and canonical family-page
    surfaces. Prior-review discovery included ignored/hidden files; GitHub PF01983
    issue search returned no existing duplicate before filing259-262.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01983.yaml
  - pages/families/PF01983.html
checks:
- check_id: focused
  name: focused
  command: pytest -q tests/test_causal_graphs.py tests/test_qc.py tests/test_record_review_contract.py
  status: passed
  required: true
  exit_code: 0
  summary: 56 focused tests passed.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01983.yaml
  - pages/families/PF01983.html
  evidence_ids:
  - release
- check_id: native
  name: native
  command: just validate-all validate-schema
  status: passed
  required: true
  exit_code: 0
  summary: 8296 records, zero projection drift,349 history files,199 structured bundles/207
    retained reports and schema checks pass.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01983.yaml
  - pages/families/PF01983.html
  evidence_ids:
  - release
- check_id: retention
  name: retention
  command: python -m dufmech.site_sources capture --commit 7207aae4a61efb550445799612cdd277cb45791e;
    python -m dufmech.site_source_publication
  status: passed
  required: true
  exit_code: 0
  summary: 9242 pins match and are retained by the published annotated candidate tag.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01983.yaml
  - pages/families/PF01983.html
  evidence_ids:
  - release
- check_id: render
  name: render
  command: just render; just site-check
  status: passed
  required: true
  exit_code: 0
  summary: Native full-corpus rendering and site contracts/budgets pass.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01983.yaml
  - pages/families/PF01983.html
  evidence_ids:
  - release
- check_id: integrity
  name: integrity
  command: uv run --locked python /private/tmp/duf-pf01983-publication-4r5mVS/integrity.py
  status: passed
  required: true
  exit_code: 0
  summary: All8296 manifest hashes; all8295 other families unchanged; old evidence/history/reviews
    and science unchanged; all18 source anchors match; copied sources and PF01983
    JSON exact.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01983.yaml
  - pages/families/PF01983.html
  evidence_ids:
  - release
- check_id: mapping
  name: mapping
  command: uv run --no-project --offline --with biopython python /private/tmp/duf-pf01983-20261016-plWvqx/map_sequences.py
  status: passed
  required: true
  exit_code: 0
  summary: Exact Mrhiz+5/Mjan+6/Msmeg0 reference mappings and B3 pMH43-to-7P97 translation
    are reproduced; B3 is209/216 identical to Mrhiz, not the same sequence.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01983.yaml
  - pages/families/PF01983.html
  evidence_ids:
  - release
- check_id: browser
  name: browser
  command: node /private/tmp/duf-pf01983-publication-4r5mVS/browser.cjs
  status: passed
  required: true
  exit_code: 0
  summary: 'Desktop1440px/mobile390px: seven graphs,18 working disclosures,2 direct/16
    unresolved labels, local source links HTTP200, no document overflow or JS errors;
    screenshots inspected.'
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01983.yaml
  - pages/families/PF01983.html
  evidence_ids:
  - release
evidence:
- evidence_id: release
  kind: validation
  reference: https://github.com/CultureBotAI/DUFMech/commit/7207aae4a61efb550445799612cdd277cb45791e
  locator: source/dufmech-pr-258-candidate; native capture, online retention, full-corpus
    rendering, integrity and browser checks
  accessed_at: '2026-10-16T04:15:12Z'
  support: supports
  summary: 9242 source files are retained by a canonical annotated tag; canonical
    family JSON and all copied sources match.
- evidence_id: failure
  kind: validation
  reference: https://github.com/CultureBotAI/DUFMech/issues/259
  locator: Initial site_sources check exit1 and CI38848873301 Verify published source
    checkpoint retention
  accessed_at: '2026-10-16T04:15:12Z'
  support: supports
  summary: The initial gate failed on data/families/PF01983.yaml stale bytes; no gate
    was disabled or bypassed.
- evidence_id: science
  kind: prior_review
  reference: reviews/structured/20261016T035526Z-pf01983-cofc-coupled-assay-contexts/review.yaml
  locator: Partial scientific review; three open findings now tracked in issues260-262
  accessed_at: '2026-10-16T04:15:12Z'
  support: supports
  summary: The record remains IN_PROGRESS with no approval pointer; all seven graph
    IDs and18 relations retain their qualifiers.
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8764529/
  locator: Hash-verified cached XML s2-4/s2-8/s4-5; visually re-inspected Figures3/6;
    reference comparison and pMH43 translation
  accessed_at: '2026-10-16T04:15:12Z'
  support: supports
  summary: The source supports distinct coupled relative-product effects, not a directly
    observed binding or channeling mechanism.
- evidence_id: paired
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6450877/
  locator: Hash-verified cached XML Sec3/Sec12; Figure2 visually re-inspected
  accessed_at: '2026-10-16T04:15:12Z'
  support: supports
  summary: Two paired reactions produce the measured product; downstream partner choice
    and missing intermediate observation constrain transfer.
assessments:
- assessment_id: publication
  area: provenance
  topic: Candidate checkpoint and canonical publication
  outcome: supported
  summary: Published annotated source retention and native regeneration repair the
    reproduced stale publication without weakening gates.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01983.yaml
  - pages/families/PF01983.html
  evidence_ids:
  - release
  - failure
- assessment_id: qualifiers
  area: graph
  topic: Claim scope and edge evidence remain intact
  outcome: supported
  summary: Publication preserves the exact scientific digest and explicit unresolved
    mechanisms, partner contexts and reference offsets; primary figure re-reading
    did not support stronger claims.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01983.yaml
  - pages/families/PF01983.html
  evidence_ids:
  - science
  - primary
  - paired
  - release
- assessment_id: ownership
  area: representation
  topic: Maintained owners and prior artifacts
  outcome: supported
  summary: Only the new family curation and derived publication surfaces change; all
    prior evidence/review/history bytes and8295 other records remain intact.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01983.yaml
  - pages/families/PF01983.html
  evidence_ids:
  - release
  - science
findings: []
actions: []
limitations:
- Same-agent review, not independent approval or experimental replication. This repository
  audit is not a new full-family scientific review.
- Only the two complete paired-enzyme reactions are DIRECT;16 mutation/partner relations
  remain UNRESOLVED. Relative fractions are not intrinsic affinity or absolute rates.
- 'Issues260-262 preserve the saved scientific findings: physical constructs/assay
  details, quantitative/atomic mechanisms, and primary-source/member coverage. None
  is closed by publishing this batch.'
- Primary figures and selected XML Methods/Results were re-read; exact cached reference
  mappings and B3 translation were rerun. No new full-source or additional-member
  coverage is claimed.
- The live Hasan PMC page returned a browser verification challenge. The existing
  hash-verified primary XML and images were used, without bypassing the challenge.
- Unrecovered supplements, printed Fo units and unauthenticated physical inserts remain
  explicit limitations. Original2008/earlier2019 source access is not resolved by
  metadata or search snippets.
- This candidate review itself needs a final retained source checkpoint and re-render.
  Full release QC, final PR/merge-group CI and deployment are subsequent gates, not
  claimed complete in this artifact.
- Issue259 was recorded in GitHub before this audit bundle existed. This bundle verifies
  its candidate repair in the publication assessment; it does not fabricate a predecessor
  structured finding or supersede the scientific review.
- All8296 records remain the corpus denominator; graph presence in132 families is
  not corpus-wide scientific completion.
```
