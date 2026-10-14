# Scoped scientific self-review of Alr racemization and cofactor assay effects

- Review: 20261011T092801Z-pf01168-alr-racemization-and-cofactor-assays
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T09:27:55Z
- Finished UTC: 2026-10-11T09:28:01Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Four MECHANISTIC graphs retain seven DIRECT OBSERVED biochemical effects for separate alanine-racemization directions, K39A activity loss, D-alanine preincubation, joint PMP/pyruvate reactivation and tritium-release comparisons. Full-protein scope, distinct reaction vessels and unresolved clone, concentration and control details remain explicit. Partial same-agent scientific review; IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01168 alanine racemase N-terminal domain, the next accession-ordered SEEDED family after IspD, using Kurokawa 1998 primary full text and exact current member mapping.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01168 | data/families/PF01168.yaml | generated | PF01168 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01168 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01168.

P10724 ALR_GEOSE, 388 aa and sequence version 2, matches the current InterPro and 1L6G canonical sequences. PF01168 spans 12-229, containing K39 but excluding Y265. The 1998 mutagenic primer translates to current residues 34-44 with K39A. Historical sequence conflicts remain explicit; donor strain, complete clones and all modified-residue identities are not independently resolved. Experiments use intact enzyme, not isolated domain.

### Directed effects and limits

graph: supported. Targets: PF01168.

Seven directly observed assay effects retain their exact joint treatments, preparation histories, pH, temperature and endpoint. Opposite racemization directions and inactivation/reactivation are separate vessels rather than a tracked cycle. K39A loss is qualitative, not a numerical zero under all conditions or proof of a unique chemical step. Figure 5 independently specifies 0.5 M methylamine, whereas Figure 4's caption implies 0.1 M and its prose says 0.5 M. The missing displayed enzyme-free methylamine control and unmeasured formaldehyde mechanism preclude stronger chemical-rescue conclusions. The mutant's opposite PLP-to-PMP reaction was not rescued under tested conditions.

### Remaining family coverage

completeness: concern. Targets: PF01168.

Complete historical constructs, exact per-assay enzyme dose and reaction duration, detection thresholds, replication, raw spectra and stronger folding/background controls remain incomplete. Watanabe 1999 was accessible only at abstract level through attempted publisher routes; its indexed erratum concerns the author's name, not established experimental correction. Tyr265, other substrates and other member contexts require independent mapping and primary review. Structural similarity to YggS/PLPBP alone is not verified current family membership or racemase activity.

## Findings

### additional-contexts: Resolve Alr assay and construct limits and extend member-specific evidence

minor / open / confirmed; issue key: pf01168-causal-context-coverage.

Reconstruct historical clones, establish per-assay metadata and controls, and reconcile the Figure 4 methylamine discrepancy without overwriting Figure 5's independently specified conditions. Inspect the full 1999 chemical-rescue paper and other mapped member/residue studies before adding chemical steps or family-wide conclusions. Preserve negative rescue results and retain a successor review before status promotion.

## Recommended Actions And Acceptance Checks

### extend-contexts

