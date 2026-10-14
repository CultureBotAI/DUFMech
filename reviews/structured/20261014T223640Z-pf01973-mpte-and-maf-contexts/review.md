# PF01973 archaeal MptE chemistry and AMB-1 Maf phenotypes

- Review: 20261014T223640Z-pf01973-mpte-and-maf-contexts
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-14T22:34:24Z
- Finished UTC: 2026-10-14T22:36:40Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Partial scientific review of eight graphs containing fourteen observed effects and two explicit computational hypotheses. Archaeal whole-protein assays, heterologous complementation, bacterial deletion/rescue, residue substitutions and proposed chemistry remain separate. Later member contexts and unresolved molecular attribution remain open; IN_PROGRESS is retained.

## Scope And Provenance

Inspect primary MptE2012 Methods, Figure 4 and supporting purity gel; Maf2018 author manuscript, original Figures 1/5/S1/S4/S7 and Table S2; map three exact reference proteins; challenge relation direction, controls, residue numbering, profile boundaries and unsupported transfer.

Selection: Next ascending uncurated family PF01973 after PF01972 within the unchanged 8296-family goal; no claim to exhaust the selected family.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c6a4d055de0a9ef0edc74f5c61cbbacfd8822904.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01973 | data/families/PF01973.yaml | generated | PF01973 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and source preservation | passed | True | PF01973 | Native record validation, exact overlay equality, evidence hashes/quotations, eight graphs/sixteen edges, frozen-field preservation and unchanged unrelated projection/source paths passed. |
| Native causal graph and QC regression tests | passed | True | PF01973 | 52 tests passed in 35.34 seconds. Structural tests do not prove biological causality. |
| Whole-corpus guarded generation | passed | True | PF01973 | Each record-generation pass validated 8296 records and found two changed generated paths; apply succeeded. Schema-only check found zero generated differences. These were separate executed commands, not a fabricated combined run. |

## Scientific And Domain Assessments

### Family identity, protein mapping and coordinate definitions

identity: supported. Targets: PF01973.

Frozen DUF115/MAF_flag10 history and member-specific mappings support relevance. Different substrates, terminal domains and structural/profile boundaries remain explicit; the N494A caption inconsistency is not propagated as a verified variant.

### Observed biochemical and cellular effects

graph: supported. Targets: PF01973.

Two direct whole-protein reaction edges and twelve cellular effects are scoped to their actual proteins and perturbations. Maf bands, supernatant detection, filaments and qualitative motility are not collapsed into an observed molecular pathway. Rescue remains conditional on the host background.

### Residue chemistry remains computationally proposed

graph: supported. Targets: PF01973.

Glu324 catalytic-base and Asp415 donor-pocket roles are HYPOTHESIZED/COMPUTATIONAL/UNRESOLVED. Noncomplementation, sulfate placement and homology do not resolve acid/base chemistry or donor binding. Tolerated substitutions remain condition-specific negative results in the gap ledger.

### Additional members and discriminating molecular experiments

completeness: concern. Targets: PF01973.

Exact constructs, archaeal native-substrate scope, Maf variant controls and later specificity systems remain unassessed or unresolved. Eight graphs do not constitute full family or corpus review.

## Findings

### mpte-contexts: Resolve archaeal constructs and extend native biochemical context

minor / open / confirmed; issue key: pf01973-mpte-mechanistic-coverage.

Trace PF0930 expression/purification and historical constructs, reconcile heat-treatment wording, inspect later MJ1634 work and test or retain limits on native substrate/flux and catalytic residues. Do not infer kinase activity for Maf members.

### maf-contexts: Discriminate Maf residue roles and extend individually mapped member systems

minor / open / confirmed; issue key: pf01973-maf-mechanism-and-member-coverage.

Assess matched variant abundance/folding, purified chemistry and donor/acceptor identity; inspect later Maf/GlfM specificity, engineered substrates and other bacterial contexts with exact mappings. Maintain the N491A control, boundary definitions and glycan stereochemical uncertainty.

## Recommended Actions And Acceptance Checks

### extend-member-mechanisms

Continue the primary-source queue and add only verified member-specific mechanisms, with a successor review recording the disposition of these findings.

- Additional graphs resolve exact tested proteins, constructs, coordinates, partners and experimental context.
- New molecular claims have discriminating evidence beyond mutation phenotype or docking; incompatible taxa and donor substrates are not merged.
- Negative results, missing controls and access limits stay explicit; native checks pass without status inflation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| mpte | https://doi.org/10.1021/cb300342u; Europe PMC XML Results and Methods 3.3-3.6/3.8-3.9; original Figure 4B/D and supplemental Figure 4 page 9 | supports | PF0930 product identification and controls, reported similar MJ1634 chemistry, and distinct E. coli folK complementation support three scoped edges. Displayed PF0930 data are not relabeled as an independent MJ1634 trace. |
| maf | https://hal.science/hal-01802950v1/file/sulzenbacher-etal-2017-HAL.pdf; Results/Methods, original Figures 1/5/S1/S4/S7, Table S2; PDF pages 7-25,29-30,31,35-36,39,42,44 | supports | Whole-gene deletion/rescue and separate E324A/D415A variants support cellular readouts. Docking-based Glu324/Asp415 roles remain hypotheses; glycan stereochemistry, variant abundance/folding and direct donor chemistry remain unresolved. |
| mapping | evidence/PF01973/member-mapping.txt; UniProt Q59028/Q8U2A9/Q2W9I6 and individual InterPro PF01973 mappings; frozen previous-name row | supports | Reference profiles are respectively 32-196/241aa,37-183/231aa and259-419/666aa. Maf structural273-530 is not the profile interval. Native E324/D415 and N491/D494 identities were verified; full historical plasmids are not reconstructed. |
| coverage | evidence/PF01973/coverage-and-exclusions.txt; Completed-source boundary, later-member queue, access/retrieval outcomes and excluded comparisons | context_only | Later Aeromonas, Shewanella/GlfM, Clostridium, Campylobacter and Helicobacter contexts remain open. MJ0408 aldolase and structurally related comparison proteins do not establish PF01973 mechanism. A browser challenge was not treated as negative evidence. |
| native | src/dufmech/records.py; Successful native generation, schema check, focused tests and temporary PF01973 structural/source-preservation assertions | supports | Only PF01973 and its projection manifest change among generated family paths. All prior imported fields, snapshots, canonical Pages and source pins are unchanged. Validation does not establish family completeness. |
| duf-projection-pf01973 | data/families/PF01973.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Same-agent partial scientific review, not independent expert approval, raw-data reanalysis or experimental replication.
- Maf2018 does not resolve exact glycan stereochemistry or mutant folding/abundance; MJ1634 chemistry is reported without a separately displayed trace.
- All earlier family findings and the remaining 8296-family objective stay active. No publication or full QC pass is claimed by this review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T223640Z-pf01973-mpte-and-maf-contexts
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: c6a4d055de0a9ef0edc74f5c61cbbacfd8822904
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01973.yaml
    sha256: 4c1e8d7477449e3df78434fa95769716be29edecf5cc016222d22ced0845123c
    role: context
  - path: data/families/PF01973.yaml
    sha256: 05157e95b8c110847e7c236a2ea43bea351454fdfa7bdc05e2a7dd5413abe7c3
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
  - path: evidence/PF01973/coverage-and-exclusions.txt
    role: context
    sha256: e8dfb09903c1b9c048feb162607bf73b70e1345f6f39a44aab93d2edcf694f54
  - path: evidence/PF01973/crecy-2012-mpte.txt
    role: context
    sha256: 601d231b6582bd80d75b93e37b0302e9364aacdf550993699782873891ce1492
  - path: evidence/PF01973/member-mapping.txt
    role: context
    sha256: 4391c8d7b3988527c816d37bc1101a4aea43562a283610afd7260a506ceeaada
  - path: evidence/PF01973/sulzenbacher-2018-maf.txt
    role: context
    sha256: d386fe9982f5703ceec75be5306af2e3ddee108f8a9be1fae34bf2b6bc7bb16b
  - path: data/worklists/pfam-previous-unknown-names-2026-10-10.json
    role: context
    sha256: a9f70f265bfe7039f5abf8e8a4545f389b66636edaf8e102c7e1a08ca1c1c10e
  - path: history/records/PF01973/2026-10-14T222220Z-codex-7efd01.yaml
    role: context
    sha256: 9a43d8d2a7bedb3447573ff233d7977ab94f32b9793de595ec74da82e0d13312
