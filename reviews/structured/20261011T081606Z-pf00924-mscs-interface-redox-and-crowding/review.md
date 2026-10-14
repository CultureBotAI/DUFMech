# Scoped scientific self-review of MscS interface perturbations and crowding

- Review: 20261011T081606Z-pf00924-mscs-interface-redox-and-crowding
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T08:15:55Z
- Finished UTC: 2026-10-11T08:16:06Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Three MECHANISTIC graphs retain six DIRECT OBSERVED edges for G168D adaptation loss, double-mutant restoration, reversible DTT-dependent double-cysteine activity, WT crowding-conditioned inactivation and relative G168D resistance. Distinct 2011/2014 assay conditions and state readouts remain separate; structural chemistry is not labeled observed. Coverage is partial and status IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF00924 MscS beta-domain, the next accession-ordered SEEDED family, using mapped E. coli MscS mutants in the 2011 and 2014 primary patch-clamp studies.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF00924 | data/families/PF00924.yaml | generated | PF00924 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF00924 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF00924.

P0C0S1 mscS/yggB/b2924/JW2891 is a 286-residue K-12 reference, sequence version 1, with exact UniProt/InterPro agreement. PF00924 spans 114-180, including N117 and G168. The source's structural beta domain is 128-181, with N117 structurally in TM3b; neither boundary is an isolated experimental fragment. Complete pTRCMscS/pB10b sequences remain unverified.

### Directed effects and limits

graph: supported. Targets: PF00924.

All edges refer to directly measured electrical behavior or test-pulse availability in intact channels. Double-mutant rescue does not mean N117K alone activates adaptation; redox reversibility does not directly identify bond chemistry or a unique closed state. The 2014 Ficoll-plus-tension context is conjunctive, with 5% panels D/E kept distinct from the 10% examples and the earlier unresolved adaptation state.

### Remaining family coverage

completeness: concern. Targets: PF00924.

Exact clone junctions, temperatures, per-panel 2014 strain assignment, some referenced preparation details and independent 2011 replicate counts remain unresolved. Raw traces, supplements, simulations, direct structural chemistry, other homologs and osmotic-survival contexts are not fully curated. The 2018 N117C/N167C lead is a different mutant and is not adopted as N117C/G168C evidence.

## Findings

### additional-contexts: Resolve MscS state chemistry and expand member-specific contexts

minor / open / confirmed; issue key: pf00924-causal-context-coverage.

Retrieve complete constructs and patch metadata, inspect independent chemistry/state measurements, and curate other homologs or cellular effects only with their own controls and domain mapping. Preserve assay-specific buffers, voltages, conditioning histories, model uncertainty and a successor retained review.

## Recommended Actions And Acceptance Checks

### extend-contexts

