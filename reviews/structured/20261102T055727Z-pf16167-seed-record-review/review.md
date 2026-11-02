# PF16167 DUF4871: seed identity, provenance and evidence-scope review

- Review: 20261102T055727Z-pf16167-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-11-02T05:51:22Z
- Finished UTC: 2026-11-02T05:57:27Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

PF16167 (DUF4871; InterPro:IPR032366) matches the verified frozen source and retains seed_status=UNKNOWN_CANDIDATE, characterization_status=UNSCORED and curation_status=SEEDED. DUF4871 (IPR032366; UNKNOWN_CANDIDATE) retains this frozen-source description: “This family consists of uncharacterized proteins around 170 residues in length and is mainly found in various Bacillus species (B. cereus, B. thuringiensis and B. anthracis). The solved structure of B. anthracis homologs has a variant of the Greek-key beta barrel fold, making the DUF4870 family a member of a large group of bacterial immunoglobulin like domains, but the functional consequences of this classification remain unknown.” All seven counters agree between row and projection: 454 proteins, 457 matches, 373 proteomes, 496 taxa, 1 structures, 249 models, 4 architectures. Verify the DUF4870/DUF4871 family referent and attribution of the reported structural comparison. This is a provisional minor wording follow-up; no replacement family or corrected structural or functional claim is asserted.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: aa7d08bcf3a9a03879d06cffd075bc083d29788f. The corpus has 8296 records; 4401 were covered and 3895 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF16167.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base aa7d08bcf3a9a03879d06cffd075bc083d29788f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF16167 | data/families/PF16167.yaml | generated | PF16167 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF16167 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF16167 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF16167 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF16167 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF16167 | 489 valid canonical history records. |
| Generated schema check | passed | True | PF16167 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF16167.

The filename, pfam_id=PF16167, id=Pfam:PF16167, short_name=DUF4871, name=Domain of unknown function (DUF4871), source URL and InterPro accession InterPro:IPR032366 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF16167.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 454 proteins, 457 matches, 1 structure entries and 249 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF16167.

DUF4871 (IPR032366; UNKNOWN_CANDIDATE) retains this frozen-source description: “This family consists of uncharacterized proteins around 170 residues in length and is mainly found in various Bacillus species (B. cereus, B. thuringiensis and B. anthracis). The solved structure of B. anthracis homologs has a variant of the Greek-key beta barrel fold, making the DUF4870 family a member of a large group of bacterial immunoglobulin like domains, but the functional consequences of this classification remain unknown.” All seven counters agree between row and projection: 454 proteins, 457 matches, 373 proteomes, 496 taxa, 1 structures, 249 models, 4 architectures.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF16167.

Metadata-only source and captured-context review. PF16167 is named DUF4871 in both name and short_name, but its imported description calls the structurally classified family DUF4870. Retain this internal naming inconsistency as a provisional minor referent-verification follow-up; the accession itself is resolved, and no replacement family or corrected structural attribution is established here. The source reports proteins around 170 residues in Bacillus, including B. cereus, B. thuringiensis and B. anthracis, and a Greek-key beta-barrel variant in B. anthracis homologs, with functional consequences unknown. Neither immunoglobulin-like classification nor pathogen occurrence proves binding, immune function or virulence. Approximate whole-protein size is not domain boundaries. Three excess matches/four architectures do not settle per-protein repeats; one structure and 249 models were not inspected.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF16167.

The captured literal accession (PF16167) and current-short-name (DUF4871) searches found no path or content hits under curation/families, evidence and history, including hidden and ignored files; the exact canonical overlay, evidence and history owners were absent. These bounded searches do not establish absence for unqueried aliases, historical DUF names, expanded names, cited publication tokens, related Pfam accessions, fold or enzyme terms, taxa, ecological terms or wider literature. No primary paper, live upstream record, structure, model or assay was inspected. A biological or historical assessment requires separately verified evidence and tested-protein scope. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF16167.