targets:
- target_id: PF01973
  path: data/families/PF01973.yaml
  label: PF01973
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01973.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 89129c238d759cb285e3ced3ca846405d18880302487db6e310c423ad29421bc
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
title: PF01973 archaeal MptE chemistry and AMB-1 Maf phenotypes
started_at: '2026-10-14T22:34:24Z'
finished_at: '2026-10-14T22:36:40Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: The same agent researched, curated and challenged these graphs;
    no independent scientific approval is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: true
summary: Partial scientific review of eight graphs containing fourteen observed effects
  and two explicit computational hypotheses. Archaeal whole-protein assays, heterologous
  complementation, bacterial deletion/rescue, residue substitutions and proposed chemistry
  remain separate. Later member contexts and unresolved molecular attribution remain
  open; IN_PROGRESS is retained.
scope:
  description: Inspect primary MptE2012 Methods, Figure 4 and supporting purity gel;
    Maf2018 author manuscript, original Figures 1/5/S1/S4/S7 and Table S2; map three
    exact reference proteins; challenge relation direction, controls, residue numbering,
    profile boundaries and unsupported transfer.
  selection: Next ascending uncurated family PF01973 after PF01972 within the unchanged
    8296-family goal; no claim to exhaust the selected family.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01973
  exclusions:
  - target: Later Maf specificity and glycoengineering studies and other bacterial
      members
    reason: Primary leads are retained, but their full experiments and construct/domain
      mappings are not yet assessed. Clostridium2024 XML retrieval and identity verification
      do not constitute scientific review.
  - target: Native archaeal flux, residue chemistry and exact historical plasmid sequences
    reason: The inspected assays do not establish these claims; PF0930 protocol tracing
      and later structural/biochemical work remain necessary.
  - target: Independent review, experimental replication and canonical publication
    reason: This is local same-agent curation; no source-pin refresh, publication
      QC, push or full-corpus completion is implied.
checks:
- check_id: native-projection
  name: Native projection and source preservation
  command: PYTHONPATH=src .venv/bin/python /private/tmp/duf-pf01973-check.py
  status: passed
  required: true
  exit_code: 0
  summary: Native record validation, exact overlay equality, evidence hashes/quotations,
    eight graphs/sixteen edges, frozen-field preservation and unchanged unrelated
    projection/source paths passed.
  target_ids:
  - PF01973
  evidence_ids:
  - native
- check_id: regressions
  name: Native causal graph and QC regression tests
  command: PYTHONPATH=src:/private/tmp/dufmech-protein-claw/src .venv/bin/python -m
    pytest -q tests/test_causal_graphs.py tests/test_qc.py
  status: passed
  required: true
  exit_code: 0
  summary: 52 tests passed in 35.34 seconds. Structural tests do not prove biological
    causality.
  target_ids:
  - PF01973
  evidence_ids:
  - native
- check_id: guarded-generation
  name: Whole-corpus guarded generation
  command: just records; just records --apply; just validate-schema
  status: passed
  required: true
  exit_code: 0
  summary: Each record-generation pass validated 8296 records and found two changed
    generated paths; apply succeeded. Schema-only check found zero generated differences.
    These were separate executed commands, not a fabricated combined run.
  target_ids:
  - PF01973
  evidence_ids:
  - native
evidence:
- evidence_id: mpte
  kind: primary_source
  reference: https://doi.org/10.1021/cb300342u
  locator: Europe PMC XML Results and Methods 3.3-3.6/3.8-3.9; original Figure 4B/D
    and supplemental Figure 4 page 9
  accessed_at: '2026-10-14T22:36:40Z'
  support: supports
  summary: PF0930 product identification and controls, reported similar MJ1634 chemistry,
    and distinct E. coli folK complementation support three scoped edges. Displayed
    PF0930 data are not relabeled as an independent MJ1634 trace.
  snapshot_sha256: 601d231b6582bd80d75b93e37b0302e9364aacdf550993699782873891ce1492
- evidence_id: maf
  kind: primary_source
  reference: https://hal.science/hal-01802950v1/file/sulzenbacher-etal-2017-HAL.pdf
  locator: Results/Methods, original Figures 1/5/S1/S4/S7, Table S2; PDF pages 7-25,29-30,31,35-36,39,42,44
  accessed_at: '2026-10-14T22:36:40Z'
  support: supports
  summary: Whole-gene deletion/rescue and separate E324A/D415A variants support cellular
    readouts. Docking-based Glu324/Asp415 roles remain hypotheses; glycan stereochemistry,
    variant abundance/folding and direct donor chemistry remain unresolved.
  snapshot_sha256: d386fe9982f5703ceec75be5306af2e3ddee108f8a9be1fae34bf2b6bc7bb16b
- evidence_id: mapping
  kind: database
  reference: evidence/PF01973/member-mapping.txt
  locator: UniProt Q59028/Q8U2A9/Q2W9I6 and individual InterPro PF01973 mappings;
    frozen previous-name row
  accessed_at: '2026-10-14T22:36:40Z'
  support: supports
  summary: Reference profiles are respectively 32-196/241aa,37-183/231aa and259-419/666aa.
    Maf structural273-530 is not the profile interval. Native E324/D415 and N491/D494
    identities were verified; full historical plasmids are not reconstructed.
  snapshot_sha256: 4391c8d7b3988527c816d37bc1101a4aea43562a283610afd7260a506ceeaada
