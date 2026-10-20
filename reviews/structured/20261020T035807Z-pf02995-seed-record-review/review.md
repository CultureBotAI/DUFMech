# PF02995 DUF229: seed identity, provenance and evidence-scope review

- Review: 20261020T035807Z-pf02995-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-20T03:53:48Z
- Finished UTC: 2026-10-20T03:58:07Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

PF02995 (DUF229; InterPro:IPR004245) matches the verified frozen source and retains seed_status=UNKNOWN_CANDIDATE, characterization_status=UNSCORED and curation_status=SEEDED. The DUF229 description calls family members uncharacterised, reports lengths of 500-1200 amino acids and suggests that a long conserved region covers several domains. It then attributes nematode larval-development and positive growth-rate annotation to the protein, without naming that protein, a GO accession, an evidence code or a source citation in the complete record or frozen row. One minor local traceability finding remains open: the imported developmental annotation identifies neither the protein nor its GO reference. The finding does not establish that the underlying biological annotation is false.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: 6c5277fbd5ab0a7b7f0244f5c248758ac77b3530. The corpus has 8296 records; 231 were covered and 8065 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF02995.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6c5277fbd5ab0a7b7f0244f5c248758ac77b3530.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF02995 | data/families/PF02995.yaml | generated | PF02995 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF02995 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF02995 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF02995 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF02995 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF02995 | 420 valid canonical history records. |
| Generated schema check | passed | True | PF02995 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF02995.

The filename, pfam_id=PF02995, id=Pfam:PF02995, short_name=DUF229, name=Protein of unknown function (DUF229), source URL and InterPro accession InterPro:IPR004245 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF02995.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 6003 proteins, 6613 matches, 0 structure entries and 5153 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF02995.

The DUF229 description calls family members uncharacterised, reports lengths of 500-1200 amino acids and suggests that a long conserved region covers several domains. It then attributes nematode larval-development and positive growth-rate annotation to the protein, without naming that protein, a GO accession, an evidence code or a source citation in the complete record or frozen row.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF02995.

The proposed multidomain organization is not a verified domain-boundary map, and the reported full-protein lengths should not become a fixed domain length. The developmental/growth annotation is neither a demonstrated molecular mechanism nor a justified family-wide phenotype. Its unnamed protein and unspecified GO terms create a local traceability gap separate from the question of whether the underlying annotation is scientifically valid.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF02995.

A source-backed clarification should identify which protein and annotation were intended and preserve the evidence basis and organism scope before adopting the developmental claims. The minor finding records this bounded traceability gap, without alleging false biology. The 151 architectures, zero structures and 5153 AlphaFold models do not resolve the annotation's identity or mechanistic meaning. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF02995.

seed_status=UNKNOWN_CANDIDATE, characterization_status=UNSCORED and curation_status=SEEDED express separate states. UNKNOWN_CANDIDATE is the retained lexical seed class, not an experimentally established absence of function. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF02995.

A source-backed clarification or explicit unresolved-context discussion belongs in the maintained PF02995 overlay or a separately authorized upstream source-refresh workflow. The frozen row and generated projection are unchanged; future curation requires actual canonical history and native validation. The proposed action has not been performed.

### Traceability of a protein-specific developmental annotation

representation: concern. Targets: PF02995.

The description attributes developmental/growth annotation to the protein without identifying a member, GO term, evidence code or citation. The selected complete record and unique frozen row do not make the intended annotation traceable; this does not establish that its underlying biology is false.

## Findings

### unidentified-go-annotation: Imported developmental annotation lacks an identifiable protein or GO reference

minor / open / confirmed; issue key: pf02995-unidentified-go-annotation.

The description moves from uncharacterised family members to a GO annotation for the protein concerning nematode larval development and growth. Neither the complete projection nor its unique frozen row identifies which protein or GO term is intended, and no citation is supplied for that sentence. This is a bounded traceability/context gap in faithfully imported prose, not a demonstrated false phenotype, erroneous family identity or missing mandatory schema field.

## Recommended Actions And Acceptance Checks

### clarify-duf229-annotation-context

During separately authorized curation, identify the protein and annotation intended by the source sentence and retain a self-contained clarification, or explicitly preserve the unresolved identity if the source cannot be recovered.

