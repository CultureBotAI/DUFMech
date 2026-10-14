# Scoped scientific self-review of IspD product formation and mutant assay effects

- Review: 20261011T092759Z-pf01128-ispd-product-and-scoped-mutant-effects
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T09:27:55Z
- Finished UTC: 2026-10-11T09:27:59Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Four graphs retain eleven OBSERVED effects, six DIRECT in purified preparations and five with UNRESOLVED directness in crude extracts. Product identification, CTP isotope trapping, fitted turnover and extract-screen endpoints remain separate. The inspected 2004 full text is a primary proof with unresolved numerical labels; no atomic trajectory or family-wide substrate transfer is asserted. Partial scientific self-review; IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01128 IspD, the next accession-ordered SEEDED family, using Rohdich 1999 and Richard 2004 primary evidence with exact current member mapping.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01128 | data/families/PF01128.yaml | generated | PF01128 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01128 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01128.

Q46893 ISPD_ECOLI is a 236-aa K12 reference, sequence version 3, with PF01128 at 8-229. UniProt, InterPro and 1I52 entity 1 canonical sequences match exactly; adopted mutation sites fall within the domain. The 1999 primer's MATTHL translation matches the current start. Initiator removal and later His8-tag cleavage are distinct preparation histories; exact donor strain, complete clones and cleavage remnant remain unverified. Frozen family identity is preserved.

### Directed effects and limits

graph: supported. Targets: PF01128.

One preparative product edge and one qualitative CTP-pulse effect are separate from four reported purified CTP-series turnover decreases. K27S, D106E, T140V and R109A retain fitting, unsaturation and uncertainty qualifications. Five inactive crude-extract variants are explicitly not purified enzymes, with OBSERVED support but UNRESOLVED directness because folding, expression and background activity can contribute. The proof's percent-axis, duration, mass/concentration and T104V/T140V conflicts are not silently repaired. Structural contacts and ordered-binding interpretation are not directly observed atomic steps.

### Remaining family coverage

completeness: concern. Targets: PF01128.

Final publisher tables/figures were not compared with the accessible proof. Complete historical constructs, numerical-label reconciliation, final kinetic-assay pH, mutant-normalization and folded-protein controls remain incomplete. Other inhibition, cellular and distinct-member contexts, including mapped TarI or CRPPA candidates, require separate primary assessment. The current work is not complete family characterization.

## Findings

### additional-contexts: Reconcile IspD proof and construct details before expanding mechanism claims

minor / open / confirmed; issue key: pf01128-causal-context-coverage.

Compare final publication figures and tables, resolve isotope-axis and concentration discrepancies and exact clones, and obtain clearer inactive-mutant normalization/folding evidence. Curate remaining member-specific substrate and cellular contexts separately, without transferring E. coli specificity or elevating crude-extract loss to an elementary catalytic defect. Retain a successor review before strengthening status.

## Recommended Actions And Acceptance Checks

### extend-contexts

