# PF08962 Rv2632c-like: seed identity, provenance and evidence-scope review

- Review: 20261022T103639Z-pf08962-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-22T10:24:56Z
- Finished UTC: 2026-10-22T10:36:39Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

PF08962 (Rv2632c-like; InterPro:IPR015057) matches the verified frozen source and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED. Rv2632c-like retains PF08962/IPR015057 and EX_DUF. The complete source names Rv2632c repeatedly, supplies a structural locator, then introduces Rv1738 in a sentence linked by "Based on this structure", with one publication token. The source does not explicitly explain the relationship between the two named proteins; neither identifier, structure nor publication was scientifically assessed. One minor local representation finding remains open: the transition from Rv2632c to Rv1738 is not explicitly explained. No biological naming correction or identity equivalence is selected, and the scientific account remains unassessed.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: 2b49c8729090bbbcbdaa956f770eee0aff153723. The corpus has 8296 records; 1681 were covered and 6615 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF08962.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2b49c8729090bbbcbdaa956f770eee0aff153723.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF08962 | data/families/PF08962.yaml | generated | PF08962 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF08962 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF08962 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF08962 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF08962 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF08962 | 438 valid canonical history records. |
| Generated schema check | passed | True | PF08962 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF08962.

The filename, pfam_id=PF08962, id=Pfam:PF08962, short_name=Rv2632c-like, name=Rv2632c-like, source URL and InterPro accession InterPro:IPR015057 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF08962.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 2482 proteins, 2482 matches, 3 structure entries and 1265 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF08962.

Rv2632c-like retains PF08962/IPR015057 and EX_DUF. The complete source names Rv2632c repeatedly, supplies a structural locator, then introduces Rv1738 in a sentence linked by "Based on this structure", with one publication token. The source does not explicitly explain the relationship between the two named proteins; neither identifier, structure nor publication was scientifically assessed.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF08962.

Review is strictly non-operational identity, provenance and attribution. The later grammatical subject is explicitly Rv1738, but its relationship to the preceding Rv2632c account is unstated. A minor local attribution finding identifies that transition without treating either name as wrong, equivalent or biologically corrected. No organism-level, functional, structural-design, sequence or experimental interpretation is added.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF08962.

The relationship between the named proteins and the source-context transition needs attributable clarification. If that relationship cannot be recovered, the finding remains unresolved. Three structures, 1265 models and seven architectures do not resolve the attribution or validate the imported scientific account. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF08962.

seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED express separate states. EX_DUF records historical renaming and is compatible with imported functional descriptions; it is not evidence that all members were tested. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF08962.

Source-backed attribution clarification belongs in the maintained PF08962 overlay or a separately authorized successor source freeze. The generated projection and frozen row remain unchanged. Later curation requires actual canonical history and native validation; this action is proposed, not performed.

### Relationship between successive named-protein accounts

representation: concern. Targets: PF08962.

The description moves from repeated Rv2632c attribution to Rv1738 using a backward source-context reference without explaining their relationship. The later grammatical subject is clear; the relationship and attribution transition remain unstated. Neither name is identified as biologically incorrect.

## Findings

### rv2632c-rv1738-attribution-transition: Clarify the transition between Rv2632c and Rv1738 attribution

minor / open / confirmed; issue key: pf08962-rv2632c-rv1738-attribution-transition.

The complete projection and unique frozen row repeatedly name Rv2632c before a sentence naming Rv1738 and referring backward with "Based on this structure". The selected text does not explicitly explain the relationship between those names. An intentional inference concerning a distinct protein is possible but is not explained locally. This is a bounded attribution concern, not a claim that either name is wrong, that the names are equivalent, or that the biological account is false.

## Recommended Actions And Acceptance Checks

### clarify-rv2632c-rv1738-attribution-transition

In separately authorized curation, examine attributable identifier and source context, then explain the relationship or transition between the two named-protein accounts without adding operational biological interpretation.

