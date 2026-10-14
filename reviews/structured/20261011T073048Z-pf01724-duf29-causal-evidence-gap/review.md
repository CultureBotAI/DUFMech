# Scoped scientific self-review of DUF29 predictions and causal-evidence gaps

- Review: 20261011T073048Z-pf01724-duf29-causal-evidence-gap
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T07:29:16Z
- Finished UTC: 2026-10-11T07:30:48Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No directed causal edge is supported by the inspected DUF29 material. Q2RPE2 and its 3FCN structure are grounded to the family, while metagenomic ORF1 predictions and the distinct TC11pol experiments are not promoted to causal function. A native discussion retains the bounded search and identity limits; status remains IN_PROGRESS.

## Scope And Provenance

Scientific assessment of a graphless disposition using selected thesis sections, primary structural deposition and verified reference-member identity; not an exhaustive DUF29 review.

Selection: PF01724 DUF29, following Q2RPE2/Rru_A3208 structural evidence and the metagenomic ORF1 primary thesis lead.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01724 | data/families/PF01724.yaml | generated | PF01724 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01724 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01724.

Q2RPE2/Rru_A3208 is a 163-residue R. rubrum ATCC 11170/S1 reference, taxon 269796, sequence version 1, with PF01724 at 8-150. UniProt and InterPro sequences agree. The 3FCN canonical entity sequence is one leading G plus this reference, with selenomethionine in the experimental sample. This verified reference mapping does not identify the thesis ORF1 clone, whose modern exact accession and taxon remain unresolved.

### Directed effects and limits

graph: supported. Targets: PF01724.

The empty graph disposition is supported for the inspected evidence set, not a biological claim that DUF29 has no function. The native discussion separates structure, predicted interactions and non-target enzyme assays from directed perturbation evidence. Neither PDB assembly assignment nor a DnaB fusion establishes causal helicase or dimerization-mediated activity. No placeholder edge is added.

### Remaining family coverage

completeness: concern. Targets: PF01724.

Bounded family/member searches and selected thesis pages do not exhaust DUF29 literature or members. Exact ORF1 sequence accession and source taxon, the population-genomics lead and any gene-specific perturbation data remain unresolved. Availability of mutant-library constructs is not a phenotype. Deposited structure coordinates and structure factors were not independently analyzed.

## Findings

### additional-contexts: Obtain member-specific primary causal evidence for DUF29

minor / open / confirmed; issue key: pf01724-causal-context-coverage.

Resolve the metagenomic ORF1 identity and inspect additional verified-member perturbation or substrate experiments. Preserve hypotheses separately from demonstrated effects, and add a graph only when the relation and direction are supported for a mapped DUF29 member with appropriate conditions. Retain a successor review rather than converting the current limited search into a family-wide absence claim.

## Recommended Actions And Acceptance Checks

### extend-contexts

