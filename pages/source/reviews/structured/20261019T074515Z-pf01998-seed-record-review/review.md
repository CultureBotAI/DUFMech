# PF01998 DUF131: seed identity, provenance and evidence-scope review

- Review: 20261019T074515Z-pf01998-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-19T07:34:29Z
- Finished UTC: 2026-10-19T07:45:15Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: seed_only
- Scientific review: false

## Summary

PF01998 (DUF131; InterPro:IPR002849) matches the verified frozen source and remains a UNKNOWN_CANDIDATE, UNSCORED, SEEDED projection. The DUF131 description says function is unknown and predicts two transmembrane helices. The topology statement is explicitly predictive; it is not an experimental membrane-localization or transport claim. The text contains no primary citation token.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated scripts/record_review.py list inventory at base 6c5277fbd5ab0a7b7f0244f5c248758ac77b3530. The corpus has 8296 records; 142 were covered and 8154 unreviewed at selection. This bundle covers only PF01998.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6c5277fbd5ab0a7b7f0244f5c248758ac77b3530.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01998 | data/families/PF01998.yaml | generated | PF01998 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF01998 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF01998 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF01998 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF01998 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF01998 | All 420 retained canonical history records validate. |
| Generated schema check | passed | True | PF01998 | 0 schema-valid records; 0 generated files differ (schema-only mode). |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF01998.

The filename, pfam_id=PF01998, id=Pfam:PF01998, short_name=DUF131, name=Protein of unknown function DUF131, source URL and InterPro:IPR002849 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF01998.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 261 proteins, 261 matches, 0 structures and 252 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF01998.

The DUF131 description says function is unknown and predicts two transmembrane helices. The topology statement is explicitly predictive; it is not an experimental membrane-localization or transport claim. The text contains no primary citation token.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF01998.

Two predicted helices do not establish membrane orientation, substrate transport, channel activity or a signaling role. The single frozen domain architecture and 252 AlphaFold models are coverage observations, not an experimentally validated common function. Zero frozen structures is not a statement about all current structural knowledge.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF01998.

Future curation would require accessible primary evidence for localization and topology, followed by scoped functional assays if available. This local seed audit does not claim that no such evidence exists elsewhere, and it preserves the UNKNOWN_CANDIDATE and UNSCORED distinctions. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF01998.

seed_status=UNKNOWN_CANDIDATE, characterization_status=UNSCORED and curation_status=SEEDED express separate states. UNKNOWN_CANDIDATE is the retained lexical seed class, not an experimentally established absence of function. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF01998.

Scientific additions would belong in the human-owned curation/families/PF01998.yaml overlay with appropriately licensed evidence and actual canonical history, followed by generation through src/dufmech/records.py. Frozen snapshots and generated records are not direct correction surfaces. No corrective edit is proposed by this seed audit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF01998.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF01998 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF01998; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three recipes: 8296 records validate with no generated drift, 420 canonical history records validate, and schema artifacts have no drift. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF01998 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf01998 | data/families/PF01998.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- scientific_review is false. Primary papers, original figures and assays, live database entries, current taxonomy and complete family-member coverage were not reviewed; source citation tokens are not verified primary evidence.
- The hidden/ignored-inclusive absence search is restricted to accession-bearing paths under curation/families, evidence and history. It does not exclude evidence in other local collections or the literature.
- Required input checks passed. The saved bundle is validated after persistence by the native saver and just reviews-check; this immutable document does not preclaim the result of that later run. Full publication QC is tracked separately and may require Pages source-pin updates.
- No scientific status, record, overlay, frozen input, canonical curation history or generated Pages artifact was changed by this review.
- One record per bundle; assessment prose was authored from the actual inspected record. The helper assembles provenance and schema fields; inspection and successful checks alone are not scientific findings.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
kind: record
repository: CultureBotAI/DUFMech
source:
  git_revision: 6c5277fbd5ab0a7b7f0244f5c248758ac77b3530
  inputs:
  - path: data/families/PF01998.yaml
    role: target
    sha256: c10951cf872a4aeab4ebef1f659bfc3e2ccf5bbfe1f4aff4dc231eb24f271d77
  - path: data/worklists/interpro-pfam-duf-2026-10-10.json
    role: context
    sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383
  - path: data/worklists/interpro-pfam-duf-2026-10-10.manifest.json
    role: context
    sha256: 31c07ffb6a169c851ea0e6e9dd527a10c04028eafeb29187bd62dc2ae848696e
  - path: data/worklists/interpro-pfam-duf-2026-10-10.tsv
    role: context
    sha256: be023c8dd9d8d3864926b5032d6f7e87a884b1a567391696822dbbecc692dae7
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 681377625fe3045abfa2433784707424931a69987e2f02b84f907dcb28f4831b
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: d1399ec6d404b485ac03680db36b07536f1233dacfd282c407b0a07a509a0d69
    role: context
  - path: docs/history.md
    sha256: 356ead13b3a462a91158eb57cfba4c011d95462662c30f811ba2e1335a2b402e
    role: context
  - path: docs/record-review-profile.md
    sha256: 78000e079c219bd049f628f517465b6e36fb35a26497f7ba7791c098fac73059
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: docs/records.md
    sha256: 4a09829f77f279ba5be373cfa15ea957d69e978d0bb74a5ab3377988d8c29ad2
    role: context
  - path: docs/reviews.md
    sha256: 02563bb1eeae36f08ca7e9e38bacc36461c65e7399df4f6c75a7215a34895ce3
    role: context
  - path: docs/sources.md
    sha256: f530f8785142b9b76f20f0853ec54a21dd96ae0e5827b820a332096ba483d70f
    role: context
  - path: justfile
    sha256: 16b490ea5da25e8c6b5f9649fd920df8b87a3e8438c1b6c1a5b8ca029deb3e36
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  snapshot_id: interpro-pfam-duf-2026-10-10
  state: working_tree
