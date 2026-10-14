# Scoped scientific assessment of DUF1638 nutrient-dependent mutant fitness

- Review: 20261011T062155Z-pf07796-duf1638-causal-graph
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T06:19:45Z
- Finished UTC: 2026-10-11T06:21:55Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain two observed indirect fitness edges for Phaeobacter inhibens PGA1_c13340, grounded to an exact archived sequence. The nutrient comparison is explicit, while direct B12 reactivation, protein interaction and broader family function remain unestablished by the inspected evidence.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF07796/DUF1638; the PGA1_c13340 row of the 2018 Figure 4B, with the 2025 SPO2162 discussion inspected only as a distinct follow-up lead.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF07796 | data/families/PF07796.yaml | generated | PF07796 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF07796 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF07796.

AFO91049.1 maps to PGA1_c13340 in P. inhibens DSM 17395, taxon 391619. Its 241-aa sequence exactly matches UniParc UPI0001632E23, which gives PF07796 at 72-230. The NCBI CDD region ends at 231 and is retained as a separate annotation. Historical UniProt references are inactive, but NCBI/UniParc establish identity. The bacterial member is not excluded by the frozen archaeal-focused description; no isolated-domain activity is inferred.

### Directed effects and limits

graph: supported. Targets: PF07796.

Both edges are PHENOTYPIC, INDIRECT, OBSERVED and EXPERIMENTAL. The insertion perturbation decreases normalized pool fitness in ammonium/sucrose, and the full methionine/sucrose nutrient condition increases it relative to that baseline. The endpoint is relative barcode abundance, not absolute growth or methionine flux. The source leaves the specific DUF1638 function unresolved despite a broader figure heading. Cofitness, operon-terminal placement and phylogenetic profiles do not establish a direct complex, definitive polarity control or cobalamin-reduction chemistry. Later MtgC/MtgD knockout rescue is not transferred to DUF1638.

### Remaining family coverage

completeness: concern. Targets: PF07796.

Only one member's two conditional fitness effects are curated. Exact nutrient concentrations, matched experiment identifiers, temperature/duration and insertion-level contributions need retrieval, along with clean genetic rescue and direct molecular assays. The 2025 SPO2162 proteomics association is a distinct member lead; its identity, underlying dataset and causal biochemical role have not been independently curated. Archaeal members and additional contexts remain outside this partial review.

## Findings

### additional-contexts: Resolve nutrient metadata and test the DUF1638 biochemical interpretation

minor / open / confirmed; issue key: pf07796-causal-context-coverage.

Obtain the experiment-level Figure 4B medium and insertion metadata, keeping ammonium/sucrose and methionine/sucrose distinct. Assess locus-specific genetic rescue and member-specific biochemical evidence before adding B12-reactivation or protein-partner edges. Independently map and inspect the later SPO2162 context; do not transfer MtgC/MtgD assays. Retain an evidence-backed successor review with unresolved scope stated explicitly.

## Recommended Actions And Acceptance Checks

### extend-contexts

