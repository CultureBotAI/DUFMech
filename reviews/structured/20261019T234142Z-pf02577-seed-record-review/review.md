# PF02577 BFN_dom: seed identity, provenance and evidence-scope review

- Review: 20261019T234142Z-pf02577-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-19T23:39:04Z
- Finished UTC: 2026-10-19T23:41:42Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

PF02577 (BFN_dom; InterPro:IPR003729) matches the verified frozen source and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED. The BFN description opens by assigning RNase and DNase activity to the domain, but later reports those activities for Oryza minuta OmBBD in vitro and explicitly proposes that they might instead involve its additional C-terminal UvrB domain and UvrC. It also places the domain in M. tuberculosis Cor proteins that lack that added region. PUB00057454 and PUB00109344 were not resolved to the underlying experiments; the imported text contains an unresolved activity-attribution tension. One minor follow-up finding records an ambiguity in the imported description. This review does not determine the correct biochemical mechanism or adopt a new function.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: 6c5277fbd5ab0a7b7f0244f5c248758ac77b3530. The corpus has 8296 records; 161 were covered and 8135 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF02577.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6c5277fbd5ab0a7b7f0244f5c248758ac77b3530.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF02577 | data/families/PF02577.yaml | generated | PF02577 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF02577 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF02577 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF02577 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF02577 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF02577 | 420 valid canonical history records. |
| Generated schema check | passed | True | PF02577 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF02577.

The filename, pfam_id=PF02577, id=Pfam:PF02577, short_name=BFN_dom, name=Bifunctional nuclease domain, source URL and InterPro accession InterPro:IPR003729 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF02577.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 9018 proteins, 9019 matches, 2 structure entries and 6182 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF02577.

The BFN description opens by assigning RNase and DNase activity to the domain, but later reports those activities for Oryza minuta OmBBD in vitro and explicitly proposes that they might instead involve its additional C-terminal UvrB domain and UvrC. It also places the domain in M. tuberculosis Cor proteins that lack that added region. PUB00057454 and PUB00109344 were not resolved to the underlying experiments; the imported text contains an unresolved activity-attribution tension.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF02577.

Reported activity of a protein with multiple domains does not establish nuclease activity of isolated PF02577, and the alternative UvrB/UvrC explanation is a proposal rather than a verified resolution in this review. The plant OmBBD context, Cor proteins composed of this domain, and the described dimeric structure must remain distinct. Neither nuclease activity nor the Cor-associated resistance context should be transferred across all family members from this description.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF02577.

Scientific follow-up should inspect the competing source interpretations, exact OmBBD and Cor sequences, purified constructs, substrates, assay controls and any partner dependence before attributing catalysis. Preserve the source contradiction explicitly until that work resolves which protein region or complex supports each result; an EX_DUF name and two frozen structures do not settle the mechanism. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF02577.

seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED express separate states. EX_DUF records historical renaming and is compatible with imported functional descriptions; it is not evidence that all members were tested. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF02577.

The imported-text ambiguity is retained as a minor open finding. Any scientific clarification belongs in the human-owned curation/families/PF02577.yaml overlay with verified source support and actual canonical history, or an authorized new upstream source freeze through scripts/freeze_duf_puf_worklist.py, followed by generation through src/dufmech/records.py. The frozen snapshot and generated projection remain unchanged. The proposed action is future work and does not claim that either scientific interpretation is correct.

### Unreconciled isolated-domain versus full-protein nuclease attribution

scope: concern. Targets: PF02577.

The opening description attributes RNase and DNase activities to the BFN domain, but its later account reports OmBBD activity in a protein with an additional UvrB domain and raises an alternative UvrB/UvrC explanation. The text does not reconcile the unqualified domain claim with that alternative. This is a source-scope ambiguity; the review does not establish which mechanism is correct.

## Findings

### domain-nuclease-attribution: Domain nuclease claim is not reconciled with an alternative OmBBD attribution

minor / open / confirmed; issue key: pf02577-domain-nuclease-attribution.

