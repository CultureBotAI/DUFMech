# PF01972 assay observation separated from predicted SDH chemistry

- Review: 20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-14T20:49:46Z
- Finished UTC: 2026-10-14T20:52:29Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Partial scientific review of two one-edge graphs: a reported Mm2878 casein-reporter response and a separately labeled computational SDH-catalysis hypothesis. Assay controls, historical construct identity, residue-level chemistry and additional family coverage remain unresolved. IN_PROGRESS is retained.

## Scope And Provenance

Assess the thesis assay Methods and original Figure24, the founding computational paper text, current locus/Pfam mapping, and RCSB structural leads. Review edge direction, attribution, evidence class, source preservation and exclusions.

Selection: Next ascending uncurated accession PF01972 after PF01970, within the unchanged 8296-family corpus goal.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2da6c366b06615fbb6c34379318771fe09f4cfda.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01972 | data/families/PF01972.yaml | generated | PF01972 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Projection, overlay and frozen-field preservation | passed | True | PF01972 | validate_record passed; graphs/discussions equal the overlay; all prior imported fields are unchanged; two one-edge graphs have the intended support and scope labels. |
| Focused graph and QC regression suite | passed | True | PF01972 | 52 passed in27.73s; structural verification is not proof of biological causality. |

## Scientific And Domain Assessments

### Member mapping and domain boundaries

identity: supported. Targets: PF01972.

Reference identity and profile interval support family relevance; the record explicitly withholds exact-clone verification and cross-family transfer.

### Observation versus mechanistic hypothesis

graph: supported. Targets: PF01972.

One PHENOTYPIC/OBSERVED edge captures an assay response and one HYPOTHETICAL edge captures the published computational proposal. Both directness values are UNRESOLVED. No observed SDH catalytic microstep, natural substrate or phage-defense effect is asserted.

### Unresolved experiments and broader family coverage

completeness: concern. Targets: PF01972.

Historical construct/purity, controls, replication, products, residue mapping and additional member mechanisms remain open; a sparse graph is not a completed family review.

## Findings

### context-coverage: Resolve assay attribution and extend mapped member mechanisms

minor / open / confirmed; issue key: pf01972-causal-context-coverage.

Recover historical Mm2878 construct/purification and discriminating controls/products; test the proposed triad and examine additional members. Resolve44FH/44FI sequence mapping and primary experiments before assigning defense edges. Missing source access is not negative biological evidence.

## Recommended Actions And Acceptance Checks

### extend-contexts

Investigate the retained attribution and coverage gaps, preserving experimental/hypothetical distinctions and appending a successor review.

