# PF01876 Rpp30 reconstitution mutation and yeast causal contexts

- Review: 20261011T191036Z-pf01876-rpp30-reconstitution-mutation-and-yeast-contexts
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T19:10:26Z
- Finished UTC: 2026-10-11T19:10:36Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Fifteen graphs retain twenty-four observed effects across five mapped reference proteins and four primary studies. Fifteen direct preparation or mutation readouts and nine indirect yeast phenotypes remain separate. Optimized protocols, mixed RNP preparations, residual mutant activity and source discrepancies constrain molecular attribution. Retain IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Stolc1997 Methods, Results, Tables1/2 and original Figures1/2/4/5/6/7; Chen2010 Methods, Table1, original Figures3/4/7 and public supplementary Methods, primers, TableS2 and kinetic controls; Chen2012 Methods, Table2 and original Figures1/2; Hamasaki2015/2016 Methods, TablesI/II and original Figures2/5. Current member-specific InterPro and UniProt records and versioned protein sequence comparisons establish mapping. Earlier2008/2011 Methods were inspected for protocol context, not new causal edges.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01876 | data/families/PF01876.yaml | generated | PF01876 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01876 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01876.

Versioned reference sequences exactly match yeast P38786/AAB96559.1/NP_011929.1, Mth O26784/AAB85193.1, Mja Q58539/WP_010870650.1, Pfu Q8TZS0/WP_011013054.1 and Pho O59543/WP_010885939.1. PF01876 intervals are respectively1-241,10-232,7-212,59-211 and50-209. Pho R107 is inside the match. JN161-derived yeast assay strains are not silently called reference S288c. Exact assay-batch sequences and some earlier construct tags remain unverified; full proteins and RNA-containing complexes are not isolated domains.

### Directed effects and limits

graph: supported. Targets: PF01876.

Fifteen direct effects retain Mth optimized maximal kobs, Mja full and truncated RNA reconstitution, Pfu product fidelity, Mja cis rate and fidelity, Pho SPR, R107A kinetics and joint-pair titration, and two yeast immunoprecipitate processing assays. Nine indirect effects retain yeast disruption and complementation, promoter-repression growth, pre-tRNA intermediates, RPR1/NME1 abundance and rRNA patterns. Composite buffer/time/dose interventions remain explicit. FC0 is not yield, KM is not binding KD, the61% all-four amplitude is not complete conversion, and no direct p30 cleavage chemistry, RNA half-life, cellular stoichiometry or family-wide mechanism is asserted.

### Remaining family coverage

completeness: concern. Targets: PF01876.

Resolve exact constructs, kinetic temperature/volume, earlier-method mixing and reference inconsistencies, IP150/IP600 and printed BSA discrepancies, Pho fit arithmetic and the K196A specificity cell. Inspect missing Pho supplementary controls and additional archaeal, plant, animal and human functional studies. All4590 frozen proteins remain in scope; these five mapped references do not exhaust family functions or establish domain-only sufficiency.

## Findings

### additional-contexts: Resolve Rpp30 assay provenance and extend member-specific causal coverage

minor / open / confirmed; issue key: pf01876-causal-context-coverage.

Recover unresolved construct and protocol details and the inaccessible Pho supplements, seek matched-buffer and mutant folding or assembly controls, and assess additional member-specific studies with exact accession/domain mapping. Keep protein-pair effects, whole-gene phenotypes, mixed RNP activity and inferred molecular intermediates distinct. Preserve condition-specific negatives and source disagreements rather than adopting a universal p30 catalytic pathway.

## Recommended Actions And Acceptance Checks

### extend-contexts

Recover unresolved construct and protocol details and the inaccessible Pho supplements, seek matched-buffer and mutant folding or assembly controls, and assess additional member-specific studies with exact accession/domain mapping. Keep protein-pair effects, whole-gene phenotypes, mixed RNP activity and inferred molecular intermediates distinct. Preserve condition-specific negatives and source disagreements rather than adopting a universal p30 catalytic pathway.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC4882637/; Main Methods and Discussion, TablesI/II, original Figures2/5; SupplementS3 not inspected | supports | The Pho POP5-RPP30 preparation has a lower fitted Ta-SL3 KD than POP5 under SPR conditions, R107A lowers reported reconstituted-complex kcat with residual activity, and jointly increasing pair dose raises cleavage fraction before a partial plateau. Distinct fitting models, uncertain kinetic conditions and missing folding or assembly controls prevent an isolated p30 catalytic or chaperone trajectory claim. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01876/protein/uniprot/O59543/; Accession and domain locations; paired UniProt identity facts | supports | Versioned reference sequences exactly match yeast P38786/AAB96559.1/NP_011929.1, Mth O26784/AAB85193.1, Mja Q58539/WP_010870650.1, Pfu Q8TZS0/WP_011013054.1 and Pho O59543/WP_010885939.1. PF01876 intervals are respectively1-241,10-232,7-212,59-211 and50-209. Pho R107 is inside the match. JN161-derived yeast assay strains are not silently called reference S288c. Exact assay-batch sequences and some earlier construct tags remain unverified; full proteins and RNA-containing complexes are not isolated domains. |
| yeast-processing | https://pmc.ncbi.nlm.nih.gov/articles/PMC316654/; Methods, Tables1/2 and original Figures1/2/4/5/6/7 | supports | Whole-gene disruption reduces outgrowth and full tagged Rpp1 complements it. Conditional repression changes growth, pre-tRNA intermediates, mature RPR1/NME1 and rRNA patterns. Tagged immunoprecipitates process pre-tRNASer and ITS141 but contain mixed RNaseP/MRP components. Steady-state signals are not half-lives, and wash-salt/BSA details remain unresolved. |
| reconstitution | https://pmc.ncbi.nlm.nih.gov/articles/PMC3001054/; Main Table1, original Figures3/4/7; Chen_et_al_080210_Rev_Supp.pdf Methods pp2-8, primers p13, TableS2 p14 and kinetic controls pp20-23 | supports | The Mth pair-containing optimized protocol increases fitted maximal kobs; Mja RNA and pair preparations produce products with full and truncated RNAs. Salt and magnesium differ from RNA-only controls. Tag-free cloning and full-protein mapping constrain scope; ES-star stabilization remains proposed and KM(STO) is not generally a binding dissociation constant. |
| fidelity | https://pmc.ncbi.nlm.nih.gov/articles/PMC3378863/; Main Methods, Table2 and original Figures1/2; earlier2008/2011 Methods for protocol discrepancies | supports | Pfu optimized protein-containing protocols increase FC0 for a nonconsensus substrate. Mja cis Gln protocols increase fitted kobs and FC0, but the pair still produces majority miscleavage and all-four product amplitude is only61%. RNA dose, time, salts, assembly phases and a misnumbered earlier-method reference prevent a matched protein-only comparison or microscopic rate attribution. |
| gaps-and-access | evidence/PF01876/rpp30-gap-ledger.txt; Bounded member/source searches, protocol conflicts, supplementary access limits and unreviewed contexts | supports | Retain partial member coverage, unresolved preparation details, paired interventions, RNA-versus-protein catalytic attribution, source arithmetic and mixed-protocol discrepancies. Access failures do not imply missing biological function. Additional structural, plant, animal and human leads remain unreviewed, not negative findings. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01876 | data/families/PF01876.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Original Stolc Figures1/2/4/5/6/7, Chen2010 Figures3/4/7, Chen2012 Figures1/2 and Hamasaki Figures2/5 were visually inspected. Chen2010 public supplementary PDF Methods, primers, TableS2 and kinetic controls were read; earlier kinetic control images were inspected in the linked Rpp29 work. Pho supplemental retrieval returned XML or download-preparation HTML and the publisher returned403; SupplementS3 was not inspected. No raw-data refit, assay-batch sequencing, exhaustive literature coverage or experimental replication. Rendered-page checks follow separately.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T191036Z-pf01876-rpp30-reconstitution-mutation-and-yeast-contexts
title: PF01876 Rpp30 reconstitution mutation and yeast causal contexts
started_at: '2026-10-11T19:10:26Z'
finished_at: '2026-10-11T19:10:36Z'
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
summary: Fifteen graphs retain twenty-four observed effects across five mapped reference
  proteins and four primary studies. Fifteen direct preparation or mutation readouts
  and nine indirect yeast phenotypes remain separate. Optimized protocols, mixed RNP
  preparations, residual mutant activity and source discrepancies constrain molecular
  attribution. Retain IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01876.yaml
    sha256: 22b5be40ce8680236c27c99455d336b2bf984c0f459477223f9d9551fd6da1cf
    role: context
  - path: data/families/PF01876.yaml
    sha256: 9fb1cfee4596b6abde66d6964576fbba113788ad17bcf07239ed2e72cfe86b32
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
  - path: evidence/PF01876/hamasaki-2015-p30.txt
    role: context
    sha256: 4fc37bc3c0bc02e5aa74e51d6c189f0ef21a23b955f9a52fe7df6ae1a2061df9
  - path: evidence/PF01876/rpp30-identity.txt
    role: context
    sha256: 8f66ff28f44cdff51917c1600b04a71582d09ce8827083422bd41c6790d64725
  - path: evidence/PF01876/stolc-1997-yeast.txt
    role: context
    sha256: dc04c2148820b58c1336b437b5d67a25e99be059993c7b32eea209d78645b6ba
  - path: evidence/PF01876/chen-2010-reconstitution.txt
    role: context
    sha256: 6d5205a18821029b23b745b445c8819bfe9b28fc050995cc6bbf2a85588432d4
  - path: evidence/PF01876/chen-2012-fidelity.txt
    role: context
    sha256: c68f4c212e38991b9b58de6054a6efbded483d35baec71a2c767d96c7bc5384a
  - path: evidence/PF01876/rpp30-gap-ledger.txt
    role: context
    sha256: f69d0eb85d7a15eeb31749cf9a7cc4833a0fbbe4db150d384e3400c359f06c38
