# Scoped scientific self-review of TilS products and aminoacylation effects

- Review: 20261011T094436Z-pf01171-tils-modification-and-aminoacylation
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T09:44:04Z
- Finished UTC: 2026-10-11T09:44:36Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Three MECHANISTIC graphs retain eight DIRECT OBSERVED effects for lysine/ethanolamine product formation and separate E. coli S100 and purified B. subtilis IleRS preparation comparisons. Exact TilS reference mapping, whole-protein scope, mass-localization limits, reaction carryover and distinct assay normalization remain explicit. Partial same-agent scientific review; IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01171 PP-loop domain, the next accession-ordered SEEDED family after GDT1, using Salowe 2009 primary assays with the cited sequence accession and later ortholog-specific evidence as an uncurated coverage lead.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01171 | data/families/PF01171.yaml | generated | PF01171 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01171 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01171.

P52097/TILS_ECOLI, 432 aa and sequence version 1, exactly matches InterPro and the paper's Z50870.1/CAA90751.1 translation, with PF01171 at 10-197. Forward primer matches the coding start; the reverse primer matches terminal WQKTLS and omits the stop, consistent with the reported C-terminal His6 fusion. Exact vector scar/full clone is not independently reconstructed. Q45477 identifies the distinct B. subtilis 168 IleRS partner; its current version 3 sequence is later than the experiment and is not presented as independent proof of the historical FLAG clone. E. coli S100 is a mixed extract.

### Directed effects and limits

graph: supported. Targets: PF01171.

Two product edges retain joint inputs and the 0.1 mM lysine versus 20 mM ethanolamine conditions. Intact mass and migration do not independently localize the reaction or visualize the adenylated intermediate. Six aminoacylation edges compare unrepurified reaction preparations with no-amine control A, not purified RNAs proven to differ only at one site. E. coli MetRS, E. coli IleRS and B. subtilis IleRS have distinct normalizations and biochemical preparations; their numbers are not one absolute scale. Reported zeros, 123 versus 100 and 99 versus 100 are not universal absence, significant superiority or kinetic equivalence. No in-vivo decoding or family-wide mechanism is inferred.

### Remaining family coverage

completeness: concern. Targets: PF01171.

Raw MS, site-specific chemical identification, historical clone scars, preparation carryover controls, replicate counts and rate uncertainty remain incomplete. Original intermediate/recognition studies and remaining genuine alternative substrates require separate assessment. The 2025 abstract and selected near-cognate-discrimination Results were inspected, but their Methods, figures and ortholog mapping remain unreviewed. The historical neighboring rof/cell-cycle annotation is not adopted for TilS.

## Findings

### additional-contexts: Strengthen TilS chemical localization and ortholog-specific assay coverage

minor / open / confirmed; issue key: pf01171-causal-context-coverage.

Obtain exact constructs, matched carryover controls and uncertainty estimates; inspect original intermediate and recognition studies before adding atomic steps. Curate remaining alternative substrates without accepting contaminated samples or isotope dilution as direct inhibition. Extend the 2025 ortholog study through Methods, figures and exact member mapping, keeping species and transcript-preparation boundaries explicit. Retain a successor scientific review before status promotion.

## Recommended Actions And Acceptance Checks

### extend-contexts

