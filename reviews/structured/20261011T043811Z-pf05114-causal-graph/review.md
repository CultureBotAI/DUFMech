# PF05114 MbnBC causal graph review

- Review: 20261011T043811Z-pf05114-causal-graph
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T04:37:56Z
- Finished UTC: 2026-10-11T04:38:11Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The purified-complex graph is supported within its declared scope and preserves a partner-necessity qualification. Remaining former DUF692 members and native pathway details need follow-up; retain IN_PROGRESS.

## Scope And Provenance

Assess the retained purified-complex edge against the primary Results and methods, reference identity mappings and cellular qualification researched during this curation session.

Selection: PF05114 selected as a formerly uncharacterized family with accessible primary mechanistic evidence.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF05114 | data/families/PF05114.yaml | generated | PF05114 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native record validation | passed | True | PF05114 | Generated projection, closed schema, graph endpoints, evidence quotations and hashes, and canonical history validate. |

## Scientific And Domain Assessments

### Exact tested system and family mapping

identity: supported. Targets: PF05114.

The graph preserves the complex, co-inputs and reference/construct distinction without assigning the result to an isolated domain.

### Direct biochemical observation with explicit limitations

graph: supported. Targets: PF05114.

A directed edge is justified for the tested system; partner necessity, family-wide transfer and unmeasured intermediates are not implied.

### Broader family and pathway coverage

completeness: concern. Targets: PF05114.

One supported graph is not a comprehensive mechanistic review of former DUF692 members.

## Findings

### additional-members: Other PF05114 members and native pathway details remain unreviewed

minor / open / confirmed; issue key: pf05114-causal-member-coverage.

Investigate TglH, ChrH and additional MbnB contexts separately, including sequence and construct mapping and ring-specific cellular evidence. Do not infer their chemistry from family membership.

## Recommended Actions And Acceptance Checks

### extend-family

Curate additional primary-evidence contexts and retain successor dispositions without erasing the partner qualification.

- Member-specific directed evidence supports each added edge.
- Reference versus construct differences and conflicting source statements remain explicit.
- A successor review declares actual scope and native checks pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| purified-complex | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9060507/fullTextXML; Results on oxidation-state-dependent activity and product analysis; Figure 3 and 7 captions; assay and MS methods | supports | Activity and product identification support the scoped complex-level edge; the graph separates the assays and does not claim atom-by-atom resolution. |
| reference-identities | https://www.ebi.ac.uk/interpro/api/protein/uniprot/A0A2D2D5M1/entry/pfam/PF05114/; Domain coordinates, with paired UniProt member, partner and substrate identifiers | supports | Reference accession and domain mapping are grounded, while engineered-construct sequence identity is not overstated. |
| partner-qualification | https://push-zb.helmholtz-munich.de/deliver.php?id=33331; Results pages 2-5; Discussion page 7; Table 1 and construction methods pages 8-9 | context_only | Ring retention in the complemented mbnC-deficient system limits a universal requirement claim, not the narrower purified-complex observation. The contradictory sentence in Results is explicitly retained as a source discrepancy. |
| native-checks | src/dufmech/records.py; Current projection validation, successful guarded regeneration and schema-only check | supports | Structural and retained-input checks pass; these are not independent scientific evidence. |
| duf-projection-pf05114 | data/families/PF05114.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Same-agent scientific assessment, not independent expert endorsement or experimental replication.
- Full-text Results, methods and figure captions were inspected; figure images, raw spectra and supplemental datasets were not independently visually checked.
- No exhaustive family review, REVIEWED promotion, publication or full publication-QC pass is claimed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T043811Z-pf05114-causal-graph
kind: record
repository: CultureBotAI/DUFMech
title: PF05114 MbnBC causal graph review
started_at: '2026-10-11T04:37:56Z'
finished_at: '2026-10-11T04:38:11Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent researched and curated this graph; no independent
    expert endorsement.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: true
