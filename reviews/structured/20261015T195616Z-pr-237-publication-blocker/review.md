# PR237 original TrmBL1 assay publication prerequisite audit

- Review: 20261015T195616Z-pr-237-publication-blocker
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-15T19:54:08Z
- Finished UTC: 2026-10-15T19:56:16Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

Native pin verification rejects the changed PF01978 overlay. Canonical Pages still carries the prior39 graphs, not the current42. Issue236 tracks the publication prerequisite; scientific issues228-230 remain open.

## Scope And Provenance

Current overlay, source-pin ledger and canonical PF01978 page before publication.

Selection: Three affected publication surfaces for the six added reported-assay effects.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base fd54481c6b74265e32499b429a124558ffa02bd2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| conf/site_source_pins.json | conf/site_source_pins.json | source | conf/site_source_pins.json |
| curation/families/PF01978.yaml | curation/families/PF01978.yaml | source | curation/families/PF01978.yaml |
| pages/families/PF01978.html | pages/families/PF01978.html | source | pages/families/PF01978.html |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native source-pin currentness | failed | True | conf/site_source_pins.json, curation/families/PF01978.yaml, pages/families/PF01978.html | site source pin bytes differ: curation/families/PF01978.yaml; capture a new source checkpoint |

## Scientific And Domain Assessments

### Retained sources and canonical rendering

provenance: concern. Targets: conf/site_source_pins.json, curation/families/PF01978.yaml, pages/families/PF01978.html.

Publish retained checkpoints and regenerate via native capture/render; do not weaken the stale-byte guard.

## Findings

### stale-publication: Original assay additions are missing from canonical pins and Pages

blocker / open / confirmed; issue key: pf01978-lee2007-stale-publication.

The publication gate rejects changed source bytes and the canonical page lacks three new graphs. This is a release prerequisite, not a demonstrated scientific claim defect.

## Recommended Actions And Acceptance Checks

### publish

Retain source checkpoints, recapture pins and regenerate canonical Pages.

- Verify annotated checkpoint retention and exact source bytes.
- Check42 graphs/96 edges, provenance links and responsive disclosures.
- Retain successor audit and its own checkpoint, then pass final full QC and exact-head CI before merge.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| stale | https://github.com/CultureBotAI/DUFMech/issues/236; Native pin verification and unchanged canonical page versus current overlay | supports | The overlay contains42 graphs; canonical Pages and pins remain at the preceding39-graph release. Verification fails closed. |

## Limits And Additional Notes

- Bounded publication-prerequisite audit, not full scientific review or merge approval.
- Scientific issues228-230 remain open; no REVIEWED promotion is made.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
repository: CultureBotAI/DUFMech
kind: repository
source:
  git_revision: fd54481c6b74265e32499b429a124558ffa02bd2
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: conf/site_source_pins.json
    sha256: b6b43edae5e9d2270e75df3f730d01547399d421f7bb2fca63bb97753c067c7d
    role: target
  - path: curation/families/PF01978.yaml
    sha256: 754d1a3879fc8bbfc3b043a43bd2c736e92431c3673940ba83de2d49b9b3c082
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
  - path: pages/families/PF01978.html
    sha256: e96e87a4315959ad65770d8b35ca374bc2ab937b425f27b397f7e8b897a5eed0
    role: target
targets:
- target_id: conf/site_source_pins.json
  path: conf/site_source_pins.json
  label: conf/site_source_pins.json
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: curation/families/PF01978.yaml
  path: curation/families/PF01978.yaml
  label: curation/families/PF01978.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: pages/families/PF01978.html
  path: pages/families/PF01978.html
  label: pages/families/PF01978.html
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
schema_version: 1.0.0
review_id: 20261015T195616Z-pr-237-publication-blocker
title: PR237 original TrmBL1 assay publication prerequisite audit
started_at: '2026-10-15T19:54:08Z'
finished_at: '2026-10-15T19:56:16Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent curated and challenges the pending batch; no independent
    approval.
skill: .claude/skills/review-repo/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: FAIL
scientific_review: false
summary: Native pin verification rejects the changed PF01978 overlay. Canonical Pages
  still carries the prior39 graphs, not the current42. Issue236 tracks the publication
  prerequisite; scientific issues228-230 remain open.
scope:
  description: Current overlay, source-pin ledger and canonical PF01978 page before
    publication.
  selection: Three affected publication surfaces for the six added reported-assay
    effects.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01978.yaml
  - pages/families/PF01978.html
checks:
- check_id: pins
  name: Native source-pin currentness
  command: uv run --locked --offline python -m dufmech.site_sources check
  status: failed
  required: true
  exit_code: 1
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01978.yaml
  - pages/families/PF01978.html
  evidence_ids:
  - stale
  summary: 'site source pin bytes differ: curation/families/PF01978.yaml; capture
    a new source checkpoint'
evidence:
- evidence_id: stale
  kind: validation
  reference: https://github.com/CultureBotAI/DUFMech/issues/236
  locator: Native pin verification and unchanged canonical page versus current overlay
  accessed_at: '2026-10-15T19:56:16Z'
  support: supports
  summary: The overlay contains42 graphs; canonical Pages and pins remain at the preceding39-graph
    release. Verification fails closed.
assessments:
- assessment_id: publication
  area: provenance
  topic: Retained sources and canonical rendering
  outcome: concern
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01978.yaml
  - pages/families/PF01978.html
  evidence_ids:
  - stale
  summary: Publish retained checkpoints and regenerate via native capture/render;
    do not weaken the stale-byte guard.
findings:
- finding_id: stale-publication
  issue_key: pf01978-lee2007-stale-publication
  category: provenance
  severity: blocker
  status: open
  certainty: confirmed
  title: Original assay additions are missing from canonical pins and Pages
  description: The publication gate rejects changed source bytes and the canonical
    page lacks three new graphs. This is a release prerequisite, not a demonstrated
    scientific claim defect.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01978.yaml
  - pages/families/PF01978.html
  evidence_ids:
  - stale
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/site_sources.py
    role: Capture retained source checkpoints through the native writer.
  - repository: CultureBotAI/DUFMech
    path: scripts/render_pages.py
    role: Regenerate canonical Pages through the native writer.
actions:
- action_id: publish
  description: Retain source checkpoints, recapture pins and regenerate canonical
    Pages.
  finding_ids:
  - stale-publication
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01978.yaml
  - pages/families/PF01978.html
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/site_sources.py
    role: Capture retained source checkpoints through the native writer.
  - repository: CultureBotAI/DUFMech
    path: scripts/render_pages.py
    role: Regenerate canonical Pages through the native writer.
  acceptance_checks:
  - Verify annotated checkpoint retention and exact source bytes.
  - Check42 graphs/96 edges, provenance links and responsive disclosures.
  - Retain successor audit and its own checkpoint, then pass final full QC and exact-head
    CI before merge.
limitations:
- Bounded publication-prerequisite audit, not full scientific review or merge approval.
- Scientific issues228-230 remain open; no REVIEWED promotion is made.
```
