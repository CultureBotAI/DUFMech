# PF01981 PTH2 hydrolysis, complementation and assay contexts

- Review: 20261015T233126Z-pf01981-pth2-causal-contexts
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-15T23:18:16Z
- Finished UTC: 2026-10-15T23:31:26Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Nine scoped graphs with16observed experimental edges advance previously seeded PF01981. Protein references, historical constructs and current retired-accession provenance remain distinct. Three open scientific follow-ups prevent full-family completion; IN_PROGRESS remains appropriate.

## Scope And Provenance

Assess every new edge for identity, direction, experimental context, evidence integrity and limits. Original2002/2003 Methods, Results, tables and Figure1 captions plus2026 main text/Table1/Table3/Figure5 image inspected. Partial family coverage, not a literature census.

Selection: First untouched seed after the earlier scoped PF01980 batch; historical DUF119/UPF0099 identity verified from the frozen prior-name mapping.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base cdb58f7e72774c96529b4267ae25b99460ff5e21.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01981 | data/families/PF01981.yaml | generated | PF01981 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| generation | passed | True | PF01981 | 8296schema-valid records; exactlyPF01981andmanifest regenerated after actualCREATE/EDIThistory. |
| focused | passed | True | PF01981 | 52tests passed in22.97s; structural invalidity, scope/digest/evidence guards and QC orchestration tested, not scientific truth. |
| schema-history | passed | True | PF01981 | Generated schema current and pre-review canonical history validates. |
| inventory-exports | passed | True | PF01981 | 899graphs/1936edges in130families;8166graphless. Association exports reflect only thePF01981status change. |
| integrity | passed | True | PF01981 | All8296manifest hashes and16quote/hash anchors pass; onlyPF01981changes, with all earlier tracked scientific/artifact inputs preserved. |
| preview | passed | True | PF01981 | Exact native unpinned JSON;1440px/390px,9graphs/16observed edges,all16working disclosures and4/10/2primary links;no document overflow or JS errors. Selected screenshots inspected. |

## Scientific And Domain Assessments

### Frozen family versus exact tested proteins

identity: supported. Targets: PF01981.

Verified historical names and mapped references. Current yeast numbering is not retrofitted onto old constructs. The retired Lokiarchaeum accession is explicitly historical; identical core sequence links the archived Pfam assignment to the assay.

### Directed experimental relations without scope inflation

graph: supported. Targets: PF01981.

All16edges reviewed. Purified substrate reactions are DIRECT/MECHANISTIC; bacterial rescue is INDIRECT/PHENOTYPIC; ionic, inhibitor and temperature responses keep UNRESOLVED molecular directness. Contexts and conjunctive reaction inputs remain separate.

### Minimal extracts and negative/conflicting observations

evidence: supported. Targets: PF01981.

Quoted fragments anchor precise source locators and own factual ledgers. No paper/figure redistribution. Native yeast negatives, full-length discrepancy, substrate units and structural hypotheses are retained rather than converted to unsupported edges.

### Authoring ownership and whole-corpus preservation

provenance: supported. Targets: PF01981.

Maintained overlay/evidence and actual CREATE/EDIT history own the curation. Native generation changes onlyPF01981andmanifest; previous evidence/reviews/history/overlays, frozen inputs and canonical Pages/pins remain byte-unchanged.

### Remaining residue, construct and family work

completeness: concern. Targets: PF01981.

The initial three-study assessment is incomplete family coverage; three open discussions and findings identify next evidence work. No REVIEWED promotion.

## Findings

### constructs-and-domain-mapping: Resolve exact historical constructs and residue mechanisms

minor / open / confirmed; issue key: pf01981-constructs-and-domain-mapping.

Current reference coordinates are not independently verified physical inserts. Historical yeast numbering and current Lokiarchaeum HMM coordinates remain unresolved. Original2005 mutants need full assay/control inspection before atomic claims.

### discrepancies-and-physiology: Resolve source discrepancies and physiological interpretation

minor / open / confirmed; issue key: pf01981-discrepancies-and-physiology.

Full-length yeast complementation outcomes differ across hosts/vectors. Source concentration/ionic/resolution discrepancies remain explicit. Native localization, thermal ecology and proposed toxicity/structural mechanisms are not established by these edges.

### family-and-literature-coverage: Continue additional exact-member and primary-study coverage

minor / open / confirmed; issue key: pf01981-family-and-literature-coverage.

Yeast UBL/proteasome and human PTRH2/BIT1 roles, other archaeal members, original residue experiments and uninspected images/supplements remain outstanding. This is not complete family review.

## Recommended Actions And Acceptance Checks

### extend-pth2-evidence

Resolve the scoped unknowns and extend primary experimental coverage without erasing negative results or merging incompatible constructs.

