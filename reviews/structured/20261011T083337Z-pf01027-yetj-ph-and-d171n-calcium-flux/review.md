# Scoped scientific self-review of YetJ pH and D171N transport effects

- Review: 20261011T083337Z-pf01027-yetj-ph-and-d171n-calcium-flux
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T08:33:19Z
- Finished UTC: 2026-10-11T08:33:37Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

One MECHANISTIC graph retains two DIRECT OBSERVED decreases in calcium influx for lower pH and D171N in the 2020 proteoliposome assay. Missing supplementary methods, prior pH-optimum differences and alternative mutant explanations are explicit. Neither purified-protein sufficiency nor observed pore/protonation microsteps are claimed. Partial coverage; IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01027 Bax1-I family, the next accession-ordered SEEDED family, using the BsYetJ transport comparisons in the 2020 primary paper.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01027 | data/families/PF01027.yaml | generated | PF01027 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01027 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01027.

B. subtilis 168 reference O31539 calJ/yetJ/BSU07200 has 214 residues, sequence version 1, exact UniProt/InterPro sequence agreement and PF01027 at 10-210. D171 matches and lies within the profile. Native reference identity does not prove the exact experimental clone, tag, background substitutions or 2019 Delta5-to-2020 construct equivalence.

### Directed effects and limits

graph: supported. Targets: PF01027.

The two edges describe measured transport changes under matched panel comparisons, not a resolved proton sensor, salt bridge or structural trajectory. No empty-liposome control is displayed in panel C, so there is no purified-protein sufficiency edge. Mutation can affect folding, assembly or incorporation, and the earlier pH optimum differs. Bacterial calcium flux does not demonstrate human apoptosis regulation.

### Remaining family coverage

completeness: concern. Targets: PF01027.

Exact lipids, protein/lipid ratio, buffers, calcium and dye doses, temperature, time window, clone and tag remain unverified because supplementary methods were inaccessible. Raw kinetics and additional controls were not reanalyzed. Earlier 2014/2019 and later ER-like lipid experiments and other family members need their own full primary inspection and mapping.

## Findings

### additional-contexts: Retrieve YetJ transport methods and resolve lipid-dependent mechanism coverage

minor / open / confirmed; issue key: pf01027-causal-context-coverage.

Obtain supplementary methods and controls, establish exact experimental constructs, and compare primary transport results across lipid environments before extending causal microsteps or a universal pH rule. Retain alternative mutant explanations and append a successor review.

## Recommended Actions And Acceptance Checks

### extend-contexts

Obtain supplementary methods and controls, establish exact experimental constructs, and compare primary transport results across lipid environments before extending causal microsteps or a universal pH rule. Retain alternative mutant explanations and append a successor review.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC7720206/; Main D171 and calcium-flux Results, gradient and mechanism Discussion; Figure 5C visually inspected | supports | Fura-2-loaded proteoliposomes receive external calcium. Figure 5C WT influx decreases at pH 7/6 relative to 8 and D171N lowers influx across tested pHs, with SEM and n=3. Nanodisc DEER, simulated protonation and proposed gating transitions are separate evidence contexts. Exact supplementary assay and construct metadata remain inaccessible. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/O31539/entry/pfam/PF01027/; Accession and domain locations; paired UniProt identity facts | supports | B. subtilis 168 reference O31539 calJ/yetJ/BSU07200 has 214 residues, sequence version 1, exact UniProt/InterPro sequence agreement and PF01027 at 10-210. D171 matches and lies within the profile. Native reference identity does not prove the exact experimental clone, tag, background substitutions or 2019 Delta5-to-2020 construct equivalence. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01027 | data/families/PF01027.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Main Figure 5 was visually inspected, adopting only panel C transport effects. Main Results and relevant Discussion were read. Supplementary PDF routes returned HTML/403 and Europe PMC reported the article outside its open-access subset; no supplementary methods, raw traces or model trajectories were inspected.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T083337Z-pf01027-yetj-ph-and-d171n-calcium-flux
title: Scoped scientific self-review of YetJ pH and D171N transport effects
started_at: '2026-10-11T08:33:19Z'
finished_at: '2026-10-11T08:33:37Z'
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
summary: One MECHANISTIC graph retains two DIRECT OBSERVED decreases in calcium influx
  for lower pH and D171N in the 2020 proteoliposome assay. Missing supplementary methods,
  prior pH-optimum differences and alternative mutant explanations are explicit. Neither
  purified-protein sufficiency nor observed pore/protonation microsteps are claimed.
  Partial coverage; IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01027.yaml
    sha256: 092eb8be268fc5c480c8e494f4991cc5eec1b73af9b3c10e37dc33c928d5cc01
    role: context
  - path: data/families/PF01027.yaml
    sha256: e558316378e05c38e32487f8c21cb7c76cc5506165ef4af38c98f510a337e584
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
  - path: evidence/PF01027/li-2020-yetJ.txt
    role: context
    sha256: eb2e3233cc841859aef0658949174019555913af0f06de0487dad3e5b8e1117d
  - path: evidence/PF01027/YetJ-identity.txt
    role: context
    sha256: 694701f85ca5158a48c472df972885915437d1e51559f4642ccf253a0ab23590