Obtain exact constructs, matched carryover controls and uncertainty estimates; inspect original intermediate and recognition studies before adding atomic steps. Curate remaining alternative substrates without accepting contaminated samples or isotope dilution as direct inhibition. Extend the 2025 ortholog study through Methods, figures and exact member mapping, keeping species and transcript-preparation boundaries explicit. Retain a successor scientific review before status promotion.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC2665086/; Experimental procedures, Results, Discussion, Tables 1-5 and visually inspected Figure 2 | supports | Joint purified TilS/ATP/transcript reactions with lysine or ethanolamine yield mass- and gel-supported modified tRNA preparations. Relative to the no-amine preparation, both increase isoleucine incorporation and decrease methionine incorporation in E. coli S100, and increase isoleucine incorporation by purified B. subtilis IleRS in a separate mixed-species system. Ornithine and N-alpha-methyllysine samples instead generated lysine-like products attributed to contamination. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/P52097/entry/pfam/PF01171/; Accession and domain locations; paired UniProt identity facts | supports | P52097/TILS_ECOLI, 432 aa and sequence version 1, exactly matches InterPro and the paper's Z50870.1/CAA90751.1 translation, with PF01171 at 10-197. Forward primer matches the coding start; the reverse primer matches terminal WQKTLS and omits the stop, consistent with the reported C-terminal His6 fusion. Exact vector scar/full clone is not independently reconstructed. Q45477 identifies the distinct B. subtilis 168 IleRS partner; its current version 3 sequence is later than the experiment and is not presented as independent proof of the historical FLAG clone. E. coli S100 is a mixed extract. |
| cited-sequence-and-primer-check | https://www.ebi.ac.uk/ena/browser/view/Z50870; Z50870.1 CDS 991-2289, CAA90751.1 translation and terminal coding bases; paired NCBI structured record | supports | Full translation matches current P52097; published primers match the coding start and stop-omitting terminal segment. This supports reference identity and the reported fusion design without inventing a fully reconstructed vector scar. |
| later-ortholog-coverage-lead | https://pmc.ncbi.nlm.nih.gov/articles/PMC12514573/; Abstract and Discrimination of near-cognate substrates by MetRS Results, with Figure 4 caption | supports | Later primary comparisons indicate ortholog-specific recognition and catalytic behavior. Full member mapping, Methods and figures were not assessed, so the source supplies follow-up context rather than new causal edges. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01171 | data/families/PF01171.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Main 2009 Methods/Results/Discussion and Tables 1-5 were read; Figure 2 was visually inspected. Raw mass spectra, Figure 3's proposed hydrogen-bond model and full clone/vector sequences were not reanalyzed. The 2025 abstract and one Results subsection/caption are only a coverage lead, not a completed review of that study or a source of new edges.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T094436Z-pf01171-tils-modification-and-aminoacylation
title: Scoped scientific self-review of TilS products and aminoacylation effects
started_at: '2026-10-11T09:44:04Z'
finished_at: '2026-10-11T09:44:36Z'
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
summary: Three MECHANISTIC graphs retain eight DIRECT OBSERVED effects for lysine/ethanolamine
  product formation and separate E. coli S100 and purified B. subtilis IleRS preparation
  comparisons. Exact TilS reference mapping, whole-protein scope, mass-localization
  limits, reaction carryover and distinct assay normalization remain explicit. Partial
  same-agent scientific review; IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01171.yaml
    sha256: 05a992af68277488f10e60d3733ce1a2320215300361f74750477be5aab1dd59
    role: context
  - path: data/families/PF01171.yaml
    sha256: d3a2517a386308747a64fa031b3458847b95df17590a72e19759445fef18e8e3
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
  - path: evidence/PF01171/salowe-2009-tils.txt
    role: context
    sha256: 544b2a00f2d9713060c325b735c83fc1b2beaf0313fdc01c6c21bcbe8822966d
  - path: evidence/PF01171/TilS-identity.txt
    role: context
    sha256: b8259ad7ec4469d61461603e33b6d55118e11555a3295f8262cefe2f66975ab0
  - path: evidence/PF01171/tils-2025-coverage-lead.txt
    role: context
    sha256: 9745795a4ae2372fa18efd3d31dd5496b623193b0bf5010d472451342362cb53
