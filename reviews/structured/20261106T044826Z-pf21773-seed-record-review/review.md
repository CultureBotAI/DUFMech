# PF21773 ODAD1_CC: seed identity, provenance and evidence-scope review

- Review: 20261106T044826Z-pf21773-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-11-06T04:35:12Z
- Finished UTC: 2026-11-06T04:48:26Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

PF21773 (ODAD1_CC; InterPro:IPR049258) matches the verified frozen source and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED. The pinned InterPro/Pfam snapshot identifies PF21773 (ODAD1_CC; InterPro:IPR049258) as EX_DUF, with local characterization UNSCORED and curation SEEDED. The complete imported description is: This domain, previously know as DUF6872, is found in Outer dynein arm-docking complex subunit 1 (ODAD1, CCDC114) from humans and similar eukaryotic proteins. In mammals, CCDC114 forms a hetero-coiled coil with ODAD1/CCDC151 within the A07/A08 interprotofilament cleft, analogous to the DC1/2 coiled coil of the trimeric ODA-DC observed in C. reinhardtii axoneme [[cite:PUB00152762],[cite:PUB00100771]]. DC2 is a homolog of the human ODAD1/CCDC151 and in C.reinhardtii it is a part of the ODA-DC that consists of three proteins: DC1, DC2, and DC3. The N-terminal halves of DC1 and DC2 form a microtubule-bound heteromeric coiled-coil [[cite:PUB00152762],[cite:PUB00152763]]. Frozen metadata report 3489 proteins, 3740 matches, 1307 proteomes, 4258 taxa, 13 structure entries, 3002 AlphaFold models and 65 domain architectures. These are source counters; no protein, sequence, structure, model or underlying publication was inspected. This is a local metadata and representation review, not external biological verification. One minor source-representation follow-up concerns the ambiguous ODAD1/CCDC114 and ODAD1/CCDC151 partner/homolog references. It does not establish false biology, a corrected alias or an experimentally characterized function for the isolated central region.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: 5642a645349854802748ae387c0e2df121c5e83f. The corpus has 8296 records; 6241 were covered and 2055 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF21773.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5642a645349854802748ae387c0e2df121c5e83f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF21773 | data/families/PF21773.yaml | generated | PF21773 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF21773 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF21773 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF21773 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF21773 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF21773 | 489 valid canonical history records. |
| Generated schema check | passed | True | PF21773 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF21773.

The filename, pfam_id=PF21773, id=Pfam:PF21773, short_name=ODAD1_CC, name=ODAD1 central coiled coil region, source URL and InterPro accession InterPro:IPR049258 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF21773.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 3489 proteins, 3740 matches, 13 structure entries and 3002 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF21773.

The pinned InterPro/Pfam snapshot identifies PF21773 (ODAD1_CC; InterPro:IPR049258) as EX_DUF, with local characterization UNSCORED and curation SEEDED. The complete imported description is: This domain, previously know as DUF6872, is found in Outer dynein arm-docking complex subunit 1 (ODAD1, CCDC114) from humans and similar eukaryotic proteins. In mammals, CCDC114 forms a hetero-coiled coil with ODAD1/CCDC151 within the A07/A08 interprotofilament cleft, analogous to the DC1/2 coiled coil of the trimeric ODA-DC observed in C. reinhardtii axoneme [[cite:PUB00152762],[cite:PUB00100771]]. DC2 is a homolog of the human ODAD1/CCDC151 and in C.reinhardtii it is a part of the ODA-DC that consists of three proteins: DC1, DC2, and DC3. The N-terminal halves of DC1 and DC2 form a microtubule-bound heteromeric coiled-coil [[cite:PUB00152762],[cite:PUB00152763]]. Frozen metadata report 3489 proteins, 3740 matches, 1307 proteomes, 4258 taxa, 13 structure entries, 3002 AlphaFold models and 65 domain architectures. These are source counters; no protein, sequence, structure, model or underlying publication was inspected. This is a local metadata and representation review, not external biological verification.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF21773.

The selected object is a central coiled-coil region of proteins described as ODAD1/CCDC114. Mammalian A07/A08-cleft placement, the algal DC1/DC2/DC3 complex and N-terminal halves of DC1/DC2 are separate imported contexts. The text subsequently uses ODAD1/CCDC151 for the partner and DC2 homolog, creating a naming/referent ambiguity requiring verification. Do not infer corrected aliases, universal trimeric stoichiometry or equivalence of the selected central region and the stated N-terminal halves.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF21773.

