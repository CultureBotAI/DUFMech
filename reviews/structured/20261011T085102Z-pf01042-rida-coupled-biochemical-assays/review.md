# Scoped scientific self-review of RidA coupled biochemical effects

- Review: 20261011T085102Z-pf01042-rida-coupled-biochemical-assays
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T08:50:51Z
- Finished UTC: 2026-10-11T08:51:02Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Five MECHANISTIC graphs retain nine DIRECT OBSERVED effects across distinct threonine-rate, ferricyanide-endpoint, substitution, serine-rate and retained-IlvE assays. Necessary partners and conditions are explicit. No elementary hydrolysis trajectory, universal family function or proven reversal of IlvE damage is claimed. Source order ambiguity and clone gaps remain; partial coverage and IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01042 Ribonuc_L-PSP/RidA, the next accession-ordered SEEDED family, using Salmonella experiments in Lambrecht 2012 and 2013.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01042 | data/families/PF01042.yaml | generated | PF01042 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01042 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01042.

LT2 RidA Q7CP78, ridA/yjgF/STM4458, 128 residues and sequence version 1, exactly matches the InterPro reference and maps PF01042 to 7-126 inclusive. Adopted substitution positions were directly checked. IlvA P20506 and IlvE P0A1A5 provide LT2 partner references, not verification of every experimental clone. C-terminal tags and distinct production hosts are stated; an E. coli production host does not change donor identity or assign mammalian RNase function.

### Directed effects and limits

graph: supported. Targets: PF01042.

The graphs retain directly measured biochemical endpoints in explicitly coupled systems, not independent sufficiency of RidA, PLP or substrate. Ferricyanide and product yield are correlated outputs from one experiment, not independent replication. Figure 6 substitutions constrain activity without uniquely proving chemical roles. Figure 1B of 2013 supports retained IlvE activity despite caption/Methods disagreement on RidA addition order, so no repair/reversal edge is adopted. No whole-family generalization or frozen-label replacement is made.

### Remaining family coverage

completeness: concern. Targets: PF01042.

Complete clone junctions and the earlier purification paper, exact ferricyanide endpoint temperature, reconciliation of IlvE addition order and modified-peptide identity remain unresolved. Raw kinetic and MS data were not reanalyzed. Other RidA homologs, cellular phenotypes, additional biochemical substrates and the family label's RNase context need separately mapped primary curation. These five graphs are not complete family coverage.

## Findings

### additional-contexts: Resolve RidA assay metadata and extend member-specific chemical coverage

minor / open / confirmed; issue key: pf01042-causal-context-coverage.

Obtain complete clone and purification details, resolve the two-hour endpoint temperature and IlvE addition order, and assess adduct evidence without inventing a modified site. Curate other homologs and cellular contexts separately with their own identity and causal support, preserving uncertainty and appending a successor review before status promotion.

## Recommended Actions And Acceptance Checks

### extend-contexts