The imported description initially states that the BFN domain has both RNase and DNase activities. Later sentences describe in vitro activity for Oryza minuta OmBBD, distinguish its extra C-terminal UvrB domain from the mycobacterial sequences, and report a proposal that the activity may instead arise through UvrB/UvrC interaction. The supplied text leaves the domain-level attribution unresolved. This finding confirms the conflicting scope and qualification within the description; it does not prove that PF02577 lacks nuclease activity, that Cor has or lacks that activity, or that the alternative mechanism is experimentally correct.

## Recommended Actions And Acceptance Checks

### resolve-bfn-activity-scope

In separately authorized curation, reconcile the competing activity attributions through the underlying sources and retain an explicit domain-versus-protein scope explanation in maintained curation content.

- Resolve PUB00057454 and PUB00109344 to the actual sources, identify the tested OmBBD and Cor proteins and construct boundaries, and distinguish whole-protein results from isolated-PF02577 experiments.
- If adopting an activity assertion, retain supporting substrates, controls, catalytic sufficiency and partner requirements from the inspected experiments; do not treat the proposed UvrB/UvrC explanation as established merely because it appears in the description.
- Explain the status of the opening domain-level claim and the alternative attribution together. If evidence remains unavailable or inconclusive, preserve that uncertainty explicitly rather than selecting either interpretation as fact.
- Preserve existing frozen snapshots and generated projections as historical/source-controlled artifacts; use maintained curation inputs or an authorized new source snapshot instead of hand-editing either surface.
- Any future overlay addition must retain real canonical curation history via just new-history and regenerate the affected projection with just records --apply.
- Run just records-check, just history-check and just reviews-check after any authorized change; run just qc before authorized publication.
- Any later resolution must be a new evidence-backed structured observation using the same issue_key and exact previous_occurrences; saving this review alone neither resolves the finding nor promotes the record.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF02577.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF02577 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF02577; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 420 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF02577 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf02577 | data/families/PF02577.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

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
  - path: data/families/PF02577.yaml
    role: target
    sha256: f3a88a8791012f541e34ea77f165037855354a2af3a8ffd149909c100c2e39fe
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
  label: PF02577
  owner_paths:
  - path: curation/families/PF02577.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF02577.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: f1249527e7e50a35b2127b9485960a48a755167b89d67148b7369e088433edb2
  target_id: PF02577
