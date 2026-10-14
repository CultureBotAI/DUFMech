# PF02621 MqnD causal-evidence and identity-gap review

- Review: 20261011T053106Z-pf02621-mqnd-identity-gap
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T05:30:47Z
- Finished UTC: 2026-10-11T05:31:06Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Primary reaction evidence was reviewed, but no canonical graph was added because the 2021 MqnD clone was not resolved to an exact sequence or accession.

## Scope And Provenance

Scientific review of MqnD product evidence and the unresolved prerequisite for adopting a protein-grounded graph; the native discussion records the gap, not a substitute graph.

Selection: PF02621 selected from its frozen menaquinone-biosynthesis identity and a primary MqnD mechanism study.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF02621 | data/families/PF02621.yaml | generated | PF02621 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF02621 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: concern. Targets: PF02621.

Q9K9F8/BH2689 is a current B. halodurans C-125 MqnD candidate with PF02621 at 1-264, but its UniProt citation is the genome paper. The inspected 2021 main text and supplement name B. halodurans MqnD without an accession, locus or sequence, so the candidate is not treated as the exact clone.

### Directed effects and limits

graph: supported. Targets: PF02621.

The primary product, trapping and isotope experiments support MqnD chemistry, but their adoption is withheld pending construct identity. The native record remains graphless with an open discussion. Oxygen-sensitive naphthoate detection and carbonyl trapping are different assay contexts; proposed microsteps are not all independently observed intermediates.

### Remaining family coverage

completeness: concern. Targets: PF02621.

Resolve the original clone using an accession-bearing construct record, sequence or unambiguous primary link. Other MqnD members, MqnA activity in this family, native roles and mechanistic alternatives remain outside the completed scope. This is not a family-wide lack-of-evidence finding.

## Findings

### additional-contexts: Resolve the experimental MqnD clone before causal graph adoption

minor / open / confirmed; issue key: pf02621-causal-context-coverage.

Obtain an accession-bearing primary construct record, clone sequence or unambiguous mapping for the tested B. halodurans MqnD. Then reassess the family assignment and add only context-specific, evidence-backed edges; do not assign the candidate reference by name alone.

## Recommended Actions And Acceptance Checks

### extend-contexts

Obtain an accession-bearing primary construct record, clone sequence or unambiguous mapping for the tested B. halodurans MqnD. Then reassess the family assignment and add only context-specific, evidence-backed edges; do not assign the candidate reference by name alone.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| experiment | https://par.nsf.gov/servlets/purl/10275113; Main page 3/Figure 4; publisher supplement S6-S7, S25-S26, S31 and rendered S32/Figure S41 | supports | Product characterization and isotope-dependent carbonyl trapping provide substantial chemistry evidence; the unresolved experimental clone identity prevents a protein-grounded canonical edge in this review. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q9K9F8/entry/pfam/PF02621/; Accession and domain locations; paired UniProt identity facts | supports | Q9K9F8/BH2689 is a current B. halodurans C-125 MqnD candidate with PF02621 at 1-264, but its UniProt citation is the genome paper. The inspected 2021 main text and supplement name B. halodurans MqnD without an accession, locus or sequence, so the candidate is not treated as the exact clone. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf02621 | data/families/PF02621.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Main page 3/Figure 4 and supplement S32/Figure S41 were visually inspected; other supplemental plots were read by text/caption only. No raw data were reanalyzed, and exact experimental clone identity remains unresolved.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T053106Z-pf02621-mqnd-identity-gap
title: PF02621 MqnD causal-evidence and identity-gap review
started_at: '2026-10-11T05:30:47Z'
finished_at: '2026-10-11T05:31:06Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent researched and curated the graph; no independent
    expert endorsement.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: true
