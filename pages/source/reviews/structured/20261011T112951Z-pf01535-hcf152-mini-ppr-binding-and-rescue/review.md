# PF01535 HCF152 mini-PPR binding effects and mapping limits

- Review: 20261011T112951Z-pf01535-hcf152-mini-ppr-binding-and-rescue
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T11:29:38Z
- Finished UTC: 2026-10-11T11:29:51Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Four observed purified-fusion binding effects are supported in two separate mutant-background graphs. Local K426 mapping falls within current PF01535, whereas N464 does not. Partial rescue, apparent-affinity interpretation and inaccessible supplementary construct/gels remain explicit; native cellular and family-wide mechanisms are not established.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Pending PF01535 selected during accession-ordered review of the full 8296-family corpus; HCF152 mini-proteins are the experimentally inspected example, not a family census.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01535 | data/families/PF01535.yaml | generated | PF01535 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01535 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01535.

Q9SF38 sequence version 1 is 778 aa and matches InterPro exactly. Current hits are 416-442 and 559-585; local Figure 2C sequence mapping identifies K426 in the first hit and N464 outside both. Old motif boundaries are not current Pfam coordinates, and unavailable primers leave complete fusions unverified. Pet309 P32522 currently has PF23276 rather than PF01535, so its separate deletion phenotypes were not transferred.

### Directed effects and limits

graph: supported. Targets: PF01535.

Four DIRECT OBSERVED edges preserve the exact single-versus-WT and double-versus-single comparisons. Directness is limited to net purified-fusion binding, not an atomic contact, a universal basic/neutral residue code, isolated-domain sufficiency or a cellular RNA-processing chain. K_D direction follows Figure 3B and the assay definition rather than reversed wording in the prose. Competitive-assay salt and heparin are excluded from the standard condition.

### Remaining family coverage

completeness: concern. Targets: PF01535.

Complete mini-protein endpoints, linker/primer sequences, underlying gels, purity and mutant-folding controls remain unverified. Other substitutions, full-length HCF152 cellular perturbations, other PPR proteins and the Pet309 family-mapping discrepancy need separate assessment.

## Findings

### additional-contexts: Resolve construct and primary-gel coverage before extending PPR mechanism claims

minor / open / confirmed; issue key: pf01535-causal-context-coverage.

Retrieve Supplement Table S1 and Figures S1/S3/S4; verify full construct sequences and the RNA-probe identity, assay replication and folding controls. Review additional mapped PPR members and cellular endpoints separately, retaining old-versus-current repeat boundaries and apparent-affinity limits.

## Recommended Actions And Acceptance Checks

### extend-contexts

