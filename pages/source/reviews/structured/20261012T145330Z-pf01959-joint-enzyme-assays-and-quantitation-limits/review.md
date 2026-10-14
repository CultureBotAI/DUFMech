# PF01959 joint-enzyme product observations and quantitative and cellular limits

- Review: 20261012T145330Z-pf01959-joint-enzyme-assays-and-quantitation-limits
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-12T14:53:10Z
- Finished UTC: 2026-10-12T14:53:30Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Partial same-agent scientific review of two graphs and three qualitative observed edges for full-length MJ0400 plus MJ1249. Directness applies to the complete biochemical mixture, not isolated PF01959 or elementary oxidative-deamination/cyclization steps. Quantitative and oxygen-condition conflicts, MMP0006 negative growth evidence and GriH full-text gaps remain explicit.

## Scope And Provenance

Inspect White2004 relevant Methods, Results, Figure3 and Table2, including original PDF pages3/7/9. Assess joint versus single-enzyme controls, derivative readouts, reported substrate amounts and conditions. Check current UniProt/InterPro member/domain identities, Porat2006 Results/legends/Methods and Suzuki2006 primary abstract. Not an exhaustive family review or independent assessment.

Selection: Next ascending uncurated PF01959 after PF01958; exact frozen family identity retained, with mapped Q58646 experiments and additional-member exclusions.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01959 | data/families/PF01959.yaml | generated | PF01959 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01959 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01959.

Q58646 v1/MJ1249 is361aa with PF01959 1-173 and PF26558 187-361, in the named M. jannaschii reference strain. The paper explicitly supplies this accession; historical plasmid sequence was not reconstructed. Q57843/MJ0400 is a separate required partner, not assigned a PF01959 activity. Q6M1B0/MMP0006 maps the same domain coordinates but its cellular context is distinct. A0JC76/GriH maps PF01959 30-208 and PF26558 221-396; current sequence equals B1VTI7, not an independent replicate. Imported fields are preserved.

### Directed effects and limits

graph: supported. Targets: PF01959.

Two MECHANISTIC graphs contain three OBSERVED/EXPERIMENTAL/DIRECT product-readout edges. Each source node is a complete joint assay; NAD and NADP are alternatives, not separate sufficient causes or a simultaneous requirement. DHQ-plus-DHB and postreaction chemically reduced quinic-acid readouts are distinguished. No validated absolute yield, elementary reaction, domain sufficiency, whole-cell essentiality or family-wide substrate transfer is claimed. The source's3,4-versus4,5 DHB wording maps onto the same ring positions by reverse numbering and is not treated as evidence of different products.

### Remaining family coverage

completeness: concern. Targets: PF01959.

Reconcile White2004 amounts, concentrations, oxygen wording and derivative quantitation; inspect raw traces, repeats, historical constructs and additional archaeal experiments. Inspect original Porat2006 plots and allele controls without transferring aroA prime phenotypes to aroB prime. Obtain full GriH assays, product identification and construct mapping; do not infer archaeal NAD dependence from shared domains. All8296 records and earlier open follow-ups remain in scope.

## Findings

### additional-contexts: Resolve joint-assay quantitative conflicts and extend mapped family contexts

minor / open / confirmed; issue key: pf01959-causal-context-coverage.

Determine why reported330nmol product exceeds stated substrate inputs and reconcile in-air versus under-argon descriptions before using quantitative yields. Extend primary evidence to raw traces, full constructs and other archaeal members. Keep MMP0006 negative growth and fractional-labeling limits separate from aroA prime deletion/rescue. Retrieve accessible Suzuki2006 full text and inspect GriH substrate/product/cofactor controls before adding its distinct graph. No quantitative correction, replacement enzyme or isolated-domain mechanism is invented.

## Recommended Actions And Acceptance Checks

### extend-contexts

