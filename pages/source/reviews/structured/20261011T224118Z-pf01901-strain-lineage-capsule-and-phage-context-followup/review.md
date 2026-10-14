# PF01901 strain lineage and selected capsule and phage context follow-up

- Review: 20261011T224118Z-pf01901-strain-lineage-capsule-and-phage-context-followup
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T22:39:08Z
- Finished UTC: 2026-10-11T22:41:18Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Seven PHENOTYPIC graphs now retain eight OBSERVED, INDIRECT effects. Three added graphs capture three separate capsule/LPS readouts and one phage complementation contrast; four earlier graph IDs and evidence ledgers remain. ATCC authority resolves the strain-lineage relationship. Two discussions remain open. This successor partial same-agent scientific review refines the earlier assessment without erasing its history or approving the family as complete. Status remains IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01901, former DUF70; seven O157 phenotype graphs and corrected reference-strain lineage.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01901 | data/families/PF01901.yaml | generated | PF01901 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01901 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: concern. Targets: PF01901.

Official ATCC documents700927 as derived from43895, resolving the previously unexplained catalog relationship, not sequencing the actual assay stock. CP041623.1 ATCC43888 CDS FNZ21_14180/QDZ55367.1 exactly matches Q8X4T7 and its start matches the Park2021 displayed cluster start. Shifrin2008 Table1 identifies SK2526 as the TUV93-0 insertion derivative with a Sakai-origin allele. Current references support member mapping, but exact historical alleles and complementation clone are unverified. The partial PF01901 match8-205 of394aa, score0.041, does not establish a catalytic boundary.

### Directed effects and limits

graph: supported. Targets: PF01901.

Nodes, directions and evidence preserve distinct ATCC43895, SK2526 and ATCC43888 contexts. Figure3B fractions are separate readouts, not a causal chain. Actual Park Figure4C supports complemented versus uncomplemented clearing; it does not supply a separate WT comparison, direct Wzy-phage binding or quantified infection efficiency. ECP26 clearing is retained. No cross-strain rescue, isolated-domain mechanism or universal glycan loss is inferred. Original four phenotype graphs retain residual and negative findings and source reporting conflicts. Evidence hashes and stable IDs are intact; historical files are unchanged.

### Remaining family coverage

completeness: concern. Targets: PF01901.

Selected2008 and2021 primary contexts now have inspected full text and original figures. Their supplements and additional host-interaction contexts are not certified. The2004 paper remains inaccessible through attempted endpoints. Exact historical alleles, expression controls, partial domain reassessment, source inconsistencies and most237 family members remain open, including archaeal physiology and FPC840 current mapping. Annotation absence is not evidence that functional literature does not exist.

## Findings

### additional-contexts: Resolve exact assay alleles and extend member-specific primary coverage

minor / open / confirmed; issue key: pf01901-causal-context-coverage.

The ATCC700927/43895 lineage issue is resolved by authority evidence, but actual experimental stock and allele sequences remain unresolved. Reassess short family mapping, inspect remaining primary contexts and assay-matched controls, and reconcile the2008 temperature/species,2021 panel-label and2024 concentration/duration reporting conflicts. Keep strain-specific rescue separate. New supported claims require overlay curation, real history, guarded regeneration and a successor review; the same coverage issue stays open.

## Recommended Actions And Acceptance Checks

### extend-contexts

