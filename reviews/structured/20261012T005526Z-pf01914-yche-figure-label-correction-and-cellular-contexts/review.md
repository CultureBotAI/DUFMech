# PF01914 successor review correcting the YchE figure label

- Review: 20261012T005526Z-pf01914-yche-figure-label-correction-and-cellular-contexts
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-12T00:54:37Z
- Finished UTC: 2026-10-12T00:55:26Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Successor to the retained20261012T005223Z review: enlarged Figure1C corrects YchE p0.387 to p0.38; p0.87 labels YjeM. The earlier report and evidence bytes are preserved, not silently rewritten. Graph counts, directions and the nonsignificant YchE uptake conclusion are unchanged. Thirteen PHENOTYPIC graphs retain39 OBSERVED/EXPERIMENTAL INDIRECT effects, with eight current evidence/identity/coverage ledgers and two OPEN discussions. SnatA, MarC and YchE contexts are kept distinct. Selected clone phenotypes, strain confounds, conflicting susceptibility results, negative comparisons and uninspected evidence remain explicit. Partial same-agent scientific self-review yields NEEDS_FOLLOWUP; IN_PROGRESS remains, not full-family characterization or endorsement.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Former UPF0056; selected assays from six primary studies, not all15684 frozen proteins or all publication results.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01914 | data/families/PF01914.yaml | generated | PF01914 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01914 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01914.

Frozen PF01914 MarC/IPR002771 is former UPF0056. K-12 P0AEY1 maps PF01914 at5-217 of221aa and P25743/YchE at9-210 of215aa. Exact AB093585.1/BAC53669.1 SnatA equals UniParc UPI0000062A6D,216aa, PF01914 9-214. Q8J305 retirement is not biological absence. ATCC25922 DR76_3329/AIL17056.1 equals UPI00000DEBB0,221aa,PF01914 5-217, with N36S relative to K-12. Published primer tails map a full-CDS validation insert3541797-3542673; the different enrichment interval ending3542008 remains unresolved. Reference equality and primer mapping do not independently sequence historical clones. Imported identity, counters and frozen snapshot remain unchanged.

### Directed effects and limits

graph: supported. Targets: PF01914.

SnatA uptake and competition are scoped to genomic constructs in AK430; WAT9 serine growth is a separate phenotype. MarC threonine edges name whole selected clones, including B2059 passenger variants and S140SS as an insertion. YchE growth rescue is not promoted to significant transport in the other tested host. Minty reconstruction graphs name the reported strain comparison, not a clean isogenic MarC deletion, because EcHW24 construction and EcNR1 comparator differ in MutS. Babel deletion growth is distinct from non-additive M35stop expression, which is not WT rescue. Gingras five modest MIC changes are conditional TOP10 construct comparisons with pFF6 and antisense controls, not clinical resistance, direct efflux or universal family function. McDermott negative susceptibility tests are retained alongside the different 2018 result; antibiotic-exposure RNA is steady-state abundance, not demonstrated promoter induction. No observed molecular transport cycle, binding-site residue or inter-study relay is asserted.

### Remaining family coverage

completeness: concern. Targets: PF01914.

Three selected member branches and six papers are not all15684 proteins. Other archaeal members, YhgN and YvbG remain uncurated. Native archaeal experiments, purified reconstitution, matched host/allele/vector antibiotic tests, independent single-allele reconstruction and historical clone sequences remain needed. Glucose units, 2011 background/uncertainty and 2018 enrichment boundaries are unresolved. Figure9 epistasis, many supplements and raw replicate data remain uninspected.

## Findings

### additional-contexts: Resolve source and clone discrepancies and extend member-specific mechanisms

minor / open / confirmed; issue key: pf01914-causal-context-coverage.

Reconstruct selected MarC variants separately from passenger mutations; verify YchE flux independently of growth rescue; resolve the 2011 MutS background and 2025 glucose units. Recover original 2018 enrichment boundaries and raw MIC uncertainty, retaining matched-control limits. Extend verified archaeal/YhgN/YvbG branches with primary assays and test purified transport before direct biochemical edges. Preserve negative results and native history; save an evidence-backed successor review for additional contexts rather than editing this partial report.

## Recommended Actions And Acceptance Checks

### extend-contexts

Reconstruct selected MarC variants separately from passenger mutations; verify YchE flux independently of growth rescue; resolve the 2011 MutS background and 2025 glucose units. Recover original 2018 enrichment boundaries and raw MIC uncertainty, retaining matched-control limits. Extend verified archaeal/YhgN/YvbG branches with primary assays and test purified transport before direct biochemical edges. Preserve negative results and native history; save an evidence-backed successor review for additional contexts rather than editing this partial report.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://doi.org/10.1093/jb/mvg021; Main pages173-178, original Figures2-4 and Tables1-3; glycine uptake, upstream constructs, inhibitors, competition and WAT9 growth. | supports | Exact KS-1 SnatA genomic constructs support cellular glycine uptake, inhibitor sensitivity, strong amino-acid competition and a separate serine-medium growth effect in heterologous E. coli. Upstream truncation leaves the full ORF and loses qualitative readouts, not a tested protein residue deletion. Whole-cell effects do not establish purified transport, every competitor as cargo, coupling stoichiometry or native archaeal action. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01914/; Accession and domain locations; paired UniProt identity facts | supports | Frozen PF01914 MarC/IPR002771 is former UPF0056. K-12 P0AEY1 maps PF01914 at5-217 of221aa and P25743/YchE at9-210 of215aa. Exact AB093585.1/BAC53669.1 SnatA equals UniParc UPI0000062A6D,216aa, PF01914 9-214. Q8J305 retirement is not biological absence. ATCC25922 DR76_3329/AIL17056.1 equals UPI00000DEBB0,221aa,PF01914 5-217, with N36S relative to K-12. Published primer tails map a full-CDS validation insert3541797-3542673; the different enrichment interval ending3542008 remains unresolved. Reference equality and primer mapping do not independently sequence historical clones. Imported identity, counters and frozen snapshot remain unchanged. |
| threonine-clones-and-yche | https://pmc.ncbi.nlm.nih.gov/articles/PMC12003319/; MarC/YchE Results, Methods2.1/2.2/2.4/2.5/2.6, Tables1-3 and original Figures1/2. | supports | Selected MarC clones increase uptake/growth; YchE growth rescue remains separate from nonsignificant different-host uptake and glucose-unit inconsistency. |
| antibiotic-rna-and-negative-susceptibility | https://pmc.ncbi.nlm.nih.gov/articles/PMC2223875/; Full short letter, original Figure1 and caption. | supports | Antibiotic exposure raises steady-state marC RNA without direct induction evidence; negative susceptibility/MarR/salicylate contexts are retained. |
| qualified-isobutanol-reconstruction | https://pmc.ncbi.nlm.nih.gov/articles/PMC3071312/; Table3, selected MarC Results/Discussion, base-strain, phenotype and recombination Methods. | supports | Carbon/solvent-dependent growth and OD effects are reported against EcNR1; EcHW24 construction introduces unresolved MutS-background qualification. |
| host-dependent-mic-and-primer-mapping | https://pmc.ncbi.nlm.nih.gov/articles/PMC5857375/; MarC Results/Discussion, functional validation, Tables1/2 and supplementary PDF pages4/5 TablesS2/S3. | supports | Five modest TOP10 MIC shifts have nonidentical control and technical-variation limits; exact donor and PCR primer mapping do not resolve the original enrichment interval. |
| isoprenol-and-butanol-growth | https://pmc.ncbi.nlm.nih.gov/articles/PMC7653855/; MarC Results/Discussion, growth and strain Methods, Tables3/4 and original Figures4/5. | supports | MarC deletion improves relative growth under two solvent conditions; M35stop fragment expression is not wild-type complementation or an additional benefit. |
| discovery-and-remaining-coverage | evidence/PF01914/coverage.txt; Ignored/hidden-inclusive local search, reviewed-family inventory, public family/member searches and scope ledger. | supports | Three member branches and six selected primary papers, not complete family coverage; retired accessions and access failures are not biological negatives. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01914 | data/families/PF01914.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Akahane original Figures2-4/Tables1-3, Bubnov Figures1/2, McDermott Figure1 and Babel Figures4/5 were visually inspected. Minty Table3 and Gingras Tables1/2 plus supplement TablesS2/S3 were inspected as parsed text/tables; not every figure, supplement or raw dataset was reviewed. Exact reference sequences and primer matching do not establish historical assay-clone identity. Source contradictions are retained, not corrected by assumption.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T005526Z-pf01914-yche-figure-label-correction-and-cellular-contexts
title: PF01914 successor review correcting the YchE figure label
started_at: '2026-10-12T00:54:37Z'
finished_at: '2026-10-12T00:55:26Z'
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
summary: 'Successor to the retained20261012T005223Z review: enlarged Figure1C corrects
  YchE p0.387 to p0.38; p0.87 labels YjeM. The earlier report and evidence bytes are
  preserved, not silently rewritten. Graph counts, directions and the nonsignificant
  YchE uptake conclusion are unchanged. Thirteen PHENOTYPIC graphs retain39 OBSERVED/EXPERIMENTAL
  INDIRECT effects, with eight current evidence/identity/coverage ledgers and two
  OPEN discussions. SnatA, MarC and YchE contexts are kept distinct. Selected clone
  phenotypes, strain confounds, conflicting susceptibility results, negative comparisons
  and uninspected evidence remain explicit. Partial same-agent scientific self-review
  yields NEEDS_FOLLOWUP; IN_PROGRESS remains, not full-family characterization or
  endorsement.'
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01914.yaml
    sha256: f923972216f3a0af33dd426a6be1209be9023fccf731cb30bb2bf8451c7c71cd
    role: context
  - path: data/families/PF01914.yaml
    sha256: aecae4124be464918d09b14f90c07cd920114e3166bc99fda83a5969a45828df
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
  - path: evidence/PF01914/akahane-2003.txt
    role: context
    sha256: 576f405a8e8066e4323ddbf9d30f8ce3f2cb3a8f7d5221e42657942c712c7cce
  - path: evidence/PF01914/identity.txt
    role: context
    sha256: 28aa35fc6cd9fe9f1af8f94f59930867951ec8e6d14fc5fc5d9405b012f2bd41
  - path: evidence/PF01914/bubnov-2025-figure1-corrected.txt
    role: context
    sha256: 2f2f41f6b16aa17eea7dd32a2fb38bf239350955318992f62832b8371f48e348
  - path: evidence/PF01914/mcdermott-2008.txt
    role: context
    sha256: 8f0f64d47bff41d3986fa3c0a9fe0019601dc706de6e901503673a35a742e4e0
  - path: evidence/PF01914/minty-2011.txt
    role: context
    sha256: 21198e46f0dad3f70e389e7c57e35cff40a36df16da5084d45f1e97df78ba854
  - path: evidence/PF01914/gingras-2018.txt
    role: context
    sha256: 77a82410ca3790377b21059eadeb40eba8a319afc681c1c7d4b438535c9eeaa2
  - path: evidence/PF01914/babel-2020.txt
    role: context
    sha256: 64ef3a358507e182807f7b1bdc126b1f7f45eacf3b77d91a4f9ed50e169a1536
  - path: evidence/PF01914/coverage.txt
    role: context
    sha256: 9bb3d9862846337b0d808a4b88ed5374a65706f1943cd9e560e3047de25f3583
