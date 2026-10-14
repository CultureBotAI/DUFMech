# PF04149 scoped causal-graph evidence review

- Review: 20261011T040849Z-pf04149-causal-pilot
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T04:00:01Z
- Finished UTC: 2026-10-11T04:08:49Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The single curated edge is supported at its stated experimental scope; neither its biochemical mechanism nor family-wide coverage is established. The record remains IN_PROGRESS.

## Scope And Provenance

Evidence, identity, direction and scope of the newly curated Scr2 graph, not exhaustive DUF397 biology or a full-corpus scientific audit.

Selection: PF04149 pilot selected because retained member context and directly relevant primary experiments are available.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF04149 | data/families/PF04149.yaml | generated | PF04149 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validation of the actual projection | passed | True | PF04149 | Actual generated projection passed closed schema, graph/evidence and canonical-history checks; rendered a local one-family preview. |
| Graph and record guard regressions | passed | True | PF04149 | 93 tests passed, including malformed edges, evidence integrity, feedback, overlay/model roundtrip and semantic-digest changes. |

## Scientific And Domain Assessments

### Exact tested object and domain mapping

identity: supported. Targets: PF04149.

The graph uses a verified member accession and explicitly limits its claim to the whole-gene experiment.

### Scoped direction without a fabricated biochemical mechanism

graph: supported. Targets: PF04149.

The required_for edge, conditional context and PHENOTYPIC/INDIRECT classification match the inspected evidence; no binding or catalysis edge was invented.

### Other characterized members and contexts

completeness: concern. Targets: PF04149.

The current graph is useful but does not yet capture other experimentally investigated DUF397 systems.

## Findings

### additional-systems: Additional characterized DUF397 contexts remain uncurated

minor / open / confirmed; issue key: pf04149-causal-context-coverage.

Review the other experimentally investigated systems independently before extending this record; preserve their distinct protein identities and medium-specific effects.

## Recommended Actions And Acceptance Checks

### extend-systems

Assess the remaining DUF397 systems and add separately scoped graphs where the primary evidence supports direction.

- Each added edge has verified protein/domain identity, context and primary evidence.
- No medium-specific effect is represented as universal family behavior.
- Native record/graph checks pass and a successor review states the actual remaining coverage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary-experiment | https://pmc.ncbi.nlm.nih.gov/articles/PMC6262351/; PMID 30524403; Results Figure 3A-B and Discussion | supports | Inspected the perturbation/control comparison supporting the graph, and the stated inability to establish a purified-protein interaction. |
| protein-identity | https://rest.uniprot.org/uniprotkb/Q9KZY4.json; primaryAccession, genes, organism, sequenceVersion and Pfam domain feature | supports | Q9KZY4 maps SCO4442 to PF04149 at residues 10-62 of the 63-residue version-1 protein in taxon 100226; this is identity evidence, not causality. |
| paralog-coverage | https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2023.1217350/full; Abstract and PubMed PMID 37492264, including figure captions | context_only | Other XRE-DUF397 systems show medium-dependent regulation, including opposite ACT effects for SCO7615/16 across media. This argues against family-wide or context-free generalization; those systems were not curated in this graph. |
| later-context | https://link.springer.com/article/10.1186/s12934-025-02843-5; Background, Methods and Abstract; PMID 41077587 | context_only | The later Scr1 experiment uses NMMP and earlier sampling, with different pathway responses including lower undecylprodigiosin. Its transcriptome/metabolome results are not direct evidence of a Scr2 biochemical step. The current graph remains limited to the original ACT assay. |
| native-validation | tests/test_causal_graphs.py; 93-test graph/record run and actual single-record validation | supports | Structural and provenance safeguards pass; these tests do not establish scientific correctness or count the other 8295 families as reviewed. |
| duf-projection-pf04149 | data/families/PF04149.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Same-agent scoped scientific assessment, not an independent expert review or replication of the experiments.
- Full supplements, all DUF397 members, and direct molecular intermediates were not exhaustively reviewed.
- PMC access challenges for later papers were worked around using the publisher and PubMed; no access failure was treated as negative evidence.
- This is one record in an 8296-family goal; the remaining 8295 families have not received scientific causal review.
- Publication, full QC and canonical Pages regeneration are separate unfinished steps; no REVIEWED promotion is requested.
- Applied the personal dufmech-causal-graphs skill together with the repository's native review and curation contracts.
- The initial repository inventory included hidden and ignored files and found no existing graph authoring surface; native support was added as a prerequisite to the requested graph work.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T040849Z-pf04149-causal-pilot
kind: record
repository: CultureBotAI/DUFMech
title: PF04149 scoped causal-graph evidence review
started_at: '2026-10-11T04:00:01Z'
finished_at: '2026-10-11T04:08:49Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: The same agent researched, curated and reassessed the graph;
    no independent scientific endorsement is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: true