targets:
- target_id: PF01876
  path: data/families/PF01876.yaml
  label: PF01876
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01876.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: b53294702dccc2d568bbec81962dc9babbfe59bf8bbc4d97d743b8bddcc1d235
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Stolc1997 Methods, Results, Tables1/2 and original Figures1/2/4/5/6/7;
    Chen2010 Methods, Table1, original Figures3/4/7 and public supplementary Methods,
    primers, TableS2 and kinetic controls; Chen2012 Methods, Table2 and original Figures1/2;
    Hamasaki2015/2016 Methods, TablesI/II and original Figures2/5. Current member-specific
    InterPro and UniProt records and versioned protein sequence comparisons establish
    mapping. Earlier2008/2011 Methods were inspected for protocol context, not new
    causal edges.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01876
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Resolve exact constructs, kinetic temperature/volume, earlier-method mixing
      and reference inconsistencies, IP150/IP600 and printed BSA discrepancies, Pho
      fit arithmetic and the K196A specificity cell. Inspect missing Pho supplementary
      controls and additional archaeal, plant, animal and human functional studies.
      All4590 frozen proteins remain in scope; these five mapped references do not
      exhaust family functions or establish domain-only sufficiency.
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
  - PF01876
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4882637/
  locator: Main Methods and Discussion, TablesI/II, original Figures2/5; SupplementS3
    not inspected
  accessed_at: '2026-10-11T19:10:36Z'
  support: supports
  snapshot_sha256: 4fc37bc3c0bc02e5aa74e51d6c189f0ef21a23b955f9a52fe7df6ae1a2061df9
  summary: The Pho POP5-RPP30 preparation has a lower fitted Ta-SL3 KD than POP5 under
    SPR conditions, R107A lowers reported reconstituted-complex kcat with residual
    activity, and jointly increasing pair dose raises cleavage fraction before a partial
    plateau. Distinct fitting models, uncertain kinetic conditions and missing folding
    or assembly controls prevent an isolated p30 catalytic or chaperone trajectory
    claim.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01876/protein/uniprot/O59543/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T19:10:36Z'
  support: supports
  snapshot_sha256: 8f66ff28f44cdff51917c1600b04a71582d09ce8827083422bd41c6790d64725
  summary: Versioned reference sequences exactly match yeast P38786/AAB96559.1/NP_011929.1,
    Mth O26784/AAB85193.1, Mja Q58539/WP_010870650.1, Pfu Q8TZS0/WP_011013054.1 and
    Pho O59543/WP_010885939.1. PF01876 intervals are respectively1-241,10-232,7-212,59-211
    and50-209. Pho R107 is inside the match. JN161-derived yeast assay strains are
    not silently called reference S288c. Exact assay-batch sequences and some earlier
    construct tags remain unverified; full proteins and RNA-containing complexes are
    not isolated domains.
- evidence_id: yeast-processing
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC316654/
  locator: Methods, Tables1/2 and original Figures1/2/4/5/6/7
  summary: Whole-gene disruption reduces outgrowth and full tagged Rpp1 complements
    it. Conditional repression changes growth, pre-tRNA intermediates, mature RPR1/NME1
    and rRNA patterns. Tagged immunoprecipitates process pre-tRNASer and ITS141 but
    contain mixed RNaseP/MRP components. Steady-state signals are not half-lives,
    and wash-salt/BSA details remain unresolved.
  accessed_at: '2026-10-11T19:10:36Z'
  support: supports
  snapshot_sha256: dc04c2148820b58c1336b437b5d67a25e99be059993c7b32eea209d78645b6ba
- evidence_id: reconstitution
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3001054/
  locator: Main Table1, original Figures3/4/7; Chen_et_al_080210_Rev_Supp.pdf Methods
    pp2-8, primers p13, TableS2 p14 and kinetic controls pp20-23
  summary: The Mth pair-containing optimized protocol increases fitted maximal kobs;
    Mja RNA and pair preparations produce products with full and truncated RNAs. Salt
    and magnesium differ from RNA-only controls. Tag-free cloning and full-protein
    mapping constrain scope; ES-star stabilization remains proposed and KM(STO) is
    not generally a binding dissociation constant.
  accessed_at: '2026-10-11T19:10:36Z'
  support: supports
  snapshot_sha256: 6d5205a18821029b23b745b445c8819bfe9b28fc050995cc6bbf2a85588432d4
- evidence_id: fidelity
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3378863/
  locator: Main Methods, Table2 and original Figures1/2; earlier2008/2011 Methods
    for protocol discrepancies
  summary: Pfu optimized protein-containing protocols increase FC0 for a nonconsensus
    substrate. Mja cis Gln protocols increase fitted kobs and FC0, but the pair still
    produces majority miscleavage and all-four product amplitude is only61%. RNA dose,
    time, salts, assembly phases and a misnumbered earlier-method reference prevent
    a matched protein-only comparison or microscopic rate attribution.
  accessed_at: '2026-10-11T19:10:36Z'
  support: supports
  snapshot_sha256: c68f4c212e38991b9b58de6054a6efbded483d35baec71a2c767d96c7bc5384a
