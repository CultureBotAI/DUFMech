# PF11155 DUF2935: seed identity, provenance and evidence-scope review

- Review: 20261029T014813Z-pf11155-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-29T01:35:30Z
- Finished UTC: 2026-10-29T01:48:13Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

PF11155 (DUF2935; InterPro:IPR021328) matches the verified frozen source and retains seed_status=UNKNOWN_CANDIDATE, characterization_status=UNSCORED and curation_status=SEEDED. PF11155/DUF2935 preserves its domain-named identity, IPR021328, qualified distribution and an imported structural account referring to an unnamed protein and two domains. The complete copied projection and actual row agree on the wording, provenance and all counters. One minor local representation finding remains OPEN: the retained family/domain account refers to the structure of this protein without identifying the observation subject. Attributable subject and scope clarification is required; no protein, structure, domain identity, metal interpretation or biological conclusion is selected.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: 1ad8fdccc772ffb9d68948351b7b2b0b8e43cd6b. The corpus has 8296 records; 2551 were covered and 5745 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF11155.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1ad8fdccc772ffb9d68948351b7b2b0b8e43cd6b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF11155 | data/families/PF11155.yaml | generated | PF11155 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF11155 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF11155 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF11155 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF11155 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF11155 | 488 valid canonical history records. |
| Generated schema check | passed | True | PF11155 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF11155.

The filename, pfam_id=PF11155, id=Pfam:PF11155, short_name=DUF2935, name=Domain of unknown function (DUF2935), source URL and InterPro accession InterPro:IPR021328 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF11155.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 1932 proteins, 3388 matches, 2 structure entries and 1174 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF11155.

PF11155/DUF2935 preserves its domain-named identity, IPR021328, qualified distribution and an imported structural account referring to an unnamed protein and two domains. The complete copied projection and actual row agree on the wording, provenance and all counters.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF11155.

Strict attribution review keeps the reviewed domain, the described full protein and the unverified structural example distinct. No tested protein identity or structure accession is established here; the account does not verify a structural property, metal interpretation or family-wide function. The appears qualification remains intact.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF11155.

The inventory lists 1,932 proteins, 3,388 matches, two structures and 1,174 models. Neither counts nor whole-copy fidelity identify the subject of the retained structural observation. One minor local attribution finding remains OPEN and requires attributable subject clarification before the account can be treated as protein-specific or family-wide curated evidence. The review disposition is needs_curation (NEEDS_FOLLOWUP). No protein, structure, domain identity or scientific interpretation is selected. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF11155.

seed_status=UNKNOWN_CANDIDATE, characterization_status=UNSCORED and curation_status=SEEDED express separate states. UNKNOWN_CANDIDATE is the retained lexical seed class, not an experimentally established absence of function. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF11155.

Attributable subject clarification belongs in separately authorized maintained PF11155 curation or a successor source freeze. This review retains a bounded representation finding and follow-up only.

### Clarify the subject of the structural observation

representation: concern. Targets: PF11155.

One minor local representation finding remains OPEN: the retained family/domain account refers to the structure of this protein without identifying the observation subject. Attributable subject and scope clarification is required; no protein, structure, domain identity, metal interpretation or biological conclusion is selected.

## Findings

### unidentified-structural-observation-subject: Clarify the subject of the structural observation

minor / open / confirmed; issue key: pf11155-unidentified-structural-observation-subject.

The family/domain description changes to 'the structure of this protein' without identifying a particular protein, organism, structure record or attributable observation subject in the retained account. The projection and selected row preserve the wording equally. Confirmed concerns the visible absence of a specified subject, not the scientific validity of the structural account.

## Recommended Actions And Acceptance Checks

### clarify-structural-observation-subject

In separately authorized curation, obtain attributable clarification of the subject and scope of the structural observation before treating it as protein-specific or family-wide curated evidence. Preserve the original wording until supported.