Resolve the metagenomic ORF1 identity and inspect additional verified-member perturbation or substrate experiments. Preserve hypotheses separately from demonstrated effects, and add a graph only when the relation and direction are supported for a mapped DUF29 member with appropriate conditions. Retain a successor review rather than converting the current limited search into a family-wide absence claim.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://hdl.handle.net/10566/13510; Selected PDF pages 131, 156, 159-161 and 199; printed pages 111, 136, 139-141 and 179; Figure 5.12 visually inspected | supports | ORF1 is assigned to DUF29 by sequence comparison. Its proposed nucleotide-related function derives from homology, genomic context and PFP predictions; the thesis explicitly retains low confidence. Figure 5.12 is a prediction workflow, not a measured causal pathway. The separate TC11pol polymerase experiments cannot be attributed to ORF1. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q2RPE2/entry/pfam/PF01724/; Accession and domain locations; paired UniProt identity facts | supports | Q2RPE2/Rru_A3208 is a 163-residue R. rubrum ATCC 11170/S1 reference, taxon 269796, sequence version 1, with PF01724 at 8-150. UniProt and InterPro sequences agree. The 3FCN canonical entity sequence is one leading G plus this reference, with selenomethionine in the experimental sample. This verified reference mapping does not identify the thesis ORF1 clone, whose modern exact accession and taxon remain unresolved. |
| structural-deposition | https://www.rcsb.org/structure/3FCN; PDB entry and polymer-entity API; experimental method, primary citation and exact canonical sequence comparison | supports | The JCSG deposit reports a 1.45 A X-ray structure released in 2008, with primary citation still To be published. The measured structure supports reference identity and architecture, not a directed biochemical or phenotype effect. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01724 | data/families/PF01724.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Thesis Figure 5.12 was visually inspected; selected other sections were inspected as text, not the complete thesis. The PDB deposition metadata and sequence mapping were inspected, not a 3D structure view or raw diffraction data. No DUF29 causal experimental figure was identified in the inspected material.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T073048Z-pf01724-duf29-causal-evidence-gap
title: Scoped scientific self-review of DUF29 predictions and causal-evidence gaps
started_at: '2026-10-11T07:29:16Z'
finished_at: '2026-10-11T07:30:48Z'
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
summary: No directed causal edge is supported by the inspected DUF29 material. Q2RPE2
  and its 3FCN structure are grounded to the family, while metagenomic ORF1 predictions
  and the distinct TC11pol experiments are not promoted to causal function. A native
  discussion retains the bounded search and identity limits; status remains IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01724.yaml
    sha256: c3aed7fc139c444fa9357caa061fa0a3e1dae5b406e8e0b47467b95a4d4d93f4
    role: context
  - path: data/families/PF01724.yaml
    sha256: 936ba86517172f2c3aa054bf38e56d0b8bd5c0a7db2ef75ea6d3d445f844988b
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
  - path: evidence/PF01724/duplessis-2007-duf29-predictions.txt
    role: context
    sha256: 2b4ed916ba058f58bd155ca1acec49342ccc8a5148873eb4501ac5f91f45d89e
  - path: evidence/PF01724/Q2RPE2-3FCN-identity.txt
    role: context
    sha256: fb98c14186e1d33ee68dd6b42860edeb138d62ee9e476599fa722f53ba452d75
targets:
- target_id: PF01724
  path: data/families/PF01724.yaml
  label: PF01724
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01724.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: eab9f4eca1570d04093d321eb8070d43ce6e9c90d337dbb8277b506825b52a23
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of a graphless disposition using selected thesis
    sections, primary structural deposition and verified reference-member identity;
    not an exhaustive DUF29 review.
  selection: PF01724 DUF29, following Q2RPE2/Rru_A3208 structural evidence and the
    metagenomic ORF1 primary thesis lead.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01724
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Bounded family/member searches and selected thesis pages do not exhaust
      DUF29 literature or members. Exact ORF1 sequence accession and source taxon,
      the population-genomics lead and any gene-specific perturbation data remain
      unresolved. Availability of mutant-library constructs is not a phenotype. Deposited
      structure coordinates and structure factors were not independently analyzed.
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
  - PF01724
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://hdl.handle.net/10566/13510
  locator: Selected PDF pages 131, 156, 159-161 and 199; printed pages 111, 136, 139-141
    and 179; Figure 5.12 visually inspected
  accessed_at: '2026-10-11T07:30:48Z'
  support: supports
  snapshot_sha256: 2b4ed916ba058f58bd155ca1acec49342ccc8a5148873eb4501ac5f91f45d89e
  summary: ORF1 is assigned to DUF29 by sequence comparison. Its proposed nucleotide-related
    function derives from homology, genomic context and PFP predictions; the thesis
    explicitly retains low confidence. Figure 5.12 is a prediction workflow, not a
    measured causal pathway. The separate TC11pol polymerase experiments cannot be
    attributed to ORF1.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q2RPE2/entry/pfam/PF01724/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T07:30:48Z'
  support: supports
  snapshot_sha256: fb98c14186e1d33ee68dd6b42860edeb138d62ee9e476599fa722f53ba452d75
  summary: Q2RPE2/Rru_A3208 is a 163-residue R. rubrum ATCC 11170/S1 reference, taxon
    269796, sequence version 1, with PF01724 at 8-150. UniProt and InterPro sequences
    agree. The 3FCN canonical entity sequence is one leading G plus this reference,
    with selenomethionine in the experimental sample. This verified reference mapping
    does not identify the thesis ORF1 clone, whose modern exact accession and taxon
    remain unresolved.