Retrieve complete constructs and patch metadata, inspect independent chemistry/state measurements, and curate other homologs or cellular effects only with their own controls and domain mapping. Preserve assay-specific buffers, voltages, conditioning histories, model uncertainty and a successor retained review.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC3013047/; Strain, mutagenesis and electrophysiology Methods; beta-domain Results and Discussion; Figures 4/6 visually inspected | supports | Figure 4 distinguishes G168D sustained current from WT and N117K/G168D current decline. Figure 6B shows reversible restoration of N117C/G168C activity by 2.5 mM DTT in an MscL-retaining background. The protocol does not distinguish desensitization from inactivation, and proposed salt-bridge or S-S locking chemistry is not directly measured. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0C0S1/entry/pfam/PF00924/; Accession and domain locations; paired UniProt identity facts | supports | P0C0S1 mscS/yggB/b2924/JW2891 is a 286-residue K-12 reference, sequence version 1, with exact UniProt/InterPro agreement. PF00924 spans 114-180, including N117 and G168. The source's structural beta domain is 128-181, with N117 structurally in TM3b; neither boundary is an isolated experimental fragment. Complete pTRCMscS/pB10b sequences remain unverified. |
| crowding-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC4003192/; Electrophysiology Methods, G168D Results and Figure 4D/E with caption | supports | Cytoplasmic 5% Ficoll increases WT inactivation during tension conditioning, while G168D is relatively resistant, with n=3 patches per genotype. The initial active population and conditioning protocol establish that crowding alone is not sufficient; membrane tension conversion uses stated assumptions. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf00924 | data/families/PF00924.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- The 2011 Figures 4/6 and 2014 Figure 4 were visually inspected. Adopted 2014 panels D/E use 5% Ficoll; panels A/B use 10%. Methods and relevant Results were read; the 2011 Discussion expressly limits state separation. Raw traces were not fitted, no bond was independently measured and supplements or simulations were not reanalyzed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T081606Z-pf00924-mscs-interface-redox-and-crowding
title: Scoped scientific self-review of MscS interface perturbations and crowding
started_at: '2026-10-11T08:15:55Z'
finished_at: '2026-10-11T08:16:06Z'
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
summary: Three MECHANISTIC graphs retain six DIRECT OBSERVED edges for G168D adaptation
  loss, double-mutant restoration, reversible DTT-dependent double-cysteine activity,
  WT crowding-conditioned inactivation and relative G168D resistance. Distinct 2011/2014
  assay conditions and state readouts remain separate; structural chemistry is not
  labeled observed. Coverage is partial and status IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF00924.yaml
    sha256: 7eded7524f962e3c2af6978df2cf36e17eda3aed50920e326b185ddf1a971058
    role: context
  - path: data/families/PF00924.yaml
    sha256: a41f0a5e64958c636ee451db1d7becc19688fb78a89dab47476d641cdc36b172
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
  - path: evidence/PF00924/koprowski-2011-mscS.txt
    role: context
    sha256: 15a5d51b3206a4adcec6c235105c55cd22b6d8b108e7dd06e0849578ccdea4f8
  - path: evidence/PF00924/MscS-identity.txt
    role: context
    sha256: 1d27dac72e322e4c458dcf489defe30febc2613c2e2ebd1e4dd5d9c56aa14d0e
  - path: evidence/PF00924/rowe-2014-mscS.txt
    role: context
    sha256: 40091e7b284047a5ca5f2346ee832ced69f4567144babe2897e4f6d3ed24070b
targets:
- target_id: PF00924
  path: data/families/PF00924.yaml
  label: PF00924
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF00924.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 2b38e2b5431bff1e3a8f9393d9322115d5871a1d321a4a1c6cf6558cf752dc9e
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF00924 MscS beta-domain, the next accession-ordered SEEDED family, using
    mapped E. coli MscS mutants in the 2011 and 2014 primary patch-clamp studies.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF00924
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Exact clone junctions, temperatures, per-panel 2014 strain assignment,
      some referenced preparation details and independent 2011 replicate counts remain
      unresolved. Raw traces, supplements, simulations, direct structural chemistry,
      other homologs and osmotic-survival contexts are not fully curated. The 2018
      N117C/N167C lead is a different mutant and is not adopted as N117C/G168C evidence.
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
  - PF00924
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3013047/
  locator: Strain, mutagenesis and electrophysiology Methods; beta-domain Results
    and Discussion; Figures 4/6 visually inspected
  accessed_at: '2026-10-11T08:16:06Z'
  support: supports
  snapshot_sha256: 15a5d51b3206a4adcec6c235105c55cd22b6d8b108e7dd06e0849578ccdea4f8
  summary: Figure 4 distinguishes G168D sustained current from WT and N117K/G168D
    current decline. Figure 6B shows reversible restoration of N117C/G168C activity
    by 2.5 mM DTT in an MscL-retaining background. The protocol does not distinguish
    desensitization from inactivation, and proposed salt-bridge or S-S locking chemistry
    is not directly measured.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0C0S1/entry/pfam/PF00924/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T08:16:06Z'
  support: supports
  snapshot_sha256: 1d27dac72e322e4c458dcf489defe30febc2613c2e2ebd1e4dd5d9c56aa14d0e
  summary: P0C0S1 mscS/yggB/b2924/JW2891 is a 286-residue K-12 reference, sequence
    version 1, with exact UniProt/InterPro agreement. PF00924 spans 114-180, including
    N117 and G168. The source's structural beta domain is 128-181, with N117 structurally
    in TM3b; neither boundary is an isolated experimental fragment. Complete pTRCMscS/pB10b
    sequences remain unverified.