summary: Primary reaction evidence was reviewed, but no canonical graph was added
  because the 2021 MqnD clone was not resolved to an exact sequence or accession.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF02621.yaml
    sha256: 2f94149ae85fa92b2ea6313b469740e9f65dcf5ac3395b6e9925c54040123bf7
    role: context
  - path: data/families/PF02621.yaml
    sha256: d8c62d0dd47ce290e0d65cb1fe997fc15c5cda0265c0e87ec34c1ed647031335
    role: target
  - path: data/worklists/interpro-pfam-duf-2026-10-10.json
    sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383
    role: context
  - path: data/worklists/interpro-pfam-duf-2026-10-10.manifest.json
    sha256: 31c07ffb6a169c851ea0e6e9dd527a10c04028eafeb29187bd62dc2ae848696e
    role: context
  - path: data/worklists/interpro-pfam-duf-2026-10-10.tsv
    sha256: be023c8dd9d8d3864926b5032d6f7e87a884b1a567391696822dbbecc692dae7
    role: context
  - path: evidence/PF02621/manion-sommerhalter-2021-mqnd.txt
    role: context
    sha256: c4b0e91d9335f5e39a1b9950036494ee9e62d963a3bba994572de1ce89519c75
  - path: evidence/PF02621/Q9K9F8-candidate-identity.txt
    role: context
    sha256: 8184b4fb127707fb29ef47230463d92eb5397a04a5d4cb5f925cfef3b6cab670
targets:
- target_id: PF02621
  path: data/families/PF02621.yaml
  label: PF02621
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF02621.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: a01fb390381fea653aab89a903a8a720a38f51da151611ee64fdac56888cbe94
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific review of MqnD product evidence and the unresolved prerequisite
    for adopting a protein-grounded graph; the native discussion records the gap,
    not a substitute graph.
  selection: PF02621 selected from its frozen menaquinone-biosynthesis identity and
    a primary MqnD mechanism study.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF02621
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Resolve the original clone using an accession-bearing construct record,
      sequence or unambiguous primary link. Other MqnD members, MqnA activity in this
      family, native roles and mechanistic alternatives remain outside the completed
      scope. This is not a family-wide lack-of-evidence finding.
checks:
- check_id: native-projection
  name: Native projection and overlay validation
  command: validate_record(record, root); assert projection graphs and discussions
    match overlay
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Current projection validates and preserves the authored graph and discussion
    content exactly.
  target_ids:
  - PF02621
  evidence_ids:
  - native
