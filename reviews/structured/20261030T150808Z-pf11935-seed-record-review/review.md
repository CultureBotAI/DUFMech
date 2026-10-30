# PF11935 SYMPK_PTA1_N: seed identity, provenance and evidence-scope review

- Review: 20261030T150808Z-pf11935-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-30T14:36:02Z
- Finished UTC: 2026-10-30T15:08:08Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: seed_only
- Scientific review: false

## Summary

PF11935 (SYMPK_PTA1_N; InterPro:IPR032460) matches the verified frozen source and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED. PF11935 / InterPro:IPR032460 reproduces Symplekin/PTA1 N-terminal, SYMPK_PTA1_N and EX_DUF from the frozen row. The full imported processing, fold and Ssu72 narrative and four citation identifiers are retained. All seven counters match, including 4,626 proteins, 4,686 matches, 18 structures and 3,038 models.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: 1ad8fdccc772ffb9d68948351b7b2b0b8e43cd6b. The corpus has 8296 records; 3031 were covered and 5265 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF11935.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1ad8fdccc772ffb9d68948351b7b2b0b8e43cd6b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF11935 | data/families/PF11935.yaml | generated | PF11935 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF11935 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF11935 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF11935 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF11935 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF11935 | 488 valid canonical history records. |
| Generated schema check | passed | True | PF11935 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF11935.

The filename, pfam_id=PF11935, id=Pfam:PF11935, short_name=SYMPK_PTA1_N, name=Symplekin/PTA1 N-terminal, source URL and InterPro accession InterPro:IPR032460 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF11935.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 4626 proteins, 4686 matches, 18 structure entries and 3038 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF11935.

PF11935 / InterPro:IPR032460 reproduces Symplekin/PTA1 N-terminal, SYMPK_PTA1_N and EX_DUF from the frozen row. The full imported processing, fold and Ssu72 narrative and four citation identifiers are retained. All seven counters match, including 4,626 proteins, 4,686 matches, 18 structures and 3,038 models.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF11935.

The target is the N-terminal domain of animal Symplekin and budding-yeast PTA1, typically 239–261 residues. Distinguish whole-protein processing roles and CPF-complex context from the domain's attributed interaction with Ssu72. Imported ARM/HEAT-fold and in-vitro stimulation statements do not establish that this domain is itself a phosphatase or validate every family member.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF11935.

The hidden/ignored-inclusive accession and short-name search under curation/families, evidence and history found no matching local material or canonical owners. The cited studies, experimental conditions and organism/member boundaries were not reassessed. EX_DUF and the imported functional narrative do not supersede local UNSCORED/SEEDED; retain seed_only without a corrective finding. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF11935.

seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED express separate states. EX_DUF records historical renaming and is compatible with imported functional descriptions; it is not evidence that all members were tested. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF11935.

Scientific additions would belong in the human-owned curation/families/PF11935.yaml overlay with appropriately licensed evidence and actual canonical history, followed by generation through src/dufmech/records.py. Frozen snapshots and generated records are not direct correction surfaces. No corrective edit is proposed by this seed audit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF11935.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF11935 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF11935; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 488 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF11935 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf11935 | data/families/PF11935.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

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
  git_revision: 1ad8fdccc772ffb9d68948351b7b2b0b8e43cd6b
  inputs:
  - path: data/families/PF11935.yaml
    role: target
    sha256: fe9d9c3fae1ebd10d93fa55386f783c2098c4b643843a3b7d5dcad67a62a091d
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
  label: PF11935
  owner_paths:
  - path: curation/families/PF11935.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF11935.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: b3f7f728f5a4e0f0a3eea229dda4ad1759b07b3da87a0723e0cde6fa14fec5f0
  target_id: PF11935
