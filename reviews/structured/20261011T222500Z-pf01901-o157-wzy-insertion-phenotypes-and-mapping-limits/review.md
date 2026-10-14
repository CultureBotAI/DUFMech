# O157 Wzy insertion phenotypes and PF01901 mapping limits

- Review: 20261011T222500Z-pf01901-o157-wzy-insertion-phenotypes-and-mapping-limits
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T22:23:25Z
- Finished UTC: 2026-10-11T22:25:00Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Four PHENOTYPIC graphs retain four OBSERVED,INDIRECT decreases:2020tube staining and2024long-O-antigen signal,microtiter staining and motility halo. Five original images and primary text constrain negative/residual findings. Two open discussions retain mapping,attribution and broader-coverage work. Family remains IN_PROGRESS;partial same-agent scientific assessment,not independent endorsement or completion of the8296-record goal.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01901,formerDUF70; selected O157 insertion phenotypes,current member references and excluded Wzy-family transfers.
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

FrozenPF01901 is formerDUF70,IPR002760,237proteins. Q57862/MJ0419 and Q57863/MJ0420 exactly match AAB98417.1/AAB98408.1,with PF01901 at11-336/14-363. O85335 equals AAC32340.1;Q8X4T7 equals BAB36267.1;both394aa,O157members with short PF01901 hit8-205,score0.041. They differ at234. The2024paper-cited CP008957.1 CDS AIG69277.1 exactly matches Q8X4T7 but the genome source names ATCC700927,whereas assays name ATCC43895. Reference-level family mapping is supported; assay-culture sequence,exact insertion and domain attribution remain unresolved. Do not assert family-wide or residue-level chemistry.

### Directed effects and limits

graph: supported. Targets: PF01901.

Each graph distinguishes the named transposon intervention from a clean deletion and its specific measured endpoint. No unsupported chain connects LPS loss to biofilm or motility,and no invasion,flagella-loss or curli-loss edge is invented. The2024mutant is reused from2020,not an independent allele. Wzy-specific rescue is not substituted from csgB complementation. Weak partial Pfam mapping and reference-culture mismatch appear in each graph. O86purified Wzy is reportedPF14296 and excluded; FPC840serotype associations and diagnosticPCR are not perturbations. Nodes,polarity,evidence hashes and graph-local identifiers preserve the native representation.

### Remaining family coverage

completeness: concern. Targets: PF01901.

Exact43895allele and insertion controls,reference-culture reconciliation, domain reassessment and source reporting discrepancies remain open. The2004 O157core study,2008capsule and2021phage studies need full primary follow-up. Most237members,archaeal physiology,FPC840currentsequence/functional evidence, the2026clustering preprint andB.anthracisclan evidence are not assessed. Current annotation absence is not proof of no functional literature.

## Findings

### additional-contexts: Resolve assay-genotype mapping and extend member-specific primary evidence

minor / open / confirmed; issue key: pf01901-causal-context-coverage.

Establish the tested ATCC43895 wzy sequence and insertion junction,resolve its relation to the cited ATCC700927reference,and reassess the short score0.041family match before domain-wide transfer. Inspect Wzy-specific rescue and downstream-expression controls and remaining primary O157 studies. Resolve2024glucose/duration discrepancies and preserve negative invasion,residual biomass,flagellin andcurli results. Curate supported additions through overlays,actual history and a successor scoped review.

## Recommended Actions And Acceptance Checks

### extend-contexts

