# PF02586 SRAP: seed identity, provenance and evidence-scope review

- Review: 20261020T032550Z-pf02586-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-19T23:42:29Z
- Finished UTC: 2026-10-20T03:25:50Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

PF02586 (SRAP; InterPro:IPR003738) matches the verified frozen source and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED. The SRAP description opens with a family-level DNA-associated autoproteolytic-switch mechanism, then uses first-person proposal wording for human Q96FZ2 and says its activity might recruit repair enzymes downstream of TET. It reports oxidized-base DNA binding without an identifiable publication citation and expands TET as an M42-family tetrahedral aminopeptidase. This review observes the unattributed proposal and unresolved terminology without determining whether the biological mechanism or acronym expansion is scientifically correct. One minor follow-up finding records an unattributed mechanistic proposal in the imported description. This review does not decide the underlying scientific claim.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: 6c5277fbd5ab0a7b7f0244f5c248758ac77b3530. The corpus has 8296 records; 171 were covered and 8125 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF02586.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6c5277fbd5ab0a7b7f0244f5c248758ac77b3530.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF02586 | data/families/PF02586.yaml | generated | PF02586 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF02586 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF02586 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF02586 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF02586 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF02586 | 420 valid canonical history records. |
| Generated schema check | passed | True | PF02586 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF02586.

The filename, pfam_id=PF02586, id=Pfam:PF02586, short_name=SRAP, name=SOS response associated peptidase (SRAP), source URL and InterPro accession InterPro:IPR003738 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF02586.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 20212 proteins, 20441 matches, 19 structure entries and 13289 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF02586.

The SRAP description opens with a family-level DNA-associated autoproteolytic-switch mechanism, then uses first-person proposal wording for human Q96FZ2 and says its activity might recruit repair enzymes downstream of TET. It reports oxidized-base DNA binding without an identifiable publication citation and expands TET as an M42-family tetrahedral aminopeptidase. This review observes the unattributed proposal and unresolved terminology without determining whether the biological mechanism or acronym expansion is scientifically correct.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF02586.

DNA binding, autoproteolysis, damage sensing, repair-enzyme recruitment and DNA-demethylation effects are separate claims. The human example and proposed mechanistic extension cannot establish the same mechanism for every bacterial or eukaryotic SRAP member. The protein token, first-person attribution and TET identity must be resolved before those statements become curated protein mappings or mechanistic assertions.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF02586.

The orphaned proposal needs an identifiable source and explicit separation of reported observations from proposed mechanism. Future authorized research should verify Q96FZ2, trace the DNA-binding and autoproteolysis claims, and check the TET terminology against the actual source. This review records a local provenance and scope concern without concluding that any reported experiment is false. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF02586.

seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED express separate states. EX_DUF records historical renaming and is compatible with imported functional descriptions; it is not evidence that all members were tested. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF02586.

The imported-text concern is retained as a minor open finding. A supported clarification belongs in the human-owned curation/families/PF02586.yaml overlay with verified sources and actual canonical history, or an authorized new source freeze through scripts/freeze_duf_puf_worklist.py, followed by generation through src/dufmech/records.py. Existing frozen and generated inputs remain unchanged. The proposed action is future work; this review does not adopt a scientific correction.

### Unattributed mechanistic proposal in imported prose

provenance: concern. Targets: PF02586.

The local description contains an unqualified family-level mechanism and first-person proposals for Q96FZ2, with no identifiable publication attribution. This is a confirmed traceability limitation. Whether the biological interpretation or TET expansion is wrong remains unresolved and is not established by this review.

## Findings

### unattributed-srap-proposal: Imported mechanistic proposal has no identifiable publication attribution

minor / open / confirmed; issue key: pf02586-unattributed-srap-proposal.

The description switches from a family-wide autoproteolytic-switch statement to first-person We propose wording for human Q96FZ2 and a might-recruit-repair-enzymes interpretation, but identifies no publication or proposer for those statements. This prevents the supplied text from distinguishing traced observations from an attributed hypothesis. The finding is the observable attribution gap, not a conclusion that the mechanism, protein binding or TET terminology is scientifically false. The TET/M42-aminopeptidase expansion and family-wide transfer remain questions for a later source review.

## Recommended Actions And Acceptance Checks

### trace-srap-proposal

In separately authorized curation, trace the imported SRAP proposal to identifiable sources and retain a scoped discussion or evidence-backed clarification distinguishing measured observations, proposed mechanism, member identity and unresolved terminology.

