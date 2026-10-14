# PF01950: Thermococcus hydrolysis and conditional cellular effects

- Review: 20261012T083350Z-pf01950-thermococcus-hydrolysis-and-conditional-effects
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-12T08:30:56Z
- Finished UTC: 2026-10-12T08:33:50Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Five graphs retain eight OBSERVED experimental effects, one DIRECT chemical-product edge and seven UNRESOLVED cellular effects. One graph is MECHANISTIC and four are PHENOTYPIC. Six evidence ledgers and three OPEN discussions retain exact conditions and follow-ups. This partial same-agent scientific review remains NEEDS_FOLLOWUP and the family IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Ascending uncurated family after PF01949; all 8296 records and earlier follow-ups remain in scope.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01950 | data/families/PF01950.yaml | generated | PF01950 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01950 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01950.

Frozen FBPase_3/former DUF100, IPR002803, EX_DUF and UNSCORED are unchanged. KOD1 Q8NKR9 v1 is 375 aa, PF01950 6-372, linked to historical AB081839.1/BAC10571.1 and genomic TK2164/BAD86353.1. ENA CDS/translation and current identity were inspected; historical recombinant or engineered-cell clones were not independently resequenced. KW128, delta-fbp-8J and delta-imp-2A are explicit engineered backgrounds. ST0318 3R1M residues2-385 exactly match F9VMT6 v1 residues1-384; paper Lys232/Tyr229 map to current Lys231/Tyr228. No class-IV Imp or human/class-I FBPase transfer.

### Directed effects and limits

graph: supported. Targets: PF01950.

Purified-protein F6P production is separate from conditional whole-gene effects. Synthetic-medium growth with and without pyruvate is distinguished from rich-medium cell-extract assays. The amino-acid-only outcome is reported without a plotted curve. Carbon-regimen substitution has separate transcript and activity outputs in each strain; RNA and extracts were sampled at different phases and no RNA-to-activity mediation edge is asserted. Northern signal is RNA abundance, not directly measured initiation. Native Imp non-compensation is not engineered complementation. Later bifunctionality prevents attributing the deletion phenotype solely to phosphatase activity. Negative and association-only results remain outside the graph.

### Remaining family coverage

completeness: concern. Targets: PF01950.

The record does not yet retain the full bifunctional aldolase/phosphatase mechanism. Full Rashid2002/Nishimasu2004, main Say2010/Fushinobu2011/Du2011 experiments and additional members remain to be inspected. Public supplements provide concrete follow-up leads and a verified ST0318 coordinate offset, not full method/construct validation. Exact historical preparations, selective-activity rescue, polarity, carbon regulator, RNA stability, protein abundance, direct cellular flux and isolated-domain function remain unresolved. Filtered reviewed annotations are not a membership or experimental census.

## Findings

### additional-contexts: Extend the bifunctional mechanism and resolve conditional cellular causation

minor / open / confirmed; issue key: pf01950-causal-context-coverage.

Inspect complete primary assays and construct-specific sequences for the later aldolase/phosphatase work, keeping paper versus UniProt coordinates explicit. Verify older Fbp assay buffer/metal/purification details without borrowing the IMPase protocol. Assess selective-activity mutants with folding and rescue controls before attributing the whole-gene growth phenotype to a single reaction. Separate synthetic from rich medium and exponential RNA from stationary extract activity. Extend member-specific primary coverage and retain a successor review; do not promote this scoped pass to REVIEWED.

## Recommended Actions And Acceptance Checks

### extend-contexts

