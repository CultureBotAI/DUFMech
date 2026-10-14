# Scoped scientific assessment of RtcB biochemical causal graphs

- Review: 20261011T064426Z-pf01139-rtcb-causal-graphs
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T06:42:47Z
- Finished UTC: 2026-10-11T06:44:26Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain three distinct assay graphs with three observed edges and one inferred chemical-assignment edge. Protein guanylylation, 5'-blocked RNA processing and 5'-OH RNA ligation are not collapsed into direct tracking of one molecule. Source-caption discrepancies and clone-provenance limits remain open.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01139 RtcB; purified full-length E. coli protein in the 2012 PNAS and NAR assays, mapped to reference P46850 and its exact experimental peptide.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01139 | data/families/PF01139.yaml | generated | PF01139 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01139 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01139.

The named 408-aa E. coli RtcB and its MS peptide 325-341 resolve to P46850 reference sequence version 3, rtcB/yhgL b3421, PF01139 29-408. The peptide matches exactly and includes H337. The 2012 sources cite the inspected 2011 protocol, which removes the His10-Smt3 tag using Ulp1 before assays. K12 is the reference, not a proven experimental cloning-template strain; full clone sequence and original cloning supplement remain unverified. Species-level taxonomy preserves that distinction.

### Directed effects and limits

graph: supported. Targets: PF01139.

Three OBSERVED DIRECT biochemical effects support adduct formation, blocked cyclic-end hydrolysis and net ligation. The blocked-RNA 3'-guanylylation edge is DIRECT but INFERRED, explicitly exposing its chemical-assignment basis. Compatible reaction steps are distinguished from separate substrates; the 5'-blocked intermediate is not drawn as the substrate of the 5'-OH ligation graph. Joint GTP/manganese/enzyme conditions, initial substrate impurities, enzyme excess and unequal panel time units remain explicit. No cellular repair, family-wide cofactor independence or atomic transition state is claimed.

### Remaining family coverage

completeness: concern. Targets: PF01139.

Partial assessment of one bacterial member and selected synthetic-substrate contexts. Exact clone provenance, independent RNA-intermediate chemistry, source-caption discrepancies and later member-specific studies remain unresolved. Human and archaeal partners, physiological substrates and cellular outcomes require their own experiments.

## Findings

### additional-contexts: Resolve RtcB source discrepancies and extend member-specific mechanism coverage

minor / open / confirmed; issue key: pf01139-causal-context-coverage.

Resolve the full cloning-template sequence and source strain, the PNAS mass-caption transposition and NAR no-GTP substrate label. Assess independent RNA-intermediate chemistry and additional member/context experiments before extending edges or promoting inferred support. Keep blocked and ligatable substrates separate, preserve residual activity and retain a successor review with actual history.

## Recommended Actions And Acceptance Checks

### extend-contexts

