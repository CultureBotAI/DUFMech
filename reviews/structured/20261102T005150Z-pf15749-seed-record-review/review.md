# PF15749 MRNIP: seed identity, provenance and evidence-scope review

- Review: 20261102T005150Z-pf15749-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-11-02T00:46:52Z
- Finished UTC: 2026-11-02T00:51:50Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: seed_only
- Scientific review: false

## Summary

PF15749 (MRNIP; InterPro:IPR049472) matches the verified frozen source and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED. EX_DUF MRNIP (IPR049472) retains imported prevention of damaged-DNA accumulation, association with the MRE11-RAD50-NBS1 complex, rapid DNA-damage-site recruitment and promotion of nuclear localization by phosphorylation of an unspecified serine. PUB00083234 was not independently read; no residue coordinate, kinase or intrinsic repair catalytic activity is established here. All seven counters agree between row and projection: 1583 proteins, 1591 matches, 1219 proteomes, 4007 taxa, 0 structures, 1370 models, 27 architectures.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: aa7d08bcf3a9a03879d06cffd075bc083d29788f. The corpus has 8296 records; 4221 were covered and 4075 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF15749.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base aa7d08bcf3a9a03879d06cffd075bc083d29788f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF15749 | data/families/PF15749.yaml | generated | PF15749 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF15749 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF15749 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF15749 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF15749 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF15749 | 489 valid canonical history records. |
| Generated schema check | passed | True | PF15749 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF15749.

The filename, pfam_id=PF15749, id=Pfam:PF15749, short_name=MRNIP, name=MRN-interacting protein, source URL and InterPro accession InterPro:IPR049472 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF15749.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 1583 proteins, 1591 matches, 0 structure entries and 1370 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF15749.

EX_DUF MRNIP (IPR049472) retains imported prevention of damaged-DNA accumulation, association with the MRE11-RAD50-NBS1 complex, rapid DNA-damage-site recruitment and promotion of nuclear localization by phosphorylation of an unspecified serine. PUB00083234 was not independently read; no residue coordinate, kinase or intrinsic repair catalytic activity is established here. All seven counters agree between row and projection: 1583 proteins, 1591 matches, 1219 proteomes, 4007 taxa, 0 structures, 1370 models, 27 architectures.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF15749.

Metadata-only source and captured-context review. EX_DUF MRNIP retains the imported role in preventing accumulation of damaged DNA, association with the MRE11-RAD50-NBS1 damage-sensing complex and rapid recruitment to DNA-damage sites. Association does not establish direct binding to each subunit, intrinsic nuclease or repair catalytic activity, tested organism or family-wide necessity. The source explicitly states that phosphorylation of a serine promotes MRNIP nuclear localization; it does not identify the serine position, kinase, phosphorylation stoichiometry or sufficiency and necessity in every family member. PUB00083234, zero structures and 1370 models were not inspected. Eight excess matches and 27 architectures do not resolve per-protein organization. No length interval or exact domain boundary is supplied.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF15749.

The captured literal accession (PF15749) and current-short-name (MRNIP) searches found no path or content hits under curation/families, evidence and history, including hidden and ignored files; the exact canonical overlay, evidence and history owners were absent. These bounded results do not establish absence for MRN, MRE11, RAD50, NBS1, expanded MRN-interacting names, phosphorylation or localization terms and PUB00083234 or wider literature. No primary paper, live upstream record, structural model or assay was inspected. A biological or historical assessment needs separately verified evidence and tested-protein scope. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF15749.

seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED express separate states. EX_DUF records historical renaming and is compatible with imported functional descriptions; it is not evidence that all members were tested. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF15749.

Scientific additions would belong in the human-owned curation/families/PF15749.yaml overlay with appropriately licensed evidence and actual canonical history, followed by generation through src/dufmech/records.py. Frozen snapshots and generated records are not direct correction surfaces. No corrective edit is proposed by this seed audit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF15749.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF15749 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF15749; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 489 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF15749 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf15749 | data/families/PF15749.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

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
  git_revision: aa7d08bcf3a9a03879d06cffd075bc083d29788f
  inputs:
  - path: data/families/PF15749.yaml
    role: target
    sha256: b34836e90bb541abe71655514f7e75d32093093a0597c909dc9a61438fefb768
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
  label: PF15749
  owner_paths:
  - path: curation/families/PF15749.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF15749.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: 24621e20cc5d6353ff1c02f7f56bf864225a42ff1f6655eca1b9449c0ad0b24e
  target_id: PF15749