seed_status=UNKNOWN_CANDIDATE, characterization_status=UNSCORED and curation_status=SEEDED express separate states. UNKNOWN_CANDIDATE is the retained lexical seed class, not an experimentally established absence of function. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF16167.

Verify imported wording through the maintained upstream-source review and freeze workflow. Any supported local clarification belongs in curation/families/PF16167.yaml with licensed evidence and actual canonical history, followed by normal projection generation. Do not hand-edit the frozen snapshot or generated projection. This review retains a verification task only; no source, overlay or history edit is made.

### Verify DUF4870 versus DUF4871 in the imported description

completeness: concern. Targets: PF16167.

The name and short_name identify DUF4871, while the same frozen row and generated description refer to the structurally classified family as DUF4870. Verify the intended family referent and attribution of the reported structural comparison before clarifying the wording. This provisional concern does not assert which token is wrong, replace a Pfam identity or establish the structural or functional claim.

## Findings

### family-name-reference: Verify DUF4870 versus DUF4871 in the imported description

minor / open / provisional; issue key: pf16167-imported-duf4870-reference.

The name and short_name identify DUF4871, while the same frozen row and generated description refer to the structurally classified family as DUF4870. Verify the intended family referent and attribution of the reported structural comparison before clarifying the wording. This provisional concern does not assert which token is wrong, replace a Pfam identity or establish the structural or functional claim.

## Recommended Actions And Acceptance Checks

### verify-family-name-reference

Verify DUF4870 versus DUF4871 in the imported description against dated authoritative source evidence before any maintained clarification.

- Retain dated authoritative evidence resolving the DUF4870/DUF4871 referent in this description and the reported B. anthracis structural example.
- State whether the family token or structural attribution requires clarification without silently transferring a claim between families.
- Route any supported clarification through maintained source/overlay/history owners; preserve frozen inputs and this review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF16167.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF16167 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF16167; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 489 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF16167 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf16167 | data/families/PF16167.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

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
  git_revision: aa7d08bcf3a9a03879d06cffd075bc083d29788f
  inputs:
  - path: data/families/PF16167.yaml
    role: target
    sha256: 81890ce9c8685272a592b2be54c0bdc35f3197df173aa1f5bb15fc0416d50f97
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
  label: PF16167
  owner_paths:
  - path: curation/families/PF16167.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF16167.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: 0d5452b78d8a3b69d915a145d480de55d08e7677188961356e33f46b0e23e513
  target_id: PF16167
