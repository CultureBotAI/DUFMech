# PF15162 SCRE: seed identity, provenance and evidence-scope review

- Review: 20261101T220624Z-pf15162-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-11-01T22:00:40Z
- Finished UTC: 2026-11-01T22:06:24Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

PF15162 (SCRE; InterPro:IPR027857) matches the verified frozen source and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED. SCRE (IPR027857) retains SPO16/SCRE identity, mammalian-yeast orthology context, synaptonemal-complex reinforcement, SHOC1 association and TEX11/MSH4 localization statements. Both source surfaces contain the incomplete citation fragment germ cells [1.; later PUB00096701 markers do not resolve that fragment. All seven counters agree between row and projection: 556 proteins, 558 matches, 477 proteomes, 1717 taxa, 0 structures, 485 models, 5 architectures. Verify the incomplete imported citation fragment. This is a minor source-text representation follow-up; no missing citation, identifier correction or coordinate is asserted.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: aa7d08bcf3a9a03879d06cffd075bc083d29788f. The corpus has 8296 records; 4111 were covered and 4185 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF15162.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base aa7d08bcf3a9a03879d06cffd075bc083d29788f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF15162 | data/families/PF15162.yaml | generated | PF15162 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF15162 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF15162 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF15162 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF15162 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF15162 | 489 valid canonical history records. |
| Generated schema check | passed | True | PF15162 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF15162.

The filename, pfam_id=PF15162, id=Pfam:PF15162, short_name=SCRE, name=Protein SPO16 homolog, source URL and InterPro accession InterPro:IPR027857 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF15162.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 556 proteins, 558 matches, 0 structure entries and 485 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF15162.

SCRE (IPR027857) retains SPO16/SCRE identity, mammalian-yeast orthology context, synaptonemal-complex reinforcement, SHOC1 association and TEX11/MSH4 localization statements. Both source surfaces contain the incomplete citation fragment germ cells [1.; later PUB00096701 markers do not resolve that fragment. All seven counters agree between row and projection: 556 proteins, 558 matches, 477 proteomes, 1717 taxa, 0 structures, 485 models, 5 architectures.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF15162.

Metadata-only source and captured-context review. Preserve EX_DUF SCRE/SPO16 and distinguish source-reported synaptonemal-complex reinforcement, SHOC1 association and TEX11/MSH4 localization from direct recombination catalysis or partner-function transfer. The literal germ cells [1. fragment is malformed in both the projection and frozen row, making that local citation incomplete. This is a confirmed bounded citation-representation defect requiring follow-up; do not infer its missing source from the later PUB00096701 markers or alter the frozen row. No primary paper, structure or any of 485 models was inspected.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF15162.

The captured literal PF15162 and SCRE searches under curation/families, evidence and history included hidden and ignored files. No accession hit or path hit was found; the one SCRE content hit is the substring in DISCREPANCIES at evidence/PF01901/sheng-2024.txt line 22, not a SCRE assertion. The exact canonical overlay, evidence and history owners were absent. These bounded results do not establish absence for historical or organism aliases or wider literature. No primary paper, live upstream record, structural model or assay was inspected. A biological or historical assessment needs separately verified evidence and tested-protein scope. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF15162.

seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED express separate states. EX_DUF records historical renaming and is compatible with imported functional descriptions; it is not evidence that all members were tested. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF15162.

Verify and clarify imported source metadata through the maintained upstream-source review and freeze workflow. Any evidence-backed local correction belongs in curation/families/PF15162.yaml with licensed evidence and actual canonical history, followed by normal projection generation. Do not hand-edit the frozen snapshot or generated projection. This review records verification work only; no source, overlay or history edit is made.

### Verify the incomplete imported citation fragment

completeness: concern. Targets: PF15162.

Both the frozen row and generated projection contain the literal text 'germ cells [1. It promotes'. The open bracket and numeric fragment do not form a complete citation. The later PUB00096701 markers occur on other assertions and do not identify what was intended at the damaged fragment. The malformed text is directly observed; its intended citation and the scientific support for the associated statement remain unverified. Exact projection-to-row agreement preserves rather than resolves the wording issue.

## Findings

### incomplete-citation-fragment: Verify the incomplete imported citation fragment

minor / open / provisional; issue key: pf15162-imported-incomplete-citation-fragment.

Both the frozen row and generated projection contain the literal text 'germ cells [1. It promotes'. The open bracket and numeric fragment do not form a complete citation. The later PUB00096701 markers occur on other assertions and do not identify what was intended at the damaged fragment. The malformed text is directly observed; its intended citation and the scientific support for the associated statement remain unverified.

## Recommended Actions And Acceptance Checks

### verify-incomplete-citation-fragment

Verify the incomplete imported citation fragment using dated authoritative evidence before proposing a maintained correction or explicit qualification.

- Retain dated authoritative evidence for the imported statement and its intended representation.
- Resolve or explicitly qualify the incomplete citation using dated authoritative source evidence; do not infer the intended reference merely from nearby PUB00096701 markers.
- If supported, apply the clarification through maintained source/overlay/history owners and retain a scoped follow-up under the same issue key; preserve this frozen snapshot and review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF15162.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF15162 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF15162; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 489 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF15162 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf15162 | data/families/PF15162.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

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
  - path: data/families/PF15162.yaml
    role: target
    sha256: 629773dc7f13ce336f1b3b9b7fed86d3b4488c6fc8a02ddfbd55c7287ddc5270
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
  label: PF15162
  owner_paths:
  - path: curation/families/PF15162.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF15162.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: 16c7e1482a9001167d027059faa4247a4b735e7dd28392e8e568da12a104a34b
  target_id: PF15162
schema_version: 1.0.0
review_id: 20261101T220624Z-pf15162-seed-record-review
title: 'PF15162 SCRE: seed identity, provenance and evidence-scope review'
started_at: '2026-11-01T22:00:40Z'
finished_at: '2026-11-01T22:06:24Z'
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
summary: 'PF15162 (SCRE; InterPro:IPR027857) matches the verified frozen source and
  retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED.
  SCRE (IPR027857) retains SPO16/SCRE identity, mammalian-yeast orthology context,
  synaptonemal-complex reinforcement, SHOC1 association and TEX11/MSH4 localization
  statements. Both source surfaces contain the incomplete citation fragment germ cells
  [1.; later PUB00096701 markers do not resolve that fragment. All seven counters
  agree between row and projection: 556 proteins, 558 matches, 477 proteomes, 1717
  taxa, 0 structures, 485 models, 5 architectures. Verify the incomplete imported
  citation fragment. This is a minor source-text representation follow-up; no missing
  citation, identifier correction or coordinate is asserted.'
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: aa7d08bcf3a9a03879d06cffd075bc083d29788f. The corpus has 8296
    records; 4111 were covered and 4185 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF15162.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF15162
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF15162
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF15162
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-398-attempt-001/PF15162-targets.yaml
    --input data/families/PF15162.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF15162
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-398-attempt-001/prepare.py
    PF15162
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF15162
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
  - PF15162
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
  - PF15162
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
  - PF15162
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF15162.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-11-01T22:06:24Z'
  support: supports
  summary: Read the complete PF15162 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: 629773dc7f13ce336f1b3b9b7fed86d3b4488c6fc8a02ddfbd55c7287ddc5270
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF15162; companion manifest and TSV; native verified inspection
  accessed_at: '2026-11-01T22:06:24Z'
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
  accessed_at: '2026-11-01T22:06:24Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-11-01T22:06:24Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 489 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF15162
  accessed_at: '2026-11-01T22:06:24Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF15162. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf15162
  kind: record_content
  reference: data/families/PF15162.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-11-01T22:06:24Z'
  support: context_only
  snapshot_sha256: 629773dc7f13ce336f1b3b9b7fed86d3b4488c6fc8a02ddfbd55c7287ddc5270
  quote: "id: Pfam:PF15162\npfam_id: PF15162\nname: Protein SPO16 homolog\nshort_name:\
    \ SCRE\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF15162\n\
    counters:\n  proteins: 556\n  matches: 558\n  proteomes: 477\n  taxa: 1717\n \
    \ structures: 0\n  alphafold_models: 485\n  domain_architectures: 5\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR027857\ndescription: This entry represents the Protein\
    \ SPO16 homolog (SPO16, also known as Synaptonemal complex\n  reinforcing element\
    \ SCRE), including the mammalian orthologue of budding yeast Spo16. It plays a\
    \ key\n  role in reinforcing the integrity of the central element of the synaptonemal\
    \ complex (SC), resulting\n  in the SC stabilization which ensures the progression\
    \ of meiotic prophase I in male and female germ\n  cells [1. It promotes homologous\
    \ recombination and crossing-over in meiotic prophase I via its association\n\
    \  with SHOC1 [[cite:PUB00096701]]. It is also required for the localization of\
    \ TEX11 and MSH4 to recombination\n  intermediates [[cite:PUB00096701]].\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF15162, id=Pfam:PF15162, short_name=SCRE, name=Protein
    SPO16 homolog, source URL and InterPro accession InterPro:IPR027857 agree with
    the selected frozen row. This establishes frozen identity correspondence, not
    current upstream taxonomy or function.
  target_ids:
  - PF15162
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 556 proteins, 558 matches, 0 structure entries and 485
    AlphaFold models are frozen database counters, not independent experiments. Raw
    input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF15162
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: 'SCRE (IPR027857) retains SPO16/SCRE identity, mammalian-yeast orthology
    context, synaptonemal-complex reinforcement, SHOC1 association and TEX11/MSH4
    localization statements. Both source surfaces contain the incomplete citation
    fragment germ cells [1.; later PUB00096701 markers do not resolve that fragment.
    All seven counters agree between row and projection: 556 proteins, 558 matches,
    477 proteomes, 1717 taxa, 0 structures, 485 models, 5 architectures.'
  target_ids:
  - PF15162
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
  summary: Metadata-only source and captured-context review. Preserve EX_DUF SCRE/SPO16
    and distinguish source-reported synaptonemal-complex reinforcement, SHOC1 association
    and TEX11/MSH4 localization from direct recombination catalysis or partner-function
    transfer. The literal germ cells [1. fragment is malformed in both the projection
    and frozen row, making that local citation incomplete. This is a confirmed bounded
    citation-representation defect requiring follow-up; do not infer its missing source
    from the later PUB00096701 markers or alter the frozen row. No primary paper,
    structure or any of 485 models was inspected.
  target_ids:
  - PF15162
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: The captured literal PF15162 and SCRE searches under curation/families,
    evidence and history included hidden and ignored files. No accession hit or path
    hit was found; the one SCRE content hit is the substring in DISCREPANCIES at evidence/PF01901/sheng-2024.txt
    line 22, not a SCRE assertion. The exact canonical overlay, evidence and history
    owners were absent. These bounded results do not establish absence for historical
    or organism aliases or wider literature. No primary paper, live upstream record,
    structural model or assay was inspected. A biological or historical assessment
    needs separately verified evidence and tested-protein scope. No accession-named
    overlay, evidence or history path was found by the bounded hidden/ignored-inclusive
    inventory; the inspected projection has no curated claim payload. Optional-field
    absence is not a seed-schema defect.
  target_ids:
  - PF15162
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
  - PF15162
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: Verify and clarify imported source metadata through the maintained upstream-source
    review and freeze workflow. Any evidence-backed local correction belongs in curation/families/PF15162.yaml
    with licensed evidence and actual canonical history, followed by normal projection
    generation. Do not hand-edit the frozen snapshot or generated projection. This
    review records verification work only; no source, overlay or history edit is made.
  target_ids:
  - PF15162
  evidence_ids:
  - profile
  - record
  - validation
- assessment_id: incomplete-citation-fragment-assessment
  area: completeness
  topic: Verify the incomplete imported citation fragment
  outcome: concern
  summary: Both the frozen row and generated projection contain the literal text 'germ
    cells [1. It promotes'. The open bracket and numeric fragment do not form a complete
    citation. The later PUB00096701 markers occur on other assertions and do not identify
    what was intended at the damaged fragment. The malformed text is directly observed;
    its intended citation and the scientific support for the associated statement
    remain unverified. Exact projection-to-row agreement preserves rather than resolves
    the wording issue.
  target_ids:
  - PF15162
  evidence_ids:
  - record
  - snapshot
findings:
- finding_id: incomplete-citation-fragment
  issue_key: pf15162-imported-incomplete-citation-fragment
  category: completeness
  severity: minor
  status: open
  certainty: provisional
  title: Verify the incomplete imported citation fragment
  description: Both the frozen row and generated projection contain the literal text
    'germ cells [1. It promotes'. The open bracket and numeric fragment do not form
    a complete citation. The later PUB00096701 markers occur on other assertions and
    do not identify what was intended at the damaged fragment. The malformed text
    is directly observed; its intended citation and the scientific support for the
    associated statement remain unverified.
  target_ids:
  - PF15162
  field_paths:
  - description
  evidence_ids:
  - record
  - snapshot
  normalization_reason: Minor bounded source-text representation issue. Frozen identity
    and projection correspondence remain intact; no missing source or biological correction
    is guessed.
  ownership_note: Verify and clarify imported source metadata through the maintained
    upstream-source review and freeze workflow. Any evidence-backed local correction
    belongs in curation/families/PF15162.yaml with licensed evidence and actual canonical
    history, followed by normal projection generation. Do not hand-edit the frozen
    snapshot or generated projection.
actions:
- action_id: verify-incomplete-citation-fragment
  description: Verify the incomplete imported citation fragment using dated authoritative
    evidence before proposing a maintained correction or explicit qualification.
  finding_ids:
  - incomplete-citation-fragment
  target_ids:
  - PF15162
  ownership_note: Verify and clarify imported source metadata through the maintained
    upstream-source review and freeze workflow. Any evidence-backed local correction
    belongs in curation/families/PF15162.yaml with licensed evidence and actual canonical
    history, followed by normal projection generation. Do not hand-edit the frozen
    snapshot or generated projection.
  acceptance_checks:
  - Retain dated authoritative evidence for the imported statement and its intended
    representation.
  - Resolve or explicitly qualify the incomplete citation using dated authoritative
    source evidence; do not infer the intended reference merely from nearby PUB00096701
    markers.
  - If supported, apply the clarification through maintained source/overlay/history
    owners and retain a scoped follow-up under the same issue key; preserve this frozen
    snapshot and review.
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