- Retain an attributable explanation of the two-name relationship and source-context transition, preserving citations and qualifications. Do not choose a biological correction or assert identity equivalence from this text alone.
- If the relationship cannot be established, document the bounded source search and keep the finding unresolved; documenting uncertainty alone does not resolve the attribution gap.
- Keep selected family, each named protein and broader context distinct. Add no functional, organism-level, structural-design, sequence or experimental interpretation. Use maintained inputs or a separately authorized successor freeze, without hand-editing generated projections or immutable rows.
- Any later curation must retain actual canonical history and pass record/history/review checks; any finding disposition must cite this observation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF08962.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF08962 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF08962; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 438 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF08962 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf08962 | data/families/PF08962.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

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
  git_revision: 2b49c8729090bbbcbdaa956f770eee0aff153723
  inputs:
  - path: data/families/PF08962.yaml
    role: target
    sha256: f1d74ca228a9cb715ca9651a5fdb1d7c3fde2a1927b35e1390beefc364df6af9
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
  label: PF08962
  owner_paths:
  - path: curation/families/PF08962.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF08962.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: d009217278cfa3397fe70db5c2fcce1afcc6df29aa48b18dd579115b6116ff6f
  target_id: PF08962
schema_version: 1.0.0
review_id: 20261022T103639Z-pf08962-seed-record-review
title: 'PF08962 Rv2632c-like: seed identity, provenance and evidence-scope review'
started_at: '2026-10-22T10:24:56Z'
finished_at: '2026-10-22T10:36:39Z'
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
summary: 'PF08962 (Rv2632c-like; InterPro:IPR015057) matches the verified frozen source
  and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED.
  Rv2632c-like retains PF08962/IPR015057 and EX_DUF. The complete source names Rv2632c
  repeatedly, supplies a structural locator, then introduces Rv1738 in a sentence
  linked by "Based on this structure", with one publication token. The source does
  not explicitly explain the relationship between the two named proteins; neither
  identifier, structure nor publication was scientifically assessed. One minor local
  representation finding remains open: the transition from Rv2632c to Rv1738 is not
  explicitly explained. No biological naming correction or identity equivalence is
  selected, and the scientific account remains unassessed.'
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: 2b49c8729090bbbcbdaa956f770eee0aff153723. The corpus has 8296
    records; 1681 were covered and 6615 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF08962.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF08962
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF08962
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF08962
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-155/PF08962-targets.yaml
    --input data/families/PF08962.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF08962
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-155/prepare.py
    PF08962
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF08962
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
  - PF08962
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
  summary: 438 valid canonical history records.
  target_ids:
  - PF08962
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
  - PF08962
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF08962.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-10-22T10:36:39Z'
  support: supports
  summary: Read the complete PF08962 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: f1d74ca228a9cb715ca9651a5fdb1d7c3fde2a1927b35e1390beefc364df6af9
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF08962; companion manifest and TSV; native verified inspection
  accessed_at: '2026-10-22T10:36:39Z'
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
  accessed_at: '2026-10-22T10:36:39Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-10-22T10:36:39Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 438 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF08962
  accessed_at: '2026-10-22T10:36:39Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF08962. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf08962
  kind: record_content
  reference: data/families/PF08962.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-22T10:36:39Z'
  support: context_only
  snapshot_sha256: f1d74ca228a9cb715ca9651a5fdb1d7c3fde2a1927b35e1390beefc364df6af9
  quote: "id: Pfam:PF08962\npfam_id: PF08962\nname: Rv2632c-like\nshort_name: Rv2632c-like\n\
    seed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status: SEEDED\n\
    source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF08962\ncounters:\n\
    \  proteins: 2482\n  matches: 2482\n  proteomes: 1537\n  taxa: 1847\n  structures:\
    \ 3\n  alphafold_models: 1265\n  domain_architectures: 7\nprovenance:\n  snapshot_id:\
    \ interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR015057\ndescription: This entry includes a set of Actinobacterial\
    \ proteins, including Rv2632c from Mycobacterium\n  tuberculosis that is strongly\
    \ implicated in the onset of non-replicating persistence, and thereby latent\n\
    \  tuberculosis. Rv2632c contains a dsRBD-like (2 layers alpha/beta) fold (PDBe:2fgg).\
    \ It shares remarkable\n  similarity with bacterial hibernation factors, despite\
    \ very low sequence similarity. Based on this structure\n  it was predicted that\
    \ Rv1738, highly up-regulated in conditions that mimic the onset of persistence,\n\
    \  helps trigger dormancy by association with the bacterial ribosome [[cite:PUB00097447]].\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF08962, id=Pfam:PF08962, short_name=Rv2632c-like,
    name=Rv2632c-like, source URL and InterPro accession InterPro:IPR015057 agree
    with the selected frozen row. This establishes frozen identity correspondence,
    not current upstream taxonomy or function.
  target_ids:
  - PF08962
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 2482 proteins, 2482 matches, 3 structure entries and
    1265 AlphaFold models are frozen database counters, not independent experiments.
    Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF08962
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: Rv2632c-like retains PF08962/IPR015057 and EX_DUF. The complete source
    names Rv2632c repeatedly, supplies a structural locator, then introduces Rv1738
    in a sentence linked by "Based on this structure", with one publication token.
    The source does not explicitly explain the relationship between the two named
    proteins; neither identifier, structure nor publication was scientifically assessed.
  target_ids:
  - PF08962
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
  summary: Review is strictly non-operational identity, provenance and attribution.
    The later grammatical subject is explicitly Rv1738, but its relationship to the
    preceding Rv2632c account is unstated. A minor local attribution finding identifies
    that transition without treating either name as wrong, equivalent or biologically
    corrected. No organism-level, functional, structural-design, sequence or experimental
    interpretation is added.
  target_ids:
  - PF08962
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: The relationship between the named proteins and the source-context transition
    needs attributable clarification. If that relationship cannot be recovered, the
    finding remains unresolved. Three structures, 1265 models and seven architectures
    do not resolve the attribution or validate the imported scientific account. No
    accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive
    inventory; the inspected projection has no curated claim payload. Optional-field
    absence is not a seed-schema defect.
  target_ids:
  - PF08962
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
  - PF08962
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: Source-backed attribution clarification belongs in the maintained PF08962
    overlay or a separately authorized successor source freeze. The generated projection
    and frozen row remain unchanged. Later curation requires actual canonical history
    and native validation; this action is proposed, not performed.
  target_ids:
  - PF08962
  evidence_ids:
  - profile
  - record
  - validation