Inspect complete primary assays and construct-specific sequences for the later aldolase/phosphatase work, keeping paper versus UniProt coordinates explicit. Verify older Fbp assay buffer/metal/purification details without borrowing the IMPase protocol. Assess selective-activity mutants with folding and rescue controls before attributing the whole-gene growth phenotype to a single reaction. Separate synthetic from rich medium and exponential RNA from stationary extract activity. Extend member-specific primary coverage and retain a successor review; do not promote this scoped pass to REVIEWED.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC516828/; Sato2004 recombinant-enzyme and assay Methods, first Results subsection and Table2 with footnotes. | supports | Purified KOD1 Fbp produces F6P from FBP at 85 C in a corrected coupled assay; the 95 C kinetic constants are a separate earlier experiment. Whole-protein chemistry is not domain-only or residue-specific causation. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01950/protein/uniprot/Q8NKR9/; Accession and domain locations; paired UniProt identity facts | supports | Frozen FBPase_3/former DUF100, IPR002803, EX_DUF and UNSCORED are unchanged. KOD1 Q8NKR9 v1 is 375 aa, PF01950 6-372, linked to historical AB081839.1/BAC10571.1 and genomic TK2164/BAD86353.1. ENA CDS/translation and current identity were inspected; historical recombinant or engineered-cell clones were not independently resequenced. KW128, delta-fbp-8J and delta-imp-2A are explicit engineered backgrounds. ST0318 3R1M residues2-385 exactly match F9VMT6 v1 residues1-384; paper Lys232/Tyr229 map to current Lys231/Tyr228. No class-IV Imp or human/class-I FBPase transfer. |
| knockout-contexts | https://pmc.ncbi.nlm.nih.gov/articles/PMC516828/; Disruption, growth and cell-extract Methods/Results; Table1 and Figures1-3, with Figures2/3 visually inspected. | supports | Whole-CDS replacement produces conditional OD and rich-medium extract effects; deletion validation, positive starch growth and absent fbp rescue bound the inference. |
| carbon-contexts | https://pmc.ncbi.nlm.nih.gov/articles/PMC516828/; Cell-extract/hybridization Methods and Results; Figure4B visually inspected. | supports | Starch-versus-pyruvate substitution decreases transcript signal and extract activity separately in KW128 and delta-imp-2A; no direct inhibition or demonstrated transcript-mediated mechanism. |
| dual-function-followup | https://www.nature.com/articles/nature10457; Public abstract/accessions; supplement S1-S8, including reaction kinetics S2 and adduct/structural comparisons S3/S5-S7. | supports | Primary later bifunctionality evidence is not dismissed; exact main assay methods and member-specific transfer remain to review. Static structures do not supply an observed conformational trajectory. |
| source-coverage | evidence/PF01950/coverage.txt; Search scope, acquisition outcomes and named remaining primary sources. | supports | Public PMC HTML and two Nature supplements were obtained; full main Nature articles and other primary methods remain unreviewed. All records and earlier follow-ups remain in scope. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01950 | data/families/PF01950.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Sato2004 full public HTML Methods/Results/Discussion and Tables1/2 read; Figures2/3/4 visually inspected. Fushinobu2011 complete supplement text inspected but not a visual/Methods review; Say2010 supplement partially inspected, not a complete quantitative or visual pass. Main Nature articles are subscription restricted. No raw data reanalysis, clone sequencing, experimental replication or independent expert endorsement.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T083350Z-pf01950-thermococcus-hydrolysis-and-conditional-effects
title: 'PF01950: Thermococcus hydrolysis and conditional cellular effects'
started_at: '2026-10-12T08:30:56Z'
finished_at: '2026-10-12T08:33:50Z'
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
summary: Five graphs retain eight OBSERVED experimental effects, one DIRECT chemical-product
  edge and seven UNRESOLVED cellular effects. One graph is MECHANISTIC and four are
  PHENOTYPIC. Six evidence ledgers and three OPEN discussions retain exact conditions
  and follow-ups. This partial same-agent scientific review remains NEEDS_FOLLOWUP
  and the family IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01950.yaml
    sha256: ec541c4ab57a9e14db3c07d3bea0de372cfbc2801e6ca41143c7959827f7474c
    role: context
  - path: data/families/PF01950.yaml
    sha256: 86e0e9425310464e557accfaa5b1eb770db20e20cb42f0e96602eb358b9bdab4
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
  - path: evidence/PF01950/sato-2004-biochemistry.txt
    role: context
    sha256: 92dd51159f203bb71a87d5732105de6eea4ef9f202afd618afe1a9be5fb9b770
  - path: evidence/PF01950/identity.txt
    role: context
    sha256: 040aea3704d69160f7dfe717dde3b09815f4bbe980379f8f30fa23d6d1dcdc7c
  - path: evidence/PF01950/sato-2004-genetics.txt
    role: context
    sha256: e3ae36fb3efddb71d32ec281b61b9311662127ef60194bcfd616dd3acf6715b7
  - path: evidence/PF01950/sato-2004-carbon-response.txt
    role: context
    sha256: 68616fcd5fa2fd30a3af366cfaeddba886d43bdfb572c891ce98e56696874477
  - path: evidence/PF01950/bifunctionality-followup.txt
    role: context
    sha256: 57d42d1372f932b949e8ed294620fbd8eb3da07b8cac090133eee1af2abb0936
  - path: evidence/PF01950/coverage.txt
    role: context
    sha256: 2bd2a11f4f871ecf4c54be16d776d9be260c711650c681e0a661813a6bceea84