schema_version: 1.0.0
review_id: 20261102T005150Z-pf15749-seed-record-review
title: 'PF15749 MRNIP: seed identity, provenance and evidence-scope review'
started_at: '2026-11-02T00:46:52Z'
finished_at: '2026-11-02T00:51:50Z'
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
summary: 'PF15749 (MRNIP; InterPro:IPR049472) matches the verified frozen source and
  retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED.
  EX_DUF MRNIP (IPR049472) retains imported prevention of damaged-DNA accumulation,
  association with the MRE11-RAD50-NBS1 complex, rapid DNA-damage-site recruitment
  and promotion of nuclear localization by phosphorylation of an unspecified serine.
  PUB00083234 was not independently read; no residue coordinate, kinase or intrinsic
  repair catalytic activity is established here. All seven counters agree between
  row and projection: 1583 proteins, 1591 matches, 1219 proteomes, 4007 taxa, 0 structures,
  1370 models, 27 architectures.'
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: aa7d08bcf3a9a03879d06cffd075bc083d29788f. The corpus has 8296
    records; 4221 were covered and 4075 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF15749.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF15749
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF15749
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF15749
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-409-attempt-001/PF15749-targets.yaml
    --input data/families/PF15749.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF15749
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-409-attempt-001/prepare.py
    PF15749
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF15749
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
  - PF15749
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
  summary: 489 valid canonical history records.
  target_ids:
  - PF15749
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
  - PF15749
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF15749.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-11-02T00:51:50Z'
  support: supports
  summary: Read the complete PF15749 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: b34836e90bb541abe71655514f7e75d32093093a0597c909dc9a61438fefb768
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF15749; companion manifest and TSV; native verified inspection
  accessed_at: '2026-11-02T00:51:50Z'
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
  accessed_at: '2026-11-02T00:51:50Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-11-02T00:51:50Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 489 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF15749
  accessed_at: '2026-11-02T00:51:50Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF15749. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf15749
  kind: record_content
  reference: data/families/PF15749.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-11-02T00:51:50Z'
  support: context_only
  snapshot_sha256: b34836e90bb541abe71655514f7e75d32093093a0597c909dc9a61438fefb768
  quote: "id: Pfam:PF15749\npfam_id: PF15749\nname: MRN-interacting protein\nshort_name:\
    \ MRNIP\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF15749\n\
    counters:\n  proteins: 1583\n  matches: 1591\n  proteomes: 1219\n  taxa: 4007\n\
    \  structures: 0\n  alphafold_models: 1370\n  domain_architectures: 27\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR049472\ndescription: This family is found in eukaryotes.\
    \ Family members include MRN complex-interacting protein\n  (MRNIP), which plays\
    \ a role in preventing the accumulation of damaged DNA in cells. It associates\
    \ with\n  the MRE11-RAD50-NBS1 (MRN) damage-sensing complex and is rapidly recruited\
    \ to sites of DNA damage. Phosphorylation\n  of a serine promotes nuclear localization\
    \ of MRNIP [[cite:PUB00083234]].\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF15749, id=Pfam:PF15749, short_name=MRNIP, name=MRN-interacting
    protein, source URL and InterPro accession InterPro:IPR049472 agree with the selected
    frozen row. This establishes frozen identity correspondence, not current upstream
    taxonomy or function.
  target_ids:
  - PF15749
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 1583 proteins, 1591 matches, 0 structure entries and
    1370 AlphaFold models are frozen database counters, not independent experiments.
    Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF15749
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: 'EX_DUF MRNIP (IPR049472) retains imported prevention of damaged-DNA accumulation,
    association with the MRE11-RAD50-NBS1 complex, rapid DNA-damage-site recruitment
    and promotion of nuclear localization by phosphorylation of an unspecified serine.
    PUB00083234 was not independently read; no residue coordinate, kinase or intrinsic
    repair catalytic activity is established here. All seven counters agree between
    row and projection: 1583 proteins, 1591 matches, 1219 proteomes, 4007 taxa, 0
    structures, 1370 models, 27 architectures.'
  target_ids:
  - PF15749
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
  summary: Metadata-only source and captured-context review. EX_DUF MRNIP retains
    the imported role in preventing accumulation of damaged DNA, association with
    the MRE11-RAD50-NBS1 damage-sensing complex and rapid recruitment to DNA-damage
    sites. Association does not establish direct binding to each subunit, intrinsic
    nuclease or repair catalytic activity, tested organism or family-wide necessity.
    The source explicitly states that phosphorylation of a serine promotes MRNIP nuclear
    localization; it does not identify the serine position, kinase, phosphorylation
    stoichiometry or sufficiency and necessity in every family member. PUB00083234,
    zero structures and 1370 models were not inspected. Eight excess matches and 27
    architectures do not resolve per-protein organization. No length interval or exact
    domain boundary is supplied.
  target_ids:
  - PF15749
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: The captured literal accession (PF15749) and current-short-name (MRNIP)
    searches found no path or content hits under curation/families, evidence and history,
    including hidden and ignored files; the exact canonical overlay, evidence and
    history owners were absent. These bounded results do not establish absence for
    MRN, MRE11, RAD50, NBS1, expanded MRN-interacting names, phosphorylation or localization
    terms and PUB00083234 or wider literature. No primary paper, live upstream record,
    structural model or assay was inspected. A biological or historical assessment
    needs separately verified evidence and tested-protein scope. No accession-named
    overlay, evidence or history path was found by the bounded hidden/ignored-inclusive
    inventory; the inspected projection has no curated claim payload. Optional-field
    absence is not a seed-schema defect.
  target_ids:
  - PF15749
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
  - PF15749
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: Scientific additions would belong in the human-owned curation/families/PF15749.yaml
    overlay with appropriately licensed evidence and actual canonical history, followed
    by generation through src/dufmech/records.py. Frozen snapshots and generated records
    are not direct correction surfaces. No corrective edit is proposed by this seed
    audit.
  target_ids:
  - PF15749
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
