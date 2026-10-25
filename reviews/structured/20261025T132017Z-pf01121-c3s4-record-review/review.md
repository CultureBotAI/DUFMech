# PF01121 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review

- Review: 20261025T132017Z-pf01121-c3s4-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-25T13:20:16Z
- Finished UTC: 2026-10-25T13:20:17Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Three MECHANISTIC graphs retain five DIRECT OBSERVED biochemical effects and one DIRECT CONTESTED R140A loss claim. E. coli preparative CoA formation is separate from full-length mycobacterial mutant kinetics; L114A directions are opposite in DCoA- and ATP-varied series. Source parameter and primer conflicts remain visible. Partial same-agent review; IN_PROGRESS. Cycle 3 Stage 2 (PR #355) grounded the two dephospho-CoA kinase turnover readout nodes (dcoa-series-apparent-turnover and atp-series-apparent-turnover) to M. tuberculosis CoaE (UniProtKB:P9WPA3). Stage 4 frozen-inventory review verified all causal graphs and grounded nodes against primary evidence caches.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01121 CoaE, the next accession-ordered SEEDED family, using Mishra 2001 and Walia 2011 with the latter's 2009 construct source.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0e26e9cdab5214d838db4f53ddefbf83772241fb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01121 | data/families/PF01121.yaml | generated | PF01121 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01121 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01121.

E. coli K-12 P0A6I9, 206 aa and sequence version 1, exactly matches InterPro with PF01121 at 3-177. Its reference plus an engineered Ala explains the measured processed N terminus. Mycobacterial P63826 is demerged; archived UPI0000127CE6 exactly equals both P9WPA3 and P9WPA2, 407 aa, with the kinase profile at 4-178 and a separate PF04229 domain. Rv1631 and internal sites support mapping, but the 2009 printed forward primer mismatches the reference N terminus and donor strain is not explicitly named in the inspected cloning paragraph. Full clone reconstruction is not claimed.

### Directed effects and limits

graph: supported. Targets: PF01121.

The overall CoA-production graph keeps ATP, magnesium and regeneration together. Mycobacterial R140K/D32A decreases and L114A increase concern the reported DCoA-varied kcat; L114A decreases in the ATP-varied column and remains a separate graph. R140A is CONTESTED because no-activity text/Table 2 conflict with Figure 5A's Km=240 uM. Other numerical conflicts are not used for precise affinity/efficiency or chemical-role claims. A mixed graph's mechanistic scope does not convert its contested edge to observed support.

### Remaining family coverage

completeness: concern. Targets: PF01121.

Complete experimental clones, mycobacterial primer reconciliation, exact enzyme doses, raw kinetic fits and their uncertainty remain incomplete. R140A, D32A ATP Km, G8A values, printed efficiency ratios and the R140K fold claim conflict. The cofactor name and magnesium/reporter controls are unresolved. Other taxa, CTP regulation, UPF0157 folding and alternative-substrate product identities need separate curation. No family-wide mechanism or independent expert endorsement is claimed.

### Cycle 3 causal-graph and protein-node grounding verification

representation: supported. Targets: PF01121.

Cycle 3 Stage 2 (PR #355) grounded the two dephospho-CoA kinase turnover readout nodes (dcoa-series-apparent-turnover and atp-series-apparent-turnover) to M. tuberculosis CoaE (UniProtKB:P9WPA3). Stage 4 frozen-inventory review verified all causal graphs and grounded nodes against primary evidence caches.

## Findings

### additional-contexts: Resolve CoaE source conflicts before strengthening catalytic conclusions

minor / open / confirmed; issue key: pf01121-causal-context-coverage.

Obtain raw data or source clarification for R140A and other parameter discrepancies, reconstruct exact clones including the mismatched forward primer, and establish assay doses/cofactor and reporter controls. Keep opposite L114A series and disputed evidence explicit, and curate remaining member-specific contexts only with adequate support and a successor review.

## Recommended Actions And Acceptance Checks

### extend-contexts

Obtain raw data or source clarification for R140A and other parameter discrepancies, reconstruct exact clones including the mismatched forward primer, and establish assay doses/cofactor and reporter controls. Keep opposite L114A series and disputed evidence explicit, and curate remaining member-specific contexts only with adequate support and a successor review.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC99492/; Assay, cloning and purification Methods; recombinant Results and Table 2; Figure 1 reaction scheme visually inspected | supports | Purified Ala-added W3110 CoaE supports preparative product formation with ATP regeneration, and the HPLC-purified product's proton NMR is reported identical to authentic CoA. Separate ADP and thioester assays corroborate activity under different conditions. Raw NMR and a preparative no-enzyme control were not supplied in the inspected material. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0A6I9/entry/pfam/PF01121/; Accession and domain locations; paired UniProt identity facts | supports | E. coli K-12 P0A6I9, 206 aa and sequence version 1, exactly matches InterPro with PF01121 at 3-177. Its reference plus an engineered Ala explains the measured processed N terminus. Mycobacterial P63826 is demerged; archived UPI0000127CE6 exactly equals both P9WPA3 and P9WPA2, 407 aa, with the kinase profile at 4-178 and a separate PF04229 domain. Rv1631 and internal sites support mapping, but the 2009 printed forward primer mismatches the reference N terminus and donor strain is not explicitly named in the inspected cloning paragraph. Full clone reconstruction is not claimed. |
| mutant-kinetics-and-conflicts | https://pmc.ncbi.nlm.nih.gov/articles/PMC3019153/; Table 2, Figure 5, R140A/R140K/D32A/L114A Results and assay/ITC Methods | supports | Reported turnover comparisons support scoped direction changes but not universal activation or direct catalytic chemistry. R140A no-reaction versus plotted Km is explicitly contested, and other source discrepancies preclude precise affinity/efficiency claims. Structural controls have exceptions. |
| mycobacterial-construct-source | https://pmc.ncbi.nlm.nih.gov/articles/PMC2765170/; Original full-length and domain cloning sections; Rv1631 identity and domain-expression Results | supports | Establishes the two-domain, tagged construct lineage cited by 2011. The printed NdeI-junction sequence encodes MVTDRD while the archived and successor references start MLRIGL, an unresolved source discrepancy rather than a silently repaired clone sequence. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| stage4-prior-review | reviews/structured/20261011T090741Z-pf01121-coae-product-and-contested-kinetics/review.yaml; Predecessor structured review 20261011T090741Z-pf01121-coae-product-and-contested-kinetics | supports | Predecessor review 20261011T090741Z-pf01121-coae-product-and-contested-kinetics verified and linked for finding continuity and semantic-digest progression on PF01121. |
| duf-projection-pf01121 | data/families/PF01121.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Mishra 2001 Figure 1 scheme and Walia 2011 Figure 5 were visually inspected; the original biochemical Results, relevant mutant Results/Methods and Table 2 were read. The scheme is not raw NMR evidence. Raw spectra, kinetic fits, structural coordinates, complete clone sequences and supplementary folding/regulatory datasets were not reanalyzed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T132017Z-pf01121-c3s4-record-review
title: PF01121 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review
started_at: '2026-10-25T13:20:16Z'
finished_at: '2026-10-25T13:20:17Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Claude-Opus-4.6
  independence: self_review
  independence_basis: Cycle 3 Stage 4 frozen-inventory record review by Antigravity
    auditing prior curation overlays, primary evidence caches, history events, and
    current projections at Git revision 0e26e9cdab5214d838db4f53ddefbf83772241fb.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: true
summary: 'Three MECHANISTIC graphs retain five DIRECT OBSERVED biochemical effects
  and one DIRECT CONTESTED R140A loss claim. E. coli preparative CoA formation is
  separate from full-length mycobacterial mutant kinetics; L114A directions are opposite
  in DCoA- and ATP-varied series. Source parameter and primer conflicts remain visible.
  Partial same-agent review; IN_PROGRESS. Cycle 3 Stage 2 (PR #355) grounded the two
  dephospho-CoA kinase turnover readout nodes (dcoa-series-apparent-turnover and atp-series-apparent-turnover)
  to M. tuberculosis CoaE (UniProtKB:P9WPA3). Stage 4 frozen-inventory review verified
  all causal graphs and grounded nodes against primary evidence caches.'
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 0e26e9cdab5214d838db4f53ddefbf83772241fb
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01121.yaml
    sha256: bbaeef7c23ecd7c95d748b2c6343eb4ac1cea7454d80c27bfbf3f18d32c73eb6
    role: context
  - path: data/families/PF01121.yaml
    sha256: 52cc068091691c523b76d4aea354e80e38740887f2b4dc143f9a2642b665147f
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
  - path: evidence/PF01121/CoaE-identity.txt
    sha256: 411d10375ca1afd1834120b67c5ce42c21a066962a37ed5a89ee1ec11cb61e2d
    role: context
  - path: evidence/PF01121/mishra-2001-coae.txt
    sha256: 75e61819739997294b8ea1563ceb16916263957b76704e47f2101f777fb073dd
    role: context
  - path: evidence/PF01121/walia-2009-construct.txt
    sha256: 672ac24896d9abbcd1fdd6d2ecec3409e9f40c5cf7cfe3293efe38a6f147ebe6
    role: context
  - path: evidence/PF01121/walia-2011-coae.txt
    sha256: 56fc6b31e07e99c5dcdff6d58e205acfa28323c6f6fff334130b5c87bbf0b520
    role: context
  - path: reviews/structured/20261011T090741Z-pf01121-coae-product-and-contested-kinetics/review.yaml
    sha256: 9d3bb07c4b265646c423869eeb37fc40090095d783c8ad9450ad81be2bbf0803
    role: context
targets:
- target_id: PF01121
  path: data/families/PF01121.yaml
  label: PF01121
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01121.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: ed43093b9ef436718143881d4493fb96ece3eb534ee5dd1a167c217dbef2290f
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01121 CoaE, the next accession-ordered SEEDED family, using Mishra
    2001 and Walia 2011 with the latter's 2009 construct source.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01121
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Complete experimental clones, mycobacterial primer reconciliation, exact
      enzyme doses, raw kinetic fits and their uncertainty remain incomplete. R140A,
      D32A ATP Km, G8A values, printed efficiency ratios and the R140K fold claim
      conflict. The cofactor name and magnesium/reporter controls are unresolved.
      Other taxa, CTP regulation, UPF0157 folding and alternative-substrate product
      identities need separate curation. No family-wide mechanism or independent expert
      endorsement is claimed.
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
  - PF01121
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC99492/
  locator: Assay, cloning and purification Methods; recombinant Results and Table
    2; Figure 1 reaction scheme visually inspected
  accessed_at: '2026-10-11T09:07:41Z'
  support: supports
  snapshot_sha256: 75e61819739997294b8ea1563ceb16916263957b76704e47f2101f777fb073dd
  summary: Purified Ala-added W3110 CoaE supports preparative product formation with
    ATP regeneration, and the HPLC-purified product's proton NMR is reported identical
    to authentic CoA. Separate ADP and thioester assays corroborate activity under
    different conditions. Raw NMR and a preparative no-enzyme control were not supplied
    in the inspected material.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0A6I9/entry/pfam/PF01121/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T09:07:41Z'
  support: supports
  snapshot_sha256: 411d10375ca1afd1834120b67c5ce42c21a066962a37ed5a89ee1ec11cb61e2d
  summary: E. coli K-12 P0A6I9, 206 aa and sequence version 1, exactly matches InterPro
    with PF01121 at 3-177. Its reference plus an engineered Ala explains the measured
    processed N terminus. Mycobacterial P63826 is demerged; archived UPI0000127CE6
    exactly equals both P9WPA3 and P9WPA2, 407 aa, with the kinase profile at 4-178
    and a separate PF04229 domain. Rv1631 and internal sites support mapping, but
    the 2009 printed forward primer mismatches the reference N terminus and donor
    strain is not explicitly named in the inspected cloning paragraph. Full clone
    reconstruction is not claimed.
- evidence_id: mutant-kinetics-and-conflicts
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3019153/
  locator: Table 2, Figure 5, R140A/R140K/D32A/L114A Results and assay/ITC Methods
  summary: Reported turnover comparisons support scoped direction changes but not
    universal activation or direct catalytic chemistry. R140A no-reaction versus plotted
    Km is explicitly contested, and other source discrepancies preclude precise affinity/efficiency
    claims. Structural controls have exceptions.
  accessed_at: '2026-10-11T09:07:41Z'
  support: supports
  snapshot_sha256: 56fc6b31e07e99c5dcdff6d58e205acfa28323c6f6fff334130b5c87bbf0b520
- evidence_id: mycobacterial-construct-source
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2765170/
  locator: Original full-length and domain cloning sections; Rv1631 identity and domain-expression
    Results
  summary: Establishes the two-domain, tagged construct lineage cited by 2011. The
    printed NdeI-junction sequence encodes MVTDRD while the archived and successor
    references start MLRIGL, an unresolved source discrepancy rather than a silently
    repaired clone sequence.
  accessed_at: '2026-10-11T09:07:41Z'
  support: supports
  snapshot_sha256: 672ac24896d9abbcd1fdd6d2ecec3409e9f40c5cf7cfe3293efe38a6f147ebe6
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T09:07:41Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: stage4-prior-review
  kind: prior_review
  reference: reviews/structured/20261011T090741Z-pf01121-coae-product-and-contested-kinetics/review.yaml
  locator: Predecessor structured review 20261011T090741Z-pf01121-coae-product-and-contested-kinetics
  accessed_at: '2026-10-25T13:20:17Z'
  support: supports
  snapshot_sha256: 9d3bb07c4b265646c423869eeb37fc40090095d783c8ad9450ad81be2bbf0803
  summary: Predecessor review 20261011T090741Z-pf01121-coae-product-and-contested-kinetics
    verified and linked for finding continuity and semantic-digest progression on
    PF01121.
- evidence_id: duf-projection-pf01121
  kind: record_content
  reference: data/families/PF01121.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-25T13:20:17Z'
  support: context_only
  snapshot_sha256: 52cc068091691c523b76d4aea354e80e38740887f2b4dc143f9a2642b665147f
  quote: "id: Pfam:PF01121\npfam_id: PF01121\nname: Dephospho-CoA kinase\nshort_name:\
    \ CoaE\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01121\n\
    counters:\n  proteins: 23389\n  matches: 23652\n  proteomes: 20973\n  taxa: 33604\n\
    \  structures: 26\n  alphafold_models: 16271\n  domain_architectures: 180\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR001977\ndescription: This family catalyses the phosphorylation\
    \ of the 3'-hydroxyl group of dephosphocoenzyme A\n  to form Coenzyme A [ec:2.7.1.24].\
    \ This enzyme uses ATP in its reaction.\ncuration_history: history/records/PF01121\n\
    discussions:\n- discussion_id: coae-kinetic-conflicts-and-construct-reconciliation\n\
    \  prompt: Reconcile CoaE primary-source kinetic and construct conflicts before\
    \ strengthening mechanistic\n    claims.\n  kind: CURATION_TODO\n  status: OPEN\n\
    \  rationale: R140A no-activity text/Table 2 conflicts with Figure 5's Km fit.\
    \ Other Km, efficiency and\n    fold-change values disagree, and the original\
    \ mycobacterial forward primer mismatches the archived\n    reference N terminus.\
    \ These are source conflicts, not permission to repair values silently or assert\n\
    \    unobserved chemistry.\n  evidence:\n  - reference: PMID:21264299\n    supports:\
    \ PARTIAL\n    evidence_source: selected_full_text\n    explanation: Table 2 and\
    \ relevant Results support scoped reported turnover changes, with a contested\n\
    \      R140A edge. Figure 5 exposes discrepancies; structural controls have exceptions\
    \ and models are not\n      directly observed microsteps.\n  - reference: PMID:19876400\n\
    \    supports: PARTIAL\n    evidence_source: selected_full_text\n    explanation:\
    \ The cited construct study identifies Rv1631 and a two-domain 407-aa protein,\
    \ but the\n      printed cloning primer prevents independently reconstructing\
    \ the full experimental sequence.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n\
    \  notes: Obtain raw kinetics, correction/author clarification and complete clones;\
    \ resolve R140A, D32A/G8A\n    parameter discrepancies, pyrophosphate-cofactor\
    \ naming and magnesium/reporter controls. Assess CTP\n    regulation, UPF0157\
    \ folding, other taxa and alternative substrates in separate graphs. The 2001\
    \ E.\n    coli NMR spectrum was not available for independent reanalysis. Partial\
    \ same-agent scientific review;\n    remain IN_PROGRESS.\ncausal_graphs:\n- graph_id:\
    \ ecoli-coae-preparative-coa-formation\n  title: Recombinant E. coli CoaE supports\
    \ preparative CoA formation\n  scope: W3110 coaE/yacE expressed in BL21(DE3) using\
    \ pET28b(+), with an engineered Ala after the start\n    codon and the measured\
    \ processed N terminus ARYIVALTGGIG. Not the mycobacterial tagged fusion protein.\n\
    \  context: 2001 preparative reaction contains 3 umol dephospho-CoA, 0.1 umol\
    \ ATP, 1 umol MgCl2, 1 umol\n    KCl, 3.5 umol phosphoenolpyruvate, 5 U pyruvate\
    \ kinase and 2 U recombinant CoaE in 5 ml water adjusted\n    to pH 8, 30 min\
    \ at room temperature. HPLC-purified product is compared with authentic CoA by\
    \ proton\n    NMR. ATP regeneration is part of the joint reaction.\n  family_mapping:\
    \ K-12 reference P0A6I9, coaE/yacE/b0103/JW0100, 206 aa, sequence version 1, exactly\
    \ matches\n    InterPro and contains PF01121 at 3-177. Ala plus native residues\
    \ 2-12 explains the measured N-terminal\n    sequence after initiator removal.\
    \ The modern record cites this W3110 study; complete plasmid sequence\n    was\
    \ not independently reconstructed.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:83333\n\
    \  limitations: Product identity is reported from NMR, but raw spectra and a preparative\
    \ no-enzyme control\n    are not supplied in the inspected material. Separate\
    \ ADP and thioester-coupled assays corroborate\n    activity under different conditions.\
    \ This graph does not establish an elementary catalytic base, isolated-profile\n\
    \    sufficiency or the products of minor alternative-substrate reactions.\n \
    \ nodes:\n  - node_id: coae-dcoa-atp-regeneration-system\n    label: Purified\
    \ recombinant CoaE with dephospho-CoA, ATP, magnesium and ATP regeneration\n \
    \   node_type: ACTIVITY\n    grounding:\n    - UniProtKB:P0A6I9\n  - node_id:\
    \ nmr-identified-coa-product\n    label: HPLC-purified product identified as CoA\
    \ by proton NMR\n    node_type: STATE\n  edges:\n  - edge_id: coae-joint-system-produces-coa\n\
    \    subject: coae-dcoa-atp-regeneration-system\n    predicate: produces\n   \
    \ object: nmr-identified-coa-product\n    mechanism: The purified enzyme reaction\
    \ yields a product reported to match authentic CoA by proton\n      NMR. The supported\
    \ overall phosphorylation retains ATP, magnesium and regeneration components as\n\
    \      joint conditions, without inventing independently observed phosphoryl-transfer\
    \ microsteps.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:11292795\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC99492/\n      snippet: identical to\
    \ that of authentic CoA\n      explanation: Preparative assay Methods and recombinant\
    \ characterization Results establish product\n        formation and reported NMR\
    \ identity. Figure 1 is a reaction scheme, not raw proof of the product\n    \
    \    spectrum.\n      cache_path: evidence/PF01121/mishra-2001-coae.txt\n    \
    \  cache_sha256: 75e61819739997294b8ea1563ceb16916263957b76704e47f2101f777fb073dd\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0A6I9/entry/pfam/PF01121/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0A6I9/entry/pfam/PF01121/\n\
    \      snippet: 'P0A6I9 Pfam:PF01121 interval: 3-177, inclusive'\n      explanation:\
    \ Maps the native reference while explicitly accounting for the engineered Ala\
    \ and processed\n        N terminus of the experimental construct.\n      cache_path:\
    \ evidence/PF01121/CoaE-identity.txt\n      cache_sha256: 411d10375ca1afd1834120b67c5ce42c21a066962a37ed5a89ee1ec11cb61e2d\n\
    - graph_id: mycobacterial-coae-dcoa-series-substitutions\n  title: Mycobacterial\
    \ CoaE substitutions alter reported DCoA-series turnover\n  scope: Full-length\
    \ hexahistidine-tagged mycobacterial CoaE and individual R140A/R140K/D32A/L114A\
    \ substitutions\n    in the 2011 study. The R140A loss claim is explicitly CONTESTED\
    \ by inconsistent source presentations.\n  context: Single-coupled alpha-ketoglutarate-dehydrogenase\
    \ assay, 25 C, five-minute A340 monitoring,\n    no-DCoA blanks subtracted. DCoA\
    \ varies with 10 mM ATP, 10 mM MgCl2, 20 mM KCl, 50 mM Tris pH 8, 2\n    U coupling\
    \ enzyme, 2 mM alpha-ketoglutarate, 0.3 mM NADP and the source's 0.3 mM pyrophosphate\
    \ cofactor.\n    Exact CoaE dose is unreported. Table 2 gives apparent kcat; Figure\
    \ 5 states two independent experiments\n    in duplicate. Separate ITC kinetics\
    \ use 20 C and different buffer, not this same reaction.\n  family_mapping: The\
    \ cited P63826 demerged into P9WPA3/Rv1631 and P9WPA2/MT1667; both 407-aa sequences\n\
    \    exactly match archived UPI0000127CE6. P9WPA3 PF01121 spans 4-178 and contains\
    \ R140/D32/L114; the intact\n    protein also has PF04229. The 2009 source names\
    \ Rv1631 but its printed forward primer mismatches the\n    reference N terminus,\
    \ so complete clone and donor-strain reconstruction remain unresolved. Two identical\n\
    \    successors do not imply two experiments.\n  scope_status: MECHANISTIC\n \
    \ taxon: NCBITaxon:1773\n  limitations: Effects concern reported fitted turnover\
    \ in this substrate series, not binding Kd or observed\n    catalytic chemistry.\
    \ Text/Table 2 report R140A no reaction while Figure 5A plots its Km as 240 uM.\n\
    \    Other Km, ratio and fold-change inconsistencies prevent precise affinity/efficiency\
    \ claims. Structural\n    controls do not establish identical folding for every\
    \ mutant. The printed cofactor name thymine pyrophosphate\n    is not silently\
    \ corrected, and raw kinetic fits remain unreviewed.\n  nodes:\n  - node_id: r140a-in-dcoa-series\n\
    \    label: R140A instead of WT in the DCoA-varied assay\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:P9WPA3\n  - node_id: r140k-in-dcoa-series\n \
    \   label: R140K instead of WT in the DCoA-varied assay\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:P9WPA3\n  - node_id: d32a-in-dcoa-series\n  \
    \  label: D32A instead of WT in the DCoA-varied assay\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:P9WPA3\n  - node_id: l114a-in-dcoa-series\n \
    \   label: L114A instead of WT in the DCoA-varied assay\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:P9WPA3\n  - node_id: dcoa-series-apparent-turnover\n\
    \    label: Apparent turnover from the DCoA-varied kinetic series\n    node_type:\
    \ ACTIVITY\n    grounding:\n    - UniProtKB:P9WPA3\n  edges:\n  - edge_id: r140a-reported-turnover-loss-contested\n\
    \    subject: r140a-in-dcoa-series\n    predicate: decreases\n    object: dcoa-series-apparent-turnover\n\
    \    mechanism: The text and Table 2 report loss of detectable kinetic activity,\
    \ but Figure 5A supplies\n      an R140A Km despite that no-reaction designation.\
    \ This internally inconsistent loss claim is retained\n      as contested, not\
    \ an observed zero or proof that R140 is an essential catalytic charge stabilizer.\n\
    \    directness: DIRECT\n    support: CONTESTED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:21264299\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3019153/\n\
    \      snippet: completely abolishes kinetic activity\n      explanation: The\
    \ R140A Results sentence and Table 2 conflict with the visually inspected Figure\n\
    \        5A R140A bar labeled Km=240 uM. The conflict is not resolved by choosing\
    \ the strongest claim.\n      cache_path: evidence/PF01121/walia-2011-coae.txt\n\
    \      cache_sha256: 56fc6b31e07e99c5dcdff6d58e205acfa28323c6f6fff334130b5c87bbf0b520\n\
    \  - edge_id: r140k-decreases-dcoa-series-turnover\n    subject: r140k-in-dcoa-series\n\
    \    predicate: decreases\n    object: dcoa-series-apparent-turnover\n    mechanism:\
    \ Table 2 reports lower DCoA-series kcat for R140K, 0.453 versus WT 1.758 per\
    \ minute. This\n      is not assigned the prose's inconsistent percentage or Km\
    \ fold change, and does not directly reveal\n      ATP shielding or transition-state\
    \ geometry.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:21264299\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC3019153/\n      snippet: dramatic loss\
    \ of catalytic activity\n      explanation: Table 2 DCoA-varied turnover and the\
    \ R140K Results support a decrease. The reported\n        518-fold Km statement\
    \ does not match 181 versus 34.9 uM and is excluded from the graph's quantitative\n\
    \        interpretation.\n      cache_path: evidence/PF01121/walia-2011-coae.txt\n\
    \      cache_sha256: 56fc6b31e07e99c5dcdff6d58e205acfa28323c6f6fff334130b5c87bbf0b520\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P9WPA3/entry/pfam/PF01121/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P9WPA3/entry/pfam/PF01121/\n\
    \      snippet: 'P9WPA3 Pfam:PF01121 interval: 4-178, inclusive'\n      explanation:\
    \ Archived P63826 and both modern strain successors have identical sequences,\
    \ with the\n        mutation sites in the kinase profile. The full experimental\
    \ clone and printed primer discrepancy\n        remain distinct limits.\n    \
    \  cache_path: evidence/PF01121/CoaE-identity.txt\n      cache_sha256: 411d10375ca1afd1834120b67c5ce42c21a066962a37ed5a89ee1ec11cb61e2d\n\
    \  - edge_id: d32a-decreases-dcoa-series-turnover\n    subject: d32a-in-dcoa-series\n\
    \    predicate: decreases\n    object: dcoa-series-apparent-turnover\n    mechanism:\
    \ Table 2 reports a lower DCoA-series kcat for D32A, 0.1026 versus WT 1.758 per\
    \ minute. No\n      precise efficiency ratio, catalytic-base assignment or magnesium-coordination\
    \ microstep is inferred\n      from this fitted endpoint.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:21264299\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3019153/\n\
    \      snippet: Kcat dropped drastically\n      explanation: The DCoA column of\
    \ Table 2 is the adopted endpoint; the separately varied ATP column\n        has\
    \ a different kcat. Its inconsistent printed efficiency ratio and the 57.5-versus-575\
    \ ATP Km\n        conflict are retained as limitations, not corrected by inference.\n\
    \      cache_path: evidence/PF01121/walia-2011-coae.txt\n      cache_sha256: 56fc6b31e07e99c5dcdff6d58e205acfa28323c6f6fff334130b5c87bbf0b520\n\
    \  - edge_id: l114a-increases-dcoa-series-turnover\n    subject: l114a-in-dcoa-series\n\
    \    predicate: increases\n    object: dcoa-series-apparent-turnover\n    mechanism:\
    \ L114A has higher apparent turnover in the DCoA-varied series, 3.414 versus WT\
    \ 1.758 per\n      minute. The direction reverses in the ATP-varied series, so\
    \ this is not a universal catalytic activation\n      claim or a direct binding-affinity\
    \ measurement.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:21264299\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC3019153/\n      snippet: increasing\
    \ the enzymatic turnover\n      explanation: L114A Results and Table 2 DCoA columns\
    \ support the increase. The ATP-series result\n        is deliberately retained\
    \ in a separate graph rather than averaged or silently discarded.\n      cache_path:\
    \ evidence/PF01121/walia-2011-coae.txt\n      cache_sha256: 56fc6b31e07e99c5dcdff6d58e205acfa28323c6f6fff334130b5c87bbf0b520\n\
    - graph_id: mycobacterial-coae-l114a-atp-series\n  title: L114A lowers apparent\
    \ turnover in the separately varied ATP series\n  scope: Full-length tagged mycobacterial\
    \ CoaE L114A versus WT in the 2011 Table 2 ATP-varied kinetic\n    comparison,\
    \ not the DCoA-varied series.\n  context: Coupled A340 assay at 25 C, 50 mM Tris\
    \ pH 8, fixed 0.5 mM DCoA and varying ATP, 10 mM MgCl2,\n    20 mM KCl, 2 U alpha-ketoglutarate\
    \ dehydrogenase, 2 mM alpha-ketoglutarate, 0.3 mM NADP and 0.3 mM\n    the source's\
    \ pyrophosphate cofactor. Five-minute monitoring with no-DCoA blanks. Exact CoaE\
    \ dose and\n    raw fit uncertainty are not supplied in the inspected table/method.\n\
    \  family_mapping: L114 matches the archived P63826 sequence and both identical\
    \ P9WPA3/P9WPA2 successors.\n    PF01121 spans 4-178 in the 407-aa P9WPA3 reference.\
    \ The second PF04229 domain and His tag remain part\n    of the tested protein;\
    \ a published forward-primer mismatch prevents exact clone reconstruction.\n \
    \ scope_status: MECHANISTIC\n  taxon: NCBITaxon:1773\n  limitations: A condition-specific\
    \ fitted kcat is not a universal turnover constant or affinity. The\n    opposite\
    \ DCoA-series direction and inconsistent reported parameters elsewhere in the\
    \ paper remain\n    explicit. No elementary contact, folding equivalence or family-wide\
    \ behavior is proved. The assay\n    cofactor's printed name and raw fit details\
    \ require clarification.\n  nodes:\n  - node_id: l114a-in-atp-series\n    label:\
    \ L114A instead of WT in the ATP-varied assay\n    node_type: PERTURBATION\n \
    \   grounding:\n    - UniProtKB:P9WPA3\n  - node_id: atp-series-apparent-turnover\n\
    \    label: Apparent turnover from the ATP-varied kinetic series\n    node_type:\
    \ ACTIVITY\n    grounding:\n    - UniProtKB:P9WPA3\n  edges:\n  - edge_id: l114a-decreases-atp-series-turnover\n\
    \    subject: l114a-in-atp-series\n    predicate: decreases\n    object: atp-series-apparent-turnover\n\
    \    mechanism: The ATP-varied Table 2 column reports L114A kcat of 1.152 versus\
    \ WT 2.886 per minute. This\n      decrease is kept separate from the DCoA-series\
    \ increase and is not interpreted as unique transition-state\n      destabilization.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:21264299\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3019153/\n\
    \      snippet: Table 2\n      explanation: The ATP-specific kcat column, not\
    \ the DCoA-specific narrative, supplies the comparison.\n        Both parameter\
    \ sets are recorded in the evidence ledger with the source's contradictions and\
    \ unreviewed\n        raw-data limitation.\n      cache_path: evidence/PF01121/walia-2011-coae.txt\n\
    \      cache_sha256: 56fc6b31e07e99c5dcdff6d58e205acfa28323c6f6fff334130b5c87bbf0b520\n\
    curation_events:\n- timestamp: '2026-10-11T08:55:42Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Add CoaE product and condition-specific\
    \ kinetic graphs with contested R140A\n  history_record: history/records/PF01121/2026-10-11T085542Z-codex-aa94d4.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-11T09:07:54Z'\n\
    \  curator: Codex\n  action: REVIEW\n  outcome: needs_followup\n  summary: Retain\
    \ partial CoaE review with contested R140A source evidence\n  history_record:\
    \ history/records/PF01121/2026-10-11T090754Z-codex-5d17d9.yaml\n  event_index:\
    \ 0\n  llm_assisted: true\n- timestamp: '2026-10-25T09:45:03Z'\n  curator: Antigravity\n\
    \  action: EDIT\n  outcome: changed\n  summary: Ground dcoa-series-apparent-turnover\
    \ and atp-series-apparent-turnover ACTIVITY nodes in PF01121\n    causal graphs\
    \ to UniProtKB:P9WPA3\n  history_record: history/records/PF01121/2026-10-25T094503Z-antigravity-267128.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: E. coli K-12 P0A6I9, 206 aa and sequence version 1, exactly matches InterPro
    with PF01121 at 3-177. Its reference plus an engineered Ala explains the measured
    processed N terminus. Mycobacterial P63826 is demerged; archived UPI0000127CE6
    exactly equals both P9WPA3 and P9WPA2, 407 aa, with the kinase profile at 4-178
    and a separate PF04229 domain. Rv1631 and internal sites support mapping, but
    the 2009 printed forward primer mismatches the reference N terminus and donor
    strain is not explicitly named in the inspected cloning paragraph. Full clone
    reconstruction is not claimed.
  target_ids:
  - PF01121
  evidence_ids:
  - identity
  - primary
  - mutant-kinetics-and-conflicts
  - mycobacterial-construct-source
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: The overall CoA-production graph keeps ATP, magnesium and regeneration
    together. Mycobacterial R140K/D32A decreases and L114A increase concern the reported
    DCoA-varied kcat; L114A decreases in the ATP-varied column and remains a separate
    graph. R140A is CONTESTED because no-activity text/Table 2 conflict with Figure
    5A's Km=240 uM. Other numerical conflicts are not used for precise affinity/efficiency
    or chemical-role claims. A mixed graph's mechanistic scope does not convert its
    contested edge to observed support.
  target_ids:
  - PF01121
  evidence_ids:
  - primary
  - native
  - mutant-kinetics-and-conflicts
  - mycobacterial-construct-source
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Complete experimental clones, mycobacterial primer reconciliation, exact
    enzyme doses, raw kinetic fits and their uncertainty remain incomplete. R140A,
    D32A ATP Km, G8A values, printed efficiency ratios and the R140K fold claim conflict.
    The cofactor name and magnesium/reporter controls are unresolved. Other taxa,
    CTP regulation, UPF0157 folding and alternative-substrate product identities need
    separate curation. No family-wide mechanism or independent expert endorsement
    is claimed.
  target_ids:
  - PF01121
  evidence_ids:
  - primary
- assessment_id: cycle3-partner-grounding-verification
  area: representation
  topic: Cycle 3 causal-graph and protein-node grounding verification
  outcome: supported
  summary: 'Cycle 3 Stage 2 (PR #355) grounded the two dephospho-CoA kinase turnover
    readout nodes (dcoa-series-apparent-turnover and atp-series-apparent-turnover)
    to M. tuberculosis CoaE (UniProtKB:P9WPA3). Stage 4 frozen-inventory review verified
    all causal graphs and grounded nodes against primary evidence caches.'
  target_ids:
  - PF01121
  evidence_ids:
  - stage4-prior-review
findings:
- finding_id: additional-contexts
  issue_key: pf01121-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve CoaE source conflicts before strengthening catalytic conclusions
  description: Obtain raw data or source clarification for R140A and other parameter
    discrepancies, reconstruct exact clones including the mismatched forward primer,
    and establish assay doses/cofactor and reporter controls. Keep opposite L114A
    series and disputed evidence explicit, and curate remaining member-specific contexts
    only with adequate support and a successor review.
  target_ids:
  - PF01121
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - mutant-kinetics-and-conflicts
  - mycobacterial-construct-source
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01121.yaml
    role: Human-owned scientific overlay
  previous_occurrences:
  - repository: CultureBotAI/DUFMech
    review_id: 20261011T090741Z-pf01121-coae-product-and-contested-kinetics
    finding_id: additional-contexts
actions:
- action_id: extend-contexts
  description: Obtain raw data or source clarification for R140A and other parameter
    discrepancies, reconstruct exact clones including the mismatched forward primer,
    and establish assay doses/cofactor and reporter controls. Keep opposite L114A
    series and disputed evidence explicit, and curate remaining member-specific contexts
    only with adequate support and a successor review.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01121
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Mishra 2001 Figure 1 scheme and Walia 2011 Figure 5 were visually inspected; the
  original biochemical Results, relevant mutant Results/Methods and Table 2 were read.
  The scheme is not raw NMR evidence. Raw spectra, kinetic fits, structural coordinates,
  complete clone sequences and supplementary folding/regulatory datasets were not
  reanalyzed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
