# PF17042 ReDtnK causal graph review

- Review: 20261011T050318Z-pf17042-redtnk-causal-graph
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T05:02:46Z
- Finished UTC: 2026-10-11T05:03:18Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The same intact ReDtnK reaction is supported with its C-terminal mapping; it is not a second experiment or proof of an independently active domain.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Former DUF1537 C-terminal family selected alongside the N-terminal record to preserve the current two-domain identity boundary.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF17042 | data/families/PF17042.yaml | generated | PF17042 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF17042 | Current projection validates and preserves the authored graphs exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF17042.

Q0K4F6 is H16_B0318 from current Cupriavidus necator H16, the article's Ralstonia eutropha H16. PF17042 spans 246-400, with PF07005 at 4-223 in the same 415-residue reference.

### Directed effects and limits

graph: supported. Targets: PF17042.

The accession-specific kinetic experiment supports intact-protein catalysis. It is retained under both mapped domains with explicit shared provenance, not duplicated as independent evidence or recast as a C-terminal-only reaction.

### Remaining family coverage

completeness: concern. Targets: PF17042.

Additional nucleotide-binding-domain members, alternate kinase substrates, genetic contexts and construct details remain outside the completed scope.

## Findings

### additional-contexts: Additional DUF1537 C-terminal contexts and members need assessment

minor / open / confirmed; issue key: pf17042-causal-context-coverage.

Review other members and construct-specific assays before extending the C-terminal record. Preserve whole-protein and domain-only evidence distinctions and the shared experiment with PF07005.

## Recommended Actions And Acceptance Checks

### extend-contexts

Review other members and construct-specific assays before extending the C-terminal record. Preserve whole-protein and domain-only evidence distinctions and the shared experiment with PF07005.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| experiment | https://www.osti.gov/servlets/purl/1329421; Table 1 and biochemical Results on E4163; kinetic assay methods on E4168; both pages rendered and inspected | supports | ReDtnK kinetics and explicit assay conditions support the intact two-domain enzyme's activity; nucleotide binding alone is not used as causal proof. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q0K4F6/entry/pfam/PF17042/; Accession and domain locations; paired UniProt identity facts | supports | Q0K4F6 is H16_B0318 from current Cupriavidus necator H16, the article's Ralstonia eutropha H16. PF17042 spans 246-400, with PF07005 at 4-223 in the same 415-residue reference. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, graph endpoints, evidence quotations and hashes, and canonical history pass; scientific validity is assessed separately. |
| duf-projection-pf17042 | data/families/PF17042.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Rendered main-paper pages E4163 and E4168 were visually inspected; supplementary construct, product and growth evidence were not independently reviewed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T050318Z-pf17042-redtnk-causal-graph
title: PF17042 ReDtnK causal graph review
started_at: '2026-10-11T05:02:46Z'
finished_at: '2026-10-11T05:03:18Z'
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
summary: The same intact ReDtnK reaction is supported with its C-terminal mapping;
  it is not a second experiment or proof of an independently active domain.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF17042.yaml
    sha256: 64c322328483f97c8cbca5dde239ba41c2d641cf69a7aa2aaf7ab1bfba3391e7
    role: context
  - path: data/families/PF17042.yaml
    sha256: c32e15d111978d08aa97016160743966f44856f6ea4dd8bb8d4ebc6d90c0faf3
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
  - path: evidence/PF07005/zhang-2016-dtnk.txt
    role: context
    sha256: 70418e45db58d9036f10aab982891b974c16090ff5230d7ff733d8d1f2290c29
  - path: evidence/PF07005/Q0K4F6-identity.txt
    role: context
    sha256: 7d2525e5d02f57e674af1c7891732ac1fe5b713fe82451f88c6f7d053de57989
targets:
- target_id: PF17042
  path: data/families/PF17042.yaml
  label: PF17042
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF17042.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 61d1a100d5e956d4b04ed125ba648870e7df8292fb238688ccb339ef89263ada
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Former DUF1537 C-terminal family selected alongside the N-terminal record
    to preserve the current two-domain identity boundary.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF17042
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Additional nucleotide-binding-domain members, alternate kinase substrates,
      genetic contexts and construct details remain outside the completed scope.