evidence:
- evidence_id: experiment
  kind: primary_source
  reference: https://par.nsf.gov/servlets/purl/10275113
  locator: Main page 3/Figure 4; publisher supplement S6-S7, S25-S26, S31 and rendered
    S32/Figure S41
  accessed_at: '2026-10-11T05:31:06Z'
  support: supports
  snapshot_sha256: c4b0e91d9335f5e39a1b9950036494ee9e62d963a3bba994572de1ce89519c75
  summary: Product characterization and isotope-dependent carbonyl trapping provide
    substantial chemistry evidence; the unresolved experimental clone identity prevents
    a protein-grounded canonical edge in this review.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q9K9F8/entry/pfam/PF02621/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T05:31:06Z'
  support: supports
  snapshot_sha256: 8184b4fb127707fb29ef47230463d92eb5397a04a5d4cb5f925cfef3b6cab670
  summary: Q9K9F8/BH2689 is a current B. halodurans C-125 MqnD candidate with PF02621
    at 1-264, but its UniProt citation is the genome paper. The inspected 2021 main
    text and supplement name B. halodurans MqnD without an accession, locus or sequence,
    so the candidate is not treated as the exact clone.
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T05:31:06Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf02621
  kind: record_content
  reference: data/families/PF02621.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T05:31:06Z'
  support: context_only
  snapshot_sha256: d8c62d0dd47ce290e0d65cb1fe997fc15c5cda0265c0e87ec34c1ed647031335
  quote: "id: Pfam:PF02621\npfam_id: PF02621\nname: Menaquinone biosynthesis\nshort_name:\
    \ VitK2_biosynth\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF02621\n\
    counters:\n  proteins: 6058\n  matches: 6185\n  proteomes: 3141\n  taxa: 4752\n\
    \  structures: 13\n  alphafold_models: 3768\n  domain_architectures: 8\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR003773\ndescription: This family includes two enzymes\
    \ which are involved in menaquinone biosynthesis. One which\n  catalyses the conversion\
    \ of cyclic de-hypoxanthine futalosine to 1,4-dihydroxy-6-naphthoate, and one\n\
    \  which may be involved in the conversion of chorismate to futalosine [[cite:PUB00045374]].\
    \ These enzymes\n  comprise two domains with alpha/beta structures, a large domain\
    \ and a small domain. A pocket between\n  the two domains may form the active\
    \ site, a conserved histidine located within this pocket could be\n  the catalytic\
    \ base [[cite:PUB00057460]].\ncuration_history: history/records/PF02621\ndiscussions:\n\
    - discussion_id: mqnd-experimental-clone-identity\n  prompt: Resolve the exact\
    \ accession or sequence of the Bacillus halodurans MqnD construct used in PMID:34143602\n\
    \    before adopting its reaction as a protein-grounded causal graph.\n  kind:\
    \ CURATION_TODO\n  status: OPEN\n  rationale: The paper and inspected supplement\
    \ support reaction chemistry but do not identify the MqnD\n    clone by locus\
    \ or accession. Q9K9F8/BH2689 matches this family and species but remains a candidate,\n\
    \    so no canonical edge is added from that identity assumption.\n  evidence:\n\
    \  - reference: PMID:34143602\n    supports: PARTIAL\n    evidence_source: full_text_and_supplement\n\
    \    explanation: Product and trapping experiments are informative; the remaining\
    \ prerequisite is exact\n      construct-to-family grounding, not absence of biochemical\
    \ evidence.\n  - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q9K9F8/entry/pfam/PF02621/\n\
    \    supports: PARTIAL\n    evidence_source: database\n    explanation: Establishes\
    \ the candidate reference's PF02621 interval, not the experimental clone's\n \
    \     sequence.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n  notes: Inspected-source\
    \ extracts and candidate identity facts are retained under evidence/PF02621. No\n\
    \    graph is hidden in this discussion; MqnA and other MqnD members still need\
    \ separate review.\ncuration_events:\n- timestamp: '2026-10-11T05:25:42Z'\n  curator:\
    \ Codex\n  action: CREATE\n  outcome: changed\n  summary: Retain MqnD construct-identity\
    \ gap without an unsupported graph\n  history_record: history/records/PF02621/2026-10-11T052542Z-codex-c93ea0.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: concern
  summary: Q9K9F8/BH2689 is a current B. halodurans C-125 MqnD candidate with PF02621
    at 1-264, but its UniProt citation is the genome paper. The inspected 2021 main
    text and supplement name B. halodurans MqnD without an accession, locus or sequence,
    so the candidate is not treated as the exact clone.
  target_ids:
  - PF02621
  evidence_ids:
  - identity
  - experiment
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: The primary product, trapping and isotope experiments support MqnD chemistry,
    but their adoption is withheld pending construct identity. The native record remains
    graphless with an open discussion. Oxygen-sensitive naphthoate detection and carbonyl
    trapping are different assay contexts; proposed microsteps are not all independently
    observed intermediates.
  target_ids:
  - PF02621
  evidence_ids:
  - experiment
  - native
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Resolve the original clone using an accession-bearing construct record,
    sequence or unambiguous primary link. Other MqnD members, MqnA activity in this
    family, native roles and mechanistic alternatives remain outside the completed
    scope. This is not a family-wide lack-of-evidence finding.
  target_ids:
  - PF02621
  evidence_ids:
  - experiment
findings:
- finding_id: additional-contexts
  issue_key: pf02621-causal-context-coverage
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the experimental MqnD clone before causal graph adoption
  description: Obtain an accession-bearing primary construct record, clone sequence
    or unambiguous mapping for the tested B. halodurans MqnD. Then reassess the family
    assignment and add only context-specific, evidence-backed edges; do not assign
    the candidate reference by name alone.
  target_ids:
  - PF02621
  field_paths:
  - discussions
  evidence_ids:
  - experiment
  - identity
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF02621.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Obtain an accession-bearing primary construct record, clone sequence
    or unambiguous mapping for the tested B. halodurans MqnD. Then reassess the family
    assignment and add only context-specific, evidence-backed edges; do not assign
    the candidate reference by name alone.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF02621
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Main page 3/Figure 4 and supplement S32/Figure S41 were visually inspected; other
  supplemental plots were read by text/caption only. No raw data were reanalyzed,
  and exact experimental clone identity remains unresolved.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