The ATCC700927/43895 lineage issue is resolved by authority evidence, but actual experimental stock and allele sequences remain unresolved. Reassess short family mapping, inspect remaining primary contexts and assay-matched controls, and reconcile the2008 temperature/species,2021 panel-label and2024 concentration/duration reporting conflicts. Keep strain-specific rescue separate. New supported claims require overlay curation, real history, guarded regeneration and a successor review; the same coverage issue stays open.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC2447026/; Table1, selected Methods/Results and visually inspected original Figure3A/B. | supports | SK2526 has reduced ferritin-associated surface material, polymeric anti-O157 LPS signal and capsular-fraction dot signal in three qualitative contrasts. Residual lower LPS material remains. No Wzy rescue was performed; etp/etk rescue cannot substitute. Caption temperature and EPEC/EHEC wording conflict with the other inspected source context and remain explicit. |
| identity | https://www.ncbi.nlm.nih.gov/nuccore/CP041623.1; Accession and domain locations; paired UniProt identity facts | supports | Official ATCC documents700927 as derived from43895, resolving the previously unexplained catalog relationship, not sequencing the actual assay stock. CP041623.1 ATCC43888 CDS FNZ21_14180/QDZ55367.1 exactly matches Q8X4T7 and its start matches the Park2021 displayed cluster start. Shifrin2008 Table1 identifies SK2526 as the TUV93-0 insertion derivative with a Sakai-origin allele. Current references support member mapping, but exact historical alleles and complementation clone are unverified. The partial PF01901 match8-205 of394aa, score0.041, does not establish a catalytic boundary. |
| phage-context | https://pmc.ncbi.nlm.nih.gov/articles/PMC8402813/; Selected Methods/Results and original Figure4, especially actual panelC. | supports | ATCC43888 complementation restores BECP10 clearing, with ECP26 retained; caption labels conflict and other-strain rescue is not implied. |
| strain-authority | https://www.atcc.org/products/700927; Product strain derivation and genome-project culture description. | supports | The catalog lineage is known; identity of the historical experimental stock is a separate limit. |
| original-identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01901/; Prior frozen identity and exact protein comparisons; strain-lineage wording refined by this successor. | supports | Frozen PF01901 identity, archaeal mappings and weak partial O157 membership are preserved without upgrading domain attribution. |
| original-mutant | https://pmc.ncbi.nlm.nih.gov/articles/PMC7232329/; Previously inspected original Figure1, Table1 and selected wzy text. | supports | Tube staining decreases while intracellular recovery is retained; csgB rescue does not rescue wzy. |
| later-mutant-contexts | https://pmc.ncbi.nlm.nih.gov/articles/PMC11394844/; Previously inspected original Figures1/2/4/5 and selected text. | supports | Residual LPS, biomass, flagellin and Congo-red binding constrain decreases in measured readouts; no allele-specific rescue was established. |
| historical-review | reviews/structured/20261011T222500Z-pf01901-o157-wzy-insertion-phenotypes-and-mapping-limits/review.yaml; Previous partial self-review; historical assessment preserved, not approval of changed content. | supports | The present report refines known strain lineage and selected primary coverage while retaining the open issue key. |
| followup-search-limits | evidence/PF01901/followup-gaps.txt; Dated source search, inspected context and actual access failures. | supports | Primary evidence gained, unresolved domain/allele mapping and source access limits remain explicit. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01901 | data/families/PF01901.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Original2008 Figure3 and2021 Figure4 were inspected in this follow-up; prior2020 Figure1 and2024 Figures1/2/4/5 assessments and evidence were retained. No raw-data reanalysis, exact clone sequencing, inaccessible supplement inspection, independent replication or exhaustive family audit is claimed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T224118Z-pf01901-strain-lineage-capsule-and-phage-context-followup
title: PF01901 strain lineage and selected capsule and phage context follow-up
started_at: '2026-10-11T22:39:08Z'
finished_at: '2026-10-11T22:41:18Z'
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
summary: Seven PHENOTYPIC graphs now retain eight OBSERVED, INDIRECT effects. Three
  added graphs capture three separate capsule/LPS readouts and one phage complementation
  contrast; four earlier graph IDs and evidence ledgers remain. ATCC authority resolves
  the strain-lineage relationship. Two discussions remain open. This successor partial
  same-agent scientific review refines the earlier assessment without erasing its
  history or approving the family as complete. Status remains IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01901.yaml
    sha256: f3b9fdfeaaede319b5a79caedb9ee0de974dd645595e994d5266b07796721724
    role: context
  - path: data/families/PF01901.yaml
    sha256: af6b6052ab5c9e26d504db21ad9d3a8df660aa98a3e0fb5c786fc48df877eeb7
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
  - path: evidence/PF01901/shifrin-2008.txt
    role: context
    sha256: 0a0b45ec1b69fb4611f6eaa1343c54187468907d84cd9326ab9bd24b7af8e231
  - path: evidence/PF01901/identity-followup.txt
    role: context
    sha256: 0c4c39e0c2da677935c22d1fc00c1fda96aff649425451fb273033d2506e6034
  - path: evidence/PF01901/park-2021.txt
    role: context
    sha256: 5365e1b63ba290b8b4a09f752746b03f06003d7b7a5cfd7e45eb2587ed810462
  - path: evidence/PF01901/identity.txt
    role: context
    sha256: fbb1cdb3f9c8b85b3199aae8d47d2e5df70fb8b165e013cb04d40e5a7e8f2bb9
  - path: evidence/PF01901/sheng-2020.txt
    role: context
    sha256: 9f6de06da18e36eba66965e742ceb73f2534a692136d663e5c39849da6adb905
  - path: evidence/PF01901/sheng-2024.txt
    role: context
    sha256: 7ab1fdc0f56fa8bed1b36c6d9b2e386f61f0dee1549bc70e71ebb37d61ff0125
  - path: reviews/structured/20261011T222500Z-pf01901-o157-wzy-insertion-phenotypes-and-mapping-limits/review.yaml
    role: context
    sha256: 260f83ce0d29b07b5b2527ee7e4e74d7ec6bdac4ef139bdb388041f13b66b98f
  - path: evidence/PF01901/followup-gaps.txt
    role: context
    sha256: 74d7580ca92b04c6f7a74543771781cb20a49e7237e795e11dd0dc07a6623cb2
targets:
- target_id: PF01901
  path: data/families/PF01901.yaml
  label: PF01901
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01901.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 18b72f171e4f8e5944b53ffa944d5adcf36a77d2763d96b13a4ee0e9372ec331
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01901, former DUF70; seven O157 phenotype graphs and corrected reference-strain
    lineage.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01901
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Selected2008 and2021 primary contexts now have inspected full text and
      original figures. Their supplements and additional host-interaction contexts
      are not certified. The2004 paper remains inaccessible through attempted endpoints.
      Exact historical alleles, expression controls, partial domain reassessment,
      source inconsistencies and most237 family members remain open, including archaeal
      physiology and FPC840 current mapping. Annotation absence is not evidence that
      functional literature does not exist.
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
  - PF01901
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2447026/
  locator: Table1, selected Methods/Results and visually inspected original Figure3A/B.
  accessed_at: '2026-10-11T22:41:18Z'
  support: supports
  snapshot_sha256: 0a0b45ec1b69fb4611f6eaa1343c54187468907d84cd9326ab9bd24b7af8e231
  summary: SK2526 has reduced ferritin-associated surface material, polymeric anti-O157
    LPS signal and capsular-fraction dot signal in three qualitative contrasts. Residual
    lower LPS material remains. No Wzy rescue was performed; etp/etk rescue cannot
    substitute. Caption temperature and EPEC/EHEC wording conflict with the other
    inspected source context and remain explicit.
