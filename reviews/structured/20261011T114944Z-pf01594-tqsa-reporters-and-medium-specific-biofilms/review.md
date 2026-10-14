# PF01594 TqsA reporter phenotypes with unresolved direct transport

- Review: 20261011T114944Z-pf01594-tqsa-reporters-and-medium-specific-biofilms
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T11:49:08Z
- Finished UTC: 2026-10-11T11:49:44Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Eight observed indirect effects are retained in seven graphs, including extracellular activity in two media, two lsr reporter phases, extracellular genetic complementation and three medium-specific attached-mass effects. Direct AI-2 transport and a serial AI-2-to-biofilm mechanism are not demonstrated by these sources.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Pending PF01594 selected during accession-ordered review of all 8296 frozen families; BW25113 ydgG/tqsA is the specific primary experimental example.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01594 | data/families/PF01594.yaml | generated | PF01594 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01594 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01594.

P0AFS5 / tqsA/ydgG / b1601 is a 344-aa K12 reference with PF01594 17-328, sequence version 1, exactly matching InterPro. The paper names b1601/ydgG and verifies a complete BW25113 replacement by PCR. This is gene-level reference mapping, not independent historical clone sequencing or an isolated-domain intervention; plasmid tags/linkers remain unverified.

### Directed effects and limits

graph: supported. Targets: PF01594.

All eight edges are PHENOTYPIC/INDIRECT/OBSERVED. Extracellular BB170 and intracellular-proxy lacZ nodes identify the actual measurements. OD600 0.6 versus 6, washed complementation at 0.9, media and antibiotic contexts stay separate. The LB staining decrease prevents a universal increase claim. The 2022 inability to demonstrate transport and preliminary binding evidence prevent an observed molecular export edge or structural-motion chain.

### Remaining family coverage

completeness: concern. Targets: PF01594.

Full historical constructs, detailed reporter protocol, initial well-assay duration/temperature, additional biofilm/motility rescue and flow contexts, other family members and direct transport experiments remain incompletely assessed. The 2022 spectra and supplementary mutant data were not visually reviewed; suspect printed units cannot be silently corrected.

## Findings

### additional-contexts: Resolve direct transport and extend assay-specific TqsA coverage

minor / open / confirmed; issue key: pf01594-causal-context-coverage.

Inspect 2022 primary/supplementary structural and binding figures, verify construct identities and ambiguous mass-shift units, and seek direct substrate/transport experiments. Curate remaining 2006 motility, rescue and flow endpoints with their own sampling and conditions, retaining the LB opposite direction, deletion pleiotropy and export-versus-uptake alternatives.

## Recommended Actions And Acceptance Checks

### extend-contexts

Inspect 2022 primary/supplementary structural and binding figures, verify construct identities and ambiguous mass-shift units, and seek direct substrate/transport experiments. Curate remaining 2006 motility, rescue and flow endpoints with their own sampling and conditions, retaining the LB opposite direction, deletion pleiotropy and export-versus-uptake alternatives.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/b/137198/files/2021/08/096.pdf; Herzberg 2006 Methods/Table 1 pp. 588-589, Results pp. 589-591, visually inspected Figure 3 p. 591 and Discussion pp. 595-597. No quantitative image reanalysis. | supports | Whole-gene deletion lowers BB170 extracellular reporter activity, increases LBglu lsr::lacZ output and changes crystal-violet-stained attached material in opposite directions depending on glucose/medium. Extracellular trans-complementation uses a distinct washed OD600-0.9 protocol. These measured proxies are not absolute AI-2 concentrations or direct flux. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0AFS5/entry/pfam/PF01594/; Accession and domain locations; paired UniProt identity facts | supports | P0AFS5 / tqsA/ydgG / b1601 is a 344-aa K12 reference with PF01594 17-328, sequence version 1, exactly matching InterPro. The paper names b1601/ydgG and verifies a complete BW25113 replacement by PCR. This is gene-level reference mapping, not independent historical clone sequencing or an isolated-domain intervention; plasmid tags/linkers remain unverified. |
| transport-limit-2022 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9475539/; Khera 2022 AI-2 interaction Results, antiport Methods and concluding Discussion. | supports | Authors report unsuccessful TqsA transport demonstrations and retain AI-2 as a probable substrate. Native-MS binding, docking and proposed motion do not establish a directly observed transport cycle; supplementary spectra and the printed mass-shift unit need assessment. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01594 | data/families/PF01594.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- The 2006 Methods and Figure 3 were visually checked in the author PDF. The 2022 selected full text was read, but figures and supplementary spectra were not visually inspected. No raw data, independent cloning or experimental replication was performed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T114944Z-pf01594-tqsa-reporters-and-medium-specific-biofilms
title: PF01594 TqsA reporter phenotypes with unresolved direct transport
started_at: '2026-10-11T11:49:08Z'
finished_at: '2026-10-11T11:49:44Z'
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
summary: Eight observed indirect effects are retained in seven graphs, including extracellular
  activity in two media, two lsr reporter phases, extracellular genetic complementation
  and three medium-specific attached-mass effects. Direct AI-2 transport and a serial
  AI-2-to-biofilm mechanism are not demonstrated by these sources.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01594.yaml
    sha256: 9f7b81f18aa97cda40a6013086b0f5edebaad169bfe637351903a87e21d0abf4
    role: context
  - path: data/families/PF01594.yaml
    sha256: 29a73639f6da67c01024171e668757d9882a2d1f820b39d3b2de5ec5245a0c51
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
  - path: evidence/PF01594/herzberg-2006-assays.txt
    role: context
    sha256: e1f5bf2694297e49b7d31b5dcc8dec7dc4efaf8d00796473fdd68e0a7ef1c795
  - path: evidence/PF01594/TqsA-identity.txt
    role: context
    sha256: 61124fbc78dbe1d52e487d9d208a1258a0fab7e0a91114f95a2a538c339aac36
  - path: evidence/PF01594/khera-2022-transport-limits.txt
    role: context
    sha256: b00768258582e0dc3cb875c47b3aece9d95b5def30a3f58c24d78a1add1642d4
