# PF04229 GrpB: seed identity, provenance and evidence-scope review

- Review: 20261021T072036Z-pf04229-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-21T07:15:11Z
- Finished UTC: 2026-10-21T07:20:36Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: seed_only
- Scientific review: false

## Summary

PF04229 (GrpB; InterPro:IPR007344) matches the verified frozen source and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED. The GrpB seed description gives a suggested superfamily assignment and a qualified domain/protein association, with PUB00066751 and PUB00066752. Those sources were not independently resolved. Bounded identity/provenance fields in a separate PF01121 overlay and its identity note additionally mention PF04229 as a distinct region of a complete protein; their scientific accuracy and historical mappings were not reverified.

## Scope And Provenance

Full inspection of the PF04229 seed projection and its unique frozen row for identity, provenance, representation and status, plus bounded identity metadata extracts from two captured PF01121 files. Only the existence and wording of prior domain/protein mapping context were assessed. The complete PF01121 overlay, underlying science and historical or live member mappings were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: 59f8f2b8a93c2e6373e02dfe0fb289ecbd76feaa. The corpus has 8296 records; 401 were covered and 7895 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF04229.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 59f8f2b8a93c2e6373e02dfe0fb289ecbd76feaa.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF04229 | data/families/PF04229.yaml | generated | PF04229 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF04229 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric and local-context input capture | passed | True | PF04229 | Captured rubric, recipe and whole-file hashes for both PF01121 context inputs; substantive reading of those inputs was limited to the stated identity/provenance extracts. |
| Exact frozen-row correspondence | passed | True | PF04229 | The PF04229 projection agrees with its unique frozen row for identity, optional fields, seed status and counters and has no own curated payload. This comparison does not verify the separate PF01121 mapping assertions. |
| Native closed-schema and projection checks | passed | True | PF04229 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF04229 | 420 valid canonical history records. |
| Generated schema check | passed | True | PF04229 | Generated schema check found 0 differing generated files. |
| Bounded exact-accession content search | passed | True | PF04229 | The hidden/ignored-inclusive content search found PF04229 references in exactly the two captured PF01121 files. This check establishes file presence, not scientific correctness. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF04229.

The filename, pfam_id=PF04229, id=Pfam:PF04229, short_name=GrpB, name=GrpB protein, source URL and InterPro accession InterPro:IPR007344 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF04229.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 7942 proteins, 7971 matches, 2 structure entries and 4945 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description and prior local identity context versus scientific support

evidence: unknown. Targets: PF04229.

The GrpB seed description gives a suggested superfamily assignment and a qualified domain/protein association, with PUB00066751 and PUB00066752. Those sources were not independently resolved. Bounded identity/provenance fields in a separate PF01121 overlay and its identity note additionally mention PF04229 as a distinct region of a complete protein; their scientific accuracy and historical mappings were not reverified.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF04229.

The PF04229 family target, the separately owned PF01121 family and the full protein are distinct entities. Local reference-identity statements and unresolved experimental identity remain different evidential scopes. Their shared protein context does not transfer whole-protein or other-domain observations to PF04229. The two PF01121 files are context inputs only, not an additional review target or adopted scientific evidence. This assessment remains non-operational identity, provenance and qualification.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF04229.

PF04229 has no own curated projection payload or overlay, but relevant identity context exists in two PF01121 files. Prior mapping statements and their explicitly retained identity limitations remain unassessed. The 7942 proteins, two structures and 98 architectures are frozen coverage metadata. No residue identity, sequence or construct detail, experimental parameter, perturbation, outcome, mechanism expansion or functional follow-up is adopted or proposed. The accession-named path inventory and literal content search establish different facts: no own PF04229 payload was found, but two PF01121 files contain relevant identity context.

### Seed, scoring and review states

consistency: supported. Targets: PF04229.

seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED express separate states. EX_DUF records historical renaming and is compatible with imported functional descriptions; it is not evidence that all members were tested. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF04229.

The PF01121 files remain prior context and are not transferred assertions or correction surfaces for PF04229. Any separately authorized PF04229 curation belongs in its own maintained overlay with attributable evidence and canonical history. This review proposes no record edit, functional follow-up or scientific status promotion.

### Bounded identity-context provenance and source binding