checks:
- check_id: native-projection
  name: Native projection and overlay validation
  command: validate_record(record, root); assert projection causal_graphs == overlay
    causal_graphs
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Current projection validates and preserves the authored graphs exactly.
  target_ids:
  - PF17042
  evidence_ids:
  - native
evidence:
- evidence_id: experiment
  kind: primary_source
  reference: https://www.osti.gov/servlets/purl/1329421
  locator: Table 1 and biochemical Results on E4163; kinetic assay methods on E4168;
    both pages rendered and inspected
  accessed_at: '2026-10-11T05:03:18Z'
  support: supports
  snapshot_sha256: 70418e45db58d9036f10aab982891b974c16090ff5230d7ff733d8d1f2290c29
  summary: ReDtnK kinetics and explicit assay conditions support the intact two-domain
    enzyme's activity; nucleotide binding alone is not used as causal proof.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q0K4F6/entry/pfam/PF17042/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T05:03:18Z'
  support: supports
  snapshot_sha256: 7d2525e5d02f57e674af1c7891732ac1fe5b713fe82451f88c6f7d053de57989
  summary: Q0K4F6 is H16_B0318 from current Cupriavidus necator H16, the article's
    Ralstonia eutropha H16. PF17042 spans 246-400, with PF07005 at 4-223 in the same
    415-residue reference.
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T05:03:18Z'
  support: supports
  summary: Closed schema, graph endpoints, evidence quotations and hashes, and canonical
    history pass; scientific validity is assessed separately.
