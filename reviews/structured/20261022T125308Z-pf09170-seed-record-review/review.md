# PF09170 STN1_2: seed identity, provenance and evidence-scope review

- Review: 20261022T125308Z-pf09170-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-22T12:42:07Z
- Finished UTC: 2026-10-22T12:53:08Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: seed_only
- Scientific review: false

## Summary

PF09170 (STN1_2; InterPro:IPR015253) matches the verified frozen source and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED. STN1_2 retains PF09170/IPR015253 and EX_DUF. The source distinguishes the CST complex and isolated subunits, explicitly selects the C-terminal Stn1 region, and gives separate component and comparator accounts. Three distinct publication tokens occur four times; none was independently assessed.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: 2b49c8729090bbbcbdaa956f770eee0aff153723. The corpus has 8296 records; 1731 were covered and 6565 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF09170.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2b49c8729090bbbcbdaa956f770eee0aff153723.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF09170 | data/families/PF09170.yaml | generated | PF09170 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF09170 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF09170 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF09170 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF09170 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF09170 | 438 valid canonical history records. |
| Generated schema check | passed | True | PF09170 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF09170.

The filename, pfam_id=PF09170, id=Pfam:PF09170, short_name=STN1_2, name=CST, complex subunit STN1, C terminal, source URL and InterPro accession InterPro:IPR015253 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF09170.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 1178 proteins, 1210 matches, 8 structure entries and 1016 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF09170.

STN1_2 retains PF09170/IPR015253 and EX_DUF. The source distinguishes the CST complex and isolated subunits, explicitly selects the C-terminal Stn1 region, and gives separate component and comparator accounts. Three distinct publication tokens occur four times; none was independently assessed.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF09170.

Selected region, complete Stn1, isolated subunits, full complex, component motifs and comparator proteins remain distinct. Complex-level properties do not transfer to an isolated region; probably and may retain uncertainty, and resemblance does not establish identical behavior. No sequence, residue or experimental interpretation is added.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF09170.

Exact region/member/component/complex/comparator/citation attribution and primary support remain unassessed. Eight structures, 1016 models and 13 architectures do not independently validate the reported relationships or region-level activity. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF09170.

seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED express separate states. EX_DUF records historical renaming and is compatible with imported functional descriptions; it is not evidence that all members were tested. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF09170.

Scientific additions would belong in the human-owned curation/families/PF09170.yaml overlay with appropriately licensed evidence and actual canonical history, followed by generation through src/dufmech/records.py. Frozen snapshots and generated records are not direct correction surfaces. No corrective edit is proposed by this seed audit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF09170.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF09170 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF09170; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 438 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF09170 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf09170 | data/families/PF09170.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- scientific_review is false. Primary papers, original figures and assays, live database entries, current taxonomy and complete family-member coverage were not reviewed; source citation tokens are not verified primary evidence.
- The hidden/ignored-inclusive absence search is restricted to accession-bearing paths under curation/families, evidence and history. It does not exclude evidence in other local collections or the literature.
- Required input checks passed. Native saving validates the supplied content and constructs the immutable pair. The persisted pair is then read back through the native validator and covered by the batch just reviews-check recipe; this document does not preclaim those later results. Full publication QC is tracked separately and may require Pages source-pin updates.
- No scientific status, record, overlay, frozen input, canonical curation history or generated Pages artifact was changed by this review.
- One record per bundle; assessment prose was authored from the actual inspected record. The helper assembles provenance and schema fields; inspection and successful checks alone are not scientific findings.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
kind: record
repository: CultureBotAI/DUFMech
source:
  git_revision: 2b49c8729090bbbcbdaa956f770eee0aff153723
  inputs:
  - path: data/families/PF09170.yaml
    role: target
    sha256: 025b99c8668c3a6552c70ff0fa2742bc8442a441584ca5536d4f1836b3e50544
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
  label: PF09170
  owner_paths:
  - path: curation/families/PF09170.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF09170.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: def78eb26b5a7cff0b411e19893e1c82773a0672a1b3628df903c65d7a97356e
  target_id: PF09170