- Identify the exact protein/taxon and GO term or source reference if recoverable; do not invent accession identifiers or evidence codes.
- Distinguish organism-level developmental annotation from an experimental molecular-function claim and retain its evidence basis and scope.
- If the antecedent cannot be recovered, explicitly retain the unresolved annotation identity in maintained discussion rather than silently treating it as family-wide evidence.
- Preserve immutable frozen snapshots and generated projections; any actual clarification belongs in authorized maintained inputs or an authorized successor source freeze.
- Any future curation must retain real canonical history and pass the native record, history and review checks; a subsequent finding disposition must cite this observation explicitly.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF02995.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF02995 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF02995; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 420 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF02995 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf02995 | data/families/PF02995.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

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
  git_revision: 6c5277fbd5ab0a7b7f0244f5c248758ac77b3530
  inputs:
  - path: data/families/PF02995.yaml
    role: target
    sha256: aea022743cf55df9020899517d3ceac233ac132ce48c5b09f7a62e1a300542f7
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
  label: PF02995
  owner_paths:
  - path: curation/families/PF02995.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF02995.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: 77a4e5c24a4c4319f19074f9790c4272eee237492ddb14bccdcb446274ba6cb1
  target_id: PF02995
schema_version: 1.0.0
review_id: 20261020T035807Z-pf02995-seed-record-review
title: 'PF02995 DUF229: seed identity, provenance and evidence-scope review'
started_at: '2026-10-20T03:53:48Z'
finished_at: '2026-10-20T03:58:07Z'
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
summary: 'PF02995 (DUF229; InterPro:IPR004245) matches the verified frozen source
  and retains seed_status=UNKNOWN_CANDIDATE, characterization_status=UNSCORED and
  curation_status=SEEDED. The DUF229 description calls family members uncharacterised,
  reports lengths of 500-1200 amino acids and suggests that a long conserved region
  covers several domains. It then attributes nematode larval-development and positive
  growth-rate annotation to the protein, without naming that protein, a GO accession,
  an evidence code or a source citation in the complete record or frozen row. One
  minor local traceability finding remains open: the imported developmental annotation
  identifies neither the protein nor its GO reference. The finding does not establish
  that the underlying biological annotation is false.'
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: 6c5277fbd5ab0a7b7f0244f5c248758ac77b3530. The corpus has 8296
    records; 231 were covered and 8065 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF02995.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF02995
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF02995
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF02995
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-010/PF02995-targets.yaml
    --input data/families/PF02995.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF02995
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-010/prepare.py
    PF02995
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF02995
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
  - PF02995
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
  - PF02995
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
  - PF02995
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF02995.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Read the complete PF02995 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: aea022743cf55df9020899517d3ceac233ac132ce48c5b09f7a62e1a300542f7
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF02995; companion manifest and TSV; native verified inspection
  accessed_at: '2026-10-20T03:58:07Z'
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
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 420 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF02995
  accessed_at: '2026-10-20T03:58:07Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF02995. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf02995
  kind: record_content
  reference: data/families/PF02995.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-20T03:58:07Z'
  support: context_only
  snapshot_sha256: aea022743cf55df9020899517d3ceac233ac132ce48c5b09f7a62e1a300542f7
  quote: "id: Pfam:PF02995\npfam_id: PF02995\nname: Protein of unknown function (DUF229)\n\
    short_name: DUF229\nseed_status: UNKNOWN_CANDIDATE\ncharacterization_status: UNSCORED\n\
    curation_status: SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF02995\n\
    counters:\n  proteins: 6003\n  matches: 6613\n  proteomes: 653\n  taxa: 2252\n\
    \  structures: 0\n  alphafold_models: 5153\n  domain_architectures: 151\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR004245\ndescription: Members of this family are uncharacterised.\
    \ They are 500-1200 amino acids in length and share\n  a long region conservation\
    \ that probably corresponds to several domains. The Go annotation for the protein\n\
    \  indicates that it is involved in nematode larval development and has a positive\
    \ regulation on growth\n  rate.\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF02995, id=Pfam:PF02995, short_name=DUF229, name=Protein
    of unknown function (DUF229), source URL and InterPro accession InterPro:IPR004245
    agree with the selected frozen row. This establishes frozen identity correspondence,
    not current upstream taxonomy or function.
  target_ids:
  - PF02995
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 6003 proteins, 6613 matches, 0 structure entries and
    5153 AlphaFold models are frozen database counters, not independent experiments.
    Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF02995
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: The DUF229 description calls family members uncharacterised, reports lengths
    of 500-1200 amino acids and suggests that a long conserved region covers several
    domains. It then attributes nematode larval-development and positive growth-rate
    annotation to the protein, without naming that protein, a GO accession, an evidence
    code or a source citation in the complete record or frozen row.
  target_ids:
  - PF02995
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
  summary: The proposed multidomain organization is not a verified domain-boundary
    map, and the reported full-protein lengths should not become a fixed domain length.
    The developmental/growth annotation is neither a demonstrated molecular mechanism
    nor a justified family-wide phenotype. Its unnamed protein and unspecified GO
    terms create a local traceability gap separate from the question of whether the
    underlying annotation is scientifically valid.
  target_ids:
  - PF02995
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: A source-backed clarification should identify which protein and annotation
    were intended and preserve the evidence basis and organism scope before adopting
    the developmental claims. The minor finding records this bounded traceability
    gap, without alleging false biology. The 151 architectures, zero structures and
    5153 AlphaFold models do not resolve the annotation's identity or mechanistic
    meaning. No accession-named overlay, evidence or history path was found by the
    bounded hidden/ignored-inclusive inventory; the inspected projection has no curated
    claim payload. Optional-field absence is not a seed-schema defect.
  target_ids:
  - PF02995
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
  - PF02995
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: A source-backed clarification or explicit unresolved-context discussion
    belongs in the maintained PF02995 overlay or a separately authorized upstream
    source-refresh workflow. The frozen row and generated projection are unchanged;
    future curation requires actual canonical history and native validation. The proposed
    action has not been performed.
  target_ids:
  - PF02995
  evidence_ids:
  - profile
  - record
  - validation