provenance: supported. Targets: PF04229.

Both named PF01121 files are captured by whole-file hashes. Bounded metadata extracts explicitly distinguish the two family regions on one named protein. This supports the existence and traceability of the prior mapping statement, not the correctness of the coordinates or scientific claims.

### Prior mapping and domain-specific scientific support remain unassessed

evidence: unknown. Targets: PF04229.

The prior documents' mapping statements and underlying observations were not independently verified. Shared protein identity does not assign whole-protein or other-domain evidence to PF04229. These contextual inputs do not establish PF04229 scientific characterization or justify changing UNSCORED/SEEDED or SEED_ONLY.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF04229.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF04229 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF04229; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 420 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF04229 | supports | The bounded path inventory found no accession-named PF04229 payload, and native inspection found no own overlay or curated projection fields. A separate content search found references in the two captured PF01121 files; the path result does not establish absence of local context. |
| local-context-overlay | curation/families/PF01121.yaml; Bounded metadata: pfam_id and causal_graphs[1:3].family_mapping; no complete-overlay read | context_only | The two target-relevant family_mapping fields distinguish PF01121 and PF04229 as different regions of a complete protein and retain limits on reference and experimental identity. These are prior local mapping assertions. Whole-file hashing binds the input but does not imply review of its remaining contents or scientific evidence. |
| local-context-note | evidence/PF01121/CoaE-identity.txt; Bounded identity/provenance lines 1-8, 14-25 and 29-32; prior identity limitations retained without scientific or experimental interpretation | context_only | The retained identity note separately names PF01121 and PF04229 in a complete protein and records prior reference-identity and unresolved experimental-identity context. Its mapping assertions and earlier source access were not independently verified. No sequence, construct, residue-role, assay or mechanistic detail is adopted. |
| local-context-search | curation; evidence; history; Literal PF04229 content references within the bounded roots | supports | The bounded content search found the two named PF01121 files. Their presence is distinct from the empty accession-named PF04229 path inventory. |
| duf-projection-pf04229 | data/families/PF04229.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- scientific_review is false. The complete PF04229 seed and frozen row were read, but the two PF01121 inputs were considered only through bounded identity/provenance extracts. The complete overlay, primary sources, live mappings and experimental material were not reassessed. Earlier access statements describe prior curation, not work performed here.
- The empty path inventory is limited to accession-named paths under curation/families, evidence and history, including hidden/ignored files. A separate content search across curation, evidence and history found exactly the two named context files. Neither establishes absence of evidence elsewhere.
- Required input checks passed. Native saving validates the supplied content and constructs the immutable pair. The persisted pair is then read back through the native validator and covered by the batch just reviews-check recipe; this document does not preclaim those later results. Full publication QC is tracked separately and may require Pages source-pin updates.
- No scientific status, record, overlay, frozen input, canonical curation history or generated Pages artifact was changed by this review.
- One record per bundle; assessment prose was authored from the actual inspected record. The helper assembles provenance and schema fields; inspection and successful checks alone are not scientific findings.
- Whole-file context hashes do not imply complete substantive reads. The two PF01121 inputs are context_only evidence; this remains one PF04229 target with its native digest, seed-only verdict, empty findings/actions and scientific_review=false. No domain-specific functional or engineering claim is transferred.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
kind: record
repository: CultureBotAI/DUFMech
source:
  git_revision: 59f8f2b8a93c2e6373e02dfe0fb289ecbd76feaa
  inputs:
  - path: data/families/PF04229.yaml
    role: target
    sha256: d14c6ce5af7c555ff74df9f36a71a9b55acbc450d368a50a855e155c4c3634c5
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
  - path: curation/families/PF01121.yaml
    sha256: 814f84ac1a5f4f83c3e190f048ee714f1aebc2b20a1073a418651249527c7717
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
  - path: evidence/PF01121/CoaE-identity.txt
    sha256: 411d10375ca1afd1834120b67c5ce42c21a066962a37ed5a89ee1ec11cb61e2d
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
  label: PF04229
  owner_paths:
  - path: curation/families/PF04229.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF04229.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: 25daceb73e603d2b619eda542ecbd74aebe9fc9473b6183122d7eed12feb078a
  target_id: PF04229
