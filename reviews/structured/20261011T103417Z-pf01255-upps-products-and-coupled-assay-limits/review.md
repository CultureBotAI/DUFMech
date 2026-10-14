# Scoped scientific self-review of UppS products and coupled-assay limits

- Review: 20261011T103417Z-pf01255-upps-products-and-coupled-assay-limits
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T10:34:01Z
- Finished UTC: 2026-10-11T10:34:17Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Three graphs retain one DIRECT OBSERVED long-chain prenyl-product effect and two UNRESOLVED OBSERVED coupled-signal effects. Residual detergent/magnesium omission output and unshown C50/C55-compatible TLC constrain stronger claims. Historical Q47675 maps by archived sequence to P60472. Partial scientific self-review; IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01255 Prenyltransf/former UPF0015, next accession-ordered SEEDED family, assessed through Apfel 1999 and exact historical/reference sequence mapping; Micrococcus and Bos-12 studies remain separate leads.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01255 | data/families/PF01255.yaml | generated | PF01255 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01255 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01255.

Q47675 is demerged to several entries, but its archived UPI0000137D08 sequence exactly matches P60472/ispU/uppS/yaeS, 253 aa and sequence version 1. InterPro maps PF01255 to 24-244 and agrees with UniProt. The historical upstream GTG and one-/two-Met forms are explicit; full clone and template strain remain unresolved. Frozen M. luteus O82827 metadata does not identify the E. coli assay protein.

### Directed effects and limits

graph: supported. Targets: PF01255.

Only the product-forming edge is DIRECT and MECHANISTIC. Triton and magnesium effects are PHENOTYPIC with UNRESOLVED directness because the measured output includes yeast pyrophosphatase and color chemistry. Both retained dose comparisons have directionally supported nonzero omission controls; neither becomes absolute dependence or monotonic activation. The graphs do not join biochemical effects to pneumococcal growth or proposed catalytic microsteps.

### Remaining family coverage

completeness: concern. Targets: PF01255.

Exact historical clones, panel-specific UppS doses, the product chromatogram and complete TLC conditions remain unresolved. The printed color-reagent notation needs reconciliation. M. luteus 1998 is abstract-only; Bos-12 2001 was inspected only through the abstract and selected Methods, without mutant figures or sequence-coordinate transfer. Other bacterial, eukaryotic and partner-dependent contexts are not comprehensively reviewed.

## Findings

### additional-contexts: Resolve UppS product and coupling evidence before mechanism extension

minor / open / confirmed; issue key: pf01255-causal-context-coverage.

Obtain the original product data and clone sequences, separate prenyltransferase activity from coupled detection effects, and review Bos-12 mutants with explicit numbering before residue-level claims. Assess additional members and eukaryotic partners from their own primary experiments. Retain successor reviews and preserve source-label, product-mixture and residual-activity qualifications.

## Recommended Actions And Acceptance Checks

### extend-contexts