- Verify historical inserts/sequence remapping and current domain coordinates, or retain explicit unresolved scope.
- Inspect original residue-mutant assays, controls and structural/biochemical limitations before causal residue chemistry.
- Resolve source discrepancies using original data or author clarification; otherwise retain them without stronger claims.
- Review the remaining primary/member contexts, preserve negative and conflicting evidence, and append successor reviews/history.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| rosas | https://pmc.ncbi.nlm.nih.gov/articles/PMC139208/; Methods; recombinant enzyme and complementation Results; Figure1 caption; Table1; yeast deletion results; evidence/PF01981/rosas2002.txt | supports | Supports separate purified MJ0051 substrate reactions and bounded bacterial rescue; preserves yeast full-length failure and native deletion negatives. |
| fromant | https://pmc.ncbi.nlm.nih.gov/articles/PMC162332/; Methods; Results; Tables1-7; Figure1 caption; evidence/PF01981/fromant2003.txt | supports | Supports substrate-specific hydrolysis, separate ionic additions, uncharged-tRNA inhibition and two heterologous rescue contexts; excludes Pth1 phenotype transfer. |
| kawashima | https://pmc.ncbi.nlm.nih.gov/articles/PMC13523710/; Methods2.1/2.5, Table1, Table3, Results3.1-3.3, original Figure5 image/caption; evidence/PF01981/kawashima2026.txt | supports | Supports the tested temperature contrasts, not native growth, irreversible unfolding or atomic residue mechanisms. Crystal and assay constructs differ. |
| mapping | evidence/PF01981/member-mapping.txt; Dated UniProt, InterPro, SIFTS and RCSB payload identities/hashes; UniSave archived entry19 and explicit current inactive response | supports | Exact reference mappings and archived-core comparison support family assignment while retaining coordinate, taxonomy and physical-construct limitations. |
| validation | data/families/PF01981.yaml; Native generation/schema/history,52focused tests, structural inventory/exports, integrity and native local preview/browser checks | supports | All8296manifest hashes, other8295records and earlier tracked artifacts preserved; exact JSON, direction labels and all16evidence disclosures checked. |
| duf-projection-pf01981 | data/families/PF01981.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- The8296-record goal remains active.130graph-bearing families are structural presence, not130completed scientific reviews.
- All16edges are observed at their declared assay/phenotype scope; none claims an observed proton transfer, nucleophile, salt-bridge switch or localization mechanism.
- 2002substrate concentration units,2003Table6 ionic conditions and2026structure resolution differ within their sources; no silent numerical correction.
- Historical yeast truncation numbering is not current P34222 numbering. Full-length rescue/failure experiments use different hosts/vectors and remain separate.
- A0A0F9U5Y0 is currently deleted; archived entry19 retains PF01981 and its118-aa core matches the paper/deposition. Current HMM boundary coordinates remain unresolved.
- XML retrieval returned500; older figure access included a browser challenge and a caption-only result;2026supplement download did not yield inspected content. These are access limits, not negative findings.
- No new source pipeline, functional score, frozen snapshot, runtime change, publication or independent scientific endorsement.
- Initial browser checks passed, but visual inspection prompted a prose-spacing EDIT; native regeneration and browser checks were repeated on the improved text. No measurements, graph relations or evidence changed.
- Canonical REVIEW history indexing and final post-review validation follow this retained observation; source pinning and release QC remain separate.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: cdb58f7e72774c96529b4267ae25b99460ff5e21
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01981.yaml
    sha256: 2e83bd2bd3c26e6c1776697df15bc9d92de8f9837b9fa60295035d8b241795b5
    role: context
  - path: data/families/PF01981.yaml
    sha256: 276b807fdd783199df5357a3fbd1a1b702f48c4f35a3b3dc685bc0995dff597a
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
  - path: evidence/PF01981/fromant2003.txt
    role: context
    sha256: b8f76cca88d5c37b0b5b909d4456ce2b0924f177c8a18be2907087b818c0932d
  - path: evidence/PF01981/kawashima2026.txt
    role: context
    sha256: 80de6e3f8e9b0f8bb66e5e1c4e1d36a6b86f991d26bdab65beec18a2d5f494dc
  - path: evidence/PF01981/member-mapping.txt
    role: context
    sha256: 9f8b8299f6c91b1712d7af4f8c776d9ec77a53e0d71d4af730edf2f30630ebef
  - path: evidence/PF01981/rosas2002.txt
    role: context
    sha256: a1e5d1f37b907b1524227a917d5d131da284d4e75448a504639a75c022681f20
  - path: history/records/PF01981/2026-10-15T230908Z-codex-c254ed.yaml
    role: context
    sha256: da9a572308817ab04dc5de794559237bb99db470f2025a112cb023dcc9b5588a
  - path: history/records/PF01981/2026-10-15T232145Z-codex-18fd80.yaml
    role: context
    sha256: e2148bbdb90c071d64ec3d7922224ce8a382eda4814353b6e340ca08b763fd8e
targets:
- target_id: PF01981
  path: data/families/PF01981.yaml
  label: PF01981
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01981.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: fd0a909e5221414e6149a7044415b70a66a85a507f44a74f08e5953480e081d5
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
schema_version: 1.0.0
review_id: 20261015T233126Z-pf01981-pth2-causal-contexts
title: PF01981 PTH2 hydrolysis, complementation and assay contexts
started_at: '2026-10-15T23:18:16Z'
finished_at: '2026-10-15T23:31:26Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: The same agent curated and challenged all new edges against
    primary Methods/Results/tables and the inspected2026 assay image. Not independent
    approval or experimental replication.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: true
summary: Nine scoped graphs with16observed experimental edges advance previously seeded
  PF01981. Protein references, historical constructs and current retired-accession
  provenance remain distinct. Three open scientific follow-ups prevent full-family
  completion; IN_PROGRESS remains appropriate.
scope:
  description: Assess every new edge for identity, direction, experimental context,
    evidence integrity and limits. Original2002/2003 Methods, Results, tables and
    Figure1 captions plus2026 main text/Table1/Table3/Figure5 image inspected. Partial
    family coverage, not a literature census.
  selection: First untouched seed after the earlier scoped PF01980 batch; historical
    DUF119/UPF0099 identity verified from the frozen prior-name mapping.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01981
  exclusions:
  - target: Original2005 residue mutants, yeast proteasome/human PTRH2 roles and other
      family members
    reason: Discovery leads, not completed primary experimental assessments.
  - target: Older Figure1 images and2026 supplementary figures
    reason: Image/download access was incomplete; accessible captions/text/tables
      were assessed without claiming raw image inspection.
  - target: Physical assay inserts, raw replicate reanalysis and atomic catalytic
      mechanism
    reason: Reference mappings and deposited sequences do not establish these.
  - target: Canonical site release and full publication QC
    reason: Only an unpinned native local preview; no new source checkpoint, source-pin
      refresh or canonical publication.
checks:
- check_id: generation
  name: generation
  command: just records; just records --apply
  status: passed
  required: true
  exit_code: 0
  summary: 8296schema-valid records; exactlyPF01981andmanifest regenerated after actualCREATE/EDIThistory.
  target_ids:
  - PF01981
  evidence_ids:
  - validation
- check_id: focused
  name: focused
  command: uv run --locked --offline --extra dev pytest -q tests/test_causal_graphs.py
    tests/test_qc.py
  status: passed
  required: true
  exit_code: 0
  summary: 52tests passed in22.97s; structural invalidity, scope/digest/evidence guards
    and QC orchestration tested, not scientific truth.
  target_ids:
  - PF01981
  evidence_ids:
  - validation
- check_id: schema-history
  name: schema-history
  command: just validate-schema history-check
  status: passed
  required: true
  exit_code: 0
  summary: Generated schema current and pre-review canonical history validates.
  target_ids:
  - PF01981
  evidence_ids:
  - validation
- check_id: inventory-exports
  name: inventory-exports
  command: just causal-graphs --apply; just causal-graphs --check; just exports --apply;
    just exports --check
  status: passed
  required: true
  exit_code: 0
  summary: 899graphs/1936edges in130families;8166graphless. Association exports reflect
    only thePF01981status change.
  target_ids:
  - PF01981
  evidence_ids:
  - validation
- check_id: integrity
  name: integrity
  command: uv run --locked --offline python /private/tmp/duf-pf01981-20261015-vhL10L/integrity.py
  status: passed
  required: true
  exit_code: 0
  summary: All8296manifest hashes and16quote/hash anchors pass; onlyPF01981changes,
    with all earlier tracked scientific/artifact inputs preserved.
  target_ids:
  - PF01981
  evidence_ids:
  - validation
