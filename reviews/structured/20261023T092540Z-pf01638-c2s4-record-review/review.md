# PF01638 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review

- Review: 20261023T092540Z-pf01638-c2s4-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-23T09:25:39Z
- Finished UTC: 2026-10-23T09:25:40Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Seven observed effects are retained in four graphs, separating intact-mass chemistry, WT/C11A EMSA, the lower-range K13A EMSA and heterologous GFP reporter responses. C11/K13 are outside current PF01638; the allosteric trajectory is not represented as directly observed. Stage 3 (PR #344) grounded the plus12-hxlr-species node in hxlr-formaldehyde-intact-mass-product to Bacillus subtilis HxlR (UniProtKB:P42406).

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Pending PF01638 in accession-ordered review of all 8296 frozen families; B. subtilis 168 HxlR is the specific example, with separately identified E. coli expression and reporter contexts.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base fde7d143a6b952fbc63b390cbfc27de38ac7701b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01638 | data/families/PF01638.yaml | generated | PF01638 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01638 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01638.

P42406 reference 120 aa, sequence version 3, exactly matches InterPro; PF01638 is 19-107, so C11/K13 and the synthetic F9-L15 peptide are outside it. PDB 7BZD is exactly GSH plus the reference, consistent with thrombin processing. The separate pBAD primer implies a possible S2G start difference, while Methods describe Gibson assembly; no exact reporter-plasmid sequence is claimed. BW25113 host taxonomy is verified separately from the B. subtilis protein-source taxon.

### Directed effects and limits

graph: supported. Targets: PF01638.

Four directly observed biochemical edges and three indirectly observed reporter effects remain in separate contexts. K13A's 0.05-0.2-uM EMSA range is not collapsed into WT/C11A's 0.2-0.6-uM series. Methods 1 mM versus gel 0.6 mM formaldehyde remains unresolved. Basal binding and high K13A reporter activity prevent null-function claims. Plus-12 mass is the observed product endpoint; bridge topology uses independent assays and static structures do not directly prove a helix-flipping trajectory.

### Remaining family coverage

completeness: concern. Targets: PF01638.

Native B. subtilis operon regulation, the 2005 cited study, exact pBAD N-terminal sequence, EMSA concentration discrepancy, reversibility, FAsor fusion contexts and other HxlR-like family ligands remain incomplete. Current protein-level evidence does not establish isolated-domain sufficiency or a universal DUF24 mechanism.

### Cycle 2 causal-graph protein-node grounding

identity: supported. Targets: PF01638.

Stage 3 (PR #344) grounded the plus12-hxlr-species node in hxlr-formaldehyde-intact-mass-product to Bacillus subtilis HxlR (UniProtKB:P42406).

## Findings

### additional-contexts: Resolve HxlR construct and assay discrepancies and extend native regulation evidence

minor / open / confirmed; issue key: pf01638-causal-context-coverage.

Verify the reporter plasmid N terminus and the 1-versus-0.6-mM EMSA treatment, retrieve the 2005 native-regulation study, and assess further members or engineered fusions as separate contexts. Preserve extra-domain residue mapping, residual binding, mutant basal differences and the distinction between static structural models and observed dynamic steps.

## Recommended Actions And Acceptance Checks

### extend-contexts

Verify the reporter plasmid N terminus and the 1-versus-0.6-mM EMSA treatment, retrieve the 2005 native-regulation study, and assess further members or engineered fusions as separate contexts. Preserve extra-domain residue mapping, residual binding, mutant basal differences and the distinction between static structural models and observed dynamic steps.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://www.nature.com/articles/s41467-020-20754-4; Zhu 2021 HxlR Results; cloning, purification, crystallization, FT-MS/MS-MS, EMSA and flow Methods; Figure 1 and Supplementary Figures 1/2 visually inspected; Supplementary Notes 2-4 and relevant Table 2 rows. | supports | Purified HxlR gains plus-12-Da species after formaldehyde treatment. WT DNA shifts increase, whereas C11A and K13A retain binding but lack the WT treatment response. Reporter GFP induction is reduced by either substitution, with distinct basal signal changes. Additional MS/MS, peptide and structural evidence supports the bridge assignment without turning separate assays into a tracked molecular trajectory. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/P42406/entry/pfam/PF01638/; Accession and domain locations; paired UniProt identity facts | supports | P42406 reference 120 aa, sequence version 3, exactly matches InterPro; PF01638 is 19-107, so C11/K13 and the synthetic F9-L15 peptide are outside it. PDB 7BZD is exactly GSH plus the reference, consistent with thrombin processing. The separate pBAD primer implies a possible S2G start difference, while Methods describe Gibson assembly; no exact reporter-plasmid sequence is claimed. BW25113 host taxonomy is verified separately from the B. subtilis protein-source taxon. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| stage4-prior-review | reviews/structured/20261011T120914Z-pf01638-hxlr-chemical-binding-and-reporter-contexts/review.yaml; Predecessor structured review 20261011T120914Z-pf01638-hxlr-chemical-binding-and-reporter-contexts | supports | Predecessor review 20261011T120914Z-pf01638-hxlr-chemical-binding-and-reporter-contexts verified and linked for finding continuity and semantic-digest progression on PF01638. |
| duf-projection-pf01638 | data/families/PF01638.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Figure 1 and Supplementary Figures 1/2 were visually inspected, including intact mass, EMSA, reporter distributions and viability/gating controls. No raw source-data reanalysis or experimental replication; the 2005 study and full FAsor application series were not reviewed. Construct sequence inference is explicitly unresolved.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261023T092540Z-pf01638-c2s4-record-review
title: PF01638 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review
started_at: '2026-10-23T09:25:39Z'
finished_at: '2026-10-23T09:25:40Z'
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
summary: 'Seven observed effects are retained in four graphs, separating intact-mass
  chemistry, WT/C11A EMSA, the lower-range K13A EMSA and heterologous GFP reporter
  responses. C11/K13 are outside current PF01638; the allosteric trajectory is not
  represented as directly observed. Stage 3 (PR #344) grounded the plus12-hxlr-species
  node in hxlr-formaldehyde-intact-mass-product to Bacillus subtilis HxlR (UniProtKB:P42406).'
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: fde7d143a6b952fbc63b390cbfc27de38ac7701b
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01638.yaml
    sha256: ba398636c115021e96fc3ea985bc07eae5a5fea193d7d52f164c57c47b8e10ba
    role: context
  - path: data/families/PF01638.yaml
    sha256: 096505b70e01944b7b1cfbc1c914080c5968a0e90079b709f3c1e0aa3614090b
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
  - path: evidence/PF01638/HxlR-identity.txt
    sha256: e23663acf3d3adc46689dc129df8ef6a933a50eee26871320360a8d3da8994da
    role: context
  - path: evidence/PF01638/zhu-2021-hxlr.txt
    sha256: 8ebaa26b6aa89c3d88b3e554a878cdc725c5c7693b62e90887e1f4069f9f217f
    role: context
  - path: reviews/structured/20261011T120914Z-pf01638-hxlr-chemical-binding-and-reporter-contexts/review.yaml
    sha256: a70832e091dc15626b17cda8df11d33c68d8a328bfb72e15100c50cac71f149b
    role: context
targets:
- target_id: PF01638
  path: data/families/PF01638.yaml
  label: PF01638
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01638.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: ffa91e2d59cb7d0e2cd5568a9f283ffb3eb7e464f0defbc66da4c9a76bf109d2
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Pending PF01638 in accession-ordered review of all 8296 frozen families;
    B. subtilis 168 HxlR is the specific example, with separately identified E. coli
    expression and reporter contexts.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01638
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Native B. subtilis operon regulation, the 2005 cited study, exact pBAD
      N-terminal sequence, EMSA concentration discrepancy, reversibility, FAsor fusion
      contexts and other HxlR-like family ligands remain incomplete. Current protein-level
      evidence does not establish isolated-domain sufficiency or a universal DUF24
      mechanism.
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
  - PF01638
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://www.nature.com/articles/s41467-020-20754-4
  locator: Zhu 2021 HxlR Results; cloning, purification, crystallization, FT-MS/MS-MS,
    EMSA and flow Methods; Figure 1 and Supplementary Figures 1/2 visually inspected;
    Supplementary Notes 2-4 and relevant Table 2 rows.
  accessed_at: '2026-10-11T12:09:14Z'
  support: supports
  snapshot_sha256: 8ebaa26b6aa89c3d88b3e554a878cdc725c5c7693b62e90887e1f4069f9f217f
  summary: Purified HxlR gains plus-12-Da species after formaldehyde treatment. WT
    DNA shifts increase, whereas C11A and K13A retain binding but lack the WT treatment
    response. Reporter GFP induction is reduced by either substitution, with distinct
    basal signal changes. Additional MS/MS, peptide and structural evidence supports
    the bridge assignment without turning separate assays into a tracked molecular
    trajectory.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P42406/entry/pfam/PF01638/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T12:09:14Z'
  support: supports
  snapshot_sha256: e23663acf3d3adc46689dc129df8ef6a933a50eee26871320360a8d3da8994da
  summary: P42406 reference 120 aa, sequence version 3, exactly matches InterPro;
    PF01638 is 19-107, so C11/K13 and the synthetic F9-L15 peptide are outside it.
    PDB 7BZD is exactly GSH plus the reference, consistent with thrombin processing.
    The separate pBAD primer implies a possible S2G start difference, while Methods
    describe Gibson assembly; no exact reporter-plasmid sequence is claimed. BW25113
    host taxonomy is verified separately from the B. subtilis protein-source taxon.
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T12:09:14Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: stage4-prior-review
  kind: prior_review
  reference: reviews/structured/20261011T120914Z-pf01638-hxlr-chemical-binding-and-reporter-contexts/review.yaml
  locator: Predecessor structured review 20261011T120914Z-pf01638-hxlr-chemical-binding-and-reporter-contexts
  accessed_at: '2026-10-23T09:25:40Z'
  support: supports
  snapshot_sha256: a70832e091dc15626b17cda8df11d33c68d8a328bfb72e15100c50cac71f149b
  summary: Predecessor review 20261011T120914Z-pf01638-hxlr-chemical-binding-and-reporter-contexts
    verified and linked for finding continuity and semantic-digest progression on
    PF01638.
- evidence_id: duf-projection-pf01638
  kind: record_content
  reference: data/families/PF01638.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-23T09:25:40Z'
  support: context_only
  snapshot_sha256: 096505b70e01944b7b1cfbc1c914080c5968a0e90079b709f3c1e0aa3614090b
  quote: "id: Pfam:PF01638\npfam_id: PF01638\nname: HxlR-like helix-turn-helix\nshort_name:\
    \ HxlR\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01638\n\
    counters:\n  proteins: 69591\n  matches: 70398\n  proteomes: 14385\n  taxa: 20061\n\
    \  structures: 18\n  alphafold_models: 41510\n  domain_architectures: 74\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002577\ndescription: HxlR, a member of this family, is\
    \ a DNA-binding protein that acts as a positive regulator\n  of the formaldehyde-inducible\
    \ hxlAB operon in Bacillus subtilis.\ncuration_history: history/records/PF01638\n\
    discussions:\n- discussion_id: hxlr-native-regulation-and-construct-questions\n\
    \  prompt: Resolve the pBAD N-terminal sequence and EMSA formaldehyde concentrations,\
    \ then extend native-regulation\n    and family-member coverage using separately\
    \ verified experiments.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: Seven\
    \ observed assay effects do not directly establish the complete allosteric trajectory,\n\
    \    native hxlAB regulation in B. subtilis, chemical reversibility or a shared\
    \ ligand mechanism across\n    PF01638.\n  evidence:\n  - reference: PMID:33495458\n\
    \    supports: PARTIAL\n    evidence_source: full_text_figure_1_supplementary_figures_1_2_table_2\n\
    \    explanation: Preserve the 1-versus-0.6-mM EMSA discrepancy, lower K13A protein\
    \ range, primer-implied\n      S2G possibility, GSH extension and C11/K13 positions\
    \ outside the current Pfam interval. C11A peptide\n      loses both plus-12 and\
    \ plus-30 products, whereas K13A retains plus-30; neither peptide is an isolated\n\
    \      Pfam domain.\n  - reference: doi:10.1111/j.1365-2958.2005.04702.x\n   \
    \ supports: PARTIAL\n    evidence_source: citation_lead_only\n    explanation:\
    \ The 2005 native-regulation study is cited by Zhu but was not independently retrieved\n\
    \      and reviewed here; no native knockout/rescue edges are inferred from that\
    \ citation.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n  notes: FAsor fusion\
    \ engineering, methylglyoxal responses, HypR/YodB/QsrR and structural-motion interpretations\n\
    \    require separate scope. Partial scientific self-review; IN_PROGRESS.\ncausal_graphs:\n\
    - graph_id: hxlr-formaldehyde-intact-mass-product\n  title: Formaldehyde produces\
    \ a plus-12-Da species of purified intact HxlR\n  scope: Purified B. subtilis\
    \ 168 HxlR expressed from pET28a in E. coli BL21(DE3), Zhu 2021 Supplementary\n\
    \    Figure 1c; not the synthetic peptide, cellular MS/MS or FAsor fusion assay.\n\
    \  context: Incubate 100 uM HxlR with 1 mM formaldehyde in 20 mM HEPES pH 7.5\
    \ and 300 mM NaCl for 1 h at\n    37 C; desalt by Micro Bio-Spin 6 and analyze\
    \ by Bruker Solarix XR FT-MS. Purification removes the\n    N-terminal His tag\
    \ with thrombin, followed by DTT treatment and SEC. The structural preparation\
    \ retains\n    a GSH cleavage extension.\n  family_mapping: P42406 sequence version\
    \ 3 is 120 aa; UniProt/InterPro sequences match, with PF01638\n    at 19-107.\
    \ PDB 7BZD entity 1 is exactly GSH plus this reference. C11 and K13 are outside\
    \ the current\n    Pfam interval. The experiment therefore concerns an intact\
    \ domain-bearing protein, not chemistry by\n    the isolated Pfam domain.\n  scope_status:\
    \ MECHANISTIC\n  taxon: NCBITaxon:224308\n  limitations: Intact-mass spectra establish\
    \ new plus-12-Da species, not their unique chemical topology\n    alone. Separate\
    \ crystal density, cellular tryptic MS/MS and synthetic-peptide substitutions\
    \ support\n    the C11/K13 methylene assignment. Those samples are not one time-resolved\
    \ reaction trajectory. Unmodified\n    and sodium-adduct species persist; no quantitative\
    \ yield, chemical reversibility or obligatory sequential\n    intermediate is\
    \ asserted.\n  nodes:\n  - node_id: formaldehyde-purified-hxlr\n    label: Treat\
    \ purified intact HxlR with 1 mM formaldehyde\n    node_type: PERTURBATION\n \
    \   grounding:\n    - UniProtKB:P42406\n  - node_id: plus12-hxlr-species\n   \
    \ label: HxlR species with a plus-12-Da intact mass shift\n    node_type: STATE\n\
    \    grounding:\n    - UniProtKB:P42406\n  edges:\n  - edge_id: formaldehyde-produces-plus12-species\n\
    \    subject: formaldehyde-purified-hxlr\n    predicate: produces\n    object:\
    \ plus12-hxlr-species\n    mechanism: Formaldehyde treatment produces new intact-protein\
    \ mass peaks displaced by 12 Da relative\n      to untreated HxlR. Cross-assay\
    \ evidence supports a C11/K13 methylene bridge, but the directly observed\n  \
    \    edge is the chemical-product mass response, not every proposed bond-forming\
    \ microstep.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:33495458\n      source_url:\
    \ https://www.nature.com/articles/s41467-020-20754-4\n      snippet: FA-treated\
    \ sample\n      explanation: Supplementary Figure 1c was visually inspected with\
    \ FT-MS Methods; Figure 1a/c/d and\n        Supplementary Note 3 provide separate\
    \ chemical-assignment evidence and its limits.\n      cache_path: evidence/PF01638/zhu-2021-hxlr.txt\n\
    \      cache_sha256: 8ebaa26b6aa89c3d88b3e554a878cdc725c5c7693b62e90887e1f4069f9f217f\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P42406/entry/pfam/PF01638/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P42406/entry/pfam/PF01638/\n\
    \      snippet: P42406 Pfam:PF01638; interval 19-107 inclusive.\n      explanation:\
    \ Exact reference/PDB sequence checks establish intact-protein scope and show\
    \ that C11/K13\n        are outside the current Pfam boundary.\n      cache_path:\
    \ evidence/PF01638/HxlR-identity.txt\n      cache_sha256: e23663acf3d3adc46689dc129df8ef6a933a50eee26871320360a8d3da8994da\n\
    - graph_id: hxlr-wt-c11a-dna-binding-response\n  title: Formaldehyde enhances\
    \ WT HxlR DNA binding, with little enhancement in C11A\n  scope: Purified pET28a-derived\
    \ WT and C11A HxlR, Zhu 2021 Figure 1e; separate from cellular reporter\n    and\
    \ K13A titrations.\n  context: EMSA Methods pretreat 100 uM protein with or without\
    \ 1 mM formaldehyde for 1-2 h at 37 C in\n    20 mM HEPES pH 7.5 and 300 mM NaCl.\
    \ Figure 1e instead labels 0.6 mM formaldehyde; this discrepancy\n    remains\
    \ unresolved. Final WT/C11A protein is 0.2, 0.4 or 0.6 uM in 20 ul with 50 nM\
    \ 50-bp BRH duplex,\n    20 mM HEPES pH 7.0, 50 mM KCl, 5 mM MgCl2 and 10% glycerol.\
    \ Table 2 specifies BRH-F/R, not the optimized\n    20-bp crystallization duplex.\
    \ Representative gels from three independent experiments.\n  family_mapping: P42406\
    \ / B. subtilis 168 reference 1-120 contains PF01638 19-107; C11 is outside that\n\
    \    interval. The N-terminal His tag is thrombin-cleaved, with GSH retained in\
    \ the sequence-verified structural\n    preparation. Neither C11A nor WT is an\
    \ isolated Pfam-domain construct.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:224308\n\
    \  limitations: Gel-shift enhancement is a direct biochemical binding response,\
    \ not a measured transcription\n    rate or fitted KD. C11A retains basal binding;\
    \ lack of enhancement is not complete loss of DNA binding.\n    Equal mutant folding\
    \ and active fraction are not established by these gels. The formaldehyde concentration\n\
    \    discrepancy is not resolved by assumed dilution, and static structural differences\
    \ do not directly\n    observe helix flipping.\n  nodes:\n  - node_id: formaldehyde-wt-binding\n\
    \    label: Formaldehyde pretreatment of WT HxlR\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:P42406\n  - node_id: shifted-brh-dna\n    label:\
    \ BRH DNA in the shifted HxlR-DNA complex\n    node_type: STATE\n  - node_id:\
    \ c11a-binding\n    label: C11A instead of WT HxlR\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:P42406\n  - node_id: fa-binding-enhancement\n\
    \    label: Formaldehyde-dependent enhancement of the DNA gel shift\n    node_type:\
    \ ACTIVITY\n  edges:\n  - edge_id: formaldehyde-increases-wt-dna-shift\n    subject:\
    \ formaldehyde-wt-binding\n    predicate: increases\n    object: shifted-brh-dna\n\
    \    mechanism: At matched WT protein concentrations, formaldehyde-treated samples\
    \ shift more BRH DNA than\n      untreated samples. This records the direct binding\
    \ response without assigning an observed allosteric\n      trajectory or native\
    \ operon output.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:33495458\n      source_url:\
    \ https://www.nature.com/articles/s41467-020-20754-4\n      snippet: enhance its\
    \ DNA affinity\n      explanation: Figure 1e was visually inspected with EMSA\
    \ Methods and Table 2. Protein concentration,\n        DNA identity and conflicting\
    \ formaldehyde labels are explicit.\n      cache_path: evidence/PF01638/zhu-2021-hxlr.txt\n\
    \      cache_sha256: 8ebaa26b6aa89c3d88b3e554a878cdc725c5c7693b62e90887e1f4069f9f217f\n\
    \  - edge_id: c11a-decreases-fa-binding-response\n    subject: c11a-binding\n\
    \    predicate: decreases\n    object: fa-binding-enhancement\n    mechanism:\
    \ C11A shows little additional shift after formaldehyde treatment compared with\
    \ WT's positive\n      response over the matched 0.2-0.6-uM series. Its residual\
    \ basal binding prevents calling the protein\n      binding-null, and the mutation\
    \ does not isolate the contribution of the Pfam domain.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:33495458\n      source_url: https://www.nature.com/articles/s41467-020-20754-4\n\
    \      snippet: enhance its DNA affinity\n      explanation: The WT/C11A paired\
    \ treatment lanes in Figure 1e and Results establish the response\n        difference,\
    \ with nonzero C11A binding retained.\n      cache_path: evidence/PF01638/zhu-2021-hxlr.txt\n\
    \      cache_sha256: 8ebaa26b6aa89c3d88b3e554a878cdc725c5c7693b62e90887e1f4069f9f217f\n\
    - graph_id: hxlr-k13a-dna-binding-response\n  title: K13A HxlR binds DNA but lacks\
    \ the WT formaldehyde enhancement\n  scope: Purified K13A HxlR in Zhu 2021 Supplementary\
    \ Figure 2d; its titration range differs from WT/C11A\n    Figure 1e.\n  context:\
    \ Supplementary Figure 2d uses 0.05, 0.1, 0.15 and 0.2 uM K13A, with or without\
    \ treatment labeled\n    0.6 mM formaldehyde. Shared EMSA Methods specify 1 mM\
    \ pretreatment of 100 uM protein for 1-2 h at\n    37 C, followed by dilution\
    \ into 50 nM BRH duplex with HEPES pH 7.0, KCl, MgCl2 and glycerol. The formaldehyde\n\
    \    discrepancy is unresolved. Representative gel from three independent experiments;\
    \ the WT positive\n    response is from the separate Figure 1e range.\n  family_mapping:\
    \ K13 is verified in P42406 and lies outside PF01638 19-107. The intact pET28a-derived\n\
    \    HxlR mutant is tested, not the isolated HxlR-like domain. The 7BZD sequence\
    \ check concerns WT structural\n    protein, not an independently resequenced\
    \ K13A assay stock.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:224308\n\
    \  limitations: The edge denotes loss of the WT treatment response, not lower\
    \ absolute DNA binding at identical\n    WT/K13A concentrations. K13A retains\
    \ strong basal shifts and the authors describe higher basal binding.\n    Different\
    \ concentration ranges do not establish a quantitative affinity ratio. Directness\
    \ is confined\n    to the biochemical response; a unique structural intermediate\
    \ or conformational trajectory is not\n    demonstrated.\n  nodes:\n  - node_id:\
    \ k13a-binding\n    label: K13A HxlR in its separate low-concentration titration\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:P42406\n  - node_id:\
    \ k13a-fa-binding-response\n    label: WT-like formaldehyde-dependent enhancement\
    \ of BRH DNA binding\n    node_type: ACTIVITY\n  edges:\n  - edge_id: k13a-decreases-fa-binding-response\n\
    \    subject: k13a-binding\n    predicate: decreases\n    object: k13a-fa-binding-response\n\
    \    mechanism: Unlike the WT positive response, K13A shows little treatment-dependent\
    \ enhancement across\n      its tested 0.05-0.2-uM range while retaining DNA binding.\
    \ The net loss of responsiveness is observed;\n      loss of all binding or equal-concentration\
    \ affinity comparisons are not asserted.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:33495458\n\
    \      source_url: https://www.nature.com/articles/s41467-020-20754-4\n      snippet:\
    \ the K13A mutant (HxlR-K13A) also remained insensitive to FA\n      explanation:\
    \ Supplementary Figure 2d and its caption were visually inspected, with the lower\
    \ protein\n        range and retained basal binding explicitly separated from\
    \ Figure 1e.\n      cache_path: evidence/PF01638/zhu-2021-hxlr.txt\n      cache_sha256:\
    \ 8ebaa26b6aa89c3d88b3e554a878cdc725c5c7693b62e90887e1f4069f9f217f\n- graph_id:\
    \ hxlr-heterologous-gfp-response\n  title: HxlR substitutions reduce the formaldehyde-induced\
    \ GFP reporter response in E. coli\n  scope: E. coli BW25113 carrying pBAD-HxlR\
    \ constructs labeled WT, C11A or K13A and a B. subtilis 168\n    hxlAB-promoter\
    \ GFP reporter, Zhu 2021 Figure 1f and Supplementary Figure 2e.\n  context: Dilute\
    \ overnight cultures 1:100 into LB, grow to OD600 0.6, induce HxlR with 4 mM L-arabinose\n\
    \    for 1 h, then treat with or without 600 uM formaldehyde for 40 min. Measure\
    \ GFP by flow cytometry\n    at 488-nm excitation and 530/30BP emission. Supplementary\
    \ Figure 2b/c provides colony-count viability\n    controls and scatter gating.\
    \ These are not the purified pET28a constructs or native B. subtilis cultures.\n\
    \  family_mapping: The source gene is P42406 from B. subtilis 168, with current\
    \ PF01638 19-107; C11 and\n    K13 are outside that interval. Supplementary Table\
    \ 2's pBAD forward primer is compatible with an MGRM\n    start instead of reference\
    \ MSRM if translated from its apparent start, but Methods describe Gibson\n  \
    \  assembly. A primer-implied S2G possibility remains unresolved; author WT/C11A/K13A\
    \ labels do not prove\n    exact native N-terminal sequence.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:679895\n  limitations: GFP distributions are\
    \ indirect reporter phenotypes, not direct transcription-rate, formaldehyde-detoxification\n\
    \    or native-operon measurements. C11A has lower basal reporter signal, whereas\
    \ K13A has higher basal\n    signal and little further induction. Viability/gating\
    \ controls do not establish equal mutant protein\n    abundance, folding or localization.\
    \ The pBAD sequence discrepancy is preserved rather than claiming\n    a resequenced\
    \ WT plasmid. Separate biochemical and cellular assays are not joined into one\
    \ observed\n    trajectory.\n  nodes:\n  - node_id: formaldehyde-wt-reporter\n\
    \    label: Add 600 uM formaldehyde to the WT-labeled HxlR reporter strain\n \
    \   node_type: PERTURBATION\n  - node_id: gfp-fluorescence\n    label: Cellular\
    \ GFP reporter fluorescence distribution\n    node_type: PHENOTYPE\n  - node_id:\
    \ c11a-reporter\n    label: C11A instead of WT-labeled pBAD-HxlR\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:P42406\n  - node_id: k13a-reporter\n\
    \    label: K13A instead of WT-labeled pBAD-HxlR\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:P42406\n  - node_id: fa-gfp-induction\n    label:\
    \ Formaldehyde-dependent GFP reporter induction\n    node_type: PHENOTYPE\n  edges:\n\
    \  - edge_id: formaldehyde-increases-wt-gfp\n    subject: formaldehyde-wt-reporter\n\
    \    predicate: increases\n    object: gfp-fluorescence\n    mechanism: Formaldehyde\
    \ shifts the WT-labeled reporter strain's GFP distribution toward greater fluorescence.\n\
    \      The measured cellular endpoint is consistent with HxlR-dependent promoter\
    \ activation but does not\n      directly measure RNA synthesis or formaldehyde\
    \ clearance.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:33495458\n      source_url:\
    \ https://www.nature.com/articles/s41467-020-20754-4\n      snippet: HxlR\n  \
    \    explanation: Figure 1f and Supplementary Figure 2e WT controls, flow-cytometry\
    \ Methods and the separate\n        viability/gating panels establish the scoped\
    \ fluorescence increase.\n      cache_path: evidence/PF01638/zhu-2021-hxlr.txt\n\
    \      cache_sha256: 8ebaa26b6aa89c3d88b3e554a878cdc725c5c7693b62e90887e1f4069f9f217f\n\
    \  - edge_id: c11a-decreases-gfp-induction\n    subject: c11a-reporter\n    predicate:\
    \ decreases\n    object: fa-gfp-induction\n    mechanism: The C11A reporter strain\
    \ shows little formaldehyde-dependent GFP induction relative to\n      the WT-labeled\
    \ strain. Its lower basal signal is retained as a distinct observation, not evidence\n\
    \      that only a single chemical step changed.\n    directness: INDIRECT\n \
    \   support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:33495458\n      source_url: https://www.nature.com/articles/s41467-020-20754-4\n\
    \      snippet: HxlR\n      explanation: Figure 1f paired WT/C11A treatment distributions\
    \ and Methods support decreased reporter\n        responsiveness, not isolated-domain\
    \ chemistry.\n      cache_path: evidence/PF01638/zhu-2021-hxlr.txt\n      cache_sha256:\
    \ 8ebaa26b6aa89c3d88b3e554a878cdc725c5c7693b62e90887e1f4069f9f217f\n  - edge_id:\
    \ k13a-decreases-gfp-induction\n    subject: k13a-reporter\n    predicate: decreases\n\
    \    object: fa-gfp-induction\n    mechanism: K13A has high basal GFP signal but\
    \ little additional formaldehyde-dependent induction compared\n      with the\
    \ WT-labeled strain. This is a loss of responsiveness, not a globally inactive\
    \ transcriptional\n      regulator or a GFP-null phenotype.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:33495458\n      source_url: https://www.nature.com/articles/s41467-020-20754-4\n\
    \      snippet: the K13A mutant (HxlR-K13A) also remained insensitive to FA\n\
    \      explanation: Supplementary Figure 2e was visually inspected with its caption\
    \ and Results; both high\n        basal signal and the weak treatment response\
    \ are retained.\n      cache_path: evidence/PF01638/zhu-2021-hxlr.txt\n      cache_sha256:\
    \ 8ebaa26b6aa89c3d88b3e554a878cdc725c5c7693b62e90887e1f4069f9f217f\ncuration_events:\n\
    - timestamp: '2026-10-11T12:00:09Z'\n  curator: Codex\n  action: CREATE\n  outcome:\
    \ changed\n  summary: Add scoped HxlR chemical, binding and reporter causal graphs\n\
    \  history_record: history/records/PF01638/2026-10-11T120009Z-codex-328cdb.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-11T12:09:23Z'\n\
    \  curator: Codex\n  action: REVIEW\n  outcome: needs_followup\n  summary: Retain\
    \ partial scientific causal-graph self-review for PF01638\n  history_record: history/records/PF01638/2026-10-11T120923Z-codex-690454.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-18T02:54:46Z'\n\
    \  curator: Antigravity\n  action: EDIT\n  outcome: changed\n  summary: Ground\
    \ causal graph gene and protein nodes in PF01638 with verified UniProtKB accessions\
    \ (UniProtKB:P42406)\n  history_record: history/records/PF01638/2026-10-18T025446Z-antigravity-794a65.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-23T07:48:04Z'\n\
    \  curator: Antigravity\n  action: EDIT\n  outcome: changed\n  summary: Ground\
    \ plus12-hxlr-species node in hxlr-formaldehyde-intact-mass-product to UniProtKB:P42406\n\
    \  history_record: history/records/PF01638/2026-10-23T074804Z-antigravity-163803.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: P42406 reference 120 aa, sequence version 3, exactly matches InterPro;
    PF01638 is 19-107, so C11/K13 and the synthetic F9-L15 peptide are outside it.
    PDB 7BZD is exactly GSH plus the reference, consistent with thrombin processing.
    The separate pBAD primer implies a possible S2G start difference, while Methods
    describe Gibson assembly; no exact reporter-plasmid sequence is claimed. BW25113
    host taxonomy is verified separately from the B. subtilis protein-source taxon.
  target_ids:
  - PF01638
  evidence_ids:
  - identity
  - primary
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Four directly observed biochemical edges and three indirectly observed
    reporter effects remain in separate contexts. K13A's 0.05-0.2-uM EMSA range is
    not collapsed into WT/C11A's 0.2-0.6-uM series. Methods 1 mM versus gel 0.6 mM
    formaldehyde remains unresolved. Basal binding and high K13A reporter activity
    prevent null-function claims. Plus-12 mass is the observed product endpoint; bridge
    topology uses independent assays and static structures do not directly prove a
    helix-flipping trajectory.
  target_ids:
  - PF01638
  evidence_ids:
  - primary
  - native
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Native B. subtilis operon regulation, the 2005 cited study, exact pBAD
    N-terminal sequence, EMSA concentration discrepancy, reversibility, FAsor fusion
    contexts and other HxlR-like family ligands remain incomplete. Current protein-level
    evidence does not establish isolated-domain sufficiency or a universal DUF24 mechanism.
  target_ids:
  - PF01638
  evidence_ids:
  - primary
- assessment_id: cycle2-partner-grounding-verification
  area: identity
  topic: Cycle 2 causal-graph protein-node grounding
  outcome: supported
  summary: 'Stage 3 (PR #344) grounded the plus12-hxlr-species node in hxlr-formaldehyde-intact-mass-product
    to Bacillus subtilis HxlR (UniProtKB:P42406).'
  target_ids:
  - PF01638
  evidence_ids:
  - stage4-prior-review
findings:
- finding_id: additional-contexts
  issue_key: pf01638-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve HxlR construct and assay discrepancies and extend native regulation
    evidence
  description: Verify the reporter plasmid N terminus and the 1-versus-0.6-mM EMSA
    treatment, retrieve the 2005 native-regulation study, and assess further members
    or engineered fusions as separate contexts. Preserve extra-domain residue mapping,
    residual binding, mutant basal differences and the distinction between static
    structural models and observed dynamic steps.
  target_ids:
  - PF01638
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01638.yaml
    role: Human-owned scientific overlay
  previous_occurrences:
  - repository: CultureBotAI/DUFMech
    review_id: 20261011T120914Z-pf01638-hxlr-chemical-binding-and-reporter-contexts
    finding_id: additional-contexts
actions:
- action_id: extend-contexts
  description: Verify the reporter plasmid N terminus and the 1-versus-0.6-mM EMSA
    treatment, retrieve the 2005 native-regulation study, and assess further members
    or engineered fusions as separate contexts. Preserve extra-domain residue mapping,
    residual binding, mutant basal differences and the distinction between static
    structural models and observed dynamic steps.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01638
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Figure 1 and Supplementary Figures 1/2 were visually inspected, including intact
  mass, EMSA, reporter distributions and viability/gating controls. No raw source-data
  reanalysis or experimental replication; the 2005 study and full FAsor application
  series were not reviewed. Construct sequence inference is explicitly unresolved.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
