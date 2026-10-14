# PF01878 Thy28 cellular effects and species-specific limits

- Review: 20261011T193644Z-pf01878-thy28-cellular-effects-and-species-limits
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T19:36:32Z
- Finished UTC: 2026-10-11T19:36:44Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Nine phenotypic graphs retain seventeen indirect observed cellular effects from WEHI-231 overexpression and DT40 knockdown/rescue/partner assays. Mouse and human Pax5 negatives restrict transfer. Reference/domain identities are verified, but exact experimental insert sequences remain partly unresolved; no residue-level biochemical mechanism or conserved JNK/ROS/Pax5 pathway is claimed. Retain IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Toyota2012 full publisher PDF Methods/Results/Discussion and original Figures1-5; Fujita2015 Methods/Results/Discussion, original Figures6-8,S1/S2 and TableS2; Kitaura2019 Methods/Results, original Figures3/5/7 and S2. Current member-specific InterPro APIs, UniProt sequence metadata, versioned reference FASTAs and the VcaM4I RCSB/UniProt discrepancy were checked. Other leads are explicitly incomplete.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01878 | data/families/PF01878.yaml | generated | PF01878 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01878 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: concern. Targets: PF01878.

Q90679 sequenceversion1 equals AAA75591.1,242aa,PF01878 residues73-235; NP_989618.2 differs at51 outside EVE. DT40 terminal primers and cDNA origin identify cThy28 but not its exact internal batch sequence. Mouse Q91YJ3 equals BAC21100.1/NP_653126.1,226aa,PF01878 residues56-219; Toyota's Thy28-V5 insert species/sequence is not established by its mouse host and incongruous protocol citation. Human Q9P016 maps56-218. RCSB-linked VcaM4I homolog A0ABY5IHE6 differs at13 positions from6YEX and reports only HNH_2; no exact PF01878 restriction-enzyme mapping is claimed.

### Directed effects and limits

graph: supported. Targets: PF01878.

Seventeen effects are INDIRECT/OBSERVED in nine PHENOTYPIC contexts. WEHI readouts distinguish partial membrane protection, compositional DNA distributions, clone6 p27, live-gated H2DCFDA intensity and pooled-clone phosphorylation/cleavage bands. Baseline differences, clone/time effects, unspecified Figure3A timing and the higher clone6 secondary-necrotic24h fraction prevent overstating protection. DT40 perturbation/rescue and MYH9 partner effects retain residual output and location-specific incomplete ChIP recovery. No parallel readouts are stitched into an observed molecular relay; MYH9 is not assigned PF01878.

### Remaining family coverage

completeness: concern. Targets: PF01878.

All11128 frozen family members remain in scope. Exact tagged sequences, domain/residue contributions and direct biochemical mechanisms remain unresolved. Mouse knockout and human-cell negatives restrict generalization but are not equivalent to challenged WEHI overexpression. Modified-base proteomics,5J3E,SmMcrB,VcaM4I and other prokaryotic EVE evidence still require exact mapping and primary figure/data review. The study set is not exhaustive family coverage.

## Findings

### additional-contexts: Resolve EVE molecular mechanism and cross-context transfer

minor / open / confirmed; issue key: pf01878-causal-context-coverage.

Verify the WEHI Thy28-V5 insert and DT40 internal sequence, test domain-specific perturbations with expression/folding/localization controls, and distinguish transcription from RNA turnover and direct contacts from ChIP/coIP recovery. Retain mammalian Pax5 negatives, rescue-expression controls and baseline differences. Inspect remaining modified-base and restriction-system primary data only after exact member-family mapping; preserve unsupported mechanisms as open questions.

## Recommended Actions And Acceptance Checks

### extend-contexts

Verify the WEHI Thy28-V5 insert and DT40 internal sequence, test domain-specific perturbations with expression/folding/localization controls, and distinguish transcription from RNA turnover and direct contacts from ChIP/coIP recovery. Retain mammalian Pax5 negatives, rescue-expression controls and baseline differences. Inspect remaining modified-base and restriction-system primary data only after exact member-family mapping; preserve unsupported mechanisms as open questions.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC4301804/; Figures6D-G,7B-D,8,S1/S2,TableS2 and construct/knockdown/rescue/ChIP Methods | supports | Two chicken Thy28 shRNA sequences lower Pax5 protein/transcripts and AID RNA. Expressed resistant full-length cThy28 rescues Pax5 and upstream MYH9 ChIP enrichment, whereas nonexpressing rescue clones do not. MYH9 depletion separately reduces Pax5. ChIP and coIP do not establish direct DNA or binary binding; proposed transcriptional and chromosomal routes remain unobserved. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01878/protein/uniprot/Q90679/; Accession and domain locations; paired UniProt identity facts | supports | Q90679 sequenceversion1 equals AAA75591.1,242aa,PF01878 residues73-235; NP_989618.2 differs at51 outside EVE. DT40 terminal primers and cDNA origin identify cThy28 but not its exact internal batch sequence. Mouse Q91YJ3 equals BAC21100.1/NP_653126.1,226aa,PF01878 residues56-219; Toyota's Thy28-V5 insert species/sequence is not established by its mouse host and incongruous protocol citation. Human Q9P016 maps56-218. RCSB-linked VcaM4I homolog A0ABY5IHE6 differs at13 positions from6YEX and reports only HNH_2; no exact PF01878 restriction-enzyme mapping is claimed. |
| wehi-assays | https://pmc.ncbi.nlm.nih.gov/articles/PMC6275998/; Publisher PDF Methods/Results/Discussion and original Figures1-5 | supports | Stable Thy28-V5 cells show partial and context-dependent changes in membrane, DNA-content, p27, oxidation-probe and signaling-blot readouts. These are indirect cellular effects, not specific H2O2 concentrations, kinase/caspase rates or a demonstrated causal relay. Construct and timing uncertainties remain explicit. |
| mammalian-negatives | https://pmc.ncbi.nlm.nih.gov/articles/PMC6645560/; Mouse targeting Methods, original Figures3/5/7 and human-cell SupplementS2 | supports | Mouse loss of Thy28 does not significantly change measured B-cell counts or the shown splenic Pax5 readout. Nalm-6 shRNA and Raji CRISPR lines retain Pax5. These are assay-specific limits on transfer, not proof of universal absence of function or a contradiction of distinct overexpression conditions. |
| coverage-and-access | evidence/PF01878/eve-gap-ledger.txt; Actual source inspection and pending evidence branches | supports | No prior target-specific curation in the searched owners, including ignored files. Publisher PDF and PLOS supplements were obtained after alternate PDF endpoints returned HTML/403. A sandbox restriction affected only uv's cached rendering dependency and approved retry succeeded; repository/skill reads worked. Remaining molecular, identity and member-coverage gaps are explicit. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01878 | data/families/PF01878.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Toyota Figures1-5, Fujita Figures6-8 and S1/S2, Kitaura Figures3/5/7 and S2 were visually inspected; TableS2 text was read. Original Fujita Figure9 and Kitaura S1 images were not visually inspected. Remaining modified-base/restriction leads have only the stated partial coverage. No raw-data refit, assay-batch sequencing, independent replication or exhaustive survey. Rendered-page checks follow separately.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T193644Z-pf01878-thy28-cellular-effects-and-species-limits
title: PF01878 Thy28 cellular effects and species-specific limits
started_at: '2026-10-11T19:36:32Z'
finished_at: '2026-10-11T19:36:44Z'
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
summary: Nine phenotypic graphs retain seventeen indirect observed cellular effects
  from WEHI-231 overexpression and DT40 knockdown/rescue/partner assays. Mouse and
  human Pax5 negatives restrict transfer. Reference/domain identities are verified,
  but exact experimental insert sequences remain partly unresolved; no residue-level
  biochemical mechanism or conserved JNK/ROS/Pax5 pathway is claimed. Retain IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01878.yaml
    sha256: 2ba3e4389a27f1fb3b9ec8cf3792af4b8e5e66ea4663de051a8ca0f1e5bd79a4
    role: context
  - path: data/families/PF01878.yaml
    sha256: 04ef840301afe385cd7a9075cc382b091a1d50cc6bf269a03937f0dde2029a27
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
  - path: evidence/PF01878/fujita-2015-dt40.txt
    role: context
    sha256: f61693f99f1bd21db179449aa4124b0bdd6f0b1866aa63ff798a0aae0c56a080
  - path: evidence/PF01878/thy28-identity.txt
    role: context
    sha256: 5a93567417a4b2465da1eb9d3ae9a1400b7f67f81017e9a0f970226b174189c9
  - path: evidence/PF01878/toyota-2012-assays.txt
    role: context
    sha256: 0c5633d14e0ff634ec33baa4ceb1aa9969700b3d40008b3c9925d7b3dfcda85e
  - path: evidence/PF01878/kitaura-2019-limits.txt
    role: context
    sha256: d9b5691e7b3c46623832320384915296b7aea783612b31e53c0c82e62b9d98b4
  - path: evidence/PF01878/eve-gap-ledger.txt
    role: context
    sha256: 1a6003610485e10073cf8e42a9224170ecc759ba8d52230e028d79805f02fb63
