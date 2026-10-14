# PF01937 YMR027W causal graph review

- Review: 20261011T043437Z-pf01937-causal-graphs
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T04:33:18Z
- Finished UTC: 2026-10-11T04:34:37Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Two scoped graphs have primary experimental support and preserve the distinction between biochemical activity and a whole-gene phenotype. Family-wide coverage remains incomplete; retain IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the two YMR027W graphs, member mapping, source quotations, context and causal strength.

Selection: PF01937 chosen for accessible primary biochemical and perturbation evidence.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01937 | data/families/PF01937.yaml | generated | PF01937 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection validation | passed | True | PF01937 | Closed schema, graph semantics, quotations, hashes and canonical history pass. A preliminary call with an unsupported keyword was corrected before this successful run. |
| Graph, record, site, history and review-contract regressions | passed | True | PF01937 | 181 passed in the current worktree; structural checks are not biological evidence. |

## Scientific And Domain Assessments

### Tested member versus family scope

identity: supported. Targets: PF01937.

The graph distinguishes the reference protein, domain coordinates and whole-gene perturbation.

### Direct biochemical evidence versus indirect phenotype

graph: supported. Targets: PF01937.

Direction and experimental context are preserved without adding unsupported atomic intermediates, flux or DNA-damage arrows.

### Other members and mechanisms

completeness: concern. Targets: PF01937.

Additional substrates, subfamilies and later primary studies still need individual assessment.

## Findings

### additional-members: DUF89 member and substrate coverage remains partial

minor / open / confirmed; issue key: pf01937-causal-member-coverage.

Extend research beyond the two YMR027W contexts, including the other tested subfamilies and later work on fission-yeast paralogs and PANK4; verify identity and conditions before transfer.

## Recommended Actions And Acceptance Checks

### extend-members

Research additional member-specific primary evidence and retain a successor review.

- Each added edge has exact protein or construct mapping, context, direction and primary support.
- Unsupported transfers and conflicting results remain explicit.
- Native validation and successor review report actual, not presumed, coverage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| experiments | https://escholarship.org/content/qt69w784bv/qt69w784bv.pdf; Results pages 3-5; Figure 2e and 4b captions; methods pages 12-13 | supports | Purified-protein phosphate release and deletion-strain metabolite accumulation support separate scoped arrows, not a directly observed intracellular reaction sequence. |
| member-identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q04371/entry/pfam/PF01937/; Protein accession, PF01937 entry_protein_locations; paired UniProt sequence version and locus | supports | Q04371 maps YMR027W to PF01937; reference sequence coordinates are not an isolated-domain assay or a verified deletion-strain sequence. |
| native-checks | tests/test_causal_graphs.py; Current projection validation and 181-test focused run | supports | The effective graph representation validates without modifying frozen identity, scoring or source metadata. |
| duf-projection-pf01937 | data/families/PF01937.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Same-agent assessment, not independent expert endorsement or experimental replication.
- Full-text Results, methods and captions were inspected; plotted figure images and supplementary data were not independently visually checked.
- No comprehensive family review, REVIEWED promotion, publication or full publication-QC pass is claimed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T043437Z-pf01937-causal-graphs
kind: record
repository: CultureBotAI/DUFMech
title: PF01937 YMR027W causal graph review
started_at: '2026-10-11T04:33:18Z'
finished_at: '2026-10-11T04:34:37Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent curated the graphs; no independent expert review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: true
summary: Two scoped graphs have primary experimental support and preserve the distinction
  between biochemical activity and a whole-gene phenotype. Family-wide coverage remains
  incomplete; retain IN_PROGRESS.
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01937.yaml
    role: context
    sha256: 8116de45ba0c11b5976b5e698020ea0c244d7bef475cb72570e1d728b9b9abdb
  - path: data/families/PF01937.yaml
    role: target
    sha256: 5f719354e03732b44e44751f31b51ee65e51dc51cdbc39e1d770670da5936bae
  - path: data/worklists/interpro-pfam-duf-2026-10-10.json
    role: context
    sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383
  - path: data/worklists/interpro-pfam-duf-2026-10-10.manifest.json
    role: context
    sha256: 31c07ffb6a169c851ea0e6e9dd527a10c04028eafeb29187bd62dc2ae848696e
  - path: data/worklists/interpro-pfam-duf-2026-10-10.tsv
    role: context
    sha256: be023c8dd9d8d3864926b5032d6f7e87a884b1a567391696822dbbecc692dae7
  - path: evidence/PF01937/huang-2016-ymr027w.txt
    role: context
    sha256: c82c18e03d76ab968345dd867ad39fc635bfe11cf00b30ab3ec77fe51c912e2e
  - path: evidence/PF01937/Q04371-identity.txt
    role: context
    sha256: 77738fb3e37e47aa46642f35917d6ff4780ddd822a5d3b13f14235435a508c74
