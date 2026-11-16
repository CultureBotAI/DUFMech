# PF06296 RelE: seed identity, provenance and evidence-scope review

- Review: 20261021T140012Z-pf06296-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-21T13:50:40Z
- Finished UTC: 2026-10-21T14:00:12Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

PF06296 (RelE; InterPro:IPR009387) matches the verified frozen source and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED. RelE preserves PF06296/IPR009387 and EX_DUF. The long name uses toxin for the selected family, while the opening description labels it antitoxins; the next sentence assigns an antitoxin label to the separately referenced RelB family PF04221. No primary citation accompanies these local labels. One minor local representation finding remains open: selected-family terminology differs between the long name and opening description without reconciliation. No correct biological role is selected, and the scientific account remains unassessed.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: 35b9a13da0689d7e262b05791d5f1d8e763f38f7. The corpus has 8296 records; 951 were covered and 7345 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF06296.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 35b9a13da0689d7e262b05791d5f1d8e763f38f7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF06296 | data/families/PF06296.yaml | generated | PF06296 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF06296 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF06296 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF06296 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF06296 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF06296 | 434 valid canonical history records. |
| Generated schema check | passed | True | PF06296 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF06296.

The filename, pfam_id=PF06296, id=Pfam:PF06296, short_name=RelE, name=RelE toxin of RelE / RelB toxin-antitoxin system, source URL and InterPro accession InterPro:IPR009387 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF06296.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 2447 proteins, 2447 matches, 6 structure entries and 1581 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF06296.

RelE preserves PF06296/IPR009387 and EX_DUF. The long name uses toxin for the selected family, while the opening description labels it antitoxins; the next sentence assigns an antitoxin label to the separately referenced RelB family PF04221. No primary citation accompanies these local labels.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF06296.

This is strictly non-operational identity and representation review. The selected family and referenced family remain distinct. The opposed role labels are a local text discrepancy; this review does not choose a biologically correct label or infer any activity, mechanism or relationship beyond the written attribution.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF06296.

One minor representation finding requests source-backed clarification of the selected-family label while leaving unresolved attribution open. The 2447 proteins and matches, six structures, 1581 models and two architectures cannot settle the terminology. Hidden/ignored-inclusive searches found no maintained accession context; no toxin, immunity, sequence, experimental or intervention account is elaborated. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF06296.

seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED express separate states. EX_DUF records historical renaming and is compatible with imported functional descriptions; it is not evidence that all members were tested. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF06296.

Source-backed identity and terminology clarification belongs in a maintained PF06296 overlay or separately authorized successor source freeze. The generated projection and frozen row remain unchanged. Later curation requires actual canonical history and native validation; the action is proposed, not performed.

### Selected-family terminology across name and description

representation: concern. Targets: PF06296.

The long name labels the selected family toxin, whereas its opening description labels it antitoxins. A separate referenced family is then labeled antitoxin. The selected text leaves these role labels unreconciled; no biological correction is selected.

## Findings

### selected-family-role-label-attribution: Reconcile selected-family terminology between name and description

minor / open / confirmed; issue key: pf06296-selected-family-role-label-attribution.

The exact projection and unique frozen row use toxin in the long name and antitoxins for the selected family in the opening description. The following sentence separately labels referenced RelB/PF04221 as antitoxin. The local wording does not reconcile the selected-family labels. This observation identifies a text-attribution discrepancy only; it does not select a biologically correct role or adopt the scientific account.

## Recommended Actions And Acceptance Checks

### clarify-selected-family-role-label-attribution

In separately authorized curation, examine attributable identity and source context and clarify the selected-family terminology while keeping it separate from the referenced family.

