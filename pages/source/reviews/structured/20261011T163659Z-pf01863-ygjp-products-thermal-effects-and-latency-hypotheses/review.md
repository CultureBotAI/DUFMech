# PF01863 YgjP product assay, archaeal thermal effects and qualified latency models

- Review: 20261011T163659Z-pf01863-ygjp-products-thermal-effects-and-latency-hypotheses
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T16:36:51Z
- Finished UTC: 2026-10-11T16:36:59Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Three observed preparation-level effects and two separately labeled structural hypotheses are retained in four graphs. Reference sequences and domain boundaries are verified, but exact historical YgjP clone identity, missing assay context, proabylysin construct-label discrepancy and unsuccessful protease activation limit interpretation. B80 and remote-homology claims are not transferred. Keep IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Sevin His6-YgjP Supplementary Figure 16 and Tables 3/9; Lopez-Pelegrin recombinant proabylysin thermal deletions and two distinct archaeal structural latency models; B80 and metagenomic claims assessed only as qualified leads.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01863 | data/families/PF01863.yaml | generated | PF01863 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01863 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: concern. Targets: PF01863.

P42597v2 exactly equals BAE77135.1/AAC76120.2 and maps PF01863 94-149, but this verifies the reference rather than the exact historical His6-YgjP clone. Q9V1Y2 equals CAB49216.1, Pfam 2-88; PDB4JIU confirms L2V despite the paper K2V label. Q57587 equals AAB98111.1, Pfam 7-95; PDB4JIX verifies K2A plus residual GP. Archaeal tail sites are outside current domain spans. B80 peptide inconsistencies prevent confident transfer of purified activity to the family.

### Directed effects and limits

graph: supported. Targets: PF01863.

Two MECHANISTIC graphs contain three DIRECT OBSERVED preparation-level effects, while two distinct HYPOTHETICAL graphs contain one UNRESOLVED HYPOTHESIZED edge each. UMP ion output is not calibrated stoichiometry or separate PPi detection. Thermal transitions are not activation, and structural occupancy is not observed inhibition. Taxa, constructs, cis/trans geometry, uncertainty and whole-protein/domain scope remain distinct. No family-wide protease function or isolated-domain sufficiency is asserted.

### Remaining family coverage

completeness: concern. Targets: PF01863.

Missing Sevin full Methods, clone sequence and cellular datasets; missing thermal raw curves and deletion-sequence deposits; unresolved K2V/L2V manuscript discrepancy; no successful archaeal activation; unresolved B80 preparation identity; uncurated additional members and computational candidates. This is not exhaustive family coverage.

## Findings

### additional-contexts: Resolve construct and assay gaps before strengthening functional or activation claims

minor / open / confirmed; issue key: pf01863-causal-context-coverage.

Obtain YgjP exact clone and validation Methods, calibrated UMP/PPi and matched controls; reconcile proabylysin sequence labels and repeat thermal comparisons with matched preparation; establish folded active archaeal products before calling tail latency observed; resolve B80 peptide/reference/mass-table inconsistencies. Inspect remaining member-specific primary contexts without importing predicted activities.

## Recommended Actions And Acceptance Checks

### extend-contexts