schema_version: 1.0.0
review_id: 20261030T150808Z-pf11935-seed-record-review
title: 'PF11935 SYMPK_PTA1_N: seed identity, provenance and evidence-scope review'
started_at: '2026-10-30T14:36:02Z'
finished_at: '2026-10-30T15:08:08Z'
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
summary: PF11935 (SYMPK_PTA1_N; InterPro:IPR032460) matches the verified frozen source
  and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED.
  PF11935 / InterPro:IPR032460 reproduces Symplekin/PTA1 N-terminal, SYMPK_PTA1_N
  and EX_DUF from the frozen row. The full imported processing, fold and Ssu72 narrative
  and four citation identifiers are retained. All seven counters match, including
  4,626 proteins, 4,686 matches, 18 structures and 3,038 models.
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: 1ad8fdccc772ffb9d68948351b7b2b0b8e43cd6b. The corpus has 8296
    records; 3031 were covered and 5265 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF11935.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF11935
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF11935
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF11935
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-290-attempt-001/PF11935-targets.yaml
    --input data/families/PF11935.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF11935
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-290-attempt-001/prepare.py
    PF11935
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF11935
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
  - PF11935
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
  summary: 488 valid canonical history records.
  target_ids:
  - PF11935
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
  - PF11935
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF11935.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-10-30T15:08:08Z'
  support: supports
  summary: Read the complete PF11935 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: fe9d9c3fae1ebd10d93fa55386f783c2098c4b643843a3b7d5dcad67a62a091d
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF11935; companion manifest and TSV; native verified inspection
  accessed_at: '2026-10-30T15:08:08Z'
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
  accessed_at: '2026-10-30T15:08:08Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-10-30T15:08:08Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 488 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF11935
  accessed_at: '2026-10-30T15:08:08Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF11935. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf11935
  kind: record_content
  reference: data/families/PF11935.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-30T15:08:08Z'
  support: context_only
  snapshot_sha256: fe9d9c3fae1ebd10d93fa55386f783c2098c4b643843a3b7d5dcad67a62a091d
  quote: "id: Pfam:PF11935\npfam_id: PF11935\nname: Symplekin/PTA1 N-terminal\nshort_name:\
    \ SYMPK_PTA1_N\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF11935\n\
    counters:\n  proteins: 4626\n  matches: 4686\n  proteomes: 2872\n  taxa: 7645\n\
    \  structures: 18\n  alphafold_models: 3038\n  domain_architectures: 70\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR032460\ndescription: This is the N-terminal domain found\
    \ in the symplekin protein from animals and PTA1 protein\n  from budding yeasts\
    \ and is typically between 239 to 261 amino acids in length. Symplekin is a scaffold\n\
    \  protein that functions as a component of a multimolecular complex involved\
    \ in histone mRNA 3'-end processing\n  [[cite:PUB00068954],[cite:PUB00068955]].\
    \ PTA1 is involved in pre-tRNA processing. PTA1 is a subunit\n  of the cleavage\
    \ and polyadenylation factor (CPF), which plays a key role in polyadenylation-dependent\n\
    \  pre-mRNA 3'-end formation and cooperates with cleavage factors including the\
    \ CFIA complex and NAB4/CFIB\n  [[cite:PUB00070276]]. This domain has the ARM\
    \ or HEAT fold, with seven pairs of antiparallel alpha-helices\n  arranged in\
    \ the shape of an arc. It is important for interaction with Ssu72 and stimulates\
    \ Ssu72 C-terminal\n  domain phosphatase activity in vitro [[cite:PUB00065426]].\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF11935, id=Pfam:PF11935, short_name=SYMPK_PTA1_N,
    name=Symplekin/PTA1 N-terminal, source URL and InterPro accession InterPro:IPR032460
    agree with the selected frozen row. This establishes frozen identity correspondence,
    not current upstream taxonomy or function.
  target_ids:
  - PF11935
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 4626 proteins, 4686 matches, 18 structure entries and
    3038 AlphaFold models are frozen database counters, not independent experiments.
    Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF11935
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: PF11935 / InterPro:IPR032460 reproduces Symplekin/PTA1 N-terminal, SYMPK_PTA1_N
    and EX_DUF from the frozen row. The full imported processing, fold and Ssu72 narrative
    and four citation identifiers are retained. All seven counters match, including
    4,626 proteins, 4,686 matches, 18 structures and 3,038 models.
  target_ids:
  - PF11935
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
  summary: The target is the N-terminal domain of animal Symplekin and budding-yeast
    PTA1, typically 239–261 residues. Distinguish whole-protein processing roles and
    CPF-complex context from the domain's attributed interaction with Ssu72. Imported
    ARM/HEAT-fold and in-vitro stimulation statements do not establish that this domain
    is itself a phosphatase or validate every family member.
  target_ids:
  - PF11935
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: The hidden/ignored-inclusive accession and short-name search under curation/families,
    evidence and history found no matching local material or canonical owners. The
    cited studies, experimental conditions and organism/member boundaries were not
    reassessed. EX_DUF and the imported functional narrative do not supersede local
    UNSCORED/SEEDED; retain seed_only without a corrective finding. No accession-named
    overlay, evidence or history path was found by the bounded hidden/ignored-inclusive
    inventory; the inspected projection has no curated claim payload. Optional-field
    absence is not a seed-schema defect.
  target_ids:
  - PF11935
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
  - PF11935
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: Scientific additions would belong in the human-owned curation/families/PF11935.yaml
    overlay with appropriately licensed evidence and actual canonical history, followed
    by generation through src/dufmech/records.py. Frozen snapshots and generated records
    are not direct correction surfaces. No corrective edit is proposed by this seed
    audit.
  target_ids:
  - PF11935
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
