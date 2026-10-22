# PF09004 ALKBH8_N: seed identity, provenance and evidence-scope review

- Review: 20261022T114150Z-pf09004-seed-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-22T11:35:09Z
- Finished UTC: 2026-10-22T11:41:50Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

PF09004 (ALKBH8_N; InterPro:IPR015095) matches the verified frozen source and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED. ALKBH8_N retains PF09004/IPR015095 and EX_DUF. The source selects an N-terminal region of named ALKBH8 proteins and homologues, relates it to another domain and supplies one publication token for a reported relationship. Exact members and the publication were not assessed. Its final relative clause and possessive do not explicitly identify the subject and possessor of the reported relationship. One minor local attribution finding remains open: the final relative clause and possessive do not explicitly identify the subject and possessor of the reported relationship. No biological subject or activity is selected.

## Scope And Provenance

Full inspection of the selected seed projection and corresponding frozen source row for identity, imported claim scope, evidence representation, provenance, completeness, ownership and status. Primary-literature support and current upstream metadata were not reassessed.

Selection: One record from the path-ordered queue of data/families/*.yaml lacking a target in the validated cumulative scripts/record_review.py list inventory. Fresh branch base: 2b49c8729090bbbcbdaa956f770eee0aff153723. The corpus has 8296 records; 1701 were covered and 6595 unreviewed at selection. Coverage includes immutable reviews retained on earlier local batch branches as recorded in the session ledger. This bundle covers only PF09004.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2b49c8729090bbbcbdaa956f770eee0aff153723.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF09004 | data/families/PF09004.yaml | generated | PF09004 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native snapshot and target inspection | passed | True | PF09004 | Verified manifest and captured exact projection, frozen row, source hashes and semantic digest. |
| Additional rubric input capture | passed | True | PF09004 | Captured rubric and recipe bytes while preserving native source inputs and snapshot identity. |
| Exact frozen-row correspondence | passed | True | PF09004 | The inspected record agrees with its frozen row for accession, labels, description, source URL, InterPro accession, seed status and every counter; no curated payload is present. |
| Native closed-schema and projection checks | passed | True | PF09004 | 8296 schema-valid records; 0 generated files differ. |
| Canonical history check | passed | True | PF09004 | 438 valid canonical history records. |
| Generated schema check | passed | True | PF09004 | Generated schema check found 0 differing generated files. |

## Scientific And Domain Assessments

### Exact Pfam/InterPro identity and naming

identity: supported. Targets: PF09004.

The filename, pfam_id=PF09004, id=Pfam:PF09004, short_name=ALKBH8_N, name=Alkylated DNA repair protein alkB homolog 8, N-terminal, source URL and InterPro accession InterPro:IPR015095 agree with the selected frozen row. This establishes frozen identity correspondence, not current upstream taxonomy or function.

### Frozen counters, raw hashes and semantic binding

provenance: supported. Targets: PF09004.

The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its generation timestamp. Its 7805 proteins, 7859 matches, 0 structure entries and 6648 AlphaFold models are frozen database counters, not independent experiments. Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.

### Imported description versus experimental support

evidence: unknown. Targets: PF09004.

ALKBH8_N retains PF09004/IPR015095 and EX_DUF. The source selects an N-terminal region of named ALKBH8 proteins and homologues, relates it to another domain and supplies one publication token for a reported relationship. Exact members and the publication were not assessed. Its final relative clause and possessive do not explicitly identify the subject and possessor of the reported relationship.

### Family, domain and tested-protein boundaries

scope: supported. Targets: PF09004.

Selected region, complete named proteins, homologues and associated domain remain distinct. The account is not independently assigned to every homologue or used to infer the broader activity in the protein name; exact relationship scope remains unassessed. The selected region, associated domain and containing protein are not chosen as the intended subject or possessor by this review.

### Seed content and remaining scientific work

completeness: unknown. Targets: PF09004.

Exact region/member/associated-domain/citation attribution and primary support remain unassessed. Zero structures, 6648 models and 794 architectures do not independently verify the source regional account or precise boundaries. One minor local attribution finding remains open: source-backed clarification is needed for the final clause; if the existing citation does not resolve the attribution, retain that uncertainty and keep the finding open. No accession-named overlay, evidence or history path was found by the bounded hidden/ignored-inclusive inventory; the inspected projection has no curated claim payload. Optional-field absence is not a seed-schema defect.

### Seed, scoring and review states

consistency: supported. Targets: PF09004.

seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED express separate states. EX_DUF records historical renaming and is compatible with imported functional descriptions; it is not evidence that all members were tested. No REVIEWED gate or curation event is implied by this bundle.

### Maintained correction surface and scoped result

ownership: supported. Targets: PF09004.

An attributable subject/possessor clarification belongs in maintained PF09004 inputs or a separately authorized successor freeze. If either attribution remains unresolved, the finding stays open. Generated projections and frozen rows remain unchanged; later curation requires actual canonical history and native validation. This action is proposed, not performed.

### Subject and possessor of the final relative clause

representation: concern. Targets: PF09004.

The description relates a selected N-terminal region to an associated RRM domain, then uses which and its in the final clause without explicitly naming the intended subject and possessor. The containing protein is another stated scope. Exact attribution remains unresolved; this review does not choose the biological entity or declare the source claim false.

## Findings

### unresolved-relative-clause-subject-possessor: Final relative clause leaves subject and possessor implicit

minor / open / confirmed; issue key: pf09004-unresolved-relative-clause-subject-possessor.

The complete PF09004 projection and unique frozen row distinguish a selected N-terminal region, an associated RRM domain and named containing proteins. The final clause uses which enhances its RNA binding affinity without explicitly identifying the subject of enhances and the possessor denoted by its. This leaves the local attribution unclear across the stated region/domain/protein scopes. No entity, relationship direction or biological activity is chosen, and no scientific claim is declared false.

## Recommended Actions And Acceptance Checks

### clarify-alkbh8-region-clause-attribution

In separately authorized curation, consult the existing citation locator PUB00062550 to identify the intended subject and possessor of the final clause, then retain an attributable clarification only if supported. Keep the finding open if the source cannot resolve either attribution.

- Resolve only if attributable source evidence identifies both the intended subject and possessor, or explicitly supported relationship scope, and maintained wording states that attribution. If the existing source does not resolve them, retain the uncertainty and keep the finding open; deleting the relative clause or adding a disclaimer alone does not resolve the finding.
- Keep the selected N-terminal region, associated RRM domain, containing proteins and homologues distinct. Do not choose the biological entity or relationship from memory, the expanded protein name, inventory counters or another family account.
- Use separately authorized maintained inputs or a successor source freeze; do not hand-edit generated projections or immutable frozen rows.
- Any later curation must retain actual canonical history and pass record/history/review checks; finding disposition must cite this prior observation. This proposed follow-up concerns attribution only and adds no residue, mechanistic or experimental interpretation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/families/PF09004.yaml; Entire projection, including identity, description, counters, status and provenance | supports | Read the complete PF09004 seed record; it contains imported metadata and no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history, curation_events or review_id. |
| snapshot | data/worklists/interpro-pfam-duf-2026-10-10.json; pfam_id=PF09004; companion manifest and TSV; native verified inspection | supports | The exact frozen row matches the projection. The native inspection verifies the retained JSON/TSV manifest; the migration snapshot generation timestamp is 2026-10-10T07:44:21.614711Z. This is not the acquisition time of this retained row. The review date does not refresh these source facts. |
| profile | docs/record-review-profile.md; Domains and Ownership; Verdicts and Status Gates; linked record-review contract and native checklist | supports | Read the local rules distinguishing imported description, seed class, evidence scoring, curated claims and scientific review, and the separate projection/overlay ownership. |
| validation | justfile; records-check, history-check, validate-schema recipes; actual batch input-check runs | supports | Observed exit 0 from all three input recipes. 8296 schema-valid records; 0 generated files differ. 438 valid canonical history records. Generated schema check found 0 differing generated files. These checks do not establish scientific truth. |
| local-search | curation/families; evidence; history; Path inventory filtered for PF09004 | supports | No path containing this accession was found in the bounded inventory. The exact overlay was also absent from native inspection; the record has no curated claim fields. |
| duf-projection-pf09004 | data/families/PF09004.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

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
  - path: data/families/PF09004.yaml
    role: target
    sha256: 6ce801a5587d3751c267f377fa743087b0c6ee67ced6f18edc427f9633ea2b0f
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
  label: PF09004
  owner_paths:
  - path: curation/families/PF09004.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF09004.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: b702fde16bdc92b3984e75b282e741c5a115164990f6779b339ecd8a84626c6b
  target_id: PF09004
schema_version: 1.0.0
review_id: 20261022T114150Z-pf09004-seed-record-review
title: 'PF09004 ALKBH8_N: seed identity, provenance and evidence-scope review'
started_at: '2026-10-22T11:35:09Z'
finished_at: '2026-10-22T11:41:50Z'
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
summary: 'PF09004 (ALKBH8_N; InterPro:IPR015095) matches the verified frozen source
  and retains seed_status=EX_DUF, characterization_status=UNSCORED and curation_status=SEEDED.
  ALKBH8_N retains PF09004/IPR015095 and EX_DUF. The source selects an N-terminal
  region of named ALKBH8 proteins and homologues, relates it to another domain and
  supplies one publication token for a reported relationship. Exact members and the
  publication were not assessed. Its final relative clause and possessive do not explicitly
  identify the subject and possessor of the reported relationship. One minor local
  attribution finding remains open: the final relative clause and possessive do not
  explicitly identify the subject and possessor of the reported relationship. No biological
  subject or activity is selected.'
scope:
  description: Full inspection of the selected seed projection and corresponding frozen
    source row for identity, imported claim scope, evidence representation, provenance,
    completeness, ownership and status. Primary-literature support and current upstream
    metadata were not reassessed.
  selection: 'One record from the path-ordered queue of data/families/*.yaml lacking
    a target in the validated cumulative scripts/record_review.py list inventory.
    Fresh branch base: 2b49c8729090bbbcbdaa956f770eee0aff153723. The corpus has 8296
    records; 1701 were covered and 6595 unreviewed at selection. Coverage includes
    immutable reviews retained on earlier local batch branches as recorded in the
    session ledger. This bundle covers only PF09004.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PF09004
  exclusions:
  - target: Primary literature, live Pfam/InterPro/UniProt state and other family
      members
    reason: The selected object is a seed projection without curated functional assertions.
      This is a local metadata and representation review; it does not establish experimental
      characterization.
checks:
- check_id: native-inspect
  name: Native snapshot and target inspection
  command: uv run --locked dufmech-review inspect record PF09004
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Verified manifest and captured exact projection, frozen row, source hashes
    and semantic digest.
  target_ids:
  - PF09004
  evidence_ids:
  - record
  - snapshot
- check_id: common-inspect
  name: Additional rubric input capture
  command: uv run --locked python scripts/record_review.py inspect --targets /private/tmp/dufmech-review-session-20261019/batch-157/PF09004-targets.yaml
    --input data/families/PF09004.yaml --input data/worklists/interpro-pfam-duf-2026-10-10.json
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
  - PF09004
  evidence_ids:
  - profile
- check_id: row-correspondence
  name: Exact frozen-row correspondence
  command: .venv/bin/python /private/tmp/dufmech-review-session-20261019/batch-157/prepare.py
    PF09004
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The inspected record agrees with its frozen row for accession, labels,
    description, source URL, InterPro accession, seed status and every counter; no
    curated payload is present.
  target_ids:
  - PF09004
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
  - PF09004
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
  - PF09004
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
  - PF09004
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/families/PF09004.yaml
  locator: Entire projection, including identity, description, counters, status and
    provenance
  accessed_at: '2026-10-22T11:41:50Z'
  support: supports
  summary: Read the complete PF09004 seed record; it contains imported metadata and
    no assertions, causal_graphs, discussions, datasets, cross_corpus_links, curation_history,
    curation_events or review_id.
  snapshot_sha256: 6ce801a5587d3751c267f377fa743087b0c6ee67ced6f18edc427f9633ea2b0f
- evidence_id: snapshot
  kind: database
  reference: data/worklists/interpro-pfam-duf-2026-10-10.json
  locator: pfam_id=PF09004; companion manifest and TSV; native verified inspection
  accessed_at: '2026-10-22T11:41:50Z'
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
  accessed_at: '2026-10-22T11:41:50Z'
  support: supports
  summary: Read the local rules distinguishing imported description, seed class, evidence
    scoring, curated claims and scientific review, and the separate projection/overlay
    ownership.
- evidence_id: validation
  kind: validation
  reference: justfile
  locator: records-check, history-check, validate-schema recipes; actual batch input-check
    runs
  accessed_at: '2026-10-22T11:41:50Z'
  support: supports
  summary: Observed exit 0 from all three input recipes. 8296 schema-valid records;
    0 generated files differ. 438 valid canonical history records. Generated schema
    check found 0 differing generated files. These checks do not establish scientific
    truth.
- evidence_id: local-search
  kind: search
  reference: curation/families; evidence; history
  locator: Path inventory filtered for PF09004
  accessed_at: '2026-10-22T11:41:50Z'
  support: supports
  summary: No path containing this accession was found in the bounded inventory. The
    exact overlay was also absent from native inspection; the record has no curated
    claim fields.
  search_scope: All paths under curation/families, evidence, and history, including
    hidden and ignored files, filtered for the exact accession PF09004. This is a
    local path inventory, not a literature search or an assertion that other corpora
    lack evidence.
- evidence_id: duf-projection-pf09004
  kind: record_content
  reference: data/families/PF09004.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-22T11:41:50Z'
  support: context_only
  snapshot_sha256: 6ce801a5587d3751c267f377fa743087b0c6ee67ced6f18edc427f9633ea2b0f
  quote: "id: Pfam:PF09004\npfam_id: PF09004\nname: Alkylated DNA repair protein alkB\
    \ homolog 8, N-terminal\nshort_name: ALKBH8_N\nseed_status: EX_DUF\ncharacterization_status:\
    \ UNSCORED\ncuration_status: SEEDED\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF09004\n\
    counters:\n  proteins: 7805\n  matches: 7859\n  proteomes: 347\n  taxa: 1239\n\
    \  structures: 0\n  alphafold_models: 6648\n  domain_architectures: 794\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR015095\ndescription: This domain is the N-terminal domain\
    \ of Alkylated DNA repair protein alkB homolog 8 (ALKBH8)\n  and its homologues.\
    \ This domain corresponds to the basic alpha-helix located at the N-terminal of\
    \ the\n  RRM domain, which enhances its RNA binding affinity [[cite:PUB00062550]].\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Pfam/InterPro identity and naming
  outcome: supported
  summary: The filename, pfam_id=PF09004, id=Pfam:PF09004, short_name=ALKBH8_N, name=Alkylated
    DNA repair protein alkB homolog 8, N-terminal, source URL and InterPro accession
    InterPro:IPR015095 agree with the selected frozen row. This establishes frozen
    identity correspondence, not current upstream taxonomy or function.
  target_ids:
  - PF09004
  evidence_ids:
  - record
  - snapshot
- assessment_id: provenance
  area: provenance
  topic: Frozen counters, raw hashes and semantic binding
  outcome: supported
  summary: The record binds interpro-pfam-duf-2026-10-10 by SHA-256 and retains its
    generation timestamp. Its 7805 proteins, 7859 matches, 0 structure entries and
    6648 AlphaFold models are frozen database counters, not independent experiments.
    Raw input hashes and the dufmech-record-content-v1 digest preserve different checks.
  target_ids:
  - PF09004
  evidence_ids:
  - record
  - snapshot
  - validation
- assessment_id: evidence-tier
  area: evidence
  topic: Imported description versus experimental support
  outcome: unknown
  summary: ALKBH8_N retains PF09004/IPR015095 and EX_DUF. The source selects an N-terminal
    region of named ALKBH8 proteins and homologues, relates it to another domain and
    supplies one publication token for a reported relationship. Exact members and
    the publication were not assessed. Its final relative clause and possessive do
    not explicitly identify the subject and possessor of the reported relationship.
  target_ids:
  - PF09004
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
  summary: Selected region, complete named proteins, homologues and associated domain
    remain distinct. The account is not independently assigned to every homologue
    or used to infer the broader activity in the protein name; exact relationship
    scope remains unassessed. The selected region, associated domain and containing
    protein are not chosen as the intended subject or possessor by this review.
  target_ids:
  - PF09004
  evidence_ids:
  - record
  - snapshot
- assessment_id: completeness
  area: completeness
  topic: Seed content and remaining scientific work
  outcome: unknown
  summary: 'Exact region/member/associated-domain/citation attribution and primary
    support remain unassessed. Zero structures, 6648 models and 794 architectures
    do not independently verify the source regional account or precise boundaries.
    One minor local attribution finding remains open: source-backed clarification
    is needed for the final clause; if the existing citation does not resolve the
    attribution, retain that uncertainty and keep the finding open. No accession-named
    overlay, evidence or history path was found by the bounded hidden/ignored-inclusive
    inventory; the inspected projection has no curated claim payload. Optional-field
    absence is not a seed-schema defect.'
  target_ids:
  - PF09004
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
  - PF09004
  evidence_ids:
  - record
  - profile
- assessment_id: ownership
  area: ownership
  topic: Maintained correction surface and scoped result
  outcome: supported
  summary: An attributable subject/possessor clarification belongs in maintained PF09004
    inputs or a separately authorized successor freeze. If either attribution remains
    unresolved, the finding stays open. Generated projections and frozen rows remain
    unchanged; later curation requires actual canonical history and native validation.
    This action is proposed, not performed.
  target_ids:
  - PF09004
  evidence_ids:
  - profile
  - record
  - validation
- assessment_id: unresolved-relative-clause-attribution
  area: representation
  topic: Subject and possessor of the final relative clause
  outcome: concern
  summary: The description relates a selected N-terminal region to an associated RRM
    domain, then uses which and its in the final clause without explicitly naming
    the intended subject and possessor. The containing protein is another stated scope.
    Exact attribution remains unresolved; this review does not choose the biological
    entity or declare the source claim false.
  target_ids:
  - PF09004
  evidence_ids:
  - record
  - snapshot
findings:
- finding_id: unresolved-relative-clause-subject-possessor
  issue_key: pf09004-unresolved-relative-clause-subject-possessor
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Final relative clause leaves subject and possessor implicit
  description: The complete PF09004 projection and unique frozen row distinguish a
    selected N-terminal region, an associated RRM domain and named containing proteins.
    The final clause uses which enhances its RNA binding affinity without explicitly
    identifying the subject of enhances and the possessor denoted by its. This leaves
    the local attribution unclear across the stated region/domain/protein scopes.
    No entity, relationship direction or biological activity is chosen, and no scientific
    claim is declared false.
  target_ids:
  - PF09004
  field_paths:
  - description
  evidence_ids:
  - record
  - snapshot
  normalization_reason: Minor reflects a local attribution ambiguity in faithfully
    imported text while stable identity, required schema fields and frozen-row correspondence
    remain intact. No biological or generator defect established.
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF09004.yaml
    role: Future maintained source-backed attribution clarification; no overlay created
      by this review.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: Workflow for a separately authorized successor source freeze; no generator
      defect alleged.
actions:
- action_id: clarify-alkbh8-region-clause-attribution
  description: In separately authorized curation, consult the existing citation locator
    PUB00062550 to identify the intended subject and possessor of the final clause,
    then retain an attributable clarification only if supported. Keep the finding
    open if the source cannot resolve either attribution.
  finding_ids:
  - unresolved-relative-clause-subject-possessor
  target_ids:
  - PF09004
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF09004.yaml
    role: Future maintained source-backed attribution clarification; no overlay created
      by this review.
  - repository: CultureBotAI/DUFMech
    path: scripts/freeze_duf_puf_worklist.py
    role: Workflow for a separately authorized successor source freeze; no generator
      defect alleged.
  generator: just records --apply
  acceptance_checks:
  - Resolve only if attributable source evidence identifies both the intended subject
    and possessor, or explicitly supported relationship scope, and maintained wording
    states that attribution. If the existing source does not resolve them, retain
    the uncertainty and keep the finding open; deleting the relative clause or adding
    a disclaimer alone does not resolve the finding.
  - Keep the selected N-terminal region, associated RRM domain, containing proteins
    and homologues distinct. Do not choose the biological entity or relationship from
    memory, the expanded protein name, inventory counters or another family account.
  - Use separately authorized maintained inputs or a successor source freeze; do not
    hand-edit generated projections or immutable frozen rows.
  - Any later curation must retain actual canonical history and pass record/history/review
    checks; finding disposition must cite this prior observation. This proposed follow-up
    concerns attribution only and adds no residue, mechanistic or experimental interpretation.
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