summary: The purified-complex graph is supported within its declared scope and preserves
  a partner-necessity qualification. Remaining former DUF692 members and native pathway
  details need follow-up; retain IN_PROGRESS.
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF05114.yaml
    role: context
    sha256: c60aa536ee08d60813562eac08fe58fd476ab6ada13bd0ca1b2a9b5193cd55ec
  - path: data/families/PF05114.yaml
    role: target
    sha256: 3f2df2864edbaa51515f8a8850c5c83f4389e8e56914fc8cc7955871c1321f9f
  - path: data/worklists/interpro-pfam-duf-2026-10-10.json
    role: context
    sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383
  - path: data/worklists/interpro-pfam-duf-2026-10-10.manifest.json
    role: context
    sha256: 31c07ffb6a169c851ea0e6e9dd527a10c04028eafeb29187bd62dc2ae848696e
  - path: data/worklists/interpro-pfam-duf-2026-10-10.tsv
    role: context
    sha256: be023c8dd9d8d3864926b5032d6f7e87a884b1a567391696822dbbecc692dae7
  - path: evidence/PF05114/park-2022-mbnbc.txt
    role: context
    sha256: 30d5d506196970552c0c2fa8018c9ee0f0d63239758c55efed493f0d9426552d
  - path: evidence/PF05114/ob3b-identities.txt
    role: context
    sha256: 9174bc6fac24ec8497095ed26b8c658c13302d18d7527c05eec273863649ca17
  - path: evidence/PF05114/dershwitz-2022-mbnc.txt
    role: context
    sha256: 4aeb65fe5eb58b8d1e7eb4de029c9e0265d3411a51b41401e41308750c25044b
targets:
- kind: generated
  label: PF05114
  path: data/families/PF05114.yaml
  record_class: FamilyRecord
  target_id: PF05114
  owner_paths:
  - path: curation/families/PF05114.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: 6bde64acbb6dbd94e1c27f6c202ae6437a49b146c9a1b4d4cf5b90ef73eacc51
scope:
  description: Assess the retained purified-complex edge against the primary Results
    and methods, reference identity mappings and cellular qualification researched
    during this curation session.
  selection: PF05114 selected as a formerly uncharacterized family with accessible
    primary mechanistic evidence.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF05114
  exclusions:
  - target: Other family members and complete methanobactin pathway
    reason: TglH, ChrH, other MbnB systems and every native pathway step have not
      been individually assessed.
checks:
- check_id: native-projection
  name: Native record validation
  command: validate_record(load_yaml(Path('data/families/PF05114.yaml')), Path.cwd())
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Generated projection, closed schema, graph endpoints, evidence quotations
    and hashes, and canonical history validate.
  target_ids:
  - PF05114
  evidence_ids:
  - native-checks
evidence:
- evidence_id: purified-complex
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9060507/fullTextXML
  locator: Results on oxidation-state-dependent activity and product analysis; Figure
    3 and 7 captions; assay and MS methods
  accessed_at: '2026-10-11T04:37:56Z'
  support: supports
  summary: Activity and product identification support the scoped complex-level edge;
    the graph separates the assays and does not claim atom-by-atom resolution.
  snapshot_sha256: 30d5d506196970552c0c2fa8018c9ee0f0d63239758c55efed493f0d9426552d
- evidence_id: reference-identities
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/A0A2D2D5M1/entry/pfam/PF05114/
  locator: Domain coordinates, with paired UniProt member, partner and substrate identifiers
  accessed_at: '2026-10-11T04:37:56Z'
  support: supports
  summary: Reference accession and domain mapping are grounded, while engineered-construct
    sequence identity is not overstated.
  snapshot_sha256: 9174bc6fac24ec8497095ed26b8c658c13302d18d7527c05eec273863649ca17
- evidence_id: partner-qualification
  kind: primary_source
  reference: https://push-zb.helmholtz-munich.de/deliver.php?id=33331
  locator: Results pages 2-5; Discussion page 7; Table 1 and construction methods
    pages 8-9
  accessed_at: '2026-10-11T04:37:56Z'
  support: context_only
  summary: Ring retention in the complemented mbnC-deficient system limits a universal
    requirement claim, not the narrower purified-complex observation. The contradictory
    sentence in Results is explicitly retained as a source discrepancy.
  snapshot_sha256: 4aeb65fe5eb58b8d1e7eb4de029c9e0265d3411a51b41401e41308750c25044b