targets:
- target_id: PF01950
  path: data/families/PF01950.yaml
  label: PF01950
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01950.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 6029671d96f8a16ce2d1bda2ba8c9aca2ad0e3720b47c169335290c39f8ff1fa
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Ascending uncurated family after PF01949; all 8296 records and earlier
    follow-ups remain in scope.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01950
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: The record does not yet retain the full bifunctional aldolase/phosphatase
      mechanism. Full Rashid2002/Nishimasu2004, main Say2010/Fushinobu2011/Du2011
      experiments and additional members remain to be inspected. Public supplements
      provide concrete follow-up leads and a verified ST0318 coordinate offset, not
      full method/construct validation. Exact historical preparations, selective-activity
      rescue, polarity, carbon regulator, RNA stability, protein abundance, direct
      cellular flux and isolated-domain function remain unresolved. Filtered reviewed
      annotations are not a membership or experimental census.
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
  - PF01950
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC516828/
  locator: Sato2004 recombinant-enzyme and assay Methods, first Results subsection
    and Table2 with footnotes.
  accessed_at: '2026-10-12T08:33:50Z'
  support: supports
  snapshot_sha256: 92dd51159f203bb71a87d5732105de6eea4ef9f202afd618afe1a9be5fb9b770
  summary: Purified KOD1 Fbp produces F6P from FBP at 85 C in a corrected coupled
    assay; the 95 C kinetic constants are a separate earlier experiment. Whole-protein
    chemistry is not domain-only or residue-specific causation.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01950/protein/uniprot/Q8NKR9/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-12T08:33:50Z'
  support: supports
  snapshot_sha256: 040aea3704d69160f7dfe717dde3b09815f4bbe980379f8f30fa23d6d1dcdc7c
  summary: Frozen FBPase_3/former DUF100, IPR002803, EX_DUF and UNSCORED are unchanged.
    KOD1 Q8NKR9 v1 is 375 aa, PF01950 6-372, linked to historical AB081839.1/BAC10571.1
    and genomic TK2164/BAD86353.1. ENA CDS/translation and current identity were inspected;
    historical recombinant or engineered-cell clones were not independently resequenced.
    KW128, delta-fbp-8J and delta-imp-2A are explicit engineered backgrounds. ST0318
    3R1M residues2-385 exactly match F9VMT6 v1 residues1-384; paper Lys232/Tyr229
    map to current Lys231/Tyr228. No class-IV Imp or human/class-I FBPase transfer.
- evidence_id: knockout-contexts
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC516828/
  locator: Disruption, growth and cell-extract Methods/Results; Table1 and Figures1-3,
    with Figures2/3 visually inspected.
  summary: Whole-CDS replacement produces conditional OD and rich-medium extract effects;
    deletion validation, positive starch growth and absent fbp rescue bound the inference.
  accessed_at: '2026-10-12T08:33:50Z'
  support: supports
  snapshot_sha256: e3ae36fb3efddb71d32ec281b61b9311662127ef60194bcfd616dd3acf6715b7
- evidence_id: carbon-contexts
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC516828/
  locator: Cell-extract/hybridization Methods and Results; Figure4B visually inspected.
  summary: Starch-versus-pyruvate substitution decreases transcript signal and extract
    activity separately in KW128 and delta-imp-2A; no direct inhibition or demonstrated
    transcript-mediated mechanism.
  accessed_at: '2026-10-12T08:33:50Z'
  support: supports
  snapshot_sha256: 68616fcd5fa2fd30a3af366cfaeddba886d43bdfb572c891ce98e56696874477
- evidence_id: dual-function-followup
  kind: primary_source
  reference: https://www.nature.com/articles/nature10457
  locator: Public abstract/accessions; supplement S1-S8, including reaction kinetics
    S2 and adduct/structural comparisons S3/S5-S7.
  summary: Primary later bifunctionality evidence is not dismissed; exact main assay
    methods and member-specific transfer remain to review. Static structures do not
    supply an observed conformational trajectory.
  accessed_at: '2026-10-12T08:33:50Z'
  support: supports
  snapshot_sha256: 57d42d1372f932b949e8ed294620fbd8eb3da07b8cac090133eee1af2abb0936