- evidence_id: structural-deposition
  kind: primary_source
  reference: https://www.rcsb.org/structure/3FCN
  locator: PDB entry and polymer-entity API; experimental method, primary citation
    and exact canonical sequence comparison
  summary: The JCSG deposit reports a 1.45 A X-ray structure released in 2008, with
    primary citation still To be published. The measured structure supports reference
    identity and architecture, not a directed biochemical or phenotype effect.
  accessed_at: '2026-10-11T07:30:48Z'
  support: supports
  snapshot_sha256: fb98c14186e1d33ee68dd6b42860edeb138d62ee9e476599fa722f53ba452d75
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T07:30:48Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01724
  kind: record_content
  reference: data/families/PF01724.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T07:30:48Z'
  support: context_only
  snapshot_sha256: 936ba86517172f2c3aa054bf38e56d0b8bd5c0a7db2ef75ea6d3d445f844988b
  quote: "id: Pfam:PF01724\npfam_id: PF01724\nname: Domain of unknown function DUF29\n\
    short_name: DUF29\nseed_status: UNKNOWN_CANDIDATE\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01724\n\
    counters:\n  proteins: 4280\n  matches: 4280\n  proteomes: 791\n  taxa: 1622\n\
    \  structures: 1\n  alphafold_models: 2600\n  domain_architectures: 11\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002636\ndescription: This family consists of various\
    \ hypothetical proteins from cyanobacteria, none of which are\n  functionally\
    \ described. The aligned region is approximately 120-140 amino acids long corresponding\
    \ to\n  almost the entire length of the proteins in the family. [swissprot:Q2RPE2],\
    \ PDB:3fcn, is a small protein\n  that has a novel all-alpha fold. The N-terminal\
    \ helical hairpin is likely to function as a dimerisation\n  module. This protein\
    \ is a member of PFam family PF01724. The function of this protein is unknown.\
    \ One\n  protein sequence contains a fusion of this protein and a DnaB domain,\
    \ suggesting a possible role in\n  DNA helicase activity (hypothetical). Dali\
    \ hits have low Z and high rmsd, suggesting probably only topological\n  similarities\
    \ (not functional relevance) (details derived from TOPSAN). The family has several\
    \ highly\n  conserved sequence motifs, including YD/ExD, DxxNVxEEIE, and CPY/F/W,\
    \ as well as conserved tryptophans.\ncuration_history: history/records/PF01724\n\
    discussions:\n- discussion_id: duf29-member-specific-causal-evidence\n  prompt:\
    \ Obtain a verified DUF29 member-specific perturbation or substrate assay before\
    \ adding a causal\n    graph.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale:\
    \ The inspected primary structural deposit and metagenomic thesis do not establish\
    \ a directed\n    DUF29 effect. All-alpha structure, DnaB fusion, predicted nucleotide\
    \ binding and gene neighborhood\n    are hypotheses or identity context, not causal\
    \ experiments. The thesis Figure 5.12 depicts a function-prediction\n    workflow,\
    \ not a biological causal pathway.\n  evidence:\n  - reference: https://hdl.handle.net/10566/13510\n\
    \    supports: PARTIAL\n    evidence_source: selected_full_text\n    explanation:\
    \ Du Plessis (2007), selected PDF pages 131, 156, 159-161 and 199, maps metagenomic\
    \ ORF1\n      to DUF29 at 9-109 and explicitly retains low-confidence functional\
    \ inference. Figure 5.12 was visually\n      inspected. Separate ORF2/Usp and\
    \ Chapter 6 TC11pol enzyme experiments are not evidence for ORF1\n      activity;\
    \ its modern exact accession and taxon remain unresolved.\n  - reference: doi:10.2210/pdb3fcn/pdb\n\
    \    supports: PARTIAL\n    evidence_source: structural_deposition\n    explanation:\
    \ PDB 3FCN is a 1.45 A structure of Rru_A3208/Q2RPE2. Its canonical 164-residue\
    \ entity\n      sequence is one leading G plus the 163-residue reference; the\
    \ sample contains selenomethionine.\n      The primary citation remains To be\
    \ published. Structure and assembly assignment alone do not demonstrate\n    \
    \  helicase, nucleotide-modification or dimerization-mediated causality.\n  -\
    \ reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q2RPE2/entry/pfam/PF01724/\n\
    \    supports: PARTIAL\n    evidence_source: database\n    explanation: Q2RPE2/Rru_A3208\
    \ from R. rubrum ATCC 11170/S1, taxon 269796, sequence version 1, maps\n     \
    \ to PF01724 at 8-150 inclusive. Exact UniProt/InterPro sequence agreement grounds\
    \ this reference\n      member but does not identify the metagenomic ORF1 clone.\n\
    \  posed_by: Codex\n  posed_date: '2026-10-11'\n  notes: Bounded searches covered\
    \ DUF29/PF01724 with function, mutant, knockout, characterization and\n    activity,\
    \ plus Q2RPE2/Rru_A3208 and sll0742/sll0743/slr0416. No causal edge is supported\
    \ by the inspected\n    material; this is not an exhaustive absence claim. Mutant-library\
    \ availability and a still-uninspected\n    population-genomics lead are not causal\
    \ phenotype evidence. Minimal source and identity assessments\n    are retained\
    \ under evidence/PF01724; no dummy graph is added.\ncuration_events:\n- timestamp:\
    \ '2026-10-11T07:23:30Z'\n  curator: Codex\n  action: CREATE\n  outcome: changed\n\
    \  summary: Retain DUF29 identity and scoped causal-evidence gap\n  history_record:\
    \ history/records/PF01724/2026-10-11T072330Z-codex-42b484.yaml\n  event_index:\
    \ 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Q2RPE2/Rru_A3208 is a 163-residue R. rubrum ATCC 11170/S1 reference, taxon
    269796, sequence version 1, with PF01724 at 8-150. UniProt and InterPro sequences
    agree. The 3FCN canonical entity sequence is one leading G plus this reference,
    with selenomethionine in the experimental sample. This verified reference mapping
    does not identify the thesis ORF1 clone, whose modern exact accession and taxon
    remain unresolved.
  target_ids:
  - PF01724
  evidence_ids:
  - identity
  - primary
  - structural-deposition
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: The empty graph disposition is supported for the inspected evidence set,
    not a biological claim that DUF29 has no function. The native discussion separates
    structure, predicted interactions and non-target enzyme assays from directed perturbation
    evidence. Neither PDB assembly assignment nor a DnaB fusion establishes causal
    helicase or dimerization-mediated activity. No placeholder edge is added.
  target_ids:
  - PF01724
  evidence_ids:
  - primary
  - native
  - structural-deposition
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Bounded family/member searches and selected thesis pages do not exhaust
    DUF29 literature or members. Exact ORF1 sequence accession and source taxon, the
    population-genomics lead and any gene-specific perturbation data remain unresolved.
    Availability of mutant-library constructs is not a phenotype. Deposited structure
    coordinates and structure factors were not independently analyzed.
  target_ids:
  - PF01724
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01724-causal-context-coverage
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Obtain member-specific primary causal evidence for DUF29
  description: Resolve the metagenomic ORF1 identity and inspect additional verified-member
    perturbation or substrate experiments. Preserve hypotheses separately from demonstrated
    effects, and add a graph only when the relation and direction are supported for
    a mapped DUF29 member with appropriate conditions. Retain a successor review rather
    than converting the current limited search into a family-wide absence claim.
  target_ids:
  - PF01724
  field_paths:
  - discussions
  evidence_ids:
  - primary
  - identity
  - structural-deposition
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01724.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Resolve the metagenomic ORF1 identity and inspect additional verified-member
    perturbation or substrate experiments. Preserve hypotheses separately from demonstrated
    effects, and add a graph only when the relation and direction are supported for
    a mapped DUF29 member with appropriate conditions. Retain a successor review rather
    than converting the current limited search into a family-wide absence claim.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01724
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Thesis Figure 5.12 was visually inspected; selected other sections were inspected
  as text, not the complete thesis. The PDB deposition metadata and sequence mapping
  were inspected, not a 3D structure view or raw diffraction data. No DUF29 causal
  experimental figure was identified in the inspected material.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