- evidence_id: identity
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/nuccore/CP041623.1
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T22:41:18Z'
  support: supports
  snapshot_sha256: 0c4c39e0c2da677935c22d1fc00c1fda96aff649425451fb273033d2506e6034
  summary: Official ATCC documents700927 as derived from43895, resolving the previously
    unexplained catalog relationship, not sequencing the actual assay stock. CP041623.1
    ATCC43888 CDS FNZ21_14180/QDZ55367.1 exactly matches Q8X4T7 and its start matches
    the Park2021 displayed cluster start. Shifrin2008 Table1 identifies SK2526 as
    the TUV93-0 insertion derivative with a Sakai-origin allele. Current references
    support member mapping, but exact historical alleles and complementation clone
    are unverified. The partial PF01901 match8-205 of394aa, score0.041, does not establish
    a catalytic boundary.
- evidence_id: phage-context
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8402813/
  locator: Selected Methods/Results and original Figure4, especially actual panelC.
  summary: ATCC43888 complementation restores BECP10 clearing, with ECP26 retained;
    caption labels conflict and other-strain rescue is not implied.
  accessed_at: '2026-10-11T22:41:18Z'
  support: supports
  snapshot_sha256: 5365e1b63ba290b8b4a09f752746b03f06003d7b7a5cfd7e45eb2587ed810462
- evidence_id: strain-authority
  kind: authority
  reference: https://www.atcc.org/products/700927
  locator: Product strain derivation and genome-project culture description.
  summary: The catalog lineage is known; identity of the historical experimental stock
    is a separate limit.
  accessed_at: '2026-10-11T22:41:18Z'
  support: supports
  snapshot_sha256: 0c4c39e0c2da677935c22d1fc00c1fda96aff649425451fb273033d2506e6034
- evidence_id: original-identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01901/
  locator: Prior frozen identity and exact protein comparisons; strain-lineage wording
    refined by this successor.
  summary: Frozen PF01901 identity, archaeal mappings and weak partial O157 membership
    are preserved without upgrading domain attribution.
  accessed_at: '2026-10-11T22:41:18Z'
  support: supports
  snapshot_sha256: fbb1cdb3f9c8b85b3199aae8d47d2e5df70fb8b165e013cb04d40e5a7e8f2bb9
- evidence_id: original-mutant
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7232329/
  locator: Previously inspected original Figure1, Table1 and selected wzy text.
  summary: Tube staining decreases while intracellular recovery is retained; csgB
    rescue does not rescue wzy.
  accessed_at: '2026-10-11T22:41:18Z'
  support: supports
  snapshot_sha256: 9f6de06da18e36eba66965e742ceb73f2534a692136d663e5c39849da6adb905
- evidence_id: later-mutant-contexts
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC11394844/
  locator: Previously inspected original Figures1/2/4/5 and selected text.
  summary: Residual LPS, biomass, flagellin and Congo-red binding constrain decreases
    in measured readouts; no allele-specific rescue was established.
  accessed_at: '2026-10-11T22:41:18Z'
  support: supports
  snapshot_sha256: 7ab1fdc0f56fa8bed1b36c6d9b2e386f61f0dee1549bc70e71ebb37d61ff0125
- evidence_id: historical-review
  kind: prior_review
  reference: reviews/structured/20261011T222500Z-pf01901-o157-wzy-insertion-phenotypes-and-mapping-limits/review.yaml
  locator: Previous partial self-review; historical assessment preserved, not approval
    of changed content.
  summary: The present report refines known strain lineage and selected primary coverage
    while retaining the open issue key.
  accessed_at: '2026-10-11T22:41:18Z'
  support: supports
  snapshot_sha256: 260f83ce0d29b07b5b2527ee7e4e74d7ec6bdac4ef139bdb388041f13b66b98f