targets:
- target_id: PF01027
  path: data/families/PF01027.yaml
  label: PF01027
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01027.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 5f1b8823032e7460f6e614c6eb4760810f592228c0cb5334624689eb38643a10
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01027 Bax1-I family, the next accession-ordered SEEDED family, using
    the BsYetJ transport comparisons in the 2020 primary paper.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01027
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Exact lipids, protein/lipid ratio, buffers, calcium and dye doses, temperature,
      time window, clone and tag remain unverified because supplementary methods were
      inaccessible. Raw kinetics and additional controls were not reanalyzed. Earlier
      2014/2019 and later ER-like lipid experiments and other family members need
      their own full primary inspection and mapping.
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
  - PF01027
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7720206/
  locator: Main D171 and calcium-flux Results, gradient and mechanism Discussion;
    Figure 5C visually inspected
  accessed_at: '2026-10-11T08:33:37Z'
  support: supports
  snapshot_sha256: eb2e3233cc841859aef0658949174019555913af0f06de0487dad3e5b8e1117d
  summary: Fura-2-loaded proteoliposomes receive external calcium. Figure 5C WT influx
    decreases at pH 7/6 relative to 8 and D171N lowers influx across tested pHs, with
    SEM and n=3. Nanodisc DEER, simulated protonation and proposed gating transitions
    are separate evidence contexts. Exact supplementary assay and construct metadata
    remain inaccessible.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/O31539/entry/pfam/PF01027/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T08:33:37Z'
  support: supports
  snapshot_sha256: 694701f85ca5158a48c472df972885915437d1e51559f4642ccf253a0ab23590
  summary: B. subtilis 168 reference O31539 calJ/yetJ/BSU07200 has 214 residues, sequence
    version 1, exact UniProt/InterPro sequence agreement and PF01027 at 10-210. D171
    matches and lies within the profile. Native reference identity does not prove
    the exact experimental clone, tag, background substitutions or 2019 Delta5-to-2020
    construct equivalence.
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T08:33:37Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01027
  kind: record_content
  reference: data/families/PF01027.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T08:33:37Z'
  support: context_only
  snapshot_sha256: e558316378e05c38e32487f8c21cb7c76cc5506165ef4af38c98f510a337e584
  quote: "id: Pfam:PF01027\npfam_id: PF01027\nname: Inhibitor of apoptosis-promoting\
    \ Bax1\nshort_name: Bax1-I\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01027\n\
    counters:\n  proteins: 27980\n  matches: 28281\n  proteomes: 13018\n  taxa: 23036\n\
    \  structures: 9\n  alphafold_models: 21884\n  domain_architectures: 248\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR006214\ndescription: Programmed cell-death involves a\
    \ set of Bcl-2 family proteins, some of which inhibit apoptosis\n  (Bcl-2 and\
    \ Bcl-XL) and some of which promote it (Bax and Bak). Human Bax inhibitor, BI-1,\
    \ is an evolutionarily\n  conserved integral membrane protein containing multiple\
    \ membrane-spanning segments predominantly localised\n  to intracellular membranes.\
    \ It has 6-7 membrane-spanning domains. The C termini of the mammalian BI-1\n\
    \  proteins are comprised of basic amino acids resembling some nuclear targeting\
    \ sequences, but otherwise\n  the predicted proteins lack motifs that suggest\
    \ a function. As plant BI-1 appears to localise predominantly\n  to the ER, we\
    \ hypothesised that plant BI-1 could also regulate cell death triggered by ER\
    \ stress [[cite:PUB00053809]].\n  BI-1 appears to exert its effect through an\
    \ interaction with calmodulin [[cite:PUB00053810]]. The budding\n  yeast member\
    \ of this family has been found unexpectedly to encode a BH3 domain-containing\
    \ protein (Ybh3p)\n  that regulates the mitochondrial pathway of apoptosis in\
    \ a phylogenetically conserved manner [[cite:PUB00110294]].\n  Examination of\
    \ the crystal structure of a bacterial member of this family shows that these\
    \ proteins\n  mediate a calcium leak across the membrane that is pH-dependent.\
    \ Calcium homoeostasis balances passive\n  calcium leak with active calcium uptake.\
    \ The structure exists in a pore-closed and pore-open conformation,\n  at pHs\
    \ of 8 and 6 respectively, and the pore can be opened by intracrystalline transition;\
    \ together\n  these findings suggest that pH controls the conformational transition\
    \ [[cite:PUB00095242]].\ncuration_history: history/records/PF01027\ndiscussions:\n\
    - discussion_id: yetj-assay-metadata-and-lipid-dependent-gating\n  prompt: Resolve\
    \ supplementary transport conditions and compare YetJ mechanisms across lipid\
    \ environments.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: Measured\
    \ pH and D171N effects do not uniquely prove the proposed TM7 transition, D171\
    \ protonation\n    or a universal TMBIM mechanism. Main text explicitly notes\
    \ a different pH optimum in the earlier study.\n  evidence:\n  - reference: PMID:33208533\n\
    \    supports: PARTIAL\n    evidence_source: selected_full_text\n    explanation:\
    \ Main Results, Discussion and Figure 5C support two transport effects, but exact\
    \ lipids,\n      doses and construct metadata remain in inaccessible supplementary\
    \ methods. Model-based explanations\n      are not adopted as observed edges.\n\
    \  posed_by: Codex\n  posed_date: '2026-10-11'\n  notes: Obtain SI methods and\
    \ controls, complete clone sequence and raw kinetics. Earlier 2014/2019 studies\n\
    \    and the 2023 ER-like-lipid study are follow-up leads, not fully curated independent\
    \ contexts. Keep\n    bacterial calcium flux separate from human apoptosis and\
    \ isolated-domain sufficiency. Partial same-agent\n    scientific review; remain\
    \ IN_PROGRESS.\ncausal_graphs:\n- graph_id: yetj-ph-and-d171n-calcium-flux\n \
    \ title: Lower pH and D171N reduce calcium influx in the 2020 BsYetJ proteoliposomes\n\
    \  scope: BsYetJ-containing proteoliposomes in the 2020 Figure 5C transport assay.\
    \ The separate nanodisc\n    DEER experiments and human Bax-inhibitor phenotypes\
    \ are not this causal system.\n  context: Fura-2-preloaded proteoliposomes receive\
    \ externally added calcium. Figure 5C compares WT and\n    D171N at pH 6, 7 and\
    \ 8; influx is reported in nM/min with SEM and n=3. Exact lipids, protein/lipid\n\
    \    ratio, calcium and dye doses, buffers, temperature, time window and tag are\
    \ in uninspected supplementary\n    methods and remain unresolved.\n  family_mapping:\
    \ B. subtilis 168 reference UniProtKB:O31539, current calJ alias yetJ, BSU07200,\
    \ has 214\n    residues and sequence version 1; exact UniProt/InterPro sequence\
    \ agreement. PF01027 spans 10-210 inclusive\n    and contains D171. Complete experimental\
    \ clone, background substitutions and tag are not independently\n    verified;\
    \ a 2019 Delta5 crystallographic construct is not transferred to this assay.\n\
    \  scope_status: MECHANISTIC\n  taxon: NCBITaxon:1423\n  limitations: Directness\
    \ refers to the measured membrane calcium-flux endpoint, not observed D171 protonation,\n\
    \    salt-bridge disruption or pore motion. The earlier study's pH-7 optimum differs\
    \ from the pH-8 maximum\n    here; no universal pH rule is inferred. Panel C does\
    \ not display an empty-liposome control, so no\n    purified-protein sufficiency\
    \ edge is added. Mutation can affect assembly or incorporation as well\n    as\
    \ gating. Exact supplementary methods and raw traces remain uninspected.\n  nodes:\n\
    \  - node_id: lower-ph-in-wt-proteoliposomes\n    label: WT proteoliposome assay\
    \ at pH 6 or 7 compared with pH 8\n    node_type: PERTURBATION\n  - node_id: d171n-in-proteoliposomes\n\
    \    label: D171N compared with WT at the same tested pH\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:O31539\n  - node_id: calcium-influx-rate\n  \
    \  label: Fura-2-reported calcium influx into proteoliposomes\n    node_type:\
    \ ACTIVITY\n  edges:\n  - edge_id: lower-ph-decreases-wt-calcium-influx\n    subject:\
    \ lower-ph-in-wt-proteoliposomes\n    predicate: decreases\n    object: calcium-influx-rate\n\
    \    mechanism: Under externally supplied calcium, WT proteoliposomes show lower\
    \ influx at pH 7 and 6 than\n      at pH 8. This is a condition-dependent transport\
    \ effect, not proof that a particular residue senses\n      protons or that the\
    \ same optimum holds in other lipids.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:33208533\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7720206/\n      snippet:\
    \ decrease substantially with decreasing pH\n      explanation: Figure 5C WT bars\
    \ and calcium-flux Results show the ordered pH dependence. The extract\n     \
    \   records this assay's measured transport endpoint and limits; no particular\
    \ protonation mechanism\n        is directly demonstrated.\n      cache_path:\
    \ evidence/PF01027/li-2020-yetJ.txt\n      cache_sha256: eb2e3233cc841859aef0658949174019555913af0f06de0487dad3e5b8e1117d\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/O31539/entry/pfam/PF01027/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/O31539/entry/pfam/PF01027/\n\
    \      snippet: 'O31539 Pfam:PF01027 interval: 10-210, inclusive'\n      explanation:\
    \ Verifies family membership of the BsYetJ reference, not a universal Bax-inhibition\n\
    \        mechanism or the exact experimental clone.\n      cache_path: evidence/PF01027/YetJ-identity.txt\n\
    \      cache_sha256: 694701f85ca5158a48c472df972885915437d1e51559f4642ccf253a0ab23590\n\
    \  - edge_id: d171n-decreases-calcium-influx\n    subject: d171n-in-proteoliposomes\n\
    \    predicate: decreases\n    object: calcium-influx-rate\n    mechanism: D171N\
    \ has markedly reduced influx relative to WT at each tested pH in the same Figure\
    \ 5C\n      comparison. The endpoint establishes a substitution effect without\
    \ resolving whether altered ion\n      recognition, gating, folding or incorporation\
    \ explains the loss.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:33208533\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC7720206/\n      snippet: largely impaired\
    \ within the pH range studied\n      explanation: Figure 5C compares WT and D171N\
    \ at pH 6/7/8. The distinct D171N-10/184 DEER experiment\n        and earlier\
    \ D171E substitution are not used as interchangeable transport constructs or observed\n\
    \        protonation events.\n      cache_path: evidence/PF01027/li-2020-yetJ.txt\n\
    \      cache_sha256: eb2e3233cc841859aef0658949174019555913af0f06de0487dad3e5b8e1117d\n\
    curation_events:\n- timestamp: '2026-10-11T08:27:31Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate two observed YetJ proteoliposome\
    \ calcium-flux effects\n  history_record: history/records/PF01027/2026-10-11T082731Z-codex-e918dc.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: B. subtilis 168 reference O31539 calJ/yetJ/BSU07200 has 214 residues, sequence
    version 1, exact UniProt/InterPro sequence agreement and PF01027 at 10-210. D171
    matches and lies within the profile. Native reference identity does not prove
    the exact experimental clone, tag, background substitutions or 2019 Delta5-to-2020
    construct equivalence.
  target_ids:
  - PF01027
  evidence_ids:
  - identity
  - primary
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: The two edges describe measured transport changes under matched panel comparisons,
    not a resolved proton sensor, salt bridge or structural trajectory. No empty-liposome
    control is displayed in panel C, so there is no purified-protein sufficiency edge.
    Mutation can affect folding, assembly or incorporation, and the earlier pH optimum
    differs. Bacterial calcium flux does not demonstrate human apoptosis regulation.
  target_ids:
  - PF01027
  evidence_ids:
  - primary
  - native
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Exact lipids, protein/lipid ratio, buffers, calcium and dye doses, temperature,
    time window, clone and tag remain unverified because supplementary methods were
    inaccessible. Raw kinetics and additional controls were not reanalyzed. Earlier
    2014/2019 and later ER-like lipid experiments and other family members need their
    own full primary inspection and mapping.
  target_ids:
  - PF01027
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01027-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Retrieve YetJ transport methods and resolve lipid-dependent mechanism coverage
  description: Obtain supplementary methods and controls, establish exact experimental
    constructs, and compare primary transport results across lipid environments before
    extending causal microsteps or a universal pH rule. Retain alternative mutant
    explanations and append a successor review.
  target_ids:
  - PF01027
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01027.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Obtain supplementary methods and controls, establish exact experimental
    constructs, and compare primary transport results across lipid environments before
    extending causal microsteps or a universal pH rule. Retain alternative mutant
    explanations and append a successor review.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01027
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Main Figure 5 was visually inspected, adopting only panel C transport effects. Main
  Results and relevant Discussion were read. Supplementary PDF routes returned HTML/403
  and Europe PMC reported the article outside its open-access subset; no supplementary
  methods, raw traces or model trajectories were inspected.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