- evidence_id: gaps-and-access
  kind: search
  reference: evidence/PF01876/rpp30-gap-ledger.txt
  locator: Bounded member/source searches, protocol conflicts, supplementary access
    limits and unreviewed contexts
  search_scope: PF01876, RNase_P_p30, Rpp30, Rpp1, Pop5 and verified archaeal/yeast
    members; ignored/hidden-inclusive curation,evidence,history/records,reviews/structured,.agents,.claude
    search on2026-10-11 found related Rpp29 evidence but no earlier PF01876-specific
    overlay. Primary article and supplemental retrieval, current reference/domain
    APIs and versioned sequence comparisons; not an exhaustive family literature search.
  summary: Retain partial member coverage, unresolved preparation details, paired
    interventions, RNA-versus-protein catalytic attribution, source arithmetic and
    mixed-protocol discrepancies. Access failures do not imply missing biological
    function. Additional structural, plant, animal and human leads remain unreviewed,
    not negative findings.
  accessed_at: '2026-10-11T19:10:36Z'
  support: supports
  snapshot_sha256: f69d0eb85d7a15eeb31749cf9a7cc4833a0fbbe4db150d384e3400c359f06c38
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T19:10:36Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01876
  kind: record_content
  reference: data/families/PF01876.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T19:10:36Z'
  support: context_only
  snapshot_sha256: 9fb1cfee4596b6abde66d6964576fbba113788ad17bcf07239ed2e72cfe86b32
  quote: "id: Pfam:PF01876\npfam_id: PF01876\nname: RNase P subunit p30\nshort_name:\
    \ RNase_P_p30\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01876\n\
    counters:\n  proteins: 4590\n  matches: 4644\n  proteomes: 3743\n  taxa: 9545\n\
    \  structures: 16\n  alphafold_models: 3969\n  domain_architectures: 62\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002738\ndescription: This protein is part of the RNase\
    \ P complex that is involved in tRNA maturation [[cite:PUB00020266]].\ncuration_history:\
    \ history/records/PF01876\ndiscussions:\n- discussion_id: p30-molecular-attribution\n\
    \  prompt: Resolve how p30 contributes to catalytic RNA assembly and activity.\n\
    \  kind: CURATION_TODO\n  status: OPEN\n  rationale: Pair effects,optimized buffers\
    \ and mixed RNP preparations do not isolate a p30 molecular\n    step. R107A has\
    \ residual activity and unverified folding/assembly controls.\n  evidence:\n \
    \ - reference: PMID:20705647\n    supports: PARTIAL\n    evidence_source: primary_kinetics_and_supplement\n\
    \    explanation: ES-to-ES-star stabilization is a mechanistic proposal,not an\
    \ observed transition.\n  - reference: PMID:26152732\n    supports: PARTIAL\n\
    \    evidence_source: primary_methods_tables_and_figures\n    explanation: Affinity\
    \ fits,mutation kinetics and activity titration support assay effects,not a uniquely\n\
    \      proven chaperone trajectory or cellular dimer.\n  notes: Obtain orthogonal\
    \ folding,assembly,active-fraction and matched-buffer controls. Resolve Pho fold\n\
    \    arithmetic,K196A table cell and kinetic conditions. Inspect missing SupplementS3\
    \ and2019/2026 structural-functional\n    follow-ups.\n  posed_by: Codex\n  posed_date:\
    \ '2026-10-11'\n- discussion_id: p30-coverage-and-protocol-gaps\n  prompt: Extend\
    \ member coverage and resolve assay provenance before generalization.\n  kind:\
    \ CURATION_TODO\n  status: OPEN\n  rationale: Five reference proteins and selected\
    \ experiments do not establish a conserved mechanism across4590\n    frozen family\
    \ members.\n  evidence:\n  - reference: PMID:9353260\n    supports: PARTIAL\n\
    \    evidence_source: primary_strain_methods_and_original_figures\n    explanation:\
    \ Whole-gene yeast phenotypes and mixed immunoprecipitates cannot uniquely separate\
    \ RNaseP,RNaseMRP\n      and secondary growth effects.\n  - reference: PMID:22298511\n\
    \    supports: PARTIAL\n    evidence_source: primary_fidelity_methods_and_tables\n\
    \    explanation: Composite protocols,nominal concentrations and model-derived\
    \ quantities require careful\n      comparison.\n  notes: See evidence/PF01876/rpp30-gap-ledger.txt.\
    \ Recover exact tags,strain/clone sequences,IP150/IP600\n    and BSA units,2012\
    \ mixing/reference discrepancies,and missing supplements. Assess human,plant,fly\n\
    \    and additional archaeal contexts with exact mapping. Keep IN_PROGRESS and\
    \ partial same-agent review.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n\
    causal_graphs:\n- graph_id: mth-optimized-cleavage-rate\n  title: The POP5-RPP30\
    \ protocol increases the fitted maximal cleavage rate\n  scope: Chen2010 Table1\
    \ and Figure7, Mth RNA alone versus RNA with the cognate protein pair.\n  context:\
    \ Approximately2 nM E.coli pre-tRNATyr,55 C,pH5.8. RNA alone0.3-20 uM in2 M NH4/500\
    \ mM Mg; pair\n    condition1-10 uM RNA in0.8 M NH4/120 mM Mg,proteins twice RNA\
    \ molarity.\n  family_mapping: MTH688 O26784 equals AAB85193.1,245 aa,PF01876\
    \ 10-232. Tag-free full-protein cloning\n    and POP5 coexpression in BL21(DE3),not\
    \ an isolated p30 domain.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:187420\n\
    \  limitations: Optimized protein/buffer protocols differ. Fitted maximal kobs\
    \ is not an independently\n    isolated chemical rate constant; the proposed ES-to-ES-star\
    \ stabilization is not directly observed.\n  nodes:\n  - node_id: pair-protocol\n\
    \    label: Use the POP5-RPP30-containing optimized RNA protocol\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:O26784\n  - node_id: maximal-kobs\n\
    \    label: Fitted maximal pre-tRNA cleavage kobs\n    node_type: PROCESS\n  edges:\n\
    \  - edge_id: pair-protocol-increases-maximal-kobs\n    subject: pair-protocol\n\
    \    predicate: increases\n    object: maximal-kobs\n    mechanism: The fitted\
    \ maximum rises from0.13 +/-0.01 to7.9 +/-1 per min. The comparison includes changed\n\
    \      ions and both proteins; it does not establish Rpp30-alone catalysis. KM(STO)\
    \ is not a measured binding\n      Kd.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:20705647\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3001054/\n      snippet:\
    \ Single-turnover kinetic studies\n      explanation: Table1,original Figure7\
    \ and supplementary kinetic controls distinguish optimized protocols\n       \
    \ and fitted parameters.\n      cache_path: evidence/PF01876/chen-2010-reconstitution.txt\n\
    \      cache_sha256: 6d5205a18821029b23b745b445c8819bfe9b28fc050995cc6bbf2a85588432d4\n\
    - graph_id: mja-full-rna-reconstitution\n  title: The RNA and POP5-RPP30 preparation\
    \ produces pre-tRNA cleavage products\n  scope: Chen2010 Figure3 upper panel,\
    \ full-length Mja RPR.\n  context: 10 nM RNA,100 nM proteins,500 nM E.coli pre-tRNATyr,30\
    \ min55 C; pair buffer50 mM Tris7.5/100\n    mM NH4/120 mM Mg. RNA-alone control\
    \ uses800 mM NH4/30 mM Mg.\n  family_mapping: MJ1139 Q58539 equals WP_010870650.1,232\
    \ aa,PF01876 7-212. Tag-free full Rpp30 coexpressed\n    with POP5; catalytic\
    \ RNA is required in this preparation.\n  scope_status: MECHANISTIC\n  taxon:\
    \ NCBITaxon:243232\n  limitations: This is a composite reconstitution/ionic-condition\
    \ comparison,not a matched-buffer test\n    of Rpp30 alone. RPP21-RPP29 alone\
    \ does not activate this type-M RNA under the tested protocol.\n  nodes:\n  -\
    \ node_id: pair-rna-protocol\n    label: Reconstitute full Mja RNA with POP5-RPP30\
    \ in the pair buffer\n    node_type: PERTURBATION\n  - node_id: cleavage-products\n\
    \    label: Mature-tRNA-sized and 5-prime-leader products\n    node_type: STATE\n\
    \  edges:\n  - edge_id: reconstitution-increases-products\n    subject: pair-rna-protocol\n\
    \    predicate: increases\n    object: cleavage-products\n    mechanism: Products\
    \ appear with RNA plus the pair compared with the published RNA-only and protein-only\n\
    \      controls. This does not make either protein independently sufficient or\
    \ imply a natural cellular\n      stoichiometry.\n    directness: DIRECT\n   \
    \ support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:20705647\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3001054/\n\
    \      snippet: Single-turnover kinetic studies\n      explanation: The retained\
    \ extract also records Figure3 and the distinct multiple-turnover buffers;\n \
    \       the original lanes3-5 were inspected.\n      cache_path: evidence/PF01876/chen-2010-reconstitution.txt\n\
    \      cache_sha256: 6d5205a18821029b23b745b445c8819bfe9b28fc050995cc6bbf2a85588432d4\n\
    - graph_id: mja-truncated-rna-reconstitution\n  title: POP5-RPP30 protocols support\
    \ cleavage by two truncated catalytic RNAs\n  scope: Chen2010 Figure4B, separate\
    \ Mja deltaS and112-nt deltaS-Min transcripts.\n  context: 500 nM RNA,1 uM proteins,1\
    \ uM pre-tRNATyr,15 min55 C;50 mM Tris7.5/400 mM NH4,120 mM Mg for\n    pair versus30\
    \ mM for RNA-only control.\n  family_mapping: Full MJ1139/Q58539 Rpp30,PF01876\
    \ 7-212; deletions are in the catalytic RNA,not the p30\n    protein. POP5 is\
    \ jointly supplied.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:243232\n\
    \  limitations: Separate engineered RNAs and optimized ions; no protein-only rescue\
    \ of an isolated p30\n    domain. Further enhancement by all four proteins does\
    \ not identify the molecular intermediate.\n  nodes:\n  - node_id: deltas-pair-protocol\n\
    \    label: Use the deltaS RNA with POP5-RPP30 protocol\n    node_type: PERTURBATION\n\
    \  - node_id: deltas-min-pair-protocol\n    label: Use the112-nt deltaS-Min RNA\
    \ with POP5-RPP30 protocol\n    node_type: PERTURBATION\n  - node_id: cleavage-products\n\
    \    label: Pre-tRNATyr cleavage products in the corresponding assay\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: deltas-pair-increases-products\n    subject: deltas-pair-protocol\n\
    \    predicate: increases\n    object: cleavage-products\n    mechanism: The deltaS\
    \ preparation produces mature-tRNA-sized and leader bands compared with its published\n\
    \      RNA-only control; both protein pair and ionic conditions are part of the\
    \ intervention.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:20705647\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC3001054/\n      snippet: Single-turnover\
    \ kinetic studies\n      explanation: Original Figure4B upper panel and separate\
    \ truncated-RNA assay Methods,not the single-turnover\n        rate protocol.\n\
    \      cache_path: evidence/PF01876/chen-2010-reconstitution.txt\n      cache_sha256:\
    \ 6d5205a18821029b23b745b445c8819bfe9b28fc050995cc6bbf2a85588432d4\n  - edge_id:\
    \ deltas-min-pair-increases-products\n    subject: deltas-min-pair-protocol\n\
    \    predicate: increases\n    object: cleavage-products\n    mechanism: The112-nt\
    \ RNA also gives cleavage products with the pair protocol. This is a minimal engineered\n\
    \      RNP under high salt,not evidence that p30 supplies all catalytic groups.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:20705647\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3001054/\n\
    \      snippet: Single-turnover kinetic studies\n      explanation: Original Figure4B\
    \ lower panel and supplemental RNA-cloning Methods establish the distinct\n  \
    \      minimal transcript.\n      cache_path: evidence/PF01876/chen-2010-reconstitution.txt\n\
    \      cache_sha256: 6d5205a18821029b23b745b445c8819bfe9b28fc050995cc6bbf2a85588432d4\n\
    - graph_id: pfu-nonconsensus-fidelity\n  title: Protein-containing Pfu protocols\
    \ increase the correctly cleaved product fraction\n  scope: Chen2012 Figure1C,\
    \ nonconsensus SynechocystisPCC6803 pre-tRNAGln.\n  context: 2 nM labeled substrate,55\
    \ C. RNA alone15 uM9 h; protein-containing reactions200 nM RNA/2 uM\n    proteins,30\
    \ min with POP5-RPP30 or10 min with all four,using separately optimized buffers.\n\
    \  family_mapping: PF1914 Q8TZS0 equals WP_011013054.1,214 aa,PF01876 59-211.\
    \ Whole protein in recombinant\n    complexes; exact assay tag and batch sequence\
    \ not independently verified.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:186497\n\
    \  limitations: RNA dose,time and buffer differ. FC0 means correct/(correct+miscleaved)\
    \ product,not total\n    substrate conversion or a rate. Neither condition isolates\
    \ Rpp30 from its partner.\n  nodes:\n  - node_id: pair-protocol\n    label: Use\
    \ the RNA plus POP5-RPP30 protocol\n    node_type: PERTURBATION\n  - node_id:\
    \ four-protein-protocol\n    label: Use the RNA plus all-four-protein protocol\n\
    \    node_type: PERTURBATION\n  - node_id: correct-fraction\n    label: Correctly\
    \ cleaved fraction among products\n    node_type: STATE\n  edges:\n  - edge_id:\
    \ pair-protocol-increases-correct-fraction\n    subject: pair-protocol\n    predicate:\
    \ increases\n    object: correct-fraction\n    mechanism: FC0 rises from0.11 +/-0.03\
    \ in the RNA-only protocol to0.59 +/-0.01 with the pair protocol;\n      protocol\
    \ differences prevent a protein-only causal attribution.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:22298511\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3378863/\n\
    \      snippet: Data analysis\n      explanation: Original Figure1C lanes2/4 and\
    \ Results; preserve the actual product-ratio denominator.\n      cache_path: evidence/PF01876/chen-2012-fidelity.txt\n\
    \      cache_sha256: c68f4c212e38991b9b58de6054a6efbded483d35baec71a2c767d96c7bc5384a\n\
    \  - edge_id: four-protein-protocol-increases-correct-fraction\n    subject: four-protein-protocol\n\
    \    predicate: increases\n    object: correct-fraction\n    mechanism: The full\
    \ four-protein protocol gives FC0 0.92 +/-0.01 versus0.11 +/-0.03 for RNA alone.\n\
    \      This is not independent replication of the pair result or isolated p30\
    \ sufficiency.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:22298511\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC3378863/\n      snippet: Data analysis\n\
    \      explanation: Original Figure1C lanes2/5 and Methods retain the9-hour versus10-minute\
    \ comparison.\n      cache_path: evidence/PF01876/chen-2012-fidelity.txt\n   \
    \   cache_sha256: c68f4c212e38991b9b58de6054a6efbded483d35baec71a2c767d96c7bc5384a\n\
    - graph_id: mja-cis-cleavage-protocols\n  title: Mja protein-containing protocols\
    \ change cis cleavage rate and fidelity\n  scope: Chen2012 Figure2 and Table2,\
    \ pre-tRNAGln-AAU-Mja-RPR conjugate.\n  context: Nominal50 nM RNA/500 nM proteins,55\
    \ C,pH6. RNA-alone favors2.5 M NH4/500 mM Mg; protein conditions0.8\n    M NH4/nominal100\
    \ mM Mg. Assembly and cleavage phases differ; all-four assembly uses25 mM Ca.\n\
    \  family_mapping: MJ1139 Q58539/WP_010870650.1,PF01876 7-212,whole recombinant\
    \ protein paired with POP5\n    and optionally RPP21-RPP29. The substrate is covalently\
    \ linked to catalytic RNA.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:243232\n\
    \  limitations: Composite optimized protocols with unresolved earlier-method mixing/reference\
    \ discrepancies.\n    FC0 excludes uncleaved RNA; total amplitudes are93% RNA,96%\
    \ pair,61% all-four. Model-derived component\n    rates are not observed microscopic\
    \ steps.\n  nodes:\n  - node_id: pair-protocol\n    label: Use the cis-RNA plus\
    \ POP5-RPP30 protocol\n    node_type: PERTURBATION\n  - node_id: four-protein-protocol\n\
    \    label: Use the cis-RNA plus all-four-protein protocol\n    node_type: PERTURBATION\n\
    \  - node_id: fitted-kobs\n    label: Fitted overall cis-cleavage kobs\n    node_type:\
    \ PROCESS\n  - node_id: correct-fraction\n    label: Correctly cleaved fraction\
    \ among products\n    node_type: STATE\n  edges:\n  - edge_id: pair-protocol-increases-kobs\n\
    \    subject: pair-protocol\n    predicate: increases\n    object: fitted-kobs\n\
    \    mechanism: Fitted kobs rises from0.004 +/-0.0004 to2.5 +/-0.1 per min across\
    \ the respective optimized\n      protocols. RNA catalysis and the paired intervention\
    \ remain explicit.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:22298511\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC3378863/\n      snippet: Data analysis\n\
    \      explanation: Table2 and original Figure2 upper-left/lower-left; these are\
    \ Gln measurements,not rescaled\n        older Tyr data.\n      cache_path: evidence/PF01876/chen-2012-fidelity.txt\n\
    \      cache_sha256: c68f4c212e38991b9b58de6054a6efbded483d35baec71a2c767d96c7bc5384a\n\
    \  - edge_id: pair-protocol-increases-correct-fraction\n    subject: pair-protocol\n\
    \    predicate: increases\n    object: correct-fraction\n    mechanism: FC0 rises\
    \ from0.18 +/-0.01 to0.43 +/-0.01. Miscleavage remains the larger product fraction\n\
    \      with the pair; improved fidelity is not complete correction.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:22298511\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3378863/\n\
    \      snippet: Data analysis\n      explanation: Table2 and original Figure2\
    \ preserve the residual majority miscleavage and product-ratio\n        definition.\n\
    \      cache_path: evidence/PF01876/chen-2012-fidelity.txt\n      cache_sha256:\
    \ c68f4c212e38991b9b58de6054a6efbded483d35baec71a2c767d96c7bc5384a\n  - edge_id:\
    \ four-protein-protocol-increases-kobs\n    subject: four-protein-protocol\n \
    \   predicate: increases\n    object: fitted-kobs\n    mechanism: The four-protein\
    \ protocol yields10.5 +/-0.8 per min versus0.004 +/-0.0004 for RNA alone,without\n\
    \      isolating a p30-specific elementary reaction.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:22298511\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3378863/\n\
    \      snippet: Data analysis\n      explanation: Original Figure2 lower-right\
    \ and Table2; the amplitude loss is separate from the rate\n        increase.\n\
    \      cache_path: evidence/PF01876/chen-2012-fidelity.txt\n      cache_sha256:\
    \ c68f4c212e38991b9b58de6054a6efbded483d35baec71a2c767d96c7bc5384a\n  - edge_id:\
    \ four-protein-protocol-increases-correct-fraction\n    subject: four-protein-protocol\n\
    \    predicate: increases\n    object: correct-fraction\n    mechanism: FC0 is0.84\
    \ +/-0.03 versus0.18 +/-0.01 for RNA alone,but the overall product amplitude is\n\
    \      only61% rather than93%. Neither quantity means complete conversion to mature\
    \ tRNA.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:22298511\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3378863/\n\
    \      snippet: Data analysis\n      explanation: Table2,original Figure2 and\
    \ amplitude analysis distinguish fidelity from substrate\n        yield.\n   \
    \   cache_path: evidence/PF01876/chen-2012-fidelity.txt\n      cache_sha256: c68f4c212e38991b9b58de6054a6efbded483d35baec71a2c767d96c7bc5384a\n\
    - graph_id: pho-pair-sl3-binding\n  title: The Pho protein complex has a lower\
    \ fitted Ta-SL3 dissociation constant\n  scope: Hamasaki2015/2016 Figure2 and\
    \ TableI, POP5 alone versus POP5-RPP30 complex.\n  context: SPR25 C,20 mM phosphate7.2/500\
    \ mM NH4Cl/0.05%Tween20; immobilized Ta-SL3,4.8 nM-3 uM sequential\n    protein\
    \ injections,double referencing.\n  family_mapping: PH1877 O59543 equals WP_010885939.1,212\
    \ aa,PF01876 50-209. Full proteins; exact preparation\n    tag/insert referred\
    \ to older protocols,not independently verified.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:70601\n  limitations: Complex kinetic-Langmuir and POP5 steady-state\
    \ fits have different Rmax. No specific binding\n    was observed in the cleavage\
    \ buffer. Published fold arithmetic differs from TableI; no exact fold\n    enhancement\
    \ or chaperone trajectory is asserted.\n  nodes:\n  - node_id: protein-complex\n\
    \    label: Use POP5-RPP30 complex instead of POP5 alone\n    node_type: PERTURBATION\n\
    \  - node_id: fitted-kd\n    label: Fitted Ta-SL3 dissociation constant\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: complex-decreases-fitted-kd\n    subject: protein-complex\n\
    \    predicate: decreases\n    object: fitted-kd\n    mechanism: Reported apparent\
    \ KD is2.27 nM for the complex versus2410 nM for POP5 alone under this\n     \
    \ SPR protocol. Distinct fitting models and surface behavior limit interpretation\
    \ as a microscopic\n      binding change.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:26152732\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4882637/\n      snippet:\
    \ Biosensor experiments\n      explanation: Original Figure2,TableI and Discussion;\
    \ binding is not automatically catalytic activation.\n      cache_path: evidence/PF01876/hamasaki-2015-p30.txt\n\
    \      cache_sha256: 4fc37bc3c0bc02e5aa74e51d6c189f0ef21a23b955f9a52fe7df6ae1a2061df9\n\
    - graph_id: pho-r107a-turnover\n  title: R107A lowers the reported turnover of\
    \ the reconstituted Pho complex\n  scope: Hamasaki2015/2016 TableII, R107A versus\
    \ WT Rpp30.\n  context: 5 pmol RNA and each of five proteins,pre-tRNATyr1.88-19.4\
    \ ug,15 min;50 mM Tris7.6/50 mM MgCl2/600\n    mM NH4OAc/60 mM NH4Cl. Kinetic\
    \ volume/temperature are not independently resolved from the cited earlier\n \
    \   protocol.\n  family_mapping: O59543/WP_010885939.1,PF01876 50-209; R107 is\
    \ verified inside the match. Full Rpp30\n    in an RNA-containing five-protein\
    \ complex,not isolated-domain catalysis.\n  scope_status: MECHANISTIC\n  taxon:\
    \ NCBITaxon:70601\n  limitations: No independent mutant folding,assembly or active-enzyme-fraction\
    \ control verified. SupplementS3\n    remains uninspected. The75 C temperature\
    \ is explicit for the separate dose assay,not silently assigned\n    here.\n \
    \ nodes:\n  - node_id: r107a\n    label: Replace WT Rpp30 with R107A\n    node_type:\
    \ PERTURBATION\n  - node_id: turnover\n    label: Reported reconstituted-complex\
    \ kcat\n    node_type: PROCESS\n  edges:\n  - edge_id: r107a-decreases-turnover\n\
    \    subject: r107a\n    predicate: decreases\n    object: turnover\n    mechanism:\
    \ Reported kcat decreases from1.11 to0.46 per min while nominal KM remains4.99\
    \ versus5.03\n      uM. Substantial activity remains; the data do not identify\
    \ R107 as a chemical catalytic residue.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:26152732\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4882637/\n      snippet:\
    \ Assay for pre-tRNA cleavage activity\n      explanation: Original TableII and\
    \ main Methods; no zero-activity claim is taken from the inconsistent\n      \
    \  K196A table cell.\n      cache_path: evidence/PF01876/hamasaki-2015-p30.txt\n\
    \      cache_sha256: 4fc37bc3c0bc02e5aa74e51d6c189f0ef21a23b955f9a52fe7df6ae1a2061df9\n\
    - graph_id: pho-pair-dose-response\n  title: Increasing the Pho protein-pair dose\
    \ increases cleavage fraction\n  scope: Hamasaki2015/2016 Figure5 open circles.\n\
    \  context: 10 pmol Pho RNA and other three proteins each10 pmol; vary POP5-RPP30\
    \ amounts,15 min75 C in\n    the reconstitution buffer. Contrast the reported5-30-pmol\
    \ protein range.\n  family_mapping: Full PH1877/O59543 Rpp30,PF01876 50-209,jointly\
    \ varied with POP5; not an independent\n    p30 titration.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:70601\n  limitations: Product fraction plateaus around70-75%,not100%.\
    \ The text's20-pmol full-activity wording\n    is approximate. Activity titration\
    \ does not directly measure molecular stoichiometry or establish\n    an in-vivo\
    \ dimer.\n  nodes:\n  - node_id: increase-pair-dose\n    label: Increase the jointly\
    \ supplied POP5-RPP30 dose\n    node_type: PERTURBATION\n  - node_id: cleavage-fraction\n\
    \    label: Pre-tRNATyr cleavage fraction after15 minutes\n    node_type: STATE\n\
    \  edges:\n  - edge_id: pair-dose-increases-cleavage\n    subject: increase-pair-dose\n\
    \    predicate: increases\n    object: cleavage-fraction\n    mechanism: Increasing\
    \ pair dose raises the product fraction over the specified range before a plateau.\n\
    \      It is not equivalent to a measured increase in an elementary cleavage rate\
    \ or a proof of2:1 stoichiometry.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:26152732\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4882637/\n      snippet:\
    \ Assay for pre-tRNA cleavage activity\n      explanation: Original Figure5 and\
    \ its explicit75 C protocol; three replicate means and the incomplete\n      \
    \  plateau are retained.\n      cache_path: evidence/PF01876/hamasaki-2015-p30.txt\n\
    \      cache_sha256: 4fc37bc3c0bc02e5aa74e51d6c189f0ef21a23b955f9a52fe7df6ae1a2061df9\n\
    - graph_id: yeast-deletion-and-complementation\n  title: RPP1 disruption prevents\
    \ haploid outgrowth and tagged Rpp1 complements it\n  scope: Stolc1997 Figures1B/2A\
    \ and strain construction, JN161-derived yeast strains.\n  context: VS161 heterozygous\
    \ diploid sporulation,20 tetrads;65% coding replacement with LEU2. Low-copy\n\
    \    pRS316 three-myc-RPP1 supports deletion spores VS162B/D;5-FOA plasmid-loss\
    \ selection tests dependence.\n  family_mapping: YHR062C P38786 equals AAB96559.1/NP_011929.1,293\
    \ aa,PF01876 1-241. Reference S288c is\n    not an independently sequenced VS\
    \ strain; three myc epitopes follow initiator methionine.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:4932\n  limitations: Whole-gene disruption and full-protein\
    \ complementation,not domain-only necessity or sufficiency.\n    Colony viability\
    \ does not prove correction of every RNA-processing phenotype.\n  nodes:\n  -\
    \ node_id: rpp1-disruption\n    label: Inherit the rpp1::LEU2 disruption without\
    \ complementation\n    node_type: PERTURBATION\n  - node_id: tagged-complement\n\
    \    label: Retain low-copy three-myc-RPP1 in the disrupted haploid\n    node_type:\
    \ PERTURBATION\n  - node_id: haploid-outgrowth\n    label: Viable haploid colony\
    \ outgrowth\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: disruption-decreases-outgrowth\n\
    \    subject: rpp1-disruption\n    predicate: decreases\n    object: haploid-outgrowth\n\
    \    mechanism: Tetrads segregate2:2 viable spores,with survivors lacking the\
    \ LEU2 disruption marker. The\n      result supports essentiality in this strain\
    \ and culture context without identifying a lethal molecular\n      intermediate.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:9353260\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC316654/\n\
    \      snippet: Gene disruption\n      explanation: Original Figure1B,20-tetrad\
    \ analysis and genotype Methods.\n      cache_path: evidence/PF01876/stolc-1997-yeast.txt\n\
    \      cache_sha256: dc04c2148820b58c1336b437b5d67a25e99be059993c7b32eea209d78645b6ba\n\
    \  - edge_id: complement-increases-outgrowth\n    subject: tagged-complement\n\
    \    predicate: increases\n    object: haploid-outgrowth\n    mechanism: Disrupted\
    \ haploids survive with the tagged full-protein plasmid but fail plasmid-loss\
    \ selection.\n      Tagged-protein detection and comparable reported growth support\
    \ this construct's function,not isolated\n      p30-domain sufficiency.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:9353260\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC316654/\n\
    \      snippet: Gene disruption\n      explanation: Original Figure2A/B and strain\
    \ construction distinguish complemented deletion spores\n        from WT controls.\n\
    \      cache_path: evidence/PF01876/stolc-1997-yeast.txt\n      cache_sha256:\
    \ dc04c2148820b58c1336b437b5d67a25e99be059993c7b32eea209d78645b6ba\n- graph_id:\
    \ yeast-glucose-shift-growth\n  title: Repressing GAL-driven RPP1 reduces growth\
    \ after the glucose shift\n  scope: Stolc1997 Figure5A, VS164 versus isogenic\
    \ VS165.\n  context: Galactose-to-glucose shift with repeated dilution to avoid\
    \ starvation; GAL10-RPP1 supplies\n    disrupted VS164,WT RPP1 plus empty vector\
    \ in VS165. Follow OD600 through30 h.\n  family_mapping: Whole YHR062C/RPP1 expression\
    \ perturbation; P38786/AAB96559.1 reference,PF01876 1-241,not\n    domain-specific\
    \ intervention.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:4932\n  limitations:\
    \ Growth is a downstream phenotype. No independent protein-depletion time course\
    \ or time-matched\n    rescue was verified; glucose controls do not resolve every\
    \ metabolic consequence.\n  nodes:\n  - node_id: repress-rpp1\n    label: Repress\
    \ the GAL-driven RPP1 copy in glucose\n    node_type: PERTURBATION\n  - node_id:\
    \ growth\n    label: OD600 growth trajectory after12-16 hours\n    node_type:\
    \ PHENOTYPE\n  edges:\n  - edge_id: repression-decreases-growth\n    subject:\
    \ repress-rpp1\n    predicate: decreases\n    object: growth\n    mechanism: The\
    \ conditional strain approaches a growth plateau while WT continues growing in\
    \ glucose.\n      The causal scope is the promoter/genotype intervention,not an\
    \ observed direct link from any one\n      RNA defect to death.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:9353260\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC316654/\n\
    \      snippet: RNA analysis\n      explanation: Original Figure5A and conditional-allele\
    \ Results establish the growth comparison separately\n        from the RNA panels.\n\
    \      cache_path: evidence/PF01876/stolc-1997-yeast.txt\n      cache_sha256:\
    \ dc04c2148820b58c1336b437b5d67a25e99be059993c7b32eea209d78645b6ba\n- graph_id:\
    \ yeast-pretrna-processing\n  title: RPP1 repression changes pre-tRNALeu3 intermediate\
    \ abundance\n  scope: Stolc1997 Figure5C, conditional VS164 glucose time course\
    \ with WT controls.\n  context: Total RNA,Northern hybridization with mature-tRNALeu\
    \ probe;0/4/7/12/16/21/30 h,WT0/30 h. Transcript\n    species distinguished by\
    \ termini and intron status.\n  family_mapping: Full YHR062C/RPP1 depletion context,P38786/AAB96559.1\
    \ reference,PF01876 1-241. No isolated-domain\n    or purified-protein experiment.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:4932\n  limitations: Steady-state\
    \ intermediates,not directly measured processing rate constants. Growth slows\n\
    \    and both RNaseP/MRP functions may change; no direct Rpp1 cleavage chemistry\
    \ is inferred.\n  nodes:\n  - node_id: repress-rpp1\n    label: Repress GAL-driven\
    \ RPP1 in glucose\n    node_type: PERTURBATION\n  - node_id: unprocessed-ends\n\
    \    label: End-unprocessed pre-tRNALeu3 species\n    node_type: STATE\n  - node_id:\
    \ ends-processed-ivs\n    label: Ends-processed intron-containing tRNALeu3 intermediate\n\
    \    node_type: STATE\n  edges:\n  - edge_id: repression-increases-unprocessed-ends\n\
    \    subject: repress-rpp1\n    predicate: increases\n    object: unprocessed-ends\n\
    \    mechanism: Primary transcript and spliced but end-unprocessed species accumulate\
    \ during repression.\n      Grouped endpoint names retain the distinct bands,not\
    \ a proven sequential reaction chain.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:9353260\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC316654/\n      snippet:\
    \ RNA analysis\n      explanation: Original Figure5C PT and5-prime/3-prime bands;\
    \ unshown leader/intron-probe data are\n        not claimed visually inspected.\n\
    \      cache_path: evidence/PF01876/stolc-1997-yeast.txt\n      cache_sha256:\
    \ dc04c2148820b58c1336b437b5d67a25e99be059993c7b32eea209d78645b6ba\n  - edge_id:\
    \ repression-decreases-processed-ivs\n    subject: repress-rpp1\n    predicate:\
    \ decreases\n    object: ends-processed-ivs\n    mechanism: The end-processed\
    \ but intron-containing intermediate declines as end-unprocessed species\n   \
    \   accumulate. This does not identify Rpp1 as a splicing enzyme.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:9353260\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC316654/\n\
    \      snippet: RNA analysis\n      explanation: Original Figure5C IVS band and\
    \ accompanying interpretation distinguish end processing\n        from intron\
    \ removal.\n      cache_path: evidence/PF01876/stolc-1997-yeast.txt\n      cache_sha256:\
    \ dc04c2148820b58c1336b437b5d67a25e99be059993c7b32eea209d78645b6ba\n- graph_id:\
    \ yeast-ribonuclease-rna-abundance\n  title: RPP1 repression lowers mature RPR1\
    \ and NME1 RNA signals\n  scope: Stolc1997 Figure5D, conditional VS164 glucose\
    \ time course.\n  context: Northern analysis through30 h after shift,with U6 internal\
    \ RNA control; compare the mature\n    RPR1 band separately from its persistent\
    \ precursor.\n  family_mapping: YHR062C/P38786 Rpp1 whole-gene context,PF01876\
    \ 1-241. RPR1 and NME1 are RNA components,not\n    p30 protein paralogs.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:4932\n  limitations: Steady-state abundance is\
    \ not a direct RNA stability or maturation-rate assay. This panel\n    lacks a\
    \ complete time-matched WT series; do not assign all change to direct protein\
    \ protection from\n    degradation.\n  nodes:\n  - node_id: repress-rpp1\n   \
    \ label: Repress GAL-driven RPP1 in glucose\n    node_type: PERTURBATION\n  -\
    \ node_id: mature-rpr1\n    label: Mature RPR1 Northern signal relative to U6\n\
    \    node_type: STATE\n  - node_id: nme1\n    label: NME1 Northern signal relative\
    \ to U6\n    node_type: STATE\n  edges:\n  - edge_id: repression-decreases-rpr1\n\
    \    subject: repress-rpp1\n    predicate: decreases\n    object: mature-rpr1\n\
    \    mechanism: Mature RPR1 signal declines strongly by21 h while the precursor\
    \ band persists. No measured\n      RNA half-life or direct assembly-to-stability\
    \ pathway is claimed.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:9353260\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC316654/\n      snippet: RNA analysis\n\
    \      explanation: Original Figure5D separates mature/precursor RPR1 with U6\
    \ loading context.\n      cache_path: evidence/PF01876/stolc-1997-yeast.txt\n\
    \      cache_sha256: dc04c2148820b58c1336b437b5d67a25e99be059993c7b32eea209d78645b6ba\n\
    \  - edge_id: repression-decreases-nme1\n    subject: repress-rpp1\n    predicate:\
    \ decreases\n    object: nme1\n    mechanism: NME1 also declines in the repression\
    \ series. Shared Rpp1 membership in RNaseP/MRP does\n      not make this a uniquely\
    \ RNaseP-mediated effect.\n    directness: INDIRECT\n    support: OBSERVED\n \
    \   evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:9353260\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC316654/\n      snippet:\
    \ RNA analysis\n      explanation: Original Figure5D NME1/U6 panels; direction\
    \ is retained without inventing a decay mechanism.\n      cache_path: evidence/PF01876/stolc-1997-yeast.txt\n\
    \      cache_sha256: dc04c2148820b58c1336b437b5d67a25e99be059993c7b32eea209d78645b6ba\n\
    - graph_id: yeast-ribosomal-rna-processing\n  title: RPP1 repression shifts ribosomal-RNA\
    \ precursor patterns\n  scope: Stolc1997 Figures5B/6, conditional VS164 with VS165\
    \ controls in Figure6.\n  context: Glucose-shift time course,ethidium-stained\
    \ gels and Northern probes across ITS1/ITS2; interpretation\n    of long and short5.8S\
    \ forms kept separate from abnormal precursor bands.\n  family_mapping: Whole\
    \ YHR062C/RPP1 intervention,P38786/AAB96559.1 reference,PF01876 1-241. RNaseP/MRP\n\
    \    and secondary growth effects are not separated by the genotype.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:4932\n  limitations: Mature18S/25S remain broadly\
    \ unchanged. Precursor boundary assignments partly rely on probe\n    hybridization\
    \ and inference; no claim that Rpp1 directly cleaves each proposed site.\n  nodes:\n\
    \  - node_id: repress-rpp1\n    label: Repress GAL-driven RPP1 in glucose\n  \
    \  node_type: PERTURBATION\n  - node_id: long-short-ratio\n    label: Long-to-short5.8S\
    \ RNA ratio\n    node_type: STATE\n  - node_id: abnormal-precursors\n    label:\
    \ Abnormal24S and21S precursor signals\n    node_type: STATE\n  edges:\n  - edge_id:\
    \ repression-increases-long-short-ratio\n    subject: repress-rpp1\n    predicate:\
    \ increases\n    object: long-short-ratio\n    mechanism: The short5.8S form declines\
    \ relative to the long form during repression. This is a processing-pattern\n\
    \      change,not direct proof of a particular p30-catalyzed cut.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:9353260\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC316654/\n\
    \      snippet: RNA analysis\n      explanation: Original Figure5B and associated\
    \ Results retain the ratio endpoint.\n      cache_path: evidence/PF01876/stolc-1997-yeast.txt\n\
    \      cache_sha256: dc04c2148820b58c1336b437b5d67a25e99be059993c7b32eea209d78645b6ba\n\
    \  - edge_id: repression-increases-abnormal-precursors\n    subject: repress-rpp1\n\
    \    predicate: increases\n    object: abnormal-precursors\n    mechanism: Bands\
    \ assigned to24S and21S species accumulate in the conditional strain. Their accumulation\n\
    \      does not demonstrate the order or direct enzyme responsible for all inferred\
    \ processing failures.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:9353260\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC316654/\n      snippet: RNA analysis\n\
    \      explanation: Original Figure6C/D and probe table; mature18S/25S controls\
    \ prevent a general loss-of-rRNA\n        claim.\n      cache_path: evidence/PF01876/stolc-1997-yeast.txt\n\
    \      cache_sha256: dc04c2148820b58c1336b437b5d67a25e99be059993c7b32eea209d78645b6ba\n\
    - graph_id: yeast-immunoprecipitate-pretrna\n  title: Tagged-Rpp1 immunoprecipitates\
    \ produce pre-tRNASer cleavage products\n  scope: Stolc1997 Figure4, tagged VS162B/D\
    \ versus untagged VS162A-prime/C-prime controls.\n  context: Anti-myc9E10/IgG-agarose\
    \ preparations,0.5 nM labeled pre-tRNASer,30 min37 C,10 mM HEPES8/400\n    mM\
    \ NH4OAc/10 mM Mg acetate/5%glycerol. Figure4 points to IP600-washed material;\
    \ assay Methods says\n    IP150.\n  family_mapping: Full three-myc-YHR062C Rpp1,P38786/AAB96559.1\
    \ reference,PF01876 1-241; native RNA/protein\n    co-precipitates,not purified\
    \ Rpp1 alone.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:4932\n  limitations:\
    \ Wash-salt discrepancy remains unresolved. The preparation contains catalytic\
    \ RNA and associated\n    proteins; it does not establish intrinsic Rpp1 nuclease\
    \ activity or domain-only sufficiency.\n  nodes:\n  - node_id: tagged-ip\n   \
    \ label: Use tagged-Rpp1 immunoprecipitate instead of untagged control beads\n\
    \    node_type: PERTURBATION\n  - node_id: cleavage-products\n    label: Mature-tRNA-sized\
    \ and5-prime-leader products\n    node_type: STATE\n  edges:\n  - edge_id: tagged-ip-increases-cleavage\n\
    \    subject: tagged-ip\n    predicate: increases\n    object: cleavage-products\n\
    \    mechanism: Tagged preparations produce the expected two bands while untagged\
    \ controls largely retain\n      precursor. Activity belongs to the captured RNP\
    \ preparation,not proven isolated p30 chemistry.\n    directness: DIRECT\n   \
    \ support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:9353260\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC316654/\n\
    \      snippet: Immunoprecipitation\n      explanation: Original Figure4 lanes2-5,caption\
    \ and assay Methods retain the IP150/IP600 ambiguity.\n      cache_path: evidence/PF01876/stolc-1997-yeast.txt\n\
    \      cache_sha256: dc04c2148820b58c1336b437b5d67a25e99be059993c7b32eea209d78645b6ba\n\
    - graph_id: yeast-immunoprecipitate-its141\n  title: Mixed Rpp1 immunoprecipitates\
    \ increase ITS141 cleavage products\n  scope: Stolc1997 Figure7, tagged versus\
    \ untagged yeast preparations.\n  context: IP150-washed anti-myc beads,3.2 nM\
    \ ITS141,2 h37 C;20 mM Tris8/10 mM MgCl2/1 mM EDTA/50 mM KCl,RNasin\n    and BSA.\
    \ Printed BSA50 mg/ml remains unresolved.\n  family_mapping: Three-myc full Rpp1,P38786/AAB96559.1,PF01876\
    \ 1-241. Both RPR1 and NME1 RNA associate\n    with the captured preparation.\n\
    \  scope_status: MECHANISTIC\n  taxon: NCBITaxon:4932\n  limitations: Background\
    \ bands occur in controls; approximate A3-region product assignment does not uniquely\n\
    \    identify RNaseP versus RNaseMRP. High-salt loss of this activity is data\
    \ not shown,not a visually\n    verified edge.\n  nodes:\n  - node_id: tagged-ip\n\
    \    label: Use tagged-Rpp1 mixed-RNP immunoprecipitate\n    node_type: PERTURBATION\n\
    \  - node_id: its141-products\n    label: ITS141 products near the expected A3-region\
    \ size\n    node_type: STATE\n  edges:\n  - edge_id: tagged-ip-increases-its141-products\n\
    \    subject: tagged-ip\n    predicate: increases\n    object: its141-products\n\
    \    mechanism: Tagged preparations yield stronger principal ITS141 cleavage products\
    \ than untagged controls.\n      This supports preparation-associated processing,not\
    \ a unique p30 reaction or exclusive RNaseP pathway.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:9353260\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC316654/\n\
    \      snippet: Immunoprecipitation\n      explanation: Original Figure7B lanes1-4\
    \ and Methods; retain mixed RNAs,background products and uncertain\n        printed\
    \ BSA unit.\n      cache_path: evidence/PF01876/stolc-1997-yeast.txt\n      cache_sha256:\
    \ dc04c2148820b58c1336b437b5d67a25e99be059993c7b32eea209d78645b6ba\ncuration_events:\n\
    - timestamp: '2026-10-11T18:57:44Z'\n  curator: Codex\n  action: CREATE\n  outcome:\
    \ changed\n  summary: Curate p30 RNA reconstitution mutation and yeast-processing\
    \ causal contexts\n  history_record: history/records/PF01876/2026-10-11T185744Z-codex-573693.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Versioned reference sequences exactly match yeast P38786/AAB96559.1/NP_011929.1,
    Mth O26784/AAB85193.1, Mja Q58539/WP_010870650.1, Pfu Q8TZS0/WP_011013054.1 and
    Pho O59543/WP_010885939.1. PF01876 intervals are respectively1-241,10-232,7-212,59-211
    and50-209. Pho R107 is inside the match. JN161-derived yeast assay strains are
    not silently called reference S288c. Exact assay-batch sequences and some earlier
    construct tags remain unverified; full proteins and RNA-containing complexes are
    not isolated domains.
  target_ids:
  - PF01876
  evidence_ids:
  - identity
  - primary
  - yeast-processing
  - reconstitution
  - fidelity
  - gaps-and-access
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Fifteen direct effects retain Mth optimized maximal kobs, Mja full and
    truncated RNA reconstitution, Pfu product fidelity, Mja cis rate and fidelity,
    Pho SPR, R107A kinetics and joint-pair titration, and two yeast immunoprecipitate
    processing assays. Nine indirect effects retain yeast disruption and complementation,
    promoter-repression growth, pre-tRNA intermediates, RPR1/NME1 abundance and rRNA
    patterns. Composite buffer/time/dose interventions remain explicit. FC0 is not
    yield, KM is not binding KD, the61% all-four amplitude is not complete conversion,
    and no direct p30 cleavage chemistry, RNA half-life, cellular stoichiometry or
    family-wide mechanism is asserted.
  target_ids:
  - PF01876
  evidence_ids:
  - primary
  - native
  - yeast-processing
  - reconstitution
  - fidelity
  - gaps-and-access
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Resolve exact constructs, kinetic temperature/volume, earlier-method mixing
    and reference inconsistencies, IP150/IP600 and printed BSA discrepancies, Pho
    fit arithmetic and the K196A specificity cell. Inspect missing Pho supplementary
    controls and additional archaeal, plant, animal and human functional studies.
    All4590 frozen proteins remain in scope; these five mapped references do not exhaust
    family functions or establish domain-only sufficiency.
  target_ids:
  - PF01876
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01876-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve Rpp30 assay provenance and extend member-specific causal coverage
  description: Recover unresolved construct and protocol details and the inaccessible
    Pho supplements, seek matched-buffer and mutant folding or assembly controls,
    and assess additional member-specific studies with exact accession/domain mapping.
    Keep protein-pair effects, whole-gene phenotypes, mixed RNP activity and inferred
    molecular intermediates distinct. Preserve condition-specific negatives and source
    disagreements rather than adopting a universal p30 catalytic pathway.
  target_ids:
  - PF01876
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - yeast-processing
  - reconstitution
  - fidelity
  - gaps-and-access
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01876.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Recover unresolved construct and protocol details and the inaccessible
    Pho supplements, seek matched-buffer and mutant folding or assembly controls,
    and assess additional member-specific studies with exact accession/domain mapping.
    Keep protein-pair effects, whole-gene phenotypes, mixed RNP activity and inferred
    molecular intermediates distinct. Preserve condition-specific negatives and source
    disagreements rather than adopting a universal p30 catalytic pathway.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01876
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Original Stolc Figures1/2/4/5/6/7, Chen2010 Figures3/4/7, Chen2012 Figures1/2 and
  Hamasaki Figures2/5 were visually inspected. Chen2010 public supplementary PDF Methods,
  primers, TableS2 and kinetic controls were read; earlier kinetic control images
  were inspected in the linked Rpp29 work. Pho supplemental retrieval returned XML
  or download-preparation HTML and the publisher returned403; SupplementS3 was not
  inspected. No raw-data refit, assay-batch sequencing, exhaustive literature coverage
  or experimental replication. Rendered-page checks follow separately.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