targets:
- kind: generated
  label: PF01937
  path: data/families/PF01937.yaml
  record_class: FamilyRecord
  target_id: PF01937
  owner_paths:
  - path: curation/families/PF01937.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: 7670b39f183d8dc73124ac70b25b6d2370f7ba31a814aac20dd0ec28c83108dd
scope:
  description: Scientific assessment of the two YMR027W graphs, member mapping, source
    quotations, context and causal strength.
  selection: PF01937 chosen for accessible primary biochemical and perturbation evidence.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01937
  exclusions:
  - target: Other DUF89 members, substrates and later studies
    reason: This review does not exhaustively assess the family's literature or characterize
      every subfamily.
checks:
- check_id: native-projection
  name: Native projection validation
  command: validate_record(load_yaml(Path('data/families/PF01937.yaml')), Path.cwd())
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Closed schema, graph semantics, quotations, hashes and canonical history
    pass. A preliminary call with an unsupported keyword was corrected before this
    successful run.
  target_ids:
  - PF01937
  evidence_ids:
  - native-checks
- check_id: focused-regressions
  name: Graph, record, site, history and review-contract regressions
  command: PYTHONPATH=src:/private/tmp/dufmech-classification-claw/src .venv/bin/python
    -m pytest tests/test_causal_graphs.py tests/test_records.py tests/test_site.py
    tests/test_history.py tests/test_record_review_contract.py -q
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 181 passed in the current worktree; structural checks are not biological
    evidence.
  target_ids:
  - PF01937
  evidence_ids:
  - native-checks
evidence:
- evidence_id: experiments
  kind: primary_source
  reference: https://escholarship.org/content/qt69w784bv/qt69w784bv.pdf
  locator: Results pages 3-5; Figure 2e and 4b captions; methods pages 12-13
  accessed_at: '2026-10-11T04:34:13Z'
  support: supports
  summary: Purified-protein phosphate release and deletion-strain metabolite accumulation
    support separate scoped arrows, not a directly observed intracellular reaction
    sequence.
  snapshot_sha256: c82c18e03d76ab968345dd867ad39fc635bfe11cf00b30ab3ec77fe51c912e2e
- evidence_id: member-identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q04371/entry/pfam/PF01937/
  locator: Protein accession, PF01937 entry_protein_locations; paired UniProt sequence
    version and locus
  accessed_at: '2026-10-11T04:33:18Z'
  support: supports
  summary: Q04371 maps YMR027W to PF01937; reference sequence coordinates are not
    an isolated-domain assay or a verified deletion-strain sequence.
  snapshot_sha256: 77738fb3e37e47aa46642f35917d6ff4780ddd822a5d3b13f14235435a508c74
- evidence_id: native-checks
  kind: validation
  reference: tests/test_causal_graphs.py
  locator: Current projection validation and 181-test focused run
  accessed_at: '2026-10-11T04:34:37Z'
  support: supports
  summary: The effective graph representation validates without modifying frozen identity,
    scoring or source metadata.
