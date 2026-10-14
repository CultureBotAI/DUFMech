# PF01885 CthTpt1 causal graph review

- Review: 20261011T051606Z-pf01885-cthtpt1-causal-graph
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T05:15:58Z
- Finished UTC: 2026-10-11T05:16:06Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Two terminal phosphate-removal endpoints are supported for the intact CthTpt1 construct; the approximately stoichiometric reactions are not generalized to all homologs or endogenous substrates.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Historical unknown-family record selected for substrate-specific primary biochemical evidence and explicit negative homolog controls.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01885 | data/families/PF01885.yaml | generated | PF01885 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01885 | Current projection validates and preserves the authored graphs exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01885.

The 2018 construct methods identify ABN54255.1, resolving to A3DJX6/kptA/Cthe_3059 from ATCC 27405, now Acetivibrio thermocellus. PF01885 spans residues 8-172 of the 182-residue reference, whereas the experiment used a complete ORF with an N-terminal His6 tag.

### Directed effects and limits

graph: supported. Targets: PF01885.

The two edges retain separate 2'- and 3'-terminal substrates and require the protein/NAD/substrate combination. Figure 1, T4 Pnkp mobility controls, omission controls and CIP challenges support the RNA hydroxyl-ended endpoints. The terminal assays are approximately stoichiometric, not demonstrated multiple-turnover catalysis. Proposed intermediate chemistry and native RNA roles are excluded.

### Remaining family coverage

completeness: concern. Targets: PF01885.

Canonical internal-phosphate activity, ADP-ribose capping, other positive homologs and biological substrates need independent scoped review. Runella and human terminal-activity negatives are retained as transfer limits, not family-wide absence. Figure 8 was assessed from text and caption, not its image.

## Findings

### additional-contexts: Additional Tpt1 reactions and member-specific biological contexts need review

minor / open / confirmed; issue key: pf01885-causal-context-coverage.

Review canonical internal-phosphate removal, capping and native-host evidence separately, retaining homolog-specific negative results and exact construct identity. Do not infer multiple turnover or an endogenous substrate from the terminal assay.

## Recommended Actions And Acceptance Checks

### extend-contexts

Review canonical internal-phosphate removal, capping and native-host evidence separately, retaining homolog-specific negative results and exact construct identity. Do not infer multiple turnover or an endogenous substrate from the terminal assay.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| experiment | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6573784/fullTextXML; Results, Figure 1 image and caption, captions 2-3 and 8, assay methods; cited 2018 recombinant-protein methods | supports | Purified CthTpt1 plus NAD supports terminal phosphate removal on separate synthetic 10-mers. Omission and phosphatase controls constrain product identity, and enzyme titration limits the turnover claim. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/A3DJX6/entry/pfam/PF01885/; Accession and domain locations; paired UniProt identity facts | supports | The 2018 construct methods identify ABN54255.1, resolving to A3DJX6/kptA/Cthe_3059 from ATCC 27405, now Acetivibrio thermocellus. PF01885 spans residues 8-172 of the 182-residue reference, whereas the experiment used a complete ORF with an N-terminal His6 tag. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, graph endpoints, evidence quotations and hashes, and canonical history pass; scientific validity is assessed separately. |
| duf-projection-pf01885 | data/families/PF01885.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Figure 1 was visually inspected; kinetic and homolog-comparison plots were assessed from text/captions only. Raw and supplementary data were not independently reanalyzed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T051606Z-pf01885-cthtpt1-causal-graph
title: PF01885 CthTpt1 causal graph review
started_at: '2026-10-11T05:15:58Z'
finished_at: '2026-10-11T05:16:06Z'
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
summary: Two terminal phosphate-removal endpoints are supported for the intact CthTpt1
  construct; the approximately stoichiometric reactions are not generalized to all
  homologs or endogenous substrates.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01885.yaml
    sha256: 781d77e2b5555b69c2b0306083499d49ecf3ed4f7fbbeea1e183d6ad725abf25
    role: context
  - path: data/families/PF01885.yaml
    sha256: 99b9494a65514c190c84f2c5dfddf5f48d5c20de7587c5e7f0fa86eb00da58d4
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
  - path: evidence/PF01885/munir-2019-cthtpt1.txt
    role: context
    sha256: 45ced6b757bc0663a6f3c749c5c8a0e9556f5f3609028c8e5850a0ca1e4b075f
  - path: evidence/PF01885/A3DJX6-identity.txt
    role: context
    sha256: 1fb0a274815b0e373d3abb22d0588ac41986a6814a023b084049845f02ee9b04