- New edges identify the actual tested member, context and relation-supporting experiment.
- Reporter controls, direct products and exact construct identity are not inferred from names or models.
- Current native checks pass; IN_PROGRESS remains until the wider scientific scope is actually resolved.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| thesis | https://publikationen.uni-tuebingen.de/xmlui/handle/10900/49675; Ammelburg2011 pp.90-91 and94; original Figure24 image | supports | Mm2878 is the arcClpP comparator; the reported reporter response is retained without assigning direct purified-enzyme chemistry or inventing unshown controls. |
| prediction | https://doi.org/10.3233/ISB-00157; Pandit/Srinivasan2004 Methods and catalytic-geometry discussion, Conclusions p.570 | supports | Sequence/fold analysis motivates an SDH mechanism hypothesis, not a residue-mutant or catalytic assay. Original alignment-image validation remains open. |
| mapping | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01972/protein/uniprot/Q8PT40/; Member-specific match plus UniProt MM_2878 query, sequence1/entry106 | supports | Q8PT40 is243aa, reference taxon192952, with PF01972 at2-241. Species/locus mapping is verified, but not the exact historical clone; taxon identifies the mapped reference strain. |
| coverage | evidence/PF01972/coverage-and-exclusions.txt; Bounded alias/member searches, PH1510 complete Pfam list,44FH entity API and44FI entry metadata | context_only | PH1510 belongs to different Pfam domains; MjMPM is DUF2121. Structural leads lack verified PF01972 construct mapping and inspected functional experiments. Local absence search included ignored/hidden files in the stated curation/evidence/history/review/inventory directories. |
| native | src/dufmech/records.py; Current projection validation, overlay equivalence and HEAD imported-field comparison | supports | Current native graph/evidence/history checks pass; all imported metadata remain unchanged. Graph/QC regression suite52passed. These checks do not promote scientific status. |
| duf-projection-pf01972 | data/families/PF01972.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Same-agent partial scientific review, not independent expert approval, raw-data reanalysis or experimental replication.
- Thesis original Figure24 inspected; the2004 alignment image and2026 functional experiments were not inspected. The scope is documented rather than silently treated as exhaustive.
- Full publication QC and canonical Pages source-pin refresh are not claimed. The record remains IN_PROGRESS and the8296-family goal remains active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T205229Z-pf01972-mm2878-assay-and-sdh-hypothesis
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 2da6c366b06615fbb6c34379318771fe09f4cfda
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01972.yaml
    sha256: 9c0fa29bdb7cb5678deaec4e25fcf62b31cda52076f9493d5dc65d67089c8262
    role: context
  - path: data/families/PF01972.yaml
    sha256: 6378f7d506ec5ec08b6878c1b8bb7f4445428688a816968394f186d88f277161
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
  - path: evidence/PF01972/ammelburg-2011-casein.txt
    role: context
    sha256: 37e12d65ba5695e667e9c08bbb231cf2de389925112f2f95f5b1e031b510d856
  - path: evidence/PF01972/coverage-and-exclusions.txt
    role: context
    sha256: ed3e8a17b0feba6bacdd3d3affa0e00d6962fc321edeba5c3d02bbc9e57d9eb3
  - path: evidence/PF01972/member-mapping.txt
    role: context
    sha256: 9c81e76b1590a5b3c25336a41aba9bdaf3ec5fd74036370a5ea3c19cf04dfbe2
  - path: evidence/PF01972/pandit-2004-prediction.txt
    role: context
    sha256: 9a52c87650b016af7f97fd3ffc98ea0874c394470cfd0785da3fc38e50413c49
targets:
- target_id: PF01972
  path: data/families/PF01972.yaml
  label: PF01972
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01972.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 24faf6f67f7cf3f7646966e2e6d756868e9476c6ef3d8b0203081b9edf72c1d7
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
title: PF01972 assay observation separated from predicted SDH chemistry
started_at: '2026-10-14T20:49:46Z'
finished_at: '2026-10-14T20:52:29Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: The same agent researched and curated these graphs; no independent
    expert approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: true
summary: 'Partial scientific review of two one-edge graphs: a reported Mm2878 casein-reporter
  response and a separately labeled computational SDH-catalysis hypothesis. Assay
  controls, historical construct identity, residue-level chemistry and additional
  family coverage remain unresolved. IN_PROGRESS is retained.'
scope:
  description: Assess the thesis assay Methods and original Figure24, the founding
    computational paper text, current locus/Pfam mapping, and RCSB structural leads.
    Review edge direction, attribution, evidence class, source preservation and exclusions.
  selection: Next ascending uncurated accession PF01972 after PF01970, within the
    unchanged 8296-family corpus goal.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01972
  exclusions:
  - target: Unverified Mm2878 clone, missing assay controls and additional member
      mechanisms
    reason: Reference mapping does not establish exact historical preparation identity
      or isolated-domain catalysis. Additional primary experiments remain necessary.
  - target: Original2004 alignment image and2026 structural defense experiments
    reason: The text was accessible but the alignment image was not inspectable; no
      residue-number assignment is claimed. Deposition metadata and an unpublished
      title are not causal experiments.
  - target: Canonical Pages publication and exhaustive corpus review
    reason: This local curation does not publish new source pins or resolve the remaining
      corpus and earlier open follow-ups.
checks:
- check_id: native-projection
  name: Projection, overlay and frozen-field preservation
  command: PYTHONPATH=src .venv/bin/python /private/tmp/duf-pf01972-review.py
  status: passed
  required: true
  exit_code: 0
  summary: validate_record passed; graphs/discussions equal the overlay; all prior
    imported fields are unchanged; two one-edge graphs have the intended support and
    scope labels.
  target_ids:
  - PF01972
  evidence_ids:
  - native
- check_id: graph-regressions
  name: Focused graph and QC regression suite
  command: PYTHONPATH=src:/private/tmp/dufmech-protein-claw/src .venv/bin/python -m
    pytest -q tests/test_causal_graphs.py tests/test_qc.py
  status: passed
  required: true
  exit_code: 0
  summary: 52 passed in27.73s; structural verification is not proof of biological
    causality.
  target_ids:
  - PF01972
  evidence_ids:
  - native
