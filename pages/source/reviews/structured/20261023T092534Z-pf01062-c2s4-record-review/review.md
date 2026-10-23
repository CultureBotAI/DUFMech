# PF01062 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review

- Review: 20261023T092534Z-pf01062-c2s4-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-23T09:25:33Z
- Finished UTC: 2026-10-23T09:25:34Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Five MECHANISTIC graphs retain eight DIRECT OBSERVED effects for bilateral chelation, trans calcium reactivation, DIDS inhibition, three normalized neck-mutant current comparisons and two coupled flux effects. Historical and current sequences match exactly in the tested region despite full-length differences. Conditions, orientation and readout limits remain explicit; partial scientific self-review and IN_PROGRESS. Stage 3 (PR #347) grounded Homo sapiens CaV1.3 (CACNA1D, UniProtKB:Q01668) and CaVbeta4 (CACNB4, UniProtKB:O00305) in best1-proline-motif-variants-shift-cav13-inhibition.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01062 Bestrophin, the next accession-ordered SEEDED family, using purified chicken BEST1 experiments in Vaisey 2016 with the cited 2014 construct/flux method.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base fde7d143a6b952fbc63b390cbfc27de38ac7701b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01062 | data/families/PF01062.yaml | generated | PF01062 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01062 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01062.

Retired E1C3A0 resolves to archived UPI0000E805B4; its 1-405 sequence exactly matches current chicken BEST1 A0A8V0ZZU7, sequence version 1. Five differences occur only after residue 405. PF01062 spans 1-324 and contains all adopted sites. PDB 4RDQ entity 1 exactly equals current 2-405 plus EGEEF; original MS/Edman confirms initiator removal to Thr2. The tested region extends beyond the Pfam profile; every mutant clone was not independently sequenced. Chicken V205 is not human I205.

### Directed effects and limits

graph: supported. Targets: PF01062.

Eight directly observed assay effects retain their exact interventions, joint mutations, voltage, normalization and orientation. Electrical current and ACMA-coupled acidification are not conflated. Calcium half-response is not a binding Kd, DIDS inhibition does not establish a binding site, and mutant retained fractions are not absolute conductance. The clasp-mutant rescue is a joint five-site construct, not independent sufficiency of individual substitutions. KpBest cation behavior and modeled conformational trajectories are not transferred.

### Remaining family coverage

completeness: concern. Targets: PF01062.

Exact mutant clone sequences, flux replicate counts and recording temperature, incorporation controls and raw single-channel behavior remain incomplete. Aperture-selectivity, remaining substitutions, full-length protein, other taxa, later inactivation, cryo-EM and GABA contexts require separate primary assessment. The cited earlier method was read for protocol details, not curated as an independent graph. This is not complete family coverage.

### Cycle 2 causal-graph partner and substrate protein grounding

identity: supported. Targets: PF01062.

Stage 3 (PR #347) grounded Homo sapiens CaV1.3 (CACNA1D, UniProtKB:Q01668) and CaVbeta4 (CACNB4, UniProtKB:O00305) in best1-proline-motif-variants-shift-cav13-inhibition.

## Findings

### additional-contexts: Extend BEST1 mechanism coverage with exact constructs and assay-specific controls

minor / open / confirmed; issue key: pf01062-causal-context-coverage.

Resolve mutant sequences and flux metadata, evaluate remaining permeability and full-length contexts, and inspect later inactivation, structural and GABA studies with their own protein mapping and controls. Preserve orientation, normalized versus absolute current and coupled-readout distinctions; retain a successor scientific review before status promotion.

## Recommended Actions And Acceptance Checks

### extend-contexts

Resolve mutant sequences and flux metadata, evaluate remaining permeability and full-length contexts, and inspect later inactivation, structural and GABA studies with their own protein mapping and controls. Preserve orientation, normalized versus absolute current and coupled-readout distinctions; retain a successor scientific review before status promotion.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC5127342/; Electrical-recording, neck and calcium Results; cloning/reconstitution/electrophysiology/flux Methods; Figures 1/3/4 visually inspected | supports | WT current decreases after bilateral EGTA and is reactivated in a separate trans-perfusion protocol; DIDS inhibits with solvent control. TripleA, F80A and F80N increase the normalized post-EGTA retained fraction. D301A/D304A reduces coupled flux and joint TripleA restores it. This is not direct observation of atomic gate motion, single-channel conductance or an absolute current increase across mutant preparations. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/A0A8V0ZZU7/entry/pfam/PF01062/; Accession and domain locations; paired UniProt identity facts | supports | Retired E1C3A0 resolves to archived UPI0000E805B4; its 1-405 sequence exactly matches current chicken BEST1 A0A8V0ZZU7, sequence version 1. Five differences occur only after residue 405. PF01062 spans 1-324 and contains all adopted sites. PDB 4RDQ entity 1 exactly equals current 2-405 plus EGEEF; original MS/Edman confirms initiator removal to Thr2. The tested region extends beyond the Pfam profile; every mutant clone was not independently sequenced. Chicken V205 is not human I205. |
| original-construct-flux-method | https://pmc.ncbi.nlm.nih.gov/articles/PMC4454446/; Cloning/expression/purification and anion-flux Methods | supports | Establishes EGEEF-tagged construct and MS/Edman-confirmed Thr2 processing, plus the ACMA/CCCP coupled-flux protocol cited by 2016. It does not supply new 2016 empty-control traces or replicate counts. |
| deposited-construct-sequence | https://data.rcsb.org/rest/v1/core/polymer_entity/4RDQ/1; Entity 1 sequence and SIFTS aligned region | supports | The deposited 409-aa sequence exactly matches modern BEST1 2-405 plus EGEEF and maps to A0A8V0ZZU7. Full-length historical identity is not asserted. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| stage4-prior-review | reviews/structured/20261011T090737Z-pf01062-best1-calcium-and-substitution-assays/review.yaml; Predecessor structured review 20261011T090737Z-pf01062-best1-calcium-and-substitution-assays | supports | Predecessor review 20261011T090737Z-pf01062-best1-calcium-and-substitution-assays verified and linked for finding continuity and semantic-digest progression on PF01062. |
| duf-projection-pf01062 | data/families/PF01062.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Vaisey 2016 Figures 1/3/4 were visually inspected and relevant main Methods/Results/Discussion read. Original 2014 construct and flux Methods were inspected. Structural coordinates, full supplemental datasets, raw traces and later primary figures were not independently reviewed. A truncated Discussion tool output was not treated as complete inspection of every sentence.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261023T092534Z-pf01062-c2s4-record-review
title: PF01062 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review
started_at: '2026-10-23T09:25:33Z'
finished_at: '2026-10-23T09:25:34Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Claude-Opus-4.6
  independence: self_review
  independence_basis: Cycle 2 Stage 4 frozen-inventory record review by Antigravity
    auditing prior Codex/Antigravity curation overlays, primary evidence caches, history
    events, and current projections at Git revision fde7d143a6b952fbc63b390cbfc27de38ac7701b.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: true
summary: 'Five MECHANISTIC graphs retain eight DIRECT OBSERVED effects for bilateral
  chelation, trans calcium reactivation, DIDS inhibition, three normalized neck-mutant
  current comparisons and two coupled flux effects. Historical and current sequences
  match exactly in the tested region despite full-length differences. Conditions,
  orientation and readout limits remain explicit; partial scientific self-review and
  IN_PROGRESS. Stage 3 (PR #347) grounded Homo sapiens CaV1.3 (CACNA1D, UniProtKB:Q01668)
  and CaVbeta4 (CACNB4, UniProtKB:O00305) in best1-proline-motif-variants-shift-cav13-inhibition.'
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: fde7d143a6b952fbc63b390cbfc27de38ac7701b
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01062.yaml
    sha256: 7a946a11f96996ae09d5d4e8ef1d5dc342fd9bf79015dc60e4d90e316b8715fe
    role: context
  - path: data/families/PF01062.yaml
    sha256: 926cb395039522bef961e9883f8139a966add427bfa2f2d000f4957a7a040402
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
  - path: evidence/PF01062/BEST1-identity.txt
    sha256: 41bc863be952a331935e10eab2083ba61dbfbece35e4feb7a0e602027912b234
    role: context
  - path: evidence/PF01062/dickson-2014-flux-method.txt
    sha256: f19cfc71cfa0e1d30e7f5b2f4ab21b1b38744b42a169016d80dc60932851b8b6
    role: context
  - path: evidence/PF01062/vaisey-2016-best1.txt
    sha256: f446cd14aa5658586dcbc19cc76d553cf6cdd53ea41c0325d4db265b4d072f7c
    role: context
  - path: reviews/structured/20261011T090737Z-pf01062-best1-calcium-and-substitution-assays/review.yaml
    sha256: fb0a0ea442f14ef54eb073085c1f20fa671467d6064fce96a706b1f6afde6e10
    role: context
targets:
- target_id: PF01062
  path: data/families/PF01062.yaml
  label: PF01062
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01062.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 91127236d054e729c3d5012b709f01f8a550c319c18e7f31cd92e3857a1c92d0
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01062 Bestrophin, the next accession-ordered SEEDED family, using purified
    chicken BEST1 experiments in Vaisey 2016 with the cited 2014 construct/flux method.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01062
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Exact mutant clone sequences, flux replicate counts and recording temperature,
      incorporation controls and raw single-channel behavior remain incomplete. Aperture-selectivity,
      remaining substitutions, full-length protein, other taxa, later inactivation,
      cryo-EM and GABA contexts require separate primary assessment. The cited earlier
      method was read for protocol details, not curated as an independent graph. This
      is not complete family coverage.
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
  - PF01062
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5127342/
  locator: Electrical-recording, neck and calcium Results; cloning/reconstitution/electrophysiology/flux
    Methods; Figures 1/3/4 visually inspected
  accessed_at: '2026-10-11T09:07:37Z'
  support: supports
  snapshot_sha256: f446cd14aa5658586dcbc19cc76d553cf6cdd53ea41c0325d4db265b4d072f7c
  summary: WT current decreases after bilateral EGTA and is reactivated in a separate
    trans-perfusion protocol; DIDS inhibits with solvent control. TripleA, F80A and
    F80N increase the normalized post-EGTA retained fraction. D301A/D304A reduces
    coupled flux and joint TripleA restores it. This is not direct observation of
    atomic gate motion, single-channel conductance or an absolute current increase
    across mutant preparations.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/A0A8V0ZZU7/entry/pfam/PF01062/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T09:07:37Z'
  support: supports
  snapshot_sha256: 41bc863be952a331935e10eab2083ba61dbfbece35e4feb7a0e602027912b234
  summary: Retired E1C3A0 resolves to archived UPI0000E805B4; its 1-405 sequence exactly
    matches current chicken BEST1 A0A8V0ZZU7, sequence version 1. Five differences
    occur only after residue 405. PF01062 spans 1-324 and contains all adopted sites.
    PDB 4RDQ entity 1 exactly equals current 2-405 plus EGEEF; original MS/Edman confirms
    initiator removal to Thr2. The tested region extends beyond the Pfam profile;
    every mutant clone was not independently sequenced. Chicken V205 is not human
    I205.
- evidence_id: original-construct-flux-method
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4454446/
  locator: Cloning/expression/purification and anion-flux Methods
  summary: Establishes EGEEF-tagged construct and MS/Edman-confirmed Thr2 processing,
    plus the ACMA/CCCP coupled-flux protocol cited by 2016. It does not supply new
    2016 empty-control traces or replicate counts.
  accessed_at: '2026-10-11T09:07:37Z'
  support: supports
  snapshot_sha256: f19cfc71cfa0e1d30e7f5b2f4ab21b1b38744b42a169016d80dc60932851b8b6
- evidence_id: deposited-construct-sequence
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4RDQ/1
  locator: Entity 1 sequence and SIFTS aligned region
  summary: The deposited 409-aa sequence exactly matches modern BEST1 2-405 plus EGEEF
    and maps to A0A8V0ZZU7. Full-length historical identity is not asserted.
  accessed_at: '2026-10-11T09:07:37Z'
  support: supports
  snapshot_sha256: 41bc863be952a331935e10eab2083ba61dbfbece35e4feb7a0e602027912b234
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T09:07:37Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: stage4-prior-review
  kind: prior_review
  reference: reviews/structured/20261011T090737Z-pf01062-best1-calcium-and-substitution-assays/review.yaml
  locator: Predecessor structured review 20261011T090737Z-pf01062-best1-calcium-and-substitution-assays
  accessed_at: '2026-10-23T09:25:34Z'
  support: supports
  snapshot_sha256: fb0a0ea442f14ef54eb073085c1f20fa671467d6064fce96a706b1f6afde6e10
  summary: Predecessor review 20261011T090737Z-pf01062-best1-calcium-and-substitution-assays
    verified and linked for finding continuity and semantic-digest progression on
    PF01062.
- evidence_id: duf-projection-pf01062
  kind: record_content
  reference: data/families/PF01062.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-23T09:25:34Z'
  support: context_only
  snapshot_sha256: 926cb395039522bef961e9883f8139a966add427bfa2f2d000f4957a7a040402
  quote: "id: Pfam:PF01062\npfam_id: PF01062\nname: Bestrophin, RFP-TM, chloride channel\n\
    short_name: Bestrophin\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01062\n\
    counters:\n  proteins: 8246\n  matches: 8846\n  proteomes: 1318\n  taxa: 4218\n\
    \  structures: 45\n  alphafold_models: 7437\n  domain_architectures: 106\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR021134\ndescription: This entry represents animal bestrophin\
    \ homologues. Bestrophin is a 68-kDa basolateral plasma\n  membrane protein expressed\
    \ in retinal pigment epithelial cells (RPE). It is encoded by the VMD2 gene,\n\
    \  which is mutated in Best macular dystrophy, a disease characterised by a depressed\
    \ light peak in the\n  electrooculogram [[cite:PUB00011865]]. VMD2 encodes a 585-amino\
    \ acid protein with an approximate mass\n  of 68 kDa which has been designated\
    \ bestrophin. Bestrophin shares homology with the Caenorhabditis elegans\n  RFP\
    \ gene family, named for the presence of a conserved arginine (R), phenylalanine\
    \ (F), proline (P),\n  amino acid sequence motif. Bestrophin is a plasma membrane\
    \ protein, localised to the basolateral surface\n  of RPE cells consistent with\
    \ a role for bestrophin in the generation or regulation of the EOG light\n  peak.\
    \ Bestrophin and other RFP family members represent a new class of chloride channels,\
    \ indicating\n  a direct role for bestrophin in generating the light peak [[cite:PUB00011865]].\
    \ The VMD2 gene underlying\n  Best disease was shown to represent the first human\
    \ member of the RFP-TM protein family. More than 97%\n  of the disease-causing\
    \ mutations are located in the N-terminal RFP-TM domain implying important functional\n\
    \  properties [[cite:PUB00011864]]. The bestrophins are four-pass transmembrane\
    \ chloride-channel proteins\n  [[cite:PUB00096747]], and the RFP-TM or bestrophin\
    \ domain extends from the N-terminus through approximately\n  350 amino acids\
    \ and contains all of the TM domains as well as nearly all reported disease causing\
    \ mutations\n  [[cite:PUB00109156]]. Interestingly, the RFP motif is not conserved\
    \ evolutionarily back beyond Metazoa,\n  neither is it in plant members.\ncuration_history:\
    \ history/records/PF01062\ndiscussions:\n- discussion_id: best1-gating-constructs-and-additional-contexts\n\
    \  prompt: Extend BEST1 gating and permeability contexts while preserving construct,\
    \ orientation and assay\n    differences.\n  kind: CURATION_TODO\n  status: OPEN\n\
    \  rationale: Purified current and coupled-flux effects do not directly resolve\
    \ every gating microstep\n    or establish a universal family mechanism. The tested\
    \ truncated region maps exactly despite full-length\n    differences between historical\
    \ and current references.\n  evidence:\n  - reference: PMID:27821745\n    supports:\
    \ PARTIAL\n    evidence_source: selected_full_text\n    explanation: Selected\
    \ primary Methods, Results and Figures 1/3/4 support eight edges. Aperture selectivity,\n\
    \      remaining substitutions and precise single-channel mechanisms need separately\
    \ scoped assessment.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n  notes:\
    \ Resolve exact mutant clones, flux replicate/temperature details and incorporation\
    \ controls. Assess\n    later inactivation (PMID:30237227), cryo-EM gating (PMID:30628889)\
    \ and GABA activation (PMID:40249777)\n    as additional primary contexts, not\
    \ already reviewed edges. Do not transfer KpBest cation selectivity,\n    human\
    \ I205 numbering or structural-model trajectories. Partial same-agent scientific\
    \ review; remain\n    IN_PROGRESS.\ncausal_graphs:\n- graph_id: best1-bilateral-egta-current-loss\n\
    \  title: Bilateral calcium chelation decreases purified chicken BEST1 current\n\
    \  scope: Chicken BEST1 encoded residues 1-405 plus C-terminal EGEEF, expressed\
    \ in Pichia and reconstituted\n    in planar bilayers. Not the full 762-aa protein,\
    \ human retinal cells or bacterial KpBest.\n  context: 2016 Figure 1B-D representative\
    \ same-bilayer comparison. Symmetric 30 mM KCl, 20 mM HEPES-NaOH\n    pH 7.6,\
    \ 0.21 mM EGTA and 0.19 mM CaCl2 initially give about 300 nM free calcium; 3:1\
    \ wt/wt POPE/POPG,\n    22-24 C. Add 10 mM EGTA to both sides. Currents at +100\
    \ mV are averaged over the final 200 ms of a\n    2-s pulse; empty-bilayer currents\
    \ are subtracted.\n  family_mapping: Historical E1C3A0 is deleted, but its archived\
    \ sequence and current A0A8V0ZZU7 match\n    exactly at 1-405; PF01062 spans 1-324\
    \ inclusive. Five full-length differences lie beyond 405. PDB\n    4RDQ entity\
    \ 1 exactly matches current residues 2-405 plus EGEEF, consistent with the cited\
    \ purification's\n    MS/Edman-confirmed Thr2 start. Other mutant clone sequences\
    \ are not independently reconstructed.\n  scope_status: MECHANISTIC\n  taxon:\
    \ NCBITaxon:9031\n  limitations: This is a direct current endpoint after chelation,\
    \ not an observed atomic gate-closing\n    trajectory. Both channel orientations\
    \ are present; bilateral chelation is not interchangeable with\n    one-sided\
    \ treatment. The construct extends beyond the Pfam profile and does not prove\
    \ isolated-domain\n    sufficiency or a universal family calcium threshold.\n\
    \  nodes:\n  - node_id: bilateral-egta-in-wt-bilayer\n    label: Add 10 mM EGTA\
    \ to both sides of the WT BEST1 bilayer\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:A0A8V0ZZU7\n  - node_id: wt-current-at-plus100\n    label: WT\
    \ BEST1 current at +100 mV\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:A0A8V0ZZU7\n\
    \  edges:\n  - edge_id: bilateral-egta-decreases-current\n    subject: bilateral-egta-in-wt-bilayer\n\
    \    predicate: decreases\n    object: wt-current-at-plus100\n    mechanism: Chelating\
    \ calcium on both sides strongly reduces the current under the same bilayer and\n\
    \      voltage conditions. The effect supports calcium-dependent activity without\
    \ directly resolving calcium-binding\n      or neck-motion microsteps.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:27821745\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5127342/\n\
    \      snippet: almost completely abolishes\n      explanation: Figure 1B-D and\
    \ the electrophysiology Methods support the bilateral EGTA comparison.\n     \
    \   These displayed traces are from one representative bilayer, not separate independent\
    \ replicates.\n      cache_path: evidence/PF01062/vaisey-2016-best1.txt\n    \
    \  cache_sha256: f446cd14aa5658586dcbc19cc76d553cf6cdd53ea41c0325d4db265b4d072f7c\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/A0A8V0ZZU7/entry/pfam/PF01062/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/A0A8V0ZZU7/entry/pfam/PF01062/\n\
    \      snippet: 'A0A8V0ZZU7 Pfam:PF01062 interval: 1-324, inclusive'\n      explanation:\
    \ Archived sequence, current mapping and deposited construct agree over the tested\
    \ region;\n        their full-length sequences are not identical. This is identity\
    \ support, not an additional causal\n        experiment.\n      cache_path: evidence/PF01062/BEST1-identity.txt\n\
    \      cache_sha256: 41bc863be952a331935e10eab2083ba61dbfbece35e4feb7a0e602027912b234\n\
    - graph_id: best1-trans-calcium-reactivation\n  title: Trans-side calcium restores\
    \ BEST1 current after orientation-selective silencing\n  scope: Purified tagged\
    \ chicken BEST1 1-405 in the 2016 Figure 1E/F bilayer protocol. The cis-side population\n\
    \    remains silenced during trans perfusion.\n  context: Symmetric 30 mM KCl,\
    \ POPE/POPG 3:1, pH 7.6, 22-24 C. After adding 10 mM EGTA to cis, trans\n    solutions\
    \ use 1 mM EGTA/calcium-EGTA mixtures to vary free calcium from near zero to 350\
    \ nM. Current\n    magnitude at -100 mV is normalized to the 350-nM response.\
    \ Three separate bilayers, SEM; two-second\n    pulses and final 200-ms averaging.\n\
    \  family_mapping: E1C3A0 archived 1-405 matches current A0A8V0ZZU7 exactly; PF01062\
    \ is 1-324. The purified\n    construct includes the EGEEF tag and processing\
    \ to Thr2 established in the cited original method;\n    it is not full-length\
    \ BEST1 or an isolated Pfam fragment.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:9031\n\
    \  limitations: The fitted half-response concentration of 17 +/- 3 nM is assay-specific\
    \ and is not a directly\n    measured calcium-binding Kd. Increasing current magnitude\
    \ at a fixed negative voltage does not imply\n    a universal direction of chloride\
    \ flow. No atomic motion, stoichiometric binding event or human disease\n    mechanism\
    \ is directly tracked.\n  nodes:\n  - node_id: trans-calcium-increase-with-cis-egta\n\
    \    label: Increase trans free calcium while cis remains chelated\n    node_type:\
    \ PERTURBATION\n  - node_id: normalized-current-magnitude-minus100\n    label:\
    \ Normalized BEST1 current magnitude at -100 mV\n    node_type: ACTIVITY\n   \
    \ grounding:\n    - UniProtKB:A0A8V0ZZU7\n  edges:\n  - edge_id: trans-calcium-increases-current-magnitude\n\
    \    subject: trans-calcium-increase-with-cis-egta\n    predicate: increases\n\
    \    object: normalized-current-magnitude-minus100\n    mechanism: Increasing\
    \ free calcium on the trans side restores current magnitude in the accessible\n\
    \      channel orientation, while the cis-facing population remains silenced.\
    \ The normalized electrophysiological\n      response is not an independently\
    \ measured binding isotherm.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:27821745\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5127342/\n      snippet:\
    \ dose-dependent manner\n      explanation: Figure 1E/F and trans-perfusion Methods\
    \ support reactivation with the stated orientation\n        and normalization\
    \ controls.\n      cache_path: evidence/PF01062/vaisey-2016-best1.txt\n      cache_sha256:\
    \ f446cd14aa5658586dcbc19cc76d553cf6cdd53ea41c0325d4db265b4d072f7c\n- graph_id:\
    \ best1-dids-current-inhibition\n  title: DIDS decreases purified BEST1 current\
    \ in the bilayer assay\n  scope: Tagged chicken BEST1 1-405 in the 2016 Figure\
    \ 1I/J planar bilayer experiment, not drug treatment\n    of retinal cells.\n\
    \  context: Standard symmetric 30 mM KCl solutions with about 300 nM free calcium,\
    \ 20 mM HEPES-NaOH pH\n    7.6, POPE/POPG 3:1 and 22-24 C. DIDS is added to both\
    \ sides through 1 mM with one minute mixing. Current\n    magnitude at -100 mV\
    \ is normalized to no DIDS. Three experiments; up to 2% DMSO vehicle does not\
    \ noticeably\n    alter current.\n  family_mapping: The E1C3A0 experimental region\
    \ 1-405 exactly matches A0A8V0ZZU7 and contains PF01062\n    at 1-324. The EGEEF-tagged,\
    \ processed construct is distinguished from the full-length reference and\n  \
    \  other bestrophins.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:9031\n\
    \  limitations: Current inhibition does not identify a DIDS binding site, unique\
    \ gating mechanism or therapeutic\n    effect. Dose-response fits depend on this\
    \ preparation and are not family-wide constants. No precise\n    drug affinity\
    \ is assigned.\n  nodes:\n  - node_id: bilateral-dids-addition\n    label: DIDS\
    \ added to both sides of the calcium-containing BEST1 bilayer\n    node_type:\
    \ PERTURBATION\n  - node_id: dids-normalized-current-magnitude\n    label: BEST1\
    \ current magnitude relative to the no-DIDS condition\n    node_type: ACTIVITY\n\
    \    grounding:\n    - UniProtKB:A0A8V0ZZU7\n  edges:\n  - edge_id: dids-decreases-best1-current\n\
    \    subject: bilateral-dids-addition\n    predicate: decreases\n    object: dids-normalized-current-magnitude\n\
    \    mechanism: DIDS lowers the measured current magnitude in a concentration-dependent\
    \ comparison, with\n      the solvent control retained. No specific molecular\
    \ binding or pore-blocking geometry is directly\n      established.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:27821745\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5127342/\n\
    \      snippet: inhibited by DIDS\n      explanation: Figure 1I/J and DIDS Methods\
    \ support the dose-dependent current decrease and vehicle\n        qualification.\n\
    \      cache_path: evidence/PF01062/vaisey-2016-best1.txt\n      cache_sha256:\
    \ f446cd14aa5658586dcbc19cc76d553cf6cdd53ea41c0325d4db265b4d072f7c\n- graph_id:\
    \ best1-neck-mutations-retained-current\n  title: Neck substitutions increase\
    \ the current fraction retained after calcium chelation\n  scope: Individual F80A/F80N\
    \ and joint I76A/F80A/F84A TripleA constructs of tagged chicken BEST1 1-405,\n\
    \    compared with WT in 2016 Figure 3C.\n  context: Symmetric 30 mM KCl bilayers,\
    \ POPE/POPG 3:1, pH 7.6, 22-24 C, initially about 300 nM free calcium.\n    Add\
    \ 10 mM EGTA to both sides and stir four minutes. Current at +100 mV after chelation\
    \ is normalized\n    to each construct's calcium-present current. Three separate\
    \ bilayers per comparison, SEM.\n  family_mapping: I76, F80 and F84 are verified\
    \ in the identical historical/current 1-405 region of E1C3A0/A0A8V0ZZU7\n    and\
    \ within PF01062 residues 1-324. TripleA is one joint perturbation, not three\
    \ independently sufficient\n    mutations.\n  scope_status: MECHANISTIC\n  taxon:\
    \ NCBITaxon:9031\n  limitations: Normalized retained fraction is not absolute\
    \ current, single-channel conductance or open\n    probability; precise incorporation\
    \ is unknown. F80I is described as nearly WT-like in calcium dependence\n    relative\
    \ to the larger mutant effects and is not assigned an all-or-none independence\
    \ edge. Neck mutations\n    do not substantially switch anion/cation selectivity.\
    \ Structural gate and quadrupole models are interpretations,\n    not directly\
    \ observed trajectories.\n  nodes:\n  - node_id: triplea-neck-substitution\n \
    \   label: Joint I76A/F80A/F84A TripleA instead of WT\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:A0A8V0ZZU7\n  - node_id: f80a-neck-substitution\n\
    \    label: F80A instead of WT\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:A0A8V0ZZU7\n  - node_id: f80n-neck-substitution\n    label: F80N\
    \ instead of WT\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:A0A8V0ZZU7\n\
    \  - node_id: current-fraction-after-egta\n    label: Fraction of calcium-present\
    \ current retained after EGTA\n    node_type: ACTIVITY\n  edges:\n  - edge_id:\
    \ triplea-increases-retained-current-fraction\n    subject: triplea-neck-substitution\n\
    \    predicate: increases\n    object: current-fraction-after-egta\n    mechanism:\
    \ The joint TripleA construct retains nearly all of its calcium-present current\
    \ after chelation,\n      unlike WT. This measures reduced calcium dependence\
    \ without proving each individual substitution\n      independently causes the\
    \ joint phenotype.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:27821745\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC5127342/\n      snippet: fraction of\
    \ current remaining\n      explanation: Figure 3C TripleA versus WT normalized\
    \ fractions, corroborated by Figure 3A/B I-V curves,\n        support the directed\
    \ comparison.\n      cache_path: evidence/PF01062/vaisey-2016-best1.txt\n    \
    \  cache_sha256: f446cd14aa5658586dcbc19cc76d553cf6cdd53ea41c0325d4db265b4d072f7c\n\
    \  - edge_id: f80a-increases-retained-current-fraction\n    subject: f80a-neck-substitution\n\
    \    predicate: increases\n    object: current-fraction-after-egta\n    mechanism:\
    \ F80A retains a larger fraction of its own calcium-present current than WT after\
    \ chelation.\n      Partial retention is not complete calcium independence or\
    \ proof of an increased absolute transport\n      rate.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:27821745\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5127342/\n\
    \      snippet: fraction of current remaining\n      explanation: Figure 3C F80A\
    \ and WT bars support the normalized retained-fraction increase under\n      \
    \  matched protocols.\n      cache_path: evidence/PF01062/vaisey-2016-best1.txt\n\
    \      cache_sha256: f446cd14aa5658586dcbc19cc76d553cf6cdd53ea41c0325d4db265b4d072f7c\n\
    \  - edge_id: f80n-increases-retained-current-fraction\n    subject: f80n-neck-substitution\n\
    \    predicate: increases\n    object: current-fraction-after-egta\n    mechanism:\
    \ F80N retains a greater fraction of current than WT after calcium chelation.\
    \ A hydrophilic\n      substitution effect supports altered regulation but does\
    \ not directly observe pore wetting or a\n      particular structural motion.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:27821745\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5127342/\n\
    \      snippet: fraction of current remaining\n      explanation: Figure 3C F80N\
    \ versus WT is the adopted comparison, not a simulated wetting trajectory.\n \
    \     cache_path: evidence/PF01062/vaisey-2016-best1.txt\n      cache_sha256:\
    \ f446cd14aa5658586dcbc19cc76d553cf6cdd53ea41c0325d4db265b4d072f7c\n- graph_id:\
    \ best1-clasp-mutation-and-neck-rescue-flux\n  title: Clasp substitutions reduce\
    \ coupled chloride flux and TripleA restores it\n  scope: D301A/D304A compared\
    \ with WT, and the joint TripleA/D301A/D304A construct compared with D301A/D304A,\n\
    \    in 2016 Figure 4A/C/D proteoliposomes. Only the external 2-uM-calcium condition\
    \ is adopted here.\n  context: 0.1 mg/ml protein and 10 mg/ml POPE/POPG before\
    \ 100-fold dilution; internal 100 mM Na2SO4,\n    10 mM HEPES pH 8.2, 1 mM EGTA.\
    \ External 125 mM NaCl and calcium-EGTA give about 2 uM free calcium.\n    CCCP\
    \ initiates ACMA quench coupled to anion influx. The cited 2014 method supplies\
    \ 2 uM ACMA, 1 uM\n    CCCP, 0.5 mg/ml BSA and external pH 8.1. Comparisons were\
    \ purified/reconstituted in parallel and assayed\n    on the same day.\n  family_mapping:\
    \ D301/D304 and I76/F80/F84 lie within A0A8V0ZZU7 PF01062 residues 1-324 and the\
    \ experimentally\n    mapped 1-405 construct. The 2014 purification confirms Thr2\
    \ processing and the deposited sequence\n    matches residues 2-405 plus EGEEF.\
    \ Complete 2016 mutant clone sequences remain unverified.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:9031\n  limitations: ACMA reports coupled acidification, not\
    \ direct chloride concentration or a tracked molecular\n    gate. The 2016 traces\
    \ do not specify exact replicate count or recording temperature; bilayer temperature\n\
    \    is not borrowed. Empty vesicles were prepared but are not displayed in Figure\
    \ 4. Size-exclusion similarity\n    does not eliminate every folding/incorporation\
    \ alternative. Outside-only calcium activates only the\n    appropriate orientation;\
    \ this can affect WT/mutant flux comparisons.\n  nodes:\n  - node_id: d301a-d304a-clasp-substitution\n\
    \    label: Joint D301A/D304A instead of WT\n    node_type: PERTURBATION\n   \
    \ grounding:\n    - UniProtKB:A0A8V0ZZU7\n  - node_id: triplea-added-to-clasp-mutant\n\
    \    label: Add joint I76A/F80A/F84A to the D301A/D304A background\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:A0A8V0ZZU7\n  - node_id: chloride-associated-acma-quench\n\
    \    label: Chloride-flux-associated ACMA fluorescence quench\n    node_type:\
    \ ACTIVITY\n  edges:\n  - edge_id: clasp-substitution-decreases-coupled-flux\n\
    \    subject: d301a-d304a-clasp-substitution\n    predicate: decreases\n    object:\
    \ chloride-associated-acma-quench\n    mechanism: The joint clasp substitution\
    \ reduces the quench observed under externally supplied calcium\n      relative\
    \ to WT. This is a measured coupled flux effect, not direct proof that a particular\
    \ calcium-coordination\n      bond was broken.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:27821745\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5127342/\n      snippet:\
    \ did not observe\n      explanation: Figure 4A/C calcium-present traces show\
    \ the WT versus clasp-mutant flux-associated\n        signal difference. The small\
    \ residual drift is not claimed to be an independently resolved zero\n       \
    \ flux.\n      cache_path: evidence/PF01062/vaisey-2016-best1.txt\n      cache_sha256:\
    \ f446cd14aa5658586dcbc19cc76d553cf6cdd53ea41c0325d4db265b4d072f7c\n    - reference:\
    \ PMID:25337878\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4454446/\n\
    \      snippet: flux assay was based\n      explanation: The original method cited\
    \ by the 2016 paper supplies dye/ionophore details and the\n        coupled nature\
    \ of the fluorescence readout, not a new 2016 control or an independent replicate.\n\
    \      cache_path: evidence/PF01062/dickson-2014-flux-method.txt\n      cache_sha256:\
    \ f19cfc71cfa0e1d30e7f5b2f4ab21b1b38744b42a169016d80dc60932851b8b6\n  - edge_id:\
    \ triplea-restores-clasp-mutant-coupled-flux\n    subject: triplea-added-to-clasp-mutant\n\
    \    predicate: increases\n    object: chloride-associated-acma-quench\n    mechanism:\
    \ Adding the joint TripleA substitution to the clasp-mutant background restores\
    \ strong quench\n      under the adopted calcium-present condition. Genetic coupling\
    \ of these regions is supported without\n      a directly observed sequence of\
    \ conformational movements or independent sufficiency of each substitution.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:27821745\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5127342/\n\
    \      snippet: restore activity\n      explanation: Figure 4C/D compares the\
    \ double mutant with the combined five-site mutant. Calcium-free\n        traces\
    \ are additional context, not silently merged into this condition.\n      cache_path:\
    \ evidence/PF01062/vaisey-2016-best1.txt\n      cache_sha256: f446cd14aa5658586dcbc19cc76d553cf6cdd53ea41c0325d4db265b4d072f7c\n\
    curation_events:\n- timestamp: '2026-10-11T08:55:42Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Add scoped chicken BEST1 calcium, DIDS\
    \ and substitution graphs\n  history_record: history/records/PF01062/2026-10-11T085542Z-codex-d83613.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-11T09:07:54Z'\n\
    \  curator: Codex\n  action: REVIEW\n  outcome: needs_followup\n  summary: Retain\
    \ partial scientific self-review of chicken BEST1 assays\n  history_record: history/records/PF01062/2026-10-11T090754Z-codex-48cf50.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-23T07:48:01Z'\n\
    \  curator: Antigravity\n  action: EDIT\n  outcome: changed\n  summary: Ground\
    \ wt-current-at-plus100 node in best1-bilateral-egta-current-loss to UniProtKB:A0A8V0ZZU7\n\
    \  history_record: history/records/PF01062/2026-10-23T074801Z-antigravity-106203.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Retired E1C3A0 resolves to archived UPI0000E805B4; its 1-405 sequence exactly
    matches current chicken BEST1 A0A8V0ZZU7, sequence version 1. Five differences
    occur only after residue 405. PF01062 spans 1-324 and contains all adopted sites.
    PDB 4RDQ entity 1 exactly equals current 2-405 plus EGEEF; original MS/Edman confirms
    initiator removal to Thr2. The tested region extends beyond the Pfam profile;
    every mutant clone was not independently sequenced. Chicken V205 is not human
    I205.
  target_ids:
  - PF01062
  evidence_ids:
  - identity
  - primary
  - original-construct-flux-method
  - deposited-construct-sequence
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Eight directly observed assay effects retain their exact interventions,
    joint mutations, voltage, normalization and orientation. Electrical current and
    ACMA-coupled acidification are not conflated. Calcium half-response is not a binding
    Kd, DIDS inhibition does not establish a binding site, and mutant retained fractions
    are not absolute conductance. The clasp-mutant rescue is a joint five-site construct,
    not independent sufficiency of individual substitutions. KpBest cation behavior
    and modeled conformational trajectories are not transferred.
  target_ids:
  - PF01062
  evidence_ids:
  - primary
  - native
  - original-construct-flux-method
  - deposited-construct-sequence
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Exact mutant clone sequences, flux replicate counts and recording temperature,
    incorporation controls and raw single-channel behavior remain incomplete. Aperture-selectivity,
    remaining substitutions, full-length protein, other taxa, later inactivation,
    cryo-EM and GABA contexts require separate primary assessment. The cited earlier
    method was read for protocol details, not curated as an independent graph. This
    is not complete family coverage.
  target_ids:
  - PF01062
  evidence_ids:
  - primary
- assessment_id: cycle2-partner-grounding-verification
  area: identity
  topic: Cycle 2 causal-graph partner and substrate protein grounding
  outcome: supported
  summary: 'Stage 3 (PR #347) grounded Homo sapiens CaV1.3 (CACNA1D, UniProtKB:Q01668)
    and CaVbeta4 (CACNB4, UniProtKB:O00305) in best1-proline-motif-variants-shift-cav13-inhibition.'
  target_ids:
  - PF01062
  evidence_ids:
  - stage4-prior-review
findings:
- finding_id: additional-contexts
  issue_key: pf01062-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Extend BEST1 mechanism coverage with exact constructs and assay-specific
    controls
  description: Resolve mutant sequences and flux metadata, evaluate remaining permeability
    and full-length contexts, and inspect later inactivation, structural and GABA
    studies with their own protein mapping and controls. Preserve orientation, normalized
    versus absolute current and coupled-readout distinctions; retain a successor scientific
    review before status promotion.
  target_ids:
  - PF01062
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - original-construct-flux-method
  - deposited-construct-sequence
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01062.yaml
    role: Human-owned scientific overlay
  previous_occurrences:
  - repository: CultureBotAI/DUFMech
    review_id: 20261011T090737Z-pf01062-best1-calcium-and-substitution-assays
    finding_id: additional-contexts
actions:
- action_id: extend-contexts
  description: Resolve mutant sequences and flux metadata, evaluate remaining permeability
    and full-length contexts, and inspect later inactivation, structural and GABA
    studies with their own protein mapping and controls. Preserve orientation, normalized
    versus absolute current and coupled-readout distinctions; retain a successor scientific
    review before status promotion.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01062
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Vaisey 2016 Figures 1/3/4 were visually inspected and relevant main Methods/Results/Discussion
  read. Original 2014 construct and flux Methods were inspected. Structural coordinates,
  full supplemental datasets, raw traces and later primary figures were not independently
  reviewed. A truncated Discussion tool output was not treated as complete inspection
  of every sentence.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