The immediate follow-up is to verify which proteins the ODAD1/CCDC114 and ODAD1/CCDC151 expressions denote in the cited annotation, without guessing a corrected name. Biological reassessment additionally needs species-specific partner identities, central versus N-terminal boundaries and the experimental basis for the complex architecture. The proposed needs_curation disposition is limited to the ambiguous representation; it does not assert false biology or authorize a source edit. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF21773.

seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED express separate states. EX_DUF records historical renaming and is compatible with imported functional descriptions; it is not evidence that all members were tested. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF21773.

The proposed task is a bounded naming/provenance check. Preserve the immutable worklist and generated projection. Any source-supported naming clarification belongs in curation/families/PF21773.yaml with appropriately licensed evidence and canonical history, followed by normal generation and validation. This review does not authorize that edit.

### Ambiguous ODAD1 partner and homolog references

consistency: concern. Targets: PF21773.

The imported description uses ODAD1 with CCDC114 initially and with CCDC151 in subsequent partner and DC2-homolog statements. Verify the intended names against the annotation and cited source before any maintained clarification. No replacement identity is inferred, and the unexamined structural and species-specific claims remain qualified.

## Findings

### PF21773-ambiguous-odad1-referent: Verify the ODAD1 partner and homolog names

minor / open / provisional; issue key: PF21773-odad1-partner-naming.

The frozen description and projection first identify ODAD1 as CCDC114, then say CCDC114 forms a hetero-coiled coil with ODAD1/CCDC151 and describe DC2 as a homolog of human ODAD1/CCDC151. Reusing ODAD1 for these different named referents leaves the intended partner and homolog assignment ambiguous within the text. Verify the annotation and cited source before clarifying the names; no corrected gene, alias, partner identity or biological falsity has been established by this local review.

## Recommended Actions And Acceptance Checks

### PF21773-verify-odad1-referents

Check the original annotation and cited evidence to establish which named proteins are intended by ODAD1/CCDC114 and ODAD1/CCDC151 in the partner and DC2-homolog statements before proposing any maintained-overlay clarification.

- Retain the exact original ODAD1/CCDC114 and ODAD1/CCDC151 wording as provenance and resolve both the partner and homolog referents with source support.
- Do not guess a replacement gene or alias, silently rewrite the frozen description, or claim that the reported structure or interaction was independently validated.
- Preserve mammalian versus C. reinhardtii scope, central versus N-terminal regions, and UNSCORED/SEEDED status.
- If clarification is later authorized and source-supported, use the maintained overlay with evidence and canonical history, then regenerate and validate normally.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF21773.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF21773 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF21773; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 489 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF21773 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf21773 | data/families/PF21773.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

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
  git_revision: 5642a645349854802748ae387c0e2df121c5e83f
  inputs:
  - path: data/families/PF21773.yaml
    role: target
    sha256: 653d1187ff4c20637f3e768aff67d041e3b302a7adb877798e2241b14453e1ab
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
  label: PF21773
  owner_paths:
  - path: curation/families/PF21773.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF21773.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: cacfe0ddd6b7cde4b807769b10e7bc0520d1941bfcb2682fc8fb8ddc713306ad
  target_id: PF21773