- check_id: preview
  name: preview
  command: uv run --locked --offline python /private/tmp/duf-pf01981-20261015-vhL10L/preview.py;
    node /private/tmp/duf-pf01981-20261015-vhL10L/browser.cjs
  status: passed
  required: true
  exit_code: 0
  summary: Exact native unpinned JSON;1440px/390px,9graphs/16observed edges,all16working
    disclosures and4/10/2primary links;no document overflow or JS errors. Selected
    screenshots inspected.
  target_ids:
  - PF01981
  evidence_ids:
  - validation
evidence:
- evidence_id: rosas
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC139208/
  locator: Methods; recombinant enzyme and complementation Results; Figure1 caption;
    Table1; yeast deletion results; evidence/PF01981/rosas2002.txt
  accessed_at: '2026-10-15T23:31:26Z'
  support: supports
  summary: Supports separate purified MJ0051 substrate reactions and bounded bacterial
    rescue; preserves yeast full-length failure and native deletion negatives.
- evidence_id: fromant
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC162332/
  locator: Methods; Results; Tables1-7; Figure1 caption; evidence/PF01981/fromant2003.txt
  accessed_at: '2026-10-15T23:31:26Z'
  support: supports
  summary: Supports substrate-specific hydrolysis, separate ionic additions, uncharged-tRNA
    inhibition and two heterologous rescue contexts; excludes Pth1 phenotype transfer.
- evidence_id: kawashima
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC13523710/
  locator: Methods2.1/2.5, Table1, Table3, Results3.1-3.3, original Figure5 image/caption;
    evidence/PF01981/kawashima2026.txt
  accessed_at: '2026-10-15T23:31:26Z'
  support: supports
  summary: Supports the tested temperature contrasts, not native growth, irreversible
    unfolding or atomic residue mechanisms. Crystal and assay constructs differ.
- evidence_id: mapping
  kind: primary_source
  reference: evidence/PF01981/member-mapping.txt
  locator: Dated UniProt, InterPro, SIFTS and RCSB payload identities/hashes; UniSave
    archived entry19 and explicit current inactive response
  accessed_at: '2026-10-15T23:31:26Z'
  support: supports
  summary: Exact reference mappings and archived-core comparison support family assignment
    while retaining coordinate, taxonomy and physical-construct limitations.
- evidence_id: validation
  kind: validation
  reference: data/families/PF01981.yaml
  locator: Native generation/schema/history,52focused tests, structural inventory/exports,
    integrity and native local preview/browser checks
  accessed_at: '2026-10-15T23:31:26Z'
  support: supports
  summary: All8296manifest hashes, other8295records and earlier tracked artifacts
    preserved; exact JSON, direction labels and all16evidence disclosures checked.