schema_version: 1.0.0
review_id: 20261019T234142Z-pf02577-seed-record-review
title: 'PF02577 BFN_dom: seed identity, provenance and evidence-scope review'
started_at: '2026-10-19T23:39:04Z'
finished_at: '2026-10-19T23:41:42Z'
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
summary: PF02577 (BFN_dom; InterPro:IPR003729) matches the verified frozen source
  and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED.
  The BFN description opens by assigning RNase and DNase activity to the domain, but
  later reports those activities for Oryza minuta OmBBD in vitro and explicitly proposes
  that they might instead involve its additional C-terminal UvrB domain and UvrC.
  It also places the domain in M. tuberculosis Cor proteins that lack that added region.
  PUB00057454 and PUB00109344 were not resolved to the underlying experiments; the
  imported text contains an unresolved activity-attribution tension. One minor follow-up
  finding records an ambiguity in the imported description. This review does not determine
  the correct biochemical mechanism or adopt a new function.
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: 6c5277fbd5ab0a7b7f0244f5c248758ac77b3530. The corpus has 8296
    records; 161 were covered and 8135 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF02577.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF02577
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF02577
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF02577
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-003/PF02577-targets.yaml
    --input data/families/PF02577.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF02577
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-003/prepare.py
    PF02577
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF02577
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
  - PF02577
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
  - PF02577
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
  - PF02577
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF02577.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-10-19T23:41:42Z'
  support: supports
  summary: Read the complete PF02577 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: f3a88a8791012f541e34ea77f165037855354a2af3a8ffd149909c100c2e39fe
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF02577; companion manifest and TSV; native verified inspection
  accessed_at: '2026-10-19T23:41:42Z'
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
  accessed_at: '2026-10-19T23:41:42Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-10-19T23:41:42Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 420 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF02577
  accessed_at: '2026-10-19T23:41:42Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF02577. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf02577
  kind: record_content
  reference: data/families/PF02577.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-19T23:41:42Z'
  support: context_only
  snapshot_sha256: f3a88a8791012f541e34ea77f165037855354a2af3a8ffd149909c100c2e39fe
  quote: "id: Pfam:PF02577\npfam_id: PF02577\nname: Bifunctional nuclease domain\n\
    short_name: BFN_dom\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF02577\n\
    counters:\n  proteins: 9018\n  matches: 9019\n  proteomes: 7423\n  taxa: 11314\n\
    \  structures: 2\n  alphafold_models: 6182\n  domain_architectures: 42\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR003729\ndescription: This entry represents the bifunctional\
    \ nuclease (BFN) domain which is specific to bacteria\n  and plant organisms.\
    \ It has both RNase and DNase activities [[cite:PUB00057454]]. The dimer of the\
    \ BFN\n  domain forms a wedge, each monomer being a basic triangular shape. The\
    \ BFN domain is composed of an\n  eight-stranded, distorted beta-sheet consisting\
    \ of a four-stranded antiparallel beta-sheet, and a four-stranded\n  mixed beta-sheet.\
    \ This domain can be found in M. tuberculosis Carbon monoxide resistance (Cor)\
    \ proteins.\n  Cor consists entirely of this domain with homologues in a variety\
    \ of organisms, including most mycobacteria,\n  Bacteroides sp., Chlamydia sp.,\
    \ Streptomyces sp., and Rhodococcussp. One of the homologs from Oryza\n  minuta\
    \ protein OmBBD was reported to exhibit DNase and RNAse activity in vitro [[cite:PUB00057454]].\n\
    \  OmBBD carries a C-terminal UvrB domain that is absent in the mycobacterial\
    \ sequences. UvrB is one component\n  of the UvrABC endonuclease system. Hence,\
    \ it was proposed that OmBBD's observed nuclease activity may\n  come not from\
    \ this domain but from an interaction of the C-terminal UvrB with the catalytic\
    \ UvrC nuclease\n  [[cite:PUB00109344]].\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF02577, id=Pfam:PF02577, short_name=BFN_dom, name=Bifunctional
    nuclease domain, source URL and InterPro accession InterPro:IPR003729 agree with
    the selected frozen row. This establishes frozen identity correspondence, not
    current upstream taxonomy or function.
  target_ids:
  - PF02577
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 9018 proteins, 9019 matches, 2 structure entries and
    6182 AlphaFold models are frozen database counters, not independent experiments.
    Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF02577
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: The BFN description opens by assigning RNase and DNase activity to the
    domain, but later reports those activities for Oryza minuta OmBBD in vitro and
    explicitly proposes that they might instead involve its additional C-terminal
    UvrB domain and UvrC. It also places the domain in M. tuberculosis Cor proteins
    that lack that added region. PUB00057454 and PUB00109344 were not resolved to
    the underlying experiments; the imported text contains an unresolved activity-attribution
    tension.
  target_ids:
  - PF02577
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
  summary: Reported activity of a protein with multiple domains does not establish
    nuclease activity of isolated PF02577, and the alternative UvrB/UvrC explanation
    is a proposal rather than a verified resolution in this review. The plant OmBBD
    context, Cor proteins composed of this domain, and the described dimeric structure
    must remain distinct. Neither nuclease activity nor the Cor-associated resistance
    context should be transferred across all family members from this description.
  target_ids:
  - PF02577
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: Scientific follow-up should inspect the competing source interpretations,
    exact OmBBD and Cor sequences, purified constructs, substrates, assay controls
    and any partner dependence before attributing catalysis. Preserve the source contradiction
    explicitly until that work resolves which protein region or complex supports each
    result; an EX_DUF name and two frozen structures do not settle the mechanism.
    No accession-named overlay, evidence or history path was found by the bounded
    hidden/ignored-inclusive inventory; the inspected projection has no curated claim
    payload. Optional-field absence is not a seed-schema defect.
  target_ids:
  - PF02577
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
  - PF02577
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: The imported-text ambiguity is retained as a minor open finding. Any scientific
    clarification belongs in the human-owned curation/families/PF02577.yaml overlay
    with verified source support and actual canonical history, or an authorized new
    upstream source freeze through scripts/freeze_duf_puf_worklist.py, followed by
    generation through src/dufmech/records.py. The frozen snapshot and generated projection
    remain unchanged. The proposed action is future work and does not claim that either
    scientific interpretation is correct.
  target_ids:
  - PF02577
  evidence_ids:
  - profile
  - record
  - validation