- assessment_id: rv2632c-rv1738-attribution-transition
  area: representation
  topic: Relationship between successive named-protein accounts
  outcome: concern
  summary: The description moves from repeated Rv2632c attribution to Rv1738 using
    a backward source-context reference without explaining their relationship. The
    later grammatical subject is clear; the relationship and attribution transition
    remain unstated. Neither name is identified as biologically incorrect.
  target_ids:
  - PF08962
  evidence_ids:
  - record
  - snapshot
findings:
- finding_id: rv2632c-rv1738-attribution-transition
  issue_key: pf08962-rv2632c-rv1738-attribution-transition
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Clarify the transition between Rv2632c and Rv1738 attribution
  description: The complete projection and unique frozen row repeatedly name Rv2632c
    before a sentence naming Rv1738 and referring backward with "Based on this structure".
    The selected text does not explicitly explain the relationship between those names.
    An intentional inference concerning a distinct protein is possible but is not
    explained locally. This is a bounded attribution concern, not a claim that either
    name is wrong, that the names are equivalent, or that the biological account is
    false.
  target_ids:
  - PF08962
  field_paths:
  - description
  evidence_ids:
  - record
  - snapshot
  normalization_reason: Minor captures the unexplained local attribution transition
    while stable family identity, required fields and frozen-source fidelity remain
    intact. Scientific validity and identifier equivalence were not assessed.
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF08962.yaml
    role: Future maintained source-backed attribution clarification; this review does
      not create an overlay.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: Workflow for a separately authorized successor source freeze; no generator
      defect is alleged.
actions:
- action_id: clarify-rv2632c-rv1738-attribution-transition
  description: In separately authorized curation, examine attributable identifier
    and source context, then explain the relationship or transition between the two
    named-protein accounts without adding operational biological interpretation.
  finding_ids:
  - rv2632c-rv1738-attribution-transition
  target_ids:
  - PF08962
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF08962.yaml
    role: Future maintained source-backed attribution clarification; this review does
      not create an overlay.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: Workflow for a separately authorized successor source freeze; no generator
      defect is alleged.
  generator: just records --apply
  acceptance_checks:
  - Retain an attributable explanation of the two-name relationship and source-context
    transition, preserving citations and qualifications. Do not choose a biological
    correction or assert identity equivalence from this text alone.
  - If the relationship cannot be established, document the bounded source search
    and keep the finding unresolved; documenting uncertainty alone does not resolve
    the attribution gap.
  - Keep selected family, each named protein and broader context distinct. Add no
    functional, organism-level, structural-design, sequence or experimental interpretation.
    Use maintained inputs or a separately authorized successor freeze, without hand-editing
    generated projections or immutable rows.
  - Any later curation must retain actual canonical history and pass record/history/review
    checks; any finding disposition must cite this observation.
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
