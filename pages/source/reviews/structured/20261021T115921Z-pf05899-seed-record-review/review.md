# PF05899 Cupin_3: seed identity, provenance and evidence-scope review

- Review: 20261021T115921Z-pf05899-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-21T11:50:41Z
- Finished UTC: 2026-10-21T11:59:21Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

PF05899 (Cupin_3; InterPro:IPR008579) matches the verified frozen source and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED. PF05899/IPR008579 retains the Cupin_3 domain identity and EX_DUF class. The source combines separate EutQ and UGlyAH member accounts with PUB00096913, PUB00063996, PUB00078751 and PUB00096858. In the final sentence, "deamination of allantoin" and "from S-ureidoglycine" leave the substrate wording unreconciled within the same asserted reaction account. One minor local representation finding remains open: the final sentence leaves two substrate descriptions unreconciled. No substrate, reaction or biochemical correction is selected.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: d658f73e7e618d3938704cdb9c86597bf47fc15e. The corpus has 8296 records; 791 were covered and 7505 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF05899.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d658f73e7e618d3938704cdb9c86597bf47fc15e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF05899 | data/families/PF05899.yaml | generated | PF05899 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF05899 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF05899 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF05899 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF05899 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF05899 | 434 valid canonical history records. |
| Generated schema check | passed | True | PF05899 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF05899.

The filename, pfam_id=PF05899, id=Pfam:PF05899, short_name=Cupin_3, name=EutQ-like cupin domain, source URL and InterPro accession InterPro:IPR008579 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF05899.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 11191 proteins, 11372 matches, 19 structure entries and 7292 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF05899.

PF05899/IPR008579 retains the Cupin_3 domain identity and EX_DUF class. The source combines separate EutQ and UGlyAH member accounts with PUB00096913, PUB00063996, PUB00078751 and PUB00096858. In the final sentence, "deamination of allantoin" and "from S-ureidoglycine" leave the substrate wording unreconciled within the same asserted reaction account.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF05899.

The selected domain, containing proteins and separately named member activities remain distinct. The final sentence has a local wording ambiguity; this review does not select a substrate, reaction, product or biochemical correction, and it does not establish which scientific claim is true.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF05899.

One minor representation follow-up is proposed to clarify the final statement from attributable source context, retaining it as unresolved if that context cannot be recovered. The 11191 proteins, nineteen structures, 7292 models and 78 architectures cannot settle the reaction wording. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF05899.

seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED express separate states. EX_DUF records historical renaming and is compatible with imported functional descriptions; it is not evidence that all members were tested. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF05899.

A source-backed clarification of the final reaction wording belongs in the maintained PF05899 overlay or a separately authorized successor source freeze. Generated and frozen inputs remain unchanged. Later curation requires actual canonical history and native validation; this action is proposed, not performed.

### Final reaction sentence leaves its substrate wording unreconciled

representation: concern. Targets: PF05899.

The final sentence uses two substrate descriptions without stating how they relate. Clarifying that representation requires attributable source context; no scientific falsity or correct reaction is established here.

## Findings

### unreconciled-substrate-wording: Final reaction sentence leaves its substrate wording unreconciled

minor / open / confirmed; issue key: pf05899-unreconciled-substrate-wording.

The final description sentence combines "deamination of allantoin" with "from S-ureidoglycine" in the same reaction account, following a separately named member and broader utilization context. The selected text and unique frozen row do not reconcile those two substrate descriptions or distinguish broader context from the direct reaction. This is a local wording ambiguity; the review does not choose the correct substrate, reaction or biochemical interpretation.

## Recommended Actions And Acceptance Checks

### clarify-pf05899-source-attribution

In separately authorized curation, read and cite the original sources for the final member-specific account and clarify which wording describes the direct reaction versus broader context, without inferring a correction. If unrecoverable, preserve the ambiguity explicitly.