- assessment_id: domain-activity-attribution-concern
  area: scope
  topic: Unreconciled isolated-domain versus full-protein nuclease attribution
  outcome: concern
  summary: The opening description attributes RNase and DNase activities to the BFN
    domain, but its later account reports OmBBD activity in a protein with an additional
    UvrB domain and raises an alternative UvrB/UvrC explanation. The text does not
    reconcile the unqualified domain claim with that alternative. This is a source-scope
    ambiguity; the review does not establish which mechanism is correct.
  target_ids:
  - PF02577
  evidence_ids:
  - record
  - snapshot
findings:
- finding_id: domain-nuclease-attribution
  issue_key: pf02577-domain-nuclease-attribution
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Domain nuclease claim is not reconciled with an alternative OmBBD attribution
  description: The imported description initially states that the BFN domain has both
    RNase and DNase activities. Later sentences describe in vitro activity for Oryza
    minuta OmBBD, distinguish its extra C-terminal UvrB domain from the mycobacterial
    sequences, and report a proposal that the activity may instead arise through UvrB/UvrC
    interaction. The supplied text leaves the domain-level attribution unresolved.
    This finding confirms the conflicting scope and qualification within the description;
    it does not prove that PF02577 lacks nuclease activity, that Cor has or lacks
    that activity, or that the alternative mechanism is experimentally correct.
  target_ids:
  - PF02577
  field_paths:
  - description
  evidence_ids:
  - record
  - snapshot
  normalization_reason: Minor is used for a bounded unresolved attribution in imported
    seed prose, with correct Pfam identity and faithful frozen-source projection.
    No curated nuclease assertion or experimentally demonstrated mechanism error is
    established by this audit.
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF02577.yaml
    role: Future human-owned discussion or evidence-backed clarification; review does
      not create this absent overlay.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: Maintained workflow for an authorized new source snapshot if corrected upstream
      metadata is adopted; no implementation defect is alleged.
actions:
- action_id: resolve-bfn-activity-scope
  description: In separately authorized curation, reconcile the competing activity
    attributions through the underlying sources and retain an explicit domain-versus-protein
    scope explanation in maintained curation content.
  finding_ids:
  - domain-nuclease-attribution
  target_ids:
  - PF02577
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF02577.yaml
    role: Future human-owned discussion or evidence-backed clarification; review does
      not create this absent overlay.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: Maintained workflow for an authorized new source snapshot if corrected upstream
      metadata is adopted; no implementation defect is alleged.
  generator: just records --apply
  acceptance_checks:
  - Resolve PUB00057454 and PUB00109344 to the actual sources, identify the tested
    OmBBD and Cor proteins and construct boundaries, and distinguish whole-protein
    results from isolated-PF02577 experiments.
  - If adopting an activity assertion, retain supporting substrates, controls, catalytic
    sufficiency and partner requirements from the inspected experiments; do not treat
    the proposed UvrB/UvrC explanation as established merely because it appears in
    the description.
  - Explain the status of the opening domain-level claim and the alternative attribution
    together. If evidence remains unavailable or inconclusive, preserve that uncertainty
    explicitly rather than selecting either interpretation as fact.
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