Obtain the original product data and clone sequences, separate prenyltransferase activity from coupled detection effects, and review Bos-12 mutants with explicit numbering before residue-level claims. Assess additional members and eukaryotic partners from their own primary experiments. Retain successor reviews and preserve source-label, product-mixture and residual-activity qualifications.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC93402/; Main expression/purification and assay Methods, relevant Results and Discussion; Figure 6 visually inspected | supports | Recombinant untagged E. coli UppS forms radiolabeled prenyl products whose reported dephosphorylated TLC products comigrate with C50/C55 standards. Figure 6 shows increased coupled phosphate output with 0.01% Triton or 0.5 mM MgCl2 relative to omission, with residual output and nonmonotonic higher-dose responses. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/P60472/entry/pfam/PF01255/; Accession and domain locations; paired UniProt identity facts | supports | Q47675 is demerged to several entries, but its archived UPI0000137D08 sequence exactly matches P60472/ispU/uppS/yaeS, 253 aa and sequence version 1. InterPro maps PF01255 to 24-244 and agrees with UniProt. The historical upstream GTG and one-/two-Met forms are explicit; full clone and template strain remain unresolved. Frozen M. luteus O82827 metadata does not identify the E. coli assay protein. |
| archived-identity | https://rest.uniprot.org/uniprotkb/Q47675.json; Demerged successors and archived UPI0000137D08 sequence comparison | supports | Current P60472 matches the archived historical sequence exactly; this is reference identity, not a reconstructed historical clone. |
| micrococcus-lead | https://pubmed.ncbi.nlm.nih.gov/9677368/; Complete primary abstract retrieved through Europe PMC | supports | Original Micrococcus luteus cloning and purification study needs separate full-method and product assessment before adding its edges. |
| bos12-lead | https://doi.org/10.1074/jbc.M106747200; Institutional primary PDF abstract and selected Methods | supports | Bos-12 and FXa-cleaved constructs differ from the adopted 1999 preparation; mutant product figures and sequence-coordinate transfer remain unreviewed. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01255 | data/families/PF01255.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Figure 6 was visually checked; other 1999 figures, raw measurements and the unshown product TLC were not independently examined. The 2001 primary PDF was read only for its abstract and selected Methods, not complete Results or product images. Same-condition direct Mg or detergent mechanisms are not established by the coupled output.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T103417Z-pf01255-upps-products-and-coupled-assay-limits
title: Scoped scientific self-review of UppS products and coupled-assay limits
started_at: '2026-10-11T10:34:01Z'
finished_at: '2026-10-11T10:34:17Z'
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
summary: Three graphs retain one DIRECT OBSERVED long-chain prenyl-product effect
  and two UNRESOLVED OBSERVED coupled-signal effects. Residual detergent/magnesium
  omission output and unshown C50/C55-compatible TLC constrain stronger claims. Historical
  Q47675 maps by archived sequence to P60472. Partial scientific self-review; IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01255.yaml
    sha256: 0cfad83b2c6472e20a5083423410d7ec59b7b895437c9569df9433ae5b755990
    role: context
  - path: data/families/PF01255.yaml
    sha256: ef60a3d90dbb211dbc14d55e17dc5f1ae8bb90ff0ee4e8a9739ea56761c7c678
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
  - path: evidence/PF01255/apfel-1999-upps.txt
    role: context
    sha256: bb2db41b12af36570d3c29fa6ba93be94ed598397151f87f3f2c032acbe1dfa7
  - path: evidence/PF01255/UppS-identity.txt
    role: context
    sha256: 476c15e0589197930ba58b3706efd489cd8db625c42bbd0022f92aa3d3bde006
  - path: evidence/PF01255/upps-coverage-leads.txt
    role: context
    sha256: ac6ef8ef7fdd736b326caa12371481923a81c54c0924756d3b6012b8b7686242
targets:
- target_id: PF01255
  path: data/families/PF01255.yaml
  label: PF01255
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01255.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 0cf79f863e6bf59c84b018c4fdb86545da852d3a9c004e144e40a8c81cb010cb
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01255 Prenyltransf/former UPF0015, next accession-ordered SEEDED family,
    assessed through Apfel 1999 and exact historical/reference sequence mapping; Micrococcus
    and Bos-12 studies remain separate leads.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01255
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Exact historical clones, panel-specific UppS doses, the product chromatogram
      and complete TLC conditions remain unresolved. The printed color-reagent notation
      needs reconciliation. M. luteus 1998 is abstract-only; Bos-12 2001 was inspected
      only through the abstract and selected Methods, without mutant figures or sequence-coordinate
      transfer. Other bacterial, eukaryotic and partner-dependent contexts are not
      comprehensively reviewed.
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
  - PF01255
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC93402/
  locator: Main expression/purification and assay Methods, relevant Results and Discussion;
    Figure 6 visually inspected
  accessed_at: '2026-10-11T10:34:17Z'
  support: supports
  snapshot_sha256: bb2db41b12af36570d3c29fa6ba93be94ed598397151f87f3f2c032acbe1dfa7
  summary: Recombinant untagged E. coli UppS forms radiolabeled prenyl products whose
    reported dephosphorylated TLC products comigrate with C50/C55 standards. Figure
    6 shows increased coupled phosphate output with 0.01% Triton or 0.5 mM MgCl2 relative
    to omission, with residual output and nonmonotonic higher-dose responses.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P60472/entry/pfam/PF01255/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T10:34:17Z'
  support: supports
  snapshot_sha256: 476c15e0589197930ba58b3706efd489cd8db625c42bbd0022f92aa3d3bde006
  summary: Q47675 is demerged to several entries, but its archived UPI0000137D08 sequence
    exactly matches P60472/ispU/uppS/yaeS, 253 aa and sequence version 1. InterPro
    maps PF01255 to 24-244 and agrees with UniProt. The historical upstream GTG and
    one-/two-Met forms are explicit; full clone and template strain remain unresolved.
    Frozen M. luteus O82827 metadata does not identify the E. coli assay protein.