schema_version: 1.0.0
review_id: 20261106T044826Z-pf21773-seed-record-review
title: 'PF21773 ODAD1_CC: seed identity, provenance and evidence-scope review'
started_at: '2026-11-06T04:35:12Z'
finished_at: '2026-11-06T04:48:26Z'
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
summary: 'PF21773 (ODAD1_CC; InterPro:IPR049258) matches the verified frozen source
  and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED.
  The pinned InterPro/Pfam snapshot identifies PF21773 (ODAD1_CC; InterPro:IPR049258)
  as EX_DUF, with local characterization UNSCORED and curation SEEDED. The complete
  imported description is: This domain, previously know as DUF6872, is found in Outer
  dynein arm-docking complex subunit 1 (ODAD1, CCDC114) from humans and similar eukaryotic
  proteins. In mammals, CCDC114 forms a hetero-coiled coil with ODAD1/CCDC151 within
  the A07/A08 interprotofilament cleft, analogous to the DC1/2 coiled coil of the
  trimeric ODA-DC observed in C. reinhardtii axoneme [[cite:PUB00152762],[cite:PUB00100771]].
  DC2 is a homolog of the human ODAD1/CCDC151 and in C.reinhardtii it is a part of
  the ODA-DC that consists of three proteins: DC1, DC2, and DC3. The N-terminal halves
  of DC1 and DC2 form a microtubule-bound heteromeric coiled-coil [[cite:PUB00152762],[cite:PUB00152763]].
  Frozen metadata report 3489 proteins, 3740 matches, 1307 proteomes, 4258 taxa, 13
  structure entries, 3002 AlphaFold models and 65 domain architectures. These are
  source counters; no protein, sequence, structure, model or underlying publication
  was inspected. This is a local metadata and representation review, not external
  biological verification. One minor source-representation follow-up concerns the
  ambiguous ODAD1/CCDC114 and ODAD1/CCDC151 partner/homolog references. It does not
  establish false biology, a corrected alias or an experimentally characterized function
  for the isolated central region.'
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: 5642a645349854802748ae387c0e2df121c5e83f. The corpus has 8296
    records; 6241 were covered and 2055 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF21773.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF21773
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF21773
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF21773
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-611-attempt-001/PF21773-targets.yaml
    --input data/families/PF21773.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF21773
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-611-attempt-001/prepare.py
    PF21773
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF21773
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
  - PF21773
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
  - PF21773
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
  - PF21773
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF21773.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-11-06T04:48:26Z'
  support: supports
  summary: Read the complete PF21773 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: 653d1187ff4c20637f3e768aff67d041e3b302a7adb877798e2241b14453e1ab
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF21773; companion manifest and TSV; native verified inspection
  accessed_at: '2026-11-06T04:48:26Z'
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
  accessed_at: '2026-11-06T04:48:26Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-11-06T04:48:26Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 489 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF21773
  accessed_at: '2026-11-06T04:48:26Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF21773. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf21773
  kind: record_content
  reference: data/families/PF21773.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-11-06T04:48:26Z'
  support: context_only
  snapshot_sha256: 653d1187ff4c20637f3e768aff67d041e3b302a7adb877798e2241b14453e1ab
  quote: "id: Pfam:PF21773\npfam_id: PF21773\nname: ODAD1 central coiled coil region\n\
    short_name: ODAD1_CC\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF21773\n\
    counters:\n  proteins: 3489\n  matches: 3740\n  proteomes: 1307\n  taxa: 4258\n\
    \  structures: 13\n  alphafold_models: 3002\n  domain_architectures: 65\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR049258\ndescription: 'This domain, previously know as\
    \ DUF6872, is found in Outer dynein arm-docking complex subunit\n  1 (ODAD1, CCDC114)\
    \ from humans and similar eukaryotic proteins. In mammals, CCDC114 forms a hetero-coiled\n\
    \  coil with ODAD1/CCDC151 within the A07/A08 interprotofilament cleft, analogous\
    \ to the DC1/2 coiled coil\n  of the trimeric ODA-DC observed in C. reinhardtii\
    \ axoneme [[cite:PUB00152762],[cite:PUB00100771]]. DC2\n  is a homolog of the\
    \ human ODAD1/CCDC151 and in C.reinhardtii it is a part of the ODA-DC that consists\n\
    \  of three proteins: DC1, DC2, and DC3. The N-terminal halves of DC1 and DC2\
    \ form a microtubule-bound\n  heteromeric coiled-coil [[cite:PUB00152762],[cite:PUB00152763]].'\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF21773, id=Pfam:PF21773, short_name=ODAD1_CC, name=ODAD1
    central coiled coil region, source URL and InterPro accession InterPro:IPR049258
    agree with the selected frozen row. This establishes frozen identity correspondence,
    not current upstream taxonomy or function.
  target_ids:
  - PF21773
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 3489 proteins, 3740 matches, 13 structure entries and
    3002 AlphaFold models are frozen database counters, not independent experiments.
    Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF21773
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: 'The pinned InterPro/Pfam snapshot identifies PF21773 (ODAD1_CC; InterPro:IPR049258)
    as EX_DUF, with local characterization UNSCORED and curation SEEDED. The complete
    imported description is: This domain, previously know as DUF6872, is found in
    Outer dynein arm-docking complex subunit 1 (ODAD1, CCDC114) from humans and similar
    eukaryotic proteins. In mammals, CCDC114 forms a hetero-coiled coil with ODAD1/CCDC151
    within the A07/A08 interprotofilament cleft, analogous to the DC1/2 coiled coil
    of the trimeric ODA-DC observed in C. reinhardtii axoneme [[cite:PUB00152762],[cite:PUB00100771]].
    DC2 is a homolog of the human ODAD1/CCDC151 and in C.reinhardtii it is a part
    of the ODA-DC that consists of three proteins: DC1, DC2, and DC3. The N-terminal
    halves of DC1 and DC2 form a microtubule-bound heteromeric coiled-coil [[cite:PUB00152762],[cite:PUB00152763]].
    Frozen metadata report 3489 proteins, 3740 matches, 1307 proteomes, 4258 taxa,
    13 structure entries, 3002 AlphaFold models and 65 domain architectures. These
    are source counters; no protein, sequence, structure, model or underlying publication
    was inspected. This is a local metadata and representation review, not external
    biological verification.'
  target_ids:
  - PF21773
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
  summary: The selected object is a central coiled-coil region of proteins described
    as ODAD1/CCDC114. Mammalian A07/A08-cleft placement, the algal DC1/DC2/DC3 complex
    and N-terminal halves of DC1/DC2 are separate imported contexts. The text subsequently
    uses ODAD1/CCDC151 for the partner and DC2 homolog, creating a naming/referent
    ambiguity requiring verification. Do not infer corrected aliases, universal trimeric
    stoichiometry or equivalence of the selected central region and the stated N-terminal
    halves.
  target_ids:
  - PF21773
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: The immediate follow-up is to verify which proteins the ODAD1/CCDC114 and
    ODAD1/CCDC151 expressions denote in the cited annotation, without guessing a corrected
    name. Biological reassessment additionally needs species-specific partner identities,
    central versus N-terminal boundaries and the experimental basis for the complex
    architecture. The proposed needs_curation disposition is limited to the ambiguous
    representation; it does not assert false biology or authorize a source edit. No
    accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive
    inventory; the inspected projection has no curated claim payload. Optional-field
    absence is not a seed-schema defect.
  target_ids:
  - PF21773
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
  - PF21773
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: The proposed task is a bounded naming/provenance check. Preserve the immutable
    worklist and generated projection. Any source-supported naming clarification belongs
    in curation/families/PF21773.yaml with appropriately licensed evidence and canonical
    history, followed by normal generation and validation. This review does not authorize
    that edit.
  target_ids:
  - PF21773
  evidence_ids:
  - profile
  - record
  - validation