- evidence_id: duf-projection-pf01981
  kind: record_content
  reference: data/families/PF01981.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-15T23:31:26Z'
  support: context_only
  snapshot_sha256: 276b807fdd783199df5357a3fbd1a1b702f48c4f35a3b3dc685bc0995dff597a
  quote: "id: Pfam:PF01981\npfam_id: PF01981\nname: Peptidyl-tRNA hydrolase PTH2\n\
    short_name: PTH2\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01981\n\
    counters:\n  proteins: 9997\n  matches: 10079\n  proteomes: 5836\n  taxa: 12623\n\
    \  structures: 8\n  alphafold_models: 7944\n  domain_architectures: 142\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002833\ndescription: Peptidyl-tRNA hydrolases are enzymes\
    \ that release tRNAs from peptidyl-tRNA during translation.\ncuration_history:\
    \ history/records/PF01981\ndiscussions:\n- discussion_id: pth2-constructs-and-domain-mapping\n\
    \  prompt: Resolve historical physical constructs and domain coordinates before\
    \ stronger domain-specific\n    or residue claims.\n  kind: CURATION_TODO\n  status:\
    \ OPEN\n  rationale: Reference-domain mappings do not independently sequence assay\
    \ constructs; yeast sequence\n    versions and the retired Lokiarchaeum accession\
    \ need explicit treatment.\n  evidence:\n  - reference: PMID:12475929\n    supports:\
    \ PARTIAL\n    evidence_source: primary_publication\n    explanation: MJ0051 and\
    \ historical YBL057c constructs are named, but current P34222 sequence2 numbering\n\
    \      is not an authenticated remapping of the old truncation.\n  - reference:\
    \ PMID:42626907\n    supports: PARTIAL\n    evidence_source: primary_publication\n\
    \    explanation: Table1 supplies distinct activity and crystal sequences; archived\
    \ UniProt entry19 maps\n      their identical core to PF01981, but current HMM\
    \ boundaries remain unresolved.\n  posed_by: Codex\n  posed_date: '2026-10-15'\n\
    \  notes: See evidence/PF01981/member-mapping.txt. Whole-protein rescue is not\
    \ isolated-domain necessity.\n    Obtain original Fromant2005 mutant data and\
    \ folding/abundance controls before claiming atomic chemistry.\n- discussion_id:\
    \ pth2-discrepancies-and-physiology\n  prompt: Resolve source discrepancies and\
    \ distinguish heterologous rescue and assay responses from native\n    physiology.\n\
    \  kind: CURATION_TODO\n  status: OPEN\n  rationale: Full-length yeast complementation\
    \ differs between2002 and2003; original substrate units,\n    Table6 ionic conditions\
    \ and2026 resolution values also differ.\n  evidence:\n  - reference: PMID:12799450\n\
    \    supports: PARTIAL\n    evidence_source: primary_publication\n    explanation:\
    \ Full-length pKKpthY2 rescue contrasts with pGRAS failure in2002. Host/vector/expression\n\
    \      differences prevent pooling. YHR189w respiratory defects are Pth1 results.\n\
    \  - reference: PMID:42626907\n    supports: PARTIAL\n    evidence_source: primary_publication\n\
    \    explanation: Figure5 measures one-minute enzyme activity, not organism growth\
    \ or an irreversible-denaturation\n      curve; structure resolution text disagrees\
    \ with Table3 and deposition.\n  posed_by: Codex\n  posed_date: '2026-10-15'\n\
    \  notes: Retain native yeast deletion negatives as condition-specific, not universal\
    \ dispensability. Do\n    not infer mitochondrial localization, tRNA-folding causality,\
    \ toxicity mechanisms or thermal niches\n    from these graphs.\n- discussion_id:\
    \ pth2-literature-and-member-coverage\n  prompt: Extend primary-source review\
    \ to residue experiments, eukaryotic roles and additional exact PF01981\n    members.\n\
    \  kind: CURATION_TODO\n  status: OPEN\n  rationale: Three inspected studies do\
    \ not complete this diverse family's mechanism coverage.\n  evidence:\n  - reference:\
    \ PMID:15766258\n    supports: PARTIAL\n    evidence_source: primary_publication\n\
    \    explanation: Abstract and later citations are discovery leads only; full\
    \ mutation assays have not\n      been inspected here.\n  posed_by: Codex\n  posed_date:\
    \ '2026-10-15'\n  notes: Follow yeast UBL/proteasome and human PTRH2/BIT1 primary\
    \ studies, older uninspected figures,\n    the2026 supplement and other archaeal\
    \ members. Structural resemblance and automated annotations are\n    not experimental\
    \ transfer.\ncausal_graphs:\n- graph_id: mjpth2-substrate-hydrolysis-2002\n  title:\
    \ Purified MJ0051 releases reaminoacylatable tRNAs\n  scope: Recombinant M. jannaschii\
    \ MJ0051 with C-terminal His6, not all PF01981 members.\n  context: Rosas2002\
    \ Figure 1B; pGR51C/pET20b protein, 37 C, 187 nM; separate diacetyl-[14C]Lys-tRNA\
    \ and\n    acetyl-[14C]Phe-tRNA assays. E. coli Pth and no-enzyme controls; subsequent\
    \ recharging with the appropriate\n    aminoacylation system.\n  family_mapping:\
    \ Q60363 sequence version 1, entry version 131, 115 aa, MJ0051; current PF01981\
    \ spans\n    1-115. The paper cites NP_247015.1. Physical vector junctions are\
    \ not independently verified; evidence/PF01981/member-mapping.txt.\n  scope_status:\
    \ MECHANISTIC\n  taxon: NCBITaxon:243232\n  limitations: No natural peptide-length\
    \ series or atomic catalytic pathway. Substrate units differ between\n    Methods\
    \ and Figure1A; no silently corrected Figure1B concentration. Image was inaccessible;\
    \ Methods,\n    Results and caption inspected. Recharging is a product-integrity\
    \ assay, not cellular translation flux.\n  nodes:\n  - node_id: lys_reaction\n\
    \    label: MJ0051 plus diacetyl-Lys-tRNA in the defined assay\n    node_type:\
    \ ACTIVITY\n    grounding:\n    - UniProtKB:Q60363\n  - node_id: lys_trna\n  \
    \  label: Released reaminoacylatable tRNA-Lys\n    node_type: STATE\n  - node_id:\
    \ phe_reaction\n    label: MJ0051 plus acetyl-Phe-tRNA in the defined assay\n\
    \    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:Q60363\n  - node_id:\
    \ phe_trna\n    label: Released reaminoacylatable tRNA-Phe\n    node_type: STATE\n\
    \  edges:\n  - edge_id: releases-lys-trna\n    subject: lys_reaction\n    predicate:\
    \ produces\n    object: lys_trna\n    mechanism: Purified-protein hydrolysis followed\
    \ by Lys recharging supports release of functional tRNA\n      rather than a nuclease-only\
    \ explanation.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:12475929\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC139208/\n      snippet: The enzyme\
    \ was able to hydrolyze both substrates\n      explanation: Figure1B, recombinant-enzyme\
    \ Results and reaminoacylation Methods; R1 in the retained\n        ledger. TLC\
    \ of extract is not recast as purified-enzyme product identification.\n      cache_path:\
    \ evidence/PF01981/rosas2002.txt\n      cache_sha256: a1e5d1f37b907b1524227a917d5d131da284d4e75448a504639a75c022681f20\n\
    \  - edge_id: releases-phe-trna\n    subject: phe_reaction\n    predicate: produces\n\
    \    object: phe_trna\n    mechanism: The separately tested acetyl-Phe substrate\
    \ yields tRNA that can be recharged; this does\n      not establish all peptide\
    \ substrates.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:12475929\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC139208/\n      snippet: The enzyme\
    \ was able to hydrolyze both substrates\n      explanation: Figure1B and recombinant-enzyme\
    \ Results; R1. Distinct substrate, not a second independent\n        publication.\n\
    \      cache_path: evidence/PF01981/rosas2002.txt\n      cache_sha256: a1e5d1f37b907b1524227a917d5d131da284d4e75448a504639a75c022681f20\n\
    - graph_id: mjpth2-heterologous-rescue-2002\n  title: MJ0051 complements E. coli\
    \ C600 pth-ts\n  scope: Whole MJ0051 gene supplied in pGR518 to an E. coli temperature-sensitive\
    \ pth background.\n  context: Table 1; LB, ampicillin 0.1 mg/ml, IPTG 1 uM; 42\
    \ C versus 32 C. Empty pKQV4 and E. coli pth\n    comparators; cured clones regain\
    \ temperature sensitivity.\n  family_mapping: MJ0051 maps to Q60363/PF01981 reference\
    \ 1-115. The rescue plasmid is not the tagged\n    purified-enzyme construct;\
    \ native archaeal essentiality is not tested.\n  scope_status: PHENOTYPIC\n  limitations:\
    \ Rescue measures growth, not intracellular substrate abundance or a direct translation\
    \ step.\n    Native host and isolated-domain necessity remain untested; pth-null\
    \ rescue is only reported without\n    displayed data and not a separate edge.\n\
    \  nodes:\n  - node_id: plasmid\n    label: pGR518-MJ0051 versus empty vector\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q60363\n  - node_id:\
    \ growth\n    label: C600 pth-ts growth at 42 C\n    node_type: PHENOTYPE\n  edges:\n\
    \  - edge_id: rescues-growth\n    subject: plasmid\n    predicate: enables\n \
    \   object: growth\n    mechanism: Growth rescue depends on retention of the MJ0051\
    \ plasmid under these conditions; intervening\n      cellular events are unresolved.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:12475929\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC139208/\n\
    \      snippet: Both pth genes, but not the empty vector\n      explanation: Table1\
    \ and complementation Results, including cured-clone control; ledger R2.\n   \
    \   cache_path: evidence/PF01981/rosas2002.txt\n      cache_sha256: a1e5d1f37b907b1524227a917d5d131da284d4e75448a504639a75c022681f20\n\
    - graph_id: yeast-pth2-truncated-rescue-2002\n  title: Historical truncated yeast\
    \ PTH2 rescues C600 pth-ts\n  scope: YBL057c-derived pGR87L, with the source's\
    \ N-terminal 86-residue deletion and initiation-codon\n    substitution.\n  context:\
    \ Table 1 and yeast Results; E. coli C600 pth-ts, 42 C, LB/ampicillin/IPTG as\
    \ in the 2002 complementation\n    assay. Full-length pGRAS did not rescue in\
    \ that experiment.\n  family_mapping: Gene correspondence to P34222 supports family\
    \ identity; current sequence version 2 is\n    208 aa with PF01981 at 89-208.\
    \ Do not equate the historical deleted 86 residues with today's numbering;\n \
    \   the physical old insert remains unresolved.\n  scope_status: PHENOTYPIC\n\
    \  limitations: No matched expression, folding or targeting measurements. No claim\
    \ that the N-terminus\n    intrinsically inhibits catalysis or proves organellar\
    \ localization. The2003 full-length rescue is\n    preserved separately.\n  nodes:\n\
    \  - node_id: truncated\n    label: Historical pGR87L versus empty vector\n  \
    \  node_type: PERTURBATION\n  - node_id: growth\n    label: C600 pth-ts growth\
    \ at 42 C\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: rescues-growth\n \
    \   subject: truncated\n    predicate: enables\n    object: growth\n    mechanism:\
    \ This historical yeast-derived construct supports bacterial growth; the direct\
    \ cellular\n      mechanism and reason for the full-length negative are unresolved.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:12475929\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC139208/\n\
    \      snippet: rescued the temperature sensitivity\n      explanation: Table1\
    \ and yeast Results; R3. Host and construct are not pooled with Fromant2003.\n\
    \      cache_path: evidence/PF01981/rosas2002.txt\n      cache_sha256: a1e5d1f37b907b1524227a917d5d131da284d4e75448a504639a75c022681f20\n\
    - graph_id: sspth2-hydrolysis-2003\n  title: Purified SSO0175 hydrolyzes defined\
    \ N-blocked aminoacyl-tRNAs\n  scope: Recombinant S. solfataricus P2 SSO0175,\
    \ with distinct substrate-specific assays.\n  context: Fromant2003 Figure 1 and\
    \ Table 5, 50 C; Tris pH 7.5, EDTA, DTT and standard 10 mM MgCl2 assay.\n    Periodate-treated\
    \ Lys substrate plus subsequent LysRS/ATP recharging tests tRNA integrity; other\
    \ substrates\n    use deacylation kinetics.\n  family_mapping: Q980V1 sequence\
    \ version 1, entry version 128, 120 aa, SSO0175; N-terminal Edman match.\n   \
    \ Later SIFTS 1XTY PF01981 spans 2-120. Mapping does not independently authenticate\
    \ the 2003 physical\n    insert.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:273057\n\
    \  limitations: Artificial N-blocked aminoacyl substrates, not a natural peptidyl-tRNA\
    \ census. Functional\n    recharging was established for Lys, not independently\
    \ for every substrate. Table5 Km estimates for\n    other substrates assume competitive\
    \ tRNA-Lys inhibition. Figure1 caption/text, not its unavailable\n    image, inspected.\n\
    \  nodes:\n  - node_id: lys_assay\n    label: Purified SSO0175 plus diacetyl-Lys-tRNA\n\
    \    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:Q980V1\n  - node_id:\
    \ lys_product\n    label: Released reaminoacylatable tRNA-Lys\n    node_type:\
    \ STATE\n  - node_id: fmet_assay\n    label: Purified SSO0175 plus formyl-Met-tRNA-fMet\n\
    \    node_type: ACTIVITY\n  - node_id: fmet_cleavage\n    label: Formyl-Met-tRNA-fMet\
    \ deacylation\n    node_type: PROCESS\n  - node_id: his_assay\n    label: Purified\
    \ SSO0175 plus acetyl-His-tRNA-His\n    node_type: ACTIVITY\n  - node_id: his_cleavage\n\
    \    label: Acetyl-His-tRNA-His deacylation\n    node_type: PROCESS\n  edges:\n\
    \  - edge_id: releases-functional-lys-trna\n    subject: lys_assay\n    predicate:\
    \ produces\n    object: lys_product\n    mechanism: Product recharging accompanies\
    \ substrate loss, with pre-existing uncharged tRNA inactivated\n      and a no-PTH\
    \ comparator. This supports tRNA-releasing hydrolysis without specifying catalytic\
    \ residues.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:12799450\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC162332/\n      snippet: capable of\
    \ liberating functional tRNA\n      explanation: Figure1 caption, corresponding\
    \ Methods/Results, ledger S1. The no-enzyme baseline is\n        nonzero.\n  \
    \    cache_path: evidence/PF01981/fromant2003.txt\n      cache_sha256: b8f76cca88d5c37b0b5b909d4456ce2b0924f177c8a18be2907087b818c0932d\n\
    \  - edge_id: supports-fmet-deacylation\n    subject: fmet_assay\n    predicate:\
    \ enables\n    object: fmet_cleavage\n    mechanism: Purified-enzyme substrate\
    \ kinetics establish deacylation of the E. coli initiator substrate\n      in\
    \ vitro, not depletion in living bacteria or native archaeal initiation.\n   \
    \ directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:12799450\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC162332/\n\
    \      snippet: capable of liberating functional tRNA\n      explanation: Table5\
    \ formyl-methionyl row and substrate-specificity Results, not the quotation alone,\n\
    \        support this edge; ledger S1. Product recharge was separately tested\
    \ only for Lys.\n      cache_path: evidence/PF01981/fromant2003.txt\n      cache_sha256:\
    \ b8f76cca88d5c37b0b5b909d4456ce2b0924f177c8a18be2907087b818c0932d\n  - edge_id:\
    \ supports-his-deacylation\n    subject: his_assay\n    predicate: enables\n \
    \   object: his_cleavage\n    mechanism: The tested acetyl-His substrate is deacylated\
    \ under the purified-enzyme conditions; a universal\n      tRNA-identity rule\
    \ is not inferred.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:12799450\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC162332/\n      snippet: capable of\
    \ liberating functional tRNA\n      explanation: Table5 acetyl-histidyl row and\
    \ substrate-specificity Results; ledger S1. The measured\n        substrate-specific\
    \ result supplies the relation.\n      cache_path: evidence/PF01981/fromant2003.txt\n\
    \      cache_sha256: b8f76cca88d5c37b0b5b909d4456ce2b0924f177c8a18be2907087b818c0932d\n\
    - graph_id: sspth2-ionic-assay-effects-2003\n  title: Separate ionic additions\
    \ increase the SSO0175 assay rate\n  scope: Purified SSO0175 and diacetyl-Lys-tRNA\
    \ under Table3 conditions; separate additions, not joint\n    necessary cofactors.\n\
    \  context: 50 C, 20 mM Tris pH 7.5, 0.1 mM EDTA, 0.1 mM DTT, 0.75 uM substrate;\
    \ enzyme 0.1-10 nM. No-addition\n    baseline 0.026/s. Reported standard errors\
    \ below 20%.\n  family_mapping: Q980V1/SSO0175; reference PF01981 at 2-120 in\
    \ 1XTY. Whole purified protein, not an isolated\n    mutant domain.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:273057\n  limitations: Rate effects do not independently\
    \ demonstrate tRNA compaction, direct ion binding or catalytic\n    metal necessity.\
    \ Enzyme concentration varies with rate; these are normalized specific activities.\n\
    \    No assertion that all salt concentrations activate.\n  nodes:\n  - node_id:\
    \ magnesium\n    label: Separate 40 mM MgCl2 addition versus no addition\n   \
    \ node_type: PERTURBATION\n  - node_id: potassium\n    label: Separate 300 mM\
    \ KCl addition versus no addition\n    node_type: PERTURBATION\n  - node_id: spermidine\n\
    \    label: Separate 0.1 mM spermidine-HCl addition versus no addition\n    node_type:\
    \ PERTURBATION\n  - node_id: rate\n    label: Defined diacetyl-Lys-tRNA deacylation\
    \ specific activity\n    node_type: ACTIVITY\n  edges:\n  - edge_id: magnesium-increases-rate\n\
    \    subject: magnesium\n    predicate: increases\n    object: rate\n    mechanism:\
    \ Table 3 reports 2.3/s with 40 mM MgCl2 versus 0.026/s without an added compound;\
    \ the molecular\n      origin of the increase is unresolved.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:12799450\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC162332/\n\
    \      snippet: each of these compounds stimulated the rate\n      explanation:\
    \ Table3 magnesium comparison and footnote; ledger S2. Not a combined cofactor\
    \ requirement.\n      cache_path: evidence/PF01981/fromant2003.txt\n      cache_sha256:\
    \ b8f76cca88d5c37b0b5b909d4456ce2b0924f177c8a18be2907087b818c0932d\n  - edge_id:\
    \ potassium-increases-rate\n    subject: potassium\n    predicate: increases\n\
    \    object: rate\n    mechanism: The separate 300 mM KCl condition gives 2.0/s\
    \ versus the no-addition baseline; no monotonic\n      salt-response rule is asserted.\n\
    \    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:12799450\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC162332/\n\
    \      snippet: each of these compounds stimulated the rate\n      explanation:\
    \ Table3 potassium row and assay footnote; ledger S2.\n      cache_path: evidence/PF01981/fromant2003.txt\n\
    \      cache_sha256: b8f76cca88d5c37b0b5b909d4456ce2b0924f177c8a18be2907087b818c0932d\n\
    \  - edge_id: spermidine-increases-rate\n    subject: spermidine\n    predicate:\
    \ increases\n    object: rate\n    mechanism: The separate 0.1 mM spermidine-HCl\
    \ condition gives 1.9/s; substrate folding is an interpretation,\n      not a\
    \ directly measured intermediate.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:12799450\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC162332/\n      snippet:\
    \ each of these compounds stimulated the rate\n      explanation: Table3 spermidine\
    \ row; ledger S2. No physiological polyamine-regulation claim.\n      cache_path:\
    \ evidence/PF01981/fromant2003.txt\n      cache_sha256: b8f76cca88d5c37b0b5b909d4456ce2b0924f177c8a18be2907087b818c0932d\n\
    - graph_id: sspth2-uncharged-trna-inhibition-2003\n  title: Uncharged tRNAs inhibit\
    \ the SSO0175 hydrolysis assay\n  scope: Separate E. coli tRNA-Lys and tRNA-fMet\
    \ additions to purified archaeal PTH2 assays.\n  context: Fromant2003 Methods/Table\
    \ 6; 50 C, Tris pH 7.5, EDTA, DTT; varied inhibitor/substrate concentrations.\n\
    \    Table 6 specifies 0.2 uM substrate and 0.075 nM enzyme; the general Methods\
    \ include MgCl2 but Table\n    6 omits it.\n  family_mapping: Q980V1/SSO0175;\
    \ later 1XTY PF01981 mapping 2-120. Nucleic-acid recognition is tested\n    with\
    \ the whole protein.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:273057\n\
    \  limitations: Preserve ionic-condition ambiguity. Reported inhibition constants\
    \ are not directly measured\n    binding affinities. Competitive behavior was\
    \ explicitly checked for tRNA-Lys; native feedback and\n    binding-site geometry\
    \ remain unresolved. rRNA/DNA negatives are assay-specific.\n  nodes:\n  - node_id:\
    \ lys_trna\n    label: Added uncharged tRNA-Lys\n    node_type: PERTURBATION\n\
    \  - node_id: fmet_trna\n    label: Added uncharged tRNA-fMet\n    node_type:\
    \ PERTURBATION\n  - node_id: rate\n    label: Diacetyl-Lys-tRNA initial deacylation\
    \ rate\n    node_type: ACTIVITY\n  edges:\n  - edge_id: lys-trna-inhibits\n  \
    \  subject: lys_trna\n    predicate: decreases\n    object: rate\n    mechanism:\
    \ Initial-rate measurements support inhibition with a competitive fit for tRNA-Lys;\
    \ no direct\n      atomic binding interaction is assigned.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:12799450\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC162332/\n\
    \      snippet: strong inhibition of the hydrolytic reaction\n      explanation:\
    \ Methods inhibition series and Table6; ledger S3. Distinguish measured rate inhibition\n\
    \        from inferred binding mechanism.\n      cache_path: evidence/PF01981/fromant2003.txt\n\
    \      cache_sha256: b8f76cca88d5c37b0b5b909d4456ce2b0924f177c8a18be2907087b818c0932d\n\
    \  - edge_id: fmet-trna-inhibits\n    subject: fmet_trna\n    predicate: decreases\n\
    \    object: rate\n    mechanism: The separate uncharged initiator-tRNA titration\
    \ inhibits deacylation; this is not evidence\n      that a native feedback circuit\
    \ operates.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:12799450\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC162332/\n      snippet: strong inhibition\
    \ of the hydrolytic reaction\n      explanation: Table6 tRNA-fMet row and Results;\
    \ ledger S3. No measured binding Kd or demonstrated\n        tRNA-fMet competitive\
    \ mode is claimed.\n      cache_path: evidence/PF01981/fromant2003.txt\n     \
    \ cache_sha256: b8f76cca88d5c37b0b5b909d4456ce2b0924f177c8a18be2907087b818c0932d\n\
    - graph_id: sspth2-heterologous-rescue-2003\n  title: SSO0175 supports growth\
    \ after E. coli Pth supply is lost\n  scope: S. solfataricus SSO0175/pTrc-pthS\
    \ in E. coli K37delta-pthTr.\n  context: Fromant2003 identification Results; 42\
    \ C eliminates the temperature-sensitive pMAKpth source\n    of bacterial Pth.\
    \ Empty pTrc99-A fails to yield thermoresistant clones.\n  family_mapping: SSO0175/Q980V1\
    \ reference sequence version 1; PF01981 mapping 2-120. Whole-gene complementation,\n\
    \    not a domain-only intervention.\n  scope_status: PHENOTYPIC\n  limitations:\
    \ No direct intracellular tRNA measurement or native archaeal essentiality test.\
    \ Excess-expression\n    toxicity in XL1-Blue is a different context, not a contradiction\
    \ of this rescue.\n  nodes:\n  - node_id: gene\n    label: pTrc-pthS versus empty\
    \ pTrc99-A\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q980V1\n\
    \  - node_id: growth\n    label: K37delta-pthTr growth at 42 C\n    node_type:\
    \ PHENOTYPE\n  edges:\n  - edge_id: supports-growth\n    subject: gene\n    predicate:\
    \ enables\n    object: growth\n    mechanism: The introduced archaeal gene supplies\
    \ a function sufficient for growth in this bacterial\n      complementation setting;\
    \ intervening in-cell steps are not directly assayed.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:12799450\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC162332/\n\
    \      snippet: acquired the capacity to grow\n      explanation: SSO0175 identification\
    \ Results and strain Table1; ledger S4. Not the separate yeast\n        pKK construct.\n\
    \      cache_path: evidence/PF01981/fromant2003.txt\n      cache_sha256: b8f76cca88d5c37b0b5b909d4456ce2b0924f177c8a18be2907087b818c0932d\n\
    - graph_id: yeast-pth2-full-length-rescue-2003\n  title: Full-length yeast YBL057c\
    \ rescues a different E. coli pth background\n  scope: Source-reported full-length\
    \ YBL057c in pKKpthY2, distinct from2002 pGRAS and pGR87L.\n  context: Fromant2003\
    \ homolog Results; E. coli K37delta-pthTr at 42 C with loss of pMAKpth. Table\
    \ 7 crude-extract\n    activity is supporting context, not a purified yeast-enzyme\
    \ assay.\n  family_mapping: YBL057C corresponds to P34222, current 208-aa sequence\
    \ version 2, with PF01981 at 89-208.\n    The full physical historical insert\
    \ is not independently sequence-verified.\n  scope_status: PHENOTYPIC\n  limitations:\
    \ Different vector, host and expression conditions from2002; no head-to-head resolution\
    \ of\n    full-length failure versus rescue. Do not infer localization or that\
    \ truncation universally changes\n    catalytic efficiency.\n  nodes:\n  - node_id:\
    \ gene\n    label: Full-length YBL057c supplied by pKKpthY2\n    node_type: PERTURBATION\n\
    \  - node_id: growth\n    label: K37delta-pthTr growth at 42 C\n    node_type:\
    \ PHENOTYPE\n  edges:\n  - edge_id: supports-growth\n    subject: gene\n    predicate:\
    \ enables\n    object: growth\n    mechanism: Full-length yeast-gene transformants\
    \ grow after loss of the bacterial Pth maintenance plasmid;\n      this is a separate\
    \ reported rescue, not a resolution of the earlier negative.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:12799450\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC162332/\n\
    \      snippet: Transformants grew\n      explanation: Homolog Results and explicit\
    \ comparison with Rosas2002; ledger S4/N1. Native yeast\n        deletion results\
    \ are not a positive mechanism edge.\n      cache_path: evidence/PF01981/fromant2003.txt\n\
    \      cache_sha256: b8f76cca88d5c37b0b5b909d4456ce2b0924f177c8a18be2907087b818c0932d\n\
    - graph_id: lokipth2-temperature-response-2026\n  title: LokiPth2 assay activity\
    \ rises to 60 C and falls at 70 C\n  scope: Synthetic LCGC14_0646670-derived protein\
    \ with GPH cleavage remnant, not the C-terminally tagged\n    crystal sample or\
    \ live archaeal growth.\n  context: Kawashima2026 Methods 2.5/Figure 5; 20 nM\
    \ enzyme, 1 uM diacetyl-[14C]Lys-tRNA, 20 mM HEPES-KOH\n    pH 7.6, 150 mM KCl,\
    \ 10 mM MgCl2, 7 mM beta-mercaptoethanol; 50 ul, 1 min, supernatant radiolabel.\n\
    \    Same substrate batch; PhPth2 comparison; three independent experiments, SD.\n\
    \  family_mapping: Table 1 core equals archived A0A0F9U5Y0 entry version 19, sequence\
    \ version 1, 118 aa,\n    which explicitly maps PF01981; PDB 24BT entity 1 carries\
    \ the same core plus a different tag. Accession\n    currently deleted; HMM boundaries\
    \ unresolved. Taxon 1538547 follows the deposition; historical metagenome\n  \
    \  taxonomy retained in member-mapping.txt.\n  scope_status: PHENOTYPIC\n  taxon:\
    \ NCBITaxon:1538547\n  limitations: One-minute rate response does not establish\
    \ irreversible protein denaturation or environmental\n    growth optimum. Comparator\
    \ limits substrate-only explanations but no separate Figure5 blank or raw\n  \
    \  replicate data were inspected. Structural salt-bridge and substrate-binding\
    \ hypotheses are not OBSERVED\n    edges.\n  nodes:\n  - node_id: warm\n    label:\
    \ Assay temperature 60 C versus 20 C\n    node_type: PERTURBATION\n  - node_id:\
    \ hotter\n    label: Assay temperature 70 C versus 60 C\n    node_type: PERTURBATION\n\
    \  - node_id: activity\n    label: LokiPth2 one-minute deacylation-assay activity\n\
    \    node_type: ACTIVITY\n  edges:\n  - edge_id: warming-increases-activity\n\
    \    subject: warm\n    predicate: increases\n    object: activity\n    mechanism:\
    \ Figure 5 reports greater activity at 60 C than 20 C under the defined assay;\
    \ no continuous\n      curve or precise optimum between sampled temperatures is\
    \ inferred.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:42626907\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC13523710/\n      snippet: The same\
    \ batch of substrate was used for all temperature conditions.\n      explanation:\
    \ Original Figure5 image and Results3.3 supply the direction, Methods2.5 the shared-substrate\n\
    \        control; ledger L2. No numerical bar digitization.\n      cache_path:\
    \ evidence/PF01981/kawashima2026.txt\n      cache_sha256: 80de6e3f8e9b0f8bb66e5e1c4e1d36a6b86f991d26bdab65beec18a2d5f494dc\n\
    \  - edge_id: further-heating-decreases-activity\n    subject: hotter\n    predicate:\
    \ decreases\n    object: activity\n    mechanism: The 70 C response is below 60\
    \ C while the PhPth2 comparator retains activity; the underlying\n      structural\
    \ transition is not directly measured.\n    directness: UNRESOLVED\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:42626907\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13523710/\n      snippet:\
    \ The same batch of substrate was used for all temperature conditions.\n     \
    \ explanation: Figure5 image/caption and Results3.3; ledger L2/N1. This is not\
    \ an irreversible heat-inactivation\n        or growth experiment.\n      cache_path:\
    \ evidence/PF01981/kawashima2026.txt\n      cache_sha256: 80de6e3f8e9b0f8bb66e5e1c4e1d36a6b86f991d26bdab65beec18a2d5f494dc\n\
    curation_events:\n- timestamp: '2026-10-15T23:09:08Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Add scoped PTH2 hydrolysis, complementation\
    \ and assay-condition causal graphs.\n  history_record: history/records/PF01981/2026-10-15T230908Z-codex-c254ed.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-15T23:21:45Z'\n\
    \  curator: Codex\n  action: EDIT\n  outcome: changed\n  summary: Improve spacing\
    \ in PTH2 assay contexts and reference mappings after visual inspection.\n  history_record:\
    \ history/records/PF01981/2026-10-15T232145Z-codex-18fd80.yaml\n  event_index:\
    \ 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Frozen family versus exact tested proteins
  outcome: supported
  summary: Verified historical names and mapped references. Current yeast numbering
    is not retrofitted onto old constructs. The retired Lokiarchaeum accession is
    explicitly historical; identical core sequence links the archived Pfam assignment
    to the assay.
  target_ids:
  - PF01981
  evidence_ids:
  - mapping
  - rosas
  - kawashima