summary: The single curated edge is supported at its stated experimental scope; neither
  its biochemical mechanism nor family-wide coverage is established. The record remains
  IN_PROGRESS.
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF04149.yaml
    role: context
    sha256: a1bcc1f616c6dcaf0c41137d6444253ea59493df3dbb7e9884712d8b81200281
  - path: data/families/PF04149.yaml
    role: target
    sha256: f54f89c0e80acfc1d52c8ca4d395881ff1c4bd57d545c8acf0f7b18183da6f1d
  - path: data/worklists/interpro-pfam-duf-2026-10-10.json
    role: context
    sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383
  - path: data/worklists/interpro-pfam-duf-2026-10-10.manifest.json
    role: context
    sha256: 31c07ffb6a169c851ea0e6e9dd527a10c04028eafeb29187bd62dc2ae848696e
  - path: data/worklists/interpro-pfam-duf-2026-10-10.tsv
    role: context
    sha256: be023c8dd9d8d3864926b5032d6f7e87a884b1a567391696822dbbecc692dae7
  - path: evidence/PF04149/santamaria-2018-scr2.txt
    role: context
    sha256: c97531aa06048cb9f369adde23d447f188da91fa169d533ecce0a5d7be0bb1a5
  - path: evidence/PF04149/uniprot-Q9KZY4-identity.txt
    role: context
    sha256: 30972462904744d03cccc74c036a9dfc1c2e10ff1a91674bb4062aa2e8d5177f
targets:
- kind: generated
  label: PF04149
  path: data/families/PF04149.yaml
  record_class: FamilyRecord
  target_id: PF04149
  owner_paths:
  - path: curation/families/PF04149.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: c69a65fe2e66fbfc6c5e313673ec9b823040059a8c2347f043a31098c5e8fc55
scope:
  description: Evidence, identity, direction and scope of the newly curated Scr2 graph,
    not exhaustive DUF397 biology or a full-corpus scientific audit.
  selection: PF04149 pilot selected because retained member context and directly relevant
    primary experiments are available.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF04149
  exclusions:
  - target: Other PF04149 members and contexts
    reason: Requires additional per-system evidence assessment; no family-wide transfer
      is claimed.
checks:
- check_id: native-record
  name: Native validation of the actual projection
  command: validate_record(load_yaml(data/families/PF04149.yaml), repo_root), followed
    by a scoped render_site preview
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Actual generated projection passed closed schema, graph/evidence and canonical-history
    checks; rendered a local one-family preview.
  target_ids:
  - PF04149
  evidence_ids:
  - native-validation
- check_id: record-regressions
  name: Graph and record guard regressions
  command: PYTHONPATH=src python -m pytest tests/test_causal_graphs.py tests/test_records.py
    -q
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 93 tests passed, including malformed edges, evidence integrity, feedback,
    overlay/model roundtrip and semantic-digest changes.
  target_ids:
  - PF04149
  evidence_ids:
  - native-validation
evidence:
- evidence_id: primary-experiment
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6262351/
  locator: PMID 30524403; Results Figure 3A-B and Discussion
  accessed_at: '2026-10-11T04:08:49Z'
  support: supports
  summary: Inspected the perturbation/control comparison supporting the graph, and
    the stated inability to establish a purified-protein interaction.
  snapshot_sha256: c97531aa06048cb9f369adde23d447f188da91fa169d533ecce0a5d7be0bb1a5