targets:
- target_id: PF01878
  path: data/families/PF01878.yaml
  label: PF01878
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01878.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: a3d2f23fb9c7e9a201c2950c0cc2f1d9bf4cc4102e33674210e9729c954a6b8b
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Toyota2012 full publisher PDF Methods/Results/Discussion and original
    Figures1-5; Fujita2015 Methods/Results/Discussion, original Figures6-8,S1/S2 and
    TableS2; Kitaura2019 Methods/Results, original Figures3/5/7 and S2. Current member-specific
    InterPro APIs, UniProt sequence metadata, versioned reference FASTAs and the VcaM4I
    RCSB/UniProt discrepancy were checked. Other leads are explicitly incomplete.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01878
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: All11128 frozen family members remain in scope. Exact tagged sequences,
      domain/residue contributions and direct biochemical mechanisms remain unresolved.
      Mouse knockout and human-cell negatives restrict generalization but are not
      equivalent to challenged WEHI overexpression. Modified-base proteomics,5J3E,SmMcrB,VcaM4I
      and other prokaryotic EVE evidence still require exact mapping and primary figure/data
      review. The study set is not exhaustive family coverage.
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
  - PF01878
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4301804/
  locator: Figures6D-G,7B-D,8,S1/S2,TableS2 and construct/knockdown/rescue/ChIP Methods
  accessed_at: '2026-10-11T19:36:44Z'
  support: supports
  snapshot_sha256: f61693f99f1bd21db179449aa4124b0bdd6f0b1866aa63ff798a0aae0c56a080
  summary: Two chicken Thy28 shRNA sequences lower Pax5 protein/transcripts and AID
    RNA. Expressed resistant full-length cThy28 rescues Pax5 and upstream MYH9 ChIP
    enrichment, whereas nonexpressing rescue clones do not. MYH9 depletion separately
    reduces Pax5. ChIP and coIP do not establish direct DNA or binary binding; proposed
    transcriptional and chromosomal routes remain unobserved.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01878/protein/uniprot/Q90679/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T19:36:44Z'
  support: supports
  snapshot_sha256: 5a93567417a4b2465da1eb9d3ae9a1400b7f67f81017e9a0f970226b174189c9
  summary: Q90679 sequenceversion1 equals AAA75591.1,242aa,PF01878 residues73-235;
    NP_989618.2 differs at51 outside EVE. DT40 terminal primers and cDNA origin identify
    cThy28 but not its exact internal batch sequence. Mouse Q91YJ3 equals BAC21100.1/NP_653126.1,226aa,PF01878
    residues56-219; Toyota's Thy28-V5 insert species/sequence is not established by
    its mouse host and incongruous protocol citation. Human Q9P016 maps56-218. RCSB-linked
    VcaM4I homolog A0ABY5IHE6 differs at13 positions from6YEX and reports only HNH_2;
    no exact PF01878 restriction-enzyme mapping is claimed.
- evidence_id: wehi-assays
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6275998/
  locator: Publisher PDF Methods/Results/Discussion and original Figures1-5
  summary: Stable Thy28-V5 cells show partial and context-dependent changes in membrane,
    DNA-content, p27, oxidation-probe and signaling-blot readouts. These are indirect
    cellular effects, not specific H2O2 concentrations, kinase/caspase rates or a
    demonstrated causal relay. Construct and timing uncertainties remain explicit.
  accessed_at: '2026-10-11T19:36:44Z'
  support: supports
  snapshot_sha256: 0c5633d14e0ff634ec33baa4ceb1aa9969700b3d40008b3c9925d7b3dfcda85e
- evidence_id: mammalian-negatives
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6645560/
  locator: Mouse targeting Methods, original Figures3/5/7 and human-cell SupplementS2
  summary: Mouse loss of Thy28 does not significantly change measured B-cell counts
    or the shown splenic Pax5 readout. Nalm-6 shRNA and Raji CRISPR lines retain Pax5.
    These are assay-specific limits on transfer, not proof of universal absence of
    function or a contradiction of distinct overexpression conditions.
  accessed_at: '2026-10-11T19:36:44Z'
  support: supports
  snapshot_sha256: d9b5691e7b3c46623832320384915296b7aea783612b31e53c0c82e62b9d98b4