Retrieve Supplement Table S1 and Figures S1/S3/S4; verify full construct sequences and the RNA-probe identity, assay replication and folding controls. Review additional mapped PPR members and cellular endpoints separately, retaining old-versus-current repeat boundaries and apparent-affinity limits.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC3315335/; Production, RNA-probe and gel-shift Methods; mutation and mini-protein Results; relevant Discussion; visually inspected Figures 2 and 3, especially Figure 3B's table. Supplement Table S1 and Figures S1/S3/S4 unavailable. | supports | 5-K12N and 6-N12R each reduce binding relative to WT. The matched 5-K12N/6-N12K and 5-K12M/6-N12R double mutants partly recover binding relative to their respective single-mutant backgrounds, not to WT. Multiple shifted species make the numerical values operational half-binding concentrations. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q9SF38/entry/pfam/PF01535/; Accession and domain locations; paired UniProt identity facts | supports | Q9SF38 sequence version 1 is 778 aa and matches InterPro exactly. Current hits are 416-442 and 559-585; local Figure 2C sequence mapping identifies K426 in the first hit and N464 outside both. Old motif boundaries are not current Pfam coordinates, and unavailable primers leave complete fusions unverified. Pet309 P32522 currently has PF23276 rather than PF01535, so its separate deletion phenotypes were not transferred. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01535 | data/families/PF01535.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Figures 2 and 3 were visually inspected and compared with the Results. Supplement requests failed or timed out; incomplete archives were not used. No raw titrations, independent purification repeats or in-vivo complementation were reanalyzed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T112951Z-pf01535-hcf152-mini-ppr-binding-and-rescue
title: PF01535 HCF152 mini-PPR binding effects and mapping limits
started_at: '2026-10-11T11:29:38Z'
finished_at: '2026-10-11T11:29:51Z'
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
summary: Four observed purified-fusion binding effects are supported in two separate
  mutant-background graphs. Local K426 mapping falls within current PF01535, whereas
  N464 does not. Partial rescue, apparent-affinity interpretation and inaccessible
  supplementary construct/gels remain explicit; native cellular and family-wide mechanisms
  are not established.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01535.yaml
    sha256: 1e83933e43171b825d7fa7ea99e6e89ad9ad87c519c134e19061cffbe95676d7
    role: context
  - path: data/families/PF01535.yaml
    sha256: 171f8b5d5a7c5ef4caf169936fbcfe28b094717a4049ae95e4f303cfc2c53136
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
  - path: evidence/PF01535/kobayashi-2012-binding.txt
    role: context
    sha256: 39b83a044602820fe88c4e4c515a06ef86d5883666a57c01909ef0cdf1c2bbe3
  - path: evidence/PF01535/HCF152-identity.txt
    role: context
    sha256: 633ef7556a900bf0866613e152a924a4555074c4bc188b64310684793d3ad063
