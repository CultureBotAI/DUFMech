# PF20352 DUF6647 computational relationship and causal-evidence-gap review

- Review: 20261011T055555Z-pf20352-duf6647-causal-evidence-gap
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T05:55:42Z
- Finished UTC: 2026-10-11T05:55:55Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the primary computational evidence and verified modeled-member identity, but leave the record graphless because the inspected sources do not establish a directed biological effect.

## Scope And Provenance

Scientific assessment of computational evidence, exact modeled-member identity and whether a native causal graph is justified; no experimental characterization or exhaustive family review is claimed.

Selection: DUF6647 selected because its YbeY-like fold description and proposed metallopeptidase-clan relationship invite unsupported substrate-function transfer.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF20352 | data/families/PF20352.yaml | generated | PF20352 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF20352 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF20352.

Figure 11A's A0A2Z2P7G5 resolves to Granulosicoccus antarcticus IMCC3135, locus IMCC3135_28660, sequence version 1, 167 residues, PF20352 at 31-143. The caption says DUF4157, but the figure image labels PF20352 DUF6647 and current accession mapping supports that label. Preserve the discrepancy without silently rewriting the source or claiming a confirmed erratum. A0A017HEP9/Lokhon_01595 was separately verified as another family member, not as an experimentally tested protein.

### Directed effects and limits

graph: supported. Targets: PF20352.

Withholding a graph is supported for the inspected sources. Embedding similarity, conserved HEXXH and superposed side chains do not establish causation, metal binding or a substrate reaction. A hypothetical RNA-cleavage or protease edge would add an untested substrate assumption. The native discussion records the positive computational evidence, caption discrepancy and specific research prerequisite, not a hidden graph or a claim of absent biological function.

### Remaining family coverage

completeness: concern. Targets: PF20352.

The bounded DUF6647/PF20352 function searches and a verified member-alias search found annotation and computational leads but no inspected causal experiment. Other members, older aliases, supplements and all-language literature were not exhaustively investigated. This is partial evidence assessment, not proof that no experimental characterization exists anywhere.

## Findings

### additional-contexts: Obtain member-specific causal evidence for DUF6647

minor / open / confirmed; issue key: pf20352-causal-context-coverage.

Follow verified member and locus aliases to primary biochemical or perturbation studies, resolving constructs and conditions before assigning a substrate or causal relation. Investigate the caption discrepancy without importing DUF4157 or YbeY activities as DUF6647 experiments. Keep the entry graphless until an evidence-backed directed effect can be represented honestly.

## Recommended Actions And Acceptance Checks

### extend-contexts

Follow verified member and locus aliases to primary biochemical or perturbation studies, resolving constructs and conditions before assigning a substrate or causal relation. Investigate the caption discrepancy without importing DUF4157 or YbeY activities as DUF6647 experiments. Keep the entry graphless until an evidence-backed directed effect can be represented honestly.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC11467057/; Methods 2.1-2.2 and 2.4, Results 3.2.1 and 3.3, Figure 11A caption and visually inspected image | supports | The study reports a ProtCNNSim score of 6.81 against DUF4157, conserved motif reasoning and AF2 superposition with a collagenase domain. These are computational relationship observations, not measurements of DUF6647 substrate cleavage, metal loading or phenotype. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/A0A2Z2P7G5/entry/pfam/PF20352/; Accession and domain locations; paired UniProt identity facts | supports | Figure 11A's A0A2Z2P7G5 resolves to Granulosicoccus antarcticus IMCC3135, locus IMCC3135_28660, sequence version 1, 167 residues, PF20352 at 31-143. The caption says DUF4157, but the figure image labels PF20352 DUF6647 and current accession mapping supports that label. Preserve the discrepancy without silently rewriting the source or claiming a confirmed erratum. A0A017HEP9/Lokhon_01595 was separately verified as another family member, not as an experimentally tested protein. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf20352 | data/families/PF20352.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Figure 11A was visually inspected and relevant methods and results were read. The AF2 model, alignments and benchmark were not rerun; raw structural files and supplementary analyses were not independently reviewed. No biological experiment was performed or identified in the inspected source.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T055555Z-pf20352-duf6647-causal-evidence-gap
title: PF20352 DUF6647 computational relationship and causal-evidence-gap review
started_at: '2026-10-11T05:55:42Z'
finished_at: '2026-10-11T05:55:55Z'
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
summary: Retain the primary computational evidence and verified modeled-member identity,
  but leave the record graphless because the inspected sources do not establish a
  directed biological effect.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF20352.yaml
    sha256: f790001890813c98b8a2189dcaa5407234adc4ad9e5fb830648df6ab1c469c5a
    role: context
  - path: data/families/PF20352.yaml
    sha256: 1a6dc2967fcf575dce5e1d30ecf4f9a0d77931a48974f778c4a16f6c0379ab4c
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
  - path: evidence/PF20352/ponamareva-2024-duf6647.txt
    role: context
    sha256: 5ed3dcdb47b0be6d6a346d7ea2d84fcf8eb72056e8e90b6d34e1f5e66f45aa07
  - path: evidence/PF20352/duf6647-identity.txt
    role: context
    sha256: 0495670665170f6fec16caa17cf652b69b119898995675d3da056effa5f2f3b9
