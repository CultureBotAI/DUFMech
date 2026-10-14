# PF01904 YecE relative-growth effects and hypothetical Tm1631 chemistry

- Review: 20261011T231925Z-pf01904-yece-relative-growth-and-tm1631-computational-cleavage
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T23:18:31Z
- Finished UTC: 2026-10-11T23:19:25Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Two graphs retain 21 OBSERVED, INDIRECT, EXPERIMENTAL growth effects and two HYPOTHESIZED, UNRESOLVED, COMPUTATIONAL cleavage steps. All 21 growth source rows and directions match the primary spreadsheet. Six main figures and two protocol pages were visually inspected; three spreadsheets and supplemental text/tables were parsed. Two open discussions retain assay, model, clone and member gaps. Status remains IN_PROGRESS; this is partial same-agent scientific review, not independent or full-family endorsement.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01904 DUF72; all 21 YecE recipient rows in Babu2014 Table S2 and a separate two-step Tm1631 computational proposal.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01904 | data/families/PF01904.yaml | generated | PF01904 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01904 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01904.

Frozen PF01904 is DUF72/IPR002763 with 14646 proteins. YecE P37348 sequence version 4 equals NP_416382.1, AAC74938.1 and BAA15679.2, 272 aa, PF01904 3-258. Tm1631 Q9X1W6 sequence version 1 equals AAD36698.1 and WP_004082107.1, 261 aa, PF01904 3-259. PDB 1VPQ entity 13-273 exactly matches Q9X1W6 after its 12-residue tag. The supplementary Figure S2 caption explicitly resolves model Lys73 as native K72; native residue 73 is T. Reference equality does not independently sequence historical assay clones or every atom of a modeled construct. Taxa and experimental systems remain separate, without adopting a secondary database strain label as the assay.

### Directed effects and limits

graph: supported. Targets: PF01904.

The joint-genotype source nodes do not imply gene-to-gene causation or isolated single-deletion effects. Positive scores do not establish WT rescue, absolute growth gain or binding. Tm1631 chemistry remains a separate hypothetical sequence under joint modeled DNA/two-Mg/nucleophile conditions. Constructed endpoints, a modeled pentacovalent minimum and relative potential energies do not establish measured activity, trapped intermediates, rates or activation free energies. No early lysine deprotonation edge or experimental K73 mutant is invented. The 2016 model extends 2013 rather than independently replicating an experiment; PDB sulfate/water does not become observed DNA/Mg binding. Every edge's cache hash and quotation were checked separately from scientific interpretation.

### Remaining family coverage

completeness: concern. Targets: PF01904.

Most 14646 frozen members, independent allele/rescue validation, exact historical clones, raw colony images and row-specific dispersion remain unassessed. Supplementary DOC figures were not visually inspected because conversion retained text but dropped images. Only five of 48 model coordinate subsets were parsed, and no QM calculation or trajectory was rerun. YunF expression, cofitness, beta-clamp motifs, prophage insertion at the yecE locus and similarly named unrelated enzymes remain excluded leads, not negative results or experimentally established DUF72 mechanisms.

## Findings

### additional-contexts: Validate member-specific mechanisms and extend assay coverage

minor / open / confirmed; issue key: pf01904-causal-context-coverage.

Seek independent YecE alleles, complementation, raw normalized fitness and precise clone identities while retaining the multiplicative comparator and marker/polar alternatives. Test Tm1631 binding, product identity, substrate specificity, metal dependence and residue effects with suitable folding controls. Inspect remaining supplementary figures and member-specific primary contexts; preserve resolved model/native numbering and keep unsupported chemistry hypothetical. Any supported additions need actual history, guarded regeneration and a successor scoped review.

## Recommended Actions And Acceptance Checks

### extend-contexts