Resolve the full cloning-template sequence and source strain, the PNAS mass-caption transposition and NAR no-GTP substrate label. Assess independent RNA-intermediate chemistry and additional member/context experiments before extending edges or promoting inferred support. Keep blocked and ligatable substrates separate, preserve residual activity and retain a successor review with actual history.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC3458531/; Methods, Results including Figures 5-6 interpretation, visually inspected Figures 2 and 7 and captions | supports | The plus-GTP time course supports cyclic-end hydrolysis followed by appearance of the assigned 3'-ppG species in 5'-blocked RNA. The chemical assignment is explicitly inferred from mobility, GTP dependence and prior intermediate chemistry. A separate 5'-OH substrate yields a diagnostic ligation-junction fragment, with GTP-omission and H337A controls. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/P46850/entry/pfam/PF01139/; Accession and domain locations; paired UniProt identity facts | supports | The named 408-aa E. coli RtcB and its MS peptide 325-341 resolve to P46850 reference sequence version 3, rtcB/yhgL b3421, PF01139 29-408. The peptide matches exactly and includes H337. The 2012 sources cite the inspected 2011 protocol, which removes the His10-Smt3 tag using Ulp1 before assays. K12 is the reference, not a proven experimental cloning-template strain; full clone sequence and original cloning supplement remain unverified. Species-level taxonomy preserves that distinction. |
| protein-adduct | https://pmc.ncbi.nlm.nih.gov/articles/PMC3341019/; Protein-guanylylation methods, peptide and MS/MS Results, visually inspected Figures 2 and 4 | supports | WT RtcB forms an SDS-resistant labeled guanylate adduct; H337A/N/Q variants do not. The experimental peptide supports the reference mapping. Figure 2 and Results show about 723.93 m/z while the HTML caption swaps digits to 732.92-732.94; no independent raw-data correction is claimed. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01139 | data/families/PF01139.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- PNAS Figures 2 and 4 and NAR Figures 2 and 7 were visually inspected. NAR Figures 5-6 and PNAS MS/MS interpretation were read as text; raw spectra, gels and fits were not independently reprocessed. The 2011 purification methods were inspected, but the original cloning supplement was not. The observed image-caption discrepancies are retained rather than normalized.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T064426Z-pf01139-rtcb-causal-graphs
title: Scoped scientific assessment of RtcB biochemical causal graphs
started_at: '2026-10-11T06:42:47Z'
finished_at: '2026-10-11T06:44:26Z'
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
summary: Retain three distinct assay graphs with three observed edges and one inferred
  chemical-assignment edge. Protein guanylylation, 5'-blocked RNA processing and 5'-OH
  RNA ligation are not collapsed into direct tracking of one molecule. Source-caption
  discrepancies and clone-provenance limits remain open.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01139.yaml
    sha256: cd788cf60ba5063c658c607e677ced546c34dbaae6e08d9bfee9763d36f9f267
    role: context
  - path: data/families/PF01139.yaml
    sha256: 0fb38ecb5992f4db4a1d36b3c4ea57e77f8db7bc9fe73a043cf34d99696b9d14
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
  - path: evidence/PF01139/chakravarty-2012-nar.txt
    role: context
    sha256: 57c04fef2ec0acf5478c85eb3a4b28e5baaa452fb95e450e017e158860218aaf
  - path: evidence/PF01139/rtcb-protocol-identity.txt
    role: context
    sha256: ff25e6e0f5706ccfda6e49800e91e8b0c74ece23570d4a81ed56283a1d9f1a80
  - path: evidence/PF01139/chakravarty-2012-pnas.txt
    role: context
    sha256: bcc7b59e60f0246dc71124c3d373bd719ae7bfb9f60c6e89f6555b3e9f24ae70
targets:
- target_id: PF01139
  path: data/families/PF01139.yaml
  label: PF01139
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01139.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 3a22646ea513e9cc89306b595cd6828b0cb0d7a07d201557e40d3f1c84df612b
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01139 RtcB; purified full-length E. coli protein in the 2012 PNAS and
    NAR assays, mapped to reference P46850 and its exact experimental peptide.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01139
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Partial assessment of one bacterial member and selected synthetic-substrate
      contexts. Exact clone provenance, independent RNA-intermediate chemistry, source-caption
      discrepancies and later member-specific studies remain unresolved. Human and
      archaeal partners, physiological substrates and cellular outcomes require their
      own experiments.
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
  - PF01139
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3458531/
  locator: Methods, Results including Figures 5-6 interpretation, visually inspected
    Figures 2 and 7 and captions
  accessed_at: '2026-10-11T06:44:26Z'
  support: supports
  snapshot_sha256: 57c04fef2ec0acf5478c85eb3a4b28e5baaa452fb95e450e017e158860218aaf
  summary: The plus-GTP time course supports cyclic-end hydrolysis followed by appearance
    of the assigned 3'-ppG species in 5'-blocked RNA. The chemical assignment is explicitly
    inferred from mobility, GTP dependence and prior intermediate chemistry. A separate
    5'-OH substrate yields a diagnostic ligation-junction fragment, with GTP-omission
    and H337A controls.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P46850/entry/pfam/PF01139/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T06:44:26Z'
  support: supports
  snapshot_sha256: ff25e6e0f5706ccfda6e49800e91e8b0c74ece23570d4a81ed56283a1d9f1a80
  summary: The named 408-aa E. coli RtcB and its MS peptide 325-341 resolve to P46850
    reference sequence version 3, rtcB/yhgL b3421, PF01139 29-408. The peptide matches
    exactly and includes H337. The 2012 sources cite the inspected 2011 protocol,
    which removes the His10-Smt3 tag using Ulp1 before assays. K12 is the reference,
    not a proven experimental cloning-template strain; full clone sequence and original
    cloning supplement remain unverified. Species-level taxonomy preserves that distinction.
