# PF10300 Iml2-TPR_39: seed identity, provenance and evidence-scope review

- Review: 20261028T082232Z-pf10300-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-28T08:07:14Z
- Finished UTC: 2026-10-28T08:22:32Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

PF10300 (Iml2-TPR_39; InterPro:IPR019412) matches the verified frozen source and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED. The Iml2-TPR_39 projection agrees with the selected row, including TT39A/B/C in the opening parenthetical and TTC39A and TTC39B in later human examples. Identity, EX_DUF status and all seven counters agree. One minor naming-attribution finding remains open: the opening TT39A/B/C label and later TTC39 labels are not explicitly reconciled. No correct spelling, alias relationship or biological identity is selected.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: 0b3ed0fb1dcbba49fff4f3123806aa8b7f3663e4. The corpus has 8296 records; 2151 were covered and 6145 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF10300.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0b3ed0fb1dcbba49fff4f3123806aa8b7f3663e4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF10300 | data/families/PF10300.yaml | generated | PF10300 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF10300 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF10300 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF10300 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF10300 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF10300 | 488 valid canonical history records. |
| Generated schema check | passed | True | PF10300 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF10300.

The filename, pfam_id=PF10300, id=Pfam:PF10300, short_name=Iml2-TPR_39, name=Iml2/Tetratricopeptide repeat protein 39, source URL and InterPro accession InterPro:IPR019412 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF10300.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 9006 proteins, 9867 matches, 0 structure entries and 7859 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF10300.

The Iml2-TPR_39 projection agrees with the selected row, including TT39A/B/C in the opening parenthetical and TTC39A and TTC39B in later human examples. Identity, EX_DUF status and all seven counters agree.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF10300.

The written naming variation is assessed as local attribution only. No preferred spelling, alias equivalence or biological identity is selected; fungal and animal examples, member-level statements and the source qualifications remain distinct.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF10300.

The selected projection and row do not explicitly reconcile TT39A/B/C with the later TTC39 labels. Source-backed naming clarification is required; uncertainty, a disclaimer or deletion alone cannot close the finding. No clinical, sequence, residue or mechanistic interpretation is added. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF10300.

seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED express separate states. EX_DUF records historical renaming and is compatible with imported functional descriptions; it is not evidence that all members were tested. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF10300.

Source-backed naming clarification belongs in the maintained PF10300 overlay or a separately authorized successor source freeze. The generated projection and frozen row remain unchanged. Later curation requires actual canonical history and native validation; the action is proposed, not performed.

### Consistent attribution of protein-group and member labels

representation: concern. Targets: PF10300.

The opening group abbreviation TT39A/B/C and later TTC39A and TTC39B labels differ in the selected projection and frozen row. Their naming relationship needs source-backed clarification. The observation concerns local written attribution and does not establish a scientific or clinical conclusion.

## Findings

### tt39-ttc39-name-attribution: Reconcile the TT39 and TTC39 naming attribution

minor / open / confirmed; issue key: pf10300-tt39-ttc39-name-attribution.

The complete selected projection and frozen row define the animal protein39A/B/C group parenthetically as TT39A/B/C, while later human examples use TTC39A and TTC39B. The selected objects do not explicitly reconcile the written forms. This finding records unresolved naming attribution without choosing a correct spelling, asserting alias equivalence or distinct biological identities, or assessing the scientific account.

## Recommended Actions And Acceptance Checks

### clarify-tt39-ttc39-name-attribution

In separately authorized curation, inspect attributable source context and reconcile the TT39A/B/C and TTC39A/B naming relationship with a source-backed explanation or consistent naming, preserving member and organism scope.

- Retain attributable support for the relationship between TT39A/B/C and the later TTC39 labels. Do not select a spelling, infer an alias relationship or assert distinct identity from the written forms alone.
- If naming intent remains unresolved, document the bounded investigation and keep this finding open. Uncertainty, a disclaimer or deletion of one label alone does not resolve the attribution.
- Preserve member-specific, organism-specific and qualified source statements. Use maintained inputs or a separately authorized successor freeze without hand-editing generated projections or immutable rows; no clinical, sequence, residue or mechanistic inference is requested.
- Any later curation must retain actual canonical history and pass applicable native record, history and review checks. A changed finding disposition must cite the source-backed reconciliation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF10300.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF10300 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF10300; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 488 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF10300 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf10300 | data/families/PF10300.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

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
  git_revision: 0b3ed0fb1dcbba49fff4f3123806aa8b7f3663e4
  inputs:
  - path: data/families/PF10300.yaml
    role: target
    sha256: c3e3c67e6d862c6cebabcea7eb738743321717efeb18e07e887f55a70c1f5bf2
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
  label: PF10300
  owner_paths:
  - path: curation/families/PF10300.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF10300.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: 4010cb2ed1ff4b14f636347905469b8468f3fdd618ed18ac2e0b61ee89f63ff7
  target_id: PF10300