Compare final publication figures and tables, resolve isotope-axis and concentration discrepancies and exact clones, and obtain clearer inactive-mutant normalization/folding evidence. Curate remaining member-specific substrate and cellular contexts separately, without transferring E. coli specificity or elevating crude-extract loss to an elementary catalytic defect. Retain a successor review before strengthening status.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC18359/; Preparation, expression, purification and product-identification Methods/Results; Tables 1-3; Figures 3 and 4 visually inspected | supports | Purified recombinant YgbP with MEP, CTP and magnesium yields HPLC-isolated CDP-ME supported by reported NMR identity. The preparative endpoint is separate from partial-preparation nucleotide promiscuity, coupled-assay substrate screens and chromoplast labeling, none of which supplies a fully resolved bacterial causal chain. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q46893/entry/pfam/PF01128/; Accession and domain locations; paired UniProt identity facts | supports | Q46893 ISPD_ECOLI is a 236-aa K12 reference, sequence version 3, with PF01128 at 8-229. UniProt, InterPro and 1I52 entity 1 canonical sequences match exactly; adopted mutation sites fall within the domain. The 1999 primer's MATTHL translation matches the current start. Initiator removal and later His8-tag cleavage are distinct preparation histories; exact donor strain, complete clones and cleavage remnant remain unverified. Frozen family identity is preserved. |
| primary-proof-kinetics | https://citeseerx.ist.psu.edu/document?doi=47f611b82af525a30852494febee3418127613b0&amp;repid=rep1&amp;type=pdf; Primary proof pages C-F; preparation and assay Methods, Figure 3 pulse controls, Figure 4 gel, Table 1 and Figure 5 | supports | Supports a qualitative CTP pulse advantage, four purified CTP-series turnover decreases and five crude-extract screening effects with unresolved directness. Lettered proof pages and placeholder publication fields identify version limits. Corrected fitted parameters, excluded outliers and contradictory labels are retained rather than averaged or silently repaired. |
| construct-reference-sequence | https://data.rcsb.org/rest/v1/core/polymer_entity/1I52/1; Entity 1 canonical sequence and UniProt alignment | supports | The 236-aa canonical sequence exactly matches current Q46893 and confirms adopted residue numbering. It does not independently reconstruct every plasmid or proteolytic junction used in 1999 or 2004. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01128 | data/families/PF01128.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Rohdich 1999 main Methods/Results/Discussion and Tables 1-3 were read; Figures 3/4 were visually inspected. Richard 2004 proof pages A-H were read, with Figure 3/4 page E and Table 1/Figure 5 page F visually checked. The final publication and last reference-only proof page were not inspected; raw NMR, original kinetic data and complete clone sequences were not reanalyzed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T092759Z-pf01128-ispd-product-and-scoped-mutant-effects
title: Scoped scientific self-review of IspD product formation and mutant assay effects
started_at: '2026-10-11T09:27:55Z'
finished_at: '2026-10-11T09:27:59Z'
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
summary: Four graphs retain eleven OBSERVED effects, six DIRECT in purified preparations
  and five with UNRESOLVED directness in crude extracts. Product identification, CTP
  isotope trapping, fitted turnover and extract-screen endpoints remain separate.
  The inspected 2004 full text is a primary proof with unresolved numerical labels;
  no atomic trajectory or family-wide substrate transfer is asserted. Partial scientific
  self-review; IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01128.yaml
    sha256: fe15bc9abc1eaa8a0b5f910893255b230ee9d360ab3fd9a39ced5d0a0e9abe74
    role: context
  - path: data/families/PF01128.yaml
    sha256: 5feda7758b18dd10408039c02927b7a3b5b3dd141e2716659b4820ee24311bff
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
  - path: evidence/PF01128/rohdich-1999-ispd.txt
    role: context
    sha256: 30a287239edc75e2aa4838681065664ae9f2cd13ca656befa3454fac25eeeef1
  - path: evidence/PF01128/IspD-identity.txt
    role: context
    sha256: a02e6feca30c822186777b5cd6b3419da37fc9dd06539b73be40ce492d523b07
  - path: evidence/PF01128/richard-2004-ispd-proof.txt
    role: context
    sha256: b48884494a3641c9bee9e06af20c71df5694405999736b49512da1f06fb4783b
targets:
- target_id: PF01128
  path: data/families/PF01128.yaml
  label: PF01128
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01128.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 085897eeec3c607ecb9a76e4aac99bc590f87fcb77fc7326b0d3715792314bf2
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01128 IspD, the next accession-ordered SEEDED family, using Rohdich
    1999 and Richard 2004 primary evidence with exact current member mapping.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01128
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Final publisher tables/figures were not compared with the accessible proof.
      Complete historical constructs, numerical-label reconciliation, final kinetic-assay
      pH, mutant-normalization and folded-protein controls remain incomplete. Other
      inhibition, cellular and distinct-member contexts, including mapped TarI or
      CRPPA candidates, require separate primary assessment. The current work is not
      complete family characterization.
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
  - PF01128
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC18359/
  locator: Preparation, expression, purification and product-identification Methods/Results;
    Tables 1-3; Figures 3 and 4 visually inspected
  accessed_at: '2026-10-11T09:27:59Z'
  support: supports
  snapshot_sha256: 30a287239edc75e2aa4838681065664ae9f2cd13ca656befa3454fac25eeeef1
  summary: Purified recombinant YgbP with MEP, CTP and magnesium yields HPLC-isolated
    CDP-ME supported by reported NMR identity. The preparative endpoint is separate
    from partial-preparation nucleotide promiscuity, coupled-assay substrate screens
    and chromoplast labeling, none of which supplies a fully resolved bacterial causal
    chain.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q46893/entry/pfam/PF01128/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T09:27:59Z'
  support: supports
  snapshot_sha256: a02e6feca30c822186777b5cd6b3419da37fc9dd06539b73be40ce492d523b07
  summary: Q46893 ISPD_ECOLI is a 236-aa K12 reference, sequence version 3, with PF01128
    at 8-229. UniProt, InterPro and 1I52 entity 1 canonical sequences match exactly;
    adopted mutation sites fall within the domain. The 1999 primer's MATTHL translation
    matches the current start. Initiator removal and later His8-tag cleavage are distinct
    preparation histories; exact donor strain, complete clones and cleavage remnant
    remain unverified. Frozen family identity is preserved.