- evidence_id: native-checks
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation, successful guarded regeneration and schema-only
    check
  accessed_at: '2026-10-11T04:38:11Z'
  support: supports
  summary: Structural and retained-input checks pass; these are not independent scientific
    evidence.
- evidence_id: duf-projection-pf05114
  kind: record_content
  reference: data/families/PF05114.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T04:38:11Z'
  support: context_only
  snapshot_sha256: 3f2df2864edbaa51515f8a8850c5c83f4389e8e56914fc8cc7955871c1321f9f
  quote: "id: Pfam:PF05114\npfam_id: PF05114\nname: RiPP precursor modification enzyme\
    \ MbnB/TglH/ChrH\nshort_name: MbnB_TglH_ChrH\nseed_status: EX_DUF\ncharacterization_status:\
    \ UNSCORED\ncuration_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF05114\n\
    counters:\n  proteins: 7264\n  matches: 7269\n  proteomes: 5572\n  taxa: 7824\n\
    \  structures: 10\n  alphafold_models: 4336\n  domain_architectures: 10\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR007801\ndescription: This entry represents a family of\
    \ multinuclear iron-containing proteins which are post-translational\n  modification\
    \ enzymes involved in the biosynthesis of ribosomally synthesized and post-translationally\n\
    \  modified peptide (RiPP) natural products, including the precursor modification\
    \ enzymes MbnB, TglH, and\n  ChrH, formerly known as DUF692 [[cite:PUB00153337],[cite:PUB00106909]].\n\
    curation_history: history/records/PF05114\ncausal_graphs:\n- graph_id: ob3b-mbnbc-mbna-modification\n\
    \  title: MbnBC-catalyzed MbnA modification\n  scope: Purified Methylosinus trichosporium\
    \ OB3b MbnBC complex, not MbnB alone or all former DUF692 proteins.\n  context:\
    \ Ascorbate-reduced MbnBC with oxygen and MbnA; stopped-flow assay at 5 C, final\
    \ 150 uM complex\n    and 300 uM substrate, MOPS pH 7.2.\n  family_mapping: Reference\
    \ MbnB is UniProtKB:A0A2D2D5M1, sequence version 1, 276 residues, PF05114 at\n\
    \    15-248. The tested tagged complex is not an isolated domain; reference MbnC\
    \ and MbnA map to A0A2D2CY73\n    and E3YBA4.\n  scope_status: MECHANISTIC\n \
    \ taxon: NCBITaxon:595536\n  limitations: No MbnB-alone sufficiency, atomic reaction\
    \ sequence or family-wide transfer asserted. The\n    mbnC-deficient cellular\
    \ study limits universal partner-necessity claims; engineered construct coordinates\n\
    \    are not transferred to reference residues.\n  nodes:\n  - node_id: reduced-complex-with-inputs\n\
    \    label: Reduced iron-containing MbnBC with oxygen and MbnA\n    node_type:\
    \ ACTIVITY\n    grounding:\n    - UniProtKB:A0A2D2D5M1\n    - UniProtKB:A0A2D2CY73\n\
    \  - node_id: mbna-oxidative-modification\n    label: Oxidative MbnA modification\n\
    \    node_type: PROCESS\n    grounding:\n    - UniProtKB:E3YBA4\n  edges:\n  -\
    \ edge_id: complex-enables-modification\n    subject: reduced-complex-with-inputs\n\
    \    predicate: enables\n    object: mbna-oxidative-modification\n    mechanism:\
    \ Optical product formation is observed; separate low-iron-complex MS/MS assays\
    \ support oxazolone/thioamide\n      product identity.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:35320042\n      source_url: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9060507/fullTextXML\n\
    \      snippet: modification of both cysteine residues\n      explanation: Figure\
    \ 3 and activity methods support the reaction; Figure 7 and MS results characterize\n\
    \        a separately prepared product. These assays do not assign every intermediate.\n\
    \      cache_path: evidence/PF05114/park-2022-mbnbc.txt\n      cache_sha256: 30d5d506196970552c0c2fa8018c9ee0f0d63239758c55efed493f0d9426552d\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/A0A2D2D5M1/entry/pfam/PF05114/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/A0A2D2D5M1/entry/pfam/PF05114/\n\
    \      snippet: 'entry accession: PF05114'\n      explanation: Domain mapping\
    \ only; paired UniProt facts ground the reference members without proving\n  \
    \      the complete engineered-construct sequence.\n      cache_path: evidence/PF05114/ob3b-identities.txt\n\
    \      cache_sha256: 9174bc6fac24ec8497095ed26b8c658c13302d18d7527c05eec273863649ca17\n\
    \    - reference: doi:10.1128/AEM.01841-21\n      source_url: https://push-zb.helmholtz-munich.de/deliver.php?id=33331\n\
    \      snippet: MbnC is not required for the formation of the N-terminal oxazolone\
    \ group\n      explanation: Scope-limiting cellular evidence, not additional support\
    \ for purified-complex kinetics.\n        The mbnABCMN-deleted strain carries\
    \ mbnABMN on pWG104; N-terminal ring retention precludes asserting\n        universal\
    \ MbnC necessity.\n      cache_path: evidence/PF05114/dershwitz-2022-mbnc.txt\n\
    \      cache_sha256: 4aeb65fe5eb58b8d1e7eb4de029c9e0265d3411a51b41401e41308750c25044b\n\
    curation_events:\n- timestamp: '2026-10-11T04:34:37Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate a scoped MbnBC causal graph for\
    \ PF05114\n  history_record: history/records/PF05114/2026-10-11T043437Z-codex-fc58f2.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: scope-identity
  area: identity
  topic: Exact tested system and family mapping
  outcome: supported
  summary: The graph preserves the complex, co-inputs and reference/construct distinction
    without assigning the result to an isolated domain.
  target_ids:
  - PF05114
  evidence_ids:
  - reference-identities
  - purified-complex
