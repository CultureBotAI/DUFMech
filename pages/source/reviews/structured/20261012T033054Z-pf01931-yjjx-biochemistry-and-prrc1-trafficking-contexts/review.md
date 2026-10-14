# PF01931: YjjX biochemistry and PRRC1 trafficking contexts

- Review: 20261012T033054Z-pf01931-yjjx-biochemistry-and-prrc1-trafficking-contexts
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-12T03:30:28Z
- Finished UTC: 2026-10-12T03:30:54Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Eight graphs retain20 OBSERVED effects,8 DIRECT,9 INDIRECT and3 UNRESOLVED, in2 MECHANISTIC and6 PHENOTYPIC contexts. Five evidence ledgers and two OPEN discussions preserve source conflicts and member/domain gaps. Same-agent scoped scientific review; IN_PROGRESS, not complete family review.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Ascending uncurated Pfam after PF01930. All8296 families and open follow-ups remain in scope.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01931 | data/families/PF01931.yaml | generated | PF01931 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01931 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01931.

Frozen DUF84/NTPase_I-T/IPR026533 identity is preserved. P39411v2 is170aa with current match4-168; deposited1U5W is184aa with MLI prefix and SGRVEHHHHHH suffix, while the thesis primer suggests MLLI. Do not transfer structural numbering without alignment. Human Q96M27v1 is445aa with current match260-376, not historical264-355. Human gene depletion/rescue and recombinant assays do not verify every clone sequence or isolated-domain sufficiency. Rat cytosol is a distinct mixed-species component. First100 UniProt matches are an incomplete member sample.

### Directed effects and limits

graph: supported. Targets: PF01931.

YjjX phosphate release and separate inhibitor-dose curves are biochemical observations, not product-specific chemistry, competitive-binding proof or native RNA sanitization. PRRC1 knockdown effects on coat fluorescence and synchronized EGFR/ShhN transport remain indirect. Peng2025 ATRAP Golgi enrichment differs from ATG9A ER retention/rescue; panelI mislabels its axis and is interpreted with images, legend and Results. GST-PRRC1 addition changes vesicle-fraction cargo signals in a multicomponent assay with no shown GST-only lane; directness remains unresolved. LC3 size/count effects are morphology, not autophagic flux or demonstrated mediation by ATG9A. Co-IP and negative lipid-free Sar1 pulldown do not become direct binding or activation edges.

### Remaining family coverage

completeness: concern. Targets: PF01931.

YjjX source discrepancies, N-terminal extension and quantitative kinetics need follow-up. PNAS supplementary clone, guide, siRNA, isoform and purification details remain inaccessible. Zebrafish Mys development and PKA studies, Liu2025 domain-specific COPII thesis, Lawhorn thiamine-antimetabolite screen, VC0702/1U14 and Thermoplasma fusions remain open primary contexts. No all-member characterization or family-wide negative is claimed.

## Findings

### additional-contexts: Resolve source and construct limits and extend domain-specific and member coverage

minor / open / confirmed; issue key: pf01931-causal-context-coverage.

Verify YjjX construct numbering and conflicting substrate/metal/Km text; obtain PNAS supplementary methods and clarify panel7I labeling. Inspect accession-mapped Mys/PKA developmental studies and PRRC1 domain-specific thesis before adding their mechanisms. Extend Lawhorn,VC0702,Salmonella and fusion-member coverage with primary controls. Retain scoped effects and IN_PROGRESS until justified full-scope successor evidence exists.

## Recommended Actions And Acceptance Checks

### extend-contexts