- evidence_id: protein-identity
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9KZY4.json
  locator: primaryAccession, genes, organism, sequenceVersion and Pfam domain feature
  accessed_at: '2026-10-11T04:08:49Z'
  support: supports
  summary: Q9KZY4 maps SCO4442 to PF04149 at residues 10-62 of the 63-residue version-1
    protein in taxon 100226; this is identity evidence, not causality.
  snapshot_sha256: 30972462904744d03cccc74c036a9dfc1c2e10ff1a91674bb4062aa2e8d5177f
- evidence_id: paralog-coverage
  kind: primary_source
  reference: https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2023.1217350/full
  locator: Abstract and PubMed PMID 37492264, including figure captions
  accessed_at: '2026-10-11T04:08:49Z'
  support: context_only
  summary: Other XRE-DUF397 systems show medium-dependent regulation, including opposite
    ACT effects for SCO7615/16 across media. This argues against family-wide or context-free
    generalization; those systems were not curated in this graph.
- evidence_id: later-context
  kind: primary_source
  reference: https://link.springer.com/article/10.1186/s12934-025-02843-5
  locator: Background, Methods and Abstract; PMID 41077587
  accessed_at: '2026-10-11T04:08:49Z'
  support: context_only
  summary: The later Scr1 experiment uses NMMP and earlier sampling, with different
    pathway responses including lower undecylprodigiosin. Its transcriptome/metabolome
    results are not direct evidence of a Scr2 biochemical step. The current graph
    remains limited to the original ACT assay.
- evidence_id: native-validation
  kind: validation
  reference: tests/test_causal_graphs.py
  locator: 93-test graph/record run and actual single-record validation
  accessed_at: '2026-10-11T04:08:49Z'
  support: supports
  summary: Structural and provenance safeguards pass; these tests do not establish
    scientific correctness or count the other 8295 families as reviewed.
- evidence_id: duf-projection-pf04149
  kind: record_content
  reference: data/families/PF04149.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T04:08:49Z'
  support: context_only
  snapshot_sha256: f54f89c0e80acfc1d52c8ca4d395881ff1c4bd57d545c8acf0f7b18183da6f1d
  quote: "id: Pfam:PF04149\npfam_id: PF04149\nname: Domain of unknown function (DUF397)\n\
    short_name: DUF397\nseed_status: UNKNOWN_CANDIDATE\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF04149\n\
    counters:\n  proteins: 37657\n  matches: 40691\n  proteomes: 1831\n  taxa: 2162\n\
    \  structures: 0\n  alphafold_models: 19000\n  domain_architectures: 25\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR007278\ndescription: The function of this family is unknown.\n\
    curation_history: history/records/PF04149\ncausal_graphs:\n- graph_id: scr2-act-induction\n\
    \  title: Scr2-dependent actinorhodin induction\n  scope: Scr2 (SCO4442; UniProtKB:Q9KZY4),\
    \ not all DUF397 proteins or an isolated domain.\n  context: S. coelicolor M145\
    \ and scr2-deletion derivatives, Scr1 overexpression, liquid YES plus xylose,\n\
    \    eight days.\n  family_mapping: UniProt Q9KZY4 sequence version 1 is 63 residues;\
    \ its Pfam PF04149 annotation spans\n    residues 10-62. The experiment perturbs\
    \ the whole gene.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:100226\n  limitations:\
    \ No direct Scr1-Scr2 binding or catalytic mechanism established here; no family-wide\
    \ transfer.\n    Other media, times and paralogs require separate graphs.\n  nodes:\n\
    \  - node_id: scr2-present\n    label: Scr2 present in a Scr1-overexpression background\n\
    \    node_type: STATE\n    grounding:\n    - UniProtKB:Q9KZY4\n  - node_id: induced-act\n\
    \    label: Scr1-induced actinorhodin production\n    node_type: PHENOTYPE\n \
    \ edges:\n  - edge_id: scr2-required-for-act\n    subject: scr2-present\n    predicate:\
    \ required_for\n    object: induced-act\n    mechanism: Loss of scr2 prevents\
    \ induction by Scr1 alone; joint expression restores it. This is a\n      conditional\
    \ requirement, not sufficiency of Scr2.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:30524403\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6262351/\n      snippet:\
    \ these two genes must act in conjunction\n      explanation: Figure 3A-B compares\
    \ deletion strains and expression constructs, with empty-vector\n        controls\
    \ and three independent experiments; supports the scoped phenotype dependency.\n\
    \      cache_path: evidence/PF04149/santamaria-2018-scr2.txt\n      cache_sha256:\
    \ c97531aa06048cb9f369adde23d447f188da91fa169d533ecce0a5d7be0bb1a5\n    - reference:\
    \ https://rest.uniprot.org/uniprotkb/Q9KZY4.json\n      source_url: https://rest.uniprot.org/uniprotkb/Q9KZY4.json\n\
    \      snippet: 'orderedLocusNames: SCO4442'\n      explanation: Identity/domain\
    \ mapping only; the causal evidence comes from the primary experiment,\n     \
    \   not this automated annotation.\n      cache_path: evidence/PF04149/uniprot-Q9KZY4-identity.txt\n\
    \      cache_sha256: 30972462904744d03cccc74c036a9dfc1c2e10ff1a91674bb4062aa2e8d5177f\n\
    curation_events:\n- timestamp: '2026-10-07T12:26:02Z'\n  curator: Codex\n  action:\
    \ REVIEW\n  outcome: no_change\n  summary: Completed a scoped PF04149 frozen-seed\
    \ and native audit integration review; biological content\n    unchanged.\n  history_record:\
    \ history/records/PF04149/2026-10-07T122602Z-codex-3e2c16.yaml\n  event_index:\
    \ 0\n  llm_assisted: true\n- timestamp: '2026-10-11T04:00:01Z'\n  curator: Codex\n\
    \  action: CREATE\n  outcome: changed\n  summary: Added a scoped DUF397 Scr2 phenotype\
    \ graph.\n  history_record: history/records/PF04149/2026-10-11T040001Z-codex-e346d1.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact tested object and domain mapping
  outcome: supported
  summary: The graph uses a verified member accession and explicitly limits its claim
    to the whole-gene experiment.
  target_ids:
  - PF04149
  evidence_ids:
  - protein-identity
  - primary-experiment
