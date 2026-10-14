# PF01951: scoped Archease activation, ligation and RNA-processing effects

- Review: 20261012T090304Z-pf01951-archease-scoped-activation-and-rna-processing
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-12T09:01:17Z
- Finished UTC: 2026-10-12T09:03:04Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Nine graphs retain seventeen OBSERVED experimental edges, nine DIRECT biochemical effects and eight UNRESOLVED mutant or cellular effects. Six graphs are MECHANISTIC and three PHENOTYPIC. Five minimal ledgers and three OPEN discussions retain scope, source and follow-up limits. This partial same-agent scientific review remains NEEDS_FOLLOWUP; PF01951 is IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Ascending family after PF01950, with additional PF01951 branches retained for follow-up; all 8296 records and earlier findings remain in scope.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01951 | data/families/PF01951.yaml | generated | PF01951 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01951 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01951.

Frozen Archease/former DUF101, IPR023572, EX_DUF and UNSCORED remain unchanged. Human Q8IWT0 v2 is167 aa with PF01951 31-167. Historical A8K0B5 resolves to it; the179-aa paper construct corresponds to the current12-residue N-terminal extension, with different historical isoform naming. PDB8BTX entity17-183 exactly equals the current167-aa sequence; paperD51/K156 map toD39/K144, verified by residue identity. O59205v1 is PH1536,142 aa, PF01951 4-142; Desai2014 insertsL after the initialM but retains native numbering. U2OS disruption does not identify a selectively tested isoform. Remaining Thermus construct identity is explicitly unresolved, not adopted as a native graph.

### Directed effects and limits

graph: supported. Targets: PF01951.

Human activation is distinct from cleaved-XBP1 ligation and isolated-intron circularization, with different RNA/protein/nucleotide concentrations. The two Archease substitutions have separate activation and ligation outputs; WT purity is not mutant-fold verification. The PhRtcB RNA-ppG assay uses pre-guanylylated enzyme and modified substrate, not the human protein-labeling readout. ATP/dGTP/ITP effects retain separate nucleotide contexts and the100 nM comparison is not pooled with800 nM ATP kinetics. U2OS day3 tRNA ratio and stress RNA outputs remain separate from the later mature-tRNA reduction; heterogeneous targeting and residual protein do not support complete knockout or universal essentiality. No unmeasured mediation chain joins these systems.

### Remaining family coverage

completeness: concern. Targets: PF01951.

Remaining Archease mutant and RtcB-rescue experiments, bacterial turnover and Thermus clone identity, PAB1946 methyltransferase support, Popow/Jurkin original cellular evidence, fly allele/localization/rescue, yeast complementation, PYROXD1 and Danio studies remain open. Acquired full texts do not count as completed reviews. No exhaustive family membership, primary-literature census, domain-only mechanism, raw-data reanalysis or independent expert endorsement.

## Findings

### additional-contexts: Extend remaining Archease contexts without cross-species or construct transfers

minor / open / confirmed; issue key: pf01951-causal-context-coverage.

Continue PF01951 primary review before treating the family as complete. Resolve Thermus strain/clone mapping, inspect archaeal mutant and RtcB-rescue figures and controls, finish Auxilien2007 Methods and assay images, and review original human and fly perturbations with exact sequence/allele mapping. Keep species-specific nucleotide negatives, modified versus native RNA, heterogeneous cell populations and independent rescue experiments explicit. Append actual history and successor review after each supported addition; all earlier family follow-ups remain open.

## Recommended Actions And Acceptance Checks

### extend-contexts

Continue PF01951 primary review before treating the family as complete. Resolve Thermus strain/clone mapping, inspect archaeal mutant and RtcB-rescue figures and controls, finish Auxilien2007 Methods and assay images, and review original human and fly perturbations with exact sequence/allele mapping. Keep species-specific nucleotide negatives, modified versus native RNA, heterogeneous cell populations and independent rescue experiments explicit. Append actual history and successor review after each supported addition; all earlier family follow-ups remain open.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC10944509/; Gerber2024 Methods and Results; Figures1/5 and supplementary S1/S2 visually inspected. | supports | Purified human Archease supports RTCB labeling and RNA ligation; matched mutant comparisons retain molecular uncertainty. Archease is not assigned RTCB catalytic chemistry or universal ATP utilization. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01951/protein/uniprot/Q8IWT0/; Accession and domain locations; paired UniProt identity facts | supports | Frozen Archease/former DUF101, IPR023572, EX_DUF and UNSCORED remain unchanged. Human Q8IWT0 v2 is167 aa with PF01951 31-167. Historical A8K0B5 resolves to it; the179-aa paper construct corresponds to the current12-residue N-terminal extension, with different historical isoform naming. PDB8BTX entity17-183 exactly equals the current167-aa sequence; paperD51/K156 map toD39/K144, verified by residue identity. O59205v1 is PH1536,142 aa, PF01951 4-142; Desai2014 insertsL after the initialM but retains native numbering. U2OS disruption does not identify a selectively tested isoform. Remaining Thermus construct identity is explicitly unresolved, not adopted as a native graph. |
| archaeal-reactions | https://pmc.ncbi.nlm.nih.gov/articles/PMC3973293/; Desai2014 Methods/Results and visually inspected Figures2/3/4, author PDF pages4/5/7. | supports | Archease increases PhRtcB ligation and trapped RNA-ppG rates and enables tested purine cofactors; conditions differ from human assays. |
| cellular-disruption | https://www.nature.com/articles/s42003-025-07523-z; Suzuki2025 Figure3C/D/F/G/H, S6G-I, S7B/D and Methods; images inspected. | supports | U2OS population targeting changes day3 tRNA ratio and stress RNA readouts; later mature-tRNA decline remains qualitative, with residual signal and no Archease-specific rescue. |
| source-coverage | evidence/PF01951/coverage.txt; Primary-source acquisition, inspected extent, unresolved identity and named follow-ups. | supports | Primary coverage spans human and archaeal assays; additional bacterial, methyltransferase and cellular branches remain explicit work, not absent evidence. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01951 | data/families/PF01951.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Gerber2024 full Methods and relevant Results with Figures1/5 and S1/S2 inspected; Desai2014 full Methods/Results with Figures2/3/4 inspected from the public author PDF; Suzuki2025 relevant Methods/Results with Figure3 and S6/S7 inspected. Desai2015 full Methods/Results read but figures only rendered, not visually audited. Auxilien2007 selected author-copy sections read, not full figure/method coverage. Francis2022 abstract and rescue caption only; Popow2014 HTML and Desai2014 supplement obtained but not fully reviewed. No raw-data reanalysis or independent expert review.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T090304Z-pf01951-archease-scoped-activation-and-rna-processing
title: 'PF01951: scoped Archease activation, ligation and RNA-processing effects'
started_at: '2026-10-12T09:01:17Z'
finished_at: '2026-10-12T09:03:04Z'
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
summary: Nine graphs retain seventeen OBSERVED experimental edges, nine DIRECT biochemical
  effects and eight UNRESOLVED mutant or cellular effects. Six graphs are MECHANISTIC
  and three PHENOTYPIC. Five minimal ledgers and three OPEN discussions retain scope,
  source and follow-up limits. This partial same-agent scientific review remains NEEDS_FOLLOWUP;
  PF01951 is IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01951.yaml
    sha256: ad1896676500f96475386cbde9bd92824ec19a5c44658a5738b86ad83f467c9f
    role: context
  - path: data/families/PF01951.yaml
    sha256: 4d2f84f2d7e265734217b797bd63d3e1d68b2c6a3b28e592c1f603cc32abdf80
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
  - path: evidence/PF01951/gerber-2024.txt
    role: context
    sha256: abc78d8f41d72e2e58ec8cafa48eae844ef07fecee3823abdffd52494890613c
  - path: evidence/PF01951/identity.txt
    role: context
    sha256: 71950660fb2ccc6582723b7882aabd6489102ca456f4ff09f626ac24c5a33885
  - path: evidence/PF01951/desai-2014.txt
    role: context
    sha256: 0dd92157e3b40af1071b0efee1e206b8405a38246a5cc756a50f2f80569b128b
  - path: evidence/PF01951/suzuki-2025.txt
    role: context
    sha256: d3e772eaf174d79f070d0c77f3a15af017a6a108dfc625efc2b0876c5e50cf68
  - path: evidence/PF01951/coverage.txt
    role: context
    sha256: c1a74e6e6601371ff5e7f84f915a7459229ee229fdcf8c37016cfa69d47e0a5c
