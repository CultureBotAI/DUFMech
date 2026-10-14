# Scoped scientific self-review of SufBD biochemical and cellular contexts

- Review: 20261011T105307Z-pf01458-sufbd-biochemical-and-cellular-contexts
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T10:50:59Z
- Finished UTC: 2026-10-11T10:53:07Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Four graphs retain five DIRECT OBSERVED purified SufB-complex effects and two INDIRECT OBSERVED SufD H360A phenotypes. Basal SufSE output, residual C405A sulfur, distinct SufB/SufD mappings and lower mutant SufD abundance remain explicit. No observed internal sulfur-tunnel or ligand trajectory is claimed. Partial scientific self-review; IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01458 SUFBD_core/former UPF0051, next accession-ordered SEEDED family after PF01345, assessed through Yuda 2017 purified and cellular experiments with supplementary controls and exact reference-domain mapping.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01458 | data/families/PF01458.yaml | generated | PF01458 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01458 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01458.

P77522 SufB is 495 aa, sequence version 2, with PF01458 225-466; P77689 SufD is 423 aa, sequence version 1, with PF01458 166-393. Both sequences match InterPro and contain the stated tested residues. C254A/C405A primer pairs encode the intended local substitutions. Table S1 specifies MG1655-derived UT109/YT2512. Complete historical clones and all junctions remain unverified, and homologous domain membership does not make SufB and SufD functions interchangeable.

### Directed effects and limits

graph: supported. Targets: PF01458.

Five direct edges describe net purified-system comparisons, not atom-resolved sulfur chemistry. The no-DTT sulfur-loading reaction is separate from the DTT-containing sulfide-output reaction; C405A's preserved stimulation and C358A's retained sulfur are kept as qualifiers. SufD cellular edges are indirect and use different plate versus liquid conditions. Lower H360A abundance and Fdx stability remain alternatives. Proposed tunnel, FADH2, ATP motion and ligand models do not become observed edges.

### Remaining family coverage

completeness: concern. Targets: PF01458.

The remaining mutant matrix, prior primary studies, full historical constructs, some plate supplementation details, raw blots/measurements and direct site-resolved chemical intermediates remain uncurated. Bacterial, archaeal and plastid members and isolated-domain sufficiency are not comprehensively covered. Figures 1/2/3/5/6 and S1/S4 were not independently visually assessed; their text/captions are not equivalent to plotted-data review.

## Findings

### additional-contexts: Resolve constructs and chemical intermediates before extending SufBD causal pathways

minor / open / confirmed; issue key: pf01458-causal-context-coverage.

Obtain full clone records and independently resolved sulfur/iron intermediates, reconcile plate supplementation and mutant abundance, and review remaining primary experiments and members. Keep SufB and SufD distinctions, C405A's endpoint-specific behavior and the proposed tunnel clearly separated. Curate supported extensions with their own exact contexts and save successor reviews.

## Recommended Actions And Acceptance Checks

### extend-contexts