- evidence_id: coverage-and-access
  kind: search
  reference: evidence/PF01878/eve-gap-ledger.txt
  locator: Actual source inspection and pending evidence branches
  search_scope: Ignored/hidden-inclusive search of maintained curation/evidence/history/review
    owners for PF01878/DUF55/THYN1/THY28; primary-source searches for EVE,Thy28,Pax5,apoptosis,VcaM4I
    and SmMcrB on2026-10-11. Not an exhaustive literature or member survey.
  summary: No prior target-specific curation in the searched owners, including ignored
    files. Publisher PDF and PLOS supplements were obtained after alternate PDF endpoints
    returned HTML/403. A sandbox restriction affected only uv's cached rendering dependency
    and approved retry succeeded; repository/skill reads worked. Remaining molecular,
    identity and member-coverage gaps are explicit.
  accessed_at: '2026-10-11T19:36:44Z'
  support: supports
  snapshot_sha256: 1a6003610485e10073cf8e42a9224170ecc759ba8d52230e028d79805f02fb63
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T19:36:44Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01878
  kind: record_content
  reference: data/families/PF01878.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T19:36:44Z'
  support: context_only
  snapshot_sha256: 04ef840301afe385cd7a9075cc382b091a1d50cc6bf269a03937f0dde2029a27
  quote: "id: Pfam:PF01878\npfam_id: PF01878\nname: EVE domain\nshort_name: EVE\n\
    seed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status: IN_PROGRESS\n\
    source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01878\ncounters:\n\
    \  proteins: 11128\n  matches: 11187\n  proteomes: 9908\n  taxa: 17496\n  structures:\
    \ 11\n  alphafold_models: 7863\n  domain_architectures: 124\nprovenance:\n  snapshot_id:\
    \ interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002740\ndescription: This domain was formerly known as\
    \ DUF55. Crystal structures have shown that this domain is\n  part of the PUA\
    \ superfamily. This domain has been named EVE and is thought to be RNA-binding\
    \ [[cite:PUB00055624]].\ncuration_history: history/records/PF01878\ndiscussions:\n\
    - discussion_id: thy28-species-and-context-limits\n  prompt: Explain why DT40\
    \ Pax5 dependence is not reproduced in tested mammalian contexts.\n  kind: CURATION_TODO\n\
    \  status: OPEN\n  rationale: Kitaura2019 mouse exons3-7 knockout retains splenic\
    \ Pax5 and B-cell counts; human Nalm-6\n    knockdown and Raji CRISPR mutants\
    \ retain Pax5. These context-specific negatives restrict transfer\n    of the\
    \ chicken result without disproving challenged WEHI-231 phenotypes.\n  evidence:\n\
    \  - reference: PMID:31329649\n    supports: PARTIAL\n    evidence_source: primary_methods_figures_and_supplement\n\
    \    explanation: Figures3/5/7 and S2 were inspected;7-week splenic Pax5 MFI280/285/280\
    \ and Pax5-positive95.6/94.7/95.6%\n      for WT/het/KO. B-cell counts across8.1-38.7-week\
    \ mice show no significant difference, not statistical\n      equivalence. Raji\
    \ uses CRISPR despite main-text knockdown wording.\n  - reference: PMID:25607658\n\
    \    supports: PARTIAL\n    evidence_source: primary_knockdown_and_rescue\n  \
    \  explanation: DT40 depletion/rescue supports a local contribution; it does not\
    \ establish a universal\n      vertebrate requirement or direct promoter binding.\n\
    \  notes: Separate species from lineage state, transformed-cell context, acute\
    \ versus stable perturbation\n    and compensatory adaptation. Inspect the unreviewed2019\
    \ S1 image before relying on its LN/spleen-discrepant\n    caption. No negative\
    \ edge was invented for unchanged readouts. Test matched systems and quantitative\n\
    \    power before universal claims.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n\
    - discussion_id: thy28-construct-and-molecular-mechanism\n  prompt: Resolve construct\
    \ sequences and the molecular contribution of EVE.\n  kind: CURATION_TODO\n  status:\
    \ OPEN\n  rationale: WEHI-231 insert sequence/species is unresolved; DT40 cDNA\
    \ is not batch-sequenced here and\n    chicken references differ at51 outside\
    \ EVE. All retained effects are indirect whole-cell observations,\n    not residue-level\
    \ mechanisms.\n  evidence:\n  - reference: PMID:22139584\n    supports: PARTIAL\n\
    \    evidence_source: primary_methods_and_original_figures\n    explanation: Stable\
    \ overexpression changes multiple readouts with baseline differences; the construct\n\
    \      citation is incongruous and Figure3A timing is unspecified. No p27/JNK/ROS\
    \ mediation experiment\n      is supplied.\n  - reference: PMID:25607658\n   \
    \ supports: PARTIAL\n    evidence_source: primary_methods_original_figures_and_table_s2\n\
    \    explanation: Rescue and ChIP support system-level effects, while direct DNA/RNA\
    \ contacts, domain necessity\n      and Fig9 molecular routes remain untested.\n\
    \  notes: Verify tagged insert sequences, expression/folding/localization controls\
    \ and domain-specific\n    perturbations. Measure direct binding or biochemical\
    \ action; use mediation experiments rather than\n    joining parallel cellular\
    \ readouts. H2DCFDA is not specific H2O2 concentration and phospho/cleavage\n\
    \    blots are not catalytic-rate assays. Preserve reused rescue lanes and nonexpressing\
    \ controls.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n- discussion_id: eve-family-and-restriction-enzyme-mapping\n\
    \  prompt: Extend EVE coverage with exact member mapping before transferring restriction\
    \ or modified-base\n    mechanisms.\n  kind: CURATION_TODO\n  status: OPEN\n \
    \ rationale: All11128 frozen proteins remain in scope. VcaM4I's structural EVE\
    \ assignment does not supply\n    a verified PF01878 match; RCSB-linked A0ABY5IHE6\
    \ differs at13 positions from6YEXentity1 and its current\n    Pfam response reports\
    \ only HNH_2.\n  evidence:\n  - reference: PMID:33450012\n    supports: PARTIAL\n\
    \    evidence_source: primary_methods_and_structural_classification\n    explanation:\
    \ Pastor2021 describes WP_010645282 and structural EVE homology. Exact sequence-family\n\
    \      assignment and original causal figures still need review before importing\
    \ its modification-dependent\n      restriction mechanism.\n  - reference: PMID:23434322\n\
    \    supports: PARTIAL\n    evidence_source: primary_metadata_and_abstract_only\n\
    \    explanation: Spruijt2013 modified-base proteomics is a follow-up lead; the\
    \ member-specific data and\n      assay conditions were not inspected and support\
    \ no retained edge yet.\n  notes: Inspect Spruijt full text and supplemental member\
    \ tables,5J3E construct/ligand evidence,SmMcrB\n    primary figures/mapping,Lutz2019\
    \ architecture-screen results and Bell2020 computational family boundaries.\n\
    \    Resolve exact WP_010645282 sequence and Pfam support; absent annotation in\
    \ a different homolog is\n    not proof that the paper's enzyme is outside PF01878.\
    \ No whole-family biochemical characterization\n    is claimed.\n  posed_by: Codex\n\
    \  posed_date: '2026-10-11'\ncausal_graphs:\n- graph_id: thy28-wehi-membrane-readouts\n\
    \  title: Thy28-V5 expression partially reduces challenged WEHI-231 membrane phenotypes\n\
    \  scope: Toyota2012 Figure2A/B, stable Thy28-V5 versus vector control in mouse\
    \ WEHI-231.\n  context: Anti-IgM10 ug/ml; RPMI1640 with10%FBS,50 uM mercaptoethanol\
    \ and100 ug/ml kanamycin,37 C/5%CO2.\n    DiOC6 staining40 nM and annexinV/7-AAD\
    \ flow cytometry; at least10000 events. Figure2B uses clones3/6.\n  family_mapping:\
    \ Mouse Thy28 reference Q91YJ3 equals BAC21100.1/NP_653126.1,226 aa,PF01878 at56-219.\n\
    \    Human THYN1 Q9P016 also maps56-218. The Thy28-V5 insert sequence/species\
    \ is unresolved; mouse host\n    identity does not verify the insert. No isolated\
    \ EVE domain is tested.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:10090\n\
    \  limitations: Stable overexpression is not physiological necessity. Figure1\
    \ confirms Thy28-V5 expression\n    and similar IgM/MHCI surface signals. Clone\
    \ selection, tag effects and indirect signaling remain possible.\n    Protection\
    \ is partial, time- and clone-dependent; no uniform reduction of every death quadrant\
    \ is\n    claimed.\n  nodes:\n  - node_id: thy28-v5-expression\n    label: Stable\
    \ Thy28-V5 expression under anti-IgM challenge\n    node_type: PERTURBATION\n\
    \  - node_id: dioc6-low-cells\n    label: Fraction of cells with low DiOC6 signal\n\
    \    node_type: PHENOTYPE\n  - node_id: early-annexin-cells\n    label: AnnexinV-positive\
    \ 7-AAD-negative fraction at24 h\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ expression-reduces-potential-loss\n    subject: thy28-v5-expression\n    predicate:\
    \ decreases\n    object: dioc6-low-cells\n    mechanism: Thy28-V5 cells have fewer\
    \ low-potential cells over12-48 h; the representative48 h values\n      are75.6%\
    \ vector versus59.9% Thy28. This is a partial cellular protection phenotype, not\
    \ direct control\n      of a mitochondrial channel.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:22139584\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6275998/\n\
    \      snippet: Data represent one of three independent experiments.\n      explanation:\
    \ Original Figure2A and flow Methods distinguish DiOC6 loss from a measured molecular\n\
    \        death mechanism; substantial loss remains.\n      cache_path: evidence/PF01878/toyota-2012-assays.txt\n\
    \      cache_sha256: 0c5633d14e0ff634ec33baa4ceb1aa9969700b3d40008b3c9925d7b3dfcda85e\n\
    \  - edge_id: expression-reduces-early-annexin-fraction\n    subject: thy28-v5-expression\n\
    \    predicate: decreases\n    object: early-annexin-cells\n    mechanism: At24\
    \ h the lower-right annexinV/7-AAD quadrant is33.3% in vector versus15.8% and3.8%\
    \ in\n      clones3/6. At48 h clone3 approaches control,54.2% versus56.6%; clone6\
    \ remains38.1%. Clone6 secondary-necrotic24\n      h cells are15.3% versus12.8%\
    \ vector, so an all-quadrant protection claim is unsupported.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:22139584\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6275998/\n\
    \      snippet: Data represent one of three independent experiments.\n      explanation:\
    \ Original Figure2B quadrant labels provide clone- and time-specific values, rather\
    \ than\n        a generic anti-apoptotic effect in every comparison.\n      cache_path:\
    \ evidence/PF01878/toyota-2012-assays.txt\n      cache_sha256: 0c5633d14e0ff634ec33baa4ceb1aa9969700b3d40008b3c9925d7b3dfcda85e\n\
    - graph_id: thy28-wehi-dna-content\n  title: Thy28-V5 clones alter the anti-IgM\
    \ DNA-content distribution\n  scope: Toyota2012 Figure3A, WEHI-231 Thy28-V5 clones3/6/13\
    \ versus vector.\n  context: Anti-IgM10 ug/ml and50 ug/ml propidium iodide DNA-content\
    \ flow cytometry. The panel does not\n    specify exposure duration; do not borrow\
    \ the12/24 h times from the separate p27 blot.\n  family_mapping: Thy28 family\
    \ reference Q91YJ3/BAC21100.1,PF01878 at56-219; exact tagged insert not sequence-verified.\n\
    \    The assay changes whole-protein expression, not the domain independently.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:10090\n  limitations: SubG1 and\
    \ G1 percentages are compositional readouts, not independent cell counts or a\
    \ measured\n    transition rate. Clone6 already has a higher baseline G1 fraction.\
    \ No p27-necessity or direct cell-cycle\n    mechanism was tested.\n  nodes:\n\
    \  - node_id: thy28-v5-expression\n    label: Stable Thy28-V5 expression with\
    \ anti-IgM\n    node_type: PERTURBATION\n  - node_id: subg1-fraction\n    label:\
    \ SubG1 DNA-content fraction\n    node_type: PHENOTYPE\n  - node_id: g1-fraction\n\
    \    label: G1 DNA-content fraction\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ expression-reduces-subg1\n    subject: thy28-v5-expression\n    predicate: decreases\n\
    \    object: subg1-fraction\n    mechanism: Challenged vector shows59.4% subG1\
    \ versus37.8/14.2/31.8% in clones3/6/13. This retains\n      an observed distribution\
    \ shift without asserting prevention of all DNA fragmentation.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:22139584\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6275998/\n\
    \      snippet: Data represent one of three independent experiments.\n      explanation:\
    \ Original Figure3A shows representative PI distributions; the unspecified stimulation\n\
    \        duration remains explicit.\n      cache_path: evidence/PF01878/toyota-2012-assays.txt\n\
    \      cache_sha256: 0c5633d14e0ff634ec33baa4ceb1aa9969700b3d40008b3c9925d7b3dfcda85e\n\
    \  - edge_id: expression-increases-g1-fraction\n    subject: thy28-v5-expression\n\
    \    predicate: increases\n    object: g1-fraction\n    mechanism: Challenged\
    \ G1 fractions are32.1% vector versus48.6/80.5/57.8% clones3/6/13. These are the\n\
    \      same distributions as the subG1 observation, not independent confirmation\
    \ of a kinetic arrest mechanism.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:22139584\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6275998/\n      snippet:\
    \ Data represent one of three independent experiments.\n      explanation: Original\
    \ Figure3A supplies matched control and clone distributions, including non-identical\n\
    \        unstimulated baselines.\n      cache_path: evidence/PF01878/toyota-2012-assays.txt\n\
    \      cache_sha256: 0c5633d14e0ff634ec33baa4ceb1aa9969700b3d40008b3c9925d7b3dfcda85e\n\
    - graph_id: thy28-wehi-p27\n  title: Thy28-V5 clone6 has a higher p27 immunoblot\
    \ signal\n  scope: Toyota2012 Figure3B, clone6 versus vector, not the pooled-clone\
    \ Figure5 experiment.\n  context: Anti-IgM10 ug/ml,12/24 h, with unstimulated\
    \ control; p27Kip1 and actin immunoblots.\n  family_mapping: Reference mouse Thy28\
    \ Q91YJ3 carries PF01878 at56-219. The exact Thy28-V5 insert remains\n    unverified;\
    \ no domain or residue perturbation is performed.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:10090\n  limitations: Basal p27 is also higher. Protein abundance\
    \ is not direct transcription, translation or\n    degradation-rate evidence;\
    \ no p27 depletion/rescue establishes mediation of the DNA-content phenotype.\n\
    \  nodes:\n  - node_id: clone6-expression\n    label: Thy28-V5 clone6 under anti-IgM\
    \ challenge\n    node_type: PERTURBATION\n  - node_id: p27-band\n    label: p27Kip1\
    \ immunoblot signal\n    node_type: STATE\n  edges:\n  - edge_id: expression-increases-p27-band\n\
    \    subject: clone6-expression\n    predicate: increases\n    object: p27-band\n\
    \    mechanism: Clone6 has stronger p27 bands at12/24 h and at baseline than vector,\
    \ with actin controls.\n      The edge records the cellular expression-associated\
    \ effect; it does not establish p27 as the causal\n      bridge to G1 accumulation.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:22139584\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6275998/\n\
    \      snippet: Data represent one of three independent experiments.\n      explanation:\
    \ Figure3B and its legend restrict the p27 assay to clone6 and expose the baseline\
    \ difference.\n      cache_path: evidence/PF01878/toyota-2012-assays.txt\n   \
    \   cache_sha256: 0c5633d14e0ff634ec33baa4ceb1aa9969700b3d40008b3c9925d7b3dfcda85e\n\
    - graph_id: thy28-wehi-oxidation-readout\n  title: Thy28-V5 clones reduce the\
    \ live-gated oxidation-probe readout\n  scope: Toyota2012 Figure4, clones3/6 versus\
    \ vector.\n  context: Anti-IgM10 ug/ml for24/36/48 h;1 uM H2DCFDA staining30 min\
    \ at37 C; FSC/SSC viable gate with7-AAD\n    viability confirmation. Medium-only48\
    \ h provides the unstimulated comparison.\n  family_mapping: Reference Q91YJ3/NP_653126.1\
    \ maps PF01878 at56-219; tagged construct sequence unresolved.\n    This is a\
    \ cellular whole-protein intervention.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:10090\n\
    \  limitations: H2DCFDA fluorescence is not specific H2O2 quantitation or mitochondrial\
    \ source localization.\n    Baselines differ and gating selects surviving cells;\
    \ probe handling, redox state and survival can\n    influence the signal. The\
    \ unpublished12 h observation is not adopted as a measured edge.\n  nodes:\n \
    \ - node_id: thy28-v5-expression\n    label: Thy28-V5 expression in clones3/6\
    \ under anti-IgM\n    node_type: PERTURBATION\n  - node_id: oxidation-fluorescence\n\
    \    label: Live-gated H2DCFDA geometric mean fluorescence\n    node_type: STATE\n\
    \  edges:\n  - edge_id: expression-reduces-oxidation-readout\n    subject: thy28-v5-expression\n\
    \    predicate: decreases\n    object: oxidation-fluorescence\n    mechanism:\
    \ At24 h the geometric means are251.2 vector versus96.4/120.1 in clones3/6;36/48\
    \ h signals\n      also remain lower. Unstimulated values83.8 versus59.8/50.7\
    \ are already different. No direct peroxide\n      scavenging or JNK-to-ROS causality\
    \ is demonstrated.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:22139584\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC6275998/\n      snippet: Geometric\
    \ mean channel\n      explanation: Original Figure4 includes24 h despite Results\
    \ emphasizing36-48 h; the histogram labels\n        identify an intensity, not\
    \ a percentage of peroxide-producing cells.\n      cache_path: evidence/PF01878/toyota-2012-assays.txt\n\
    \      cache_sha256: 0c5633d14e0ff634ec33baa4ceb1aa9969700b3d40008b3c9925d7b3dfcda85e\n\
    - graph_id: thy28-wehi-signaling-blots\n  title: Pooled Thy28-V5 clones reduce\
    \ challenged phospho-JNK and caspase-cleavage readouts\n  scope: Toyota2012 Figure5,\
    \ mixture of clones3/6/13 versus vector.\n  context: Anti-IgM10 ug/ml; JNK1 immunoprecipitation\
    \ and phospho-JNK blot at12/24 h; cleaved-caspase3\n    blot at24/48 h. Actin\
    \ and total-protein controls are shown; plotted folds use unstimulated vector\n\
    \    as reference.\n  family_mapping: Mouse reference Q91YJ3 PF01878 at56-219\
    \ contextualizes Thy28, but the tagged insert\n    sequence/species is unresolved.\
    \ Pooled clones are not separate independent molecular perturbations.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:10090\n  limitations: Phosphorylation and cleavage\
    \ bands are not kinase/caspase catalytic-rate assays. Baseline\n    signals differ.\
    \ Parallel changes do not establish their causal order, a direct Thy28 substrate,\
    \ or\n    a JNK-H2O2 feedback mechanism.\n  nodes:\n  - node_id: pooled-expression\n\
    \    label: Pooled Thy28-V5 clones under anti-IgM challenge\n    node_type: PERTURBATION\n\
    \  - node_id: phospho-jnk-signal\n    label: Phospho-JNK immunoblot signal at12/24\
    \ h\n    node_type: STATE\n  - node_id: cleaved-caspase3-signal\n    label: Cleaved-caspase3\
    \ immunoblot signal at24/48 h\n    node_type: STATE\n  edges:\n  - edge_id: expression-reduces-phospho-jnk\n\
    \    subject: pooled-expression\n    predicate: decreases\n    object: phospho-jnk-signal\n\
    \    mechanism: Normalized pJNK values at12/24 h are1.8/1.2 for vector and0.8/0.6\
    \ for Thy28; baseline1.0\n      versus0.7. This is an indirect cellular phosphorylation\
    \ readout, not direct inhibition of JNK catalysis\n      by EVE.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:22139584\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6275998/\n\
    \      snippet: mixture of clones\n      explanation: Original Figure5A and immunoprecipitation\
    \ Methods identify the pool, time points and\n        phospho/total-JNK controls.\n\
    \      cache_path: evidence/PF01878/toyota-2012-assays.txt\n      cache_sha256:\
    \ 0c5633d14e0ff634ec33baa4ceb1aa9969700b3d40008b3c9925d7b3dfcda85e\n  - edge_id:\
    \ expression-reduces-caspase-cleavage\n    subject: pooled-expression\n    predicate:\
    \ decreases\n    object: cleaved-caspase3-signal\n    mechanism: Normalized cleavage\
    \ signals at24/48 h are2.6/3.0 vector versus1.3/1.8 Thy28, not abolition.\n  \
    \    This supports a downstream cellular effect without demonstrating direct caspase\
    \ inhibition or mediation\n      by the separately measured JNK change.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:22139584\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6275998/\n\
    \      snippet: mixture of clones\n      explanation: Original Figure5B and the\
    \ caspase-assay Methods specify an immunoblot rather than an\n        enzymatic\
    \ substrate assay.\n      cache_path: evidence/PF01878/toyota-2012-assays.txt\n\
    \      cache_sha256: 0c5633d14e0ff634ec33baa4ceb1aa9969700b3d40008b3c9925d7b3dfcda85e\n\
    - graph_id: cthy28-dt40-knockdown\n  title: Chicken Thy28 knockdown lowers selected\
    \ DT40 expression readouts\n  scope: Fujita2015 Figure6D/E and SupplementS1, two\
    \ clones each for Seq3/Seq4 versus shGFP controls.\n  context: Stable pSUPER-Neo\
    \ shRNAs in chicken DT40 B cells, G4181.5 mg/ml selection. RT-PCR normalized\n\
    \    to GAPDH,mean/SEM,n=3; immunoblot with beta-tubulin loading control. No anti-IgM\
    \ challenge is applied\n    in this experiment.\n  family_mapping: cThy28 reference\
    \ Q90679 sequenceversion1 equals AAA75591.1,242 aa,PF01878 at73-235.\n    NP_989618.2\
    \ differs at51 outside EVE. DT40 cDNA and TableS2 terminal primers support gene\
    \ assignment,\n    not exact internal sequence; no isolated domain is tested.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:9031\n  limitations: Whole-transcript\
    \ knockdown cannot identify a DUF residue mechanism. Pax5 transcripts remain\n\
    \    nonzero. Retained IgM argues against wholesale loss of B-cell phenotype but\
    \ is not exhaustive identity\n    profiling. AID need not be directly regulated\
    \ by Thy28.\n  nodes:\n  - node_id: cthy28-knockdown\n    label: Stable chicken\
    \ Thy28 knockdown with Seq3 or Seq4\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q90679\n  - node_id: pax5-rna\n    label: GAPDH-normalized Pax5\
    \ total and1A/1B transcripts\n    node_type: STATE\n  - node_id: pax5-protein\n\
    \    label: Pax5 immunoblot abundance\n    node_type: STATE\n  - node_id: aid-rna\n\
    \    label: GAPDH-normalized AID transcript abundance\n    node_type: STATE\n\
    \  edges:\n  - edge_id: knockdown-reduces-pax5-rna\n    subject: cthy28-knockdown\n\
    \    predicate: decreases\n    object: pax5-rna\n    mechanism: Both shRNA sequences\
    \ reduce total Pax5 and the1A/1B transcript readouts relative to shGFP.\n    \
    \  Steady-state RNA measurements do not distinguish transcription from RNA turnover,\
    \ and the residual\n      signal precludes an absolute requirement for every Pax5\
    \ transcript.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:25607658\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC4301804/\n      snippet: shRNA-mediated\
    \ knocking-down\n      explanation: Original Figure6E shows all four knockdown\
    \ clones and two shGFP controls with total\n        and alternative-first-exon\
    \ readouts.\n      cache_path: evidence/PF01878/fujita-2015-dt40.txt\n      cache_sha256:\
    \ f61693f99f1bd21db179449aa4124b0bdd6f0b1866aa63ff798a0aae0c56a080\n  - edge_id:\
    \ knockdown-reduces-pax5-protein\n    subject: cthy28-knockdown\n    predicate:\
    \ decreases\n    object: pax5-protein\n    mechanism: Pax5 protein bands decrease\
    \ with Thy28 knockdown in the four clones. This supports the\n      cellular effect\
    \ and complements the RNA measurements, without proving direct promoter binding\
    \ or\n      a protein-degradation mechanism.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:25607658\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4301804/\n      snippet:\
    \ shRNA-mediated knocking-down\n      explanation: Original Figure6D retains Thy28\
    \ and beta-tubulin controls for the Pax5 blot.\n      cache_path: evidence/PF01878/fujita-2015-dt40.txt\n\
    \      cache_sha256: f61693f99f1bd21db179449aa4124b0bdd6f0b1866aa63ff798a0aae0c56a080\n\
    \  - edge_id: knockdown-reduces-aid-rna\n    subject: cthy28-knockdown\n    predicate:\
    \ decreases\n    object: aid-rna\n    mechanism: AID RNA is lower in Seq3/Seq4\
    \ clones, whereas surface IgM is retained. The experiment does\n      not isolate\
    \ whether AID reduction is mediated by Pax5 or another consequence of Thy28 depletion.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:25607658\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4301804/\n\
    \      snippet: shRNA-mediated knocking-down\n      explanation: Original SupplementS1A/B\
    \ and its Methods distinguish AID RT-PCR from the unchanged\n        surface-IgM\
    \ readout; no numerical significance threshold is inferred from the inconsistent\
    \ asterisk\n        legend.\n      cache_path: evidence/PF01878/fujita-2015-dt40.txt\n\
    \      cache_sha256: f61693f99f1bd21db179449aa4124b0bdd6f0b1866aa63ff798a0aae0c56a080\n\
    - graph_id: cthy28-dt40-rescue\n  title: Expressed RNAi-resistant chicken Thy28\
    \ restores DT40 Pax5 readouts\n  scope: Fujita2015 Figure6F/G and SupplementS2,\
    \ Seq3 knockdown with expressed3xFLAG-cThy28 silent mutant.\n  context: Full-length\
    \ DT40 cDNA, N-terminal3xFLAG, synonymous changes at the Seq3 target; pcDNA-Hyg-3xFL-cThy28-mut\n\
    \    co-transfected with shRNA. Two expressing rescue clones; RNA normalized to\
    \ GAPDH,n=3. S2 includes\n    two nonexpressing rescue clones.\n  family_mapping:\
    \ Chicken Q90679/AAA75591.1 maps PF01878 at73-235. RefSeq NP_989618.2 has W51\
    \ rather than\n    L51 outside that match; the internal DT40 insert sequence is\
    \ not independently verified. Silent RNAi-resistance\n    substitutions do not\
    \ test protein residues.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:9031\n\
    \  limitations: Rescue supports an on-target contribution but cannot isolate the\
    \ EVE domain or direct molecular\n    action. Figure6F and SupplementS2 reuse\
    \ some lanes, not independent replication. Nonexpressing rescue\n    clones fail\
    \ to restore Pax5.\n  nodes:\n  - node_id: resistant-cthy28-expression\n    label:\
    \ Express RNAi-resistant3xFLAG-cThy28 during Seq3 knockdown\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q90679\n  - node_id: pax5-rna\n    label: Pax5\
    \ total and1A/1B transcript readouts\n    node_type: STATE\n  - node_id: pax5-protein\n\
    \    label: Pax5 protein abundance\n    node_type: STATE\n  edges:\n  - edge_id:\
    \ rescue-increases-pax5-rna\n    subject: resistant-cthy28-expression\n    predicate:\
    \ increases\n    object: pax5-rna\n    mechanism: Expressing rescue clones recover\
    \ total and1A/1B transcript levels toward shGFP controls\n      relative to depleted\
    \ cells. The comparison is a whole-protein complementation result, not proof\n\
    \      of a conserved biochemical transcription reaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:25607658\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4301804/\n\
    \      snippet: RNAi rescue experiment\n      explanation: Figure6G compared with\
    \ Figure6E and the explicitly described Seq3-resistant construct\n        supports\
    \ complementation; not every clone has a quantified knockdown-only paired measurement.\n\
    \      cache_path: evidence/PF01878/fujita-2015-dt40.txt\n      cache_sha256:\
    \ f61693f99f1bd21db179449aa4124b0bdd6f0b1866aa63ff798a0aae0c56a080\n  - edge_id:\
    \ rescue-increases-pax5-protein\n    subject: resistant-cthy28-expression\n  \
    \  predicate: increases\n    object: pax5-protein\n    mechanism: Pax5 bands return\
    \ toward control in the two clones expressing3xFLAG-cThy28, whereas S2\n     \
    \ clones3/4 without detectable tagged rescue protein remain low. This distinguishes\
    \ delivered construct\n      from successful protein expression.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:25607658\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4301804/\n\
    \      snippet: RNAi rescue experiment\n      explanation: Original Figure6F and\
    \ complete SupplementS2 blot/legend show expression-dependent rescue\n       \
    \ and the reused lanes.\n      cache_path: evidence/PF01878/fujita-2015-dt40.txt\n\
    \      cache_sha256: f61693f99f1bd21db179449aa4124b0bdd6f0b1866aa63ff798a0aae0c56a080\n\
    - graph_id: cthy28-dt40-myh9-enrichment\n  title: Thy28 perturbation changes upstream\
    \ Pax5-locus MYH9 ChIP enrichment\n  scope: Fujita2015 Figure7B, shGFP#1,Thy28-Seq3#2\
    \ and expressing rescue#2.\n  context: Anti-MYH9 ChIP measured as percent input,n=3;\
    \ compare upstream-3.3/-1.3/-0.5 kb amplicons separately\n    from TSS and downstream\
    \ amplicons. Stable DT40 derivatives, not purified binding proteins.\n  family_mapping:\
    \ Full-length cThy28 maps to the Q90679/AAA75591.1 reference, PF01878 at73-235;\
    \ no domain-specific\n    intervention. Exact internal sequence of the DT40-derived\
    \ tagged rescue is unresolved.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:9031\n\
    \  limitations: ChIP recovery is an occupancy-associated cellular readout, not\
    \ direct DNA contact or purified\n    recruitment kinetics. MYH9 transcript levels\
    \ are not comparably depleted in Figure8A, but protein-level\n    abundance/localization\
    \ alternatives are not fully resolved. Restoration is not uniform at all amplicons.\n\
    \  nodes:\n  - node_id: cthy28-knockdown\n    label: Thy28 Seq3#2 knockdown versus\
    \ shGFP#1\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q90679\n\
    \  - node_id: resistant-cthy28-expression\n    label: Express RNAi-resistant3xFLAG-cThy28\
    \ rescue#2\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q90679\n\
    \  - node_id: upstream-myh9-enrichment\n    label: MYH9 ChIP enrichment at upstream\
    \ Pax5 amplicons\n    node_type: STATE\n  edges:\n  - edge_id: knockdown-reduces-myh9-enrichment\n\
    \    subject: cthy28-knockdown\n    predicate: decreases\n    object: upstream-myh9-enrichment\n\
    \    mechanism: Thy28 depletion reduces upstream MYH9 ChIP recovery, particularly-3.3/-1.3/-0.5\
    \ kb. This\n      supports a cellular Thy28 contribution to locus association,\
    \ without proving direct Thy28-MYH9 binding\n      or identifying an RNA/DNA bridge.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:25607658\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4301804/\n\
    \      snippet: Interaction of MYH9 with the Pax5 1A promoter region.\n      explanation:\
    \ Original Figure7B and ChIP Methods retain exact clones and percent-input readout;\
    \ Figure7A\n        coIP/MS is association evidence only.\n      cache_path: evidence/PF01878/fujita-2015-dt40.txt\n\
    \      cache_sha256: f61693f99f1bd21db179449aa4124b0bdd6f0b1866aa63ff798a0aae0c56a080\n\
    \  - edge_id: rescue-increases-myh9-enrichment\n    subject: resistant-cthy28-expression\n\
    \    predicate: increases\n    object: upstream-myh9-enrichment\n    mechanism:\
    \ Expressing rescue#2 increases upstream ChIP signal relative to Seq3#2, with\
    \ incomplete\n      recovery at some sites. A single rescued clone and selected\
    \ amplicons do not establish universal\n      recruitment or direct activation\
    \ of transcription machinery.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:25607658\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4301804/\n      snippet:\
    \ Interaction of MYH9 with the Pax5 1A promoter region.\n      explanation: Figure7B\
    \ rescue and knockdown bars support locus-specific complementation without joining\n\
    \        ChIP occupancy to a measured transcriptional intermediate.\n      cache_path:\
    \ evidence/PF01878/fujita-2015-dt40.txt\n      cache_sha256: f61693f99f1bd21db179449aa4124b0bdd6f0b1866aa63ff798a0aae0c56a080\n\
    - graph_id: cthy28-dt40-myh9-knockdown\n  title: MYH9 knockdown lowers Pax5 expression\
    \ in the DT40 Thy28-associated system\n  scope: Fujita2015 Figure7C/D, two shMYH9\
    \ clones versus shGFP#1.\n  context: Stable DT40 derivatives; Pax5/MYH9 immunoblots\
    \ with CBB loading control and GAPDH-normalized\n    Pax5 RT-PCR,mean/SEM,n=3.\
    \ Figure8B separately measures Thy28 RNA.\n  family_mapping: PF01878 belongs to\
    \ the associated cThy28 Q90679/AAA75591.1 at73-235, not to MYH9. This\n    partner\
    \ perturbation contextualizes the Thy28 system; it does not test an EVE residue\
    \ or prove every\n    MYH9 effect is mediated through Thy28.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:9031\n  limitations: One MYH9 shRNA sequence\
    \ with two clones; no MYH9 rescue is reported. Thy28 transcript retention\n  \
    \  is not a protein-level control. Effects on transcription machinery or chromosomal\
    \ contacts remain\n    untested alternatives, not an observed causal relay from\
    \ Thy28.\n  nodes:\n  - node_id: myh9-knockdown\n    label: Stable MYH9 knockdown\
    \ in DT40\n    node_type: PERTURBATION\n  - node_id: pax5-rna\n    label: Pax5\
    \ total and1A/1B transcript readouts\n    node_type: STATE\n  - node_id: pax5-protein\n\
    \    label: Pax5 immunoblot abundance\n    node_type: STATE\n  edges:\n  - edge_id:\
    \ myh9-knockdown-reduces-pax5-rna\n    subject: myh9-knockdown\n    predicate:\
    \ decreases\n    object: pax5-rna\n    mechanism: Both shMYH9 clones have reduced\
    \ but nonzero total and1A/1B Pax5 RNA. The result is consistent\n      with a\
    \ partner contribution to expression, but does not isolate RNA synthesis from\
    \ stability or\n      show that Thy28 acts exclusively through MYH9.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:25607658\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4301804/\n\
    \      snippet: shRNA-mediated knocking-down\n      explanation: Original Figure7D\
    \ and Figure8B separate the Pax5 response from preserved Thy28 RNA,\n        without\
    \ claiming a MYH9 rescue or direct molecular step.\n      cache_path: evidence/PF01878/fujita-2015-dt40.txt\n\
    \      cache_sha256: f61693f99f1bd21db179449aa4124b0bdd6f0b1866aa63ff798a0aae0c56a080\n\
    \  - edge_id: myh9-knockdown-reduces-pax5-protein\n    subject: myh9-knockdown\n\
    \    predicate: decreases\n    object: pax5-protein\n    mechanism: Pax5 protein\
    \ bands decrease alongside MYH9 knockdown. No EVE-domain sufficiency, direct\n\
    \      MYH9 promoter catalysis or absolute Pax5-expression requirement is established.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:25607658\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4301804/\n\
    \      snippet: shRNA-mediated knocking-down\n      explanation: Original Figure7C\
    \ includes two MYH9-knockdown clones, shGFP and CBB controls; this\n        protein\
    \ readout is distinct from the RT-PCR result.\n      cache_path: evidence/PF01878/fujita-2015-dt40.txt\n\
    \      cache_sha256: f61693f99f1bd21db179449aa4124b0bdd6f0b1866aa63ff798a0aae0c56a080\n\
    curation_events:\n- timestamp: '2026-10-11T19:25:04Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate scoped Thy28 cellular causal effects\
    \ for PF01878\n  history_record: history/records/PF01878/2026-10-11T192504Z-codex-404ba6.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: concern
  summary: Q90679 sequenceversion1 equals AAA75591.1,242aa,PF01878 residues73-235;
    NP_989618.2 differs at51 outside EVE. DT40 terminal primers and cDNA origin identify
    cThy28 but not its exact internal batch sequence. Mouse Q91YJ3 equals BAC21100.1/NP_653126.1,226aa,PF01878
    residues56-219; Toyota's Thy28-V5 insert species/sequence is not established by
    its mouse host and incongruous protocol citation. Human Q9P016 maps56-218. RCSB-linked
    VcaM4I homolog A0ABY5IHE6 differs at13 positions from6YEX and reports only HNH_2;
    no exact PF01878 restriction-enzyme mapping is claimed.
  target_ids:
  - PF01878
  evidence_ids:
  - identity
  - primary
  - wehi-assays
  - mammalian-negatives
  - coverage-and-access
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Seventeen effects are INDIRECT/OBSERVED in nine PHENOTYPIC contexts. WEHI
    readouts distinguish partial membrane protection, compositional DNA distributions,
    clone6 p27, live-gated H2DCFDA intensity and pooled-clone phosphorylation/cleavage
    bands. Baseline differences, clone/time effects, unspecified Figure3A timing and
    the higher clone6 secondary-necrotic24h fraction prevent overstating protection.
    DT40 perturbation/rescue and MYH9 partner effects retain residual output and location-specific
    incomplete ChIP recovery. No parallel readouts are stitched into an observed molecular
    relay; MYH9 is not assigned PF01878.
  target_ids:
  - PF01878
  evidence_ids:
  - primary
  - native
  - wehi-assays
  - mammalian-negatives
  - coverage-and-access
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: All11128 frozen family members remain in scope. Exact tagged sequences,
    domain/residue contributions and direct biochemical mechanisms remain unresolved.
    Mouse knockout and human-cell negatives restrict generalization but are not equivalent
    to challenged WEHI overexpression. Modified-base proteomics,5J3E,SmMcrB,VcaM4I
    and other prokaryotic EVE evidence still require exact mapping and primary figure/data
    review. The study set is not exhaustive family coverage.
  target_ids:
  - PF01878
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01878-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve EVE molecular mechanism and cross-context transfer
  description: Verify the WEHI Thy28-V5 insert and DT40 internal sequence, test domain-specific
    perturbations with expression/folding/localization controls, and distinguish transcription
    from RNA turnover and direct contacts from ChIP/coIP recovery. Retain mammalian
    Pax5 negatives, rescue-expression controls and baseline differences. Inspect remaining
    modified-base and restriction-system primary data only after exact member-family
    mapping; preserve unsupported mechanisms as open questions.
  target_ids:
  - PF01878
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - wehi-assays
  - mammalian-negatives
  - coverage-and-access
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01878.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Verify the WEHI Thy28-V5 insert and DT40 internal sequence, test domain-specific
    perturbations with expression/folding/localization controls, and distinguish transcription
    from RNA turnover and direct contacts from ChIP/coIP recovery. Retain mammalian
    Pax5 negatives, rescue-expression controls and baseline differences. Inspect remaining
    modified-base and restriction-system primary data only after exact member-family
    mapping; preserve unsupported mechanisms as open questions.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01878
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Toyota Figures1-5, Fujita Figures6-8 and S1/S2, Kitaura Figures3/5/7 and S2 were
  visually inspected; TableS2 text was read. Original Fujita Figure9 and Kitaura S1
  images were not visually inspected. Remaining modified-base/restriction leads have
  only the stated partial coverage. No raw-data refit, assay-batch sequencing, independent
  replication or exhaustive survey. Rendered-page checks follow separately.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