evidence:
- evidence_id: thesis
  kind: primary_source
  reference: https://publikationen.uni-tuebingen.de/xmlui/handle/10900/49675
  locator: Ammelburg2011 pp.90-91 and94; original Figure24 image
  accessed_at: '2026-10-14T20:52:29Z'
  support: supports
  summary: Mm2878 is the arcClpP comparator; the reported reporter response is retained
    without assigning direct purified-enzyme chemistry or inventing unshown controls.
  snapshot_sha256: 37e12d65ba5695e667e9c08bbb231cf2de389925112f2f95f5b1e031b510d856
- evidence_id: prediction
  kind: primary_source
  reference: https://doi.org/10.3233/ISB-00157
  locator: Pandit/Srinivasan2004 Methods and catalytic-geometry discussion, Conclusions
    p.570
  accessed_at: '2026-10-14T20:52:29Z'
  support: supports
  summary: Sequence/fold analysis motivates an SDH mechanism hypothesis, not a residue-mutant
    or catalytic assay. Original alignment-image validation remains open.
  snapshot_sha256: 9a52c87650b016af7f97fd3ffc98ea0874c394470cfd0785da3fc38e50413c49
- evidence_id: mapping
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01972/protein/uniprot/Q8PT40/
  locator: Member-specific match plus UniProt MM_2878 query, sequence1/entry106
  accessed_at: '2026-10-14T20:52:29Z'
  support: supports
  summary: Q8PT40 is243aa, reference taxon192952, with PF01972 at2-241. Species/locus
    mapping is verified, but not the exact historical clone; taxon identifies the
    mapped reference strain.
  snapshot_sha256: 9c81e76b1590a5b3c25336a41aba9bdaf3ec5fd74036370a5ea3c19cf04dfbe2
- evidence_id: coverage
  kind: search
  search_scope: Web searches for PF01972, DUF114, SDH_protease, MJ0137, Mm2878/MM_2878,
    Q8PT40 and the exact2026 deposition study title; UniProt PH1510 query and RCSB44FH/44FI
    metadata. Local rg --no-ignore --hidden searched curation, evidence, history/records,
    reviews/structured and reports/causal_graphs. Not an exhaustive literature census;
    original2004 alignment image and2026 experimental text were not inspectable.
  reference: evidence/PF01972/coverage-and-exclusions.txt
  locator: Bounded alias/member searches, PH1510 complete Pfam list,44FH entity API
    and44FI entry metadata
  accessed_at: '2026-10-14T20:52:29Z'
  support: context_only
  summary: PH1510 belongs to different Pfam domains; MjMPM is DUF2121. Structural
    leads lack verified PF01972 construct mapping and inspected functional experiments.
    Local absence search included ignored/hidden files in the stated curation/evidence/history/review/inventory
    directories.
  snapshot_sha256: ed3e8a17b0feba6bacdd3d3affa0e00d6962fc321edeba5c3d02bbc9e57d9eb3
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation, overlay equivalence and HEAD imported-field
    comparison
  accessed_at: '2026-10-14T20:52:29Z'
  support: supports
  summary: Current native graph/evidence/history checks pass; all imported metadata
    remain unchanged. Graph/QC regression suite52passed. These checks do not promote
    scientific status.