Determine why reported330nmol product exceeds stated substrate inputs and reconcile in-air versus under-argon descriptions before using quantitative yields. Extend primary evidence to raw traces, full constructs and other archaeal members. Keep MMP0006 negative growth and fractional-labeling limits separate from aroA prime deletion/rescue. Retrieve accessible Suzuki2006 full text and inspect GriH substrate/product/cofactor controls before adding its distinct graph. No quantitative correction, replacement enzyme or isolated-domain mechanism is invented.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://doi.org/10.1021/bi0495127; White2004 Methods p7620, Figure3 p7624, recombinant-enzyme Results and Table2 with complete footnote p7626; original PDF pages3/7/9 visually inspected | supports | Pair-specific product formation is supported against single-enzyme controls. NAD and NADP assays have different buffer/readout from the phosphate controls and are retained only qualitatively. Reported330nmol exceeds the stated200nmol ASA and275nmol DKFP inputs; air/argon descriptions conflict. Immediate intermediates, NADH formation and residue-specific chemistry are not directly observed here. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/Q58646/; Accession and domain locations; paired UniProt identity facts | supports | Q58646 v1/MJ1249 is361aa with PF01959 1-173 and PF26558 187-361, in the named M. jannaschii reference strain. The paper explicitly supplies this accession; historical plasmid sequence was not reconstructed. Q57843/MJ0400 is a separate required partner, not assigned a PF01959 activity. Q6M1B0/MMP0006 maps the same domain coordinates but its cellular context is distinct. A0JC76/GriH maps PF01959 30-208 and PF26558 221-396; current sequence equals B1VTI7, not an independent replicate. Imported fields are preserved. |
| cellular-negative | https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2006.05426.x; Porat2006 MMP0006/S140 Results, Figure4/5 legends and initial DKFP-pathway extract-assay Methods | supports | S140 internal aroB prime replacement retains growth without aromatic-amino-acid/PABA supplementation in acetate minimal medium and reported high fractional labeling. This does not establish universal dispensability or a replacement enzyme, and aroA prime rescue concerns another gene. |
| grih-divergence | https://pubmed.ncbi.nlm.nih.gov/17003031/; Suzuki2006 primary abstract, not full assays or supplements | supports | GriH has a reported Mn-dependent aminohydroxybenzoate-forming role with GriI, distinct from archaeal DHQ chemistry. Current domain mapping is verified, but full primary experimental assessment and historical construct remain open; no observed GriH edge is added. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01959 | data/families/PF01959.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- White2004 relevant primary full text and original PDF pages3/7/9 were inspected, including Figure3/Table2, not raw chromatograms or every source figure. Porat2006 primary HTML Results, legends and extract-assay Methods were read; original growth plots and unshown Southern data were not visually inspected. Suzuki2006 coverage is primary abstract only; JBC PDF request returned403. No experimental replication.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.
- Ignored and hidden curation, evidence, history and structured-review paths were included in the collision search; no pre-existing PF01959 artifact was found in those scopes.
- Filesystem reads of both checkouts and installed skills succeeded without escalation, and the existing causal-graph skill passed quick_validate. The earlier filesystem-read denial was not reproduced; no permissions or configuration were changed.
- Native graph storage is supported in this unmerged worktree. Skill installation alone is not being reported as graph storage support on main or a published graph.
- Minimal source ledgers are hash-bound; the main checkout and immutable worklist remain untouched. The same agent authored and reviewed this scoped curation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T145330Z-pf01959-joint-enzyme-assays-and-quantitation-limits
title: PF01959 joint-enzyme product observations and quantitative and cellular limits
started_at: '2026-10-12T14:53:10Z'
finished_at: '2026-10-12T14:53:30Z'
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
summary: Partial same-agent scientific review of two graphs and three qualitative
  observed edges for full-length MJ0400 plus MJ1249. Directness applies to the complete
  biochemical mixture, not isolated PF01959 or elementary oxidative-deamination/cyclization
  steps. Quantitative and oxygen-condition conflicts, MMP0006 negative growth evidence
  and GriH full-text gaps remain explicit.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01959.yaml
    sha256: 481517667231ff25e6f35d68d5d09335484baf3e4a1a75a8adffc4767ed82deb
    role: context
  - path: data/families/PF01959.yaml
    sha256: 3b6e5393aef9e43780ad34b5fef81a8e6febc442977b1c4d0ed8fa26b4905245
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
  - path: evidence/PF01959/white-2004-joint-enzyme-assays.txt
    role: context
    sha256: da40baca40eff0bc28e659668f17453d7587803d11071c84c379daccda76a114
  - path: evidence/PF01959/identity-and-domain-boundaries.txt
    role: context
    sha256: f09aa493c00cd9407bcf4e0cfe0f2bab46886a4b36b14e9a761dd063979ac616
  - path: evidence/PF01959/porat-2006-negative-and-grih-followup.txt
    role: context
    sha256: 899d7dd3d1080b513bec7f47b243a74ee81291d3bc0e100425de5a35650c8e4b