- evidence_id: coverage
  kind: search
  reference: evidence/PF01973/coverage-and-exclusions.txt
  search_scope: PF01973, DUF115, MAF_flag10, MptE, MJ1634, PF0930, amb0685 and exact-title
    follow-up searches; primary repositories/Europe PMC and UniProt/InterPro. Local
    rg --no-ignore --hidden in curation, evidence, history/records and reviews/structured
    included ignored and hidden files. Not an exhaustive literature census.
  locator: Completed-source boundary, later-member queue, access/retrieval outcomes
    and excluded comparisons
  accessed_at: '2026-10-14T22:36:40Z'
  support: context_only
  summary: Later Aeromonas, Shewanella/GlfM, Clostridium, Campylobacter and Helicobacter
    contexts remain open. MJ0408 aldolase and structurally related comparison proteins
    do not establish PF01973 mechanism. A browser challenge was not treated as negative
    evidence.
  snapshot_sha256: e8dfb09903c1b9c048feb162607bf73b70e1345f6f39a44aab93d2edcf694f54
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Successful native generation, schema check, focused tests and temporary
    PF01973 structural/source-preservation assertions
  accessed_at: '2026-10-14T22:36:40Z'
  support: supports
  summary: Only PF01973 and its projection manifest change among generated family
    paths. All prior imported fields, snapshots, canonical Pages and source pins are
    unchanged. Validation does not establish family completeness.