Establish the tested ATCC43895 wzy sequence and insertion junction,resolve its relation to the cited ATCC700927reference,and reassess the short score0.041family match before domain-wide transfer. Inspect Wzy-specific rescue and downstream-expression controls and remaining primary O157 studies. Resolve2024glucose/duration discrepancies and preserve negative invasion,residual biomass,flagellin andcurli results. Curate supported additions through overlays,actual history and a successor scoped review.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC11394844/; Results,Methods,Tables1/2 and originalFigures1/2/4/5. | supports | The reused ATCC43895 wzy-Tn5 mutant has reduced long-O-antigen signal, retained crystal-violet biomass and motility-halo diameter. Residual one-unit LPS,ring staining,flagellin and Congo-red binding remain. This is a whole-cell phenotype set without allele-specific rescue,not purified polymerization. Glucose,time and text-versus-plot discrepancies are explicitly retained. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01901/; Accession and domain locations; paired UniProt identity facts | supports | FrozenPF01901 is formerDUF70,IPR002760,237proteins. Q57862/MJ0419 and Q57863/MJ0420 exactly match AAB98417.1/AAB98408.1,with PF01901 at11-336/14-363. O85335 equals AAC32340.1;Q8X4T7 equals BAB36267.1;both394aa,O157members with short PF01901 hit8-205,score0.041. They differ at234. The2024paper-cited CP008957.1 CDS AIG69277.1 exactly matches Q8X4T7 but the genome source names ATCC700927,whereas assays name ATCC43895. Reference-level family mapping is supported; assay-culture sequence,exact insertion and domain attribution remain unresolved. Do not assert family-wide or residue-level chemistry. |
| original-mutant | https://pmc.ncbi.nlm.nih.gov/articles/PMC7232329/; Selected wzy Methods/Results,Table1 and originalFigure1A-D. | supports | Reduced tube staining with retained intracellular recovery; csgB rescue and pathogenicity effects are not assigned to wzy. |
| excluded-transfer-assessment | evidence/PF01901/excluded-transfers.txt; Selected1998orf2/PCR,2017Table3/serotyping and2014O86main text/Methods. | supports | Gene names,clan relationships and PCR associations do not justify transferred catalytic edges. |
| search-and-access-limits | evidence/PF01901/gaps.txt; Dated search scope,unresolved mapping,primary leads and access limitations. | supports | Remaining allele/assay identity,attribution and literature gaps stay open; repository/skill reads work without a global permission claim. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01901 | data/families/PF01901.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Original2020Figure1 and2024Figures1/2/4/5 were visually inspected; selected primary text,tables and source mapping were read. No raw-data reanalysis, culture sequencing,independent replication or exhaustive family audit. Full2004/2008/2021papers and2017figures/supplements are not certified.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T222500Z-pf01901-o157-wzy-insertion-phenotypes-and-mapping-limits
title: O157 Wzy insertion phenotypes and PF01901 mapping limits
started_at: '2026-10-11T22:23:25Z'
finished_at: '2026-10-11T22:25:00Z'
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
summary: Four PHENOTYPIC graphs retain four OBSERVED,INDIRECT decreases:2020tube staining
  and2024long-O-antigen signal,microtiter staining and motility halo. Five original
  images and primary text constrain negative/residual findings. Two open discussions
  retain mapping,attribution and broader-coverage work. Family remains IN_PROGRESS;partial
  same-agent scientific assessment,not independent endorsement or completion of the8296-record
  goal.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01901.yaml
    sha256: 2e56fdbeb7adf5f03f729be3fb32d237d5b32d86c6eadc7d06bf53eea6dcf56d
    role: context
  - path: data/families/PF01901.yaml
    sha256: 1d5eeb6493684748b4a011824801247c00a89d72f116868631b3bfc5397beb43
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
  - path: evidence/PF01901/sheng-2024.txt
    role: context
    sha256: 7ab1fdc0f56fa8bed1b36c6d9b2e386f61f0dee1549bc70e71ebb37d61ff0125
  - path: evidence/PF01901/identity.txt
    role: context
    sha256: fbb1cdb3f9c8b85b3199aae8d47d2e5df70fb8b165e013cb04d40e5a7e8f2bb9
  - path: evidence/PF01901/sheng-2020.txt
    role: context
    sha256: 9f6de06da18e36eba66965e742ceb73f2534a692136d663e5c39849da6adb905
  - path: evidence/PF01901/excluded-transfers.txt
    role: context
    sha256: 216424b39b4a3e5f693165970f678beb566acbf94ae31c9de8af88e7aa892cf9
  - path: evidence/PF01901/gaps.txt
    role: context
    sha256: 092f688412bddd83c003cfed7add144b0516afa6bfd94ccc094e721c9964ff0a
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
    sha256: 5e426dd11dd4188aad4bf639eae76e14d76358ee04b5d7984c7c3dbedc950516
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01901,formerDUF70; selected O157 insertion phenotypes,current member
    references and excluded Wzy-family transfers.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01901
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Exact43895allele and insertion controls,reference-culture reconciliation,
      domain reassessment and source reporting discrepancies remain open. The2004
      O157core study,2008capsule and2021phage studies need full primary follow-up.
      Most237members,archaeal physiology,FPC840currentsequence/functional evidence,
      the2026clustering preprint andB.anthracisclan evidence are not assessed. Current
      annotation absence is not proof of no functional literature.
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
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC11394844/
  locator: Results,Methods,Tables1/2 and originalFigures1/2/4/5.
  accessed_at: '2026-10-11T22:25:00Z'
  support: supports
  snapshot_sha256: 7ab1fdc0f56fa8bed1b36c6d9b2e386f61f0dee1549bc70e71ebb37d61ff0125
  summary: The reused ATCC43895 wzy-Tn5 mutant has reduced long-O-antigen signal,
    retained crystal-violet biomass and motility-halo diameter. Residual one-unit
    LPS,ring staining,flagellin and Congo-red binding remain. This is a whole-cell
    phenotype set without allele-specific rescue,not purified polymerization. Glucose,time
    and text-versus-plot discrepancies are explicitly retained.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01901/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T22:25:00Z'
  support: supports
  snapshot_sha256: fbb1cdb3f9c8b85b3199aae8d47d2e5df70fb8b165e013cb04d40e5a7e8f2bb9
  summary: FrozenPF01901 is formerDUF70,IPR002760,237proteins. Q57862/MJ0419 and Q57863/MJ0420
    exactly match AAB98417.1/AAB98408.1,with PF01901 at11-336/14-363. O85335 equals
    AAC32340.1;Q8X4T7 equals BAB36267.1;both394aa,O157members with short PF01901 hit8-205,score0.041.
    They differ at234. The2024paper-cited CP008957.1 CDS AIG69277.1 exactly matches
    Q8X4T7 but the genome source names ATCC700927,whereas assays name ATCC43895. Reference-level
    family mapping is supported; assay-culture sequence,exact insertion and domain
    attribution remain unresolved. Do not assert family-wide or residue-level chemistry.
