# PF16288 DUF4934: seed identity, provenance and evidence-scope review

- Review: 20261102T075820Z-pf16288-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-11-02T07:51:11Z
- Finished UTC: 2026-11-02T07:58:20Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

PF16288 (DUF4934; InterPro:IPR032558) matches the verified frozen source and retains seed_status=UNKNOWN_CANDIDATE, characterization_status=UNSCORED and curation_status=SEEDED. DUF4934 (IPR032558; UNKNOWN_CANDIDATE) retains this frozen-source description: “This family consists of uncharacterised proteins around 400 residues in length and is mainly found in various Bacteroides species, such as Bacteroides fragilis and Bacteroides sp.These proteins adopt a six stranded beta-propeller domain. The function of this family is unknown.” All seven counters agree between row and projection: 1687 proteins, 1687 matches, 319 proteomes, 524 taxa, 0 structures, 1145 models, 3 architectures. Verify which structural elements are counted by the imported six stranded beta-propeller wording; this provisional minor follow-up asserts no typo, replacement topology or new function.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: aa7d08bcf3a9a03879d06cffd075bc083d29788f. The corpus has 8296 records; 4461 were covered and 3835 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF16288.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base aa7d08bcf3a9a03879d06cffd075bc083d29788f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF16288 | data/families/PF16288.yaml | generated | PF16288 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF16288 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF16288 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF16288 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF16288 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF16288 | 489 valid canonical history records. |
| Generated schema check | passed | True | PF16288 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF16288.

The filename, pfam_id=PF16288, id=Pfam:PF16288, short_name=DUF4934, name=Domain of unknown function (DUF4934), source URL and InterPro accession InterPro:IPR032558 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF16288.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 1687 proteins, 1687 matches, 0 structure entries and 1145 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF16288.

DUF4934 (IPR032558; UNKNOWN_CANDIDATE) retains this frozen-source description: “This family consists of uncharacterised proteins around 400 residues in length and is mainly found in various Bacteroides species, such as Bacteroides fragilis and Bacteroides sp.These proteins adopt a six stranded beta-propeller domain. The function of this family is unknown.” All seven counters agree between row and projection: 1687 proteins, 1687 matches, 319 proteomes, 524 taxa, 0 structures, 1145 models, 3 architectures.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF16288.

Metadata-only source and captured-context review. DUF4934 describes approximately 400-residue proteins in Bacteroides, including Bacteroides fragilis and unspecified Bacteroides sp., and states that these proteins adopt a six stranded beta-propeller domain while function is unknown. Retain this exact imported structural wording without silently converting stranded to bladed, claiming six repeats or independently confirming a fold or biochemical role. The missing space in sp.These leaves the claims intelligible and establishes no scientific correction here. Protein length is not exact domain extent. Equal 1687 proteins/matches and three architectures do not establish universal organization. Zero structures and 1145 models were not inspected. The intended counted structural elements remain unresolved: retain a provisional minor follow-up to verify the topology terminology before interpreting six as a strand or blade count. This requests verification and asserts no typo, corrected topology or new biological result.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF16288.

The captured literal accession (PF16288) and current-short-name (DUF4934) searches found no path or content hits under curation/families, evidence and history, including hidden and ignored files; the exact canonical overlay, evidence and history owners were absent. These bounded searches do not establish absence for unqueried aliases, historical DUF names, expanded names, cited publication tokens, related Pfam accessions, protein names, fold or enzyme terms, taxa, ecological terms or wider literature. No primary paper, live upstream record, structure, model or assay was inspected. A biological or historical assessment requires separately verified evidence and tested-protein scope. Beta-propeller, stranded/bladed variants and named Bacteroides aliases were not separate queries; no absence claim is made for them. The bounded empty context does not resolve the counted structural elements in the imported beta-propeller wording; retain the explicit verification action through maintained source or overlay owners. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF16288.