schema_version: 1.0.0
review_id: 20261028T082232Z-pf10300-seed-record-review
title: 'PF10300 Iml2-TPR_39: seed identity, provenance and evidence-scope review'
started_at: '2026-10-28T08:07:14Z'
finished_at: '2026-10-28T08:22:32Z'
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
summary: 'PF10300 (Iml2-TPR_39; InterPro:IPR019412) matches the verified frozen source
  and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED.
  The Iml2-TPR_39 projection agrees with the selected row, including TT39A/B/C in
  the opening parenthetical and TTC39A and TTC39B in later human examples. Identity,
  EX_DUF status and all seven counters agree. One minor naming-attribution finding
  remains open: the opening TT39A/B/C label and later TTC39 labels are not explicitly
  reconciled. No correct spelling, alias relationship or biological identity is selected.'
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: 0b3ed0fb1dcbba49fff4f3123806aa8b7f3663e4. The corpus has 8296
    records; 2151 were covered and 6145 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF10300.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF10300
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF10300
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF10300
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-202-attempt-001/PF10300-targets.yaml
    --input data/families/PF10300.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF10300
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-202-attempt-001/prepare.py
    PF10300
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF10300
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
  - PF10300
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
  summary: 488 valid canonical history records.
  target_ids:
  - PF10300
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
  - PF10300
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF10300.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-10-28T08:22:32Z'
  support: supports
  summary: Read the complete PF10300 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: c3e3c67e6d862c6cebabcea7eb738743321717efeb18e07e887f55a70c1f5bf2
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF10300; companion manifest and TSV; native verified inspection
  accessed_at: '2026-10-28T08:22:32Z'
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
  accessed_at: '2026-10-28T08:22:32Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-10-28T08:22:32Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 488 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF10300
  accessed_at: '2026-10-28T08:22:32Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF10300. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf10300
  kind: record_content
  reference: data/families/PF10300.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-28T08:22:32Z'
  support: context_only
  snapshot_sha256: c3e3c67e6d862c6cebabcea7eb738743321717efeb18e07e887f55a70c1f5bf2
  quote: "id: Pfam:PF10300\npfam_id: PF10300\nname: Iml2/Tetratricopeptide repeat\
    \ protein 39\nshort_name: Iml2-TPR_39\nseed_status: EX_DUF\ncharacterization_status:\
    \ UNSCORED\ncuration_status: SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF10300\n\
    counters:\n  proteins: 9006\n  matches: 9867\n  proteomes: 2835\n  taxa: 7559\n\
    \  structures: 0\n  alphafold_models: 7859\n  domain_architectures: 143\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR019412\ndescription: This is a family of proteins conserved\
    \ from fungi to humans, including fungal Inclusion body\n  clearance protein Iml2\
    \ protein, animal tetratricopeptide repeat protein 39A/B/C (TT39A/B/C) and some\n\
    \  uncharacterised proteins. Members of this family carry a tetratricopeptide\
    \ repeat [pfam:PF07719] at\n  their C terminus. This entry includes Iml2 and its\
    \ paralogue-YKR018C from S. cerevisiae; Iml2 localises\n  to the cytoplasm and\
    \ nucleus [[cite:PUB00016470]], and its expression is increased in response to\
    \ DNA\n  replication stress [[cite:PUB00066967]]. It is found to be involved in\
    \ lipid droplet-mediated inclusion\n  body clearing after protein folding stress\
    \ [[cite:PUB00088292]]. In humans, TTC39A (also known as DEME6)\n  is expressed\
    \ in primary breast carcinomas but not in normal breast tissue, and has a putative\
    \ eukaryotic\n  RNP-1 RNA binding region and a candidate anchoring transmembrane\
    \ domain. It is coordinately regulated\n  with oestrogen receptor, but is not\
    \ necessarily oestradiol-responsive [[cite:PUB00044224]]. TTC39B has\n  been linked\
    \ to lipid metabolism [[cite:PUB00072592]].\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF10300, id=Pfam:PF10300, short_name=Iml2-TPR_39,
    name=Iml2/Tetratricopeptide repeat protein 39, source URL and InterPro accession
    InterPro:IPR019412 agree with the selected frozen row. This establishes frozen
    identity correspondence, not current upstream taxonomy or function.
  target_ids:
  - PF10300
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 9006 proteins, 9867 matches, 0 structure entries and
    7859 AlphaFold models are frozen database counters, not independent experiments.
    Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF10300
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: The Iml2-TPR_39 projection agrees with the selected row, including TT39A/B/C
    in the opening parenthetical and TTC39A and TTC39B in later human examples. Identity,
    EX_DUF status and all seven counters agree.
  target_ids:
  - PF10300
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
  summary: The written naming variation is assessed as local attribution only. No
    preferred spelling, alias equivalence or biological identity is selected; fungal
    and animal examples, member-level statements and the source qualifications remain
    distinct.
  target_ids:
  - PF10300
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: The selected projection and row do not explicitly reconcile TT39A/B/C with
    the later TTC39 labels. Source-backed naming clarification is required; uncertainty,
    a disclaimer or deletion alone cannot close the finding. No clinical, sequence,
    residue or mechanistic interpretation is added. No accession-named overlay, evidence
    or history path was found by the bounded hidden/ignored-inclusive inventory; the
    inspected projection has no curated claim payload. Optional-field absence is not
    a seed-schema defect.
  target_ids:
  - PF10300
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
  - PF10300
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: Source-backed naming clarification belongs in the maintained PF10300 overlay
    or a separately authorized successor source freeze. The generated projection and
    frozen row remain unchanged. Later curation requires actual canonical history
    and native validation; the action is proposed, not performed.
  target_ids:
  - PF10300
  evidence_ids:
  - profile
  - record
  - validation