- evidence_id: archived-identity
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q47675.json
  locator: Demerged successors and archived UPI0000137D08 sequence comparison
  summary: Current P60472 matches the archived historical sequence exactly; this is
    reference identity, not a reconstructed historical clone.
  accessed_at: '2026-10-11T10:34:17Z'
  support: supports
  snapshot_sha256: 476c15e0589197930ba58b3706efd489cd8db625c42bbd0022f92aa3d3bde006
- evidence_id: micrococcus-lead
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/9677368/
  locator: Complete primary abstract retrieved through Europe PMC
  summary: Original Micrococcus luteus cloning and purification study needs separate
    full-method and product assessment before adding its edges.
  accessed_at: '2026-10-11T10:34:17Z'
  support: supports
  snapshot_sha256: ac6ef8ef7fdd736b326caa12371481923a81c54c0924756d3b6012b8b7686242
- evidence_id: bos12-lead
  kind: primary_source
  reference: https://doi.org/10.1074/jbc.M106747200
  locator: Institutional primary PDF abstract and selected Methods
  summary: Bos-12 and FXa-cleaved constructs differ from the adopted 1999 preparation;
    mutant product figures and sequence-coordinate transfer remain unreviewed.
  accessed_at: '2026-10-11T10:34:17Z'
  support: supports
  snapshot_sha256: ac6ef8ef7fdd736b326caa12371481923a81c54c0924756d3b6012b8b7686242
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T10:34:17Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01255
  kind: record_content
  reference: data/families/PF01255.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T10:34:17Z'
  support: context_only
  snapshot_sha256: ef60a3d90dbb211dbc14d55e17dc5f1ae8bb90ff0ee4e8a9739ea56761c7c678
  quote: "id: Pfam:PF01255\npfam_id: PF01255\nname: Putative undecaprenyl diphosphate\
    \ synthase\nshort_name: Prenyltransf\nseed_status: EX_DUF\ncharacterization_status:\
    \ UNSCORED\ncuration_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01255\n\
    counters:\n  proteins: 31979\n  matches: 33207\n  proteomes: 21625\n  taxa: 34832\n\
    \  structures: 103\n  alphafold_models: 22269\n  domain_architectures: 142\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR001441\ndescription: Previously known as uncharacterized\
    \ protein family UPF0015, a single member of this family\n  [swissprot:O82827]\
    \ has been identified as an undecaprenyl diphosphate synthase [[cite:PUB00003021]].\n\
    curation_history: history/records/PF01255\ndiscussions:\n- discussion_id: upps-product-clone-and-coupling-coverage\n\
    \  prompt: Resolve original clone and product data, separate coupled-assay effects,\
    \ and extend cis-prenyltransferase\n    member coverage.\n  kind: CURATION_TODO\n\
    \  status: OPEN\n  rationale: Product formation and two coupled-assay comparisons\
    \ do not establish a complete residue-level\n    mechanism. Frozen UPF0015 metadata\
    \ and the M. luteus example remain distinct from the adopted E. coli\n    preparation.\
    \ Operon-level essentiality, product-length variants and eukaryotic homologs need\
    \ independent\n    scope and evidence.\n  evidence:\n  - reference: PMID:9882662\n\
    \    supports: PARTIAL\n    evidence_source: full_text\n    explanation: Figure\
    \ 6 was visually inspected; product TLC is reported but unshown. The pneumococcal\n\
    \      Results and Discussion retain downstream-operon and promoter-strength caveats\
    \ and are not adopted\n      as E. coli effects.\n  - reference: PMID:9677368\n\
    \    supports: PARTIAL\n    evidence_source: abstract\n    explanation: Original\
    \ M. luteus cloning study is an inspected abstract lead, not full experimental\n\
    \      coverage.\n  - reference: doi:10.1074/jbc.M106747200\n    supports: PARTIAL\n\
    \    evidence_source: selected_full_text\n    explanation: Abstract and selected\
    \ Methods identify Bos-12, FXa processing and mutant/product experiments.\n  \
    \    Mutant figures and exact sequence-coordinate transfer were not reviewed,\
    \ so no L137A or tunnel-motion\n      edge is adopted.\n  posed_by: Codex\n  posed_date:\
    \ '2026-10-11'\n  notes: Preserve residual output rather than claiming absolute\
    \ cofactor dependence. Obtain the original\n    TLC and full clone sequences,\
    \ and inspect later product-specificity and partner-dependent eukaryotic\n   \
    \ contexts. Partial scientific self-review; status remains IN_PROGRESS.\ncausal_graphs:\n\
    - graph_id: ecoli-upps-prenyl-product-formation\n  title: Recombinant E. coli\
    \ UppS forms long-chain prenyl products\n  scope: Untagged recombinant E. coli\
    \ UppS in Apfel 1999; intact protein rather than an isolated PF01255\n    segment\
    \ or every cis-prenyltransferase.\n  context: The pUppS-wt-EC construct uses the\
    \ upstream GTG start and is expressed in BL21(DE3)(pLysS),\n    then purified\
    \ by ammonium sulfate fractionation, Phospho-Ultrogel and Superdex 200. The standard\
    \ radioactive\n    assay uses 100 ul, 100 mM Tris-HCl pH 7.5, 0.2 mM MgCl2, 0.05%\
    \ Triton X-100, 10 uM FPP and 10 uM radiolabeled\n    IPP for 30 min at 35 C.\
    \ Companion product identification uses potato acid phosphatase and reversed-phase\n\
    \    TLC; its precise incubation recipe is not separately specified.\n  family_mapping:\
    \ Historical Q47675/YAES_ECOLI has demerged into several entries. Its archived\
    \ UPI0000137D08\n    sequence exactly matches the 253-aa K12 reference UniProtKB:P60472\
    \ (ispU/uppS/yaeS), sequence version\n    1, and the InterPro sequence. PF01255\
    \ maps to residues 24-244 inclusive. This reference mapping does\n    not establish\
    \ the historical PCR donor strain or all clone junctions; BL21 is the expression\
    \ host.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:562\n  limitations: Reported\
    \ major dephosphorylated products comigrate with both undecaprenol and decaprenol;\n\
    \    C30-C45 products also occur. TLC is described as data not shown, not independently\
    \ inspected chromatography.\n    No exclusive C55 product, stereochemical remeasurement,\
    \ eight resolved condensation microsteps, isolated-domain\n    sufficiency or\
    \ cellular peptidoglycan flux is claimed. Native one-/two-Met forms and tagged\
    \ preparations\n    are not silently equated with the adopted recombinant preparation.\n\
    \  nodes:\n  - node_id: upps-with-fpp-ipp\n    label: Untagged recombinant UppS\
    \ with FPP and IPP in the complete assay\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:P60472\n  - node_id: long-chain-prenyl-products\n    label: Radiolabeled\
    \ prenyl products with major C50/C55-compatible TLC products after dephosphorylation\n\
    \    node_type: STATE\n  edges:\n  - edge_id: upps-produces-long-chain-prenyl-products\n\
    \    subject: upps-with-fpp-ipp\n    predicate: produces\n    object: long-chain-prenyl-products\n\
    \    mechanism: Purified recombinant protein incorporates radiolabeled IPP into\
    \ extractable prenyl products\n      with FPP as cosubstrate. Reported phosphatase-treated\
    \ product mobilities support long-chain product\n      formation but not a single\
    \ exclusive chain length or a directly observed catalytic trajectory.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:9882662\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC93402/\n\
    \      snippet: same mobility\n      explanation: Assay Methods and the structural/functional\
    \ analysis Results connect purified protein\n        with radiolabeled product\
    \ formation and the reported C50/C55-compatible TLC assignment. The product\n\
    \        chromatogram itself is not shown.\n      cache_path: evidence/PF01255/apfel-1999-upps.txt\n\
    \      cache_sha256: bb2db41b12af36570d3c29fa6ba93be94ed598397151f87f3f2c032acbe1dfa7\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P60472/entry/pfam/PF01255/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P60472/entry/pfam/PF01255/\n\
    \      snippet: 'Pfam:PF01255; domain interval: 24-244, inclusive.'\n      explanation:\
    \ Sequence-based resolution of the cited accession establishes the reference family\
    \ interval,\n        not the assay's chemistry or complete historical clone identity.\n\
    \      cache_path: evidence/PF01255/UppS-identity.txt\n      cache_sha256: 476c15e0589197930ba58b3706efd489cd8db625c42bbd0022f92aa3d3bde006\n\
    - graph_id: ecoli-upps-coupled-detergent-response\n  title: Triton addition increases\
    \ the UppS coupled-assay signal\n  scope: Recombinant untagged E. coli UppS together\
    \ with yeast inorganic pyrophosphatase in Apfel 1999\n    Figure 6; the observed\
    \ coupled output is not assigned to an isolated UppS elementary step.\n  context:\
    \ Compare 0.01% Triton X-100 with omission in the coupled phosphate assay. Other\
    \ standard components\n    are 100 mM Tris-HCl pH 7.5, 0.2 mM MgCl2, 10 uM IPP,\
    \ 10 uM FPP and 0.003 U S. cerevisiae inorganic\n    pyrophosphatase in 100 ul\
    \ for 30 min at 35 C. Malachite-green A660 is calibrated against phosphate;\n\
    \    Figure 6 normalizes each series to its maximum. Exact UppS dose is not given\
    \ in the caption.\n  family_mapping: Intact recombinant UppS is mapped through\
    \ historical Q47675 and its exact archived sequence\n    to P60472, PF01255 24-244.\
    \ The yeast coupling enzyme is a required assay partner, not a PF01255 member.\n\
    \    Reference identity does not establish every historical expression junction.\n\
    \  scope_status: PHENOTYPIC\n  limitations: Figure 6 shows residual signal without\
    \ detergent, and higher detergent concentrations lower\n    the signal again.\
    \ This is not absolute detergent dependence, monotonic activation, or a cellular\
    \ membrane\n    mechanism. Solubilization, product release, the coupling enzyme\
    \ and detection chemistry are not separately\n    resolved. The Methods color-reagent\
    \ acid notation remains uncorrected; raw triplicates were not reanalyzed.\n  nodes:\n\
    \  - node_id: triton-point-zero-one-percent\n    label: 0.01% Triton X-100 rather\
    \ than omission in the complete coupled reaction\n    node_type: PERTURBATION\n\
    \  - node_id: coupled-phosphate-output\n    label: Normalized phosphate-dependent\
    \ A660 output of the UppS/pyrophosphatase assay\n    node_type: PHENOTYPE\n  edges:\n\
    \  - edge_id: triton-increases-coupled-output\n    subject: triton-point-zero-one-percent\n\
    \    predicate: increases\n    object: coupled-phosphate-output\n    mechanism:\
    \ The 0.01% detergent condition yields greater normalized output than the zero-detergent\n\
    \      condition in the visually inspected Figure 6. The effect is retained at\
    \ assay level because the\n      molecular step responsible is not independently\
    \ isolated.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:9882662\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC93402/\n      snippet: residual activity\n\
    \      explanation: Figure 6 and its caption support the direction, normalization\
    \ and nonzero omission\n        control; coupled-assay Methods establish the second\
    \ enzyme and optical endpoint.\n      cache_path: evidence/PF01255/apfel-1999-upps.txt\n\
    \      cache_sha256: bb2db41b12af36570d3c29fa6ba93be94ed598397151f87f3f2c032acbe1dfa7\n\
    - graph_id: ecoli-upps-coupled-magnesium-response\n  title: Magnesium addition\
    \ increases the UppS coupled-assay signal\n  scope: Recombinant untagged E. coli\
    \ UppS plus yeast inorganic pyrophosphatase in Apfel 1999 Figure 6,\n    separate\
    \ from the detergent series and product-identification experiment.\n  context:\
    \ Compare 0.5 mM MgCl2 with omission. Other standard coupled-assay components\
    \ are 100 mM Tris-HCl\n    pH 7.5, 0.05% Triton X-100, 10 uM each IPP/FPP and\
    \ 0.003 U yeast inorganic pyrophosphatase in 100\n    ul, 35 C for 30 min. Phosphate-dependent\
    \ A660 output is normalized to the maximum within this series;\n    the enzyme\
    \ dose and raw triplicates remain unverified.\n  family_mapping: Historical Q47675\
    \ maps by archived sequence identity to E. coli reference P60472, PF01255\n  \
    \  residues 24-244. The adopted construct is the untagged recombinant protein,\
    \ not M. luteus O82827 from\n    the frozen family description or an isolated\
    \ domain.\n  scope_status: PHENOTYPIC\n  limitations: Residual signal without\
    \ added MgCl2 is visible. Both the prenyltransferase and coupling\n    reaction\
    \ can contribute to the Mg-dependent output; direct UppS metal occupancy or catalytic\
    \ metal\n    stoichiometry is not shown. The nonmonotonic concentration series\
    \ is not generalized to all doses\n    or to in-vivo growth. No edge connects\
    \ this mixed-enzyme optical assay to pneumococcal essentiality.\n  nodes:\n  -\
    \ node_id: magnesium-point-five-millimolar\n    label: 0.5 mM MgCl2 rather than\
    \ omission in the complete coupled reaction\n    node_type: PERTURBATION\n  -\
    \ node_id: magnesium-series-phosphate-output\n    label: Normalized phosphate-dependent\
    \ A660 output in the magnesium series\n    node_type: PHENOTYPE\n  edges:\n  -\
    \ edge_id: magnesium-increases-coupled-output\n    subject: magnesium-point-five-millimolar\n\
    \    predicate: increases\n    object: magnesium-series-phosphate-output\n   \
    \ mechanism: Added 0.5 mM MgCl2 increases the coupled optical output relative\
    \ to omission in Figure\n      6. This preserves the experimental direction without\
    \ claiming that the metal directly activates\n      a particular UppS residue\
    \ or elementary reaction.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:9882662\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC93402/\n      snippet:\
    \ residual activity\n      explanation: The visually inspected magnesium panel\
    \ supports an increase with nonzero omission signal.\n        Main Methods make\
    \ the pyrophosphatase coupling explicit; abstract wording does not override the\n\
    \        plotted residual activity.\n      cache_path: evidence/PF01255/apfel-1999-upps.txt\n\
    \      cache_sha256: bb2db41b12af36570d3c29fa6ba93be94ed598397151f87f3f2c032acbe1dfa7\n\
    curation_events:\n- timestamp: '2026-10-11T10:22:52Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate UppS product formation and separately\
    \ qualified coupled-assay effects\n  history_record: history/records/PF01255/2026-10-11T102252Z-codex-df8910.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Q47675 is demerged to several entries, but its archived UPI0000137D08 sequence
    exactly matches P60472/ispU/uppS/yaeS, 253 aa and sequence version 1. InterPro
    maps PF01255 to 24-244 and agrees with UniProt. The historical upstream GTG and
    one-/two-Met forms are explicit; full clone and template strain remain unresolved.
    Frozen M. luteus O82827 metadata does not identify the E. coli assay protein.
  target_ids:
  - PF01255
  evidence_ids:
  - identity
  - primary
  - archived-identity
  - micrococcus-lead
  - bos12-lead
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Only the product-forming edge is DIRECT and MECHANISTIC. Triton and magnesium
    effects are PHENOTYPIC with UNRESOLVED directness because the measured output
    includes yeast pyrophosphatase and color chemistry. Both retained dose comparisons
    have directionally supported nonzero omission controls; neither becomes absolute
    dependence or monotonic activation. The graphs do not join biochemical effects
    to pneumococcal growth or proposed catalytic microsteps.
  target_ids:
  - PF01255
  evidence_ids:
  - primary
  - native
  - archived-identity
  - micrococcus-lead
  - bos12-lead
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Exact historical clones, panel-specific UppS doses, the product chromatogram
    and complete TLC conditions remain unresolved. The printed color-reagent notation
    needs reconciliation. M. luteus 1998 is abstract-only; Bos-12 2001 was inspected
    only through the abstract and selected Methods, without mutant figures or sequence-coordinate
    transfer. Other bacterial, eukaryotic and partner-dependent contexts are not comprehensively
    reviewed.
  target_ids:
  - PF01255
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01255-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve UppS product and coupling evidence before mechanism extension
  description: Obtain the original product data and clone sequences, separate prenyltransferase
    activity from coupled detection effects, and review Bos-12 mutants with explicit
    numbering before residue-level claims. Assess additional members and eukaryotic
    partners from their own primary experiments. Retain successor reviews and preserve
    source-label, product-mixture and residual-activity qualifications.
  target_ids:
  - PF01255
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - archived-identity
  - micrococcus-lead
  - bos12-lead
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01255.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Obtain the original product data and clone sequences, separate prenyltransferase
    activity from coupled detection effects, and review Bos-12 mutants with explicit
    numbering before residue-level claims. Assess additional members and eukaryotic
    partners from their own primary experiments. Retain successor reviews and preserve
    source-label, product-mixture and residual-activity qualifications.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01255
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Figure 6 was visually checked; other 1999 figures, raw measurements and the unshown
  product TLC were not independently examined. The 2001 primary PDF was read only
  for its abstract and selected Methods, not complete Results or product images. Same-condition
  direct Mg or detergent mechanisms are not established by the coupled output.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