Verify YjjX construct numbering and conflicting substrate/metal/Km text; obtain PNAS supplementary methods and clarify panel7I labeling. Inspect accession-mapped Mys/PKA developmental studies and PRRC1 domain-specific thesis before adding their mechanisms. Extend Lawhorn,VC0702,Salmonella and fusion-member coverage with primary controls. Retain scoped effects and IN_PROGRESS until justified full-scope successor evidence exists.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR69981.PDF; Author thesis chapter4 republication of Zheng2005; PDF109,119,121-123,125-131,133-135; Tables4.2/4.3 and Figure4.5 visually checked. | supports | Purified YjjX supports five separate purine-substrate phosphate-release assays and inhibition of ITPase signal by separately added ATP,GTP and thiamine pyrophosphate. No direct product identification, RNA-protection effect or elementary residue mechanism is established by these assays. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01931/; Accession and domain locations; paired UniProt identity facts | supports | Frozen DUF84/NTPase_I-T/IPR026533 identity is preserved. P39411v2 is170aa with current match4-168; deposited1U5W is184aa with MLI prefix and SGRVEHHHHHH suffix, while the thesis primer suggests MLLI. Do not transfer structural numbering without alignment. Human Q96M27v1 is445aa with current match260-376, not historical264-355. Human gene depletion/rescue and recombinant assays do not verify every clone sequence or isolated-domain sufficiency. Rat cytosol is a distinct mixed-species component. First100 UniProt matches are an incomplete member sample. |
| human-knockdown | https://pmc.ncbi.nlm.nih.gov/articles/PMC8536394/; Huang2021 PRRC1 Results, Methods and Figure5. | supports | HEK293T knockdown increases coat fluorescence and delays two RUSH reporters. Association data do not establish direct binding or isolated-domain chemistry. |
| human-knockout-and-reconstitution | https://pmc.ncbi.nlm.nih.gov/articles/PMC12519218/; Peng2025 PRRC1 Results, Methods and Figure7. | supports | Distinct ATRAP/ATG9A localization effects,ATG9A rescue,mixed-assay cargo packaging and LC3 morphology are retained with panelI label conflict and missing-method limits. |
| source-coverage | evidence/PF01931/coverage.txt; Member inventory, primary leads and access ledger. | supports | Remaining member and domain-specific studies are follow-ups, not negative evidence or automatically transferred pathways. No claim of exhaustive search. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01931 | data/families/PF01931.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- YjjX Tables4.2/4.3 and Figure4.5, Huang Figure5 and Peng Figure7 visually inspected; corresponding primary Results and Methods read. YjjX source was author's explicit republication, not independent replication. PNAS supplements and Liu thesis full text unavailable. No raw-data reanalysis, clone resequencing, independent expert review or exhaustive member survey. Browser and corpus verification are recorded separately after retention.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T033054Z-pf01931-yjjx-biochemistry-and-prrc1-trafficking-contexts
title: 'PF01931: YjjX biochemistry and PRRC1 trafficking contexts'
started_at: '2026-10-12T03:30:28Z'
finished_at: '2026-10-12T03:30:54Z'
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
summary: Eight graphs retain20 OBSERVED effects,8 DIRECT,9 INDIRECT and3 UNRESOLVED,
  in2 MECHANISTIC and6 PHENOTYPIC contexts. Five evidence ledgers and two OPEN discussions
  preserve source conflicts and member/domain gaps. Same-agent scoped scientific review;
  IN_PROGRESS, not complete family review.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01931.yaml
    sha256: 6c5c0b85a20ba6ab520dccd4713a10a2ab097ab2d3871db63a086a7492129f53
    role: context
  - path: data/families/PF01931.yaml
    sha256: 1f314f46f6221c2982d5f738c988b1385143f181d0a3a7a40e2e73f2be7f0214
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
  - path: evidence/PF01931/zheng-2005.txt
    role: context
    sha256: f1b0e6eb3fe0854c25cbf76643c584ea6c913dac8e0cf7c5922b58d82b09dba2
  - path: evidence/PF01931/identity.txt
    role: context
    sha256: 9207049089ca760dd8c9fbe6c2f1f7be22902bea5b80eefbf5e59a78f31c70f6
  - path: evidence/PF01931/huang-2021.txt
    role: context
    sha256: 926a457831cb58656e252438e3c957427d5c955430f2881127130b8b58f96da2
  - path: evidence/PF01931/peng-2025.txt
    role: context
    sha256: af7e652b91d8ac0e2dc063f6429299ccbe7855bf07cd972ddaaedbd152937fe0
  - path: evidence/PF01931/coverage.txt
    role: context
    sha256: a561cd9749f6bac4866ea02ad72f60f5861dbd040ee4751b8e0bae202e57a8ac
targets:
- target_id: PF01931
  path: data/families/PF01931.yaml
  label: PF01931
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01931.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: e5a01b035c3c2b918f684a6f4958819131d401acd03d34427c0cb49ea70e90b4
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Ascending uncurated Pfam after PF01930. All8296 families and open follow-ups
    remain in scope.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01931
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: YjjX source discrepancies, N-terminal extension and quantitative kinetics
      need follow-up. PNAS supplementary clone, guide, siRNA, isoform and purification
      details remain inaccessible. Zebrafish Mys development and PKA studies, Liu2025
      domain-specific COPII thesis, Lawhorn thiamine-antimetabolite screen, VC0702/1U14
      and Thermoplasma fusions remain open primary contexts. No all-member characterization
      or family-wide negative is claimed.
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
  - PF01931
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR69981.PDF
  locator: Author thesis chapter4 republication of Zheng2005; PDF109,119,121-123,125-131,133-135;
    Tables4.2/4.3 and Figure4.5 visually checked.
  accessed_at: '2026-10-12T03:30:54Z'
  support: supports
  snapshot_sha256: f1b0e6eb3fe0854c25cbf76643c584ea6c913dac8e0cf7c5922b58d82b09dba2
  summary: Purified YjjX supports five separate purine-substrate phosphate-release
    assays and inhibition of ITPase signal by separately added ATP,GTP and thiamine
    pyrophosphate. No direct product identification, RNA-protection effect or elementary
    residue mechanism is established by these assays.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01931/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-12T03:30:54Z'
  support: supports
  snapshot_sha256: 9207049089ca760dd8c9fbe6c2f1f7be22902bea5b80eefbf5e59a78f31c70f6
  summary: Frozen DUF84/NTPase_I-T/IPR026533 identity is preserved. P39411v2 is170aa
    with current match4-168; deposited1U5W is184aa with MLI prefix and SGRVEHHHHHH
    suffix, while the thesis primer suggests MLLI. Do not transfer structural numbering
    without alignment. Human Q96M27v1 is445aa with current match260-376, not historical264-355.
    Human gene depletion/rescue and recombinant assays do not verify every clone sequence
    or isolated-domain sufficiency. Rat cytosol is a distinct mixed-species component.
    First100 UniProt matches are an incomplete member sample.
- evidence_id: human-knockdown
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8536394/
  locator: Huang2021 PRRC1 Results, Methods and Figure5.
  summary: HEK293T knockdown increases coat fluorescence and delays two RUSH reporters.
    Association data do not establish direct binding or isolated-domain chemistry.
  accessed_at: '2026-10-12T03:30:54Z'
  support: supports
  snapshot_sha256: 926a457831cb58656e252438e3c957427d5c955430f2881127130b8b58f96da2
- evidence_id: human-knockout-and-reconstitution
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC12519218/
  locator: Peng2025 PRRC1 Results, Methods and Figure7.
  summary: Distinct ATRAP/ATG9A localization effects,ATG9A rescue,mixed-assay cargo
    packaging and LC3 morphology are retained with panelI label conflict and missing-method
    limits.
  accessed_at: '2026-10-12T03:30:54Z'
  support: supports
  snapshot_sha256: af7e652b91d8ac0e2dc063f6429299ccbe7855bf07cd972ddaaedbd152937fe0