- evidence_id: duf-projection-pf01937
  kind: record_content
  reference: data/families/PF01937.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T04:34:37Z'
  support: context_only
  snapshot_sha256: 5f719354e03732b44e44751f31b51ee65e51dc51cdbc39e1d770670da5936bae
  quote: "id: Pfam:PF01937\npfam_id: PF01937\nname: Damage-control phosphatase ARMT1-like\
    \ domain\nshort_name: ARMT1-like_dom\nseed_status: EX_DUF\ncharacterization_status:\
    \ UNSCORED\ncuration_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01937\n\
    counters:\n  proteins: 9217\n  matches: 9512\n  proteomes: 4951\n  taxa: 11762\n\
    \  structures: 16\n  alphafold_models: 7564\n  domain_architectures: 110\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002791\ndescription: This domain is widely distributed\
    \ in all domains of life and occur in stand-alone form and\n  as C-terminal fusions\
    \ to pantothenate kinase (PanK) in plants and animals. They are metal-dependent\n\
    \  phosphatases involved in metabolic damage-control processes termed \"damage\
    \ pre-emption\" or \"housecleaning\".\n  S.cerevisiae Damage-control phosphatase\
    \ YMR027W and the human orthologue Damage-control phosphatase\n  ARMT1 (also known\
    \ as C6orf211) are involved in response to DNA damage, a damage pre-emption function.\n\
    \  Crystal structure of Damage-control phosphatase At2g17340 from Arabidopsis\
    \ revealed a novel protein\n  fold and several conserved residues coordinating\
    \ a metal ion (probably Mg2+), which exhibits a high\n  degree of conservation,\
    \ suggesting that the metal-binding site is central for the function [[cite:PUB00088733]].\n\
    curation_history: history/records/PF01937\ncausal_graphs:\n- graph_id: ymr027w-f1p-hydrolysis\n\
    \  title: YMR027W fructose-1-phosphate hydrolysis\n  scope: Recombinant S. cerevisiae\
    \ YMR027W, mapped to UniProtKB:Q04371; not every DUF89 member.\n  context: Purified\
    \ enzyme; 0.25 mM fructose-1-phosphate, 0.1 mM Co2+, 30 C.\n  family_mapping:\
    \ Q04371 sequence version 1 has 470 residues; InterPro maps PF01937 to 19-437.\
    \ The assay\n    uses the protein, not an isolated 19-437 construct.\n  scope_status:\
    \ MECHANISTIC\n  taxon: NCBITaxon:559292\n  limitations: Does not establish the\
    \ physiological metal or individual catalytic intermediates. Other\n    substrates\
    \ and subfamilies require separate scope.\n  nodes:\n  - node_id: metal-supported-enzyme\n\
    \    label: Purified YMR027W activity with cobalt and substrate\n    node_type:\
    \ ACTIVITY\n    grounding:\n    - UniProtKB:Q04371\n  - node_id: f1p-hydrolysis\n\
    \    label: Fructose-1-phosphate dephosphorylation\n    node_type: PROCESS\n \
    \ edges:\n  - edge_id: enzyme-enables-hydrolysis\n    subject: metal-supported-enzyme\n\
    \    predicate: enables\n    object: f1p-hydrolysis\n    mechanism: The purified\
    \ protein hydrolyzes this phosphoester; phosphate release is measured.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:27322068\n      source_url: https://escholarship.org/content/qt69w784bv/qt69w784bv.pdf\n\
    \      snippet: fructose 1- and 6-phosphates for YMR027W\n      explanation: Results\
    \ p. 4 and Figure 2e; enzyme-assay methods p. 12 describe Malachite Green detection\n\
    \        and replicate assays.\n      cache_path: evidence/PF01937/huang-2016-ymr027w.txt\n\
    \      cache_sha256: c82c18e03d76ab968345dd867ad39fc635bfe11cf00b30ab3ec77fe51c912e2e\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q04371/entry/pfam/PF01937/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q04371/entry/pfam/PF01937/\n\
    \      snippet: 'entry accession: PF01937'\n      explanation: Member/domain identity\
    \ and coordinates only; the paired UniProt extraction establishes\n        sequence\
    \ version, length and locus.\n      cache_path: evidence/PF01937/Q04371-identity.txt\n\
    \      cache_sha256: 77738fb3e37e47aa46642f35917d6ff4780ddd822a5d3b13f14235435a508c74\n\
    - graph_id: ymr027w-deletion-f1p\n  title: YMR027W deletion and fructose-1-phosphate\
    \ abundance\n  scope: S. cerevisiae diploid deletion strain Y30602 versus wild-type\
    \ BY4743; whole-gene perturbation.\n  context: Supplemented SD with 2% fructose,\
    \ 30 C, harvested at OD600 0.5.\n  family_mapping: YMR027W maps to reference UniProtKB:Q04371\
    \ and PF01937 at 19-437. Reference sequence\n    coordinates are not an isolated-domain\
    \ experiment in BY4743.\n  scope_status: PHENOTYPIC\n  limitations: No direct\
    \ intracellular reaction sequence or DNA-damage edge inferred. Rescue was not\
    \ assessed\n    in this curation; other growth conditions remain separate.\n \
    \ nodes:\n  - node_id: ymr027w-deletion\n    label: YMR027W deletion\n    node_type:\
    \ PERTURBATION\n  - node_id: cellular-f1p\n    label: Cellular fructose-1-phosphate\
    \ abundance\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: deletion-increases-f1p\n\
    \    subject: ymr027w-deletion\n    predicate: increases\n    object: cellular-f1p\n\
    \    mechanism: Gene deletion increases the measured metabolite pool relative\
    \ to the matched wild type.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:27322068\n\
    \      source_url: https://escholarship.org/content/qt69w784bv/qt69w784bv.pdf\n\
    \      snippet: significant accumulation\n      explanation: Results p. 5 and\
    \ Figure 4b; GC-MS and growth conditions in methods p. 13. A pool measurement\n\
    \        does not itself measure flux.\n      cache_path: evidence/PF01937/huang-2016-ymr027w.txt\n\
    \      cache_sha256: c82c18e03d76ab968345dd867ad39fc635bfe11cf00b30ab3ec77fe51c912e2e\n\
    \    - reference: https://rest.uniprot.org/uniprotkb/Q04371.json\n      source_url:\
    \ https://rest.uniprot.org/uniprotkb/Q04371.json\n      snippet: 'orderedLocusNames:\
    \ YMR027W'\n      explanation: Reference-member mapping only, not independent\
    \ experimental support or proof of the\n        deletion strain's sequence.\n\
    \      cache_path: evidence/PF01937/Q04371-identity.txt\n      cache_sha256: 77738fb3e37e47aa46642f35917d6ff4780ddd822a5d3b13f14235435a508c74\n\
    curation_events:\n- timestamp: '2026-10-11T04:26:58Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate separate YMR027W enzyme and deletion\
    \ causal graphs\n  history_record: history/records/PF01937/2026-10-11T042658Z-codex-6fb381.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Tested member versus family scope
  outcome: supported
  summary: The graph distinguishes the reference protein, domain coordinates and whole-gene
    perturbation.
  target_ids:
  - PF01937
  evidence_ids:
  - member-identity
  - experiments