- If recoverable, cite source context and write an unambiguous member-specific statement that distinguishes the direct reaction from broader utilization context without selecting biology from memory. If not recoverable, document the bounded search and retain this finding as unresolved; documenting uncertainty alone does not resolve it.
- Keep the selected family or domain, complete proteins and separately named member or partner accounts distinct; preserve source qualifiers and studied-member scope.
- Do not choose a biological correction from memory or hand-edit generated projections or immutable frozen rows; use authorized maintained inputs or a successor freeze.
- Any later curation must retain actual canonical history and pass record/history/review checks; any finding disposition must cite this observation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF05899.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF05899 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF05899; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 434 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF05899 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf05899 | data/families/PF05899.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

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
  git_revision: d658f73e7e618d3938704cdb9c86597bf47fc15e
  inputs:
  - path: data/families/PF05899.yaml
    role: target
    sha256: acaeb2dea85ba0687f8904831f7538713271500294f3a86b06396026d125b05d
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
  label: PF05899
  owner_paths:
  - path: curation/families/PF05899.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF05899.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: d5afc01b93fe74ab7438373e43003389526e6111b02cdceb7a668a07d6ab1c3f
  target_id: PF05899
schema_version: 1.0.0
review_id: 20261021T115921Z-pf05899-seed-record-review
title: 'PF05899 Cupin_3: seed identity, provenance and evidence-scope review'
started_at: '2026-10-21T11:50:41Z'
finished_at: '2026-10-21T11:59:21Z'
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
summary: 'PF05899 (Cupin_3; InterPro:IPR008579) matches the verified frozen source
  and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED.
  PF05899/IPR008579 retains the Cupin_3 domain identity and EX_DUF class. The source
  combines separate EutQ and UGlyAH member accounts with PUB00096913, PUB00063996,
  PUB00078751 and PUB00096858. In the final sentence, "deamination of allantoin" and
  "from S-ureidoglycine" leave the substrate wording unreconciled within the same
  asserted reaction account. One minor local representation finding remains open:
  the final sentence leaves two substrate descriptions unreconciled. No substrate,
  reaction or biochemical correction is selected.'
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: d658f73e7e618d3938704cdb9c86597bf47fc15e. The corpus has 8296
    records; 791 were covered and 7505 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF05899.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF05899
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF05899
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF05899
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-066/PF05899-targets.yaml
    --input data/families/PF05899.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF05899
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-066/prepare.py
    PF05899
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF05899
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
  - PF05899
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
  summary: 434 valid canonical history records.
  target_ids:
  - PF05899
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
  - PF05899
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF05899.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-10-21T11:59:21Z'
  support: supports
  summary: Read the complete PF05899 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: acaeb2dea85ba0687f8904831f7538713271500294f3a86b06396026d125b05d
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF05899; companion manifest and TSV; native verified inspection
  accessed_at: '2026-10-21T11:59:21Z'
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
  accessed_at: '2026-10-21T11:59:21Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-10-21T11:59:21Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 434 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF05899
  accessed_at: '2026-10-21T11:59:21Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF05899. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf05899
  kind: record_content
  reference: data/families/PF05899.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-21T11:59:21Z'
  support: context_only
  snapshot_sha256: acaeb2dea85ba0687f8904831f7538713271500294f3a86b06396026d125b05d
  quote: "id: Pfam:PF05899\npfam_id: PF05899\nname: EutQ-like cupin domain\nshort_name:\
    \ Cupin_3\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF05899\n\
    counters:\n  proteins: 11191\n  matches: 11372\n  proteomes: 5435\n  taxa: 8650\n\
    \  structures: 19\n  alphafold_models: 7292\n  domain_architectures: 78\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR008579\ndescription: This entry represents the cupin\
    \ domain, with a conserved jelly roll-like beta-barrel fold\n  capable of homodimerisation\
    \ found in bacteria, plant and fungi. It is present in EutQ family from the\n\
    \  eut operon, involved in ethanolamine degradation. EutQ is essential during\
    \ anoxic growth and has acetate\n  kinase activity [[cite:PUB00096913]]. The cupin\
    \ domain from EutQ does not possess the His residues responsible\n  for metal\
    \ coordination in other classes of cupins [[cite:PUB00063996]]. This domain is\
    \ also found in\n  (S)-ureidoglycine aminohydrolase (UGlyAH) from E.coli, which\
    \ is involved in the anaerobic nitrogen utilisation\n  via the assimilation of\
    \ allantoin. It catalyses the deamination of allantoin to produce S-ureidoglycolate\n\
    \  and ammonia from S-ureidoglycine [[cite:PUB00078751],[cite:PUB00096858]].\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF05899, id=Pfam:PF05899, short_name=Cupin_3, name=EutQ-like
    cupin domain, source URL and InterPro accession InterPro:IPR008579 agree with
    the selected frozen row. This establishes frozen identity correspondence, not
    current upstream taxonomy or function.
  target_ids:
  - PF05899
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 11191 proteins, 11372 matches, 19 structure entries
    and 7292 AlphaFold models are frozen database counters, not independent experiments.
    Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF05899
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: PF05899/IPR008579 retains the Cupin_3 domain identity and EX_DUF class.
    The source combines separate EutQ and UGlyAH member accounts with PUB00096913,
    PUB00063996, PUB00078751 and PUB00096858. In the final sentence, "deamination
    of allantoin" and "from S-ureidoglycine" leave the substrate wording unreconciled
    within the same asserted reaction account.
  target_ids:
  - PF05899
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
  summary: The selected domain, containing proteins and separately named member activities
    remain distinct. The final sentence has a local wording ambiguity; this review
    does not select a substrate, reaction, product or biochemical correction, and
    it does not establish which scientific claim is true.
  target_ids:
  - PF05899
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: One minor representation follow-up is proposed to clarify the final statement
    from attributable source context, retaining it as unresolved if that context cannot
    be recovered. The 11191 proteins, nineteen structures, 7292 models and 78 architectures
    cannot settle the reaction wording. No accession-named overlay, evidence or history
    path was found by the bounded hidden/ignored-inclusive inventory; the inspected
    projection has no curated claim payload. Optional-field absence is not a seed-schema
    defect.
  target_ids:
  - PF05899
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
  - PF05899
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: A source-backed clarification of the final reaction wording belongs in
    the maintained PF05899 overlay or a separately authorized successor source freeze.
    Generated and frozen inputs remain unchanged. Later curation requires actual canonical
    history and native validation; this action is proposed, not performed.
  target_ids:
  - PF05899
  evidence_ids:
  - profile
  - record
  - validation