Obtain YgjP exact clone and validation Methods, calibrated UMP/PPi and matched controls; reconcile proabylysin sequence labels and repeat thermal comparisons with matched preparation; establish folded active archaeal products before calling tail latency observed; resolve B80 peptide/reference/mass-table inconsistencies. Inspect remaining member-specific primary contexts without importing predicted activities.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC3774397/; Protein Production and Purification, Proteolytic and Inhibitory Activity Assays, activation-results paragraph, structural analysis and original Figure 3A-D | supports | Proabylysin deletion preparations have reported Tm 85/65 C versus full-length 95 C, with differing purification heat treatment. Tail occupancy motivates separate cis and trans latency hypotheses; no active protease was obtained and an inactive-ancestor alternative remains open. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01863/; Accession and domain locations; paired UniProt identity facts | supports | P42597v2 exactly equals BAE77135.1/AAC76120.2 and maps PF01863 94-149, but this verifies the reference rather than the exact historical His6-YgjP clone. Q9V1Y2 equals CAB49216.1, Pfam 2-88; PDB4JIU confirms L2V despite the paper K2V label. Q57587 equals AAB98111.1, Pfam 7-95; PDB4JIX verifies K2A plus residual GP. Archaeal tail sites are outside current domain spans. B80 peptide inconsistencies prevent confident transfer of purified activity to the family. |
| ygjp-product-assay | https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnmeth.4103/MediaObjects/41592_2017_BFnmeth4103_MOESM62_ESM.pdf; PDF page 17 Supplementary Figure 16a-c and publisher Tables 3 row 956 and 9 row 10 | supports | Purified 50 ug/mL His6-YgjP with 10 mM UTP shows UTP decline and UMP rise versus heat-inactivated comparator, three replicates. Distinct ion response scales, missing exact clone and protocol, and unquantified PPi constrain the net product edge. |
| coverage-ledger | evidence/PF01863/ygjp-gap-ledger.txt; Named searches, access limits, B80 reference comparison and Lobb Table 4 candidate interpretation | supports | Preserve exact access and coverage limits. B80 Table 2 inconsistencies prevent activity transfer; metagenomic remote homology and HExxH candidates do not become causal evidence. Failed assays are condition-specific, and inaccessible protocols are not negative results. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01863 | data/families/PF01863.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Original Sevin Supplementary Figure 16 and Lopez-Pelegrin Figure 3 were visually inspected; Tables 3/9 and B80 Table 2 were parsed. No raw spectral reanalysis, diffraction re-refinement, inaccessible main Methods, full cellular datasets or experimental replication is claimed. Rendered-page checks are reported separately after generation.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T163659Z-pf01863-ygjp-products-thermal-effects-and-latency-hypotheses
title: PF01863 YgjP product assay, archaeal thermal effects and qualified latency
  models
started_at: '2026-10-11T16:36:51Z'
finished_at: '2026-10-11T16:36:59Z'
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
summary: Three observed preparation-level effects and two separately labeled structural
  hypotheses are retained in four graphs. Reference sequences and domain boundaries
  are verified, but exact historical YgjP clone identity, missing assay context, proabylysin
  construct-label discrepancy and unsuccessful protease activation limit interpretation.
  B80 and remote-homology claims are not transferred. Keep IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01863.yaml
    sha256: 3fd3f3c7c5fce334b3b6410f6a505c51e06805f8e5d7984900d55174b7dfbfcb
    role: context
  - path: data/families/PF01863.yaml
    sha256: b54e1f2a2398b963d83dae816750804e2bfa0eeeef5aecbfb55cb8c375d0ebef
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
  - path: evidence/PF01863/lopez-pelegrin-2013-minigluzincins.txt
    role: context
    sha256: eea4b1c7eb4e4c639aee446f64ec6e79e281cb0b67c0f90f5ce23ac744dae938
  - path: evidence/PF01863/YgjP-identity.txt
    role: context
    sha256: 630b011a36ad9cbc1d5b1343ee41d0b14ae6096b03580f5b09fe0f19c400935b
  - path: evidence/PF01863/sevin-2017-ygjp.txt
    role: context
    sha256: 09afed3fab4d86f57dc76c1ec458c3d342996b0c3fd1376681de557f2c04bacf
  - path: evidence/PF01863/ygjp-gap-ledger.txt
    role: context
    sha256: bf7ebe6ddb3759b70727b6f64f214c43c530818b9a2df9cff1ed81f40a37d402