targets:
- target_id: PF01951
  path: data/families/PF01951.yaml
  label: PF01951
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01951.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: f2f16a113ab9d83bda5df8085be34939f7fab670a6ce338122200bed708fcbe6
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Ascending family after PF01950, with additional PF01951 branches retained
    for follow-up; all 8296 records and earlier findings remain in scope.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01951
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Remaining Archease mutant and RtcB-rescue experiments, bacterial turnover
      and Thermus clone identity, PAB1946 methyltransferase support, Popow/Jurkin
      original cellular evidence, fly allele/localization/rescue, yeast complementation,
      PYROXD1 and Danio studies remain open. Acquired full texts do not count as completed
      reviews. No exhaustive family membership, primary-literature census, domain-only
      mechanism, raw-data reanalysis or independent expert endorsement.
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
  - PF01951
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10944509/
  locator: Gerber2024 Methods and Results; Figures1/5 and supplementary S1/S2 visually
    inspected.
  accessed_at: '2026-10-12T09:03:04Z'
  support: supports
  snapshot_sha256: abc78d8f41d72e2e58ec8cafa48eae844ef07fecee3823abdffd52494890613c
  summary: Purified human Archease supports RTCB labeling and RNA ligation; matched
    mutant comparisons retain molecular uncertainty. Archease is not assigned RTCB
    catalytic chemistry or universal ATP utilization.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01951/protein/uniprot/Q8IWT0/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-12T09:03:04Z'
  support: supports
  snapshot_sha256: 71950660fb2ccc6582723b7882aabd6489102ca456f4ff09f626ac24c5a33885
  summary: Frozen Archease/former DUF101, IPR023572, EX_DUF and UNSCORED remain unchanged.
    Human Q8IWT0 v2 is167 aa with PF01951 31-167. Historical A8K0B5 resolves to it;
    the179-aa paper construct corresponds to the current12-residue N-terminal extension,
    with different historical isoform naming. PDB8BTX entity17-183 exactly equals
    the current167-aa sequence; paperD51/K156 map toD39/K144, verified by residue
    identity. O59205v1 is PH1536,142 aa, PF01951 4-142; Desai2014 insertsL after the
    initialM but retains native numbering. U2OS disruption does not identify a selectively
    tested isoform. Remaining Thermus construct identity is explicitly unresolved,
    not adopted as a native graph.
- evidence_id: archaeal-reactions
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3973293/
  locator: Desai2014 Methods/Results and visually inspected Figures2/3/4, author PDF
    pages4/5/7.
  summary: Archease increases PhRtcB ligation and trapped RNA-ppG rates and enables
    tested purine cofactors; conditions differ from human assays.
  accessed_at: '2026-10-12T09:03:04Z'
  support: supports
  snapshot_sha256: 0dd92157e3b40af1071b0efee1e206b8405a38246a5cc756a50f2f80569b128b
- evidence_id: cellular-disruption
  kind: primary_source
  reference: https://www.nature.com/articles/s42003-025-07523-z
  locator: Suzuki2025 Figure3C/D/F/G/H, S6G-I, S7B/D and Methods; images inspected.
  summary: U2OS population targeting changes day3 tRNA ratio and stress RNA readouts;
    later mature-tRNA decline remains qualitative, with residual signal and no Archease-specific
    rescue.
  accessed_at: '2026-10-12T09:03:04Z'
  support: supports
  snapshot_sha256: d3e772eaf174d79f070d0c77f3a15af017a6a108dfc625efc2b0876c5e50cf68