- assessment_id: graphs
  area: graph
  topic: Directed experimental relations without scope inflation
  outcome: supported
  summary: All16edges reviewed. Purified substrate reactions are DIRECT/MECHANISTIC;
    bacterial rescue is INDIRECT/PHENOTYPIC; ionic, inhibitor and temperature responses
    keep UNRESOLVED molecular directness. Contexts and conjunctive reaction inputs
    remain separate.
  target_ids:
  - PF01981
  evidence_ids:
  - rosas
  - fromant
  - kawashima
  - validation
- assessment_id: evidence
  area: evidence
  topic: Minimal extracts and negative/conflicting observations
  outcome: supported
  summary: Quoted fragments anchor precise source locators and own factual ledgers.
    No paper/figure redistribution. Native yeast negatives, full-length discrepancy,
    substrate units and structural hypotheses are retained rather than converted to
    unsupported edges.
  target_ids:
  - PF01981
  evidence_ids:
  - rosas
  - fromant
  - kawashima
- assessment_id: provenance
  area: provenance
  topic: Authoring ownership and whole-corpus preservation
  outcome: supported
  summary: Maintained overlay/evidence and actual CREATE/EDIT history own the curation.
    Native generation changes onlyPF01981andmanifest; previous evidence/reviews/history/overlays,
    frozen inputs and canonical Pages/pins remain byte-unchanged.
  target_ids:
  - PF01981
  evidence_ids:
  - mapping
  - validation