Seek independent YecE alleles, complementation, raw normalized fitness and precise clone identities while retaining the multiplicative comparator and marker/polar alternatives. Test Tm1631 binding, product identity, substrate specificity, metal dependence and residue effects with suitable folding controls. Inspect remaining supplementary figures and member-specific primary contexts; preserve resolved model/native numbering and keep unsupported chemistry hypothetical. Any supported additions need actual history, guarded regeneration and a successor scoped review.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/; Main screen Methods/Results, parsed Tables S1/S2/S16, and visually inspected single-page Protocols S2/S16. | supports | Twenty-one joint yecE/partner deletion genotypes have normalized colony growth below (16) or above (5) the multiplicative single-mutant expectation. The comparator is not WT or addition of one deletion. All selected donors are This Study, non-essential Hfr Cavalli deletion::Cm strains; recipients are Keio deletion::Kan. Rich LB dual selection, 36 h at 32 C, and eight measurements per pair remain explicit. Exact source rows, scores and directions were programmatically checked against the parsed primary table. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/P37348/; Accession and domain locations; paired UniProt identity facts | supports | Frozen PF01904 is DUF72/IPR002763 with 14646 proteins. YecE P37348 sequence version 4 equals NP_416382.1, AAC74938.1 and BAA15679.2, 272 aa, PF01904 3-258. Tm1631 Q9X1W6 sequence version 1 equals AAD36698.1 and WP_004082107.1, 261 aa, PF01904 3-259. PDB 1VPQ entity 13-273 exactly matches Q9X1W6 after its 12-residue tag. The supplementary Figure S2 caption explicitly resolves model Lys73 as native K72; native residue 73 is T. Reference equality does not independently sequence historical assay clones or every atom of a modeled construct. Taxa and experimental systems remain separate, without adopting a secondary database strain label as the assay. |
| tm1631-computational-chemistry | https://pmc.ncbi.nlm.nih.gov/articles/PMC4939058/; Main Methods/Results, original Figures 1-5, parsed supplementary captions/tables and five coordinate subsets. | supports | Two hypothetical chemical steps retain initial-state and energy-profile assumptions; supplemental caption resolves Lys73/native K72. No nuclease assay or simulation rerun. |
| tm1631-pose-generation | https://pmc.ncbi.nlm.nih.gov/articles/PMC3828134/; Selected main Methods/Results, original Figure 5 and parsed supplemental text/captions. | supports | Binding-site similarity and restrained dynamics yield a model, not physical binding or experimentally demonstrated DNA repair; MM/GBSA entropy assumptions remain explicit. |
| source-search-and-limits | evidence/PF01904/coverage.txt; Dated source/member search, excluded leads and access ledger. | supports | Secondary database interaction entry led to primary data without being counted as replication. UV cache, CDN and converter retries were scoped; no global access fix or configuration change. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01904 | data/families/PF01904.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Visually inspected Konc2013 Figure 5, Ogrizek2016 Figures 1-5 and Babu2014 Protocols S2/S16. Parsed three XLS tables after conversion and 2013/2016 DOC text/tables without their images. Five model coordinate subsets were parsed, not rerun. No raw colony-image, exact clone-sequence, whole-family or full publication-QC certification.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T231925Z-pf01904-yece-relative-growth-and-tm1631-computational-cleavage
title: PF01904 YecE relative-growth effects and hypothetical Tm1631 chemistry
started_at: '2026-10-11T23:18:31Z'
finished_at: '2026-10-11T23:19:25Z'
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
summary: Two graphs retain 21 OBSERVED, INDIRECT, EXPERIMENTAL growth effects and
  two HYPOTHESIZED, UNRESOLVED, COMPUTATIONAL cleavage steps. All 21 growth source
  rows and directions match the primary spreadsheet. Six main figures and two protocol
  pages were visually inspected; three spreadsheets and supplemental text/tables were
  parsed. Two open discussions retain assay, model, clone and member gaps. Status
  remains IN_PROGRESS; this is partial same-agent scientific review, not independent
  or full-family endorsement.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01904.yaml
    sha256: dead3287b9d249d69eabfce766d6f82496a862ef5bd634e6da5c9d7b6bf6afc4
    role: context
  - path: data/families/PF01904.yaml
    sha256: df7202bb00be8d641eed87640750a51a1257f747acd4802cc43831b23f3b64ff
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
  - path: evidence/PF01904/babu-2014.txt
    role: context
    sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4
  - path: evidence/PF01904/identity.txt
    role: context
    sha256: a4f4f4c5752a5b1fbc76f5093d284bdbfb25a2b6dd87db4545f577d6b2390b35
  - path: evidence/PF01904/ogrizek-2016.txt
    role: context
    sha256: 14035fbe893099339ba98311c2b78203dfc6e94b87e81cac2f573700206708d0
  - path: evidence/PF01904/konc-2013.txt
    role: context
    sha256: 7d5ecf80239acc3851042ca722f16099a4c5294a94061e20ae1037e8ef77f034
  - path: evidence/PF01904/coverage.txt
    role: context
    sha256: 4a06552287c12c4394703caea51677a734a7b9389b4496dc91c2762994e2714d