- evidence_id: original-mutant
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7232329/
  locator: Selected wzy Methods/Results,Table1 and originalFigure1A-D.
  summary: Reduced tube staining with retained intracellular recovery; csgB rescue
    and pathogenicity effects are not assigned to wzy.
  accessed_at: '2026-10-11T22:25:00Z'
  support: supports
  snapshot_sha256: 9f6de06da18e36eba66965e742ceb73f2534a692136d663e5c39849da6adb905
- evidence_id: excluded-transfer-assessment
  kind: search
  reference: evidence/PF01901/excluded-transfers.txt
  locator: Selected1998orf2/PCR,2017Table3/serotyping and2014O86main text/Methods.
  search_scope: Primary-source checks ofPMC108385,PMC5601056 andPMC3989392 to distinguish
    O157prediction,HHpredassociation and O86PF14296biochemistry. No2017 images/supplements
    or current O86family reassignment is certified.
  summary: Gene names,clan relationships and PCR associations do not justify transferred
    catalytic edges.
  accessed_at: '2026-10-11T22:25:00Z'
  support: supports
  snapshot_sha256: 216424b39b4a3e5f693165970f678beb566acbf94ae31c9de8af88e7aa892cf9
- evidence_id: search-and-access-limits
  kind: search
  reference: evidence/PF01901/gaps.txt
  locator: Dated search scope,unresolved mapping,primary leads and access limitations.
  search_scope: Ignored/hidden-inclusive local search ofcuration,evidence,history,reviews,
    reports(exceptinventory.json) forPF01901,DUF70,MJ0419,MJ0420,FPC840_340035. Public
    queries for those names,function/polymerase,O157wzyperturbation, complementation,in-vitro,O85335,Q6LY80modA
    and named primarytitles. Current237-entryUniProt query and four exactNCBIprotein
    comparisons; CP008957.1CDS comparison. PMC2008challenge,EuropePMC500/403 and2004DOI
    access failure are limits,not negative evidence. Noexhaustivecoverage.
  summary: Remaining allele/assay identity,attribution and literature gaps stay open;
    repository/skill reads work without a global permission claim.
  accessed_at: '2026-10-11T22:25:00Z'
  support: supports
  snapshot_sha256: 092f688412bddd83c003cfed7add144b0516afa6bfd94ccc094e721c9964ff0a
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T22:25:00Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01901
  kind: record_content
  reference: data/families/PF01901.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T22:25:00Z'
  support: context_only
  snapshot_sha256: 1d5eeb6493684748b4a011824801247c00a89d72f116868631b3bfc5397beb43
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
    \  prompt: Resolve the tested wzy allele,reference-culture discrepancy and assay\
    \ reporting before assigning\n    a domain mechanism.\n  kind: CURATION_TODO\n\
    \  status: OPEN\n  rationale: Whole-cell insertion effects support the measured\
    \ directions but do not isolate Wzy chemistry,polar\n    effects or a PF01901\
    \ catalytic segment. Current O157 membership is a short score0.041 hit,unlike\
    \ the\n    strong archaeal matches.\n  evidence:\n  - reference: PMID:39273173\n\
    \    supports: PARTIAL\n    evidence_source: selected_full_text_and_figures\n\
    \    explanation: Figures1/2/4 retain long-O-antigen,biomass and halo reductions;\
    \ residual signal,flagellin\n      and Congo-red binding constrain interpretation.\
    \ The cited CP008957 reference equals Q8X4T7 but names\n      ATCC700927,not an\
    \ independently sequenced ATCC43895 culture. Glucose and duration discrepancies\n\
    \      remain unresolved.\n  - reference: PMID:32316415\n    supports: PARTIAL\n\
    \    evidence_source: selected_full_text_and_figure\n    explanation: Figure1B\
    \ supports reduced tube staining;1D does not show the csgB-like invasion reduction\n\
    \      for wzy. csgB rescue must not become wzy rescue. The later study reuses\
    \ this mutant.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n  notes: Retain\
    \ exact allele/strain evidence,Wzy-specific rescue and downstream-expression controls\
    \ if\n    available; obtain assay-matched growth/biomass controls. These four\
    \ graphs are indirect observed phenotypes,not\n    purified polymerization or\
    \ family-wide functional assignment. Minimal evidence and source limits are\n\
    \    in evidence/PF01901.\n- discussion_id: duf70-primary-context-and-family-coverage\n\
    \  prompt: Inspect additional O157 primary experiments and archaeal members without\
    \ transferring other\n    Wzy families.\n  kind: CURATION_TODO\n  status: OPEN\n\
    \  rationale: The237 frozen proteins are not covered by one O157 mutant. Reviewed\
    \ Q57862/MJ0419 and Q57863/MJ0420\n    are uncharacterized in the inspected annotation;\
    \ this is not proof of absent experiments. EX_DUF naming\n    and clanCL0499 do\
    \ not establish universal polymerase chemistry.\n  evidence:\n  - reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01901/\n\
    \    supports: PARTIAL\n    evidence_source: database\n    explanation: Current\
    \ family metadata remains tentative. Exact sequence comparisons map four references;\n\
    \      archaeal PF01901 intervals are11-336 and14-363,whereas O157 is8-205. O85335\
    \ and Q8X4T7 differ at234.\n  - reference: PMID:28955320\n    supports: PARTIAL\n\
    \    evidence_source: selected_full_text_and_table\n    explanation: FPC840_340035\
    \ has a Table3 HHpredPF01901 relationship but no reported InterProScan hit.\n\
    \      Comparative genomics and serotype PCR are not gene-perturbation evidence;\
    \ current sequence mapping\n      remains open.\n  posed_by: Codex\n  posed_date:\
    \ '2026-10-11'\n  notes: The2014purified Wzy paper tests O86 and reports PF14296,not\
    \ this O157 member. Follow up2004doi10.1074/jbc.M401879200,2008capsule\n    and2021BECP10studies;\
    \ access failures and uninspected primary details are not negative findings. No\n\
    \    molybdate edge follows from the submitted modA name of Q6LY80. Keep IN_PROGRESS\
    \ pending broader member-specific\n    evidence.\ncausal_graphs:\n- graph_id:\
    \ o157-wzy-tn5-tube-staining-2020\n  title: Wzy disruption reduces tube biofilm\
    \ staining in the tested O157 strain\n  scope: Sheng2020 Figure1B; ATCC43895 wzy-Tn5\
    \ versus its parental culture.\n  context: Qualitative crystal-violet tube assay\
    \ at37 C under static conditions. The30 C library screen\n    is a separate assay,\
    \ not a replicate of this endpoint.\n  family_mapping: The2024follow-up cites\
    \ genome CP008957; its AIG69277.1/EDL933_3111 reference exactly\n    matches Q8X4T7/BAB36267.1,394\
    \ aa,with current PF01901 at8-205,score0.041. CP008957.1 names ATCC700927\n  \
    \  whereas the experiments name ATCC43895. This is reference-level mapping,not\
    \ an independently sequenced\n    assay culture; the insertion junction and affected\
    \ domain segment remain unresolved.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:83334\n\
    \  limitations: No Wzy-specific rescue or downstream-expression control was established.\
    \ csgB complementation\n    is not wzy rescue. The later2024study retains residual\
    \ biofilm under its conditions; do not infer\n    universal absence or direct\
    \ PF01901 chemistry.\n  nodes:\n  - node_id: wzy-insertion\n    label: Reported\
    \ wzy-Tn5 allele in the ATCC43895 background\n    node_type: PERTURBATION\n  -\
    \ node_id: tube-staining\n    label: Retained crystal-violet tube-ring staining\n\
    \    node_type: PHENOTYPE\n  edges:\n  - edge_id: insertion-decreases-tube-staining\n\
    \    subject: wzy-insertion\n    predicate: decreases\n    object: tube-staining\n\
    \    mechanism: The named wzy-Tn5 tube has much less ring staining than the parental43895\
    \ tube. This whole-cell\n      phenotype does not resolve biomass,attachment,dye\
    \ retention or polar contributions. Comparable intracellular\n      recovery in\
    \ Figure1D is not converted into an invasion-defect edge.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:32316415\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7232329/\n\
    \      snippet: biofilm-negative\n      explanation: Original Figure1B and its\
    \ caption establish the qualitative tube contrast; Table1 names\n        wzy-Tn5.\
    \ Original1D constrains invasion claims. The insertion was mapped by the authors,not\
    \ independently\n        sequenced in this review.\n      cache_path: evidence/PF01901/sheng-2020.txt\n\
    \      cache_sha256: 9f6de06da18e36eba66965e742ceb73f2534a692136d663e5c39849da6adb905\n\
    - graph_id: o157-wzy-tn5-lps-2024\n  title: The wzy-Tn5 culture has reduced long-O-antigen\
    \ LPS signal\n  scope: Sheng2024 Figure1B; ATCC43895 wzy-Tn5 versus parental LPS.\n\
    \  context: Silver-stained Tricine-SDS-PAGE of whole-cell LPS preparations. Figure1A\
    \ is an expected-structure\n    schematic,not a purified polymerase experiment\
    \ or complete chemical structure determination.\n  family_mapping: Paper-cited\
    \ CP008957.1 encodes AIG69277.1,exactly matching Q8X4T7/BAB36267.1. Current\n\
    \    PF01901 covers8-205 of394 aa with score0.041. The reference source is ATCC700927,not\
    \ independently\n    verified ATCC43895 assay DNA. O85335/AAC32340.1 differs from\
    \ Q8X4T7 at234 and is not silently substituted.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:83334\n  limitations: The actual genotype is Tn5,not a verified\
    \ clean delta-wzy deletion despite the schematic\n    label. No allele-specific\
    \ rescue,exact insertion position or neighboring-expression measurement was\n\
    \    established. The weak partial family hit does not establish an isolated catalytic\
    \ domain or archaeal\n    transfer.\n  nodes:\n  - node_id: wzy-insertion\n  \
    \  label: Reported wzy-Tn5 allele in the ATCC43895 background\n    node_type:\
    \ PERTURBATION\n  - node_id: long-o-antigen-signal\n    label: Long-O-antigen\
    \ LPS gel signal\n    node_type: STATE\n  edges:\n  - edge_id: insertion-decreases-long-o-antigen\n\
    \    subject: wzy-insertion\n    predicate: decreases\n    object: long-o-antigen-signal\n\
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
    \    and ANOVA with Dunnett comparison.\n  family_mapping: The cited reference\
    \ CP008957.1/AIG69277.1 equals Q8X4T7/BAB36267.1,394 aa,PF01901 8-205,score0.041.\n\
    \    ATCC700927 reference versus ATCC43895 assay identity and exact Tn5 insertion\
    \ remain unresolved; this\n    is a whole-protein reference association,not a\
    \ verified domain-specific perturbation.\n  scope_status: PHENOTYPIC\n  taxon:\
    \ NCBITaxon:83334\n  limitations: Lower staining is not complete biofilm loss;\
    \ Figure2A retains a weaker ring. Tube duration\n    is overnight in Methods versus48h\
    \ in caption/Results. Figure3 does not supply a matched wzy growth\n    curve.\
    \ No Wzy-specific rescue was established; reused2020allele is not an independent\
    \ genotype replication.\n  nodes:\n  - node_id: wzy-insertion\n    label: Reported\
    \ wzy-Tn5 allele in the ATCC43895 background\n    node_type: PERTURBATION\n  -\
    \ node_id: retained-cv-signal\n    label: Microtiter retained crystal-violet absorbance\n\
    \    node_type: PHENOTYPE\n  edges:\n  - edge_id: insertion-decreases-cv-signal\n\
    \    subject: wzy-insertion\n    predicate: decreases\n    object: retained-cv-signal\n\
    \    mechanism: The wzy-Tn5 bar is below parental43895 with the caption's p<0.01\
    \ comparison. Residual signal\n      remains. Altered attachment,biomass,dye retention\
    \ or envelope effects are not separated; no causal\n      chain from the LPS band\
    \ to this readout is inferred from their co-occurrence.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:39273173\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11394844/\n\
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
    \ t-test and p<0.01 for the wzy contrast.\n  family_mapping: Reference CP008957.1/AIG69277.1\
    \ exactly matches Q8X4T7/BAB36267.1 with PF01901 8-205\n    of394 aa,score0.041.\
    \ The source culture is ATCC700927 whereas the tested culture is named ATCC43895;\n\
    \    the insertion sequence was not independently verified. Whole-cell phenotype,not\
    \ a residue-specific\n    archaeal mechanism.\n  scope_status: PHENOTYPIC\n  taxon:\
    \ NCBITaxon:83334\n  limitations: Residual spread and the flagellin immunoblot\
    \ band remain. Halo diameter is not motor speed\n    or flagellum abundance. No\
    \ Wzy-specific rescue or matched wzy growth control was established. Retained\n\
    \    Congo-red binding in Figure5 also excludes a complete-curli-loss claim.\n\
    \  nodes:\n  - node_id: wzy-insertion\n    label: Reported wzy-Tn5 allele in the\
    \ ATCC43895 background\n    node_type: PERTURBATION\n  - node_id: motility-halo\n\
    \    label: Soft-agar motility-halo diameter\n    node_type: PHENOTYPE\n  edges:\n\
    \  - edge_id: insertion-decreases-halo\n    subject: wzy-insertion\n    predicate:\
    \ decreases\n    object: motility-halo\n    mechanism: The wzy-Tn5 halo is smaller\
    \ but nonzero compared with WT. The same figure retains a flagellin\n      band,so\
    \ neither absence of flagella nor direct inhibition of their biosynthesis follows.\
    \ Envelope,motility\n      and growth contributions remain unresolved.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:39273173\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11394844/\n\
    \      snippet: impaired motility\n      explanation: Original Figure4 upper bars\
    \ and lower immunoblot were inspected together. Figure5 retains\n        wzy Congo-red\
    \ binding. The40h/48h discrepancy and lack of allele-specific rescue prevent stronger\n\
    \        mechanistic attribution.\n      cache_path: evidence/PF01901/sheng-2024.txt\n\
    \      cache_sha256: 7ab1fdc0f56fa8bed1b36c6d9b2e386f61f0dee1549bc70e71ebb37d61ff0125\n\
    curation_events:\n- timestamp: '2026-10-11T22:16:32Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate four O157 wzy insertion phenotype\
    \ graphs with reference-level PF01901 mapping\n  history_record: history/records/PF01901/2026-10-11T221632Z-codex-6f33bc.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: concern
  summary: FrozenPF01901 is formerDUF70,IPR002760,237proteins. Q57862/MJ0419 and Q57863/MJ0420
    exactly match AAB98417.1/AAB98408.1,with PF01901 at11-336/14-363. O85335 equals
    AAC32340.1;Q8X4T7 equals BAB36267.1;both394aa,O157members with short PF01901 hit8-205,score0.041.
    They differ at234. The2024paper-cited CP008957.1 CDS AIG69277.1 exactly matches
    Q8X4T7 but the genome source names ATCC700927,whereas assays name ATCC43895. Reference-level
    family mapping is supported; assay-culture sequence,exact insertion and domain
    attribution remain unresolved. Do not assert family-wide or residue-level chemistry.
  target_ids:
  - PF01901
  evidence_ids:
  - identity
  - primary
  - original-mutant
  - excluded-transfer-assessment
  - search-and-access-limits
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Each graph distinguishes the named transposon intervention from a clean
    deletion and its specific measured endpoint. No unsupported chain connects LPS
    loss to biofilm or motility,and no invasion,flagella-loss or curli-loss edge is
    invented. The2024mutant is reused from2020,not an independent allele. Wzy-specific
    rescue is not substituted from csgB complementation. Weak partial Pfam mapping
    and reference-culture mismatch appear in each graph. O86purified Wzy is reportedPF14296
    and excluded; FPC840serotype associations and diagnosticPCR are not perturbations.
    Nodes,polarity,evidence hashes and graph-local identifiers preserve the native
    representation.
  target_ids:
  - PF01901
  evidence_ids:
  - primary
  - native
  - original-mutant
  - excluded-transfer-assessment
  - search-and-access-limits
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Exact43895allele and insertion controls,reference-culture reconciliation,
    domain reassessment and source reporting discrepancies remain open. The2004 O157core
    study,2008capsule and2021phage studies need full primary follow-up. Most237members,archaeal
    physiology,FPC840currentsequence/functional evidence, the2026clustering preprint
    andB.anthracisclan evidence are not assessed. Current annotation absence is not
    proof of no functional literature.
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
  title: Resolve assay-genotype mapping and extend member-specific primary evidence
  description: Establish the tested ATCC43895 wzy sequence and insertion junction,resolve
    its relation to the cited ATCC700927reference,and reassess the short score0.041family
    match before domain-wide transfer. Inspect Wzy-specific rescue and downstream-expression
    controls and remaining primary O157 studies. Resolve2024glucose/duration discrepancies
    and preserve negative invasion,residual biomass,flagellin andcurli results. Curate
    supported additions through overlays,actual history and a successor scoped review.
  target_ids:
  - PF01901
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - original-mutant
  - excluded-transfer-assessment
  - search-and-access-limits
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01901.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Establish the tested ATCC43895 wzy sequence and insertion junction,resolve
    its relation to the cited ATCC700927reference,and reassess the short score0.041family
    match before domain-wide transfer. Inspect Wzy-specific rescue and downstream-expression
    controls and remaining primary O157 studies. Resolve2024glucose/duration discrepancies
    and preserve negative invasion,residual biomass,flagellin andcurli results. Curate
    supported additions through overlays,actual history and a successor scoped review.
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
- Original2020Figure1 and2024Figures1/2/4/5 were visually inspected; selected primary
  text,tables and source mapping were read. No raw-data reanalysis, culture sequencing,independent
  replication or exhaustive family audit. Full2004/2008/2021papers and2017figures/supplements
  are not certified.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
