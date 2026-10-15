# PF01980 TrmO_N publication prerequisite audit

- Review: 20261015T212235Z-pf01980-publication-blocker
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-15T21:21:08Z
- Finished UTC: 2026-10-15T21:22:35Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

Native source-pin verification rejects the PF01980 projection. Canonical pins and Pages remain at the preceding release. Issue239 tracks the prerequisite; scientific follow-ups240-242 remain OPEN.

## Scope And Provenance

Overlay, source-pin ledger and canonical family page before publication.

Selection: Three affected publication surfaces for the initial12 graphs/24 edges.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base b6e9a5d811a33d76dd392be315d05cf7ccabfbe5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| conf/site_source_pins.json | conf/site_source_pins.json | source | conf/site_source_pins.json |
| curation/families/PF01980.yaml | curation/families/PF01980.yaml | source | curation/families/PF01980.yaml |
| pages/families/PF01980.html | pages/families/PF01980.html | source | pages/families/PF01980.html |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native source-pin currentness | failed | True | conf/site_source_pins.json, curation/families/PF01980.yaml, pages/families/PF01980.html | site source pin bytes differ: data/families/PF01980.yaml; capture a new source checkpoint |

## Scientific And Domain Assessments

### Retained sources and canonical rendering

provenance: concern. Targets: conf/site_source_pins.json, curation/families/PF01980.yaml, pages/families/PF01980.html.

Retain and capture source checkpoints, then render through native writers; do not weaken stale-byte guards.

## Findings

### stale-publication: TrmO additions are not yet represented in canonical pins and Pages

blocker / open / confirmed; issue key: pf01980-trmo-stale-publication.

The required gate rejects changed source bytes. This is a release prerequisite, not a demonstrated scientific-claim defect.

## Recommended Actions And Acceptance Checks

### publish

Retain source checkpoints, capture pins and regenerate canonical Pages.

- Verify annotated checkpoint retention and exact source bytes.
- Check12graphs/24edges, evidence links and responsive disclosures.
- Retain successor audit and its source checkpoint; pass final full QC and exact-head CI before merge.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| stale | https://github.com/CultureBotAI/DUFMech/issues/239; Actual native pin failure and unchanged canonical page versus current overlay | supports | The candidate has12graphs/24edges, but canonical Pages and pins remain byte-identical to the previous release. Verification fails closed. |

## Limits And Additional Notes

- Publication-prerequisite audit, not a full scientific review or merge approval.
- Scientific issues240-242 remain OPEN. No REVIEWED promotion is made.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
repository: CultureBotAI/DUFMech
kind: repository
source:
  git_revision: b6e9a5d811a33d76dd392be315d05cf7ccabfbe5
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: conf/site_source_pins.json
    sha256: 73b6eb85d168780e186cfc4308d734ccc28ed6ad24de32af9953212a31b95c27
    role: target
  - path: curation/families/PF01980.yaml
    sha256: 04fd1a76aaf61cee22ed61f6c4b44490c94a5c5a24eb075712d5018024a19495
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
  - path: pages/families/PF01980.html
    sha256: 1717ecc09c65a7bd290296c502cfc74474a5786313961a5e243a80ccea5f131d
    role: target
targets:
- target_id: conf/site_source_pins.json
  path: conf/site_source_pins.json
  label: conf/site_source_pins.json
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: curation/families/PF01980.yaml
  path: curation/families/PF01980.yaml
  label: curation/families/PF01980.yaml
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
- target_id: pages/families/PF01980.html
  path: pages/families/PF01980.html
  label: pages/families/PF01980.html
  kind: source
  ownership_note: Inspect the selected source's ownership before proposing an edit.
schema_version: 1.0.0
review_id: 20261015T212235Z-pf01980-publication-blocker
title: PF01980 TrmO_N publication prerequisite audit
started_at: '2026-10-15T21:21:08Z'
finished_at: '2026-10-15T21:22:35Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent curated and challenges this batch; not independent
    approval.
skill: .claude/skills/review-repo/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: FAIL
scientific_review: false
summary: Native source-pin verification rejects the PF01980 projection. Canonical
  pins and Pages remain at the preceding release. Issue239 tracks the prerequisite;
  scientific follow-ups240-242 remain OPEN.
scope:
  description: Overlay, source-pin ledger and canonical family page before publication.
  selection: Three affected publication surfaces for the initial12 graphs/24 edges.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01980.yaml
  - pages/families/PF01980.html
checks:
- check_id: pins
  name: Native source-pin currentness
  command: uv run --locked --offline python -m dufmech.site_sources check
  status: failed
  required: true
  exit_code: 1
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01980.yaml
  - pages/families/PF01980.html
  evidence_ids:
  - stale
  summary: 'site source pin bytes differ: data/families/PF01980.yaml; capture a new
    source checkpoint'
evidence:
- evidence_id: stale
  kind: validation
  reference: https://github.com/CultureBotAI/DUFMech/issues/239
  locator: Actual native pin failure and unchanged canonical page versus current overlay
  accessed_at: '2026-10-15T21:22:35Z'
  support: supports
  summary: The candidate has12graphs/24edges, but canonical Pages and pins remain
    byte-identical to the previous release. Verification fails closed.
assessments:
- assessment_id: publication
  area: provenance
  topic: Retained sources and canonical rendering
  outcome: concern
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01980.yaml
  - pages/families/PF01980.html
  evidence_ids:
  - stale
  summary: Retain and capture source checkpoints, then render through native writers;
    do not weaken stale-byte guards.
findings:
- finding_id: stale-publication
  issue_key: pf01980-trmo-stale-publication
  category: provenance
  severity: blocker
  status: open
  certainty: confirmed
  title: TrmO additions are not yet represented in canonical pins and Pages
  description: The required gate rejects changed source bytes. This is a release prerequisite,
    not a demonstrated scientific-claim defect.
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01980.yaml
  - pages/families/PF01980.html
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
  description: Retain source checkpoints, capture pins and regenerate canonical Pages.
  finding_ids:
  - stale-publication
  target_ids:
  - conf/site_source_pins.json
  - curation/families/PF01980.yaml
  - pages/families/PF01980.html
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/site_sources.py
    role: Capture retained source checkpoints through the native writer.
  - repository: CultureBotAI/DUFMech
    path: scripts/render_pages.py
    role: Regenerate canonical Pages through the native writer.
  acceptance_checks:
  - Verify annotated checkpoint retention and exact source bytes.
  - Check12graphs/24edges, evidence links and responsive disclosures.
  - Retain successor audit and its source checkpoint; pass final full QC and exact-head
    CI before merge.
limitations:
- Publication-prerequisite audit, not a full scientific review or merge approval.
- Scientific issues240-242 remain OPEN. No REVIEWED promotion is made.
```