- evidence_id: duf-projection-pf01973
  kind: record_content
  reference: data/families/PF01973.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-14T22:36:40Z'
  support: context_only
  snapshot_sha256: 05157e95b8c110847e7c236a2ea43bea351454fdfa7bdc05e2a7dd5413abe7c3
  quote: "id: Pfam:PF01973\npfam_id: PF01973\nname: 6-hydroxymethylpterin diphosphokinase\
    \ MptE-like\nshort_name: MptE-like\nseed_status: EX_DUF\ncharacterization_status:\
    \ UNSCORED\ncuration_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01973\n\
    counters:\n  proteins: 3321\n  matches: 3325\n  proteomes: 2320\n  taxa: 4154\n\
    \  structures: 3\n  alphafold_models: 2353\n  domain_architectures: 52\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002826\ndescription: This domain can be found in a group\
    \ of proteins, including archaeal 6-hydroxymethylpterin\n  diphosphokinase (6-HMDPK),\
    \ known as MptE, which catalyses the formation of 6-hydroxymethyl-7,8-dihydropterin\n\
    \  diphosphate (6-HMDP) from 6-HMD and ATP [[cite:PUB00061602]]. 6-HMDP is the\
    \ precursor of the pterin\n  containing moiety of the essential C1-carriers tetrahydrofolate\
    \ and tetrahydromethanopterin. This entry\n  also includes a number of uncharacterised\
    \ proteins from bacteria.\ncuration_history: history/records/PF01973\ndiscussions:\n\
    - discussion_id: mpte-substrates-and-constructs\n  prompt: Resolve archaeal substrate\
    \ breadth, constructs and catalytic steps beyond the reported assays.\n  kind:\
    \ CURATION_TODO\n  status: OPEN\n  rationale: Purified whole-protein reactions\
    \ and heterologous rescue establish bounded activities, not\n    a universal PF01973\
    \ substrate or native archaeal flux.\n  evidence:\n  - reference: PMID:22931285\n\
    \    supports: PARTIAL\n    evidence_source: primary_publication\n    explanation:\
    \ Original Figure 4 and Methods distinguish displayed PF0930 chemistry from reported\
    \ similar\n      MJ1634 activity and E. coli complementation. The supporting purity\
    \ gel concerns MJ1634.\n  posed_by: Codex\n  posed_date: '2026-10-14'\n  notes:\
    \ Trace the cited PF0930 expression protocol and exact constructs, reconcile 70/80\
    \ C purification\n    wording, test natural substrate breadth and catalytic residues,\
    \ and inspect later structural/biochemical\n    work. A monophosphate workup peak\
    \ is not a demonstrated enzyme step. See evidence/PF01973/crecy-2012-mpte.txt.\n\
    - discussion_id: maf-chemistry-versus-phenotypes\n  prompt: Resolve Maf donor\
    \ stereochemistry and distinguish residue chemistry from protein stability or\n\
    \    expression effects.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale:\
    \ Deletion/rescue and E324A/D415A perturbations support cellular effects, but\
    \ do not by themselves\n    demonstrate donor transfer or acid/base catalysis\
    \ by isolated PF01973.\n  evidence:\n  - reference: PMID:29076618\n    supports:\
    \ PARTIAL\n    evidence_source: primary_publication\n    explanation: Figures\
    \ 1/5/S1/S4 and Methods support scoped phenotypes; Figures 4/S7 are structural/docking\n\
    \      proposals. Maf abundance/folding controls and a donor-bound Maf structure\
    \ are not established by\n      those experiments.\n  posed_by: Codex\n  posed_date:\
    \ '2026-10-14'\n  notes: Preserve the S283A/D318A/N491A condition-specific negative\
    \ results. The N494A caption conflicts\n    with Figure 5B, Methods, primers and\
    \ sequence; use N491A for that control, not an invented variant.\n    The paper's\
    \ structural 273-530 interval differs from the current 259-419 Pfam match. Do\
    \ not transfer\n    kinase chemistry to Maf or glycosylation to archaeal MptE.\n\
    - discussion_id: additional-maf-member-contexts\n  prompt: Extend PF01973 coverage\
    \ through individually mapped Maf members and partner-specific experiments.\n\
    \  kind: CURATION_TODO\n  status: OPEN\n  rationale: The founding archaeal and\
    \ AMB-1 experiments do not exhaust later Maf specificity, glycoengineering\n \
    \   and other bacterial contexts.\n  evidence:\n  - reference: doi:10.1002/mbo3.19\n\
    \    supports: PARTIAL\n    evidence_source: primary_publication_lead\n    explanation:\
    \ Aeromonas Maf1 study identified for a separate full-text, construct and domain-mapping\n\
    \      assessment; not used as evidence for the current graphs.\n  - reference:\
    \ https://www.sciencedirect.com/science/article/pii/S0960982224007012\n    supports:\
    \ PARTIAL\n    evidence_source: primary_publication_lead\n    explanation: The\
    \ 2024 multicomponent specificity study remains a full-methods/figure and exact-member\n\
    \      follow-up; publisher access returned 403 in this session.\n  - reference:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC11339370/\n    supports: PARTIAL\n\
    \    evidence_source: primary_publication_lead\n    explanation: Clostridium mini-flagellin\
    \ glycoengineering identified for further assessment; no native-substrate\n  \
    \    or direct catalytic claim is transferred from search metadata.\n  posed_by:\
    \ Codex\n  posed_date: '2026-10-14'\n  notes: Continue the explicit evidence/PF01973/coverage-and-exclusions.txt\
    \ queue, including earlier Aeromonas,\n    Campylobacter, Helicobacter and newer\
    \ studies. Full family review remains incomplete, and all earlier\n    corpus\
    \ follow-ups stay open.\ncausal_graphs:\n- graph_id: pf0930-pterin-diphosphate-2012\n\
    \  title: PF0930 produces pterin diphosphate in a purified-protein assay\n  scope:\
    \ Recombinant P. furiosus PF0930/MptE, mapped to Q8U2A9; whole-protein biochemical\
    \ activity, not\n    isolated-domain sufficiency.\n  context: 3.5 ng enzyme with\
    \ 100 uM 6-HMD and 1 mM ATP in 200 uL containing 8 mM MgCl2, 16 mM DTT and\n \
    \   40 mM TES/KCl pH 7.4; argon, 70 C, 10 minutes. Products detected after iodine\
    \ oxidation.\n  family_mapping: Q8U2A9 sequence 1/entry 94 is the 231-residue\
    \ PF0930 reference; current InterPro PF01973\n    match is 37-183 inclusive. The\
    \ study cloned PF0930 into modified pET24d; exact extra construct residues\n \
    \   remain unverified. See evidence/PF01973/member-mapping.txt.\n  taxon: NCBITaxon:186497\n\
    \  scope_status: MECHANISTIC\n  limitations: Product identity is supported by\
    \ chromatography, optical spectra and desalted MS, but no\n    atomic mechanism,\
    \ native flux or isolated Pfam truncation is tested. CTP/UTP/GTP retain activity,\n\
    \    so ATP is not an exclusive donor. The monophosphate peak's origin is unresolved.\n\
    \  nodes:\n  - node_id: enzyme_substrate_mix\n    label: PF0930 reaction with\
    \ 6-HMD, ATP and Mg2+\n    node_type: PROCESS\n    grounding:\n    - UniProtKB:Q8U2A9\n\
    \  - node_id: pterin_diphosphate\n    label: 6-Hydroxymethyl-7,8-dihydropterin\
    \ diphosphate\n    node_type: STATE\n  edges:\n  - edge_id: pf0930-produces-diphosphate\n\
    \    subject: enzyme_substrate_mix\n    predicate: produces\n    object: pterin_diphosphate\n\
    \    mechanism: Purified PF0930 converts the supplied pterin in the joint reaction\
    \ mixture to the diphosphorylated\n      product. Zero-time, no-enzyme and matched\
    \ nonexpressing-extract MonoQ controls support enzyme attribution;\n      the\
    \ source node does not make any single reagent sufficient.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:22931285\n      source_url: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3500442/fullTextXML\n\
    \      snippet: catalyze the formation of 6-HMDP\n      explanation: Results,\
    \ original Figure 4D and Methods 3.8-3.9; oxidized product matched a standard\n\
    \        and desalted LC-ESI-MS/MRM. The figure displays PF0930, not a separate\
    \ MJ1634 trace.\n      cache_path: evidence/PF01973/crecy-2012-mpte.txt\n    \
    \  cache_sha256: 601d231b6582bd80d75b93e37b0302e9364aacdf550993699782873891ce1492\n\
    - graph_id: mj1634-pterin-diphosphate-2012\n  title: MJ1634 has reported pterin\
    \ diphosphokinase activity\n  scope: Recombinant M. jannaschii MJ1634/MptE, mapped\
    \ to Q59028; the study reports similar biochemical\n    results to PF0930 without\
    \ a separate displayed MJ1634 chromatogram.\n  context: Methods specify MJ1634\
    \ as an alternative enzyme in the same 70 C, 10-minute 6-HMD/ATP/Mg2+\n    assay\
    \ used for PF0930. MJ1634 was expressed using pT7-7 in E. coli BL21-Codon Plus\
    \ (DE3)-RIL and purified\n    by heat treatment and MonoQ.\n  family_mapping:\
    \ Q59028 sequence 1/entry 111 is the 241-residue MJ1634 reference, current PF01973\
    \ interval\n    32-196. The paper identifies NP_248644.1 and sequenced genomic\
    \ clones; no isolated profile fragment\n    was tested. See evidence/PF01973/member-mapping.txt.\n\
    \  taxon: NCBITaxon:243232\n  scope_status: MECHANISTIC\n  limitations: This is\
    \ a reported whole-protein biochemical result, not independent inspection of a\
    \ MJ1634\n    trace, raw kinetics or its own MS series. The original supplementary\
    \ gel identifies MJ1634 fractions\n    and notes CAT contamination in other lanes.\
    \ Results and Methods differ on heat-treatment temperature.\n  nodes:\n  - node_id:\
    \ enzyme_substrate_mix\n    label: MJ1634 reaction with 6-HMD, ATP and Mg2+\n\
    \    node_type: PROCESS\n    grounding:\n    - UniProtKB:Q59028\n  - node_id:\
    \ pterin_diphosphate\n    label: Reported 6-HMD diphosphate product\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: mj1634-produces-diphosphate\n    subject: enzyme_substrate_mix\n\
    \    predicate: produces\n    object: pterin_diphosphate\n    mechanism: The Figure\
    \ 4D caption explicitly extends the biochemical result to MJ1634 and Methods specify\n\
    \      its assay. The edge retains that report without transferring PF0930's displayed\
    \ conversion percentage\n      or claiming resolved catalytic residues.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:22931285\n      source_url: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3500442/fullTextXML\n\
    \      snippet: Similar results were obtained with the MJ1634 protein.\n     \
    \ explanation: Figure 4D caption and Methods 3.4-3.5/3.8; supplementary Figure\
    \ 4 independently documents\n        the MJ1634 preparation, not its reaction\
    \ time course.\n      cache_path: evidence/PF01973/crecy-2012-mpte.txt\n     \
    \ cache_sha256: 601d231b6582bd80d75b93e37b0302e9364aacdf550993699782873891ce1492\n\
    - graph_id: mj1634-folk-complementation-2012\n  title: MJ1634 restores growth\
    \ of an E. coli folK deletion strain\n  scope: M. jannaschii MJ1634 expressed\
    \ in E. coli C600 delta-folK::tetB; heterologous complementation,\n    not a native\
    \ archaeal deletion phenotype.\n  context: pBAD24-derived MJ1634 plasmid; LB with\
    \ appropriate antibiotics, with or without thymidine,\n    incubated 48 hours.\
    \ Rescue is observed without arabinose induction. Empty vector, E. coli folK and\n\
    \    thymidine supplementation are controls.\n  family_mapping: The sequenced\
    \ genomic MJ1634 clone corresponds to Q59028/NP_248644.1; reference protein\n\
    \    is 241 residues with PF01973 at 32-196. The experimental host differs from\
    \ the archaeal reference\n    taxon.\n  scope_status: PHENOTYPIC\n  limitations:\
    \ Growth rescue is an indirect cellular readout. It does not measure native archaeal\
    \ flux,\n    cofactor concentrations, expression-normalized enzyme efficiency\
    \ or the sufficiency of the isolated\n    profile interval.\n  nodes:\n  - node_id:\
    \ mj1634_expression\n    label: MJ1634 expression in the folK-deficient host\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q59028\n  - node_id:\
    \ growth_without_thymidine\n    label: Growth on LB without added thymidine\n\
    \    node_type: PHENOTYPE\n  edges:\n  - edge_id: mj1634-enables-growth\n    subject:\
    \ mj1634_expression\n    predicate: enables\n    object: growth_without_thymidine\n\
    \    mechanism: The archaeal clone restores growth under conditions in which the\
    \ empty-vector folK deletion\n      strain is thymidine dependent. Normal host\
    \ partners remain present; the protein alone is not asserted\n      to synthesize\
    \ the entire cofactor.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:22931285\n      source_url:\
    \ https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3500442/fullTextXML\n  \
    \    snippet: complemented the dT auxotrophy\n      explanation: Genetic-validation\
    \ Results, original Figure 4B and complementation Methods; Figure\n        4A\
    \ concerns the different MJ0408/FolB system and is not this edge.\n      cache_path:\
    \ evidence/PF01973/crecy-2012-mpte.txt\n      cache_sha256: 601d231b6582bd80d75b93e37b0302e9364aacdf550993699782873891ce1492\n\
    - graph_id: amb0685-deletion-2018\n  title: Maf deletion disrupts flagellin maturation\
    \ and motility in AMB-1\n  scope: Whole amb0685/maf deletion in Magnetospirillum\
    \ magneticum AMB-1, currently Paramagnetospirillum\n    magneticum; not a selective\
    \ PF01973 deletion.\n  context: PCR-checked short-linker gene replacement intended\
    \ to minimize polar effects; AMB-1 grown/manipulated\n    in MG medium at 30 C\
    \ under microaerophilic conditions. Wild type and in-trans complementation provide\n\
    \    comparisons.\n  family_mapping: Q2W9I6 sequence 1/entry 87, 666 residues,\
    \ WP_011383128.1; PF01973 at 259-419, with separate\n    PF20157/PF20156 domains.\
    \ The paper's central structural region is 273-530. See evidence/PF01973/member-mapping.txt.\n\
    \  taxon: NCBITaxon:342108\n  scope_status: PHENOTYPIC\n  limitations: Whole-protein\
    \ deletion does not isolate catalytic-domain sufficiency. Loss of detectable\n\
    \    extracellular Fla is not a measured export rate; filament and motility outcomes\
    \ are not proof of a\n    direct molecular link. The glycan remains pseudaminic\
    \ acid or a close derivative, not stereochemically\n    resolved.\n  nodes:\n\
    \  - node_id: maf_deletion\n    label: amb0685/maf deletion\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q2W9I6\n  - node_id: modified_flagellin\n   \
    \ label: Nonulosonic-acid-modified flagellin\n    node_type: STATE\n  - node_id:\
    \ extracellular_flagellin\n    label: Detectable extracellular flagellin\n   \
    \ node_type: PHENOTYPE\n  - node_id: flagellar_filaments\n    label: Visible flagellar\
    \ filaments\n    node_type: PHENOTYPE\n  - node_id: cell_motility\n    label:\
    \ Observed cell motility\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: deletion-reduces-modified-flagellin\n\
    \    subject: maf_deletion\n    predicate: decreases\n    object: modified_flagellin\n\
    \    mechanism: The deletion loses the approximately 70-kDa modified Fla band\
    \ and detected nonulosonic-acid\n      peptide modifications while approximately\
    \ 55-kDa intracellular Fla remains. The mutation therefore\n      affects maturation\
    \ rather than simply abolishing all flagellin production.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:29076618\n      source_url: https://hal.science/hal-01802950v1/file/sulzenbacher-etal-2017-HAL.pdf\n\
    \      snippet: flagellin was still produced\n      explanation: Results and original\
    \ Figure 1G-H plus Figure S4 compare wild type and deletion, including\n     \
    \   the modified and unmodified peptide spectra. No specific donor stereoisomer\
    \ is asserted.\n      cache_path: evidence/PF01973/sulzenbacher-2018-maf.txt\n\
    \      cache_sha256: d386fe9982f5703ceec75be5306af2e3ddee108f8a9be1fae34bf2b6bc7bb16b\n\
    \  - edge_id: deletion-reduces-extracellular-flagellin\n    subject: maf_deletion\n\
    \    predicate: decreases\n    object: extracellular_flagellin\n    mechanism:\
    \ Anti-Fla probing of concentrated culture supernatants detects a wild-type signal\
    \ but none\n      in the deletion preparation. The edge describes detection in\
    \ that assay, without resolving export\n      versus extracellular stability or\
    \ other intermediate causes.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:29076618\n\
    \      source_url: https://hal.science/hal-01802950v1/file/sulzenbacher-etal-2017-HAL.pdf\n\
    \      snippet: flagellin was still produced\n      explanation: Results on HAL\
    \ PDF page 9 and original Figure S1A-B on page 36; retained intracellular\n  \
    \      Fla is the important comparison, not evidence of a measured transport mechanism.\n\
    \      cache_path: evidence/PF01973/sulzenbacher-2018-maf.txt\n      cache_sha256:\
    \ d386fe9982f5703ceec75be5306af2e3ddee108f8a9be1fae34bf2b6bc7bb16b\n  - edge_id:\
    \ deletion-reduces-filaments\n    subject: maf_deletion\n    predicate: decreases\n\
    \    object: flagellar_filaments\n    mechanism: Electron micrographs show a filament\
    \ in wild type and its absence in the maf deletion comparison.\n      This is\
    \ a downstream cellular phenotype; no direct assembly reaction is assigned to\
    \ Maf.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:29076618\n      source_url: https://hal.science/hal-01802950v1/file/sulzenbacher-etal-2017-HAL.pdf\n\
    \      snippet: restored the wild type phenotype\n      explanation: Original\
    \ Figure 1D-E gives the deletion comparison; Figure 1F and Results provide rescue\n\
    \        supporting attribution to maf. The edge does not join glycosylation and\
    \ assembly into an observed\n        molecular chain.\n      cache_path: evidence/PF01973/sulzenbacher-2018-maf.txt\n\
    \      cache_sha256: d386fe9982f5703ceec75be5306af2e3ddee108f8a9be1fae34bf2b6bc7bb16b\n\
    \  - edge_id: deletion-reduces-motility\n    subject: maf_deletion\n    predicate:\
    \ decreases\n    object: cell_motility\n    mechanism: The authors report nonmotile\
    \ deletion cells and recovery after maf complementation. This\n      qualitative\
    \ observation is not a quantified motility rate or proof that every Maf homolog\
    \ controls\n      motility.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:29076618\n\
    \      source_url: https://hal.science/hal-01802950v1/file/sulzenbacher-etal-2017-HAL.pdf\n\
    \      snippet: restored the wild type phenotype\n      explanation: HAL PDF Results\
    \ pages 8-9 explicitly describe deletion and rescue motility; Figure\n       \
    \ 1 shows associated filament phenotypes, not a direct motility measurement.\n\
    \      cache_path: evidence/PF01973/sulzenbacher-2018-maf.txt\n      cache_sha256:\
    \ d386fe9982f5703ceec75be5306af2e3ddee108f8a9be1fae34bf2b6bc7bb16b\n- graph_id:\
    \ amb0685-rescue-2018\n  title: Wild-type Maf restores the AMB-1 deletion phenotypes\n\
    \  scope: In-trans pAK22-maf complementation of the AMB-1 amb0685 deletion; whole-protein\
    \ rescue in its\n    cellular background.\n  context: Wild-type maf cloned into\
    \ replicative pAK22 and introduced by conjugation; MG medium at 30\n    C and\
    \ microaerophilic conditions. Comparisons are parental AMB-1 and its maf deletion.\n\
    \  family_mapping: Q2W9I6/WP_011383128.1 is the 666-residue Maf reference, with\
    \ current PF01973 259-419\n    and terminal PF20157/PF20156 domains. Complementation\
    \ is not restricted to the profile match.\n  taxon: NCBITaxon:342108\n  scope_status:\
    \ PHENOTYPIC\n  limitations: Rescue is conditional on other cellular factors and\
    \ donor availability. No isolated-domain\n    sufficiency, expression-normalized\
    \ catalytic rate, supernatant-rescue assay or fully resolved glycan\n    structure\
    \ is established.\n  nodes:\n  - node_id: wild_type_complement\n    label: Wild-type\
    \ maf supplied to the deletion strain\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q2W9I6\n  - node_id: modified_flagellin\n    label: Approximately\
    \ 70-kDa modified flagellin band\n    node_type: STATE\n  - node_id: flagellar_filaments\n\
    \    label: Visible flagellar filaments\n    node_type: PHENOTYPE\n  - node_id:\
    \ cell_motility\n    label: Observed cell motility\n    node_type: PHENOTYPE\n\
    \  edges:\n  - edge_id: complementation-enables-modified-flagellin\n    subject:\
    \ wild_type_complement\n    predicate: enables\n    object: modified_flagellin\n\
    \    mechanism: Supplying wild-type maf restores the approximately 70-kDa anti-Fla\
    \ band lost in the deletion.\n      The result supports gene-specific restoration\
    \ of maturation, not direct observation of the glycosyl-transfer\n      reaction.\n\
    \    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:29076618\n      source_url: https://hal.science/hal-01802950v1/file/sulzenbacher-etal-2017-HAL.pdf\n\
    \      snippet: restored the wild type phenotype\n      explanation: Results and\
    \ original Figure 1G-I, especially the complemented protein extract in panel\n\
    \        I; Methods describe the wild-type complementation construct.\n      cache_path:\
    \ evidence/PF01973/sulzenbacher-2018-maf.txt\n      cache_sha256: d386fe9982f5703ceec75be5306af2e3ddee108f8a9be1fae34bf2b6bc7bb16b\n\
    \  - edge_id: complementation-enables-filaments\n    subject: wild_type_complement\n\
    \    predicate: enables\n    object: flagellar_filaments\n    mechanism: The complemented\
    \ deletion strain again displays an external flagellar filament. This supports\n\
    \      a downstream rescue phenotype without asserting direct assembly by Maf.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:29076618\n      source_url: https://hal.science/hal-01802950v1/file/sulzenbacher-etal-2017-HAL.pdf\n\
    \      snippet: restored the wild type phenotype\n      explanation: Original\
    \ Figure 1D-F compares parental, deletion and complemented cells by electron\n\
    \        microscopy.\n      cache_path: evidence/PF01973/sulzenbacher-2018-maf.txt\n\
    \      cache_sha256: d386fe9982f5703ceec75be5306af2e3ddee108f8a9be1fae34bf2b6bc7bb16b\n\
    \  - edge_id: complementation-enables-motility\n    subject: wild_type_complement\n\
    \    predicate: enables\n    object: cell_motility\n    mechanism: The text reports\
    \ recovery of cell motility following wild-type maf complementation. The\n   \
    \   causal effect is scoped to the tested deletion background and is not a separately\
    \ quantified rate.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:29076618\n      source_url:\
    \ https://hal.science/hal-01802950v1/file/sulzenbacher-etal-2017-HAL.pdf\n   \
    \   snippet: restored the wild type phenotype\n      explanation: HAL PDF Results\
    \ page 9 and complementation Methods pages 18-19; no supernatant-export\n    \
    \    rescue is added from Figure S1, which has only wild type and deletion.\n\
    \      cache_path: evidence/PF01973/sulzenbacher-2018-maf.txt\n      cache_sha256:\
    \ d386fe9982f5703ceec75be5306af2e3ddee108f8a9be1fae34bf2b6bc7bb16b\n- graph_id:\
    \ amb0685-e324a-2018\n  title: E324A prevents Maf complementation of the tested\
    \ readouts\n  scope: Single E324A substitution in full-length pAK22-maf expressed\
    \ in the AMB-1 maf deletion strain;\n    compared with wild-type complementation.\n\
    \  context: Sequence-verified mutation plasmid; anti-Fla Western and reported\
    \ optical-microscope motility\n    readouts. The tested S283A, D318A and N491A\
    \ constructs retain both readouts under the same study conditions.\n  family_mapping:\
    \ Native Q2W9I6 residue 324 is E and lies within current PF01973 259-419 and the\
    \ paper's\n    structural 273-530 region. No isolated domain or E324A/D415A double\
    \ mutant is implied.\n  taxon: NCBITaxon:342108\n  scope_status: PHENOTYPIC\n\
    \  limitations: Loss of complementation can result from catalytic, folding, abundance\
    \ or localization effects.\n    The mutation experiment does not show matched\
    \ Maf abundance/folding controls; anti-Fla is not an anti-Maf\n    control. General-base\
    \ chemistry remains hypothetical.\n  nodes:\n  - node_id: e324a_variant\n    label:\
    \ E324A Maf complementation construct\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q2W9I6\n  - node_id: modified_flagellin\n    label: Approximately\
    \ 70-kDa anti-Fla band\n    node_type: PHENOTYPE\n  - node_id: restored_motility\n\
    \    label: Motility restored by complementation\n    node_type: PHENOTYPE\n \
    \ edges:\n  - edge_id: e324a-reduces-flagellin-readout\n    subject: e324a_variant\n\
    \    predicate: decreases\n    object: modified_flagellin\n    mechanism: The\
    \ E324A complement lacks the 70-kDa band obtained with wild-type maf and retained\
    \ in\n      the S283A/D318A/N491A comparisons. This records the band phenotype,\
    \ not a measured intrinsic catalytic\n      rate.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:29076618\n      source_url: https://hal.science/hal-01802950v1/file/sulzenbacher-etal-2017-HAL.pdf\n\
    \      snippet: bacterial motility was not restored\n      explanation: Original\
    \ Figure 5B and adjacent Results on HAL page 14 associate E324A with absence\n\
    \        of the glycosylated-Fla band as well as the separately reported motility\
    \ effect.\n      cache_path: evidence/PF01973/sulzenbacher-2018-maf.txt\n    \
    \  cache_sha256: d386fe9982f5703ceec75be5306af2e3ddee108f8a9be1fae34bf2b6bc7bb16b\n\
    \  - edge_id: e324a-reduces-motility-rescue\n    subject: e324a_variant\n    predicate:\
    \ decreases\n    object: restored_motility\n    mechanism: Unlike wild-type maf,\
    \ the E324A construct does not restore the reported motility phenotype.\n    \
    \  This is a downstream cellular effect, not evidence identifying the reaction's\
    \ catalytic base.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:29076618\n      source_url:\
    \ https://hal.science/hal-01802950v1/file/sulzenbacher-etal-2017-HAL.pdf\n   \
    \   snippet: bacterial motility was not restored\n      explanation: Results accompanying\
    \ Figure 5 explicitly describe the E324A complementation outcome;\n        no\
    \ quantitative motility measurement or rate is inferred.\n      cache_path: evidence/PF01973/sulzenbacher-2018-maf.txt\n\
    \      cache_sha256: d386fe9982f5703ceec75be5306af2e3ddee108f8a9be1fae34bf2b6bc7bb16b\n\
    - graph_id: amb0685-d415a-2018\n  title: D415A prevents Maf complementation of\
    \ the tested readouts\n  scope: Single D415A substitution in full-length pAK22-maf\
    \ expressed in the AMB-1 maf deletion strain;\n    distinct from the E324A construct.\n\
    \  context: Sequence-verified mutation plasmid, anti-Fla Western and reported\
    \ optical-microscope motility\n    readouts; wild-type complementation and retained\
    \ S283A/D318A/N491A responses provide comparisons.\n  family_mapping: Native Q2W9I6\
    \ residue 415 is D, within current PF01973 259-419 and structural 273-530.\n \
    \   Current profile boundaries are not experimental truncations.\n  taxon: NCBITaxon:342108\n\
    \  scope_status: PHENOTYPIC\n  limitations: The observed phenotype does not distinguish\
    \ donor-pocket geometry, protein stability, abundance\n    or other indirect effects.\
    \ No Maf donor-binding measurement, matched variant-folding control or isolated-domain\n\
    \    assay is shown in this experiment.\n  nodes:\n  - node_id: d415a_variant\n\
    \    label: D415A Maf complementation construct\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q2W9I6\n  - node_id: modified_flagellin\n   \
    \ label: Approximately 70-kDa anti-Fla band\n    node_type: PHENOTYPE\n  - node_id:\
    \ restored_motility\n    label: Motility restored by complementation\n    node_type:\
    \ PHENOTYPE\n  edges:\n  - edge_id: d415a-reduces-flagellin-readout\n    subject:\
    \ d415a_variant\n    predicate: decreases\n    object: modified_flagellin\n  \
    \  mechanism: D415A complementation lacks the 70-kDa anti-Fla band seen with wild-type\
    \ maf and the study's\n      tolerated substitutions. The experiment does not\
    \ identify why D415A fails to support this maturation\n      readout.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:29076618\n      source_url: https://hal.science/hal-01802950v1/file/sulzenbacher-etal-2017-HAL.pdf\n\
    \      snippet: bacterial motility was not restored\n      explanation: Original\
    \ Figure 5B, its Results and Table S2 identify the D415A single-mutant construct\n\
    \        and its missing band; the shared sentence also describes E324A, not a\
    \ double mutant.\n      cache_path: evidence/PF01973/sulzenbacher-2018-maf.txt\n\
    \      cache_sha256: d386fe9982f5703ceec75be5306af2e3ddee108f8a9be1fae34bf2b6bc7bb16b\n\
    \  - edge_id: d415a-reduces-motility-rescue\n    subject: d415a_variant\n    predicate:\
    \ decreases\n    object: restored_motility\n    mechanism: The D415A construct\
    \ fails to restore the motility phenotype recovered with wild-type maf.\n    \
    \  It remains an indirect cellular effect, not a direct donor-contact or transport\
    \ assay.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:29076618\n      source_url:\
    \ https://hal.science/hal-01802950v1/file/sulzenbacher-etal-2017-HAL.pdf\n   \
    \   snippet: bacterial motility was not restored\n      explanation: Results accompanying\
    \ Figure 5 name D415A among the noncomplementing constructs; Methods\n       \
    \ identify sequence verification and microscopy-based assessment.\n      cache_path:\
    \ evidence/PF01973/sulzenbacher-2018-maf.txt\n      cache_sha256: d386fe9982f5703ceec75be5306af2e3ddee108f8a9be1fae34bf2b6bc7bb16b\n\
    - graph_id: amb0685-proposed-residue-roles-2018\n  title: Proposed Maf catalytic\
    \ and donor-pocket roles remain hypotheses\n  scope: Structural/docking interpretation\
    \ of AMB-1 Maf Glu324 and Asp415; not experimentally resolved\n    chemical steps\
    \ or family-wide residue assignments.\n  context: Maf structure 5MU5 compared\
    \ with C. jejuni Cst-II; CMP-Pse5Ac7Ac is docked, not crystallographically\n \
    \   observed in Maf. Whole-protein mutant phenotypes motivate but do not establish\
    \ the proposed molecular\n    explanation.\n  family_mapping: Q2W9I6 E324/D415\
    \ both map within PF01973 259-419. Cst-II and its residue roles are comparison-system\n\
    \    evidence, not direct demonstrations for this family.\n  taxon: NCBITaxon:342108\n\
    \  scope_status: HYPOTHETICAL\n  limitations: Precise donor stereochemistry, acceptor\
    \ positioning, catalytic-base identity and donor-pocket\n    contacts remain unresolved.\
    \ No direct proton-transfer observation or mutant binding/kinetic dissection\n\
    \    is available in the inspected study. Retain the observed phenotypes in their\
    \ separate graphs.\n  nodes:\n  - node_id: proposed_glu324_role\n    label: Proposed\
    \ Glu324 catalytic-base role in Maf\n    node_type: STATE\n    grounding:\n  \
    \  - UniProtKB:Q2W9I6\n  - node_id: proposed_transfer\n    label: Proposed nonulosonic-acid\
    \ transfer to flagellin\n    node_type: ACTIVITY\n  - node_id: proposed_asp415_role\n\
    \    label: Proposed Asp415 organization of the donor pocket\n    node_type: STATE\n\
    \    grounding:\n    - UniProtKB:Q2W9I6\n  - node_id: proposed_donor_binding\n\
    \    label: Proposed accommodation of the donor nucleotide moiety\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: proposed-glu324-enables-transfer\n    subject:\
    \ proposed_glu324_role\n    predicate: enables\n    object: proposed_transfer\n\
    \    mechanism: The authors propose a catalytic role for Glu324 from its position\
    \ near the modeled reaction\n      center, comparison with sialyltransferases\
    \ and loss of mutant complementation. The general-base\n      assignment is explicitly\
    \ hypothetical.\n    directness: UNRESOLVED\n    support: HYPOTHESIZED\n    evidence_kind:\
    \ COMPUTATIONAL\n    evidence:\n    - reference: PMID:29076618\n      source_url:\
    \ https://hal.science/hal-01802950v1/file/sulzenbacher-etal-2017-HAL.pdf\n   \
    \   snippet: putative catalytic base Glu324\n      explanation: Figures 4/S7,\
    \ docking Methods and Discussion explicitly leave catalytic identity for\n   \
    \     further testing. Sulfate overlap and a noncomplementing variant are not\
    \ observation of this chemical\n        step.\n      cache_path: evidence/PF01973/sulzenbacher-2018-maf.txt\n\
    \      cache_sha256: d386fe9982f5703ceec75be5306af2e3ddee108f8a9be1fae34bf2b6bc7bb16b\n\
    \  - edge_id: proposed-asp415-enables-donor-accommodation\n    subject: proposed_asp415_role\n\
    \    predicate: enables\n    object: proposed_donor_binding\n    mechanism: Asp415\
    \ is proposed to organize a donor-nucleotide binding loop by analogy to Cst-II\
    \ Asp154.\n      This is a structure-based causal hypothesis, not a Maf ligand-binding\
    \ measurement or demonstrated\n      direct contact.\n    directness: UNRESOLVED\n\
    \    support: HYPOTHESIZED\n    evidence_kind: COMPUTATIONAL\n    evidence:\n\
    \    - reference: PMID:29076618\n      source_url: https://hal.science/hal-01802950v1/file/sulzenbacher-etal-2017-HAL.pdf\n\
    \      snippet: Asp415 might exercise the same role\n      explanation: HAL PDF\
    \ Results page 15, adjacent structural comparison and original docking figure;\n\
    \        the D415A cellular phenotype cannot discriminate this proposal from destabilization.\n\
    \      cache_path: evidence/PF01973/sulzenbacher-2018-maf.txt\n      cache_sha256:\
    \ d386fe9982f5703ceec75be5306af2e3ddee108f8a9be1fae34bf2b6bc7bb16b\ncuration_events:\n\
    - timestamp: '2026-10-14T22:22:20Z'\n  curator: Codex\n  action: CREATE\n  outcome:\
    \ changed\n  summary: Curate scoped archaeal MptE and AMB-1 Maf causal graphs\n\
    \  history_record: history/records/PF01973/2026-10-14T222220Z-codex-7efd01.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Family identity, protein mapping and coordinate definitions
  outcome: supported
  target_ids:
  - PF01973
  evidence_ids:
  - mapping
  - mpte
  - maf
  summary: Frozen DUF115/MAF_flag10 history and member-specific mappings support relevance.
    Different substrates, terminal domains and structural/profile boundaries remain
    explicit; the N494A caption inconsistency is not propagated as a verified variant.
