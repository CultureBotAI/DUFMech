# PF01938 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review

- Review: 20261023T092558Z-pf01938-c2s4-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-23T09:25:57Z
- Finished UTC: 2026-10-23T09:25:58Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Ten graphs retain32 OBSERVED effects,6 DIRECT,5 INDIRECT and21 UNRESOLVED across3 MECHANISTIC and7 PHENOTYPIC contexts. Four ledgers and two OPEN discussions retain assay-chemistry,construct,induction and coverage limits. Partial same-agent scientific review; IN_PROGRESS,not complete family characterization or publication. Stage 3 (PR #347) grounded Saccharomyces cerevisiae Trl1 (UniProtKB:P09880) in sc-trl1-healing-step-2019.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Ascending uncurated family after PF01936; all8296 records and all existing follow-ups remain in scope.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base fde7d143a6b952fbc63b390cbfc27de38ac7701b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01938 | data/families/PF01938.yaml | generated | PF01938 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01938 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01938.

Frozen TRAM/formerDUF90,IPR002792,EX_DUF andUNSCORED metadata is preserved. Q6M142v1 has69 residues and PF01938 13-67; all11 selected native-numbering residues match and are in-domain. PDB1YVC maps1-69 with an extra terminalL,not the tagged assay construct. Native host is S0001,not an assumed S2 wild type. Vector-derived biochemical termini remain incompletely verified; repeated D25A primer-table purpose labels do not override Figure4/S1 Table variants. Multidomain enzyme annotations are not isolated-TRAM catalytic evidence.

### Directed effects and limits

graph: supported. Targets: PF01938.

Every edge names its measured comparator and conditions. Figure3/5 beacon substrates are explicitly DNA,not RNA. Binding is represented only as complex formation,not activation or downstream remodeling. Native growth deletion/rescue is distinct from biochemical assays and heterologous BX04 rescue. I33A loses RL211 reporter growth with reduced protein abundance yet restores native growth; K62A partially rescues. WT1515 leader genotype differences are not falsely described as identical fluorescence after1515MT mutation. Cold-shock signals are transient genotype-context observations,not a direct TRAM temperature-sensing pathway. No unsupported transcriptome-to-growth or autoregulatory chain is created.

### Remaining family coverage

completeness: concern. Targets: PF01938.

R15 member accession mapping and2017 figures/supplement remain followups;2017 uninduced3066 reporter activity versus induced inhibition is compatible with the2019 induced negative and is not unconditional contradiction. Ctr3 and2025 PyTRAM require primary assay/mapping work. Multidomain MiaB,RimO,RumA,RlmCD,Trm2,CDKAL1/CDK5RAP1 contexts remain open. One capped500-entry UniProt page is not a census; raw RNA-seq/RIP and all35071 family proteins were not reviewed exhaustively.

### Cycle 2 causal-graph partner and substrate protein grounding

identity: supported. Targets: PF01938.

Stage 3 (PR #347) grounded Saccharomyces cerevisiae Trl1 (UniProtKB:P09880) in sc-trl1-healing-step-2019.

## Findings

### additional-contexts: Extend native-RNA and other-member evidence without assay transfer

minor / open / confirmed; issue key: pf01938-causal-context-coverage.

Map R15,Ctr3 andPyTRAM tested accessions; inspect their full primary assays and relevant figures/supplements. Preserve induction dependence,RNase contamination and the separate PyCsp identity. For enzyme fusions,resolve domain-specific contribution before catalytic edges. Clarify tagged-construct sequences,mutant abundance/folding and direct native RNA/transcription steps; curate additional transcriptome contexts only with scoped causal support. Preserve all existing followups and IN_PROGRESS.

## Recommended Actions And Acceptance Checks

### extend-contexts

Map R15,Ctr3 andPyTRAM tested accessions; inspect their full primary assays and relevant figures/supplements. Preserve induction dependence,RNase contamination and the separate PyCsp identity. For enzyme fusions,resolve domain-specific contribution before catalytic edges. Clarify tagged-construct sequences,mutant abundance/folding and direct native RNA/transcription steps; curate additional transcriptome contexts only with scoped causal support. Preserve all existing followups and IN_PROGRESS.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/; Figures1,3,4,5,S2,S4,S7 visually inspected; relevant Results/Methods and S1/S2 tables read. | supports | RNA complex formation and DNA-beacon fluorescence are direct molecular assay effects. Native growth,RL211 reporter growth,UTR-mCherry fluorescence and heterologous cold rescue remain separate effects. Variant experiments do not supply direct purified-mutant RNA-unfolding measurements. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01938/protein/uniprot/Q6M142/; Accession and domain locations; paired UniProt identity facts | supports | Frozen TRAM/formerDUF90,IPR002792,EX_DUF andUNSCORED metadata is preserved. Q6M142v1 has69 residues and PF01938 13-67; all11 selected native-numbering residues match and are in-domain. PDB1YVC maps1-69 with an extra terminalL,not the tagged assay construct. Native host is S0001,not an assumed S2 wild type. Vector-derived biochemical termini remain incompletely verified; repeated D25A primer-table purpose labels do not override Figure4/S1 Table variants. Multidomain enzyme annotations are not isolated-TRAM catalytic evidence. |
| induction-context | https://pmc.ncbi.nlm.nih.gov/articles/PMC5572242/; Relevant2017 Results,Methods and Figure3/5 captions. | supports | R15 reporter effects depend on IPTG induction; RNase-assisted RNA loss does not identify intrinsic TRAM RNase. Exact member mapping and visual followup remain open. |
| source-coverage | evidence/PF01938/coverage.txt; Scoped local search and member/source followup ledger. | supports | The native MMP0076 curation is supported but not exhaustive; other proteins,enzyme-domain transfer and direct native RNA mechanisms remain open. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| stage4-prior-review | reviews/structured/20261021T114819Z-pf01938-stage4-record-review/review.yaml; Predecessor structured review 20261021T114819Z-pf01938-stage4-record-review | supports | Predecessor review 20261021T114819Z-pf01938-stage4-record-review verified and linked for finding continuity and semantic-digest progression on PF01938. |
| duf-projection-pf01938 | data/families/PF01938.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Figures1,3,4,5,S2,S4,S7 visually checked;S1/S2 DOCX tables parsed,not fully page-rendered.2017 text/captions were inspected without independent figure-pixel review. S3 SPR image and raw RNA-seq/RIP datasets were not independently analyzed.2025 full-text request redirected to abstract. No clone resequencing,experimental replication,independent expert review or full family census.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261023T092558Z-pf01938-c2s4-record-review
title: PF01938 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review
started_at: '2026-10-23T09:25:57Z'
finished_at: '2026-10-23T09:25:58Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Claude-Opus-4.6
  independence: self_review
  independence_basis: Cycle 2 Stage 4 frozen-inventory record review by Antigravity
    auditing prior Codex/Antigravity curation overlays, primary evidence caches, history
    events, and current projections at Git revision fde7d143a6b952fbc63b390cbfc27de38ac7701b.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: true
summary: 'Ten graphs retain32 OBSERVED effects,6 DIRECT,5 INDIRECT and21 UNRESOLVED
  across3 MECHANISTIC and7 PHENOTYPIC contexts. Four ledgers and two OPEN discussions
  retain assay-chemistry,construct,induction and coverage limits. Partial same-agent
  scientific review; IN_PROGRESS,not complete family characterization or publication.
  Stage 3 (PR #347) grounded Saccharomyces cerevisiae Trl1 (UniProtKB:P09880) in sc-trl1-healing-step-2019.'
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: fde7d143a6b952fbc63b390cbfc27de38ac7701b
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01938.yaml
    sha256: 23794399b55f66f796b157b0fe751f4e371e1cf000b7d4866b5e4f05d06e0488
    role: context
  - path: data/families/PF01938.yaml
    sha256: 8e22f23c40a8f5d16b92617dc04f668b0bb569ffb59d3cffe9b4f05e3136f41c
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
  - path: evidence/PF01938/coverage.txt
    sha256: db4377fc59a3c2236f3576503bddb67698323da8d124de39022251b607fc0969
    role: context
  - path: evidence/PF01938/identity.txt
    sha256: 024a6885238d3257b046088da6746c0577c8b8dafb1c38d9fa1dccc73b89339b
    role: context
  - path: evidence/PF01938/li-2019.txt
    sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3
    role: context
  - path: evidence/PF01938/zhang-2017.txt
    sha256: 7c52f41e47be80c9454125793a51cc864b8f86c4e2ffab05a9881a5742c06438
    role: context
  - path: reviews/structured/20261021T114819Z-pf01938-stage4-record-review/review.yaml
    sha256: d39f6102c431faab739d7a73d75dc525a686c97590768b0acb165999754e85c7
    role: context
targets:
- target_id: PF01938
  path: data/families/PF01938.yaml
  label: PF01938
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01938.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 6861ed2fa7b6a95d704c3241846d1b33129e9178a565cb3e881f75ef715c204c
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Ascending uncurated family after PF01936; all8296 records and all existing
    follow-ups remain in scope.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01938
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: R15 member accession mapping and2017 figures/supplement remain followups;2017
      uninduced3066 reporter activity versus induced inhibition is compatible with
      the2019 induced negative and is not unconditional contradiction. Ctr3 and2025
      PyTRAM require primary assay/mapping work. Multidomain MiaB,RimO,RumA,RlmCD,Trm2,CDKAL1/CDK5RAP1
      contexts remain open. One capped500-entry UniProt page is not a census; raw
      RNA-seq/RIP and all35071 family proteins were not reviewed exhaustively.
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
  - PF01938
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/
  locator: Figures1,3,4,5,S2,S4,S7 visually inspected; relevant Results/Methods and
    S1/S2 tables read.
  accessed_at: '2026-10-12T05:29:35Z'
  support: supports
  snapshot_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3
  summary: RNA complex formation and DNA-beacon fluorescence are direct molecular
    assay effects. Native growth,RL211 reporter growth,UTR-mCherry fluorescence and
    heterologous cold rescue remain separate effects. Variant experiments do not supply
    direct purified-mutant RNA-unfolding measurements.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01938/protein/uniprot/Q6M142/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-12T05:29:35Z'
  support: supports
  snapshot_sha256: 024a6885238d3257b046088da6746c0577c8b8dafb1c38d9fa1dccc73b89339b
  summary: Frozen TRAM/formerDUF90,IPR002792,EX_DUF andUNSCORED metadata is preserved.
    Q6M142v1 has69 residues and PF01938 13-67; all11 selected native-numbering residues
    match and are in-domain. PDB1YVC maps1-69 with an extra terminalL,not the tagged
    assay construct. Native host is S0001,not an assumed S2 wild type. Vector-derived
    biochemical termini remain incompletely verified; repeated D25A primer-table purpose
    labels do not override Figure4/S1 Table variants. Multidomain enzyme annotations
    are not isolated-TRAM catalytic evidence.
- evidence_id: induction-context
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5572242/
  locator: Relevant2017 Results,Methods and Figure3/5 captions.
  summary: R15 reporter effects depend on IPTG induction; RNase-assisted RNA loss
    does not identify intrinsic TRAM RNase. Exact member mapping and visual followup
    remain open.
  accessed_at: '2026-10-12T05:29:35Z'
  support: supports
  snapshot_sha256: 7c52f41e47be80c9454125793a51cc864b8f86c4e2ffab05a9881a5742c06438
- evidence_id: source-coverage
  kind: search
  reference: evidence/PF01938/coverage.txt
  locator: Scoped local search and member/source followup ledger.
  search_scope: PF01938,DUF90,TRAM,MMP0076,Mpsy loci,Ctr3,PyTRAM and current Pfam/UniProt/PDB
    records; local search included ignored/hidden text paths but excluded inputs/JSON.
  summary: The native MMP0076 curation is supported but not exhaustive; other proteins,enzyme-domain
    transfer and direct native RNA mechanisms remain open.
  accessed_at: '2026-10-12T05:29:35Z'
  support: supports
  snapshot_sha256: db4377fc59a3c2236f3576503bddb67698323da8d124de39022251b607fc0969
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-12T05:29:35Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: stage4-prior-review
  kind: prior_review
  reference: reviews/structured/20261021T114819Z-pf01938-stage4-record-review/review.yaml
  locator: Predecessor structured review 20261021T114819Z-pf01938-stage4-record-review
  accessed_at: '2026-10-23T09:25:58Z'
  support: supports
  snapshot_sha256: d39f6102c431faab739d7a73d75dc525a686c97590768b0acb165999754e85c7
  summary: Predecessor review 20261021T114819Z-pf01938-stage4-record-review verified
    and linked for finding continuity and semantic-digest progression on PF01938.
- evidence_id: duf-projection-pf01938
  kind: record_content
  reference: data/families/PF01938.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-23T09:25:58Z'
  support: context_only
  snapshot_sha256: 8e22f23c40a8f5d16b92617dc04f668b0bb569ffb59d3cffe9b4f05e3136f41c
  quote: "id: Pfam:PF01938\npfam_id: PF01938\nname: TRAM domain\nshort_name: TRAM\n\
    seed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status: IN_PROGRESS\n\
    source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01938\ncounters:\n\
    \  proteins: 35071\n  matches: 35074\n  proteomes: 19606\n  taxa: 31439\n  structures:\
    \ 18\n  alphafold_models: 24317\n  domain_architectures: 123\nprovenance:\n  snapshot_id:\
    \ interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002792\ndescription: This small domain has no known function.\
    \ However it may perform a nucleic acid binding role\n  (Bateman A. unpublished\
    \ observation).\ncuration_history: history/records/PF01938\ndiscussions:\n- discussion_id:\
    \ pf01938-native-rna-mechanism\n  prompt: Resolve the native RNA-remodeling steps\
    \ without relabeling DNA beacons or reporter phenotypes\n    as direct RNA transcription\
    \ measurements.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: RNA binding,\
    \ DNA-beacon fluorescence, reporter growth, mCherry fluorescence and native growth\n\
    \    are distinct measurements with unresolved connecting steps.\n  evidence:\n\
    \  - reference: PMID:31404065\n    supports: PARTIAL\n    evidence_source: primary_figures_methods_and_supplement\n\
    \    explanation: Figures3C/5A use oligodeoxynucleotides. Figure4 mutant tests\
    \ are cellular reporters and\n      complementation, not directly measured mutant\
    \ RNA-unfolding reactions. I33A abundance and host-dependent\n      rescue matter.\n\
    \  posed_by: Codex\n  posed_date: '2026-10-12'\n  notes: Preserve reference Q6M142\
    \ numbering versus tagged constructs, S0001 versus S2 reference identity,\n  \
    \  repeated D25A primer-table labels, and50/100ug/mL ampicillin discrepancy. RNA-seq\
    \ and RIP do not independently\n    establish every direct target or feedback\
    \ edge.\n- discussion_id: pf01938-other-members-and-induction\n  prompt: Extend\
    \ accession-mapped archaeal and multidomain TRAM contexts with their actual induction\
    \ and\n    domain boundaries.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale:\
    \ MMP0076 does not characterize all35071 proteins and123 architectures; R15 induction\
    \ dependence\n    must not become an unconditional contradiction.\n  evidence:\n\
    \  - reference: PMID:28878753\n    supports: PARTIAL\n    evidence_source: primary_text_and_captions\n\
    \    explanation: R15 TRAM3066 supports RL211 growth without IPTG but not after\
    \ induction. RNase-assisted\n      PP6 loss is not intrinsic TRAM RNase activity.\n\
    \  - reference: PMID:40325874\n    supports: PARTIAL\n    evidence_source: primary_abstract_only\n\
    \    explanation: PyTRAM native cold-growth and RNA-chaperone work requires exact\
    \ mapping and full assay\n      inspection; PYCH_0765 is the separate PyCsp.\n\
    \  posed_by: Codex\n  posed_date: '2026-10-12'\n  notes: Follow up Ctr3 PMID26769275\
    \ and MiaB/RimO/RumA/RlmCD/Trm2/CDKAL1/CDK5RAP1 domain-specific work.\n    One\
    \ capped500-entry member page is not complete coverage. See evidence/PF01938/coverage.txt.\n\
    causal_graphs:\n- graph_id: tram0076-native-growth-37c-2019\n  title: MMP0076\
    \ supports native growth at37C\n  scope: Li2019 Figure1A; M. maripaludis S0001-derived\
    \ deletion and complementation strains.\n  context: MMP0076 replaced with pac;\
    \ pMEV2-0076 rescue and empty-vector controls. Pre-reduced DSMZ141,40mM\n    formate,N2/CO2\
    \ 80:20 at0.1MPa,37C; triplicate OD600 growth curves.\n  family_mapping: Reference\
    \ MMP0076 is Q6M142v1,69aa,PF01938 13-67. Assayed host is S0001,not an assumed\n\
    \    S2 wild-type culture. Whole stand-alone protein is deleted or expressed,not\
    \ isolated13-67.\n  scope_status: PHENOTYPIC\n  limitations: Growth is a distal\
    \ phenotype. Adjacent-gene RNA levels are unchanged and complementation\n    supports\
    \ locus specificity,not every molecular intermediate. The mutant still grows.\n\
    \  nodes:\n  - node_id: deletion\n    label: MMP0076 deletion instead of parental\
    \ S0001\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q6M142\n\
    \  - node_id: rescue\n    label: WT MMP0076 supplied to deletion strain\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:Q6M142\n  - node_id: growth\n\
    \    label: Native exponential growth rate at37C\n    node_type: PHENOTYPE\n \
    \ edges:\n  - edge_id: deletion-growth-reduction\n    subject: deletion\n    predicate:\
    \ decreases\n    object: growth\n    mechanism: The deletion reduces the measured\
    \ rate from0.15 to0.065h^-1 without establishing which\n      RNA defect mediates\
    \ the growth effect.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet: Growth of\
    \ strain\n      explanation: Figure1A and growth/deletion Methods; triplicate\
    \ cultures and empty-vector controls.\n        Measured growth-rate contrast,\
    \ not inferred RNA chemistry.\n      cache_path: evidence/PF01938/li-2019.txt\n\
    \      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    \  - edge_id: complementation-growth-increase\n    subject: rescue\n    predicate:\
    \ increases\n    object: growth\n    mechanism: Plasmid-borne WT MMP0076 restores\
    \ growth kinetics toward parental levels compared with\n      the deletion strain\
    \ control.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet: Growth of\
    \ strain\n      explanation: Figure1A WT complementation curve and Methods; do\
    \ not confuse this rescue with failure\n        of individual substitutions in\
    \ Figure4D.\n      cache_path: evidence/PF01938/li-2019.txt\n      cache_sha256:\
    \ 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n- graph_id:\
    \ tram0076-native-growth-22c-2019\n  title: MMP0076 deletion slows native growth\
    \ at22C\n  scope: Li2019 Figure1C; parental S0001 versus delta0076.\n  context:\
    \ Native archaeal OD600 growth curves at22C,triplicate cultures; routine formate-containing\
    \ DSMZ141\n    and N2/CO2 gas conditions as described in Methods.\n  family_mapping:\
    \ MMP0076 maps to Q6M142v1,69aa,PF01938 13-67. Whole-protein deletion in S0001,not\
    \ a domain-specific\n    knockout or heterologous BX04 rescue.\n  scope_status:\
    \ PHENOTYPIC\n  limitations: No22C complementation curve is shown. Lower growth\
    \ also occurs at37C,so the gene is not\n    demonstrated to act only during cold\
    \ stress.\n  nodes:\n  - node_id: deletion\n    label: MMP0076 deletion instead\
    \ of parental S0001\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q6M142\n\
    \  - node_id: growth\n    label: Native exponential growth rate at22C\n    node_type:\
    \ PHENOTYPE\n  edges:\n  - edge_id: deletion-cool-growth-reduction\n    subject:\
    \ deletion\n    predicate: decreases\n    object: growth\n    mechanism: Deletion\
    \ lowers the measured growth rate from0.042 to0.023h^-1 under the tested cool-growth\n\
    \      conditions.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet: Growth of\
    \ strain\n      explanation: Figure1C growth comparison; Figure1A rescue is a\
    \ separate37C context. Distinct cool-growth\n        comparison.\n      cache_path:\
    \ evidence/PF01938/li-2019.txt\n      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    - graph_id: tram0076-rna-complexes-2019\n  title: Purified TRAM0076 forms shifted\
    \ RNA complexes\n  scope: Li2019 Figure3A PP1 and PP10 rEMSA reactions.\n  context:\
    \ Purified His6-tagged protein and3-prime-biotin RNA,20uL,25C20min. PP1 5nM plus0/25/50uM\
    \ protein;\n    PP10 10nM plus0/50/100uM protein; free-probe controls.\n  family_mapping:\
    \ Full Q6M142-reference MMP0076,PF01938 13-67,expressed from pET28a in BL21(DE3)pLysS.\n\
    \    Vector-derived termini are not fully sequence-verified; not isolated13-67\
    \ or exactly the PDB1YVC construct.\n  scope_status: MECHANISTIC\n  limitations:\
    \ Complex formation is not activation, cleavage or RNA melting. High protein:RNA\
    \ ratios and\n    assay-dependent apparent affinities remain explicit; no claim\
    \ of identical affinity for all possible\n    RNAs.\n  nodes:\n  - node_id: pp1\n\
    \    label: Tagged TRAM0076 added to PP1 RNA\n    node_type: ACTIVITY\n    grounding:\n\
    \    - UniProtKB:Q6M142\n  - node_id: pp10\n    label: Tagged TRAM0076 added to\
    \ PP10 RNA\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:Q6M142\n\
    \  - node_id: complex1\n    label: Shifted PP1 RNA complex\n    node_type: STATE\n\
    \    grounding:\n    - UniProtKB:Q6M142\n  - node_id: complex10\n    label: Shifted\
    \ PP10 RNA complex\n    node_type: STATE\n    grounding:\n    - UniProtKB:Q6M142\n\
    \  edges:\n  - edge_id: pp1-complex-formation\n    subject: pp1\n    predicate:\
    \ produces\n    object: complex1\n    mechanism: Protein addition produces a slower-migrating\
    \ PP1 complex compared with free RNA under the\n      defined binding conditions.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:31404065\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n\
    \      snippet: RNA binding\n      explanation: Figure3A PP1 lanes and rEMSA Methods;\
    \ molecular binding observation,not a downstream\n        causal activation inferred\
    \ from association.\n      cache_path: evidence/PF01938/li-2019.txt\n      cache_sha256:\
    \ 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n  - edge_id:\
    \ pp10-complex-formation\n    subject: pp10\n    predicate: produces\n    object:\
    \ complex10\n    mechanism: Protein addition produces a slower-migrating PP10\
    \ complex compared with its free-probe\n      control.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:31404065\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n\
    \      snippet: RNA binding\n      explanation: Figure3A PP10 lanes with matched10nM\
    \ RNA and50/100uM protein; distinct from PP1 concentrations.\n      cache_path:\
    \ evidence/PF01938/li-2019.txt\n      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    - graph_id: tram0076-dna-duplex-beacon-2019\n  title: TRAM0076 increases DNA-duplex\
    \ beacon fluorescence\n  scope: Li2019 Figure3C; purified WT protein and partially\
    \ complementary DNA oligos.\n  context: FITC/BHQ1 oligos annealed after95C5min\
    \ and cooling to4C;20pmol substrate,20uM protein,200uL,200mM\n    Tris-Cl pH7.5,10mM\
    \ MgCl2,room temperature;460/515nm readout.\n  family_mapping: His6-tagged full\
    \ MMP0076 preparation,reference Q6M142v1 PF01938 13-67. Purified construct\n \
    \   termini are not completely sequence-verified; not an isolated domain or a\
    \ mutant assay.\n  scope_status: MECHANISTIC\n  limitations: Substrates are DNA,not\
    \ RNA. Fluorescence supports duplex-opening activity under this assay\n    but\
    \ does not directly resolve native RNA melting,ATP-dependent helicase chemistry\
    \ or every dye-binding\n    alternative.\n  nodes:\n  - node_id: reaction\n  \
    \  label: WT TRAM0076 added to annealed DNA beacon\n    node_type: ACTIVITY\n\
    \    grounding:\n    - UniProtKB:Q6M142\n  - node_id: fluorescence\n    label:\
    \ Relative FITC beacon fluorescence\n    node_type: STATE\n  edges:\n  - edge_id:\
    \ dna-beacon-fluorescence-increase\n    subject: reaction\n    predicate: increases\n\
    \    object: fluorescence\n    mechanism: Purified protein addition raises fluorescence\
    \ from the13% annealed baseline to about54%\n      of heat-denatured signal,consistent\
    \ with relief of duplex-associated quenching.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet:\
    \ two partially complementary oligodeoxynucleotides\n      explanation: Figure3C\
    \ and nucleic-acid unfolding Methods explicitly establish DNA chemistry; CspA/CspE\n\
    \        and annealed/denatured controls.\n      cache_path: evidence/PF01938/li-2019.txt\n\
    \      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    - graph_id: tram0076-utr-dna-beacons-2019\n  title: TRAM0076 increases UTR-sequence\
    \ DNA-beacon signals\n  scope: Li2019 Figure5A; DNA versions of three transcript\
    \ leaders.\n  context: FITC/BHQ1-labeled MMP0127,1515,1697 leader-sequence DNA\
    \ oligos;20pmol substrate,20uM tagged\n    protein,200uL,200mM Tris-Cl pH7.5,10mM\
    \ MgCl2,room temperature,460/515nm,annealed and Csp controls.\n  family_mapping:\
    \ Full tagged MMP0076,reference Q6M142v1,PF01938 13-67. The UTR gene identifiers\
    \ specify\n    substrate sequences,not additional TRAM family members.\n  scope_status:\
    \ MECHANISTIC\n  limitations: These are oligodeoxynucleotides despite RNA-oriented\
    \ Results wording and predicted RNA\n    diagrams. Fluorescence is a direct assay\
    \ effect,not direct visualization of native transcript folding\n    or transcription.\n\
    \  nodes:\n  - node_id: dna0127\n    label: WT TRAM0076 plus annealed UTR0127\
    \ DNA beacon\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:Q6M142\n\
    \  - node_id: dna1515\n    label: WT TRAM0076 plus annealed UTR1515 DNA beacon\n\
    \    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:Q6M142\n  - node_id:\
    \ dna1697\n    label: WT TRAM0076 plus annealed UTR1697 DNA beacon\n    node_type:\
    \ ACTIVITY\n    grounding:\n    - UniProtKB:Q6M142\n  - node_id: signal0127\n\
    \    label: UTR0127 DNA-beacon fluorescence\n    node_type: STATE\n  - node_id:\
    \ signal1515\n    label: UTR1515 DNA-beacon fluorescence\n    node_type: STATE\n\
    \  - node_id: signal1697\n    label: UTR1697 DNA-beacon fluorescence\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: utr0127-beacon-increase\n    subject: dna0127\n\
    \    predicate: increases\n    object: signal0127\n    mechanism: WT protein raises\
    \ the0127 DNA-beacon signal relative to its annealed control,consistent\n    \
    \  with reduced quenching.\n    directness: DIRECT\n    support: OBSERVED\n  \
    \  evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet:\
    \ two partially complementary oligodeoxynucleotides\n      explanation: Figure5A\
    \ UTR0127 and the Methods paragraph specifying three leader oligodeoxynucleotides;\n\
    \        not RNA melting measured directly.\n      cache_path: evidence/PF01938/li-2019.txt\n\
    \      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    \  - edge_id: utr1515-beacon-increase\n    subject: dna1515\n    predicate: increases\n\
    \    object: signal1515\n    mechanism: WT protein raises the1515 DNA-beacon signal\
    \ relative to its annealed control.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet:\
    \ two partially complementary oligodeoxynucleotides\n      explanation: Figure5A\
    \ UTR1515 and nucleic-acid unfolding Methods; not the cellular UTR1515MT reporter\n\
    \        experiment.\n      cache_path: evidence/PF01938/li-2019.txt\n      cache_sha256:\
    \ 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n  - edge_id:\
    \ utr1697-beacon-increase\n    subject: dna1697\n    predicate: increases\n  \
    \  object: signal1697\n    mechanism: WT protein raises the1697 DNA-beacon signal\
    \ relative to its annealed control; activity\n      is not assumed identical to\
    \ the other leaders.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet: two partially\
    \ complementary oligodeoxynucleotides\n      explanation: Figure5A UTR1697; retain\
    \ the distinct substrate and lower signal rather than a universal\n        quantitative\
    \ effect.\n      cache_path: evidence/PF01938/li-2019.txt\n      cache_sha256:\
    \ 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n- graph_id:\
    \ tram0076-rl211-reporter-2019\n  title: TRAM0076 expression and variants alter\
    \ RL211 reporter growth\n  scope: Li2019 Figures3B and4C; E. coli RL211 trpL-cat\
    \ reporter.\n  context: pINIII constructs,1mM IPTG,30ug/mL chloramphenicol,37C2-3days,matched\
    \ minus-Cm growth controls.\n    Figure3 caption gives50ug/mL ampicillin; Methods\
    \ gives100ug/mL.\n  family_mapping: MMP0076 Q6M142v1,PF01938 13-67; I33,R35,F39,F42,K62,F63,F65\
    \ all lie in the match and\n    are separately changed to alanine. Host is E.\
    \ coli; protein origin is M. maripaludis.\n  taxon: NCBITaxon:562\n  scope_status:\
    \ PHENOTYPIC\n  limitations: Reporter growth supports an antitermination interpretation\
    \ without directly measuring the\n    RNA hairpin. I33A abundance is reduced;\
    \ folding/abundance effects are not excluded for every mutant.\n    D25A,K28A,G30A,G32A\
    \ retain activity. Induced TRAM3066 is a different protein and condition-specific\n\
    \    negative.\n  nodes:\n  - node_id: wt\n    label: WT TRAM0076 instead of empty\
    \ pINIII\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q6M142\n\
    \  - node_id: i33a\n    label: I33A instead of WT TRAM0076\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q6M142\n  - node_id: r35a\n    label: R35A instead\
    \ of WT TRAM0076\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q6M142\n\
    \  - node_id: f39a\n    label: F39A instead of WT TRAM0076\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q6M142\n  - node_id: f42a\n    label: F42A instead\
    \ of WT TRAM0076\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q6M142\n\
    \  - node_id: k62a\n    label: K62A instead of WT TRAM0076\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q6M142\n  - node_id: f63a\n    label: F63A instead\
    \ of WT TRAM0076\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q6M142\n\
    \  - node_id: f65a\n    label: F65A instead of WT TRAM0076\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q6M142\n  - node_id: growth\n    label: Growth\
    \ of induced RL211 on chloramphenicol\n    node_type: PHENOTYPE\n  edges:\n  -\
    \ edge_id: wt-reporter-growth-increase\n    subject: wt\n    predicate: increases\n\
    \    object: growth\n    mechanism: Expressed WT TRAM0076 improves growth on chloramphenicol\
    \ compared with empty vector in\n      the terminator-linked reporter strain.\n\
    \    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:31404065\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n\
    \      snippet: chloramphenicol resistance\n      explanation: Figure3B WT versus\
    \ pINIII and Figure4C controls; reporter observation is not a purified\n     \
    \   RNA reaction.\n      cache_path: evidence/PF01938/li-2019.txt\n      cache_sha256:\
    \ 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n  - edge_id:\
    \ i33a-reporter-growth-reduction\n    subject: i33a\n    predicate: decreases\n\
    \    object: growth\n    mechanism: I33A lowers +Cm reporter growth relative to\
    \ WT; reduced protein abundance is a material\n      alternative to a specific\
    \ catalytic defect.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet: chloramphenicol\
    \ resistance\n      explanation: Figure4C I33A and Results abundance qualification;\
    \ I33A does rescue native growth and\n        is not included among failed native\
    \ variants.\n      cache_path: evidence/PF01938/li-2019.txt\n      cache_sha256:\
    \ 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n  - edge_id:\
    \ r35a-reporter-growth-reduction\n    subject: r35a\n    predicate: decreases\n\
    \    object: growth\n    mechanism: Individual R35A replacement reduces induced\
    \ +Cm reporter growth relative to WT.\n    directness: UNRESOLVED\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet:\
    \ chloramphenicol resistance\n      explanation: Figure4C R35A,+Cm versus WT with\
    \ -Cm control; no direct-mutant beacon result asserted.\n      cache_path: evidence/PF01938/li-2019.txt\n\
    \      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    \  - edge_id: f39a-reporter-growth-reduction\n    subject: f39a\n    predicate:\
    \ decreases\n    object: growth\n    mechanism: Individual F39A replacement reduces\
    \ induced +Cm reporter growth relative to WT.\n    directness: UNRESOLVED\n  \
    \  support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:31404065\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n\
    \      snippet: chloramphenicol resistance\n      explanation: Figure4C F39A with\
    \ matched -Cm viability control.\n      cache_path: evidence/PF01938/li-2019.txt\n\
    \      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    \  - edge_id: f42a-reporter-growth-reduction\n    subject: f42a\n    predicate:\
    \ decreases\n    object: growth\n    mechanism: Individual F42A replacement reduces\
    \ induced +Cm reporter growth relative to WT.\n    directness: UNRESOLVED\n  \
    \  support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:31404065\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n\
    \      snippet: chloramphenicol resistance\n      explanation: Figure4C F42A with\
    \ matched -Cm viability control.\n      cache_path: evidence/PF01938/li-2019.txt\n\
    \      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    \  - edge_id: k62a-reporter-growth-reduction\n    subject: k62a\n    predicate:\
    \ decreases\n    object: growth\n    mechanism: Individual K62A replacement reduces\
    \ induced +Cm reporter growth relative to WT; it is not\n      fully inactive\
    \ in the separate native-growth assay.\n    directness: UNRESOLVED\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet:\
    \ chloramphenicol resistance\n      explanation: Figure4C K62A; native partial\
    \ rescue in4D is retained separately.\n      cache_path: evidence/PF01938/li-2019.txt\n\
    \      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    \  - edge_id: f63a-reporter-growth-reduction\n    subject: f63a\n    predicate:\
    \ decreases\n    object: growth\n    mechanism: Individual F63A replacement reduces\
    \ induced +Cm reporter growth relative to WT.\n    directness: UNRESOLVED\n  \
    \  support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:31404065\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n\
    \      snippet: chloramphenicol resistance\n      explanation: Figure4C F63A with\
    \ matched -Cm viability control.\n      cache_path: evidence/PF01938/li-2019.txt\n\
    \      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    \  - edge_id: f65a-reporter-growth-reduction\n    subject: f65a\n    predicate:\
    \ decreases\n    object: growth\n    mechanism: Individual F65A replacement reduces\
    \ induced +Cm reporter growth relative to WT.\n    directness: UNRESOLVED\n  \
    \  support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:31404065\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n\
    \      snippet: chloramphenicol resistance\n      explanation: Figure4C F65A with\
    \ matched -Cm viability control.\n      cache_path: evidence/PF01938/li-2019.txt\n\
    \      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    - graph_id: tram0076-native-variant-growth-2019\n  title: TRAM0076 variants impair\
    \ native growth complementation\n  scope: Li2019 Figure4D andS4; six individual\
    \ variants versus WT complementation in delta0076.\n  context: M. maripaludis\
    \ S0001-derived deletion strain,pMEV2 expression,37C,triplicate OD600 timecourses,empty-vector\n\
    \    and WT-complement controls.\n  family_mapping: Q6M142v1 PF01938 13-67 contains\
    \ R35,F39,F42,K62,F63,F65; each is individually replaced\n    by alanine. Whole\
    \ stand-alone proteins are expressed.\n  scope_status: PHENOTYPIC\n  limitations:\
    \ The assay measures growth kinetics,not zero growth or a purified mutant RNA-unfolding\
    \ rate.\n    K62A partially rescues. I33A,K28A,G30A,G32A restore growth; host-dependent\
    \ abundance/folding alternatives\n    remain unresolved.\n  nodes:\n  - node_id:\
    \ r35a\n    label: R35A instead of WT complementation\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q6M142\n  - node_id: f39a\n    label: F39A instead\
    \ of WT complementation\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q6M142\n\
    \  - node_id: f42a\n    label: F42A instead of WT complementation\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:Q6M142\n  - node_id: k62a\n  \
    \  label: K62A instead of WT complementation\n    node_type: PERTURBATION\n  \
    \  grounding:\n    - UniProtKB:Q6M142\n  - node_id: f63a\n    label: F63A instead\
    \ of WT complementation\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q6M142\n\
    \  - node_id: f65a\n    label: F65A instead of WT complementation\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:Q6M142\n  - node_id: growth\n\
    \    label: Growth kinetics restored by complementation at37C\n    node_type:\
    \ PHENOTYPE\n  edges:\n  - edge_id: r35a-native-growth-reduction\n    subject:\
    \ r35a\n    predicate: decreases\n    object: growth\n    mechanism: R35A complementation\
    \ gives slower growth kinetics than WT complementation and resembles\n      the\
    \ deletion control.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet: also did not\
    \ complement\n      explanation: Figure4D left,R35A versus WT complementation;\
    \ the growth difference does not isolate\n        its molecular cause.\n     \
    \ cache_path: evidence/PF01938/li-2019.txt\n      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    \  - edge_id: f39a-native-growth-reduction\n    subject: f39a\n    predicate:\
    \ decreases\n    object: growth\n    mechanism: F39A fails to restore the faster\
    \ WT-complemented growth kinetics.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet:\
    \ also did not complement\n      explanation: Figure4D left,F39A versus WT complementation,not\
    \ a lethality test.\n      cache_path: evidence/PF01938/li-2019.txt\n      cache_sha256:\
    \ 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n  - edge_id:\
    \ f42a-native-growth-reduction\n    subject: f42a\n    predicate: decreases\n\
    \    object: growth\n    mechanism: F42A fails to restore the faster WT-complemented\
    \ growth kinetics.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet: also did not\
    \ complement\n      explanation: Figure4D left,F42A versus WT complementation.\n\
    \      cache_path: evidence/PF01938/li-2019.txt\n      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    \  - edge_id: k62a-native-growth-reduction\n    subject: k62a\n    predicate:\
    \ decreases\n    object: growth\n    mechanism: K62A only partially restores growth\
    \ and remains slower than WT complementation; it is not\n      equated with complete\
    \ failure.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet: partially\
    \ complemented\n      explanation: Figure4D right,K62A intermediate curve and\
    \ explicit partial-complementation Results\n        qualification; partial rescue\
    \ is not complete failure.\n      cache_path: evidence/PF01938/li-2019.txt\n \
    \     cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    \  - edge_id: f63a-native-growth-reduction\n    subject: f63a\n    predicate:\
    \ decreases\n    object: growth\n    mechanism: F63A fails to restore the faster\
    \ WT-complemented growth kinetics.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet:\
    \ also did not complement\n      explanation: Figure4D right,F63A versus WT complementation.\n\
    \      cache_path: evidence/PF01938/li-2019.txt\n      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    \  - edge_id: f65a-native-growth-reduction\n    subject: f65a\n    predicate:\
    \ decreases\n    object: growth\n    mechanism: F65A fails to restore the faster\
    \ WT-complemented growth kinetics.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet:\
    \ also did not complement\n      explanation: Figure4D right,F65A versus WT complementation.\n\
    \      cache_path: evidence/PF01938/li-2019.txt\n      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    - graph_id: tram0076-native-utr-reporters-2019\n  title: MMP0076 genotype and\
    \ leader sequence alter mCherry signals\n  scope: Li2019 Figure5B-D; three UTR\
    \ reporters and the1515MT leader comparison.\n  context: pMEV4 UTR-mCherry constructs\
    \ in parental S0001 and delta0076;triplicate early/middle/late growth-phase\n\
    \    cultures;575/610nm fluorescence normalized per mL*OD.\n  family_mapping:\
    \ Deleted whole MMP0076 maps to Q6M142v1 PF01938 13-67. UTR1515MT modifies the\
    \ reporter\n    leader,not the TRAM protein or a separate Pfam member.\n  scope_status:\
    \ PHENOTYPIC\n  limitations: Fluorescence does not separate transcription,translation,RNA\
    \ stability or fluorophore maturation.\n    Predicted hairpin disruption is not\
    \ direct structural verification in cells.1515MT bars are not identical\n    between\
    \ hosts; the parental advantage is lost or reversed.\n  nodes:\n  - node_id: deletion\n\
    \    label: Delta0076 instead of parental S0001\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q6M142\n  - node_id: leader\n    label: UTR1515MT\
    \ instead of WT1515 leader\n    node_type: PERTURBATION\n  - node_id: signal0127\n\
    \    label: Normalized UTR0127-mCherry fluorescence\n    node_type: PHENOTYPE\n\
    \  - node_id: signal1515\n    label: Normalized UTR1515-mCherry fluorescence\n\
    \    node_type: PHENOTYPE\n  - node_id: signal1697\n    label: Normalized UTR1697-mCherry\
    \ fluorescence\n    node_type: PHENOTYPE\n  - node_id: advantage\n    label: Parental-minus-deletion\
    \ reporter fluorescence advantage\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ deletion-utr0127-signal-reduction\n    subject: deletion\n    predicate: decreases\n\
    \    object: signal0127\n    mechanism: Deletion modestly lowers0127-leader reporter\
    \ signal versus parental cultures at the sampled\n      growth phases.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:31404065\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n\
    \      snippet: expression of mCherry\n      explanation: Figure5C UTR0127 bars;\
    \ measured reporter fluorescence,not direct transcription rate.\n      cache_path:\
    \ evidence/PF01938/li-2019.txt\n      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    \  - edge_id: deletion-utr1515-signal-reduction\n    subject: deletion\n    predicate:\
    \ decreases\n    object: signal1515\n    mechanism: Deletion lowers1515-leader\
    \ reporter fluorescence relative to parental cultures.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:31404065\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n\
    \      snippet: expression of mCherry\n      explanation: Figure5C UTR1515 bars,three\
    \ phases,triplicate cultures.\n      cache_path: evidence/PF01938/li-2019.txt\n\
    \      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    \  - edge_id: deletion-utr1697-signal-reduction\n    subject: deletion\n    predicate:\
    \ decreases\n    object: signal1697\n    mechanism: Deletion lowers1697-leader\
    \ reporter fluorescence relative to parental cultures.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:31404065\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n\
    \      snippet: expression of mCherry\n      explanation: Figure5C UTR1697 bars;\
    \ not assumed quantitatively equal to0127.\n      cache_path: evidence/PF01938/li-2019.txt\n\
    \      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    \  - edge_id: leader-mutation-reduces-genotype-contrast\n    subject: leader\n\
    \    predicate: decreases\n    object: advantage\n    mechanism: The1515MT leader\
    \ removes or reverses the parental fluorescence advantage observed with\n    \
    \  the WT1515 leader across the genotype comparison.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:31404065\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n\
    \      snippet: expression of mCherry\n      explanation: Figure5B,C,D interaction\
    \ comparison; do not claim equal fluorescence at every stage\n        or directly\
    \ observed RNA hairpin melting.\n      cache_path: evidence/PF01938/li-2019.txt\n\
    \      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    - graph_id: tram0076-bx04-cold-rescue-2019\n  title: Induced TRAM0076 improves\
    \ heterologous cold growth\n  scope: Li2019 S2A,B; E. coli BX04 delta-cspABGE\
    \ with pIN-0076.\n  context: IPTG-induced pIN-0076 versus induced empty pINIII;18C\
    \ and22C LB/ampicillin plates,37C viability\n    controls,2-5days,OD6000.9 starting\
    \ cultures and tenfold dilutions. Methods100ug/mL ampicillin; S2\n    IPTG dose\
    \ unspecified.\n  family_mapping: Expressed MMP0076 is Q6M142-reference full protein,PF01938\
    \ 13-67. Recipient is E. coli\n    BX04,not the native archaeal deletion strain.\n\
    \  taxon: NCBITaxon:562\n  scope_status: PHENOTYPIC\n  limitations: Induced cold-growth\
    \ rescue is indirect and does not identify the native archaeal RNA substrate.\n\
    \    Uninduced and induced conditions differ; no claim of induction-independent\
    \ rescue or complete equivalence\n    to Csps.\n  nodes:\n  - node_id: expression\n\
    \    label: Induced TRAM0076 instead of empty vector in BX04\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q6M142\n  - node_id: growth18\n    label: BX04\
    \ growth at18C\n    node_type: PHENOTYPE\n  - node_id: growth22\n    label: BX04\
    \ growth at22C\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: induced-cold18-growth-increase\n\
    \    subject: expression\n    predicate: increases\n    object: growth18\n   \
    \ mechanism: Expressing TRAM0076 improves18C growth relative to the induced empty-vector\
    \ control.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet: growth at\
    \ low\n      explanation: S2A18C+IPTG panel and S2B expression controls; distinct\
    \ from native mutant complementation.\n      cache_path: evidence/PF01938/li-2019.txt\n\
    \      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    \  - edge_id: induced-cold22-growth-increase\n    subject: expression\n    predicate:\
    \ increases\n    object: growth22\n    mechanism: Expressing TRAM0076 improves22C\
    \ growth relative to the induced empty-vector control.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:31404065\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n\
    \      snippet: growth at low\n      explanation: S2A22C+IPTG panel with37C viability\
    \ comparator; not native22C complementation.\n      cache_path: evidence/PF01938/li-2019.txt\n\
    \      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    - graph_id: tram0076-parental-cold-reporters-2019\n  title: Cold shock transiently\
    \ increases parental UTR reporter signals\n  scope: Li2019 S7; parental S0001\
    \ reporter timecourses with deletion and1515MT controls.\n  context: Middle-exponential37C\
    \ cultures shifted to4C,0-8h sampling,triplicate normalized mCherry fluorescence.\n\
    \    Each WT-leader reporter is compared to its own preshift baseline.\n  family_mapping:\
    \ Parental cells contain intact MMP0076,reference Q6M142v1 PF01938 13-67. This\
    \ is a temperature\n    perturbation in a TRAM-containing system,not a direct\
    \ assay of isolated TRAM thermosensing.\n  scope_status: PHENOTYPIC\n  limitations:\
    \ The rise is transient and genotype controls differ in baseline. Deletion curves\
    \ are not\n    rigorously flat. UTR1515MT lacks the sustained parental increase.\
    \ Reporter fluorescence alone does\n    not prove a TRAM-mediated transcription\
    \ chain.\n  nodes:\n  - node_id: cold\n    label: Parental reporter cultures shifted\
    \ from37C to4C\n    node_type: PERTURBATION\n  - node_id: signal0127\n    label:\
    \ UTR0127-mCherry signal during early cold shock\n    node_type: PHENOTYPE\n \
    \ - node_id: signal1515\n    label: UTR1515-mCherry signal during early cold shock\n\
    \    node_type: PHENOTYPE\n  - node_id: signal1697\n    label: UTR1697-mCherry\
    \ signal during early cold shock\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ cold-utr0127-signal-increase\n    subject: cold\n    predicate: increases\n\
    \    object: signal0127\n    mechanism: Cold shock raises the parental0127 reporter\
    \ signal above its preshift value over the early\n      timecourse,with a later\
    \ decline.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet: expression\
    \ of mCherry\n      explanation: S7 top-left timecourse and top-right deletion\
    \ comparator; observed temperature response,not\n        direct attribution of\
    \ every step to TRAM.\n      cache_path: evidence/PF01938/li-2019.txt\n      cache_sha256:\
    \ 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n  - edge_id:\
    \ cold-utr1515-signal-increase\n    subject: cold\n    predicate: increases\n\
    \    object: signal1515\n    mechanism: Cold shock raises the parental WT1515-leader\
    \ reporter signal over its preshift value; the1515MT\n      leader lacks the sustained\
    \ rise.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet: expression\
    \ of mCherry\n      explanation: S7 bottom-left WT1515 versus its0h baseline,with1515MT\
    \ and deletion panels retaining\n        contextual limits.\n      cache_path:\
    \ evidence/PF01938/li-2019.txt\n      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    \  - edge_id: cold-utr1697-signal-increase\n    subject: cold\n    predicate:\
    \ increases\n    object: signal1697\n    mechanism: Cold shock raises the parental1697\
    \ reporter signal over its preshift value; the smaller\n      deletion-strain\
    \ changes are not described as zero.\n    directness: UNRESOLVED\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:31404065\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6705878/\n      snippet:\
    \ expression of mCherry\n      explanation: S7 middle-left timecourse and middle-right\
    \ deletion comparator; retain the separate\n        baselines and fluctuations.\n\
    \      cache_path: evidence/PF01938/li-2019.txt\n      cache_sha256: 96912ee2641c669680cdfbf4666a500a3b5fe71de582ba72fd85cd63283714e3\n\
    curation_events:\n- timestamp: '2026-10-12T05:17:59Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: needs_followup\n  summary: Curate PF01938 TRAM0076 assay-specific\
    \ causal contexts\n  history_record: history/records/PF01938/2026-10-12T051759Z-codex-792f49.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-12T05:29:59Z'\n\
    \  curator: Codex\n  action: REVIEW\n  outcome: needs_followup\n  summary: Retain\
    \ scoped PF01938 TRAM0076 causal review\n  history_record: history/records/PF01938/2026-10-12T052959Z-codex-abed6e.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-18T02:54:46Z'\n\
    \  curator: Antigravity\n  action: EDIT\n  outcome: changed\n  summary: Ground\
    \ causal graph gene and protein nodes in PF01938 with verified UniProtKB accessions\
    \ (UniProtKB:Q6M142)\n  history_record: history/records/PF01938/2026-10-18T025446Z-antigravity-2892a8.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-21T07:32:29Z'\n\
    \  curator: Antigravity\n  action: EDIT\n  outcome: changed\n  summary: Ground\
    \ MMP0076/TRAM0076 perturbation nodes across four Li 2019 causal graphs to UniProtKB:Q6M142\n\
    \  history_record: history/records/PF01938/2026-10-21T073229Z-antigravity-60bdea.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-23T07:48:12Z'\n\
    \  curator: Antigravity\n  action: EDIT\n  outcome: changed\n  summary: Ground\
    \ shifted RNA complex nodes in tram0076-rna-complexes-2019 to UniProtKB:Q6M142\n\
    \  history_record: history/records/PF01938/2026-10-23T074812Z-antigravity-193803.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Frozen TRAM/formerDUF90,IPR002792,EX_DUF andUNSCORED metadata is preserved.
    Q6M142v1 has69 residues and PF01938 13-67; all11 selected native-numbering residues
    match and are in-domain. PDB1YVC maps1-69 with an extra terminalL,not the tagged
    assay construct. Native host is S0001,not an assumed S2 wild type. Vector-derived
    biochemical termini remain incompletely verified; repeated D25A primer-table purpose
    labels do not override Figure4/S1 Table variants. Multidomain enzyme annotations
    are not isolated-TRAM catalytic evidence.
  target_ids:
  - PF01938
  evidence_ids:
  - identity
  - primary
  - induction-context
  - source-coverage
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Every edge names its measured comparator and conditions. Figure3/5 beacon
    substrates are explicitly DNA,not RNA. Binding is represented only as complex
    formation,not activation or downstream remodeling. Native growth deletion/rescue
    is distinct from biochemical assays and heterologous BX04 rescue. I33A loses RL211
    reporter growth with reduced protein abundance yet restores native growth; K62A
    partially rescues. WT1515 leader genotype differences are not falsely described
    as identical fluorescence after1515MT mutation. Cold-shock signals are transient
    genotype-context observations,not a direct TRAM temperature-sensing pathway. No
    unsupported transcriptome-to-growth or autoregulatory chain is created.
  target_ids:
  - PF01938
  evidence_ids:
  - primary
  - native
  - induction-context
  - source-coverage
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: R15 member accession mapping and2017 figures/supplement remain followups;2017
    uninduced3066 reporter activity versus induced inhibition is compatible with the2019
    induced negative and is not unconditional contradiction. Ctr3 and2025 PyTRAM require
    primary assay/mapping work. Multidomain MiaB,RimO,RumA,RlmCD,Trm2,CDKAL1/CDK5RAP1
    contexts remain open. One capped500-entry UniProt page is not a census; raw RNA-seq/RIP
    and all35071 family proteins were not reviewed exhaustively.
  target_ids:
  - PF01938
  evidence_ids:
  - primary
- assessment_id: cycle2-partner-grounding-verification
  area: identity
  topic: Cycle 2 causal-graph partner and substrate protein grounding
  outcome: supported
  summary: 'Stage 3 (PR #347) grounded Saccharomyces cerevisiae Trl1 (UniProtKB:P09880)
    in sc-trl1-healing-step-2019.'
  target_ids:
  - PF01938
  evidence_ids:
  - stage4-prior-review
findings:
- finding_id: additional-contexts
  issue_key: pf01938-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Extend native-RNA and other-member evidence without assay transfer
  description: Map R15,Ctr3 andPyTRAM tested accessions; inspect their full primary
    assays and relevant figures/supplements. Preserve induction dependence,RNase contamination
    and the separate PyCsp identity. For enzyme fusions,resolve domain-specific contribution
    before catalytic edges. Clarify tagged-construct sequences,mutant abundance/folding
    and direct native RNA/transcription steps; curate additional transcriptome contexts
    only with scoped causal support. Preserve all existing followups and IN_PROGRESS.
  target_ids:
  - PF01938
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - induction-context
  - source-coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01938.yaml
    role: Human-owned scientific overlay
  previous_occurrences:
  - repository: CultureBotAI/DUFMech
    review_id: 20261021T114819Z-pf01938-stage4-record-review
    finding_id: additional-contexts
actions:
- action_id: extend-contexts
  description: Map R15,Ctr3 andPyTRAM tested accessions; inspect their full primary
    assays and relevant figures/supplements. Preserve induction dependence,RNase contamination
    and the separate PyCsp identity. For enzyme fusions,resolve domain-specific contribution
    before catalytic edges. Clarify tagged-construct sequences,mutant abundance/folding
    and direct native RNA/transcription steps; curate additional transcriptome contexts
    only with scoped causal support. Preserve all existing followups and IN_PROGRESS.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01938
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Figures1,3,4,5,S2,S4,S7 visually checked;S1/S2 DOCX tables parsed,not fully page-rendered.2017
  text/captions were inspected without independent figure-pixel review. S3 SPR image
  and raw RNA-seq/RIP datasets were not independently analyzed.2025 full-text request
  redirected to abstract. No clone resequencing,experimental replication,independent
  expert review or full family census.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