- Identify the source of the first-person proposal or explicitly preserve it as an untraced hypothesis; do not invent a paper, author, PMID or supporting quotation.
- If adopting scientific claims, verify the exact Q96FZ2 protein and tested constructs, resolve the TET enzyme identity, and separate DNA binding, autoproteolysis, recruitment and demethylation claims with appropriately licensed evidence.
- Do not treat the visible source text as proof that the TET expansion or family-level mechanism is erroneous; any such correction requires actual source evidence.
- Preserve existing frozen snapshots and generated projections as historical/source-controlled artifacts; use maintained curation inputs or an authorized new source snapshot instead of hand-editing either surface.
- Any future overlay addition must retain real canonical curation history via just new-history and regenerate the affected projection with just records --apply.
- Run just records-check, just history-check and just reviews-check after any authorized change; run just qc before authorized publication.
- Any later resolution must be a new evidence-backed structured observation using the same issue_key and exact previous_occurrences; saving this review alone neither resolves the finding nor promotes the record.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF02586.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF02586 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF02586; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 420 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF02586 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf02586 | data/families/PF02586.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

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
  - path: data/families/PF02586.yaml
    role: target
    sha256: d5af6bf8650bc587f90ee4b8b0508f0bbc758e270597b3ae5ce6c5a760960b09
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
  label: PF02586
  owner_paths:
  - path: curation/families/PF02586.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF02586.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: 6edab20cf94bc67a1727c3c2856673721de667c46854ed450d9d30bd0ef58eac
  target_id: PF02586
schema_version: 1.0.0
review_id: 20261020T032550Z-pf02586-seed-record-review
title: 'PF02586 SRAP: seed identity, provenance and evidence-scope review'
started_at: '2026-10-19T23:42:29Z'
finished_at: '2026-10-20T03:25:50Z'
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
summary: PF02586 (SRAP; InterPro:IPR003738) matches the verified frozen source and
  retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED.
  The SRAP description opens with a family-level DNA-associated autoproteolytic-switch
  mechanism, then uses first-person proposal wording for human Q96FZ2 and says its
  activity might recruit repair enzymes downstream of TET. It reports oxidized-base
  DNA binding without an identifiable publication citation and expands TET as an M42-family
  tetrahedral aminopeptidase. This review observes the unattributed proposal and unresolved
  terminology without determining whether the biological mechanism or acronym expansion
  is scientifically correct. One minor follow-up finding records an unattributed mechanistic
  proposal in the imported description. This review does not decide the underlying
  scientific claim.
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: 6c5277fbd5ab0a7b7f0244f5c248758ac77b3530. The corpus has 8296
    records; 171 were covered and 8125 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF02586.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF02586
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF02586
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF02586
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-004/PF02586-targets.yaml
    --input data/families/PF02586.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF02586
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-004/prepare.py
    PF02586
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF02586
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
  - PF02586
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
  - PF02586
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
  - PF02586
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF02586.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-10-20T03:25:50Z'
  support: supports
  summary: Read the complete PF02586 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: d5af6bf8650bc587f90ee4b8b0508f0bbc758e270597b3ae5ce6c5a760960b09
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF02586; companion manifest and TSV; native verified inspection
  accessed_at: '2026-10-20T03:25:50Z'
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
  accessed_at: '2026-10-20T03:25:50Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-10-20T03:25:50Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 420 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF02586
  accessed_at: '2026-10-20T03:25:50Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF02586. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf02586
  kind: record_content
  reference: data/families/PF02586.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-20T03:25:50Z'
  support: context_only
  snapshot_sha256: d5af6bf8650bc587f90ee4b8b0508f0bbc758e270597b3ae5ce6c5a760960b09
  quote: "id: Pfam:PF02586\npfam_id: PF02586\nname: SOS response associated peptidase\
    \ (SRAP)\nshort_name: SRAP\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF02586\n\
    counters:\n  proteins: 20212\n  matches: 20441\n  proteomes: 14674\n  taxa: 23969\n\
    \  structures: 19\n  alphafold_models: 13289\n  domain_architectures: 96\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR003738\ndescription: The SRAP family functions as a DNA-associated\
    \ autoproteolytic switch that recruits diverse\n  repair enzymes onto DNA damage.\
    \ We propose that the human protein Q96FZ2:UniProtKB, the eukaryotic member\n\
    \  of the SRAP family, which has been recently shown to bind specifically to DNA\
    \ with 5-hydroxymethylcytosine,\n  5-formylcytosine and 5-carboxycytosine, is\
    \ a sensor for these oxidized bases generated by the TET (tetrahedral\n  aminopeptidase\
    \ of the M42 family) enzymes from methylcytosine. Hence, its autoproteolytic activity\
    \ might\n  help it act as a switch that recruits DNA repair enzymes to remove\
    \ these oxidized methylcytosine species\n  as part of the DNA demethylation pathway\
    \ downstream of the TET enzymes.\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF02586, id=Pfam:PF02586, short_name=SRAP, name=SOS
    response associated peptidase (SRAP), source URL and InterPro accession InterPro:IPR003738
    agree with the selected frozen row. This establishes frozen identity correspondence,
    not current upstream taxonomy or function.
  target_ids:
  - PF02586
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 20212 proteins, 20441 matches, 19 structure entries
    and 13289 AlphaFold models are frozen database counters, not independent experiments.
    Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF02586
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: The SRAP description opens with a family-level DNA-associated autoproteolytic-switch
    mechanism, then uses first-person proposal wording for human Q96FZ2 and says its
    activity might recruit repair enzymes downstream of TET. It reports oxidized-base
    DNA binding without an identifiable publication citation and expands TET as an
    M42-family tetrahedral aminopeptidase. This review observes the unattributed proposal
    and unresolved terminology without determining whether the biological mechanism
    or acronym expansion is scientifically correct.
  target_ids:
  - PF02586
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
  summary: DNA binding, autoproteolysis, damage sensing, repair-enzyme recruitment
    and DNA-demethylation effects are separate claims. The human example and proposed
    mechanistic extension cannot establish the same mechanism for every bacterial
    or eukaryotic SRAP member. The protein token, first-person attribution and TET
    identity must be resolved before those statements become curated protein mappings
    or mechanistic assertions.
  target_ids:
  - PF02586
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: The orphaned proposal needs an identifiable source and explicit separation
    of reported observations from proposed mechanism. Future authorized research should
    verify Q96FZ2, trace the DNA-binding and autoproteolysis claims, and check the
    TET terminology against the actual source. This review records a local provenance
    and scope concern without concluding that any reported experiment is false. No
    accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive
    inventory; the inspected projection has no curated claim payload. Optional-field
    absence is not a seed-schema defect.
  target_ids:
  - PF02586
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
  - PF02586
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: The imported-text concern is retained as a minor open finding. A supported
    clarification belongs in the human-owned curation/families/PF02586.yaml overlay
    with verified sources and actual canonical history, or an authorized new source
    freeze through scripts/freeze_duf_puf_worklist.py, followed by generation through
    src/dufmech/records.py. Existing frozen and generated inputs remain unchanged.
    The proposed action is future work; this review does not adopt a scientific correction.
  target_ids:
  - PF02586
  evidence_ids:
  - profile
  - record
  - validation