- assessment_id: causality
  area: graph
  topic: Direct biochemical observation with explicit limitations
  outcome: supported
  summary: A directed edge is justified for the tested system; partner necessity,
    family-wide transfer and unmeasured intermediates are not implied.
  target_ids:
  - PF05114
  evidence_ids:
  - purified-complex
  - partner-qualification
  - native-checks
- assessment_id: remaining-coverage
  area: completeness
  topic: Broader family and pathway coverage
  outcome: concern
  summary: One supported graph is not a comprehensive mechanistic review of former
    DUF692 members.
  target_ids:
  - PF05114
  evidence_ids:
  - purified-complex
  - partner-qualification
findings:
- finding_id: additional-members
  issue_key: pf05114-causal-member-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Other PF05114 members and native pathway details remain unreviewed
  description: Investigate TglH, ChrH and additional MbnB contexts separately, including
    sequence and construct mapping and ring-specific cellular evidence. Do not infer
    their chemistry from family membership.
  target_ids:
  - PF05114
  field_paths:
  - causal_graphs
  evidence_ids:
  - purified-complex
  - partner-qualification
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF05114.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-family
  description: Curate additional primary-evidence contexts and retain successor dispositions
    without erasing the partner qualification.
  finding_ids:
  - additional-members
  target_ids:
  - PF05114
  ownership_note: Edit overlay and minimal evidence extracts, append actual history,
    regenerate and review.
  acceptance_checks:
  - Member-specific directed evidence supports each added edge.
  - Reference versus construct differences and conflicting source statements remain
    explicit.
  - A successor review declares actual scope and native checks pass.
limitations:
- Same-agent scientific assessment, not independent expert endorsement or experimental
  replication.
- Full-text Results, methods and figure captions were inspected; figure images, raw
  spectra and supplemental datasets were not independently visually checked.
- No exhaustive family review, REVIEWED promotion, publication or full publication-QC
  pass is claimed.
```