targets:
- target_id: PF01904
  path: data/families/PF01904.yaml
  label: PF01904
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01904.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 2d29ac3a5a2b7c6a0bb314f77cf7c20e15fe922c710584ad9454ce13a6ccc1cd
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01904 DUF72; all 21 YecE recipient rows in Babu2014 Table S2 and a
    separate two-step Tm1631 computational proposal.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01904
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Most 14646 frozen members, independent allele/rescue validation, exact
      historical clones, raw colony images and row-specific dispersion remain unassessed.
      Supplementary DOC figures were not visually inspected because conversion retained
      text but dropped images. Only five of 48 model coordinate subsets were parsed,
      and no QM calculation or trajectory was rerun. YunF expression, cofitness, beta-clamp
      motifs, prophage insertion at the yecE locus and similarly named unrelated enzymes
      remain excluded leads, not negative results or experimentally established DUF72
      mechanisms.
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
  - PF01904
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/
  locator: Main screen Methods/Results, parsed Tables S1/S2/S16, and visually inspected
    single-page Protocols S2/S16.
  accessed_at: '2026-10-11T23:19:25Z'
  support: supports
  snapshot_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4
  summary: Twenty-one joint yecE/partner deletion genotypes have normalized colony
    growth below (16) or above (5) the multiplicative single-mutant expectation. The
    comparator is not WT or addition of one deletion. All selected donors are This
    Study, non-essential Hfr Cavalli deletion::Cm strains; recipients are Keio deletion::Kan.
    Rich LB dual selection, 36 h at 32 C, and eight measurements per pair remain explicit.
    Exact source rows, scores and directions were programmatically checked against
    the parsed primary table.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/P37348/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T23:19:25Z'
  support: supports
  snapshot_sha256: a4f4f4c5752a5b1fbc76f5093d284bdbfb25a2b6dd87db4545f577d6b2390b35
  summary: Frozen PF01904 is DUF72/IPR002763 with 14646 proteins. YecE P37348 sequence
    version 4 equals NP_416382.1, AAC74938.1 and BAA15679.2, 272 aa, PF01904 3-258.
    Tm1631 Q9X1W6 sequence version 1 equals AAD36698.1 and WP_004082107.1, 261 aa,
    PF01904 3-259. PDB 1VPQ entity 13-273 exactly matches Q9X1W6 after its 12-residue
    tag. The supplementary Figure S2 caption explicitly resolves model Lys73 as native
    K72; native residue 73 is T. Reference equality does not independently sequence
    historical assay clones or every atom of a modeled construct. Taxa and experimental
    systems remain separate, without adopting a secondary database strain label as
    the assay.
- evidence_id: tm1631-computational-chemistry
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4939058/
  locator: Main Methods/Results, original Figures 1-5, parsed supplementary captions/tables
    and five coordinate subsets.
  summary: Two hypothetical chemical steps retain initial-state and energy-profile
    assumptions; supplemental caption resolves Lys73/native K72. No nuclease assay
    or simulation rerun.
  accessed_at: '2026-10-11T23:19:25Z'
  support: supports
  snapshot_sha256: 14035fbe893099339ba98311c2b78203dfc6e94b87e81cac2f573700206708d0
- evidence_id: tm1631-pose-generation
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3828134/
  locator: Selected main Methods/Results, original Figure 5 and parsed supplemental
    text/captions.
  summary: Binding-site similarity and restrained dynamics yield a model, not physical
    binding or experimentally demonstrated DNA repair; MM/GBSA entropy assumptions
    remain explicit.
  accessed_at: '2026-10-11T23:19:25Z'
  support: supports
  snapshot_sha256: 7d5ecf80239acc3851042ca722f16099a4c5294a94061e20ae1037e8ef77f034