schema_version: 1.0.0
review_id: 20261102T055727Z-pf16167-seed-record-review
title: 'PF16167 DUF4871: seed identity, provenance and evidence-scope review'
started_at: '2026-11-02T05:51:22Z'
finished_at: '2026-11-02T05:57:27Z'
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
summary: 'PF16167 (DUF4871; InterPro:IPR032366) matches the verified frozen source
  and retains seed_status=UNKNOWN_CANDIDATE, characterization_status=UNSCORED and
  curation_status=SEEDED. DUF4871 (IPR032366; UNKNOWN_CANDIDATE) retains this frozen-source
  description: “This family consists of uncharacterized proteins around 170 residues
  in length and is mainly found in various Bacillus species (B. cereus, B. thuringiensis
  and B. anthracis). The solved structure of B. anthracis homologs has a variant of
  the Greek-key beta barrel fold, making the DUF4870 family a member of a large group
  of bacterial immunoglobulin like domains, but the functional consequences of this
  classification remain unknown.” All seven counters agree between row and projection:
  454 proteins, 457 matches, 373 proteomes, 496 taxa, 1 structures, 249 models, 4
  architectures. Verify the DUF4870/DUF4871 family referent and attribution of the
  reported structural comparison. This is a provisional minor wording follow-up; no
  replacement family or corrected structural or functional claim is asserted.'
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: aa7d08bcf3a9a03879d06cffd075bc083d29788f. The corpus has 8296
    records; 4401 were covered and 3895 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF16167.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF16167
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF16167
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF16167
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-427-attempt-001/PF16167-targets.yaml
    --input data/families/PF16167.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF16167
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-427-attempt-001/prepare.py
    PF16167
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF16167
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
  - PF16167
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
  - PF16167
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
  - PF16167
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF16167.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-11-02T05:57:27Z'
  support: supports
  summary: Read the complete PF16167 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: 81890ce9c8685272a592b2be54c0bdc35f3197df173aa1f5bb15fc0416d50f97
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF16167; companion manifest and TSV; native verified inspection
  accessed_at: '2026-11-02T05:57:27Z'
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
  accessed_at: '2026-11-02T05:57:27Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-11-02T05:57:27Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 489 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF16167
  accessed_at: '2026-11-02T05:57:27Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF16167. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf16167
  kind: record_content
  reference: data/families/PF16167.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-11-02T05:57:27Z'
  support: context_only
  snapshot_sha256: 81890ce9c8685272a592b2be54c0bdc35f3197df173aa1f5bb15fc0416d50f97
  quote: "id: Pfam:PF16167\npfam_id: PF16167\nname: Domain of unknown function (DUF4871)\n\
    short_name: DUF4871\nseed_status: UNKNOWN_CANDIDATE\ncharacterization_status:\
    \ UNSCORED\ncuration_status: SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF16167\n\
    counters:\n  proteins: 454\n  matches: 457\n  proteomes: 373\n  taxa: 496\n  structures:\
    \ 1\n  alphafold_models: 249\n  domain_architectures: 4\nprovenance:\n  snapshot_id:\
    \ interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR032366\ndescription: This family consists of uncharacterized\
    \ proteins around 170 residues in length and is mainly\n  found in various Bacillus\
    \ species (B. cereus, B. thuringiensis and B. anthracis). The solved structure\n\
    \  of B. anthracis homologs has a variant of the Greek-key beta barrel fold, making\
    \ the DUF4870 family\n  a member of a large group of bacterial immunoglobulin\
    \ like domains, but the functional consequences\n  of this classification remain\
    \ unknown.\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF16167, id=Pfam:PF16167, short_name=DUF4871, name=Domain
    of unknown function (DUF4871), source URL and InterPro accession InterPro:IPR032366
    agree with the selected frozen row. This establishes frozen identity correspondence,
    not current upstream taxonomy or function.
  target_ids:
  - PF16167
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 454 proteins, 457 matches, 1 structure entries and 249
    AlphaFold models are frozen database counters, not independent experiments. Raw
    input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF16167
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: 'DUF4871 (IPR032366; UNKNOWN_CANDIDATE) retains this frozen-source description:
    “This family consists of uncharacterized proteins around 170 residues in length
    and is mainly found in various Bacillus species (B. cereus, B. thuringiensis and
    B. anthracis). The solved structure of B. anthracis homologs has a variant of
    the Greek-key beta barrel fold, making the DUF4870 family a member of a large
    group of bacterial immunoglobulin like domains, but the functional consequences
    of this classification remain unknown.” All seven counters agree between row and
    projection: 454 proteins, 457 matches, 373 proteomes, 496 taxa, 1 structures,
    249 models, 4 architectures.'
  target_ids:
  - PF16167
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
  summary: Metadata-only source and captured-context review. PF16167 is named DUF4871
    in both name and short_name, but its imported description calls the structurally
    classified family DUF4870. Retain this internal naming inconsistency as a provisional
    minor referent-verification follow-up; the accession itself is resolved, and no
    replacement family or corrected structural attribution is established here. The
    source reports proteins around 170 residues in Bacillus, including B. cereus,
    B. thuringiensis and B. anthracis, and a Greek-key beta-barrel variant in B. anthracis
    homologs, with functional consequences unknown. Neither immunoglobulin-like classification
    nor pathogen occurrence proves binding, immune function or virulence. Approximate
    whole-protein size is not domain boundaries. Three excess matches/four architectures
    do not settle per-protein repeats; one structure and 249 models were not inspected.
  target_ids:
  - PF16167
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: The captured literal accession (PF16167) and current-short-name (DUF4871)
    searches found no path or content hits under curation/families, evidence and history,
    including hidden and ignored files; the exact canonical overlay, evidence and
    history owners were absent. These bounded searches do not establish absence for
    unqueried aliases, historical DUF names, expanded names, cited publication tokens,
    related Pfam accessions, fold or enzyme terms, taxa, ecological terms or wider
    literature. No primary paper, live upstream record, structure, model or assay
    was inspected. A biological or historical assessment requires separately verified
    evidence and tested-protein scope. No accession-named overlay, evidence or history
    path was found by the bounded hidden/ignored-inclusive inventory; the inspected
    projection has no curated claim payload. Optional-field absence is not a seed-schema
    defect.
  target_ids:
  - PF16167
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
  - PF16167
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: Verify imported wording through the maintained upstream-source review and
    freeze workflow. Any supported local clarification belongs in curation/families/PF16167.yaml
    with licensed evidence and actual canonical history, followed by normal projection
    generation. Do not hand-edit the frozen snapshot or generated projection. This
    review retains a verification task only; no source, overlay or history edit is
    made.
  target_ids:
  - PF16167
  evidence_ids:
  - profile
  - record
  - validation