- assessment_id: observations
  area: graph
  topic: Observed biochemical and cellular effects
  outcome: supported
  target_ids:
  - PF01973
  evidence_ids:
  - mpte
  - maf
  - native
  summary: Two direct whole-protein reaction edges and twelve cellular effects are
    scoped to their actual proteins and perturbations. Maf bands, supernatant detection,
    filaments and qualitative motility are not collapsed into an observed molecular
    pathway. Rescue remains conditional on the host background.
- assessment_id: hypotheses
  area: graph
  topic: Residue chemistry remains computationally proposed
  outcome: supported
  target_ids:
  - PF01973
  evidence_ids:
  - maf
  - mapping
  summary: Glu324 catalytic-base and Asp415 donor-pocket roles are HYPOTHESIZED/COMPUTATIONAL/UNRESOLVED.
    Noncomplementation, sulfate placement and homology do not resolve acid/base chemistry
    or donor binding. Tolerated substitutions remain condition-specific negative results
    in the gap ledger.
- assessment_id: coverage
  area: completeness
  topic: Additional members and discriminating molecular experiments
  outcome: concern
  target_ids:
  - PF01973
  evidence_ids:
  - mpte
  - maf
  - coverage
  summary: Exact constructs, archaeal native-substrate scope, Maf variant controls
    and later specificity systems remain unassessed or unresolved. Eight graphs do
    not constitute full family or corpus review.