- assessment_id: tt39-ttc39-name-attribution
  area: representation
  topic: Consistent attribution of protein-group and member labels
  outcome: concern
  summary: The opening group abbreviation TT39A/B/C and later TTC39A and TTC39B labels
    differ in the selected projection and frozen row. Their naming relationship needs
    source-backed clarification. The observation concerns local written attribution
    and does not establish a scientific or clinical conclusion.
  target_ids:
  - PF10300
  evidence_ids:
  - record
  - snapshot
findings:
- finding_id: tt39-ttc39-name-attribution
  issue_key: pf10300-tt39-ttc39-name-attribution
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Reconcile the TT39 and TTC39 naming attribution
  description: The complete selected projection and frozen row define the animal protein39A/B/C
    group parenthetically as TT39A/B/C, while later human examples use TTC39A and
    TTC39B. The selected objects do not explicitly reconcile the written forms. This
    finding records unresolved naming attribution without choosing a correct spelling,
    asserting alias equivalence or distinct biological identities, or assessing the
    scientific account.
  target_ids:
  - PF10300
  field_paths:
  - description
  evidence_ids:
  - record
  - snapshot
  normalization_reason: Minor reflects a bounded naming-attribution inconsistency
    while required fields, Pfam identity and frozen-source fidelity remain intact.
    Confirmed refers to the observed text variation; intended naming and biological
    identity remain unresolved.
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF10300.yaml
    role: Future maintained source-backed naming-attribution clarification; this review
      creates no overlay.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: Workflow for a separately authorized successor source freeze; no generator
      defect is alleged.
actions:
- action_id: clarify-tt39-ttc39-name-attribution
  description: In separately authorized curation, inspect attributable source context
    and reconcile the TT39A/B/C and TTC39A/B naming relationship with a source-backed
    explanation or consistent naming, preserving member and organism scope.
  finding_ids:
  - tt39-ttc39-name-attribution
  target_ids:
  - PF10300
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF10300.yaml
    role: Future maintained source-backed naming-attribution clarification; this review
      creates no overlay.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: Workflow for a separately authorized successor source freeze; no generator
      defect is alleged.
  generator: just records --apply
  acceptance_checks:
  - Retain attributable support for the relationship between TT39A/B/C and the later
    TTC39 labels. Do not select a spelling, infer an alias relationship or assert
    distinct identity from the written forms alone.
  - If naming intent remains unresolved, document the bounded investigation and keep
    this finding open. Uncertainty, a disclaimer or deletion of one label alone does
    not resolve the attribution.
  - Preserve member-specific, organism-specific and qualified source statements. Use
    maintained inputs or a separately authorized successor freeze without hand-editing
    generated projections or immutable rows; no clinical, sequence, residue or mechanistic
    inference is requested.
  - Any later curation must retain actual canonical history and pass applicable native
    record, history and review checks. A changed finding disposition must cite the
    source-backed reconciliation.
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