- evidence_id: primary-proof-kinetics
  kind: primary_source
  reference: https://citeseerx.ist.psu.edu/document?doi=47f611b82af525a30852494febee3418127613b0&repid=rep1&type=pdf
  locator: Primary proof pages C-F; preparation and assay Methods, Figure 3 pulse
    controls, Figure 4 gel, Table 1 and Figure 5
  summary: Supports a qualitative CTP pulse advantage, four purified CTP-series turnover
    decreases and five crude-extract screening effects with unresolved directness.
    Lettered proof pages and placeholder publication fields identify version limits.
    Corrected fitted parameters, excluded outliers and contradictory labels are retained
    rather than averaged or silently repaired.
  accessed_at: '2026-10-11T09:27:59Z'
  support: supports
  snapshot_sha256: b48884494a3641c9bee9e06af20c71df5694405999736b49512da1f06fb4783b
- evidence_id: construct-reference-sequence
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1I52/1
  locator: Entity 1 canonical sequence and UniProt alignment
  summary: The 236-aa canonical sequence exactly matches current Q46893 and confirms
    adopted residue numbering. It does not independently reconstruct every plasmid
    or proteolytic junction used in 1999 or 2004.
  accessed_at: '2026-10-11T09:27:59Z'
  support: supports
  snapshot_sha256: a02e6feca30c822186777b5cd6b3419da37fc9dd06539b73be40ce492d523b07
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T09:27:59Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01128
  kind: record_content
  reference: data/families/PF01128.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T09:27:59Z'
  support: context_only
  snapshot_sha256: 5feda7758b18dd10408039c02927b7a3b5b3dd141e2716659b4820ee24311bff
  quote: "id: Pfam:PF01128\npfam_id: PF01128\nname: 2-C-methyl-D-erythritol 4-phosphate\
    \ cytidylyltransferase\nshort_name: IspD\nseed_status: EX_DUF\ncharacterization_status:\
    \ UNSCORED\ncuration_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01128\n\
    counters:\n  proteins: 19574\n  matches: 19791\n  proteomes: 16789\n  taxa: 26255\n\
    \  structures: 56\n  alphafold_models: 13015\n  domain_architectures: 60\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR034683\ndescription: Members of this family are enzymes\
    \ which catalyse the formation of 4-diphosphocytidyl-2-C-methyl-D-erythritol\n\
    \  from cytidine triphosphate and 2-C-methyl-D-erythritol 4-phosphate (MEP) [[cite:PUB00011034]].\n\
    curation_history: history/records/PF01128\ndiscussions:\n- discussion_id: ispd-final-publication-and-divergent-members\n\
    \  prompt: Resolve proof-version and construct details and extend IspD-family\
    \ contexts without transferring\n    one member's substrate specificity.\n  kind:\
    \ CURATION_TODO\n  status: OPEN\n  rationale: Eleven experimental edges cover\
    \ E. coli product formation, CTP isotope trapping, purified\n    kinetics and\
    \ unpurified screens. Molecular interpretations and distinct-function homologs\
    \ require\n    separate assessment.\n  evidence:\n  - reference: PMID:15379557\n\
    \    supports: PARTIAL\n    evidence_source: primary_proof_and_published_abstract\n\
    \    explanation: Primary proof Methods, Table 1 and Figures 3-5 were inspected;\
    \ final publisher full text\n      was inaccessible through the attempted route.\n\
    \  notes: Compare the proof with final figures/tables, reconcile isotope-axis\
    \ and concentration inconsistencies,\n    and establish exact cleavage junctions\
    \ and clone sequences. Review uncurated inhibition, cellular\n    and other-member\
    \ experiments, including TarI and human CRPPA candidates only after member mapping.\n\
    \    Do not equate a structural contact with observed transition-state chemistry\
    \ or the plant-label experiment\n    with a resolved bacterial chain. Partial\
    \ same-agent scientific review; remain IN_PROGRESS.\n  posed_by: Codex\n  posed_date:\
    \ '2026-10-11'\ncausal_graphs:\n- graph_id: ecoli-ispd-preparative-cdpme\n  title:\
    \ Purified E. coli IspD produces CDP-ME\n  scope: Recombinant ygbP from pNCOygbP\
    \ in XL1-blue, purified in the 1999 study. This is an intact enzyme\n    assay,\
    \ not an isolated Pfam fragment or a plant pathway experiment.\n  context: 225\
    \ ug enzyme, 46 mM each MEP and CTP, 10 mM MgCl2, 100 mM Tris-HCl pH 8, 0.7 ml,\
    \ 37 C for\n    1 h; HPLC purification and NMR product identification.\n  family_mapping:\
    \ Q46893/ISPD_ECOLI, ispD/ygbP/b2747, 236-aa K12 reference, sequence version 3;\
    \ PF01128\n    spans 8-229. UniProt and InterPro sequences match. The paper reports\
    \ initiator-methionine removal\n    and an N-terminal sequence consistent with\
    \ ygbP. Exact donor strain and complete plasmid sequence\n    are not independently\
    \ resolved.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:562\n  limitations:\
    \ NMR supports product identity, not a directly observed transition state. Raw\
    \ spectra and\n    preparative replicate/control details remain unverified. Partial-preparation\
    \ nucleotide promiscuity,\n    recombinant coupled-assay signals and plant label\
    \ incorporation are not equivalent experiments or\n    independently identified\
    \ products.\n  nodes:\n  - node_id: purified-ispd-with-mep-ctp-magnesium\n   \
    \ label: Purified IspD with MEP, CTP and magnesium\n    node_type: ACTIVITY\n\
    \    grounding:\n    - UniProtKB:Q46893\n  - node_id: nmr-supported-cdpme\n  \
    \  label: HPLC-isolated CDP-ME identified by NMR\n    node_type: STATE\n  edges:\n\
    \  - edge_id: ispd-system-produces-cdpme\n    subject: purified-ispd-with-mep-ctp-magnesium\n\
    \    predicate: produces\n    object: nmr-supported-cdpme\n    mechanism: The\
    \ joint preparative reaction yields CDP-ME. Its agreement with the independently\
    \ characterized\n      partial-preparation product supports this chemical endpoint\
    \ without resolving each phosphate-transfer\n      microstep.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:10518523\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC18359/\n\
    \      snippet: NMR analysis confirmed\n      explanation: Preparation Methods,\
    \ Table 2 and recombinant-product Results establish the adopted\n        endpoint;\
    \ Figure 4 supports purification scope.\n      cache_path: evidence/PF01128/rohdich-1999-ispd.txt\n\
    \      cache_sha256: 30a287239edc75e2aa4838681065664ae9f2cd13ca656befa3454fac25eeeef1\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q46893/entry/pfam/PF01128/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q46893/entry/pfam/PF01128/\n\
    \      snippet: 'Q46893 Pfam:PF01128 interval: 8-229, inclusive'\n      explanation:\
    \ Exact current reference mapping; identity evidence is not an additional causal\
    \ experiment.\n      cache_path: evidence/PF01128/IspD-identity.txt\n      cache_sha256:\
    \ a02e6feca30c822186777b5cd6b3419da37fc9dd06539b73be40ce492d523b07\n- graph_id:\
    \ ecoli-ispd-ctp-isotope-trapping\n  title: CTP preloading increases early labeled\
    \ CDP-ME formation\n  scope: Purified, thrombin-cleaved E. coli YgbP in the 2004\
    \ primary proof's Figure 3B pulse-chase comparison;\n    not the distinct MEP-pulse\
    \ experiment.\n  context: Pulse 2 mM labeled CTP with 2.2 mM enzyme, then chase\
    \ with 10 mM each CTP/MEP, 100 mM Tris\n    pH 8, 10 mM MgCl2, 2 mM DTT and 4.48\
    \ U pyrophosphatase. Compare label-in-pulse with label-in-chase\n    control at\
    \ early sampled times; TLC/phosphorimaging. Methods uses room-temperature preincubation\
    \ and\n    5-s sampling.\n  family_mapping: The cited construct-source structure\
    \ 1I52 entity 1 exactly matches Q46893's 236-aa sequence,\n    including PF01128\
    \ at 8-229. pHIS8-ygbP is expressed in BL21(DE3), then tag-cleaved for purified\
    \ assays.\n    Exact cleavage remnant and every later clone sequence remain unverified.\n\
    \  scope_status: MECHANISTIC\n  taxon: NCBITaxon:562\n  limitations: The inspected\
    \ copy has lettered proof pages and placeholder publication fields; final tables/figures\n\
    \    were not compared. Figure 3's percent-axis scale conflicts with the prose's\
    \ trapped fraction, so only\n    direction is retained. A 40-s displayed series\
    \ differs from the 50-s Methods duration. Isotope trapping\n    supports the authors'\
    \ ordered-binding interpretation but does not directly image binding or prove\n\
    \    that MEP can never associate first.\n  nodes:\n  - node_id: labeled-ctp-in-pulse\n\
    \    label: Put labeled CTP in the enzyme pulse rather than the chase\n    node_type:\
    \ PERTURBATION\n  - node_id: early-labeled-cdpme\n    label: Early labeled CDP-ME\
    \ formation after addition of both substrates\n    node_type: ACTIVITY\n    grounding:\n\
    \    - UniProtKB:Q46893\n  edges:\n  - edge_id: ctp-preloading-increases-early-label\n\
    \    subject: labeled-ctp-in-pulse\n    predicate: increases\n    object: early-labeled-cdpme\n\
    \    mechanism: The CTP-pulse curve rises ahead of the matched label-in-chase\
    \ control. This is a controlled\n      isotope-trapping effect, not an exact binding\
    \ fraction, equilibrium Kd or observed atomic trajectory.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:15379557\n      source_url: https://citeseerx.ist.psu.edu/document?doi=47f611b82af525a30852494febee3418127613b0&repid=rep1&type=pdf\n\
    \      snippet: ordered, sequential mechanism\n      explanation: Primary proof\
    \ pages D/E, Figure 3B and control Methods support the early-product comparison;\n\
    \        the quotation is the authors' interpretation, not an additional observed\
    \ step.\n      cache_path: evidence/PF01128/richard-2004-ispd-proof.txt\n    \
    \  cache_sha256: b48884494a3641c9bee9e06af20c71df5694405999736b49512da1f06fb4783b\n\
    - graph_id: ecoli-ispd-purified-ctp-series-mutants\n  title: Purified IspD substitutions\
    \ lower reported CTP-series turnover\n  scope: K27S, D106E, T140V and R109A versus\
    \ WT in the 2004 proof's purified, tag-cleaved preparations.\n    Inactive unpurified\
    \ mutants belong to a separate graph.\n  context: TLC product kinetics at 23 C;\
    \ 5 ul with 398 nmol Tris-HCl, 40 nmol MgCl2, 79 nmol NaOH and\n    0.7 U pyrophosphatase;\
    \ 6/12-min sampling. CTP varies, MEP is fixed separately for each mutant. Table\n\
    \    1 uses a CTP-inhibition fit, plus MEP-unsaturation corrections for T140V/R109A.\
    \ At least two independent\n    assay sets; variable protein doses keep consumption\
    \ below 10%.\n  family_mapping: Q46893 and 1I52 canonical sequences match; PF01128\
    \ spans 8-229 and contains K27, D106,\n    R109 and T140. The experiments concern\
    \ full-length enzyme from pHIS8-ygbP, not independent sufficiency\n    of those\
    \ residues or the isolated domain.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:562\n\
    \  limitations: These are reported fitted parameters, not direct binding affinities\
    \ or observed transition-state\n    stabilization. Final assay pH and complete\
    \ clones remain unverified. Between-run variation, excluded\n    fit outliers\
    \ and substrate-inhibition corrections matter. The proof footnote says T104V where\
    \ the\n    main row says T140V; K27S's corrected MEP and CTP values differ and\
    \ are not silently averaged. Final\n    publication comparison remains open.\n\
    \  nodes:\n  - node_id: k27s-purified\n    label: K27S instead of WT in purified\
    \ kinetics\n    node_type: PERTURBATION\n  - node_id: d106e-purified\n    label:\
    \ D106E instead of WT in purified kinetics\n    node_type: PERTURBATION\n  - node_id:\
    \ t140v-purified\n    label: T140V instead of WT in purified kinetics\n    node_type:\
    \ PERTURBATION\n  - node_id: r109a-purified\n    label: R109A instead of WT in\
    \ purified kinetics\n    node_type: PERTURBATION\n  - node_id: reported-ctp-series-turnover\n\
    \    label: Reported CTP-series turnover from labeled CDP-ME kinetics\n    node_type:\
    \ ACTIVITY\n    grounding:\n    - UniProtKB:Q46893\n  edges:\n  - edge_id: k27s-decreases-ctp-turnover\n\
    \    subject: k27s-purified\n    predicate: decreases\n    object: reported-ctp-series-turnover\n\
    \    mechanism: Table 1 reports K27S at 2.05 versus WT 54.1 per second in the\
    \ CTP series. Residual activity\n      is retained; neither absolute inactivity\
    \ nor a unique lysine chemical role is asserted.\n    directness: DIRECT\n   \
    \ support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:15379557\n      source_url: https://citeseerx.ist.psu.edu/document?doi=47f611b82af525a30852494febee3418127613b0&repid=rep1&type=pdf\n\
    \      snippet: Table 1\n      explanation: Proof page F, K27S and WT CTP columns;\
    \ purification and kinetic Methods on page D.\n        Figure 5 instead uses the\
    \ corrected MEP comparison.\n      cache_path: evidence/PF01128/richard-2004-ispd-proof.txt\n\
    \      cache_sha256: b48884494a3641c9bee9e06af20c71df5694405999736b49512da1f06fb4783b\n\
    \  - edge_id: d106e-decreases-ctp-turnover\n    subject: d106e-purified\n    predicate:\
    \ decreases\n    object: reported-ctp-series-turnover\n    mechanism: D106E has\
    \ lower reported CTP-series turnover than WT, 0.93 versus 54.1 per second. This\n\
    \      does not directly establish which binding, conformational or chemical step\
    \ changed.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:15379557\n      source_url:\
    \ https://citeseerx.ist.psu.edu/document?doi=47f611b82af525a30852494febee3418127613b0&repid=rep1&type=pdf\n\
    \      snippet: Table 1\n      explanation: Proof page F, D106E and WT CTP columns;\
    \ substantial between-run uncertainty is retained\n        in the assessment.\n\
    \      cache_path: evidence/PF01128/richard-2004-ispd-proof.txt\n      cache_sha256:\
    \ b48884494a3641c9bee9e06af20c71df5694405999736b49512da1f06fb4783b\n  - edge_id:\
    \ t140v-decreases-ctp-turnover\n    subject: t140v-purified\n    predicate: decreases\n\
    \    object: reported-ctp-series-turnover\n    mechanism: The T140V row gives\
    \ corrected CTP-series turnover of 1.8 versus WT 54.1 per second. The\n      additional\
    \ correction for unsaturating MEP is part of this estimate, not an independently\
    \ observed\n      catalytic constant.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:15379557\n\
    \      source_url: https://citeseerx.ist.psu.edu/document?doi=47f611b82af525a30852494febee3418127613b0&repid=rep1&type=pdf\n\
    \      snippet: Table 1\n      explanation: Proof page F, T140V row and footnote\
    \ c; the separate T104V wording discrepancy remains\n        unresolved.\n   \
    \   cache_path: evidence/PF01128/richard-2004-ispd-proof.txt\n      cache_sha256:\
    \ b48884494a3641c9bee9e06af20c71df5694405999736b49512da1f06fb4783b\n  - edge_id:\
    \ r109a-decreases-ctp-turnover\n    subject: r109a-purified\n    predicate: decreases\n\
    \    object: reported-ctp-series-turnover\n    mechanism: Corrected R109A CTP-series\
    \ turnover is 0.26 versus WT 54.1 per second. The measured product\n      kinetics\
    \ and model correction support a decrease, not a directly observed hydrogen-bond\
    \ network\n      or universal binding defect.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:15379557\n\
    \      source_url: https://citeseerx.ist.psu.edu/document?doi=47f611b82af525a30852494febee3418127613b0&repid=rep1&type=pdf\n\
    \      snippet: Table 1\n      explanation: Proof page F, R109A CTP column and\
    \ footnote c; distinct from the MEP-series estimate.\n      cache_path: evidence/PF01128/richard-2004-ispd-proof.txt\n\
    \      cache_sha256: b48884494a3641c9bee9e06af20c71df5694405999736b49512da1f06fb4783b\n\
    - graph_id: ecoli-ispd-crude-extract-mutant-effects\n  title: Five IspD substitutions\
    \ reduce crude-extract CDP-ME production\n  scope: BL21(DE3) extracts expressing\
    \ D106A, D106N, K213S, K27A or T165V, compared with WT, in the 2004\n    proof.\
    \ These variants were not further purified. PHENOTYPIC denotes the biochemical\
    \ assay effect without\n    a resolved molecular cause.\n  context: 217 nmol labeled\
    \ MEP, 81.3 nmol CTP, 400 nmol Tris-HCl, 40 nmol MgCl2, 79 nmol NaOH and a nominal\n\
    \    1-ug YgbP-containing crude sample in 5 ul; 23 C, 1/15 h. TLC background from\
    \ a blank lacking YgbP\n    is subtracted. Exact protein-normalization basis and\
    \ final assay pH remain unresolved.\n  family_mapping: Intended substitutions\
    \ map to Q46893's PF01128 interval 8-229; the cited 1I52 reference\n    sequence\
    \ matches. Unlike purified kinetics, the crude screen precedes His8-tag cleavage.\
    \ Complete\n    mutant clone sequences are not independently verified.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:562\n  limitations: No activity was detected\
    \ under the reported screen, not proven chemically impossible under\n    all conditions.\
    \ Directness is UNRESOLVED because expression, soluble yield, folding and background\n\
    \    enzymes can contribute. D106/T165 variants partly form inclusion bodies.\
    \ The source's sensitivity\n    estimate does not supply independent mutant-specific\
    \ detection limits or folded-protein controls.\n    Proof-only full-text access\
    \ remains explicit.\n  nodes:\n  - node_id: d106a-crude\n    label: Express D106A\
    \ instead of WT\n    node_type: PERTURBATION\n  - node_id: d106n-crude\n    label:\
    \ Express D106N instead of WT\n    node_type: PERTURBATION\n  - node_id: k213s-crude\n\
    \    label: Express K213S instead of WT\n    node_type: PERTURBATION\n  - node_id:\
    \ k27a-crude\n    label: Express K27A instead of WT\n    node_type: PERTURBATION\n\
    \  - node_id: t165v-crude\n    label: Express T165V instead of WT\n    node_type:\
    \ PERTURBATION\n  - node_id: crude-extract-cdpme-output\n    label: Detected labeled\
    \ CDP-ME formation in the crude-extract screen\n    node_type: ACTIVITY\n    grounding:\n\
    \    - UniProtKB:Q46893\n  edges:\n  - edge_id: d106a-lowers-crude-output\n  \
    \  subject: d106a-crude\n    predicate: decreases\n    object: crude-extract-cdpme-output\n\
    \    mechanism: D106A gives no detected product activity relative to the active\
    \ WT screen; this does not\n      isolate an elementary chemical defect.\n   \
    \ directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:15379557\n      source_url: https://citeseerx.ist.psu.edu/document?doi=47f611b82af525a30852494febee3418127613b0&repid=rep1&type=pdf\n\
    \      snippet: inactive\n      explanation: Proof page E crude-extract Results\
    \ and page F Table 1; not a purified D106A kinetic\n        measurement.\n   \
    \   cache_path: evidence/PF01128/richard-2004-ispd-proof.txt\n      cache_sha256:\
    \ b48884494a3641c9bee9e06af20c71df5694405999736b49512da1f06fb4783b\n  - edge_id:\
    \ d106n-lowers-crude-output\n    subject: d106n-crude\n    predicate: decreases\n\
    \    object: crude-extract-cdpme-output\n    mechanism: D106N gives no detected\
    \ product activity in this extract comparison; abundance and folding\n      are\
    \ not excluded as contributors.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:15379557\n\
    \      source_url: https://citeseerx.ist.psu.edu/document?doi=47f611b82af525a30852494febee3418127613b0&repid=rep1&type=pdf\n\
    \      snippet: inactive\n      explanation: Proof page E crude-extract Results\
    \ and page F Table 1; no purified D106N curve is claimed.\n      cache_path: evidence/PF01128/richard-2004-ispd-proof.txt\n\
    \      cache_sha256: b48884494a3641c9bee9e06af20c71df5694405999736b49512da1f06fb4783b\n\
    \  - edge_id: k213s-lowers-crude-output\n    subject: k213s-crude\n    predicate:\
    \ decreases\n    object: crude-extract-cdpme-output\n    mechanism: K213S lowers\
    \ detected extract product formation below the screen's reported activity detection;\n\
    \      charge stabilization is an interpretation, not the measured endpoint.\n\
    \    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:15379557\n      source_url: https://citeseerx.ist.psu.edu/document?doi=47f611b82af525a30852494febee3418127613b0&repid=rep1&type=pdf\n\
    \      snippet: inactive\n      explanation: Proof page E screen and page F Table\
    \ 1, with the no-further-purification qualification.\n      cache_path: evidence/PF01128/richard-2004-ispd-proof.txt\n\
    \      cache_sha256: b48884494a3641c9bee9e06af20c71df5694405999736b49512da1f06fb4783b\n\
    \  - edge_id: k27a-lowers-crude-output\n    subject: k27a-crude\n    predicate:\
    \ decreases\n    object: crude-extract-cdpme-output\n    mechanism: K27A has no\
    \ detected extract activity in the screen. It is not conflated with K27S, which\n\
    \      retains purified activity.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:15379557\n\
    \      source_url: https://citeseerx.ist.psu.edu/document?doi=47f611b82af525a30852494febee3418127613b0&repid=rep1&type=pdf\n\
    \      snippet: inactive\n      explanation: Proof page E and Table 1 distinguish\
    \ K27A screening from the separately purified K27S\n        mutant.\n      cache_path:\
    \ evidence/PF01128/richard-2004-ispd-proof.txt\n      cache_sha256: b48884494a3641c9bee9e06af20c71df5694405999736b49512da1f06fb4783b\n\
    \  - edge_id: t165v-lowers-crude-output\n    subject: t165v-crude\n    predicate:\
    \ decreases\n    object: crude-extract-cdpme-output\n    mechanism: T165V gives\
    \ no detected extract activity. Its aggregation qualification prevents assigning\n\
    \      the entire decrease to a particular substrate contact.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:15379557\n      source_url: https://citeseerx.ist.psu.edu/document?doi=47f611b82af525a30852494febee3418127613b0&repid=rep1&type=pdf\n\
    \      snippet: inactive\n      explanation: Proof page E describes inclusion\
    \ bodies and screen results; Table 1's inactive label\n        is not a purified\
    \ turnover fit.\n      cache_path: evidence/PF01128/richard-2004-ispd-proof.txt\n\
    \      cache_sha256: b48884494a3641c9bee9e06af20c71df5694405999736b49512da1f06fb4783b\n\
    curation_events:\n- timestamp: '2026-10-11T09:15:06Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Add scoped IspD product, isotope-trapping\
    \ and mutant graphs\n  history_record: history/records/PF01128/2026-10-11T091506Z-codex-f15b16.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Q46893 ISPD_ECOLI is a 236-aa K12 reference, sequence version 3, with PF01128
    at 8-229. UniProt, InterPro and 1I52 entity 1 canonical sequences match exactly;
    adopted mutation sites fall within the domain. The 1999 primer's MATTHL translation
    matches the current start. Initiator removal and later His8-tag cleavage are distinct
    preparation histories; exact donor strain, complete clones and cleavage remnant
    remain unverified. Frozen family identity is preserved.
  target_ids:
  - PF01128
  evidence_ids:
  - identity
  - primary
  - primary-proof-kinetics
  - construct-reference-sequence
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: One preparative product edge and one qualitative CTP-pulse effect are separate
    from four reported purified CTP-series turnover decreases. K27S, D106E, T140V
    and R109A retain fitting, unsaturation and uncertainty qualifications. Five inactive
    crude-extract variants are explicitly not purified enzymes, with OBSERVED support
    but UNRESOLVED directness because folding, expression and background activity
    can contribute. The proof's percent-axis, duration, mass/concentration and T104V/T140V
    conflicts are not silently repaired. Structural contacts and ordered-binding interpretation
    are not directly observed atomic steps.
  target_ids:
  - PF01128
  evidence_ids:
  - primary
  - native
  - primary-proof-kinetics
  - construct-reference-sequence
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Final publisher tables/figures were not compared with the accessible proof.
    Complete historical constructs, numerical-label reconciliation, final kinetic-assay
    pH, mutant-normalization and folded-protein controls remain incomplete. Other
    inhibition, cellular and distinct-member contexts, including mapped TarI or CRPPA
    candidates, require separate primary assessment. The current work is not complete
    family characterization.
  target_ids:
  - PF01128
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01128-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Reconcile IspD proof and construct details before expanding mechanism claims
  description: Compare final publication figures and tables, resolve isotope-axis
    and concentration discrepancies and exact clones, and obtain clearer inactive-mutant
    normalization/folding evidence. Curate remaining member-specific substrate and
    cellular contexts separately, without transferring E. coli specificity or elevating
    crude-extract loss to an elementary catalytic defect. Retain a successor review
    before strengthening status.
  target_ids:
  - PF01128
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - primary-proof-kinetics
  - construct-reference-sequence
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01128.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Compare final publication figures and tables, resolve isotope-axis
    and concentration discrepancies and exact clones, and obtain clearer inactive-mutant
    normalization/folding evidence. Curate remaining member-specific substrate and
    cellular contexts separately, without transferring E. coli specificity or elevating
    crude-extract loss to an elementary catalytic defect. Retain a successor review
    before strengthening status.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01128
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Rohdich 1999 main Methods/Results/Discussion and Tables 1-3 were read; Figures 3/4
  were visually inspected. Richard 2004 proof pages A-H were read, with Figure 3/4
  page E and Table 1/Figure 5 page F visually checked. The final publication and last
  reference-only proof page were not inspected; raw NMR, original kinetic data and
  complete clone sequences were not reanalyzed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