- evidence_id: source-search-and-limits
  kind: search
  reference: evidence/PF01904/coverage.txt
  locator: Dated source/member search, excluded leads and access ledger.
  search_scope: Ignored/hidden-inclusive local curation/evidence/history/review/report
    search excluding inventory.json for PF01904/DUF72/IPR002763; public PF01904, DUF72,
    UPF0759, Tm1631, YecE, YunF, nuclease, repair, deletion and genetic-interaction
    queries. Current sequence/domain and deposited reference comparisons; not an exhaustive
    all-member search.
  summary: Secondary database interaction entry led to primary data without being
    counted as replication. UV cache, CDN and converter retries were scoped; no global
    access fix or configuration change.
  accessed_at: '2026-10-11T23:19:25Z'
  support: supports
  snapshot_sha256: 4a06552287c12c4394703caea51677a734a7b9389b4496dc91c2762994e2714d
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T23:19:25Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01904
  kind: record_content
  reference: data/families/PF01904.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T23:19:25Z'
  support: context_only
  snapshot_sha256: df7202bb00be8d641eed87640750a51a1257f747acd4802cc43831b23f3b64ff
  quote: "id: Pfam:PF01904\npfam_id: PF01904\nname: Protein of unknown function DUF72\n\
    short_name: DUF72\nseed_status: UNKNOWN_CANDIDATE\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01904\n\
    counters:\n  proteins: 14646\n  matches: 14657\n  proteomes: 9981\n  taxa: 13949\n\
    \  structures: 3\n  alphafold_models: 8861\n  domain_architectures: 30\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002763\ndescription: The function of this family is unknown.\n\
    curation_history: history/records/PF01904\ndiscussions:\n- discussion_id: duf72-model-to-experiment-gap\n\
    \  prompt: Test the proposed Tm1631 chemistry without treating simulation as experimental\
    \ characterization.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: Two computational\
    \ steps preserve the proposed reaction but do not establish nuclease activity.\n\
    \    The 2016 work extends the 2013 model rather than independently replicating\
    \ an experiment.\n  evidence:\n  - reference: PMID:24244144\n    supports: PARTIAL\n\
    \    evidence_source: primary_computational_methods\n    explanation: Binding-site\
    \ similarity, restrained molecular dynamics and an entropy-qualified MM/GBSA\n\
    \      comparison generate a candidate pose; beta-clamp association is motif based,\
    \ not measured.\n  - reference: PMID:27398092\n    supports: PARTIAL\n    evidence_source:\
    \ primary_computational_methods_and_supplement\n    explanation: Main figures\
    \ and supplemental caption resolve the proposed path and model Lys73/native\n\
    \      K72 mapping. Initial protonation and ion chemistry remain assumptions,\
    \ not experimentally tested\n      steps.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n\
    \  notes: Seek independently verified DNA binding, product identity, metal dependence,\
    \ substrate specificity\n    and residue perturbations with folding/abundance\
    \ controls. Keep modeled/native numbering explicit.\n    Supplementary DOC text/tables\
    \ were parsed but images were dropped by conversion, so their plots were\n   \
    \ not visually checked. No simulation was rerun.\n- discussion_id: duf72-yece-assay-and-member-coverage\n\
    \  prompt: Independently validate YecE joint-genotype phenotypes and extend member-specific\
    \ coverage.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: Twenty-one observed\
    \ indirect growth effects preserve a multiplicative single-mutant baseline,\n\
    \    not a molecular interaction network or general DUF72 DNA-repair mechanism.\n\
    \  evidence:\n  - reference: PMID:24586182\n    supports: SUPPORT\n    evidence_source:\
    \ primary_tables_and_screen_protocols\n    explanation: All exact YecE recipient\
    \ rows were retained with scores and donor identities; linkage\n      filtering\
    \ and repeated colony measurements do not remove every marker, polar or secondary-mutation\n\
    \      alternative.\n  - reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/P37348/\n\
    \    supports: SUPPORT\n    evidence_source: current_member_mapping\n    explanation:\
    \ Reference YecE maps PF01904 at 3-258; reference equality does not independently\
    \ sequence\n      each historical assay clone.\n  posed_by: Codex\n  posed_date:\
    \ '2026-10-11'\n  notes: Examine raw fitness data, independent alleles, complementation\
    \ and exact Hfr/Keio-derived clone\n    identity. Positive interactions are not\
    \ WT rescue. YunF expression, cofitness, prophage insertion\n    at the yecE locus\
    \ and similarly named unrelated enzymes remain excluded leads. Most of the 14646\
    \ frozen\n    members and other structures remain unassessed. Keep IN_PROGRESS;\
    \ this is partial same-agent curation.\ncausal_graphs:\n- graph_id: yece-joint-deletion-relative-growth-2014\n\
    \  title: YecE joint deletions alter colony growth relative to multiplicative\
    \ expectations\n  scope: Babu2014 Table S2; all 21 exact b1868__yecE recipient\
    \ rows, each a separate joint genotype.\n  context: Hfr Cavalli donor deletion::Cm\
    \ transferred into a Keio F- recipient deletion::Kan; rich LB\n    with dual selection,\
    \ 36 h outgrowth at 32 C. Protocol S2 reports two screens, four biological recipient\n\
    \    colonies and eight measurements per pair.\n  family_mapping: E. coli K-12\
    \ YecE P37348, sequence version 4, equals NP_416382.1, AAC74938.1 and BAA15679.2;\n\
    \    272 aa with PF01904 at 3-258. b1868/JW1857 reference identity is not independent\
    \ sequencing of the\n    historical assay clone.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:83333\n  limitations: Normalized double-mutant colony growth\
    \ is compared with multiplicative expected fitness\n    from the single mutants,\
    \ not WT or the addition of one deletion. Positive scores are not WT rescue\n\
    \    or faster absolute growth. All 21 donors are non-essential and labeled This\
    \ Study in Table S1; Table\n    S16 verifies their Hfr Cavalli deletion::Cm context.\
    \ Raw colony images, row-specific dispersion, exact\n    clone sequences and allele-specific\
    \ rescue were not inspected. Marker, polar and secondary-mutation\n    effects\
    \ remain alternatives; no gene-to-gene molecular pathway is inferred.\n  nodes:\n\
    \  - node_id: yece-caic-joint-loss\n    label: Joint yecE (b1868) and caiC (b0037)\
    \ deletion\n    node_type: PERTURBATION\n  - node_id: yece-degp-joint-loss\n \
    \   label: Joint yecE (b1868) and degP (b0161) deletion\n    node_type: PERTURBATION\n\
    \  - node_id: yece-asnb-joint-loss\n    label: Joint yecE (b1868) and asnB (b0674)\
    \ deletion\n    node_type: PERTURBATION\n  - node_id: yece-ycbx-joint-loss\n \
    \   label: Joint yecE (b1868) and ycbX (b0947) deletion\n    node_type: PERTURBATION\n\
    \  - node_id: yece-cbpa-joint-loss\n    label: Joint yecE (b1868) and cbpA (b1000)\
    \ deletion\n    node_type: PERTURBATION\n  - node_id: yece-yceg-joint-loss\n \
    \   label: Joint yecE (b1868) and yceG (b1097) deletion\n    node_type: PERTURBATION\n\
    \  - node_id: yece-pspf-joint-loss\n    label: Joint yecE (b1868) and pspF (b1303)\
    \ deletion\n    node_type: PERTURBATION\n  - node_id: yece-pspa-joint-loss\n \
    \   label: Joint yecE (b1868) and pspA (b1304) deletion\n    node_type: PERTURBATION\n\
    \  - node_id: yece-grxd-joint-loss\n    label: Joint yecE (b1868) and grxD (b1654)\
    \ deletion\n    node_type: PERTURBATION\n  - node_id: yece-cspc-joint-loss\n \
    \   label: Joint yecE (b1868) and cspC (b1823) deletion\n    node_type: PERTURBATION\n\
    \  - node_id: yece-yfbj-joint-loss\n    label: Joint yecE (b1868) and yfbJ (b2258)\
    \ deletion\n    node_type: PERTURBATION\n  - node_id: yece-csda-joint-loss\n \
    \   label: Joint yecE (b1868) and csdA (b2810) deletion\n    node_type: PERTURBATION\n\
    \  - node_id: yece-ygeo-joint-loss\n    label: Joint yecE (b1868) and ygeO (b2859)\
    \ deletion\n    node_type: PERTURBATION\n  - node_id: yece-ygfz-joint-loss\n \
    \   label: Joint yecE (b1868) and ygfZ (b2898) deletion\n    node_type: PERTURBATION\n\
    \  - node_id: yece-yghd-joint-loss\n    label: Joint yecE (b1868) and yghD (b2968)\
    \ deletion\n    node_type: PERTURBATION\n  - node_id: yece-exbb-joint-loss\n \
    \   label: Joint yecE (b1868) and exbB (b3006) deletion\n    node_type: PERTURBATION\n\
    \  - node_id: yece-ttdb-joint-loss\n    label: Joint yecE (b1868) and ttdB (b3062)\
    \ deletion\n    node_type: PERTURBATION\n  - node_id: yece-gltb-joint-loss\n \
    \   label: Joint yecE (b1868) and gltB (b3212) deletion\n    node_type: PERTURBATION\n\
    \  - node_id: yece-gltd-joint-loss\n    label: Joint yecE (b1868) and gltD (b3213)\
    \ deletion\n    node_type: PERTURBATION\n  - node_id: yece-alr-joint-loss\n  \
    \  label: Joint yecE (b1868) and alr (b4053) deletion\n    node_type: PERTURBATION\n\
    \  - node_id: yece-idnd-joint-loss\n    label: Joint yecE (b1868) and idnD (b4267)\
    \ deletion\n    node_type: PERTURBATION\n  - node_id: relative-colony-growth\n\
    \    label: Normalized colony growth relative to the multiplicative expectation\n\
    \    node_type: PHENOTYPE\n  edges:\n  - edge_id: yece-caic-increases-relative-growth\n\
    \    subject: yece-caic-joint-loss\n    predicate: increases\n    object: relative-colony-growth\n\
    \    mechanism: The joint yecE/caiC deletion has an alleviating S-score of 3.37006,\
    \ indicating normalized\n      colony growth above the multiplicative single-mutant\
    \ expectation. This is an indirect joint-genotype\n      phenotype, not the isolated\
    \ effect of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 770, b0037__caiC donor and b1868__yecE\n\
    \        recipient, score 3.37006. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-degp-decreases-relative-growth\n    subject: yece-degp-joint-loss\n\
    \    predicate: decreases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/degP deletion has an aggravating S-score of -5.62642, indicating\
    \ normalized\n      colony growth below the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 2485, b0161__degP donor and b1868__yecE\n\
    \        recipient, score -5.62642. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-asnb-increases-relative-growth\n    subject: yece-asnb-joint-loss\n\
    \    predicate: increases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/asnB deletion has an alleviating S-score of 4.08422, indicating\
    \ normalized\n      colony growth above the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 5426, b0674__asnB donor and b1868__yecE\n\
    \        recipient, score 4.08422. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-ycbx-decreases-relative-growth\n    subject: yece-ycbx-joint-loss\n\
    \    predicate: decreases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/ycbX deletion has an aggravating S-score of -4.66203, indicating\
    \ normalized\n      colony growth below the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 8381, b0947__ycbX donor and b1868__yecE\n\
    \        recipient, score -4.66203. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-cbpa-decreases-relative-growth\n    subject: yece-cbpa-joint-loss\n\
    \    predicate: decreases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/cbpA deletion has an aggravating S-score of -5.59002, indicating\
    \ normalized\n      colony growth below the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 9826, b1000__cbpA donor and b1868__yecE\n\
    \        recipient, score -5.59002. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-yceg-decreases-relative-growth\n    subject: yece-yceg-joint-loss\n\
    \    predicate: decreases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/yceG deletion has an aggravating S-score of -3.49669, indicating\
    \ normalized\n      colony growth below the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 10464, b1097__yceG donor and b1868__yecE\n\
    \        recipient, score -3.49669. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-pspf-decreases-relative-growth\n    subject: yece-pspf-joint-loss\n\
    \    predicate: decreases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/pspF deletion has an aggravating S-score of -7.56451, indicating\
    \ normalized\n      colony growth below the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 12254, b1303__pspF donor and b1868__yecE\n\
    \        recipient, score -7.56451. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-pspa-increases-relative-growth\n    subject: yece-pspa-joint-loss\n\
    \    predicate: increases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/pspA deletion has an alleviating S-score of 4.29089, indicating\
    \ normalized\n      colony growth above the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 12789, b1304__pspA donor and b1868__yecE\n\
    \        recipient, score 4.29089. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-grxd-decreases-relative-growth\n    subject: yece-grxd-joint-loss\n\
    \    predicate: decreases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/grxD deletion has an aggravating S-score of -3.97002, indicating\
    \ normalized\n      colony growth below the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 15375, b1654__grxD donor and b1868__yecE\n\
    \        recipient, score -3.97002. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-cspc-decreases-relative-growth\n    subject: yece-cspc-joint-loss\n\
    \    predicate: decreases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/cspC deletion has an aggravating S-score of -3.83624, indicating\
    \ normalized\n      colony growth below the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 17866, b1823__cspC donor and b1868__yecE\n\
    \        recipient, score -3.83624. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-yfbj-decreases-relative-growth\n    subject: yece-yfbj-joint-loss\n\
    \    predicate: decreases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/yfbJ deletion has an aggravating S-score of -4.12818, indicating\
    \ normalized\n      colony growth below the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 19366, b2258__yfbJ donor and b1868__yecE\n\
    \        recipient, score -4.12818. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-csda-increases-relative-growth\n    subject: yece-csda-joint-loss\n\
    \    predicate: increases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/csdA deletion has an alleviating S-score of 5.14678, indicating\
    \ normalized\n      colony growth above the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 24559, b2810__csdA donor and b1868__yecE\n\
    \        recipient, score 5.14678. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-ygeo-decreases-relative-growth\n    subject: yece-ygeo-joint-loss\n\
    \    predicate: decreases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/ygeO deletion has an aggravating S-score of -4.1279, indicating\
    \ normalized\n      colony growth below the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 26960, b2859__ygeO donor and b1868__yecE\n\
    \        recipient, score -4.1279. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-ygfz-decreases-relative-growth\n    subject: yece-ygfz-joint-loss\n\
    \    predicate: decreases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/ygfZ deletion has an aggravating S-score of -13.2114, indicating\
    \ normalized\n      colony growth below the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 28298, b2898__ygfZ donor and b1868__yecE\n\
    \        recipient, score -13.2114. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-yghd-decreases-relative-growth\n    subject: yece-yghd-joint-loss\n\
    \    predicate: decreases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/yghD deletion has an aggravating S-score of -9.47303, indicating\
    \ normalized\n      colony growth below the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 29267, b2968__yghD donor and b1868__yecE\n\
    \        recipient, score -9.47303. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-exbb-decreases-relative-growth\n    subject: yece-exbb-joint-loss\n\
    \    predicate: decreases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/exbB deletion has an aggravating S-score of -8.29434, indicating\
    \ normalized\n      colony growth below the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 30395, b3006__exbB donor and b1868__yecE\n\
    \        recipient, score -8.29434. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-ttdb-decreases-relative-growth\n    subject: yece-ttdb-joint-loss\n\
    \    predicate: decreases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/ttdB deletion has an aggravating S-score of -3.844, indicating\
    \ normalized\n      colony growth below the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 31057, b3062__ttdB donor and b1868__yecE\n\
    \        recipient, score -3.844. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-gltb-decreases-relative-growth\n    subject: yece-gltb-joint-loss\n\
    \    predicate: decreases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/gltB deletion has an aggravating S-score of -3.71264, indicating\
    \ normalized\n      colony growth below the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 32697, b3212__gltB donor and b1868__yecE\n\
    \        recipient, score -3.71264. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-gltd-increases-relative-growth\n    subject: yece-gltd-joint-loss\n\
    \    predicate: increases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/gltD deletion has an alleviating S-score of 4.00211, indicating\
    \ normalized\n      colony growth above the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 32995, b3213__gltD donor and b1868__yecE\n\
    \        recipient, score 4.00211. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-alr-decreases-relative-growth\n    subject: yece-alr-joint-loss\n\
    \    predicate: decreases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/alr deletion has an aggravating S-score of -12.8803, indicating\
    \ normalized\n      colony growth below the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 39573, b4053__alr donor and b1868__yecE\n\
    \        recipient, score -12.8803. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    \  - edge_id: yece-idnd-decreases-relative-growth\n    subject: yece-idnd-joint-loss\n\
    \    predicate: decreases\n    object: relative-colony-growth\n    mechanism:\
    \ The joint yecE/idnD deletion has an aggravating S-score of -8.24387, indicating\
    \ normalized\n      colony growth below the multiplicative single-mutant expectation.\
    \ This is an indirect joint-genotype\n      phenotype, not the isolated effect\
    \ of either deletion or direct protein interaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24586182\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930520/\n\
    \      snippet: high-confidence epistatic interactions\n      explanation: Table\
    \ S2 sheet WG_GI_Score_Mar_06_2013, row 42250, b4267__idnD donor and b1868__yecE\n\
    \        recipient, score -8.24387. Parsed Tables S1/S16 establish donor origin;\
    \ visually inspected Protocols\n        S2/S16 and main Methods establish design\
    \ and baseline. No absolute growth fraction is inferred\n        from the S-score.\n\
    \      cache_path: evidence/PF01904/babu-2014.txt\n      cache_sha256: 2cfad6f2522638ae511ee44e50f5dd39aa657c64e71f2bb1524163e8d48ed2e4\n\
    - graph_id: tm1631-modeled-dna-cleavage-2016\n  title: Proposed Tm1631 DNA cleavage\
    \ in a preorganized computational system\n  scope: Ogrizek2016 Figures 1-3 and\
    \ modeled coordinate subsets, extending the Konc2013 Tm1631-DNA pose;\n    no\
    \ experimental nuclease assay.\n  context: Joint modeled Tm1631, DNA, two Mg ions\
    \ and an assumed nucleophile; a 42-atom QM region treated\n    with B3LYP/6-31G*\
    \ within CHARMM36. Sixteen interpolated replicas connect constructed reactant/product\n\
    \    endpoints.\n  family_mapping: Thermotoga maritima MSB8 Tm1631 Q9X1W6, sequence\
    \ version 1, equals AAD36698.1 and WP_004082107.1;\n    261 aa, PF01904 at 3-259.\
    \ PDB 1VPQ entity residues 13-273 match this sequence after a 12-residue tag.\n\
    \    Supplement Figure S2 maps modeled Lys73 to native K72; reference residue\
    \ 73 is T.\n  scope_status: HYPOTHETICAL\n  taxon: NCBITaxon:243274\n  limitations:\
    \ PDB 1VPQ contains sulfate and water, not observed bound DNA or Mg. The starting\
    \ pose and\n    chemistry are constructed; 2013 restraints, initial neutral lysine,\
    \ hydroxide generation and ion identity/count\n    remain assumptions. Relative\
    \ potential-energy profiles are not measured rates or fully sampled activation\n\
    \    free energies. Figures 4/5 change ion or wider-environment conditions, not\
    \ an isolated protein-only\n    deletion. Five coordinate subsets were parsed,\
    \ not rerun as QM calculations. No demonstrated DNA binding,\n    residue-mutant\
    \ effect, biological repair or family-wide nuclease activity.\n  nodes:\n  - node_id:\
    \ modeled-reactant-system\n    label: Preorganized Tm1631-DNA system with two\
    \ Mg ions and assumed nucleophile\n    node_type: STATE\n  - node_id: proposed-pentacovalent-state\n\
    \    label: Proposed pentacovalent DNA phosphate state in the joint modeled system\n\
    \    node_type: STATE\n  - node_id: proposed-nicked-dna\n    label: Proposed nicked\
    \ DNA after modeled P-O3' cleavage\n    node_type: STATE\n  edges:\n  - edge_id:\
    \ proposed-nucleophilic-attack\n    subject: modeled-reactant-system\n    predicate:\
    \ converts_to\n    object: proposed-pentacovalent-state\n    mechanism: The proposed\
    \ path places a nucleophile near the DNA phosphate and produces a pentacovalent\n\
    \      state; replica 5 is a modeled potential-energy minimum, not an experimentally\
    \ trapped intermediate.\n      An early lysine-deprotonation event was not established\
    \ and is not added as a separate edge.\n    directness: UNRESOLVED\n    support:\
    \ HYPOTHESIZED\n    evidence_kind: COMPUTATIONAL\n    evidence:\n    - reference:\
    \ PMID:27398092\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4939058/\n\
    \      snippet: pentacovalent intermediate\n      explanation: Visually inspected\
    \ original Figures 1-3, main Methods and parsed supplemental captions/coordinate\n\
    \        subsets support the authors' computational proposal only. Figure S2 explicitly\
    \ resolves model\n        Lys73 as native K72; no K73 mutant or measured proton-transfer\
    \ event.\n      cache_path: evidence/PF01904/ogrizek-2016.txt\n      cache_sha256:\
    \ 14035fbe893099339ba98311c2b78203dfc6e94b87e81cac2f573700206708d0\n  - edge_id:\
    \ proposed-phosphodiester-cleavage\n    subject: proposed-pentacovalent-state\n\
    \    predicate: converts_to\n    object: proposed-nicked-dna\n    mechanism: Under\
    \ the same joint modeled conditions, the proposed phosphate intermediate proceeds\
    \ to\n      P-O3' bond cleavage. Constructed product endpoints and relative potential\
    \ energies do not establish\n      real turnover, product release, cleavage specificity\
    \ or an independent experimental observation.\n    directness: UNRESOLVED\n  \
    \  support: HYPOTHESIZED\n    evidence_kind: COMPUTATIONAL\n    evidence:\n  \
    \  - reference: PMID:27398092\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4939058/\n\
    \      snippet: pentacovalent intermediate\n      explanation: Original Figures\
    \ 1-3 and Methods describe the proposed path to the constructed cleaved-DNA\n\
    \        endpoint. Figures 4/5 retain distinct ion and environment comparisons;\
    \ their profiles are not\n        adopted as kinetic rate enhancements.\n    \
    \  cache_path: evidence/PF01904/ogrizek-2016.txt\n      cache_sha256: 14035fbe893099339ba98311c2b78203dfc6e94b87e81cac2f573700206708d0\n\
    curation_events:\n- timestamp: '2026-10-11T23:06:35Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate YecE joint-genotype phenotypes\
    \ and a separate Tm1631 computational mechanism\n  history_record: history/records/PF01904/2026-10-11T230635Z-codex-014186.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Frozen PF01904 is DUF72/IPR002763 with 14646 proteins. YecE P37348 sequence
    version 4 equals NP_416382.1, AAC74938.1 and BAA15679.2, 272 aa, PF01904 3-258.
    Tm1631 Q9X1W6 sequence version 1 equals AAD36698.1 and WP_004082107.1, 261 aa,
    PF01904 3-259. PDB 1VPQ entity 13-273 exactly matches Q9X1W6 after its 12-residue
    tag. The supplementary Figure S2 caption explicitly resolves model Lys73 as native
    K72; native residue 73 is T. Reference equality does not independently sequence
    historical assay clones or every atom of a modeled construct. Taxa and experimental
    systems remain separate, without adopting a secondary database strain label as
    the assay.
  target_ids:
  - PF01904
  evidence_ids:
  - identity
  - primary
  - tm1631-computational-chemistry
  - tm1631-pose-generation
  - source-search-and-limits
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: The joint-genotype source nodes do not imply gene-to-gene causation or
    isolated single-deletion effects. Positive scores do not establish WT rescue,
    absolute growth gain or binding. Tm1631 chemistry remains a separate hypothetical
    sequence under joint modeled DNA/two-Mg/nucleophile conditions. Constructed endpoints,
    a modeled pentacovalent minimum and relative potential energies do not establish
    measured activity, trapped intermediates, rates or activation free energies. No
    early lysine deprotonation edge or experimental K73 mutant is invented. The 2016
    model extends 2013 rather than independently replicating an experiment; PDB sulfate/water
    does not become observed DNA/Mg binding. Every edge's cache hash and quotation
    were checked separately from scientific interpretation.
  target_ids:
  - PF01904
  evidence_ids:
  - primary
  - native
  - tm1631-computational-chemistry
  - tm1631-pose-generation
  - source-search-and-limits
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Most 14646 frozen members, independent allele/rescue validation, exact
    historical clones, raw colony images and row-specific dispersion remain unassessed.
    Supplementary DOC figures were not visually inspected because conversion retained
    text but dropped images. Only five of 48 model coordinate subsets were parsed,
    and no QM calculation or trajectory was rerun. YunF expression, cofitness, beta-clamp
    motifs, prophage insertion at the yecE locus and similarly named unrelated enzymes
    remain excluded leads, not negative results or experimentally established DUF72
    mechanisms.
  target_ids:
  - PF01904
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01904-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Validate member-specific mechanisms and extend assay coverage
  description: Seek independent YecE alleles, complementation, raw normalized fitness
    and precise clone identities while retaining the multiplicative comparator and
    marker/polar alternatives. Test Tm1631 binding, product identity, substrate specificity,
    metal dependence and residue effects with suitable folding controls. Inspect remaining
    supplementary figures and member-specific primary contexts; preserve resolved
    model/native numbering and keep unsupported chemistry hypothetical. Any supported
    additions need actual history, guarded regeneration and a successor scoped review.
  target_ids:
  - PF01904
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - tm1631-computational-chemistry
  - tm1631-pose-generation
  - source-search-and-limits
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01904.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Seek independent YecE alleles, complementation, raw normalized fitness
    and precise clone identities while retaining the multiplicative comparator and
    marker/polar alternatives. Test Tm1631 binding, product identity, substrate specificity,
    metal dependence and residue effects with suitable folding controls. Inspect remaining
    supplementary figures and member-specific primary contexts; preserve resolved
    model/native numbering and keep unsupported chemistry hypothetical. Any supported
    additions need actual history, guarded regeneration and a successor scoped review.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01904
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Visually inspected Konc2013 Figure 5, Ogrizek2016 Figures 1-5 and Babu2014 Protocols
  S2/S16. Parsed three XLS tables after conversion and 2013/2016 DOC text/tables without
  their images. Five model coordinate subsets were parsed, not rerun. No raw colony-image,
  exact clone-sequence, whole-family or full publication-QC certification.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
