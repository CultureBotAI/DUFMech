# PF01927 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review

- Review: 20261025T132049Z-pf01927-c3s4-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-25T13:20:48Z
- Finished UTC: 2026-10-25T13:20:49Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Four evidence ledgers support14 graphs with24 OBSERVED edges:19 DIRECT biochemical or physical assembly effects,3 INDIRECT cellular effects and2 UNRESOLVED coexpression recovery effects. Eleven graphs are MECHANISTIC and three PHENOTYPIC. Native overlay integrity and all24 primary quotations pass, using25 unique quoted words jointly from the paper. Same-agent partial scientific assessment; two OPEN discussions and IN_PROGRESS status retain coverage and construct uncertainties. Cycle 3 Stage 3 (PR #357) grounded the MUT-7 mitotic germline localization node focal and RNA-binding FP state node binding to C. elegans MUT-7 (UniProtKB:P34607), and the EXD3 RNA-binding FP state node binding to H. sapiens EXD3 (UniProtKB:Q8N9H8). Stage 4 frozen-inventory review verified all causal graphs and grounded nodes against primary evidence caches.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Ascending remaining frozen Pfam accession after PF01925. All8296 families and open context follow-ups remain in the corpus-wide goal.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0e26e9cdab5214d838db4f53ddefbf83772241fb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01927 | data/families/PF01927.yaml | generated | PF01927 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01927 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01927.

Frozen PF01927 Mut7-C/IPR002782/EX_DUF and formerDUF82 are preserved. CeMUT-7 P34607v1 is910aa with current Pfam666-779; HsEXD3 Q8N9H8v3 is876aa with match631-734. Broad CTDs633-910 and624-876 exceed those matches. CeD435,R853,T855,W812stop andHsD399 are OUTSIDE Pfam. Reference CeI453 supports retaining the paper's D435A/D453A discrepancy. Partner MUT-16 uses O62011 longer-isoform numbering. Protein, construct and isolated-domain effects are not conflated.

### Directed effects and limits

graph: supported. Targets: PF01927.

Complex formation, composite MUT-16 capture and crowded-mixture droplets are separate physical contexts, not isolated-component sufficiency or direct MUT-7/MUT-16 contact. Two coprecipitation changes retain unresolved directness because folding and MUT-8 solubility may affect recovery. Untagged RNAi hatch phenotypes and tagged HA localization use distinct strains and remain indirect. No all-foci dissolution or exclusive localization-to-RNAi chain is asserted. FP and cleavage comparisons retain broad-CTD scope, tags, salt conditions and extra-domain alleles. Figure7A33.4uM conflicts with Results18.7/S8C18.69; no exact fold is adopted. Figure5D435A/D453A and the imaging reagent mismatch remain explicit. Salt/fold changes are joint contexts; no MUT-8 activation or observed native22G trimming mechanism is inferred.

### Remaining family coverage

completeness: concern. Targets: PF01927.

The 2024 study and inspected supplement do not characterize all5065 frozen proteins. Original1999/2005 genetics,2021 neuronal contexts,2025 MUT-16/MUT-8 study,plantWEX and prokaryotic members need full primary-assay review. Thermococcus RNA binding is predicted and Nibbler lacks the CTD; neither is an observed Pfam edge. Exact per-panel full-length clone/tag assignments, binding-fit and allele-numbering discrepancies, actual imaging reagent, native substrate identity and isolated-Pfam sufficiency remain open.

### Cycle 3 causal-graph and protein-node grounding verification

representation: supported. Targets: PF01927.

Cycle 3 Stage 3 (PR #357) grounded the MUT-7 mitotic germline localization node focal and RNA-binding FP state node binding to C. elegans MUT-7 (UniProtKB:P34607), and the EXD3 RNA-binding FP state node binding to H. sapiens EXD3 (UniProtKB:Q8N9H8). Stage 4 frozen-inventory review verified all causal graphs and grounded nodes against primary evidence caches.

## Findings

### additional-contexts: Resolve construct and source conflicts and extend native-function/member coverage

minor / open / confirmed; issue key: pf01927-causal-context-coverage.

Resolve the Figure7A/S8C affinity discrepancy, D435A/D453A naming, cleavage-panel full-length clone assignment and actual imaging reagent. Review the remaining historical, neuronal, plant and prokaryotic primary contexts and the published2025 assembly study. Seek member-specific native RNA and isolated-domain evidence without transferring predicted contacts or joining different strains into an observed molecular pathway. Preserve current conditional negatives and IN_PROGRESS status until warranted successor review.

## Recommended Actions And Acceptance Checks

### extend-contexts

Resolve the Figure7A/S8C affinity discrepancy, D435A/D453A naming, cleavage-panel full-length clone assignment and actual imaging reagent. Review the remaining historical, neuronal, plant and prokaryotic primary contexts and the published2025 assembly study. Seek member-specific native RNA and isolated-domain evidence without transferring predicted contacts or joining different strains into an observed molecular pathway. Preserve current conditional negatives and IN_PROGRESS status until warranted successor review.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/; Busetto2024 Figures5 and7; Methods; publisher supplement S8 and TablesS1/S2. | supports | Separate worm and human truncation assays support reduced RNA-binding response and slower RNA degradation, with retained truncated-protein activity. Metal and KCl/LiCl assays have context-specific substrate effects. The experimental CTDs exceed current Pfam intervals; isolated CTDs are not demonstrated nucleases. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01927/; Accession and domain locations; paired UniProt identity facts | supports | Frozen PF01927 Mut7-C/IPR002782/EX_DUF and formerDUF82 are preserved. CeMUT-7 P34607v1 is910aa with current Pfam666-779; HsEXD3 Q8N9H8v3 is876aa with match631-734. Broad CTDs633-910 and624-876 exceed those matches. CeD435,R853,T855,W812stop andHsD399 are OUTSIDE Pfam. Reference CeI453 supports retaining the paper's D435A/D453A discrepancy. Partner MUT-16 uses O62011 longer-isoform numbering. Protein, construct and isolated-domain effects are not conflated. |
| complex-cellular | https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/; Figures1-4/6; supplement S2/S3/S5 and TablesS1/S2/S4 | supports | Physical assembly and composite capture/droplet readouts are separated from coexpression recovery and strain-specific cellular phenotypes; solubility, abundance, tags and persistent MUT-16 foci qualify inference. |
| manufacturer | https://documents.thermofisher.com/TFS-Assets/BID/certificate/Certificates-of-Analysis/A11029%20Lot%202306579%20CofA.pdf; Page1 catalog/product fields, lot2306579 certificate dated18-Feb-2021 | supports | Manufacturer identifies A11029 as Alexa Fluor488, confirming a mismatch with the study's stated Alexa Fluor555. Neither the actual experiment's reagent nor its lot is established by this certificate. |
| coverage | evidence/PF01927/constructs-and-coverage.txt; Construct tables, scoped literature search and access ledger | supports | Boundary/tag assignments, broader unreviewed member contexts, nonadopted predicted complexes and access limits are retained. No family-wide negative or exhaustive characterization is claimed. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| stage4-prior-review | reviews/structured/20261023T092552Z-pf01927-c2s4-record-review/review.yaml; Predecessor structured review 20261023T092552Z-pf01927-c2s4-record-review | supports | Predecessor review 20261023T092552Z-pf01927-c2s4-record-review verified and linked for finding continuity and semantic-digest progression on PF01927. |
| duf-projection-pf01927 | data/families/PF01927.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- All original main figures1-7 and rendered supplement S2/S3/S5/S8 and TablesS1/S2/S4 were inspected during curation; crystallographic statistics were read as text. The manufacturer A11029 certificate was inspected for catalog identity only. No raw-data reanalysis, exact plasmid resequencing, independent expert endorsement or exhaustive family source survey. Browser/corpus verification is reported separately after retention.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T132049Z-pf01927-c3s4-record-review
title: PF01927 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review
started_at: '2026-10-25T13:20:48Z'
finished_at: '2026-10-25T13:20:49Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Claude-Opus-4.6
  independence: self_review
  independence_basis: Cycle 3 Stage 4 frozen-inventory record review by Antigravity
    auditing prior curation overlays, primary evidence caches, history events, and
    current projections at Git revision 0e26e9cdab5214d838db4f53ddefbf83772241fb.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: true
summary: 'Four evidence ledgers support14 graphs with24 OBSERVED edges:19 DIRECT biochemical
  or physical assembly effects,3 INDIRECT cellular effects and2 UNRESOLVED coexpression
  recovery effects. Eleven graphs are MECHANISTIC and three PHENOTYPIC. Native overlay
  integrity and all24 primary quotations pass, using25 unique quoted words jointly
  from the paper. Same-agent partial scientific assessment; two OPEN discussions and
  IN_PROGRESS status retain coverage and construct uncertainties. Cycle 3 Stage 3
  (PR #357) grounded the MUT-7 mitotic germline localization node focal and RNA-binding
  FP state node binding to C. elegans MUT-7 (UniProtKB:P34607), and the EXD3 RNA-binding
  FP state node binding to H. sapiens EXD3 (UniProtKB:Q8N9H8). Stage 4 frozen-inventory
  review verified all causal graphs and grounded nodes against primary evidence caches.'
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 0e26e9cdab5214d838db4f53ddefbf83772241fb
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01927.yaml
    sha256: a29d2ba81a8057bc3987b94cfab4d9a24f36bce3b28d3eb435ec8ef0c0734be2
    role: context
  - path: data/families/PF01927.yaml
    sha256: 59596c552ccb715e7a794e2b498277870f691c836aef64a4d2cbd6794db812f8
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
  - path: evidence/PF01927/busetto-2024-biochemistry.txt
    sha256: 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977
    role: context
  - path: evidence/PF01927/busetto-2024-complex-cellular.txt
    sha256: 140a97c1f5d0f2b6476948a27cc47f4ad50d1d774532d9ab2176e46c033d91f0
    role: context
  - path: evidence/PF01927/constructs-and-coverage.txt
    sha256: 41b96b71514c3119fb4c1b3f091e6959830020f1541025196c5545870b7f5cf4
    role: context
  - path: evidence/PF01927/identity.txt
    sha256: c68a3627c9cd2abfcbfea411124df9d3bb084e3e2bbdb0faab1aee438ec82de2
    role: context
  - path: reviews/structured/20261023T092552Z-pf01927-c2s4-record-review/review.yaml
    sha256: 7ea21a3ed7bc8ad2191ea4a597e2bde7b5b963c8a60d16d4ce088cca99d3aa21
    role: context
targets:
- target_id: PF01927
  path: data/families/PF01927.yaml
  label: PF01927
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01927.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: b216bcc94cd34267d9c781842398e6b94c73fbe7b60c64e40a5bda351317ba04
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Ascending remaining frozen Pfam accession after PF01925. All8296 families
    and open context follow-ups remain in the corpus-wide goal.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01927
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: The 2024 study and inspected supplement do not characterize all5065 frozen
      proteins. Original1999/2005 genetics,2021 neuronal contexts,2025 MUT-16/MUT-8
      study,plantWEX and prokaryotic members need full primary-assay review. Thermococcus
      RNA binding is predicted and Nibbler lacks the CTD; neither is an observed Pfam
      edge. Exact per-panel full-length clone/tag assignments, binding-fit and allele-numbering
      discrepancies, actual imaging reagent, native substrate identity and isolated-Pfam
      sufficiency remain open.
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
  - PF01927
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/
  locator: Busetto2024 Figures5 and7; Methods; publisher supplement S8 and TablesS1/S2.
  accessed_at: '2026-10-12T02:44:36Z'
  support: supports
  snapshot_sha256: 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977
  summary: Separate worm and human truncation assays support reduced RNA-binding response
    and slower RNA degradation, with retained truncated-protein activity. Metal and
    KCl/LiCl assays have context-specific substrate effects. The experimental CTDs
    exceed current Pfam intervals; isolated CTDs are not demonstrated nucleases.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01927/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-12T02:44:36Z'
  support: supports
  snapshot_sha256: c68a3627c9cd2abfcbfea411124df9d3bb084e3e2bbdb0faab1aee438ec82de2
  summary: Frozen PF01927 Mut7-C/IPR002782/EX_DUF and formerDUF82 are preserved. CeMUT-7
    P34607v1 is910aa with current Pfam666-779; HsEXD3 Q8N9H8v3 is876aa with match631-734.
    Broad CTDs633-910 and624-876 exceed those matches. CeD435,R853,T855,W812stop andHsD399
    are OUTSIDE Pfam. Reference CeI453 supports retaining the paper's D435A/D453A
    discrepancy. Partner MUT-16 uses O62011 longer-isoform numbering. Protein, construct
    and isolated-domain effects are not conflated.
- evidence_id: complex-cellular
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/
  locator: Figures1-4/6; supplement S2/S3/S5 and TablesS1/S2/S4
  summary: Physical assembly and composite capture/droplet readouts are separated
    from coexpression recovery and strain-specific cellular phenotypes; solubility,
    abundance, tags and persistent MUT-16 foci qualify inference.
  accessed_at: '2026-10-12T02:44:36Z'
  support: supports
  snapshot_sha256: 140a97c1f5d0f2b6476948a27cc47f4ad50d1d774532d9ab2176e46c033d91f0
- evidence_id: manufacturer
  kind: primary_source
  reference: https://documents.thermofisher.com/TFS-Assets/BID/certificate/Certificates-of-Analysis/A11029%20Lot%202306579%20CofA.pdf
  locator: Page1 catalog/product fields, lot2306579 certificate dated18-Feb-2021
  summary: Manufacturer identifies A11029 as Alexa Fluor488, confirming a mismatch
    with the study's stated Alexa Fluor555. Neither the actual experiment's reagent
    nor its lot is established by this certificate.
  accessed_at: '2026-10-12T02:44:36Z'
  support: supports
  snapshot_sha256: 140a97c1f5d0f2b6476948a27cc47f4ad50d1d774532d9ab2176e46c033d91f0
- evidence_id: coverage
  kind: search
  reference: evidence/PF01927/constructs-and-coverage.txt
  locator: Construct tables, scoped literature search and access ledger
  search_scope: PF01927/DUF82/MUT7-C/MUT-7/EXD3/CTD/RDE-2/MUT-8 and2025-2026 updates;
    ignored/hidden-inclusive local searches. Full review of the adopted2024 source
    but only stated abstract/selected-section coverage of other leads.
  summary: Boundary/tag assignments, broader unreviewed member contexts, nonadopted
    predicted complexes and access limits are retained. No family-wide negative or
    exhaustive characterization is claimed.
  accessed_at: '2026-10-12T02:44:36Z'
  support: supports
  snapshot_sha256: 41b96b71514c3119fb4c1b3f091e6959830020f1541025196c5545870b7f5cf4
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-12T02:44:36Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: stage4-prior-review
  kind: prior_review
  reference: reviews/structured/20261023T092552Z-pf01927-c2s4-record-review/review.yaml
  locator: Predecessor structured review 20261023T092552Z-pf01927-c2s4-record-review
  accessed_at: '2026-10-25T13:20:49Z'
  support: supports
  snapshot_sha256: 7ea21a3ed7bc8ad2191ea4a597e2bde7b5b963c8a60d16d4ce088cca99d3aa21
  summary: Predecessor review 20261023T092552Z-pf01927-c2s4-record-review verified
    and linked for finding continuity and semantic-digest progression on PF01927.
- evidence_id: duf-projection-pf01927
  kind: record_content
  reference: data/families/PF01927.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-25T13:20:49Z'
  support: context_only
  snapshot_sha256: 59596c552ccb715e7a794e2b498277870f691c836aef64a4d2cbd6794db812f8
  quote: "id: Pfam:PF01927\npfam_id: PF01927\nname: Mut7-C RNAse domain\nshort_name:\
    \ Mut7-C\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01927\n\
    counters:\n  proteins: 5065\n  matches: 5593\n  proteomes: 4159\n  taxa: 8924\n\
    \  structures: 1\n  alphafold_models: 3652\n  domain_architectures: 48\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002782\ndescription: RNAse domain of the PIN fold [[cite:PUB00066661]]\
    \ with an inserted Zinc Ribbon at the C terminus\n  [[cite:PUB00034476]].\ncuration_history:\
    \ history/records/PF01927\ndiscussions:\n- discussion_id: pf01927-domain-and-source-boundaries\n\
    \  prompt: Resolve construct and source discrepancies without treating broad-CTD\
    \ assays as isolated Pfam\n    mechanisms.\n  kind: CURATION_TODO\n  status: OPEN\n\
    \  rationale: The experimental CTD is wider than the current Pfam match; extra-domain\
    \ substitutions, affinity-label\n    conflicts and tag differences limit attribution.\n\
    \  evidence:\n  - reference: PMID:39188014\n    supports: PARTIAL\n    evidence_source:\
    \ primary_constructs_figures_and_supplement\n    explanation: Separate binding,cleavage,coexpression\
    \ and cellular readouts support scoped effects;\n      they do not prove the matched\
    \ Pfam segment is sufficient.\n  posed_by: Codex\n  posed_date: '2026-10-12'\n\
    \  notes: Ce PF01927 666-779 versusCTD633-910; Hs631-734 versus624-876. R853/T855,D435,D399\
    \ andW812stop\n    are outside the matches. Figure7A truncated Kd33.4 conflicts\
    \ with Results18.7/S8C18.69. Figure5/S1\n    D435A conflicts with Results D453A.\
    \ Preserve uncertain FL clone/tag assignment,reagent-label discrepancy\n    and\
    \ coexpression-solubility confounds. No intrinsic isolated-CTD nuclease is demonstrated.\n\
    - discussion_id: pf01927-native-function-and-member-coverage\n  prompt: Extend\
    \ primary evidence for native RNA targets and remaining animal,plant and prokaryotic\
    \ member\n    contexts.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: One\
    \ domain-focused study does not characterize all5065 frozen proteins or all native\
    \ small-RNA\n    mechanisms.\n  evidence:\n  - reference: PMID:39188014\n    supports:\
    \ PARTIAL\n    evidence_source: primary_results_and_discussion\n    explanation:\
    \ Native small-RNA substrates and the ancestral archaeal/bacterial role remain\
    \ unresolved\n      despite animal binding and degradation assays.\n  - reference:\
    \ PMID:33646120\n    supports: PARTIAL\n    evidence_source: abstract_level_followup\n\
    \    explanation: Neuronal MUT-7/22G contexts require a separate primary-assay\
    \ and construct review.\n  - reference: PMID:40781776\n    supports: PARTIAL\n\
    \    evidence_source: published_update_abstract\n    explanation: MUT-16/MUT-8\
    \ simulations and experiments update the earlier preprint,not a directly adopted\n\
    \      PF01927 mechanism.\n  posed_by: Codex\n  posed_date: '2026-10-12'\n  notes:\
    \ Tops2005,Ketting1999,Hsu2021,plantWEX and other member studies remain follow-ups;\
    \ no full-family\n    negative claim. Thermococcus RNA binding is predicted here,not\
    \ observed; Drosophila Nibbler lacks\n    the tested CTD. Conditional negatives\
    \ and raw-data limitations are retained in evidence/PF01927. No\n    simulated\
    \ RNA forceps mechanism, direct MUT-7/MUT-16 contact or all-foci dissolution is\
    \ asserted.\ncausal_graphs:\n- graph_id: cemut7-ctd-complex-2024\n  title: Broad\
    \ MUT-7 and MUT-8 CTDs form a stable complex\n  scope: Busetto2024 purified CeMUT-7\
    \ 633-910 and CeMUT-8 322-578; shorter crystallized pair633-899/322-567\n    is\
    \ independent structural support.\n  context: Coexpression and purification with3C\
    \ tag cleavage; S2A SEC-MALS at5.4mg/ml,20mM Tris pH7.5,150mM\n    NaCl,2mM DTT.\
    \ Approximately60kDa complex versus32/29kDa components;8Q66 resolves the trimmed\
    \ pair.\n  family_mapping: CeMUT-7 P34607 sequence v1,910aa,taxon6239; current\
    \ PF01927 is666-779, inside the broader\n    experimental CTD633-910. NTD-EXO1-625\
    \ removes additional flanking residues. D435,R853,T855 and pk204\n    W812stop\
    \ are OUTSIDE the matched interval. These are whole-protein or broad-CTD assays,\
    \ not isolated666-779\n    sufficiency.\n  taxon: NCBITaxon:6239\n  scope_status:\
    \ MECHANISTIC\n  limitations: Joint composition is required in this observation.\
    \ No dissociation constant, assembly kinetics,\n    native substrate or isolated-Pfam\
    \ sufficiency is measured. CTD boundaries exceed the current match;\n    the structure\
    \ is not an RNA-bound catalytic intermediate.\n  nodes:\n  - node_id: pair\n \
    \   label: CeMUT-7 CTD plus CeMUT-8 CTD\n    node_type: STATE\n    grounding:\n\
    \    - UniProtKB:P34607\n    - UniProtKB:Q19672\n  - node_id: complex\n    label:\
    \ Stable purified CTD heterodimer\n    node_type: STATE\n    grounding:\n    -\
    \ UniProtKB:P34607\n    - UniProtKB:Q19672\n  edges:\n  - edge_id: pair-complex\n\
    \    subject: pair\n    predicate: produces\n    object: complex\n    mechanism:\
    \ The coexpressed broad CTDs yield an isolable heterodimer supported by SEC-MALS\
    \ and the\n      structure of the slightly trimmed pair.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:39188014\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n\
    \      snippet: heterodimer\n      explanation: Results interaction section; Figure1,\
    \ S2A and Figure2/8Q66. Physical assembly, not\n        a claim of activation.\n\
    \      cache_path: evidence/PF01927/busetto-2024-complex-cellular.txt\n      cache_sha256:\
    \ 140a97c1f5d0f2b6476948a27cc47f4ad50d1d774532d9ab2176e46c033d91f0\n- graph_id:\
    \ cemut7-interface-pulldown-2024\n  title: CTD perturbations reduce MUT-8 coprecipitation\n\
    \  scope: 'Busetto2024 MBP coexpression pulldowns: WT633-910 versus R853E/T855E633-910\
    \ or CTD-C773-910,\n    with MUT-8 CTD322-578.'\n  context: Figure4C and S3H;\
    \ TableS2 Ce285,Ce302,Ce349 and Ce299. N-His10-MBP-3C bait, N-His10-3C prey;\n\
    \    amylose retention from BL21(DE3)-derivative lysate. Lysis250mM NaCl,pH8.0;\
    \ resin1-2h at4C; lysate,supernatant,eluate\n    and prey-only controls.\n  family_mapping:\
    \ CeMUT-7 P34607 sequence v1,910aa,taxon6239; current PF01927 is666-779, inside\
    \ the broader\n    experimental CTD633-910. NTD-EXO1-625 removes additional flanking\
    \ residues. D435,R853,T855 and pk204\n    W812stop are OUTSIDE the matched interval.\
    \ These are whole-protein or broad-CTD assays, not isolated666-779\n    sufficiency.\n\
    \  taxon: NCBITaxon:6239\n  scope_status: PHENOTYPIC\n  limitations: R853E/T855E\
    \ are outside PF01927;773-910 overlaps only the matched interval's end. MUT-8\n\
    \    solubility depends on coexpression partner, so these are recovery effects\
    \ with UNRESOLVED directness,\n    not measured affinities or exclusive contact\
    \ disruption. Purified mutant-folding equivalence is not\n    demonstrated.\n\
    \  nodes:\n  - node_id: double\n    label: R853E/T855E broad CTD versus WT CTD\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:P34607\n  - node_id:\
    \ short\n    label: CTD-C773-910 versus CTD633-910\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:P34607\n  - node_id: retained\n    label: MUT-8\
    \ CTD recovered in MBP eluate\n    node_type: STATE\n    grounding:\n    - UniProtKB:Q19672\n\
    \  edges:\n  - edge_id: double-loss\n    subject: double\n    predicate: decreases\n\
    \    object: retained\n    mechanism: The double-substituted bait recovers less\
    \ MUT-8 CTD in the matched coexpression assay;\n      folding and prey solubility\
    \ remain alternative contributors.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:39188014\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n      snippet:\
    \ failed to co-precipitate\n      explanation: Figure4C; matched bait, prey and\
    \ fraction lanes.\n      cache_path: evidence/PF01927/busetto-2024-complex-cellular.txt\n\
    \      cache_sha256: 140a97c1f5d0f2b6476948a27cc47f4ad50d1d774532d9ab2176e46c033d91f0\n\
    \  - edge_id: short-loss\n    subject: short\n    predicate: decreases\n    object:\
    \ retained\n    mechanism: The shortened CTD-C bait recovers MUT-8 poorly compared\
    \ with the broader CTD; residual\n      recovery is not treated as zero binding.\n\
    \    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:39188014\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n\
    \      snippet: co-precipitated poorly\n      explanation: S3H and corresponding\
    \ Results; CTD-C retains some coprecipitation.\n      cache_path: evidence/PF01927/busetto-2024-complex-cellular.txt\n\
    \      cache_sha256: 140a97c1f5d0f2b6476948a27cc47f4ad50d1d774532d9ab2176e46c033d91f0\n\
    - graph_id: cemut7-mut16-capture-2024\n  title: The joint MUT-7/MUT-8 complex\
    \ is captured by MUT-16\n  scope: Busetto2024 purified CeMUT-7 FL1-910/MUT-8 FL1-578\
    \ and GST-MUT-16 584-724, longer O62011 isoform\n    numbering.\n  context: Figure3B\
    \ and S5A/B.5uM proteins,20mM HEPES pH7.5,150mM NaCl,10%glycerol,0.05%IGEPAL,2mM\
    \ DTT;30min\n    preincubation,1-2h glutathione-resin incubation at4C. MUT-16\
    \ Ce298 retains GST/C-His10 in this assay.\n  family_mapping: CeMUT-7 P34607 sequence\
    \ v1,910aa,taxon6239; current PF01927 is666-779, inside the broader\n    experimental\
    \ CTD633-910. NTD-EXO1-625 removes additional flanking residues. D435,R853,T855\
    \ and pk204\n    W812stop are OUTSIDE the matched interval. These are whole-protein\
    \ or broad-CTD assays, not isolated666-779\n    sufficiency.\n  taxon: NCBITaxon:6239\n\
    \  scope_status: MECHANISTIC\n  limitations: MUT-7 alone and the CTD pair do not\
    \ show the full-pair capture. Beads without bait are\n    controls. The retained\
    \ association is mediated through the joint complex, not direct MUT-7/MUT-16\n\
    \    binding or PF01927 contact with MUT-16. Partner-only ITC does not measure\
    \ this ternary affinity.\n  nodes:\n  - node_id: joint\n    label: FL MUT-7/MUT-8\
    \ plus immobilized GST-MUT-16 fragment\n    node_type: STATE\n    grounding:\n\
    \    - UniProtKB:P34607\n    - UniProtKB:Q19672\n    - UniProtKB:O62011\n  - node_id:\
    \ capture\n    label: MUT-7/MUT-8 recovered with MUT-16 bait\n    node_type: STATE\n\
    \    grounding:\n    - UniProtKB:P34607\n    - UniProtKB:Q19672\n    - UniProtKB:O62011\n\
    \  edges:\n  - edge_id: joint-capture\n    subject: joint\n    predicate: enables\n\
    \    object: capture\n    mechanism: Purified full-length MUT-7/MUT-8 is recovered\
    \ by the MUT-16 fragment above bead-only control;\n      the experiment requires\
    \ the composite binding context.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:39188014\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n      snippet:\
    \ co-precipitated\n      explanation: Figure3B GST input/eluate lanes; S5 corroborates\
    \ fragment and CTD-pair comparisons.\n      cache_path: evidence/PF01927/busetto-2024-complex-cellular.txt\n\
    \      cache_sha256: 140a97c1f5d0f2b6476948a27cc47f4ad50d1d774532d9ab2176e46c033d91f0\n\
    - graph_id: cemut7-droplets-2024\n  title: Joint complex assembly promotes droplets\
    \ under crowding\n  scope: Busetto2024 full-length CeMUT-7/MUT-8 combined with\
    \ MUT-16 584-724; separate-component and minimal-pair\n    controls.\n  context:\
    \ Figure3F;10uM proteins,20mM Tris pH7.5,150mM NaCl,2mM DTT,5%PEG6000;100min incubation\
    \ before\n    bright-field imaging. Ce255/Ce15 tags cleaved; Ce298 GST cleaved\
    \ but C-His10 retained.\n  family_mapping: CeMUT-7 P34607 sequence v1,910aa,taxon6239;\
    \ current PF01927 is666-779, inside the broader\n    experimental CTD633-910.\
    \ NTD-EXO1-625 removes additional flanking residues. D435,R853,T855 and pk204\n\
    \    W812stop are OUTSIDE the matched interval. These are whole-protein or broad-CTD\
    \ assays, not isolated666-779\n    sufficiency.\n  taxon: NCBITaxon:6239\n  scope_status:\
    \ MECHANISTIC\n  limitations: An in-vitro droplet readout is not complete proof\
    \ of liquid-liquid phase separation, physiological\n    concentration dependence,\
    \ or a resolved PF01927 contact mechanism. Neither MUT-7 alone nor any component\n\
    \    alone is shown sufficient; the minimal MUT-8 NTD/MUT-16 pair also lacks comparable\
    \ droplets.\n  nodes:\n  - node_id: mixture\n    label: FL MUT-7/MUT-8 plus MUT-16\
    \ fragment under PEG crowding\n    node_type: STATE\n    grounding:\n    - UniProtKB:P34607\n\
    \    - UniProtKB:Q19672\n    - UniProtKB:O62011\n  - node_id: droplets\n    label:\
    \ Visible in-vitro droplets\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ joint-droplets\n    subject: mixture\n    predicate: produces\n    object: droplets\n\
    \    mechanism: The joint mixture develops droplets whereas the tested component\
    \ preparations do not; this\n      is a directly observed physical assembly effect\
    \ under the specified crowding condition.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:39188014\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n      snippet:\
    \ formed droplets\n      explanation: Figure3F bright-field panels and condensate\
    \ Methods; no cellular sufficiency transfer.\n      cache_path: evidence/PF01927/busetto-2024-complex-cellular.txt\n\
    \      cache_sha256: 140a97c1f5d0f2b6476948a27cc47f4ad50d1d774532d9ab2176e46c033d91f0\n\
    - graph_id: cemut7-pos1-rnai-2024\n  title: MUT-7 variants increase hatching during\
    \ pos-1 RNAi\n  scope: 'Busetto2024 Figure4D: N2 versus untagged RFK1714 xf367[R853E,T855E]\
    \ and RFK502 pk204.'\n  context: 20C; synchronized L1 exposure to pos-1-dsRNA\
    \ bacteria, continued through adulthood; first24h\n    of laid eggs scored. About15-20\
    \ parents per strain; empty-vector controls. Plotted values are means+/-SD,\n\
    \    not necessarily pooled egg ratios.\n  family_mapping: CeMUT-7 P34607 sequence\
    \ v1,910aa,taxon6239; current PF01927 is666-779, inside the broader\n    experimental\
    \ CTD633-910. NTD-EXO1-625 removes additional flanking residues. D435,R853,T855\
    \ and pk204\n    W812stop are OUTSIDE the matched interval. These are whole-protein\
    \ or broad-CTD assays, not isolated666-779\n    sufficiency.\n  taxon: NCBITaxon:6239\n\
    \  scope_status: PHENOTYPIC\n  limitations: Measured endpoint is viable progeny,\
    \ not RNA cleavage or22G abundance. Empty-vector hatch\n    rates differ by genotype.\
    \ Egg totals are not independent biological-replicate counts. Both variants\n\
    \    alter the broader CTD outside current PF01927; no exclusive localization-mediated\
    \ mechanism or isolated\n    domain requirement is asserted.\n  nodes:\n  - node_id:\
    \ double\n    label: Untagged R853E/T855E versus N2 under pos-1 RNAi\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:P34607\n  - node_id: stop\n  \
    \  label: pk204 W812stop versus N2 under pos-1 RNAi\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:P34607\n  - node_id: hatch\n    label: Progeny\
    \ hatching during pos-1 RNAi\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ double-hatch\n    subject: double\n    predicate: increases\n    object: hatch\n\
    \    mechanism: The double-mutant strain retains hatching when pos-1 RNAi strongly\
    \ suppresses WT hatching;\n      this is an indirect cellular RNAi-response phenotype.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:39188014\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n\
    \      snippet: RNAi-resistant animals\n      explanation: Figure4D and TableS4;\
    \ displayed pos-1 totals327/352 versus N2 1/1300.\n      cache_path: evidence/PF01927/busetto-2024-complex-cellular.txt\n\
    \      cache_sha256: 140a97c1f5d0f2b6476948a27cc47f4ad50d1d774532d9ab2176e46c033d91f0\n\
    \  - edge_id: stop-hatch\n    subject: stop\n    predicate: increases\n    object:\
    \ hatch\n    mechanism: The pk204 control strain also retains hatching under the\
    \ same challenge; a broad truncation\n      does not localize causality to the\
    \ Pfam match.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:39188014\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n      snippet: RNAi-resistant\
    \ animals\n      explanation: Figure4D pk204 positive-control bar,319/491; genotype\
    \ in TableS4 and Figure1.\n      cache_path: evidence/PF01927/busetto-2024-complex-cellular.txt\n\
    \      cache_sha256: 140a97c1f5d0f2b6476948a27cc47f4ad50d1d774532d9ab2176e46c033d91f0\n\
    - graph_id: cemut7-ha-localization-2024\n  title: The CTD interface variant loses\
    \ focal germline signal\n  scope: 'Busetto2024 Figure4E/F: RFK1754 HA-MUT-7 versus\
    \ RFK1755 HA-MUT-7(R853E,T855E), distinct from\n    untagged RNAi strains.'\n\
    \  context: Late-L4 hermaphrodite dissected mitotic germline; anti-HA immunofluorescence\
    \ with DAPI. Three\n    independent imaging replicates; N2 antibody-negative control.\
    \ Western blot with histoneH3 control\n    shows similar protein abundance. N-terminal\
    \ HA plus(GGGGS)x3 linker.\n  family_mapping: CeMUT-7 P34607 sequence v1,910aa,taxon6239;\
    \ current PF01927 is666-779, inside the broader\n    experimental CTD633-910.\
    \ NTD-EXO1-625 removes additional flanking residues. D435,R853,T855 and pk204\n\
    \    W812stop are OUTSIDE the matched interval. These are whole-protein or broad-CTD\
    \ assays, not isolated666-779\n    sufficiency.\n  taxon: NCBITaxon:6239\n  scope_status:\
    \ PHENOTYPIC\n  limitations: Loss of focal HA signal is indirect cellular localization\
    \ evidence, not direct measurement\n    of binding or RNA processing. S5E MUT-16::GFP\
    \ foci persist in a separate reporter strain; do not infer\n    dissolution of\
    \ all Mutator foci. Methods says Alexa Fluor555 while listing A11029; the manufacturer's\n\
    \    A11029 certificate identifies Alexa Fluor488. The actual experimental reagent\
    \ is not independently\n    resolved.\n  nodes:\n  - node_id: double\n    label:\
    \ HA-R853E/T855E versus HA-WT MUT-7\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:P34607\n  - node_id: focal\n    label: Focal MUT-7 signal in\
    \ mitotic germline\n    node_type: PHENOTYPE\n    grounding:\n    - UniProtKB:P34607\n\
    \  edges:\n  - edge_id: double-focal\n    subject: double\n    predicate: decreases\n\
    \    object: focal\n    mechanism: The matched tagged mutant has reduced focal\
    \ HA localization despite similar total abundance.\n      This supports a localization\
    \ effect but not an exclusively binding-mediated causal pathway.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:39188014\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n\
    \      snippet: no longer localizes\n      explanation: Figure4E/F with HA/HistoneH3\
    \ controls; TableS4 specifies the tagged strains.\n      cache_path: evidence/PF01927/busetto-2024-complex-cellular.txt\n\
    \      cache_sha256: 140a97c1f5d0f2b6476948a27cc47f4ad50d1d774532d9ab2176e46c033d91f0\n\
    - graph_id: cemut7-fp-rna-2024\n  title: Removing the broad worm CTD reduces RNA-binding\
    \ response\n  scope: 'Busetto2024 Figure7A: CeMUT-7 FL1-910 versus NTD-EXO1-625;\
    \ isolated633-910 and CTD/MUT-8 CTD\n    controls.'\n  context: FAM16-mer50nM;\
    \ protein titration,30min at room temperature;20mM HEPES pH7.5,150mM NaCl,10%glycerol,5mM\n\
    \    EDTA. RNA-only-subtracted FP; three measurements,mean+/-SD,Hill fits. S1\
    \ Ce409 FL retains C-His10\n    after N-MBP cleavage.\n  family_mapping: CeMUT-7\
    \ P34607 sequence v1,910aa,taxon6239; current PF01927 is666-779, inside the broader\n\
    \    experimental CTD633-910. NTD-EXO1-625 removes additional flanking residues.\
    \ D435,R853,T855 and pk204\n    W812stop are OUTSIDE the matched interval. These\
    \ are whole-protein or broad-CTD assays, not isolated666-779\n    sufficiency.\n\
    \  taxon: NCBITaxon:6239\n  scope_status: MECHANISTIC\n  limitations: Results/S8C\
    \ give18.7/18.69uM for truncated protein but Figure7A labels33.4uM; FL is2.325uM\n\
    \    in S8C. Bmax also differs. Preserve the lower observed response without choosing\
    \ an exact affinity\n    ratio. Isolated CTD fits are unstable; the missing interval\
    \ is larger than PF01927. No atomic RNA-contact\n    mechanism or folding equivalence\
    \ is established.\n  nodes:\n  - node_id: trunc\n    label: NTD-EXO1-625 versus\
    \ FL1-910\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:P34607\n\
    \  - node_id: binding\n    label: 16-mer RNA-binding FP response\n    node_type:\
    \ STATE\n    grounding:\n    - UniProtKB:P34607\n  edges:\n  - edge_id: trunc-binding\n\
    \    subject: trunc\n    predicate: decreases\n    object: binding\n    mechanism:\
    \ Removing the broader C-terminal region reduces the measured RNA-binding response;\
    \ the direction\n      is consistent despite the conflicting reported truncation-affinity\
    \ values.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:39188014\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n\
    \      snippet: weaker affinity\n      explanation: Figure7A, S8C and RNA-binding\
    \ Results; binding assay separate from cleavage.\n      cache_path: evidence/PF01927/busetto-2024-biochemistry.txt\n\
    \      cache_sha256: 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977\n\
    - graph_id: hsexd3-fp-rna-2024\n  title: Removing the broad human CTD reduces\
    \ RNA-binding response\n  scope: 'Busetto2024 Figure7B: human EXD3 FL1-876 D399A\
    \ versus NTD-EXO1-582 D399A; CTD624-876 control.'\n  context: FAM16-mer50nM; protein\
    \ titration,30min at room temperature;20mM HEPES pH7.5,250mM NaCl. RNA-only-subtracted\n\
    \    FP; three measurements,mean+/-SD,Hill fits. S1 Hs90/Hs91 have cleaved N-His10-MBP\
    \ tags.\n  family_mapping: Human EXD3 Q8N9H8 sequence v3,876aa,taxon9606; PF01927\
    \ is631-734. Experimental CTD624-876\n    is wider; NTD-EXO1-582 removes additional\
    \ residues. D399 is OUTSIDE PF01927. No isolated631-734 sufficiency\n    or family-wide\
    \ function is established.\n  taxon: NCBITaxon:9606\n  scope_status: MECHANISTIC\n\
    \  limitations: S8D fits1.862 versus11.15uM; CTD-only fit is unstable. Shared\
    \ D399A lies outside PF01927.\n    This is not active-WT catalysis, and worm/human\
    \ salt and mutation backgrounds differ. The truncated\n    interval is larger\
    \ than the Pfam match; no isolated-domain sufficiency.\n  nodes:\n  - node_id:\
    \ trunc\n    label: EXD3 NTD-EXO-D399A versus FL-D399A\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q8N9H8\n  - node_id: binding\n    label: 16-mer\
    \ RNA-binding FP response\n    node_type: STATE\n    grounding:\n    - UniProtKB:Q8N9H8\n\
    \  edges:\n  - edge_id: trunc-binding\n    subject: trunc\n    predicate: decreases\n\
    \    object: binding\n    mechanism: The shorter inactive EXD3 construct has a\
    \ weaker RNA-binding response than the longer inactive\n      construct under\
    \ matched human assay conditions.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:39188014\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n      snippet:\
    \ weaker affinity\n      explanation: Figure7B, S8D and RNA-binding Results; both\
    \ constructs share D399A.\n      cache_path: evidence/PF01927/busetto-2024-biochemistry.txt\n\
    \      cache_sha256: 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977\n\
    - graph_id: cemut7-cleavage-time-2024\n  title: MUT-7 CTD truncation slows RNA\
    \ degradation\n  scope: 'Busetto2024 Figure7C: active WT FL1-910 versus NTD-EXO1-625;\
    \ isolated CTD negative control.'\n  context: 0.5uM enzyme,1uM FAM28-mer,20mM\
    \ HEPES,150mM NaCl,2mM MnCl2,room temperature. TBE-urea PAGE\n    after2.5,10,15,30,60,120min\
    \ and overnight. Ce255 orCe409 FL panel assignment unresolved; Ce333 truncation\n\
    \    andCe285 CTD have cleaved N-tags.\n  family_mapping: CeMUT-7 P34607 sequence\
    \ v1,910aa,taxon6239; current PF01927 is666-779, inside the broader\n    experimental\
    \ CTD633-910. NTD-EXO1-625 removes additional flanking residues. D435,R853,T855\
    \ and pk204\n    W812stop are OUTSIDE the matched interval. These are whole-protein\
    \ or broad-CTD assays, not isolated666-779\n    sufficiency.\n  taxon: NCBITaxon:6239\n\
    \  scope_status: MECHANISTIC\n  limitations: Truncation retains activity; isolated\
    \ CTD is not an active nuclease. Qualitative gel time\n    courses are not fitted\
    \ turnover constants or identified native substrates. HEPES reaction pH is not\n\
    \    explicitly given. Removed sequence exceeds PF01927; no exclusive RNA-affinity\
    \ mediation is demonstrated.\n  nodes:\n  - node_id: fl\n    label: Purified active\
    \ FL1-910 with RNA and Mn\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:P34607\n\
    \  - node_id: trunc\n    label: NTD-EXO1-625 versus FL1-910\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:P34607\n  - node_id: rna\n    label: FAM28-mer\
    \ RNA substrate\n    node_type: STATE\n  - node_id: loss\n    label: RNA degradation\
    \ over the measured time course\n    node_type: PROCESS\n  edges:\n  - edge_id:\
    \ fl-cleavage\n    subject: fl\n    predicate: degrades\n    object: rna\n   \
    \ mechanism: The active full-length preparation converts the labelled substrate\
    \ into shorter products\n      across the displayed time course.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:39188014\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n\
    \      snippet: degraded RNA more efficiently\n      explanation: Figure7C FL\
    \ lanes and RNase Methods; CTD-only and no-enzyme controls.\n      cache_path:\
    \ evidence/PF01927/busetto-2024-biochemistry.txt\n      cache_sha256: 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977\n\
    \  - edge_id: trunc-slower\n    subject: trunc\n    predicate: decreases\n   \
    \ object: loss\n    mechanism: At matched time points the truncated preparation\
    \ degrades RNA less efficiently than full\n      length, without eliminating activity.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:39188014\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n\
    \      snippet: degraded RNA more efficiently\n      explanation: Figure7C side-by-side\
    \ FL/NTD-EXO time courses; no kinetic constant inferred.\n      cache_path: evidence/PF01927/busetto-2024-biochemistry.txt\n\
    \      cache_sha256: 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977\n\
    - graph_id: hsexd3-cleavage-time-2024\n  title: EXD3 CTD truncation slows RNA\
    \ degradation\n  scope: 'Busetto2024 Figure7D: active WT FL1-876 versus NTD-EXO1-582;\
    \ isolated CTD negative control.'\n  context: 0.5uM enzyme,1uM FAM28-mer,20mM\
    \ HEPES,250mM NaCl,2mM MnCl2,room temperature. TBE-urea PAGE\n    after2.5,10,15,30,60,120min\
    \ and overnight. Hs87/Hs88/Hs89; N-His10-MBP cleaved.\n  family_mapping: Human\
    \ EXD3 Q8N9H8 sequence v3,876aa,taxon9606; PF01927 is631-734. Experimental CTD624-876\n\
    \    is wider; NTD-EXO1-582 removes additional residues. D399 is OUTSIDE PF01927.\
    \ No isolated631-734 sufficiency\n    or family-wide function is established.\n\
    \  taxon: NCBITaxon:9606\n  scope_status: MECHANISTIC\n  limitations: Truncation\
    \ retains activity; isolated CTD is not an active nuclease. Qualitative gel time\n\
    \    courses are not fitted turnover constants or identified native substrates.\
    \ HEPES reaction pH is not\n    explicitly given. Removed sequence exceeds PF01927;\
    \ no exclusive RNA-affinity mediation is demonstrated.\n  nodes:\n  - node_id:\
    \ fl\n    label: Purified active FL1-876 with RNA and Mn\n    node_type: ACTIVITY\n\
    \    grounding:\n    - UniProtKB:Q8N9H8\n  - node_id: trunc\n    label: NTD-EXO1-582\
    \ versus FL1-876\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q8N9H8\n\
    \  - node_id: rna\n    label: FAM28-mer RNA substrate\n    node_type: STATE\n\
    \  - node_id: loss\n    label: RNA degradation over the measured time course\n\
    \    node_type: PROCESS\n  edges:\n  - edge_id: fl-cleavage\n    subject: fl\n\
    \    predicate: degrades\n    object: rna\n    mechanism: The active full-length\
    \ preparation converts the labelled substrate into shorter products\n      across\
    \ the displayed time course.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:39188014\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n      snippet:\
    \ degraded RNA more efficiently\n      explanation: Figure7D FL lanes and RNase\
    \ Methods; CTD-only and no-enzyme controls.\n      cache_path: evidence/PF01927/busetto-2024-biochemistry.txt\n\
    \      cache_sha256: 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977\n\
    \  - edge_id: trunc-slower\n    subject: trunc\n    predicate: decreases\n   \
    \ object: loss\n    mechanism: At matched time points the truncated preparation\
    \ degrades RNA less efficiently than full\n      length, without eliminating activity.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:39188014\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n\
    \      snippet: degraded RNA more efficiently\n      explanation: Figure7D side-by-side\
    \ FL/NTD-EXO time courses; no kinetic constant inferred.\n      cache_path: evidence/PF01927/busetto-2024-biochemistry.txt\n\
    \      cache_sha256: 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977\n\
    - graph_id: cemut7-cation-cleavage-2024\n  title: Mn and Mg support MUT-7 cleavage\
    \ in the tested assay\n  scope: Busetto2024 Figure5B purified CeMUT-7 FL1-910;\
    \ divalent-salt comparison at fixed protein and\n    RNA.\n  context: 0.5uM enzyme,1uM\
    \ FAM28-mer,30min at room temperature;20mM HEPES,50mM KCl;5mM MnCl2 orMgCl2\n\
    \    versus no divalent salt. No-protein,ZnCl2 andCaCl2 lanes are controls.\n\
    \  family_mapping: CeMUT-7 P34607 sequence v1,910aa,taxon6239; current PF01927\
    \ is666-779, inside the broader\n    experimental CTD633-910. NTD-EXO1-625 removes\
    \ additional flanking residues. D435,R853,T855 and pk204\n    W812stop are OUTSIDE\
    \ the matched interval. These are whole-protein or broad-CTD assays, not isolated666-779\n\
    \    sufficiency.\n  taxon: NCBITaxon:6239\n  scope_status: MECHANISTIC\n  limitations:\
    \ Mn gives stronger cleavage than Mg; Zn,Ca and no-ion lanes show no detectable\
    \ activity\n    here, not absolute inactivity in every condition. No physiological\
    \ cofactor exclusivity, isolated-CTD\n    catalysis or detailed metal-ion mechanism.\
    \ FL Ce255/Ce409 per-panel assignment and reaction pH are\n    unresolved.\n \
    \ nodes:\n  - node_id: mn\n    label: MnCl2 with MUT-7 and RNA versus no divalent\
    \ salt\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:P34607\n\
    \  - node_id: mg\n    label: MgCl2 with MUT-7 and RNA versus no divalent salt\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:P34607\n  - node_id:\
    \ products\n    label: Shortened labelled RNA products\n    node_type: STATE\n\
    \  edges:\n  - edge_id: mn-products\n    subject: mn\n    predicate: increases\n\
    \    object: products\n    mechanism: Mn supports substantial substrate cleavage\
    \ by the complete enzyme in this controlled reaction.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:39188014\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n\
    \      snippet: highest\n      explanation: Figure5B Mn lane and metal-dependent\
    \ Results identify Mn as supporting the strongest\n        activity in this assay.\n\
    \      cache_path: evidence/PF01927/busetto-2024-biochemistry.txt\n      cache_sha256:\
    \ 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977\n  - edge_id:\
    \ mg-products\n    subject: mg\n    predicate: increases\n    object: products\n\
    \    mechanism: Mg supports weaker but detectable cleavage under the same assay\
    \ conditions.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:39188014\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n      snippet: some activity\n\
    \      explanation: Figure5B Mg lane and metal-dependent Results.\n      cache_path:\
    \ evidence/PF01927/busetto-2024-biochemistry.txt\n      cache_sha256: 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977\n\
    - graph_id: cemut7-partner-cleavage-2024\n  title: The full MUT-7/MUT-8 complex\
    \ degrades RNA\n  scope: Busetto2024 Figure5C purified CeMUT-7 FL1-910/MUT-8 FL1-578,\
    \ compared with MUT-7 alone and an\n    inactive composite control.\n  context:\
    \ 0,0.01,0.05,0.2,1uM protein preparations;1uM FAM28-mer,20mM HEPES,50mM KCl,2mM\
    \ MnCl2,30min\n    at room temperature. Ce255/Ce15 affinity tags cleaved.\n  family_mapping:\
    \ CeMUT-7 P34607 sequence v1,910aa,taxon6239; current PF01927 is666-779, inside\
    \ the broader\n    experimental CTD633-910. NTD-EXO1-625 removes additional flanking\
    \ residues. D435,R853,T855 and pk204\n    W812stop are OUTSIDE the matched interval.\
    \ These are whole-protein or broad-CTD assays, not isolated666-779\n    sufficiency.\n\
    \  taxon: NCBITaxon:6239\n  scope_status: MECHANISTIC\n  limitations: MUT-7 alone\
    \ shows similar activity, so no activation edge is assigned to MUT-8. Inactive\n\
    \    control changes both MUT-7 allele and MUT-8 boundary. Figure5/S1 say D435A\
    \ while Results says D453A;\n    reference position453 is I. No isolated-Pfam\
    \ nuclease claim.\n  nodes:\n  - node_id: pair\n    label: Active FL MUT-7/MUT-8\
    \ with Mn and RNA\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:P34607\n\
    \    - UniProtKB:Q19672\n  - node_id: rna\n    label: FAM28-mer RNA substrate\n\
    \    node_type: STATE\n  edges:\n  - edge_id: pair-cleavage\n    subject: pair\n\
    \    predicate: degrades\n    object: rna\n    mechanism: The active purified\
    \ pair generates shorter RNA products; this records activity of the joint\n  \
    \    preparation without asserting that MUT-8 stimulates catalysis.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:39188014\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n\
    \      snippet: degraded\n      explanation: Figure5C active complex dose series\
    \ and matched MUT-7-only comparison.\n      cache_path: evidence/PF01927/busetto-2024-biochemistry.txt\n\
    \      cache_sha256: 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977\n\
    - graph_id: cemut7-kcl-substrates-2024\n  title: MUT-7 cleaves unstructured RNA\
    \ and trims a pUG extension\n  scope: Busetto2024 Figure5E/G CeMUT-7 FL1-910 with\
    \ RNA substrates in KCl; different substrates are separate\n    endpoints.\n \
    \ context: 1uM FAM RNA,20mM HEPES,50mM KCl,2mM MnCl2,30min at room temperature.\
    \ Figure5E0-1uM enzyme;\n    Figure5G positive enzyme concentration not specified.\
    \ GU substrates pre-folded in KCl; no-enzyme controls.\n  family_mapping: CeMUT-7\
    \ P34607 sequence v1,910aa,taxon6239; current PF01927 is666-779, inside the broader\n\
    \    experimental CTD633-910. NTD-EXO1-625 removes additional flanking residues.\
    \ D435,R853,T855 and pk204\n    W812stop are OUTSIDE the matched interval. These\
    \ are whole-protein or broad-CTD assays, not isolated666-779\n    sufficiency.\n\
    \  taxon: NCBITaxon:6239\n  scope_status: MECHANISTIC\n  limitations: GU14 core\
    \ is resistant to efficient degradation in this context. A core-sized gel product\n\
    \    after tail trimming is not sequencing of every product or native small-RNA\
    \ processing. Salt and folding\n    change together versus LiCl; no isolated fold-only\
    \ causal effect is asserted.\n  nodes:\n  - node_id: enzyme\n    label: Active\
    \ FL MUT-7 under KCl conditions\n    node_type: ACTIVITY\n    grounding:\n   \
    \ - UniProtKB:P34607\n  - node_id: generic\n    label: Generic FAM28-mer RNA\n\
    \    node_type: STATE\n  - node_id: gu8\n    label: FAM-GU8 RNA\n    node_type:\
    \ STATE\n  - node_id: tail\n    label: Active MUT-7 with pre-folded GU14 plus\
    \ A10 extension\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:P34607\n\
    \  - node_id: core\n    label: Labelled product migrating near the GU14 core\n\
    \    node_type: STATE\n  edges:\n  - edge_id: generic-cleavage\n    subject: enzyme\n\
    \    predicate: degrades\n    object: generic\n    mechanism: The enzyme degrades\
    \ the generic RNA control in this potassium condition.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:39188014\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n\
    \      snippet: degraded\n      explanation: Figure5E generic28-mer dose series.\n\
    \      cache_path: evidence/PF01927/busetto-2024-biochemistry.txt\n      cache_sha256:\
    \ 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977\n  - edge_id:\
    \ gu8-cleavage\n    subject: enzyme\n    predicate: degrades\n    object: gu8\n\
    \    mechanism: The shorter GU repeat substrate is degraded in the matched potassium\
    \ assay.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:39188014\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n\
    \      snippet: degraded\n      explanation: Figure5E GU8 dose series.\n     \
    \ cache_path: evidence/PF01927/busetto-2024-biochemistry.txt\n      cache_sha256:\
    \ 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977\n  - edge_id:\
    \ tail-trimming\n    subject: tail\n    predicate: produces\n    object: core\n\
    \    mechanism: The extended substrate loses its A-tail and leaves a core-sized\
    \ labelled product under\n      potassium conditions.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:39188014\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n\
    \      snippet: trimmed\n      explanation: Figure5G KCl GU14-A10 plus/minus enzyme\
    \ lanes and corresponding Results.\n      cache_path: evidence/PF01927/busetto-2024-biochemistry.txt\n\
    \      cache_sha256: 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977\n\
    - graph_id: cemut7-licl-substrates-2024\n  title: MUT-7 degrades GU substrates\
    \ in the lithium condition\n  scope: Busetto2024 Figure5F/G CeMUT-7 FL1-910; LiCl\
    \ substrate context kept distinct from KCl.\n  context: 1uM FAM RNA,20mM HEPES,50mM\
    \ LiCl,2mM MnCl2,30min at room temperature. Figure5F0-1uM enzyme;\n    Figure5G\
    \ positive concentration unspecified. GU RNA pre-folded withLiCl; no-enzyme controls.\n\
    \  family_mapping: CeMUT-7 P34607 sequence v1,910aa,taxon6239; current PF01927\
    \ is666-779, inside the broader\n    experimental CTD633-910. NTD-EXO1-625 removes\
    \ additional flanking residues. D435,R853,T855 and pk204\n    W812stop are OUTSIDE\
    \ the matched interval. These are whole-protein or broad-CTD assays, not isolated666-779\n\
    \    sufficiency.\n  taxon: NCBITaxon:6239\n  scope_status: MECHANISTIC\n  limitations:\
    \ LiCl also changes folding and solvent conditions, so these reactions do not\
    \ isolate a structural\n    cause from an ion effect. Native22G production, physiological\
    \ substrates and isolated-CTD activity\n    remain unresolved. Figure5D supports\
    \ different GU14 native-gel mobility, not a complete atomic fold\n    determination.\n\
    \  nodes:\n  - node_id: enzyme\n    label: Active FL MUT-7 under LiCl conditions\n\
    \    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:P34607\n  - node_id:\
    \ generic\n    label: Generic FAM28-mer RNA\n    node_type: STATE\n  - node_id:\
    \ gu8\n    label: FAM-GU8 RNA\n    node_type: STATE\n  - node_id: gu14\n    label:\
    \ FAM-GU14 RNA\n    node_type: STATE\n  - node_id: tail\n    label: FAM-GU14 with\
    \ A10 extension\n    node_type: STATE\n  edges:\n  - edge_id: generic-cleavage\n\
    \    subject: enzyme\n    predicate: degrades\n    object: generic\n    mechanism:\
    \ The generic control RNA is degraded in the lithium assay.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:39188014\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n\
    \      snippet: degraded\n      explanation: Figure5F generic28-mer lanes.\n \
    \     cache_path: evidence/PF01927/busetto-2024-biochemistry.txt\n      cache_sha256:\
    \ 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977\n  - edge_id:\
    \ gu8-cleavage\n    subject: enzyme\n    predicate: degrades\n    object: gu8\n\
    \    mechanism: GU8 is degraded under the matched lithium condition.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:39188014\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n\
    \      snippet: degraded\n      explanation: Figure5F GU8 lanes.\n      cache_path:\
    \ evidence/PF01927/busetto-2024-biochemistry.txt\n      cache_sha256: 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977\n\
    \  - edge_id: gu14-cleavage\n    subject: enzyme\n    predicate: degrades\n  \
    \  object: gu14\n    mechanism: GU14 is degraded in lithium, unlike its potassium-folding\
    \ condition.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:39188014\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n      snippet: degraded\n\
    \      explanation: Figure5F GU14 dose series and Figure5G unextended control.\n\
    \      cache_path: evidence/PF01927/busetto-2024-biochemistry.txt\n      cache_sha256:\
    \ 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977\n  - edge_id:\
    \ extended-cleavage\n    subject: enzyme\n    predicate: degrades\n    object:\
    \ tail\n    mechanism: Both the extension and GU core are susceptible in the lithium\
    \ reaction; the result is not\n      limited to A-tail trimming.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:39188014\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11347159/\n\
    \      snippet: degraded\n      explanation: Figure5G LiCl GU14-A10 plus/minus\
    \ enzyme lanes.\n      cache_path: evidence/PF01927/busetto-2024-biochemistry.txt\n\
    \      cache_sha256: 395a3901d4bf3a7c000148d0377c2020c0018311377accfa3b32c39cd96fb977\n\
    curation_events:\n- timestamp: '2026-10-12T02:28:34Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate PF01927 MUT-7 and EXD3 binding,\
    \ cleavage, assembly and cellular contexts.\n  history_record: history/records/PF01927/2026-10-12T022834Z-codex-012b27.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-12T02:41:32Z'\n\
    \  curator: Codex\n  action: EDIT\n  outcome: changed\n  summary: Verify the PF01927\
    \ imaging reagent catalog discrepancy.\n  history_record: history/records/PF01927/2026-10-12T024132Z-codex-9f0324.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-12T02:42:23Z'\n\
    \  curator: Codex\n  action: REVIEW\n  outcome: needs_followup\n  summary: Retain\
    \ partial PF01927 causal evidence self-review.\n  history_record: history/records/PF01927/2026-10-12T024223Z-codex-0ae9df.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-23T07:48:09Z'\n\
    \  curator: Antigravity\n  action: EDIT\n  outcome: changed\n  summary: Ground\
    \ purified CeMUT-7/MUT-8/MUT-16 complex state nodes in PF01927 causal graphs\n\
    \  history_record: history/records/PF01927/2026-10-23T074809Z-antigravity-192703.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-25T11:15:00Z'\n\
    \  curator: Antigravity\n  action: EDIT\n  outcome: changed\n  summary: Ground\
    \ PF01927 causal-graph protein/gene/complex nodes with UniProtKB:P34607, UniProtKB:Q8N9H8\n\
    \  history_record: history/records/PF01927/2026-10-25T111500Z-antigravity-0d6fee.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Frozen PF01927 Mut7-C/IPR002782/EX_DUF and formerDUF82 are preserved. CeMUT-7
    P34607v1 is910aa with current Pfam666-779; HsEXD3 Q8N9H8v3 is876aa with match631-734.
    Broad CTDs633-910 and624-876 exceed those matches. CeD435,R853,T855,W812stop andHsD399
    are OUTSIDE Pfam. Reference CeI453 supports retaining the paper's D435A/D453A
    discrepancy. Partner MUT-16 uses O62011 longer-isoform numbering. Protein, construct
    and isolated-domain effects are not conflated.
  target_ids:
  - PF01927
  evidence_ids:
  - identity
  - primary
  - complex-cellular
  - manufacturer
  - coverage
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Complex formation, composite MUT-16 capture and crowded-mixture droplets
    are separate physical contexts, not isolated-component sufficiency or direct MUT-7/MUT-16
    contact. Two coprecipitation changes retain unresolved directness because folding
    and MUT-8 solubility may affect recovery. Untagged RNAi hatch phenotypes and tagged
    HA localization use distinct strains and remain indirect. No all-foci dissolution
    or exclusive localization-to-RNAi chain is asserted. FP and cleavage comparisons
    retain broad-CTD scope, tags, salt conditions and extra-domain alleles. Figure7A33.4uM
    conflicts with Results18.7/S8C18.69; no exact fold is adopted. Figure5D435A/D453A
    and the imaging reagent mismatch remain explicit. Salt/fold changes are joint
    contexts; no MUT-8 activation or observed native22G trimming mechanism is inferred.
  target_ids:
  - PF01927
  evidence_ids:
  - primary
  - native
  - complex-cellular
  - manufacturer
  - coverage
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: The 2024 study and inspected supplement do not characterize all5065 frozen
    proteins. Original1999/2005 genetics,2021 neuronal contexts,2025 MUT-16/MUT-8
    study,plantWEX and prokaryotic members need full primary-assay review. Thermococcus
    RNA binding is predicted and Nibbler lacks the CTD; neither is an observed Pfam
    edge. Exact per-panel full-length clone/tag assignments, binding-fit and allele-numbering
    discrepancies, actual imaging reagent, native substrate identity and isolated-Pfam
    sufficiency remain open.
  target_ids:
  - PF01927
  evidence_ids:
  - primary
- assessment_id: cycle3-partner-grounding-verification
  area: representation
  topic: Cycle 3 causal-graph and protein-node grounding verification
  outcome: supported
  summary: 'Cycle 3 Stage 3 (PR #357) grounded the MUT-7 mitotic germline localization
    node focal and RNA-binding FP state node binding to C. elegans MUT-7 (UniProtKB:P34607),
    and the EXD3 RNA-binding FP state node binding to H. sapiens EXD3 (UniProtKB:Q8N9H8).
    Stage 4 frozen-inventory review verified all causal graphs and grounded nodes
    against primary evidence caches.'
  target_ids:
  - PF01927
  evidence_ids:
  - stage4-prior-review
findings:
- finding_id: additional-contexts
  issue_key: pf01927-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve construct and source conflicts and extend native-function/member
    coverage
  description: Resolve the Figure7A/S8C affinity discrepancy, D435A/D453A naming,
    cleavage-panel full-length clone assignment and actual imaging reagent. Review
    the remaining historical, neuronal, plant and prokaryotic primary contexts and
    the published2025 assembly study. Seek member-specific native RNA and isolated-domain
    evidence without transferring predicted contacts or joining different strains
    into an observed molecular pathway. Preserve current conditional negatives and
    IN_PROGRESS status until warranted successor review.
  target_ids:
  - PF01927
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - complex-cellular
  - manufacturer
  - coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01927.yaml
    role: Human-owned scientific overlay
  previous_occurrences:
  - repository: CultureBotAI/DUFMech
    review_id: 20261023T092552Z-pf01927-c2s4-record-review
    finding_id: additional-contexts
actions:
- action_id: extend-contexts
  description: Resolve the Figure7A/S8C affinity discrepancy, D435A/D453A naming,
    cleavage-panel full-length clone assignment and actual imaging reagent. Review
    the remaining historical, neuronal, plant and prokaryotic primary contexts and
    the published2025 assembly study. Seek member-specific native RNA and isolated-domain
    evidence without transferring predicted contacts or joining different strains
    into an observed molecular pathway. Preserve current conditional negatives and
    IN_PROGRESS status until warranted successor review.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01927
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- All original main figures1-7 and rendered supplement S2/S3/S5/S8 and TablesS1/S2/S4
  were inspected during curation; crystallographic statistics were read as text. The
  manufacturer A11029 certificate was inspected for catalog identity only. No raw-data
  reanalysis, exact plasmid resequencing, independent expert endorsement or exhaustive
  family source survey. Browser/corpus verification is reported separately after retention.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