- Retain an attributable explanation or consistent source-backed selected-family terminology. Do not select a biological correction solely from this local name/description discrepancy.
- If the intended attribution cannot be established, document the bounded source search and keep the finding unresolved; documenting uncertainty alone does not resolve the discrepancy.
- Keep the selected and referenced families distinct. Follow-up remains strictly non-operational with no toxin, immunity, activity, sequence, mechanistic, experimental or intervention elaboration. Use maintained inputs or a separately authorized successor freeze, without hand-editing generated projections or immutable rows.
- Any later curation must retain actual canonical history and pass record/history/review checks; any disposition must cite this observation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF06296.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF06296 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF06296; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 434 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF06296 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf06296 | data/families/PF06296.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

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
  git_revision: 35b9a13da0689d7e262b05791d5f1d8e763f38f7
  inputs:
  - path: data/families/PF06296.yaml
    role: target
    sha256: a0d87c7fa4612b9b7ecfd136471a88e381383bb2d868abe46bac1947eb729466
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
  label: PF06296
  owner_paths:
  - path: curation/families/PF06296.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF06296.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: dfec95534dab41b167ca4d712b95e2f2dff8b8b8da7365a89bc7caa79ebb3ba7
  target_id: PF06296
schema_version: 1.0.0
review_id: 20261021T140012Z-pf06296-seed-record-review
title: 'PF06296 RelE: seed identity, provenance and evidence-scope review'
started_at: '2026-10-21T13:50:40Z'
finished_at: '2026-10-21T14:00:12Z'
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
summary: 'PF06296 (RelE; InterPro:IPR009387) matches the verified frozen source and
  retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED.
  RelE preserves PF06296/IPR009387 and EX_DUF. The long name uses toxin for the selected
  family, while the opening description labels it antitoxins; the next sentence assigns
  an antitoxin label to the separately referenced RelB family PF04221. No primary
  citation accompanies these local labels. One minor local representation finding
  remains open: selected-family terminology differs between the long name and opening
  description without reconciliation. No correct biological role is selected, and
  the scientific account remains unassessed.'
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: 35b9a13da0689d7e262b05791d5f1d8e763f38f7. The corpus has 8296
    records; 951 were covered and 7345 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF06296.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF06296
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF06296
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF06296
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-082/PF06296-targets.yaml
    --input data/families/PF06296.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF06296
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-082/prepare.py
    PF06296
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF06296
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
  - PF06296
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
  - PF06296
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
  - PF06296
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF06296.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-10-21T14:00:12Z'
  support: supports
  summary: Read the complete PF06296 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: a0d87c7fa4612b9b7ecfd136471a88e381383bb2d868abe46bac1947eb729466
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF06296; companion manifest and TSV; native verified inspection
  accessed_at: '2026-10-21T14:00:12Z'
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
  accessed_at: '2026-10-21T14:00:12Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-10-21T14:00:12Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 434 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF06296
  accessed_at: '2026-10-21T14:00:12Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF06296. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf06296
  kind: record_content
  reference: data/families/PF06296.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-21T14:00:12Z'
  support: context_only
  snapshot_sha256: a0d87c7fa4612b9b7ecfd136471a88e381383bb2d868abe46bac1947eb729466
  quote: "id: Pfam:PF06296\npfam_id: PF06296\nname: RelE toxin of RelE / RelB toxin-antitoxin\
    \ system\nshort_name: RelE\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF06296\n\
    counters:\n  proteins: 2447\n  matches: 2447\n  proteomes: 1915\n  taxa: 3533\n\
    \  structures: 6\n  alphafold_models: 1581\n  domain_architectures: 2\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR009387\ndescription: RelE is a family of Gram-negative\
    \ bacterial antitoxins of the RelE/RelB toxin-antitoxin system.\n  Its cognate\
    \ antitoxin is family RelB, [pfam:PF04221].\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF06296, id=Pfam:PF06296, short_name=RelE, name=RelE
    toxin of RelE / RelB toxin-antitoxin system, source URL and InterPro accession
    InterPro:IPR009387 agree with the selected frozen row. This establishes frozen
    identity correspondence, not current upstream taxonomy or function.
  target_ids:
  - PF06296
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 2447 proteins, 2447 matches, 6 structure entries and
    1581 AlphaFold models are frozen database counters, not independent experiments.
    Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF06296
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: RelE preserves PF06296/IPR009387 and EX_DUF. The long name uses toxin for
    the selected family, while the opening description labels it antitoxins; the next
    sentence assigns an antitoxin label to the separately referenced RelB family PF04221.
    No primary citation accompanies these local labels.
  target_ids:
  - PF06296
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
  summary: This is strictly non-operational identity and representation review. The
    selected family and referenced family remain distinct. The opposed role labels
    are a local text discrepancy; this review does not choose a biologically correct
    label or infer any activity, mechanism or relationship beyond the written attribution.
  target_ids:
  - PF06296
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: One minor representation finding requests source-backed clarification of
    the selected-family label while leaving unresolved attribution open. The 2447
    proteins and matches, six structures, 1581 models and two architectures cannot
    settle the terminology. Hidden/ignored-inclusive searches found no maintained
    accession context; no toxin, immunity, sequence, experimental or intervention
    account is elaborated. No accession-named overlay, evidence or history path was
    found by the bounded hidden/ignored-inclusive inventory; the inspected projection
    has no curated claim payload. Optional-field absence is not a seed-schema defect.
  target_ids:
  - PF06296
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
  - PF06296
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: Source-backed identity and terminology clarification belongs in a maintained
    PF06296 overlay or separately authorized successor source freeze. The generated
    projection and frozen row remain unchanged. Later curation requires actual canonical
    history and native validation; the action is proposed, not performed.
  target_ids:
  - PF06296
  evidence_ids:
  - profile
  - record
  - validation