- Retain an attributable source locator identifying the subject and scope of the structural observation without choosing a protein or structure from contextual proximity or database counts.
- If attributable clarification is unavailable, document the bounded subject-attribution gap and retain the finding OPEN; a disclaimer alone does not resolve it.
- Any later authorized correction must preserve this immutable projection and selected row and use maintained inputs or a separately authorized successor freeze; no sequence, mechanistic or experimental work is requested.
- Later disposition must cite source-backed clarification and retain actual canonical history and applicable validation evidence.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF11155.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF11155 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF11155; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 488 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF11155 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf11155 | data/families/PF11155.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- scientific_review is false. Primary papers, original figures and assays, live database entries, current taxonomy and complete family-member coverage were not reviewed; source citation tokens are not verified primary evidence.
- The hidden/ignored-inclusive absence search is restricted to accession-bearing paths under curation/families, evidence and history. It does not exclude evidence in other local collections or the literature.
- Required input checks passed. Native saving validates the supplied content and constructs the immutable pair. The persisted pair is then read back through the native validator and covered by the batch just reviews-check recipe; this document does not preclaim those later results. Full publication QC is tracked separately and may require Pages source-pin updates.
- No scientific status, record, overlay, frozen input, canonical curation history or generated Pages artifact was changed by this review.
- One record per bundle; assessment prose was authored from the actual inspected record. The helper assembles provenance and schema fields; inspection and successful checks alone are not scientific findings.
- The explicit follow-up finding concerns imported textual representation. It does not resolve scientific truth or authorize the proposed corrective work.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
kind: record
repository: CultureBotAI/DUFMech
source:
  git_revision: 1ad8fdccc772ffb9d68948351b7b2b0b8e43cd6b
  inputs:
  - path: data/families/PF11155.yaml
    role: target
    sha256: 31ab57fc20bb275d9433e726ea0ba9e7b463f1efecd948ee7e8f08fbabfc12b8
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
  label: PF11155
  owner_paths:
  - path: curation/families/PF11155.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF11155.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: d5bceb2a8fe125ed3a623a30fc60f8738cc69c7d62a4b2edbf03951afeccb423
  target_id: PF11155
schema_version: 1.0.0
review_id: 20261029T014813Z-pf11155-seed-record-review
title: 'PF11155 DUF2935: seed identity, provenance and evidence-scope review'
started_at: '2026-10-29T01:35:30Z'
finished_at: '2026-10-29T01:48:13Z'
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
verdict: needs_curation
native_verdict: NEEDS_FOLLOWUP
scientific_review: false
summary: 'PF11155 (DUF2935; InterPro:IPR021328) matches the verified frozen source
  and retains seed_status=UNKNOWN_CANDIDATE, characterization_status=UNSCORED and
  curation_status=SEEDED. PF11155/DUF2935 preserves its domain-named identity, IPR021328,
  qualified distribution and an imported structural account referring to an unnamed
  protein and two domains. The complete copied projection and actual row agree on
  the wording, provenance and all counters. One minor local representation finding
  remains OPEN: the retained family/domain account refers to the structure of this
  protein without identifying the observation subject. Attributable subject and scope
  clarification is required; no protein, structure, domain identity, metal interpretation
  or biological conclusion is selected.'
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: 1ad8fdccc772ffb9d68948351b7b2b0b8e43cd6b. The corpus has 8296
    records; 2551 were covered and 5745 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF11155.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF11155
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF11155
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF11155
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-242-attempt-001/PF11155-targets.yaml
    --input data/families/PF11155.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF11155
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-242-attempt-001/prepare.py
    PF11155
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF11155
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
  - PF11155
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
  - PF11155
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
  - PF11155
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF11155.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-10-29T01:48:13Z'
  support: supports
  summary: Read the complete PF11155 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: 31ab57fc20bb275d9433e726ea0ba9e7b463f1efecd948ee7e8f08fbabfc12b8
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF11155; companion manifest and TSV; native verified inspection
  accessed_at: '2026-10-29T01:48:13Z'
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
  accessed_at: '2026-10-29T01:48:13Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-10-29T01:48:13Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 488 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF11155
  accessed_at: '2026-10-29T01:48:13Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF11155. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf11155
  kind: record_content
  reference: data/families/PF11155.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-29T01:48:13Z'
  support: context_only
  snapshot_sha256: 31ab57fc20bb275d9433e726ea0ba9e7b463f1efecd948ee7e8f08fbabfc12b8
  quote: "id: Pfam:PF11155\npfam_id: PF11155\nname: Domain of unknown function (DUF2935)\n\
    short_name: DUF2935\nseed_status: UNKNOWN_CANDIDATE\ncharacterization_status:\
    \ UNSCORED\ncuration_status: SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF11155\n\
    counters:\n  proteins: 1932\n  matches: 3388\n  proteomes: 1153\n  taxa: 1707\n\
    \  structures: 2\n  alphafold_models: 1174\n  domain_architectures: 4\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR021328\ndescription: This family of proteins with unknown\
    \ function appears to be restricted to Firmicutes. The\n  structure of this protein\
    \ has been solved and each domain is composed of four alpha helices. A metal\n\
    \  cluster composed of iron and magnesium lies between the two domains.\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF11155, id=Pfam:PF11155, short_name=DUF2935, name=Domain
    of unknown function (DUF2935), source URL and InterPro accession InterPro:IPR021328
    agree with the selected frozen row. This establishes frozen identity correspondence,
    not current upstream taxonomy or function.
  target_ids:
  - PF11155
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 1932 proteins, 3388 matches, 2 structure entries and
    1174 AlphaFold models are frozen database counters, not independent experiments.
    Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF11155
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: PF11155/DUF2935 preserves its domain-named identity, IPR021328, qualified
    distribution and an imported structural account referring to an unnamed protein
    and two domains. The complete copied projection and actual row agree on the wording,
    provenance and all counters.
  target_ids:
  - PF11155
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
  summary: Strict attribution review keeps the reviewed domain, the described full
    protein and the unverified structural example distinct. No tested protein identity
    or structure accession is established here; the account does not verify a structural
    property, metal interpretation or family-wide function. The appears qualification
    remains intact.
  target_ids:
  - PF11155
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: The inventory lists 1,932 proteins, 3,388 matches, two structures and 1,174
    models. Neither counts nor whole-copy fidelity identify the subject of the retained
    structural observation. One minor local attribution finding remains OPEN and requires
    attributable subject clarification before the account can be treated as protein-specific
    or family-wide curated evidence. The review disposition is needs_curation (NEEDS_FOLLOWUP).
    No protein, structure, domain identity or scientific interpretation is selected.
    No accession-named overlay, evidence or history path was found by the bounded
    hidden/ignored-inclusive inventory; the inspected projection has no curated claim
    payload. Optional-field absence is not a seed-schema defect.
  target_ids:
  - PF11155
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
  - PF11155
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: Attributable subject clarification belongs in separately authorized maintained
    PF11155 curation or a successor source freeze. This review retains a bounded representation
    finding and follow-up only.
  target_ids:
  - PF11155
  evidence_ids:
  - profile
  - record
  - validation