Obtain complete clone and purification details, resolve the two-hour endpoint temperature and IlvE addition order, and assess adduct evidence without inventing a modified site. Curate other homologs and cellular contexts separately with their own identity and causal support, preserving uncertainty and appending a successor review before status promotion.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC3270999/; Experimental Procedures, Results and Discussion; Figures 2, 4, 6 and 7 visually inspected | supports | Coupled assays support added-RidA rate enhancement with threonine and serine, two distinct outputs in ferricyanide trapping, and decreased enhancement for Y17F, R105A, E120K and E120A. High-pH rates use 30-60 s; Figure 6 uses single CHES rather than the mixed kinetic buffer. None of the substitutions eliminates all activity; atomic water or proton-transfer interpretations are not observed edges. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q7CP78/entry/pfam/PF01042/; Accession and domain locations; paired UniProt identity facts | supports | LT2 RidA Q7CP78, ridA/yjgF/STM4458, 128 residues and sequence version 1, exactly matches the InterPro reference and maps PF01042 to 7-126 inclusive. Adopted substitution positions were directly checked. IlvA P20506 and IlvE P0A1A5 provide LT2 partner references, not verification of every experimental clone. C-terminal tags and distinct production hosts are stated; an E. coli production host does not change donor identity or assign mammalian RNase function. |
| retained-ilve-activity | https://pmc.ncbi.nlm.nih.gov/articles/PMC3565831/; Figure 1B Salmonella comparison; radioactive IlvE Methods, purification and relevant Results/Discussion | supports | RidA increases retained IlvE activity in the IlvA/serine condition. Methods include RidA during preincubation whereas caption wording suggests later addition, limiting prevention-versus-reversal interpretation. Other homologs, 3-chloroalanine methods and adduct MS are distinct contexts rather than silently transferred controls or microsteps. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01042 | data/families/PF01042.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Lambrecht 2012 Figures 2/4/6/7 and Lambrecht 2013 Figure 1 were visually inspected. Relevant Methods and Results were read, with the 2012 Discussion and 2013 mechanism qualifications considered. No raw kinetics, replicate gels, MS reanalysis or complete historical construct reconstruction was performed. The 2012 model figure is not adopted as an observed trajectory.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T085102Z-pf01042-rida-coupled-biochemical-assays
title: Scoped scientific self-review of RidA coupled biochemical effects
started_at: '2026-10-11T08:50:51Z'
finished_at: '2026-10-11T08:51:02Z'
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
summary: Five MECHANISTIC graphs retain nine DIRECT OBSERVED effects across distinct
  threonine-rate, ferricyanide-endpoint, substitution, serine-rate and retained-IlvE
  assays. Necessary partners and conditions are explicit. No elementary hydrolysis
  trajectory, universal family function or proven reversal of IlvE damage is claimed.
  Source order ambiguity and clone gaps remain; partial coverage and IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01042.yaml
    sha256: 50141525d4aa2f7d7ab296715cbb84508a3652702b0357e4ddf866d019825a92
    role: context
  - path: data/families/PF01042.yaml
    sha256: 91b48444e12f1a78f08159530fd1683e373626d9ad5a2b3be4de8575c51fb041
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
  - path: evidence/PF01042/lambrecht-2012-ridA.txt
    role: context
    sha256: 44bebd6b53abf4bf626d60cecda72c21923d7b23dec4a7096b29a11034c9a50c
  - path: evidence/PF01042/RidA-identity.txt
    role: context
    sha256: b481b4fe96410b0c8aa9f8f5c96fec413a3a7655cbdd1050140c65ceebcd60b3
  - path: evidence/PF01042/lambrecht-2013-ridA.txt
    role: context
    sha256: 7a4b26847f592333f017c826611c5e001984b6b5ab591d2ed4a0516ab20c80c2
targets:
- target_id: PF01042
  path: data/families/PF01042.yaml
  label: PF01042
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01042.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: ef9e3345c2921560496d55c21e56bf2a85969b339304de754475e8a778884287
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01042 Ribonuc_L-PSP/RidA, the next accession-ordered SEEDED family,
    using Salmonella experiments in Lambrecht 2012 and 2013.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01042
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Complete clone junctions and the earlier purification paper, exact ferricyanide
      endpoint temperature, reconciliation of IlvE addition order and modified-peptide
      identity remain unresolved. Raw kinetic and MS data were not reanalyzed. Other
      RidA homologs, cellular phenotypes, additional biochemical substrates and the
      family label's RNase context need separately mapped primary curation. These
      five graphs are not complete family coverage.
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
  - PF01042
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3270999/
  locator: Experimental Procedures, Results and Discussion; Figures 2, 4, 6 and 7
    visually inspected
  accessed_at: '2026-10-11T08:51:02Z'
  support: supports
  snapshot_sha256: 44bebd6b53abf4bf626d60cecda72c21923d7b23dec4a7096b29a11034c9a50c
  summary: Coupled assays support added-RidA rate enhancement with threonine and serine,
    two distinct outputs in ferricyanide trapping, and decreased enhancement for Y17F,
    R105A, E120K and E120A. High-pH rates use 30-60 s; Figure 6 uses single CHES rather
    than the mixed kinetic buffer. None of the substitutions eliminates all activity;
    atomic water or proton-transfer interpretations are not observed edges.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q7CP78/entry/pfam/PF01042/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T08:51:02Z'
  support: supports
  snapshot_sha256: b481b4fe96410b0c8aa9f8f5c96fec413a3a7655cbdd1050140c65ceebcd60b3
  summary: LT2 RidA Q7CP78, ridA/yjgF/STM4458, 128 residues and sequence version 1,
    exactly matches the InterPro reference and maps PF01042 to 7-126 inclusive. Adopted
    substitution positions were directly checked. IlvA P20506 and IlvE P0A1A5 provide
    LT2 partner references, not verification of every experimental clone. C-terminal
    tags and distinct production hosts are stated; an E. coli production host does
    not change donor identity or assign mammalian RNase function.