Obtain the experiment-level Figure 4B medium and insertion metadata, keeping ammonium/sucrose and methionine/sucrose distinct. Assess locus-specific genetic rescue and member-specific biochemical evidence before adding B12-reactivation or protein-partner edges. Independently map and inspect the later SPO2162 context; do not transfer MtgC/MtgD assays. Retain an evidence-backed successor review with unresolved scope stated explicitly.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC5764234/; RamA-like-protein results, visually inspected Figure 4, Table 2 and strains/media and mutant-fitness methods | supports | Insertion-mutant gene fitness is negative in the ammonium/sucrose condition and relieved in the methionine/sucrose condition. Figure labels and carbon/nitrogen-source methods prevent treating this as an otherwise identical ammonium-containing medium plus one extra supplement. Specific nutrient doses and experiment identifiers remain unresolved. |
| identity | https://rest.uniprot.org/uniparc/UPI0001632E23.json; Accession and domain locations; paired UniProt identity facts | supports | AFO91049.1 maps to PGA1_c13340 in P. inhibens DSM 17395, taxon 391619. Its 241-aa sequence exactly matches UniParc UPI0001632E23, which gives PF07796 at 72-230. The NCBI CDD region ends at 231 and is retained as a separate annotation. Historical UniProt references are inactive, but NCBI/UniParc establish identity. The bacterial member is not excluded by the frozen archaeal-focused description; no isolated-domain activity is inferred. |
| later-duf1638-lead | https://pmc.ncbi.nlm.nih.gov/articles/PMC12478193/; Main proteomics results mentioning SPO2162 and separate MtgC/MtgD mutant-results sections | supports | The paper reports higher SPO2162 abundance under N-osmolyte conditions and discusses a predicted cobalamin-reactivation role. The inspected knockout/complementation evidence concerns other proteins and cannot prove a DUF1638 reaction. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf07796 | data/families/PF07796.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- The 2018 Figure 4 was visually inspected with relevant results and main methods. The 2025 main proteomics and MtgC/MtgD mutant-results sections were read, but that paper's figure, supplement and raw proteomics were not independently curated. Raw barcode data and phylogenetic profiling were not reanalyzed; no experimental replication is claimed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T062155Z-pf07796-duf1638-causal-graph
title: Scoped scientific assessment of DUF1638 nutrient-dependent mutant fitness
started_at: '2026-10-11T06:19:45Z'
finished_at: '2026-10-11T06:21:55Z'
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
summary: Retain two observed indirect fitness edges for Phaeobacter inhibens PGA1_c13340,
  grounded to an exact archived sequence. The nutrient comparison is explicit, while
  direct B12 reactivation, protein interaction and broader family function remain
  unestablished by the inspected evidence.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF07796.yaml
    sha256: 7c6843f954df340b9407740224a901a741080f3db8af70dc645ab4e90a171be0
    role: context
  - path: data/families/PF07796.yaml
    sha256: 5019cad19ce4f71efba702386331628d80b5743458a91a15897e5b4b93ea0809
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
  - path: evidence/PF07796/price-2018-duf1638.txt
    role: context
    sha256: 554b459470b3aa5e2180e27be9d1acfbfbbf6f4b88d8abd7ae1f51fe3ac648b7
  - path: evidence/PF07796/PGA1c13340-identity.txt
    role: context
    sha256: 292f2715a2cb7dc650e05e1fac3ea33cf118543c92c72dded7c22f266f361b06
  - path: evidence/PF07796/mausz-2025-duf1638-lead.txt
    role: context
    sha256: 9bfb2303fc0c06da3dfc203850a2753d5863b865829ddb22b88b826b3dd388e4
targets:
- target_id: PF07796
  path: data/families/PF07796.yaml
  label: PF07796
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF07796.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 3b0e03e7c100f56e3e14f037e2386cfc0ecd184139e6d02042acb2c4ff63833e
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF07796/DUF1638; the PGA1_c13340 row of the 2018 Figure 4B, with the
    2025 SPO2162 discussion inspected only as a distinct follow-up lead.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF07796
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Only one member's two conditional fitness effects are curated. Exact nutrient
      concentrations, matched experiment identifiers, temperature/duration and insertion-level
      contributions need retrieval, along with clean genetic rescue and direct molecular
      assays. The 2025 SPO2162 proteomics association is a distinct member lead; its
      identity, underlying dataset and causal biochemical role have not been independently
      curated. Archaeal members and additional contexts remain outside this partial
      review.
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
  - PF07796
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5764234/
  locator: RamA-like-protein results, visually inspected Figure 4, Table 2 and strains/media
    and mutant-fitness methods
  accessed_at: '2026-10-11T06:21:55Z'
  support: supports
  snapshot_sha256: 554b459470b3aa5e2180e27be9d1acfbfbbf6f4b88d8abd7ae1f51fe3ac648b7
  summary: Insertion-mutant gene fitness is negative in the ammonium/sucrose condition
    and relieved in the methionine/sucrose condition. Figure labels and carbon/nitrogen-source
    methods prevent treating this as an otherwise identical ammonium-containing medium
    plus one extra supplement. Specific nutrient doses and experiment identifiers
    remain unresolved.
- evidence_id: identity
  kind: database
  reference: https://rest.uniprot.org/uniparc/UPI0001632E23.json
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T06:21:55Z'
  support: supports
  snapshot_sha256: 292f2715a2cb7dc650e05e1fac3ea33cf118543c92c72dded7c22f266f361b06
  summary: AFO91049.1 maps to PGA1_c13340 in P. inhibens DSM 17395, taxon 391619.
    Its 241-aa sequence exactly matches UniParc UPI0001632E23, which gives PF07796
    at 72-230. The NCBI CDD region ends at 231 and is retained as a separate annotation.
    Historical UniProt references are inactive, but NCBI/UniParc establish identity.
    The bacterial member is not excluded by the frozen archaeal-focused description;
    no isolated-domain activity is inferred.