targets:
- kind: generated
  label: PF01998
  owner_paths:
  - path: curation/families/PF01998.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF01998.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: 5ddd3b506d3157105f7389b40863b8a8ccd7f490ee576b6d6b148aefc14662ff
  target_id: PF01998
schema_version: 1.0.0
review_id: 20261019T074515Z-pf01998-seed-record-review
title: 'PF01998 DUF131: seed identity, provenance and evidence-scope review'
started_at: '2026-10-19T07:34:29Z'
finished_at: '2026-10-19T07:45:15Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: This review session did not author or modify the inspected seed
    projection or frozen source. This is an independent repository audit by an AI
    agent, not external scientific peer review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: seed_only
native_verdict: SEED_ONLY
scientific_review: false
summary: PF01998 (DUF131; InterPro:IPR002849) matches the verified frozen source and
  remains a UNKNOWN_CANDIDATE, UNSCORED, SEEDED projection. The DUF131 description
  says function is unknown and predicts two transmembrane helices. The topology statement
  is explicitly predictive; it is not an experimental membrane-localization or transport
  claim. The text contains no primary citation token.
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated scripts/record_review.py list inventory at base 6c5277fbd5ab0a7b7f0244f5c248758ac77b3530.
    The corpus has 8296 records; 142 were covered and 8154 unreviewed at selection.
    This bundle covers only PF01998.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF01998
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF01998
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF01998
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/PF01998-targets.yaml
    --input data/families/PF01998.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
    --input data/worklists/interpro-pfam-duf-2026-10-10.manifest.json --input data/worklists/interpro-pfam-duf-2026-10-10.tsv
    --input docs/records.md --input docs/reviews.md --input docs/history.md --input
    docs/sources.md --input docs/record-reviews.md --input docs/record-review-profile.md
    --input .claude/skills/review-yaml-record/SKILL.md --input .claude/skills/curate-yaml-record/references/review-checklist.md
    --input schema/record_review.yaml --input justfile
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Captured rubric and recipe bytes while preserving native source inputs
    and snapshot identity.
  target_ids:
  - PF01998
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/prepare.py
    PF01998
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF01998
  evidence_ids:
  - record
  - snapshot
- check_id: records
  name: Native closed-schema and projection checks
  command: just records-check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 8296 schema-valid records; 0 generated files differ.
  target_ids:
  - PF01998
  evidence_ids:
  - validation
  scope_note: Shared batch input check executed before saving these reviews. The selected
    projection and its maintained inputs remained unchanged.
- check_id: history
  name: Canonical history check
  command: just history-check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: All 420 retained canonical history records validate.
  target_ids:
  - PF01998
  evidence_ids:
  - validation
  scope_note: Shared batch input check; this seed has no curation_history or generated
    curation_events.
- check_id: schema
  name: Generated schema check
  command: just validate-schema
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 0 schema-valid records; 0 generated files differ (schema-only mode).
  target_ids:
  - PF01998
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF01998.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-10-19T07:45:15Z'
  support: supports
  summary: Read the complete PF01998 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: c10951cf872a4aeab4ebef1f659bfc3e2ccf5bbfe1f4aff4dc231eb24f271d77
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF01998; companion manifest and TSV; native verified inspection
  accessed_at: '2026-10-19T07:45:15Z'
  support: supports
  summary: The exact frozen row matches the projection. The native inspection verifies
    the retained JSON/TSV manifest; the migration snapshot generation timestamp is
    2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained
    row. The review date does not refresh these source facts.
  snapshot_sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383
