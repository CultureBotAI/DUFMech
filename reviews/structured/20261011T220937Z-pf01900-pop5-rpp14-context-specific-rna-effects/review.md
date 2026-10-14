# Pop5 and Rpp14 context-specific RNA effects and causal limits

- Review: 20261011T220937Z-pf01900-pop5-rpp14-context-specific-rna-effects
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T22:06:16Z
- Finished UTC: 2026-10-11T22:09:37Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Nineteen scoped graphs retain35 observed effects:3direct,14unresolved, 18indirect;2mechanistic and17phenotypic graphs. Primary figures and recovered supplementary methods constrain joint archaeal protocols, SPR and dose effects, human preparation assays and cell-level knockdown/rescue. Two open discussions preserve causal-attribution and family-coverage work. Status is IN_PROGRESS; this is partial same-agent scientific review,not approval of every family member or completion of the8296-record goal.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01900, next uncurated accession after PF01899; six mapped archaeal/human references and selected primary biochemical/cellular assays.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01900 | data/families/PF01900.yaml | generated | PF01900 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01900 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01900.

FrozenPF01900 is formerDUF69,notPF01899/DUF68. Six UniProt sequences exactly match versioned NCBI references: O26783/AAB85192.1,MTH_687,124aa,domain13-116; Q57917/AAB98484.1,MJ0494,134aa,17-111; Q8U151/AAL81502.1,PF1378,120aa,17-113; O59150/BAA30588.1,PH1481,120aa,17-113; humanO95059/NP_008973.1,124aa,35-108; humanQ969H6/NP_057002.2,163aa,7-115. Current reference matches do not sequence each assay vial or human transgene. Pop5 and Rpp14 remain distinct members, and Rpp30R107A is not transferred. Delta14C overlaps only107-113 ofPfam.

### Directed effects and limits

graph: supported. Targets: PF01900.

Each edge has the tested conjunction and measured direction, with unique local IDs and hash-anchored evidence. Mth/Mja/Pfu comparisons retain changed buffers,doses and times; correct-site fractions are not conversion or rates. ApparentSPRaffinity is not full-RNAactivation or molecular stoichiometry. F14HEK293 andF39HeLa fractions remain separate. Figure4C does not support increased40minMono fromPop5. Mg-free95%-pure preparations remain unresolved in catalytic attribution; Rpp14 omission retains H1-complex cleavage. Myc-Rpp14 sedimentation is ex-vivo,not observed intracellular aggregation. RPP14shRNAprotein depletion was not established. Cas9 populations are not sequenced null clones and retain RPP14mRNA; upstream-background suppression is not RPP14null complementation. RNA amount nodes are STATE,not catalytic activity labels. Shared PF01876 assay evidence is not independent replication.

### Remaining family coverage

completeness: concern. Targets: PF01900.

The5287 frozen proteins are not exhaustively characterized. Full original 2006loop-deletion and2013helix/FRETmethods/figures,2015mutantSPRcurves, exacthumanclone sequences/doses,2008MjacisTyr,2011assembly,2012annealing, yeast/otherarchaealcontexts,1999/2002humanbiochemistry,2024telomere and metazoanMRP evidence remain follow-ups. Abstracts,structures and association networks are not promoted to observed causal edges.

## Findings

### additional-contexts: Complete missing construct, catalytic-attribution and homolog evidence

minor / open / confirmed; issue key: pf01900-causal-context-coverage.

Obtain exact human assay/transgene constructs and matched preparation controls; reconcile the2023gradient and2026replicate/statistical discrepancies; inspect original2006/2013mutational studies and2015SPRcurves. Assess additional member-specific primary assays before extending graphs. Preserve residual activity, partner/buffer conjunctions, endpoint-specific rescue and negative controls. Add a successor review and canonical history without changing historical reports or promoting the family to REVIEWED on structural checks.

## Recommended Actions And Acceptance Checks

### extend-contexts

Obtain exact human assay/transgene constructs and matched preparation controls; reconcile the2023gradient and2026replicate/statistical discrepancies; inspect original2006/2013mutational studies and2015SPRcurves. Assess additional member-specific primary assays before extending graphs. Preserve residual activity, partner/buffer conjunctions, endpoint-specific rescue and negative controls. Add a successor review and canonical history without changing historical reports or promoting the family to REVIEWED on structural checks.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC13408128/; Figure2c-e/j-l/o/r/s; SupplementFigure2d/e; Methods; SupplementData2. | supports | RPP14-targeted HeLa Mirror populations have lower H1/MRP RNA and higher unprocessed MALAT1/MEN-beta/ITS1site2 signals. POP5 targeting lowers H1/MRP with28S normalization. IntronlessRPP14 suppresses H1/MRP and lncRNA-junction defects separately in TRNAU1AP and PRPF39 backgrounds. Residual RPP14 mRNA, replicate/statistical discrepancies, unverified transgene sequence and suppression rather than RPP14-null complementation are explicit. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01900/; Accession and domain locations; paired UniProt identity facts | supports | FrozenPF01900 is formerDUF69,notPF01899/DUF68. Six UniProt sequences exactly match versioned NCBI references: O26783/AAB85192.1,MTH_687,124aa,domain13-116; Q57917/AAB98484.1,MJ0494,134aa,17-111; Q8U151/AAL81502.1,PF1378,120aa,17-113; O59150/BAA30588.1,PH1481,120aa,17-113; humanO95059/NP_008973.1,124aa,35-108; humanQ969H6/NP_057002.2,163aa,7-115. Current reference matches do not sequence each assay vial or human transgene. Pop5 and Rpp14 remain distinct members, and Rpp30R107A is not transferred. Delta14C overlaps only107-113 ofPfam. |
| archaeal-reconstitution | https://pmc.ncbi.nlm.nih.gov/articles/PMC3001054/; Table1,Figures3/4/7;supplementMethods/TableS2/pulse-chase controls. | supports | Joint archaeal protein and ionic protocols; minimal-RNA reconstitution and fitted maximal rate,not Pop5-alone sufficiency. |
| archaeal-fidelity | https://pmc.ncbi.nlm.nih.gov/articles/PMC3378863/; Figures1/2,Table2,assayMethods. | supports | Distinct Pfu trans and Mja cis protocols change correct-site fractions and fitted rates; total amplitudes and condition inconsistencies remain explicit. |
| pho-binding-dose | https://pmc.ncbi.nlm.nih.gov/articles/PMC4882637/; TableI,Figures2/5,SPR and cleavageMethods. | supports | Pair and Delta14C apparent-affinity effects; joint-dose cleavage endpoint; retained loop-mutant binding and missing supplemental sensorgrams. |
| human-biochemistry | https://pmc.ncbi.nlm.nih.gov/articles/PMC10589621/; Figures3-7;supplementMethodspp1-6,FigureS2p8,legendspp11-12. | supports | Fraction and preparation effects,partial reconstitution omission,sedimentation andRNAi; no enhanced40minMono inFigure4C or proven intrinsic chemical site. |
| evidence-gaps | evidence/PF01900/gaps.txt; Dated search,access,attribution and coverage ledger. | supports | Missing contexts,methods and source discrepancies are explicit; skill and repository reads work while one offline renderer needed a scoped cache-access retry. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01900 | data/families/PF01900.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Original2010Figures3/4/7 and supplementTableS2,2012Figures1/2, 2015Figures2/5,2023Figures3-7 and supplementS2,2026Figure2 and supplement2 were visually inspected. Primary text/tables and supplementary methods were read within the retained scope. No raw gel reanalysis,genotype sequencing, independent replication or exhaustive primary-literature search is claimed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T220937Z-pf01900-pop5-rpp14-context-specific-rna-effects
title: Pop5 and Rpp14 context-specific RNA effects and causal limits
started_at: '2026-10-11T22:06:16Z'
finished_at: '2026-10-11T22:09:37Z'
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
summary: Nineteen scoped graphs retain35 observed effects:3direct,14unresolved, 18indirect;2mechanistic
  and17phenotypic graphs. Primary figures and recovered supplementary methods constrain
  joint archaeal protocols, SPR and dose effects, human preparation assays and cell-level
  knockdown/rescue. Two open discussions preserve causal-attribution and family-coverage
  work. Status is IN_PROGRESS; this is partial same-agent scientific review,not approval
  of every family member or completion of the8296-record goal.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01900.yaml
    sha256: b2181351866305293c0921fbb351dee20ab6fb24f4fd02d84f396f2925f5b413
    role: context
  - path: data/families/PF01900.yaml
    sha256: 4b6210c7ee6a5dfeea1271c1f0b2fc6b649aa1c7dd7199f4fb047d4c64eaf89f
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
  - path: evidence/PF01900/human-2026.txt
    role: context
    sha256: 4cf799887d0f8f998bb4f261d08f4f5998c12aff9e4e512680424f3e37d118eb
  - path: evidence/PF01900/identity.txt
    role: context
    sha256: 7b21b1074789d1aa30012ffab645e04276213a0fca90b88c859f022f8179ca62
  - path: evidence/PF01876/chen-2010-reconstitution.txt
    role: context
    sha256: 6d5205a18821029b23b745b445c8819bfe9b28fc050995cc6bbf2a85588432d4
  - path: evidence/PF01876/chen-2012-fidelity.txt
    role: context
    sha256: c68f4c212e38991b9b58de6054a6efbded483d35baec71a2c767d96c7bc5384a
  - path: evidence/PF01900/hamasaki-2015-pop5.txt
    role: context
    sha256: f1bdd22119e3805dac8355bc6efd3623921a1a2395fe86464afad3ec8039d87f
  - path: evidence/PF01900/human-2023.txt
    role: context
    sha256: bd2e70bfac8e3e11d6e7e1fdc688e6dd71ed0f76bcd5eedc7e3796d1690ba0dc
  - path: evidence/PF01900/gaps.txt
    role: context
    sha256: 84c54b42197ebde1272fd31932c83a761c9fb05dd4b2133b615ecd5150b4739a