- assessment_id: imported-description-concern
  area: provenance
  topic: Unattributed mechanistic proposal in imported prose
  outcome: concern
  summary: The local description contains an unqualified family-level mechanism and
    first-person proposals for Q96FZ2, with no identifiable publication attribution.
    This is a confirmed traceability limitation. Whether the biological interpretation
    or TET expansion is wrong remains unresolved and is not established by this review.
  target_ids:
  - PF02586
  evidence_ids:
  - record
  - snapshot
findings:
- finding_id: unattributed-srap-proposal
  issue_key: pf02586-unattributed-srap-proposal
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Imported mechanistic proposal has no identifiable publication attribution
  description: The description switches from a family-wide autoproteolytic-switch
    statement to first-person We propose wording for human Q96FZ2 and a might-recruit-repair-enzymes
    interpretation, but identifies no publication or proposer for those statements.
    This prevents the supplied text from distinguishing traced observations from an
    attributed hypothesis. The finding is the observable attribution gap, not a conclusion
    that the mechanism, protein binding or TET terminology is scientifically false.
    The TET/M42-aminopeptidase expansion and family-wide transfer remain questions
    for a later source review.
  target_ids:
  - PF02586
  field_paths:
  - description
  evidence_ids:
  - record
  - snapshot
  normalization_reason: Minor denotes a bounded imported-text provenance problem in
    a SEEDED projection. Exact identity and faithful source projection are supported;
    this audit does not establish an invalid curated scientific claim or a biological
    mechanism error.
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF02586.yaml
    role: Future human-owned discussion or evidence-backed clarification; this absent
      overlay is not created by review.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: Maintained source-freeze workflow for a future authorized, newly identified
      snapshot if upstream description correction is adopted; no script defect is
      alleged.
actions:
- action_id: trace-srap-proposal
  description: In separately authorized curation, trace the imported SRAP proposal
    to identifiable sources and retain a scoped discussion or evidence-backed clarification
    distinguishing measured observations, proposed mechanism, member identity and
    unresolved terminology.
  finding_ids:
  - unattributed-srap-proposal
  target_ids:
  - PF02586
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF02586.yaml
    role: Future human-owned discussion or evidence-backed clarification; this absent
      overlay is not created by review.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: Maintained source-freeze workflow for a future authorized, newly identified
      snapshot if upstream description correction is adopted; no script defect is
      alleged.
  generator: just records --apply
  acceptance_checks:
  - Identify the source of the first-person proposal or explicitly preserve it as
    an untraced hypothesis; do not invent a paper, author, PMID or supporting quotation.
  - If adopting scientific claims, verify the exact Q96FZ2 protein and tested constructs,
    resolve the TET enzyme identity, and separate DNA binding, autoproteolysis, recruitment
    and demethylation claims with appropriately licensed evidence.
  - Do not treat the visible source text as proof that the TET expansion or family-level
    mechanism is erroneous; any such correction requires actual source evidence.
  - Preserve existing frozen snapshots and generated projections as historical/source-controlled
    artifacts; use maintained curation inputs or an authorized new source snapshot
    instead of hand-editing either surface.
  - Any future overlay addition must retain real canonical curation history via just
    new-history and regenerate the affected projection with just records --apply.
  - Run just records-check, just history-check and just reviews-check after any authorized
    change; run just qc before authorized publication.
  - Any later resolution must be a new evidence-backed structured observation using
    the same issue_key and exact previous_occurrences; saving this review alone neither
    resolves the finding nor promotes the record.
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