schema_version: 1.0.0
review_id: 20261021T072036Z-pf04229-seed-record-review
title: 'PF04229 GrpB: seed identity, provenance and evidence-scope review'
started_at: '2026-10-21T07:15:11Z'
finished_at: '2026-10-21T07:20:36Z'
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
summary: PF04229 (GrpB; InterPro:IPR007344) matches the verified frozen source and
  retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED.
  The GrpB seed description gives a suggested superfamily assignment and a qualified
  domain/protein association, with PUB00066751 and PUB00066752. Those sources were
  not independently resolved. Bounded identity/provenance fields in a separate PF01121
  overlay and its identity note additionally mention PF04229 as a distinct region
  of a complete protein; their scientific accuracy and historical mappings were not
  reverified.
scope:
  description: Full inspection of the PF04229 seed projection and its unique frozen
    row for identity, provenance, representation and status, plus bounded identity
    metadata extracts from two captured PF01121 files. Only the existence and wording
    of prior domain/protein mapping context were assessed. The complete PF01121 overlay,
    underlying science and historical or live member mappings were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: 59f8f2b8a93c2e6373e02dfe0fb289ecbd76feaa. The corpus has 8296
    records; 401 were covered and 7895 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF04229.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF04229
  exclusions:
  - target: Primary literature, live database state, complete PF01121 overlay content,
      scientific mapping verification and other-family scientific assessment
    reason: The PF01121 files are local identity/provenance context only. PF01121
      is not a review target; no experimental parameters, constructs, perturbations,
      outcomes or mechanistic interpretation are adopted.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF04229
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF04229
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric and local-context input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-027/PF04229-targets.yaml
    --input data/families/PF04229.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
    --input data/worklists/interpro-pfam-duf-2026-10-10.manifest.json --input data/worklists/interpro-pfam-duf-2026-10-10.tsv
    --input docs/records.md --input docs/reviews.md --input docs/history.md --input
    docs/sources.md --input docs/record-reviews.md --input docs/record-review-profile.md
    --input .claude/skills/review-yaml-record/SKILL.md --input .claude/skills/curate-yaml-record/references/review-checklist.md
    --input schema/record_review.yaml --input justfile --input curation/families/PF01121.yaml
    --input evidence/PF01121/CoaE-identity.txt
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Captured rubric, recipe and whole-file hashes for both PF01121 context
    inputs; substantive reading of those inputs was limited to the stated identity/provenance
    extracts.
  target_ids:
  - PF04229
  evidence_ids:
  - profile
  - local-context-overlay
  - local-context-note
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-027/prepare.py
    PF04229
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The PF04229 projection agrees with its unique frozen row for identity,
    optional fields, seed status and counters and has no own curated payload. This
    comparison does not verify the separate PF01121 mapping assertions.
  target_ids:
  - PF04229
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
  - PF04229
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
  summary: 420 valid canonical history records.
  target_ids:
  - PF04229
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
  - PF04229
  evidence_ids:
  - validation
- check_id: local-context-search
  name: Bounded exact-accession content search
  command: rg -l --text --hidden --no-ignore --fixed-strings --word-regexp -- PF04229
    curation evidence history
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The hidden/ignored-inclusive content search found PF04229 references in
    exactly the two captured PF01121 files. This check establishes file presence,
    not scientific correctness.
  target_ids:
  - PF04229
  evidence_ids:
  - local-context-search
  - local-context-overlay
  - local-context-note
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF04229.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-10-21T07:20:36Z'
  support: supports
  summary: Read the complete PF04229 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: d14c6ce5af7c555ff74df9f36a71a9b55acbc450d368a50a855e155c4c3634c5
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF04229; companion manifest and TSV; native verified inspection
  accessed_at: '2026-10-21T07:20:36Z'
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
  accessed_at: '2026-10-21T07:20:36Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-10-21T07:20:36Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 420 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF04229
  accessed_at: '2026-10-21T07:20:36Z'
  support: supports
  summary: The bounded path inventory found no accession-named PF04229 payload, and
    native inspection found no own overlay or curated projection fields. A separate
    content search found references in the two captured PF01121 files; the path result
    does not establish absence of local context.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF04229. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: local-context-overlay
  kind: record_content
  reference: curation/families/PF01121.yaml
  locator: 'Bounded metadata: pfam_id and causal_graphs[1:3].family_mapping; no complete-overlay
    read'
  accessed_at: '2026-10-21T07:20:36Z'
  support: context_only
  summary: The two target-relevant family_mapping fields distinguish PF01121 and PF04229
    as different regions of a complete protein and retain limits on reference and
    experimental identity. These are prior local mapping assertions. Whole-file hashing
    binds the input but does not imply review of its remaining contents or scientific
    evidence.
  snapshot_sha256: 814f84ac1a5f4f83c3e190f048ee714f1aebc2b20a1073a418651249527c7717
