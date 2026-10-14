# PF01784 YbgI folE conditional phenotype and mechanism-gap review

- Review: 20261011T054325Z-pf01784-ybgi-causal-context
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T05:43:12Z
- Finished UTC: 2026-10-11T05:43:25Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Figure 8b supports a narrowly timed liquid-growth phenotype in the folE-deficient background, not a general DUF34 enzyme assignment.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: DUF34 family selected to separate primary genotype evidence from contested enzyme annotation and proposed metal-insertion function.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01784 | data/families/PF01784.yaml | generated | PF01784 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01784 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01784.

The primary paper explicitly identifies E. coli YbgI as P0AFP6 and describes the MG1655 transduction scheme. Current identity facts resolve b0710/JW0700, sequence version 1, 247 residues, and PF01784 at 1-246. Exact derivative strain names and oligonucleotides from inaccessible Table S2 remain unverified; the family mapping does not imply an isolated-domain experiment.

### Directed effects and limits

graph: supported. Targets: PF01784.

The single indirect phenotypic edge is limited to the visually observed approximately 5-15 h liquid-OD comparison, not fitted growth rates, viability, endpoint biomass or the separate plate condition. No liquid-endpoint rescue is claimed. Contradictory prose is retained in both graph limitations and a native discussion, and no GTP-cyclohydrolase or metal-insertase edge is inferred from complementation failure, annotations or structural metal binding.

### Remaining family coverage

completeness: concern. Targets: PF01784.

Reconcile the broader growth wording and obtain Table S2, raw growth data and a matched rescue before strengthening gene-specific mechanistic claims. HcgD, HP0959 and the YbgI cell-wall study need direct primary-evidence review; none is imported as a molecular mechanism from this paper's discussion or a database summary.

## Findings

### additional-contexts: Resolve YbgI context discrepancies and review member-specific molecular evidence

minor / open / confirmed; issue key: pf01784-causal-context-coverage.

Obtain the missing supplement and assess the liquid-versus-plate distinction, allele effects and matched rescue for the retained phenotype. Independently inspect primary HcgD and HP0959 evidence before assigning a molecular function; do not replace one family-wide annotation with another unsupported one.

## Recommended Actions And Acceptance Checks

### extend-contexts

Obtain the missing supplement and assess the liquid-versus-plate distinction, allele effects and matched rescue for the retained phenotype. Independently inspect primary HcgD and HP0959 evidence before assigning a molecular function; do not replace one family-wide annotation with another unsupported one.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| experiment | https://pmc.ncbi.nlm.nih.gov/articles/PMC8469502/; Methods 2.7-2.9, Results 3.9, conclusions and visually inspected Figure 8 | supports | MG1655-derived ybgI folE double mutants have lower early liquid-culture OD600 than folE-only mutants with deoxythymidine. The article contains unresolved broader growth wording and a plate-imaging-time disagreement, which are retained explicitly. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0AFP6/entry/pfam/PF01784/; Accession and domain locations; paired UniProt identity facts | supports | The primary paper explicitly identifies E. coli YbgI as P0AFP6 and describes the MG1655 transduction scheme. Current identity facts resolve b0710/JW0700, sequence version 1, 247 residues, and PF01784 at 1-246. Exact derivative strain names and oligonucleotides from inaccessible Table S2 remain unverified; the family mapping does not imply an isolated-domain experiment. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01784 | data/families/PF01784.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Figure 8 was visually inspected and relevant main-text methods were read. The supplement endpoint returned HTML and the publisher route returned 403, so Table S2 was not inspected. No raw curve reanalysis or inspection of the primary HcgD/HP0959 studies was completed; PMID:29625546 was abstract-only.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T054325Z-pf01784-ybgi-causal-context
title: PF01784 YbgI folE conditional phenotype and mechanism-gap review
started_at: '2026-10-11T05:43:12Z'
finished_at: '2026-10-11T05:43:25Z'
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
summary: Figure 8b supports a narrowly timed liquid-growth phenotype in the folE-deficient
  background, not a general DUF34 enzyme assignment.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01784.yaml
    sha256: 63e621bc1272687696f21d4f19ef38f127d30420a53c2aab94be4f0ac5245561
    role: context
  - path: data/families/PF01784.yaml
    sha256: edb18a7c89ceb83c7f3c569a6a2e46292d863c076f0ed408dc1d843bd3d2293a
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
  - path: evidence/PF01784/reed-2021-ybgi.txt
    role: context
    sha256: d8c1f795754e212c045d8b8e0d7a96430829a3524613d26dee5535535870a861
  - path: evidence/PF01784/P0AFP6-identity.txt
    role: context
    sha256: 9f21d691f020e2fa5f34d5d9db74b260cd161d72d8860474a6fcd4619eeec859