- assessment_id: family-name-reference-assessment
  area: completeness
  topic: Verify DUF4870 versus DUF4871 in the imported description
  outcome: concern
  summary: The name and short_name identify DUF4871, while the same frozen row and
    generated description refer to the structurally classified family as DUF4870.
    Verify the intended family referent and attribution of the reported structural
    comparison before clarifying the wording. This provisional concern does not assert
    which token is wrong, replace a Pfam identity or establish the structural or functional
    claim.
  target_ids:
  - PF16167
  evidence_ids:
  - record
  - snapshot
findings:
- finding_id: family-name-reference
  issue_key: pf16167-imported-duf4870-reference
  category: completeness
  severity: minor
  status: open
  certainty: provisional
  title: Verify DUF4870 versus DUF4871 in the imported description
  description: The name and short_name identify DUF4871, while the same frozen row
    and generated description refer to the structurally classified family as DUF4870.
    Verify the intended family referent and attribution of the reported structural
    comparison before clarifying the wording. This provisional concern does not assert
    which token is wrong, replace a Pfam identity or establish the structural or functional
    claim.
  target_ids:
  - PF16167
  field_paths:
  - description
  evidence_ids:
  - record
  - snapshot
  normalization_reason: Bounded provisional representation/referent concern in actual
    imported wording; no established biological error or corrected identity/chemistry
    is asserted.
  ownership_note: Verify imported wording through the maintained upstream-source review
    and freeze workflow. Any supported local clarification belongs in curation/families/PF16167.yaml
    with licensed evidence and actual canonical history, followed by normal projection
    generation. Do not hand-edit the frozen snapshot or generated projection.
actions:
- action_id: verify-family-name-reference
  description: Verify DUF4870 versus DUF4871 in the imported description against dated
    authoritative source evidence before any maintained clarification.
  finding_ids:
  - family-name-reference
  target_ids:
  - PF16167
  ownership_note: Verify imported wording through the maintained upstream-source review
    and freeze workflow. Any supported local clarification belongs in curation/families/PF16167.yaml
    with licensed evidence and actual canonical history, followed by normal projection
    generation. Do not hand-edit the frozen snapshot or generated projection.
  acceptance_checks:
  - Retain dated authoritative evidence resolving the DUF4870/DUF4871 referent in
    this description and the reported B. anthracis structural example.
  - State whether the family token or structural attribution requires clarification
    without silently transferring a claim between families.
  - Route any supported clarification through maintained source/overlay/history owners;
    preserve frozen inputs and this review.
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