- assessment_id: unreconciled-substrate-wording
  area: representation
  topic: Final reaction sentence leaves its substrate wording unreconciled
  outcome: concern
  summary: The final sentence uses two substrate descriptions without stating how
    they relate. Clarifying that representation requires attributable source context;
    no scientific falsity or correct reaction is established here.
  target_ids:
  - PF05899
  evidence_ids:
  - record
  - snapshot
findings:
- finding_id: unreconciled-substrate-wording
  issue_key: pf05899-unreconciled-substrate-wording
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Final reaction sentence leaves its substrate wording unreconciled
  description: The final description sentence combines "deamination of allantoin"
    with "from S-ureidoglycine" in the same reaction account, following a separately
    named member and broader utilization context. The selected text and unique frozen
    row do not reconcile those two substrate descriptions or distinguish broader context
    from the direct reaction. This is a local wording ambiguity; the review does not
    choose the correct substrate, reaction or biochemical interpretation.
  target_ids:
  - PF05899
  field_paths:
  - description
  evidence_ids:
  - record
  - snapshot
  normalization_reason: Minor is proposed for a bounded local attribution or wording
    gap. Required identity, schema fields and frozen-source fidelity remain intact;
    no scientific correction is established.
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF05899.yaml
    role: Future maintained source-backed clarification; this review does not create
      an overlay.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: Workflow for a separately authorized successor source freeze; no generator
      defect is alleged.
actions:
- action_id: clarify-pf05899-source-attribution
  description: In separately authorized curation, read and cite the original sources
    for the final member-specific account and clarify which wording describes the
    direct reaction versus broader context, without inferring a correction. If unrecoverable,
    preserve the ambiguity explicitly.
  finding_ids:
  - unreconciled-substrate-wording
  target_ids:
  - PF05899
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF05899.yaml
    role: Future maintained source-backed clarification; this review does not create
      an overlay.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: Workflow for a separately authorized successor source freeze; no generator
      defect is alleged.
  generator: just records --apply
  acceptance_checks:
  - If recoverable, cite source context and write an unambiguous member-specific statement
    that distinguishes the direct reaction from broader utilization context without
    selecting biology from memory. If not recoverable, document the bounded search
    and retain this finding as unresolved; documenting uncertainty alone does not
    resolve it.
  - Keep the selected family or domain, complete proteins and separately named member
    or partner accounts distinct; preserve source qualifiers and studied-member scope.
  - Do not choose a biological correction from memory or hand-edit generated projections
    or immutable frozen rows; use authorized maintained inputs or a successor freeze.
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