targets:
- target_id: PF01885
  path: data/families/PF01885.yaml
  label: PF01885
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01885.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 8802b12299f5f7038bd414c5669dd2278c13053d5d580c8d6d223c669d93a94d
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Historical unknown-family record selected for substrate-specific primary
    biochemical evidence and explicit negative homolog controls.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01885
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Canonical internal-phosphate activity, ADP-ribose capping, other positive
      homologs and biological substrates need independent scoped review. Runella and
      human terminal-activity negatives are retained as transfer limits, not family-wide
      absence. Figure 8 was assessed from text and caption, not its image.
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
  - PF01885
  evidence_ids:
  - native
evidence:
- evidence_id: experiment
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6573784/fullTextXML
  locator: Results, Figure 1 image and caption, captions 2-3 and 8, assay methods;
    cited 2018 recombinant-protein methods
  accessed_at: '2026-10-11T05:16:06Z'
  support: supports
  snapshot_sha256: 45ced6b757bc0663a6f3c749c5c8a0e9556f5f3609028c8e5850a0ca1e4b075f
  summary: Purified CthTpt1 plus NAD supports terminal phosphate removal on separate
    synthetic 10-mers. Omission and phosphatase controls constrain product identity,
    and enzyme titration limits the turnover claim.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/A3DJX6/entry/pfam/PF01885/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T05:16:06Z'
  support: supports
  snapshot_sha256: 1fb0a274815b0e373d3abb22d0588ac41986a6814a023b084049845f02ee9b04
  summary: The 2018 construct methods identify ABN54255.1, resolving to A3DJX6/kptA/Cthe_3059
    from ATCC 27405, now Acetivibrio thermocellus. PF01885 spans residues 8-172 of
    the 182-residue reference, whereas the experiment used a complete ORF with an
    N-terminal His6 tag.
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T05:16:06Z'
  support: supports
  summary: Closed schema, graph endpoints, evidence quotations and hashes, and canonical
    history pass; scientific validity is assessed separately.