- evidence_id: later-duf1638-lead
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC12478193/
  locator: Main proteomics results mentioning SPO2162 and separate MtgC/MtgD mutant-results
    sections
  summary: The paper reports higher SPO2162 abundance under N-osmolyte conditions
    and discusses a predicted cobalamin-reactivation role. The inspected knockout/complementation
    evidence concerns other proteins and cannot prove a DUF1638 reaction.
  accessed_at: '2026-10-11T06:21:55Z'
  support: supports
  snapshot_sha256: 9bfb2303fc0c06da3dfc203850a2753d5863b865829ddb22b88b826b3dd388e4
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T06:21:55Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf07796
  kind: record_content
  reference: data/families/PF07796.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T06:21:55Z'
  support: context_only
  snapshot_sha256: 5019cad19ce4f71efba702386331628d80b5743458a91a15897e5b4b93ea0809
  quote: "id: Pfam:PF07796\npfam_id: PF07796\nname: Protein of unknown function (DUF1638)\n\
    short_name: DUF1638\nseed_status: UNKNOWN_CANDIDATE\ncharacterization_status:\
    \ UNSCORED\ncuration_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF07796\n\
    counters:\n  proteins: 1741\n  matches: 1743\n  proteomes: 1383\n  taxa: 2446\n\
    \  structures: 0\n  alphafold_models: 1252\n  domain_architectures: 27\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR012437\ndescription: This family contains sequences covering\
    \ an approximately 270 amino acid stretch of a group\n  of hypothetical proteins.\
    \ These proteins are expressed by archaeal species of the Methanosarcina genus.\n\
    curation_history: history/records/PF07796\ndiscussions:\n- discussion_id: duf1638-fitness-versus-reactivation\n\
    \  prompt: Retrieve experiment-level nutrient and insertion metadata and test\
    \ the proposed DUF1638 biochemical\n    role independently of its fitness association.\n\
    \  kind: CURATION_TODO\n  status: OPEN\n  rationale: The retained evidence supports\
    \ conditional pooled fitness, while B12 reactivation remains\n    a proposed molecular\
    \ interpretation for this protein. Gene-specific rescue, exact nutrient comparisons,\n\
    \    additional member contexts and biochemical assays require separate evidence.\n\
    \  evidence:\n  - reference: PMID:29324779\n    supports: PARTIAL\n    evidence_source:\
    \ full_text\n    explanation: Figure 4 was visually inspected. The authors explicitly\
    \ leave the specific DUF1638 function\n      unresolved; operon position and phylogenetic\
    \ co-occurrence are not biochemical demonstrations.\n  - reference: PMID:40956897\n\
    \    supports: PARTIAL\n    evidence_source: selected_full_text\n    explanation:\
    \ The 2025 main text reports greater SPO2162 abundance during N-osmolyte growth\
    \ and a proposed\n      cobalamin-reactivation role. Its inspected knockout/complementation\
    \ experiments concern MtgC/MtgD,\n      not DUF1638; the SPO2162 mapping and underlying\
    \ data were not independently curated here.\n  posed_by: Codex\n  posed_date:\
    \ '2026-10-11'\n  notes: Do not transfer a neighboring protein's complementation\
    \ or biochemical activity to DUF1638, or\n    interpret a frozen archaeal-focused\
    \ description as excluding this verified bacterial member. No family-wide\n  \
    \  negative conclusion follows from the bounded search.\ncausal_graphs:\n- graph_id:\
    \ pinhibens-duf1638-pooled-fitness\n  title: PGA1_c13340 insertion-mutant fitness\
    \ depends on the supplied nutrients\n  scope: Pooled barcoded transposon mutants\
    \ of Phaeobacter inhibens DSM 17395/BS107, focusing on the PGA1_c13340\n    row\
    \ in Figure 4B; not an individual deletion, purified reaction or demonstrated\
    \ B12-reactivation mechanism.\n  context: The retained comparison is between the\
    \ figure's ammonium-plus-sucrose and methionine-plus-sucrose\n    conditions.\
    \ The caption describes varied carbon and nitrogen sources; methods omit ammonium\
    \ for nitrogen-source\n    tests. This is not assumed to be methionine added to\
    \ an otherwise identical ammonium-containing medium.\n    General fitness methods\
    \ recover pools in rich medium, transfer at OD600 0.02 into 5 mL and sequence\n\
    \    barcodes before growth and at saturation. P. inhibens is grown aerobically\
    \ with shaking; exact plotted\n    nutrient doses, temperature and duration remain\
    \ unverified.\n  family_mapping: PGA1_c13340 is NCBIProtein:AFO91049.1 on the\
    \ reverse strand of CP002976.1 at 1377532-1378257,\n    with a 241-aa sequence\
    \ identical to UniParc UPI0001632E23. UniParc maps PF07796 at 72-230. NCBI's\n\
    \    CDD-based interval ends at 231; these are not silently treated as identical\
    \ annotations. Historical\n    UniProt entries are inactive, but the sequence/locus\
    \ identity is retained. The experiment concerns\n    a bacterial member, not only\
    \ the archaeal members emphasized in the frozen family description.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:391619\n  limitations: Relative fitness is normalized\
    \ mutant abundance during pooled growth, not an absolute growth\n    rate or direct\
    \ methionine flux. No clean deletion or gene complementation is established here.\
    \ Operon-terminal\n    placement argues against polarity but is not a direct polarity\
    \ control; cross-feeding and insertion-level\n    effects remain possible. Cofitness\
    \ and phylogenetic co-occurrence with RamA-like proteins do not prove\n    interaction\
    \ or electron transfer. The source's B12-reactivation figure heading is broader\
    \ than its\n    explicit uncertainty about the DUF1638 molecular function.\n \
    \ nodes:\n  - node_id: pga1-c13340-insertions\n    label: Transposon disruption\
    \ of PGA1_c13340 in the P. inhibens pool\n    node_type: PERTURBATION\n    grounding:\n\
    \    - NCBIProtein:AFO91049.1\n  - node_id: methionine-sucrose-condition\n   \
    \ label: Methionine/sucrose condition instead of ammonium/sucrose\n    node_type:\
    \ PERTURBATION\n  - node_id: pga1-c13340-relative-fitness\n    label: Relative\
    \ fitness of PGA1_c13340 insertion mutants during pooled growth\n    node_type:\
    \ PHENOTYPE\n  edges:\n  - edge_id: insertions-decrease-ammonium-sucrose-fitness\n\
    \    subject: pga1-c13340-insertions\n    predicate: decreases\n    object: pga1-c13340-relative-fitness\n\
    \    mechanism: In the ammonium/sucrose condition, PGA1_c13340 insertion strains\
    \ have negative normalized\n      gene fitness, reflecting loss of relative abundance\
    \ during pool growth. The phenotype is conditional\n      on the tested medium\
    \ and comparison baseline.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:29324779\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5764234/\n      snippet:\
    \ rescued by added methionine\n      explanation: Visually inspected Figure 4B\
    \ establishes the negative ammonium/sucrose fitness values\n        for the identified\
    \ DUF1638 row; the quoted rescue result supplies adjacent perturbation context,\n\
    \        not a direct catalytic measurement.\n      cache_path: evidence/PF07796/price-2018-duf1638.txt\n\
    \      cache_sha256: 554b459470b3aa5e2180e27be9d1acfbfbbf6f4b88d8abd7ae1f51fe3ac648b7\n\
    \    - reference: https://rest.uniprot.org/uniparc/UPI0001632E23.json\n      source_url:\
    \ https://rest.uniprot.org/uniparc/UPI0001632E23.json\n      snippet: 'database:\
    \ Pfam; databaseId: PF07796; locations: 72-230, inclusive'\n      explanation:\
    \ Sequence-verified locus-to-family mapping paired with NCBI AFO91049.1; not experimental\n\
    \        evidence for growth or an isolated-domain construct.\n      cache_path:\
    \ evidence/PF07796/PGA1c13340-identity.txt\n      cache_sha256: 292f2715a2cb7dc650e05e1fac3ea33cf118543c92c72dded7c22f266f361b06\n\
    \  - edge_id: methionine-sucrose-increases-mutant-fitness\n    subject: methionine-sucrose-condition\n\
    \    predicate: increases\n    object: pga1-c13340-relative-fitness\n    mechanism:\
    \ PGA1_c13340 mutant fitness is relieved in the plotted methionine/sucrose condition\
    \ relative\n      to ammonium/sucrose. The full nutrient-condition comparison\
    \ is the intervention; no independently\n      sufficient methionine-to-cobalamin\
    \ chemical step is asserted.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:29324779\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5764234/\n      snippet:\
    \ rescued by added methionine\n      explanation: Figure 4B labels and the RamA-like-protein\
    \ results support the nutritional fitness\n        comparison. Exact doses and\
    \ matched experiment identifiers remain open, and the generic supplementation\n\
    \        wording is not used to erase the figure's nitrogen-source distinction.\n\
    \      cache_path: evidence/PF07796/price-2018-duf1638.txt\n      cache_sha256:\
    \ 554b459470b3aa5e2180e27be9d1acfbfbbf6f4b88d8abd7ae1f51fe3ac648b7\n    - reference:\
    \ https://rest.uniprot.org/uniparc/UPI0001632E23.json\n      source_url: https://rest.uniprot.org/uniparc/UPI0001632E23.json\n\
    \      snippet: 'locus_tag: PGA1_c13340'\n      explanation: Resolves the tested\
    \ strain/locus and family membership only; inactive archive accessions\n     \
    \   are not treated as absent biological evidence.\n      cache_path: evidence/PF07796/PGA1c13340-identity.txt\n\
    \      cache_sha256: 292f2715a2cb7dc650e05e1fac3ea33cf118543c92c72dded7c22f266f361b06\n\
    curation_events:\n- timestamp: '2026-10-11T06:18:34Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Add DUF1638 nutrient-dependent pooled-fitness\
    \ causal graph\n  history_record: history/records/PF07796/2026-10-11T061834Z-codex-7e7c6f.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: AFO91049.1 maps to PGA1_c13340 in P. inhibens DSM 17395, taxon 391619.
    Its 241-aa sequence exactly matches UniParc UPI0001632E23, which gives PF07796
    at 72-230. The NCBI CDD region ends at 231 and is retained as a separate annotation.
    Historical UniProt references are inactive, but NCBI/UniParc establish identity.
    The bacterial member is not excluded by the frozen archaeal-focused description;
    no isolated-domain activity is inferred.
  target_ids:
  - PF07796
  evidence_ids:
  - identity
  - primary
  - later-duf1638-lead
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Both edges are PHENOTYPIC, INDIRECT, OBSERVED and EXPERIMENTAL. The insertion
    perturbation decreases normalized pool fitness in ammonium/sucrose, and the full
    methionine/sucrose nutrient condition increases it relative to that baseline.
    The endpoint is relative barcode abundance, not absolute growth or methionine
    flux. The source leaves the specific DUF1638 function unresolved despite a broader
    figure heading. Cofitness, operon-terminal placement and phylogenetic profiles
    do not establish a direct complex, definitive polarity control or cobalamin-reduction
    chemistry. Later MtgC/MtgD knockout rescue is not transferred to DUF1638.
  target_ids:
  - PF07796
  evidence_ids:
  - primary
  - native
  - later-duf1638-lead
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Only one member's two conditional fitness effects are curated. Exact nutrient
    concentrations, matched experiment identifiers, temperature/duration and insertion-level
    contributions need retrieval, along with clean genetic rescue and direct molecular
    assays. The 2025 SPO2162 proteomics association is a distinct member lead; its
    identity, underlying dataset and causal biochemical role have not been independently
    curated. Archaeal members and additional contexts remain outside this partial
    review.
  target_ids:
  - PF07796
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf07796-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve nutrient metadata and test the DUF1638 biochemical interpretation
  description: Obtain the experiment-level Figure 4B medium and insertion metadata,
    keeping ammonium/sucrose and methionine/sucrose distinct. Assess locus-specific
    genetic rescue and member-specific biochemical evidence before adding B12-reactivation
    or protein-partner edges. Independently map and inspect the later SPO2162 context;
    do not transfer MtgC/MtgD assays. Retain an evidence-backed successor review with
    unresolved scope stated explicitly.
  target_ids:
  - PF07796
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - later-duf1638-lead
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF07796.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Obtain the experiment-level Figure 4B medium and insertion metadata,
    keeping ammonium/sucrose and methionine/sucrose distinct. Assess locus-specific
    genetic rescue and member-specific biochemical evidence before adding B12-reactivation
    or protein-partner edges. Independently map and inspect the later SPO2162 context;
    do not transfer MtgC/MtgD assays. Retain an evidence-backed successor review with
    unresolved scope stated explicitly.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF07796
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- The 2018 Figure 4 was visually inspected with relevant results and main methods.
  The 2025 main proteomics and MtgC/MtgD mutant-results sections were read, but that
  paper's figure, supplement and raw proteomics were not independently curated. Raw
  barcode data and phylogenetic profiling were not reanalyzed; no experimental replication
  is claimed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