- assessment_id: protein-name-representation
  area: consistency
  topic: Ambiguous ODAD1 partner and homolog references
  outcome: concern
  summary: The imported description uses ODAD1 with CCDC114 initially and with CCDC151
    in subsequent partner and DC2-homolog statements. Verify the intended names against
    the annotation and cited source before any maintained clarification. No replacement
    identity is inferred, and the unexamined structural and species-specific claims
    remain qualified.
  target_ids:
  - PF21773
  evidence_ids:
  - record
  - snapshot
findings:
- finding_id: PF21773-ambiguous-odad1-referent
  issue_key: PF21773-odad1-partner-naming
  category: consistency
  severity: minor
  status: open
  certainty: provisional
  title: Verify the ODAD1 partner and homolog names
  description: The frozen description and projection first identify ODAD1 as CCDC114,
    then say CCDC114 forms a hetero-coiled coil with ODAD1/CCDC151 and describe DC2
    as a homolog of human ODAD1/CCDC151. Reusing ODAD1 for these different named referents
    leaves the intended partner and homolog assignment ambiguous within the text.
    Verify the annotation and cited source before clarifying the names; no corrected
    gene, alias, partner identity or biological falsity has been established by this
    local review.
  target_ids:
  - PF21773
  field_paths:
  - description
  evidence_ids:
  - record
  - snapshot
  normalization_reason: One bounded source-representation task groups the partner
    and homolog uses of the same ambiguous alias. Unverified structural claims, species
    transfer and domain scope are limitations rather than additional findings.
  ownership_note: Preserve the immutable worklist and generated projection. Any source-supported
    naming clarification belongs in curation/families/PF21773.yaml with appropriately
    licensed evidence and canonical history, followed by normal generation and validation.
    This review does not authorize that edit.
actions:
- action_id: PF21773-verify-odad1-referents
  description: Check the original annotation and cited evidence to establish which
    named proteins are intended by ODAD1/CCDC114 and ODAD1/CCDC151 in the partner
    and DC2-homolog statements before proposing any maintained-overlay clarification.
  finding_ids:
  - PF21773-ambiguous-odad1-referent
  target_ids:
  - PF21773
  ownership_note: Preserve the immutable worklist and generated projection. Any source-supported
    naming clarification belongs in curation/families/PF21773.yaml with appropriately
    licensed evidence and canonical history, followed by normal generation and validation.
    This review does not authorize that edit.
  acceptance_checks:
  - Retain the exact original ODAD1/CCDC114 and ODAD1/CCDC151 wording as provenance
    and resolve both the partner and homolog referents with source support.
  - Do not guess a replacement gene or alias, silently rewrite the frozen description,
    or claim that the reported structure or interaction was independently validated.
  - Preserve mammalian versus C. reinhardtii scope, central versus N-terminal regions,
    and UNSCORED/SEEDED status.
  - If clarification is later authorized and source-supported, use the maintained
    overlay with evidence and canonical history, then regenerate and validate normally.
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