- evidence_id: followup-search-limits
  kind: search
  reference: evidence/PF01901/followup-gaps.txt
  locator: Dated source search, inspected context and actual access failures.
  search_scope: Ignored/hidden-inclusive local checks for QDZ55367, SK2526, BECP10
    and strain derivation; public authority and versioned GenBank checks;2004, 2008
    and2021 primary-source searches. Uninspected challenge responses, non-PDF HTML
    and timed-out partial archive are not negative evidence.
  summary: Primary evidence gained, unresolved domain/allele mapping and source access
    limits remain explicit.
  accessed_at: '2026-10-11T22:41:18Z'
  support: supports
  snapshot_sha256: 74d7580ca92b04c6f7a74543771781cb20a49e7237e795e11dd0dc07a6623cb2
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T22:41:18Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01901
  kind: record_content
  reference: data/families/PF01901.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T22:41:18Z'
  support: context_only
  snapshot_sha256: af6b6052ab5c9e26d504db21ad9d3a8df660aa98a3e0fb5c786fc48df877eeb7
  quote: "id: Pfam:PF01901\npfam_id: PF01901\nname: Putative O-antigen polymerase\n\
    short_name: O_anti_polymase\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01901\n\
    counters:\n  proteins: 237\n  matches: 285\n  proteomes: 164\n  taxa: 385\n  structures:\
    \ 0\n  alphafold_models: 186\n  domain_architectures: 2\nprovenance:\n  snapshot_id:\
    \ interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002760\ndescription: Archaebacterial proteins of unknown\
    \ function. Members of this family may be transmembrane\n  proteins. These are\
    \ potentially O-antigen assembly enzymes, with up to 11 transmembrane regions.\n\
    curation_history: history/records/PF01901\ndiscussions:\n- discussion_id: duf70-assay-identity-and-attribution\n\
    \  prompt: Resolve exact experimental wzy alleles and assay reporting before assigning\
    \ a domain mechanism.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: Whole-cell\
    \ insertion effects support the measured directions but do not isolate Wzy chemistry,polar\n\
    \    effects or a PF01901 catalytic segment. Current O157 membership is a short\
    \ score0.041 hit,unlike the\n    strong archaeal matches.\n  evidence:\n  - reference:\
    \ https://www.atcc.org/products/700927\n    supports: SUPPORT\n    evidence_source:\
    \ culture_collection_authority\n    explanation: ATCC establishes the700927-to-43895derivative\
    \ relationship. Earlier unexplained-lineage\n      wording is refined,not converted\
    \ into proof of an exact historical assay sequence.\n  - reference: PMID:34452334\n\
    \    supports: PARTIAL\n    evidence_source: selected_full_text_and_figure\n \
    \   explanation: ATCC43888 complementation supports its spot-clearing contrast,not\
    \ rescue of another strain's\n      allele. Its matched QDZ55367.1 reference improves\
    \ identity grounding without sequencing the plasmid.\n  - reference: PMID:39273173\n\
    \    supports: PARTIAL\n    evidence_source: selected_full_text_and_figures\n\
    \    explanation: Figures1/2/4 retain long-O-antigen,biomass and halo reductions;\
    \ residual signal,flagellin\n      and Congo-red binding constrain interpretation.\
    \ The cited CP008957 reference equals Q8X4T7 but names\n      ATCC700927,not an\
    \ independently sequenced ATCC43895 culture. Glucose and duration discrepancies\n\
    \      remain unresolved.\n  - reference: PMID:32316415\n    supports: PARTIAL\n\
    \    evidence_source: selected_full_text_and_figure\n    explanation: Figure1B\
    \ supports reduced tube staining;1D does not show the csgB-like invasion reduction\n\
    \      for wzy. csgB rescue must not become wzy rescue. The later study reuses\
    \ this mutant.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n  notes: Seven\
    \ graphs retain eight indirect observed effects,not purified polymerization or\
    \ a family-wide\n    assignment. The strain lineage is resolved,but exact alleles,downstream-expression\
    \ controls and assay-matched\n    controls remain open. ATCC43888 rescue is separate\
    \ from the unrescued2008/2020/2024contexts. New evidence\n    supplements historical\
    \ ledgers without overwriting them.\n- discussion_id: duf70-primary-context-and-family-coverage\n\
    \  prompt: Inspect additional O157 primary experiments and archaeal members without\
    \ transferring other\n    Wzy families.\n  kind: CURATION_TODO\n  status: OPEN\n\
    \  rationale: The237 frozen proteins are not covered by these O157 contexts. Reviewed\
    \ Q57862/MJ0419 and\n    Q57863/MJ0420 are uncharacterized in the inspected annotation;\
    \ this is not proof of absent experiments.\n    EX_DUF naming and clanCL0499 do\
    \ not establish universal polymerase chemistry.\n  evidence:\n  - reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01901/\n\
    \    supports: PARTIAL\n    evidence_source: database\n    explanation: Current\
    \ family metadata remains tentative. Exact sequence comparisons map four references;\n\
    \      archaeal PF01901 intervals are11-336 and14-363,whereas O157 is8-205. O85335\
    \ and Q8X4T7 differ at234.\n  - reference: PMID:28955320\n    supports: PARTIAL\n\
    \    evidence_source: selected_full_text_and_table\n    explanation: FPC840_340035\
    \ has a Table3 HHpredPF01901 relationship but no reported InterProScan hit.\n\
    \      Comparative genomics and serotype PCR are not gene-perturbation evidence;\
    \ current sequence mapping\n      remains open.\n  posed_by: Codex\n  posed_date:\
    \ '2026-10-11'\n  notes: Selected2008capsule and2021BECP10evidence is now inspected;\
    \ their additional contexts and supplements\n    remain bounded. The2004doi10.1074/jbc.M401879200full\
    \ paper remains inaccessible through attempted\n    endpoints. O86purified Wzy\
    \ is reportedPF14296,not transferable here. No molybdate edge follows from\n \
    \   Q6LY80's submitted name. Keep IN_PROGRESS pending member-specific evidence.\n\
    causal_graphs:\n- graph_id: o157-wzy-tn5-tube-staining-2020\n  title: Wzy disruption\
    \ reduces tube biofilm staining in the tested O157 strain\n  scope: Sheng2020\
    \ Figure1B; ATCC43895 wzy-Tn5 versus its parental culture.\n  context: Qualitative\
    \ crystal-violet tube assay at37 C under static conditions. The30 C library screen\n\
    \    is a separate assay, not a replicate of this endpoint.\n  family_mapping:\
    \ The2024follow-up cites CP008957.1; AIG69277.1/EDL933_3111 equals Q8X4T7/BAB36267.1,394\n\
    \    aa,PF01901 8-205,score0.041. ATCC documents ATCC700927 as derived from ATCC43895.\
    \ Their lineage relationship\n    is established; the experimental stock, insertion\
    \ junction and affected domain segment are not independently\n    sequenced here.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:83334\n  limitations: No Wzy-specific\
    \ rescue or downstream-expression control was established. csgB complementation\n\
    \    is not wzy rescue. The later2024study retains residual biofilm under its\
    \ conditions; do not infer\n    universal absence or direct PF01901 chemistry.\n\
    \  nodes:\n  - node_id: wzy-insertion\n    label: Reported wzy-Tn5 allele in the\
    \ ATCC43895 background\n    node_type: PERTURBATION\n  - node_id: tube-staining\n\
    \    label: Retained crystal-violet tube-ring staining\n    node_type: PHENOTYPE\n\
    \  edges:\n  - edge_id: insertion-decreases-tube-staining\n    subject: wzy-insertion\n\
    \    predicate: decreases\n    object: tube-staining\n    mechanism: The named\
    \ wzy-Tn5 tube has much less ring staining than the parental43895 tube. This whole-cell\n\
    \      phenotype does not resolve biomass,attachment,dye retention or polar contributions.\
    \ Comparable intracellular\n      recovery in Figure1D is not converted into an\
    \ invasion-defect edge.\n    directness: INDIRECT\n    support: OBSERVED\n   \
    \ evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:32316415\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7232329/\n      snippet:\
    \ biofilm-negative\n      explanation: Original Figure1B and its caption establish\
    \ the qualitative tube contrast; Table1 names\n        wzy-Tn5. Original1D constrains\
    \ invasion claims. The insertion was mapped by the authors,not independently\n\
    \        sequenced in this review.\n      cache_path: evidence/PF01901/sheng-2020.txt\n\
    \      cache_sha256: 9f6de06da18e36eba66965e742ceb73f2534a692136d663e5c39849da6adb905\n\
    - graph_id: o157-wzy-tn5-lps-2024\n  title: The wzy-Tn5 culture has reduced long-O-antigen\
    \ LPS signal\n  scope: Sheng2024 Figure1B; ATCC43895 wzy-Tn5 versus parental LPS.\n\
    \  context: Silver-stained Tricine-SDS-PAGE of whole-cell LPS preparations. Figure1A\
    \ is an expected-structure\n    schematic,not a purified polymerase experiment\
    \ or complete chemical structure determination.\n  family_mapping: CP008957.1/AIG69277.1\
    \ equals Q8X4T7/BAB36267.1,with PF01901 at8-205 of394 aa,score0.041.\n    ATCC700927\
    \ is a documented derivative of ATCC43895,not independently sequenced assay DNA.\
    \ O85335/AAC32340.1\n    differs at234 and is not substituted; the historical\
    \ insertion remains unverified.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:83334\n\
    \  limitations: The actual genotype is Tn5,not a verified clean delta-wzy deletion\
    \ despite the schematic\n    label. No allele-specific rescue,exact insertion\
    \ position or neighboring-expression measurement was\n    established. The weak\
    \ partial family hit does not establish an isolated catalytic domain or archaeal\n\
    \    transfer.\n  nodes:\n  - node_id: wzy-insertion\n    label: Reported wzy-Tn5\
    \ allele in the ATCC43895 background\n    node_type: PERTURBATION\n  - node_id:\
    \ long-o-antigen-signal\n    label: Long-O-antigen LPS gel signal\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: insertion-decreases-long-o-antigen\n    subject:\
    \ wzy-insertion\n    predicate: decreases\n    object: long-o-antigen-signal\n\
    \    mechanism: The mutant lane loses the parental long-O-antigen signal while\
    \ retaining a lower band assigned\n      to one repeat unit. This supports a strain-scoped\
    \ LPS assembly contribution without demonstrating\n      purified Wzy chemistry,processivity\
    \ or a particular glycosidic linkage.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:39273173\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11394844/\n      snippet:\
    \ single O-antigen unit\n      explanation: Visually inspected Figure1B is the\
    \ observed gel; Figure1A supplies an interpretation,not\n        an independent\
    \ chemical assay. Table1 identifies reuse of the2020insertion mutant.\n      cache_path:\
    \ evidence/PF01901/sheng-2024.txt\n      cache_sha256: 7ab1fdc0f56fa8bed1b36c6d9b2e386f61f0dee1549bc70e71ebb37d61ff0125\n\
    - graph_id: o157-wzy-tn5-microtiter-biomass-2024\n  title: Wzy disruption reduces\
    \ retained microtiter biofilm staining\n  scope: Sheng2024 Figure2B; ATCC43895\
    \ wzy-Tn5 versus parental culture.\n  context: Crystal-violet microtiter endpoint\
    \ at37 C after24h. Methods says MSM with0.04%glucose but the\n    caption says4%;\
    \ this source discrepancy is unresolved. Caption reports six assays per strain,mean/SD\n\
    \    and ANOVA with Dunnett comparison.\n  family_mapping: CP008957.1/AIG69277.1\
    \ equals Q8X4T7/BAB36267.1,394 aa,PF01901 8-205,score0.041. ATCC700927\n    is\
    \ a documented derivative of ATCC43895. Exact experimental-stock sequence and\
    \ insertion remain unresolved;\n    this is not a verified domain-specific perturbation.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:83334\n  limitations: Lower staining\
    \ is not complete biofilm loss; Figure2A retains a weaker ring. Tube duration\n\
    \    is overnight in Methods versus48h in caption/Results. Figure3 does not supply\
    \ a matched wzy growth\n    curve. No Wzy-specific rescue was established; reused2020allele\
    \ is not an independent genotype replication.\n  nodes:\n  - node_id: wzy-insertion\n\
    \    label: Reported wzy-Tn5 allele in the ATCC43895 background\n    node_type:\
    \ PERTURBATION\n  - node_id: retained-cv-signal\n    label: Microtiter retained\
    \ crystal-violet absorbance\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ insertion-decreases-cv-signal\n    subject: wzy-insertion\n    predicate: decreases\n\
    \    object: retained-cv-signal\n    mechanism: The wzy-Tn5 bar is below parental43895\
    \ with the caption's p<0.01 comparison. Residual signal\n      remains. Altered\
    \ attachment,biomass,dye retention or envelope effects are not separated; no causal\n\
    \      chain from the LPS band to this readout is inferred from their co-occurrence.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:39273173\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11394844/\n\
    \      snippet: wzy-Tn5\n      explanation: Original Figure2B and its caption\
    \ establish the directional comparison and reported\n        statistics. Original2A\
    \ retains a ring. The glucose,time and plotted-versus-text mean discrepancies\n\
    \        remain explicit instead of supplying a false exact protocol or effect\
    \ size.\n      cache_path: evidence/PF01901/sheng-2024.txt\n      cache_sha256:\
    \ 7ab1fdc0f56fa8bed1b36c6d9b2e386f61f0dee1549bc70e71ebb37d61ff0125\n- graph_id:\
    \ o157-wzy-tn5-motility-2024\n  title: Wzy disruption reduces but does not abolish\
    \ motility-halo spread\n  scope: Sheng2024 Figure4; ATCC43895 wzy-Tn5 versus parental\
    \ culture.\n  context: Soft-agar population-spread endpoint. Methods/caption report40h\
    \ while Results says48h. Caption\n    gives three repeats,mean/SD,two-tailed unpaired\
    \ t-test and p<0.01 for the wzy contrast.\n  family_mapping: CP008957.1/AIG69277.1\
    \ equals Q8X4T7/BAB36267.1,PF01901 8-205 of394 aa,score0.041. ATCC700927\n   \
    \ derives from ATCC43895 according to ATCC. The historical assay stock and insertion\
    \ are not independently\n    verified; no residue-specific archaeal mechanism\
    \ follows.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:83334\n  limitations:\
    \ Residual spread and the flagellin immunoblot band remain. Halo diameter is not\
    \ motor speed\n    or flagellum abundance. No Wzy-specific rescue or matched wzy\
    \ growth control was established. Retained\n    Congo-red binding in Figure5 also\
    \ excludes a complete-curli-loss claim.\n  nodes:\n  - node_id: wzy-insertion\n\
    \    label: Reported wzy-Tn5 allele in the ATCC43895 background\n    node_type:\
    \ PERTURBATION\n  - node_id: motility-halo\n    label: Soft-agar motility-halo\
    \ diameter\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: insertion-decreases-halo\n\
    \    subject: wzy-insertion\n    predicate: decreases\n    object: motility-halo\n\
    \    mechanism: The wzy-Tn5 halo is smaller but nonzero compared with WT. The\
    \ same figure retains a flagellin\n      band,so neither absence of flagella nor\
    \ direct inhibition of their biosynthesis follows. Envelope,motility\n      and\
    \ growth contributions remain unresolved.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:39273173\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11394844/\n      snippet:\
    \ impaired motility\n      explanation: Original Figure4 upper bars and lower\
    \ immunoblot were inspected together. Figure5 retains\n        wzy Congo-red binding.\
    \ The40h/48h discrepancy and lack of allele-specific rescue prevent stronger\n\
    \        mechanistic attribution.\n      cache_path: evidence/PF01901/sheng-2024.txt\n\
    \      cache_sha256: 7ab1fdc0f56fa8bed1b36c6d9b2e386f61f0dee1549bc70e71ebb37d61ff0125\n\
    - graph_id: o157-sk2526-surface-coat-2008\n  title: The SK2526 insertion mutant\
    \ has less ferritin-associated surface material\n  scope: Shifrin2008 Figure3A;\
    \ reported wzy insertion versus parental EHEC context.\n  context: Representative\
    \ thin-section microscopy. Figure3 caption gives30 C,EM Methods37 C; the discrepancy\n\
    \    remains unresolved. The caption's EPEC wording conflicts with the EHEC heading\
    \ and Results.\n  family_mapping: Table1 assigns SK2526 to TUV93-0,an EDL933 derivative,and\
    \ identifies a Sakai-origin\n    allele. Sakai Q8X4T7/BAB36267.1 equals EDL933\
    \ AIG69277.1; PF01901 8-205 of394 aa,score0.041. Exact\n    historical allele\
    \ sequence is unverified; no O127 transfer is made.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:83334\n  limitations: Representative images do not quantify\
    \ capsule mass. No Wzy rescue was performed; etp/etk\n    complementation is not\
    \ interchangeable. Staining,assembly and abundance explanations remain unresolved.\n\
    \  nodes:\n  - node_id: sk2526-insertion\n    label: SK2526 wzy insertion in the\
    \ TUV93-0 background\n    node_type: PERTURBATION\n  - node_id: ferritin-coat\n\
    \    label: Ferritin-associated surface-coat signal\n    node_type: PHENOTYPE\n\
    \  edges:\n  - edge_id: insertion-decreases-coat\n    subject: sk2526-insertion\n\
    \    predicate: decreases\n    object: ferritin-coat\n    mechanism: The mutant\
    \ micrograph has less peripheral material. This supports an envelope phenotype,not\n\
    \      an isolated-domain chemical mechanism or a quantitative universal capsule-loss\
    \ claim.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:18502854\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC2447026/\n      snippet: wzy\n    \
    \  explanation: Original Figure3A,Table1 and selected Methods/Results; temperature\
    \ and caption-species\n        conflicts retained.\n      cache_path: evidence/PF01901/shifrin-2008.txt\n\
    \      cache_sha256: 0a0b45ec1b69fb4611f6eaa1343c54187468907d84cd9326ab9bd24b7af8e231\n\
    - graph_id: o157-sk2526-polysaccharide-signals-2008\n  title: The insertion mutant\
    \ has lower LPS and capsular-fraction signals\n  scope: Shifrin2008 Figure3B;\
    \ two separately measured polysaccharide fractions.\n  context: Anti-O157 LPS\
    \ immunoblot and capsular-fraction dot assay,normalized to bacterial numbers.\
    \ These\n    are distinct readouts,not a causal chain between fractions.\n  family_mapping:\
    \ SK2526 derives from TUV93-0 with the Sakai-origin insertion. Q8X4T7/BAB36267.1\
    \ and AIG69277.1\n    are matching references,PF01901 8-205 of394 aa,score0.041.\
    \ Whole-cell allele evidence does not isolate\n    that partial domain; actual\
    \ stocks were not sequenced here.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:83334\n\
    \  limitations: No Wzy complementation or quantitative replication was established.\
    \ Lower-migrating LPS\n    material remains; immunoreactivity does not establish\
    \ complete chemical absence,linkage identity or\n    polymerase kinetics.\n  nodes:\n\
    \  - node_id: sk2526-insertion\n    label: SK2526 wzy insertion in the TUV93-0\
    \ background\n    node_type: PERTURBATION\n  - node_id: lps-o157-signal\n    label:\
    \ Polymeric anti-O157 LPS signal\n    node_type: STATE\n  - node_id: capsule-o157-signal\n\
    \    label: Anti-O157 capsular-fraction dot signal\n    node_type: STATE\n  edges:\n\
    \  - edge_id: insertion-decreases-lps-signal\n    subject: sk2526-insertion\n\
    \    predicate: decreases\n    object: lps-o157-signal\n    mechanism: The mutant\
    \ has lower polymeric immunoreactivity; residual lower material precludes an all-glycan-loss\n\
    \      interpretation.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:18502854\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC2447026/\n      snippet: wzy\n    \
    \  explanation: Original Figure3B upper panel; a measured signal,not a direct\
    \ chemical assay.\n      cache_path: evidence/PF01901/shifrin-2008.txt\n     \
    \ cache_sha256: 0a0b45ec1b69fb4611f6eaa1343c54187468907d84cd9326ab9bd24b7af8e231\n\
    \  - edge_id: insertion-decreases-capsule-signal\n    subject: sk2526-insertion\n\
    \    predicate: decreases\n    object: capsule-o157-signal\n    mechanism: The\
    \ separated capsular-fraction dot is weaker. Recovery and antigenicity remain\
    \ alternatives\n      to a specific defect in glycosidic-bond formation.\n   \
    \ directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:18502854\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2447026/\n\
    \      snippet: wzy\n      explanation: Original Figure3B lower panel,kept distinct\
    \ from its LPS immunoblot.\n      cache_path: evidence/PF01901/shifrin-2008.txt\n\
    \      cache_sha256: 0a0b45ec1b69fb4611f6eaa1343c54187468907d84cd9326ab9bd24b7af8e231\n\
    - graph_id: o157-43888-wzy-complementation-2021\n  title: Wzy complementation\
    \ restores BECP10 spot clearing in ATCC43888\n  scope: Park2021 original Figure4C;\
    \ complemented versus uncomplemented wzy-insertion culture.\n  context: Qualitative\
    \ phage spot readout with retained ECP26 clearing as a comparator. The actual\
    \ image\n    labels spots C,although the caption says A; no quantitative adsorption\
    \ rate is inferred.\n  family_mapping: ATCC43888 reference CP041623.1/FNZ21_14180\
    \ encodes QDZ55367.1,exactly equal to Q8X4T7/BAB36267.1,394\n    aa,PF01901 8-205,score0.041.\
    \ Its CDS start matches the displayed cluster start2969732. This does not\n  \
    \  independently sequence the experimental insertion or plasmid.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:83334\n  limitations: Empty-vector comparison,exact\
    \ construct/tag and figure-specific replication were not established.\n    This\
    \ is not rescue of the separate SK2526 or ATCC43895 mutants. Spot clearing is\
    \ not proof of direct\n    Wzy binding or productive-infection efficiency.\n \
    \ nodes:\n  - node_id: wzy-complementation\n    label: Reported wzy complementation\
    \ in the ATCC43888 insertion background\n    node_type: PERTURBATION\n  - node_id:\
    \ becp10-clearing\n    label: BECP10 spot clearing\n    node_type: PHENOTYPE\n\
    \  edges:\n  - edge_id: complementation-increases-clearing\n    subject: wzy-complementation\n\
    \    predicate: increases\n    object: becp10-clearing\n    mechanism: Clearing\
    \ returns in the complemented culture. A Wzy-dependent surface contribution is\
    \ consistent\n      with this contrast; direct receptor chemistry is not established.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:34452334\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8402813/\n\
    \      snippet: restored sensitivity\n      explanation: Original Figure4C,not\
    \ the caption's panel A. No duplicate deletion-versus-WT edge is\n        inferred\
    \ from this complemented/uncomplemented comparison.\n      cache_path: evidence/PF01901/park-2021.txt\n\
    \      cache_sha256: 5365e1b63ba290b8b4a09f752746b03f06003d7b7a5cfd7e45eb2587ed810462\n\
    curation_events:\n- timestamp: '2026-10-11T22:16:32Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate four O157 wzy insertion phenotype\
    \ graphs with reference-level PF01901 mapping\n  history_record: history/records/PF01901/2026-10-11T221632Z-codex-6f33bc.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-11T22:23:25Z'\n\
    \  curator: Codex\n  action: REVIEW\n  outcome: needs_followup\n  summary: Retain\
    \ partial scientific self-review of PF01901 O157 phenotype graphs\n  history_record:\
    \ history/records/PF01901/2026-10-11T222325Z-codex-d48ef3.yaml\n  event_index:\
    \ 0\n  llm_assisted: true\n- timestamp: '2026-10-11T22:31:01Z'\n  curator: Codex\n\
    \  action: EDIT\n  outcome: changed\n  summary: Extend PF01901 capsule and phage-complementation\
    \ contexts and refine strain lineage\n  history_record: history/records/PF01901/2026-10-11T223101Z-codex-51854f.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: concern
  summary: Official ATCC documents700927 as derived from43895, resolving the previously
    unexplained catalog relationship, not sequencing the actual assay stock. CP041623.1
    ATCC43888 CDS FNZ21_14180/QDZ55367.1 exactly matches Q8X4T7 and its start matches
    the Park2021 displayed cluster start. Shifrin2008 Table1 identifies SK2526 as
    the TUV93-0 insertion derivative with a Sakai-origin allele. Current references
    support member mapping, but exact historical alleles and complementation clone
    are unverified. The partial PF01901 match8-205 of394aa, score0.041, does not establish
    a catalytic boundary.
  target_ids:
  - PF01901
  evidence_ids:
  - identity
  - primary
  - phage-context
  - strain-authority
  - original-identity
  - original-mutant
  - later-mutant-contexts
  - historical-review
  - followup-search-limits
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Nodes, directions and evidence preserve distinct ATCC43895, SK2526 and
    ATCC43888 contexts. Figure3B fractions are separate readouts, not a causal chain.
    Actual Park Figure4C supports complemented versus uncomplemented clearing; it
    does not supply a separate WT comparison, direct Wzy-phage binding or quantified
    infection efficiency. ECP26 clearing is retained. No cross-strain rescue, isolated-domain
    mechanism or universal glycan loss is inferred. Original four phenotype graphs
    retain residual and negative findings and source reporting conflicts. Evidence
    hashes and stable IDs are intact; historical files are unchanged.
  target_ids:
  - PF01901
  evidence_ids:
  - primary
  - native
  - phage-context
  - strain-authority
  - original-identity
  - original-mutant
  - later-mutant-contexts
  - historical-review
  - followup-search-limits
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Selected2008 and2021 primary contexts now have inspected full text and
    original figures. Their supplements and additional host-interaction contexts are
    not certified. The2004 paper remains inaccessible through attempted endpoints.
    Exact historical alleles, expression controls, partial domain reassessment, source
    inconsistencies and most237 family members remain open, including archaeal physiology
    and FPC840 current mapping. Annotation absence is not evidence that functional
    literature does not exist.
  target_ids:
  - PF01901
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01901-causal-context-coverage
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve exact assay alleles and extend member-specific primary coverage
  description: The ATCC700927/43895 lineage issue is resolved by authority evidence,
    but actual experimental stock and allele sequences remain unresolved. Reassess
    short family mapping, inspect remaining primary contexts and assay-matched controls,
    and reconcile the2008 temperature/species,2021 panel-label and2024 concentration/duration
    reporting conflicts. Keep strain-specific rescue separate. New supported claims
    require overlay curation, real history, guarded regeneration and a successor review;
    the same coverage issue stays open.
  target_ids:
  - PF01901
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - phage-context
  - strain-authority
  - original-identity
  - original-mutant
  - later-mutant-contexts
  - historical-review
  - followup-search-limits
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01901.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: The ATCC700927/43895 lineage issue is resolved by authority evidence,
    but actual experimental stock and allele sequences remain unresolved. Reassess
    short family mapping, inspect remaining primary contexts and assay-matched controls,
    and reconcile the2008 temperature/species,2021 panel-label and2024 concentration/duration
    reporting conflicts. Keep strain-specific rescue separate. New supported claims
    require overlay curation, real history, guarded regeneration and a successor review;
    the same coverage issue stays open.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01901
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Original2008 Figure3 and2021 Figure4 were inspected in this follow-up; prior2020
  Figure1 and2024 Figures1/2/4/5 assessments and evidence were retained. No raw-data
  reanalysis, exact clone sequencing, inaccessible supplement inspection, independent
  replication or exhaustive family audit is claimed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
