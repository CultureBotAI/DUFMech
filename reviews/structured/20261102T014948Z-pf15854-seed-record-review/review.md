# PF15854 GPR15L: seed identity, provenance and evidence-scope review

- Review: 20261102T014948Z-pf15854-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-11-02T01:43:52Z
- Finished UTC: 2026-11-02T01:49:48Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: seed_only
- Scientific review: false

## Summary

PF15854 (GPR15L; InterPro:IPR031713) matches the verified frozen source and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED. EX_DUF GPR15L (IPR031713) preserves ligand activation/attraction and epithelial-expression descriptions, human C10ORF99, AP-57/CSBF aliases, distinct 9 kDa and 57-residue descriptions, CC-motif features and a C-terminal activating peptide. The GPR15 receptor co-receptor role is distinct from ligand function; two disulfide bonds are predicted and classic CC/CXC homology is not asserted. PUB00088053/PUB00088054 and the reported assays were not independently read. All seven counters agree between row and projection: 121 proteins, 122 matches, 114 proteomes, 422 taxa, 1 structures, 106 models, 4 architectures.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: aa7d08bcf3a9a03879d06cffd075bc083d29788f. The corpus has 8296 records; 4261 were covered and 4035 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF15854.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base aa7d08bcf3a9a03879d06cffd075bc083d29788f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF15854 | data/families/PF15854.yaml | generated | PF15854 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF15854 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF15854 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF15854 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF15854 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF15854 | 489 valid canonical history records. |
| Generated schema check | passed | True | PF15854 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF15854.

The filename, pfam_id=PF15854, id=Pfam:PF15854, short_name=GPR15L, name=G-protein coupled receptor ligand 15, source URL and InterPro accession InterPro:IPR031713 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF15854.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 121 proteins, 122 matches, 1 structure entries and 106 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF15854.

EX_DUF GPR15L (IPR031713) preserves ligand activation/attraction and epithelial-expression descriptions, human C10ORF99, AP-57/CSBF aliases, distinct 9 kDa and 57-residue descriptions, CC-motif features and a C-terminal activating peptide. The GPR15 receptor co-receptor role is distinct from ligand function; two disulfide bonds are predicted and classic CC/CXC homology is not asserted. PUB00088053/PUB00088054 and the reported assays were not independently read. All seven counters agree between row and projection: 121 proteins, 122 matches, 114 proteomes, 422 taxa, 1 structures, 106 models, 4 architectures.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF15854.

Metadata-only source and captured-context review. EX_DUF GPR15L preserves imported receptor-binding/activation and attraction of GPR15-expressing T cells, epithelial expression, human C10ORF99 naming, AP-57/CSBF aliases and reported antimicrobial/cancer-cell-growth effects. The opening SIV/HIV-2 co-receptor and trafficking statements concern GPR15 receptor, not an independently established viral co-receptor function of the ligand. The 9 kDa polypeptide and 57-amino-acid AP-57 descriptions are distinct source descriptions, not an inferred precursor cleavage map, invariant whole-protein length or domain boundaries. CC motif and chemokine-like features do not establish classic CC/CXC sequence homology; two disulfide bonds are explicitly predicted, and the activating terminal peptide is described as C-terminal. PUB00088053/PUB00088054, receptor binding, SUSD2 interaction, cellular assays, peptide processing and one structure entry were not inspected. No antiviral, cancer-treatment or universal homologue activity is certified. One excess match and four architectures do not define individual organization; 106 models remain uninspected.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF15854.

The captured literal accession (PF15854) and current-short-name (GPR15L) searches found no path or content hits under curation/families, evidence and history, including hidden and ignored files; the exact canonical overlay, evidence and history owners were absent. These bounded results do not establish absence for GPR15, C10ORF99, AP-57, CSBF, SUSD2, CC/CXC terms and PUB00088053/PUB00088054 or wider literature. No primary paper, live upstream record, structural model or assay was inspected. A biological or historical assessment needs separately verified evidence and tested-protein scope. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF15854.

seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED express separate states. EX_DUF records historical renaming and is compatible with imported functional descriptions; it is not evidence that all members were tested. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF15854.