- evidence_id: duf-projection-pf01972
  kind: record_content
  reference: data/families/PF01972.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-14T20:52:29Z'
  support: context_only
  snapshot_sha256: 6378f7d506ec5ec08b6878c1b8bb7f4445428688a816968394f186d88f277161
  quote: "id: Pfam:PF01972\npfam_id: PF01972\nname: ClpP-like SDH-type serine proteinase\n\
    short_name: SDH_protease\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01972\n\
    counters:\n  proteins: 1120\n  matches: 1122\n  proteomes: 1017\n  taxa: 2604\n\
    \  structures: 0\n  alphafold_models: 812\n  domain_architectures: 2\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002825\ndescription: This family of archaebacterial proteins,\
    \ formerly known as DUF114, has been found to be a\n  serine proteinase distantly\
    \ related to ClpP proteinases that belong to the serine proteinase superfamily.\n\
    \  The family has a catalytic triad of Ser, Asp, His residues in a linear sequential\
    \ arrangement (SDH),\n  which shows an altered residue ordering compared with\
    \ the classical ClpP proteinases (SHD) but similar\n  to that of the carboxypeptidase\
    \ clan [[cite:PUB00053691]].\ncuration_history: history/records/PF01972\ndiscussions:\n\
    - discussion_id: mm2878-assay-attribution\n  prompt: Verify the historical Mm2878\
    \ preparation and distinguish reporter response from direct enzyme\n    chemistry.\n\
    \  kind: CURATION_TODO\n  status: OPEN\n  rationale: The thesis comparator is\
    \ relevant to PF01972, but the displayed assay does not isolate catalytic\n  \
    \  attribution or identify cleavage products.\n  evidence:\n  - reference: https://publikationen.uni-tuebingen.de/xmlui/handle/10900/49675\n\
    \    supports: PARTIAL\n    evidence_source: primary_doctoral_thesis\n    explanation:\
    \ Pages 90-91 and original Figure24 on page94 were inspected. MjMPM purification\
    \ must not\n      be relabeled as Mm2878 purification; blank, inactive-enzyme\
    \ and replication information are unresolved.\n  - reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01972/protein/uniprot/Q8PT40/\n\
    \    supports: SUPPORT\n    evidence_source: database\n    explanation: Current\
    \ Q8PT40/MM_2878 maps PF01972 at2-241 in a243-residue reference. The historical\n\
    \      clone is not sequence-verified.\n  posed_by: Codex\n  posed_date: '2026-10-14'\n\
    \  notes: Seek preparation/construct records, matched controls, products and independent\
    \ replication. Do\n    not transfer MjMPM/DUF2121 properties or interpret comparator\
    \ bar heights as kinetic superiority.\n- discussion_id: sdh-triad-and-family-transfer\n\
    \  prompt: Test the predicted catalytic arrangement and investigate additional\
    \ mapped PF01972 members.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale:\
    \ A Pfam rename and remote ClpP similarity are not demonstrations of the Ser-Asp-His\
    \ mechanism\n    or a universal physiological substrate.\n  evidence:\n  - reference:\
    \ PMID:15752073\n    supports: PARTIAL\n    evidence_source: primary_computational_publication\n\
    \    explanation: The2004 Methods and Conclusions describe sequence/fold-based\
    \ prediction. No residue-mutagenesis\n      or proteolysis experiment is reported\
    \ there.\n  - reference: https://rest.uniprot.org/uniprotkb/O59179.json\n    supports:\
    \ SUPPORT\n    evidence_source: database\n    explanation: PH1510's current Pfam\
    \ list contains PF25145/PF24961/PF01957, not PF01972. Its S49 naming\n      does\
    \ not authorize cross-family chemistry transfer.\n  posed_by: Codex\n  posed_date:\
    \ '2026-10-14'\n  notes: Original2004 alignment-image verification, historical\
    \ residue mapping, localization, natural\n    substrates and other member assays\
    \ remain open. The imported description stays immutable; the hypothesis\n    graph\
    \ does not endorse its experimental wording.\n- discussion_id: klebsiella-2026-structural-leads\n\
    \  prompt: Resolve the44FH/44FI construct mapping and primary experiments before\
    \ adding defense or proteolysis\n    edges.\n  kind: CURATION_TODO\n  status:\
    \ OPEN\n  rationale: An SDH-labeled structure and unpublished citation title do\
    \ not establish a directed phage-defense\n    mechanism.\n  evidence:\n  - reference:\
    \ doi:10.2210/pdb44FH/pdb\n    supports: PARTIAL\n    evidence_source: primary_structural_deposition\n\
    \    explanation: RCSB entry and entity1 metadata inspected;304-residue Klebsiella\
    \ protein,2.86-A EM structure.\n      The entity response lacks a reference-sequence/Pfam\
    \ annotation.\n  - reference: doi:10.2210/pdb44FI/pdb\n    supports: PARTIAL\n\
    \    evidence_source: primary_structural_deposition\n    explanation: Entry metadata\
    \ describe a3.51-A complex with short hypothetical-protein chains and an\n   \
    \   unpublished citation. Neither binding nor the title demonstrates cleavage\
    \ or infection effects.\n  posed_by: Codex\n  posed_date: '2026-10-14'\n  notes:\
    \ These are research leads, not confirmed PF01972 experimental mechanisms. evidence/PF01972\
    \ coverage\n    notes retain search/access limits. Frozen structures=0 is not\
    \ overwritten.\ncausal_graphs:\n- graph_id: mm2878-casein-reporter-2011\n  title:\
    \ Mm2878 preparation produces a casein-reporter response\n  scope: Methanosarcina\
    \ mazei Mm2878 comparator in Ammelburg2011 Figure24; preparation-level assay,\
    \ not\n    isolated-domain chemistry.\n  context: 25nM preparation,200nM TR-X\
    \ BODIPY-casein,20mM HEPES pH7.5,150mM NaCl,0.5mM TCEP;37C for2h;580/620nm\n \
    \   excitation/emission.\n  family_mapping: UniProt Q8PT40 sequence1/entry106\
    \ identifies MM_2878 in M. mazei Goe1,243aa; current\n    InterPro maps PF01972\
    \ at2-241 inclusive. Species/locus correspondence does not verify the thesis clone\n\
    \    or tags. See evidence/PF01972/member-mapping.txt.\n  taxon: NCBITaxon:192952\n\
    \  scope_status: PHENOTYPIC\n  limitations: No blank, inactive-Mm2878 control,\
    \ replication or error bars are shown in Figure24. The\n    adjacent purification\
    \ protocol concerns MjMPM. Reporter dequenching does not resolve Mm2878-specific\n\
    \    catalysis, contamination, cleavage sites, SDH residues or physiological function.\n\
    \  nodes:\n  - node_id: preparation\n    label: Mm2878 preparation incubated with\
    \ quenched casein reporter\n    node_type: PERTURBATION\n    grounding:\n    -\
    \ UniProtKB:Q8PT40\n  - node_id: fluorescence\n    label: BODIPY-casein fluorescence\
    \ readout\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: preparation-reporter-response\n\
    \    subject: preparation\n    predicate: increases\n    object: fluorescence\n\
    \    mechanism: The thesis reports fluorescence increase during this preparation-level\
    \ assay. The edge\n      records that response, not a demonstrated purified-enzyme\
    \ bond-cleavage mechanism.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: https://publikationen.uni-tuebingen.de/xmlui/handle/10900/49675\n\
    \      source_url: https://publikationen.uni-tuebingen.de/xmlui/bitstream/handle/10900/49675/pdf/Dissertation_Ammelburg.pdf\n\
    \      snippet: Increase of BODIPY fluorescence reflecting Casein cleavage\n \
    \     explanation: Assay Methods p.91 and original Figure24/caption p.94 identify\
    \ Mm2878 as the arcClpP\n        comparator; retain direction only, without inventing\
    \ a matched blank or product assay.\n      cache_path: evidence/PF01972/ammelburg-2011-casein.txt\n\
    \      cache_sha256: 37e12d65ba5695e667e9c08bbb231cf2de389925112f2f95f5b1e031b510d856\n\
    - graph_id: duf114-predicted-sdh-catalysis-2004\n  title: Predicted SDH catalytic\
    \ arrangement may enable proteolysis\n  scope: DUF114 homologs analyzed by Pandit\
    \ and Srinivasan2004; proposed family mechanism, not experimental\n    transfer\
    \ to every PF01972 member.\n  context: Sequence/profile comparisons and fold recognition\
    \ against known ClpP-related structures; no\n    tested residue perturbation or\
    \ biological compartment established.\n  family_mapping: The paper's DUF114 family\
    \ is the current PF01972/IPR002825 identity. Related ClpP and\n    proteaseIV\
    \ sequences are comparison families. Exact historical alignment-to-current residue\
    \ numbering\n    is not asserted.\n  scope_status: HYPOTHETICAL\n  limitations:\
    \ Conserved residues and predicted fold geometry do not prove catalytic necessity\
    \ or sufficiency.\n    No residue numbers, substrate specificity, secretion requirement\
    \ or measured catalytic intermediate\n    is assigned. The Mm2878 reporter assay\
    \ does not validate this atomic mechanism.\n  nodes:\n  - node_id: proposed_arrangement\n\
    \    label: Proposed joint Ser-Asp-His active-site geometry\n    node_type: STATE\n\
    \    grounding:\n    - Pfam:PF01972\n  - node_id: proposed_hydrolysis\n    label:\
    \ Proposed peptide-bond hydrolysis activity\n    node_type: ACTIVITY\n  edges:\n\
    \  - edge_id: predicted-triad-proteolysis\n    subject: proposed_arrangement\n\
    \    predicate: enables\n    object: proposed_hydrolysis\n    mechanism: The authors\
    \ propose that a compatible geometry despite altered His/Asp sequence order could\n\
    \      support serine-proteinase activity. This is a computationally motivated\
    \ causal hypothesis.\n    directness: UNRESOLVED\n    support: HYPOTHESIZED\n\
    \    evidence_kind: COMPUTATIONAL\n    evidence:\n    - reference: PMID:15752073\n\
    \      source_url: https://journals.sagepub.com/doi/pdf/10.3233/ISB-00157\n  \
    \    snippet: probable serine proteinase\n      explanation: Catalytic-geometry\
    \ discussion pp.568-570 and Conclusions p.570; not an experimentally\n       \
    \ determined active site or residue-mutant assay.\n      cache_path: evidence/PF01972/pandit-2004-prediction.txt\n\
    \      cache_sha256: 9a52c87650b016af7f97fd3ffc98ea0874c394470cfd0785da3fc38e50413c49\n\
    curation_events:\n- timestamp: '2026-10-14T20:42:47Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate scoped Mm2878 reporter observation\
    \ and separate DUF114 catalytic hypothesis.\n  history_record: history/records/PF01972/2026-10-14T204247Z-codex-3b40ac.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Member mapping and domain boundaries
  outcome: supported
  target_ids:
  - PF01972
  evidence_ids:
  - mapping
  - coverage
  summary: Reference identity and profile interval support family relevance; the record
    explicitly withholds exact-clone verification and cross-family transfer.