- evidence_id: duf-projection-pf17042
  kind: record_content
  reference: data/families/PF17042.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T05:03:18Z'
  support: context_only
  snapshot_sha256: c32e15d111978d08aa97016160743966f44856f6ea4dd8bb8d4ebc6d90c0faf3
  quote: "id: Pfam:PF17042\npfam_id: PF17042\nname: Nucleotide-binding C-terminal\
    \ domain\nshort_name: NBD_C\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF17042\n\
    counters:\n  proteins: 9377\n  matches: 9386\n  proteomes: 6036\n  taxa: 9738\n\
    \  structures: 7\n  alphafold_models: 5700\n  domain_architectures: 80\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR031475\ndescription: This is the C-terminal domain found\
    \ in proteins in a range of Proteobacteria as well as the\n  Gram-positive Oceanobacillus\
    \ iheyensis. Structural analysis of the whole protein indicates the N- and\n \
    \ C-termini act together to produce a surface into which a threonate-ADP complex\
    \ is bound, demonstrating\n  that a sugar binding site is on the N-terminal domain,\
    \ and a nucleotide binding site is in the C-terminal\n  domain [[cite:PUB00085179]].\
    \ There is a critical motif, DDXTG, at approximately residues 22-25. Proteins\n\
    \  containing this domain have been predicted as kinases. Some members are associated\
    \ with PdxA2 by physical\n  clustering and gene fusion with PdxA2. Some members\
    \ that are fused with PdxA2 have been shown to be\n  involved in L-4-hydroxythreonine\
    \ (4HT) phosphorylation, part of the alternative pathway to make PLP\n  (pyridoxal\
    \ 5'-phosphate) out of a toxic metabolite, 4HT. However, 4HT phosphorylation might\
    \ not be the\n  main function of this group of proteins. Moreover, some members\
    \ that are not associated with pdxA2,\n  and even one that is associated with\
    \ pdxA2, have lost 4HT kinase activity [[cite:PUB00083215]]. Functional\n  analysis\
    \ demonstrate that family members include D-Threonate kinases (DtnK), D-Erythronate\
    \ kinases (DenK)\n  and 3-Oxo-tetronate kinases (OtnK) [[cite:PUB00085179]].\n\
    curation_history: history/records/PF17042\ncausal_graphs:\n- graph_id: redtnk-d-threonate-phosphorylation\n\
    \  title: Intact ReDtnK phosphorylation of D-threonate\n  scope: Purified ReDtnK\
    \ Q0K4F6 from Ralstonia eutropha H16, currently Cupriavidus necator H16; whole-protein\n\
    \    activity.\n  context: ATP-dependent assay at 25 C, Tris-HCl pH 8.0, MgCl2\
    \ and KCl; ADP readout coupled through PK/LDH\n    to NADH consumption.\n  family_mapping:\
    \ Q0K4F6, sequence version 1, 415 residues; PF17042 spans 246-400 and PF07005\
    \ spans 4-223.\n    This record maps the C-terminal domain within the assayed\
    \ intact enzyme.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:381666\n  limitations:\
    \ Neither isolated domain was assayed for sufficiency. Exact purification-tag\
    \ details and\n    supplementary product/growth data were not independently checked.\
    \ This is the same experiment retained\n    with PF07005, not independent replication;\
    \ substrate specificity is not transferred to every member.\n  nodes:\n  - node_id:\
    \ redtnk-atp-d-threonate\n    label: Intact ReDtnK with ATP, Mg and D-threonate\n\
    \    node_type: STATE\n    grounding:\n    - UniProtKB:Q0K4F6\n  - node_id: d-threonate-phosphorylation\n\
    \    label: D-threonate phosphorylation to D-threonate 4-phosphate\n    node_type:\
    \ PROCESS\n  edges:\n  - edge_id: redtnk-enables-d-threonate-phosphorylation\n\
    \    subject: redtnk-atp-d-threonate\n    predicate: enables\n    object: d-threonate-phosphorylation\n\
    \    mechanism: The purified intact kinase transfers phosphate from ATP to D-threonate;\
    \ Table 1 quantifies\n      the substrate-dependent activity.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:27402745\n      source_url: https://www.osti.gov/servlets/purl/1329421\n\
    \      snippet: ATP-dependent phosphorylation\n      explanation: Table 1 and\
    \ biochemical Results on E4163, with kinetic methods on E4168; the assay\n   \
    \     measures ADP through a coupling system, not direct product mass spectrometry.\n\
    \      cache_path: evidence/PF07005/zhang-2016-dtnk.txt\n      cache_sha256: 70418e45db58d9036f10aab982891b974c16090ff5230d7ff733d8d1f2290c29\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q0K4F6/entry/pfam/PF17042/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q0K4F6/entry/pfam/PF17042/\n\
    \      snippet: 'entry accession: PF17042'\n      explanation: C-terminal Pfam\
    \ mapping in the tested DtnK reference sequence; both modern domains\n       \
    \ are retained in this full-protein context.\n      cache_path: evidence/PF07005/Q0K4F6-identity.txt\n\
    \      cache_sha256: 7d2525e5d02f57e674af1c7891732ac1fe5b713fe82451f88c6f7d053de57989\n\
    curation_events:\n- timestamp: '2026-10-11T04:59:21Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate intact ReDtnK activity with its\
    \ C-terminal domain mapping\n  history_record: history/records/PF17042/2026-10-11T045921Z-codex-747a47.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Q0K4F6 is H16_B0318 from current Cupriavidus necator H16, the article's
    Ralstonia eutropha H16. PF17042 spans 246-400, with PF07005 at 4-223 in the same
    415-residue reference.
  target_ids:
  - PF17042
  evidence_ids:
  - identity
  - experiment
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: The accession-specific kinetic experiment supports intact-protein catalysis.
    It is retained under both mapped domains with explicit shared provenance, not
    duplicated as independent evidence or recast as a C-terminal-only reaction.
  target_ids:
  - PF17042
  evidence_ids:
  - experiment
  - native
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Additional nucleotide-binding-domain members, alternate kinase substrates,
    genetic contexts and construct details remain outside the completed scope.
  target_ids:
  - PF17042
  evidence_ids:
  - experiment
findings:
- finding_id: additional-contexts
  issue_key: pf17042-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Additional DUF1537 C-terminal contexts and members need assessment
  description: Review other members and construct-specific assays before extending
    the C-terminal record. Preserve whole-protein and domain-only evidence distinctions
    and the shared experiment with PF07005.
  target_ids:
  - PF17042
  field_paths:
  - causal_graphs
  evidence_ids:
  - experiment
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF17042.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Review other members and construct-specific assays before extending
    the C-terminal record. Preserve whole-protein and domain-only evidence distinctions
    and the shared experiment with PF07005.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF17042
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Rendered main-paper pages E4163 and E4168 were visually inspected; supplementary
  construct, product and growth evidence were not independently reviewed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