Obtain full clone records and independently resolved sulfur/iron intermediates, reconcile plate supplementation and mutant abundance, and review remaining primary experiments and members. Keep SufB and SufD distinctions, C405A's endpoint-specific behavior and the proposed tunnel clearly separated. Curate supported extensions with their own exact contexts and save successor reviews.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://www.nature.com/articles/s41598-017-09846-2; Main Results/Discussion/Methods and supplemental tables/captions; Figure 4 and supplemental Figures S2/S3 visually inspected | supports | C254A, Q285A and W287A lower complete SufSE/SufBCD sulfide output relative to their matched WT reactions; C254A removes added-complex stimulation, not basal activity. C254A and C405A reduce complex-retained sulfur in a separate loading/separation assay. SufD H360A fails to restore unsupplemented plate growth and lowers detected holo-Fdx in separately supplemented cultures, with an abundance qualification. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/P77522/entry/pfam/PF01458/; Accession and domain locations; paired UniProt identity facts | supports | P77522 SufB is 495 aa, sequence version 2, with PF01458 225-466; P77689 SufD is 423 aa, sequence version 1, with PF01458 166-393. Both sequences match InterPro and contain the stated tested residues. C254A/C405A primer pairs encode the intended local substitutions. Table S1 specifies MG1655-derived UT109/YT2512. Complete historical clones and all junctions remain unverified, and homologous domain membership does not make SufB and SufD functions interchangeable. |
| supplemental-controls | https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41598-017-09846-2/MediaObjects/41598_2017_9846_MOESM1_ESM.pdf; Tables S1-S5 and figure captions; S2/S3 images on pages 14-15 visually inspected | supports | Strain/plasmid metadata, mutation primers, SufD phenotypes/abundance and purified-complex assembly controls constrain the retained comparisons. Other mutation-table entries are not automatically converted to graph edges. |
| sufd-mapping | https://www.ebi.ac.uk/interpro/api/protein/uniprot/P77689/entry/pfam/PF01458/; P77689 PF01458 interval 166-393 and exact sequence agreement | supports | H360 lies inside SufD's homologous domain, which is not assigned the SufB-specific biochemical effects. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01458 | data/families/PF01458.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Main Results/Discussion/Methods and supplemental tables/captions were read. Figure 4 and S2/S3 were visually checked; other figures and raw measurements were not independently analyzed. Local primer translation verifies only the C254A/C405A coding neighborhoods, not complete constructs. PMC HTML returned a challenge, while publisher HTML and the original supplement were accessible.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T105307Z-pf01458-sufbd-biochemical-and-cellular-contexts
title: Scoped scientific self-review of SufBD biochemical and cellular contexts
started_at: '2026-10-11T10:50:59Z'
finished_at: '2026-10-11T10:53:07Z'
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
summary: Four graphs retain five DIRECT OBSERVED purified SufB-complex effects and
  two INDIRECT OBSERVED SufD H360A phenotypes. Basal SufSE output, residual C405A
  sulfur, distinct SufB/SufD mappings and lower mutant SufD abundance remain explicit.
  No observed internal sulfur-tunnel or ligand trajectory is claimed. Partial scientific
  self-review; IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01458.yaml
    sha256: 8bbe59bbfb55ad1129d77202283f43b24338924ce68cff56e046afd1ece809ae
    role: context
  - path: data/families/PF01458.yaml
    sha256: baebe944211896521398796973912ab757b5d7975eef94799e19e86668f1553c
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
  - path: evidence/PF01458/yuda-2017-sufbd.txt
    role: context
    sha256: 1542a7061896016ba21f51ad63de0706c194cff8e9cdb9b4042302df6039e8f4
  - path: evidence/PF01458/SufBD-identity.txt
    role: context
    sha256: 60f41fd4f59263bdb4ab0c06763778e6c5290f83d9e1ba8c3e98c6f7f512abdb
targets:
- target_id: PF01458
  path: data/families/PF01458.yaml
  label: PF01458
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01458.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 9275f9547552cdac718420c7eeeee966222f05a23896e49d118c4ccaab3863dc
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01458 SUFBD_core/former UPF0051, next accession-ordered SEEDED family
    after PF01345, assessed through Yuda 2017 purified and cellular experiments with
    supplementary controls and exact reference-domain mapping.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01458
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: The remaining mutant matrix, prior primary studies, full historical constructs,
      some plate supplementation details, raw blots/measurements and direct site-resolved
      chemical intermediates remain uncurated. Bacterial, archaeal and plastid members
      and isolated-domain sufficiency are not comprehensively covered. Figures 1/2/3/5/6
      and S1/S4 were not independently visually assessed; their text/captions are
      not equivalent to plotted-data review.
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
  - PF01458
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://www.nature.com/articles/s41598-017-09846-2
  locator: Main Results/Discussion/Methods and supplemental tables/captions; Figure
    4 and supplemental Figures S2/S3 visually inspected
  accessed_at: '2026-10-11T10:53:07Z'
  support: supports
  snapshot_sha256: 1542a7061896016ba21f51ad63de0706c194cff8e9cdb9b4042302df6039e8f4
  summary: C254A, Q285A and W287A lower complete SufSE/SufBCD sulfide output relative
    to their matched WT reactions; C254A removes added-complex stimulation, not basal
    activity. C254A and C405A reduce complex-retained sulfur in a separate loading/separation
    assay. SufD H360A fails to restore unsupplemented plate growth and lowers detected
    holo-Fdx in separately supplemented cultures, with an abundance qualification.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P77522/entry/pfam/PF01458/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T10:53:07Z'
  support: supports
  snapshot_sha256: 60f41fd4f59263bdb4ab0c06763778e6c5290f83d9e1ba8c3e98c6f7f512abdb
  summary: P77522 SufB is 495 aa, sequence version 2, with PF01458 225-466; P77689
    SufD is 423 aa, sequence version 1, with PF01458 166-393. Both sequences match
    InterPro and contain the stated tested residues. C254A/C405A primer pairs encode
    the intended local substitutions. Table S1 specifies MG1655-derived UT109/YT2512.
    Complete historical clones and all junctions remain unverified, and homologous
    domain membership does not make SufB and SufD functions interchangeable.
