# Scoped scientific self-review of Dus2 redox and product assays

- Review: 20261011T101620Z-pf01207-dus2-separated-redox-and-product-assays
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T10:16:05Z
- Finished UTC: 2026-10-11T10:16:20Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Five MECHANISTIC graphs retain five DIRECT OBSERVED effects for NADPH-dependent flavin reduction, synthetic-RNA dihydrouridine formation, native-RNA flavin oxidation and separate bacterial-RNA reverse assays. Conflicting primers, concentrations, substrate strings and temperatures constrain stronger claims. Partial scientific self-review; IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01207 Dus, next accession-ordered SEEDED family after PF01205, assessed through Rider 2009 WT biochemical assays with current P53720 mapping and a later DusA abstract lead.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01207 | data/families/PF01207.yaml | generated | PF01207 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01207 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01207.

P53720/DUS2_YEAST maps SMM1/DUS2/YNR015W, 384 aa and sequence version 1, to PF01207 32-352 with exact UniProt/InterPro agreement. The study identifies supplied pEfx-4b and YNR015w-knockout-derived RNA, but complete clones and tag junctions remain unverified. C117 lies inside the domain, yet the printed forward mutagenic primer encodes Q120 while its reverse partner and current reference encode H120. No C117A-only identity or mutant-specific causal edge is asserted.

### Directed effects and limits

graph: supported. Targets: PF01207.

Each graph retains one observed redox or product endpoint in its actual vessel and substrate context. The synthetic product assay does not independently localize U20. Native-RNA flavin oxidation is not promoted to a measured specific prior modification. Aerobic 18-h content loss and anaerobic bacterial-RNA flavin reduction remain separate mixed-species assays, not native reverse flux. No atomic hydride/proton-transfer or transitive full-cycle edge is invented.

### Remaining family coverage

completeness: concern. Targets: PF01207.

Figure 3 caption and Results differ at 35/60-uM enzyme and 450/457 nm; printed RNA template strings do not independently resolve the purported intron difference. Figure 4 image says mM while caption says uM. The C117A comparison uses a different temperature and contradictory oligos. Exact clones, RNA modifications, raw spectra, site-localized products and kinetic uncertainty need further work. The 2002 abstract and 2026 DusA abstract are leads, not adopted experimental extensions.

## Findings

### additional-contexts: Reconcile Dus2 constructs and substrates before residue-specific extension

minor / open / confirmed; issue key: pf01207-causal-context-coverage.

Obtain original WT/mutant sequences and exact RNA templates, reconcile concentrations and primer disagreements, and inspect matched-temperature comparisons and raw product data. Assess separate yeast specificity and modern bacterial/human or non-tRNA contexts with exact member mapping. Keep every new edge scoped to its experimentally supported endpoint and retain an evidence-backed successor review.

## Recommended Actions And Acceptance Checks

### extend-contexts