targets:
- target_id: PF01594
  path: data/families/PF01594.yaml
  label: PF01594
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01594.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 501ca76b9d24c382b015c85b1c280259e7b49a77e6c67f2a7045064c90b615d0
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Pending PF01594 selected during accession-ordered review of all 8296
    frozen families; BW25113 ydgG/tqsA is the specific primary experimental example.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01594
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Full historical constructs, detailed reporter protocol, initial well-assay
      duration/temperature, additional biofilm/motility rescue and flow contexts,
      other family members and direct transport experiments remain incompletely assessed.
      The 2022 spectra and supplementary mutant data were not visually reviewed; suspect
      printed units cannot be silently corrected.
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
  - PF01594
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/b/137198/files/2021/08/096.pdf
  locator: Herzberg 2006 Methods/Table 1 pp. 588-589, Results pp. 589-591, visually
    inspected Figure 3 p. 591 and Discussion pp. 595-597. No quantitative image reanalysis.
  accessed_at: '2026-10-11T11:49:44Z'
  support: supports
  snapshot_sha256: e1f5bf2694297e49b7d31b5dcc8dec7dc4efaf8d00796473fdd68e0a7ef1c795
  summary: Whole-gene deletion lowers BB170 extracellular reporter activity, increases
    LBglu lsr::lacZ output and changes crystal-violet-stained attached material in
    opposite directions depending on glucose/medium. Extracellular trans-complementation
    uses a distinct washed OD600-0.9 protocol. These measured proxies are not absolute
    AI-2 concentrations or direct flux.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0AFS5/entry/pfam/PF01594/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T11:49:44Z'
  support: supports
  snapshot_sha256: 61124fbc78dbe1d52e487d9d208a1258a0fab7e0a91114f95a2a538c339aac36
  summary: P0AFS5 / tqsA/ydgG / b1601 is a 344-aa K12 reference with PF01594 17-328,
    sequence version 1, exactly matching InterPro. The paper names b1601/ydgG and
    verifies a complete BW25113 replacement by PCR. This is gene-level reference mapping,
    not independent historical clone sequencing or an isolated-domain intervention;
    plasmid tags/linkers remain unverified.