targets:
- target_id: PF01535
  path: data/families/PF01535.yaml
  label: PF01535
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01535.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: fed5b14c110308f24c00a6f7ffe90515c0c6589e6974215318c9f1dff356dbf4
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Pending PF01535 selected during accession-ordered review of the full
    8296-family corpus; HCF152 mini-proteins are the experimentally inspected example,
    not a family census.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01535
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Complete mini-protein endpoints, linker/primer sequences, underlying gels,
      purity and mutant-folding controls remain unverified. Other substitutions, full-length
      HCF152 cellular perturbations, other PPR proteins and the Pet309 family-mapping
      discrepancy need separate assessment.
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
  - PF01535
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3315335/
  locator: Production, RNA-probe and gel-shift Methods; mutation and mini-protein
    Results; relevant Discussion; visually inspected Figures 2 and 3, especially Figure
    3B's table. Supplement Table S1 and Figures S1/S3/S4 unavailable.
  accessed_at: '2026-10-11T11:29:51Z'
  support: supports
  snapshot_sha256: 39b83a044602820fe88c4e4c515a06ef86d5883666a57c01909ef0cdf1c2bbe3
  summary: 5-K12N and 6-N12R each reduce binding relative to WT. The matched 5-K12N/6-N12K
    and 5-K12M/6-N12R double mutants partly recover binding relative to their respective
    single-mutant backgrounds, not to WT. Multiple shifted species make the numerical
    values operational half-binding concentrations.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q9SF38/entry/pfam/PF01535/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T11:29:51Z'
  support: supports
  snapshot_sha256: 633ef7556a900bf0866613e152a924a4555074c4bc188b64310684793d3ad063
  summary: Q9SF38 sequence version 1 is 778 aa and matches InterPro exactly. Current
    hits are 416-442 and 559-585; local Figure 2C sequence mapping identifies K426
    in the first hit and N464 outside both. Old motif boundaries are not current Pfam
    coordinates, and unavailable primers leave complete fusions unverified. Pet309
    P32522 currently has PF23276 rather than PF01535, so its separate deletion phenotypes
    were not transferred.
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T11:29:51Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01535
  kind: record_content
  reference: data/families/PF01535.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T11:29:51Z'
  support: context_only
  snapshot_sha256: 171f8b5d5a7c5ef4caf169936fbcfe28b094717a4049ae95e4f303cfc2c53136
  quote: "id: Pfam:PF01535\npfam_id: PF01535\nname: PPR repeat\nshort_name: PPR\n\
    seed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status: IN_PROGRESS\n\
    source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01535\ncounters:\n\
    \  proteins: 228033\n  matches: 700640\n  proteomes: 3274\n  taxa: 9110\n  structures:\
    \ 30\n  alphafold_models: 180864\n  domain_architectures: 35610\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002885\ndescription: This repeat has no known function.\
    \ It is about 35 amino acids long and found in up to 18\n  copies in some proteins.\
    \ This family appears to be greatly expanded in plants. This repeat occurs in\n\
    \  PET309 [swissprot:P32522] that may be involved in RNA stabilisation [[cite:PUB00001271]].\
    \ This domain\n  occurs in crp1 that is involved in RNA processing [[cite:PUB00001258]].\
    \ This repeat is associated with\n  a predicted plant protein [swissprot:O49549]\
    \ that has a domain organisation similar to the human BRCA1\n  protein. The repeat\
    \ has been called PPR [[cite:PUB00017589]].\ncuration_history: history/records/PF01535\n\
    discussions:\n- discussion_id: ppr-current-mapping-constructs-and-cellular-transfer\n\
    \  prompt: Resolve complete HCF152 assay constructs and current PPR-family mapping\
    \ before extending the\n    causal graph.\n  kind: CURATION_TODO\n  status: OPEN\n\
    \  rationale: Local K426 mapping is supported, but old repeat definitions, present\
    \ Pfam hits and full fusion\n    boundaries are different claims. Binding changes\
    \ do not automatically establish native RNA processing,\n    translation or editing\
    \ mechanisms.\n  evidence:\n  - reference: PMID:22127869\n    supports: PARTIAL\n\
    \    evidence_source: full_text_and_main_figures\n    explanation: Main Methods,\
    \ relevant Results/Discussion and Figures 2/3 support four scoped mutation\n \
    \     comparisons. Supplement Table S1 and Figures S1/S3/S4 were inaccessible;\
    \ purity, complete constructs,\n      underlying gels and a definitive residue-contact\
    \ interpretation remain open. Figure 3B puts K12H\n      at 27 nM versus WT 9.7\
    \ nM; it is not literally unchanged.\n  - reference: PMID:25181249\n    supports:\
    \ PARTIAL\n    evidence_source: selected_full_text_and_identity_databases\n  \
    \  explanation: Pet309 deletion/translation work is a separate lead. The tested\
    \ D273-10B derivatives\n      differ from the S288c reference context, and the\
    \ inspected current P32522 Pfam assignments contain\n      PF23276 rather than\
    \ PF01535. Its PPR annotation is not sufficient to transfer those deletion phenotypes\n\
    \      into this family graph.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n\
    \  notes: Assess other PPR members and full-length HCF152 perturbations from their\
    \ own primary evidence.\n    Do not repair the source's reversed K_D wording silently\
    \ or treat an inaccessible supplement as negative\n    evidence. Partial scientific\
    \ self-review; IN_PROGRESS.\ncausal_graphs:\n- graph_id: hcf152-mini-ppr-k12n-and-rescue\n\
    \  title: Motif-5 K12N reduces RNA binding and motif-6 N12K partly restores it\n\
    \  scope: Arabidopsis HCF152-derived HCF/5&6 mini-protein fusions in Kobayashi\
    \ 2012 Figure 3B; not full-length\n    chloroplast protein or all PPR proteins.\n\
    \  context: Purified N-terminal thioredoxin and C-terminal six-His fusions are\
    \ titrated against 250 pM\n    radiolabeled Dd120 RNA, a 120-nt psbH-region probe.\
    \ Reactions use 20 ul, 10 mM Tris-HCl pH 8.0, 40\n    mM KCl, 6 mM MgCl2, 0.05\
    \ mM EDTA, 2 mM DTT and 8% w/v glycerol at 25 C for 15 min, followed by 10%\n\
    \    native PAGE. Apparent K_D is the protein concentration at 50% total RNA binding;\
    \ the competitive-assay\n    extra salt/heparin is not part of this condition.\n\
    \  family_mapping: Q9SF38 / HCF152 / At3g09650 is the 778-aa Arabidopsis reference,\
    \ sequence version 1,\n    identical between UniProt and InterPro. Current PF01535\
    \ hits are 416-442 and 559-585. Local Figure\n    2C motif residues identify 5-K12\
    \ as reference K426 inside the first hit and 6-N12 as N464 outside\n    both current\
    \ hits. Historical motif numbering is not the same as current Pfam boundaries.\
    \ Complete\n    mini-protein endpoints and linkers remain unverified because supplementary\
    \ primers were inaccessible.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:3702\n\
    \  limitations: Directness concerns the purified fusion's net binding response,\
    \ not a proven atomic RNA\n    contact or isolated PF01535 sufficiency. Multiple\
    \ shifted species limit equilibrium interpretation.\n    Figures 2/3 were visually\
    \ inspected; supplemental gels, purity and primers were not. Independent purification\n\
    \    batches and mutant-folding equivalence remain unestablished. The double mutant\
    \ remains much weaker\n    than WT; no cellular processing or editing chain is\
    \ inferred.\n  nodes:\n  - node_id: motif5-k12n-versus-wt\n    label: HCF/5&6\
    \ 5-K12N rather than WT\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q9SF38\n\
    \  - node_id: motif6-n12k-on-k12n\n    label: Add 6-N12K to the 5-K12N mini-protein\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q9SF38\n  - node_id:\
    \ dd120-binding-k12n-series\n    label: Dd120 RNA binding in the HCF/5&6 fusion\
    \ titration\n    node_type: ACTIVITY\n  edges:\n  - edge_id: motif5-k12n-decreases-binding\n\
    \    subject: motif5-k12n-versus-wt\n    predicate: decreases\n    object: dd120-binding-k12n-series\n\
    \    mechanism: The 5-K12N fusion requires more than 2500 nM protein to reach\
    \ the operational half-binding\n      threshold, compared with 9.7 nM for WT.\
    \ This supports reduced binding in the tested assay, not complete\n      absence\
    \ of every RNA interaction.\n    directness: DIRECT\n    support: OBSERVED\n \
    \   evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:22127869\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3315335/\n      snippet:\
    \ partially recovered\n      explanation: Figure 3B's WT and 5-K12N values, the\
    \ mutation Results and gel-shift Methods establish\n        the loss-of-binding\
    \ comparison. The retained direction follows the figure and operational definition,\n\
    \        not the text's reversed K_D wording.\n      cache_path: evidence/PF01535/kobayashi-2012-binding.txt\n\
    \      cache_sha256: 39b83a044602820fe88c4e4c515a06ef86d5883666a57c01909ef0cdf1c2bbe3\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q9SF38/entry/pfam/PF01535/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q9SF38/entry/pfam/PF01535/\n\
    \      snippet: 'Q9SF38 Pfam:PF01535; repeat intervals: 416-442 and 559-585, inclusive.'\n\
    \      explanation: Current sequence matching places locally mapped K426 inside\
    \ PF01535 while preserving\n        the different old motif convention and unresolved\
    \ complete assay constructs.\n      cache_path: evidence/PF01535/HCF152-identity.txt\n\
    \      cache_sha256: 633ef7556a900bf0866613e152a924a4555074c4bc188b64310684793d3ad063\n\
    \  - edge_id: motif6-n12k-partially-restores-binding\n    subject: motif6-n12k-on-k12n\n\
    \    predicate: increases\n    object: dd120-binding-k12n-series\n    mechanism:\
    \ On the 5-K12N background, adding 6-N12K lowers the operational half-binding\
    \ concentration\n      from above 2500 nM to 384.6 nM. The comparison is to the\
    \ single mutant, not WT; this is partial\n      recovery and does not prove a\
    \ particular inter-residue contact.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:22127869\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3315335/\n      snippet:\
    \ partially recovered\n      explanation: Visually inspected Figure 3B and its\
    \ Results explicitly compare the 5-K12N single mutant\n        with the 5-K12N/6-N12K\
    \ double mutant. N464 lies outside the current PF01535 hit, so this is a\n   \
    \     fusion-context rescue rather than an isolated-domain claim.\n      cache_path:\
    \ evidence/PF01535/kobayashi-2012-binding.txt\n      cache_sha256: 39b83a044602820fe88c4e4c515a06ef86d5883666a57c01909ef0cdf1c2bbe3\n\
    - graph_id: hcf152-mini-ppr-n12r-and-rescue\n  title: Motif-6 N12R reduces RNA\
    \ binding and motif-5 K12M partly restores it\n  scope: Separate HCF/5&6 single-\
    \ and double-mutant comparisons from Kobayashi 2012 Figure 3B, retaining\n   \
    \ the N-terminal thioredoxin and C-terminal six-His fusions.\n  context: Dd120\
    \ RNA at 250 pM is incubated with serial protein concentrations in 20 ul containing\
    \ 10\n    mM Tris-HCl pH 8.0, 40 mM KCl, 6 mM MgCl2, 0.05 mM EDTA, 2 mM DTT and\
    \ 8% w/v glycerol, for 15 min\n    at 25 C. Native 10% PAGE supplies the operational\
    \ 50%-binding concentration; no extra competitive-assay\n    salt or heparin is\
    \ assumed.\n  family_mapping: Local motif sequence mapping to Q9SF38 places 6-N12\
    \ at N464 outside current PF01535\n    and 5-K12 at K426 within 416-442. Q9SF38\
    \ also has a separate 559-585 PF01535 hit, not this motif-5/6\n    pair. These\
    \ are perturbations of the same mapped-protein-derived fusion, not proof that\
    \ each perturbed\n    residue belongs to the current Pfam hit. Historical full\
    \ clone boundaries remain unresolved.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:3702\n\
    \  limitations: The N12R effect is outside the current Pfam interval and may involve\
    \ the broader fusion\n    context. The matched double-mutant comparison does not\
    \ independently establish an isolated K12M effect.\n    No direct RNA-contact\
    \ geometry, universal basic/neutral residue rule, native chloroplast effect or\n\
    \    folding equivalence is established. Supplemental gels and primer table remain\
    \ inaccessible.\n  nodes:\n  - node_id: motif6-n12r-versus-wt\n    label: HCF/5&6\
    \ 6-N12R rather than WT\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q9SF38\n\
    \  - node_id: motif5-k12m-on-n12r\n    label: Add 5-K12M to the 6-N12R mini-protein\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q9SF38\n  - node_id:\
    \ dd120-binding-n12r-series\n    label: Dd120 RNA binding in the N12R-background\
    \ fusion titration\n    node_type: ACTIVITY\n  edges:\n  - edge_id: motif6-n12r-decreases-binding\n\
    \    subject: motif6-n12r-versus-wt\n    predicate: decreases\n    object: dd120-binding-n12r-series\n\
    \    mechanism: The 6-N12R fusion has an apparent half-binding concentration above\
    \ 2500 nM versus 9.7 nM\n      for WT. This supports reduced assay binding despite\
    \ introducing an additional basic residue; no\n      specific physical explanation\
    \ is uniquely established.\n    directness: DIRECT\n    support: OBSERVED\n  \
    \  evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:22127869\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3315335/\n      snippet:\
    \ partially recovered\n      explanation: Figure 3B's 6-N12R and WT rows were\
    \ visually checked against the Results and assay\n        definition; an unquantified\
    \ ND value is not treated as zero binding.\n      cache_path: evidence/PF01535/kobayashi-2012-binding.txt\n\
    \      cache_sha256: 39b83a044602820fe88c4e4c515a06ef86d5883666a57c01909ef0cdf1c2bbe3\n\
    \  - edge_id: motif5-k12m-partially-restores-binding\n    subject: motif5-k12m-on-n12r\n\
    \    predicate: increases\n    object: dd120-binding-n12r-series\n    mechanism:\
    \ Adding 5-K12M to 6-N12R lowers the operational half-binding concentration from\
    \ above 2500\n      nM to 454.5 nM. The observed improvement remains far from\
    \ WT and is limited to this double-versus-single-mutant\n      comparison.\n \
    \   directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:22127869\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3315335/\n\
    \      snippet: partially recovered\n      explanation: Visually inspected Figure\
    \ 3B and mutation Results support partial recovery on the N12R\n        background.\
    \ This does not establish that a universal paired-residue code or K12M alone causes\n\
    \        the same result.\n      cache_path: evidence/PF01535/kobayashi-2012-binding.txt\n\
    \      cache_sha256: 39b83a044602820fe88c4e4c515a06ef86d5883666a57c01909ef0cdf1c2bbe3\n\
    curation_events:\n- timestamp: '2026-10-11T11:21:57Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curated HCF152 mini-PPR binding losses\
    \ and partial rescues.\n  history_record: history/records/PF01535/2026-10-11T112157Z-codex-4fa265.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Q9SF38 sequence version 1 is 778 aa and matches InterPro exactly. Current
    hits are 416-442 and 559-585; local Figure 2C sequence mapping identifies K426
    in the first hit and N464 outside both. Old motif boundaries are not current Pfam
    coordinates, and unavailable primers leave complete fusions unverified. Pet309
    P32522 currently has PF23276 rather than PF01535, so its separate deletion phenotypes
    were not transferred.
  target_ids:
  - PF01535
  evidence_ids:
  - identity
  - primary
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Four DIRECT OBSERVED edges preserve the exact single-versus-WT and double-versus-single
    comparisons. Directness is limited to net purified-fusion binding, not an atomic
    contact, a universal basic/neutral residue code, isolated-domain sufficiency or
    a cellular RNA-processing chain. K_D direction follows Figure 3B and the assay
    definition rather than reversed wording in the prose. Competitive-assay salt and
    heparin are excluded from the standard condition.
  target_ids:
  - PF01535
  evidence_ids:
  - primary
  - native
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Complete mini-protein endpoints, linker/primer sequences, underlying gels,
    purity and mutant-folding controls remain unverified. Other substitutions, full-length
    HCF152 cellular perturbations, other PPR proteins and the Pet309 family-mapping
    discrepancy need separate assessment.
  target_ids:
  - PF01535
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01535-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve construct and primary-gel coverage before extending PPR mechanism
    claims
  description: Retrieve Supplement Table S1 and Figures S1/S3/S4; verify full construct
    sequences and the RNA-probe identity, assay replication and folding controls.
    Review additional mapped PPR members and cellular endpoints separately, retaining
    old-versus-current repeat boundaries and apparent-affinity limits.
  target_ids:
  - PF01535
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01535.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Retrieve Supplement Table S1 and Figures S1/S3/S4; verify full construct
    sequences and the RNA-probe identity, assay replication and folding controls.
    Review additional mapped PPR members and cellular endpoints separately, retaining
    old-versus-current repeat boundaries and apparent-affinity limits.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01535
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Figures 2 and 3 were visually inspected and compared with the Results. Supplement
  requests failed or timed out; incomplete archives were not used. No raw titrations,
  independent purification repeats or in-vivo complementation were reanalyzed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