Obtain original WT/mutant sequences and exact RNA templates, reconcile concentrations and primer disagreements, and inspect matched-temperature comparisons and raw product data. Assess separate yeast specificity and modern bacterial/human or non-tRNA contexts with exact member mapping. Keep every new edge scoped to its experimentally supported endpoint and retain an evidence-backed successor review.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC2667719/; Main Methods, Results and Discussion; Figures 2-5 and 8 visually inspected | supports | Purified yeast WT Dus2 undergoes NADPH-dependent flavin reduction, forms colorimetrically detected dihydrouridine in a reported synthetic tRNA preparation, and is reoxidized by knockout-derived tRNA-Leu. In separate mixed-species experiments it reduces bulk bacterial RNA dihydrouridine content aerobically and its oxidized flavin is reduced by bacterial tRNA anaerobically. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/P53720/entry/pfam/PF01207/; Accession and domain locations; paired UniProt identity facts | supports | P53720/DUS2_YEAST maps SMM1/DUS2/YNR015W, 384 aa and sequence version 1, to PF01207 32-352 with exact UniProt/InterPro agreement. The study identifies supplied pEfx-4b and YNR015w-knockout-derived RNA, but complete clones and tag junctions remain unverified. C117 lies inside the domain, yet the printed forward mutagenic primer encodes Q120 while its reverse partner and current reference encode H120. No C117A-only identity or mutant-specific causal edge is asserted. |
| later-bacterial-dusa-lead | https://doi.org/10.1093/nar/gkag432; Complete primary abstract indexed by Europe PMC, PMID 42080256 | supports | Identifies distinct E. coli DusA binding, charging and translation contexts for future full-text assessment; neither the species nor substrate-specific conclusions are transferred to yeast Dus2. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01207 | data/families/PF01207.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Figures 2-5 and 8 were visually inspected; main Methods, Results and Discussion were read. Raw spectra, unshown stereochemical NMR and complete clones were not independently verified. Binding/amino-acid figures and structural models were not visually assessed. The 2026 primary abstract was retrieved through Europe PMC after the DOI web-reader route failed; full study review is not claimed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T101620Z-pf01207-dus2-separated-redox-and-product-assays
title: Scoped scientific self-review of Dus2 redox and product assays
started_at: '2026-10-11T10:16:05Z'
finished_at: '2026-10-11T10:16:20Z'
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
summary: Five MECHANISTIC graphs retain five DIRECT OBSERVED effects for NADPH-dependent
  flavin reduction, synthetic-RNA dihydrouridine formation, native-RNA flavin oxidation
  and separate bacterial-RNA reverse assays. Conflicting primers, concentrations,
  substrate strings and temperatures constrain stronger claims. Partial scientific
  self-review; IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01207.yaml
    sha256: 77a2c92f8ba11783e1c90a9e2e85b411bc3ddc8937ae94832613a64d1e603309
    role: context
  - path: data/families/PF01207.yaml
    sha256: a33dd887b2e14b8e61eb883cb02b119890d5beede2e65eb030b3c01179027d0e
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
  - path: evidence/PF01207/rider-2009-dus2.txt
    role: context
    sha256: c01a2e7cbc35858ec094ea5adfc89d1b3aa0bbf0d0c3456f354a7e696149de3a
  - path: evidence/PF01207/Dus2-identity.txt
    role: context
    sha256: 6c4f5beb1289f972df2ac118c61096353c79904fee209b8bd7b153b6ee0845ef
  - path: evidence/PF01207/dusa-2026-coverage-lead.txt
    role: context
    sha256: b17f76869e0bed1609e2048b9d82335be3d5ecd4378a3cfe1e59f64154af98d8
targets:
- target_id: PF01207
  path: data/families/PF01207.yaml
  label: PF01207
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01207.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 1cd35cb2c48d30196a440ae5faa8c5e89b475c2d36838170a34d5377b3c9c107
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01207 Dus, next accession-ordered SEEDED family after PF01205, assessed
    through Rider 2009 WT biochemical assays with current P53720 mapping and a later
    DusA abstract lead.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01207
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Figure 3 caption and Results differ at 35/60-uM enzyme and 450/457 nm;
      printed RNA template strings do not independently resolve the purported intron
      difference. Figure 4 image says mM while caption says uM. The C117A comparison
      uses a different temperature and contradictory oligos. Exact clones, RNA modifications,
      raw spectra, site-localized products and kinetic uncertainty need further work.
      The 2002 abstract and 2026 DusA abstract are leads, not adopted experimental
      extensions.
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
  - PF01207
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2667719/
  locator: Main Methods, Results and Discussion; Figures 2-5 and 8 visually inspected
  accessed_at: '2026-10-11T10:16:20Z'
  support: supports
  snapshot_sha256: c01a2e7cbc35858ec094ea5adfc89d1b3aa0bbf0d0c3456f354a7e696149de3a
  summary: Purified yeast WT Dus2 undergoes NADPH-dependent flavin reduction, forms
    colorimetrically detected dihydrouridine in a reported synthetic tRNA preparation,
    and is reoxidized by knockout-derived tRNA-Leu. In separate mixed-species experiments
    it reduces bulk bacterial RNA dihydrouridine content aerobically and its oxidized
    flavin is reduced by bacterial tRNA anaerobically.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P53720/entry/pfam/PF01207/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T10:16:20Z'
  support: supports
  snapshot_sha256: 6c4f5beb1289f972df2ac118c61096353c79904fee209b8bd7b153b6ee0845ef
  summary: P53720/DUS2_YEAST maps SMM1/DUS2/YNR015W, 384 aa and sequence version 1,
    to PF01207 32-352 with exact UniProt/InterPro agreement. The study identifies
    supplied pEfx-4b and YNR015w-knockout-derived RNA, but complete clones and tag
    junctions remain unverified. C117 lies inside the domain, yet the printed forward
    mutagenic primer encodes Q120 while its reverse partner and current reference
    encode H120. No C117A-only identity or mutant-specific causal edge is asserted.