targets:
- target_id: PF01171
  path: data/families/PF01171.yaml
  label: PF01171
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01171.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: af5d0c67c8fc56e94c4c148f57dddde64e7481c95590d3716625f3ab40a7840d
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01171 PP-loop domain, the next accession-ordered SEEDED family after
    GDT1, using Salowe 2009 primary assays with the cited sequence accession and later
    ortholog-specific evidence as an uncurated coverage lead.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01171
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Raw MS, site-specific chemical identification, historical clone scars,
      preparation carryover controls, replicate counts and rate uncertainty remain
      incomplete. Original intermediate/recognition studies and remaining genuine
      alternative substrates require separate assessment. The 2025 abstract and selected
      near-cognate-discrimination Results were inspected, but their Methods, figures
      and ortholog mapping remain unreviewed. The historical neighboring rof/cell-cycle
      annotation is not adopted for TilS.
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
  - PF01171
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2665086/
  locator: Experimental procedures, Results, Discussion, Tables 1-5 and visually inspected
    Figure 2
  accessed_at: '2026-10-11T09:44:36Z'
  support: supports
  snapshot_sha256: 544b2a00f2d9713060c325b735c83fc1b2beaf0313fdc01c6c21bcbe8822966d
  summary: Joint purified TilS/ATP/transcript reactions with lysine or ethanolamine
    yield mass- and gel-supported modified tRNA preparations. Relative to the no-amine
    preparation, both increase isoleucine incorporation and decrease methionine incorporation
    in E. coli S100, and increase isoleucine incorporation by purified B. subtilis
    IleRS in a separate mixed-species system. Ornithine and N-alpha-methyllysine samples
    instead generated lysine-like products attributed to contamination.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P52097/entry/pfam/PF01171/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T09:44:36Z'
  support: supports
  snapshot_sha256: b8259ad7ec4469d61461603e33b6d55118e11555a3295f8262cefe2f66975ab0
  summary: P52097/TILS_ECOLI, 432 aa and sequence version 1, exactly matches InterPro
    and the paper's Z50870.1/CAA90751.1 translation, with PF01171 at 10-197. Forward
    primer matches the coding start; the reverse primer matches terminal WQKTLS and
    omits the stop, consistent with the reported C-terminal His6 fusion. Exact vector
    scar/full clone is not independently reconstructed. Q45477 identifies the distinct
    B. subtilis 168 IleRS partner; its current version 3 sequence is later than the
    experiment and is not presented as independent proof of the historical FLAG clone.
    E. coli S100 is a mixed extract.
- evidence_id: cited-sequence-and-primer-check
  kind: database
  reference: https://www.ebi.ac.uk/ena/browser/view/Z50870
  locator: Z50870.1 CDS 991-2289, CAA90751.1 translation and terminal coding bases;
    paired NCBI structured record
  summary: Full translation matches current P52097; published primers match the coding
    start and stop-omitting terminal segment. This supports reference identity and
    the reported fusion design without inventing a fully reconstructed vector scar.
  accessed_at: '2026-10-11T09:44:36Z'
  support: supports
  snapshot_sha256: b8259ad7ec4469d61461603e33b6d55118e11555a3295f8262cefe2f66975ab0