targets:
- target_id: PF01863
  path: data/families/PF01863.yaml
  label: PF01863
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01863.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: fc6f8a3b00ae28dcb843f7c12e798df65a2cbcb9d439377a3f9c1330f28f4bfe
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Sevin His6-YgjP Supplementary Figure 16 and Tables 3/9; Lopez-Pelegrin
    recombinant proabylysin thermal deletions and two distinct archaeal structural
    latency models; B80 and metagenomic claims assessed only as qualified leads.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01863
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Missing Sevin full Methods, clone sequence and cellular datasets; missing
      thermal raw curves and deletion-sequence deposits; unresolved K2V/L2V manuscript
      discrepancy; no successful archaeal activation; unresolved B80 preparation identity;
      uncurated additional members and computational candidates. This is not exhaustive
      family coverage.
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
  - PF01863
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3774397/
  locator: Protein Production and Purification, Proteolytic and Inhibitory Activity
    Assays, activation-results paragraph, structural analysis and original Figure
    3A-D
  accessed_at: '2026-10-11T16:36:59Z'
  support: supports
  snapshot_sha256: eea4b1c7eb4e4c639aee446f64ec6e79e281cb0b67c0f90f5ce23ac744dae938
  summary: Proabylysin deletion preparations have reported Tm 85/65 C versus full-length
    95 C, with differing purification heat treatment. Tail occupancy motivates separate
    cis and trans latency hypotheses; no active protease was obtained and an inactive-ancestor
    alternative remains open.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01863/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T16:36:59Z'
  support: supports
  snapshot_sha256: 630b011a36ad9cbc1d5b1343ee41d0b14ae6096b03580f5b09fe0f19c400935b
  summary: P42597v2 exactly equals BAE77135.1/AAC76120.2 and maps PF01863 94-149,
    but this verifies the reference rather than the exact historical His6-YgjP clone.
    Q9V1Y2 equals CAB49216.1, Pfam 2-88; PDB4JIU confirms L2V despite the paper K2V
    label. Q57587 equals AAB98111.1, Pfam 7-95; PDB4JIX verifies K2A plus residual
    GP. Archaeal tail sites are outside current domain spans. B80 peptide inconsistencies
    prevent confident transfer of purified activity to the family.
- evidence_id: ygjp-product-assay
  kind: primary_source
  reference: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnmeth.4103/MediaObjects/41592_2017_BFnmeth4103_MOESM62_ESM.pdf
  locator: PDF page 17 Supplementary Figure 16a-c and publisher Tables 3 row 956 and
    9 row 10
  summary: Purified 50 ug/mL His6-YgjP with 10 mM UTP shows UTP decline and UMP rise
    versus heat-inactivated comparator, three replicates. Distinct ion response scales,
    missing exact clone and protocol, and unquantified PPi constrain the net product
    edge.
  accessed_at: '2026-10-11T16:36:59Z'
  support: supports
  snapshot_sha256: 09afed3fab4d86f57dc76c1ec458c3d342996b0c3fd1376681de557f2c04bacf