- assessment_id: unidentified-structural-observation-subject
  area: representation
  topic: Clarify the subject of the structural observation
  outcome: concern
  summary: 'One minor local representation finding remains OPEN: the retained family/domain
    account refers to the structure of this protein without identifying the observation
    subject. Attributable subject and scope clarification is required; no protein,
    structure, domain identity, metal interpretation or biological conclusion is selected.'
  target_ids:
  - PF11155
  evidence_ids:
  - record
  - snapshot
findings:
- finding_id: unidentified-structural-observation-subject
  issue_key: pf11155-unidentified-structural-observation-subject
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Clarify the subject of the structural observation
  description: The family/domain description changes to 'the structure of this protein'
    without identifying a particular protein, organism, structure record or attributable
    observation subject in the retained account. The projection and selected row preserve
    the wording equally. Confirmed concerns the visible absence of a specified subject,
    not the scientific validity of the structural account.
  target_ids:
  - PF11155
  field_paths:
  - description
  evidence_ids:
  - record
  - snapshot
  normalization_reason: A localized representation gap leaves accession identity and
    frozen provenance intact. No protein, structure, domain or biological meaning
    is selected.
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF11155.yaml
    role: Future maintained source-backed subject and scope clarification only; no
      record or overlay is edited by this review.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: A separately authorized successor source freeze may retain attributable
      clarification; no generator defect is alleged.
actions:
- action_id: clarify-structural-observation-subject
  description: In separately authorized curation, obtain attributable clarification
    of the subject and scope of the structural observation before treating it as protein-specific
    or family-wide curated evidence. Preserve the original wording until supported.
  finding_ids:
  - unidentified-structural-observation-subject
  target_ids:
  - PF11155
  acceptance_checks:
  - Retain an attributable source locator identifying the subject and scope of the
    structural observation without choosing a protein or structure from contextual
    proximity or database counts.
  - If attributable clarification is unavailable, document the bounded subject-attribution
    gap and retain the finding OPEN; a disclaimer alone does not resolve it.
  - Any later authorized correction must preserve this immutable projection and selected
    row and use maintained inputs or a separately authorized successor freeze; no
    sequence, mechanistic or experimental work is requested.
  - Later disposition must cite source-backed clarification and retain actual canonical
    history and applicable validation evidence.
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF11155.yaml
    role: Future maintained source-backed subject and scope clarification only; no
      record or overlay is edited by this review.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: A separately authorized successor source freeze may retain attributable
      clarification; no generator defect is alleged.
  generator: just records --apply
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
- The explicit follow-up finding concerns imported textual representation. It does
  not resolve scientific truth or authorize the proposed corrective work.
tags:
- seed-review
- unreviewed-record-coverage
```