targets:
- target_id: PF01959
  path: data/families/PF01959.yaml
  label: PF01959
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01959.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: b3ea3c2386d3b5558fc903f0ea2702d5df5320060e8b461c0eb04ec9abbf5c39
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Inspect White2004 relevant Methods, Results, Figure3 and Table2, including
    original PDF pages3/7/9. Assess joint versus single-enzyme controls, derivative
    readouts, reported substrate amounts and conditions. Check current UniProt/InterPro
    member/domain identities, Porat2006 Results/legends/Methods and Suzuki2006 primary
    abstract. Not an exhaustive family review or independent assessment.
  selection: Next ascending uncurated PF01959 after PF01958; exact frozen family identity
    retained, with mapped Q58646 experiments and additional-member exclusions.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01959
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Reconcile White2004 amounts, concentrations, oxygen wording and derivative
      quantitation; inspect raw traces, repeats, historical constructs and additional
      archaeal experiments. Inspect original Porat2006 plots and allele controls without
      transferring aroA prime phenotypes to aroB prime. Obtain full GriH assays, product
      identification and construct mapping; do not infer archaeal NAD dependence from
      shared domains. All8296 records and earlier open follow-ups remain in scope.
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
  - PF01959
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1021/bi0495127
  locator: White2004 Methods p7620, Figure3 p7624, recombinant-enzyme Results and
    Table2 with complete footnote p7626; original PDF pages3/7/9 visually inspected
  accessed_at: '2026-10-12T14:53:30Z'
  support: supports
  snapshot_sha256: da40baca40eff0bc28e659668f17453d7587803d11071c84c379daccda76a114
  summary: Pair-specific product formation is supported against single-enzyme controls.
    NAD and NADP assays have different buffer/readout from the phosphate controls
    and are retained only qualitatively. Reported330nmol exceeds the stated200nmol
    ASA and275nmol DKFP inputs; air/argon descriptions conflict. Immediate intermediates,
    NADH formation and residue-specific chemistry are not directly observed here.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/Q58646/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-12T14:53:30Z'
  support: supports
  snapshot_sha256: f09aa493c00cd9407bcf4e0cfe0f2bab46886a4b36b14e9a761dd063979ac616
  summary: Q58646 v1/MJ1249 is361aa with PF01959 1-173 and PF26558 187-361, in the
    named M. jannaschii reference strain. The paper explicitly supplies this accession;
    historical plasmid sequence was not reconstructed. Q57843/MJ0400 is a separate
    required partner, not assigned a PF01959 activity. Q6M1B0/MMP0006 maps the same
    domain coordinates but its cellular context is distinct. A0JC76/GriH maps PF01959
    30-208 and PF26558 221-396; current sequence equals B1VTI7, not an independent
    replicate. Imported fields are preserved.
- evidence_id: cellular-negative
  kind: primary_source
  reference: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2006.05426.x
  locator: Porat2006 MMP0006/S140 Results, Figure4/5 legends and initial DKFP-pathway
    extract-assay Methods
  summary: S140 internal aroB prime replacement retains growth without aromatic-amino-acid/PABA
    supplementation in acetate minimal medium and reported high fractional labeling.
    This does not establish universal dispensability or a replacement enzyme, and
    aroA prime rescue concerns another gene.
  accessed_at: '2026-10-12T14:53:30Z'
  support: supports
  snapshot_sha256: 899d7dd3d1080b513bec7f47b243a74ee81291d3bc0e100425de5a35650c8e4b