Scientific additions would belong in the human-owned curation/families/PF15854.yaml overlay with appropriately licensed evidence and actual canonical history, followed by generation through src/dufmech/records.py. Frozen snapshots and generated records are not direct correction surfaces. No corrective edit is proposed by this seed audit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF15854.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF15854 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF15854; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 489 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF15854 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf15854 | data/families/PF15854.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

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
  - path: data/families/PF15854.yaml
    role: target
    sha256: 35d064f60cce4fd4299340c9144e77fb85769aee1d79bc84bafd710884af241b
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
  label: PF15854
  owner_paths:
  - path: curation/families/PF15854.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF15854.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: 137200cf5b92fcb7d9be05e3322c82e48f9810bfbe573aefc2b9cb27d3a9e3c7
  target_id: PF15854
schema_version: 1.0.0
review_id: 20261102T014948Z-pf15854-seed-record-review
title: 'PF15854 GPR15L: seed identity, provenance and evidence-scope review'
started_at: '2026-11-02T01:43:52Z'
finished_at: '2026-11-02T01:49:48Z'
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
summary: 'PF15854 (GPR15L; InterPro:IPR031713) matches the verified frozen source
  and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED.
  EX_DUF GPR15L (IPR031713) preserves ligand activation/attraction and epithelial-expression
  descriptions, human C10ORF99, AP-57/CSBF aliases, distinct 9 kDa and 57-residue
  descriptions, CC-motif features and a C-terminal activating peptide. The GPR15 receptor
  co-receptor role is distinct from ligand function; two disulfide bonds are predicted
  and classic CC/CXC homology is not asserted. PUB00088053/PUB00088054 and the reported
  assays were not independently read. All seven counters agree between row and projection:
  121 proteins, 122 matches, 114 proteomes, 422 taxa, 1 structures, 106 models, 4
  architectures.'
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: aa7d08bcf3a9a03879d06cffd075bc083d29788f. The corpus has 8296
    records; 4261 were covered and 4035 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF15854.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF15854
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF15854
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF15854
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-413-attempt-001/PF15854-targets.yaml
    --input data/families/PF15854.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF15854
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-413-attempt-001/prepare.py
    PF15854
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF15854
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
  - PF15854
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
  - PF15854
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
  - PF15854
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF15854.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-11-02T01:49:48Z'
  support: supports
  summary: Read the complete PF15854 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: 35d064f60cce4fd4299340c9144e77fb85769aee1d79bc84bafd710884af241b
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF15854; companion manifest and TSV; native verified inspection
  accessed_at: '2026-11-02T01:49:48Z'
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
  accessed_at: '2026-11-02T01:49:48Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-11-02T01:49:48Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 489 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF15854
  accessed_at: '2026-11-02T01:49:48Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF15854. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf15854
  kind: record_content
  reference: data/families/PF15854.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-11-02T01:49:48Z'
  support: context_only
  snapshot_sha256: 35d064f60cce4fd4299340c9144e77fb85769aee1d79bc84bafd710884af241b
  quote: "id: Pfam:PF15854\npfam_id: PF15854\nname: G-protein coupled receptor ligand\
    \ 15\nshort_name: GPR15L\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF15854\n\
    counters:\n  proteins: 121\n  matches: 122\n  proteomes: 114\n  taxa: 422\n  structures:\
    \ 1\n  alphafold_models: 106\n  domain_architectures: 4\nprovenance:\n  snapshot_id:\
    \ interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR031713\ndescription: GPR15 is an orphan G protein-coupled\
    \ receptor (GPCR) that is found in lymphocytes. It functions\n  as a co-receptor\
    \ of simian immunodeficiency virus and HIV-2 and plays a role in the trafficking\
    \ of T\n  cells to the lamina propria in the colon and to the skin [[cite:PUB00088053]].\
    \ An activating ligand\n  named GPR15L is shown to bind GPR15 and attract GPR15-expressing\
    \ T cells including lymphocytes in colon-draining\n  lymph nodes and thymic precursors\
    \ of dermal epithelial T cell. This 9kDa CC-motif containing cationic\n  polypeptide\
    \ has been previously described as the 57 amino acid antimicrobial peptide AP-57,\
    \ and as a\n  Sushi Containing Domain-2 (SUSD2)-binding factor (CSBF), capable\
    \ of inhibiting the growth of intestinal\n  epithelial cancer cell lines. The\
    \ chemokine is expressed by epithelial cells in gastrointestinal and\n  genitourinary\
    \ mucosae and in the skin [[cite:PUB00088054]]. In humans GPR15L, is encoded by\
    \ the gene\n  C10ORF99 and has some features similar to the CC family of chemokines\
    \ [[cite:PUB00088053]]. However,\n  it lacks significant homology to classic CC\
    \ and CXC chemokines, yet shares many features with them,\n  including a cationic\
    \ domain predicted to comprise two disulfide bonds and a highly conserved GPCR-activating\n\
    \  terminal peptide. Furthermore, the activating peptides of CC chemokines are\
    \ typically located at the\n  N-terminus, while that of GPR15L is C-terminal,\
    \ a feature that it shares with some other GPCR ligands\n  like chemerin and apela\
    \ [[cite:PUB00088054]].\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF15854, id=Pfam:PF15854, short_name=GPR15L, name=G-protein
    coupled receptor ligand 15, source URL and InterPro accession InterPro:IPR031713
    agree with the selected frozen row. This establishes frozen identity correspondence,
    not current upstream taxonomy or function.
  target_ids:
  - PF15854
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 121 proteins, 122 matches, 1 structure entries and 106
    AlphaFold models are frozen database counters, not independent experiments. Raw
    input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF15854
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: 'EX_DUF GPR15L (IPR031713) preserves ligand activation/attraction and epithelial-expression
    descriptions, human C10ORF99, AP-57/CSBF aliases, distinct 9 kDa and 57-residue
    descriptions, CC-motif features and a C-terminal activating peptide. The GPR15
    receptor co-receptor role is distinct from ligand function; two disulfide bonds
    are predicted and classic CC/CXC homology is not asserted. PUB00088053/PUB00088054
    and the reported assays were not independently read. All seven counters agree
    between row and projection: 121 proteins, 122 matches, 114 proteomes, 422 taxa,
    1 structures, 106 models, 4 architectures.'
  target_ids:
  - PF15854
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
  summary: Metadata-only source and captured-context review. EX_DUF GPR15L preserves
    imported receptor-binding/activation and attraction of GPR15-expressing T cells,
    epithelial expression, human C10ORF99 naming, AP-57/CSBF aliases and reported
    antimicrobial/cancer-cell-growth effects. The opening SIV/HIV-2 co-receptor and
    trafficking statements concern GPR15 receptor, not an independently established
    viral co-receptor function of the ligand. The 9 kDa polypeptide and 57-amino-acid
    AP-57 descriptions are distinct source descriptions, not an inferred precursor
    cleavage map, invariant whole-protein length or domain boundaries. CC motif and
    chemokine-like features do not establish classic CC/CXC sequence homology; two
    disulfide bonds are explicitly predicted, and the activating terminal peptide
    is described as C-terminal. PUB00088053/PUB00088054, receptor binding, SUSD2 interaction,
    cellular assays, peptide processing and one structure entry were not inspected.
    No antiviral, cancer-treatment or universal homologue activity is certified. One
    excess match and four architectures do not define individual organization; 106
    models remain uninspected.
  target_ids:
  - PF15854
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: The captured literal accession (PF15854) and current-short-name (GPR15L)
    searches found no path or content hits under curation/families, evidence and history,
    including hidden and ignored files; the exact canonical overlay, evidence and
    history owners were absent. These bounded results do not establish absence for
    GPR15, C10ORF99, AP-57, CSBF, SUSD2, CC/CXC terms and PUB00088053/PUB00088054
    or wider literature. No primary paper, live upstream record, structural model
    or assay was inspected. A biological or historical assessment needs separately
    verified evidence and tested-protein scope. No accession-named overlay, evidence
    or history path was found by the bounded hidden/ignored-inclusive inventory; the
    inspected projection has no curated claim payload. Optional-field absence is not
    a seed-schema defect.
  target_ids:
  - PF15854
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
  - PF15854
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: Scientific additions would belong in the human-owned curation/families/PF15854.yaml
    overlay with appropriately licensed evidence and actual canonical history, followed
    by generation through src/dufmech/records.py. Frozen snapshots and generated records
    are not direct correction surfaces. No corrective edit is proposed by this seed
    audit.
  target_ids:
  - PF15854
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