seed_status=UNKNOWN_CANDIDATE, characterization_status=UNSCORED and curation_status=SEEDED express separate states. UNKNOWN_CANDIDATE is the retained lexical seed class, not an experimentally established absence of function. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF16288.

Verify the imported description through the maintained upstream-source review and freeze workflow. Any supported local clarification belongs in curation/families/PF16288.yaml with licensed evidence and actual canonical history, followed by normal projection generation. Do not hand-edit this frozen snapshot or generated projection. This review records a verification task; no source, overlay or history edit is made.

### Verify the imported beta-propeller structural-element count

completeness: concern. Targets: PF16288.

The frozen row and generated projection describe a 'six stranded beta-propeller domain'. Verify which structural elements the count six refers to and the intended topology terminology before using this phrase as a strand or blade count. This bounded representation concern does not establish a typo, a six-bladed replacement, a different fold or a biological error.

## Findings

### propeller-structural-element-wording: Verify the structural elements counted in the imported beta-propeller wording

minor / open / provisional; issue key: pf16288-imported-propeller-element-count.

The frozen row and generated projection describe a 'six stranded beta-propeller domain'. Verify which structural elements the count six refers to and the intended topology terminology before using this phrase as a strand or blade count. This bounded representation concern does not establish a typo, a six-bladed replacement, a different fold or a biological error.

## Recommended Actions And Acceptance Checks

### verify-propeller-structural-elements

Verify the intended structural-element count and topology terminology in the literal 'six stranded beta-propeller domain' using dated authoritative evidence, without silently substituting a blade count or a different fold.

- Retain dated authoritative evidence resolving what elements the stated count six refers to and the intended beta-propeller description.
- Record whether the wording is confirmed or needs clarification without assuming a typo, a six-bladed replacement, a different fold, exact domain coordinates or a newly established function.
- If supported, route clarification through maintained source/overlay/history owners under the same issue key while preserving this frozen snapshot and review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF16288.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF16288 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF16288; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 489 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF16288 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf16288 | data/families/PF16288.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

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
  - path: data/families/PF16288.yaml
    role: target
    sha256: 99f1a9ad654125a158ed9c2759ee5a3d2735eb5bc7bb81251374152e02f3fc59
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
  label: PF16288
  owner_paths:
  - path: curation/families/PF16288.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF16288.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: b5b71b18e62ea2d9563082ba46e03ab2d27ac241f7ded8ca94b1942860f927f2
  target_id: PF16288