- evidence_id: later-ortholog-coverage-lead
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC12514573/
  locator: Abstract and Discrimination of near-cognate substrates by MetRS Results,
    with Figure 4 caption
  summary: Later primary comparisons indicate ortholog-specific recognition and catalytic
    behavior. Full member mapping, Methods and figures were not assessed, so the source
    supplies follow-up context rather than new causal edges.
  accessed_at: '2026-10-11T09:44:36Z'
  support: supports
  snapshot_sha256: 9745795a4ae2372fa18efd3d31dd5496b623193b0bf5010d472451342362cb53
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T09:44:36Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01171
  kind: record_content
  reference: data/families/PF01171.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T09:44:36Z'
  support: context_only
  snapshot_sha256: d3a2517a386308747a64fa031b3458847b95df17590a72e19759445fef18e8e3
  quote: "id: Pfam:PF01171\npfam_id: PF01171\nname: PP-loop domain\nshort_name: ATP_bind_3\n\
    seed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status: IN_PROGRESS\n\
    source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01171\ncounters:\n\
    \  proteins: 33613\n  matches: 34389\n  proteomes: 21356\n  taxa: 34246\n  structures:\
    \ 16\n  alphafold_models: 23049\n  domain_architectures: 200\nprovenance:\n  snapshot_id:\
    \ interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR011063\ndescription: The structure of tRNA(Ile)-lysidine\
    \ synthetase consists of an N-terminal dinucleotide-binding\n  fold domain (NTD),\
    \ and a C-terminal globular domain (CTD). The structure of the NTD closely resembles\n\
    \  that of a P-loop \"N-type\" ATP pyrophosphatase [[cite:PUB00034489]]. These\
    \ proteins belong to the PP-loop\n  superfamily [[cite:PUB00014303]].\ncuration_history:\
    \ history/records/PF01171\ndiscussions:\n- discussion_id: tils-atomic-steps-and-ortholog-coverage\n\
    \  prompt: Extend TilS evidence with exact constructs, modification-site chemistry\
    \ and ortholog-specific\n    substrate recognition.\n  kind: CURATION_TODO\n \
    \ status: OPEN\n  rationale: Eight observed cell-free assay effects cover two\
    \ product preparations and separate aminoacylation\n    systems. They do not establish\
    \ a fully observed atomic mechanism, purified-RNA-only causality or the\n    activities\
    \ of every PP-loop protein.\n  evidence:\n  - reference: PMID:19233850\n    supports:\
    \ PARTIAL\n    evidence_source: inspected_primary_full_text\n    explanation:\
    \ Tables 4/5 and Figure 2 support the adopted effects; contamination, isotope\
    \ dilution,\n      preparation carryover and normalization limits are retained.\n\
    \  - reference: PMID:40914250\n    supports: PARTIAL\n    evidence_source: primary_abstract_and_selected_results\n\
    \    explanation: Later ortholog-specific recognition findings identify additional\
    \ work; methods, exact\n      member mappings and figures were not fully reviewed.\n\
    \  notes: Resolve experimental clone scars, carryover controls and error estimates;\
    \ inspect the original\n    adenylated-intermediate and recognition studies before\
    \ adding those microsteps. Curate remaining true\n    alternative substrates separately\
    \ from contaminated ornithine/N-alpha-methyllysine samples. Extend\n    the 2025\
    \ ortholog study after member mapping and Methods/figure assessment. Do not infer\
    \ cellular\n    decoding, drug efficacy or family-wide chemistry from these preparations.\
    \ Partial same-agent scientific\n    review; remain IN_PROGRESS.\n  posed_by:\
    \ Codex\n  posed_date: '2026-10-11'\ncausal_graphs:\n- graph_id: ecoli-tils-lysine-and-ethanolamine-products\n\
    \  title: TilS produces lysine- and ethanolamine-modified tRNA preparations\n\
    \  scope: Purified C-terminal His6 E. coli K12 TilS and transcribed E. coli tRNAIle2\
    \ in Salowe 2009 Table\n    4 reactions B/H, compared with no-amine reaction A.\
    \ Intact-RNA mass and gel migration support modification\n    products, not an\
    \ independently localized atomic pathway.\n  context: 75 ul, 50 mM TAPS pH 8.5,\
    \ 3 mM MgCl2, 0.5 mM TCEP, 0.1 mg/ml BSA, 20 uM transcript, 100 uM\n    ATP and\
    \ 500 nM TilS; 37 C for 4 h. Use 0.1 mM lysine in B or 20 mM ethanolamine in H.\
    \ Preparations\n    are frozen without further workup; product gels, intact-RNA\
    \ MS and residual-substrate radiolysine\n    assays are distinct readouts.\n \
    \ family_mapping: P52097/TILS_ECOLI, tilS/mesJ/yaeN/b0188, 432 aa, sequence version\
    \ 1. UniProt, InterPro\n    and cited Z50870.1/CAA90751.1 match exactly; PF01171\
    \ spans 10-197. Published primers match the coding\n    start and terminal WQKTLS,\
    \ excluding the native stop for a reported C-terminal His6 fusion. Complete\n\
    \    vector scar and experimental clone are not independently reconstructed.\n\
    \  scope_status: MECHANISTIC\n  taxon: NCBITaxon:83333\n  limitations: Whole TilS\
    \ also contains C-terminal tRNA-recognition domains. Neither isolated PP-loop\n\
    \    sufficiency nor a directly tracked adenylation/nucleophilic-attack sequence\
    \ follows from these data.\n    Raw spectra, exact modification-site localization,\
    \ replicate counts and uncertainty are unverified\n    here. N-alpha-methyllysine\
    \ and ornithine samples gave lysine-like products attributed to contamination,\n\
    \    not confirmed alternative incorporation.\n  nodes:\n  - node_id: tils-atp-transcript-lysine\n\
    \    label: Joint purified TilS, ATP, transcript and 0.1 mM lysine reaction\n\
    \    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:P52097\n  - node_id:\
    \ lysine-modified-trna-preparation\n    label: Reaction B tRNA product consistent\
    \ with lysine incorporation\n    node_type: STATE\n  - node_id: tils-atp-transcript-ethanolamine\n\
    \    label: Joint purified TilS, ATP, transcript and 20 mM ethanolamine reaction\n\
    \    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:P52097\n  - node_id:\
    \ ethanolamine-modified-trna-preparation\n    label: Reaction H tRNA product consistent\
    \ with ethanolamine incorporation\n    node_type: STATE\n  edges:\n  - edge_id:\
    \ tils-lysine-reaction-produces-modified-trna\n    subject: tils-atp-transcript-lysine\n\
    \    predicate: produces\n    object: lysine-modified-trna-preparation\n    mechanism:\
    \ Reaction B shifts the tRNA gel band and gives an intact mass consistent with\
    \ the expected\n      lysine-modified product. This supports net modification,\
    \ not independent proof of its exact bond\n      geometry or site from mass alone.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:19233850\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2665086/\n\
    \      snippet: modified tRNA products\n      explanation: Table 4 B versus A,\
    \ visually inspected Figure 2 B lanes and preparative Methods; the\n        mass\
    \ discrepancy is within the paper's reported error.\n      cache_path: evidence/PF01171/salowe-2009-tils.txt\n\
    \      cache_sha256: 544b2a00f2d9713060c325b735c83fc1b2beaf0313fdc01c6c21bcbe8822966d\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P52097/entry/pfam/PF01171/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P52097/entry/pfam/PF01171/\n\
    \      snippet: 'P52097 Pfam:PF01171 interval: 10-197, inclusive.'\n      explanation:\
    \ Exact reference and source-accession mapping; other TilS domains remain part\
    \ of the\n        experimental protein.\n      cache_path: evidence/PF01171/TilS-identity.txt\n\
    \      cache_sha256: b8259ad7ec4469d61461603e33b6d55118e11555a3295f8262cefe2f66975ab0\n\
    \  - edge_id: tils-ethanolamine-reaction-produces-modified-trna\n    subject:\
    \ tils-atp-transcript-ethanolamine\n    predicate: produces\n    object: ethanolamine-modified-trna-preparation\n\
    \    mechanism: Reaction H yields a shifted tRNA species and an intact mass consistent\
    \ with ethanolamine\n      addition. The 20 mM alternative substrate condition\
    \ is not evidence that this product normally occurs\n      in cells or that its\
    \ catalytic efficiency equals lysine's.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:19233850\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2665086/\n      snippet:\
    \ modified tRNA products\n      explanation: Table 4 H versus A and Figure 2 H\
    \ lane, distinct from the contaminated K/L reactions.\n      cache_path: evidence/PF01171/salowe-2009-tils.txt\n\
    \      cache_sha256: 544b2a00f2d9713060c325b735c83fc1b2beaf0313fdc01c6c21bcbe8822966d\n\
    - graph_id: ecoli-tils-preparations-s100-aminoacylation\n  title: TilS-modified\
    \ preparations change aminoacylation in E. coli extract\n  scope: Reaction B or\
    \ H preparations versus no-amine A in the separate E. coli S100 IleRS/MetRS activity\n\
    \    columns of Table 5. S100 is a partially purified mixed extract from BL21(DE3),\
    \ not either isolated\n    synthetase.\n  context: Dilute frozen modification\
    \ mixtures to 100 nM tRNA in 30 ul of 50 mM HEPES pH 7.3, 10 mM Mg(OAc)2,\n  \
    \  100 mM KCl, 0.5 mM TCEP, 0.1 mg/ml BSA, 100 uM ATP, 100 nM tritiated isoleucine\
    \ or methionine, and\n    40 ug/ml S100 protein. Two hours at room temperature,\
    \ followed by acidic SPA capture.\n  family_mapping: The modifying enzyme is intact\
    \ P52097-associated TilS, PF01171 10-197 plus its C-terminal\n    domains. S100\
    \ reporter enzymes and transcript are separate components; the graph does not\
    \ assign their\n    catalysis to PF01171.\n  scope_status: MECHANISTIC\n  taxon:\
    \ NCBITaxon:562\n  limitations: Preparations were not repurified, so residual\
    \ amine, ATP and TilS may carry over. The causal\n    comparison is between reaction\
    \ preparations, not purified RNAs proven to differ at only one atom.\n    Table\
    \ 5 columns use different normalization references; values are not absolute cross-enzyme\
    \ rates.\n    No replicate/error estimates or universal zero-activity threshold\
    \ are supplied, and no in-vivo AUA\n    decoding is measured here.\n  nodes:\n\
    \  - node_id: use-lysine-modified-preparation\n    label: Use lysine reaction\
    \ B preparation rather than no-amine A\n    node_type: PERTURBATION\n  - node_id:\
    \ use-ethanolamine-modified-preparation\n    label: Use ethanolamine reaction\
    \ H preparation rather than no-amine A\n    node_type: PERTURBATION\n  - node_id:\
    \ s100-isoleucine-incorporation\n    label: Isoleucine incorporation into tRNA\
    \ in the S100 assay\n    node_type: ACTIVITY\n  - node_id: s100-methionine-incorporation\n\
    \    label: Methionine incorporation into tRNA in the S100 assay\n    node_type:\
    \ ACTIVITY\n  edges:\n  - edge_id: lysine-preparation-increases-s100-isoleucine\n\
    \    subject: use-lysine-modified-preparation\n    predicate: increases\n    object:\
    \ s100-isoleucine-incorporation\n    mechanism: The B preparation supports a higher\
    \ isoleucine-incorporation signal than A, reported as\n      100 versus 2 on the\
    \ E. coli IleRS column's own scale. It is a preparation-level biochemical effect,\n\
    \      not a direct observation of anticodon hydrogen bonding.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:19233850\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2665086/\n\
    \      snippet: aminoacylation\n      explanation: Table 5 A/B E. coli IleRS column\
    \ and synthetase-assay Methods; normalized to B, not\n        tRNAMet.\n     \
    \ cache_path: evidence/PF01171/salowe-2009-tils.txt\n      cache_sha256: 544b2a00f2d9713060c325b735c83fc1b2beaf0313fdc01c6c21bcbe8822966d\n\
    \  - edge_id: lysine-preparation-decreases-s100-methionine\n    subject: use-lysine-modified-preparation\n\
    \    predicate: decreases\n    object: s100-methionine-incorporation\n    mechanism:\
    \ The B preparation gives less detected methionine incorporation than A, reported\
    \ as 0 versus\n      23 on the MetRS column's tRNAMet-normalized scale. This is\
    \ a bounded assay loss, not a universal\n      impossibility of methionylation.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:19233850\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2665086/\n\
    \      snippet: aminoacylation\n      explanation: Table 5 A/B E. coli MetRS column,\
    \ its distinct normalization footnote and matched assay\n        protocol.\n \
    \     cache_path: evidence/PF01171/salowe-2009-tils.txt\n      cache_sha256: 544b2a00f2d9713060c325b735c83fc1b2beaf0313fdc01c6c21bcbe8822966d\n\
    \  - edge_id: ethanolamine-preparation-increases-s100-isoleucine\n    subject:\
    \ use-ethanolamine-modified-preparation\n    predicate: increases\n    object:\
    \ s100-isoleucine-incorporation\n    mechanism: The H preparation increases isoleucine\
    \ incorporation relative to A, reported as 123 versus\n      2. The graph does\
    \ not interpret 123 versus B's 100 as a statistically established improvement\
    \ over\n      the natural modifier.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:19233850\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2665086/\n      snippet:\
    \ aminoacylation\n      explanation: Table 5 A/H E. coli IleRS column, linked\
    \ to the mass-supported Table 4 H preparation.\n      cache_path: evidence/PF01171/salowe-2009-tils.txt\n\
    \      cache_sha256: 544b2a00f2d9713060c325b735c83fc1b2beaf0313fdc01c6c21bcbe8822966d\n\
    \  - edge_id: ethanolamine-preparation-decreases-s100-methionine\n    subject:\
    \ use-ethanolamine-modified-preparation\n    predicate: decreases\n    object:\
    \ s100-methionine-incorporation\n    mechanism: The H preparation lowers detected\
    \ methionine incorporation relative to A, reported as 0\n      versus 23 on the\
    \ MetRS-specific scale. Carryover and detection limits remain explicit.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:19233850\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2665086/\n\
    \      snippet: aminoacylation\n      explanation: Table 5 A/H E. coli MetRS column,\
    \ not purified MetRS or an in-vivo decoding experiment.\n      cache_path: evidence/PF01171/salowe-2009-tils.txt\n\
    \      cache_sha256: 544b2a00f2d9713060c325b735c83fc1b2beaf0313fdc01c6c21bcbe8822966d\n\
    - graph_id: tils-preparations-bsubtilis-ilers\n  title: Modified E. coli tRNA\
    \ preparations support B. subtilis IleRS\n  scope: A deliberately mixed-species\
    \ biochemical system in Table 5, with E. coli TilS-treated E. coli\n    transcript\
    \ and purified B. subtilis 168 FLAG-IleRS. This is separate from the E. coli S100\
    \ experiment.\n  context: Reaction B or H preparations diluted to 100 nM tRNA,\
    \ 0.1 nM recombinant IleRS, 100 nM tritiated\n    isoleucine and 100 uM ATP in\
    \ the 30-ul HEPES pH 7.3 synthetase assay with 10 mM Mg(OAc)2. Two hours\n   \
    \ at room temperature; acidic SPA capture. Compare each preparation with no-amine\
    \ A.\n  family_mapping: P52097 TilS supplies PF01171 at 10-197 and produces the\
    \ tested preparations. The partner\n    accession Q45477 identifies B. subtilis\
    \ 168 IleRS, not a PP-loop-family enzyme. Its current sequence\n    version 3\
    \ is later than the 2009 experiment; complete historical FLAG construct identity\
    \ is not independently\n    reconstructed.\n  scope_status: MECHANISTIC\n  limitations:\
    \ This mixed-species result is not a native cellular pathway or evidence for B.\
    \ subtilis\n    TilS activity. The B/H preparations are unrepurified and may retain\
    \ reaction components. The reported\n    100/99 values have no supplied uncertainty\
    \ establishing equivalence, and the zero control is bounded\n    by assay detection.\
    \ No codon recognition or translation rate is measured.\n  nodes:\n  - node_id:\
    \ lysine-preparation-with-bsubtilis-ilers\n    label: Use reaction B rather than\
    \ A with purified B. subtilis IleRS\n    node_type: PERTURBATION\n  - node_id:\
    \ ethanolamine-preparation-with-bsubtilis-ilers\n    label: Use reaction H rather\
    \ than A with purified B. subtilis IleRS\n    node_type: PERTURBATION\n  - node_id:\
    \ bsubtilis-ilers-isoleucine-incorporation\n    label: Isoleucine incorporation\
    \ by the purified B. subtilis IleRS system\n    node_type: ACTIVITY\n    grounding:\n\
    \    - UniProtKB:Q45477\n  edges:\n  - edge_id: lysine-preparation-increases-bsubtilis-aminoacylation\n\
    \    subject: lysine-preparation-with-bsubtilis-ilers\n    predicate: increases\n\
    \    object: bsubtilis-ilers-isoleucine-incorporation\n    mechanism: The lysine-modified\
    \ preparation supports greater isoleucine incorporation than the no-amine\n  \
    \    preparation with purified B. subtilis IleRS. This does not transfer the exact\
    \ E. coli extract rate\n      or its enzyme composition.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:19233850\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2665086/\n\
    \      snippet: aminoacylation\n      explanation: Table 5 A/B B. subtilis column\
    \ and recombinant IleRS/assay Methods; 100 versus 0 on\n        that column's\
    \ scale.\n      cache_path: evidence/PF01171/salowe-2009-tils.txt\n      cache_sha256:\
    \ 544b2a00f2d9713060c325b735c83fc1b2beaf0313fdc01c6c21bcbe8822966d\n  - edge_id:\
    \ ethanolamine-preparation-increases-bsubtilis-aminoacylation\n    subject: ethanolamine-preparation-with-bsubtilis-ilers\n\
    \    predicate: increases\n    object: bsubtilis-ilers-isoleucine-incorporation\n\
    \    mechanism: The ethanolamine-modified preparation also supports increased\
    \ incorporation relative to\n      A, reported as 99 versus 0. Similarity to B\
    \ is not treated as proof of identical kinetics or physiological\n      substitution\
    \ of ethanolamine for lysine.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:19233850\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2665086/\n      snippet:\
    \ aminoacylation\n      explanation: Table 5 A/H B. subtilis column and Table\
    \ 4 H identity, with mixed-species and carryover\n        qualifications.\n  \
    \    cache_path: evidence/PF01171/salowe-2009-tils.txt\n      cache_sha256: 544b2a00f2d9713060c325b735c83fc1b2beaf0313fdc01c6c21bcbe8822966d\n\
    curation_events:\n- timestamp: '2026-10-11T09:32:43Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Add scoped TilS modification and aminoacylation\
    \ graphs\n  history_record: history/records/PF01171/2026-10-11T093243Z-codex-7ffe62.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: P52097/TILS_ECOLI, 432 aa and sequence version 1, exactly matches InterPro
    and the paper's Z50870.1/CAA90751.1 translation, with PF01171 at 10-197. Forward
    primer matches the coding start; the reverse primer matches terminal WQKTLS and
    omits the stop, consistent with the reported C-terminal His6 fusion. Exact vector
    scar/full clone is not independently reconstructed. Q45477 identifies the distinct
    B. subtilis 168 IleRS partner; its current version 3 sequence is later than the
    experiment and is not presented as independent proof of the historical FLAG clone.
    E. coli S100 is a mixed extract.
  target_ids:
  - PF01171
  evidence_ids:
  - identity
  - primary
  - cited-sequence-and-primer-check
  - later-ortholog-coverage-lead
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Two product edges retain joint inputs and the 0.1 mM lysine versus 20 mM
    ethanolamine conditions. Intact mass and migration do not independently localize
    the reaction or visualize the adenylated intermediate. Six aminoacylation edges
    compare unrepurified reaction preparations with no-amine control A, not purified
    RNAs proven to differ only at one site. E. coli MetRS, E. coli IleRS and B. subtilis
    IleRS have distinct normalizations and biochemical preparations; their numbers
    are not one absolute scale. Reported zeros, 123 versus 100 and 99 versus 100 are
    not universal absence, significant superiority or kinetic equivalence. No in-vivo
    decoding or family-wide mechanism is inferred.
  target_ids:
  - PF01171
  evidence_ids:
  - primary
  - native
  - cited-sequence-and-primer-check
  - later-ortholog-coverage-lead
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Raw MS, site-specific chemical identification, historical clone scars,
    preparation carryover controls, replicate counts and rate uncertainty remain incomplete.
    Original intermediate/recognition studies and remaining genuine alternative substrates
    require separate assessment. The 2025 abstract and selected near-cognate-discrimination
    Results were inspected, but their Methods, figures and ortholog mapping remain
    unreviewed. The historical neighboring rof/cell-cycle annotation is not adopted
    for TilS.
  target_ids:
  - PF01171
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01171-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Strengthen TilS chemical localization and ortholog-specific assay coverage
  description: Obtain exact constructs, matched carryover controls and uncertainty
    estimates; inspect original intermediate and recognition studies before adding
    atomic steps. Curate remaining alternative substrates without accepting contaminated
    samples or isotope dilution as direct inhibition. Extend the 2025 ortholog study
    through Methods, figures and exact member mapping, keeping species and transcript-preparation
    boundaries explicit. Retain a successor scientific review before status promotion.
  target_ids:
  - PF01171
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - cited-sequence-and-primer-check
  - later-ortholog-coverage-lead
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01171.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Obtain exact constructs, matched carryover controls and uncertainty
    estimates; inspect original intermediate and recognition studies before adding
    atomic steps. Curate remaining alternative substrates without accepting contaminated
    samples or isotope dilution as direct inhibition. Extend the 2025 ortholog study
    through Methods, figures and exact member mapping, keeping species and transcript-preparation
    boundaries explicit. Retain a successor scientific review before status promotion.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01171
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Main 2009 Methods/Results/Discussion and Tables 1-5 were read; Figure 2 was visually
  inspected. Raw mass spectra, Figure 3's proposed hydrogen-bond model and full clone/vector
  sequences were not reanalyzed. The 2025 abstract and one Results subsection/caption
  are only a coverage lead, not a completed review of that study or a source of new
  edges.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