- evidence_id: local-context-note
  kind: record_content
  reference: evidence/PF01121/CoaE-identity.txt
  locator: Bounded identity/provenance lines 1-8, 14-25 and 29-32; prior identity
    limitations retained without scientific or experimental interpretation
  accessed_at: '2026-10-21T07:20:36Z'
  support: context_only
  summary: The retained identity note separately names PF01121 and PF04229 in a complete
    protein and records prior reference-identity and unresolved experimental-identity
    context. Its mapping assertions and earlier source access were not independently
    verified. No sequence, construct, residue-role, assay or mechanistic detail is
    adopted.
  snapshot_sha256: 411d10375ca1afd1834120b67c5ce42c21a066962a37ed5a89ee1ec11cb61e2d
- evidence_id: local-context-search
  kind: search
  reference: curation; evidence; history
  locator: Literal PF04229 content references within the bounded roots
  accessed_at: '2026-10-21T07:20:36Z'
  support: supports
  summary: The bounded content search found the two named PF01121 files. Their presence
    is distinct from the empty accession-named PF04229 path inventory.
  search_scope: Literal exact-accession content search under curation, evidence and
    history, including hidden and ignored files. It establishes bounded local references,
    not literature completeness or scientific support.
- evidence_id: duf-projection-pf04229
  kind: record_content
  reference: data/families/PF04229.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-21T07:20:36Z'
  support: context_only
  snapshot_sha256: d14c6ce5af7c555ff74df9f36a71a9b55acbc450d368a50a855e155c4c3634c5
  quote: "id: Pfam:PF04229\npfam_id: PF04229\nname: GrpB protein\nshort_name: GrpB\n\
    seed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status: SEEDED\n\
    source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF04229\ncounters:\n\
    \  proteins: 7942\n  matches: 7971\n  proteomes: 5605\n  taxa: 8694\n  structures:\
    \ 2\n  alphafold_models: 4945\n  domain_architectures: 98\nprovenance:\n  snapshot_id:\
    \ interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR007344\ndescription: This family has been suggested to\
    \ belong to the nucleotidyltransferase superfamily [[cite:PUB00066751]].\n  It\
    \ occurs at the C-terminus of dephospho-CoA kinase (CoaE) in a number of cases,\
    \ where it plays a role\n  in the proper folding of the enzyme [[cite:PUB00066752]].\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF04229, id=Pfam:PF04229, short_name=GrpB, name=GrpB
    protein, source URL and InterPro accession InterPro:IPR007344 agree with the selected
    frozen row. This establishes frozen identity correspondence, not current upstream
    taxonomy or function.
  target_ids:
  - PF04229
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 7942 proteins, 7971 matches, 2 structure entries and
    4945 AlphaFold models are frozen database counters, not independent experiments.
    Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF04229
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description and prior local identity context versus scientific support
  outcome: unknown
  summary: The GrpB seed description gives a suggested superfamily assignment and
    a qualified domain/protein association, with PUB00066751 and PUB00066752. Those
    sources were not independently resolved. Bounded identity/provenance fields in
    a separate PF01121 overlay and its identity note additionally mention PF04229
    as a distinct region of a complete protein; their scientific accuracy and historical
    mappings were not reverified.
  target_ids:
  - PF04229
  evidence_ids:
  - record
  - snapshot
  - local-context-overlay
  - local-context-note
  dimensions:
  - name: evidence-tier
    value: Imported metadata and bounded prior identity/provenance context; primary
      support not reassessed
    definition: The material actually considered in this local metadata review. Prior
      mapping claims and source-access statements are contextual, not fresh scientific
      verification.
    evidence_ids:
    - record
    - snapshot
    - local-context-overlay
    - local-context-note