targets:
- target_id: PF01900
  path: data/families/PF01900.yaml
  label: PF01900
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01900.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: ebb83480db23e6496c1105dccf1b2bb13efac5401a187cde487575d11225bc77
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01900, next uncurated accession after PF01899; six mapped archaeal/human
    references and selected primary biochemical/cellular assays.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01900
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: The5287 frozen proteins are not exhaustively characterized. Full original
      2006loop-deletion and2013helix/FRETmethods/figures,2015mutantSPRcurves, exacthumanclone
      sequences/doses,2008MjacisTyr,2011assembly,2012annealing, yeast/otherarchaealcontexts,1999/2002humanbiochemistry,2024telomere
      and metazoanMRP evidence remain follow-ups. Abstracts,structures and association
      networks are not promoted to observed causal edges.
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
  - PF01900
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC13408128/
  locator: Figure2c-e/j-l/o/r/s; SupplementFigure2d/e; Methods; SupplementData2.
  accessed_at: '2026-10-11T22:09:37Z'
  support: supports
  snapshot_sha256: 4cf799887d0f8f998bb4f261d08f4f5998c12aff9e4e512680424f3e37d118eb
  summary: RPP14-targeted HeLa Mirror populations have lower H1/MRP RNA and higher
    unprocessed MALAT1/MEN-beta/ITS1site2 signals. POP5 targeting lowers H1/MRP with28S
    normalization. IntronlessRPP14 suppresses H1/MRP and lncRNA-junction defects separately
    in TRNAU1AP and PRPF39 backgrounds. Residual RPP14 mRNA, replicate/statistical
    discrepancies, unverified transgene sequence and suppression rather than RPP14-null
    complementation are explicit.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01900/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T22:09:37Z'
  support: supports
  snapshot_sha256: 7b21b1074789d1aa30012ffab645e04276213a0fca90b88c859f022f8179ca62
  summary: 'FrozenPF01900 is formerDUF69,notPF01899/DUF68. Six UniProt sequences exactly
    match versioned NCBI references: O26783/AAB85192.1,MTH_687,124aa,domain13-116;
    Q57917/AAB98484.1,MJ0494,134aa,17-111; Q8U151/AAL81502.1,PF1378,120aa,17-113;
    O59150/BAA30588.1,PH1481,120aa,17-113; humanO95059/NP_008973.1,124aa,35-108; humanQ969H6/NP_057002.2,163aa,7-115.
    Current reference matches do not sequence each assay vial or human transgene.
    Pop5 and Rpp14 remain distinct members, and Rpp30R107A is not transferred. Delta14C
    overlaps only107-113 ofPfam.'
- evidence_id: archaeal-reconstitution
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3001054/
  locator: Table1,Figures3/4/7;supplementMethods/TableS2/pulse-chase controls.
  summary: Joint archaeal protein and ionic protocols; minimal-RNA reconstitution
    and fitted maximal rate,not Pop5-alone sufficiency.
  accessed_at: '2026-10-11T22:09:37Z'
  support: supports
  snapshot_sha256: 6d5205a18821029b23b745b445c8819bfe9b28fc050995cc6bbf2a85588432d4
- evidence_id: archaeal-fidelity
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3378863/
  locator: Figures1/2,Table2,assayMethods.
  summary: Distinct Pfu trans and Mja cis protocols change correct-site fractions
    and fitted rates; total amplitudes and condition inconsistencies remain explicit.
  accessed_at: '2026-10-11T22:09:37Z'
  support: supports
  snapshot_sha256: c68f4c212e38991b9b58de6054a6efbded483d35baec71a2c767d96c7bc5384a
- evidence_id: pho-binding-dose
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4882637/
  locator: TableI,Figures2/5,SPR and cleavageMethods.
  summary: Pair and Delta14C apparent-affinity effects; joint-dose cleavage endpoint;
    retained loop-mutant binding and missing supplemental sensorgrams.
  accessed_at: '2026-10-11T22:09:37Z'
  support: supports
  snapshot_sha256: f1bdd22119e3805dac8355bc6efd3623921a1a2395fe86464afad3ec8039d87f
- evidence_id: human-biochemistry
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10589621/
  locator: Figures3-7;supplementMethodspp1-6,FigureS2p8,legendspp11-12.
  summary: Fraction and preparation effects,partial reconstitution omission,sedimentation
    andRNAi; no enhanced40minMono inFigure4C or proven intrinsic chemical site.
  accessed_at: '2026-10-11T22:09:37Z'
  support: supports
  snapshot_sha256: bd2e70bfac8e3e11d6e7e1fdc688e6dd71ed0f76bcd5eedc7e3796d1690ba0dc