schema_version: 1.0.0
review_id: 20261022T125308Z-pf09170-seed-record-review
title: 'PF09170 STN1_2: seed identity, provenance and evidence-scope review'
started_at: '2026-10-22T12:42:07Z'
finished_at: '2026-10-22T12:53:08Z'
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
summary: PF09170 (STN1_2; InterPro:IPR015253) matches the verified frozen source and
  retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED.
  STN1_2 retains PF09170/IPR015253 and EX_DUF. The source distinguishes the CST complex
  and isolated subunits, explicitly selects the C-terminal Stn1 region, and gives
  separate component and comparator accounts. Three distinct publication tokens occur
  four times; none was independently assessed.
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: 2b49c8729090bbbcbdaa956f770eee0aff153723. The corpus has 8296
    records; 1731 were covered and 6565 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF09170.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF09170
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF09170
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF09170
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-160/PF09170-targets.yaml
    --input data/families/PF09170.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF09170
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-160/prepare.py
    PF09170
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF09170
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
  - PF09170
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
  summary: 438 valid canonical history records.
  target_ids:
  - PF09170
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
  summary: Generated schema check found 0 differing generated files.
  target_ids:
  - PF09170
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF09170.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-10-22T12:53:08Z'
  support: supports
  summary: Read the complete PF09170 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: 025b99c8668c3a6552c70ff0fa2742bc8442a441584ca5536d4f1836b3e50544
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF09170; companion manifest and TSV; native verified inspection
  accessed_at: '2026-10-22T12:53:08Z'
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
  accessed_at: '2026-10-22T12:53:08Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-10-22T12:53:08Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 438 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF09170
  accessed_at: '2026-10-22T12:53:08Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF09170. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf09170
  kind: record_content
  reference: data/families/PF09170.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-22T12:53:08Z'
  support: context_only
  snapshot_sha256: 025b99c8668c3a6552c70ff0fa2742bc8442a441584ca5536d4f1836b3e50544
  quote: "id: Pfam:PF09170\npfam_id: PF09170\nname: CST, complex subunit STN1, C terminal\n\
    short_name: STN1_2\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF09170\n\
    counters:\n  proteins: 1178\n  matches: 1210\n  proteomes: 755\n  taxa: 2397\n\
    \  structures: 8\n  alphafold_models: 1016\n  domain_architectures: 13\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR015253\ndescription: STN1 is a component of the CST complex,\
    \ a complex that binds to single-stranded DNA and is\n  required for protecting\
    \ telomeres from DNA degradation. The CST complex binds single-stranded DNA with\n\
    \  high affinity in a sequence-independent manner, while isolated subunits bind\
    \ DNA with low affinity on\n  their own. In addition to telomere protection, the\
    \ CST complex probably has a more general role in DNA\n  metabolism at non-telomeric\
    \ sites. This entry represents the C-terminal region of Stn1 which has two\n \
    \ winged helix-turn-helix (wHTH) motifs, wHTH1 and wHTH2 [[cite:PUB00053885],[cite:PUB00097419]].\
    \ wHTH1\n  is structurally similar to that in RPA32 with a large insertion between\
    \ helices alpha2 and alpha3, unique\n  to Stn1, that may allow interaction with\
    \ a different set of proteins that function at telomeres such\n  as Ctc1 [[cite:PUB00097419]].\
    \ wHTH2 is most similar to the DNA-binding wHTH motifs of the pur operon\n  repressor\
    \ and RepE replication initiator, but it does not bind double-stranded DNA [[cite:PUB00057805]].\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF09170, id=Pfam:PF09170, short_name=STN1_2, name=CST,
    complex subunit STN1, C terminal, source URL and InterPro accession InterPro:IPR015253
    agree with the selected frozen row. This establishes frozen identity correspondence,
    not current upstream taxonomy or function.
  target_ids:
  - PF09170
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 1178 proteins, 1210 matches, 8 structure entries and
    1016 AlphaFold models are frozen database counters, not independent experiments.
    Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF09170
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: STN1_2 retains PF09170/IPR015253 and EX_DUF. The source distinguishes the
    CST complex and isolated subunits, explicitly selects the C-terminal Stn1 region,
    and gives separate component and comparator accounts. Three distinct publication
    tokens occur four times; none was independently assessed.
  target_ids:
  - PF09170
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
  summary: Selected region, complete Stn1, isolated subunits, full complex, component
    motifs and comparator proteins remain distinct. Complex-level properties do not
    transfer to an isolated region; probably and may retain uncertainty, and resemblance
    does not establish identical behavior. No sequence, residue or experimental interpretation
    is added.
  target_ids:
  - PF09170
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: Exact region/member/component/complex/comparator/citation attribution and
    primary support remain unassessed. Eight structures, 1016 models and 13 architectures
    do not independently validate the reported relationships or region-level activity.
    No accession-named overlay, evidence or history path was found by the bounded
    hidden/ignored-inclusive inventory; the inspected projection has no curated claim
    payload. Optional-field absence is not a seed-schema defect.
  target_ids:
  - PF09170
  evidence_ids:
  - record
  - local-search
  - profile
- assessment_id: status
  area: consistency
  topic: Seed, scoring and review states
  outcome: supported
  summary: seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED
    express separate states. EX_DUF records historical renaming and is compatible
    with imported functional descriptions; it is not evidence that all members were
    tested. No REVIEWED gate or curation event is implied by this bundle.
  target_ids:
  - PF09170
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: Scientific additions would belong in the human-owned curation/families/PF09170.yaml
    overlay with appropriately licensed evidence and actual canonical history, followed
    by generation through src/dufmech/records.py. Frozen snapshots and generated records
    are not direct correction surfaces. No corrective edit is proposed by this seed
    audit.
  target_ids:
  - PF09170
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
- Required input checks passed. Native saving validates the supplied content and constructs
  the immutable pair. The persisted pair is then read back through the native validator
  and covered by the batch just reviews-check recipe; this document does not preclaim
  those later results. Full publication QC is tracked separately and may require Pages
  source-pin updates.
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