targets:
- target_id: PF01784
  path: data/families/PF01784.yaml
  label: PF01784
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01784.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 30cfaee502d282f7a88b0ff6dbb324816684f0d65a45aff5d3b8892928c1e7ca
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: DUF34 family selected to separate primary genotype evidence from contested
    enzyme annotation and proposed metal-insertion function.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01784
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Reconcile the broader growth wording and obtain Table S2, raw growth data
      and a matched rescue before strengthening gene-specific mechanistic claims.
      HcgD, HP0959 and the YbgI cell-wall study need direct primary-evidence review;
      none is imported as a molecular mechanism from this paper's discussion or a
      database summary.
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
  - PF01784
  evidence_ids:
  - native
evidence:
- evidence_id: experiment
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8469502/
  locator: Methods 2.7-2.9, Results 3.9, conclusions and visually inspected Figure
    8
  accessed_at: '2026-10-11T05:43:25Z'
  support: supports
  snapshot_sha256: d8c1f795754e212c045d8b8e0d7a96430829a3524613d26dee5535535870a861
  summary: MG1655-derived ybgI folE double mutants have lower early liquid-culture
    OD600 than folE-only mutants with deoxythymidine. The article contains unresolved
    broader growth wording and a plate-imaging-time disagreement, which are retained
    explicitly.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0AFP6/entry/pfam/PF01784/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T05:43:25Z'
  support: supports
  snapshot_sha256: 9f21d691f020e2fa5f34d5d9db74b260cd161d72d8860474a6fcd4619eeec859
  summary: The primary paper explicitly identifies E. coli YbgI as P0AFP6 and describes
    the MG1655 transduction scheme. Current identity facts resolve b0710/JW0700, sequence
    version 1, 247 residues, and PF01784 at 1-246. Exact derivative strain names and
    oligonucleotides from inaccessible Table S2 remain unverified; the family mapping
    does not imply an isolated-domain experiment.
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T05:43:25Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01784
  kind: record_content
  reference: data/families/PF01784.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T05:43:25Z'
  support: context_only
  snapshot_sha256: edb18a7c89ceb83c7f3c569a6a2e46292d863c076f0ed408dc1d843bd3d2293a
  quote: "id: Pfam:PF01784\npfam_id: PF01784\nname: Duf34/NIF3 (NGG1p interacting\
    \ factor 3)\nshort_name: DUF34_NIF3\nseed_status: KNOWN_HISTORICAL_DUF\ncharacterization_status:\
    \ UNSCORED\ncuration_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01784\n\
    counters:\n  proteins: 18574\n  matches: 18654\n  proteomes: 16807\n  taxa: 26806\n\
    \  structures: 16\n  alphafold_models: 12676\n  domain_architectures: 53\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002678\ndescription: This family includes the DUF34/metal-binding\
    \ protein/NIF3 proteins, which are widely distributed\n  across superkingdoms.\
    \ They were previously annotated as GTP cyclohydrolase 1 type 2 [[cite:PUB00070175]]\n\
    \  and, recently, through a comprehensive literature review and integrative bioinformatics\
    \ analyses it\n  was revealed that annotations for these members were misleading\
    \ as they were based on a single set of\n  in vitro results examining the NIF3\
    \ homolog of Helicobacter pylori [[cite:PUB00070175]]. Actually, they\n  have\
    \ varied phenotypes with the unifying functional role as metal-binding proteins\
    \ [[cite:PUB00100327]].\n  This entry contains several NIF3 (NGG1p interacting\
    \ factor 3) protein homologues. NIF3 interacts with\n  the yeast transcriptional\
    \ coactivator NGG1p which is part of the ADA complex, the exact function of\n\
    \  this interaction is unknown [[cite:PUB00002954],[cite:PUB00019927]].\ncuration_history:\
    \ history/records/PF01784\ndiscussions:\n- discussion_id: ybgi-fole-context-and-mechanism\n\
    \  prompt: Resolve the liquid-versus-plate growth wording and test the molecular\
    \ basis of the conditional\n    ybgI folE interaction before extending this graph.\n\
    \  kind: CURATION_TODO\n  status: OPEN\n  rationale: The inspected curve supports\
    \ a narrow genotype effect, whereas complementation failure does\n    not prove\
    \ an absence of all YbgI chemistry. Family-wide metal-insertase and GTP-cyclohydrolase\
    \ assignments\n    require member-specific primary evidence.\n  evidence:\n  -\
    \ reference: PMID:34572495\n    supports: PARTIAL\n    evidence_source: full_text\n\
    \    explanation: Figure 8b supports lower early liquid OD, but later Results\
    \ prose describes better double-mutant\n      growth on dT. Plate methods and\
    \ caption also differ on imaging time; neither discrepancy is silently\n     \
    \ resolved.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n  notes: Supplement\
    \ access failed, so derivative identifiers and primers in Table S2 remain unverified.\n\
    \    HcgD, HP0959 and the YbgI cell-wall study are follow-up leads, not adopted\
    \ molecular mechanisms.\ncausal_graphs:\n- graph_id: ecoli-ybgi-fole-liquid-growth\n\
    \  title: Additional ybgI deletion lowers early culture density in a folE mutant\n\
    \  scope: E. coli K-12 MG1655-derived ybgI folE double mutant compared with its\
    \ folE-only mutant; whole-gene\n    genetic comparison, not isolated-domain biochemistry.\n\
    \  context: Liquid LB with 0.3 mM deoxythymidine, starting OD600 0.1, 37 C; growth\
    \ followed for 40 h with\n    five replicates. The adopted comparison is the lower\
    \ double-mutant OD600 during approximately 5-15\n    h in Figure 8b.\n  family_mapping:\
    \ The study explicitly identifies E. coli YbgI as UniProtKB:P0AFP6; b0710/JW0700,\
    \ sequence\n    version 1, 247 residues, PF01784 spans 1-246. Reference coordinates\
    \ do not imply an isolated-domain\n    test.\n  scope_status: PHENOTYPIC\n  taxon:\
    \ NCBITaxon:83333\n  limitations: The result is conditional on folE deficiency\
    \ and liquid-medium timing; ybgI deletion alone\n    was similar to wild type.\
    \ No ybgI rescue of this liquid-growth endpoint was established, and indirect\n\
    \    or allele-context effects remain possible. Later prose describing better\
    \ double-mutant growth on dT\n    is unresolved and not generalized over the inspected\
    \ curve. No metal-insertion or GTP-cyclohydrolase\n    mechanism is assigned.\n\
    \  nodes:\n  - node_id: additional-ybgi-deletion\n    label: Additional ybgI deletion\
    \ in the folE-deficient background\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:P0AFP6\n  - node_id: early-liquid-od\n    label: Culture OD600\
    \ at approximately 5-15 h in dT-supplemented LB\n    node_type: PHENOTYPE\n  edges:\n\
    \  - edge_id: double-mutant-decreases-early-od\n    subject: additional-ybgi-deletion\n\
    \    predicate: decreases\n    object: early-liquid-od\n    mechanism: The defined\
    \ double-mutant genotype has lower early culture density than the folE-only control\n\
    \      under the matched liquid-growth condition; the molecular cause remains\
    \ unresolved.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:34572495\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC8469502/\n      snippet: grew at a\
    \ slower rate than the folE single mutant\n      explanation: Methods 2.7-2.8,\
    \ Results 3.9 and visually inspected Figure 8b support the scoped OD\n       \
    \ comparison. No fitted growth rate, universal requirement or metal-delivery reaction\
    \ is inferred.\n      cache_path: evidence/PF01784/reed-2021-ybgi.txt\n      cache_sha256:\
    \ d8c1f795754e212c045d8b8e0d7a96430829a3524613d26dee5535535870a861\n    - reference:\
    \ https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0AFP6/entry/pfam/PF01784/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0AFP6/entry/pfam/PF01784/\n\
    \      snippet: 'entry accession: PF01784'\n      explanation: Reference identity\
    \ and domain mapping only; the primary paper supplies the experimental\n     \
    \   genotype and background.\n      cache_path: evidence/PF01784/P0AFP6-identity.txt\n\
    \      cache_sha256: 9f21d691f020e2fa5f34d5d9db74b260cd161d72d8860474a6fcd4619eeec859\n\
    curation_events:\n- timestamp: '2026-10-11T05:40:34Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate the conditional YbgI folE liquid-growth\
    \ phenotype\n  history_record: history/records/PF01784/2026-10-11T054034Z-codex-ff489d.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: The primary paper explicitly identifies E. coli YbgI as P0AFP6 and describes
    the MG1655 transduction scheme. Current identity facts resolve b0710/JW0700, sequence
    version 1, 247 residues, and PF01784 at 1-246. Exact derivative strain names and
    oligonucleotides from inaccessible Table S2 remain unverified; the family mapping
    does not imply an isolated-domain experiment.
  target_ids:
  - PF01784
  evidence_ids:
  - identity
  - experiment
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: The single indirect phenotypic edge is limited to the visually observed
    approximately 5-15 h liquid-OD comparison, not fitted growth rates, viability,
    endpoint biomass or the separate plate condition. No liquid-endpoint rescue is
    claimed. Contradictory prose is retained in both graph limitations and a native
    discussion, and no GTP-cyclohydrolase or metal-insertase edge is inferred from
    complementation failure, annotations or structural metal binding.
  target_ids:
  - PF01784
  evidence_ids:
  - experiment
  - native
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Reconcile the broader growth wording and obtain Table S2, raw growth data
    and a matched rescue before strengthening gene-specific mechanistic claims. HcgD,
    HP0959 and the YbgI cell-wall study need direct primary-evidence review; none
    is imported as a molecular mechanism from this paper's discussion or a database
    summary.
  target_ids:
  - PF01784
  evidence_ids:
  - experiment
findings:
- finding_id: additional-contexts
  issue_key: pf01784-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve YbgI context discrepancies and review member-specific molecular evidence
  description: Obtain the missing supplement and assess the liquid-versus-plate distinction,
    allele effects and matched rescue for the retained phenotype. Independently inspect
    primary HcgD and HP0959 evidence before assigning a molecular function; do not
    replace one family-wide annotation with another unsupported one.
  target_ids:
  - PF01784
  field_paths:
  - causal_graphs
  - discussions
  evidence_ids:
  - experiment
  - identity
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01784.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Obtain the missing supplement and assess the liquid-versus-plate distinction,
    allele effects and matched rescue for the retained phenotype. Independently inspect
    primary HcgD and HP0959 evidence before assigning a molecular function; do not
    replace one family-wide annotation with another unsupported one.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01784
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Figure 8 was visually inspected and relevant main-text methods were read. The supplement
  endpoint returned HTML and the publisher route returned 403, so Table S2 was not
  inspected. No raw curve reanalysis or inspection of the primary HcgD/HP0959 studies
  was completed; PMID:29625546 was abstract-only.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