- evidence_id: profile
  kind: authority
  reference: docs/record-review-profile.md
  locator: Domains and Ownership; Verdicts and Status Gates; linked record-review
    contract and native checklist
  accessed_at: '2026-10-19T07:45:15Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-10-19T07:45:15Z'
  support: supports
  summary: 'Observed exit 0 from all three recipes: 8296 records validate with no
    generated drift, 420 canonical history records validate, and schema artifacts
    have no drift. These checks do not establish scientific truth.'
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF01998
  accessed_at: '2026-10-19T07:45:15Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF01998. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf01998
  kind: record_content
  reference: data/families/PF01998.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-19T07:45:15Z'
  support: context_only
  snapshot_sha256: c10951cf872a4aeab4ebef1f659bfc3e2ccf5bbfe1f4aff4dc231eb24f271d77
  quote: "id: Pfam:PF01998\npfam_id: PF01998\nname: Protein of unknown function DUF131\n\
    short_name: DUF131\nseed_status: UNKNOWN_CANDIDATE\ncharacterization_status: UNSCORED\n\
    curation_status: SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01998\n\
    counters:\n  proteins: 261\n  matches: 261\n  proteomes: 193\n  taxa: 428\n  structures:\
    \ 0\n  alphafold_models: 252\n  domain_architectures: 1\nprovenance:\n  snapshot_id:\
    \ interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002849\ndescription: This archaebacterial protein family\
    \ has no known function. The proteins are predicted to\n  contain two transmembrane\
    \ helices.\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF01998, id=Pfam:PF01998, short_name=DUF131, name=Protein
    of unknown function DUF131, source URL and InterPro:IPR002849 agree with the selected
    frozen row. This establishes frozen identity correspondence, not current upstream
    taxonomy or function.
  target_ids:
  - PF01998
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 261 proteins, 261 matches, 0 structures and 252 AlphaFold
    models are frozen database counters, not independent experiments. Raw input hashes
    and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF01998
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: The DUF131 description says function is unknown and predicts two transmembrane
    helices. The topology statement is explicitly predictive; it is not an experimental
    membrane-localization or transport claim. The text contains no primary citation
    token.
  target_ids:
  - PF01998
  evidence_ids:
  - record
  - snapshot
  dimensions:
  - name: evidence-tier
    value: Imported database description; primary support not reassessed
    definition: Evidence actually examined for this audit; it is not a label for all
      evidence that may exist for the family.
    evidence_ids:
    - record
    - snapshot
- assessment_id: claim-scope
  area: scope
  topic: Family, domain and tested-protein boundaries
  outcome: supported
  summary: Two predicted helices do not establish membrane orientation, substrate
    transport, channel activity or a signaling role. The single frozen domain architecture
    and 252 AlphaFold models are coverage observations, not an experimentally validated
    common function. Zero frozen structures is not a statement about all current structural
    knowledge.
  target_ids:
  - PF01998
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: Future curation would require accessible primary evidence for localization
    and topology, followed by scoped functional assays if available. This local seed
    audit does not claim that no such evidence exists elsewhere, and it preserves
    the UNKNOWN_CANDIDATE and UNSCORED distinctions. No accession-named overlay, evidence
    or history path was found by the bounded hidden/ignored-inclusive inventory; the
    inspected projection has no curated claim payload. Optional-field absence is not
    a seed-schema defect.
  target_ids:
  - PF01998
  evidence_ids:
  - record
  - local-search
  - profile
- assessment_id: status
  area: consistency
  topic: Seed, scoring and review states
  outcome: supported
  summary: seed_status=UNKNOWN_CANDIDATE, characterization_status=UNSCORED and curation_status=SEEDED
    express separate states. UNKNOWN_CANDIDATE is the retained lexical seed class,
    not an experimentally established absence of function. No REVIEWED gate or curation
    event is implied by this bundle.
  target_ids:
  - PF01998
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: Scientific additions would belong in the human-owned curation/families/PF01998.yaml
    overlay with appropriately licensed evidence and actual canonical history, followed
    by generation through src/dufmech/records.py. Frozen snapshots and generated records
    are not direct correction surfaces. No corrective edit is proposed by this seed
    audit.
  target_ids:
  - PF01998
  evidence_ids:
  - profile
  - record
  - validation
findings: []
actions: []
limitations:
- scientific_review is false. Primary papers, original figures and assays, live database
  entries, current taxonomy and complete family-member coverage were not reviewed;
  source citation tokens are not verified primary evidence.
- The hidden/ignored-inclusive absence search is restricted to accession-bearing paths
  under curation/families, evidence and history. It does not exclude evidence in other
  local collections or the literature.
- Required input checks passed. The saved bundle is validated after persistence by
  the native saver and just reviews-check; this immutable document does not preclaim
  the result of that later run. Full publication QC is tracked separately and may
  require Pages source-pin updates.
- No scientific status, record, overlay, frozen input, canonical curation history
  or generated Pages artifact was changed by this review.
notes:
- One record per bundle; assessment prose was authored from the actual inspected record.
  The helper assembles provenance and schema fields; inspection and successful checks
  alone are not scientific findings.
tags:
- seed-review
- unreviewed-record-coverage
```