- evidence_id: transport-limit-2022
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC9475539/
  locator: Khera 2022 AI-2 interaction Results, antiport Methods and concluding Discussion.
  summary: Authors report unsuccessful TqsA transport demonstrations and retain AI-2
    as a probable substrate. Native-MS binding, docking and proposed motion do not
    establish a directly observed transport cycle; supplementary spectra and the printed
    mass-shift unit need assessment.
  accessed_at: '2026-10-11T11:49:44Z'
  support: supports
  snapshot_sha256: b00768258582e0dc3cb875c47b3aece9d95b5def30a3f58c24d78a1add1642d4
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T11:49:44Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01594
  kind: record_content
  reference: data/families/PF01594.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T11:49:44Z'
  support: context_only
  snapshot_sha256: 29a73639f6da67c01024171e668757d9882a2d1f820b39d3b2de5ec5245a0c51
  quote: "id: Pfam:PF01594\npfam_id: PF01594\nname: AI-2E family transporter\nshort_name:\
    \ AI-2E_transport\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01594\n\
    counters:\n  proteins: 58169\n  matches: 58317\n  proteomes: 19308\n  taxa: 29447\n\
    \  structures: 2\n  alphafold_models: 37191\n  domain_architectures: 79\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002549\ndescription: This family includes four different\
    \ proteins from E. coli alone. One of them, YdgG or TqsA,\n  has been shown to\
    \ mediate transport of the quorum-sensing signal autoinducer 2 (AI-2). It is not\
    \ clear\n  if TqsA enhances secretion of AI-2 or inhibits AI-2 uptake. By altering\
    \ the intracellular concentration\n  of AI-2, TqsA affects gene expression in\
    \ biofilms and biofilm formation [[cite:PUB00076990]]. TsqA belongs\n  to the\
    \ AI-2 exporter (AI-2E) superfamily [[cite:PUB00076989]].\ncuration_history: history/records/PF01594\n\
    discussions:\n- discussion_id: tqsa-transport-direction-and-phenotype-mediators\n\
    \  prompt: Resolve direct TqsA transport and assay-specific mediators before extending\
    \ reporter effects\n    into a molecular pathway.\n  kind: CURATION_TODO\n  status:\
    \ OPEN\n  rationale: The historical knockout/rescue data support scoped cellular\
    \ effects but do not distinguish\n    enhanced export from inhibited uptake, and\
    \ structure/binding does not by itself establish transport.\n  evidence:\n  -\
    \ reference: PMID:16385049\n    supports: PARTIAL\n    evidence_source: full_text_and_figure_3\n\
    \    explanation: Eight observed indirect effects retain separate extracellular,\
    \ intracellular-proxy, complementation\n      and medium-specific staining contexts.\
    \ The exact historical clone, initial well-assay time/temperature\n      and detailed\
    \ reporter protocol remain open. Other motility, flow-cell and complementation\
    \ endpoints\n      require separate curation; MIC ordering is ambiguous.\n  -\
    \ reference: PMID:35698912\n    supports: PARTIAL\n    evidence_source: selected_full_text\n\
    \    explanation: The 2022 Discussion explicitly reports inability to demonstrate\
    \ TqsA transport with attempted\n      methods. Native-MS binding and proposed\
    \ structural movement do not supply an observed transmembrane\n      step. Preliminary\
    \ mutants, the suspect printed mass-shift unit and uninspected supplementary spectra\n\
    \      require further assessment; condition-specific negative antiport results\
    \ are not universal nonfunction.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n\
    \  notes: Do not transfer Upf0118 antiport to TqsA or collapse the four E. coli\
    \ family members. Retain\n    the LB biofilm decrease, glucose-dependent regulation,\
    \ possible deletion pleiotropy and lack of established\n    AI-2-specific mediation.\
    \ Partial scientific self-review; IN_PROGRESS.\ncausal_graphs:\n- graph_id: tqsa-deletion-extracellular-activity-lb\n\
    \  title: Whole-gene ydgG deletion lowers extracellular AI-2 reporter activity\
    \ in LB\n  scope: E. coli K-12 BW25113 and its complete ydgG::KmR replacement,\
    \ Herzberg 2006 pp. 589-590; not a\n    purified TqsA transport assay.\n  context:\
    \ Overnight donor cultures are diluted 1:100 in LB and harvested at OD600 0.6.\
    \ Filter-sterilized\n    supernatants are assayed with V. harveyi BB170 luminescence\
    \ normalized per reporter cell. The cited\n    detailed reporter protocol was\
    \ not independently inspected; no absolute AI-2 concentration or reporter\n  \
    \  incubation time is invented.\n  family_mapping: P0AFS5 / tqsA/ydgG / b1601\
    \ is the 344-aa K12 reference, sequence version 1, with PF01594\n    17-328. The\
    \ paper identifies b1601/ydgG and verifies the complete BW25113 deletion by five\
    \ PCRs. Reference\n    sequence and InterPro match exactly, but the historical\
    \ assay strain/clone was not independently sequenced.\n    Deletion removes the\
    \ whole gene, not only the domain.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:83333\n\
    \  limitations: Reporter activity is not a direct chemical concentration or membrane\
    \ flux. Pleiotropy,\n    polarity and altered signal production/uptake remain\
    \ possible. This assay cannot distinguish increased\n    export from decreased\
    \ uptake; the later structural study did not demonstrate TqsA transport with its\n\
    \    attempted methods.\n  nodes:\n  - node_id: tqsa-deletion-lb\n    label: Complete\
    \ ydgG::KmR replacement rather than WT in LB\n    node_type: PERTURBATION\n  \
    \  grounding:\n    - UniProtKB:P0AFS5\n  - node_id: extracellular-bb170-lb\n \
    \   label: BB170 luminescence activity elicited by LB supernatant\n    node_type:\
    \ ACTIVITY\n  edges:\n  - edge_id: deletion-decreases-extracellular-lb\n    subject:\
    \ tqsa-deletion-lb\n    predicate: decreases\n    object: extracellular-bb170-lb\n\
    \    mechanism: The WT/knockout extracellular activity ratio is reported as 13\
    \ +/- 9 in LB. The deletion\n      decreases this reporter endpoint; it does not\
    \ directly prove TqsA-mediated AI-2 export or a domain-specific\n      reaction.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:16385049\n      source_url: https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/b/137198/files/2021/08/096.pdf\n\
    \      snippet: YdgG\n      explanation: AI-2 Methods p. 589 and extracellular-activity\
    \ Results p. 590 provide the LB comparison\n        and reporter endpoint; Discussion\
    \ retains export-versus-uptake alternatives.\n      cache_path: evidence/PF01594/herzberg-2006-assays.txt\n\
    \      cache_sha256: e1f5bf2694297e49b7d31b5dcc8dec7dc4efaf8d00796473fdd68e0a7ef1c795\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0AFS5/entry/pfam/PF01594/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0AFS5/entry/pfam/PF01594/\n\
    \      snippet: 'P0AFS5 Pfam:PF01594; domain interval: 17-328, inclusive.'\n \
    \     explanation: Current reference mapping supports the gene/domain association,\
    \ not identity of every\n        historical construct or isolated-domain causality.\n\
    \      cache_path: evidence/PF01594/TqsA-identity.txt\n      cache_sha256: 61124fbc78dbe1d52e487d9d208a1258a0fab7e0a91114f95a2a538c339aac36\n\
    - graph_id: tqsa-deletion-extracellular-activity-lbglu\n  title: Whole-gene ydgG\
    \ deletion lowers extracellular reporter activity in glucose-supplemented LB\n\
    \  scope: The separate BW25113 ydgG::KmR versus WT comparison in Herzberg 2006\
    \ LBglu cultures.\n  context: LBglu is LB plus 0.2% glucose. Overnight donor cultures\
    \ are diluted 1:100 and harvested at\n    OD600 0.6. Filtered supernatants are\
    \ tested with BB170 luminescence normalized per reporter cell.\n    This plasmid-free\
    \ comparison is not the washed OD600-0.9 complementation assay.\n  family_mapping:\
    \ b1601/ydgG maps to P0AFS5, 344 aa, PF01594 17-328; the intervention replaces\
    \ the entire\n    BW25113 gene with a kanamycin cassette. K12 reference identity\
    \ is not independent historical clone\n    resequencing.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:83333\n  limitations: This indirect bioassay does not establish\
    \ absolute extracellular AI-2, protein-mediated\n    flux or a single transport\
    \ direction. Glucose changes regulatory context; the LB result is not substituted\n\
    \    for this condition.\n  nodes:\n  - node_id: tqsa-deletion-lbglu\n    label:\
    \ Complete ydgG::KmR replacement rather than WT in LBglu\n    node_type: PERTURBATION\n\
    \  - node_id: extracellular-bb170-lbglu\n    label: BB170 luminescence activity\
    \ elicited by LBglu supernatant\n    node_type: ACTIVITY\n  edges:\n  - edge_id:\
    \ deletion-decreases-extracellular-lbglu\n    subject: tqsa-deletion-lbglu\n \
    \   predicate: decreases\n    object: extracellular-bb170-lbglu\n    mechanism:\
    \ WT supernatant produces 4 +/- 2 times the knockout reporter activity in LBglu.\
    \ The retained\n      direction is a deletion effect on the measured reporter\
    \ response, not a direct TqsA export step.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:16385049\n\
    \      source_url: https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/b/137198/files/2021/08/096.pdf\n\
    \      snippet: YdgG\n      explanation: Extracellular-activity Results p. 590\
    \ distinguish the 4 +/- 2 LBglu ratio from the\n        13 +/- 9 LB ratio; Methods\
    \ define donor sampling and the reporter.\n      cache_path: evidence/PF01594/herzberg-2006-assays.txt\n\
    \      cache_sha256: e1f5bf2694297e49b7d31b5dcc8dec7dc4efaf8d00796473fdd68e0a7ef1c795\n\
    - graph_id: tqsa-deletion-lsr-reporter-phases\n  title: ydgG deletion increases\
    \ lsr promoter reporter output in two LBglu growth phases\n  scope: BW25113 WT\
    \ and ydgG::KmR carrying pLW11 lsrACDBFG::lacZ, Herzberg 2006 Figure 3; not direct\
    \ intracellular\n    AI-2 quantitation.\n  context: LB plus 0.2% glucose; overnight\
    \ cultures are diluted to obtain exponential cells at OD600 0.6\n    and stationary\
    \ cells at OD600 6. Beta-galactosidase activity is reported as ONPG cleavage per\
    \ minute\n    per protein mass. Figure 3 uses duplicate experiments and SD; the\
    \ two phases remain separate endpoints.\n  family_mapping: The complete BW25113\
    \ ydgG deletion maps at gene level to 344-aa P0AFS5, whose current\n    PF01594\
    \ domain spans 17-328. The reporter plasmid is a separate assay entity and does\
    \ not measure\n    the isolated domain.\n  scope_status: PHENOTYPIC\n  taxon:\
    \ NCBITaxon:83333\n  limitations: lsr transcription is an indirect intracellular-signal\
    \ proxy affected by regulatory context,\n    including glucose catabolite repression.\
    \ The authors propose a future luxS/ydgG double-mutant test;\n    AI-2 mediation\
    \ is not uniquely established. No intracellular chemical concentration, export\
    \ velocity\n    or serial reporter-to-biofilm chain is inferred.\n  nodes:\n \
    \ - node_id: tqsa-deletion-exponential\n    label: ydgG::KmR rather than WT at\
    \ OD600 0.6 in LBglu\n    node_type: PERTURBATION\n  - node_id: tqsa-deletion-stationary\n\
    \    label: ydgG::KmR rather than WT at OD600 6 in LBglu\n    node_type: PERTURBATION\n\
    \  - node_id: lsr-exponential-output\n    label: Exponential-phase lsrACDBFG::lacZ\
    \ beta-galactosidase output\n    node_type: ACTIVITY\n  - node_id: lsr-stationary-output\n\
    \    label: Stationary-phase lsrACDBFG::lacZ beta-galactosidase output\n    node_type:\
    \ ACTIVITY\n  edges:\n  - edge_id: deletion-increases-exponential-lsr\n    subject:\
    \ tqsa-deletion-exponential\n    predicate: increases\n    object: lsr-exponential-output\n\
    \    mechanism: The knockout/WT lsr reporter ratio is 16 +/- 5 under exponential\
    \ LBglu conditions. Increased\n      beta-galactosidase is observed; the implied\
    \ intracellular AI-2 change is not a direct chemical measurement.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:16385049\n      source_url: https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/b/137198/files/2021/08/096.pdf\n\
    \      snippet: YdgG\n      explanation: Visually inspected Figure 3 and Results\
    \ p. 591 support the exponential LBglu comparison;\n        AI-2 Methods p. 589\
    \ identify the reporter and OD600 endpoint.\n      cache_path: evidence/PF01594/herzberg-2006-assays.txt\n\
    \      cache_sha256: e1f5bf2694297e49b7d31b5dcc8dec7dc4efaf8d00796473fdd68e0a7ef1c795\n\
    \  - edge_id: deletion-increases-stationary-lsr\n    subject: tqsa-deletion-stationary\n\
    \    predicate: increases\n    object: lsr-stationary-output\n    mechanism: At\
    \ stationary phase the knockout/WT lsr reporter ratio is 10 +/- 5. This separate\
    \ endpoint\n      is not treated as a time-resolved mechanistic transition from\
    \ the exponential-phase measurement.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:16385049\n\
    \      source_url: https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/b/137198/files/2021/08/096.pdf\n\
    \      snippet: YdgG\n      explanation: Figure 3's stationary LBglu bars and\
    \ Results p. 591 establish the increase under the\n        independently specified\
    \ OD600-6 condition.\n      cache_path: evidence/PF01594/herzberg-2006-assays.txt\n\
    \      cache_sha256: e1f5bf2694297e49b7d31b5dcc8dec7dc4efaf8d00796473fdd68e0a7ef1c795\n\
    - graph_id: tqsa-complemented-extracellular-activity\n  title: Induced ydgG complementation\
    \ restores extracellular reporter activity\n  scope: BW25113 ydgG::KmR with pCA24NydgG+\
    \ and empty-vector controls, Herzberg 2006 extracellular complementation\n   \
    \ experiment.\n  context: Cultures receive IPTG and 30 ug/ml chloramphenicol,\
    \ are harvested at OD600 0.6, washed twice\n    for 10 min at 8820g to remove\
    \ antibiotic that inhibits the Vibrio reporter, and resuspended in 20\n    ml\
    \ LB plus 0.2% glucose. Supernatants are sampled after growth to OD600 0.9. The\
    \ retained endpoint\n    is 1.5 mM IPTG, compared with the uncomplemented/vector\
    \ context and normalized to WT with pCA24N.\n  family_mapping: The historical\
    \ pCA24NydgG+ expresses the b1601/ydgG gene corresponding to P0AFS5, PF01594\n\
    \    17-328. Full historical tag/linker sequence is not established. Gene-level\
    \ trans-complementation does\n    not isolate the domain or rule out every overexpression-mediated\
    \ effect.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:83333\n  limitations:\
    \ Restoration concerns the extracellular BB170 bioassay only; it is not direct\
    \ export, restoration\n    of intracellular lsr output or a universal rescue of\
    \ all deletion phenotypes. Washed OD600-0.9 cultures\n    must not be merged with\
    \ the plasmid-free OD600-0.6 comparisons.\n  nodes:\n  - node_id: induce-tqsa-complement\n\
    \    label: Induce pCA24NydgG+ in the deletion background with 1.5 mM IPTG\n \
    \   node_type: PERTURBATION\n  - node_id: complemented-extracellular-output\n\
    \    label: Extracellular BB170 activity after antibiotic removal and regrowth\n\
    \    node_type: ACTIVITY\n  edges:\n  - edge_id: complementation-increases-extracellular-output\n\
    \    subject: induce-tqsa-complement\n    predicate: increases\n    object: complemented-extracellular-output\n\
    \    mechanism: Induced ydgG expression increases the deletion strain's extracellular\
    \ reporter activity\n      toward the WT-empty-vector level; the reported complemented/WT\
    \ ratio at 1.5 mM IPTG is 1.0 +/- 0.3.\n      This is genetic support for the\
    \ phenotype, not resolution of export versus uptake.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:16385049\n      source_url: https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/b/137198/files/2021/08/096.pdf\n\
    \      snippet: YdgG\n      explanation: Complementation Methods p. 589 and Results\
    \ p. 591 explicitly state the wash/regrowth\n        protocol, empty-vector comparator,\
    \ dose series and restoration endpoint.\n      cache_path: evidence/PF01594/herzberg-2006-assays.txt\n\
    \      cache_sha256: e1f5bf2694297e49b7d31b5dcc8dec7dc4efaf8d00796473fdd68e0a7ef1c795\n\
    - graph_id: tqsa-deletion-biofilm-lbglu\n  title: ydgG deletion increases crystal-violet-stained\
    \ attached material in LBglu\n  scope: BW25113 ydgG::KmR versus WT in the 96-well\
    \ assay, Herzberg 2006 p. 589; not the separate flow-cell\n    experiment.\n \
    \ context: LB plus 0.2% glucose; overnight cultures diluted to OD600 0.05. Attached\
    \ material at the bottom\n    and air-liquid interface is stained with 0.1% crystal\
    \ violet for 20 min. Two independent experiments,\n    each four wells, are reported.\
    \ Initial-assay culture duration and temperature are not explicit in\n    the\
    \ inspected Methods.\n  family_mapping: Complete ydgG replacement affects the\
    \ whole P0AFS5-associated gene, including PF01594\n    17-328 and its flanks;\
    \ the current reference is 344 aa and gene-matched to BW25113, not independently\n\
    \    clone-sequenced.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:83333\n\
    \  limitations: Staining is an attached-mass proxy, not a uniquely AI-2-mediated\
    \ mechanism or direct domain\n    activity. The paper reports separate trans-complementation\
    \ with different antibiotic/induction conditions;\n    that is not silently substituted\
    \ into this plasmid-free comparison. The direction reverses in unsupplemented\n\
    \    LB.\n  nodes:\n  - node_id: tqsa-deletion-biofilm-lbglu\n    label: ydgG::KmR\
    \ rather than WT in LB plus glucose\n    node_type: PERTURBATION\n  - node_id:\
    \ stained-mass-lbglu\n    label: Crystal-violet-stained attached material in LBglu\
    \ wells\n    node_type: STATE\n  edges:\n  - edge_id: deletion-increases-lbglu-attached-mass\n\
    \    subject: tqsa-deletion-biofilm-lbglu\n    predicate: increases\n    object:\
    \ stained-mass-lbglu\n    mechanism: The knockout/WT staining ratio is 3.8 +/-\
    \ 0.2 in LBglu. This assay-specific increase is\n      not proof that TqsA directly\
    \ represses a molecular biofilm pathway or that every medium has the\n      same\
    \ response.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:16385049\n      source_url:\
    \ https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/b/137198/files/2021/08/096.pdf\n\
    \      snippet: YdgG\n      explanation: The 96-well Methods p. 588 and initial\
    \ biofilm Results p. 589 support this LBglu ratio,\n        not the much larger\
    \ flow-cell ratios.\n      cache_path: evidence/PF01594/herzberg-2006-assays.txt\n\
    \      cache_sha256: e1f5bf2694297e49b7d31b5dcc8dec7dc4efaf8d00796473fdd68e0a7ef1c795\n\
    - graph_id: tqsa-deletion-biofilm-m9cglu\n  title: ydgG deletion increases attached\
    \ material in glucose/Casamino-Acids M9 wells\n  scope: The separate BW25113 ydgG::KmR\
    \ versus WT M9Cglu 96-well comparison in Herzberg 2006.\n  context: M9 supplemented\
    \ with 0.4% glucose and 0.4% Casamino Acids; overnight cultures diluted to OD600\n\
    \    0.05. Total attached material is stained with 0.1% crystal violet for 20\
    \ min. Two independent experiments\n    with four wells each; initial-assay incubation\
    \ duration and temperature remain unverified.\n  family_mapping: The whole-gene\
    \ intervention maps to P0AFS5 / b1601, PF01594 17-328, in the BW25113 assay\n\
    \    background. It does not specifically remove only the annotated domain.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:83333\n  limitations: The 96-well\
    \ endpoint is not the separate 24-h flow-chamber assay, and four wells are technical\n\
    \    subsamples rather than four independent cultures. This modest increase does\
    \ not establish export direction,\n    substrate specificity or a causal AI-2-to-biofilm\
    \ chain.\n  nodes:\n  - node_id: tqsa-deletion-m9cglu\n    label: ydgG::KmR rather\
    \ than WT in M9Cglu wells\n    node_type: PERTURBATION\n  - node_id: stained-mass-m9cglu\n\
    \    label: Crystal-violet-stained attached material in M9Cglu wells\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: deletion-increases-m9cglu-attached-mass\n    subject:\
    \ tqsa-deletion-m9cglu\n    predicate: increases\n    object: stained-mass-m9cglu\n\
    \    mechanism: The knockout/WT crystal-violet endpoint ratio is 1.6 +/- 0.1.\
    \ The direction is retained\n      only for this medium and assay, without importing\
    \ the flow-cell biomass or thickness magnitudes.\n    directness: INDIRECT\n \
    \   support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:16385049\n      source_url: https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/b/137198/files/2021/08/096.pdf\n\
    \      snippet: YdgG\n      explanation: Methods p. 588 define M9Cglu and staining;\
    \ Results p. 589 provide the distinct 1.6\n        +/- 0.1 well-assay ratio.\n\
    \      cache_path: evidence/PF01594/herzberg-2006-assays.txt\n      cache_sha256:\
    \ e1f5bf2694297e49b7d31b5dcc8dec7dc4efaf8d00796473fdd68e0a7ef1c795\n- graph_id:\
    \ tqsa-deletion-biofilm-lb\n  title: ydgG deletion decreases attached material\
    \ in LB without added glucose\n  scope: The condition-specific opposite-direction\
    \ BW25113 comparison in Herzberg 2006's 96-well assay.\n  context: Unsupplemented\
    \ LB; cultures start at OD600 0.05 after overnight growth. Both bottom and air-liquid-interface\n\
    \    material contribute to the 0.1% crystal-violet stain after 20 min. Two independent\
    \ experiments with\n    four wells each; incubation duration and temperature of\
    \ this initial experiment are not specified\n    in the inspected Methods.\n \
    \ family_mapping: BW25113 complete ydgG::KmR replacement corresponds to the gene\
    \ encoding P0AFS5, whose\n    reference domain is PF01594 17-328. This is a whole-gene\
    \ phenotype, not isolated-domain biochemical\n    activity.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:83333\n  limitations: This decrease prevents a medium-independent\
    \ claim that ydgG deletion increases biofilm.\n    The endpoint is attached stainable\
    \ material, not a molecular transport rate; no causal mediator is\n    uniquely\
    \ established.\n  nodes:\n  - node_id: tqsa-deletion-biofilm-lb\n    label: ydgG::KmR\
    \ rather than WT in LB without added glucose\n    node_type: PERTURBATION\n  -\
    \ node_id: stained-mass-lb\n    label: Crystal-violet-stained attached material\
    \ in LB wells\n    node_type: STATE\n  edges:\n  - edge_id: deletion-decreases-lb-attached-mass\n\
    \    subject: tqsa-deletion-biofilm-lb\n    predicate: decreases\n    object:\
    \ stained-mass-lb\n    mechanism: The knockout/WT staining ratio is 0.5 +/- 0.1\
    \ in LB, opposite to the increases in glucose-supplemented\n      media. The contextual\
    \ negative is retained rather than erased by the paper's broad repression wording.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:16385049\n      source_url: https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/b/137198/files/2021/08/096.pdf\n\
    \      snippet: YdgG\n      explanation: Initial biofilm Results p. 589 explicitly\
    \ report decreased staining in LB, while Methods\n        p. 588 define the assay\
    \ and medium.\n      cache_path: evidence/PF01594/herzberg-2006-assays.txt\n \
    \     cache_sha256: e1f5bf2694297e49b7d31b5dcc8dec7dc4efaf8d00796473fdd68e0a7ef1c795\n\
    curation_events:\n- timestamp: '2026-10-11T11:42:11Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Add eight TqsA gene-perturbation reporter\
    \ and medium-specific biofilm effects without asserting\n    direct AI-2 transport.\n\
    \  history_record: history/records/PF01594/2026-10-11T114211Z-codex-2cd742.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: P0AFS5 / tqsA/ydgG / b1601 is a 344-aa K12 reference with PF01594 17-328,
    sequence version 1, exactly matching InterPro. The paper names b1601/ydgG and
    verifies a complete BW25113 replacement by PCR. This is gene-level reference mapping,
    not independent historical clone sequencing or an isolated-domain intervention;
    plasmid tags/linkers remain unverified.
  target_ids:
  - PF01594
  evidence_ids:
  - identity
  - primary
  - transport-limit-2022
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: All eight edges are PHENOTYPIC/INDIRECT/OBSERVED. Extracellular BB170 and
    intracellular-proxy lacZ nodes identify the actual measurements. OD600 0.6 versus
    6, washed complementation at 0.9, media and antibiotic contexts stay separate.
    The LB staining decrease prevents a universal increase claim. The 2022 inability
    to demonstrate transport and preliminary binding evidence prevent an observed
    molecular export edge or structural-motion chain.
  target_ids:
  - PF01594
  evidence_ids:
  - primary
  - native
  - transport-limit-2022
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Full historical constructs, detailed reporter protocol, initial well-assay
    duration/temperature, additional biofilm/motility rescue and flow contexts, other
    family members and direct transport experiments remain incompletely assessed.
    The 2022 spectra and supplementary mutant data were not visually reviewed; suspect
    printed units cannot be silently corrected.
  target_ids:
  - PF01594
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01594-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve direct transport and extend assay-specific TqsA coverage
  description: Inspect 2022 primary/supplementary structural and binding figures,
    verify construct identities and ambiguous mass-shift units, and seek direct substrate/transport
    experiments. Curate remaining 2006 motility, rescue and flow endpoints with their
    own sampling and conditions, retaining the LB opposite direction, deletion pleiotropy
    and export-versus-uptake alternatives.
  target_ids:
  - PF01594
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - transport-limit-2022
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01594.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Inspect 2022 primary/supplementary structural and binding figures,
    verify construct identities and ambiguous mass-shift units, and seek direct substrate/transport
    experiments. Curate remaining 2006 motility, rescue and flow endpoints with their
    own sampling and conditions, retaining the LB opposite direction, deletion pleiotropy
    and export-versus-uptake alternatives.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01594
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- The 2006 Methods and Figure 3 were visually checked in the author PDF. The 2022
  selected full text was read, but figures and supplementary spectra were not visually
  inspected. No raw data, independent cloning or experimental replication was performed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