Reconstruct historical clones, establish per-assay metadata and controls, and reconcile the Figure 4 methylamine discrepancy without overwriting Figure 5's independently specified conditions. Inspect the full 1999 chemical-rescue paper and other mapped member/residue studies before adding chemical steps or family-wide conclusions. Preserve negative rescue results and retain a successor review before status promotion.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://www.jstage.jst.go.jp/article/biochemistry1922/124/6/124_6_1163/_pdf; Printed pages 1163-1169 main text, preparation and assay Methods, Figures 2-5 and Table I visually inspected | supports | Separate stereospecific product assays establish D-to-L and L-to-D racemization by intact Alr. K39A loses detected racemase activity. Table I distinguishes D-alanine preincubation loss from a separate apoenzyme/PMP/pyruvate reactivation protocol. Figure 5 shows reduced tritium release with K39A and increased release with methylamine, not quantified restoration of normal racemase turnover. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/P10724/entry/pfam/PF01168/; Accession and domain locations; paired UniProt identity facts | supports | P10724 ALR_GEOSE, 388 aa and sequence version 2, matches the current InterPro and 1L6G canonical sequences. PF01168 spans 12-229, containing K39 but excluding Y265. The 1998 mutagenic primer translates to current residues 34-44 with K39A. Historical sequence conflicts remain explicit; donor strain, complete clones and all modified-residue identities are not independently resolved. Experiments use intact enzyme, not isolated domain. |
| structure-reference-sequence | https://data.rcsb.org/rest/v1/core/polymer_entity/1L6G/1; Entity 1 canonical sequence and accession mapping | supports | Current 1L6G canonical sequence exactly matches P10724, supporting reference residue numbering but not proof that every historical recombinant clone or chemically modified residue is identical. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01168 | data/families/PF01168.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- The 1998 primary main text, Methods and Discussion were read; printed pages 1165-1167 containing Figures 2-5 and Table I were visually checked. Raw spectra, original count data, structural coordinates and complete cloned sequences were not reanalyzed. The 1999 rescue paper's full text was not available through attempted publisher routes, so no edges derive from its abstract.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T092801Z-pf01168-alr-racemization-and-cofactor-assays
title: Scoped scientific self-review of Alr racemization and cofactor assay effects
started_at: '2026-10-11T09:27:55Z'
finished_at: '2026-10-11T09:28:01Z'
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
summary: Four MECHANISTIC graphs retain seven DIRECT OBSERVED biochemical effects
  for separate alanine-racemization directions, K39A activity loss, D-alanine preincubation,
  joint PMP/pyruvate reactivation and tritium-release comparisons. Full-protein scope,
  distinct reaction vessels and unresolved clone, concentration and control details
  remain explicit. Partial same-agent scientific review; IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01168.yaml
    sha256: 6b39ba8b5258dbbfe101aa848627d84fb59251a18348e187e5f85457f7631846
    role: context
  - path: data/families/PF01168.yaml
    sha256: 1dc4e251c2aa7083aa408eebfdb19d0fc4eb18577b6f6078d864e0bb51f4567b
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
  - path: evidence/PF01168/kurokawa-1998-alr.txt
    role: context
    sha256: e9e2d711fb79aefad7bbfb0887c4ccfd4265728fb77db7c3a650aacabcdb477f
  - path: evidence/PF01168/Alr-identity.txt
    role: context
    sha256: 6a24bab0fadaf1eb4d06d6b960d57ba87d2caec93455d04efb747756ab73e7aa
targets:
- target_id: PF01168
  path: data/families/PF01168.yaml
  label: PF01168
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01168.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: a3ef188a68dbe158803a99bd9c8cfd323025b5f5579ed22fc3d29f9975474c2f
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01168 alanine racemase N-terminal domain, the next accession-ordered
    SEEDED family after IspD, using Kurokawa 1998 primary full text and exact current
    member mapping.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01168
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Complete historical constructs, exact per-assay enzyme dose and reaction
      duration, detection thresholds, replication, raw spectra and stronger folding/background
      controls remain incomplete. Watanabe 1999 was accessible only at abstract level
      through attempted publisher routes; its indexed erratum concerns the author's
      name, not established experimental correction. Tyr265, other substrates and
      other member contexts require independent mapping and primary review. Structural
      similarity to YggS/PLPBP alone is not verified current family membership or
      racemase activity.
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
  - PF01168
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/biochemistry1922/124/6/124_6_1163/_pdf
  locator: Printed pages 1163-1169 main text, preparation and assay Methods, Figures
    2-5 and Table I visually inspected
  accessed_at: '2026-10-11T09:28:01Z'
  support: supports
  snapshot_sha256: e9e2d711fb79aefad7bbfb0887c4ccfd4265728fb77db7c3a650aacabcdb477f
  summary: Separate stereospecific product assays establish D-to-L and L-to-D racemization
    by intact Alr. K39A loses detected racemase activity. Table I distinguishes D-alanine
    preincubation loss from a separate apoenzyme/PMP/pyruvate reactivation protocol.
    Figure 5 shows reduced tritium release with K39A and increased release with methylamine,
    not quantified restoration of normal racemase turnover.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P10724/entry/pfam/PF01168/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T09:28:01Z'
  support: supports
  snapshot_sha256: 6a24bab0fadaf1eb4d06d6b960d57ba87d2caec93455d04efb747756ab73e7aa
  summary: P10724 ALR_GEOSE, 388 aa and sequence version 2, matches the current InterPro
    and 1L6G canonical sequences. PF01168 spans 12-229, containing K39 but excluding
    Y265. The 1998 mutagenic primer translates to current residues 34-44 with K39A.
    Historical sequence conflicts remain explicit; donor strain, complete clones and
    all modified-residue identities are not independently resolved. Experiments use
    intact enzyme, not isolated domain.