- assessment_id: selected-family-role-label-attribution
  area: representation
  topic: Selected-family terminology across name and description
  outcome: concern
  summary: The long name labels the selected family toxin, whereas its opening description
    labels it antitoxins. A separate referenced family is then labeled antitoxin.
    The selected text leaves these role labels unreconciled; no biological correction
    is selected.
  target_ids:
  - PF06296
  evidence_ids:
  - record
  - snapshot
findings:
- finding_id: selected-family-role-label-attribution
  issue_key: pf06296-selected-family-role-label-attribution
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Reconcile selected-family terminology between name and description
  description: The exact projection and unique frozen row use toxin in the long name
    and antitoxins for the selected family in the opening description. The following
    sentence separately labels referenced RelB/PF04221 as antitoxin. The local wording
    does not reconcile the selected-family labels. This observation identifies a text-attribution
    discrepancy only; it does not select a biologically correct role or adopt the
    scientific account.
  target_ids:
  - PF06296
  field_paths:
  - name
  - description
  evidence_ids:
  - record
  - snapshot
  normalization_reason: Minor captures an internally unreconciled terminology difference
    while stable Pfam identity, required fields and frozen-source fidelity remain
    intact. Scientific validity and correct biological role were not assessed.
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF06296.yaml
    role: Future maintained source-backed identity and terminology clarification;
      no overlay created by this review.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: Workflow for a separately authorized successor source freeze; no generator
      defect alleged.
actions:
- action_id: clarify-selected-family-role-label-attribution
  description: In separately authorized curation, examine attributable identity and
    source context and clarify the selected-family terminology while keeping it separate
    from the referenced family.
  finding_ids:
  - selected-family-role-label-attribution
  target_ids:
  - PF06296
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF06296.yaml
    role: Future maintained source-backed identity and terminology clarification;
      no overlay created by this review.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: Workflow for a separately authorized successor source freeze; no generator
      defect alleged.
  generator: just records --apply
  acceptance_checks:
  - Retain an attributable explanation or consistent source-backed selected-family
    terminology. Do not select a biological correction solely from this local name/description
    discrepancy.
  - If the intended attribution cannot be established, document the bounded source
    search and keep the finding unresolved; documenting uncertainty alone does not
    resolve the discrepancy.
  - Keep the selected and referenced families distinct. Follow-up remains strictly
    non-operational with no toxin, immunity, activity, sequence, mechanistic, experimental
    or intervention elaboration. Use maintained inputs or a separately authorized
    successor freeze, without hand-editing generated projections or immutable rows.
  - Any later curation must retain actual canonical history and pass record/history/review
    checks; any disposition must cite this observation.
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