schema_version: 1.0.0
review_id: 20261102T075820Z-pf16288-seed-record-review
title: 'PF16288 DUF4934: seed identity, provenance and evidence-scope review'
started_at: '2026-11-02T07:51:11Z'
finished_at: '2026-11-02T07:58:20Z'
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
summary: 'PF16288 (DUF4934; InterPro:IPR032558) matches the verified frozen source
  and retains seed_status=UNKNOWN_CANDIDATE, characterization_status=UNSCORED and
  curation_status=SEEDED. DUF4934 (IPR032558; UNKNOWN_CANDIDATE) retains this frozen-source
  description: “This family consists of uncharacterised proteins around 400 residues
  in length and is mainly found in various Bacteroides species, such as Bacteroides
  fragilis and Bacteroides sp.These proteins adopt a six stranded beta-propeller domain.
  The function of this family is unknown.” All seven counters agree between row and
  projection: 1687 proteins, 1687 matches, 319 proteomes, 524 taxa, 0 structures,
  1145 models, 3 architectures. Verify which structural elements are counted by the
  imported six stranded beta-propeller wording; this provisional minor follow-up asserts
  no typo, replacement topology or new function.'
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: aa7d08bcf3a9a03879d06cffd075bc083d29788f. The corpus has 8296
    records; 4461 were covered and 3835 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF16288.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF16288
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF16288
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF16288
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-433-attempt-001/PF16288-targets.yaml
    --input data/families/PF16288.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF16288
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-433-attempt-001/prepare.py
    PF16288
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF16288
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
  - PF16288
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
  - PF16288
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
  - PF16288
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF16288.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-11-02T07:58:20Z'
  support: supports
  summary: Read the complete PF16288 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: 99f1a9ad654125a158ed9c2759ee5a3d2735eb5bc7bb81251374152e02f3fc59
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF16288; companion manifest and TSV; native verified inspection
  accessed_at: '2026-11-02T07:58:20Z'
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
  accessed_at: '2026-11-02T07:58:20Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-11-02T07:58:20Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 489 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF16288
  accessed_at: '2026-11-02T07:58:20Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF16288. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf16288
  kind: record_content
  reference: data/families/PF16288.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-11-02T07:58:20Z'
  support: context_only
  snapshot_sha256: 99f1a9ad654125a158ed9c2759ee5a3d2735eb5bc7bb81251374152e02f3fc59
  quote: "id: Pfam:PF16288\npfam_id: PF16288\nname: Domain of unknown function (DUF4934)\n\
    short_name: DUF4934\nseed_status: UNKNOWN_CANDIDATE\ncharacterization_status:\
    \ UNSCORED\ncuration_status: SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF16288\n\
    counters:\n  proteins: 1687\n  matches: 1687\n  proteomes: 319\n  taxa: 524\n\
    \  structures: 0\n  alphafold_models: 1145\n  domain_architectures: 3\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR032558\ndescription: This family consists of uncharacterised\
    \ proteins around 400 residues in length and is mainly\n  found in various Bacteroides\
    \ species, such as Bacteroides fragilis and Bacteroides sp.These proteins\n  adopt\
    \ a six stranded beta-propeller domain. The function of this family is unknown.\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF16288, id=Pfam:PF16288, short_name=DUF4934, name=Domain
    of unknown function (DUF4934), source URL and InterPro accession InterPro:IPR032558
    agree with the selected frozen row. This establishes frozen identity correspondence,
    not current upstream taxonomy or function.
  target_ids:
  - PF16288
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 1687 proteins, 1687 matches, 0 structure entries and
    1145 AlphaFold models are frozen database counters, not independent experiments.
    Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF16288
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: 'DUF4934 (IPR032558; UNKNOWN_CANDIDATE) retains this frozen-source description:
    “This family consists of uncharacterised proteins around 400 residues in length
    and is mainly found in various Bacteroides species, such as Bacteroides fragilis
    and Bacteroides sp.These proteins adopt a six stranded beta-propeller domain.
    The function of this family is unknown.” All seven counters agree between row
    and projection: 1687 proteins, 1687 matches, 319 proteomes, 524 taxa, 0 structures,
    1145 models, 3 architectures.'
  target_ids:
  - PF16288
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
  summary: 'Metadata-only source and captured-context review. DUF4934 describes approximately
    400-residue proteins in Bacteroides, including Bacteroides fragilis and unspecified
    Bacteroides sp., and states that these proteins adopt a six stranded beta-propeller
    domain while function is unknown. Retain this exact imported structural wording
    without silently converting stranded to bladed, claiming six repeats or independently
    confirming a fold or biochemical role. The missing space in sp.These leaves the
    claims intelligible and establishes no scientific correction here. Protein length
    is not exact domain extent. Equal 1687 proteins/matches and three architectures
    do not establish universal organization. Zero structures and 1145 models were
    not inspected. The intended counted structural elements remain unresolved: retain
    a provisional minor follow-up to verify the topology terminology before interpreting
    six as a strand or blade count. This requests verification and asserts no typo,
    corrected topology or new biological result.'
  target_ids:
  - PF16288
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: The captured literal accession (PF16288) and current-short-name (DUF4934)
    searches found no path or content hits under curation/families, evidence and history,
    including hidden and ignored files; the exact canonical overlay, evidence and
    history owners were absent. These bounded searches do not establish absence for
    unqueried aliases, historical DUF names, expanded names, cited publication tokens,
    related Pfam accessions, protein names, fold or enzyme terms, taxa, ecological
    terms or wider literature. No primary paper, live upstream record, structure,
    model or assay was inspected. A biological or historical assessment requires separately
    verified evidence and tested-protein scope. Beta-propeller, stranded/bladed variants
    and named Bacteroides aliases were not separate queries; no absence claim is made
    for them. The bounded empty context does not resolve the counted structural elements
    in the imported beta-propeller wording; retain the explicit verification action
    through maintained source or overlay owners. No accession-named overlay, evidence
    or history path was found by the bounded hidden/ignored-inclusive inventory; the
    inspected projection has no curated claim payload. Optional-field absence is not
    a seed-schema defect.
  target_ids:
  - PF16288
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
  - PF16288
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: Verify the imported description through the maintained upstream-source
    review and freeze workflow. Any supported local clarification belongs in curation/families/PF16288.yaml
    with licensed evidence and actual canonical history, followed by normal projection
    generation. Do not hand-edit this frozen snapshot or generated projection. This
    review records a verification task; no source, overlay or history edit is made.
  target_ids:
  - PF16288
  evidence_ids:
  - profile
  - record
  - validation