- evidence_id: duf-projection-pf01885
  kind: record_content
  reference: data/families/PF01885.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T05:16:06Z'
  support: context_only
  snapshot_sha256: 99b9494a65514c190c84f2c5dfddf5f48d5c20de7587c5e7f0fa86eb00da58d4
  quote: "id: Pfam:PF01885\npfam_id: PF01885\nname: RNA 2'-phosphotransferase, Tpt1\
    \ / KptA family\nshort_name: PTS_2-RNA\nseed_status: EX_DUF\ncharacterization_status:\
    \ UNSCORED\ncuration_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01885\n\
    counters:\n  proteins: 8160\n  matches: 8272\n  proteomes: 6226\n  taxa: 12585\n\
    \  structures: 28\n  alphafold_models: 5779\n  domain_architectures: 192\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002745\ndescription: Tpt1 catalyses the last step of\
    \ tRNA splicing in yeast. It transfers the splice junction\n  2'-phosphate from\
    \ ligated tRNA to NAD, to produce ADP-ribose 1\"-2\"-cyclic phosphate. This is\
    \ presumed\n  to be followed by a transesterification step to release the RNA.\
    \ The first step of this reaction is\n  similar to that catalysed by some bacterial\
    \ toxins. E. coli KptA and mouse Tpt1 are likely to use the\n  same reaction mechanism\
    \ [[cite:PUB00008050]].\ncuration_history: history/records/PF01885\ncausal_graphs:\n\
    - graph_id: cthtpt1-terminal-phosphate-removal\n  title: CthTpt1-dependent RNA\
    \ terminal phosphate removal\n  scope: Purified full-length His6-CthTpt1 (ABN54255.1)\
    \ from Clostridium thermocellum ATCC 27405, expressed\n    in E. coli.\n  context:\
    \ Separate 10-mer AUCACGCUUA substrates bearing a terminal 2'- or 3'-phosphate;\
    \ 0.2 uM RNA, 0.5\n    uM enzyme, 1 mM NAD+, 100 mM Tris-HCl pH 7.5, 37 C, 30\
    \ minutes.\n  family_mapping: A3DJX6, kptA/Cthe_3059, sequence version 1, 182\
    \ residues; PF01885 spans reference residues\n    8-172. Current species name\
    \ is Acetivibrio thermocellus.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:203119\n\
    \  limitations: Terminal removal is approximately stoichiometric under these conditions,\
    \ not demonstrated\n    multiple-turnover catalysis. PAGE product assignment uses\
    \ T4 Pnkp and CIP controls. Intermediate chemistry,\n    endogenous substrates\
    \ and domain-only sufficiency are not established here; tested Runella and human\n\
    \    homologs lack equivalent terminal activity.\n  nodes:\n  - node_id: cthtpt1-2p-system\n\
    \    label: His6-CthTpt1 with NAD+ and terminal 2'-phosphate RNA\n    node_type:\
    \ STATE\n    grounding:\n    - UniProtKB:A3DJX6\n  - node_id: terminal-2p-removal\n\
    \    label: RNA terminal 2'-phosphate removal to 2'-OH\n    node_type: PROCESS\n\
    \  - node_id: cthtpt1-3p-system\n    label: His6-CthTpt1 with NAD+ and terminal\
    \ 3'-phosphate RNA\n    node_type: STATE\n    grounding:\n    - UniProtKB:A3DJX6\n\
    \  - node_id: terminal-3p-removal\n    label: RNA terminal 3'-phosphate removal\
    \ to 3'-OH\n    node_type: PROCESS\n  edges:\n  - edge_id: cthtpt1-enables-terminal-2p-removal\n\
    \    subject: cthtpt1-2p-system\n    predicate: enables\n    object: terminal-2p-removal\n\
    \    mechanism: The purified protein and NAD+ support loss of the terminal 2'-phosphate;\
    \ the RNA product\n      comigrates with the T4 Pnkp-generated hydroxyl-ended\
    \ control on denaturing PAGE.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:31019096\n\
    \      source_url: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6573784/fullTextXML\n\
    \      snippet: Removal of the 2'-PO4 and 3'-PO4 groups by CthTpt1 depended on\
    \ NAD+.\n      explanation: Figure 1 image, Results and assay methods support\
    \ this biochemical endpoint, with no-enzyme\n        and no-NAD+ controls. The\
    \ full intermediate pathway is not asserted.\n      cache_path: evidence/PF01885/munir-2019-cthtpt1.txt\n\
    \      cache_sha256: 45ced6b757bc0663a6f3c749c5c8a0e9556f5f3609028c8e5850a0ca1e4b075f\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/A3DJX6/entry/pfam/PF01885/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/A3DJX6/entry/pfam/PF01885/\n\
    \      snippet: 'entry accession: PF01885'\n      explanation: The experimental\
    \ accession maps to this reference protein and its Pfam interval, not\n      \
    \  an independently tested isolated domain.\n      cache_path: evidence/PF01885/A3DJX6-identity.txt\n\
    \      cache_sha256: 1fb0a274815b0e373d3abb22d0588ac41986a6814a023b084049845f02ee9b04\n\
    \  - edge_id: cthtpt1-enables-terminal-3p-removal\n    subject: cthtpt1-3p-system\n\
    \    predicate: enables\n    object: terminal-3p-removal\n    mechanism: In a\
    \ separate substrate assay, the purified protein and NAD+ support formation of\
    \ hydroxyl-ended\n      RNA from the terminal 3'-phosphate substrate; PAGE and\
    \ phosphatase challenges constrain product\n      assignment.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:31019096\n      source_url: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6573784/fullTextXML\n\
    \      snippet: Removal of the 2'-PO4 and 3'-PO4 groups by CthTpt1 depended on\
    \ NAD+.\n      explanation: Figure 1 image and Results distinguish this slower\
    \ terminal 3'-phosphate reaction from\n        the 2'-phosphate assay; a putative\
    \ intermediate is not a separate observed edge.\n      cache_path: evidence/PF01885/munir-2019-cthtpt1.txt\n\
    \      cache_sha256: 45ced6b757bc0663a6f3c749c5c8a0e9556f5f3609028c8e5850a0ca1e4b075f\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/A3DJX6/entry/pfam/PF01885/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/A3DJX6/entry/pfam/PF01885/\n\
    \      snippet: 'entry accession: PF01885'\n      explanation: The mapping anchors\
    \ the full-length construct to this family without transferring activity\n   \
    \     to all homologs.\n      cache_path: evidence/PF01885/A3DJX6-identity.txt\n\
    \      cache_sha256: 1fb0a274815b0e373d3abb22d0588ac41986a6814a023b084049845f02ee9b04\n\
    curation_events:\n- timestamp: '2026-10-11T05:13:11Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Add scoped CthTpt1 terminal RNA phosphate-removal\
    \ graph\n  history_record: history/records/PF01885/2026-10-11T051311Z-codex-bbd7f2.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: The 2018 construct methods identify ABN54255.1, resolving to A3DJX6/kptA/Cthe_3059
    from ATCC 27405, now Acetivibrio thermocellus. PF01885 spans residues 8-172 of
    the 182-residue reference, whereas the experiment used a complete ORF with an
    N-terminal His6 tag.
  target_ids:
  - PF01885
  evidence_ids:
  - identity
  - experiment
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: The two edges retain separate 2'- and 3'-terminal substrates and require
    the protein/NAD/substrate combination. Figure 1, T4 Pnkp mobility controls, omission
    controls and CIP challenges support the RNA hydroxyl-ended endpoints. The terminal
    assays are approximately stoichiometric, not demonstrated multiple-turnover catalysis.
    Proposed intermediate chemistry and native RNA roles are excluded.
  target_ids:
  - PF01885
  evidence_ids:
  - experiment
  - native
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Canonical internal-phosphate activity, ADP-ribose capping, other positive
    homologs and biological substrates need independent scoped review. Runella and
    human terminal-activity negatives are retained as transfer limits, not family-wide
    absence. Figure 8 was assessed from text and caption, not its image.
  target_ids:
  - PF01885
  evidence_ids:
  - experiment
findings:
- finding_id: additional-contexts
  issue_key: pf01885-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Additional Tpt1 reactions and member-specific biological contexts need review
  description: Review canonical internal-phosphate removal, capping and native-host
    evidence separately, retaining homolog-specific negative results and exact construct
    identity. Do not infer multiple turnover or an endogenous substrate from the terminal
    assay.
  target_ids:
  - PF01885
  field_paths:
  - causal_graphs
  evidence_ids:
  - experiment
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01885.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Review canonical internal-phosphate removal, capping and native-host
    evidence separately, retaining homolog-specific negative results and exact construct
    identity. Do not infer multiple turnover or an endogenous substrate from the terminal
    assay.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01885
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Figure 1 was visually inspected; kinetic and homolog-comparison plots were assessed
  from text/captions only. Raw and supplementary data were not independently reanalyzed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