- evidence_id: supplemental-controls
  kind: primary_source
  reference: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41598-017-09846-2/MediaObjects/41598_2017_9846_MOESM1_ESM.pdf
  locator: Tables S1-S5 and figure captions; S2/S3 images on pages 14-15 visually
    inspected
  summary: Strain/plasmid metadata, mutation primers, SufD phenotypes/abundance and
    purified-complex assembly controls constrain the retained comparisons. Other mutation-table
    entries are not automatically converted to graph edges.
  accessed_at: '2026-10-11T10:53:07Z'
  support: supports
  snapshot_sha256: 1542a7061896016ba21f51ad63de0706c194cff8e9cdb9b4042302df6039e8f4
- evidence_id: sufd-mapping
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P77689/entry/pfam/PF01458/
  locator: P77689 PF01458 interval 166-393 and exact sequence agreement
  summary: H360 lies inside SufD's homologous domain, which is not assigned the SufB-specific
    biochemical effects.
  accessed_at: '2026-10-11T10:53:07Z'
  support: supports
  snapshot_sha256: 60f41fd4f59263bdb4ab0c06763778e6c5290f83d9e1ba8c3e98c6f7f512abdb
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T10:53:07Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01458
  kind: record_content
  reference: data/families/PF01458.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T10:53:07Z'
  support: context_only
  snapshot_sha256: baebe944211896521398796973912ab757b5d7975eef94799e19e86668f1553c
  quote: "id: Pfam:PF01458\npfam_id: PF01458\nname: SUF system FeS cluster assembly,\
    \ SufBD core domain\nshort_name: SUFBD_core\nseed_status: EX_DUF\ncharacterization_status:\
    \ UNSCORED\ncuration_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01458\n\
    counters:\n  proteins: 30443\n  matches: 30502\n  proteomes: 15015\n  taxa: 22322\n\
    \  structures: 8\n  alphafold_models: 20235\n  domain_architectures: 56\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR000825\ndescription: 'Iron-sulphur (FeS) clusters are\
    \ important cofactors for numerous proteins involved in electron\n  transfer,\
    \ in redox and non-redox catalysis, in gene regulation, and as sensors of oxygen\
    \ and iron. These\n  functions depend on the various FeS cluster prosthetic groups,\
    \ the most common being [2Fe-2S] and [4Fe-4S]\n  [[cite:PUB00035635]]. FeS cluster\
    \ assembly is a complex process involving the mobilisation of Fe and\n  S atoms\
    \ from storage sources, their assembly into [Fe-S] form, their transport to specific\
    \ cellular\n  locations, and their transfer to recipient apoproteins. So far,\
    \ three FeS assembly machineries have\n  been identified, which are capable of\
    \ synthesising all types of [Fe-S] clusters: ISC (iron-sulphur cluster),\n  SUF\
    \ (sulphur assimilation), and NIF (nitrogen fixation) systems. The SUF system\
    \ is an alternative pathway\n  to the ISC system that operates under iron starvation\
    \ and oxidative stress. It is found in eubacteria,\n  archaea and eukaryotes (plastids).\
    \ The SUF system is encoded by the suf operon (sufABCDSE), and the\n  six encoded\
    \ proteins are arranged into two complexes (SufSE and SufBCD) and one protein\
    \ (SufA). SufS\n  is a pyridoxal-phosphate (PLP) protein displaying cysteine desulphurase\
    \ activity. SufE acts as a scaffold\n  protein that accepts S from SufS and donates\
    \ it to SufA [[cite:PUB00035639]]. SufC is an ATPase with\n  an unorthodox ATP-binding\
    \ cassette (ABC)-like component. SufA is homologous to IscA [[cite:PUB00035640]],\n\
    \  acting as a scaffold protein in which Fe and S atoms are assembled into [FeS]\
    \ cluster forms, which can\n  then easily be transferred to apoproteins targets.\
    \ This entry represents the core domain of SufB and\n  SufD proteins, which are\
    \ homologous, and form part of the SufBCD complex in the SUF system [[cite:PUB00089444]].\n\
    \  SufB accepts sulfur transferred from SufE [[cite:PUB00089442]], whereas SufD\
    \ may play a role in iron\n  acquisition [[cite:PUB00089443]].'\ncuration_history:\
    \ history/records/PF01458\ndiscussions:\n- discussion_id: sufbd-chemical-route-and-member-coverage\n\
    \  prompt: Resolve complete constructs and direct sulfur/iron chemistry, keeping\
    \ SufB and SufD roles distinct.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale:\
    \ Purified-complex substitution effects and cellular complementation phenotypes\
    \ support bounded\n    causal edges, not the entire proposed sulfur tunnel, ATP-driven\
    \ motion or ligand sequence. PF01458\n    covers two homologous proteins with\
    \ nonidentical roles.\n  evidence:\n  - reference: PMID:28839209\n    supports:\
    \ PARTIAL\n    evidence_source: full_text_and_supplement\n    explanation: Main\
    \ Methods/Results/Discussion and supplemental tables/captions were read; Figure\
    \ 4\n      and S2/S3 were visually checked. The internal tunnel and residue-ligation\
    \ model remain proposed\n      explanations. C405A preserves stimulation despite\
    \ reduced sulfur retention; C358A is not another\n      sulfur-loading loss.\n\
    \  posed_by: Codex\n  posed_date: '2026-10-11'\n  notes: Examine remaining mutant\
    \ panels and primary studies of bacterial, archaeal and plastid systems,\n   \
    \ including ATP/FADH2 effects and actual Fe-S products. Obtain full cloned sequences\
    \ and direct site-resolved\n    sulfur data. Preserve basal output, residual sulfur,\
    \ SufD abundance and culture-condition qualifications.\n    Partial scientific\
    \ self-review; IN_PROGRESS.\ncausal_graphs:\n- graph_id: ecoli-sufb-substitutions-sufse-output\n\
    \  title: SufB substitutions reduce stimulation of the SufSE sulfide-output assay\n\
    \  scope: Purified E. coli SufBCD complexes carrying separate C254A, Q285A or\
    \ W287A SufB substitutions\n    in Yuda 2017 Figure 4a; not isolated PF01458 or\
    \ a stand-alone SufB desulfurase.\n  context: Compare each variant with its panel's\
    \ WT at 3 uM SufBCD, with 0.5 uM SufS, 2 uM SufE, 2 mM\n    L-cysteine and 2 mM\
    \ DTT in 25 mM Tris-HCl pH 7.8, 150 mM NaCl, 30 C for 10 min. Released sulfide\
    \ is\n    detected as methylene blue and activity normalized per mg SufS. pGSO164-derived\
    \ complexes were expressed\n    in YT2512 and chromatographically purified; SufS\
    \ and untagged SufE were separately supplied.\n  family_mapping: E. coli K12 SufB\
    \ is UniProtKB:P77522, 495 aa, sequence version 2, with PF01458 at 225-466.\n\
    \    C254, Q285 and W287 lie inside it. Partner SufD P77689 has the homologous\
    \ family interval 166-393\n    but does not inherit the SufB-specific substitution\
    \ effect. Table S2 C254A primers agree locally with\n    the reference; full historical\
    \ clones and junctions remain unverified.\n  scope_status: MECHANISTIC\n  taxon:\
    \ NCBITaxon:83333\n  limitations: C254A removes added-complex stimulation, not\
    \ basal SufSE output. Q285A/W287A retain stimulation.\n    This net purified-system\
    \ readout does not directly track persulfide chemistry or assign the chemical\n\
    \    step responsible. S3 supports comparable complex assembly and Figure 4b retains\
    \ SufE interaction,\n    but neither proves identical local folding. Means and\
    \ SD reflect at least three measurements, not\n    established independent protein\
    \ batches.\n  nodes:\n  - node_id: sufb-c254a-complex\n    label: C254A SufB in\
    \ SufBCD instead of WT at 3 uM in the complete SufSE assay\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:P77522\n  - node_id: sufb-q285a-complex\n   \
    \ label: Q285A SufB in SufBCD instead of WT at 3 uM in its matched assay\n   \
    \ node_type: PERTURBATION\n    grounding:\n    - UniProtKB:P77522\n  - node_id:\
    \ sufb-w287a-complex\n    label: W287A SufB in SufBCD instead of WT at 3 uM in\
    \ its matched assay\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:P77522\n\
    \  - node_id: complete-assay-sulfide-output\n    label: Methylene-blue sulfide-output\
    \ activity of the complete SufS-SufE-SufBCD reaction\n    node_type: ACTIVITY\n\
    \  edges:\n  - edge_id: c254a-decreases-sufse-output\n    subject: sufb-c254a-complex\n\
    \    predicate: decreases\n    object: complete-assay-sulfide-output\n    mechanism:\
    \ C254A-containing complex yields less sulfide output than WT and remains near\
    \ the no-added-complex\n      baseline. The directly observed substitution effect\
    \ concerns the assembled reaction, not isolated-domain\n      catalysis or absolute\
    \ loss of all cysteine desulfuration.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:28839209\n\
    \      source_url: https://www.nature.com/articles/s41598-017-09846-2\n      snippet:\
    \ no enhancement was observed\n      explanation: Figure 4a and Methods establish\
    \ the WT comparison, nonzero baseline and complete reaction;\n        supplemental\
    \ S3 and Figure 4b qualify assembly and interaction alternatives.\n      cache_path:\
    \ evidence/PF01458/yuda-2017-sufbd.txt\n      cache_sha256: 1542a7061896016ba21f51ad63de0706c194cff8e9cdb9b4042302df6039e8f4\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P77522/entry/pfam/PF01458/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P77522/entry/pfam/PF01458/\n\
    \      snippet: 'SufB Pfam:PF01458; domain interval: 225-466, inclusive.'\n  \
    \    explanation: Reference sequence and locally translated mutation primers establish\
    \ the family mapping,\n        not the experiment's inferred sulfur trajectory.\n\
    \      cache_path: evidence/PF01458/SufBD-identity.txt\n      cache_sha256: 60f41fd4f59263bdb4ab0c06763778e6c5290f83d9e1ba8c3e98c6f7f512abdb\n\
    \  - edge_id: q285a-decreases-sufse-output\n    subject: sufb-q285a-complex\n\
    \    predicate: decreases\n    object: complete-assay-sulfide-output\n    mechanism:\
    \ The Q285A preparation yields lower activity than its matched WT at 3 uM complex\
    \ while remaining\n      above the no-complex baseline. Partial stimulation is\
    \ retained, without assigning an atomic contact\n      or independently observed\
    \ sulfur-transfer microstep.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:28839209\n\
    \      source_url: https://www.nature.com/articles/s41598-017-09846-2\n      snippet:\
    \ modest increase\n      explanation: The separate Q285A panel in visually inspected\
    \ Figure 4a supports the partial decrease\n        relative to WT retained here,\
    \ not total loss of stimulation.\n      cache_path: evidence/PF01458/yuda-2017-sufbd.txt\n\
    \      cache_sha256: 1542a7061896016ba21f51ad63de0706c194cff8e9cdb9b4042302df6039e8f4\n\
    \  - edge_id: w287a-decreases-sufse-output\n    subject: sufb-w287a-complex\n\
    \    predicate: decreases\n    object: complete-assay-sulfide-output\n    mechanism:\
    \ W287A lowers the sulfide-output activity relative to its matched WT at 3 uM\
    \ complex, but\n      does not eliminate stimulation. This purified-system comparison\
    \ is not a direct binding-affinity\n      or tunnel-gating measurement.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:28839209\n      source_url: https://www.nature.com/articles/s41598-017-09846-2\n\
    \      snippet: modest increase\n      explanation: Figure 4a's W287A panel and\
    \ its stated reaction conditions support this bounded decrease\n        relative\
    \ to WT, with residual stimulation preserved.\n      cache_path: evidence/PF01458/yuda-2017-sufbd.txt\n\
    \      cache_sha256: 1542a7061896016ba21f51ad63de0706c194cff8e9cdb9b4042302df6039e8f4\n\
    - graph_id: ecoli-sufb-substitutions-bound-sulfur\n  title: C254A and C405A lower\
    \ sulfur retained by the SufBCD complex\n  scope: Separately purified E. coli\
    \ SufBCD variants in Yuda 2017 Figure 4c, not residue-resolved sulfur\n    occupancy\
    \ or a complete Fe-S synthesis pathway.\n  context: React 10 uM SufBCD, 0.5 uM\
    \ each SufS/SufE and 2 mM L-cysteine in 125 ul of 50 mM Tris-HCl pH\n    7.8,\
    \ 150 mM NaCl at 30 C for 3 h without DTT. Remove smaller components using a 100-kDa\
    \ ultrafilter,\n    normalize retained complex by A280, then release bound sulfur\
    \ with 2 mM DTT and measure methylene\n    blue at 670 nm. Means/SD derive from\
    \ at least three measurements.\n  family_mapping: P77522 SufB has PF01458 225-466,\
    \ encompassing both C254 and C405. C254A and C405A primer\n    pairs encode only\
    \ their intended local substitutions relative to the current sequence. Intact\
    \ SufBCD\n    and required SufS/SufE partners were assayed, not the isolated family\
    \ region.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:83333\n  limitations:\
    \ WT retains 4.8 +/- 0.9 sulfur atoms per complex, C405A 1.0 +/- 0.1, and C254A\
    \ has no detected\n    signal; the detection limit is unspecified. Retained sulfur\
    \ is an operational complex-level endpoint,\n    not proof of every attachment\
    \ site, a C254-to-C405 transfer trajectory, FADH2 chemistry or an assembled\n\
    \    Fe-S cluster. SufD C358A retains roughly WT sulfur and is not represented\
    \ as another loss mutation.\n  nodes:\n  - node_id: c254a-in-sulfur-loading\n\
    \    label: C254A-containing SufBCD rather than WT in the no-DTT loading reaction\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:P77522\n  - node_id:\
    \ c405a-in-sulfur-loading\n    label: C405A-containing SufBCD rather than WT in\
    \ the no-DTT loading reaction\n    node_type: PERTURBATION\n    grounding:\n \
    \   - UniProtKB:P77522\n  - node_id: complex-retained-sulfur\n    label: DTT-releasable\
    \ sulfur per retained SufBCD complex after loading and separation\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: c254a-decreases-retained-sulfur\n    subject:\
    \ c254a-in-sulfur-loading\n    predicate: decreases\n    object: complex-retained-sulfur\n\
    \    mechanism: Replacing SufB C254 with alanine reduces the complex-associated\
    \ sulfur signal to below\n      detection in the loading/separation assay. This\
    \ directly tests the variant preparation but does\n      not itself observe individual\
    \ trans-persulfuration events.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:28839209\n\
    \      source_url: https://www.nature.com/articles/s41598-017-09846-2\n      snippet:\
    \ abolished the sulfur transfer\n      explanation: Figure 4c and the separate\
    \ no-DTT loading/separation protocol support the complex-level\n        sulfur\
    \ decrease. The authors' transfer interpretation is not promoted to a directly\
    \ tracked atomic\n        trajectory.\n      cache_path: evidence/PF01458/yuda-2017-sufbd.txt\n\
    \      cache_sha256: 1542a7061896016ba21f51ad63de0706c194cff8e9cdb9b4042302df6039e8f4\n\
    \  - edge_id: c405a-decreases-retained-sulfur\n    subject: c405a-in-sulfur-loading\n\
    \    predicate: decreases\n    object: complex-retained-sulfur\n    mechanism:\
    \ C405A reduces retained sulfur relative to WT while leaving measurable residual\
    \ sulfur.\n      Its approximately WT Figure 4a stimulation remains a distinct\
    \ negative control against treating\n      every readout as the same causal step.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:28839209\n      source_url: https://www.nature.com/articles/s41598-017-09846-2\n\
    \      snippet: decidedly less\n      explanation: Figure 4c and its Results provide\
    \ the residual sulfur comparison for C405A; Figure\n        4a separately shows\
    \ preserved stimulation, preventing conflation of the endpoints.\n      cache_path:\
    \ evidence/PF01458/yuda-2017-sufbd.txt\n      cache_sha256: 1542a7061896016ba21f51ad63de0706c194cff8e9cdb9b4042302df6039e8f4\n\
    - graph_id: ecoli-sufd-h360a-complementation-growth\n  title: SufD H360A fails\
    \ to restore growth without mevalonate in UT109\n  scope: E. coli MG1655-derived\
    \ UT109 with isc/suf deletions and a mevalonate bypass plasmid, complemented\n\
    \    by separate suf constructs in Yuda 2017 supplemental Figure S2a.\n  context:\
    \ UT109 carries pUMV22 Sp-r, pRK-sufABC-SE and pBBR-sufD encoding WT or H360A.\
    \ Compare LB plate\n    growth without MVA at 37 C for 24 h; the figure also includes\
    \ vector and other SufD substitutions.\n    Glucose supplementation of this particular\
    \ plate is not independently specified beyond the general\n    supplemented-medium\
    \ method.\n  family_mapping: Reference P77689 SufD, 423 aa, sequence version 1,\
    \ maps PF01458 to 166-393 and H360\n    falls within that region. UT109 is explicitly\
    \ an MG1655 derivative in Table S1. The allele is expressed\n    as an intact\
    \ protein, not an isolated domain or the homologous SufB protein.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:83333\n  limitations: This is failed complementation\
    \ under a specific bypass-dependent condition, not unconditional\n    lethality\
    \ or observed iron ligation. SufD H360A abundance is somewhat lower in the separately\
    \ supplemented\n    liquid-culture Western experiment; altered abundance can contribute.\
    \ MVA-supported viability and WT\n    complementation do not establish a residue-specific\
    \ chemical mechanism.\n  nodes:\n  - node_id: h360a-complementing-allele\n   \
    \ label: H360A rather than WT SufD in the UT109 complementation system\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:P77689\n  - node_id: ut109-growth-without-mva\n\
    \    label: Plate growth without MVA at 37 C after 24 h\n    node_type: PHENOTYPE\n\
    \  edges:\n  - edge_id: h360a-decreases-complementation-growth\n    subject: h360a-complementing-allele\n\
    \    predicate: decreases\n    object: ut109-growth-without-mva\n    mechanism:\
    \ H360A does not support the WT-complemented growth phenotype in the visually\
    \ inspected S2a\n      plates. The cellular effect remains indirect because Fe-S\
    \ assembly, expression and downstream metabolism\n      are not resolved into\
    \ a measured molecular chain.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:28839209\n\
    \      source_url: https://www.nature.com/articles/s41598-017-09846-2\n      snippet:\
    \ did not complement\n      explanation: Supplemental Figure S2a and Table S1\
    \ establish the phenotype and strain; the main-text\n        abundance qualification\
    \ and S2c prevent an equal-expression or direct-ligation claim.\n      cache_path:\
    \ evidence/PF01458/yuda-2017-sufbd.txt\n      cache_sha256: 1542a7061896016ba21f51ad63de0706c194cff8e9cdb9b4042302df6039e8f4\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P77689/entry/pfam/PF01458/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P77689/entry/pfam/PF01458/\n\
    \      snippet: 'SufD Pfam:PF01458; domain interval: 166-393, inclusive.'\n  \
    \    explanation: Locates H360 in the homologous SufD core without transferring\
    \ SufB-specific sulfur\n        effects to it.\n      cache_path: evidence/PF01458/SufBD-identity.txt\n\
    \      cache_sha256: 60f41fd4f59263bdb4ab0c06763778e6c5290f83d9e1ba8c3e98c6f7f512abdb\n\
    - graph_id: ecoli-sufd-h360a-holo-fdx\n  title: SufD H360A lowers detected holo-Fdx\
    \ in complemented UT109 cells\n  scope: The SufD H360A cellular comparison in\
    \ Yuda 2017 supplemental Figure S2b, separate from unsupplemented\n    plate growth\
    \ and from purified SufB reactions.\n  context: UT109 with pUMV22 Sp-r, pRK-sufABC-SE\
    \ and WT or H360A pBBR-sufD is grown in Superbroth with\n    glucose and MVA at\
    \ 37 C to early stationary phase. General supplementation is 0.4% glucose and\
    \ 200\n    uM racemic mevalonolactone. Cell-density-normalized lysates undergo\
    \ native PAGE and anti-Fdx Western\n    blotting; Suf protein abundance is assessed\
    \ separately by SDS-PAGE/Western blotting.\n  family_mapping: P77689 SufD contains\
    \ PF01458 at 166-393, including H360. This is a whole-protein substitution\n \
    \   in an MG1655-derived host; the family also contains SufB but its reactions\
    \ are not equivalent experimental\n    evidence.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:83333\n  limitations: Holo-Fdx signal is not a direct measurement\
    \ of all cellular Fe-S clusters or a purified\n    insertion reaction. Apo-Fdx\
    \ is not detected, so total Fdx stability is an alternative contribution.\n  \
    \  SufD H360A is somewhat less abundant; the Western control does not establish\
    \ equal expression. No\n    quantified fold-change, replicate confidence or serial\
    \ connection to the plate-growth graph is claimed.\n  nodes:\n  - node_id: h360a-supplemented-culture\n\
    \    label: H360A rather than WT SufD in MVA/glucose-supplemented UT109 cultures\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:P77689\n  - node_id:\
    \ detected-holo-fdx\n    label: Holo-Fdx band detected in cell-density-normalized\
    \ native-PAGE immunoblots\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: h360a-decreases-holo-fdx-signal\n\
    \    subject: h360a-supplemented-culture\n    predicate: decreases\n    object:\
    \ detected-holo-fdx\n    mechanism: S2b shows less detected holo-Fdx with H360A\
    \ than with WT SufD under the supplemented liquid-culture\n      conditions. The\
    \ result is retained as an indirect cellular maturation-associated phenotype,\
    \ not\n      direct proof of a particular Fe-S ligand or transfer route.\n   \
    \ directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:28839209\n      source_url: https://www.nature.com/articles/s41598-017-09846-2\n\
    \      snippet: maturation failure\n      explanation: Visually inspected S2b/c,\
    \ Figure 1's referenced assay caption and Methods support the\n        endpoint\
    \ and abundance qualification. This culture contains MVA absent from the separate\
    \ plate\n        comparison; exact plate glucose is unresolved.\n      cache_path:\
    \ evidence/PF01458/yuda-2017-sufbd.txt\n      cache_sha256: 1542a7061896016ba21f51ad63de0706c194cff8e9cdb9b4042302df6039e8f4\n\
    curation_events:\n- timestamp: '2026-10-11T10:41:56Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate separate SufB biochemical and\
    \ SufD cellular causal effects\n  history_record: history/records/PF01458/2026-10-11T104156Z-codex-3dec5b.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: P77522 SufB is 495 aa, sequence version 2, with PF01458 225-466; P77689
    SufD is 423 aa, sequence version 1, with PF01458 166-393. Both sequences match
    InterPro and contain the stated tested residues. C254A/C405A primer pairs encode
    the intended local substitutions. Table S1 specifies MG1655-derived UT109/YT2512.
    Complete historical clones and all junctions remain unverified, and homologous
    domain membership does not make SufB and SufD functions interchangeable.
  target_ids:
  - PF01458
  evidence_ids:
  - identity
  - primary
  - supplemental-controls
  - sufd-mapping
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Five direct edges describe net purified-system comparisons, not atom-resolved
    sulfur chemistry. The no-DTT sulfur-loading reaction is separate from the DTT-containing
    sulfide-output reaction; C405A's preserved stimulation and C358A's retained sulfur
    are kept as qualifiers. SufD cellular edges are indirect and use different plate
    versus liquid conditions. Lower H360A abundance and Fdx stability remain alternatives.
    Proposed tunnel, FADH2, ATP motion and ligand models do not become observed edges.
  target_ids:
  - PF01458
  evidence_ids:
  - primary
  - native
  - supplemental-controls
  - sufd-mapping
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: The remaining mutant matrix, prior primary studies, full historical constructs,
    some plate supplementation details, raw blots/measurements and direct site-resolved
    chemical intermediates remain uncurated. Bacterial, archaeal and plastid members
    and isolated-domain sufficiency are not comprehensively covered. Figures 1/2/3/5/6
    and S1/S4 were not independently visually assessed; their text/captions are not
    equivalent to plotted-data review.
  target_ids:
  - PF01458
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01458-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve constructs and chemical intermediates before extending SufBD causal
    pathways
  description: Obtain full clone records and independently resolved sulfur/iron intermediates,
    reconcile plate supplementation and mutant abundance, and review remaining primary
    experiments and members. Keep SufB and SufD distinctions, C405A's endpoint-specific
    behavior and the proposed tunnel clearly separated. Curate supported extensions
    with their own exact contexts and save successor reviews.
  target_ids:
  - PF01458
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - supplemental-controls
  - sufd-mapping
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01458.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Obtain full clone records and independently resolved sulfur/iron intermediates,
    reconcile plate supplementation and mutant abundance, and review remaining primary
    experiments and members. Keep SufB and SufD distinctions, C405A's endpoint-specific
    behavior and the proposed tunnel clearly separated. Curate supported extensions
    with their own exact contexts and save successor reviews.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01458
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Main Results/Discussion/Methods and supplemental tables/captions were read. Figure
  4 and S2/S3 were visually checked; other figures and raw measurements were not independently
  analyzed. Local primer translation verifies only the C254A/C405A coding neighborhoods,
  not complete constructs. PMC HTML returned a challenge, while publisher HTML and
  the original supplement were accessible.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