- evidence_id: source-coverage
  kind: search
  reference: evidence/PF01950/coverage.txt
  locator: Search scope, acquisition outcomes and named remaining primary sources.
  search_scope: PF01950, FBPase_3, DUF100, exact paper titles and DOI/accession leads;
    pre-edit authoring/evidence/history/structured-review paths included ignored and
    hidden files.
  summary: Public PMC HTML and two Nature supplements were obtained; full main Nature
    articles and other primary methods remain unreviewed. All records and earlier
    follow-ups remain in scope.
  accessed_at: '2026-10-12T08:33:50Z'
  support: supports
  snapshot_sha256: 2bd2a11f4f871ecf4c54be16d776d9be260c711650c681e0a661813a6bceea84
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-12T08:33:50Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01950
  kind: record_content
  reference: data/families/PF01950.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-12T08:33:50Z'
  support: context_only
  snapshot_sha256: 86e0e9425310464e557accfaa5b1eb770db20e20cb42f0e96602eb358b9bdab4
  quote: "id: Pfam:PF01950\npfam_id: PF01950\nname: Fructose-1,6-bisphosphatase\n\
    short_name: FBPase_3\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01950\n\
    counters:\n  proteins: 507\n  matches: 518\n  proteomes: 487\n  taxa: 1110\n \
    \ structures: 8\n  alphafold_models: 440\n  domain_architectures: 2\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002803\ndescription: This is a family of bacterial and\
    \ archaeal fructose-1,6-bisphosphatases (FBPases). FBPase\n  catalyses the hydrolysis\
    \ of D-fructose-1,6-bisphosphate (FBP) to D-fructose-6-phosphate (F6P) and orthophosphate\n\
    \  and is an essential regulatory enzyme in the glyconeogenic pathway.\ncuration_history:\
    \ history/records/PF01950\ndiscussions:\n- discussion_id: pf01950-bifunctional-mechanism\n\
    \  prompt: Complete member-specific aldolase/phosphatase and residue-level evidence\
    \ before extending the\n    chemical graph.\n  kind: CURATION_TODO\n  status:\
    \ OPEN\n  rationale: The retained Thermococcus hydrolysis experiment does not\
    \ describe the later-discovered dual\n    reaction or prove a family-wide mechanism.\n\
    \  evidence:\n  - reference: PMID:21983966\n    supports: PARTIAL\n    evidence_source:\
    \ primary_publication\n    explanation: Public abstract and supplementary S2-S8\
    \ inspected; main Methods and mutant experiments\n      remain unreviewed. Static\
    \ structures are not an observed switching trajectory.\n  - reference: PMID:20348906\n\
    \    supports: PARTIAL\n    evidence_source: primary_publication\n    explanation:\
    \ Abstract and selected supplement sections inspected; assay identities, conditions\
    \ and\n      controls need full review.\n  posed_by: Codex\n  posed_date: '2026-10-12'\n\
    \  notes: ST0318 PDB3R1M has one extra initial methionine versus F9VMT6 v1; paper\
    \ Lys232/Tyr229 map to\n    UniProt Lys231/Tyr228. Verify each construct separately.\
    \ See evidence/PF01950/bifunctionality-followup.txt.\n- discussion_id: pf01950-cellular-causation\n\
    \  prompt: Resolve which Fbp activity supports the conditional growth phenotype\
    \ and identify the carbon-response\n    mechanism.\n  kind: CURATION_TODO\n  status:\
    \ OPEN\n  rationale: Whole-gene deletion removes both potential activities; rich-medium\
    \ extracts and synthetic-medium\n    growth were measured in different experiments.\n\
    \  evidence:\n  - reference: PMID:15317785\n    supports: PARTIAL\n    evidence_source:\
    \ primary_publication\n    explanation: Deletion validation, growth, extract activity\
    \ and Northern experiments inspected. No\n      fbp reintroduction or selective-activity\
    \ rescue was found in the full paper.\n  posed_by: Codex\n  posed_date: '2026-10-12'\n\
    \  notes: Monocistronic RNA reduces but does not exhaustively exclude polarity.\
    \ Test selective catalytic\n    mutants with protein/folding controls and rescue;\
    \ separate RNA abundance from initiation rate and\n    direct inhibition from\
    \ carbon-regimen responses.\n- discussion_id: pf01950-remaining-evidence\n  prompt:\
    \ Extend primary coverage beyond the scoped KOD1-derived experiments.\n  kind:\
    \ CURATION_TODO\n  status: OPEN\n  rationale: A Pfam rename, reviewed database\
    \ annotation and homolog alignment are not experiments on\n    every family member.\n\
    \  evidence:\n  - reference: PMID:12065581\n    supports: PARTIAL\n    evidence_source:\
    \ primary_publication\n    explanation: Earlier Fbp assay referenced by Sato2004;\
    \ exact buffer, metal concentration and historical\n      recombinant construct\
    \ remain to be independently checked.\n  - reference: PMID:15274916\n    supports:\
    \ PARTIAL\n    evidence_source: database\n    explanation: Imported family citation\
    \ and UniProt mutant annotations are leads; full structural paper\n      was not\
    \ inspected.\n  posed_by: Codex\n  posed_date: '2026-10-12'\n  notes: Inspect\
    \ Du2011, the Thermococcus onnurineus study, other tested members and subsequent\
    \ literature.\n    Keep computational mechanisms distinct. See evidence/PF01950/coverage.txt;\
    \ all records and earlier\n    follow-ups remain in scope.\ncausal_graphs:\n-\
    \ graph_id: tk-fbp-hydrolysis-2004\n  title: Purified Thermococcus Fbp converts\
    \ FBP to F6P\n  scope: Whole-protein Fbp from Thermococcus kodakarensis KOD1,\
    \ expressed in E. coli.\n  context: Sato2004 Table2; purified preparation with\
    \ 2 mM FBP at 85 C; F6P detected by coupled glucose-6-phosphate\n    isomerase/dehydrogenase\
    \ assay. FBP-minus and thermal-decomposition corrections were applied.\n  family_mapping:\
    \ Q8NKR9 v1, 375 aa, fbp/TK2164; historical AB081839.1/BAC10571.1 and genome BAD86353.1;\n\
    \    PF01950 residues 6-372. Historical recombinant clone was not independently\
    \ resequenced.\n  taxon: NCBITaxon:69014\n  scope_status: MECHANISTIC\n  limitations:\
    \ Whole protein, not isolated-domain catalysis. Exact assay buffer and metal concentration\n\
    \    refer to uninspected Rashid2002 methods. The 95 C kinetic constants are not\
    \ the 85 C activity endpoint.\n    No aldolase, residue chemistry or universal\
    \ family activity is inferred from this experiment.\n  nodes:\n  - node_id: reaction\n\
    \    label: Purified KOD1 Fbp with FBP under assay conditions\n    node_type:\
    \ ACTIVITY\n    grounding:\n    - UniProtKB:Q8NKR9\n  - node_id: f6p\n    label:\
    \ F6P product detected by coupled assay\n    node_type: STATE\n  edges:\n  - edge_id:\
    \ tk-fbp-f6p\n    subject: reaction\n    predicate: produces\n    object: f6p\n\
    \    mechanism: The purified whole-protein preparation hydrolyzes FBP at its 1-phosphate\
    \ position; the\n      coupled F6P readout gives 18.9 +/- 0.7 U/mg at 85 C.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:15317785\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC516828/\n\
    \      snippet: generate F6P\n      explanation: First Results subsection and\
    \ Table2/footnotes; three independent activity experiments\n        and FBP assay\
    \ controls. Product detection is coupled, not direct mass spectrometry.\n    \
    \  cache_path: evidence/PF01950/sato-2004-biochemistry.txt\n      cache_sha256:\
    \ 92dd51159f203bb71a87d5732105de6eea4ef9f202afd618afe1a9be5fb9b770\n- graph_id:\
    \ kw128-fbp-deletion-growth-2004\n  title: Fbp deletion reduces growth in defined\
    \ gluconeogenic media\n  scope: KOD1-derived KW128 compared with delta-fbp-8J,\
    \ not wild-type KOD1 versus a domain mutant.\n  context: Anaerobic 85 C; rich-medium\
    \ preculture followed by synthetic ASW-AA with 20 amino acids and\n    sulfur,\
    \ with or without 5 g/L sodium pyruvate. Starch supplementation is a separate\
    \ positive growth\n    condition.\n  family_mapping: Entire 1128-bp fbp/TK2164\
    \ CDS replaced with trpE; PCR, sequencing and Southern validation\n    reported.\
    \ Reference Q8NKR9 v1, PF01950 6-372; KW128 is delta-pyrF delta-trpE::pyrF.\n\
    \  taxon: NCBITaxon:69014\n  scope_status: PHENOTYPIC\n  limitations: OD660 is\
    \ not viability. Amino-acid-only growth result is reported without its curve.\
    \ No\n    fbp reintroduction rescue; the monocistronic transcript does not exhaustively\
    \ exclude polarity. Loss\n    of a bifunctional protein does not identify which\
    \ activity limits growth or demonstrate universal\n    essentiality.\n  nodes:\n\
    \  - node_id: deletion\n    label: Delta-fbp-8J whole-gene replacement versus\
    \ KW128\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q8NKR9\n\
    \  - node_id: pyruvate_growth\n    label: OD660 growth in ASW-AA plus pyruvate\n\
    \    node_type: PHENOTYPE\n  - node_id: amino_acid_growth\n    label: Growth in\
    \ ASW-AA without added pyruvate\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ deletion-pyruvate-growth\n    subject: deletion\n    predicate: decreases\n\
    \    object: pyruvate_growth\n    mechanism: The deletion strain lacks the OD\
    \ increase seen in KW128 and delta-imp-2A under the matched\n      pyruvate condition;\
    \ the missing intracellular reaction is not selectively tested.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:15317785\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC516828/\n\
    \      snippet: was not able to grow\n      explanation: Growth Methods/Results,\
    \ Table1 and visually inspected Figure3; starch-supported growth\n        limits\
    \ the essentiality claim.\n      cache_path: evidence/PF01950/sato-2004-genetics.txt\n\
    \      cache_sha256: e3ae36fb3efddb71d32ec281b61b9311662127ef60194bcfd616dd3acf6715b7\n\
    \  - edge_id: deletion-amino-acid-growth\n    subject: deletion\n    predicate:\
    \ decreases\n    object: amino_acid_growth\n    mechanism: The authors report\
    \ the same conditional growth defect when amino acids supply gluconeogenic\n \
    \     carbon without added pyruvate; this is not a separately plotted quantitative\
    \ effect.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:15317785\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC516828/\n      snippet: The same results\n\
    \      explanation: Growth Results explicitly extend the comparison to ASW-AA\
    \ without pyruvate; underlying\n        curve and numerical replication for that\
    \ condition are not shown.\n      cache_path: evidence/PF01950/sato-2004-genetics.txt\n\
    \      cache_sha256: e3ae36fb3efddb71d32ec281b61b9311662127ef60194bcfd616dd3acf6715b7\n\
    - graph_id: kw128-fbp-deletion-extract-2004\n  title: Fbp deletion reduces extract\
    \ FBPase activity\n  scope: Rich-medium KW128 versus delta-fbp-8J cell extracts.\n\
    \  context: ASW-YT plus 5 g/L sodium pyruvate, anaerobic 85 C for 15 h, early\
    \ stationary phase. FBPase\n    measured by the coupled F6P assay, not by in vivo\
    \ flux analysis.\n  family_mapping: The delta-fbp-8J entire-CDS replacement targets\
    \ fbp/TK2164; Q8NKR9 v1 maps PF01950 6-372.\n    Whole-gene effect in an engineered\
    \ KOD1-derived background.\n  taxon: NCBITaxon:69014\n  scope_status: PHENOTYPIC\n\
    \  limitations: Rich ASW-YT supports mutant growth; this is not the synthetic-medium\
    \ growth experiment.\n    No direct intracellular flux, individual aldolase contribution,\
    \ fbp rescue or domain-only perturbation\n    is established. Other activities\
    \ below assay detection are not proven absent.\n  nodes:\n  - node_id: deletion\n\
    \    label: Delta-fbp-8J versus KW128 in rich pyruvate medium\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:Q8NKR9\n  - node_id: activity\n\
    \    label: FBPase activity in early-stationary cell extracts\n    node_type:\
    \ ACTIVITY\n  edges:\n  - edge_id: deletion-extract-fbpase\n    subject: deletion\n\
    \    predicate: decreases\n    object: activity\n    mechanism: Extract activity\
    \ detected in KW128 is undetectable in delta-fbp-8J under matched rich-medium\n\
    \      conditions; no measured cellular intermediate links this result to the\
    \ separate growth assay.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:15317785\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC516828/\n      snippet:\
    \ activity could not be detected\n      explanation: 'Cell-extract Methods/Results:\
    \ KW128 0.37 +/- 0.02 U/mg, delta-imp-2A 0.34 +/- 0.01;\n        delta-fbp-8J\
    \ undetected. Assay detection context and rich-medium growth retained.'\n    \
    \  cache_path: evidence/PF01950/sato-2004-genetics.txt\n      cache_sha256: e3ae36fb3efddb71d32ec281b61b9311662127ef60194bcfd616dd3acf6715b7\n\
    - graph_id: kw128-carbon-regimen-2004\n  title: Carbon regimen changes Fbp transcript\
    \ and extract activity in KW128\n  scope: Starch-versus-pyruvate supplementation\
    \ within KW128 only.\n  context: Rich ASW-YT with 5 g/L starch versus 5 g/L sodium\
    \ pyruvate, anaerobic 85 C. RNA sampled early\n    exponential phase, 30 ug per\
    \ Northern lane; extract activity sampled after 15 h at early stationary\n   \
    \ phase.\n  family_mapping: Intact fbp/TK2164 in KOD1-derived KW128; Q8NKR9 v1\
    \ PF01950 6-372. The probe detects\n    the fbp transcript, not a distinct class-IV\
    \ imp transcript.\n  taxon: NCBITaxon:69014\n  scope_status: PHENOTYPIC\n  limitations:\
    \ Regimen substitution, not addition of starch to fixed pyruvate or direct enzyme\
    \ inhibition.\n    Northern signal measures RNA abundance rather than initiation\
    \ rate. Different sampling phases preclude\n    an observed RNA-to-activity edge;\
    \ carbon sensing, RNA stability and protein abundance are unresolved.\n  nodes:\n\
    \  - node_id: regimen\n    label: Starch instead of pyruvate supplementation in\
    \ KW128\n    node_type: PERTURBATION\n  - node_id: transcript\n    label: Fbp\
    \ Northern signal in early-exponential KW128\n    node_type: STATE\n    grounding:\n\
    \    - UniProtKB:Q8NKR9\n  - node_id: activity\n    label: FBPase activity in\
    \ early-stationary KW128 extract\n    node_type: ACTIVITY\n  edges:\n  - edge_id:\
    \ kw128-regimen-transcript\n    subject: regimen\n    predicate: decreases\n \
    \   object: transcript\n    mechanism: The fbp-probe signal is weaker under starch\
    \ supplementation; the regulator and contribution\n      of RNA turnover are not\
    \ measured.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:15317785\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC516828/\n      snippet: highly reduced\n\
    \      explanation: Figure4B KW128 P/S lanes visually inspected; equal RNA loading\
    \ and delta-fbp probe-negative\n        comparison, without a quantified fold\
    \ change.\n      cache_path: evidence/PF01950/sato-2004-carbon-response.txt\n\
    \      cache_sha256: 68616fcd5fa2fd30a3af366cfaeddba886d43bdfb572c891ce98e56696874477\n\
    \  - edge_id: kw128-regimen-activity\n    subject: regimen\n    predicate: decreases\n\
    \    object: activity\n    mechanism: Starch-grown KW128 extracts have activity\
    \ below 0.01 U/mg versus 0.37 +/- 0.02 U/mg after\n      pyruvate growth; this\
    \ does not demonstrate direct starch inhibition of purified Fbp.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:15317785\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC516828/\n\
    \      snippet: no detectable FBPase activity\n      explanation: Cell-extract\
    \ Results and paired carbon-regimen Methods; the strain-specific activity\n  \
    \      values support this edge independently of the Northern result.\n      cache_path:\
    \ evidence/PF01950/sato-2004-carbon-response.txt\n      cache_sha256: 68616fcd5fa2fd30a3af366cfaeddba886d43bdfb572c891ce98e56696874477\n\
    - graph_id: deltaimp-carbon-regimen-2004\n  title: Carbon regimen changes Fbp\
    \ transcript and extract activity in delta-imp-2A\n  scope: Starch-versus-pyruvate\
    \ supplementation within delta-imp-2A, not an effect of imp deletion.\n  context:\
    \ Rich ASW-YT with 5 g/L starch versus 5 g/L sodium pyruvate, anaerobic 85 C.\
    \ Early-exponential\n    RNA and 15 h early-stationary extracts were sampled separately.\n\
    \  family_mapping: Intact fbp/TK2164 (Q8NKR9 v1, PF01950 6-372) in the imp-disrupted\
    \ KOD1-derived strain.\n    The imp gene is a different family and not a second\
    \ PF01950 paralog.\n  taxon: NCBITaxon:69014\n  scope_status: PHENOTYPIC\n  limitations:\
    \ No direct carbon-binding or regulatory mechanism. Transcript and extract measurements\
    \ do\n    not form a demonstrated mediation chain. The imp and fbp blot panels\
    \ have different development times\n    and cannot quantify cross-gene abundance.\
    \ This graph does not infer a causal effect from the near-equal\n    KW128 and\
    \ delta-imp activities.\n  nodes:\n  - node_id: regimen\n    label: Starch instead\
    \ of pyruvate in delta-imp-2A\n    node_type: PERTURBATION\n  - node_id: transcript\n\
    \    label: Fbp Northern signal in early-exponential delta-imp-2A\n    node_type:\
    \ STATE\n    grounding:\n    - UniProtKB:Q8NKR9\n  - node_id: activity\n    label:\
    \ FBPase activity in early-stationary delta-imp-2A extract\n    node_type: ACTIVITY\n\
    \  edges:\n  - edge_id: deltaimp-regimen-transcript\n    subject: regimen\n  \
    \  predicate: decreases\n    object: transcript\n    mechanism: Figure4B shows\
    \ reduced fbp transcript signal under starch relative to pyruvate within delta-imp-2A;\n\
    \      the molecular carbon-response pathway remains unresolved.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:15317785\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC516828/\n\
    \      snippet: highly reduced\n      explanation: Figure4B delta-imp-2A P/S lanes\
    \ and transcription Results; no independent regulator\n        perturbation or\
    \ quantitative RNA fold change.\n      cache_path: evidence/PF01950/sato-2004-carbon-response.txt\n\
    \      cache_sha256: 68616fcd5fa2fd30a3af366cfaeddba886d43bdfb572c891ce98e56696874477\n\
    \  - edge_id: deltaimp-regimen-activity\n    subject: regimen\n    predicate:\
    \ decreases\n    object: activity\n    mechanism: Extract activity is undetectable\
    \ with starch rather than the 0.34 +/- 0.01 U/mg measured\n      after pyruvate\
    \ growth; direct enzyme inhibition is not established.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:15317785\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC516828/\n\
    \      snippet: no detectable FBPase activity\n      explanation: Cell-extract\
    \ Results specify undetectable activity in both disruptants with starch,\n   \
    \     versus the strain-specific pyruvate activity; this is separate from the\
    \ Northern observation.\n      cache_path: evidence/PF01950/sato-2004-carbon-response.txt\n\
    \      cache_sha256: 68616fcd5fa2fd30a3af366cfaeddba886d43bdfb572c891ce98e56696874477\n\
    curation_events:\n- timestamp: '2026-10-12T08:17:30Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: needs_followup\n  summary: Curate scoped PF01950 Thermococcus\
    \ hydrolysis and conditional cellular effects\n  history_record: history/records/PF01950/2026-10-12T081730Z-codex-0a2935.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Frozen FBPase_3/former DUF100, IPR002803, EX_DUF and UNSCORED are unchanged.
    KOD1 Q8NKR9 v1 is 375 aa, PF01950 6-372, linked to historical AB081839.1/BAC10571.1
    and genomic TK2164/BAD86353.1. ENA CDS/translation and current identity were inspected;
    historical recombinant or engineered-cell clones were not independently resequenced.
    KW128, delta-fbp-8J and delta-imp-2A are explicit engineered backgrounds. ST0318
    3R1M residues2-385 exactly match F9VMT6 v1 residues1-384; paper Lys232/Tyr229
    map to current Lys231/Tyr228. No class-IV Imp or human/class-I FBPase transfer.
  target_ids:
  - PF01950
  evidence_ids:
  - identity
  - primary
  - knockout-contexts
  - carbon-contexts
  - dual-function-followup
  - source-coverage
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Purified-protein F6P production is separate from conditional whole-gene
    effects. Synthetic-medium growth with and without pyruvate is distinguished from
    rich-medium cell-extract assays. The amino-acid-only outcome is reported without
    a plotted curve. Carbon-regimen substitution has separate transcript and activity
    outputs in each strain; RNA and extracts were sampled at different phases and
    no RNA-to-activity mediation edge is asserted. Northern signal is RNA abundance,
    not directly measured initiation. Native Imp non-compensation is not engineered
    complementation. Later bifunctionality prevents attributing the deletion phenotype
    solely to phosphatase activity. Negative and association-only results remain outside
    the graph.
  target_ids:
  - PF01950
  evidence_ids:
  - primary
  - native
  - knockout-contexts
  - carbon-contexts
  - dual-function-followup
  - source-coverage
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: The record does not yet retain the full bifunctional aldolase/phosphatase
    mechanism. Full Rashid2002/Nishimasu2004, main Say2010/Fushinobu2011/Du2011 experiments
    and additional members remain to be inspected. Public supplements provide concrete
    follow-up leads and a verified ST0318 coordinate offset, not full method/construct
    validation. Exact historical preparations, selective-activity rescue, polarity,
    carbon regulator, RNA stability, protein abundance, direct cellular flux and isolated-domain
    function remain unresolved. Filtered reviewed annotations are not a membership
    or experimental census.
  target_ids:
  - PF01950
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01950-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Extend the bifunctional mechanism and resolve conditional cellular causation
  description: Inspect complete primary assays and construct-specific sequences for
    the later aldolase/phosphatase work, keeping paper versus UniProt coordinates
    explicit. Verify older Fbp assay buffer/metal/purification details without borrowing
    the IMPase protocol. Assess selective-activity mutants with folding and rescue
    controls before attributing the whole-gene growth phenotype to a single reaction.
    Separate synthetic from rich medium and exponential RNA from stationary extract
    activity. Extend member-specific primary coverage and retain a successor review;
    do not promote this scoped pass to REVIEWED.
  target_ids:
  - PF01950
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - knockout-contexts
  - carbon-contexts
  - dual-function-followup
  - source-coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01950.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Inspect complete primary assays and construct-specific sequences for
    the later aldolase/phosphatase work, keeping paper versus UniProt coordinates
    explicit. Verify older Fbp assay buffer/metal/purification details without borrowing
    the IMPase protocol. Assess selective-activity mutants with folding and rescue
    controls before attributing the whole-gene growth phenotype to a single reaction.
    Separate synthetic from rich medium and exponential RNA from stationary extract
    activity. Extend member-specific primary coverage and retain a successor review;
    do not promote this scoped pass to REVIEWED.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01950
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Sato2004 full public HTML Methods/Results/Discussion and Tables1/2 read; Figures2/3/4
  visually inspected. Fushinobu2011 complete supplement text inspected but not a visual/Methods
  review; Say2010 supplement partially inspected, not a complete quantitative or visual
  pass. Main Nature articles are subscription restricted. No raw data reanalysis,
  clone sequencing, experimental replication or independent expert endorsement.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