- evidence_id: structure-reference-sequence
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1L6G/1
  locator: Entity 1 canonical sequence and accession mapping
  summary: Current 1L6G canonical sequence exactly matches P10724, supporting reference
    residue numbering but not proof that every historical recombinant clone or chemically
    modified residue is identical.
  accessed_at: '2026-10-11T09:28:01Z'
  support: supports
  snapshot_sha256: 6a24bab0fadaf1eb4d06d6b960d57ba87d2caec93455d04efb747756ab73e7aa
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T09:28:01Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01168
  kind: record_content
  reference: data/families/PF01168.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T09:28:01Z'
  support: context_only
  snapshot_sha256: 1dc4e251c2aa7083aa408eebfdb19d0fc4eb18577b6f6078d864e0bb51f4567b
  quote: "id: Pfam:PF01168\npfam_id: PF01168\nname: Alanine racemase, N-terminal domain\n\
    short_name: Ala_racemase_N\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01168\n\
    counters:\n  proteins: 61405\n  matches: 61451\n  proteomes: 20949\n  taxa: 33587\n\
    \  structures: 114\n  alphafold_models: 39913\n  domain_architectures: 206\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR001608\ncuration_history: history/records/PF01168\ndiscussions:\n\
    - discussion_id: alr-residue-chemistry-and-family-coverage\n  prompt: Extend alanine-racemase\
    \ contexts while resolving clone, assay and chemical-rescue limits.\n  kind: CURATION_TODO\n\
    \  status: OPEN\n  rationale: Seven experimental effects concern one intact enzyme\
    \ and K39A. They do not establish isolated\n    PF01168 activity, all family substrates,\
    \ physiological regulation or a fully observed catalytic trajectory.\n  evidence:\n\
    \  - reference: PMID:9832621\n    supports: PARTIAL\n    evidence_source: inspected_primary_full_text\n\
    \    explanation: Main Methods, Results, Table I and Figures 2-5 support the scoped\
    \ assays; atomic schemes\n      remain interpretations.\n  notes: Establish complete\
    \ historical clones and per-assay doses, times, detection limits and replication.\n\
    \    Resolve the Figure 4 0.1/0.5 M methylamine discrepancy without changing Figure\
    \ 5's independent conditions.\n    The 1999 chemical-rescue paper PMID:9933615\
    \ was accessible only at abstract level in attempted publisher\n    routes; its\
    \ indexed erratum concerns the author's name. Tyr265, other-substrate and other-member\
    \ studies\n    need separate review and mapping. Structural similarity to YggS/PLPBP\
    \ alone is not evidence of racemase\n    activity or of current PF01168 membership.\
    \ Partial same-agent scientific review; remain IN_PROGRESS.\n  posed_by: Codex\n\
    \  posed_date: '2026-10-11'\ncausal_graphs:\n- graph_id: geobacillus-alr-racemization-and-k39a\n\
    \  title: Intact alanine racemase interconverts alanine enantiomers\n  scope:\
    \ Purified B. stearothermophilus (now Geobacillus) alanine racemase and K39A in\
    \ the 1998 study.\n    The two substrate directions are separate assays, not a\
    \ tracked molecular cycle.\n  context: 1 ml with 100 umol CHES pH 9 and 30 umol\
    \ D- or L-alanine, 37 C; stop at 100 C for 10 min. L-product\n    is measured\
    \ using alanine dehydrogenase/NAD+, D-product using DAAT/lactate dehydrogenase/NADH.\
    \ Figure\n    3A varies pH in specified buffers. Exact reaction duration and enzyme\
    \ amount per comparison remain\n    unresolved.\n  family_mapping: P10724/ALR_GEOSE,\
    \ alr/dal, 388-aa reference sequence version 2, matches InterPro and\n    1L6G's\
    \ canonical sequence. PF01168 spans 12-229 and includes K39, but excludes Y265\
    \ in the other domain.\n    The 1998 mutagenic primer matches residues 34-44 with\
    \ K39A; complete clones and donor strain are not\n    independently resolved.\n\
    \  scope_status: MECHANISTIC\n  taxon: NCBITaxon:1422\n  limitations: These are\
    \ intact-enzyme product assays. Neither the isolated N-terminal domain's sufficiency\n\
    \    nor every proton-transfer step is observed. K39A's activity loss does not\
    \ by itself prove one unique\n    chemical role; its reported absorption similarity\
    \ is not a complete folding control. Older sequence\n    conflicts and unspecified\
    \ detection limits/replicates remain explicit. Coupling enzymes measure quenched\n\
    \    products, not live-cell peptidoglycan flux.\n  nodes:\n  - node_id: holo-alr-with-d-alanine\n\
    \    label: Intact holo-Alr with D-alanine\n    node_type: ACTIVITY\n    grounding:\n\
    \    - UniProtKB:P10724\n  - node_id: l-alanine-product\n    label: L-alanine\
    \ detected by the product assay\n    node_type: STATE\n  - node_id: holo-alr-with-l-alanine\n\
    \    label: Intact holo-Alr with L-alanine\n    node_type: ACTIVITY\n    grounding:\n\
    \    - UniProtKB:P10724\n  - node_id: d-alanine-product\n    label: D-alanine\
    \ detected by the product assay\n    node_type: STATE\n  - node_id: k39a-racemase-substitution\n\
    \    label: K39A instead of WT without exogenous alkylamine\n    node_type: PERTURBATION\n\
    \  - node_id: detectable-racemase-activity\n    label: Detectable alanine-racemization\
    \ activity\n    node_type: ACTIVITY\n  edges:\n  - edge_id: alr-d-substrate-produces-l-alanine\n\
    \    subject: holo-alr-with-d-alanine\n    predicate: produces\n    object: l-alanine-product\n\
    \    mechanism: Quenched D-alanine reactions yield L-alanine measured by the stereospecific\
    \ reporter assay.\n      The assay establishes net conversion, not the proposed\
    \ sequence of catalytic intermediates.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:9832621\n\
    \      source_url: https://www.jstage.jst.go.jp/article/biochemistry1922/124/6/124_6_1163/_pdf\n\
    \      snippet: racemase reaction\n      explanation: Printed page 1165 Enzyme\
    \ Assay and visually inspected Figure 3A support the D-to-L\n        direction.\n\
    \      cache_path: evidence/PF01168/kurokawa-1998-alr.txt\n      cache_sha256:\
    \ e9e2d711fb79aefad7bbfb0887c4ccfd4265728fb77db7c3a650aacabcdb477f\n    - reference:\
    \ https://www.ebi.ac.uk/interpro/api/protein/uniprot/P10724/entry/pfam/PF01168/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P10724/entry/pfam/PF01168/\n\
    \      snippet: 'P10724 Pfam:PF01168 interval: 12-229, inclusive'\n      explanation:\
    \ Whole-protein identity and profile interval, with current sequence and historical\
    \ clone\n        qualifications retained.\n      cache_path: evidence/PF01168/Alr-identity.txt\n\
    \      cache_sha256: 6a24bab0fadaf1eb4d06d6b960d57ba87d2caec93455d04efb747756ab73e7aa\n\
    \  - edge_id: alr-l-substrate-produces-d-alanine\n    subject: holo-alr-with-l-alanine\n\
    \    predicate: produces\n    object: d-alanine-product\n    mechanism: The separate\
    \ L-alanine reaction yields D-alanine detected by DAAT and lactate dehydrogenase\n\
    \      after quenching. No cellular consequence or automatic family-wide transfer\
    \ is attached.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:9832621\n      source_url:\
    \ https://www.jstage.jst.go.jp/article/biochemistry1922/124/6/124_6_1163/_pdf\n\
    \      snippet: racemase reaction\n      explanation: Page 1165's separate product\
    \ assay and Figure 3A's L-to-D curve; not a continuation\n        of the other\
    \ reaction vessel.\n      cache_path: evidence/PF01168/kurokawa-1998-alr.txt\n\
    \      cache_sha256: e9e2d711fb79aefad7bbfb0887c4ccfd4265728fb77db7c3a650aacabcdb477f\n\
    \  - edge_id: k39a-decreases-detectable-racemization\n    subject: k39a-racemase-substitution\n\
    \    predicate: decreases\n    object: detectable-racemase-activity\n    mechanism:\
    \ The purified K39A preparation lacks detected racemase activity in the reported\
    \ comparison.\n      This is a qualitative loss under the tested conditions, not\
    \ a numerical zero under every possible\n      assay.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:9832621\n      source_url: https://www.jstage.jst.go.jp/article/biochemistry1922/124/6/124_6_1163/_pdf\n\
    \      snippet: no racemase activity\n      explanation: Page 1166, Role of the\
    \ Active-Site Lysyl Residue, with mutant preparation and assay\n        Methods\
    \ on pages 1164-1165.\n      cache_path: evidence/PF01168/kurokawa-1998-alr.txt\n\
    \      cache_sha256: e9e2d711fb79aefad7bbfb0887c4ccfd4265728fb77db7c3a650aacabcdb477f\n\
    - graph_id: geobacillus-alr-alanine-preincubation-loss\n  title: D-alanine preincubation\
    \ at pH 7 lowers retained Alr activity\n  scope: WT holoenzyme in Table I's 1998\
    \ inactivation experiment, distinct from the pH-9 racemization\n    assay and\
    \ the pH-7.2 spectral time course.\n  context: 10 ug holoenzyme, 0.5 umol D-alanine,\
    \ 10 umol potassium phosphate pH 7, 0.01% 2-mercaptoethanol,\n    100 ul; 25 C\
    \ for 12 h. Remaining D-to-L racemase activity is assayed afterward.\n  family_mapping:\
    \ Intact P10724-associated recombinant Alr; PF01168 12-229 maps within the whole\
    \ enzyme.\n    This experiment does not selectively perturb or isolate that domain.\n\
    \  scope_status: MECHANISTIC\n  taxon: NCBITaxon:1422\n  limitations: Table I\
    \ reports activity loss, while separate spectra support a PLP/PMP interpretation.\n\
    \    This is not an observed intracellular regulatory switch or proof that physiological\
    \ D-alanine always\n    inhibits Alr. No independently reconstructed raw kinetics\
    \ or exact detection threshold is available.\n  nodes:\n  - node_id: d-alanine-preincubation-ph7\n\
    \    label: Preincubate WT holo-Alr with D-alanine at pH 7 for 12 h\n    node_type:\
    \ PERTURBATION\n  - node_id: retained-d-to-l-racemase\n    label: Retained D-to-L\
    \ racemase activity\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:P10724\n\
    \  edges:\n  - edge_id: d-alanine-preincubation-decreases-retained-activity\n\
    \    subject: d-alanine-preincubation-ph7\n    predicate: decreases\n    object:\
    \ retained-d-to-l-racemase\n    mechanism: D-alanine preincubation lowers the\
    \ subsequent activity readout. The coupled assay endpoint\n      is retained separately\
    \ from the proposed transamination microsteps.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:9832621\n\
    \      source_url: https://www.jstage.jst.go.jp/article/biochemistry1922/124/6/124_6_1163/_pdf\n\
    \      snippet: inactivated\n      explanation: Visually inspected Table I's D-alanine\
    \ row and footnote a; Figure 2 is supporting spectral\n        evidence under\
    \ different pH/dose conditions.\n      cache_path: evidence/PF01168/kurokawa-1998-alr.txt\n\
    \      cache_sha256: e9e2d711fb79aefad7bbfb0887c4ccfd4265728fb77db7c3a650aacabcdb477f\n\
    - graph_id: geobacillus-alr-pmp-pyruvate-reactivation\n  title: Joint PMP and\
    \ pyruvate treatment restores racemase activity\n  scope: WT apoenzyme in Table\
    \ I's distinct reactivation experiment. This is not a time-resolved reversal\n\
    \    in the same molecules used for D-alanine inactivation.\n  context: 50 ug\
    \ apoenzyme, 1 umol PMP, 2.5 umol pyruvate, 10 umol K2HPO4-KOH pH 10 and 0.01%\
    \ 2-mercaptoethanol\n    in 100 ul; 25 C for 12 h. Recovered activity is measured\
    \ with D-alanine.\n  family_mapping: Full P10724-associated Alr, containing PF01168\
    \ at 12-229 plus its C-terminal region.\n    Apoenzyme preparation is by hydroxylamine\
    \ treatment/dialysis, not a gene deletion or isolated-domain\n    preparation.\n\
    \  scope_status: MECHANISTIC\n  taxon: NCBITaxon:1422\n  limitations: PMP, pyruvate,\
    \ enzyme and alkaline conditions are a joint intervention; none is represented\n\
    \    as independently sufficient. Activity recovery and spectral changes do not\
    \ directly identify each\n    proton-transfer step. The separate mutant methylamine\
    \ experiment has different conditions.\n  nodes:\n  - node_id: apo-alr-pmp-pyruvate-treatment\n\
    \    label: Incubate WT apo-Alr jointly with PMP and pyruvate at pH 10\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:P10724\n  - node_id: recovered-d-to-l-racemase\n\
    \    label: Recovered D-to-L racemase activity\n    node_type: ACTIVITY\n  edges:\n\
    \  - edge_id: pmp-pyruvate-treatment-increases-racemase-activity\n    subject:\
    \ apo-alr-pmp-pyruvate-treatment\n    predicate: increases\n    object: recovered-d-to-l-racemase\n\
    \    mechanism: The joint treatment restores detectable racemization to the apoenzyme\
    \ preparation. It does\n      not establish that pyruvate alone repairs every\
    \ inactivated form or that a physiological feedback\n      cycle has been tracked.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:9832621\n      source_url: https://www.jstage.jst.go.jp/article/biochemistry1922/124/6/124_6_1163/_pdf\n\
    \      snippet: recovered\n      explanation: Table I, pyruvate row and footnote\
    \ b, with apoenzyme Methods; separate Figure 4A supports\n        the cofactor-state\
    \ interpretation.\n      cache_path: evidence/PF01168/kurokawa-1998-alr.txt\n\
    \      cache_sha256: e9e2d711fb79aefad7bbfb0887c4ccfd4265728fb77db7c3a650aacabcdb477f\n\
    - graph_id: geobacillus-alr-k39a-tritium-rescue\n  title: K39A reduces tritium\
    \ release and methylamine increases it\n  scope: WT and K39A apo-Alr in the 1998\
    \ Figure 5 labeled-PMP experiment. The adopted rescue is tritium\n    release,\
    \ not a quantified return of normal alanine-racemization turnover.\n  context:\
    \ 100 ul, 10 umol CHES pH 9, 8.7 nmol enzyme, 8 nmol randomly labeled [4'-3H]PMP\
    \ and 8.5 umol\n    pyruvate, 30 C. Add 50 umol methylamine hydrochloride for\
    \ the rescue arm, giving 0.5 M. Acid-quenched\n    aliquots are dried and remaining\
    \ radioactivity measured; volatile release is calculated. Figure 5\n    displays\
    \ up to 8 h.\n  family_mapping: K39 is within P10724's PF01168 12-229 interval;\
    \ the mutagenic primer locally matches\n    K39A. Full-length enzyme is expressed\
    \ through pAR310 in JM109. Exact complete clones and affinity-free\n    preparation\
    \ details remain scoped to the inspected protocol.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:1422\n  limitations: Tritium release is not directly equated\
    \ with product concentration or racemase turnover.\n    WT and methylamine-rescued\
    \ mutant reach different plateaus; an enzyme-free methylamine control is\n   \
    \ not displayed in Figure 5. Formaldehyde in the proposed recycling scheme was\
    \ not identified. Figure\n    4's methylamine caption implies 0.1 M while its\
    \ prose says 0.5 M; Figure 5's separate Methods supplies\n    the adopted 0.5\
    \ M. The opposite PLP-to-PMP mutant reaction was not rescued under the tested\
    \ conditions.\n    Replication and complete folding controls remain limited.\n\
    \  nodes:\n  - node_id: k39a-labeled-pmp-assay\n    label: K39A instead of WT\
    \ in the labeled-PMP/pyruvate assay\n    node_type: PERTURBATION\n  - node_id:\
    \ methylamine-added-to-k39a\n    label: Add 0.5 M methylamine to K39A with PMP\
    \ and pyruvate\n    node_type: PERTURBATION\n  - node_id: volatile-tritium-release\n\
    \    label: Volatile tritium release from labeled PMP\n    node_type: ACTIVITY\n\
    \    grounding:\n    - UniProtKB:P10724\n  edges:\n  - edge_id: k39a-decreases-tritium-release\n\
    \    subject: k39a-labeled-pmp-assay\n    predicate: decreases\n    object: volatile-tritium-release\n\
    \    mechanism: The K39A trace remains near baseline while WT releases label.\
    \ The assay supports a residue-dependent\n      effect without directly observing\
    \ the proposed hydrogen-transfer intermediates.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:9832621\n\
    \      source_url: https://www.jstage.jst.go.jp/article/biochemistry1922/124/6/124_6_1163/_pdf\n\
    \      snippet: no tritium was released\n      explanation: Figure 5 WT/K39A comparison,\
    \ page 1165 Methods and page 1168 Results; the result is\n        bounded to the\
    \ stated preparation and readout.\n      cache_path: evidence/PF01168/kurokawa-1998-alr.txt\n\
    \      cache_sha256: e9e2d711fb79aefad7bbfb0887c4ccfd4265728fb77db7c3a650aacabcdb477f\n\
    \  - edge_id: methylamine-increases-k39a-tritium-release\n    subject: methylamine-added-to-k39a\n\
    \    predicate: increases\n    object: volatile-tritium-release\n    mechanism:\
    \ Methylamine increases label release from the otherwise weak K39A preparation.\
    \ Its higher\n      final release than WT is not interpreted as greater native\
    \ catalytic activity or proof of the unmeasured\n      formaldehyde pathway.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:9832621\n      source_url: https://www.jstage.jst.go.jp/article/biochemistry1922/124/6/124_6_1163/_pdf\n\
    \      snippet: tritium was released\n      explanation: Figure 5 K39A plus/minus\
    \ methylamine and the independently specified 100-ul assay conditions;\n     \
    \   not the conflicting Figure 4 concentration.\n      cache_path: evidence/PF01168/kurokawa-1998-alr.txt\n\
    \      cache_sha256: e9e2d711fb79aefad7bbfb0887c4ccfd4265728fb77db7c3a650aacabcdb477f\n\
    curation_events:\n- timestamp: '2026-10-11T09:15:06Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Add scoped Alr racemization and cofactor-assay\
    \ graphs\n  history_record: history/records/PF01168/2026-10-11T091506Z-codex-0d975f.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: P10724 ALR_GEOSE, 388 aa and sequence version 2, matches the current InterPro
    and 1L6G canonical sequences. PF01168 spans 12-229, containing K39 but excluding
    Y265. The 1998 mutagenic primer translates to current residues 34-44 with K39A.
    Historical sequence conflicts remain explicit; donor strain, complete clones and
    all modified-residue identities are not independently resolved. Experiments use
    intact enzyme, not isolated domain.
  target_ids:
  - PF01168
  evidence_ids:
  - identity
  - primary
  - structure-reference-sequence
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Seven directly observed assay effects retain their exact joint treatments,
    preparation histories, pH, temperature and endpoint. Opposite racemization directions
    and inactivation/reactivation are separate vessels rather than a tracked cycle.
    K39A loss is qualitative, not a numerical zero under all conditions or proof of
    a unique chemical step. Figure 5 independently specifies 0.5 M methylamine, whereas
    Figure 4's caption implies 0.1 M and its prose says 0.5 M. The missing displayed
    enzyme-free methylamine control and unmeasured formaldehyde mechanism preclude
    stronger chemical-rescue conclusions. The mutant's opposite PLP-to-PMP reaction
    was not rescued under tested conditions.
  target_ids:
  - PF01168
  evidence_ids:
  - primary
  - native
  - structure-reference-sequence
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Complete historical constructs, exact per-assay enzyme dose and reaction
    duration, detection thresholds, replication, raw spectra and stronger folding/background
    controls remain incomplete. Watanabe 1999 was accessible only at abstract level
    through attempted publisher routes; its indexed erratum concerns the author's
    name, not established experimental correction. Tyr265, other substrates and other
    member contexts require independent mapping and primary review. Structural similarity
    to YggS/PLPBP alone is not verified current family membership or racemase activity.
  target_ids:
  - PF01168
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01168-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve Alr assay and construct limits and extend member-specific evidence
  description: Reconstruct historical clones, establish per-assay metadata and controls,
    and reconcile the Figure 4 methylamine discrepancy without overwriting Figure
    5's independently specified conditions. Inspect the full 1999 chemical-rescue
    paper and other mapped member/residue studies before adding chemical steps or
    family-wide conclusions. Preserve negative rescue results and retain a successor
    review before status promotion.
  target_ids:
  - PF01168
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - structure-reference-sequence
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01168.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Reconstruct historical clones, establish per-assay metadata and controls,
    and reconcile the Figure 4 methylamine discrepancy without overwriting Figure
    5's independently specified conditions. Inspect the full 1999 chemical-rescue
    paper and other mapped member/residue studies before adding chemical steps or
    family-wide conclusions. Preserve negative rescue results and retain a successor
    review before status promotion.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01168
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- The 1998 primary main text, Methods and Discussion were read; printed pages 1165-1167
  containing Figures 2-5 and Table I were visually checked. Raw spectra, original
  count data, structural coordinates and complete cloned sequences were not reanalyzed.
  The 1999 rescue paper's full text was not available through attempted publisher
  routes, so no edges derive from its abstract.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