targets:
- target_id: PF20352
  path: data/families/PF20352.yaml
  label: PF20352
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF20352.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: bef30f4a84e68595dd9d1aa5ae6bfc3f0e96512c33912ff7c85791c6f032b886
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of computational evidence, exact modeled-member
    identity and whether a native causal graph is justified; no experimental characterization
    or exhaustive family review is claimed.
  selection: DUF6647 selected because its YbeY-like fold description and proposed
    metallopeptidase-clan relationship invite unsupported substrate-function transfer.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF20352
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: The bounded DUF6647/PF20352 function searches and a verified member-alias
      search found annotation and computational leads but no inspected causal experiment.
      Other members, older aliases, supplements and all-language literature were not
      exhaustively investigated. This is partial evidence assessment, not proof that
      no experimental characterization exists anywhere.
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
  - PF20352
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC11467057/
  locator: Methods 2.1-2.2 and 2.4, Results 3.2.1 and 3.3, Figure 11A caption and
    visually inspected image
  accessed_at: '2026-10-11T05:55:55Z'
  support: supports
  snapshot_sha256: 5ed3dcdb47b0be6d6a346d7ea2d84fcf8eb72056e8e90b6d34e1f5e66f45aa07
  summary: The study reports a ProtCNNSim score of 6.81 against DUF4157, conserved
    motif reasoning and AF2 superposition with a collagenase domain. These are computational
    relationship observations, not measurements of DUF6647 substrate cleavage, metal
    loading or phenotype.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/A0A2Z2P7G5/entry/pfam/PF20352/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T05:55:55Z'
  support: supports
  snapshot_sha256: 0495670665170f6fec16caa17cf652b69b119898995675d3da056effa5f2f3b9
  summary: Figure 11A's A0A2Z2P7G5 resolves to Granulosicoccus antarcticus IMCC3135,
    locus IMCC3135_28660, sequence version 1, 167 residues, PF20352 at 31-143. The
    caption says DUF4157, but the figure image labels PF20352 DUF6647 and current
    accession mapping supports that label. Preserve the discrepancy without silently
    rewriting the source or claiming a confirmed erratum. A0A017HEP9/Lokhon_01595
    was separately verified as another family member, not as an experimentally tested
    protein.
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T05:55:55Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf20352
  kind: record_content
  reference: data/families/PF20352.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T05:55:55Z'
  support: context_only
  snapshot_sha256: 1a6dc2967fcf575dce5e1d30ecf4f9a0d77931a48974f778c4a16f6c0379ab4c
  quote: "id: Pfam:PF20352\npfam_id: PF20352\nname: Domain of unknown function (DUF6647)\n\
    short_name: DUF6647\nseed_status: UNKNOWN_CANDIDATE\ncharacterization_status:\
    \ UNSCORED\ncuration_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF20352\n\
    counters:\n  proteins: 187\n  matches: 187\n  proteomes: 172\n  taxa: 345\n  structures:\
    \ 0\n  alphafold_models: 132\n  domain_architectures: 2\nprovenance:\n  snapshot_id:\
    \ interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR046589\ndescription: This family of proteins is functionally\
    \ uncharacterised. This family of proteins is found\n  in bacteria. Proteins in\
    \ this family are typically between 158 and 180 amino acids in length. Proteins\n\
    \  in this family have a metzincin-like fold and are most closely related to the\
    \ structure of the YbeY\n  endoribonuclease proteins.\ncuration_history: history/records/PF20352\n\
    discussions:\n- discussion_id: duf6647-directed-effect-evidence\n  prompt: Establish\
    \ a member-specific biological effect or substrate reaction before adding a DUF6647\n\
    \    causal graph.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: The inspected\
    \ primary study supports a computational relationship to metallopeptidase families,\n\
    \    not a directed biological effect. YbeY-like structure does not establish\
    \ RNA cleavage, and a mini-zincin\n    analogy does not identify a protein substrate\
    \ or metal-dependent catalytic step.\n  evidence:\n  - reference: PMID:39399373\n\
    \    supports: PARTIAL\n    evidence_source: full_text\n    explanation: Methods,\
    \ Section 3.2.1 and visually inspected Figure 11A provide embedding similarity,\n\
    \      motif and model-superposition evidence. These are not experiments measuring\
    \ DUF6647 substrate cleavage\n      or a perturbation phenotype.\n  - reference:\
    \ https://www.ebi.ac.uk/interpro/api/protein/uniprot/A0A2Z2P7G5/entry/pfam/PF20352/\n\
    \    supports: PARTIAL\n    evidence_source: database\n    explanation: The modeled\
    \ Granulosicoccus antarcticus IMCC3135 protein is A0A2Z2P7G5, sequence version\n\
    \      1, 167 residues, PF20352 at 31-143. This validates model identity, not\
    \ experimental function.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n  notes:\
    \ The Figure 11A caption says DUF4157, but its accession and the image label support\
    \ PF20352 DUF6647.\n    Preserve this discrepancy without silently changing the\
    \ paper or frozen family metadata. Minimal primary\n    and identity extracts\
    \ are retained under evidence/PF20352. The bounded family/member search is not\n\
    \    an exhaustive absence claim; no dummy or hidden graph is added.\ncuration_events:\n\
    - timestamp: '2026-10-11T05:52:06Z'\n  curator: Codex\n  action: CREATE\n  outcome:\
    \ changed\n  summary: Retain DUF6647 computational evidence and causal-graph prerequisite\n\
    \  history_record: history/records/PF20352/2026-10-11T055206Z-codex-5a2681.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Figure 11A's A0A2Z2P7G5 resolves to Granulosicoccus antarcticus IMCC3135,
    locus IMCC3135_28660, sequence version 1, 167 residues, PF20352 at 31-143. The
    caption says DUF4157, but the figure image labels PF20352 DUF6647 and current
    accession mapping supports that label. Preserve the discrepancy without silently
    rewriting the source or claiming a confirmed erratum. A0A017HEP9/Lokhon_01595
    was separately verified as another family member, not as an experimentally tested
    protein.
  target_ids:
  - PF20352
  evidence_ids:
  - identity
  - primary
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Withholding a graph is supported for the inspected sources. Embedding similarity,
    conserved HEXXH and superposed side chains do not establish causation, metal binding
    or a substrate reaction. A hypothetical RNA-cleavage or protease edge would add
    an untested substrate assumption. The native discussion records the positive computational
    evidence, caption discrepancy and specific research prerequisite, not a hidden
    graph or a claim of absent biological function.
  target_ids:
  - PF20352
  evidence_ids:
  - primary
  - native
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: The bounded DUF6647/PF20352 function searches and a verified member-alias
    search found annotation and computational leads but no inspected causal experiment.
    Other members, older aliases, supplements and all-language literature were not
    exhaustively investigated. This is partial evidence assessment, not proof that
    no experimental characterization exists anywhere.
  target_ids:
  - PF20352
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf20352-causal-context-coverage
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Obtain member-specific causal evidence for DUF6647
  description: Follow verified member and locus aliases to primary biochemical or
    perturbation studies, resolving constructs and conditions before assigning a substrate
    or causal relation. Investigate the caption discrepancy without importing DUF4157
    or YbeY activities as DUF6647 experiments. Keep the entry graphless until an evidence-backed
    directed effect can be represented honestly.
  target_ids:
  - PF20352
  field_paths:
  - discussions
  evidence_ids:
  - primary
  - identity
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF20352.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Follow verified member and locus aliases to primary biochemical or
    perturbation studies, resolving constructs and conditions before assigning a substrate
    or causal relation. Investigate the caption discrepancy without importing DUF4157
    or YbeY activities as DUF6647 experiments. Keep the entry graphless until an evidence-backed
    directed effect can be represented honestly.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF20352
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Figure 11A was visually inspected and relevant methods and results were read. The
  AF2 model, alignments and benchmark were not rerun; raw structural files and supplementary
  analyses were not independently reviewed. No biological experiment was performed
  or identified in the inspected source.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