- evidence_id: later-bacterial-dusa-lead
  kind: primary_source
  reference: https://doi.org/10.1093/nar/gkag432
  locator: Complete primary abstract indexed by Europe PMC, PMID 42080256
  summary: Identifies distinct E. coli DusA binding, charging and translation contexts
    for future full-text assessment; neither the species nor substrate-specific conclusions
    are transferred to yeast Dus2.
  accessed_at: '2026-10-11T10:16:20Z'
  support: supports
  snapshot_sha256: b17f76869e0bed1609e2048b9d82335be3d5ecd4378a3cfe1e59f64154af98d8
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T10:16:20Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01207
  kind: record_content
  reference: data/families/PF01207.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T10:16:20Z'
  support: context_only
  snapshot_sha256: a33dd887b2e14b8e61eb883cb02b119890d5beede2e65eb030b3c01179027d0e
  quote: "id: Pfam:PF01207\npfam_id: PF01207\nname: Dihydrouridine synthase (Dus)\n\
    short_name: Dus\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01207\n\
    counters:\n  proteins: 46157\n  matches: 47750\n  proteomes: 21293\n  taxa: 34157\n\
    \  structures: 15\n  alphafold_models: 33123\n  domain_architectures: 370\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR035587\ndescription: Members of this family catalyse\
    \ the reduction of the 5,6-double bond of a uridine residue\n  on tRNA. Dihydrouridine\
    \ modification of tRNA is widely observed in prokaryotes and eukaryotes, and also\n\
    \  in some archae. Most dihydrouridines are found in the D loop of t-RNAs. The\
    \ role of dihydrouridine in\n  tRNA is currently unknown, but may increase conformational\
    \ flexibility of the tRNA. It is likely that\n  different family members have\
    \ different substrate specificities, which may overlap. Dus 1 ([swissprot:Q9HGN6])\n\
    \  from Saccharomyces cerevisiae acts on pre-tRNA-Phe, while Dus 2 ([swissprot:P53720])\
    \ acts on pre-tRNA-Tyr\n  and pre-tRNA-Leu. Dus 1 is active as a single subunit,\
    \ requiring NADPH or NADH, and is stimulated by\n  the presence of FAD [[cite:PUB00014304]].\
    \ Some family members may be targeted to the mitochondria and\n  even have a role\
    \ in mitochondria [[cite:PUB00014304]].\ncuration_history: history/records/PF01207\n\
    discussions:\n- discussion_id: dus2-clone-substrate-and-half-reaction-limits\n\
    \  prompt: Resolve Dus2 construct and substrate discrepancies before adding residue-specific\
    \ microsteps.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: Five direct\
    \ redox/product effects do not establish a fully observed catalytic cycle, a specific\n\
    \    prior modification or every Dus member's physiological role.\n  evidence:\n\
    \  - reference: PMID:19139092\n    supports: PARTIAL\n    evidence_source: inspected_primary_methods_results_and_figures\n\
    \    explanation: Separate half-reactions support net redox/product effects. The\
    \ C117A primer pair disagrees\n      at H120/Q120, and mutant/native-RNA comparisons\
    \ use different temperatures.\n  - reference: doi:10.1093/nar/gkag432\n    supports:\
    \ PARTIAL\n    evidence_source: primary_abstract_only\n    explanation: A 2026\
    \ E. coli DusA study reports distinct binding and translation contexts requiring\n\
    \      separate member-specific review.\n  notes: Obtain pEfx-4b and mutant sequences,\
    \ exact tRNA templates and modification inventories. Reconcile\n    35/60-uM enzyme,\
    \ 450/457-nm readout and Figure 4 mM/uM labels. No mutant-specific edge is adopted;\n\
    \    C117A-only identity and a C117 proton-transfer step remain unverified. Inspect\
    \ 2002/2004 yeast specificity\n    and newer bacterial, human and RNA-class studies\
    \ independently; do not transfer FAD stimulation in\n    earlier assays to an\
    \ identical FMN preparation. Raw spectra and unshown NMR were not reanalyzed.\
    \ Partial\n    scientific self-review; remain IN_PROGRESS.\n  posed_by: Codex\n\
    \  posed_date: '2026-10-11'\ncausal_graphs:\n- graph_id: dus2-nadph-flavin-reduction\n\
    \  title: NADPH reduces the flavin of purified yeast Dus2\n  scope: Recombinant\
    \ WT Saccharomyces cerevisiae Dus2 in Rider 2009 Figure 2 and reductive-half-reaction\n\
    \    Results. This is an anaerobic purified-protein assay, not cellular RNA modification.\n\
    \  context: Mix 15 uM oxidized enzyme with anaerobic NADPH concentration series\
    \ at 4 C in 100 mM HEPES\n    pH 7.5, 100 mM NaCl, 10 mM MgCl2 and 10% glycerol.\
    \ Stopped-flow absorbance at 450 nm measures flavin\n    reduction. DTT is removed\
    \ immediately before assays.\n  family_mapping: P53720/DUS2_YEAST is SMM1/DUS2/YNR015W,\
    \ 384 aa, sequence version 1, with PF01207 at\n    32-352. UniProt and InterPro\
    \ sequences agree. The study uses the supplied pEfx-4b yeast DUS2 plasmid\n  \
    \  and BL21(DE3) expression, cobalt-affinity and DEAE purification. Exact historical\
    \ tag junctions and\n    clone sequence remain unverified.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:4932\n  limitations: Minor slower spectral phases may reflect\
    \ damaged protein. The observed reduction does not\n    independently establish\
    \ the proposed NADP dissociation rate or every hydride-transfer microstep. FMN\n\
    \    in this preparation is not a claim that all family members have identical\
    \ cofactor or substrate behavior.\n  nodes:\n  - node_id: add-nadph-to-oxidized-dus2\n\
    \    label: Mix NADPH with anaerobic oxidized WT Dus2\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:P53720\n  - node_id: dus2-reduced-flavin\n  \
    \  label: Reduced enzyme-bound flavin measured by A450 loss\n    node_type: STATE\n\
    \  edges:\n  - edge_id: nadph-produces-reduced-dus2-flavin\n    subject: add-nadph-to-oxidized-dus2\n\
    \    predicate: produces\n    object: dus2-reduced-flavin\n    mechanism: NADPH\
    \ addition produces a concentration-dependent major decrease in oxidized-flavin\
    \ absorbance.\n      The edge records the experimentally observed redox conversion,\
    \ not a complete catalytic cycle or\n      inferred product-release trajectory.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:19139092\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2667719/\n\
    \      snippet: flavin reduction\n      explanation: Figure 2 was visually inspected\
    \ with the reductive-half-reaction Results and anaerobic\n        kinetics Methods;\
    \ small secondary phases remain qualified.\n      cache_path: evidence/PF01207/rider-2009-dus2.txt\n\
    \      cache_sha256: c01a2e7cbc35858ec094ea5adfc89d1b3aa0bbf0d0c3456f354a7e696149de3a\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P53720/entry/pfam/PF01207/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P53720/entry/pfam/PF01207/\n\
    \      snippet: 'P53720 Pfam:PF01207 interval: 32-352, inclusive.'\n      explanation:\
    \ Current exact reference/domain mapping supports member scope without independently\n\
    \        reconstructing the historical expression clone.\n      cache_path: evidence/PF01207/Dus2-identity.txt\n\
    \      cache_sha256: 6c4f5beb1289f972df2ac118c61096353c79904fee209b8bd7b153b6ee0845ef\n\
    - graph_id: dus2-synthetic-trna-dihydrouridine\n  title: Prereduced Dus2 forms\
    \ dihydrouridine in a synthetic tRNA preparation\n  scope: WT yeast Dus2 acting\
    \ on the reported synthetic pre-tRNA-Leu preparation in Figure 3 and oxidative-half-reaction\n\
    \    Results. No nucleotide position is independently assigned by this endpoint.\n\
    \  context: Dithionite-prereduced enzyme reacts anaerobically at 25 C in the pH-7.5\
    \ HEPES/NaCl/MgCl2/glycerol\n    buffer. Results give 60 uM enzyme and 700 uM\
    \ RNA, whereas the caption gives 35 uM enzyme. Flavin reoxidation\n    is followed\
    \ over hours; a separate alkaline-ring-opening A550 colorimetric assay measures\
    \ dihydrouridine\n    against a standard curve.\n  family_mapping: Intact yeast\
    \ Dus2 maps to P53720 and PF01207 32-352. The published pre/intronless template\n\
    \    strings differ by a promoter-containing prefix rather than an evident intron,\
    \ so the exact assayed\n    RNA sequence is not reconstructed from those strings.\n\
    \  scope_status: MECHANISTIC\n  taxon: NCBITaxon:4932\n  limitations: The enzyme\
    \ concentration and 450/457-nm reporting differ between caption and Results. Product\n\
    \    colorimetry supports dihydrouridine formation but is not site-resolved sequencing\
    \ or mass spectrometry.\n    Exact RNA sequence, matched no-enzyme raw data and\
    \ stoichiometry were not independently verified;\n    no precise kinetic constant\
    \ or C117 proton-transfer edge is adopted.\n  nodes:\n  - node_id: prereduced-dus2-synthetic-trna\n\
    \    label: React prereduced WT Dus2 with reported synthetic pre-tRNA-Leu\n  \
    \  node_type: ACTIVITY\n    grounding:\n    - UniProtKB:P53720\n  - node_id: synthetic-trna-dihydrouridine-product\n\
    \    label: Colorimetrically detected dihydrouridine product\n    node_type: STATE\n\
    \  edges:\n  - edge_id: dus2-produces-synthetic-trna-dihydrouridine\n    subject:\
    \ prereduced-dus2-synthetic-trna\n    predicate: produces\n    object: synthetic-trna-dihydrouridine-product\n\
    \    mechanism: Reaction of the reduced enzyme with the reported RNA preparation\
    \ yields dihydrouridine\n      alongside flavin oxidation. The evidence supports\
    \ net product formation, not the exact order of\n      binding, proton transfer\
    \ and release.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:19139092\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC2667719/\n      snippet: dihydrouridine\n\
    \      explanation: Figure 3 spectra were visually inspected; adjacent product-analysis\
    \ Results and colorimetric\n        Methods establish the separate chemical endpoint\
    \ and its limitations.\n      cache_path: evidence/PF01207/rider-2009-dus2.txt\n\
    \      cache_sha256: c01a2e7cbc35858ec094ea5adfc89d1b3aa0bbf0d0c3456f354a7e696149de3a\n\
    - graph_id: dus2-knockout-derived-trna-flavin-oxidation\n  title: Knockout-derived\
    \ tRNA-Leu reoxidizes reduced WT Dus2\n  scope: WT yeast Dus2 with affinity-purified\
    \ tRNA-Leu from a YNR015w knockout in Figure 4. The RNA is\n    partially matured,\
    \ not an unmodified in-vitro transcript.\n  context: Anaerobic 20 uM Dus2 is reduced\
    \ with dithionite and mixed with RNA at 4 C in 100 mM HEPES pH\n    7.5, 100 mM\
    \ NaCl, 10 mM MgCl2 and 10% glycerol. A450 increases in stopped-flow experiments.\
    \ The caption\n    gives RNA up to 800 uM; the plotted concentration axis says\
    \ mM.\n  family_mapping: The protein is the same P53720-mapped WT yeast Dus2 preparation,\
    \ PF01207 32-352. The\n    RNA source is specified by YNR015w deletion, but its\
    \ exact strain identifier, full modification inventory\n    and oligonucleotide\
    \ sequence were not independently established.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:4932\n  limitations: This edge records flavin oxidation, not\
    \ an independently localized D20 product. The substrate-preparation\n    comparison\
    \ to synthetic RNA and the C117A comparison use different temperatures. Neither\
    \ an exact\n    fold improvement nor a specific required prior modification is\
    \ asserted. The caption/image concentration\n    discrepancy remains open.\n \
    \ nodes:\n  - node_id: add-knockout-derived-trna-to-dus2\n    label: Add knockout-derived\
    \ tRNA-Leu to prereduced WT Dus2\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:P53720\n  - node_id: native-trna-oxidized-dus2-flavin\n    label:\
    \ Reoxidized enzyme-bound flavin measured by A450 increase\n    node_type: STATE\n\
    \  edges:\n  - edge_id: knockout-derived-trna-produces-oxidized-dus2-flavin\n\
    \    subject: add-knockout-derived-trna-to-dus2\n    predicate: produces\n   \
    \ object: native-trna-oxidized-dus2-flavin\n    mechanism: The purified knockout-derived\
    \ RNA preparation oxidizes the prereduced flavin in the WT\n      enzyme. Separate\
    \ preparation and temperature effects are not collapsed into an isolated modification-specific\n\
    \      causal claim.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:19139092\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC2667719/\n      snippet: dihydrouridine\n\
    \      explanation: Visually inspected Figure 4 and read native-RNA purification\
    \ and kinetics Methods;\n        Figure 5's different mutant conditions constrain,\
    \ rather than extend, this edge.\n      cache_path: evidence/PF01207/rider-2009-dus2.txt\n\
    \      cache_sha256: c01a2e7cbc35858ec094ea5adfc89d1b3aa0bbf0d0c3456f354a7e696149de3a\n\
    - graph_id: dus2-ecoli-trna-aerobic-dihydrouridine-loss\n  title: Aerobic yeast\
    \ Dus2 treatment lowers dihydrouridine in bulk bacterial tRNA\n  scope: Recombinant\
    \ yeast Dus2 with bulk E. coli tRNA in the 18-h reverse-reaction experiment. This\
    \ is\n    a mixed-species in-vitro endpoint.\n  context: Treat 90 uM bulk E. coli\
    \ tRNA with 40 uM Dus2 aerobically for 18 h and assay dihydrouridine\n    content.\
    \ General kinetics default to 4 C, but the endpoint paragraph does not explicitly\
    \ restate temperature.\n    Do not borrow the anaerobic stopped-flow conditions\
    \ as an exact endpoint recipe.\n  family_mapping: The enzyme maps to P53720 with\
    \ PF01207 32-352; the bacterial RNA mixture is a separate\n    substrate whose\
    \ strain and individual tRNA composition are not resolved. It is not a pure yeast\
    \ physiological\n    system.\n  scope_status: MECHANISTIC\n  limitations: The\
    \ measured content decreases but is not eliminated. The assay does not identify\
    \ each\n    affected tRNA or nucleotide, measure cellular reverse flux, or independently\
    \ characterize every oxidation\n    product. Oxygen-supported endpoint turnover\
    \ is distinct from the short anaerobic spectral assay.\n  nodes:\n  - node_id:\
    \ aerobic-dus2-treatment-ecoli-trna\n    label: Treat bulk E. coli tRNA with yeast\
    \ Dus2 aerobically for 18 h\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:P53720\n\
    \  - node_id: bulk-ecoli-trna-dihydrouridine-content\n    label: Colorimetric\
    \ dihydrouridine content of the bulk bacterial tRNA\n    node_type: STATE\n  edges:\n\
    \  - edge_id: aerobic-dus2-treatment-decreases-bulk-dihydrouridine\n    subject:\
    \ aerobic-dus2-treatment-ecoli-trna\n    predicate: decreases\n    object: bulk-ecoli-trna-dihydrouridine-content\n\
    \    mechanism: The aerobic enzyme treatment reduces the measured dihydrouridine\
    \ content of the RNA mixture,\n      supporting reverse biochemical activity in\
    \ this context. It does not establish which yeast RNA sites\n      would undergo\
    \ a reverse reaction in cells.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:19139092\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2667719/\n      snippet:\
    \ dihydrouridine\n      explanation: Reverse-reaction Results and colorimetric\
    \ Methods were inspected; this reported endpoint\n        is separate from the\
    \ visually inspected Figure 8 spectral trace.\n      cache_path: evidence/PF01207/rider-2009-dus2.txt\n\
    \      cache_sha256: c01a2e7cbc35858ec094ea5adfc89d1b3aa0bbf0d0c3456f354a7e696149de3a\n\
    - graph_id: dus2-ecoli-trna-anaerobic-flavin-reduction\n  title: Bulk bacterial\
    \ tRNA reduces the flavin of yeast Dus2 anaerobically\n  scope: Oxidized WT yeast\
    \ Dus2 with bulk E. coli tRNA in Rider 2009 Figure 8, distinct from the aerobic\n\
    \    18-h content assay.\n  context: Mix anaerobic enzyme and RNA at 4 C in 100\
    \ mM HEPES pH 7.5, 100 mM NaCl, 10 mM MgCl2 and 10%\n    glycerol. Dus2 is 20\
    \ uM after mixing; stopped-flow A450 decrease is fitted with two phases.\n  family_mapping:\
    \ P53720 yeast Dus2 contains PF01207 32-352; the bacterial tRNA is a heterogeneous\
    \ substrate\n    pool. The shared enzyme identity does not make these mixed-species\
    \ half-reactions a directly tracked\n    native cycle.\n  scope_status: MECHANISTIC\n\
    \  limitations: RNA composition and individual reaction sites are unresolved.\
    \ Fitted mixture rate constants\n    are not intrinsic constants for a single\
    \ yeast tRNA. The smaller spectral phase and potential damaged\n    enzyme are\
    \ not extra molecular intermediates.\n  nodes:\n  - node_id: add-bulk-ecoli-trna-to-oxidized-dus2\n\
    \    label: Mix bulk E. coli tRNA with anaerobic oxidized yeast Dus2\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:P53720\n  - node_id: bacterial-trna-reduced-dus2-flavin\n\
    \    label: Reduced enzyme-bound flavin measured by A450 loss\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: bacterial-trna-produces-reduced-dus2-flavin\n\
    \    subject: add-bulk-ecoli-trna-to-oxidized-dus2\n    predicate: produces\n\
    \    object: bacterial-trna-reduced-dus2-flavin\n    mechanism: The bacterial\
    \ RNA mixture reduces the enzyme-bound flavin under anaerobic conditions. Together\n\
    \      with the separately measured aerobic content loss this supports biochemical\
    \ reversibility, but the\n      assays are not represented as one observed molecular\
    \ trajectory.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:19139092\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC2667719/\n      snippet: flavin reduction\n\
    \      explanation: Figure 8 was visually inspected with its caption and reverse-reaction\
    \ Results; the\n        paper explicitly warns against assigning mixture kinetics\
    \ to a pure yeast system.\n      cache_path: evidence/PF01207/rider-2009-dus2.txt\n\
    \      cache_sha256: c01a2e7cbc35858ec094ea5adfc89d1b3aa0bbf0d0c3456f354a7e696149de3a\n\
    curation_events:\n- timestamp: '2026-10-11T10:08:17Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate five scoped Dus2 redox and product-formation\
    \ effects\n  history_record: history/records/PF01207/2026-10-11T100817Z-codex-2bc635.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: P53720/DUS2_YEAST maps SMM1/DUS2/YNR015W, 384 aa and sequence version 1,
    to PF01207 32-352 with exact UniProt/InterPro agreement. The study identifies
    supplied pEfx-4b and YNR015w-knockout-derived RNA, but complete clones and tag
    junctions remain unverified. C117 lies inside the domain, yet the printed forward
    mutagenic primer encodes Q120 while its reverse partner and current reference
    encode H120. No C117A-only identity or mutant-specific causal edge is asserted.
  target_ids:
  - PF01207
  evidence_ids:
  - identity
  - primary
  - later-bacterial-dusa-lead
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Each graph retains one observed redox or product endpoint in its actual
    vessel and substrate context. The synthetic product assay does not independently
    localize U20. Native-RNA flavin oxidation is not promoted to a measured specific
    prior modification. Aerobic 18-h content loss and anaerobic bacterial-RNA flavin
    reduction remain separate mixed-species assays, not native reverse flux. No atomic
    hydride/proton-transfer or transitive full-cycle edge is invented.
  target_ids:
  - PF01207
  evidence_ids:
  - primary
  - native
  - later-bacterial-dusa-lead
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Figure 3 caption and Results differ at 35/60-uM enzyme and 450/457 nm;
    printed RNA template strings do not independently resolve the purported intron
    difference. Figure 4 image says mM while caption says uM. The C117A comparison
    uses a different temperature and contradictory oligos. Exact clones, RNA modifications,
    raw spectra, site-localized products and kinetic uncertainty need further work.
    The 2002 abstract and 2026 DusA abstract are leads, not adopted experimental extensions.
  target_ids:
  - PF01207
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01207-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Reconcile Dus2 constructs and substrates before residue-specific extension
  description: Obtain original WT/mutant sequences and exact RNA templates, reconcile
    concentrations and primer disagreements, and inspect matched-temperature comparisons
    and raw product data. Assess separate yeast specificity and modern bacterial/human
    or non-tRNA contexts with exact member mapping. Keep every new edge scoped to
    its experimentally supported endpoint and retain an evidence-backed successor
    review.
  target_ids:
  - PF01207
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - later-bacterial-dusa-lead
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01207.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Obtain original WT/mutant sequences and exact RNA templates, reconcile
    concentrations and primer disagreements, and inspect matched-temperature comparisons
    and raw product data. Assess separate yeast specificity and modern bacterial/human
    or non-tRNA contexts with exact member mapping. Keep every new edge scoped to
    its experimentally supported endpoint and retain an evidence-backed successor
    review.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01207
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Figures 2-5 and 8 were visually inspected; main Methods, Results and Discussion
  were read. Raw spectra, unshown stereochemical NMR and complete clones were not
  independently verified. Binding/amino-acid figures and structural models were not
  visually assessed. The 2026 primary abstract was retrieved through Europe PMC after
  the DOI web-reader route failed; full study review is not claimed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