- evidence_id: grih-divergence
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/17003031/
  locator: Suzuki2006 primary abstract, not full assays or supplements
  summary: GriH has a reported Mn-dependent aminohydroxybenzoate-forming role with
    GriI, distinct from archaeal DHQ chemistry. Current domain mapping is verified,
    but full primary experimental assessment and historical construct remain open;
    no observed GriH edge is added.
  accessed_at: '2026-10-12T14:53:30Z'
  support: supports
  snapshot_sha256: 899d7dd3d1080b513bec7f47b243a74ee81291d3bc0e100425de5a35650c8e4b
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-12T14:53:30Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01959
  kind: record_content
  reference: data/families/PF01959.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-12T14:53:30Z'
  support: context_only
  snapshot_sha256: 3b6e5393aef9e43780ad34b5fef81a8e6febc442977b1c4d0ed8fa26b4905245
  quote: "id: Pfam:PF01959\npfam_id: PF01959\nname: 3-dehydroquinate synthase II N-terminal\
    \ domain\nshort_name: DHQS\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01959\n\
    counters:\n  proteins: 1847\n  matches: 1855\n  proteomes: 1461\n  taxa: 2975\n\
    \  structures: 0\n  alphafold_models: 1397\n  domain_architectures: 24\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR030960\ndescription: This entry represents the N-terminal\
    \ TIM barrel domain of 3-dehydroquinate synthase II. This\n  family includes members\
    \ of 3-dehydroquinate synthase II ([ec:1.4.1.24]), encoded by aroB genes in M.\n\
    \  maripaludis which is widely distributed in methanogens. In M. jannaschii, proteins\
    \ ADTH synthase (AroA)\n  and DHQ synthase II (AroB) are required to convert 6-deoxy-5-ketofructose-1-phosphate\
    \ (DKFP) and aspartate\n  semialdehyde to 3-dehydroquinate (DHQ) in vitro [[cite:PUB00109170],[cite:PUB00060486]].\n\
    curation_history: history/records/PF01959\ndiscussions:\n- discussion_id: pf01959-causal-context-coverage\n\
    \  prompt: Reconcile the reported joint-assay yields and extend independently\
    \ mapped member contexts.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale:\
    \ Purified MJ0400 plus MJ1249 supports product formation, but the reported quantitative\
    \ yields\n    conflict with the stated substrate amounts and do not resolve an\
    \ isolated PF01959 mechanism.\n  evidence:\n  - reference: PMID:15182204\n   \
    \ supports: PARTIAL\n    evidence_source: primary_publication\n    explanation:\
    \ Methods, Figure3 and Table2 were inspected, including original PDF pages3/7/9.\
    \ Rows9/10\n      report330nmol although stated inputs contain200nmol ASA and275nmol\
    \ DKFP; the air/argon descriptions\n      also conflict.\n  posed_by: Codex\n\
    \  posed_date: '2026-10-12'\n  notes: Resolve concentration, volume and product-quantitation\
    \ discrepancies before using absolute yields\n    or stoichiometry. Obtain raw\
    \ traces, replicate details and construct sequences; inspect additional\n    members\
    \ and GriH full experiments. Retain joint-protein scope, buffer/readout differences\
    \ and unmeasured\n    microsteps. All earlier corpus follow-ups remain open.\n\
    - discussion_id: pf01959-cellular-negative-and-grih-divergence\n  prompt: Keep\
    \ the MMP0006 negative phenotype and bacterial GriH chemistry separate from archaeal\
    \ joint-enzyme\n    assays.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale:\
    \ A mapped archaeal AroB' disruption does not require aromatic amino acids or\
    \ PABA under the\n    tested growth conditions; bacterial GriH has a distinct\
    \ product and reported cofactor context.\n  evidence:\n  - reference: PMID:17010158\n\
    \    supports: SUPPORT\n    evidence_source: primary_publication\n    explanation:\
    \ S140 disrupts MMP0006/aroB prime and grows in acetate-containing minimal medium.\
    \ AroA\n      prime deletion/rescue strains S170/S176 target another gene; their\
    \ phenotypes cannot be assigned\n      here.\n  - reference: PMID:17003031\n \
    \   supports: PARTIAL\n    evidence_source: primary_publication\n    explanation:\
    \ Only the primary abstract was inspected for GriH 3-amino-4-hydroxybenzoate formation.\n\
    \      Full assays and construct boundaries remain unreviewed; no observed GriH\
    \ edge is added.\n  posed_by: Codex\n  posed_date: '2026-10-12'\n  notes: Q6M1B0/MMP0006\
    \ has PF01959 1-173 and PF26558 187-361. S140 fractional labeling is not absolute\n\
    \    pathway flux, and no replacement enzyme is identified. A0JC76/GriH has PF01959\
    \ 30-208 and PF26558\n    221-396; its current sequence matches B1VTI7, not an\
    \ independent experiment. Retrieve full GriH paper\n    and controls. No universal\
    \ essentiality, dispensability or NAD dependence is inferred.\ncausal_graphs:\n\
    - graph_id: methanocaldococcus-joint-phosphate-assay-2004\n  title: MJ0400 and\
    \ MJ1249 jointly generate the measured DHQ-related product pool\n  scope: Purified\
    \ full-length Methanocaldococcus jannaschii MJ0400 and MJ1249 expressed separately\
    \ in\n    E. coli BL21-CodonPlus(DE3)-RIL; the causal source is the complete two-enzyme\
    \ assay, not an isolated\n    domain.\n  context: White2004 Table2 rows1-3 and\
    \ Methods p7620; 12.8ug MJ0400 plus35.7ug MJ1249, DKFP1.9mM and\n    ASA1.4mM\
    \ in145ul phosphate9.7mM pH7.2,30min60C under argon. Single-enzyme controls are\
    \ each below0.012nmol;\n    the pair reports7nmol summed DHQ and DHB by derivative\
    \ GC-MS with quinic-acid internal standard.\n  family_mapping: The paper identifies\
    \ MJ1249 as Q58646; current v1 reference is361aa with PF01959 1-173\n    and PF26558\
    \ 187-361, strain JAL-1/DSM2661/ATCC43067. MJ0400/Q57843 is a separate required\
    \ assay partner;\n    no PF01959 assignment is made for its activity. Historical\
    \ plasmid sequences were not independently\n    reconstructed.\n  taxon: NCBITaxon:243232\n\
    \  scope_status: MECHANISTIC\n  limitations: The output sums DHQ and its reported\
    \ downstream DHB readout, not a pure DHQ yield. No isolated-domain\n    sufficiency,\
    \ cellular essentiality, residue-level chemistry or direct observation of every\
    \ intermediate\n    is established. MJ0400 preparation contained a small chloramphenicol-acetyltransferase\
    \ contaminant.\n    No replicate/error estimates or raw chromatograms were reviewed.\n\
    \  nodes:\n  - node_id: joint-mix\n    label: MJ0400 plus MJ1249 with DKFP and\
    \ ASA in the phosphate assay\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:Q58646\n\
    \    - UniProtKB:Q57843\n  - node_id: product-pool\n    label: Measured combined\
    \ DHQ and DHB product pool\n    node_type: STATE\n  edges:\n  - edge_id: joint-product-formation\n\
    \    subject: joint-mix\n    predicate: produces\n    object: product-pool\n \
    \   mechanism: The reconstituted pair generates a product signal above both single-enzyme\
    \ controls. DIRECT\n      describes the measured biochemical reaction of the complete\
    \ mixture, not an elementary MJ1249-only\n      reaction or isolated N-terminal\
    \ domain catalysis.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:15182204\n      source_url:\
    \ https://doi.org/10.1021/bi0495127\n      snippet: Quantitation of DHQ Generated\
    \ with Purified Recombinant Enzymes Incubated with Precursors\n      explanation:\
    \ Table2 rows1-3 with footnote and Methods p7620 define the single-enzyme controls,\
    \ joint\n        assay and combined-product readout; original table was visually\
    \ inspected.\n      cache_path: evidence/PF01959/white-2004-joint-enzyme-assays.txt\n\
    \      cache_sha256: da40baca40eff0bc28e659668f17453d7587803d11071c84c379daccda76a114\n\
    - graph_id: methanocaldococcus-joint-pyridine-assays-2004\n  title: Separate NAD\
    \ and NADP joint assays produce the DHQ-derived readout\n  scope: Full-length\
    \ MJ0400 plus MJ1249 preparations assayed together with alternative added pyridine\n\
    \    nucleotides; not independently sufficient MJ1249, NAD or NADP.\n  context:\
    \ White2004 Table2 rows10/11,125ul with Tris28mM pH7.5, MgCl2 5.6mM, ASA1.6mM\
    \ and DKFP2.2mM,30min60C.\n    The same12.8ug MJ0400 and35.7ug MJ1249 are used.\
    \ Postreaction NaBH4 converts DHQ to quinic acid, assayed\n    by GC-MS with shikimate\
    \ internal standard. NAD and NADP are tested separately; their individual concentrations\n\
    \    are not specified in Table2.\n  family_mapping: Intact MJ1249/Q58646 v1 contains\
    \ PF01959 1-173 and PF26558 187-361; MJ0400/Q57843 supplies\n    a separate upstream\
    \ activity. Full-protein and multienzyme context are not transferred to the isolated\n\
    \    domain or to bacterial GriH.\n  taxon: NCBITaxon:243232\n  scope_status:\
    \ MECHANISTIC\n  limitations: Qualitative product formation only. The paper reports330nmol\
    \ for the NAD condition and150nmol\n    for NADP, but330nmol exceeds the stated200nmol\
    \ ASA and275nmol DKFP inputs; absolute yield and stoichiometry\n    remain unresolved.\
    \ The footnote says both in air and all samples under argon. Buffer and readout\
    \ differ\n    from rows1-3, so no clean cofactor fold-stimulation is inferred.\
    \ NADH formation, transient intermediates\n    and catalytic residues are not\
    \ directly measured here.\n  nodes:\n  - node_id: nad-mix\n    label: MJ0400 plus\
    \ MJ1249 with DKFP and ASA in the NAD-containing assay\n    node_type: ACTIVITY\n\
    \    grounding:\n    - UniProtKB:Q58646\n    - UniProtKB:Q57843\n  - node_id:\
    \ nad-product\n    label: DHQ-derived quinic-acid readout after the NAD assay\n\
    \    node_type: STATE\n  - node_id: nadp-mix\n    label: MJ0400 plus MJ1249 with\
    \ DKFP and ASA in the NADP-containing assay\n    node_type: ACTIVITY\n    grounding:\n\
    \    - UniProtKB:Q58646\n    - UniProtKB:Q57843\n  - node_id: nadp-product\n \
    \   label: DHQ-derived quinic-acid readout after the NADP assay\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: nad-assay-product\n    subject: nad-mix\n    predicate:\
    \ produces\n    object: nad-product\n    mechanism: The complete NAD-containing\
    \ reaction yields the product-associated GC-MS signal after chemical\n      reduction.\
    \ The edge retains the reported qualitative observation, not the inconsistent\
    \ absolute\n      amount, an enzyme-catalyzed quinic-acid reaction or an isolated\
    \ MJ1249 microstep.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:15182204\n      source_url:\
    \ https://doi.org/10.1021/bi0495127\n      snippet: the amount of quinic acid\
    \ observed.\n      explanation: Table2 row10, footnote and recombinant-assay Methods\
    \ specify the chemically converted\n        readout; reported yield and oxygen-condition\
    \ conflicts are retained in limitations.\n      cache_path: evidence/PF01959/white-2004-joint-enzyme-assays.txt\n\
    \      cache_sha256: da40baca40eff0bc28e659668f17453d7587803d11071c84c379daccda76a114\n\
    \  - edge_id: nadp-assay-product\n    subject: nadp-mix\n    predicate: produces\n\
    \    object: nadp-product\n    mechanism: The separate NADP-containing joint reaction\
    \ yields the product-associated signal after\n      chemical reduction. This is\
    \ not simultaneous NAD-plus-NADP dependence, a cofactor-preference kinetic\n \
    \     measurement or a family-wide specificity assignment.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:15182204\n      source_url: https://doi.org/10.1021/bi0495127\n\
    \      snippet: the amount of quinic acid observed.\n      explanation: Table2\
    \ row11 and footnote distinguish NADP from NAD and define the postreaction GC-MS\n\
    \        readout; alternative cofactor conditions are kept separate.\n      cache_path:\
    \ evidence/PF01959/white-2004-joint-enzyme-assays.txt\n      cache_sha256: da40baca40eff0bc28e659668f17453d7587803d11071c84c379daccda76a114\n\
    curation_events:\n- timestamp: '2026-10-12T14:47:26Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate PF01959 joint-enzyme product graphs\
    \ with explicit assay conflicts and negative contexts.\n  history_record: history/records/PF01959/2026-10-12T144726Z-codex-ac3bba.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Q58646 v1/MJ1249 is361aa with PF01959 1-173 and PF26558 187-361, in the
    named M. jannaschii reference strain. The paper explicitly supplies this accession;
    historical plasmid sequence was not reconstructed. Q57843/MJ0400 is a separate
    required partner, not assigned a PF01959 activity. Q6M1B0/MMP0006 maps the same
    domain coordinates but its cellular context is distinct. A0JC76/GriH maps PF01959
    30-208 and PF26558 221-396; current sequence equals B1VTI7, not an independent
    replicate. Imported fields are preserved.
  target_ids:
  - PF01959
  evidence_ids:
  - identity
  - primary
  - cellular-negative
  - grih-divergence
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Two MECHANISTIC graphs contain three OBSERVED/EXPERIMENTAL/DIRECT product-readout
    edges. Each source node is a complete joint assay; NAD and NADP are alternatives,
    not separate sufficient causes or a simultaneous requirement. DHQ-plus-DHB and
    postreaction chemically reduced quinic-acid readouts are distinguished. No validated
    absolute yield, elementary reaction, domain sufficiency, whole-cell essentiality
    or family-wide substrate transfer is claimed. The source's3,4-versus4,5 DHB wording
    maps onto the same ring positions by reverse numbering and is not treated as evidence
    of different products.
  target_ids:
  - PF01959
  evidence_ids:
  - primary
  - native
  - cellular-negative
  - grih-divergence
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Reconcile White2004 amounts, concentrations, oxygen wording and derivative
    quantitation; inspect raw traces, repeats, historical constructs and additional
    archaeal experiments. Inspect original Porat2006 plots and allele controls without
    transferring aroA prime phenotypes to aroB prime. Obtain full GriH assays, product
    identification and construct mapping; do not infer archaeal NAD dependence from
    shared domains. All8296 records and earlier open follow-ups remain in scope.
  target_ids:
  - PF01959
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01959-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve joint-assay quantitative conflicts and extend mapped family contexts
  description: Determine why reported330nmol product exceeds stated substrate inputs
    and reconcile in-air versus under-argon descriptions before using quantitative
    yields. Extend primary evidence to raw traces, full constructs and other archaeal
    members. Keep MMP0006 negative growth and fractional-labeling limits separate
    from aroA prime deletion/rescue. Retrieve accessible Suzuki2006 full text and
    inspect GriH substrate/product/cofactor controls before adding its distinct graph.
    No quantitative correction, replacement enzyme or isolated-domain mechanism is
    invented.
  target_ids:
  - PF01959
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - cellular-negative
  - grih-divergence
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01959.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Determine why reported330nmol product exceeds stated substrate inputs
    and reconcile in-air versus under-argon descriptions before using quantitative
    yields. Extend primary evidence to raw traces, full constructs and other archaeal
    members. Keep MMP0006 negative growth and fractional-labeling limits separate
    from aroA prime deletion/rescue. Retrieve accessible Suzuki2006 full text and
    inspect GriH substrate/product/cofactor controls before adding its distinct graph.
    No quantitative correction, replacement enzyme or isolated-domain mechanism is
    invented.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01959
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- White2004 relevant primary full text and original PDF pages3/7/9 were inspected,
  including Figure3/Table2, not raw chromatograms or every source figure. Porat2006
  primary HTML Results, legends and extract-assay Methods were read; original growth
  plots and unshown Southern data were not visually inspected. Suzuki2006 coverage
  is primary abstract only; JBC PDF request returned403. No experimental replication.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
- Ignored and hidden curation, evidence, history and structured-review paths were
  included in the collision search; no pre-existing PF01959 artifact was found in
  those scopes.
- Filesystem reads of both checkouts and installed skills succeeded without escalation,
  and the existing causal-graph skill passed quick_validate. The earlier filesystem-read
  denial was not reproduced; no permissions or configuration were changed.
- Native graph storage is supported in this unmerged worktree. Skill installation
  alone is not being reported as graph storage support on main or a published graph.
- Minimal source ledgers are hash-bound; the main checkout and immutable worklist
  remain untouched. The same agent authored and reviewed this scoped curation.
```
