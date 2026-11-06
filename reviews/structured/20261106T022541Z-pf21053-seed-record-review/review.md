# PF21053 BFA1_C: seed identity, provenance and evidence-scope review

- Review: 20261106T022541Z-pf21053-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-11-06T02:11:45Z
- Finished UTC: 2026-11-06T02:25:41Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: seed_only
- Scientific review: false

## Summary

PF21053 (BFA1_C; InterPro:IPR048378) matches the verified frozen source and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED. The pinned InterPro/Pfam snapshot identifies PF21053 (BFA1_C; InterPro:IPR048378) as EX_DUF, with local characterization UNSCORED and curation SEEDED. The complete imported description is: This domain is predominantly found at the C-terminal end of proteins from cyanobacteria and plants, including Biogenesis factor required for ATP synthase 1 (BFA1, [swissprot:F4J1U2]) from Arabidopsis thaliana. BFA1 promotes the assembly of the CF1 subcomplex of the chloroplast ATP synthase by specifically interacting with the gamma and beta subunits. This domain consists of ten beta-sheets and one alpha- helix forming a typical beta-barrel, which locates perpendicularly to [pfam:PF12204] [[cite:PUB00100989]]. Frozen metadata report 798 proteins, 802 matches, 564 proteomes, 1611 taxa, 2 structure entries, 605 AlphaFold models and 15 domain architectures. These are source counters; no protein, sequence, structure, model or underlying publication was inspected. This is a local metadata and representation review, not external biological verification.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: 5642a645349854802748ae387c0e2df121c5e83f. The corpus has 8296 records; 6211 were covered and 2085 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF21053.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5642a645349854802748ae387c0e2df121c5e83f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF21053 | data/families/PF21053.yaml | generated | PF21053 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF21053 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF21053 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF21053 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF21053 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF21053 | 489 valid canonical history records. |
| Generated schema check | passed | True | PF21053 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF21053.

The filename, pfam_id=PF21053, id=Pfam:PF21053, short_name=BFA1_C, name=Biogenesis factor required for ATP synthase 1, C-terminal domain, source URL and InterPro accession InterPro:IPR048378 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF21053.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 798 proteins, 802 matches, 2 structure entries and 605 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF21053.

The pinned InterPro/Pfam snapshot identifies PF21053 (BFA1_C; InterPro:IPR048378) as EX_DUF, with local characterization UNSCORED and curation SEEDED. The complete imported description is: This domain is predominantly found at the C-terminal end of proteins from cyanobacteria and plants, including Biogenesis factor required for ATP synthase 1 (BFA1, [swissprot:F4J1U2]) from Arabidopsis thaliana. BFA1 promotes the assembly of the CF1 subcomplex of the chloroplast ATP synthase by specifically interacting with the gamma and beta subunits. This domain consists of ten beta-sheets and one alpha- helix forming a typical beta-barrel, which locates perpendicularly to [pfam:PF12204] [[cite:PUB00100989]]. Frozen metadata report 798 proteins, 802 matches, 564 proteomes, 1611 taxa, 2 structure entries, 605 AlphaFold models and 15 domain architectures. These are source counters; no protein, sequence, structure, model or underlying publication was inspected. This is a local metadata and representation review, not external biological verification.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF21053.

Review scope is the imported BFA1 C-terminal domain. Predominantly cyanobacterial and plant occurrence is not exclusive. The Arabidopsis thaliana BFA1 example and its CF1 assembly and gamma/beta-subunit interaction claims concern the named protein, not demonstrated sufficiency of this isolated domain or every family member. Preserve the literal ten beta-sheets, one alpha- helix and perpendicular [pfam:PF12204] description without certifying geometry or silently changing sheets to strands. [swissprot:F4J1U2] and [[cite:PUB00100989]] were not resolved.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF21053.

A biological reassessment would require resolving F4J1U2, PF12204 and PUB00100989, checking the reported assembly/interactions, and distinguishing whole-protein evidence from effects or sufficiency of this C-terminal domain. Structural wording, geometry and the scope across family members remain unverified; retain seed_only. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF21053.

seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED express separate states. EX_DUF records historical renaming and is compatible with imported functional descriptions; it is not evidence that all members were tested. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF21053.

Scientific additions would belong in the human-owned curation/families/PF21053.yaml overlay with appropriately licensed evidence and actual canonical history, followed by generation through src/dufmech/records.py. Frozen snapshots and generated records are not direct correction surfaces. No corrective edit is proposed by this seed audit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF21053.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF21053 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF21053; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 489 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF21053 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf21053 | data/families/PF21053.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

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
  git_revision: 5642a645349854802748ae387c0e2df121c5e83f
  inputs:
  - path: data/families/PF21053.yaml
    role: target
    sha256: 2df835882b9647daa1e23b4c94a0237546f98fdbcc9988e6f29ed665f7b0bdaa
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
  label: PF21053
  owner_paths:
  - path: curation/families/PF21053.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF21053.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: 3b0f740e3c057c80dd6dcada31053633213d6d94b30432effff29312b947e951
  target_id: PF21053
schema_version: 1.0.0
review_id: 20261106T022541Z-pf21053-seed-record-review
title: 'PF21053 BFA1_C: seed identity, provenance and evidence-scope review'
started_at: '2026-11-06T02:11:45Z'
finished_at: '2026-11-06T02:25:41Z'
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
summary: 'PF21053 (BFA1_C; InterPro:IPR048378) matches the verified frozen source
  and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED.
  The pinned InterPro/Pfam snapshot identifies PF21053 (BFA1_C; InterPro:IPR048378)
  as EX_DUF, with local characterization UNSCORED and curation SEEDED. The complete
  imported description is: This domain is predominantly found at the C-terminal end
  of proteins from cyanobacteria and plants, including Biogenesis factor required
  for ATP synthase 1 (BFA1, [swissprot:F4J1U2]) from Arabidopsis thaliana. BFA1 promotes
  the assembly of the CF1 subcomplex of the chloroplast ATP synthase by specifically
  interacting with the gamma and beta subunits. This domain consists of ten beta-sheets
  and one alpha- helix forming a typical beta-barrel, which locates perpendicularly
  to [pfam:PF12204] [[cite:PUB00100989]]. Frozen metadata report 798 proteins, 802
  matches, 564 proteomes, 1611 taxa, 2 structure entries, 605 AlphaFold models and
  15 domain architectures. These are source counters; no protein, sequence, structure,
  model or underlying publication was inspected. This is a local metadata and representation
  review, not external biological verification.'
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: 5642a645349854802748ae387c0e2df121c5e83f. The corpus has 8296
    records; 6211 were covered and 2085 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF21053.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF21053
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF21053
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF21053
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-608-attempt-001/PF21053-targets.yaml
    --input data/families/PF21053.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF21053
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-608-attempt-001/prepare.py
    PF21053
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF21053
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
  - PF21053
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
  - PF21053
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
  - PF21053
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF21053.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-11-06T02:25:41Z'
  support: supports
  summary: Read the complete PF21053 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: 2df835882b9647daa1e23b4c94a0237546f98fdbcc9988e6f29ed665f7b0bdaa
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF21053; companion manifest and TSV; native verified inspection
  accessed_at: '2026-11-06T02:25:41Z'
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
  accessed_at: '2026-11-06T02:25:41Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-11-06T02:25:41Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 489 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF21053
  accessed_at: '2026-11-06T02:25:41Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF21053. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf21053
  kind: record_content
  reference: data/families/PF21053.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-11-06T02:25:41Z'
  support: context_only
  snapshot_sha256: 2df835882b9647daa1e23b4c94a0237546f98fdbcc9988e6f29ed665f7b0bdaa
  quote: "id: Pfam:PF21053\npfam_id: PF21053\nname: Biogenesis factor required for\
    \ ATP synthase 1, C-terminal domain\nshort_name: BFA1_C\nseed_status: EX_DUF\n\
    characterization_status: UNSCORED\ncuration_status: SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF21053\n\
    counters:\n  proteins: 798\n  matches: 802\n  proteomes: 564\n  taxa: 1611\n \
    \ structures: 2\n  alphafold_models: 605\n  domain_architectures: 15\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR048378\ndescription: This domain is predominantly found\
    \ at the C-terminal end of proteins from cyanobacteria and\n  plants, including\
    \ Biogenesis factor required for ATP synthase 1 (BFA1, [swissprot:F4J1U2]) from\
    \ Arabidopsis\n  thaliana. BFA1 promotes the assembly of the CF1 subcomplex of\
    \ the chloroplast ATP synthase by specifically\n  interacting with the gamma and\
    \ beta subunits. This domain consists of ten beta-sheets and one alpha-\n  helix\
    \ forming a typical beta-barrel, which locates perpendicularly to [pfam:PF12204]\
    \ [[cite:PUB00100989]].\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF21053, id=Pfam:PF21053, short_name=BFA1_C, name=Biogenesis
    factor required for ATP synthase 1, C-terminal domain, source URL and InterPro
    accession InterPro:IPR048378 agree with the selected frozen row. This establishes
    frozen identity correspondence, not current upstream taxonomy or function.
  target_ids:
  - PF21053
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 798 proteins, 802 matches, 2 structure entries and 605
    AlphaFold models are frozen database counters, not independent experiments. Raw
    input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF21053
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: 'The pinned InterPro/Pfam snapshot identifies PF21053 (BFA1_C; InterPro:IPR048378)
    as EX_DUF, with local characterization UNSCORED and curation SEEDED. The complete
    imported description is: This domain is predominantly found at the C-terminal
    end of proteins from cyanobacteria and plants, including Biogenesis factor required
    for ATP synthase 1 (BFA1, [swissprot:F4J1U2]) from Arabidopsis thaliana. BFA1
    promotes the assembly of the CF1 subcomplex of the chloroplast ATP synthase by
    specifically interacting with the gamma and beta subunits. This domain consists
    of ten beta-sheets and one alpha- helix forming a typical beta-barrel, which locates
    perpendicularly to [pfam:PF12204] [[cite:PUB00100989]]. Frozen metadata report
    798 proteins, 802 matches, 564 proteomes, 1611 taxa, 2 structure entries, 605
    AlphaFold models and 15 domain architectures. These are source counters; no protein,
    sequence, structure, model or underlying publication was inspected. This is a
    local metadata and representation review, not external biological verification.'
  target_ids:
  - PF21053
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
  summary: Review scope is the imported BFA1 C-terminal domain. Predominantly cyanobacterial
    and plant occurrence is not exclusive. The Arabidopsis thaliana BFA1 example and
    its CF1 assembly and gamma/beta-subunit interaction claims concern the named protein,
    not demonstrated sufficiency of this isolated domain or every family member. Preserve
    the literal ten beta-sheets, one alpha- helix and perpendicular [pfam:PF12204]
    description without certifying geometry or silently changing sheets to strands.
    [swissprot:F4J1U2] and [[cite:PUB00100989]] were not resolved.
  target_ids:
  - PF21053
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: A biological reassessment would require resolving F4J1U2, PF12204 and PUB00100989,
    checking the reported assembly/interactions, and distinguishing whole-protein
    evidence from effects or sufficiency of this C-terminal domain. Structural wording,
    geometry and the scope across family members remain unverified; retain seed_only.
    No accession-named overlay, evidence or history path was found by the bounded
    hidden/ignored-inclusive inventory; the inspected projection has no curated claim
    payload. Optional-field absence is not a seed-schema defect.
  target_ids:
  - PF21053
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
  - PF21053
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: Scientific additions would belong in the human-owned curation/families/PF21053.yaml
    overlay with appropriately licensed evidence and actual canonical history, followed
    by generation through src/dufmech/records.py. Frozen snapshots and generated records
    are not direct correction surfaces. No corrective edit is proposed by this seed
    audit.
  target_ids:
  - PF21053
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