- assessment_id: claim-scope
  area: scope
  topic: Family, domain and tested-protein boundaries
  outcome: supported
  summary: The PF04229 family target, the separately owned PF01121 family and the
    full protein are distinct entities. Local reference-identity statements and unresolved
    experimental identity remain different evidential scopes. Their shared protein
    context does not transfer whole-protein or other-domain observations to PF04229.
    The two PF01121 files are context inputs only, not an additional review target
    or adopted scientific evidence. This assessment remains non-operational identity,
    provenance and qualification.
  target_ids:
  - PF04229
  evidence_ids:
  - record
  - snapshot
  - local-context-overlay
  - local-context-note
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: 'PF04229 has no own curated projection payload or overlay, but relevant
    identity context exists in two PF01121 files. Prior mapping statements and their
    explicitly retained identity limitations remain unassessed. The 7942 proteins,
    two structures and 98 architectures are frozen coverage metadata. No residue identity,
    sequence or construct detail, experimental parameter, perturbation, outcome, mechanism
    expansion or functional follow-up is adopted or proposed. The accession-named
    path inventory and literal content search establish different facts: no own PF04229
    payload was found, but two PF01121 files contain relevant identity context.'
  target_ids:
  - PF04229
  evidence_ids:
  - record
  - local-search
  - profile
  - local-context-overlay
  - local-context-note
  - local-context-search
- assessment_id: status
  area: consistency
  topic: Seed, scoring and review states
  outcome: supported
  summary: seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED
    express separate states. EX_DUF records historical renaming and is compatible
    with imported functional descriptions; it is not evidence that all members were
    tested. No REVIEWED gate or curation event is implied by this bundle.
  target_ids:
  - PF04229
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: The PF01121 files remain prior context and are not transferred assertions
    or correction surfaces for PF04229. Any separately authorized PF04229 curation
    belongs in its own maintained overlay with attributable evidence and canonical
    history. This review proposes no record edit, functional follow-up or scientific
    status promotion.
  target_ids:
  - PF04229
  evidence_ids:
  - profile
  - record
  - validation
  - local-context-overlay
  - local-context-note
- assessment_id: local-context-provenance
  area: provenance
  topic: Bounded identity-context provenance and source binding
  outcome: supported
  summary: Both named PF01121 files are captured by whole-file hashes. Bounded metadata
    extracts explicitly distinguish the two family regions on one named protein. This
    supports the existence and traceability of the prior mapping statement, not the
    correctness of the coordinates or scientific claims.
  target_ids:
  - PF04229
  evidence_ids:
  - local-context-overlay
  - local-context-note
  - local-context-search
- assessment_id: local-context-scientific-support
  area: evidence
  topic: Prior mapping and domain-specific scientific support remain unassessed
  outcome: unknown
  summary: The prior documents' mapping statements and underlying observations were
    not independently verified. Shared protein identity does not assign whole-protein
    or other-domain evidence to PF04229. These contextual inputs do not establish
    PF04229 scientific characterization or justify changing UNSCORED/SEEDED or SEED_ONLY.
  target_ids:
  - PF04229
  evidence_ids:
  - local-context-overlay
  - local-context-note
findings: []
actions: []
limitations:
- scientific_review is false. The complete PF04229 seed and frozen row were read,
  but the two PF01121 inputs were considered only through bounded identity/provenance
  extracts. The complete overlay, primary sources, live mappings and experimental
  material were not reassessed. Earlier access statements describe prior curation,
  not work performed here.
- The empty path inventory is limited to accession-named paths under curation/families,
  evidence and history, including hidden/ignored files. A separate content search
  across curation, evidence and history found exactly the two named context files.
  Neither establishes absence of evidence elsewhere.
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
- Whole-file context hashes do not imply complete substantive reads. The two PF01121
  inputs are context_only evidence; this remains one PF04229 target with its native
  digest, seed-only verdict, empty findings/actions and scientific_review=false. No
  domain-specific functional or engineering claim is transferred.
tags:
- seed-review
- unreviewed-record-coverage
```