- assessment_id: coverage
  area: completeness
  topic: Remaining residue, construct and family work
  outcome: concern
  summary: The initial three-study assessment is incomplete family coverage; three
    open discussions and findings identify next evidence work. No REVIEWED promotion.
  target_ids:
  - PF01981
  evidence_ids:
  - mapping
  - rosas
  - fromant
  - kawashima
findings:
- finding_id: constructs-and-domain-mapping
  issue_key: pf01981-constructs-and-domain-mapping
  title: Resolve exact historical constructs and residue mechanisms
  description: Current reference coordinates are not independently verified physical
    inserts. Historical yeast numbering and current Lokiarchaeum HMM coordinates remain
    unresolved. Original2005 mutants need full assay/control inspection before atomic
    claims.
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - PF01981
  field_paths:
  - causal_graphs
  - discussions
  evidence_ids:
  - mapping
  - rosas
  - kawashima
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01981.yaml
    role: Maintained scientific overlay; generated projection is not manually edited.
- finding_id: discrepancies-and-physiology
  issue_key: pf01981-discrepancies-and-physiology
  title: Resolve source discrepancies and physiological interpretation
  description: Full-length yeast complementation outcomes differ across hosts/vectors.
    Source concentration/ionic/resolution discrepancies remain explicit. Native localization,
    thermal ecology and proposed toxicity/structural mechanisms are not established
    by these edges.
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - PF01981
  field_paths:
  - causal_graphs
  - discussions
  evidence_ids:
  - rosas
  - fromant
  - kawashima
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01981.yaml
    role: Maintained scientific overlay; generated projection is not manually edited.