- evidence_id: protein-adduct
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3341019/
  locator: Protein-guanylylation methods, peptide and MS/MS Results, visually inspected
    Figures 2 and 4
  summary: WT RtcB forms an SDS-resistant labeled guanylate adduct; H337A/N/Q variants
    do not. The experimental peptide supports the reference mapping. Figure 2 and
    Results show about 723.93 m/z while the HTML caption swaps digits to 732.92-732.94;
    no independent raw-data correction is claimed.
  accessed_at: '2026-10-11T06:44:26Z'
  support: supports
  snapshot_sha256: bcc7b59e60f0246dc71124c3d373bd719ae7bfb9f60c6e89f6555b3e9f24ae70
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T06:44:26Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01139
  kind: record_content
  reference: data/families/PF01139.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T06:44:26Z'
  support: context_only
  snapshot_sha256: 0fb38ecb5992f4db4a1d36b3c4ea57e77f8db7bc9fe73a043cf34d99696b9d14
  quote: "id: Pfam:PF01139\npfam_id: PF01139\nname: tRNA-splicing ligase RtcB\nshort_name:\
    \ RtcB\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01139\n\
    counters:\n  proteins: 12598\n  matches: 15105\n  proteomes: 9357\n  taxa: 17245\n\
    \  structures: 20\n  alphafold_models: 8370\n  domain_architectures: 66\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR001233\ndescription: This family of RNA ligases ([ec:6.5.1.3])\
    \ join 2',3'-cyclic phosphate and 5'-OH ends. They\n  catalyse the splicing of\
    \ tRNA and may also participate in tRNA repair and recovery from stress-induced\n\
    \  RNA damage [[cite:PUB00152168],[cite:PUB00057853],[cite:PUB00056744]].\ncuration_history:\
    \ history/records/PF01139\ndiscussions:\n- discussion_id: rtcb-construct-intermediates-and-contexts\n\
    \  prompt: Resolve clone provenance and source-caption discrepancies, and extend\
    \ member-specific ligation\n    evidence without mixing blocked and ligatable\
    \ substrates.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: The protein-adduct\
    \ assay, blocked-end processing time course and net ligation experiment\n    are\
    \ distinct contexts. Their combination supports a mechanistic model but is not\
    \ direct tracking of\n    one molecule through every step. One chemical-assignment\
    \ edge remains INFERRED.\n  evidence:\n  - reference: PMID:22474365\n    supports:\
    \ PARTIAL\n    evidence_source: full_text\n    explanation: Figures 2 and 4 were\
    \ visually inspected. The image/Results mass value differs from the\n      caption,\
    \ and loss-of-function mutants do not alone resolve atomic transition states.\n\
    \  - reference: PMID:22730297\n    supports: PARTIAL\n    evidence_source: full_text\n\
    \    explanation: Figures 2 and 7 were visually inspected; Figures 5-6 were assessed\
    \ from Results/captions.\n      The no-GTP control label, residual substrate species\
    \ and time-axis differences remain explicit.\n      The proposed direct cyclic-end\
    \ ligation alternative is not adopted.\n  - reference: PMID:22045815\n    supports:\
    \ PARTIAL\n    evidence_source: full_text\n    explanation: The cited purification\
    \ protocol removes the His10-Smt3 tag before assays; the earlier\n      protocol\
    \ was checked in PMID:21224389. Neither inspection independently establishes the\
    \ exact cloning-template\n      strain.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n\
    \  notes: Remaining work includes exact cloning-sequence provenance, independent\
    \ chemical validation of\n    the RNA intermediate, later E. coli mechanistic\
    \ studies and other members. Human/archaeal partners\n    and cellular repair\
    \ outcomes are not transferred from this bacterial system. Status remains IN_PROGRESS.\n\
    causal_graphs:\n- graph_id: ecoli-rtcb-guanylylation\n  title: Purified E. coli\
    \ RtcB forms a covalent guanylate adduct\n  scope: Full-length recombinant E.\
    \ coli RtcB, purified after His10-Smt3 tag removal; a protein-adduct\n    assay,\
    \ not an isolated domain or a cellular RNA-repair phenotype.\n  context: The 2012\
    \ PNAS Figure 4B assay uses 10 uL, 50 mM Tris pH 8.0, 2 mM MnCl2, 10 uM alpha-32P-GTP\n\
    \    and 5 uM RtcB at 37 C for 1 min. SDS-PAGE and autoradiography measure protein\
    \ labeling. H337A/N/Q\n    variants and the protein-loading gel are controls.\
    \ GTP, manganese and enzyme are joint inputs.\n  family_mapping: The paper's 408-aa\
    \ E. coli RtcB maps to reference P46850, sequence version 3, rtcB/yhgL,\n    b3421,\
    \ PF01139 at 29-408. The reported MS peptide 325-341 exactly matches the reference\
    \ and contains\n    H337. The reference is K12; the exact cloning-template strain\
    \ and full final clone sequence remain\n    unverified, so graph taxonomy is E.\
    \ coli species rather than an asserted experimental K12 strain.\n  scope_status:\
    \ MECHANISTIC\n  taxon: NCBITaxon:562\n  limitations: Peptide mass and mutation\
    \ evidence support the H337 assignment, but the graph does not\n    assert a directly\
    \ observed transition state. Figure 2's image and Results give m/z about 723.93\
    \ while\n    its HTML caption transposes this to 732.92-732.94; no raw spectrum\
    \ was reprocessed. The source's DNA-guanylylation\n    assay is not relabeled\
    \ as RNA chemistry or joined to this graph as a directly tracked molecule.\n \
    \ nodes:\n  - node_id: rtcb-with-gtp-manganese\n    label: Tag-free E. coli RtcB\
    \ exposed to GTP and Mn2+\n    node_type: STATE\n    grounding:\n    - UniProtKB:P46850\n\
    \  - node_id: rtcb-gmp-adduct\n    label: Covalent RtcB-GMP adduct\n    node_type:\
    \ STATE\n    grounding:\n    - UniProtKB:P46850\n  edges:\n  - edge_id: rtcb-forms-guanylate-adduct\n\
    \    subject: rtcb-with-gtp-manganese\n    predicate: converts_to\n    object:\
    \ rtcb-gmp-adduct\n    mechanism: GTP-derived label becomes an SDS-resistant RtcB\
    \ adduct in the manganese-containing reaction.\n      Peptide analysis and H337\
    \ substitutions support a histidinyl-GMP assignment, without resolving every\n\
    \      bond-making microstep.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:22474365\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3341019/\n      snippet:\
    \ form an SDS-resistant 45-kDa\n      explanation: Visually inspected Figure 4A-B\
    \ establishes protein loading and WT-specific labeling;\n        Figure 2 and\
    \ MS/MS Results support the adduct interpretation with the caption discrepancy\
    \ retained.\n      cache_path: evidence/PF01139/chakravarty-2012-pnas.txt\n  \
    \    cache_sha256: bcc7b59e60f0246dc71124c3d373bd719ae7bfb9f60c6e89f6555b3e9f24ae70\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P46850/entry/pfam/PF01139/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P46850/entry/pfam/PF01139/\n\
    \      snippet: 'Pfam interval: PF01139 at 29-408, inclusive.'\n      explanation:\
    \ Reference sequence, exact experimental peptide match and cited tag-removal protocol\n\
    \        support member/domain mapping, not an independently verified cloning-template\
    \ strain.\n      cache_path: evidence/PF01139/rtcb-protocol-identity.txt\n   \
    \   cache_sha256: ff25e6e0f5706ccfda6e49800e91e8b0c74ece23570d4a81ed56283a1d9f1a80\n\
    - graph_id: ecoli-rtcb-blocked-rna-processing\n  title: RtcB processing of a 5'-blocked\
    \ cyclic-phosphate RNA substrate\n  scope: Tag-free E. coli RtcB acting on a synthetic\
    \ 20-mer with a 5'-phosphate and a 2',3'-cyclic phosphate;\n    not the ligatable\
    \ 5'-OH substrate or native tRNA.\n  context: The 2012 NAR Figure 7 plus-GTP time\
    \ course uses 50 mM Tris pH 8.0, 2 mM MnCl2, 100 uM GTP,\n    1 uM RtcB and 0.1\
    \ uM labeled RNA at 37 C. RNase T1 digestion and urea-PAGE resolve terminal products\n\
    \    over 0-120 s. RtcB, GTP and manganese are present together for both edges.\n\
    \  family_mapping: E. coli RtcB corresponds to the 408-aa P46850 reference, sequence\
    \ version 3, with PF01139\n    at 29-408. Cited purification uses Ulp1-cleaved\
    \ His10-Smt3 protein followed by nickel chromatography\n    and gel filtration.\
    \ Exact source strain and final clone sequence remain unverified; this is full-length\n\
    \    protein, not the isolated Pfam interval.\n  scope_status: MECHANISTIC\n \
    \ taxon: NCBITaxon:562\n  limitations: Starting RNA contains about 10% 3'-phosphate,\
    \ and residual 5'-OH substrate accounts for\n    a small ligation signal. The\
    \ no-GTP control is labeled pRNAp in the caption but pRNA>p in the main\n    text;\
    \ neither identity is silently imposed, and the adopted edges use the plus-GTP\
    \ time course. The\n    specific 3'-ppG chemical assignment is inferred from mobility,\
    \ GTP dependence and prior intermediate\n    chemistry, not independently reidentified\
    \ here. Enzyme-excess kinetics are not steady-state turnover.\n  nodes:\n  - node_id:\
    \ blocked-rna-cyclic-phosphate\n    label: 5'-P RNA with a 2',3'-cyclic phosphate\
    \ end\n    node_type: STATE\n  - node_id: blocked-rna-three-phosphate\n    label:\
    \ 5'-P RNA with a 3'-phosphate end\n    node_type: STATE\n  - node_id: blocked-rna-guanylate\n\
    \    label: 5'-P RNA product assigned as RNA(3')pp(5')G\n    node_type: STATE\n\
    \  edges:\n  - edge_id: rtcb-hydrolyzes-cyclic-rna-end\n    subject: blocked-rna-cyclic-phosphate\n\
    \    predicate: converts_to\n    object: blocked-rna-three-phosphate\n    mechanism:\
    \ In the joint RtcB/GTP/Mn2+ reaction, loss of the cyclic-phosphate T1 fragment\
    \ accompanies\n      rapid accumulation of the 3'-phosphate fragment above its\
    \ starting background.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:22730297\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC3458531/\n      snippet: being converted\
    \ predominantly to the more rapidly migrating\n      explanation: Visually inspected\
    \ Figure 7A-B supports hydrolysis in the plus-GTP time course, retaining\n   \
    \     initial 3'-phosphate contamination and the separate control-label discrepancy.\
    \ No absolute absence\n        of slow GTP-free hydrolysis is claimed.\n     \
    \ cache_path: evidence/PF01139/chakravarty-2012-nar.txt\n      cache_sha256: 57c04fef2ec0acf5478c85eb3a4b28e5baaa452fb95e450e017e158860218aaf\n\
    \  - edge_id: rtcb-guanylates-blocked-rna-end\n    subject: blocked-rna-three-phosphate\n\
    \    predicate: converts_to\n    object: blocked-rna-guanylate\n    mechanism:\
    \ The delayed RNA product is assigned as the 3'-guanylylated derivative in the\
    \ RtcB/GTP/Mn2+\n      reaction. Figures 5-6 interpretation and Figure 7 temporal\
    \ ordering support this chemical step;\n      its assignment remains explicitly\
    \ inferred rather than an independently reidentified RNA structure.\n    directness:\
    \ DIRECT\n    support: INFERRED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:22730297\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3458531/\n\
    \      snippet: lagged behind the generation\n      explanation: Main Results\
    \ for Figures 5-6 and visually inspected Figure 7 support the product assignment\n\
    \        and order. The observed band is not hidden uncertainty; structural identity\
    \ and a directly tracked\n        enzyme-to-RNA GMP handoff are not independently\
    \ demonstrated by this time course alone.\n      cache_path: evidence/PF01139/chakravarty-2012-nar.txt\n\
    \      cache_sha256: 57c04fef2ec0acf5478c85eb3a4b28e5baaa452fb95e450e017e158860218aaf\n\
    - graph_id: ecoli-rtcb-cyclic-end-rna-ligation\n  title: RtcB seals a synthetic\
    \ 5'-OH cyclic-phosphate RNA\n  scope: Full-length tag-free E. coli RtcB and a\
    \ ligatable synthetic 20-mer with 5'-OH and 2',3'-cyclic\n    phosphate ends;\
    \ net intramolecular RNA end joining.\n  context: The 2012 NAR Figure 2 WT plus-GTP\
    \ assay uses 50 mM Tris pH 8.0, 2 mM MnCl2, 100 uM GTP, 1 uM\n    RtcB and 0.1\
    \ uM labeled RNA at 37 C. RNase T1 digestion reveals a six-nucleotide ligation-junction\n\
    \    fragment. Minus-GTP and H337A panels use longer minute-scale time courses,\
    \ unlike the WT plus-GTP\n    seconds-scale panel.\n  family_mapping: The 408-aa\
    \ E. coli RtcB is mapped to P46850 sequence version 3 and PF01139 at 29-408;\n\
    \    experimental peptide identity and cited tag-removal protocol are retained\
    \ separately. K12 is the mapped\n    reference, not a verified experimental cloning-template\
    \ strain.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:562\n  limitations:\
    \ The substrate preparation includes about 7-8% 3'-phosphate ends, but this does\
    \ not account\n    for the much larger ligated fraction. The endpoint and time\
    \ course concern synthetic RNA under enzyme\n    excess, not turnover rates or\
    \ physiological tRNA substrates. This graph is not connected directly\n    to\
    \ the 5'-blocked substrate graph. No family-wide, archaeal or mammalian cofactor\
    \ independence is\n    inferred.\n  nodes:\n  - node_id: rtcb-ligatable-rna-reaction\n\
    \    label: RtcB with 5'-OH cyclic-phosphate RNA, GTP and Mn2+\n    node_type:\
    \ ACTIVITY\n    grounding:\n    - UniProtKB:P46850\n  - node_id: sealed-rna-junction\n\
    \    label: Sealed RNA phosphodiester junction\n    node_type: STATE\n  edges:\n\
    \  - edge_id: rtcb-produces-sealed-rna\n    subject: rtcb-ligatable-rna-reaction\n\
    \    predicate: produces\n    object: sealed-rna-junction\n    mechanism: The\
    \ complete biochemical reaction yields the diagnostic RNase T1 fragment spanning\
    \ the\n      newly joined ends. GTP omission and H337A controls suppress efficient\
    \ ligation; the graph represents\n      the measured net reaction, not a direct\
    \ one-step attack on the cyclic end.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:22730297\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3458531/\n      snippet:\
    \ 87% of the input substrate being ligated\n      explanation: Visually inspected\
    \ Figure 2 and its Results identify the junction fragment and controls.\n    \
    \    Source time units and incomplete substrate cyclization are retained; slow\
    \ residual hydrolysis\n        is not mistaken for ligation.\n      cache_path:\
    \ evidence/PF01139/chakravarty-2012-nar.txt\n      cache_sha256: 57c04fef2ec0acf5478c85eb3a4b28e5baaa452fb95e450e017e158860218aaf\n\
    curation_events:\n- timestamp: '2026-10-11T06:40:02Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate distinct RtcB protein-adduct,\
    \ RNA-processing and ligation graphs\n  history_record: history/records/PF01139/2026-10-11T064002Z-codex-59d71c.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: The named 408-aa E. coli RtcB and its MS peptide 325-341 resolve to P46850
    reference sequence version 3, rtcB/yhgL b3421, PF01139 29-408. The peptide matches
    exactly and includes H337. The 2012 sources cite the inspected 2011 protocol,
    which removes the His10-Smt3 tag using Ulp1 before assays. K12 is the reference,
    not a proven experimental cloning-template strain; full clone sequence and original
    cloning supplement remain unverified. Species-level taxonomy preserves that distinction.
  target_ids:
  - PF01139
  evidence_ids:
  - identity
  - primary
  - protein-adduct
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Three OBSERVED DIRECT biochemical effects support adduct formation, blocked
    cyclic-end hydrolysis and net ligation. The blocked-RNA 3'-guanylylation edge
    is DIRECT but INFERRED, explicitly exposing its chemical-assignment basis. Compatible
    reaction steps are distinguished from separate substrates; the 5'-blocked intermediate
    is not drawn as the substrate of the 5'-OH ligation graph. Joint GTP/manganese/enzyme
    conditions, initial substrate impurities, enzyme excess and unequal panel time
    units remain explicit. No cellular repair, family-wide cofactor independence or
    atomic transition state is claimed.
  target_ids:
  - PF01139
  evidence_ids:
  - primary
  - native
  - protein-adduct
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Partial assessment of one bacterial member and selected synthetic-substrate
    contexts. Exact clone provenance, independent RNA-intermediate chemistry, source-caption
    discrepancies and later member-specific studies remain unresolved. Human and archaeal
    partners, physiological substrates and cellular outcomes require their own experiments.
  target_ids:
  - PF01139
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01139-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve RtcB source discrepancies and extend member-specific mechanism coverage
  description: Resolve the full cloning-template sequence and source strain, the PNAS
    mass-caption transposition and NAR no-GTP substrate label. Assess independent
    RNA-intermediate chemistry and additional member/context experiments before extending
    edges or promoting inferred support. Keep blocked and ligatable substrates separate,
    preserve residual activity and retain a successor review with actual history.
  target_ids:
  - PF01139
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - protein-adduct
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01139.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Resolve the full cloning-template sequence and source strain, the PNAS
    mass-caption transposition and NAR no-GTP substrate label. Assess independent
    RNA-intermediate chemistry and additional member/context experiments before extending
    edges or promoting inferred support. Keep blocked and ligatable substrates separate,
    preserve residual activity and retain a successor review with actual history.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01139
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- PNAS Figures 2 and 4 and NAR Figures 2 and 7 were visually inspected. NAR Figures
  5-6 and PNAS MS/MS interpretation were read as text; raw spectra, gels and fits
  were not independently reprocessed. The 2011 purification methods were inspected,
  but the original cloning supplement was not. The observed image-caption discrepancies
  are retained rather than normalized.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