- evidence_id: coverage-ledger
  kind: search
  reference: evidence/PF01863/ygjp-gap-ledger.txt
  locator: Named searches, access limits, B80 reference comparison and Lobb Table
    4 candidate interpretation
  search_scope: PF01863/DUF45/YgjP/proabylysin/projannalysin identity and four InterPro-linked
    papers, with UniProt/InterPro/NCBI/PDB reference checks, 2013 fulltext, 2017 supplements,
    B80 primary sections/tables and Lobb targeted-discovery section/Table4 on 2026-10-11.
    Ignored/hidden repository files included. Not exhaustive family literature coverage.
  summary: Preserve exact access and coverage limits. B80 Table 2 inconsistencies
    prevent activity transfer; metagenomic remote homology and HExxH candidates do
    not become causal evidence. Failed assays are condition-specific, and inaccessible
    protocols are not negative results.
  accessed_at: '2026-10-11T16:36:59Z'
  support: supports
  snapshot_sha256: bf7ebe6ddb3759b70727b6f64f214c43c530818b9a2df9cff1ed81f40a37d402
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T16:36:59Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01863
  kind: record_content
  reference: data/families/PF01863.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T16:36:59Z'
  support: context_only
  snapshot_sha256: b54e1f2a2398b963d83dae816750804e2bfa0eeeef5aecbfb55cb8c375d0ebef
  quote: "id: Pfam:PF01863\npfam_id: PF01863\nname: YgjP-like, metallopeptidase domain\n\
    short_name: YgjP-like\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01863\n\
    counters:\n  proteins: 15247\n  matches: 15593\n  proteomes: 12259\n  taxa: 17503\n\
    \  structures: 2\n  alphafold_models: 9610\n  domain_architectures: 18\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002725\ndescription: This is a conserved domain containing\
    \ the catalytic zinc-metallopeptidase (HExxH) catalytic\n  motif. Proteins containing\
    \ this domain are found in some archaebacteria, as well as Helicobacter pylori.\n\
    \  The proteins are 190-240 amino acids long, with the C terminus being the most\
    \ conserved region, containing\n  three conserved histidines [[cite:PUB00098014],[cite:PUB00098016],[cite:PUB00098015],[cite:PUB00084997]].\n\
    \  This domain is found in YgjP from E. coli [[cite:PUB00084997]], a predicted\
    \ metal-dependent hydrolase\n  that hydrolyses UTP to UMP and diphosphate in vitro;\
    \ and in MJ0123 from Methanocaldococcus jannaschii\n  (also referred to as projannalysin)\
    \ [[cite:PUB00098015]].\ncuration_history: history/records/PF01863\ndiscussions:\n\
    - discussion_id: ygjp-construct-and-assay-context\n  prompt: Resolve the historical\
    \ YgjP construct and complete the primary assay context.\n  kind: CURATION_TODO\n\
    \  status: OPEN\n  rationale: Public supplements support net UMP production, but\
    \ reference identity is not exact clone\n    identity and ion counts are not calibrated\
    \ molar product measurements.\n  evidence:\n  - reference: PMID:27941785\n   \
    \ supports: PARTIAL\n    evidence_source: primary_supplementary_figure_16_and_tables_3_9\n\
    \    explanation: Retain heat-inactivated comparator, missing buffer/temperature,\
    \ exact-clone uncertainty,\n      PPi measurement limit and tested-substrate negatives.\n\
    \  notes: See evidence/PF01863/YgjP-identity.txt and ygjp-gap-ledger.txt. Obtain\
    \ Methods, clone sequence,\n    calibrated product assays and cellular evidence\
    \ before adding chemistry or physiological edges.\n  posed_by: Codex\n  posed_date:\
    \ '2026-10-11'\n- discussion_id: minigluzincin-activation-and-identity\n  prompt:\
    \ Distinguish structural latency models from demonstrated protease function.\n\
    \  kind: CURATION_TODO\n  status: OPEN\n  rationale: Archaeal proteins lacked\
    \ detected activity in tested panels and activation attempts failed.\n    Thermal\
    \ deletion effects do not prove de-inhibition; manuscript K2V disagrees with reference/deposit\n\
    \    L2V.\n  evidence:\n  - reference: PMID:23733187\n    supports: PARTIAL\n\
    \    evidence_source: primary_methods_structures_and_activation_results\n    explanation:\
    \ Separate whole-protein thermal effects, two structural hypotheses, failed activation\n\
    \      and inactive-ancestor alternative; C-terminal perturbations lie outside\
    \ current Pfam spans.\n  notes: Resolve deletion sequences and construct-label\
    \ discrepancy; test matched folded activation products\n    and controls. Do not\
    \ import membrane metalloprotease activity by structural similarity.\n  posed_by:\
    \ Codex\n  posed_date: '2026-10-11'\n- discussion_id: b80-and-metagenomic-identity-gaps\n\
    \  prompt: Verify B80 protein identity and keep remote-homology candidates separate\
    \ from assays.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: A Pfam-linked\
    \ publication is not enough to map a purified activity to the family when peptide/reference\n\
    \    and coordinate inconsistencies remain. Remote homology and HExxH alone do\
    \ not establish directed causation.\n  evidence:\n  - reference: PMID:25802851\n\
    \    supports: PARTIAL\n    evidence_source: primary_table_2_and_independent_reference_comparison\n\
    \    explanation: Some peptide matches support a candidate, but other peptides/coordinates\
    \ and mass-table\n      entries require resolution before assigning the B80 preparation\
    \ to PF01863.\n  - reference: PMID:26257768\n    supports: PARTIAL\n    evidence_source:\
    \ primary_table_4_computational_candidates\n    explanation: Metagenomic ORFan\
    \ matches to 4JIU/4JIX are predictions awaiting experimental characterization,\n\
    \      not measured proteolytic effects.\n  notes: Retain IN_PROGRESS and the\
    \ scoped gap ledger; neither these partial graphs nor the EX_DUF label\n    constitutes\
    \ a complete family review.\n  posed_by: Codex\n  posed_date: '2026-10-11'\ncausal_graphs:\n\
    - graph_id: ecoli-ygjp-utp-assay\n  title: Purified E. coli YgjP preparation converts\
    \ UTP to UMP\n  scope: 'Sevin 2017 Supplementary Figure 16 and Tables 3/9: intact\
    \ His6-YgjP preparation, not an isolated\n    domain or in-vivo flux.'\n  context:\
    \ 50 ug/mL purified enzyme with 10 mM UTP; three replicates, mean and SD. Mass-spectrometric\n\
    \    UTP and UMP ion traces compared with heat-inactivated YgjP. Selected TALON\
    \ and anion-exchange fractions\n    are shown in Figure 16b. Assay buffer, temperature\
    \ and heat-inactivation protocol were not verified.\n  family_mapping: Table 3\
    \ identifies b3085/ygjP. Reference P42597 sequence version 2 exactly equals BAE77135.1\n\
    \    and AAC76120.2, 167 aa; PF01863 94-149. The reference is K-12, but exact\
    \ historical ASKA clone sequence,\n    donor strain and expression host remain\
    \ unverified. No residue-specific or isolated-domain attribution.\n  scope_status:\
    \ MECHANISTIC\n  taxon: NCBITaxon:562\n  limitations: DIRECT means a net purified-preparation\
    \ effect, not proof of a chemical microstep or exclusion\n    of every copurifying\
    \ activity. Distinct ion response scales preclude molar stoichiometry or kcat.\n\
    \    PPi appears in the reaction scheme, not a separately quantified trace. Main\
    \ article Methods and full\n    cellular datasets were not inspected.\n  nodes:\n\
    \  - node_id: active-ygjp-with-utp\n    label: Purified His6-YgjP preparation\
    \ incubated with UTP\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:P42597\n\
    \  - node_id: ump-product\n    label: UMP product detected in the assay\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: preparation-produces-ump\n    subject: active-ygjp-with-utp\n\
    \    predicate: produces\n    object: ump-product\n    mechanism: UTP m/z 482.961\
    \ declines while UMP m/z 323.029 rises relative to the heat-inactivated comparator.\n\
    \      Table 9 reports slow UTP-to-UMP conversion and negative tests with ATP,\
    \ GTP, CTP, dTTP and ITP;\n      it does not establish physiological specificity\
    \ or a measured PPi stoichiometry.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:27941785\n\
    \      source_url: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnmeth.4103/MediaObjects/41592_2017_BFnmeth4103_MOESM62_ESM.pdf\n\
    \      snippet: Experimental validation of the novel enzyme YgjP (Upp).\n    \
    \  explanation: Visually inspected Supplementary Figure 16a-c and parsed Table\
    \ 9 row 10 support the\n        net preparation-level product assignment with\
    \ a heat-inactivated comparator; exact assay and construct\n        limitations\
    \ remain explicit.\n      cache_path: evidence/PF01863/sevin-2017-ygjp.txt\n \
    \     cache_sha256: 09afed3fab4d86f57dc76c1ec458c3d342996b0c3fd1376681de557f2c04bacf\n\
    - graph_id: proabylysin-truncation-thermal-transition\n  title: Proabylysin C-terminal\
    \ deletions lower the reported thermal transition\n  scope: 'Lopez-Pelegrin 2013\
    \ activation results: two purified deletion preparations compared with the\n \
    \   full-length recombinant proabylysin scaffold.'\n  context: Synthetic pCRI7\
    \ constructs expressed in E. coli BL21(DE3), without an added tag. Sypro Orange\n\
    \    thermofluor on iCycler iQ; deletion preparations were heat-treated at 50-65\
    \ C during purification,\n    versus 85 C for full length. Exact dye-assay buffer,\
    \ ramp, replicate count and uncertainty were not\n    established.\n  family_mapping:\
    \ PAB3079 Q9V1Y2 version 1 equals CAB49216.1, 105 aa; Pyrococcus abyssi GE5 reference\n\
    \    taxon 272844. PF01863 2-88 excludes the deleted M104/V105 sites. Reference\
    \ and PDB 4JIU establish\n    L2V in the recombinant scaffold, contradicting the\
    \ paper's K2V label. Separate deletion sequences\n    were not deposited in the\
    \ inspected sources.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:272844\n\
    \  limitations: Preparation-level thermal effects, not isolated-domain sufficiency,\
    \ quantified unfolding\n    energetics or protease activation. The published WT\
    \ comparator is the recombinant full-length scaffold.\n    Different purification\
    \ heat treatments and missing raw thermal curves limit mechanistic attribution;\n\
    \    the two deletions do not isolate the contribution of M104 alone.\n  nodes:\n\
    \  - node_id: delete-v105\n    label: Remove terminal V105 from the recombinant\
    \ proabylysin scaffold\n    node_type: PERTURBATION\n  - node_id: delete-m104-v105\n\
    \    label: Remove terminal M104 and V105 from the proabylysin scaffold\n    node_type:\
    \ PERTURBATION\n  - node_id: thermal-transition\n    label: Apparent thermofluor\
    \ melting temperature\n    node_type: STATE\n  edges:\n  - edge_id: delta-v105-lowers-transition\n\
    \    subject: delete-v105\n    predicate: decreases\n    object: thermal-transition\n\
    \    mechanism: The one-residue deletion preparation has reported Tm 85 C versus\
    \ full-length 95 C. No active\n      protease was obtained; the measurement does\
    \ not establish a successful removal of inhibitory latency.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:23733187\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3774397/\n\
    \      snippet: 85 and 65\n      explanation: Activation-results paragraph reports\
    \ the one- and two-residue deletion melting temperatures,\n        respectively,\
    \ with a 95 C full-length comparator; Methods establishes thermofluor and differing\n\
    \        purification conditions.\n      cache_path: evidence/PF01863/lopez-pelegrin-2013-minigluzincins.txt\n\
    \      cache_sha256: eea4b1c7eb4e4c639aee446f64ec6e79e281cb0b67c0f90f5ce23ac744dae938\n\
    \  - edge_id: delta-m104-v105-lowers-transition\n    subject: delete-m104-v105\n\
    \    predicate: decreases\n    object: thermal-transition\n    mechanism: The\
    \ two-residue deletion preparation has reported Tm 65 C versus full-length 95\
    \ C. Larger\n      truncations had expression/solubility problems; their absent\
    \ purified activity measurements are\n      not treated as catalytic nulls.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:23733187\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3774397/\n\
    \      snippet: 85 and 65\n      explanation: Same activation-results comparison,\
    \ explicitly scoped to purified preparations and\n        a thermal readout, not\
    \ a rate or physiological phenotype.\n      cache_path: evidence/PF01863/lopez-pelegrin-2013-minigluzincins.txt\n\
    \      cache_sha256: eea4b1c7eb4e4c639aee446f64ec6e79e281cb0b67c0f90f5ce23ac744dae938\n\
    - graph_id: proabylysin-tail-latency-hypothesis\n  title: Proabylysin intramolecular\
    \ tail may suppress proteolysis\n  scope: Structural interpretation of recombinant\
    \ proabylysin 4JIU and Figure 3A, not demonstrated protease\n    activation.\n\
    \  context: A Q101-V105 C-terminal segment occupies the putative substrate cleft\
    \ in reverse substrate orientation,\n    with V105 carboxylate coordinating Zn.\
    \ Negative tested-substrate panels and unsuccessful activation\n    trials are\
    \ retained as limits.\n  family_mapping: Q9V1Y2/CAB49216.1, native numbering;\
    \ deposited L2V scaffold, paper K2V discrepancy retained.\n    PF01863 2-88 contains\
    \ H60/E61/H64 and H72, but not Q101-V105. Whole-protein architecture, not a domain-only\n\
    \    mechanism.\n  scope_status: HYPOTHETICAL\n  taxon: NCBITaxon:272844\n  limitations:\
    \ Structural occupancy supports a proposed explanation for inactivity, not proof\
    \ of reversible\n    inhibition or a functional zymogen. No active abylysin was\
    \ obtained. Tail truncation destabilizes\n    the protein, and an inactive-ancestor\
    \ interpretation remains possible. No family-wide protease claim.\n  nodes:\n\
    \  - node_id: intramolecular-tail-occupancy\n    label: Q101-V105 occupies the\
    \ cleft and coordinates Zn through V105\n    node_type: STATE\n  - node_id: proposed-proabylysin-proteolysis\n\
    \    label: Proposed proteolytic activity of the intact proabylysin scaffold\n\
    \    node_type: ACTIVITY\n  edges:\n  - edge_id: tail-may-suppress-proteolysis\n\
    \    subject: intramolecular-tail-occupancy\n    predicate: decreases\n    object:\
    \ proposed-proabylysin-proteolysis\n    mechanism: The tail could obstruct substrate\
    \ access and the catalytic metal environment. Its crystallographic\n      placement\
    \ motivates this model, but failed activation and destabilizing deletion preparations\
    \ do\n      not demonstrate that tail removal restores proteolysis.\n    directness:\
    \ UNRESOLVED\n    support: HYPOTHESIZED\n    evidence_kind: EXPERIMENTAL\n   \
    \ evidence:\n    - reference: PMID:23733187\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3774397/\n\
    \      snippet: we failed to obtain active abylysin and jannalysin\n      explanation:\
    \ Figure 3A and structural interpretation motivate tail-mediated latency; the\
    \ activation-results\n        paragraph prevents promotion to an observed inhibitory\
    \ causal step.\n      cache_path: evidence/PF01863/lopez-pelegrin-2013-minigluzincins.txt\n\
    \      cache_sha256: eea4b1c7eb4e4c639aee446f64ec6e79e281cb0b67c0f90f5ce23ac744dae938\n\
    - graph_id: projannalysin-partner-helix-latency-hypothesis\n  title: Projannalysin\
    \ partner helix may suppress proteolysis\n  scope: Structural interpretation of\
    \ the recombinant projannalysin dimer 4JIX and Figure 3B-D, kept distinct\n  \
    \  from the proabylysin intramolecular model.\n  context: Partner E102-I110 helix\
    \ lies across each putative cleft. I110 carboxylate is 4.1-4.2 A from\n    Zn,\
    \ unlike proabylysin V105 coordination. Purified protein is dimeric by size exclusion;\
    \ crystallographic\n    geometry alone does not prove intracellular dimerization\
    \ or catalytic activity.\n  family_mapping: MJ0123 Q57587 version 1 equals AAB98111.1,\
    \ 110 aa; JAL-1/DSM 2661 taxon 243232. PF01863\n    7-95 contains H69/E70/H73\
    \ and H81 but excludes E102-I110. PDB 4JIX has K2A plus residual N-terminal\n\
    \    GP after His6/TEV cleavage; native numbering, not polymer seq_id, is used.\n\
    \  scope_status: HYPOTHETICAL\n  taxon: NCBITaxon:243232\n  limitations: The proposed\
    \ trans-blocking mechanism is not directly tested by a folded active product.\n\
    \    The five-residue deletion and limited-proteolysis attempts were unsuccessful.\
    \ Negative assays do not\n    establish inactivity against every possible substrate;\
    \ the inactive-ancestor alternative remains open.\n  nodes:\n  - node_id: partner-helix-occupancy\n\
    \    label: Partner E102-I110 helix occupies the projannalysin cleft\n    node_type:\
    \ STATE\n  - node_id: proposed-projannalysin-proteolysis\n    label: Proposed\
    \ proteolytic activity of the projannalysin scaffold\n    node_type: ACTIVITY\n\
    \  edges:\n  - edge_id: partner-helix-may-suppress-proteolysis\n    subject: partner-helix-occupancy\n\
    \    predicate: decreases\n    object: proposed-projannalysin-proteolysis\n  \
    \  mechanism: The swapped terminal helix could restrict substrate access in trans.\
    \ No active jannalysin\n      was obtained, so this is an experimental-structure-motivated\
    \ hypothesis, not an observed inhibition/rescue\n      comparison or transfer\
    \ of proabylysin's Zn-ligand mechanism.\n    directness: UNRESOLVED\n    support:\
    \ HYPOTHESIZED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:23733187\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3774397/\n\
    \      snippet: we failed to obtain active abylysin and jannalysin\n      explanation:\
    \ Figure 3B-D and the dimer structural analysis support the proposed geometry;\
    \ negative\n        activation trials and the distinct terminal-carboxylate distance\
    \ constrain causal interpretation.\n      cache_path: evidence/PF01863/lopez-pelegrin-2013-minigluzincins.txt\n\
    \      cache_sha256: eea4b1c7eb4e4c639aee446f64ec6e79e281cb0b67c0f90f5ce23ac744dae938\n\
    curation_events:\n- timestamp: '2026-10-11T16:31:29Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate PF01863 YgjP activity, proabylysin\
    \ thermal effects and two separate latency hypotheses\n  history_record: history/records/PF01863/2026-10-11T163129Z-codex-26c747.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: concern
  summary: P42597v2 exactly equals BAE77135.1/AAC76120.2 and maps PF01863 94-149,
    but this verifies the reference rather than the exact historical His6-YgjP clone.
    Q9V1Y2 equals CAB49216.1, Pfam 2-88; PDB4JIU confirms L2V despite the paper K2V
    label. Q57587 equals AAB98111.1, Pfam 7-95; PDB4JIX verifies K2A plus residual
    GP. Archaeal tail sites are outside current domain spans. B80 peptide inconsistencies
    prevent confident transfer of purified activity to the family.
  target_ids:
  - PF01863
  evidence_ids:
  - identity
  - primary
  - ygjp-product-assay
  - coverage-ledger
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Two MECHANISTIC graphs contain three DIRECT OBSERVED preparation-level
    effects, while two distinct HYPOTHETICAL graphs contain one UNRESOLVED HYPOTHESIZED
    edge each. UMP ion output is not calibrated stoichiometry or separate PPi detection.
    Thermal transitions are not activation, and structural occupancy is not observed
    inhibition. Taxa, constructs, cis/trans geometry, uncertainty and whole-protein/domain
    scope remain distinct. No family-wide protease function or isolated-domain sufficiency
    is asserted.
  target_ids:
  - PF01863
  evidence_ids:
  - primary
  - native
  - ygjp-product-assay
  - coverage-ledger
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Missing Sevin full Methods, clone sequence and cellular datasets; missing
    thermal raw curves and deletion-sequence deposits; unresolved K2V/L2V manuscript
    discrepancy; no successful archaeal activation; unresolved B80 preparation identity;
    uncurated additional members and computational candidates. This is not exhaustive
    family coverage.
  target_ids:
  - PF01863
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01863-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve construct and assay gaps before strengthening functional or activation
    claims
  description: Obtain YgjP exact clone and validation Methods, calibrated UMP/PPi
    and matched controls; reconcile proabylysin sequence labels and repeat thermal
    comparisons with matched preparation; establish folded active archaeal products
    before calling tail latency observed; resolve B80 peptide/reference/mass-table
    inconsistencies. Inspect remaining member-specific primary contexts without importing
    predicted activities.
  target_ids:
  - PF01863
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - ygjp-product-assay
  - coverage-ledger
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01863.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Obtain YgjP exact clone and validation Methods, calibrated UMP/PPi
    and matched controls; reconcile proabylysin sequence labels and repeat thermal
    comparisons with matched preparation; establish folded active archaeal products
    before calling tail latency observed; resolve B80 peptide/reference/mass-table
    inconsistencies. Inspect remaining member-specific primary contexts without importing
    predicted activities.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01863
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Original Sevin Supplementary Figure 16 and Lopez-Pelegrin Figure 3 were visually
  inspected; Tables 3/9 and B80 Table 2 were parsed. No raw spectral reanalysis, diffraction
  re-refinement, inaccessible main Methods, full cellular datasets or experimental
  replication is claimed. Rendered-page checks are reported separately after generation.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