targets:
- target_id: PF01914
  path: data/families/PF01914.yaml
  label: PF01914
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01914.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: b5bccdc33105dd206354b011caed1fd0475d54f692e0b04c45cf9b305b15808b
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Former UPF0056; selected assays from six primary studies, not all15684
    frozen proteins or all publication results.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01914
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Three selected member branches and six papers are not all15684 proteins.
      Other archaeal members, YhgN and YvbG remain uncurated. Native archaeal experiments,
      purified reconstitution, matched host/allele/vector antibiotic tests, independent
      single-allele reconstruction and historical clone sequences remain needed. Glucose
      units, 2011 background/uncertainty and 2018 enrichment boundaries are unresolved.
      Figure9 epistasis, many supplements and raw replicate data remain uninspected.
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
  - PF01914
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1093/jb/mvg021
  locator: Main pages173-178, original Figures2-4 and Tables1-3; glycine uptake, upstream
    constructs, inhibitors, competition and WAT9 growth.
  accessed_at: '2026-10-12T00:55:26Z'
  support: supports
  snapshot_sha256: 576f405a8e8066e4323ddbf9d30f8ce3f2cb3a8f7d5221e42657942c712c7cce
  summary: Exact KS-1 SnatA genomic constructs support cellular glycine uptake, inhibitor
    sensitivity, strong amino-acid competition and a separate serine-medium growth
    effect in heterologous E. coli. Upstream truncation leaves the full ORF and loses
    qualitative readouts, not a tested protein residue deletion. Whole-cell effects
    do not establish purified transport, every competitor as cargo, coupling stoichiometry
    or native archaeal action.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01914/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-12T00:55:26Z'
  support: supports
  snapshot_sha256: 28aa35fc6cd9fe9f1af8f94f59930867951ec8e6d14fc5fc5d9405b012f2bd41
  summary: Frozen PF01914 MarC/IPR002771 is former UPF0056. K-12 P0AEY1 maps PF01914
    at5-217 of221aa and P25743/YchE at9-210 of215aa. Exact AB093585.1/BAC53669.1 SnatA
    equals UniParc UPI0000062A6D,216aa, PF01914 9-214. Q8J305 retirement is not biological
    absence. ATCC25922 DR76_3329/AIL17056.1 equals UPI00000DEBB0,221aa,PF01914 5-217,
    with N36S relative to K-12. Published primer tails map a full-CDS validation insert3541797-3542673;
    the different enrichment interval ending3542008 remains unresolved. Reference
    equality and primer mapping do not independently sequence historical clones. Imported
    identity, counters and frozen snapshot remain unchanged.
- evidence_id: threonine-clones-and-yche
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC12003319/
  locator: MarC/YchE Results, Methods2.1/2.2/2.4/2.5/2.6, Tables1-3 and original Figures1/2.
  summary: Selected MarC clones increase uptake/growth; YchE growth rescue remains
    separate from nonsignificant different-host uptake and glucose-unit inconsistency.
  accessed_at: '2026-10-12T00:55:26Z'
  support: supports
  snapshot_sha256: 2f2f41f6b16aa17eea7dd32a2fb38bf239350955318992f62832b8371f48e348
- evidence_id: antibiotic-rna-and-negative-susceptibility
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2223875/
  locator: Full short letter, original Figure1 and caption.
  summary: Antibiotic exposure raises steady-state marC RNA without direct induction
    evidence; negative susceptibility/MarR/salicylate contexts are retained.
  accessed_at: '2026-10-12T00:55:26Z'
  support: supports
  snapshot_sha256: 8f0f64d47bff41d3986fa3c0a9fe0019601dc706de6e901503673a35a742e4e0
- evidence_id: qualified-isobutanol-reconstruction
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3071312/
  locator: Table3, selected MarC Results/Discussion, base-strain, phenotype and recombination
    Methods.
  summary: Carbon/solvent-dependent growth and OD effects are reported against EcNR1;
    EcHW24 construction introduces unresolved MutS-background qualification.
  accessed_at: '2026-10-12T00:55:26Z'
  support: supports
  snapshot_sha256: 21198e46f0dad3f70e389e7c57e35cff40a36df16da5084d45f1e97df78ba854
- evidence_id: host-dependent-mic-and-primer-mapping
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5857375/
  locator: MarC Results/Discussion, functional validation, Tables1/2 and supplementary
    PDF pages4/5 TablesS2/S3.
  summary: Five modest TOP10 MIC shifts have nonidentical control and technical-variation
    limits; exact donor and PCR primer mapping do not resolve the original enrichment
    interval.
  accessed_at: '2026-10-12T00:55:26Z'
  support: supports
  snapshot_sha256: 77a82410ca3790377b21059eadeb40eba8a319afc681c1c7d4b438535c9eeaa2
- evidence_id: isoprenol-and-butanol-growth
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7653855/
  locator: MarC Results/Discussion, growth and strain Methods, Tables3/4 and original
    Figures4/5.
  summary: MarC deletion improves relative growth under two solvent conditions; M35stop
    fragment expression is not wild-type complementation or an additional benefit.
  accessed_at: '2026-10-12T00:55:26Z'
  support: supports
  snapshot_sha256: 64ef3a358507e182807f7b1bdc126b1f7f45eacf3b77d91a4f9ed50e169a1536