- evidence_id: evidence-gaps
  kind: search
  search_scope: Ignored/hidden-inclusive PF01900/DUF69/Rpp14/Pop5/RNP2 search in local
    curation,evidence,history,reviews,reports; public primary searches for Pop5 MTH687,exact2013title/DOI,2006ph1481p-loop
    deletion and OHu15516D. Source inspection is bounded to the cited primary articles,
    figures,supplements and six current reference mappings. Missing full 2006/2013methods
    and2015mutantcurves are access/coverage limits,not evidence of absence. No exhaustive
    literature or all-member audit.
  reference: evidence/PF01900/gaps.txt
  locator: Dated search,access,attribution and coverage ledger.
  summary: Missing contexts,methods and source discrepancies are explicit; skill and
    repository reads work while one offline renderer needed a scoped cache-access
    retry.
  accessed_at: '2026-10-11T22:09:37Z'
  support: supports
  snapshot_sha256: 84c54b42197ebde1272fd31932c83a761c9fb05dd4b2133b615ecd5150b4739a
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T22:09:37Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01900
  kind: record_content
  reference: data/families/PF01900.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T22:09:37Z'
  support: context_only
  snapshot_sha256: 4b6210c7ee6a5dfeea1271c1f0b2fc6b649aa1c7dd7199f4fb047d4c64eaf89f
  quote: "id: Pfam:PF01900\npfam_id: PF01900\nname: Rpp14/Pop5 family\nshort_name:\
    \ RNase_P_Rpp14\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01900\n\
    counters:\n  proteins: 5287\n  matches: 5297\n  proteomes: 3673\n  taxa: 9445\n\
    \  structures: 15\n  alphafold_models: 4599\n  domain_architectures: 79\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002759\ndescription: tRNA processing enzyme ribonuclease\
    \ P (RNase P) is a ubiquitous ribozyme that catalyzes a\n  Mg2-dependent hydrolysis\
    \ to remove the 5'-leader sequence of precursor tRNA (pre-tRNA). Archaeal and\n\
    \  eukaryotic RNase P consist of a single RNA and archaeal RNase P has four or\
    \ five proteins, while eukaryotic\n  RNase P consists of 9 or 10 proteins [[cite:PUB00007201]].\
    \ Human RNase P is composed of a singular protein\n  Pop1 and three subcomplexes,\
    \ the Rpp20-Rpp25 heterodimer, Pop5-Rpp14- (Rpp30)2-Rpp40 heteropentamer,\n  and\
    \ Rpp21-Rpp29-Rpp38 heterotrimer. This family includes Rnp2 (also known as Pop5)\
    \ from archaea [[cite:PUB00097410]]\n  and Pop5/Rpp14 from eukaryotes [[cite:PUB00100655],[cite:PUB00097413]].\n\
    curation_history: history/records/PF01900\ndiscussions:\n- discussion_id: pop5-catalytic-attribution-and-methods\n\
    \  prompt: Resolve preparation, construct and assay discrepancies before assigning\
    \ direct Pop5/Rpp14 chemistry.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale:\
    \ Observed fraction and cell-level effects do not prove an isolated-domain nuclease,\
    \ RNA stability\n    mechanism or universal catalytic requirement.\n  evidence:\n\
    \  - reference: PMID:37831743\n    supports: PARTIAL\n    evidence_source: primary_figures_and_recovered_supplement\n\
    \    explanation: Figure4C lacks enhanced40minMono; Mg-free preparations are about95%\
    \ pure; RNAi protein\n      depletion failed; Figure6 gradient labels conflict.\n\
    \  - reference: PMID:42277007\n    supports: PARTIAL\n    evidence_source: primary_methods_figures_supplement_and_oligo_table\n\
    \    explanation: Residual RPP14 mRNA, replicate/test discrepancies and upstream-suppression\
    \ rather than\n      RPP14-null rescue remain material.\n  - reference: PMID:26152732\n\
    \    supports: PARTIAL\n    evidence_source: primary_table_methods_and_original_figures\n\
    \    explanation: Different SPR fits, unavailable mutant sensorgrams and cleavage-dose\
    \ versus molecular-stoichiometry\n      distinction remain explicit.\n  posed_by:\
    \ Codex\n  posed_date: '2026-10-11'\n  notes: Obtain exact transgene sequences/doses,\
    \ matched-buffer biochemical tests, catalytic-site controls\n    and endpoint-specific\
    \ rescue. Hash-anchored ledgers are under evidence/PF01900; reused archaeal ledgers\n\
    \    under PF01876.\n- discussion_id: pop5-family-and-historical-coverage\n  prompt:\
    \ Extend primary causal review to additional Pop5/Rpp14 homologs and historical\
    \ mutation studies.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: Six reference\
    \ mappings and selected archaeal/human assays do not characterize all5287 frozen\n\
    \    proteins. Renaming DUF69 does not establish family-wide function.\n  evidence:\n\
    \  - reference: PMID:16430919\n    supports: PARTIAL\n    evidence_source: primary_abstract_only\n\
    \    explanation: Loop-deletion dimerization and reconstitution lead; full original\
    \ methods/figures still\n      needed.\n  - reference: PMID:24120499\n    supports:\
    \ PARTIAL\n    evidence_source: primary_abstract_only\n    explanation: C-terminal\
    \ helix deletion/FRET lead; complete original conditions and control data still\n\
    \      needed.\n  - reference: PMID:20705647\n    supports: PARTIAL\n    evidence_source:\
    \ primary_methods_figures_and_supplement\n    explanation: Pair reconstitution\
    \ and locus table are inspected; other homologs and heterologous RNA\n      contexts\
    \ remain outside these retained graphs.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n\
    \  notes: Review2008Mja cis-Tyr,2011assembly,2012annealing,2018yeast,2022Mja,1999/2002human\
    \ discovery/catalysis,2024POP5telomere\n    and metazoanMRP leads. No unsupported\
    \ edge fills a coverage gap; partial self-review leaves IN_PROGRESS.\ncausal_graphs:\n\
    - graph_id: mth-pop5-pair-optimized-rate\n  title: Mth Pop5/Rpp30 protocol increases\
    \ fitted cleavage rate\n  scope: Chen2010 Table1/Figure7; M. thermautotrophicus\
    \ DeltaH RNase P trans-cleavage.\n  context: 55 C,pH5.8,about2 nM E. coli pre-tRNATyr.\
    \ RNA-alone0.3-20 uM at2 M NH4/500 mM Mg; pair1-10\n    uM RNA,2-fold protein\
    \ excess,0.8 M NH4/120 mM Mg.\n  family_mapping: O26783/MTH_687 reference equals\
    \ AAB85192.1,124 aa,PF01900 13-116. Chen2010 supplement\n    TableS2 identifies\
    \ MTH687 as Pop5, not adjacent Rpp30/MTH688; tag-free, sequence-checked full-length\n\
    \    cloning.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:187420\n  limitations:\
    \ The intervention includes both proteins and changed ionic conditions. This is\
    \ not a matched-buffer\n    Pop5-only effect, measured Kd, or observation of ES-to-ES-star\
    \ motion. Maximal kobs is fitted; rapid-dissociation\n    controls do not cover\
    \ the faster pair reaction.\n  nodes:\n  - node_id: pair-protocol\n    label:\
    \ Add Pop5/Rpp30 and switch to its optimized ionic protocol\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:O26783\n  - node_id: maximal-kobs\n    label:\
    \ Fitted maximal pre-tRNA cleavage kobs\n    node_type: ACTIVITY\n  edges:\n \
    \ - edge_id: pair-protocol-increases-maximal-kobs\n    subject: pair-protocol\n\
    \    predicate: increases\n    object: maximal-kobs\n    mechanism: The composite\
    \ protocol raises maximal kobs from0.13+/-0.01 to7.9+/-1 per min. It does not\n\
    \      isolate the contribution of Pop5 from Rpp30 or salts.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:20705647\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3001054/\n\
    \      snippet: Single-turnover kinetic studies\n      explanation: Table1 and\
    \ original Figure7; supplementary cloning/TableS2 and pulse-chase qualification.\n\
    \      cache_path: evidence/PF01876/chen-2010-reconstitution.txt\n      cache_sha256:\
    \ 6d5205a18821029b23b745b445c8819bfe9b28fc050995cc6bbf2a85588432d4\n- graph_id:\
    \ mja-pop5-full-rna\n  title: Pop5/Rpp30 supports Mja full-length RNA cleavage\n\
    \  scope: Chen2010; full-length Mja RPR.\n  context: 10 nM RNA,100 nM each protein,500\
    \ nM E. coli pre-tRNATyr,30min55 C,Tris7.5/100 mM NH4/120 mM\n    Mg; RNA control800\
    \ mM NH4/30 mM Mg.\n  family_mapping: Q57917/MJ0494 reference equals AAB98484.1,134\
    \ aa,PF01900 17-111. Chen2010 supplement\n    TableS2 and cloning methods identify\
    \ the tag-free Pop5 member. RNA truncations are not deletions of\n    the protein\
    \ domain.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:243232\n  limitations:\
    \ RNA-alone control has different salts. Pop5/Rpp30 without RNA is negative; Rpp21/Rpp29\n\
    \    alone does not activate the displayed RNA. This is joint reconstitution,\
    \ not Pop5-alone cleavage or\n    isolated-domain sufficiency.\n  nodes:\n  -\
    \ node_id: pair-reconstitution\n    label: Combine the specified Mja RNA with\
    \ Pop5/Rpp30 and its assay buffer\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q57917\n  - node_id: cleavage-products\n    label: Detected mature-tRNA\
    \ and leader products\n    node_type: ACTIVITY\n  edges:\n  - edge_id: pair-reconstitution-enables-cleavage-products\n\
    \    subject: pair-reconstitution\n    predicate: enables\n    object: cleavage-products\n\
    \    mechanism: The specified RNA/protein/buffer combination gives the displayed\
    \ products. RNA and both\n      proteins remain a conjunction; the experiment\
    \ does not identify a protein catalytic residue.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:20705647\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3001054/\n\
    \      snippet: Single-turnover kinetic studies\n      explanation: Figure3 upper\
    \ panel, lanes3-7 and Methods/supplement.\n      cache_path: evidence/PF01876/chen-2010-reconstitution.txt\n\
    \      cache_sha256: 6d5205a18821029b23b745b445c8819bfe9b28fc050995cc6bbf2a85588432d4\n\
    - graph_id: mja-pop5-delta-s\n  title: Pop5/Rpp30 supports Mja delta-S RNA cleavage\n\
    \  scope: Chen2010; Mja RPR delta-S lacking nts67-192.\n  context: 500 nM RNA,1\
    \ uM proteins,1 uM substrate,15min55 C,Tris7.5/400 mM NH4; pair120 mM Mg versus\n\
    \    RNA control30 mM.\n  family_mapping: Q57917/MJ0494 reference equals AAB98484.1,134\
    \ aa,PF01900 17-111. Chen2010 supplement\n    TableS2 and cloning methods identify\
    \ the tag-free Pop5 member. RNA truncations are not deletions of\n    the protein\
    \ domain.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:243232\n  limitations:\
    \ RNA-alone control has different salts. Pop5/Rpp30 without RNA is negative; Rpp21/Rpp29\n\
    \    alone does not activate the displayed RNA. This is joint reconstitution,\
    \ not Pop5-alone cleavage or\n    isolated-domain sufficiency.\n  nodes:\n  -\
    \ node_id: pair-reconstitution\n    label: Combine the specified Mja RNA with\
    \ Pop5/Rpp30 and its assay buffer\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q57917\n  - node_id: cleavage-products\n    label: Detected mature-tRNA\
    \ and leader products\n    node_type: ACTIVITY\n  edges:\n  - edge_id: pair-reconstitution-enables-cleavage-products\n\
    \    subject: pair-reconstitution\n    predicate: enables\n    object: cleavage-products\n\
    \    mechanism: The specified RNA/protein/buffer combination gives the displayed\
    \ products. RNA and both\n      proteins remain a conjunction; the experiment\
    \ does not identify a protein catalytic residue.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:20705647\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3001054/\n\
    \      snippet: Single-turnover kinetic studies\n      explanation: Figure4 upper\
    \ panel, lanes3-7 and Methods/supplement.\n      cache_path: evidence/PF01876/chen-2010-reconstitution.txt\n\
    \      cache_sha256: 6d5205a18821029b23b745b445c8819bfe9b28fc050995cc6bbf2a85588432d4\n\
    - graph_id: mja-pop5-minimal-rna\n  title: Pop5/Rpp30 supports the minimal Mja\
    \ RNA\n  scope: Chen2010; 112nt Mja RPR delta-S-Min.\n  context: 500 nM RNA,1\
    \ uM proteins,1 uM substrate,15min55 C,Tris7.5/400 mM NH4; pair120 mM Mg versus\n\
    \    RNA control30 mM.\n  family_mapping: Q57917/MJ0494 reference equals AAB98484.1,134\
    \ aa,PF01900 17-111. Chen2010 supplement\n    TableS2 and cloning methods identify\
    \ the tag-free Pop5 member. RNA truncations are not deletions of\n    the protein\
    \ domain.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:243232\n  limitations:\
    \ RNA-alone control has different salts. Pop5/Rpp30 without RNA is negative; Rpp21/Rpp29\n\
    \    alone does not activate the displayed RNA. This is joint reconstitution,\
    \ not Pop5-alone cleavage or\n    isolated-domain sufficiency.\n  nodes:\n  -\
    \ node_id: pair-reconstitution\n    label: Combine the specified Mja RNA with\
    \ Pop5/Rpp30 and its assay buffer\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q57917\n  - node_id: cleavage-products\n    label: Detected mature-tRNA\
    \ and leader products\n    node_type: ACTIVITY\n  edges:\n  - edge_id: pair-reconstitution-enables-cleavage-products\n\
    \    subject: pair-reconstitution\n    predicate: enables\n    object: cleavage-products\n\
    \    mechanism: The specified RNA/protein/buffer combination gives the displayed\
    \ products. RNA and both\n      proteins remain a conjunction; the experiment\
    \ does not identify a protein catalytic residue.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:20705647\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3001054/\n\
    \      snippet: Single-turnover kinetic studies\n      explanation: Figure4 lower\
    \ panel, lanes3-7 and Methods/supplement.\n      cache_path: evidence/PF01876/chen-2010-reconstitution.txt\n\
    \      cache_sha256: 6d5205a18821029b23b745b445c8819bfe9b28fc050995cc6bbf2a85588432d4\n\
    - graph_id: pfu-pop5-gln-fidelity\n  title: Pfu Pop5/Rpp30 protocol favors the\
    \ correct cleavage site\n  scope: Chen2012 Figure1C; P. furiosus RNase P with\
    \ nonconsensus Synechocystis PCC6803 pre-tRNAGln.\n  context: 55 C,2 nM labeled\
    \ substrate. RNA alone15 uM for9h; pair200 nM RNA/2 uM proteins for30min. Ionic\n\
    \    protocols separately optimized.\n  family_mapping: Q8U151/PF1378 reference\
    \ equals AAL81502.1,120 aa,PF01900 17-113. Supplement TableS2\n    identifies\
    \ this Pop5 locus. Exact2012 assay aliquot sequence was not independently established.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:186497\n  limitations: Different\
    \ RNA doses, durations and buffers prevent a protein-only rate comparison. The\n\
    \    endpoint is correct/(correct+miscleaved), not fraction of starting substrate\
    \ or total conversion.\n    Four-protein value0.92 is a distinct condition.\n\
    \  nodes:\n  - node_id: pair-protocol\n    label: Use the Pfu RNA plus Pop5/Rpp30\
    \ cleavage protocol\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q8U151\n\
    \  - node_id: correct-fraction\n    label: Correct-site fraction among cleavage\
    \ products\n    node_type: ACTIVITY\n  edges:\n  - edge_id: pair-protocol-increases-correct-fraction\n\
    \    subject: pair-protocol\n    predicate: increases\n    object: correct-fraction\n\
    \    mechanism: The displayed fraction rises from0.11+/-0.03 to0.59+/-0.01. This\
    \ is a composite-protocol\n      fidelity endpoint, not evidence of a directly\
    \ observed substrate-docking transition.\n    directness: UNRESOLVED\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:22298511\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3378863/\n      snippet:\
    \ Data analysis\n      explanation: Original Figure1C lanes2/4, Results and assay\
    \ Methods.\n      cache_path: evidence/PF01876/chen-2012-fidelity.txt\n      cache_sha256:\
    \ c68f4c212e38991b9b58de6054a6efbded483d35baec71a2c767d96c7bc5384a\n- graph_id:\
    \ mja-pop5-gln-cis\n  title: Mja Pop5/Rpp30 protocol changes cis-cleavage rate\
    \ and fidelity\n  scope: Chen2012 Table2/Figure2; pre-tRNAGln-AAU-MjaRPR self-cleaving\
    \ construct.\n  context: 55 C,pH6,nominal50 nM RNA/500 nM proteins; separate assembly/cleavage\
    \ phases. RNA-alone2.5\n    M NH4/500 mM Mg versus pair0.8 M NH4/nominal100 mM\
    \ Mg.\n  family_mapping: Q57917/MJ0494 reference equals AAB98484.1,134 aa,PF01900\
    \ 17-111. Chen2010 supplement\n    TableS2 and cloning methods identify the tag-free\
    \ Pop5 member. RNA truncations are not deletions of\n    the protein domain.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:243232\n  limitations: Older protocol\
    \ mixing and reference-number inconsistencies remain unresolved; do not assert\n\
    \    matched final conditions. Tethered substrate is not trans cleavage. Derived\
    \ parallel-pathway constants\n    and older rescaled Tyr rates are not new observed\
    \ microsteps.\n  nodes:\n  - node_id: pair-protocol\n    label: Assemble the cis\
    \ construct with Pop5/Rpp30 under its optimized protocol\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q57917\n  - node_id: cis-kobs\n    label: Fitted\
    \ total cis-cleavage kobs\n    node_type: ACTIVITY\n  - node_id: correct-fraction\n\
    \    label: Correct-site fraction of cis-cleavage products\n    node_type: ACTIVITY\n\
    \  edges:\n  - edge_id: pair-protocol-increases-cis-kobs\n    subject: pair-protocol\n\
    \    predicate: increases\n    object: cis-kobs\n    mechanism: Table2 gives0.004+/-0.0004\
    \ to2.5+/-0.1 per min. Both correct and incorrect products contribute;\n     \
    \ no autonomous Pop5 nuclease is implied.\n    directness: UNRESOLVED\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:22298511\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3378863/\n      snippet:\
    \ Data analysis\n      explanation: Table2, original Figure2 and Methods.\n  \
    \    cache_path: evidence/PF01876/chen-2012-fidelity.txt\n      cache_sha256:\
    \ c68f4c212e38991b9b58de6054a6efbded483d35baec71a2c767d96c7bc5384a\n  - edge_id:\
    \ pair-protocol-increases-correct-fraction\n    subject: pair-protocol\n    predicate:\
    \ increases\n    object: correct-fraction\n    mechanism: The fitted fraction\
    \ rises from0.18+/-0.01 to0.43+/-0.01. Total amplitudes93% and96% are\n      different\
    \ quantities; the four-protein61% amplitude is not complete conversion.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:22298511\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3378863/\n\
    \      snippet: Data analysis\n      explanation: Table2 and original Figure2;\
    \ retained2012 protocol ledger.\n      cache_path: evidence/PF01876/chen-2012-fidelity.txt\n\
    \      cache_sha256: c68f4c212e38991b9b58de6054a6efbded483d35baec71a2c767d96c7bc5384a\n\
    - graph_id: pho-pop5-sl3-affinity\n  title: Pop5 partnership and C-terminal deletion\
    \ change apparent SL3 affinity\n  scope: Hamasaki2015 TableI/Figure2; P. horikoshii\
    \ Pop5 and Ta-SL3 SPR.\n  context: 25 C,20 mM phosphate7.2,500 mM NH4Cl,0.05%Tween20,immobilized\
    \ Ta-SL3; sequential4.8 nM-3 uM\n    analyte.\n  family_mapping: O59150/PH1481\
    \ reference equals BAA30588.1,120 aa,PF01900 17-113. Delta14C removes reference107-120,\n\
    \    overlapping the domain at107-113; DeltaL43-48 is internal. Rpp30 R107A is\
    \ not a Pop5 mutation.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:70601\n\
    \  limitations: Different steady-state and Langmuir fits and Rmax values limit\
    \ numerical fold comparisons.\n    Specific binding is not seen in high-Mg cleavage\
    \ buffer. DeltaL43-48 retains specific binding atKd6.52\n    nM. Delta14C supplemental\
    \ sensorgrams were not visually inspected; its TableI result was.\n  nodes:\n\
    \  - node_id: pair-vs-pop5\n    label: Use Pop5/Rpp30 instead of Pop5 alone\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:O59150\n  - node_id:\
    \ delta14c\n    label: Replace Pop5 with its C-terminal14-residue deletion in\
    \ the pair\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:O59150\n\
    \  - node_id: sl3-affinity\n    label: Apparent Ta-SL3 affinity\n    node_type:\
    \ ACTIVITY\n  - node_id: mutant-sl3-affinity\n    label: Apparent Ta-SL3 affinity\
    \ of the Pop5/Rpp30 preparation\n    node_type: ACTIVITY\n  edges:\n  - edge_id:\
    \ pair-vs-pop5-increases-sl3-affinity\n    subject: pair-vs-pop5\n    predicate:\
    \ increases\n    object: sl3-affinity\n    mechanism: The pair has fitted Kd2.27\
    \ nM versus2410 nM for Pop5 alone. Binding improvement is measured,\n      but\
    \ binding does not itself establish full-RNA activation.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:26152732\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4882637/\n\
    \      snippet: Kinetic constants\n      explanation: TableI and original Figure2;\
    \ printed830-fold claim is not adopted.\n      cache_path: evidence/PF01900/hamasaki-2015-pop5.txt\n\
    \      cache_sha256: f1bdd22119e3805dac8355bc6efd3623921a1a2395fe86464afad3ec8039d87f\n\
    \  - edge_id: delta14c-decreases-mutant-sl3-affinity\n    subject: delta14c\n\
    \    predicate: decreases\n    object: mutant-sl3-affinity\n    mechanism: Replacing\
    \ Pop5 with Delta14C gives Kd1770 nM versus2.27 nM for the WT pair. It weakens\n\
    \      but does not abolish pair binding; folding and complex stability are not\
    \ excluded explanations.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:26152732\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC4882637/\n      snippet: Kinetic constants\n\
    \      explanation: TableI and C-terminal-mutant Results; supplementary curve\
    \ unavailable.\n      cache_path: evidence/PF01900/hamasaki-2015-pop5.txt\n  \
    \    cache_sha256: f1bdd22119e3805dac8355bc6efd3623921a1a2395fe86464afad3ec8039d87f\n\
    - graph_id: pho-pop5-pair-dose\n  title: Joint Pop5/Rpp30 dose increases reconstituted\
    \ cleavage\n  scope: Hamasaki2015 original Figure5 open-circle series; P. horikoshii\
    \ RNase P.\n  context: 5-to30 pmol each Pop5/Rpp30,10 pmol RNA and each Rpp21/Rpp29/Rpp38;15min75\
    \ C,50 mM Tris7.6,50\n    mM MgCl2,600 mM NH4OAc,60 mM NH4Cl.\n  family_mapping:\
    \ O59150/PH1481 reference equals BAA30588.1,120 aa,PF01900 17-113. Delta14C removes\
    \ reference107-120,\n    overlapping the domain at107-113; DeltaL43-48 is internal.\
    \ Rpp30 R107A is not a Pop5 mutation.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:70601\n\
    \  limitations: The measured endpoint plateaus near70-75%,not100%. Both proteins\
    \ are titrated; this does\n    not establish Pop5-alone sufficiency or directly\
    \ measure molecular stoichiometry. Triplicate assays.\n  nodes:\n  - node_id:\
    \ increase-pair-dose\n    label: Increase Pop5 and Rpp30 together from5 to30 pmol\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:O59150\n  - node_id:\
    \ cleavage-endpoint\n    label: Pre-tRNATyr cleavage fraction after15 minutes\n\
    \    node_type: ACTIVITY\n  edges:\n  - edge_id: increase-pair-dose-increases-cleavage-endpoint\n\
    \    subject: increase-pair-dose\n    predicate: increases\n    object: cleavage-endpoint\n\
    \    mechanism: The open-circle series rises from roughly23% to70% over this range\
    \ with the other components\n      fixed. This is a direct effect in the assembled\
    \ biochemical assay, not an intracellular assembly\n      sequence.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:26152732\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4882637/\n\
    \      snippet: Kinetic constants\n      explanation: Original Figure5 and pre-tRNA\
    \ cleavage Methods.\n      cache_path: evidence/PF01900/hamasaki-2015-pop5.txt\n\
    \      cache_sha256: f1bdd22119e3805dac8355bc6efd3623921a1a2395fe86464afad3ec8039d87f\n\
    - graph_id: human-rpp14-f14\n  title: Rpp14 addition changes HEK293 fraction-associated\
    \ RNA products\n  scope: 2023 Figure3; F14 from HEK293 S100/tRNAArg transcription\
    \ complexes.\n  context: Gradient-isolated F14 with or without recombinant His-Rpp14;\
    \ internally labeled S. pombe pre-tRNASer\n    plus excess cold precursor;37 C,MRP/TNET\
    \ with nominal15 mM Mg,10 mM DTT,rRNasin.\n  family_mapping: Human RPP14 reference\
    \ O95059 equals NP_008973.1,124 aa,sequence version3,PF01900 35-108.\n    This\
    \ is gene-to-family mapping; exact experimental cDNA, tag termini and allele sequences\
    \ are not\n    independently verified.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:9606\n\
    \  limitations: Exact protein dose and full buffer composition are unresolved.\
    \ Fractions contain other\n    proteins; Rpp14 alone is negative in the Mg-containing\
    \ Figure2 assay. These are preparation-dependent\n    signals, not direct Rpp14\
    \ phosphorolysis or catalytic-site assignments.\n  nodes:\n  - node_id: add-rpp14\n\
    \    label: Add the recombinant Rpp14 preparation to F14\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:O95059\n  - node_id: early-leader\n    label:\
    \ Excised28nt leader signal at1-10 minutes\n    node_type: STATE\n  - node_id:\
    \ mononucleotide\n    label: Mononucleotide signal at5-40 minutes\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: add-rpp14-increases-early-leader\n    subject:\
    \ add-rpp14\n    predicate: increases\n    object: early-leader\n    mechanism:\
    \ Rpp14 addition raises the transient early leader signal, but both conditions\
    \ lose most\n      leader later. Accumulation reflects formation and removal,\
    \ not an independently measured endonuclease\n      rate.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:37831743\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10589621/\n\
    \      snippet: Substrate cleavage assays\n      explanation: Original Figure3A/B\
    \ and supplementary Methodspp2-6; at least3 independent experiments.\n      cache_path:\
    \ evidence/PF01900/human-2023.txt\n      cache_sha256: bd2e70bfac8e3e11d6e7e1fdc688e6dd71ed0f76bcd5eedc7e3796d1690ba0dc\n\
    \  - edge_id: add-rpp14-increases-mononucleotide\n    subject: add-rpp14\n   \
    \ predicate: increases\n    object: mononucleotide\n    mechanism: The supplemented\
    \ fraction has greater mononucleotide signal over the displayed times. This\n\
    \      supports an effect of added preparation in the fraction, not proof that\
    \ Rpp14 alone supplies the\n      catalytic chemistry.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:37831743\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10589621/\n\
    \      snippet: Substrate cleavage assays\n      explanation: Original Figure3A/C,\
    \ with the Figure2 Rpp14-alone negative control retained.\n      cache_path: evidence/PF01900/human-2023.txt\n\
    \      cache_sha256: bd2e70bfac8e3e11d6e7e1fdc688e6dd71ed0f76bcd5eedc7e3796d1690ba0dc\n\
    - graph_id: human-pop5-f39\n  title: Pop5 addition reduces precursor signal in\
    \ the HeLa F39 assay\n  scope: 2023 Figure4; F39 from HeLa S100/tRNATyr complexes\
    \ purified by gel filtration.\n  context: F39 with/without recombinant His-Pop5,0-40min37\
    \ C; internally labeled pre-tRNASer,excess cold\n    substrate,Mg-containing MRP/TNET.\n\
    \  family_mapping: Human POP5 reference Q969H6 equals NP_057002.2,163 aa,sequence\
    \ version1,PF01900 7-115.\n    POP5 and RPP14 are distinct members; exact experimental\
    \ insert or edited alleles are not independently\n    sequenced.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:9606\n  limitations: Figure4C40-minute mononucleotide\
    \ signals are approximately comparable, not increased by\n    Pop5. Leader signal\
    \ is lower; do not equate it to a higher cleavage rate. Exact dose unresolved;\
    \ fraction\n    and residual preparation components can mediate the result.\n\
    \  nodes:\n  - node_id: add-pop5\n    label: Add the recombinant Pop5 preparation\
    \ to F39\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q969H6\n\
    \  - node_id: intact-precursor\n    label: Intact pre-tRNASer signal during the\
    \ time course\n    node_type: STATE\n  edges:\n  - edge_id: add-pop5-decreases-intact-precursor\n\
    \    subject: add-pop5\n    predicate: decreases\n    object: intact-precursor\n\
    \    mechanism: The fraction-plus-Pop5 lanes show precursor loss relative to fraction\
    \ alone, as reported\n      with the original gel. No quantitative turnover constant\
    \ or autonomous Pop5 exonuclease is inferred.\n    directness: UNRESOLVED\n  \
    \  support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:37831743\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10589621/\n\
    \      snippet: Substrate cleavage assays\n      explanation: Original Figure4A\
    \ lanes4-8 versus14-18; B/C constrain interpretation.\n      cache_path: evidence/PF01900/human-2023.txt\n\
    \      cache_sha256: bd2e70bfac8e3e11d6e7e1fdc688e6dd71ed0f76bcd5eedc7e3796d1690ba0dc\n\
    - graph_id: human-rpp14-reconstitution-omission\n  title: Omitting Rpp14 lowers\
    \ products in H1-RNA reconstitution\n  scope: 2023 Figure5; H1 RNA plus fresh\
    \ recombinant Rpp14,20,21,25,29,30,40 and Pop5.\n  context: Compare complete assembly\
    \ with Rpp14 omission while the other seven proteins remain, in the\n    Mg-containing\
    \ assay.\n  family_mapping: Human RPP14 reference O95059 equals NP_008973.1,124\
    \ aa,sequence version3,PF01900 35-108.\n    This is gene-to-family mapping; exact\
    \ experimental cDNA, tag termini and allele sequences are not\n    independently\
    \ verified.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:9606\n  limitations:\
    \ Omission retains cleavage, so Rpp14 is not absolutely required under these conditions.\n\
    \    Exact protein doses and figure-specific reaction time remain unresolved.\
    \ Reconstituted RNase P does\n    not degrade excised leader; this is not the\
    \ fraction-associated exonuclease context.\n  nodes:\n  - node_id: omit-rpp14\n\
    \    label: Omit Rpp14 from the eight-protein H1-RNA assembly\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:O95059\n  - node_id: trna-product\n\
    \    label: tRNA product band intensity\n    node_type: STATE\n  - node_id: leader-product\n\
    \    label: Excised leader band intensity\n    node_type: STATE\n  edges:\n  -\
    \ edge_id: omit-rpp14-decreases-trna-product\n    subject: omit-rpp14\n    predicate:\
    \ decreases\n    object: trna-product\n    mechanism: Figure5B shows lower product\
    \ after Rpp14 omission than complete reconstitution. Partner\n      proteins and\
    \ catalytic RNA remain present; the mediating molecular step is unresolved.\n\
    \    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:37831743\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10589621/\n\
    \      snippet: Substrate cleavage assays\n      explanation: Original Figure5A\
    \ lane11 versus5 and Figure5B.\n      cache_path: evidence/PF01900/human-2023.txt\n\
    \      cache_sha256: bd2e70bfac8e3e11d6e7e1fdc688e6dd71ed0f76bcd5eedc7e3796d1690ba0dc\n\
    \  - edge_id: omit-rpp14-decreases-leader-product\n    subject: omit-rpp14\n \
    \   predicate: decreases\n    object: leader-product\n    mechanism: Figure5C\
    \ reports less leader after Rpp14 omission, but a residual band remains. This\
    \ is\n      not complete loss of cleavage or proof of a Rpp14 catalytic residue.\n\
    \    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:37831743\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10589621/\n\
    \      snippet: Substrate cleavage assays\n      explanation: Original Figure5A/C;\
    \ fresh-protein and storage limitations in supplement.\n      cache_path: evidence/PF01900/human-2023.txt\n\
    \      cache_sha256: bd2e70bfac8e3e11d6e7e1fdc688e6dd71ed0f76bcd5eedc7e3796d1690ba0dc\n\
    - graph_id: human-rpp14-mg-free\n  title: Rpp14-enriched preparation depletes\
    \ precursor without added divalent ions\n  scope: 2023 SupplementFigureS2C lane8;\
    \ recombinant human Rpp14.\n  context: Exo buffer50 mM KCl,15 mM Na2HPO4,20 mM\
    \ Tris8.0,100-300 ng cold pre-tRNASer,rRNasin,10 mM DTT;\n    Ni-affinity refolded\
    \ preparation.\n  family_mapping: Human RPP14 reference O95059 equals NP_008973.1,124\
    \ aa,sequence version3,PF01900 35-108.\n    This is gene-to-family mapping; exact\
    \ experimental cDNA, tag termini and allele sequences are not\n    independently\
    \ verified.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:9606\n  limitations:\
    \ Approximately95% purity by stained gel does not exclude residual nuclease contamination.\n\
    \    Exact assay dose/time and tag termini unresolved. No chemical-active-site,\
    \ reaction-direction or intrinsic\n    phosphorolysis claim; Mg-containing protein-alone\
    \ assays differ.\n  nodes:\n  - node_id: add-preparation\n    label: Add the Rpp14-enriched\
    \ recombinant preparation\n    node_type: PERTURBATION\n    grounding:\n    -\
    \ UniProtKB:O95059\n  - node_id: intact-precursor\n    label: Intact labeled pre-tRNASer\
    \ signal\n    node_type: STATE\n  edges:\n  - edge_id: add-preparation-decreases-intact-precursor\n\
    \    subject: add-preparation\n    predicate: decreases\n    object: intact-precursor\n\
    \    mechanism: The indicated lane shows precursor depletion and a mononucleotide\
    \ band, unlike Rpp20/Rpp25\n      controls. Causality is scoped to the preparation\
    \ and buffer, not proven assignment of catalytic\n      chemistry to the isolated\
    \ family domain.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:37831743\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC10589621/\n      snippet: Substrate\
    \ cleavage assays\n      explanation: Visually inspected SupplementFigureS2C lane8;\
    \ Methodspp5-6 and legendspp11-12.\n      cache_path: evidence/PF01900/human-2023.txt\n\
    \      cache_sha256: bd2e70bfac8e3e11d6e7e1fdc688e6dd71ed0f76bcd5eedc7e3796d1690ba0dc\n\
    - graph_id: human-pop5-mg-free\n  title: Pop5-enriched preparation depletes precursor\
    \ without added divalent ions\n  scope: 2023 SupplementFigureS2C lane12; recombinant\
    \ human Pop5.\n  context: Exo buffer50 mM KCl,15 mM Na2HPO4,20 mM Tris8.0,100-300\
    \ ng cold pre-tRNASer,rRNasin,10 mM DTT;\n    Ni-affinity refolded preparation.\n\
    \  family_mapping: Human POP5 reference Q969H6 equals NP_057002.2,163 aa,sequence\
    \ version1,PF01900 7-115.\n    POP5 and RPP14 are distinct members; exact experimental\
    \ insert or edited alleles are not independently\n    sequenced.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:9606\n  limitations: Approximately95% purity\
    \ by stained gel does not exclude residual nuclease contamination.\n    Exact\
    \ assay dose/time and tag termini unresolved. No chemical-active-site, reaction-direction\
    \ or intrinsic\n    phosphorolysis claim; Mg-containing protein-alone assays differ.\n\
    \  nodes:\n  - node_id: add-preparation\n    label: Add the Pop5-enriched recombinant\
    \ preparation\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q969H6\n\
    \  - node_id: intact-precursor\n    label: Intact labeled pre-tRNASer signal\n\
    \    node_type: STATE\n  edges:\n  - edge_id: add-preparation-decreases-intact-precursor\n\
    \    subject: add-preparation\n    predicate: decreases\n    object: intact-precursor\n\
    \    mechanism: The indicated lane shows precursor depletion and a mononucleotide\
    \ band, unlike Rpp20/Rpp25\n      controls. Causality is scoped to the preparation\
    \ and buffer, not proven assignment of catalytic\n      chemistry to the isolated\
    \ family domain.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:37831743\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC10589621/\n      snippet: Substrate\
    \ cleavage assays\n      explanation: Visually inspected SupplementFigureS2C lane12;\
    \ Methodspp5-6 and legendspp11-12.\n      cache_path: evidence/PF01900/human-2023.txt\n\
    \      cache_sha256: bd2e70bfac8e3e11d6e7e1fdc688e6dd71ed0f76bcd5eedc7e3796d1690ba0dc\n\
    - graph_id: human-rpp14-overexpression-sedimentation\n  title: Myc-Rpp14 overexpression\
    \ shifts active gradient fractions\n  scope: 2023 Figure6; HeLa cells transiently\
    \ expressing myc-Rpp14 for42h.\n  context: S100 tRNAArg transcription complexes,velocity\
    \ sedimentation,ex-vivo pre-tRNASer processing;\n    comparison with untransfected\
    \ controls.\n  family_mapping: Human RPP14 reference O95059 equals NP_008973.1,124\
    \ aa,sequence version3,PF01900 35-108.\n    This is gene-to-family mapping; exact\
    \ experimental cDNA, tag termini and allele sequences are not\n    independently\
    \ verified.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:9606\n  limitations:\
    \ Figure heading15-40% glycerol conflicts with text/Methods15-35%. Sedimentation\
    \ is not a\n    direct measurement of intracellular aggregation. Larger leader\
    \ accumulation is not increased mononucleotide\n    output; exact myc-cDNA sequence\
    \ unverified.\n  nodes:\n  - node_id: express-myc-rpp14\n    label: Overexpress\
    \ myc-Rpp14 before extract preparation\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:O95059\n  - node_id: sedimentation\n    label: Sedimentation\
    \ of fractions retaining RNase-P-associated activity\n    node_type: PHENOTYPE\n\
    \  edges:\n  - edge_id: express-myc-rpp14-increases-sedimentation\n    subject:\
    \ express-myc-rpp14\n    predicate: increases\n    object: sedimentation\n   \
    \ mechanism: Activity shifts toward later fractions20-24 compared with control14-20.\
    \ The measured difference\n      is extract-complex fractionation, not an observed\
    \ aggregation-to-processing molecular chain.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:37831743\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10589621/\n      snippet:\
    \ Substrate cleavage assays\n      explanation: Original Figure6A-D, Results and\
    \ velocity-sedimentation Methods; at least3 assays.\n      cache_path: evidence/PF01900/human-2023.txt\n\
    \      cache_sha256: bd2e70bfac8e3e11d6e7e1fdc688e6dd71ed0f76bcd5eedc7e3796d1690ba0dc\n\
    - graph_id: human-rpp14-shrna-arg-processing\n  title: RPP14 shRNAs impair Arg-tRNA\
    \ processing in HEK293 extracts\n  scope: 2023 Figure7D/H/I; three RPP14-targeting\
    \ shRNAs in HEK293.\n  context: Transient shRNAsA/Bcoding,C3UTR; S20 extracts24/48h\
    \ used for tRNAArg transcription/processing,\n    with PEI-only controls.\n  family_mapping:\
    \ Human RPP14 reference O95059 equals NP_008973.1,124 aa,sequence version3,PF01900\
    \ 35-108.\n    This is gene-to-family mapping; exact experimental cDNA, tag termini\
    \ and allele sequences are not\n    independently verified.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:9606\n  limitations: RPP14 mRNA decreases but protein depletion\
    \ was not established by western. No non-targeting\n    shRNA or target-resistant\
    \ rescue shown. Recovery at72h and variation among other tRNA endpoints prevent\n\
    \    universal tRNA or permanent-loss claims.\n  nodes:\n  - node_id: rpp14-shrna\n\
    \    label: Express the RPP14-targeting shRNAs\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:O95059\n  - node_id: arg-precursor\n    label:\
    \ Precursor-tRNAArg band signal at24/48 hours\n    node_type: STATE\n  - node_id:\
    \ arg-mature\n    label: Mature-tRNAArg band signal at24/48 hours\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: rpp14-shrna-increases-arg-precursor\n    subject:\
    \ rpp14-shrna\n    predicate: increases\n    object: arg-precursor\n    mechanism:\
    \ Targeting conditions accumulate precursor during extract transcription; persistent\
    \ transcription\n      does not prove an unchanged transcription rate.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:37831743\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10589621/\n\
    \      snippet: Substrate cleavage assays\n      explanation: Original Figure7D/H\
    \ and supplement knockdown Methodspp1-2.\n      cache_path: evidence/PF01900/human-2023.txt\n\
    \      cache_sha256: bd2e70bfac8e3e11d6e7e1fdc688e6dd71ed0f76bcd5eedc7e3796d1690ba0dc\n\
    \  - edge_id: rpp14-shrna-decreases-arg-mature\n    subject: rpp14-shrna\n   \
    \ predicate: decreases\n    object: arg-mature\n    mechanism: Mature-product\
    \ signal is reduced in the targeting conditions, with recovery toward72h.\n  \
    \    This is a whole-gene extract phenotype, not isolated-domain catalysis.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:37831743\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10589621/\n\
    \      snippet: Substrate cleavage assays\n      explanation: Original Figure7D/I;\
    \ mRNA engagement and unsuccessful protein western explicitly retained.\n    \
    \  cache_path: evidence/PF01900/human-2023.txt\n      cache_sha256: bd2e70bfac8e3e11d6e7e1fdc688e6dd71ed0f76bcd5eedc7e3796d1690ba0dc\n\
    - graph_id: human-rpp14-cas9-rna-processing\n  title: RPP14 targeting changes\
    \ catalytic-RNA levels and precursor accumulation\n  scope: Panah2026 Figure2c-e/o/s;\
    \ RPP14-targeted HeLa Mirror populations.\n  context: HeLa Mirror reporter populations,lentiviralCas9/sgRNA,72h\
    \ then4days blasticidin,FACS sorting,3h\n    before total-RNA extraction;37 C\
    \ DMEM10%FBS,RT-qPCR delta-deltaCt.18S rRNA normalization.\n  family_mapping:\
    \ Human RPP14 reference O95059 equals NP_008973.1,124 aa,sequence version3,PF01900\
    \ 35-108.\n    This is gene-to-family mapping; exact experimental cDNA, tag termini\
    \ and allele sequences are not\n    independently verified.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:9606\n  limitations: Not fully genotyped null clones; residual\
    \ RPP14 mRNA is about35%. Figure caption and Methods\n    disagree on biological\
    \ replicate counts; Methods permits at least1 biological x4 technical for these\n\
    \    KO assays. Steady-state and junction signals are not direct turnover or RNA-decay\
    \ rates.\n  nodes:\n  - node_id: rpp14-targeting\n    label: Target RPP14 with\
    \ pAVA3507 Cas9/sgRNA\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:O95059\n\
    \  - node_id: h1-rna\n    label: Steady-state H1 RNA signal\n    node_type: STATE\n\
    \  - node_id: mrp-rna\n    label: Steady-state MRP RNA signal\n    node_type:\
    \ STATE\n  - node_id: malat1-junction\n    label: Unprocessed MALAT1-mascRNA junction\
    \ signal\n    node_type: STATE\n  - node_id: menbeta-junction\n    label: Unprocessed\
    \ MEN-beta-menRNA junction signal\n    node_type: STATE\n  - node_id: its1-site2\n\
    \    label: Unprocessed pre-rRNA ITS1 site2 signal\n    node_type: STATE\n  edges:\n\
    \  - edge_id: rpp14-targeting-decreases-h1-rna\n    subject: rpp14-targeting\n\
    \    predicate: decreases\n    object: h1-rna\n    mechanism: The paper reports9.1-fold\
    \ lower H1 RNA. This does not distinguish RNA synthesis, processing\n      or\
    \ stability intermediates.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:42277007\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13408128/\n      snippet:\
    \ Gene rescue\n      explanation: Figure2c; supplement2a target engagement.\n\
    \      cache_path: evidence/PF01900/human-2026.txt\n      cache_sha256: 4cf799887d0f8f998bb4f261d08f4f5998c12aff9e4e512680424f3e37d118eb\n\
    \  - edge_id: rpp14-targeting-decreases-mrp-rna\n    subject: rpp14-targeting\n\
    \    predicate: decreases\n    object: mrp-rna\n    mechanism: The reported4.5-fold\
    \ reduction is a cell-level dependency, not a measured decay constant\n      or\
    \ direct Pop5/Rpp14 stabilization mechanism.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:42277007\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13408128/\n      snippet:\
    \ Gene rescue\n      explanation: Figure2o and Methods.\n      cache_path: evidence/PF01900/human-2026.txt\n\
    \      cache_sha256: 4cf799887d0f8f998bb4f261d08f4f5998c12aff9e4e512680424f3e37d118eb\n\
    \  - edge_id: rpp14-targeting-increases-malat1-junction\n    subject: rpp14-targeting\n\
    \    predicate: increases\n    object: malat1-junction\n    mechanism: RPP14 targeting\
    \ increases RNA spanning the RNase P cleavage site. The endpoint is precursor\n\
    \      accumulation, not a direct enzymatic velocity.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:42277007\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13408128/\n\
    \      snippet: Gene rescue\n      explanation: Figure2d,nestedRT-qPCR Methods.\n\
    \      cache_path: evidence/PF01900/human-2026.txt\n      cache_sha256: 4cf799887d0f8f998bb4f261d08f4f5998c12aff9e4e512680424f3e37d118eb\n\
    \  - edge_id: rpp14-targeting-increases-menbeta-junction\n    subject: rpp14-targeting\n\
    \    predicate: increases\n    object: menbeta-junction\n    mechanism: The cleavage-junction\
    \ signal increases relative to negative controls, within the targeted\n      cell\
    \ population.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:42277007\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC13408128/\n      snippet: Gene rescue\n\
    \      explanation: Figure2e,nestedRT-qPCR Methods.\n      cache_path: evidence/PF01900/human-2026.txt\n\
    \      cache_sha256: 4cf799887d0f8f998bb4f261d08f4f5998c12aff9e4e512680424f3e37d118eb\n\
    \  - edge_id: rpp14-targeting-increases-its1-site2\n    subject: rpp14-targeting\n\
    \    predicate: increases\n    object: its1-site2\n    mechanism: The uncleaved-site\
    \ qPCR signal is elevated; the data do not resolve a direct Rpp14 cleavage\n \
    \     reaction.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:42277007\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC13408128/\n      snippet: Gene rescue\n\
    \      explanation: Figure2s and endogenous-substrate Methods.\n      cache_path:\
    \ evidence/PF01900/human-2026.txt\n      cache_sha256: 4cf799887d0f8f998bb4f261d08f4f5998c12aff9e4e512680424f3e37d118eb\n\
    - graph_id: human-pop5-cas9-catalytic-rnas\n  title: POP5 targeting lowers H1\
    \ and MRP RNA levels\n  scope: Panah2026 SupplementFigure2d/e; POP5-targeted HeLa\
    \ Mirror populations.\n  context: HeLa Mirror reporter populations,lentiviralCas9/sgRNA,72h\
    \ then4days blasticidin,FACS sorting,3h\n    before total-RNA extraction;37 C\
    \ DMEM10%FBS,RT-qPCR delta-deltaCt.28S rRNA normalization.\n  family_mapping:\
    \ Human POP5 reference Q969H6 equals NP_057002.2,163 aa,sequence version1,PF01900\
    \ 7-115.\n    POP5 and RPP14 are distinct members; exact experimental insert or\
    \ edited alleles are not independently\n    sequenced.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:9606\n  limitations: Supplement reports at least1 biological\
    \ x4 technical replicate. The exact edited alleles\n    and protein depletion\
    \ are not established here. These are steady-state signals, not RNA half-lives\n\
    \    or family-wide catalytic effects.\n  nodes:\n  - node_id: pop5-targeting\n\
    \    label: Target POP5 with pAVA3498 Cas9/sgRNA\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q969H6\n  - node_id: h1-rna\n    label: 28S-normalized\
    \ H1 RNA signal\n    node_type: STATE\n  - node_id: mrp-rna\n    label: 28S-normalized\
    \ MRP RNA signal\n    node_type: STATE\n  edges:\n  - edge_id: pop5-targeting-decreases-h1-rna\n\
    \    subject: pop5-targeting\n    predicate: decreases\n    object: h1-rna\n \
    \   mechanism: POP5-targeted cells have lower signal than the displayed controls.\
    \ No molecular stabilization\n      intermediate was experimentally resolved.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:42277007\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13408128/\n\
    \      snippet: Gene rescue\n      explanation: Visually inspected SupplementFigure2d;\
    \ Data2 specifies the POP5 guide.\n      cache_path: evidence/PF01900/human-2026.txt\n\
    \      cache_sha256: 4cf799887d0f8f998bb4f261d08f4f5998c12aff9e4e512680424f3e37d118eb\n\
    \  - edge_id: pop5-targeting-decreases-mrp-rna\n    subject: pop5-targeting\n\
    \    predicate: decreases\n    object: mrp-rna\n    mechanism: POP5 targeting\
    \ lowers MRP RNA signal in the same population-level assay. This does not\n  \
    \    imply a direct RNA-degradation pathway.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:42277007\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13408128/\n      snippet:\
    \ Gene rescue\n      explanation: Visually inspected SupplementFigure2e and its\
    \ replicate/normalization caption.\n      cache_path: evidence/PF01900/human-2026.txt\n\
    \      cache_sha256: 4cf799887d0f8f998bb4f261d08f4f5998c12aff9e4e512680424f3e37d118eb\n\
    - graph_id: human-rpp14-rescue-trnau1ap\n  title: RPP14 cDNA suppresses RNA defects\
    \ after TRNAU1AP targeting\n  scope: Panah2026 Figure2j-l/r; TRNAU1AP-targeted\
    \ HeLa Mirror population.\n  context: Sorted cells at30%confluence,10h before3ug\
    \ pAVA3915/GenScriptOHu15516D intronlessRPP14 transfection,media24h,TRIlysis48h;\n\
    \    vectorpAVA1221 comparator,18S-normalizedRT-qPCR.\n  family_mapping: Human\
    \ RPP14 reference O95059 equals NP_008973.1,124 aa,sequence version3,PF01900 35-108.\n\
    \    This is gene-to-family mapping; exact experimental cDNA, tag termini and\
    \ allele sequences are not\n    independently verified.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:9606\n  limitations: Suppression of an upstream-knockout background,\
    \ not direct RPP14-knockout complementation.\n    Exact RPP14 transgene sequence/tag\
    \ unverified. Two biological xatleast3technical replicates; caption/Methods\n\
    \    differ on statistical test. These panels do not establish pre-tRNA or pre-rRNA\
    \ rescue.\n  nodes:\n  - node_id: rpp14-cdna\n    label: Express intronless RPP14\
    \ in the TRNAU1AP-targeted population\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:O95059\n  - node_id: h1-rna\n    label: H1 RNA steady-state signal\n\
    \    node_type: STATE\n  - node_id: mrp-rna\n    label: MRP RNA steady-state signal\n\
    \    node_type: STATE\n  - node_id: malat1-junction\n    label: Unprocessed MALAT1-mascRNA\
    \ junction signal\n    node_type: STATE\n  - node_id: menbeta-junction\n    label:\
    \ Unprocessed MEN-beta-menRNA junction signal\n    node_type: STATE\n  edges:\n\
    \  - edge_id: rpp14-cdna-increases-h1-rna\n    subject: rpp14-cdna\n    predicate:\
    \ increases\n    object: h1-rna\n    mechanism: RPP14 cDNA raises H1 RNA toward\
    \ the control level in this background. This supports conditional\n      suppression,\
    \ not direct measurement of RNA stabilization.\n    directness: INDIRECT\n   \
    \ support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:42277007\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13408128/\n\
    \      snippet: Gene rescue\n      explanation: Figure2j and rescue Methods.\n\
    \      cache_path: evidence/PF01900/human-2026.txt\n      cache_sha256: 4cf799887d0f8f998bb4f261d08f4f5998c12aff9e4e512680424f3e37d118eb\n\
    \  - edge_id: rpp14-cdna-increases-mrp-rna\n    subject: rpp14-cdna\n    predicate:\
    \ increases\n    object: mrp-rna\n    mechanism: RPP14 cDNA raises MRP RNA toward\
    \ controls; the upstream perturbation remains. Do not infer\n      that all effects\
    \ of TRNAU1AP are RPP14-dependent.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:42277007\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13408128/\n      snippet:\
    \ Gene rescue\n      explanation: Figure2r and rescue Methods.\n      cache_path:\
    \ evidence/PF01900/human-2026.txt\n      cache_sha256: 4cf799887d0f8f998bb4f261d08f4f5998c12aff9e4e512680424f3e37d118eb\n\
    \  - edge_id: rpp14-cdna-decreases-malat1-junction\n    subject: rpp14-cdna\n\
    \    predicate: decreases\n    object: malat1-junction\n    mechanism: The RPP14-expressing\
    \ population has lower unprocessed-junction signal than its vector comparison.\n\
    \      No serial molecular pathway is directly tracked.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:42277007\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13408128/\n\
    \      snippet: Gene rescue\n      explanation: Figure2k and Supplement2b.\n \
    \     cache_path: evidence/PF01900/human-2026.txt\n      cache_sha256: 4cf799887d0f8f998bb4f261d08f4f5998c12aff9e4e512680424f3e37d118eb\n\
    \  - edge_id: rpp14-cdna-decreases-menbeta-junction\n    subject: rpp14-cdna\n\
    \    predicate: decreases\n    object: menbeta-junction\n    mechanism: The unprocessed\
    \ MEN-beta-menRNA signal falls after RPP14 expression in this specific upstream\n\
    \      background.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:42277007\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC13408128/\n      snippet: Gene rescue\n\
    \      explanation: Figure2l and Supplement2b.\n      cache_path: evidence/PF01900/human-2026.txt\n\
    \      cache_sha256: 4cf799887d0f8f998bb4f261d08f4f5998c12aff9e4e512680424f3e37d118eb\n\
    - graph_id: human-rpp14-rescue-prpf39\n  title: RPP14 cDNA suppresses RNA defects\
    \ after PRPF39 targeting\n  scope: Panah2026 Figure2j-l/r; PRPF39-targeted HeLa\
    \ Mirror population.\n  context: Sorted cells at30%confluence,10h before3ug pAVA3915/GenScriptOHu15516D\
    \ intronlessRPP14 transfection,media24h,TRIlysis48h;\n    vectorpAVA1221 comparator,18S-normalizedRT-qPCR.\n\
    \  family_mapping: Human RPP14 reference O95059 equals NP_008973.1,124 aa,sequence\
    \ version3,PF01900 35-108.\n    This is gene-to-family mapping; exact experimental\
    \ cDNA, tag termini and allele sequences are not\n    independently verified.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:9606\n  limitations: Suppression\
    \ of an upstream-knockout background, not direct RPP14-knockout complementation.\n\
    \    Exact RPP14 transgene sequence/tag unverified. Two biological xatleast3technical\
    \ replicates; caption/Methods\n    differ on statistical test. These panels do\
    \ not establish pre-tRNA or pre-rRNA rescue.\n  nodes:\n  - node_id: rpp14-cdna\n\
    \    label: Express intronless RPP14 in the PRPF39-targeted population\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:O95059\n  - node_id: h1-rna\n\
    \    label: H1 RNA steady-state signal\n    node_type: STATE\n  - node_id: mrp-rna\n\
    \    label: MRP RNA steady-state signal\n    node_type: STATE\n  - node_id: malat1-junction\n\
    \    label: Unprocessed MALAT1-mascRNA junction signal\n    node_type: STATE\n\
    \  - node_id: menbeta-junction\n    label: Unprocessed MEN-beta-menRNA junction\
    \ signal\n    node_type: STATE\n  edges:\n  - edge_id: rpp14-cdna-increases-h1-rna\n\
    \    subject: rpp14-cdna\n    predicate: increases\n    object: h1-rna\n    mechanism:\
    \ RPP14 cDNA raises H1 RNA toward the control level in this background. This supports\
    \ conditional\n      suppression, not direct measurement of RNA stabilization.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:42277007\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13408128/\n\
    \      snippet: Gene rescue\n      explanation: Figure2j and rescue Methods.\n\
    \      cache_path: evidence/PF01900/human-2026.txt\n      cache_sha256: 4cf799887d0f8f998bb4f261d08f4f5998c12aff9e4e512680424f3e37d118eb\n\
    \  - edge_id: rpp14-cdna-increases-mrp-rna\n    subject: rpp14-cdna\n    predicate:\
    \ increases\n    object: mrp-rna\n    mechanism: RPP14 cDNA raises MRP RNA toward\
    \ controls; the upstream perturbation remains. Do not infer\n      that all effects\
    \ of PRPF39 are RPP14-dependent.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:42277007\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13408128/\n      snippet:\
    \ Gene rescue\n      explanation: Figure2r and rescue Methods.\n      cache_path:\
    \ evidence/PF01900/human-2026.txt\n      cache_sha256: 4cf799887d0f8f998bb4f261d08f4f5998c12aff9e4e512680424f3e37d118eb\n\
    \  - edge_id: rpp14-cdna-decreases-malat1-junction\n    subject: rpp14-cdna\n\
    \    predicate: decreases\n    object: malat1-junction\n    mechanism: The RPP14-expressing\
    \ population has lower unprocessed-junction signal than its vector comparison.\n\
    \      No serial molecular pathway is directly tracked.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:42277007\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13408128/\n\
    \      snippet: Gene rescue\n      explanation: Figure2k and Supplement2b.\n \
    \     cache_path: evidence/PF01900/human-2026.txt\n      cache_sha256: 4cf799887d0f8f998bb4f261d08f4f5998c12aff9e4e512680424f3e37d118eb\n\
    \  - edge_id: rpp14-cdna-decreases-menbeta-junction\n    subject: rpp14-cdna\n\
    \    predicate: decreases\n    object: menbeta-junction\n    mechanism: The unprocessed\
    \ MEN-beta-menRNA signal falls after RPP14 expression in this specific upstream\n\
    \      background.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:42277007\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC13408128/\n      snippet: Gene rescue\n\
    \      explanation: Figure2l and Supplement2b.\n      cache_path: evidence/PF01900/human-2026.txt\n\
    \      cache_sha256: 4cf799887d0f8f998bb4f261d08f4f5998c12aff9e4e512680424f3e37d118eb\n\
    curation_events:\n- timestamp: '2026-10-11T21:58:50Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate scoped Pop5 and Rpp14 causal assays\
    \ for former DUF69\n  history_record: history/records/PF01900/2026-10-11T215850Z-codex-2868bb.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: 'FrozenPF01900 is formerDUF69,notPF01899/DUF68. Six UniProt sequences exactly
    match versioned NCBI references: O26783/AAB85192.1,MTH_687,124aa,domain13-116;
    Q57917/AAB98484.1,MJ0494,134aa,17-111; Q8U151/AAL81502.1,PF1378,120aa,17-113;
    O59150/BAA30588.1,PH1481,120aa,17-113; humanO95059/NP_008973.1,124aa,35-108; humanQ969H6/NP_057002.2,163aa,7-115.
    Current reference matches do not sequence each assay vial or human transgene.
    Pop5 and Rpp14 remain distinct members, and Rpp30R107A is not transferred. Delta14C
    overlaps only107-113 ofPfam.'
  target_ids:
  - PF01900
  evidence_ids:
  - identity
  - primary
  - archaeal-reconstitution
  - archaeal-fidelity
  - pho-binding-dose
  - human-biochemistry
  - evidence-gaps
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Each edge has the tested conjunction and measured direction, with unique
    local IDs and hash-anchored evidence. Mth/Mja/Pfu comparisons retain changed buffers,doses
    and times; correct-site fractions are not conversion or rates. ApparentSPRaffinity
    is not full-RNAactivation or molecular stoichiometry. F14HEK293 andF39HeLa fractions
    remain separate. Figure4C does not support increased40minMono fromPop5. Mg-free95%-pure
    preparations remain unresolved in catalytic attribution; Rpp14 omission retains
    H1-complex cleavage. Myc-Rpp14 sedimentation is ex-vivo,not observed intracellular
    aggregation. RPP14shRNAprotein depletion was not established. Cas9 populations
    are not sequenced null clones and retain RPP14mRNA; upstream-background suppression
    is not RPP14null complementation. RNA amount nodes are STATE,not catalytic activity
    labels. Shared PF01876 assay evidence is not independent replication.
  target_ids:
  - PF01900
  evidence_ids:
  - primary
  - native
  - archaeal-reconstitution
  - archaeal-fidelity
  - pho-binding-dose
  - human-biochemistry
  - evidence-gaps
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: The5287 frozen proteins are not exhaustively characterized. Full original
    2006loop-deletion and2013helix/FRETmethods/figures,2015mutantSPRcurves, exacthumanclone
    sequences/doses,2008MjacisTyr,2011assembly,2012annealing, yeast/otherarchaealcontexts,1999/2002humanbiochemistry,2024telomere
    and metazoanMRP evidence remain follow-ups. Abstracts,structures and association
    networks are not promoted to observed causal edges.
  target_ids:
  - PF01900
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01900-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Complete missing construct, catalytic-attribution and homolog evidence
  description: Obtain exact human assay/transgene constructs and matched preparation
    controls; reconcile the2023gradient and2026replicate/statistical discrepancies;
    inspect original2006/2013mutational studies and2015SPRcurves. Assess additional
    member-specific primary assays before extending graphs. Preserve residual activity,
    partner/buffer conjunctions, endpoint-specific rescue and negative controls. Add
    a successor review and canonical history without changing historical reports or
    promoting the family to REVIEWED on structural checks.
  target_ids:
  - PF01900
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - archaeal-reconstitution
  - archaeal-fidelity
  - pho-binding-dose
  - human-biochemistry
  - evidence-gaps
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01900.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Obtain exact human assay/transgene constructs and matched preparation
    controls; reconcile the2023gradient and2026replicate/statistical discrepancies;
    inspect original2006/2013mutational studies and2015SPRcurves. Assess additional
    member-specific primary assays before extending graphs. Preserve residual activity,
    partner/buffer conjunctions, endpoint-specific rescue and negative controls. Add
    a successor review and canonical history without changing historical reports or
    promoting the family to REVIEWED on structural checks.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01900
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Original2010Figures3/4/7 and supplementTableS2,2012Figures1/2, 2015Figures2/5,2023Figures3-7
  and supplementS2,2026Figure2 and supplement2 were visually inspected. Primary text/tables
  and supplementary methods were read within the retained scope. No raw gel reanalysis,genotype
  sequencing, independent replication or exhaustive primary-literature search is claimed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