- assessment_id: edge-scope
  area: graph
  topic: Scoped direction without a fabricated biochemical mechanism
  outcome: supported
  summary: The required_for edge, conditional context and PHENOTYPIC/INDIRECT classification
    match the inspected evidence; no binding or catalysis edge was invented.
  target_ids:
  - PF04149
  evidence_ids:
  - primary-experiment
  - later-context
  - native-validation
- assessment_id: breadth
  area: completeness
  topic: Other characterized members and contexts
  outcome: concern
  summary: The current graph is useful but does not yet capture other experimentally
    investigated DUF397 systems.
  target_ids:
  - PF04149
  evidence_ids:
  - paralog-coverage
findings:
- finding_id: additional-systems
  issue_key: pf04149-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Additional characterized DUF397 contexts remain uncurated
  description: Review the other experimentally investigated systems independently
    before extending this record; preserve their distinct protein identities and medium-specific
    effects.
  target_ids:
  - PF04149
  field_paths:
  - causal_graphs
  evidence_ids:
  - paralog-coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF04149.yaml
    role: Human-owned graph curation
actions:
- action_id: extend-systems
  description: Assess the remaining DUF397 systems and add separately scoped graphs
    where the primary evidence supports direction.
  finding_ids:
  - additional-systems
  target_ids:
  - PF04149
  ownership_note: Curate the overlay and evidence extracts, append canonical history,
    regenerate and retain a successor review.
  acceptance_checks:
  - Each added edge has verified protein/domain identity, context and primary evidence.
  - No medium-specific effect is represented as universal family behavior.
  - Native record/graph checks pass and a successor review states the actual remaining
    coverage.
limitations:
- Same-agent scoped scientific assessment, not an independent expert review or replication
  of the experiments.
- Full supplements, all DUF397 members, and direct molecular intermediates were not
  exhaustively reviewed.
- PMC access challenges for later papers were worked around using the publisher and
  PubMed; no access failure was treated as negative evidence.
- This is one record in an 8296-family goal; the remaining 8295 families have not
  received scientific causal review.
- Publication, full QC and canonical Pages regeneration are separate unfinished steps;
  no REVIEWED promotion is requested.
notes:
- Applied the personal dufmech-causal-graphs skill together with the repository's
  native review and curation contracts.
- The initial repository inventory included hidden and ignored files and found no
  existing graph authoring surface; native support was added as a prerequisite to
  the requested graph work.
```