- finding_id: family-and-literature-coverage
  issue_key: pf01981-family-and-literature-coverage
  title: Continue additional exact-member and primary-study coverage
  description: Yeast UBL/proteasome and human PTRH2/BIT1 roles, other archaeal members,
    original residue experiments and uninspected images/supplements remain outstanding.
    This is not complete family review.
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - PF01981
  field_paths:
  - causal_graphs
  - discussions
  evidence_ids:
  - mapping
  - fromant
  - kawashima
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01981.yaml
    role: Maintained scientific overlay; generated projection is not manually edited.
actions:
- action_id: extend-pth2-evidence
  description: Resolve the scoped unknowns and extend primary experimental coverage
    without erasing negative results or merging incompatible constructs.
  finding_ids:
  - constructs-and-domain-mapping
  - discrepancies-and-physiology
  - family-and-literature-coverage
  target_ids:
  - PF01981
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01981.yaml
    role: Maintained scientific overlay; generated projection is not manually edited.
  acceptance_checks:
  - Verify historical inserts/sequence remapping and current domain coordinates, or
    retain explicit unresolved scope.
  - Inspect original residue-mutant assays, controls and structural/biochemical limitations
    before causal residue chemistry.
  - Resolve source discrepancies using original data or author clarification; otherwise
    retain them without stronger claims.
  - Review the remaining primary/member contexts, preserve negative and conflicting
    evidence, and append successor reviews/history.
limitations:
- The8296-record goal remains active.130graph-bearing families are structural presence,
  not130completed scientific reviews.
- All16edges are observed at their declared assay/phenotype scope; none claims an
  observed proton transfer, nucleophile, salt-bridge switch or localization mechanism.
- 2002substrate concentration units,2003Table6 ionic conditions and2026structure resolution
  differ within their sources; no silent numerical correction.
- Historical yeast truncation numbering is not current P34222 numbering. Full-length
  rescue/failure experiments use different hosts/vectors and remain separate.
- A0A0F9U5Y0 is currently deleted; archived entry19 retains PF01981 and its118-aa
  core matches the paper/deposition. Current HMM boundary coordinates remain unresolved.
- XML retrieval returned500; older figure access included a browser challenge and
  a caption-only result;2026supplement download did not yield inspected content. These
  are access limits, not negative findings.
- No new source pipeline, functional score, frozen snapshot, runtime change, publication
  or independent scientific endorsement.
- Initial browser checks passed, but visual inspection prompted a prose-spacing EDIT;
  native regeneration and browser checks were repeated on the improved text. No measurements,
  graph relations or evidence changed.
- Canonical REVIEW history indexing and final post-review validation follow this retained
  observation; source pinning and release QC remain separate.
```