- evidence_id: crowding-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4003192/
  locator: Electrophysiology Methods, G168D Results and Figure 4D/E with caption
  summary: Cytoplasmic 5% Ficoll increases WT inactivation during tension conditioning,
    while G168D is relatively resistant, with n=3 patches per genotype. The initial
    active population and conditioning protocol establish that crowding alone is not
    sufficient; membrane tension conversion uses stated assumptions.
  accessed_at: '2026-10-11T08:16:06Z'
  support: supports
  snapshot_sha256: 40091e7b284047a5ca5f2346ee832ced69f4567144babe2897e4f6d3ed24070b
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T08:16:06Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf00924
  kind: record_content
  reference: data/families/PF00924.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T08:16:06Z'
  support: context_only
  snapshot_sha256: a41f0a5e64958c636ee451db1d7becc19688fb78a89dab47476d641cdc36b172
  quote: "id: Pfam:PF00924\npfam_id: PF00924\nname: Mechanosensitive ion channel,\
    \ beta-domain\nshort_name: MS_channel_2nd\nseed_status: EX_DUF\ncharacterization_status:\
    \ UNSCORED\ncuration_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF00924\n\
    counters:\n  proteins: 69957\n  matches: 69995\n  proteomes: 20063\n  taxa: 30243\n\
    \  structures: 65\n  alphafold_models: 46372\n  domain_architectures: 274\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR006685\ndescription: This entry includes small conductance\
    \ mechanosensitive channels (MscS), which assembles to\n  a homoheptameric complex\
    \ [[cite:PUB00019883],[cite:PUB00019884],[cite:PUB00019885],[cite:PUB00101036],[cite:PUB00062568],[cite:PUB00101037]].\n\
    \  Each monomer consists of a N-terminal transmembrane region and a large cytoplasmic\
    \ segment composed\n  of a five-stranded antiparallel beta-sheet (middle/second)\
    \ domain and a C-terminal alpha/beta-domain\n  [[cite:PUB00101036],[cite:PUB00062568],[cite:PUB00101037],[cite:PUB00064132]].\
    \ This is the beta domain\n  which adopts a Sm-like barrel structure.\ncuration_history:\
    \ history/records/PF00924\ndiscussions:\n- discussion_id: mscs-state-chemistry-and-family-coverage\n\
    \  prompt: Resolve MscS interdomain chemistry and broaden member-specific causal\
    \ coverage.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: Channel-current\
    \ perturbations establish functional coupling but do not directly demonstrate\n\
    \    the proposed salt bridge, specific disulfide geometry or cage-motion pathway.\
    \ The two studies use\n    different state readouts and assay conditions.\n  evidence:\n\
    \  - reference: PMID:20978126\n    supports: PARTIAL\n    evidence_source: full_text\n\
    \    explanation: Figures 4/6 and Discussion support adaptation and reversible\
    \ DTT responses while leaving\n      desensitization-versus-inactivation and structural\
    \ chemistry unresolved.\n  - reference: PMID:24778428\n    supports: PARTIAL\n\
    \    evidence_source: selected_full_text\n    explanation: Figure 4D/E, electrophysiology\
    \ Methods and G168D Results support crowding-conditioned\n      inactivation.\
    \ Structural simulations, supplements and other gating contexts were not independently\n\
    \      curated.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n  notes: Obtain\
    \ complete clone sequences, per-panel host assignments, cited preparation protocols\
    \ and\n    independent bond/state measurements. The 2018 N117C/N167C lead is a\
    \ different double mutant, not N117C/G168C.\n    Other homologs and osmotic-survival\
    \ phenotypes need separate evidence and domain mapping. Partial\n    same-agent\
    \ review does not promote this IN_PROGRESS entry to REVIEWED.\ncausal_graphs:\n\
    - graph_id: mscs-interface-pressure-adaptation\n  title: G168D impairs MscS current\
    \ adaptation and N117K restores it in the double mutant\n  scope: Full-length\
    \ E. coli MscS variants in inside-out membrane patches from MJF465 lacking mscK,\
    \ mscS\n    and mscL; adopted endpoint is current decline during sustained pressure,\
    \ not an isolated beta-domain\n    activity.\n  context: pTRCMscS variants; bath\
    \ 400 mM sucrose, 200 mM KCl, 90 mM MgCl2, 4 mM CaCl2, 5 mM HEPES at\n    pH 7.2.\
    \ Pipette solution omits sucrose; pipette voltage is +15 mV. Pressure steps are\
    \ separated by\n    at least 3 min. Figure 4 displays three pressure responses\
    \ from the same patch per genotype, not three\n    independent replicates.\n \
    \ family_mapping: UniProtKB:P0C0S1, mscS/yggB/b2924/JW2891, is a 286-residue K-12\
    \ reference, sequence\n    version 1. Exact UniProt/InterPro agreement places\
    \ PF00924 at 114-180, including N117 and G168. The\n    paper's structural beta\
    \ domain is 128-181 and places N117 in TM3b. HMM and structural boundaries must\n\
    \    not be conflated; complete experimental clone junctions remain unverified.\n\
    \  scope_status: MECHANISTIC\n  taxon: NCBITaxon:83333\n  limitations: The 2011\
    \ protocol does not distinguish desensitization from inactivation. No direct salt-bridge\n\
    \    formation or interdomain motion is measured; cartoons are interpretations.\
    \ Pressure levels differ\n    among traces and no exact common-pressure rate is\
    \ claimed. Temperature, patch-specific induction and\n    independent replication\
    \ are not established by the adopted panels.\n  nodes:\n  - node_id: mscs-g168d-substitution\n\
    \    label: G168D replacing WT MscS in pressure-clamp assays\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:P0C0S1\n  - node_id: mscs-n117k-added-to-g168d\n\
    \    label: N117K added to the G168D full-length channel\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:P0C0S1\n  - node_id: sustained-pressure-current-adaptation\n\
    \    label: Decline of MscS current during sustained pressure\n    node_type:\
    \ PROCESS\n  edges:\n  - edge_id: g168d-decreases-current-adaptation\n    subject:\
    \ mscs-g168d-substitution\n    predicate: decreases\n    object: sustained-pressure-current-adaptation\n\
    \    mechanism: G168D traces retain activity during maintained pressure where\
    \ WT traces decline. The edge\n      encodes the directly observed channel-current\
    \ behavior without assigning a unique hidden gating\n      state or atomic explanation.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:20978126\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3013047/\n\
    \      snippet: no visible adaptation\n      explanation: Figure 4 WT and G168D\
    \ recordings and the beta-domain Results show the loss of visible\n        decline.\
    \ Discussion explicitly limits separation of desensitization and inactivation.\n\
    \      cache_path: evidence/PF00924/koprowski-2011-mscS.txt\n      cache_sha256:\
    \ 15a5d51b3206a4adcec6c235105c55cd22b6d8b108e7dd06e0849578ccdea4f8\n    - reference:\
    \ https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0C0S1/entry/pfam/PF00924/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0C0S1/entry/pfam/PF00924/\n\
    \      snippet: 'P0C0S1 Pfam:PF00924 interval: 114-180, inclusive'\n      explanation:\
    \ Maps both altered reference residues within the profile interval while preserving\
    \ the\n        distinct structural TM3b/beta assignments.\n      cache_path: evidence/PF00924/MscS-identity.txt\n\
    \      cache_sha256: 1d27dac72e322e4c458dcf489defe30febc2613c2e2ebd1e4dd5d9c56aa14d0e\n\
    \  - edge_id: n117k-in-g168d-restores-current-adaptation\n    subject: mscs-n117k-added-to-g168d\n\
    \    predicate: increases\n    object: sustained-pressure-current-adaptation\n\
    \    mechanism: The N117K/G168D double mutant regains WT-like current decline\
    \ compared with G168D. This\n      context-specific restoration is not an activating\
    \ effect of N117K alone or direct proof of a compensating\n      salt bridge.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:20978126\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3013047/\n\
    \      snippet: restored the wild type phenotype\n      explanation: Figure 4\
    \ compares the double mutant with both singles and WT. The double-mutant electrical\n\
    \        phenotype is adopted; its structural salt-bridge cartoon is not labeled\
    \ observed.\n      cache_path: evidence/PF00924/koprowski-2011-mscS.txt\n    \
    \  cache_sha256: 15a5d51b3206a4adcec6c235105c55cd22b6d8b108e7dd06e0849578ccdea4f8\n\
    - graph_id: mscs-double-cysteine-redox-response\n  title: DTT reversibly restores\
    \ pressure-evoked N117C/G168C MscS activity\n  scope: Full-length N117C/G168C\
    \ MscS in MJF429, which lacks mscK and mscS but retains MscL. The endpoint\n \
    \   is detectable MscS channel activity, not a directly measured disulfide reaction.\n\
    \  context: Figure 6B inside-out patches with the 2011 pH 7.2 bath and +15 mV\
    \ pipette protocol. Control,\n    2.5 mM DTT and washout are compared at the illustrated\
    \ pressure steps; MscL openings remain a pressure-response\n    control. Single-cysteine\
    \ channels are active in Figure 6A, but its caption does not assign their individual\n\
    \    patches to a strain.\n  family_mapping: P0C0S1 reference N117 and G168 both\
    \ lie in PF00924 residues 114-180. N117 belongs structurally\n    to TM3b and\
    \ G168 to the beta domain. Native full-length channel mutations, not a truncated-domain\n\
    \    reconstitution, underlie these comparisons.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:83333\n  limitations: Reversible reducing-agent dependence\
    \ supports a redox-sensitive constraint but does not\n    itself measure an S-S\
    \ bond or distinguish closed from inactivated states. Complete construct sequence,\n\
    \    temperature, independent replicate counts and folding controls are unresolved.\
    \ No universal redox\n    regulation of WT MscS is inferred.\n  nodes:\n  - node_id:\
    \ dtt-in-double-cysteine-assay\n    label: Addition of 2.5 mM DTT to N117C/G168C\
    \ pressure assay\n    node_type: PERTURBATION\n  - node_id: dtt-washout-double-cysteine\n\
    \    label: DTT washout after the reducing condition\n    node_type: PERTURBATION\n\
    \  - node_id: double-cysteine-channel-activity\n    label: Pressure-evoked N117C/G168C\
    \ MscS opening activity\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:P0C0S1\n\
    \  edges:\n  - edge_id: dtt-increases-double-cysteine-activity\n    subject: dtt-in-double-cysteine-assay\n\
    \    predicate: increases\n    object: double-cysteine-channel-activity\n    mechanism:\
    \ DTT restores detected MscS openings in the double-mutant preparation where nonreducing\n\
    \      control pressures above the MscL threshold fail to open detectable MscS\
    \ channels. The measured electrical\n      response is retained without a direct\
    \ bond-cleavage arrow.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:20978126\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC3013047/\n      snippet: unless DTT\n\
    \      explanation: Figure 6B control and DTT traces show the reversible appearance\
    \ of MscS activity; MscL\n        is retained in the MJF429 background.\n    \
    \  cache_path: evidence/PF00924/koprowski-2011-mscS.txt\n      cache_sha256: 15a5d51b3206a4adcec6c235105c55cd22b6d8b108e7dd06e0849578ccdea4f8\n\
    \  - edge_id: dtt-washout-decreases-double-cysteine-activity\n    subject: dtt-washout-double-cysteine\n\
    \    predicate: decreases\n    object: double-cysteine-channel-activity\n    mechanism:\
    \ Removing DTT after the reducing condition eliminates detected MscS activity\
    \ while MscL\n      openings persist. This reversibility is part of the observed\
    \ assay, not proof of one uniquely identified\n      nonconducting conformation.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:20978126\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3013047/\n\
    \      snippet: Washing out DTT\n      explanation: Figure 6B washout trace and\
    \ caption establish loss of MscS activity after DTT removal.\n        The accompanying\
    \ S-S cartoon remains interpretive.\n      cache_path: evidence/PF00924/koprowski-2011-mscS.txt\n\
    \      cache_sha256: 15a5d51b3206a4adcec6c235105c55cd22b6d8b108e7dd06e0849578ccdea4f8\n\
    - graph_id: mscs-crowding-conditioned-inactivation\n  title: Cytoplasmic Ficoll\
    \ promotes tension-conditioned WT MscS inactivation more than G168D\n  scope:\
    \ Figure 4D/E of the 2014 study, using full-length WT and G168D MscS and pulse-step-pulse\
    \ availability\n    measurements. This is distinct from the 2011 sustained-pressure\
    \ adaptation protocol.\n  context: pB10b expression; Methods name MJF465 and PB113,\
    \ with retained MscL in PB113 used for mutant\n    midpoint calibration, but do\
    \ not assign each Figure 4 patch to one strain. Inside-out bath has 400\n    mM\
    \ sucrose, 200 mM KCl, 50 mM MgCl2, 5 mM CaCl2, 5 mM HEPES at pH 7.4; pipette\
    \ potential 30 mV. Cytoplasmic\n    Ficoll 400 is 5% w/v, n=3 patches per genotype,\
    \ with a 10-second conditioning tension between test\n    pulses.\n  family_mapping:\
    \ G168D changes the reference glycine within P0C0S1 PF00924 residues 114-180.\
    \ The intact\n    channel, membrane and controlled mechanical perturbation are\
    \ the tested system, not isolated beta-domain\n    sufficiency. Full pB10b clone\
    \ sequence is not independently reconstructed.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:83333\n  limitations: Inactivation is operationally measured\
    \ through the decreased channel population available\n    at the second test pulse.\
    \ Tension is required; Ficoll alone is not assigned a sufficient cause. Pressure-to-tension\n\
    \    conversion uses reference midpoints and a constant-curvature assumption.\
    \ Cage compression, salt bridges\n    and specific atomic trajectories are not\
    \ directly observed. Panels A/B use 10% Ficoll and must not\n    be substituted\
    \ for the D/E conditions.\n  nodes:\n  - node_id: wt-ficoll-conditioning-system\n\
    \    label: WT MscS with 5% Ficoll and conditioning tension\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:P0C0S1\n  - node_id: g168d-ficoll-conditioning-replacement\n\
    \    label: G168D replacing WT in the Ficoll-plus-tension assay\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:P0C0S1\n  - node_id: conditioned-inactivated-channel-fraction\n\
    \    label: Channel fraction unavailable at the second test pulse\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: ficoll-with-tension-increases-wt-inactivation\n\
    \    subject: wt-ficoll-conditioning-system\n    predicate: increases\n    object:\
    \ conditioned-inactivated-channel-fraction\n    mechanism: Adding cytoplasmic\
    \ 5% Ficoll increases the unavailable WT fraction under the conditioning-tension\n\
    \      protocol relative to no-Ficoll WT. Crowder and mechanical history form\
    \ a joint context; the initially\n      activatable population remains available\
    \ before conditioning.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:24778428\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC4003192/\n      snippet: greatly increased\n\
    \      explanation: Figure 4D and its caption quantify increased WT inactivation\
    \ at 5% Ficoll. No complete-inactivation\n        claim at every tension is adopted,\
    \ and the separate 10% panel-A example is not substituted for\n        this comparison.\n\
    \      cache_path: evidence/PF00924/rowe-2014-mscS.txt\n      cache_sha256: 40091e7b284047a5ca5f2346ee832ced69f4567144babe2897e4f6d3ed24070b\n\
    \  - edge_id: g168d-decreases-crowding-conditioned-inactivation\n    subject:\
    \ g168d-ficoll-conditioning-replacement\n    predicate: decreases\n    object:\
    \ conditioned-inactivated-channel-fraction\n    mechanism: Under the 5% Ficoll\
    \ and conditioning-tension protocol, G168D retains a larger available\n      channel\
    \ fraction than WT. This is relative resistance to inactivation, not an absolute\
    \ inability\n      to inactivate or proof of cage compression as the sole cause.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:24778428\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4003192/\n\
    \      snippet: remained largely unchanged\n      explanation: Figure 4D/E and\
    \ the associated Results support the mutant-versus-WT comparison at 5%\n     \
    \   Ficoll. No 2011 voltage, buffer or unresolved adaptation-state label is imported\
    \ into this later\n        experiment.\n      cache_path: evidence/PF00924/rowe-2014-mscS.txt\n\
    \      cache_sha256: 40091e7b284047a5ca5f2346ee832ced69f4567144babe2897e4f6d3ed24070b\n\
    curation_events:\n- timestamp: '2026-10-11T08:03:27Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate MscS interface, redox-response\
    \ and crowding-context graphs\n  history_record: history/records/PF00924/2026-10-11T080327Z-codex-781890.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: P0C0S1 mscS/yggB/b2924/JW2891 is a 286-residue K-12 reference, sequence
    version 1, with exact UniProt/InterPro agreement. PF00924 spans 114-180, including
    N117 and G168. The source's structural beta domain is 128-181, with N117 structurally
    in TM3b; neither boundary is an isolated experimental fragment. Complete pTRCMscS/pB10b
    sequences remain unverified.
  target_ids:
  - PF00924
  evidence_ids:
  - identity
  - primary
  - crowding-primary
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: All edges refer to directly measured electrical behavior or test-pulse
    availability in intact channels. Double-mutant rescue does not mean N117K alone
    activates adaptation; redox reversibility does not directly identify bond chemistry
    or a unique closed state. The 2014 Ficoll-plus-tension context is conjunctive,
    with 5% panels D/E kept distinct from the 10% examples and the earlier unresolved
    adaptation state.
  target_ids:
  - PF00924
  evidence_ids:
  - primary
  - native
  - crowding-primary
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Exact clone junctions, temperatures, per-panel 2014 strain assignment,
    some referenced preparation details and independent 2011 replicate counts remain
    unresolved. Raw traces, supplements, simulations, direct structural chemistry,
    other homologs and osmotic-survival contexts are not fully curated. The 2018 N117C/N167C
    lead is a different mutant and is not adopted as N117C/G168C evidence.
  target_ids:
  - PF00924
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf00924-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve MscS state chemistry and expand member-specific contexts
  description: Retrieve complete constructs and patch metadata, inspect independent
    chemistry/state measurements, and curate other homologs or cellular effects only
    with their own controls and domain mapping. Preserve assay-specific buffers, voltages,
    conditioning histories, model uncertainty and a successor retained review.
  target_ids:
  - PF00924
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - crowding-primary
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF00924.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Retrieve complete constructs and patch metadata, inspect independent
    chemistry/state measurements, and curate other homologs or cellular effects only
    with their own controls and domain mapping. Preserve assay-specific buffers, voltages,
    conditioning histories, model uncertainty and a successor retained review.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF00924
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- The 2011 Figures 4/6 and 2014 Figure 4 were visually inspected. Adopted 2014 panels
  D/E use 5% Ficoll; panels A/B use 10%. Methods and relevant Results were read; the
  2011 Discussion expressly limits state separation. Raw traces were not fitted, no
  bond was independently measured and supplements or simulations were not reanalyzed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