findings:
- finding_id: mpte-contexts
  issue_key: pf01973-mpte-mechanistic-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve archaeal constructs and extend native biochemical context
  description: Trace PF0930 expression/purification and historical constructs, reconcile
    heat-treatment wording, inspect later MJ1634 work and test or retain limits on
    native substrate/flux and catalytic residues. Do not infer kinase activity for
    Maf members.
  target_ids:
  - PF01973
  field_paths:
  - causal_graphs
  - discussions
  evidence_ids:
  - mpte
  - mapping
  - coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01973.yaml
    role: Human-owned scientific overlay; regenerate the projection through the native
      writer.
- finding_id: maf-contexts
  issue_key: pf01973-maf-mechanism-and-member-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Discriminate Maf residue roles and extend individually mapped member systems
  description: Assess matched variant abundance/folding, purified chemistry and donor/acceptor
    identity; inspect later Maf/GlfM specificity, engineered substrates and other
    bacterial contexts with exact mappings. Maintain the N491A control, boundary definitions
    and glycan stereochemical uncertainty.
  target_ids:
  - PF01973
  field_paths:
  - causal_graphs
  - discussions
  evidence_ids:
  - maf
  - mapping
  - coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01973.yaml
    role: Human-owned scientific overlay; regenerate the projection through the native
      writer.
actions:
- action_id: extend-member-mechanisms
  description: Continue the primary-source queue and add only verified member-specific
    mechanisms, with a successor review recording the disposition of these findings.
  finding_ids:
  - mpte-contexts
  - maf-contexts
  target_ids:
  - PF01973
  ownership_note: Edit maintained overlay/evidence, append canonical history and regenerate
    records; do not edit frozen sources or this retained review.
  acceptance_checks:
  - Additional graphs resolve exact tested proteins, constructs, coordinates, partners
    and experimental context.
  - New molecular claims have discriminating evidence beyond mutation phenotype or
    docking; incompatible taxa and donor substrates are not merged.
  - Negative results, missing controls and access limits stay explicit; native checks
    pass without status inflation.
limitations:
- Same-agent partial scientific review, not independent expert approval, raw-data
  reanalysis or experimental replication.
- Maf2018 does not resolve exact glycan stereochemistry or mutant folding/abundance;
  MJ1634 chemistry is reported without a separately displayed trace.
- All earlier family findings and the remaining 8296-family objective stay active.
  No publication or full QC pass is claimed by this review.
tags:
- causal-graphs
- pf01973
- scientific-self-review
- mpte
- maf
```
