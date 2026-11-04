# PF19720 DUF6214: seed identity, provenance and evidence-scope review

- Review: 20261104T105852Z-pf19720-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-11-04T10:50:23Z
- Finished UTC: 2026-11-04T10:58:52Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: seed_only
- Scientific review: false

## Summary

PF19720 (DUF6214; InterPro:IPR046186) matches the verified frozen source and retains seed_status=UNKNOWN_CANDIDATE, characterization_status=UNSCORED and curation_status=SEEDED. The complete projection and frozen row agree on DUF6214/IPR046186 and UNKNOWN_CANDIDATE. The imported description associates a member with BGC0001782, other (unspecified), spiroindimicin A and Streptomyces sp. SCSIO 03032, citing PUB00099387. It says the family appears predominantly in Actinobacteria. Frozen counts are 370 proteins, 401 matches, 365 proteomes, 404 taxa, 0 structure entries, 152 AlphaFold models and 3 domain architecture entries.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: aa7d08bcf3a9a03879d06cffd075bc083d29788f. The corpus has 8296 records; 5561 were covered and 2735 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF19720.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base aa7d08bcf3a9a03879d06cffd075bc083d29788f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF19720 | data/families/PF19720.yaml | generated | PF19720 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF19720 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF19720 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF19720 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF19720 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF19720 | 489 valid canonical history records. |
| Generated schema check | passed | True | PF19720 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF19720.

The filename, pfam_id=PF19720, id=Pfam:PF19720, short_name=DUF6214, name=Family of unknown function (DUF6214), source URL and InterPro accession InterPro:IPR046186 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF19720.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 370 proteins, 401 matches, 0 structure entries and 152 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF19720.

The complete projection and frozen row agree on DUF6214/IPR046186 and UNKNOWN_CANDIDATE. The imported description associates a member with BGC0001782, other (unspecified), spiroindimicin A and Streptomyces sp. SCSIO 03032, citing PUB00099387. It says the family appears predominantly in Actinobacteria. Frozen counts are 370 proteins, 401 matches, 365 proteomes, 404 taxa, 0 structure entries, 152 AlphaFold models and 3 domain architecture entries.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF19720.

Preserve the unspecified class and exact strain designation without inventing a species. Excess matches do not establish repeat or copy architecture. The association does not establish a specific reaction, necessity or family-wide spiroindimicin A production.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF19720.

No primary paper, individual protein, sequence, alignment, assay, taxonomy, structure or model was inspected. Bounded hidden/ignored-inclusive searches used literal PF19720 and DUF6214 under curation/families, evidence and history and found no path or content matches. Cluster identifiers, citation tokens, compound, organism, strain, taxonomic, structural and functional terms were not separately searched. BGC0001782, the unspecified class, strain-to-member mapping and PUB00099387 were not independently checked. No class refinement, species or domain arrangement was inferred. Zero structure entries is a frozen count, not proof that structures or experiments are absent elsewhere. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF19720.

seed_status=UNKNOWN_CANDIDATE, characterization_status=UNSCORED and curation_status=SEEDED express separate states. UNKNOWN_CANDIDATE is the retained lexical seed class, not an experimentally established absence of function. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF19720.

Scientific additions would belong in the human-owned curation/families/PF19720.yaml overlay with appropriately licensed evidence and actual canonical history, followed by generation through src/dufmech/records.py. Frozen snapshots and generated records are not direct correction surfaces. No corrective edit is proposed by this seed audit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF19720.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF19720 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF19720; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 489 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF19720 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf19720 | data/families/PF19720.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

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
  - path: data/families/PF19720.yaml
    role: target
    sha256: 91c9c495668af1a53983509e62872009fc41fc56ccae3d5340523e49a3b867bc
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
  label: PF19720
  owner_paths:
  - path: curation/families/PF19720.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF19720.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: a7a5cb4c4f5523ad0063a440898073ee85762300c936ea4aef0df82f4be99618
  target_id: PF19720