- evidence_id: source-coverage
  kind: search
  reference: evidence/PF01951/coverage.txt
  locator: Primary-source acquisition, inspected extent, unresolved identity and named
    follow-ups.
  search_scope: PF01951, Archease, DUF101, member accessions, exact titles and a2026
    update scan; pre-edit curation/evidence/history/review search included ignored
    and hidden files but excluded JSON.
  summary: Primary coverage spans human and archaeal assays; additional bacterial,
    methyltransferase and cellular branches remain explicit work, not absent evidence.
  accessed_at: '2026-10-12T09:03:04Z'
  support: supports
  snapshot_sha256: c1a74e6e6601371ff5e7f84f915a7459229ee229fdcf8c37016cfa69d47e0a5c
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-12T09:03:04Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01951
  kind: record_content
  reference: data/families/PF01951.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-12T09:03:04Z'
  support: context_only
  snapshot_sha256: 4d2f84f2d7e265734217b797bd63d3e1d68b2c6a3b28e592c1f603cc32abdf80
  quote: "id: Pfam:PF01951\npfam_id: PF01951\nname: Archease protein family (MTH1598/TM1083)\n\
    short_name: Archease\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01951\n\
    counters:\n  proteins: 3523\n  matches: 3542\n  proteomes: 2944\n  taxa: 7482\n\
    \  structures: 9\n  alphafold_models: 2910\n  domain_architectures: 34\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR023572\ndescription: This archease family of proteins\
    \ [[cite:PUB00109176]], has two SHS2 domains [[cite:PUB00057445]],\n  with one\
    \ inserted into another. It is predicted to be an enzyme [[cite:PUB00057445]].\
    \ It is predicted\n  to act as a chaperone in DNA/RNA metabolism [[cite:PUB00109176]].\n\
    curation_history: history/records/PF01951\ndiscussions:\n- discussion_id: pf01951-other-assay-contexts\n\
    \  prompt: Extend the remaining Archease biochemical contexts with exact construct\
    \ mappings.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: The initial human\
    \ and archaeal assays are not the whole family mechanism.\n  evidence:\n  - reference:\
    \ PMID:26385509\n    supports: PARTIAL\n    evidence_source: primary_publication\n\
    \    explanation: Full Desai2015 Results/Methods read. Thermus construct accession\
    \ and strain, figure audit\n      and species-specific turnover comparisons remain\
    \ to resolve.\n  - reference: PMID:17470432\n    supports: PARTIAL\n    evidence_source:\
    \ primary_publication\n    explanation: Selected public author-copy methods/results\
    \ inspected; PAB1946 methyltransferase-support\n      assays need complete buffer,\
    \ control and visual review.\n  - reference: PMID:24435797\n    supports: PARTIAL\n\
    \    evidence_source: primary_publication\n    explanation: Desai2014 Archease\
    \ and RtcB mutant effects and trapped-intermediate experiments require\n     \
    \ additional edge-specific review.\n  posed_by: Codex\n  posed_date: '2026-10-12'\n\
    \  notes: Follow evidence/PF01951/coverage.txt. No universal ATP utilization,\
    \ oligomeric state, physiological\n    metal or coevolution edge is established\
    \ by the retained assays.\n- discussion_id: pf01951-cellular-and-regulatory-coverage\n\
    \  prompt: Review original human, fly and other cellular Archease evidence before\
    \ extending phenotype chains.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale:\
    \ Whole-gene phenotypes and localization changes do not by themselves prove a\
    \ domain-specific\n    molecular pathway.\n  evidence:\n  - reference: PMID:24870230\n\
    \    supports: PARTIAL\n    evidence_source: primary_publication\n    explanation:\
    \ Popow2014 full public HTML obtained; detailed Methods/Extended Data review remains.\n\
    \  - reference: PMID:25378478\n    supports: PARTIAL\n    evidence_source: primary_publication\n\
    \    explanation: Jurkin2014 is a follow-up lead, not a reviewed Archease-specific\
    \ plasma-cell knockout.\n  - reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC9641670/\n\
    \    supports: PARTIAL\n    evidence_source: primary_publication\n    explanation:\
    \ Drosophila disjointed/CG6353 phenotype and rescue caption inspected; allele\
    \ map and complete\n      experiments remain to review.\n  posed_by: Codex\n \
    \ posed_date: '2026-10-12'\n  notes: Keep DDX1/RTCB rescue distinct from Archease\
    \ rescue, and do not concatenate nuclear localization,\n    tRNA maturation and\
    \ membrane growth from a proposed model.\n- discussion_id: pf01951-residue-and-population-limits\n\
    \  prompt: Resolve mutant folding controls and heterogeneous cellular disruption\
    \ before stronger mechanistic\n    attribution.\n  kind: CURATION_TODO\n  status:\
    \ OPEN\n  rationale: Static contacts support a mechanism model but do not distinguish\
    \ all consequences of substitution;\n    the U2OS experiment uses sorted transfected\
    \ populations.\n  evidence:\n  - reference: PMID:38493148\n    supports: PARTIAL\n\
    \    evidence_source: primary_publication\n    explanation: D51A/K156A inhibit\
    \ activation and ligation, but S1 is WT purity, not mutant folding verification.\n\
    \      Paper positions map to current Q8IWT0 D39/K144.\n  - reference: doi:10.1038/s42003-025-07523-z\n\
    \    supports: PARTIAL\n    evidence_source: primary_publication\n    explanation:\
    \ S6 documents majority one-base insertion and reduced protein, not a uniform\
    \ biallelic\n      clone. S7 retains residual mature tRNA.\n  posed_by: Codex\n\
    \  posed_date: '2026-10-12'\n  notes: No source-independent expert endorsement,\
    \ isolated-domain test, Archease-specific cellular rescue\n    or observed release\
    \ trajectory is claimed.\ncausal_graphs:\n- graph_id: human-rtcb-activation-2024\n\
    \  title: Human Archease enables RTCB guanylylation\n  scope: Recombinant human\
    \ whole-protein Archease and RTCB in a purified activation assay.\n  context:\
    \ Figure1e; 1 uM each protein, 80 nM alpha-32P-GTP, 0.5 mM MnCl2, 30 C. The four\
    \ conditions separate\n    Archease and Mn addition.\n  family_mapping: Paper\
    \ A8K0B5 179-aa construct maps to Q8IWT0 v2 with a 12-aa N-terminal extension;\
    \ canonical\n    PF01951 31-167. Archease expressed in E. coli, RTCB Q9Y3I0 in\
    \ Sf21. Current isoform naming differs\n    from the paper.\n  taxon: NCBITaxon:9606\n\
    \  scope_status: MECHANISTIC\n  limitations: Whole protein, not an isolated domain\
    \ or universal family activity. Tag removal was optional.\n    Protein-associated\
    \ radiolabel is the readout; Methods specify SDS-PAGE while the figure caption\
    \ says\n    urea-PAGE. No Archease-alone ligase activity or observed dissociation\
    \ trajectory is asserted.\n  nodes:\n  - node_id: activation\n    label: Archease\
    \ added to RTCB with GTP and Mn\n    node_type: ACTIVITY\n    grounding:\n   \
    \ - UniProtKB:Q8IWT0\n    - UniProtKB:Q9Y3I0\n  - node_id: rtcb_gmp\n    label:\
    \ Covalent RTCB-GMP intermediate\n    node_type: STATE\n    grounding:\n    -\
    \ UniProtKB:Q9Y3I0\n  edges:\n  - edge_id: human-archease-rtcb-gmp\n    subject:\
    \ activation\n    predicate: enables\n    object: rtcb_gmp\n    mechanism: Archease\
    \ promotes the GTP-dependent labeling of RTCB under the matched Mn-containing\
    \ conditions;\n      the activated histidine belongs to RTCB.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:38493148\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10944509/\n\
    \      snippet: promotes guanylylation\n      explanation: Figure1e and activation\
    \ Methods; Archease-minus and Mn-minus controls, three replicates.\n        Structure\
    \ alone is not the evidence for this directed biochemical effect.\n      cache_path:\
    \ evidence/PF01951/gerber-2024.txt\n      cache_sha256: abc78d8f41d72e2e58ec8cafa48eae844ef07fecee3823abdffd52494890613c\n\
    - graph_id: human-xbp1-fragment-ligation-2024\n  title: Archease supports RTCB\
    \ ligation of cleaved XBP1 fragments\n  scope: Reconstituted human XBP1 stem-loop\
    \ ligation, not a cellular stress response.\n  context: IRE1-cleaved RNA 250 nM,\
    \ RTCB 500 nM, Archease 1 uM, GTP 1 mM, MnCl2 0.5 mM, 30 C; ligation\n    buffer\
    \ includes 2 mM MgCl2. Figure1b time course.\n  family_mapping: Whole human 179-aa\
    \ Archease construct; historical A8K0B5 maps to Q8IWT0 v2 plus 12 N-terminal\n\
    \    residues, canonical PF01951 31-167.\n  taxon: NCBITaxon:9606\n  scope_status:\
    \ MECHANISTIC\n  limitations: Joint reaction conditions, not Archease alone as\
    \ a sufficient ligase. Exon and intron products\n    are separate outputs; no\
    \ product-to-product edge. The marked unknown byproduct is not assigned an\n \
    \   identity or physiological function.\n  nodes:\n  - node_id: reaction\n   \
    \ label: Archease with RTCB and cleaved XBP1 substrate\n    node_type: ACTIVITY\n\
    \    grounding:\n    - UniProtKB:Q8IWT0\n    - UniProtKB:Q9Y3I0\n  - node_id:\
    \ exons\n    label: Ligated XBP1 exon fragment\n    node_type: STATE\n  - node_id:\
    \ intron\n    label: Circular XBP1 intron from cleaved substrate\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: human-xbp1-exon-ligation\n    subject: reaction\n\
    \    predicate: produces\n    object: exons\n    mechanism: With Archease, the\
    \ RTCB-containing reaction accumulates the exon-ligated band absent from\n   \
    \   the matched Archease-minus reaction.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:38493148\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10944509/\n      snippet:\
    \ dependent upon addition of Archease\n      explanation: Figure1b visually inspected\
    \ with substrate and cleavage controls; three replicate reactions.\n        No\
    \ cellular transcriptional effect is measured here.\n      cache_path: evidence/PF01951/gerber-2024.txt\n\
    \      cache_sha256: abc78d8f41d72e2e58ec8cafa48eae844ef07fecee3823abdffd52494890613c\n\
    \  - edge_id: human-xbp1-intron-ligation\n    subject: reaction\n    predicate:\
    \ produces\n    object: intron\n    mechanism: The same joint reaction generates\
    \ the faster-migrating intron species assigned as circular\n      RNA, independently\
    \ of the exon product.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:38493148\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC10944509/\n      snippet: dependent\
    \ upon addition of Archease\n      explanation: Figure1b lower product band and\
    \ corresponding Results, not the unidentified asterisk\n        band; subsequent\
    \ isolated-intron assay provides a separate corroborating context.\n      cache_path:\
    \ evidence/PF01951/gerber-2024.txt\n      cache_sha256: abc78d8f41d72e2e58ec8cafa48eae844ef07fecee3823abdffd52494890613c\n\
    - graph_id: human-isolated-intron-2024\n  title: Archease supports isolated XBP1\
    \ intron circularization\n  scope: Purified human proteins with the isolated 26-nt\
    \ intron.\n  context: Figure1c/d; 1 uM 5'-OH/3'-P RNA, 250 nM RTCB, 1 uM Archease,\
    \ 1 mM GTP, 0.5 mM MnCl2, 30 C,\n    ligation buffer with 2 mM MgCl2.\n  family_mapping:\
    \ Human long Archease construct corresponding to Q8IWT0 v2 plus 12 residues; PF01951\
    \ 31-167\n    on the 167-aa reference.\n  taxon: NCBITaxon:9606\n  scope_status:\
    \ MECHANISTIC\n  limitations: Single-substrate assay distinct from cleaved stem-loop\
    \ ligation and from guanylylation\n    conditions. The apparent rate is not a\
    \ cellular flux. S2b ATP substitution is negative and is not\n    generalized\
    \ to archaeal proteins.\n  nodes:\n  - node_id: reaction\n    label: Archease\
    \ plus RTCB and isolated intron with GTP and Mn\n    node_type: ACTIVITY\n   \
    \ grounding:\n    - UniProtKB:Q8IWT0\n    - UniProtKB:Q9Y3I0\n  - node_id: circle\n\
    \    label: Circular 26-nt intron product\n    node_type: STATE\n  edges:\n  -\
    \ edge_id: human-intron-circle\n    subject: reaction\n    predicate: produces\n\
    \    object: circle\n    mechanism: Archease enables RTCB-dependent intron circularization\
    \ with an apparent rate constant of\n      0.015/min; no ligated product is detected\
    \ without Archease in this assay.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:38493148\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10944509/\n      snippet:\
    \ dependent upon addition of Archease\n      explanation: Figure1c/d and ligation\
    \ Methods; three technical replicates and Archease-minus comparison.\n       \
    \ S2b confirms the tested human ATP-negative condition.\n      cache_path: evidence/PF01951/gerber-2024.txt\n\
    \      cache_sha256: abc78d8f41d72e2e58ec8cafa48eae844ef07fecee3823abdffd52494890613c\n\
    - graph_id: human-archease-mutants-2024\n  title: Archease substitutions impair\
    \ activation and ligation\n  scope: Separate D51A and K156A substitutions in the\
    \ human long construct, compared with WT.\n  context: Figure5a activation uses\
    \ 1 uM RTCB/Archease and 80 nM labeled GTP; Figure5b ligation uses 250\n    nM\
    \ RTCB, 1 uM Archease/RNA and 1 mM GTP. Both 30 C and 0.5 mM MnCl2.\n  family_mapping:\
    \ Paper D51A/K156A map to canonical Q8IWT0 v2 D39A/K144A, within PF01951 31-167.\
    \ PDB8BTX\n    entity residues17-183 exactly match the reference, with four tag-derived\
    \ plus twelve construct-extension\n    residues before it.\n  taxon: NCBITaxon:9606\n\
    \  scope_status: PHENOTYPIC\n  limitations: S1 is a WT purity gel, not independent\
    \ mutant-fold verification. Contact geometry supports\n    metal/phosphate roles\
    \ but substitution effects remain molecularly UNRESOLVED. Activation and ligation\n\
    \    are separate measurements, not proof of a measured mediation trajectory.\n\
    \  nodes:\n  - node_id: d51a\n    label: Paper D51A versus WT Archease\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:Q8IWT0\n  - node_id: k156a\n \
    \   label: Paper K156A versus WT Archease\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q8IWT0\n  - node_id: activation\n    label: RTCB guanylylation\
    \ signal\n    node_type: ACTIVITY\n  - node_id: ligation\n    label: Isolated\
    \ intron circularization\n    node_type: ACTIVITY\n  edges:\n  - edge_id: d51a-activation\n\
    \    subject: d51a\n    predicate: decreases\n    object: activation\n    mechanism:\
    \ D51A removes detectable RTCB-associated radiolabel under the matched activation\
    \ conditions;\n      folding and interaction alternatives are not independently\
    \ excluded.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:38493148\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC10944509/\n      snippet: Both variants\
    \ abrogated guanylylation\n      explanation: Figure5a D51A lanes and Methods;\
    \ exact paper-to-reference offset verified.\n      cache_path: evidence/PF01951/gerber-2024.txt\n\
    \      cache_sha256: abc78d8f41d72e2e58ec8cafa48eae844ef07fecee3823abdffd52494890613c\n\
    \  - edge_id: k156a-activation\n    subject: k156a\n    predicate: decreases\n\
    \    object: activation\n    mechanism: K156A removes detectable RTCB-associated\
    \ radiolabel compared with WT; the assay does not\n      isolate phosphate contact\
    \ loss from other mutant effects.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:38493148\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10944509/\n      snippet:\
    \ Both variants abrogated guanylylation\n      explanation: Figure5a K156A lanes\
    \ and Methods; no transfer from RTCB active-site mutants.\n      cache_path: evidence/PF01951/gerber-2024.txt\n\
    \      cache_sha256: abc78d8f41d72e2e58ec8cafa48eae844ef07fecee3823abdffd52494890613c\n\
    \  - edge_id: d51a-ligation\n    subject: d51a\n    predicate: decreases\n   \
    \ object: ligation\n    mechanism: No circular intron product is detected with\
    \ D51A under conditions where WT supports ligation;\n      this is a distinct\
    \ product assay.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:38493148\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC10944509/\n      snippet: Both variants\
    \ abrogated guanylylation\n      explanation: Figure5b D51A lanes and accompanying\
    \ Results directly support the ligation endpoint\n        in addition to the quoted\
    \ activation effect.\n      cache_path: evidence/PF01951/gerber-2024.txt\n   \
    \   cache_sha256: abc78d8f41d72e2e58ec8cafa48eae844ef07fecee3823abdffd52494890613c\n\
    \  - edge_id: k156a-ligation\n    subject: k156a\n    predicate: decreases\n \
    \   object: ligation\n    mechanism: No circular intron product is detected with\
    \ K156A relative to WT; neither an isolated-domain\n      mechanism nor a cellular\
    \ phenotype is measured.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:38493148\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10944509/\n      snippet:\
    \ Both variants abrogated guanylylation\n      explanation: Figure5b K156A lanes\
    \ and accompanying Results; activation and ligation effects are\n        retained\
    \ separately.\n      cache_path: evidence/PF01951/gerber-2024.txt\n      cache_sha256:\
    \ abc78d8f41d72e2e58ec8cafa48eae844ef07fecee3823abdffd52494890613c\n- graph_id:\
    \ ph-archease-ligation-2014\n  title: Pyrococcus Archease accelerates RtcB RNA\
    \ ligation\n  scope: Recombinant P. horikoshii proteins under single-turnover\
    \ conditions.\n  context: Figure2; 70 C, Bis-Tris pH7.0, NaCl 300 mM, MnCl2 0.25\
    \ mM, GTP 0.10 mM, RtcB 5 uM, each 10-nt\n    RNA 1 uM, Archease 100 nM versus\
    \ none.\n  family_mapping: O59205 v1 PH1536, 142 aa, PF01951 4-142; E. coli-produced\
    \ construct inserts L after\n    initial M, while the paper retains native numbering.\n\
    \  taxon: NCBITaxon:70601\n  scope_status: MECHANISTIC\n  limitations: Whole-protein\
    \ activation; Archease alone is not assigned ligase chemistry. Apparent single-turnover\n\
    \    rate, not kcat or cellular flux; only about half the substrate ligates. Two\
    \ experiments. Full Methods/Results\n    and Figure2 image inspected; no raw-data\
    \ reanalysis.\n  nodes:\n  - node_id: addition\n    label: Archease added to PhRtcB\
    \ GTP ligation reaction\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:O59205\n\
    \  - node_id: ligation\n    label: Formation rate of the 20-nt ligation product\n\
    \    node_type: ACTIVITY\n  edges:\n  - edge_id: ph-archease-ligation-rate\n \
    \   subject: addition\n    predicate: increases\n    object: ligation\n    mechanism:\
    \ Addition of 100 nM Archease increases apparent ligation kobs from 0.011 to 0.033/min\
    \ with\n      other reaction components held constant.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24435797\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3973293/\n\
    \      snippet: accelerates\n      explanation: Figure2, RNA ligation Methods\
    \ and corresponding Results; not the later multiple-turnover\n        bacterial\
    \ assay.\n      cache_path: evidence/PF01951/desai-2014.txt\n      cache_sha256:\
    \ 0dd92157e3b40af1071b0efee1e206b8405a38246a5cc756a50f2f80569b128b\n- graph_id:\
    \ ph-archease-rna-guanylylation-2014\n  title: Pyrococcus Archease accelerates\
    \ RNA 3'-phosphate guanylylation\n  scope: Pre-guanylylated P. horikoshii RtcB\
    \ and a trapped RNA intermediate assay.\n  context: Figure3a/b; 5 uM preactivated\
    \ RtcB, 1 uM 2'-F/3'-P RNA, no second RNA fragment, 100 nM Archease\n    versus\
    \ none; 70 C, GTP 0.10 mM and MnCl2 0.25 mM.\n  family_mapping: P. horikoshii\
    \ O59205 v1, PF01951 4-142; whole recombinant Archease with the documented\n \
    \   cloning insertion.\n  taxon: NCBITaxon:70601\n  scope_status: MECHANISTIC\n\
    \  limitations: Modified substrate traps RNA-ppG and prevents normal intramolecular\
    \ reaction. This is RNA\n    guanylylation, not the human RTCB labeling assay.\
    \ Atomic mechanism and physiological RNA substrate\n    remain unmeasured; Figure3\
    \ visually inspected without raw-data reanalysis.\n  nodes:\n  - node_id: addition\n\
    \    label: Archease with pre-guanylylated PhRtcB and modified RNA\n    node_type:\
    \ ACTIVITY\n    grounding:\n    - UniProtKB:O59205\n  - node_id: rnappg\n    label:\
    \ RNA-ppG intermediate formation rate\n    node_type: ACTIVITY\n  edges:\n  -\
    \ edge_id: ph-archease-rnappg-rate\n    subject: addition\n    predicate: increases\n\
    \    object: rnappg\n    mechanism: Archease raises apparent RNA-ppG formation\
    \ kobs from 0.018 to 0.063/min in the modified-substrate\n      assay, separating\
    \ this transfer from final ligation.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:24435797\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3973293/\n      snippet:\
    \ accelerates\n      explanation: Figure3a/b, RNA guanylylation Methods and Results;\
    \ two experiments with the 3-prime\n        RNA fragment excluded.\n      cache_path:\
    \ evidence/PF01951/desai-2014.txt\n      cache_sha256: 0dd92157e3b40af1071b0efee1e206b8405a38246a5cc756a50f2f80569b128b\n\
    - graph_id: ph-archease-purine-cofactors-2014\n  title: Pyrococcus Archease broadens\
    \ tested purine cofactor utilization\n  scope: Separate ATP, dGTP and ITP conditions\
    \ for P. horikoshii RtcB.\n  context: Figure4a/b; 30 min at 70 C, 5 uM RtcB, each\
    \ RNA half 1 uM, 100 nM Archease, MnCl2 0.25 mM and\n    the specified NTP 0.10\
    \ mM; matched Archease-minus comparisons.\n  family_mapping: O59205 v1, PH1536,\
    \ PF01951 4-142; the same whole recombinant protein as the PhRtcB ligation\n \
    \   assay.\n  taxon: NCBITaxon:70601\n  scope_status: MECHANISTIC\n  limitations:\
    \ Each edge has its own nucleotide condition; these are not independent sufficient\
    \ causes\n    without RtcB and substrate. CTP/UTP are negative. ATP kinetics elsewhere\
    \ use 800 nM Archease. Human\n    and Thermus ATP-negative results limit cross-species\
    \ transfer. Figure4 visually inspected; no raw-data\n    reanalysis.\n  nodes:\n\
    \  - node_id: atp\n    label: Archease added to PhRtcB reaction with ATP\n   \
    \ node_type: ACTIVITY\n    grounding:\n    - UniProtKB:O59205\n  - node_id: dgtp\n\
    \    label: Archease added to PhRtcB reaction with dGTP\n    node_type: ACTIVITY\n\
    \    grounding:\n    - UniProtKB:O59205\n  - node_id: itp\n    label: Archease\
    \ added to PhRtcB reaction with ITP\n    node_type: ACTIVITY\n    grounding:\n\
    \    - UniProtKB:O59205\n  - node_id: atp_product\n    label: Ligated RNA in the\
    \ ATP condition\n    node_type: STATE\n  - node_id: dgtp_product\n    label: Ligated\
    \ RNA in the dGTP condition\n    node_type: STATE\n  - node_id: itp_product\n\
    \    label: Ligated RNA in the ITP condition\n    node_type: STATE\n  edges:\n\
    \  - edge_id: ph-atp-ligation\n    subject: atp\n    predicate: increases\n  \
    \  object: atp_product\n    mechanism: Archease enables effective ATP-supported\
    \ ligation in the tested PhRtcB reaction; this does\n      not establish ATP delivery\
    \ or binding by Archease.\n    directness: DIRECT\n    support: OBSERVED\n   \
    \ evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:24435797\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3973293/\n      snippet:\
    \ enabled efficient utilization\n      explanation: Figure4a/b ATP comparison\
    \ at 100 nM Archease, distinct from the 800 nM kinetic experiments.\n      cache_path:\
    \ evidence/PF01951/desai-2014.txt\n      cache_sha256: 0dd92157e3b40af1071b0efee1e206b8405a38246a5cc756a50f2f80569b128b\n\
    \  - edge_id: ph-dgtp-ligation\n    subject: dgtp\n    predicate: increases\n\
    \    object: dgtp_product\n    mechanism: Archease increases the dGTP-supported\
    \ product yield by approximately tenfold in the 30-minute\n      assay; the measured\
    \ endpoint is not a binding constant.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:24435797\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3973293/\n      snippet:\
    \ enabled efficient utilization\n      explanation: Figure4a/b dGTP lanes and\
    \ Results; same RNA, Mn and protein concentrations within this\n        comparison.\n\
    \      cache_path: evidence/PF01951/desai-2014.txt\n      cache_sha256: 0dd92157e3b40af1071b0efee1e206b8405a38246a5cc756a50f2f80569b128b\n\
    \  - edge_id: ph-itp-ligation\n    subject: itp\n    predicate: increases\n  \
    \  object: itp_product\n    mechanism: Archease increases ITP-supported product\
    \ yield by approximately eightfold in the matched\n      30-minute reaction.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:24435797\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3973293/\n\
    \      snippet: enabled efficient utilization\n      explanation: Figure4a/b ITP\
    \ lanes and corresponding Results; does not imply utilization of every\n     \
    \   purine analogue.\n      cache_path: evidence/PF01951/desai-2014.txt\n    \
    \  cache_sha256: 0dd92157e3b40af1071b0efee1e206b8405a38246a5cc756a50f2f80569b128b\n\
    - graph_id: u2os-archease-disruption-day3-2025\n  title: Archease disruption changes\
    \ RNA-processing readouts in U2OS cells\n  scope: Sorted human U2OS populations\
    \ after transient Archease-targeting CRISPR/Cas9 versus control vector.\n  context:\
    \ Day3 after sorting; Tyr-GTA Northern on 2.5 ug RNA. Separate stress assays use\
    \ 10 ug/ml tunicamycin\n    for 4 h with GAPDH-normalized qRT-PCR; three independent\
    \ samples.\n  family_mapping: Whole human Archease locus, represented by Q8IWT0\
    \ v2 with PF01951 31-167. S6H shows\n    a majority one-base insertion, not a\
    \ uniform clone. No expressed isoform or isolated domain is selectively\n    assigned.\n\
    \  taxon: NCBITaxon:9606\n  scope_status: PHENOTYPIC\n  limitations: S6I protein\
    \ reduction and ACTB controls support disruption; residual protein and population\n\
    \    heterogeneity remain. No Archease reintroduction rescue or directly measured\
    \ mediation from ligation\n    to ERDJ4. Day3 mature-tRNA abundance is not claimed\
    \ to decrease.\n  nodes:\n  - node_id: disruption\n    label: Archease-targeted\
    \ U2OS population versus control\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q8IWT0\n  - node_id: trna_ratio\n    label: Tyr-GTA intermediate\
    \ to mature tRNA ratio at day3\n    node_type: PHENOTYPE\n  - node_id: xbp1_ratio\n\
    \    label: XBP1s to XBP1u ratio after tunicamycin\n    node_type: PHENOTYPE\n\
    \  - node_id: erdj4\n    label: ERDJ4 RNA induction after tunicamycin\n    node_type:\
    \ PHENOTYPE\n  edges:\n  - edge_id: u2os-disruption-trna-ratio\n    subject: disruption\n\
    \    predicate: increases\n    object: trna_ratio\n    mechanism: The targeted\
    \ population accumulates a higher Tyr-GTA intermediate/mature ratio, consistent\n\
    \      with impaired processing but not a direct cellular measurement of the biochemical\
    \ intermediate-transfer\n      mechanism.\n    directness: UNRESOLVED\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: doi:10.1038/s42003-025-07523-z\n\
    \      source_url: https://www.nature.com/articles/s42003-025-07523-z\n      snippet:\
    \ splicing defects\n      explanation: Figure3F/G and S6G-I visually inspected;\
    \ day3 Northern ratio, not total disappearance\n        of mature RNA.\n     \
    \ cache_path: evidence/PF01951/suzuki-2025.txt\n      cache_sha256: d3e772eaf174d79f070d0c77f3a15af017a6a108dfc625efc2b0876c5e50cf68\n\
    \  - edge_id: u2os-disruption-xbp1-ratio\n    subject: disruption\n    predicate:\
    \ decreases\n    object: xbp1_ratio\n    mechanism: Archease targeting lowers\
    \ the stress-induced XBP1s/XBP1u RNA ratio under the tested tunicamycin\n    \
    \  condition; no purified-reaction rate is assigned to this cellular endpoint.\n\
    \    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: doi:10.1038/s42003-025-07523-z\n      source_url:\
    \ https://www.nature.com/articles/s42003-025-07523-z\n      snippet: splicing\
    \ defects\n      explanation: Figure3D at 4 h and qRT-PCR Methods; the RTCB and\
    \ DDX1 interventions remain separate\n        experiments.\n      cache_path:\
    \ evidence/PF01951/suzuki-2025.txt\n      cache_sha256: d3e772eaf174d79f070d0c77f3a15af017a6a108dfc625efc2b0876c5e50cf68\n\
    \  - edge_id: u2os-disruption-erdj4\n    subject: disruption\n    predicate: decreases\n\
    \    object: erdj4\n    mechanism: Targeting Archease reduces ERDJ4 RNA induction\
    \ after 4 h tunicamycin relative to control;\n      the transcriptional relay\
    \ is not directly perturbed in this experiment.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: doi:10.1038/s42003-025-07523-z\n      source_url: https://www.nature.com/articles/s42003-025-07523-z\n\
    \      snippet: splicing defects\n      explanation: Figure3H and Methods; a separately\
    \ measured output, not an observed XBP1-to-ERDJ4 mediation\n        edge.\n  \
    \    cache_path: evidence/PF01951/suzuki-2025.txt\n      cache_sha256: d3e772eaf174d79f070d0c77f3a15af017a6a108dfc625efc2b0876c5e50cf68\n\
    - graph_id: u2os-archease-disruption-day8-2025\n  title: Mature Tyr-GTA tRNA declines\
    \ later after Archease disruption\n  scope: The same U2OS perturbation design\
    \ sampled eight days after sorting.\n  context: S7B/D; 2.5 ug total RNA, Tyr-GTA\
    \ 5'-exon Northern and Archease/ACTB immunoblots. Distinct from\n    the day3\
    \ ratio comparison.\n  family_mapping: Whole Archease-locus disruption; Q8IWT0\
    \ v2 reference with PF01951 31-167, not a domain-specific\n    allele or uniform\
    \ biallelic clone.\n  taxon: NCBITaxon:9606\n  scope_status: PHENOTYPIC\n  limitations:\
    \ Qualitative band reduction without a reported numerical fold change or panel-specific\
    \ significance.\n    Residual mature RNA persists; residual protein, RNA turnover\
    \ and alternative processing remain possible.\n    No universal essentiality or\
    \ complete RNA loss is inferred.\n  nodes:\n  - node_id: disruption\n    label:\
    \ Archease-targeted U2OS population at day8\n    node_type: PERTURBATION\n   \
    \ grounding:\n    - UniProtKB:Q8IWT0\n  - node_id: mature\n    label: Mature Tyr-GTA\
    \ tRNA band at day8\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: u2os-day8-mature-trna\n\
    \    subject: disruption\n    predicate: decreases\n    object: mature\n    mechanism:\
    \ The mature Tyr-GTA band is reduced in the targeted population at the later sampling\
    \ time,\n      while a residual band remains; the contribution of RNA turnover\
    \ is not measured.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: doi:10.1038/s42003-025-07523-z\n\
    \      source_url: https://www.nature.com/articles/s42003-025-07523-z\n      snippet:\
    \ reduction of the mature tRNA\n      explanation: S7B/D and corresponding Results\
    \ visually/textually inspected; no numerical effect size\n        is invented\
    \ from the blot.\n      cache_path: evidence/PF01951/suzuki-2025.txt\n      cache_sha256:\
    \ d3e772eaf174d79f070d0c77f3a15af017a6a108dfc625efc2b0876c5e50cf68\ncuration_events:\n\
    - timestamp: '2026-10-12T08:52:08Z'\n  curator: Codex\n  action: CREATE\n  outcome:\
    \ changed\n  summary: Curate scoped Archease activation, ligation and RNA-processing\
    \ graphs\n  history_record: history/records/PF01951/2026-10-12T085208Z-codex-b29ac6.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Frozen Archease/former DUF101, IPR023572, EX_DUF and UNSCORED remain unchanged.
    Human Q8IWT0 v2 is167 aa with PF01951 31-167. Historical A8K0B5 resolves to it;
    the179-aa paper construct corresponds to the current12-residue N-terminal extension,
    with different historical isoform naming. PDB8BTX entity17-183 exactly equals
    the current167-aa sequence; paperD51/K156 map toD39/K144, verified by residue
    identity. O59205v1 is PH1536,142 aa, PF01951 4-142; Desai2014 insertsL after the
    initialM but retains native numbering. U2OS disruption does not identify a selectively
    tested isoform. Remaining Thermus construct identity is explicitly unresolved,
    not adopted as a native graph.
  target_ids:
  - PF01951
  evidence_ids:
  - identity
  - primary
  - archaeal-reactions
  - cellular-disruption
  - source-coverage
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Human activation is distinct from cleaved-XBP1 ligation and isolated-intron
    circularization, with different RNA/protein/nucleotide concentrations. The two
    Archease substitutions have separate activation and ligation outputs; WT purity
    is not mutant-fold verification. The PhRtcB RNA-ppG assay uses pre-guanylylated
    enzyme and modified substrate, not the human protein-labeling readout. ATP/dGTP/ITP
    effects retain separate nucleotide contexts and the100 nM comparison is not pooled
    with800 nM ATP kinetics. U2OS day3 tRNA ratio and stress RNA outputs remain separate
    from the later mature-tRNA reduction; heterogeneous targeting and residual protein
    do not support complete knockout or universal essentiality. No unmeasured mediation
    chain joins these systems.
  target_ids:
  - PF01951
  evidence_ids:
  - primary
  - native
  - archaeal-reactions
  - cellular-disruption
  - source-coverage
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Remaining Archease mutant and RtcB-rescue experiments, bacterial turnover
    and Thermus clone identity, PAB1946 methyltransferase support, Popow/Jurkin original
    cellular evidence, fly allele/localization/rescue, yeast complementation, PYROXD1
    and Danio studies remain open. Acquired full texts do not count as completed reviews.
    No exhaustive family membership, primary-literature census, domain-only mechanism,
    raw-data reanalysis or independent expert endorsement.
  target_ids:
  - PF01951
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01951-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Extend remaining Archease contexts without cross-species or construct transfers
  description: Continue PF01951 primary review before treating the family as complete.
    Resolve Thermus strain/clone mapping, inspect archaeal mutant and RtcB-rescue
    figures and controls, finish Auxilien2007 Methods and assay images, and review
    original human and fly perturbations with exact sequence/allele mapping. Keep
    species-specific nucleotide negatives, modified versus native RNA, heterogeneous
    cell populations and independent rescue experiments explicit. Append actual history
    and successor review after each supported addition; all earlier family follow-ups
    remain open.
  target_ids:
  - PF01951
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - archaeal-reactions
  - cellular-disruption
  - source-coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01951.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Continue PF01951 primary review before treating the family as complete.
    Resolve Thermus strain/clone mapping, inspect archaeal mutant and RtcB-rescue
    figures and controls, finish Auxilien2007 Methods and assay images, and review
    original human and fly perturbations with exact sequence/allele mapping. Keep
    species-specific nucleotide negatives, modified versus native RNA, heterogeneous
    cell populations and independent rescue experiments explicit. Append actual history
    and successor review after each supported addition; all earlier family follow-ups
    remain open.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01951
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Gerber2024 full Methods and relevant Results with Figures1/5 and S1/S2 inspected;
  Desai2014 full Methods/Results with Figures2/3/4 inspected from the public author
  PDF; Suzuki2025 relevant Methods/Results with Figure3 and S6/S7 inspected. Desai2015
  full Methods/Results read but figures only rendered, not visually audited. Auxilien2007
  selected author-copy sections read, not full figure/method coverage. Francis2022
  abstract and rescue caption only; Popow2014 HTML and Desai2014 supplement obtained
  but not fully reviewed. No raw-data reanalysis or independent expert review.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