- assessment_id: causal-scope
  area: graph
  topic: Observation versus mechanistic hypothesis
  outcome: supported
  target_ids:
  - PF01972
  evidence_ids:
  - thesis
  - prediction
  - native
  summary: One PHENOTYPIC/OBSERVED edge captures an assay response and one HYPOTHETICAL
    edge captures the published computational proposal. Both directness values are
    UNRESOLVED. No observed SDH catalytic microstep, natural substrate or phage-defense
    effect is asserted.
- assessment_id: coverage
  area: completeness
  topic: Unresolved experiments and broader family coverage
  outcome: concern
  target_ids:
  - PF01972
  evidence_ids:
  - thesis
  - prediction
  - coverage
  summary: Historical construct/purity, controls, replication, products, residue mapping
    and additional member mechanisms remain open; a sparse graph is not a completed
    family review.
findings:
- finding_id: context-coverage
  issue_key: pf01972-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve assay attribution and extend mapped member mechanisms
  description: Recover historical Mm2878 construct/purification and discriminating
    controls/products; test the proposed triad and examine additional members. Resolve44FH/44FI
    sequence mapping and primary experiments before assigning defense edges. Missing
    source access is not negative biological evidence.
  target_ids:
  - PF01972
  field_paths:
  - causal_graphs
  - discussions
  evidence_ids:
  - thesis
  - prediction
  - mapping
  - coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01972.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Investigate the retained attribution and coverage gaps, preserving
    experimental/hypothetical distinctions and appending a successor review.
  finding_ids:
  - context-coverage
  target_ids:
  - PF01972
  ownership_note: Curate overlay/evidence, append canonical history, regenerate native
    projections and retain a successor scientific review.
  acceptance_checks:
  - New edges identify the actual tested member, context and relation-supporting experiment.
  - Reporter controls, direct products and exact construct identity are not inferred
    from names or models.
  - Current native checks pass; IN_PROGRESS remains until the wider scientific scope
    is actually resolved.
limitations:
- Same-agent partial scientific review, not independent expert approval, raw-data
  reanalysis or experimental replication.
- Thesis original Figure24 inspected; the2004 alignment image and2026 functional experiments
  were not inspected. The scope is documented rather than silently treated as exhaustive.
- Full publication QC and canonical Pages source-pin refresh are not claimed. The
  record remains IN_PROGRESS and the8296-family goal remains active.
tags:
- causal-graphs
- pf01972
- scientific-self-review
```