schema_version: 1.0.0
review_id: 20261104T105852Z-pf19720-seed-record-review
title: 'PF19720 DUF6214: seed identity, provenance and evidence-scope review'
started_at: '2026-11-04T10:50:23Z'
finished_at: '2026-11-04T10:58:52Z'
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
summary: PF19720 (DUF6214; InterPro:IPR046186) matches the verified frozen source
  and retains seed_status=UNKNOWN_CANDIDATE, characterization_status=UNSCORED and
  curation_status=SEEDED. The complete projection and frozen row agree on DUF6214/IPR046186
  and UNKNOWN_CANDIDATE. The imported description associates a member with BGC0001782,
  other (unspecified), spiroindimicin A and Streptomyces sp. SCSIO 03032, citing PUB00099387.
  It says the family appears predominantly in Actinobacteria. Frozen counts are 370
  proteins, 401 matches, 365 proteomes, 404 taxa, 0 structure entries, 152 AlphaFold
  models and 3 domain architecture entries.
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: aa7d08bcf3a9a03879d06cffd075bc083d29788f. The corpus has 8296
    records; 5561 were covered and 2735 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF19720.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF19720
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF19720
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF19720
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-543-attempt-001/PF19720-targets.yaml
    --input data/families/PF19720.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF19720
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-543-attempt-001/prepare.py
    PF19720
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF19720
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
  - PF19720
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
  - PF19720
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
  - PF19720
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF19720.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-11-04T10:58:52Z'
  support: supports
  summary: Read the complete PF19720 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: 91c9c495668af1a53983509e62872009fc41fc56ccae3d5340523e49a3b867bc
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF19720; companion manifest and TSV; native verified inspection
  accessed_at: '2026-11-04T10:58:52Z'
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
  accessed_at: '2026-11-04T10:58:52Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-11-04T10:58:52Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 489 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF19720
  accessed_at: '2026-11-04T10:58:52Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF19720. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf19720
  kind: record_content
  reference: data/families/PF19720.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-11-04T10:58:52Z'
  support: context_only
  snapshot_sha256: 91c9c495668af1a53983509e62872009fc41fc56ccae3d5340523e49a3b867bc
  quote: "id: Pfam:PF19720\npfam_id: PF19720\nname: Family of unknown function (DUF6214)\n\
    short_name: DUF6214\nseed_status: UNKNOWN_CANDIDATE\ncharacterization_status:\
    \ UNSCORED\ncuration_status: SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF19720\n\
    counters:\n  proteins: 370\n  matches: 401\n  proteomes: 365\n  taxa: 404\n  structures:\
    \ 0\n  alphafold_models: 152\n  domain_architectures: 3\nprovenance:\n  snapshot_id:\
    \ interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR046186\ndescription: This entry represents a member of\
    \ a biosynthetic gene cluster (BGC). This BGC (BGC0001782)\n  is described by\
    \ MIBiG as an example of the following biosynthetic class, other (unspecified).\
    \ It includes\n  a member from the spiroindimicin A biosynthetic gene cluster\
    \ from Streptomyces sp. SCSIO 03032 [[cite:PUB00099387]].\n  This family appears\
    \ to be predominantly found in Actinobacteria.\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF19720, id=Pfam:PF19720, short_name=DUF6214, name=Family
    of unknown function (DUF6214), source URL and InterPro accession InterPro:IPR046186
    agree with the selected frozen row. This establishes frozen identity correspondence,
    not current upstream taxonomy or function.
  target_ids:
  - PF19720
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 370 proteins, 401 matches, 0 structure entries and 152
    AlphaFold models are frozen database counters, not independent experiments. Raw
    input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF19720
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: The complete projection and frozen row agree on DUF6214/IPR046186 and UNKNOWN_CANDIDATE.
    The imported description associates a member with BGC0001782, other (unspecified),
    spiroindimicin A and Streptomyces sp. SCSIO 03032, citing PUB00099387. It says
    the family appears predominantly in Actinobacteria. Frozen counts are 370 proteins,
    401 matches, 365 proteomes, 404 taxa, 0 structure entries, 152 AlphaFold models
    and 3 domain architecture entries.
  target_ids:
  - PF19720
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
  summary: Preserve the unspecified class and exact strain designation without inventing
    a species. Excess matches do not establish repeat or copy architecture. The association
    does not establish a specific reaction, necessity or family-wide spiroindimicin
    A production.
  target_ids:
  - PF19720
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: No primary paper, individual protein, sequence, alignment, assay, taxonomy,
    structure or model was inspected. Bounded hidden/ignored-inclusive searches used
    literal PF19720 and DUF6214 under curation/families, evidence and history and
    found no path or content matches. Cluster identifiers, citation tokens, compound,
    organism, strain, taxonomic, structural and functional terms were not separately
    searched. BGC0001782, the unspecified class, strain-to-member mapping and PUB00099387
    were not independently checked. No class refinement, species or domain arrangement
    was inferred. Zero structure entries is a frozen count, not proof that structures
    or experiments are absent elsewhere. No accession-named overlay, evidence or history
    path was found by the bounded hidden/ignored-inclusive inventory; the inspected
    projection has no curated claim payload. Optional-field absence is not a seed-schema
    defect.
  target_ids:
  - PF19720
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
  - PF19720
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: Scientific additions would belong in the human-owned curation/families/PF19720.yaml
    overlay with appropriately licensed evidence and actual canonical history, followed
    by generation through src/dufmech/records.py. Frozen snapshots and generated records
    are not direct correction surfaces. No corrective edit is proposed by this seed
    audit.
  target_ids:
  - PF19720
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