- evidence_id: source-coverage
  kind: search
  reference: evidence/PF01931/coverage.txt
  locator: Member inventory, primary leads and access ledger.
  search_scope: DUF84/PF01931/NTPase_I-T/YjjX/PRRC1; current InterPro and first100
    UniProt members; primary-reference searches and ignored/hidden-inclusive local
    curation search.
  summary: Remaining member and domain-specific studies are follow-ups, not negative
    evidence or automatically transferred pathways. No claim of exhaustive search.
  accessed_at: '2026-10-12T03:30:54Z'
  support: supports
  snapshot_sha256: a561cd9749f6bac4866ea02ad72f60f5861dbd040ee4751b8e0bae202e57a8ac
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-12T03:30:54Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01931
  kind: record_content
  reference: data/families/PF01931.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-12T03:30:54Z'
  support: context_only
  snapshot_sha256: 1f314f46f6221c2982d5f738c988b1385143f181d0a3a7a40e2e73f2be7f0214
  quote: "id: Pfam:PF01931\npfam_id: PF01931\nname: Protein of unknown function DUF84\n\
    short_name: NTPase_I-T\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01931\n\
    counters:\n  proteins: 3984\n  matches: 4030\n  proteomes: 3631\n  taxa: 7463\n\
    \  structures: 4\n  alphafold_models: 2998\n  domain_architectures: 24\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR026533\ndescription: NTPase_I-T is a family of NTPases\
    \ with supreme activity against ITP and XTP. Active site\n  analysis and structure\
    \ comparison of YjjX strongly suggested that it is an NTP binding protein with\n\
    \  nucleoside triphosphatase activity. YjjX exhibits a mixed alpha-beta fold [[cite:PUB00038960],[cite:PUB00037841]].\n\
    curation_history: history/records/PF01931\ndiscussions:\n- discussion_id: pf01931-construct-and-source-conflicts\n\
    \  prompt: Resolve construct numbering, primary-source discrepancies and missing\
    \ supplementary methods.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale:\
    \ Assay-specific effects are supported without identifying every construct or\
    \ silently normalizing\n    conflicting statements.\n  evidence:\n  - reference:\
    \ PMID:16216582\n    supports: PARTIAL\n    evidence_source: author_thesis_republication\n\
    \    explanation: Substrate exclusions, GDP Km and Mn activity differ between\
    \ prose and tables; deposited\n      and primer-derived N termini also differ.\n\
    \  - reference: PMID:41032520\n    supports: PARTIAL\n    evidence_source: primary_figure_and_results\n\
    \    explanation: Figure7I labels ATRAP while its images, legend and Results identify\
    \ ATG9A; supplement-dependent\n      construct details remain unavailable.\n \
    \ posed_by: Codex\n  posed_date: '2026-10-12'\n  notes: Retain MLI versus primer-suggested\
    \ MLLI extension,5mM standard versus10mM kinetic Mg, and unavailable\n    PNAS\
    \ supplementary methods. TPP is thiamine pyrophosphate. Human PRRC1 accession\
    \ identifies the gene,\n    not verified sequence identity of every experimental\
    \ clone.\n- discussion_id: pf01931-member-and-domain-coverage\n  prompt: Extend\
    \ primary review to zebrafish Mys, domain-specific PRRC1 assays and other NTPase_I-T\
    \ members.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: YjjX and whole-human-PRRC1\
    \ assays do not characterize every frozen family member or prove\n    isolated\
    \ PF01931 function.\n  evidence:\n  - reference: PMID:18342848\n    supports:\
    \ PARTIAL\n    evidence_source: primary_source_discovery\n    explanation: Zebrafish\
    \ misty-somites developmental study is a discovered follow-up, not a reviewed\n\
    \      graph.\n  - reference: PMID:20018846\n    supports: PARTIAL\n    evidence_source:\
    \ primary_source_discovery\n    explanation: Mys-PKA regulation needs construct-mapped\
    \ primary methods and figure review.\n  posed_by: Codex\n  posed_date: '2026-10-12'\n\
    \  notes: See coverage ledger for Lawhorn thiamine-antimetabolite screen, VC0702/1U14,\
    \ Thermoplasma fusions\n    and Liu2025 thesis. No RNA-protection, translation-inhibition,\
    \ PRRC1 NTP hydrolysis or family-wide\n    negative conclusion is established\
    \ here.\ncausal_graphs:\n- graph_id: yjjx-substrate-hydrolysis-2005\n  title:\
    \ Purified YjjX releases phosphate with five tested purine substrates\n  scope:\
    \ Zheng2005 study inspected through author's2009 thesis chapter4, table4.2 and\
    \ Methods4.5.5-6;\n    separate substrate reactions.\n  context: C-His6 YjjX expressed\
    \ in BL21(DE3);25C,pH6.75 Bis-Tris. Standard assay5mM MgCl2, table kinetics10mM;\n\
    \    enzyme-free substrate blanks subtracted.\n  family_mapping: P39411 sequencev2,170aa,taxon83333;\
    \ PF01931 matches4-168. Deposited1U5W184aa is MLI\n    plus canonical sequence\
    \ plus SGRVEHHHHHH; primer suggests MLLI. No isolated-domain assay.\n  taxon:\
    \ NCBITaxon:83333\n  scope_status: MECHANISTIC\n  limitations: Colorimetric phosphate\
    \ release does not independently identify IDP/XDP or elementary chemistry.\n \
    \   dATP/dCTP prose versus8mM table signals conflict. No native nucleotide-pool\
    \ or oxidative-survival\n    effect is measured.\n  nodes:\n  - node_id: itp\n\
    \    label: Purified YjjX with ITP and Mg\n    node_type: STATE\n    grounding:\n\
    \    - UniProtKB:P39411\n  - node_id: xtp\n    label: Purified YjjX with XTP and\
    \ Mg\n    node_type: STATE\n  - node_id: ditp\n    label: Purified YjjX with dITP\
    \ and Mg\n    node_type: STATE\n  - node_id: gtp\n    label: Purified YjjX with\
    \ GTP and Mg\n    node_type: STATE\n  - node_id: gdp\n    label: Purified YjjX\
    \ with GDP and Mg\n    node_type: STATE\n  - node_id: phosphate\n    label: Background-corrected\
    \ phosphate release\n    node_type: STATE\n  edges:\n  - edge_id: itp-hydrolysis\n\
    \    subject: itp\n    predicate: produces\n    object: phosphate\n    mechanism:\
    \ The enzyme-containing ITP assay gives phosphate above enzyme-free background;\
    \ apparent\n      kinetic parameters support substrate turnover.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:16216582\n      source_url: https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR69981.PDF\n\
    \      snippet: Kinetic Data of YjjX with Various Substrates\n      explanation:\
    \ Thesis table4.2 ITP row, Results4.3.4 and phosphate assay Methods4.5.5-6.\n\
    \      cache_path: evidence/PF01931/zheng-2005.txt\n      cache_sha256: f1b0e6eb3fe0854c25cbf76643c584ea6c913dac8e0cf7c5922b58d82b09dba2\n\
    \  - edge_id: xtp-hydrolysis\n    subject: xtp\n    predicate: produces\n    object:\
    \ phosphate\n    mechanism: Purified YjjX supports XTP-dependent phosphate release;\
    \ the remaining nucleotide product\n      is not separately resolved here.\n \
    \   directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:16216582\n      source_url: https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR69981.PDF\n\
    \      snippet: Kinetic Data of YjjX with Various Substrates\n      explanation:\
    \ Thesis table4.2 XTP row and background-corrected assay Methods.\n      cache_path:\
    \ evidence/PF01931/zheng-2005.txt\n      cache_sha256: f1b0e6eb3fe0854c25cbf76643c584ea6c913dac8e0cf7c5922b58d82b09dba2\n\
    \  - edge_id: ditp-hydrolysis\n    subject: ditp\n    predicate: produces\n  \
    \  object: phosphate\n    mechanism: The dITP assay shows phosphate release at\
    \ the tested concentrations; a higher apparent\n      Km does not prove a physiological\
    \ DNA-protection role.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:16216582\n      source_url:\
    \ https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR69981.PDF\n\
    \      snippet: Kinetic Data of YjjX with Various Substrates\n      explanation:\
    \ Thesis table4.2 dITP row, Results and Methods.\n      cache_path: evidence/PF01931/zheng-2005.txt\n\
    \      cache_sha256: f1b0e6eb3fe0854c25cbf76643c584ea6c913dac8e0cf7c5922b58d82b09dba2\n\
    \  - edge_id: gtp-hydrolysis\n    subject: gtp\n    predicate: produces\n    object:\
    \ phosphate\n    mechanism: GTP is a weaker phosphate-release substrate in the\
    \ separate substrate assay; this differs\n      from its effect when added to\
    \ an ITP reaction.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:16216582\n      source_url:\
    \ https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR69981.PDF\n\
    \      snippet: Kinetic Data of YjjX with Various Substrates\n      explanation:\
    \ Thesis table4.2 GTP row and Discussion, not the inhibitor curve.\n      cache_path:\
    \ evidence/PF01931/zheng-2005.txt\n      cache_sha256: f1b0e6eb3fe0854c25cbf76643c584ea6c913dac8e0cf7c5922b58d82b09dba2\n\
    \  - edge_id: gdp-hydrolysis\n    subject: gdp\n    predicate: produces\n    object:\
    \ phosphate\n    mechanism: GDP supports phosphate release in the purified-enzyme\
    \ assay; this does not establish regulation\n      of an EF-Tu-bound nucleotide.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:16216582\n      source_url: https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR69981.PDF\n\
    \      snippet: Kinetic Data of YjjX with Various Substrates\n      explanation:\
    \ Thesis table4.2 GDP row; prose/table Km discrepancy retained without adopting\
    \ a numerical\n        edge.\n      cache_path: evidence/PF01931/zheng-2005.txt\n\
    \      cache_sha256: f1b0e6eb3fe0854c25cbf76643c584ea6c913dac8e0cf7c5922b58d82b09dba2\n\
    - graph_id: yjjx-inhibitor-assay-2005\n  title: Three separately added compounds\
    \ reduce YjjX ITPase signal\n  scope: Zheng2005 thesis-republished figure4.5;\
    \ individually varied ATP,GTP or thiamine pyrophosphate.\n  context: Purified\
    \ C-His6 YjjX ITP assay,pH6.75,25C,divalent metal; relative activity versus added-compound\n\
    \    concentration.\n  family_mapping: P39411 sequencev2,170aa; PF01931 matches4-168.\
    \ Full recombinant protein with unresolved\n    N-terminal extension numbering.\n\
    \  taxon: NCBITaxon:83333\n  scope_status: MECHANISTIC\n  limitations: Dose-dependent\
    \ reaction inhibition does not independently establish competitive binding\n \
    \   or a thiamine-detoxification pathway. TPP is not thymidine triphosphate; GTP\
    \ also has weak substrate\n    activity in a different assay.\n  nodes:\n  - node_id:\
    \ atp\n    label: ATP addition to the YjjX ITP reaction\n    node_type: PERTURBATION\n\
    \  - node_id: gtp\n    label: GTP addition to the YjjX ITP reaction\n    node_type:\
    \ PERTURBATION\n  - node_id: tpp\n    label: Thiamine pyrophosphate addition to\
    \ the YjjX ITP reaction\n    node_type: PERTURBATION\n  - node_id: activity\n\
    \    label: Relative ITPase phosphate-release signal\n    node_type: ACTIVITY\n\
    \    grounding:\n    - UniProtKB:P39411\n  edges:\n  - edge_id: atp-inhibition\n\
    \    subject: atp\n    predicate: decreases\n    object: activity\n    mechanism:\
    \ Increasing separately added ATP reduces the measured ITPase signal under the\
    \ purified-protein\n      assay conditions.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:16216582\n\
    \      source_url: https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR69981.PDF\n\
    \      snippet: ITPase Activity\n      explanation: Thesis figure4.5 ATP curve\
    \ and caption, read with Methods4.5.5-6.\n      cache_path: evidence/PF01931/zheng-2005.txt\n\
    \      cache_sha256: f1b0e6eb3fe0854c25cbf76643c584ea6c913dac8e0cf7c5922b58d82b09dba2\n\
    \  - edge_id: gtp-inhibition\n    subject: gtp\n    predicate: decreases\n   \
    \ object: activity\n    mechanism: Increasing GTP in the ITP-containing reaction\
    \ lowers relative ITPase signal; no cellular\n      GTP-regulation mechanism is\
    \ established.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:16216582\n      source_url:\
    \ https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR69981.PDF\n\
    \      snippet: ITPase Activity\n      explanation: Thesis figure4.5 GTP curve;\
    \ distinguished from table4.2 GTP-substrate assay.\n      cache_path: evidence/PF01931/zheng-2005.txt\n\
    \      cache_sha256: f1b0e6eb3fe0854c25cbf76643c584ea6c913dac8e0cf7c5922b58d82b09dba2\n\
    \  - edge_id: tpp-inhibition\n    subject: tpp\n    predicate: decreases\n   \
    \ object: activity\n    mechanism: Thiamine pyrophosphate reduces the measured\
    \ ITPase signal; hydrolysis of TPP or an antimetabolite\n      is not shown by\
    \ this inhibition test.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:16216582\n      source_url:\
    \ https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR69981.PDF\n\
    \      snippet: ITPase Activity\n      explanation: Thesis figure4.5 TPP curve\
    \ and Results explicitly identifying thiamine pyrophosphate.\n      cache_path:\
    \ evidence/PF01931/zheng-2005.txt\n      cache_sha256: f1b0e6eb3fe0854c25cbf76643c584ea6c913dac8e0cf7c5922b58d82b09dba2\n\
    - graph_id: prrc1-coat-signal-2021\n  title: PRRC1 knockdown increases two COPII\
    \ immunofluorescence signals\n  scope: Huang2021 Figure5E-T, HEK293T PRRC1 siRNA\
    \ versus control.\n  context: Day3 after transfection; total cellular fluorescence,three\
    \ experiments,>125cells per experiment.\n    SEC31A protein abundance and Golgin97\
    \ controls.\n  family_mapping: Human Q96M27 sequencev1,445aa,PF01931 matches260-376.\
    \ Whole-gene knockdown, not isolated-domain\n    perturbation; exact siRNA/isoform\
    \ details unverified.\n  taxon: NCBITaxon:9606\n  scope_status: PHENOTYPIC\n \
    \ limitations: Fluorescence is not a direct coat-disassembly rate. No siRNA-resistant\
    \ rescue is shown\n    here; domain mechanism and indirect cellular alternatives\
    \ remain unresolved.\n  nodes:\n  - node_id: knockdown\n    label: PRRC1 siRNA\
    \ versus control in HEK293T\n    node_type: PERTURBATION\n    grounding:\n   \
    \ - UniProtKB:Q96M27\n  - node_id: sec31\n    label: Cellular SEC31A immunofluorescence\n\
    \    node_type: PHENOTYPE\n  - node_id: sec24\n    label: Cellular SEC24C immunofluorescence\n\
    \    node_type: PHENOTYPE\n  edges:\n  - edge_id: sec31-signal\n    subject: knockdown\n\
    \    predicate: increases\n    object: sec31\n    mechanism: PRRC1 depletion increases\
    \ the cellular SEC31A fluorescent readout despite comparable total\n      SEC31A\
    \ protein on immunoblot.\n    directness: INDIRECT\n    support: OBSERVED\n  \
    \  evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:34433667\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8536394/\n      snippet:\
    \ knockdown\n      explanation: Figure5E,F-K,R, with Golgin97 controlT; measured\
    \ localization proxy, not direct uncoating.\n      cache_path: evidence/PF01931/huang-2021.txt\n\
    \      cache_sha256: 926a457831cb58656e252438e3c957427d5c955430f2881127130b8b58f96da2\n\
    \  - edge_id: sec24-signal\n    subject: knockdown\n    predicate: increases\n\
    \    object: sec24\n    mechanism: PRRC1 depletion increases cellular SEC24C immunofluorescence\
    \ under the matched imaging\n      protocol.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:34433667\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8536394/\n      snippet:\
    \ knockdown\n      explanation: Figure5L-Q,S and controlT; no direct molecular\
    \ interaction assigned.\n      cache_path: evidence/PF01931/huang-2021.txt\n \
    \     cache_sha256: 926a457831cb58656e252438e3c957427d5c955430f2881127130b8b58f96da2\n\
    - graph_id: prrc1-rush-transport-2021\n  title: PRRC1 depletion delays two RUSH\
    \ reporters reaching the Golgi\n  scope: Huang2021 Figure5U-X, separate SBP-EGFP-EGFR\
    \ and SBP-EGFP-ShhN reporters in HEK293T.\n  context: Day3 siRNA; reporter24h\
    \ after siRNA;40uM biotin and100ng/ul cycloheximide release,15/30min;three\n \
    \   experiments,>100cells each.\n  family_mapping: Q96M27 sequencev1,445aa; PF01931\
    \ matches260-376. Gene depletion cannot identify the\n    active domain or catalytic\
    \ residues.\n  taxon: NCBITaxon:9606\n  scope_status: PHENOTYPIC\n  limitations:\
    \ Fraction of Golgi-positive cells is a trafficking readout, not direct cargo\
    \ binding or\n    proof of a specific COPII reaction. Not equivalent to2025 steady-state\
    \ EGFR localization.\n  nodes:\n  - node_id: knockdown\n    label: PRRC1 knockdown\
    \ during synchronized reporter release\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q96M27\n  - node_id: egfr\n    label: Cells with Golgi-localized\
    \ EGFR reporter\n    node_type: PHENOTYPE\n  - node_id: shhn\n    label: Cells\
    \ with Golgi-localized ShhN reporter\n    node_type: PHENOTYPE\n  edges:\n  -\
    \ edge_id: egfr-delay\n    subject: knockdown\n    predicate: decreases\n    object:\
    \ egfr\n    mechanism: Knockdown reduces the fraction reaching the scored Golgi-positive\
    \ EGFR state at matched\n      post-release times.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:34433667\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8536394/\n\
    \      snippet: knockdown\n      explanation: Figure5U-V and RUSH Methods; control\
    \ siRNA and time-zero included.\n      cache_path: evidence/PF01931/huang-2021.txt\n\
    \      cache_sha256: 926a457831cb58656e252438e3c957427d5c955430f2881127130b8b58f96da2\n\
    \  - edge_id: shhn-delay\n    subject: knockdown\n    predicate: decreases\n \
    \   object: shhn\n    mechanism: Knockdown reduces Golgi-positive ShhN reporter\
    \ cells at the assayed post-release times.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:34433667\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8536394/\n      snippet:\
    \ knockdown\n      explanation: Figure5W-X, separate soluble reporter assay; not\
    \ inferred from the EGFR result.\n      cache_path: evidence/PF01931/huang-2021.txt\n\
    \      cache_sha256: 926a457831cb58656e252438e3c957427d5c955430f2881127130b8b58f96da2\n\
    - graph_id: prrc1-atrap-localization-2025\n  title: PRRC1 knockout increases Golgi-associated\
    \ ATRAP signal\n  scope: Peng2025 Figure7C-F, WT versus PRRC1 knockout HeLa cells.\n\
    \  context: Steady-state ATRAP localization, Golgi/total above-threshold fluorescence;30-51cells\
    \ per group\n    per replicate.\n  family_mapping: Human Q96M27 sequencev1,445aa;\
    \ PF01931 matches260-376. Immunoblot-validated whole-gene\n    knockout; exact\
    \ clone sequence not verified.\n  taxon: NCBITaxon:9606\n  scope_status: PHENOTYPIC\n\
    \  limitations: Increased Golgi fraction supports a localization defect, not a\
    \ direct export rate or AP4-dependent\n    biochemical step. Steady-state EGFR\
    \ surface localization is a condition-specific negative comparator.\n  nodes:\n\
    \  - node_id: knockout\n    label: PRRC1 knockout in HeLa\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q96M27\n  - node_id: golgi\n    label: Golgi\
    \ fraction of ATRAP fluorescence\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ retention\n    subject: knockout\n    predicate: increases\n    object: golgi\n\
    \    mechanism: Knockout shifts the ATRAP readout toward the Golgi region relative\
    \ to WT cells.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:41032520\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC12519218/\n      snippet: PRRC1 KO\n\
    \      explanation: Figure7C-E, with EGFR comparatorF; no ATRAP rescue inferred\
    \ from mislabeled panelI.\n      cache_path: evidence/PF01931/peng-2025.txt\n\
    \      cache_sha256: af7e652b91d8ac0e2dc063f6429299ccbe7855bf07cd972ddaaedbd152937fe0\n\
    - graph_id: prrc1-atg9a-localization-2025\n  title: PRRC1 knockout and re-expression\
    \ alter ATG9A localization\n  scope: Peng2025 Figure7H-I, WT,PRRC1 knockout and\
    \ knockout plus PRRC1-HA HeLa cells.\n  context: ATG9A/TGN46/Climp-63 imaging;30-56cells\
    \ per group per replicate. Rescue compared with knockout\n    background.\n  family_mapping:\
    \ Human Q96M27 sequencev1,445aa; PF01931 matches260-376. Whole-protein rescue;\
    \ exact isoform\n    and construct sequence remain unverified.\n  taxon: NCBITaxon:9606\n\
    \  scope_status: PHENOTYPIC\n  limitations: PanelI y-axis says ATRAP but images,\
    \ legend and Results identify ATG9A. Retain discrepancy.\n    ER colocalization\
    \ and rescue do not identify isolated-domain sufficiency or direct cargo binding.\n\
    \  nodes:\n  - node_id: knockout\n    label: PRRC1 knockout versus WT\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:Q96M27\n  - node_id: rescue\n\
    \    label: PRRC1-HA expression in knockout cells\n    node_type: PERTURBATION\n\
    \  - node_id: golgi\n    label: Golgi fraction of ATG9A fluorescence\n    node_type:\
    \ PHENOTYPE\n  edges:\n  - edge_id: loss\n    subject: knockout\n    predicate:\
    \ decreases\n    object: golgi\n    mechanism: Knockout reduces the ATG9A Golgi\
    \ fraction, with increased ER-marker colocalization in the\n      companion images.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:41032520\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12519218/\n\
    \      snippet: PRRC1 KO\n      explanation: Figure7H-I and Results; ATG9A interpretation\
    \ explicitly qualified by panelI label conflict.\n      cache_path: evidence/PF01931/peng-2025.txt\n\
    \      cache_sha256: af7e652b91d8ac0e2dc063f6429299ccbe7855bf07cd972ddaaedbd152937fe0\n\
    \  - edge_id: rescue\n    subject: rescue\n    predicate: increases\n    object:\
    \ golgi\n    mechanism: PRRC1-HA re-expression restores the ATG9A localization\
    \ readout relative to knockout cells\n      without assigning an elementary molecular\
    \ mechanism.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:41032520\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC12519218/\n      snippet: PRRC1 KO\n\
    \      explanation: Figure7H rescue images and panelI rescue group, read with\
    \ caption and text rather than\n        mislabeled y-axis alone.\n      cache_path:\
    \ evidence/PF01931/peng-2025.txt\n      cache_sha256: af7e652b91d8ac0e2dc063f6429299ccbe7855bf07cd972ddaaedbd152937fe0\n\
    - graph_id: prrc1-vesicle-fraction-2025\n  title: Added GST-PRRC1 increases three\
    \ cargo signals in vesicle fractions\n  scope: Peng2025 Figure7J-K, semi-intact-cell\
    \ vesicle formation with purified GST-PRRC1 and rat liver\n    cytosol.\n  context:\
    \ Compare0 versus0.01mg/ml GST-PRRC1 at0.4mg/ml rat liver cytosol,n3. Separate2mg/ml\
    \ cytosol\n    lanes are not pooled into this claim.\n  family_mapping: Human\
    \ PRRC1 gene anchor Q96M27 sequencev1,445aa,PF01931 matches260-376; exact recombinant\n\
    \    clone sequence and purification details are supplement-dependent and unverified.\n\
    \  taxon: NCBITaxon:9606\n  scope_status: PHENOTYPIC\n  limitations: Multicomponent\
    \ mixed-species assay measures recovered cargo, not isolated-domain chemistry\n\
    \    or direct cargo recognition. No GST-only lane is shown. Mechanistic intermediates\
    \ and exact semi-intact-cell\n    genotype remain unverified.\n  nodes:\n  - node_id:\
    \ addition\n    label: GST-PRRC1 addition to low-cytosol budding reaction\n  \
    \  node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q96M27\n  - node_id:\
    \ atg9a\n    label: ATG9A in the recovered vesicle fraction\n    node_type: PHENOTYPE\n\
    \  - node_id: ergic53\n    label: ERGIC53 in the recovered vesicle fraction\n\
    \    node_type: PHENOTYPE\n  - node_id: sec22b\n    label: SEC22B in the recovered\
    \ vesicle fraction\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: atg9a-packaging\n\
    \    subject: addition\n    predicate: increases\n    object: atg9a\n    mechanism:\
    \ The GST-PRRC1-supplemented reaction yields more vesicle-associated ATG9A signal\
    \ under limiting-cytosol\n      conditions.\n    directness: UNRESOLVED\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:41032520\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12519218/\n      snippet:\
    \ GST-PRRC1\n      explanation: Figure7J paired0.4mg/ml RLC lanes and K quantification;\
    \ Methods references supplement\n        for preparation.\n      cache_path: evidence/PF01931/peng-2025.txt\n\
    \      cache_sha256: af7e652b91d8ac0e2dc063f6429299ccbe7855bf07cd972ddaaedbd152937fe0\n\
    \  - edge_id: ergic53-packaging\n    subject: addition\n    predicate: increases\n\
    \    object: ergic53\n    mechanism: Added GST-PRRC1 increases recovered ERGIC53\
    \ signal in the matched low-cytosol reaction.\n    directness: UNRESOLVED\n  \
    \  support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:41032520\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12519218/\n\
    \      snippet: GST-PRRC1\n      explanation: Figure7J ERGIC53 blot and K quantification;\
    \ does not establish a direct PRRC1-ERGIC53\n        interaction.\n      cache_path:\
    \ evidence/PF01931/peng-2025.txt\n      cache_sha256: af7e652b91d8ac0e2dc063f6429299ccbe7855bf07cd972ddaaedbd152937fe0\n\
    \  - edge_id: sec22b-packaging\n    subject: addition\n    predicate: increases\n\
    \    object: sec22b\n    mechanism: Added GST-PRRC1 increases recovered SEC22B\
    \ signal in the low-cytosol assay.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:41032520\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12519218/\n      snippet:\
    \ GST-PRRC1\n      explanation: Figure7J SEC22B blot and K quantification, separated\
    \ from high-cytosol lanes.\n      cache_path: evidence/PF01931/peng-2025.txt\n\
    \      cache_sha256: af7e652b91d8ac0e2dc063f6429299ccbe7855bf07cd972ddaaedbd152937fe0\n\
    - graph_id: prrc1-starvation-puncta-2025\n  title: PRRC1 knockout reduces starvation-associated\
    \ LC3 puncta\n  scope: Peng2025 Figure7L-N, WT versus PRRC1 knockout HeLa cells.\n\
    \  context: 60min EBSS starvation; ImageJ particle size and number,30-38cells\
    \ per group per replicate;\n    non-starved images also shown.\n  family_mapping:\
    \ Human Q96M27 sequencev1,445aa; PF01931 matches260-376. Whole-gene knockout,\
    \ not domain-selective\n    mutation.\n  taxon: NCBITaxon:9606\n  scope_status:\
    \ PHENOTYPIC\n  limitations: LC3 morphology is not autophagic flux. No demonstrated\
    \ mediation through ATG9A, direct\n    PRRC1-to-LC3 mechanism or separate LC3\
    \ rescue is established by these panels.\n  nodes:\n  - node_id: knockout\n  \
    \  label: PRRC1 knockout under60min EBSS starvation\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q96M27\n  - node_id: size\n    label: Mean LC3\
    \ punctum size\n    node_type: PHENOTYPE\n  - node_id: number\n    label: LC3\
    \ puncta per cell\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: punctum-size\n\
    \    subject: knockout\n    predicate: decreases\n    object: size\n    mechanism:\
    \ Knockout cells display smaller scored LC3 puncta thanWT after starvation.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:41032520\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12519218/\n\
    \      snippet: PRRC1 KO\n      explanation: Figure7L images and M size quantification;\
    \ morphology only.\n      cache_path: evidence/PF01931/peng-2025.txt\n      cache_sha256:\
    \ af7e652b91d8ac0e2dc063f6429299ccbe7855bf07cd972ddaaedbd152937fe0\n  - edge_id:\
    \ punctum-number\n    subject: knockout\n    predicate: decreases\n    object:\
    \ number\n    mechanism: Knockout cells have fewer scored LC3 puncta per cell\
    \ in the starvation condition.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:41032520\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12519218/\n      snippet:\
    \ PRRC1 KO\n      explanation: Figure7L and N; no unobserved ATG9A-to-autophagy\
    \ chain added.\n      cache_path: evidence/PF01931/peng-2025.txt\n      cache_sha256:\
    \ af7e652b91d8ac0e2dc063f6429299ccbe7855bf07cd972ddaaedbd152937fe0\ncuration_events:\n\
    - timestamp: '2026-10-12T03:16:56Z'\n  curator: Codex\n  action: CREATE\n  outcome:\
    \ needs_followup\n  summary: Curate YjjX biochemical and human PRRC1 trafficking\
    \ contexts for PF01931\n  history_record: history/records/PF01931/2026-10-12T031656Z-codex-007f82.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Frozen DUF84/NTPase_I-T/IPR026533 identity is preserved. P39411v2 is170aa
    with current match4-168; deposited1U5W is184aa with MLI prefix and SGRVEHHHHHH
    suffix, while the thesis primer suggests MLLI. Do not transfer structural numbering
    without alignment. Human Q96M27v1 is445aa with current match260-376, not historical264-355.
    Human gene depletion/rescue and recombinant assays do not verify every clone sequence
    or isolated-domain sufficiency. Rat cytosol is a distinct mixed-species component.
    First100 UniProt matches are an incomplete member sample.
  target_ids:
  - PF01931
  evidence_ids:
  - identity
  - primary
  - human-knockdown
  - human-knockout-and-reconstitution
  - source-coverage
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: YjjX phosphate release and separate inhibitor-dose curves are biochemical
    observations, not product-specific chemistry, competitive-binding proof or native
    RNA sanitization. PRRC1 knockdown effects on coat fluorescence and synchronized
    EGFR/ShhN transport remain indirect. Peng2025 ATRAP Golgi enrichment differs from
    ATG9A ER retention/rescue; panelI mislabels its axis and is interpreted with images,
    legend and Results. GST-PRRC1 addition changes vesicle-fraction cargo signals
    in a multicomponent assay with no shown GST-only lane; directness remains unresolved.
    LC3 size/count effects are morphology, not autophagic flux or demonstrated mediation
    by ATG9A. Co-IP and negative lipid-free Sar1 pulldown do not become direct binding
    or activation edges.
  target_ids:
  - PF01931
  evidence_ids:
  - primary
  - native
  - human-knockdown
  - human-knockout-and-reconstitution
  - source-coverage
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: YjjX source discrepancies, N-terminal extension and quantitative kinetics
    need follow-up. PNAS supplementary clone, guide, siRNA, isoform and purification
    details remain inaccessible. Zebrafish Mys development and PKA studies, Liu2025
    domain-specific COPII thesis, Lawhorn thiamine-antimetabolite screen, VC0702/1U14
    and Thermoplasma fusions remain open primary contexts. No all-member characterization
    or family-wide negative is claimed.
  target_ids:
  - PF01931
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01931-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve source and construct limits and extend domain-specific and member
    coverage
  description: Verify YjjX construct numbering and conflicting substrate/metal/Km
    text; obtain PNAS supplementary methods and clarify panel7I labeling. Inspect
    accession-mapped Mys/PKA developmental studies and PRRC1 domain-specific thesis
    before adding their mechanisms. Extend Lawhorn,VC0702,Salmonella and fusion-member
    coverage with primary controls. Retain scoped effects and IN_PROGRESS until justified
    full-scope successor evidence exists.
  target_ids:
  - PF01931
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - human-knockdown
  - human-knockout-and-reconstitution
  - source-coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01931.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Verify YjjX construct numbering and conflicting substrate/metal/Km
    text; obtain PNAS supplementary methods and clarify panel7I labeling. Inspect
    accession-mapped Mys/PKA developmental studies and PRRC1 domain-specific thesis
    before adding their mechanisms. Extend Lawhorn,VC0702,Salmonella and fusion-member
    coverage with primary controls. Retain scoped effects and IN_PROGRESS until justified
    full-scope successor evidence exists.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01931
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- YjjX Tables4.2/4.3 and Figure4.5, Huang Figure5 and Peng Figure7 visually inspected;
  corresponding primary Results and Methods read. YjjX source was author's explicit
  republication, not independent replication. PNAS supplements and Liu thesis full
  text unavailable. No raw-data reanalysis, clone resequencing, independent expert
  review or exhaustive member survey. Browser and corpus verification are recorded
  separately after retention.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