- assessment_id: unidentified-go-context
  area: representation
  topic: Traceability of a protein-specific developmental annotation
  outcome: concern
  summary: The description attributes developmental/growth annotation to the protein
    without identifying a member, GO term, evidence code or citation. The selected
    complete record and unique frozen row do not make the intended annotation traceable;
    this does not establish that its underlying biology is false.
  target_ids:
  - PF02995
  evidence_ids:
  - record
  - snapshot
findings:
- finding_id: unidentified-go-annotation
  issue_key: pf02995-unidentified-go-annotation
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Imported developmental annotation lacks an identifiable protein or GO reference
  description: The description moves from uncharacterised family members to a GO annotation
    for the protein concerning nematode larval development and growth. Neither the
    complete projection nor its unique frozen row identifies which protein or GO term
    is intended, and no citation is supplied for that sentence. This is a bounded
    traceability/context gap in faithfully imported prose, not a demonstrated false
    phenotype, erroneous family identity or missing mandatory schema field.
  target_ids:
  - PF02995
  field_paths:
  - description
  evidence_ids:
  - record
  - snapshot
  normalization_reason: Minor is proposed for a bounded source-context/traceability
    defect. Exact identity and source correspondence are intact; no curated functional
    assertion or false scientific claim is established.
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF02995.yaml
    role: Future maintained discussion or source-backed clarification; review does
      not create this overlay.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: Maintained workflow for any separately authorized new upstream snapshot;
      no generator defect is alleged.
actions:
- action_id: clarify-duf229-annotation-context
  description: During separately authorized curation, identify the protein and annotation
    intended by the source sentence and retain a self-contained clarification, or
    explicitly preserve the unresolved identity if the source cannot be recovered.
  finding_ids:
  - unidentified-go-annotation
  target_ids:
  - PF02995
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF02995.yaml
    role: Future maintained discussion or source-backed clarification; review does
      not create this overlay.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: Maintained workflow for any separately authorized new upstream snapshot;
      no generator defect is alleged.
  generator: just records --apply
  acceptance_checks:
  - Identify the exact protein/taxon and GO term or source reference if recoverable;
    do not invent accession identifiers or evidence codes.
  - Distinguish organism-level developmental annotation from an experimental molecular-function
    claim and retain its evidence basis and scope.
  - If the antecedent cannot be recovered, explicitly retain the unresolved annotation
    identity in maintained discussion rather than silently treating it as family-wide
    evidence.
  - Preserve immutable frozen snapshots and generated projections; any actual clarification
    belongs in authorized maintained inputs or an authorized successor source freeze.
  - Any future curation must retain real canonical history and pass the native record,
    history and review checks; a subsequent finding disposition must cite this observation
    explicitly.
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