- evidence_id: retained-ilve-activity
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3565831/
  locator: Figure 1B Salmonella comparison; radioactive IlvE Methods, purification
    and relevant Results/Discussion
  summary: RidA increases retained IlvE activity in the IlvA/serine condition. Methods
    include RidA during preincubation whereas caption wording suggests later addition,
    limiting prevention-versus-reversal interpretation. Other homologs, 3-chloroalanine
    methods and adduct MS are distinct contexts rather than silently transferred controls
    or microsteps.
  accessed_at: '2026-10-11T08:51:02Z'
  support: supports
  snapshot_sha256: 7a4b26847f592333f017c826611c5e001984b6b5ab591d2ed4a0516ab20c80c2
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T08:51:02Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01042
  kind: record_content
  reference: data/families/PF01042.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T08:51:02Z'
  support: context_only
  snapshot_sha256: 91b48444e12f1a78f08159530fd1683e373626d9ad5a2b3be4de8575c51fb041
  quote: "id: Pfam:PF01042\npfam_id: PF01042\nname: Endoribonuclease L-PSP\nshort_name:\
    \ Ribonuc_L-PSP\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01042\n\
    counters:\n  proteins: 74014\n  matches: 76763\n  proteomes: 19722\n  taxa: 31830\n\
    \  structures: 76\n  alphafold_models: 48953\n  domain_architectures: 403\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR006175\ndescription: Endoribonuclease active on single-stranded\
    \ mRNA. Inhibits protein synthesis by cleavage of\n  mRNA [[cite:PUB00007949]].\
    \ Previously thought to inhibit protein synthesis initiation [[cite:PUB00002939]].\n\
    \  This protein may also be involved in the regulation of purine biosynthesis\
    \ [[cite:PUB00007948]]. YjgF\n  (renamed RidA) family members are enamine/imine\
    \ deaminases. They hydrolyze reactive intermediates released\n  by PLP-dependent\
    \ enzymes, including threonine dehydratase [[cite:PUB00064878]]. YjgF also prevents\
    \ inhibition\n  of transaminase B (IlvE) in Salmonella [[cite:PUB00109184]].\n\
    curation_history: history/records/PF01042\ndiscussions:\n- discussion_id: rida-addition-order-chemistry-and-family-coverage\n\
    \  prompt: Resolve RidA construct and addition-order details, then extend member-specific\
    \ chemical and\n    cellular contexts.\n  kind: CURATION_TODO\n  status: OPEN\n\
    \  rationale: Coupled biochemical endpoints and substitutions support directed\
    \ effects without directly\n    resolving every enamine/imine hydrolysis microstep.\
    \ The IlvE assay has an addition-order discrepancy,\n    and the imported RNase\
    \ label is not a Salmonella experiment.\n  evidence:\n  - reference: PMID:22094463\n\
    \    supports: PARTIAL\n    evidence_source: selected_full_text\n    explanation:\
    \ Methods, Results, Discussion and Figures 2/4/6/7 support the retained comparisons.\
    \ Additional\n      homologs, cellular complementation and complete clone history\
    \ are not independently curated.\n  - reference: PMID:23386433\n    supports:\
    \ PARTIAL\n    evidence_source: selected_full_text\n    explanation: Figure 1B\
    \ supports retained IlvE activity; caption/Methods order and unlocalized adduct\n\
    \      chemistry limit stronger repair and atomic-mechanism claims.\n  posed_by:\
    \ Codex\n  posed_date: '2026-10-11'\n  notes: Retrieve complete clones and earlier\
    \ purification details; resolve addition order and endpoint\n    temperature;\
    \ assess adduct evidence and separately map other homologs and cellular phenotypes.\
    \ Preserve\n    frozen seed labels and do not transfer mammalian RNase activity.\
    \ Partial same-agent scientific review;\n    remain IN_PROGRESS.\ncausal_graphs:\n\
    - graph_id: rida-ilva-threonine-product-rate\n  title: RidA increases 2-ketobutyrate\
    \ formation in the coupled IlvA assay\n  scope: Intact Salmonella RidA/YjgF and\
    \ IlvA with C-terminal His6 tags, not isolated PF01042 or a mammalian\n    L-PSP\
    \ RNase assay.\n  context: Figure 2B of the 2012 study; 0.9 uM IlvA, 1.6 uM RidA\
    \ when present, 10 uM PLP, threonine series,\n    50 mM each TAPS/CHES/CAPS at\
    \ pH 9.5, 200 uL, 22 C. A230 initial rates use 30-60 s at this pH. Doses\n   \
    \ are monomer-based. Two replicates with SE, representative of more than five\
    \ independent experiments.\n  family_mapping: LT2 reference UniProtKB:Q7CP78,\
    \ ridA/yjgF/STM4458, 128 residues, sequence version 1,\n    agrees exactly with\
    \ InterPro; PF01042 spans 7-126 inclusive. Production in E. coli BL21AI does not\n\
    \    change the Salmonella donor identity. Complete clone junctions remain unverified.\n\
    \  scope_status: MECHANISTIC\n  taxon: NCBITaxon:99287\n  limitations: Directness\
    \ describes a measured coupled biochemical output. RidA alone is not asserted\n\
    \    to dehydrate threonine. Separate TLC/MS support product identity, not direct\
    \ visualization of an enamine,\n    imine, water-positioning or proton-transfer\
    \ trajectory. Frozen family labels do not assign this protein\n    RNase activity\
    \ or establish a universal family function.\n  nodes:\n  - node_id: rida-added-to-ilva-threonine\n\
    \    label: RidA added to the IlvA, threonine and PLP assay\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q7CP78\n    - UniProtKB:P20506\n  - node_id:\
    \ two-ketobutyrate-initial-rate\n    label: Initial rate of 2-ketobutyrate formation\n\
    \    node_type: ACTIVITY\n  edges:\n  - edge_id: rida-increases-threonine-product-rate\n\
    \    subject: rida-added-to-ilva-threonine\n    predicate: increases\n    object:\
    \ two-ketobutyrate-initial-rate\n    mechanism: Adding RidA increases the measured\
    \ keto-acid production rate relative to IlvA without RidA\n      across the tested\
    \ substrate series. IlvA, substrate and assay cofactors remain explicit joint\
    \ conditions;\n      this is not a RidA-only reaction or an elementary chemical\
    \ step.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:22094463\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3270999/\n\
    \      snippet: significantly increased the rate\n      explanation: Figure 2B\
    \ and the kinetic Methods support the added-RidA comparison at pH 9.5. The\n \
    \       high-pH rate window is 30-60 s, not the initial burst.\n      cache_path:\
    \ evidence/PF01042/lambrecht-2012-ridA.txt\n      cache_sha256: 44bebd6b53abf4bf626d60cecda72c21923d7b23dec4a7096b29a11034c9a50c\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q7CP78/entry/pfam/PF01042/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q7CP78/entry/pfam/PF01042/\n\
    \      snippet: 'Q7CP78 Pfam:PF01042 interval: 7-126, inclusive'\n      explanation:\
    \ Maps the Salmonella reference to PF01042; identity evidence is not a separate\
    \ causal\n        experiment or proof of every experimental clone sequence.\n\
    \      cache_path: evidence/PF01042/RidA-identity.txt\n      cache_sha256: b481b4fe96410b0c8aa9f8f5c96fec413a3a7655cbdd1050140c65ceebcd60b3\n\
    - graph_id: rida-ferricyanide-partition-endpoint\n  title: RidA changes ferricyanide\
    \ reduction and keto-acid yield in a trapping assay\n  scope: The tagged Salmonella\
    \ RidA/IlvA preparation in the 2012 Figure 4B two-hour endpoint, separate\n  \
    \  from the initial-rate assay.\n  context: 10 mM threonine, 5 mM ferricyanide,\
    \ 0.9 uM IlvA, 10 uM PLP, 1.6 uM RidA when present, 50 mM\n    each TAPS/CHES/CAPS\
    \ pH 9.5. Reduced ferricyanide is measured by A420 and 2-ketobutyrate by DNPH\
    \ derivatization.\n    Two replicates with SD, representative of four independent\
    \ endpoint experiments. Dedicated endpoint-method\n    temperature is not specified.\n\
    \  family_mapping: Intact LT2 RidA Q7CP78, sequence version 1, contains PF01042\
    \ at 7-126; IlvA maps to\n    P20506. Tags and reference mapping are established,\
    \ but complete clone junctions remain unverified.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:99287\n  limitations: Two outputs from one experiment are\
    \ not independent replication or a serial observed pathway.\n    Ferricyanide\
    \ trapping supports accessible reactive intermediates but does not directly resolve\
    \ their\n    structure or RidA catalytic microsteps. DNPH avoids ferricyanide\
    \ interference at A230. Temperatures\n    of other assays are not silently transferred\
    \ to this endpoint.\n  nodes:\n  - node_id: rida-in-ferricyanide-assay\n    label:\
    \ RidA added to IlvA, threonine, PLP and ferricyanide\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q7CP78\n    - UniProtKB:P20506\n  - node_id:\
    \ ferricyanide-reduced-at-two-hours\n    label: Amount of ferricyanide reduced\
    \ at two hours\n    node_type: STATE\n  - node_id: two-ketobutyrate-at-two-hours\n\
    \    label: Yield of 2-ketobutyrate at two hours\n    node_type: STATE\n  edges:\n\
    \  - edge_id: rida-decreases-ferricyanide-reduction\n    subject: rida-in-ferricyanide-assay\n\
    \    predicate: decreases\n    object: ferricyanide-reduced-at-two-hours\n   \
    \ mechanism: The RidA-containing reaction reduces less ferricyanide than the matched\
    \ reaction lacking\n      RidA at the two-hour endpoint. Intermediate removal\
    \ is an interpretation of this trapping result,\n      not a directly imaged molecular\
    \ trajectory.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:22094463\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC3270999/\n      snippet: dramatically\
    \ decreased\n      explanation: Figure 4B rightmost pair and accompanying Results\
    \ show less ferricyanide reduction\n        with RidA at 5 mM ferricyanide; no\
    \ exact value was digitized.\n      cache_path: evidence/PF01042/lambrecht-2012-ridA.txt\n\
    \      cache_sha256: 44bebd6b53abf4bf626d60cecda72c21923d7b23dec4a7096b29a11034c9a50c\n\
    \  - edge_id: rida-increases-trapping-assay-product-yield\n    subject: rida-in-ferricyanide-assay\n\
    \    predicate: increases\n    object: two-ketobutyrate-at-two-hours\n    mechanism:\
    \ Under the same trapping conditions, adding RidA increases the keto-acid endpoint\
    \ yield.\n      This measured product redistribution is not presented as independent\
    \ evidence that each proposed\n      hydrolytic microstep was observed.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:22094463\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3270999/\n\
    \      snippet: converted to 2-ketobutyrate\n      explanation: Figure 4B product\
    \ bars and the right-pair Results comparison support higher product\n        yield\
    \ with RidA, with DNPH rather than A230 quantitation.\n      cache_path: evidence/PF01042/lambrecht-2012-ridA.txt\n\
    \      cache_sha256: 44bebd6b53abf4bf626d60cecda72c21923d7b23dec4a7096b29a11034c9a50c\n\
    - graph_id: rida-substitutions-reduce-coupled-rate-enhancement\n  title: Y17F,\
    \ R105A, E120K and E120A reduce RidA-dependent rate enhancement\n  scope: Individually\
    \ purified tagged Salmonella RidA variants compared with WT in the 2012 Figure\
    \ 6 pH\n    9.5 panel.\n  context: 15 mM threonine, 0.9 uM IlvA, 1.6 uM WT or\
    \ variant RidA, 50 mM CHES pH 9.5. General kinetic\n    conditions include 10\
    \ uM PLP, 200 uL, 22 C and the 30-60 s rate window. Output is the fold increase\n\
    \    over IlvA alone. Three replicates with SD, representative of three independent\
    \ experiments. The separate\n    pH 8 HEPES bars are not merged into this context.\n\
    \  family_mapping: Q7CP78 sequence version 1 contains Y17, R105 and E120 within\
    \ PF01042 residues 7-126.\n    Intact C-terminally His6-tagged QuikChange variants\
    \ use the same purification approach as WT; exact\n    clones remain unsequenced\
    \ in this assessment.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:99287\n\
    \  limitations: Each substitution reduces, but does not eliminate, measured enhancement.\
    \ Activity changes\n    do not uniquely resolve water positioning, an essential\
    \ acid/base residue or an isolated-domain mechanism.\n    Purification and reported\
    \ stability do not independently establish identical folding or active-protein\n\
    \    fraction. R105A retains burst kinetics and has the lowest enhancement.\n\
    \  nodes:\n  - node_id: y17f-in-coupled-assay\n    label: RidA Y17F substituted\
    \ for WT\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q7CP78\n\
    \  - node_id: r105a-in-coupled-assay\n    label: RidA R105A substituted for WT\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q7CP78\n  - node_id:\
    \ e120k-in-coupled-assay\n    label: RidA E120K substituted for WT\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:Q7CP78\n  - node_id: e120a-in-coupled-assay\n\
    \    label: RidA E120A substituted for WT\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q7CP78\n  - node_id: product-rate-fold-enhancement\n    label:\
    \ Fold enhancement of 2-ketobutyrate initial rate over IlvA alone\n    node_type:\
    \ ACTIVITY\n  edges:\n  - edge_id: y17f-decreases-rate-enhancement\n    subject:\
    \ y17f-in-coupled-assay\n    predicate: decreases\n    object: product-rate-fold-enhancement\n\
    \    mechanism: Y17F gives less coupled product-rate enhancement than WT at equal\
    \ nominal monomer concentration,\n      without abolishing the enhancement or\
    \ establishing a unique residue-level chemical role.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:22094463\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3270999/\n\
    \      snippet: all four variants were defective\n      explanation: Figure 6\
    \ gray Y17F and WT bars support this substitution-specific comparison at pH\n\
    \        9.5; no atomic model is adopted as observed evidence.\n      cache_path:\
    \ evidence/PF01042/lambrecht-2012-ridA.txt\n      cache_sha256: 44bebd6b53abf4bf626d60cecda72c21923d7b23dec4a7096b29a11034c9a50c\n\
    \  - edge_id: r105a-decreases-rate-enhancement\n    subject: r105a-in-coupled-assay\n\
    \    predicate: decreases\n    object: product-rate-fold-enhancement\n    mechanism:\
    \ R105A gives less coupled product-rate enhancement than WT and is the lowest\
    \ of the tested\n      variants. This does not make all residual activity zero\
    \ or directly demonstrate an imine-binding\n      pose.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:22094463\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3270999/\n\
    \      snippet: all four variants were defective\n      explanation: Figure 6\
    \ gray R105A and WT bars support the decrease. The source notes residual enhancement\n\
    \        and burst kinetics, which qualify an essential-catalyst interpretation.\n\
    \      cache_path: evidence/PF01042/lambrecht-2012-ridA.txt\n      cache_sha256:\
    \ 44bebd6b53abf4bf626d60cecda72c21923d7b23dec4a7096b29a11034c9a50c\n  - edge_id:\
    \ e120k-decreases-rate-enhancement\n    subject: e120k-in-coupled-assay\n    predicate:\
    \ decreases\n    object: product-rate-fold-enhancement\n    mechanism: E120K lowers\
    \ the enhancement relative to WT at pH 9.5 while retaining activity. The perturbation\n\
    \      effect does not directly identify general acid/base chemistry or water\
    \ orientation.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:22094463\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC3270999/\n      snippet: all four variants\
    \ were defective\n      explanation: Figure 6 gray E120K and WT bars are the adopted\
    \ comparison; distinct pH 8 measurements\n        remain separate.\n      cache_path:\
    \ evidence/PF01042/lambrecht-2012-ridA.txt\n      cache_sha256: 44bebd6b53abf4bf626d60cecda72c21923d7b23dec4a7096b29a11034c9a50c\n\
    \  - edge_id: e120a-decreases-rate-enhancement\n    subject: e120a-in-coupled-assay\n\
    \    predicate: decreases\n    object: product-rate-fold-enhancement\n    mechanism:\
    \ E120A lowers the enhancement relative to WT at pH 9.5 but remains above IlvA\
    \ alone. A measured\n      substitution effect is not a direct view of an elementary\
    \ catalytic step.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:22094463\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC3270999/\n      snippet: all four variants\
    \ were defective\n      explanation: Figure 6 gray E120A and WT bars support this\
    \ decrease with retained activity.\n      cache_path: evidence/PF01042/lambrecht-2012-ridA.txt\n\
    \      cache_sha256: 44bebd6b53abf4bf626d60cecda72c21923d7b23dec4a7096b29a11034c9a50c\n\
    - graph_id: rida-ilva-serine-product-rate\n  title: RidA increases pyruvate formation\
    \ in the coupled IlvA and serine assay\n  scope: Tagged Salmonella RidA/IlvA in\
    \ the 2012 Figure 7 serine-substrate experiment, not the threonine\n    assay\
    \ or a stand-alone RidA dehydratase.\n  context: Serine concentration series at\
    \ pH 9.5, 0.9 uM IlvA, 1.6 uM RidA when present, 10 uM PLP, 50\n    mM each TAPS/CHES/CAPS,\
    \ 200 uL, 22 C. A230 rates use 30-60 s. Two replicates with SE, representative\n\
    \    of three independent experiments. No precise plotted rate was digitized.\n\
    \  family_mapping: LT2 reference RidA Q7CP78 sequence version 1 contains PF01042\
    \ at 7-126, with exact UniProt/InterPro\n    sequence agreement. The intact protein\
    \ and IlvA P20506 are the mapped coupled system; full clone junctions\n    remain\
    \ unverified.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:99287\n  limitations:\
    \ The endpoint supports enhanced product formation in a coupled assay. The corresponding\n\
    \    reactive metabolite, hydrolysis sequence and proposed catalytic water geometry\
    \ are not directly observed\n    by A230. Results are not transferred to all family\
    \ members or mammalian RNase function.\n  nodes:\n  - node_id: rida-added-to-ilva-serine\n\
    \    label: RidA added to IlvA, serine and PLP\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q7CP78\n    - UniProtKB:P20506\n  - node_id:\
    \ pyruvate-initial-rate\n    label: Initial rate of pyruvate formation\n    node_type:\
    \ ACTIVITY\n  edges:\n  - edge_id: rida-increases-serine-product-rate\n    subject:\
    \ rida-added-to-ilva-serine\n    predicate: increases\n    object: pyruvate-initial-rate\n\
    \    mechanism: Adding RidA increases pyruvate production rate across the measured\
    \ serine series compared\n      with IlvA without RidA. This observed coupled\
    \ output does not independently make RidA sufficient\n      for serine dehydration.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:22094463\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3270999/\n\
    \      snippet: rate of pyruvate formation was 2.2-fold faster\n      explanation:\
    \ Figure 7 and the serine Results support the direction. The quoted prose includes\
    \ a\n        particular comparison, but the graph does not digitize rates or impose\
    \ that fold change across\n        concentrations.\n      cache_path: evidence/PF01042/lambrecht-2012-ridA.txt\n\
    \      cache_sha256: 44bebd6b53abf4bf626d60cecda72c21923d7b23dec4a7096b29a11034c9a50c\n\
    - graph_id: rida-retained-ilve-activity\n  title: RidA increases retained IlvE\
    \ activity in an IlvA and serine mixture\n  scope: The Salmonella RidA comparison\
    \ in the 2013 Figure 1B radioactive IlvE assay. Other species' homologs\n    and\
    \ cellular extracts are not this graph.\n  context: 50 mM potassium phosphate\
    \ pH 9, 50 uM PLP, 12.5 mM 2-ketoglutarate, 0.75 ug IlvE, 10 ug IlvA,\n    50\
    \ mM serine and 16 ug RidA where indicated. Methods list these mixtures preincubated\
    \ 2 h at 37 C,\n    then 5 mM radiolabeled isoleucine (20 nCi) for 15 min at 37\
    \ C. TLC-resolved 2-keto-3-methylvalerate\n    reports IlvE specific activity.\
    \ Two replicates with ranges, independently repeated at least twice.\n  family_mapping:\
    \ Intact LT2 RidA Q7CP78 sequence version 1 contains PF01042 residues 7-126. IlvA\
    \ P20506\n    and IlvE P0A1A5 are LT2 reference mappings. IlvE carries a C-terminal\
    \ His6 tag and was produced in\n    SB300A1-derived Salmonella strains; RidA/IlvA\
    \ purification cites earlier procedures. Complete clones\n    remain unverified.\n\
    \  scope_status: MECHANISTIC\n  taxon: NCBITaxon:99287\n  limitations: Figure\
    \ 1B caption wording places RidA addition after preincubation, whereas Methods\
    \ include\n    it in the preincubation mixture and Results interpret protection.\
    \ The graph adopts the endpoint comparison,\n    not reversal of pre-existing\
    \ damage. The separate 3-chloroalanine assay is not an identical control.\n  \
    \  Adduct identity, nucleophilic site and raw MS were not independently resolved.\n\
    \  nodes:\n  - node_id: rida-in-ilve-ilva-serine-assay\n    label: Salmonella\
    \ RidA included in the IlvE, IlvA and serine condition\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q7CP78\n    - UniProtKB:P20506\n    - UniProtKB:P0A1A5\n\
    \  - node_id: retained-ilve-specific-activity\n    label: Retained IlvE specific\
    \ activity measured by radiolabeled keto-acid formation\n    node_type: ACTIVITY\n\
    \  edges:\n  - edge_id: rida-increases-retained-ilve-activity\n    subject: rida-in-ilve-ilva-serine-assay\n\
    \    predicate: increases\n    object: retained-ilve-specific-activity\n    mechanism:\
    \ The RidA-containing IlvA/serine mixture retains more IlvE activity than the\
    \ matched inhibited\n      mixture without RidA. This does not uniquely distinguish\
    \ prevention from reversal given the source's\n      addition-order ambiguity,\
    \ or directly observe an adduct-removal mechanism.\n    directness: DIRECT\n \
    \   support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:23386433\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3565831/\n\
    \      snippet: dramatically decreased the negative effect\n      explanation:\
    \ Figure 1B Salmonella bar, Results and radioactive Methods establish the retained-activity\n\
    \        comparison. The caption/Methods order discrepancy is explicitly retained\
    \ rather than interpreted\n        as proven repair.\n      cache_path: evidence/PF01042/lambrecht-2013-ridA.txt\n\
    \      cache_sha256: 7a4b26847f592333f017c826611c5e001984b6b5ab591d2ed4a0516ab20c80c2\n\
    curation_events:\n- timestamp: '2026-10-11T08:44:50Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Add scoped RidA coupled-biochemical causal\
    \ graphs\n  history_record: history/records/PF01042/2026-10-11T084450Z-codex-599147.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: LT2 RidA Q7CP78, ridA/yjgF/STM4458, 128 residues and sequence version 1,
    exactly matches the InterPro reference and maps PF01042 to 7-126 inclusive. Adopted
    substitution positions were directly checked. IlvA P20506 and IlvE P0A1A5 provide
    LT2 partner references, not verification of every experimental clone. C-terminal
    tags and distinct production hosts are stated; an E. coli production host does
    not change donor identity or assign mammalian RNase function.
  target_ids:
  - PF01042
  evidence_ids:
  - identity
  - primary
  - retained-ilve-activity
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: The graphs retain directly measured biochemical endpoints in explicitly
    coupled systems, not independent sufficiency of RidA, PLP or substrate. Ferricyanide
    and product yield are correlated outputs from one experiment, not independent
    replication. Figure 6 substitutions constrain activity without uniquely proving
    chemical roles. Figure 1B of 2013 supports retained IlvE activity despite caption/Methods
    disagreement on RidA addition order, so no repair/reversal edge is adopted. No
    whole-family generalization or frozen-label replacement is made.
  target_ids:
  - PF01042
  evidence_ids:
  - primary
  - native
  - retained-ilve-activity
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Complete clone junctions and the earlier purification paper, exact ferricyanide
    endpoint temperature, reconciliation of IlvE addition order and modified-peptide
    identity remain unresolved. Raw kinetic and MS data were not reanalyzed. Other
    RidA homologs, cellular phenotypes, additional biochemical substrates and the
    family label's RNase context need separately mapped primary curation. These five
    graphs are not complete family coverage.
  target_ids:
  - PF01042
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01042-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve RidA assay metadata and extend member-specific chemical coverage
  description: Obtain complete clone and purification details, resolve the two-hour
    endpoint temperature and IlvE addition order, and assess adduct evidence without
    inventing a modified site. Curate other homologs and cellular contexts separately
    with their own identity and causal support, preserving uncertainty and appending
    a successor review before status promotion.
  target_ids:
  - PF01042
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - retained-ilve-activity
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01042.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Obtain complete clone and purification details, resolve the two-hour
    endpoint temperature and IlvE addition order, and assess adduct evidence without
    inventing a modified site. Curate other homologs and cellular contexts separately
    with their own identity and causal support, preserving uncertainty and appending
    a successor review before status promotion.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01042
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Lambrecht 2012 Figures 2/4/6/7 and Lambrecht 2013 Figure 1 were visually inspected.
  Relevant Methods and Results were read, with the 2012 Discussion and 2013 mechanism
  qualifications considered. No raw kinetics, replicate gels, MS reanalysis or complete
  historical construct reconstruction was performed. The 2012 model figure is not
  adopted as an observed trajectory.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