- assessment_id: propeller-element-wording-assessment
  area: completeness
  topic: Verify the imported beta-propeller structural-element count
  outcome: concern
  summary: The frozen row and generated projection describe a 'six stranded beta-propeller
    domain'. Verify which structural elements the count six refers to and the intended
    topology terminology before using this phrase as a strand or blade count. This
    bounded representation concern does not establish a typo, a six-bladed replacement,
    a different fold or a biological error.
  target_ids:
  - PF16288
  evidence_ids:
  - record
  - snapshot
findings:
- finding_id: propeller-structural-element-wording
  issue_key: pf16288-imported-propeller-element-count
  category: completeness
  severity: minor
  status: open
  certainty: provisional
  title: Verify the structural elements counted in the imported beta-propeller wording
  description: The frozen row and generated projection describe a 'six stranded beta-propeller
    domain'. Verify which structural elements the count six refers to and the intended
    topology terminology before using this phrase as a strand or blade count. This
    bounded representation concern does not establish a typo, a six-bladed replacement,
    a different fold or a biological error.
  target_ids:
  - PF16288
  field_paths:
  - description
  evidence_ids:
  - record
  - snapshot
  normalization_reason: Provisional structural-wording ambiguity affecting interpretation
    of the counted elements; no corrected topology or biological claim asserted.
  ownership_note: Verify the imported description through the maintained upstream-source
    review and freeze workflow. Any supported local clarification belongs in curation/families/PF16288.yaml
    with licensed evidence and actual canonical history, followed by normal projection
    generation. Do not hand-edit this frozen snapshot or generated projection.
actions:
- action_id: verify-propeller-structural-elements
  description: Verify the intended structural-element count and topology terminology
    in the literal 'six stranded beta-propeller domain' using dated authoritative
    evidence, without silently substituting a blade count or a different fold.
  finding_ids:
  - propeller-structural-element-wording
  target_ids:
  - PF16288
  ownership_note: Verify the imported description through the maintained upstream-source
    review and freeze workflow. Any supported local clarification belongs in curation/families/PF16288.yaml
    with licensed evidence and actual canonical history, followed by normal projection
    generation. Do not hand-edit this frozen snapshot or generated projection.
  acceptance_checks:
  - Retain dated authoritative evidence resolving what elements the stated count six
    refers to and the intended beta-propeller description.
  - Record whether the wording is confirmed or needs clarification without assuming
    a typo, a six-bladed replacement, a different fold, exact domain coordinates or
    a newly established function.
  - If supported, route clarification through maintained source/overlay/history owners
    under the same issue key while preserving this frozen snapshot and review.
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