- assessment_id: causal-strength
  area: graph
  topic: Direct biochemical evidence versus indirect phenotype
  outcome: supported
  summary: Direction and experimental context are preserved without adding unsupported
    atomic intermediates, flux or DNA-damage arrows.
  target_ids:
  - PF01937
  evidence_ids:
  - experiments
  - native-checks
- assessment_id: remaining-coverage
  area: completeness
  topic: Other members and mechanisms
  outcome: concern
  summary: Additional substrates, subfamilies and later primary studies still need
    individual assessment.
  target_ids:
  - PF01937
  evidence_ids:
  - experiments
findings:
- finding_id: additional-members
  issue_key: pf01937-causal-member-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: DUF89 member and substrate coverage remains partial
  description: Extend research beyond the two YMR027W contexts, including the other
    tested subfamilies and later work on fission-yeast paralogs and PANK4; verify
    identity and conditions before transfer.
  target_ids:
  - PF01937
  field_paths:
  - causal_graphs
  evidence_ids:
  - experiments
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01937.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-members
  description: Research additional member-specific primary evidence and retain a successor
    review.
  finding_ids:
  - additional-members
  target_ids:
  - PF01937
  ownership_note: Curate overlay and evidence, append canonical history, regenerate
    guarded projections.
  acceptance_checks:
  - Each added edge has exact protein or construct mapping, context, direction and
    primary support.
  - Unsupported transfers and conflicting results remain explicit.
  - Native validation and successor review report actual, not presumed, coverage.
limitations:
- Same-agent assessment, not independent expert endorsement or experimental replication.
- Full-text Results, methods and captions were inspected; plotted figure images and
  supplementary data were not independently visually checked.
- No comprehensive family review, REVIEWED promotion, publication or full publication-QC
  pass is claimed.
```