- evidence_id: discovery-and-remaining-coverage
  kind: search
  reference: evidence/PF01914/coverage.txt
  locator: Ignored/hidden-inclusive local search, reviewed-family inventory, public
    family/member searches and scope ledger.
  search_scope: PF01914/UPF0056/MarC/YchE/SnatA and selected functional leads; local
    curation/evidence/history/reviews/reports excluding generated inventory.
  summary: Three member branches and six selected primary papers, not complete family
    coverage; retired accessions and access failures are not biological negatives.
  accessed_at: '2026-10-12T00:55:26Z'
  support: supports
  snapshot_sha256: 9bb3d9862846337b0d808a4b88ed5374a65706f1943cd9e560e3047de25f3583
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-12T00:55:26Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01914
  kind: record_content
  reference: data/families/PF01914.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-12T00:55:26Z'
  support: context_only
  snapshot_sha256: aecae4124be464918d09b14f90c07cd920114e3166bc99fda83a5969a45828df
  quote: "id: Pfam:PF01914\npfam_id: PF01914\nname: MarC family integral membrane\
    \ protein\nshort_name: MarC\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01914\n\
    counters:\n  proteins: 15684\n  matches: 15727\n  proteomes: 10592\n  taxa: 14991\n\
    \  structures: 0\n  alphafold_models: 10306\n  domain_architectures: 8\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002771\ndescription: Integral membrane protein family\
    \ that includes the protein MarC. MarC was thought to be a\n  multiple antibiotic\
    \ resistance protein. Nevertheless, a study has shown that MarC is not involved\
    \ in\n  multiple antibiotic resistance [[cite:PUB00077123]]. The function of this\
    \ family is unclear.\ncuration_history: history/records/PF01914\ndiscussions:\n\
    - discussion_id: upf0056-member-and-mechanism-coverage\n  prompt: Extend verified\
    \ family branches and distinguish cellular phenotypes from a direct transport\n\
    \    cycle.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: Selected SnatA,\
    \ MarC and YchE experiments do not characterize all 15684 frozen proteins or\n\
    \    every PF01914 domain.\n  evidence:\n  - reference: doi:10.1093/jb/mvg021\n\
    \    supports: PARTIAL\n    evidence_source: heterologous_primary_assays\n   \
    \ explanation: SnatA construct effects and competition are supported, but purified\
    \ transport, coupling\n      stoichiometry, dimer necessity and native archaeal\
    \ function remain untested.\n  - reference: PMID:40248429\n    supports: PARTIAL\n\
    \    evidence_source: selected_clone_primary_assays\n    explanation: MarC selected\
    \ clones increase uptake/growth; YchE growth rescue does not yield significant\n\
    \      uptake in the other tested host.\n  posed_by: Codex\n  posed_date: '2026-10-12'\n\
    \  notes: Investigate mapped YhgN, YvbG, PH0214/PH0760/PAB0863/PAB2220/MJ0972/MJ1677\
    \ independently. Reconstruct\n    variants and B2059 passenger mutations; verify\
    \ protein abundance and clone sequences. Do not convert\n    AlphaFold or family\
    \ naming into causal residue evidence. Retain IN_PROGRESS and partial coverage.\n\
    - discussion_id: marc-source-and-strain-discrepancies\n  prompt: Resolve host,\
    \ allele and source discrepancies before making universal MarC claims.\n  kind:\
    \ CURATION_TODO\n  status: OPEN\n  rationale: Different strains, controls and\
    \ endpoints produce different directions; source inconsistencies\n    cannot be\
    \ silently corrected.\n  evidence:\n  - reference: PMID:21435272\n    supports:\
    \ PARTIAL\n    evidence_source: reconstruction_background_check\n    explanation:\
    \ Table 3 compares with EcNR1 but construction uses MutS-negative EcHW24 or progeny.\n\
    \  - reference: PMID:29319470\n    supports: PARTIAL\n    evidence_source: mic_and_primer_check\n\
    \    explanation: TOP10 MIC increases are small and host dependent; primer mapping\
    \ supports the validation\n      insert but not the reported enrichment boundaries.\n\
    \  - reference: PMID:17954692\n    supports: PARTIAL\n    evidence_source: negative_susceptibility_context\n\
    \    explanation: AG100 antibiotic-susceptibility negatives and RNA stabilization\
    \ qualify later resistance\n      interpretations.\n  posed_by: Codex\n  posed_date:\
    \ '2026-10-12'\n  notes: Resolve 2011 MutS background and uncertainty type, 2018\
    \ enrichment interval/raw MIC variation,\n    2025 glucose units and YchE flux,\
    \ and historical clone sequences. M35stop is not wild-type complementation.\n\
    \    Compare matching allele/recipient/vector/assay conditions before reconciliation.\
    \ Retain negative and\n    unassessed branches in evidence/PF01914; any additional\
    \ edges require a successor review.\ncausal_graphs:\n- graph_id: snata-expression-uptake-2003\n\
    \  title: SnatA genomic constructs restore heterologous glycine uptake\n  scope:\
    \ Akahane2003 KS-1 snatA genomic inserts expressed in E. coli AK430 cycA::kan,\
    \ not native archaeal\n    membranes.\n  context: Figure 4A pSA28 versus empty\
    \ pUC119; Figure 2A qualitative pSA17 construct comparison. Washed-cell\n    radioglycine\
    \ filtration at 37 C, HEPES/Tris pH 7.4, MgSO4 and Tris-lactate.\n  family_mapping:\
    \ Thermococcus sp. KS-1/JCM11816 SnatA BAC53669.1 from AB093585.1 equals UniParc\
    \ UPI0000062A6D,\n    216 aa, PF01914 9-214. Q8J305 is retired, not biologically\
    \ absent. Genomic constructs contain full\n    SnatA plus flanking DNA; no isolated-domain\
    \ sufficiency.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:1295125\n  limitations:\
    \ pSA28 contains about 2.8 kb and pSA17 is a smaller genomic insert; pSA17 is\
    \ not tested\n    by the Figure 4 time course. Whole-cell uptake and apparent\
    \ Kt 24 uM do not establish purified binding\n    affinity, oligomer requirement,\
    \ H+:glycine stoichiometry or an atomic transport cycle.\n  nodes:\n  - node_id:\
    \ psa28\n    label: AK430 expressing pSA28 relative to empty pUC119\n    node_type:\
    \ PERTURBATION\n  - node_id: psa17\n    label: AK430 expressing positive pSA17\
    \ derivative\n    node_type: PERTURBATION\n  - node_id: glycine-uptake\n    label:\
    \ Cell-associated radiolabeled glycine uptake\n    node_type: PROCESS\n  edges:\n\
    \  - edge_id: psa28-increases-uptake\n    subject: psa28\n    predicate: increases\n\
    \    object: glycine-uptake\n    mechanism: The SnatA-containing pSA28 construct\
    \ increases cellular glycine accumulation over the empty-vector\n      background;\
    \ intermediates and flanking-sequence effects are not isolated.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: doi:10.1093/jb/mvg021\n      source_url: https://doi.org/10.1093/jb/mvg021\n\
    \      snippet: a protein of 216 amino acid residues\n      explanation: Figure\
    \ 4A original plot and glycine-transport Methods; pUC119 control.\n      cache_path:\
    \ evidence/PF01914/akahane-2003.txt\n      cache_sha256: 576f405a8e8066e4323ddbf9d30f8ce3f2cb3a8f7d5221e42657942c712c7cce\n\
    \  - edge_id: psa17-enables-uptake\n    subject: psa17\n    predicate: enables\n\
    \    object: glycine-uptake\n    mechanism: The smaller pSA17 genomic construct\
    \ retains the positive qualitative uptake score; this\n      is not a separately\
    \ measured purified transporter rate.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: doi:10.1093/jb/mvg021\n\
    \      source_url: https://doi.org/10.1093/jb/mvg021\n      snippet: a protein\
    \ of 216 amino acid residues\n      explanation: Figure 2A construct map and primary-structure\
    \ Results, pSA17 positive score versus\n        negative derivatives.\n      cache_path:\
    \ evidence/PF01914/akahane-2003.txt\n      cache_sha256: 576f405a8e8066e4323ddbf9d30f8ce3f2cb3a8f7d5221e42657942c712c7cce\n\
    - graph_id: snata-upstream-construct-2003\n  title: Upstream truncation reduces\
    \ SnatA-construct phenotypes\n  scope: pSA14 versus positive pSA17 in heterologous\
    \ E. coli AK430; full SnatA coding sequence remains\n    present.\n  context:\
    \ Figure 2A qualitative glycine uptake and D-alanine colony formation. pSA14 starts\
    \ 97 bp upstream\n    of snatA; colony selection uses 5 mg/ml D-alanine minimal\
    \ medium, 37 C, about one week.\n  family_mapping: Thermococcus sp. KS-1/JCM11816\
    \ SnatA BAC53669.1 from AB093585.1 equals UniParc UPI0000062A6D,\n    216 aa,\
    \ PF01914 9-214. Q8J305 is retired, not biologically absent. Genomic constructs\
    \ contain full\n    SnatA plus flanking DNA; no isolated-domain sufficiency.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:1295125\n  limitations: Upstream\
    \ DNA loss is not a SnatA residue deletion. A needed expression-control region\
    \ is\n    suggested, but direct promoter binding, transcript abundance, exact\
    \ native archaeal regulation and\n    equal construct protein abundance are unmeasured.\n\
    \  nodes:\n  - node_id: upstream-truncation\n    label: pSA14 upstream-truncated\
    \ construct relative to pSA17\n    node_type: PERTURBATION\n  - node_id: glycine-uptake\n\
    \    label: Qualitative glycine uptake\n    node_type: PROCESS\n  - node_id: d-alanine-colonies\n\
    \    label: D-alanine-supported colony formation\n    node_type: PHENOTYPE\n \
    \ edges:\n  - edge_id: truncation-decreases-uptake\n    subject: upstream-truncation\n\
    \    predicate: decreases\n    object: glycine-uptake\n    mechanism: The upstream-truncated\
    \ construct loses the uptake score despite retaining the full snatA\n      ORF;\
    \ this is an expression-construct effect.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: doi:10.1093/jb/mvg021\n\
    \      source_url: https://doi.org/10.1093/jb/mvg021\n      snippet: a protein\
    \ of 216 amino acid residues\n      explanation: Figure 2A and primary-structure\
    \ Results, full-ORF pSA14 negative versus pSA17 positive.\n      cache_path: evidence/PF01914/akahane-2003.txt\n\
    \      cache_sha256: 576f405a8e8066e4323ddbf9d30f8ce3f2cb3a8f7d5221e42657942c712c7cce\n\
    \  - edge_id: truncation-decreases-colonies\n    subject: upstream-truncation\n\
    \    predicate: decreases\n    object: d-alanine-colonies\n    mechanism: pSA14\
    \ loses D-alanine colony formation relative to pSA17 in the specified selection;\
    \ direct\n      D-alanine transport is not quantified.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: doi:10.1093/jb/mvg021\n      source_url: https://doi.org/10.1093/jb/mvg021\n\
    \      snippet: a protein of 216 amino acid residues\n      explanation: Figure\
    \ 2A construct scores and functional-cloning Methods.\n      cache_path: evidence/PF01914/akahane-2003.txt\n\
    \      cache_sha256: 576f405a8e8066e4323ddbf9d30f8ce3f2cb3a8f7d5221e42657942c712c7cce\n\
    - graph_id: snata-energetic-perturbations-2003\n  title: Energy-disrupting treatments\
    \ reduce SnatA-associated cellular uptake\n  scope: AK430 carrying pSA28, with\
    \ inhibitor treatment compared with the same construct without inhibitor.\n  context:\
    \ Figure 4 whole-cell radioglycine uptake at 37 C. FCCP 10 ug/ml is separate from\
    \ the valinomycin-plus-nigericin\n    condition.\n  family_mapping: Thermococcus\
    \ sp. KS-1/JCM11816 SnatA BAC53669.1 from AB093585.1 equals UniParc UPI0000062A6D,\n\
    \    216 aa, PF01914 9-214. Q8J305 is retired, not biologically absent. Genomic\
    \ constructs contain full\n    SnatA plus flanking DNA; no isolated-domain sufficiency.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:1295125\n  limitations: Valinomycin\
    \ alone does not inhibit in this assay. General energetic or viability effects\n\
    \    are not excluded. Proton-motive-force coupling is a model consistent with\
    \ the data, not measured proton\n    stoichiometry or inhibitor binding to SnatA;\
    \ Na/K results are data not shown.\n  nodes:\n  - node_id: fccp\n    label: FCCP\
    \ 10 ug/ml in AK430/pSA28\n    node_type: PERTURBATION\n  - node_id: ionophore-pair\n\
    \    label: Valinomycin plus nigericin in AK430/pSA28\n    node_type: PERTURBATION\n\
    \  - node_id: uptake\n    label: Cell-associated radioglycine uptake\n    node_type:\
    \ PROCESS\n  edges:\n  - edge_id: fccp-reduces-uptake\n    subject: fccp\n   \
    \ predicate: decreases\n    object: uptake\n    mechanism: FCCP reduces cellular\
    \ glycine accumulation; the experiment perturbs whole-cell energization,\n   \
    \   not only the SnatA molecule.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: doi:10.1093/jb/mvg021\n\
    \      source_url: https://doi.org/10.1093/jb/mvg021\n      snippet: a protein\
    \ of 216 amino acid residues\n      explanation: Figure 4A original plot, treated\
    \ pSA28 versus untreated pSA28.\n      cache_path: evidence/PF01914/akahane-2003.txt\n\
    \      cache_sha256: 576f405a8e8066e4323ddbf9d30f8ce3f2cb3a8f7d5221e42657942c712c7cce\n\
    \  - edge_id: ionophore-pair-reduces-uptake\n    subject: ionophore-pair\n   \
    \ predicate: decreases\n    object: uptake\n    mechanism: The combined ionophores\
    \ reduce uptake; the pair is one joint perturbation and neither component\n  \
    \    is represented as independently sufficient.\n    directness: INDIRECT\n \
    \   support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ doi:10.1093/jb/mvg021\n      source_url: https://doi.org/10.1093/jb/mvg021\n\
    \      snippet: a protein of 216 amino acid residues\n      explanation: Figure\
    \ 4B original plot; valinomycin alone is the separate noninhibitory comparison.\n\
    \      cache_path: evidence/PF01914/akahane-2003.txt\n      cache_sha256: 576f405a8e8066e4323ddbf9d30f8ce3f2cb3a8f7d5221e42657942c712c7cce\n\
    - graph_id: snata-strong-competition-2003\n  title: Six amino acids strongly reduce\
    \ SnatA-associated radioglycine uptake\n  scope: Selected strong competition assays\
    \ in AK430/pSA28, not independently measured uptake of each\n    competitor.\n\
    \  context: 'Table 2: 4 uM radioglycine, 830 uM competitor, 60 minutes; inhibition\
    \ percentages are normalized\n    as reported against the glycine competitor effect.'\n\
    \  family_mapping: Thermococcus sp. KS-1/JCM11816 SnatA BAC53669.1 from AB093585.1\
    \ equals UniParc UPI0000062A6D,\n    216 aa, PF01914 9-214. Q8J305 is retired,\
    \ not biologically absent. Genomic constructs contain full\n    SnatA plus flanking\
    \ DNA; no isolated-domain sufficiency.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:1295125\n\
    \  limitations: Competition alone does not establish that every competitor crosses\
    \ the membrane, direct\n    binding residues or a universal specificity order.\
    \ Weaker and zero effects are retained in the evidence\n    ledger; CycA/ACP assays\
    \ use different times and concentrations.\n  nodes:\n  - node_id: ala\n    label:\
    \ L-alanine competitor at 830 uM\n    node_type: PERTURBATION\n  - node_id: cys\n\
    \    label: L-cysteine competitor at 830 uM\n    node_type: PERTURBATION\n  -\
    \ node_id: thr\n    label: L-threonine competitor at 830 uM\n    node_type: PERTURBATION\n\
    \  - node_id: ser\n    label: L-serine competitor at 830 uM\n    node_type: PERTURBATION\n\
    \  - node_id: met\n    label: L-methionine competitor at 830 uM\n    node_type:\
    \ PERTURBATION\n  - node_id: trp\n    label: L-tryptophan competitor at 830 uM\n\
    \    node_type: PERTURBATION\n  - node_id: glycine-uptake\n    label: Radioglycine\
    \ uptake in AK430/pSA28\n    node_type: PROCESS\n  edges:\n  - edge_id: ala-reduces-glycine-uptake\n\
    \    subject: ala\n    predicate: decreases\n    object: glycine-uptake\n    mechanism:\
    \ L-alanine gives 84% reported normalized inhibition in this competition assay;\
    \ no separate\n      direct flux of this amino acid is asserted.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: doi:10.1093/jb/mvg021\n      source_url: https://doi.org/10.1093/jb/mvg021\n\
    \      snippet: a protein of 216 amino acid residues\n      explanation: Table\
    \ 2 original image, SnatA column and L-alanine row; caption defines assay timing\n\
    \        and normalization.\n      cache_path: evidence/PF01914/akahane-2003.txt\n\
    \      cache_sha256: 576f405a8e8066e4323ddbf9d30f8ce3f2cb3a8f7d5221e42657942c712c7cce\n\
    \  - edge_id: cys-reduces-glycine-uptake\n    subject: cys\n    predicate: decreases\n\
    \    object: glycine-uptake\n    mechanism: L-cysteine gives 95% reported normalized\
    \ inhibition in this competition assay; no separate\n      direct flux of this\
    \ amino acid is asserted.\n    directness: INDIRECT\n    support: OBSERVED\n \
    \   evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: doi:10.1093/jb/mvg021\n\
    \      source_url: https://doi.org/10.1093/jb/mvg021\n      snippet: a protein\
    \ of 216 amino acid residues\n      explanation: Table 2 original image, SnatA\
    \ column and L-cysteine row; caption defines assay timing\n        and normalization.\n\
    \      cache_path: evidence/PF01914/akahane-2003.txt\n      cache_sha256: 576f405a8e8066e4323ddbf9d30f8ce3f2cb3a8f7d5221e42657942c712c7cce\n\
    \  - edge_id: thr-reduces-glycine-uptake\n    subject: thr\n    predicate: decreases\n\
    \    object: glycine-uptake\n    mechanism: L-threonine gives 100% reported normalized\
    \ inhibition in this competition assay; no separate\n      direct flux of this\
    \ amino acid is asserted.\n    directness: INDIRECT\n    support: OBSERVED\n \
    \   evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: doi:10.1093/jb/mvg021\n\
    \      source_url: https://doi.org/10.1093/jb/mvg021\n      snippet: a protein\
    \ of 216 amino acid residues\n      explanation: Table 2 original image, SnatA\
    \ column and L-threonine row; caption defines assay timing\n        and normalization.\n\
    \      cache_path: evidence/PF01914/akahane-2003.txt\n      cache_sha256: 576f405a8e8066e4323ddbf9d30f8ce3f2cb3a8f7d5221e42657942c712c7cce\n\
    \  - edge_id: ser-reduces-glycine-uptake\n    subject: ser\n    predicate: decreases\n\
    \    object: glycine-uptake\n    mechanism: L-serine gives 90% reported normalized\
    \ inhibition in this competition assay; no separate\n      direct flux of this\
    \ amino acid is asserted.\n    directness: INDIRECT\n    support: OBSERVED\n \
    \   evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: doi:10.1093/jb/mvg021\n\
    \      source_url: https://doi.org/10.1093/jb/mvg021\n      snippet: a protein\
    \ of 216 amino acid residues\n      explanation: Table 2 original image, SnatA\
    \ column and L-serine row; caption defines assay timing\n        and normalization.\n\
    \      cache_path: evidence/PF01914/akahane-2003.txt\n      cache_sha256: 576f405a8e8066e4323ddbf9d30f8ce3f2cb3a8f7d5221e42657942c712c7cce\n\
    \  - edge_id: met-reduces-glycine-uptake\n    subject: met\n    predicate: decreases\n\
    \    object: glycine-uptake\n    mechanism: L-methionine gives 65% reported normalized\
    \ inhibition in this competition assay; no separate\n      direct flux of this\
    \ amino acid is asserted.\n    directness: INDIRECT\n    support: OBSERVED\n \
    \   evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: doi:10.1093/jb/mvg021\n\
    \      source_url: https://doi.org/10.1093/jb/mvg021\n      snippet: a protein\
    \ of 216 amino acid residues\n      explanation: Table 2 original image, SnatA\
    \ column and L-methionine row; caption defines assay timing\n        and normalization.\n\
    \      cache_path: evidence/PF01914/akahane-2003.txt\n      cache_sha256: 576f405a8e8066e4323ddbf9d30f8ce3f2cb3a8f7d5221e42657942c712c7cce\n\
    \  - edge_id: trp-reduces-glycine-uptake\n    subject: trp\n    predicate: decreases\n\
    \    object: glycine-uptake\n    mechanism: L-tryptophan gives 60% reported normalized\
    \ inhibition in this competition assay; no separate\n      direct flux of this\
    \ amino acid is asserted.\n    directness: INDIRECT\n    support: OBSERVED\n \
    \   evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: doi:10.1093/jb/mvg021\n\
    \      source_url: https://doi.org/10.1093/jb/mvg021\n      snippet: a protein\
    \ of 216 amino acid residues\n      explanation: Table 2 original image, SnatA\
    \ column and L-tryptophan row; caption defines assay timing\n        and normalization.\n\
    \      cache_path: evidence/PF01914/akahane-2003.txt\n      cache_sha256: 576f405a8e8066e4323ddbf9d30f8ce3f2cb3a8f7d5221e42657942c712c7cce\n\
    - graph_id: snata-serine-growth-2003\n  title: SnatA construct suppresses WAT9\
    \ growth on serine\n  scope: WAT9 sstT-defective E. coli expressing pSA28 versus\
    \ empty pUC119; not AK430 or native KS-1.\n  context: 'Table 3: minimal agar,\
    \ L-serine 5 mg/ml, 24 hours at 37 C. Both constructs grow with lactose\n    40\
    \ mM.'\n  family_mapping: Thermococcus sp. KS-1/JCM11816 SnatA BAC53669.1 from\
    \ AB093585.1 equals UniParc UPI0000062A6D,\n    216 aa, PF01914 9-214. Q8J305\
    \ is retired, not biologically absent. Genomic constructs contain full\n    SnatA\
    \ plus flanking DNA; no isolated-domain sufficiency.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:1295125\n  limitations: Qualitative colony growth is not a\
    \ direct serine-flux measurement or proof of the proposed\n    feedback-inhibition\
    \ relay. W3133-2 and WAT9 expressing sstT are separate controls; lactose growth\n\
    \    limits a nonspecific growth-defect explanation.\n  nodes:\n  - node_id: snata-expression\n\
    \    label: WAT9 carrying pSA28 relative to empty pUC119\n    node_type: PERTURBATION\n\
    \  - node_id: serine-growth\n    label: Colony growth on L-serine medium\n   \
    \ node_type: PHENOTYPE\n  edges:\n  - edge_id: snata-reduces-serine-growth\n \
    \   subject: snata-expression\n    predicate: decreases\n    object: serine-growth\n\
    \    mechanism: The genomic snatA construct changes the serine-medium score from\
    \ growth to no growth; biochemical\n      accumulation and downstream feedback\
    \ are not directly measured.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: doi:10.1093/jb/mvg021\n\
    \      source_url: https://doi.org/10.1093/jb/mvg021\n      snippet: a protein\
    \ of 216 amino acid residues\n      explanation: Table 3 original image, WAT9/pUC119\
    \ and WAT9/pSA28 rows, serine and lactose controls.\n      cache_path: evidence/PF01914/akahane-2003.txt\n\
    \      cache_sha256: 576f405a8e8066e4323ddbf9d30f8ce3f2cb3a8f7d5221e42657942c712c7cce\n\
    - graph_id: marc-selected-clone-growth-2025\n  title: Selected MarC-variant clones\
    \ improve limiting-threonine growth\n  scope: Bubnov2025 four independently selected\
    \ B1950-derived clones, not each purified variant or a family-wide\n    allele\
    \ effect.\n  context: B1950 is MG1655 delta-thrBC/delta-sstT/delta-tdcBCDE::neo/delta-thrP/delta-brnQ/delta-livKHMGF/delta-yjeM/delta-sdaC/delta-ydgI/delta-ychE;\n\
    \    clones are compared with this parental background. Figure 2A spot growth\
    \ at 0.4/0.8 mM threonine,\n    with 4 mM as permissive comparison.\n  family_mapping:\
    \ E. coli K-12 MarC P0AEY1/b1529/JW1522 sequence version 1, 221 aa, PF01914 5-217.\
    \ This\n    is reference mapping, not independent sequencing of historical strains\
    \ or proof of isolated-domain\n    function.\n  scope_status: PHENOTYPIC\n  taxon:\
    \ NCBITaxon:83333\n  limitations: Selected clones are not independently reconstructed\
    \ single-allele replacements. B2059 also\n    carries ydbD I155I and insO R20W;\
    \ common mutations were filtered in variant calling. S140SS is a serine\n    insertion,\
    \ not a substitution. No purified transport, residue-level binding mechanism or\
    \ WT physiological\n    specificity is established. Printed glucose units differ\
    \ between Methods (0.2% versus 0.2 g/L).\n  nodes:\n  - node_id: b2058\n    label:\
    \ B2058 MarC S140SS serine insertion relative to B1950\n    node_type: PERTURBATION\n\
    \  - node_id: b2059\n    label: B2059 MarC V145E plus ydbD I155I and insO R20W\
    \ relative to B1950\n    node_type: PERTURBATION\n  - node_id: b2063\n    label:\
    \ B2063 MarC L10Q relative to B1950\n    node_type: PERTURBATION\n  - node_id:\
    \ b2068\n    label: B2068 MarC G11E relative to B1950\n    node_type: PERTURBATION\n\
    \  - node_id: growth\n    label: Spot growth at limiting threonine\n    node_type:\
    \ PHENOTYPE\n  edges:\n  - edge_id: b2058-increases-growth\n    subject: b2058\n\
    \    predicate: increases\n    object: growth\n    mechanism: B2058 MarC S140SS\
    \ serine insertion shows improved spot growth versus B1950 under the limiting-threonine\n\
    \      conditions; the whole selected clone is the supported perturbation.\n \
    \   directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:40248429\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12003319/\n\
    \      snippet: marC V145E\n      explanation: Figure 2A original spots and Tables\
    \ 1/3 for clone genotypes; no isogenic allele-swap\n        rescue assumed.\n\
    \      cache_path: evidence/PF01914/bubnov-2025-figure1-corrected.txt\n      cache_sha256:\
    \ 2f2f41f6b16aa17eea7dd32a2fb38bf239350955318992f62832b8371f48e348\n  - edge_id:\
    \ b2059-increases-growth\n    subject: b2059\n    predicate: increases\n    object:\
    \ growth\n    mechanism: B2059 MarC V145E plus ydbD I155I and insO R20W shows\
    \ improved spot growth versus B1950\n      under the limiting-threonine conditions;\
    \ the whole selected clone is the supported perturbation.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:40248429\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12003319/\n\
    \      snippet: marC V145E\n      explanation: Figure 2A original spots and Tables\
    \ 1/3 for clone genotypes; no isogenic allele-swap\n        rescue assumed.\n\
    \      cache_path: evidence/PF01914/bubnov-2025-figure1-corrected.txt\n      cache_sha256:\
    \ 2f2f41f6b16aa17eea7dd32a2fb38bf239350955318992f62832b8371f48e348\n  - edge_id:\
    \ b2063-increases-growth\n    subject: b2063\n    predicate: increases\n    object:\
    \ growth\n    mechanism: B2063 MarC L10Q shows improved spot growth versus B1950\
    \ under the limiting-threonine conditions;\n      the whole selected clone is\
    \ the supported perturbation.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:40248429\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12003319/\n      snippet:\
    \ marC V145E\n      explanation: Figure 2A original spots and Tables 1/3 for clone\
    \ genotypes; no isogenic allele-swap\n        rescue assumed.\n      cache_path:\
    \ evidence/PF01914/bubnov-2025-figure1-corrected.txt\n      cache_sha256: 2f2f41f6b16aa17eea7dd32a2fb38bf239350955318992f62832b8371f48e348\n\
    \  - edge_id: b2068-increases-growth\n    subject: b2068\n    predicate: increases\n\
    \    object: growth\n    mechanism: B2068 MarC G11E shows improved spot growth\
    \ versus B1950 under the limiting-threonine conditions;\n      the whole selected\
    \ clone is the supported perturbation.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:40248429\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12003319/\n      snippet:\
    \ marC V145E\n      explanation: Figure 2A original spots and Tables 1/3 for clone\
    \ genotypes; no isogenic allele-swap\n        rescue assumed.\n      cache_path:\
    \ evidence/PF01914/bubnov-2025-figure1-corrected.txt\n      cache_sha256: 2f2f41f6b16aa17eea7dd32a2fb38bf239350955318992f62832b8371f48e348\n\
    - graph_id: marc-selected-clone-uptake-2025\n  title: Selected MarC-variant clones\
    \ increase cellular threonine uptake\n  scope: Bubnov2025 cellular uptake in four\
    \ B1950-derived selected clones, separate from the growth assay.\n  context: 'B1950\
    \ is MG1655 delta-thrBC/delta-sstT/delta-tdcBCDE::neo/delta-thrP/delta-brnQ/delta-livKHMGF/delta-yjeM/delta-sdaC/delta-ydgI/delta-ychE;\n\
    \    clones are compared with this parental background. Figure 2B: 2.5 mM 14C-threonine,\
    \ one minute, 37\n    C, dry-cell-weight normalization, three biological replicates\
    \ with SD.'\n  family_mapping: E. coli K-12 MarC P0AEY1/b1529/JW1522 sequence\
    \ version 1, 221 aa, PF01914 5-217. This\n    is reference mapping, not independent\
    \ sequencing of historical strains or proof of isolated-domain\n    function.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:83333\n  limitations: Selected\
    \ clones are not independently reconstructed single-allele replacements. B2059\
    \ also\n    carries ydbD I155I and insO R20W; common mutations were filtered in\
    \ variant calling. S140SS is a serine\n    insertion, not a substitution. No purified\
    \ transport, residue-level binding mechanism or WT physiological\n    specificity\
    \ is established. Printed glucose units differ between Methods (0.2% versus 0.2\
    \ g/L). Figure\n    2B uses unequal-variance two-sided t-tests; no exact bar-height\
    \ values are invented.\n  nodes:\n  - node_id: b2058\n    label: B2058 MarC S140SS\
    \ serine insertion relative to B1950\n    node_type: PERTURBATION\n  - node_id:\
    \ b2059\n    label: B2059 MarC V145E plus ydbD I155I and insO R20W relative to\
    \ B1950\n    node_type: PERTURBATION\n  - node_id: b2063\n    label: B2063 MarC\
    \ L10Q relative to B1950\n    node_type: PERTURBATION\n  - node_id: b2068\n  \
    \  label: B2068 MarC G11E relative to B1950\n    node_type: PERTURBATION\n  -\
    \ node_id: uptake\n    label: One-minute cellular 14C-threonine uptake\n    node_type:\
    \ PROCESS\n  edges:\n  - edge_id: b2058-increases-uptake\n    subject: b2058\n\
    \    predicate: increases\n    object: uptake\n    mechanism: B2058 MarC S140SS\
    \ serine insertion has a higher measured uptake rate than B1950. Clone-level\n\
    \      uptake does not by itself isolate the altered residue's transport chemistry.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:40248429\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12003319/\n\
    \      snippet: marC V145E\n      explanation: Figure 2B original plot, uptake\
    \ Methods 2.6 and Table 3; all four MarC clone comparisons\n        retain their\
    \ reported direction.\n      cache_path: evidence/PF01914/bubnov-2025-figure1-corrected.txt\n\
    \      cache_sha256: 2f2f41f6b16aa17eea7dd32a2fb38bf239350955318992f62832b8371f48e348\n\
    \  - edge_id: b2059-increases-uptake\n    subject: b2059\n    predicate: increases\n\
    \    object: uptake\n    mechanism: B2059 MarC V145E plus ydbD I155I and insO\
    \ R20W has a higher measured uptake rate than B1950.\n      Clone-level uptake\
    \ does not by itself isolate the altered residue's transport chemistry.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:40248429\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12003319/\n\
    \      snippet: marC V145E\n      explanation: Figure 2B original plot, uptake\
    \ Methods 2.6 and Table 3; all four MarC clone comparisons\n        retain their\
    \ reported direction.\n      cache_path: evidence/PF01914/bubnov-2025-figure1-corrected.txt\n\
    \      cache_sha256: 2f2f41f6b16aa17eea7dd32a2fb38bf239350955318992f62832b8371f48e348\n\
    \  - edge_id: b2063-increases-uptake\n    subject: b2063\n    predicate: increases\n\
    \    object: uptake\n    mechanism: B2063 MarC L10Q has a higher measured uptake\
    \ rate than B1950. Clone-level uptake does not\n      by itself isolate the altered\
    \ residue's transport chemistry.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:40248429\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12003319/\n      snippet:\
    \ marC V145E\n      explanation: Figure 2B original plot, uptake Methods 2.6 and\
    \ Table 3; all four MarC clone comparisons\n        retain their reported direction.\n\
    \      cache_path: evidence/PF01914/bubnov-2025-figure1-corrected.txt\n      cache_sha256:\
    \ 2f2f41f6b16aa17eea7dd32a2fb38bf239350955318992f62832b8371f48e348\n  - edge_id:\
    \ b2068-increases-uptake\n    subject: b2068\n    predicate: increases\n    object:\
    \ uptake\n    mechanism: B2068 MarC G11E has a higher measured uptake rate than\
    \ B1950. Clone-level uptake does not\n      by itself isolate the altered residue's\
    \ transport chemistry.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:40248429\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC12003319/\n      snippet: marC V145E\n\
    \      explanation: Figure 2B original plot, uptake Methods 2.6 and Table 3; all\
    \ four MarC clone comparisons\n        retain their reported direction.\n    \
    \  cache_path: evidence/PF01914/bubnov-2025-figure1-corrected.txt\n      cache_sha256:\
    \ 2f2f41f6b16aa17eea7dd32a2fb38bf239350955318992f62832b8371f48e348\n- graph_id:\
    \ yche-genomic-insert-growth-2025\n  title: YchE-containing genomic insert improves\
    \ B1895 growth\n  scope: Bubnov2025 pBRychE versus empty pBR322 in auxotrophic\
    \ B1895, not the B1950 clone background.\n  context: B1895 MG1655 delta-thrBC/delta-sstT/delta-tdcBCDE::neo/delta-thrP/delta-brnQ/delta-livKHMGF::cat.\n\
    \    Figure 1A spots at 1.25 mM threonine.\n  family_mapping: K-12 YchE P25743/b1242/JW1229\
    \ sequence version 2, 215 aa, PF01914 9-210. Table 2 pBRychE\n    insert U00096.3\
    \ 1297744-1301027 contains genomic flanks, not only the isolated domain.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:83333\n  limitations: Figure 1C uptake in a different\
    \ prototrophic host B2394 at 800 uM threonine is not significantly\n    increased\
    \ (p=0.38). Growth rescue is not an observed YchE transport edge. The shared glucose-unit\n\
    \    discrepancy remains open; combined deletion effects are not assigned to YchE\
    \ alone.\n  nodes:\n  - node_id: pbr-yche\n    label: B1895 carrying pBRychE relative\
    \ to empty pBR322\n    node_type: PERTURBATION\n  - node_id: growth\n    label:\
    \ Spot growth at 1.25 mM threonine\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ yche-insert-increases-growth\n    subject: pbr-yche\n    predicate: increases\n\
    \    object: growth\n    mechanism: The genomic insert improves growth in this\
    \ auxotrophic host; indirect metabolic and flanking-sequence\n      effects are\
    \ not excluded.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:40248429\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC12003319/\n      snippet: marC V145E\n\
    \      explanation: Figure 1A original spots and Table 2 insert; Figure 1C different-host\
    \ nonsignificant\n        uptake is retained as a limit.\n      cache_path: evidence/PF01914/bubnov-2025-figure1-corrected.txt\n\
    \      cache_sha256: 2f2f41f6b16aa17eea7dd32a2fb38bf239350955318992f62832b8371f48e348\n\
    - graph_id: marc-reconstruction-glucose-2011\n  title: Reported marC reconstruction\
    \ has condition-dependent glucose growth effects\n  scope: Minty2011 reported\
    \ marC::kan reconstruction versus EcNR1; genotype ambiguity is part of the scope,\n\
    \    not an assumed clean isogenic deletion.\n  context: NG50 minimal medium with\
    \ glucose 50 g/L and biotin 0.25 mg/L, 30 C. Separately 0% and 0.5%\n    (w/v)\
    \ isobutanol; OD600 time courses over 48 hours.\n  family_mapping: E. coli K-12\
    \ MarC P0AEY1/b1529/JW1522 sequence version 1, 221 aa, PF01914 5-217. This\n \
    \   is reference mapping, not independent sequencing of historical strains or\
    \ proof of isolated-domain\n    function.\n  scope_status: PHENOTYPIC\n  taxon:\
    \ NCBITaxon:83333\n  limitations: Table 3 caption calls the reconstruction EcNR1-derived,\
    \ but Results/Methods construct it\n    in EcHW24 or progeny, an EcNR1 MutS-negative\
    \ derivative. The comparator is EcNR1, so a MutS/background\n    confound remains.\
    \ Uncertainty type and row-level significance are unresolved. Deletion only approximates\n\
    \    IS1/IS5 insertions; adjacent marRAB changes and direct solvent transport\
    \ are unmeasured.\n  nodes:\n  - node_id: no-solvent\n    label: Reported marC::kan\
    \ strain versus EcNR1 in glucose, 0% isobutanol\n    node_type: PERTURBATION\n\
    \  - node_id: isobutanol\n    label: Reported marC::kan strain versus EcNR1 in\
    \ glucose, 0.5% isobutanol\n    node_type: PERTURBATION\n  - node_id: no-solvent-growth-value\n\
    \    label: 0% isobutanol maximum specific growth rate\n    node_type: PHENOTYPE\n\
    \  - node_id: no-solvent-maximum-od-value\n    label: 0% isobutanol maximum OD600\n\
    \    node_type: PHENOTYPE\n  - node_id: isobutanol-growth-value\n    label: 0.5%\
    \ isobutanol maximum specific growth rate\n    node_type: PHENOTYPE\n  - node_id:\
    \ isobutanol-maximum-od-value\n    label: 0.5% isobutanol maximum OD600\n    node_type:\
    \ PHENOTYPE\n  edges:\n  - edge_id: no-solvent-growth\n    subject: no-solvent\n\
    \    predicate: decreases\n    object: no-solvent-growth-value\n    mechanism:\
    \ The reported marC::kan reconstruction shows -3.2% maximum specific growth-rate\
    \ change versus\n      EcNR1 in glucose medium without isobutanol; possible background\
    \ differences prevent assigning this\n      solely to MarC loss.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:21435272\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3071312/\n\
    \      snippet: approximated the effect of transposon insertions by knocking out\n\
    \      explanation: Table 3 marC::kan glucose row, 0% isobutanol column; phenotype,\
    \ base-strain and knockout\n        Methods.\n      cache_path: evidence/PF01914/minty-2011.txt\n\
    \      cache_sha256: 21198e46f0dad3f70e389e7c57e35cff40a36df16da5084d45f1e97df78ba854\n\
    \  - edge_id: no-solvent-maximum-od\n    subject: no-solvent\n    predicate: decreases\n\
    \    object: no-solvent-maximum-od-value\n    mechanism: The reported marC::kan\
    \ reconstruction shows -7.8% maximum OD600 change versus EcNR1 in\n      glucose\
    \ medium without isobutanol; possible background differences prevent assigning\
    \ this solely\n      to MarC loss.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:21435272\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3071312/\n      snippet:\
    \ approximated the effect of transposon insertions by knocking out\n      explanation:\
    \ Table 3 marC::kan glucose row, 0% isobutanol column; phenotype, base-strain\
    \ and knockout\n        Methods.\n      cache_path: evidence/PF01914/minty-2011.txt\n\
    \      cache_sha256: 21198e46f0dad3f70e389e7c57e35cff40a36df16da5084d45f1e97df78ba854\n\
    \  - edge_id: isobutanol-growth\n    subject: isobutanol\n    predicate: increases\n\
    \    object: isobutanol-growth-value\n    mechanism: The reported marC::kan reconstruction\
    \ shows +20% maximum specific growth-rate change versus\n      EcNR1 in glucose\
    \ medium with 0.5% (w/v) isobutanol; possible background differences prevent assigning\n\
    \      this solely to MarC loss.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:21435272\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3071312/\n      snippet:\
    \ approximated the effect of transposon insertions by knocking out\n      explanation:\
    \ Table 3 marC::kan glucose row, 0.5% isobutanol column; phenotype, base-strain\
    \ and knockout\n        Methods.\n      cache_path: evidence/PF01914/minty-2011.txt\n\
    \      cache_sha256: 21198e46f0dad3f70e389e7c57e35cff40a36df16da5084d45f1e97df78ba854\n\
    \  - edge_id: isobutanol-maximum-od\n    subject: isobutanol\n    predicate: increases\n\
    \    object: isobutanol-maximum-od-value\n    mechanism: The reported marC::kan\
    \ reconstruction shows +40% maximum OD600 change versus EcNR1 in glucose\n   \
    \   medium with 0.5% (w/v) isobutanol; possible background differences prevent\
    \ assigning this solely\n      to MarC loss.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:21435272\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3071312/\n      snippet:\
    \ approximated the effect of transposon insertions by knocking out\n      explanation:\
    \ Table 3 marC::kan glucose row, 0.5% isobutanol column; phenotype, base-strain\
    \ and knockout\n        Methods.\n      cache_path: evidence/PF01914/minty-2011.txt\n\
    \      cache_sha256: 21198e46f0dad3f70e389e7c57e35cff40a36df16da5084d45f1e97df78ba854\n\
    - graph_id: marc-reconstruction-xylose-2011\n  title: Reported marC reconstruction\
    \ has condition-dependent xylose growth effects\n  scope: Minty2011 reported marC::kan\
    \ reconstruction versus EcNR1; genotype ambiguity is part of the scope,\n    not\
    \ an assumed clean isogenic deletion.\n  context: NX50 minimal medium with xylose\
    \ 50 g/L and biotin 0.25 mg/L, 30 C. Separately 0% and 0.5% (w/v)\n    isobutanol;\
    \ OD600 time courses over 48 hours.\n  family_mapping: E. coli K-12 MarC P0AEY1/b1529/JW1522\
    \ sequence version 1, 221 aa, PF01914 5-217. This\n    is reference mapping, not\
    \ independent sequencing of historical strains or proof of isolated-domain\n \
    \   function.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:83333\n  limitations:\
    \ Table 3 caption calls the reconstruction EcNR1-derived, but Results/Methods\
    \ construct it\n    in EcHW24 or progeny, an EcNR1 MutS-negative derivative. The\
    \ comparator is EcNR1, so a MutS/background\n    confound remains. Uncertainty\
    \ type and row-level significance are unresolved. Deletion only approximates\n\
    \    IS1/IS5 insertions; adjacent marRAB changes and direct solvent transport\
    \ are unmeasured.\n  nodes:\n  - node_id: no-solvent\n    label: Reported marC::kan\
    \ strain versus EcNR1 in xylose, 0% isobutanol\n    node_type: PERTURBATION\n\
    \  - node_id: isobutanol\n    label: Reported marC::kan strain versus EcNR1 in\
    \ xylose, 0.5% isobutanol\n    node_type: PERTURBATION\n  - node_id: no-solvent-growth-value\n\
    \    label: 0% isobutanol maximum specific growth rate\n    node_type: PHENOTYPE\n\
    \  - node_id: no-solvent-maximum-od-value\n    label: 0% isobutanol maximum OD600\n\
    \    node_type: PHENOTYPE\n  - node_id: isobutanol-growth-value\n    label: 0.5%\
    \ isobutanol maximum specific growth rate\n    node_type: PHENOTYPE\n  - node_id:\
    \ isobutanol-maximum-od-value\n    label: 0.5% isobutanol maximum OD600\n    node_type:\
    \ PHENOTYPE\n  edges:\n  - edge_id: no-solvent-growth\n    subject: no-solvent\n\
    \    predicate: decreases\n    object: no-solvent-growth-value\n    mechanism:\
    \ The reported marC::kan reconstruction shows -5% maximum specific growth-rate\
    \ change versus\n      EcNR1 in xylose medium without isobutanol; possible background\
    \ differences prevent assigning this\n      solely to MarC loss.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:21435272\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3071312/\n\
    \      snippet: approximated the effect of transposon insertions by knocking out\n\
    \      explanation: Table 3 marC::kan xylose row, 0% isobutanol column; phenotype,\
    \ base-strain and knockout\n        Methods.\n      cache_path: evidence/PF01914/minty-2011.txt\n\
    \      cache_sha256: 21198e46f0dad3f70e389e7c57e35cff40a36df16da5084d45f1e97df78ba854\n\
    \  - edge_id: no-solvent-maximum-od\n    subject: no-solvent\n    predicate: decreases\n\
    \    object: no-solvent-maximum-od-value\n    mechanism: The reported marC::kan\
    \ reconstruction shows -2.4% maximum OD600 change versus EcNR1 in\n      xylose\
    \ medium without isobutanol; possible background differences prevent assigning\
    \ this solely\n      to MarC loss.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:21435272\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3071312/\n      snippet:\
    \ approximated the effect of transposon insertions by knocking out\n      explanation:\
    \ Table 3 marC::kan xylose row, 0% isobutanol column; phenotype, base-strain and\
    \ knockout\n        Methods.\n      cache_path: evidence/PF01914/minty-2011.txt\n\
    \      cache_sha256: 21198e46f0dad3f70e389e7c57e35cff40a36df16da5084d45f1e97df78ba854\n\
    \  - edge_id: isobutanol-growth\n    subject: isobutanol\n    predicate: increases\n\
    \    object: isobutanol-growth-value\n    mechanism: The reported marC::kan reconstruction\
    \ shows +39% maximum specific growth-rate change versus\n      EcNR1 in xylose\
    \ medium with 0.5% (w/v) isobutanol; possible background differences prevent assigning\n\
    \      this solely to MarC loss.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:21435272\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3071312/\n      snippet:\
    \ approximated the effect of transposon insertions by knocking out\n      explanation:\
    \ Table 3 marC::kan xylose row, 0.5% isobutanol column; phenotype, base-strain\
    \ and knockout\n        Methods.\n      cache_path: evidence/PF01914/minty-2011.txt\n\
    \      cache_sha256: 21198e46f0dad3f70e389e7c57e35cff40a36df16da5084d45f1e97df78ba854\n\
    \  - edge_id: isobutanol-maximum-od\n    subject: isobutanol\n    predicate: increases\n\
    \    object: isobutanol-maximum-od-value\n    mechanism: The reported marC::kan\
    \ reconstruction shows +7.6% maximum OD600 change versus EcNR1 in\n      xylose\
    \ medium with 0.5% (w/v) isobutanol; possible background differences prevent assigning\
    \ this\n      solely to MarC loss.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:21435272\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3071312/\n      snippet:\
    \ approximated the effect of transposon insertions by knocking out\n      explanation:\
    \ Table 3 marC::kan xylose row, 0.5% isobutanol column; phenotype, base-strain\
    \ and knockout\n        Methods.\n      cache_path: evidence/PF01914/minty-2011.txt\n\
    \      cache_sha256: 21198e46f0dad3f70e389e7c57e35cff40a36df16da5084d45f1e97df78ba854\n\
    - graph_id: marc-solvent-growth-2020\n  title: MarC deletion improves growth under\
    \ two solvent challenges\n  scope: Babel2020 MG1655-derived deletion background\
    \ compared with the study's initial MG1655; not all\n    evolved mutations or\
    \ a direct efflux assay.\n  context: Figures 4/5, 37 C, M9 glucose 5 g/L. Isoprenol\
    \ 50 mM and butanol 5 g/L are separate conditions;\n    relative fitness is growth\
    \ rate divided by the reference rate in that condition.\n  family_mapping: E.\
    \ coli K-12 MarC P0AEY1/b1529/JW1522 sequence version 1, 221 aa, PF01914 5-217.\
    \ This\n    is reference mapping, not independent sequencing of historical strains\
    \ or proof of isolated-domain\n    function. The CGSC6300-derived experimental\
    \ stock has restored gatC, functional glrR and REP321j variation;\n    it is not\
    \ assumed identical to the canonical reference.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:83333\n  limitations: Strain 953 is delta-marC750::kanR; 960\
    \ expresses the M35stop fragment and 1087 carries\n    empty vector in the deletion\
    \ background. Fragment expression adds no significant benefit and is not\n   \
    \ wild-type complementation. Three biological replicates/SD; no exact bar estimates.\
    \ Vanillin does not\n    show a strong benefit. Transport chemistry and domain/residue\
    \ sufficiency remain unresolved.\n  nodes:\n  - node_id: deletion-isoprenol\n\
    \    label: MarC deletion background under 50 mM isoprenol\n    node_type: PERTURBATION\n\
    \  - node_id: deletion-butanol\n    label: MarC deletion under 5 g/L butanol\n\
    \    node_type: PERTURBATION\n  - node_id: isoprenol-growth\n    label: Relative\
    \ growth rate under isoprenol\n    node_type: PHENOTYPE\n  - node_id: butanol-growth\n\
    \    label: Relative growth rate under butanol\n    node_type: PHENOTYPE\n  edges:\n\
    \  - edge_id: deletion-improves-isoprenol-growth\n    subject: deletion-isoprenol\n\
    \    predicate: increases\n    object: isoprenol-growth\n    mechanism: The deletion\
    \ condition has greater relative growth than the initial MG1655 reference under\n\
    \      isoprenol; the truncated-protein comparison does not demonstrate a native\
    \ rescue.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:33292484\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC7653855/\n      snippet: did not significantly\
    \ change the fitness compared to the knock-out\n      explanation: Figure 4 original\
    \ plot, MarC Results and strain Table 4; M35stop versus deletion remains\n   \
    \     a non-additive comparison.\n      cache_path: evidence/PF01914/babel-2020.txt\n\
    \      cache_sha256: 64ef3a358507e182807f7b1bdc126b1f7f45eacf3b77d91a4f9ed50e169a1536\n\
    \  - edge_id: deletion-improves-butanol-growth\n    subject: deletion-butanol\n\
    \    predicate: increases\n    object: butanol-growth\n    mechanism: The deletion\
    \ strain has improved relative growth under butanol; the result is not generalized\n\
    \      to every solvent or to direct transport.\n    directness: INDIRECT\n  \
    \  support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:33292484\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7653855/\n\
    \      snippet: did not significantly change the fitness compared to the knock-out\n\
    \      explanation: Figure 5 original plot, butanol condition and growth Methods.\n\
    \      cache_path: evidence/PF01914/babel-2020.txt\n      cache_sha256: 64ef3a358507e182807f7b1bdc126b1f7f45eacf3b77d91a4f9ed50e169a1536\n\
    - graph_id: marc-top10-mic-2018\n  title: ATCC25922 MarC construct modestly increases\
    \ TOP10 MICs\n  scope: Gingras2018 PCR-subcloned ATCC25922 marC genomic insert\
    \ expressed in TOP10, compared with TOP10/pFF6;\n    not the original enrichment\
    \ fragment.\n  context: Table 2 triplicate MIC measurements, ug/ml. pFF6 is a\
    \ nonsuicidal unrelated-insert control\n    because empty pZErO-2 is suicidal;\
    \ antisense-marC controls remain at baseline.\n  family_mapping: ATCC25922 DR76_3329/AIL17056.1\
    \ equals UniParc UPI00000DEBB0, 221 aa, PF01914 5-217;\n    N36S relative to K-12\
    \ P0AEY1. Table S2 primer mapping predicts CP009072.1 insert 3541797-3542673 including\n\
    \    the full CDS and upstream DNA, not independent sequencing of the historical\
    \ plasmid.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:562\n  limitations:\
    \ Changes are about one twofold dilution and may lie within technical variability;\
    \ not clinical\n    resistance or direct efflux. pFF6 is not an identical empty\
    \ vector. ATCC25922 recipient has no ceftriaxone\n    increase and McDermott2008\
    \ AG100 tests were negative. Original enrichment interval 3540651-3542008\n  \
    \  ends at the MarC start and remains unresolved; no enrichment-fragment edge\
    \ is asserted.\n  nodes:\n  - node_id: marc-construct\n    label: TOP10/pZErO-2-marC\
    \ relative to TOP10/pFF6\n    node_type: PERTURBATION\n  - node_id: cro\n    label:\
    \ Ceftriaxone MIC in TOP10\n    node_type: PHENOTYPE\n  - node_id: gen\n    label:\
    \ Gentamicin MIC in TOP10\n    node_type: PHENOTYPE\n  - node_id: lev\n    label:\
    \ Levofloxacin MIC in TOP10\n    node_type: PHENOTYPE\n  - node_id: tet\n    label:\
    \ Tetracycline MIC in TOP10\n    node_type: PHENOTYPE\n  - node_id: tmp\n    label:\
    \ Trimethoprim MIC in TOP10\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ cro-mic-increase\n    subject: marc-construct\n    predicate: increases\n  \
    \  object: cro\n    mechanism: Ceftriaxone MIC is reported as 0.13 to 0.25 ug/ml\
    \ in this construct/host comparison; the\n      modest shift is not an independently\
    \ established clinical resistance category.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:29319470\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5857375/\n      snippet:\
    \ marC\n      explanation: Table 2 TOP10/pFF6 and marC rows, Ceftriaxone column;\
    \ antisense control and validation\n        Methods; Table S2 clone primers.\n\
    \      cache_path: evidence/PF01914/gingras-2018.txt\n      cache_sha256: 77a82410ca3790377b21059eadeb40eba8a319afc681c1c7d4b438535c9eeaa2\n\
    \  - edge_id: gen-mic-increase\n    subject: marc-construct\n    predicate: increases\n\
    \    object: gen\n    mechanism: Gentamicin MIC is reported as 0.50 to 1.00 ug/ml\
    \ in this construct/host comparison; the\n      modest shift is not an independently\
    \ established clinical resistance category.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:29319470\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5857375/\n      snippet:\
    \ marC\n      explanation: Table 2 TOP10/pFF6 and marC rows, Gentamicin column;\
    \ antisense control and validation\n        Methods; Table S2 clone primers.\n\
    \      cache_path: evidence/PF01914/gingras-2018.txt\n      cache_sha256: 77a82410ca3790377b21059eadeb40eba8a319afc681c1c7d4b438535c9eeaa2\n\
    \  - edge_id: lev-mic-increase\n    subject: marc-construct\n    predicate: increases\n\
    \    object: lev\n    mechanism: Levofloxacin MIC is reported as 0.016 to 0.031\
    \ ug/ml in this construct/host comparison;\n      the modest shift is not an independently\
    \ established clinical resistance category.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:29319470\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5857375/\n      snippet:\
    \ marC\n      explanation: Table 2 TOP10/pFF6 and marC rows, Levofloxacin column;\
    \ antisense control and validation\n        Methods; Table S2 clone primers.\n\
    \      cache_path: evidence/PF01914/gingras-2018.txt\n      cache_sha256: 77a82410ca3790377b21059eadeb40eba8a319afc681c1c7d4b438535c9eeaa2\n\
    \  - edge_id: tet-mic-increase\n    subject: marc-construct\n    predicate: increases\n\
    \    object: tet\n    mechanism: Tetracycline MIC is reported as 1.00 to 2.00\
    \ ug/ml in this construct/host comparison; the\n      modest shift is not an independently\
    \ established clinical resistance category.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:29319470\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5857375/\n      snippet:\
    \ marC\n      explanation: Table 2 TOP10/pFF6 and marC rows, Tetracycline column;\
    \ antisense control and validation\n        Methods; Table S2 clone primers.\n\
    \      cache_path: evidence/PF01914/gingras-2018.txt\n      cache_sha256: 77a82410ca3790377b21059eadeb40eba8a319afc681c1c7d4b438535c9eeaa2\n\
    \  - edge_id: tmp-mic-increase\n    subject: marc-construct\n    predicate: increases\n\
    \    object: tmp\n    mechanism: Trimethoprim MIC is reported as 0.25 to 0.50\
    \ ug/ml in this construct/host comparison; the\n      modest shift is not an independently\
    \ established clinical resistance category.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:29319470\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5857375/\n      snippet:\
    \ marC\n      explanation: Table 2 TOP10/pFF6 and marC rows, Trimethoprim column;\
    \ antisense control and validation\n        Methods; Table S2 clone primers.\n\
    \      cache_path: evidence/PF01914/gingras-2018.txt\n      cache_sha256: 77a82410ca3790377b21059eadeb40eba8a319afc681c1c7d4b438535c9eeaa2\n\
    - graph_id: marc-antibiotic-rna-2008\n  title: Antibiotic exposure raises steady-state\
    \ marC RNA\n  scope: McDermott2008 AG100 drug-exposed versus untreated cultures,\
    \ not a MarC efflux or direct transcription\n    assay.\n  context: 'Original\
    \ Figure 1 Northern blot: mid-exponential LB cultures, 30 C, one-hour exposure.\
    \ Separate\n    tetracycline and chloramphenicol 5 ug/ml conditions.'\n  family_mapping:\
    \ E. coli K-12 MarC P0AEY1/b1529/JW1522 sequence version 1, 221 aa, PF01914 5-217.\
    \ This\n    is reference mapping, not independent sequencing of historical strains\
    \ or proof of isolated-domain\n    function.\n  scope_status: PHENOTYPIC\n  taxon:\
    \ NCBITaxon:562\n  limitations: The stronger blot signal is not quantified as\
    \ a fold-change or significance estimate. The\n    authors favor mRNA stabilization\
    \ over true induction; MarR binding and direct transcription are not\n    established.\
    \ Salicylate and marR-inactive comparison are negative in the inspected conditions.\
    \ Susceptibility\n    negatives are retained separately from RNA effects.\n  nodes:\n\
    \  - node_id: tetracycline\n    label: AG100 exposed to tetracycline 5 ug/ml for\
    \ one hour\n    node_type: PERTURBATION\n  - node_id: chloramphenicol\n    label:\
    \ AG100 exposed to chloramphenicol 5 ug/ml for one hour\n    node_type: PERTURBATION\n\
    \  - node_id: marc-rna\n    label: Steady-state marC RNA signal\n    node_type:\
    \ STATE\n    grounding:\n    - UniProtKB:P0AEY1\n  edges:\n  - edge_id: tet-increases-rna\n\
    \    subject: tetracycline\n    predicate: increases\n    object: marc-rna\n \
    \   mechanism: The treated culture has a stronger marC Northern signal than untreated\
    \ cells; changes in\n      RNA synthesis versus degradation are unresolved.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:17954692\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2223875/\n\
    \      snippet: likely reflects stabilization of mRNA rather than true induction\n\
    \      explanation: Figure 1 original image, lane 6 versus lane 1; caption and\
    \ RNA-stabilization discussion.\n      cache_path: evidence/PF01914/mcdermott-2008.txt\n\
    \      cache_sha256: 8f0f64d47bff41d3986fa3c0a9fe0019601dc706de6e901503673a35a742e4e0\n\
    \  - edge_id: cam-increases-rna\n    subject: chloramphenicol\n    predicate:\
    \ increases\n    object: marc-rna\n    mechanism: Chloramphenicol exposure increases\
    \ steady-state RNA signal, without establishing direct\n      activation of the\
    \ marC promoter.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:17954692\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC2223875/\n      snippet: likely reflects\
    \ stabilization of mRNA rather than true induction\n      explanation: Figure\
    \ 1 original image, lane 4 versus lane 1; caption and RNA-stabilization discussion.\n\
    \      cache_path: evidence/PF01914/mcdermott-2008.txt\n      cache_sha256: 8f0f64d47bff41d3986fa3c0a9fe0019601dc706de6e901503673a35a742e4e0\n\
    curation_events:\n- timestamp: '2026-10-12T00:39:19Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate PF01914 SnatA, MarC and YchE condition-specific\
    \ cellular graphs\n  history_record: history/records/PF01914/2026-10-12T003919Z-codex-ec1842.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-12T00:50:36Z'\n\
    \  curator: Codex\n  action: REVIEW\n  outcome: needs_followup\n  summary: Review\
    \ PF01914 SnatA, MarC and YchE contextual cellular graphs\n  history_record: history/records/PF01914/2026-10-12T005036Z-codex-319eb0.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-12T00:53:33Z'\n\
    \  curator: Codex\n  action: EDIT\n  outcome: changed\n  summary: Correct YchE\
    \ Figure1C p-value transcription without changing graph direction\n  history_record:\
    \ history/records/PF01914/2026-10-12T005333Z-codex-52f262.yaml\n  event_index:\
    \ 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Frozen PF01914 MarC/IPR002771 is former UPF0056. K-12 P0AEY1 maps PF01914
    at5-217 of221aa and P25743/YchE at9-210 of215aa. Exact AB093585.1/BAC53669.1 SnatA
    equals UniParc UPI0000062A6D,216aa, PF01914 9-214. Q8J305 retirement is not biological
    absence. ATCC25922 DR76_3329/AIL17056.1 equals UPI00000DEBB0,221aa,PF01914 5-217,
    with N36S relative to K-12. Published primer tails map a full-CDS validation insert3541797-3542673;
    the different enrichment interval ending3542008 remains unresolved. Reference
    equality and primer mapping do not independently sequence historical clones. Imported
    identity, counters and frozen snapshot remain unchanged.
  target_ids:
  - PF01914
  evidence_ids:
  - identity
  - primary
  - threonine-clones-and-yche
  - antibiotic-rna-and-negative-susceptibility
  - qualified-isobutanol-reconstruction
  - host-dependent-mic-and-primer-mapping
  - isoprenol-and-butanol-growth
  - discovery-and-remaining-coverage
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: SnatA uptake and competition are scoped to genomic constructs in AK430;
    WAT9 serine growth is a separate phenotype. MarC threonine edges name whole selected
    clones, including B2059 passenger variants and S140SS as an insertion. YchE growth
    rescue is not promoted to significant transport in the other tested host. Minty
    reconstruction graphs name the reported strain comparison, not a clean isogenic
    MarC deletion, because EcHW24 construction and EcNR1 comparator differ in MutS.
    Babel deletion growth is distinct from non-additive M35stop expression, which
    is not WT rescue. Gingras five modest MIC changes are conditional TOP10 construct
    comparisons with pFF6 and antisense controls, not clinical resistance, direct
    efflux or universal family function. McDermott negative susceptibility tests are
    retained alongside the different 2018 result; antibiotic-exposure RNA is steady-state
    abundance, not demonstrated promoter induction. No observed molecular transport
    cycle, binding-site residue or inter-study relay is asserted.
  target_ids:
  - PF01914
  evidence_ids:
  - primary
  - native
  - threonine-clones-and-yche
  - antibiotic-rna-and-negative-susceptibility
  - qualified-isobutanol-reconstruction
  - host-dependent-mic-and-primer-mapping
  - isoprenol-and-butanol-growth
  - discovery-and-remaining-coverage
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Three selected member branches and six papers are not all15684 proteins.
    Other archaeal members, YhgN and YvbG remain uncurated. Native archaeal experiments,
    purified reconstitution, matched host/allele/vector antibiotic tests, independent
    single-allele reconstruction and historical clone sequences remain needed. Glucose
    units, 2011 background/uncertainty and 2018 enrichment boundaries are unresolved.
    Figure9 epistasis, many supplements and raw replicate data remain uninspected.
  target_ids:
  - PF01914
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01914-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve source and clone discrepancies and extend member-specific mechanisms
  description: Reconstruct selected MarC variants separately from passenger mutations;
    verify YchE flux independently of growth rescue; resolve the 2011 MutS background
    and 2025 glucose units. Recover original 2018 enrichment boundaries and raw MIC
    uncertainty, retaining matched-control limits. Extend verified archaeal/YhgN/YvbG
    branches with primary assays and test purified transport before direct biochemical
    edges. Preserve negative results and native history; save an evidence-backed successor
    review for additional contexts rather than editing this partial report.
  target_ids:
  - PF01914
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - threonine-clones-and-yche
  - antibiotic-rna-and-negative-susceptibility
  - qualified-isobutanol-reconstruction
  - host-dependent-mic-and-primer-mapping
  - isoprenol-and-butanol-growth
  - discovery-and-remaining-coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01914.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Reconstruct selected MarC variants separately from passenger mutations;
    verify YchE flux independently of growth rescue; resolve the 2011 MutS background
    and 2025 glucose units. Recover original 2018 enrichment boundaries and raw MIC
    uncertainty, retaining matched-control limits. Extend verified archaeal/YhgN/YvbG
    branches with primary assays and test purified transport before direct biochemical
    edges. Preserve negative results and native history; save an evidence-backed successor
    review for additional contexts rather than editing this partial report.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01914
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Akahane original Figures2-4/Tables1-3, Bubnov Figures1/2, McDermott Figure1 and
  Babel Figures4/5 were visually inspected. Minty Table3 and Gingras Tables1/2 plus
  supplement TablesS2/S3 were inspected as parsed text/tables; not every figure, supplement
  or raw dataset was reviewed. Exact reference sequences and primer matching do not
  establish historical assay-clone identity. Source contradictions are retained, not
  corrected by assumption.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
