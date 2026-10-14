# PF01944: scoped SpoIIM localization and suppressor effects

- Review: 20261012T071012Z-pf01944-spoiim-scoped-localization-and-suppressor-effects
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-12T07:09:40Z
- Finished UTC: 2026-10-12T07:10:12Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Eight PHENOTYPIC graphs retain ten OBSERVED experimental effects, all with UNRESOLVED molecular directness, five evidence ledgers and two OPEN discussions. Same-agent scientific review is partial; native status remains IN_PROGRESS. No direct SpoIIM hydrolase activity, binding interface, universal family function or complete source coverage is claimed.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Ascending uncurated family after PF01941; all 8296 records and earlier follow-ups remain in scope.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01944 | data/families/PF01944.yaml | generated | PF01944 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01944 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: concern. Targets: PF01944.

Frozen SpoIIM/former DUF95, IPR002798, EX_DUF, UNSCORED and all imported fields remain unchanged. Reference P37873 v1 maps PF01944 25-203 and verifies I92, while position 82 is K. The reference organism is strain 168; tested constructs are PY79 derivatives and are not independently resequenced. The repeated I92T designation is retained with the I82T caption discrepancy. CD1221 maps by locus to Q18B81, but a current Pfam assignment/domain coordinates were not returned, so candidate C. difficile effects are not asserted as mapped PF01944 edges. Archaeal members are not assigned sporulation functions.

### Directed effects and limits

graph: supported. Targets: PF01944.

Reporter targeting, full-length reporter abundance and heat-resistant spore production remain separate measured outcomes. PspoIID and native-promoter constructs are not merged. Initial septal localization differs from leading-edge positioning. GFP fusion synergy with spoIIB limits native transfer; persistent general P membrane association prevents a membrane-insertion claim. I92T suppression is conditional on GFP-P S108G, not a general WT gain, and localization/rescue are not joined as a proven mediator chain. Partner D/P chemistry and physical-association leads are not M catalysis. Chastanet primary Results, captions and Methods support retained effects, with uninspected figure images disclosed.

### Remaining family coverage

completeness: concern. Targets: PF01944.

Chastanet figures, supplementary strain/suppressor tables and exact historical clones remain open. Early engulfment experiments, later secondary targeting and SpoIIQ immobilization, other suppressor alleles, LcyD full Methods/member mapping, candidate Q18B81 profile mapping and archaeal proteins need further investigation. C. difficile studies used distinct assay conditions; no significant liquid-culture effect versus a modest plate-culture deficit is not collapsed into one universal mechanism. Three reviewed UniProt hits are not a family census.

## Findings

### additional-contexts: Resolve source and construct discrepancies and extend member coverage

minor / open / confirmed; issue key: pf01944-causal-context-coverage.

Inspect Chastanet Figures 1-3/7 and Tables S3/S4, resolve I92T/I82T and Abs292/Abs216 labels, independently verify historical PY79 constructs and Aung's Figure 3D strain. Resolve Q18B81 family membership before assigning candidate C. difficile effects to PF01944; retain culture-specific outcomes. Obtain LcyD Methods, accessions and controls; assess archaeal and remaining bacterial members and separate joint perturbations. Append successor evidence-backed reviews without promoting this partial pass to REVIEWED.

## Recommended Actions And Acceptance Checks

### extend-contexts

Inspect Chastanet Figures 1-3/7 and Tables S3/S4, resolve I92T/I82T and Abs292/Abs216 labels, independently verify historical PY79 constructs and Aung's Figure 3D strain. Resolve Q18B81 family membership before assigning candidate C. difficile effects to PF01944; retain culture-specific outcomes. Obtain LcyD Methods, accessions and controls; assess archaeal and remaining bacterial members and separate joint perturbations. Append successor evidence-backed reviews without promoting this partial pass to REVIEWED.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC2885130/; Results on localization and fusion rescue, Table 1, GFP Methods and visually inspected Figure 3. | supports | Matched reporter comparisons support four directed localization effects, with explicit partially functional GFP constructs, partner perturbations and a Figure 3D strain-label discrepancy. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/P37873/; Accession and domain locations; paired UniProt identity facts | supports | Frozen SpoIIM/former DUF95, IPR002798, EX_DUF, UNSCORED and all imported fields remain unchanged. Reference P37873 v1 maps PF01944 25-203 and verifies I92, while position 82 is K. The reference organism is strain 168; tested constructs are PY79 derivatives and are not independently resequenced. The repeated I92T designation is retained with the I82T caption discrepancy. CD1221 maps by locus to Q18B81, but a current Pfam assignment/domain coordinates were not returned, so candidate C. difficile effects are not asserted as mapped PF01944 edges. Archaeal members are not assigned sporulation functions. |
| native-promoter-suppressor | https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2007.05652.x; Results, Figure 1-3/7 captions, strain construction, suppressor and microscopy/immunoblot Methods. | supports | Six reported effects retain construct, allele-specificity, membrane-association and source-discrepancy limits; images and supplementary tables remain uninspected. |
| candidate-cdiff-ribis | https://pmc.ncbi.nlm.nih.gov/articles/PMC6311989/; Figure 1B locus identity, Figure 2 visual inspection and growth/sporulation/heat-resistance Methods. | supports | Candidate CD1221 deletion has a modest plate-culture heat-resistance deficit, not failed spore formation; current Pfam mapping is unresolved and no native graph edge is added. |
| candidate-cdiff-dembek | https://pmc.ncbi.nlm.nih.gov/articles/PMC6221140/; Primary XML Results, Figures 2-4 captions and selected Methods. | supports | Nonsignificant M-mutant effects under distinct liquid-culture and microscopy conditions constrain generalization; no invented no_effect predicate is used. |
| source-coverage | evidence/PF01944/coverage.txt; Scoped source search, accession mapping and local prior-art search. | supports | Source access failures, unreviewed downloaded papers, candidate mapping and unresolved family branches remain explicit follow-ups. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01944 | data/families/PF01944.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Aung Figure 3 and Ribis Figure 2 were visually inspected. Chastanet full primary text/Methods/captions and selected Dembek XML sections were read, but their figure images and supplement tables were unavailable to this pass. Wiley downloads returned HTTP403; one supplementary endpoint returned HTML, another an XML error and another timed out. Mu 2014 was inspected only as a primary abstract. No raw-data replication or independent expert review.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T071012Z-pf01944-spoiim-scoped-localization-and-suppressor-effects
title: 'PF01944: scoped SpoIIM localization and suppressor effects'
started_at: '2026-10-12T07:09:40Z'
finished_at: '2026-10-12T07:10:12Z'
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
summary: Eight PHENOTYPIC graphs retain ten OBSERVED experimental effects, all with
  UNRESOLVED molecular directness, five evidence ledgers and two OPEN discussions.
  Same-agent scientific review is partial; native status remains IN_PROGRESS. No direct
  SpoIIM hydrolase activity, binding interface, universal family function or complete
  source coverage is claimed.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01944.yaml
    sha256: 4b2a80d8d62544606435a3a01667a69487402e1736dc67b64b8c9304bfc94506
    role: context
  - path: data/families/PF01944.yaml
    sha256: b13d4d832e64d621ddbfd0d410c6441af9f15157012df7758da26cbb436e95e7
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
  - path: evidence/PF01944/aung-2007.txt
    role: context
    sha256: a4a0040e203e0c83775cd032a43f8d982b2fa970fa5a9ca6eea4fb13244efbe8
  - path: evidence/PF01944/identity.txt
    role: context
    sha256: 105d6ff3389aca25155ada5603ff6b0c7c6429f4ab94eadb95c5c50127a648c4
  - path: evidence/PF01944/chastanet-2007.txt
    role: context
    sha256: debcb337b0a39753df705855fe00841519942be60040aa9736a4e6e841b7db80
  - path: evidence/PF01944/candidate-contexts.txt
    role: context
    sha256: b12d2e5916676264d3f3a160ef029bf60306bc7ca847f2758ef9fd1ddb88d20c
  - path: evidence/PF01944/coverage.txt
    role: context
    sha256: 49695b968efe080692370707eaf38950ccaddd86dd2d495d99fe12e89516913a
targets:
- target_id: PF01944
  path: data/families/PF01944.yaml
  label: PF01944
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01944.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 37d4fb0a0ef816380b811698df31f1d623fc175549eb7a60ccf99d073bb1b2da
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Ascending uncurated family after PF01941; all 8296 records and earlier
    follow-ups remain in scope.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01944
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Chastanet figures, supplementary strain/suppressor tables and exact historical
      clones remain open. Early engulfment experiments, later secondary targeting
      and SpoIIQ immobilization, other suppressor alleles, LcyD full Methods/member
      mapping, candidate Q18B81 profile mapping and archaeal proteins need further
      investigation. C. difficile studies used distinct assay conditions; no significant
      liquid-culture effect versus a modest plate-culture deficit is not collapsed
      into one universal mechanism. Three reviewed UniProt hits are not a family census.
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
  - PF01944
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2885130/
  locator: Results on localization and fusion rescue, Table 1, GFP Methods and visually
    inspected Figure 3.
  accessed_at: '2026-10-12T07:10:12Z'
  support: supports
  snapshot_sha256: a4a0040e203e0c83775cd032a43f8d982b2fa970fa5a9ca6eea4fb13244efbe8
  summary: Matched reporter comparisons support four directed localization effects,
    with explicit partially functional GFP constructs, partner perturbations and a
    Figure 3D strain-label discrepancy.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/P37873/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-12T07:10:12Z'
  support: supports
  snapshot_sha256: 105d6ff3389aca25155ada5603ff6b0c7c6429f4ab94eadb95c5c50127a648c4
  summary: Frozen SpoIIM/former DUF95, IPR002798, EX_DUF, UNSCORED and all imported
    fields remain unchanged. Reference P37873 v1 maps PF01944 25-203 and verifies
    I92, while position 82 is K. The reference organism is strain 168; tested constructs
    are PY79 derivatives and are not independently resequenced. The repeated I92T
    designation is retained with the I82T caption discrepancy. CD1221 maps by locus
    to Q18B81, but a current Pfam assignment/domain coordinates were not returned,
    so candidate C. difficile effects are not asserted as mapped PF01944 edges. Archaeal
    members are not assigned sporulation functions.
- evidence_id: native-promoter-suppressor
  kind: primary_source
  reference: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2007.05652.x
  locator: Results, Figure 1-3/7 captions, strain construction, suppressor and microscopy/immunoblot
    Methods.
  summary: Six reported effects retain construct, allele-specificity, membrane-association
    and source-discrepancy limits; images and supplementary tables remain uninspected.
  accessed_at: '2026-10-12T07:10:12Z'
  support: supports
  snapshot_sha256: debcb337b0a39753df705855fe00841519942be60040aa9736a4e6e841b7db80
- evidence_id: candidate-cdiff-ribis
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6311989/
  locator: Figure 1B locus identity, Figure 2 visual inspection and growth/sporulation/heat-resistance
    Methods.
  summary: Candidate CD1221 deletion has a modest plate-culture heat-resistance deficit,
    not failed spore formation; current Pfam mapping is unresolved and no native graph
    edge is added.
  accessed_at: '2026-10-12T07:10:12Z'
  support: supports
  snapshot_sha256: b12d2e5916676264d3f3a160ef029bf60306bc7ca847f2758ef9fd1ddb88d20c
- evidence_id: candidate-cdiff-dembek
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6221140/
  locator: Primary XML Results, Figures 2-4 captions and selected Methods.
  summary: Nonsignificant M-mutant effects under distinct liquid-culture and microscopy
    conditions constrain generalization; no invented no_effect predicate is used.
  accessed_at: '2026-10-12T07:10:12Z'
  support: supports
  snapshot_sha256: b12d2e5916676264d3f3a160ef029bf60306bc7ca847f2758ef9fd1ddb88d20c
- evidence_id: source-coverage
  kind: search
  reference: evidence/PF01944/coverage.txt
  locator: Scoped source search, accession mapping and local prior-art search.
  search_scope: PF01944, DUF95, SpoIIM, CD1221/CD630_12210 and LcyD; ignored/hidden
    local text included in curation/evidence/history/structured reviews, excluding
    JSON.
  summary: Source access failures, unreviewed downloaded papers, candidate mapping
    and unresolved family branches remain explicit follow-ups.
  accessed_at: '2026-10-12T07:10:12Z'
  support: supports
  snapshot_sha256: 49695b968efe080692370707eaf38950ccaddd86dd2d495d99fe12e89516913a
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-12T07:10:12Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01944
  kind: record_content
  reference: data/families/PF01944.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-12T07:10:12Z'
  support: context_only
  snapshot_sha256: b13d4d832e64d621ddbfd0d410c6441af9f15157012df7758da26cbb436e95e7
  quote: "id: Pfam:PF01944\npfam_id: PF01944\nname: Stage II sporulation protein M\n\
    short_name: SpoIIM\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01944\n\
    counters:\n  proteins: 8861\n  matches: 8865\n  proteomes: 7738\n  taxa: 10914\n\
    \  structures: 0\n  alphafold_models: 5639\n  domain_architectures: 14\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002798\ndescription: SpoIIM is on e of four stage II\
    \ sporulation proteins that is necessary for the forespore\n  inside the mother-cell\
    \ to be properly internalised through the breakdown of peptidoglycans trapped\
    \ between\n  the membranes of the septum separating the forespore and the mother-cell.\
    \ The four proteins working\n  in sequence are SpoIIB, [pfam:PF05036], SpoIIM,\
    \ SpoIIP, [pfam:PF07454], and finally SpoIID, [pfam:PF08486].\n  D, M and P are\
    \ in a complex with each other and the complex assembles in a hierarchical manner\
    \ such\n  that M, which serves as a membrane anchor, recruits P to the septum\
    \ and P, in turn, recruits D to the\n  septum [[cite:PUB00109154]].\ncuration_history:\
    \ history/records/PF01944\ndiscussions:\n- discussion_id: pf01944-construct-and-mechanism-limits\n\
    \  prompt: Resolve construct discrepancies and physical mechanisms behind SpoIIM\
    \ localization and suppression\n    phenotypes.\n  kind: CURATION_TODO\n  status:\
    \ OPEN\n  rationale: GFP targeting and allele-specific suppression do not establish\
    \ direct molecular contact or\n    SpoIIM hydrolase activity.\n  evidence:\n \
    \ - reference: PMID:17376078\n    supports: PARTIAL\n    evidence_source: primary_publication\n\
    \    explanation: I92T suppression is supported by Results and captions, but Figure\
    \ 3C says I82T and images/supplement\n      tables remain uninspected.\n  posed_by:\
    \ Codex\n  posed_date: '2026-10-12'\n  notes: Preserve Aung Figure 3D KP722/KP764\
    \ and Chastanet Abs292/Abs216 discrepancies. Reference P37873\n    is strain 168;\
    \ experiments use PY79 derivatives. See evidence/PF01944/identity.txt and coverage.txt.\n\
    - discussion_id: pf01944-member-and-source-coverage\n  prompt: Resolve candidate\
    \ homolog mapping and extend evidence coverage beyond the inspected Bacillus\n\
    \    contexts.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: Archaeal members\
    \ and bacteriocin-associated proteins are not characterized by the sporulation\n\
    \    name; C. difficile CD1221 lacks a verified current Pfam mapping here.\n \
    \ evidence:\n  - reference: PMID:30066347\n    supports: PARTIAL\n    evidence_source:\
    \ primary_publication\n    explanation: A modest plate-culture heat-resistance\
    \ decrease differs from the nonsignificant result\n      under Dembek's liquid-culture\
    \ conditions; neither establishes universal SpoIIM necessity.\n  - reference:\
    \ PMID:23906710\n    supports: PARTIAL\n    evidence_source: primary_publication\n\
    \    explanation: LcyD abstract reports export/immunity observations, but full\
    \ Methods and member mapping\n      remain open; mature peptide in knockout cells\
    \ does not demonstrate LcyD cyclase activity.\n  posed_by: Codex\n  posed_date:\
    \ '2026-10-12'\n  notes: Inspect remaining primary sources and exact constructs;\
    \ do not convert joint DMP/AH perturbations\n    to isolated SpoIIM effects. All\
    \ corpus records and prior follow-ups remain in scope.\ncausal_graphs:\n- graph_id:\
    \ bsub-spoiim-loss-gfp-spoiip-2007\n  title: SpoIIM disruption reduces GFP-SpoIIP\
    \ septal targeting\n  scope: Aung 2007 Figure 3E/H, KP722 versus KP776.\n  context:\
    \ B. subtilis PY79 derivatives, PspoIID-gfp-spoIIP at amyE with spoIIP::tet; resuspension\
    \ sporulation\n    at 37 C, t1.75 h, FM4-64 microscopy.\n  family_mapping: SpoIIM\
    \ reference P37873 v1, BSU23530, 214 aa, PF01944 25-203. Tested PY79 spoIIM::Tn917\n\
    \    is a whole-protein perturbation; historical clone sequence is not independently\
    \ verified.\n  taxon: NCBITaxon:1423\n  scope_status: PHENOTYPIC\n  limitations:\
    \ Reporter targeting is not direct binding or isolated-domain activity. GFP fusions\
    \ are partly\n    functional; stability and developmental arrest can affect fluorescence.\n\
    \  nodes:\n  - node_id: loss-m\n    label: spoIIM::Tn917 in GFP-SpoIIP reporter\
    \ cells\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:P37873\n\
    \  - node_id: septal-p\n    label: Septal targeting of GFP-SpoIIP\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: m-loss-p-targeting\n    subject: loss-m\n    predicate:\
    \ decreases\n    object: septal-p\n    mechanism: Loss of SpoIIM shifts the reporter\
    \ from septal foci toward a largely dispersed distribution\n      under the matched\
    \ imaging conditions.\n    directness: UNRESOLVED\n    support: OBSERVED\n   \
    \ evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:17824930\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2885130/\n      snippet:\
    \ Fig. 3.\n      explanation: Panels E/H visually inspected; Table 1 and GFP microscopy\
    \ Methods establish the genotype\n        and t1.75-h comparison.\n      cache_path:\
    \ evidence/PF01944/aung-2007.txt\n      cache_sha256: a4a0040e203e0c83775cd032a43f8d982b2fa970fa5a9ca6eea4fb13244efbe8\n\
    - graph_id: bsub-spoiib-loss-gfp-spoiim-2007\n  title: SpoIIB disruption reduces\
    \ GFP-SpoIIM septal targeting\n  scope: Aung 2007 Figure 3A/B, KP721 versus KP762.\n\
    \  context: PY79 derivatives, PspoIID-gfp-spoIIM at amyE with spoIIM::Tn917; 37\
    \ C resuspension sporulation,\n    t1.75 h.\n  family_mapping: Reporter contains\
    \ the B. subtilis SpoIIM protein; reference P37873 v1 PF01944 25-203.\n    SpoIIB\
    \ is the perturbed partner, not a PF01944 protein.\n  taxon: NCBITaxon:1423\n\
    \  scope_status: PHENOTYPIC\n  limitations: The spoIIB-plus-GFP construct has\
    \ a synergistic engulfment defect. This is not proof that\n    native SpoIIB is\
    \ universally essential or binds SpoIIM directly.\n  nodes:\n  - node_id: loss-b\n\
    \    label: spoIIB::erm in GFP-SpoIIM reporter cells\n    node_type: PERTURBATION\n\
    \  - node_id: septal-m\n    label: Septal targeting of GFP-SpoIIM\n    node_type:\
    \ STATE\n    grounding:\n    - UniProtKB:P37873\n  edges:\n  - edge_id: b-loss-m-targeting\n\
    \    subject: loss-b\n    predicate: decreases\n    object: septal-m\n    mechanism:\
    \ The partner mutation reduces septal enrichment and leaves GFP-SpoIIM distributed\
    \ around\n      the mother-cell membrane.\n    directness: UNRESOLVED\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:17824930\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2885130/\n      snippet:\
    \ Fig. 3.\n      explanation: Panels A/B visually inspected with Table 1; fusion-dependent\
    \ engulfment failure is\n        explicitly retained.\n      cache_path: evidence/PF01944/aung-2007.txt\n\
    \      cache_sha256: a4a0040e203e0c83775cd032a43f8d982b2fa970fa5a9ca6eea4fb13244efbe8\n\
    - graph_id: bsub-partner-mutants-spoiim-position-2007\n  title: Two partner mutants\
    \ restrict GFP-SpoIIM to the septal midpoint\n  scope: Separate Aung 2007 Figure\
    \ 3C and 3D comparisons with Figure 3A.\n  context: PY79 PspoIID-gfp-spoIIM reporter\
    \ replacing native M function; spoIID298 or spoIIP::tet backgrounds;\n    37 C,\
    \ t1.75 h resuspension sporulation.\n  family_mapping: SpoIIM reference P37873\
    \ v1, PF01944 25-203. The D and P perturbations affect localization\n    of the\
    \ M-containing reporter, not M sequence.\n  taxon: NCBITaxon:1423\n  scope_status:\
    \ PHENOTYPIC\n  limitations: Initial septal targeting persists; this is not loss\
    \ of all M localization. Developmental\n    arrest prevents attribution to a direct\
    \ transport step. Figure 3D says KP722 but Table 1 assigns this\n    genotype\
    \ to KP764; the genotype is retained without silently repairing the caption.\n\
    \  nodes:\n  - node_id: d-mutant\n    label: spoIID298 with GFP-SpoIIM\n    node_type:\
    \ PERTURBATION\n  - node_id: p-mutant\n    label: spoIIP::tet with GFP-SpoIIM\n\
    \    node_type: PERTURBATION\n  - node_id: leading-m\n    label: GFP-SpoIIM positioning\
    \ at advancing membrane edges\n    node_type: STATE\n    grounding:\n    - UniProtKB:P37873\n\
    \  edges:\n  - edge_id: d-mutant-m-position\n    subject: d-mutant\n    predicate:\
    \ decreases\n    object: leading-m\n    mechanism: The spoIID298 reporter remains\
    \ concentrated at the septal midpoint rather than progressing\n      to the leading-edge\
    \ pattern.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:17824930\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC2885130/\n      snippet: Fig. 3.\n\
    \      explanation: Panel C versus A visually inspected; Table 1 identifies KP763.\
    \ No direct molecular\n        migration mechanism is resolved.\n      cache_path:\
    \ evidence/PF01944/aung-2007.txt\n      cache_sha256: a4a0040e203e0c83775cd032a43f8d982b2fa970fa5a9ca6eea4fb13244efbe8\n\
    \  - edge_id: p-mutant-m-position\n    subject: p-mutant\n    predicate: decreases\n\
    \    object: leading-m\n    mechanism: The spoIIP-disrupted reporter likewise\
    \ remains at the septal midpoint in the displayed\n      comparison.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:17824930\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2885130/\n\
    \      snippet: Fig. 3.\n      explanation: Panel D versus A visually inspected.\
    \ Caption/Table 1 strain-label discrepancy remains\n        open; the effect is\
    \ genotype-scoped.\n      cache_path: evidence/PF01944/aung-2007.txt\n      cache_sha256:\
    \ a4a0040e203e0c83775cd032a43f8d982b2fa970fa5a9ca6eea4fb13244efbe8\n- graph_id:\
    \ bsub-native-promoter-spoiim-loss-2007\n  title: SpoIIM loss reduces native-promoter\
    \ partner targeting\n  scope: Chastanet 2007 Figure 1B, two distinct GFP fusion\
    \ backgrounds.\n  context: PY79 derivatives expressing native-promoter GFP-P or\
    \ GFP-D at their normal loci. Microscopy\n    Methods specify resuspension sporulation,\
    \ 130 min and 37 C growth.\n  family_mapping: Native SpoIIM disruption in PY79;\
    \ reference P37873 v1, PF01944 25-203. No isolated PF01944\n    fragment or independently\
    \ verified historical sequence.\n  taxon: NCBITaxon:1423\n  scope_status: PHENOTYPIC\n\
    \  limitations: Whole-protein requirement for septal enrichment does not establish\
    \ direct M-P or M-D contact.\n    General P membrane association persists. Figure\
    \ images/supplement not inspected; support is inspected\n    primary Results,\
    \ captions and Methods.\n  nodes:\n  - node_id: m-loss-p\n    label: SpoIIM loss\
    \ in native-promoter GFP-P cells\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:P37873\n  - node_id: m-loss-d\n    label: SpoIIM loss in native-promoter\
    \ GFP-D cells\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:P37873\n\
    \  - node_id: septal-p\n    label: Native-promoter GFP-P septal enrichment\n \
    \   node_type: STATE\n  - node_id: septal-d\n    label: Native-promoter GFP-D\
    \ septal enrichment\n    node_type: STATE\n  edges:\n  - edge_id: native-p-targeting\n\
    \    subject: m-loss-p\n    predicate: decreases\n    object: septal-p\n    mechanism:\
    \ M disruption reduces specific septal targeting of GFP-P, while fractionation\
    \ does not show\n      loss of its general membrane association.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:17376078\n      source_url: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2007.05652.x\n\
    \      snippet: Fluorescence microscopy\n      explanation: Figure 1B Results/caption,\
    \ Abs57 versus Abs49, and Figure 2 membrane-fractionation\n        interpretation;\
    \ figure image not inspected.\n      cache_path: evidence/PF01944/chastanet-2007.txt\n\
    \      cache_sha256: debcb337b0a39753df705855fe00841519942be60040aa9736a4e6e841b7db80\n\
    \  - edge_id: native-d-targeting\n    subject: m-loss-d\n    predicate: decreases\n\
    \    object: septal-d\n    mechanism: M disruption also reduces GFP-D septal targeting\
    \ in its own reporter background; mediation\n      through P remains possible.\n\
    \    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:17376078\n      source_url: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2007.05652.x\n\
    \      snippet: Fluorescence microscopy\n      explanation: Figure 1B Results/caption,\
    \ Abs343 versus Abs325; not a transitive inference from the\n        GFP-P contrast.\n\
    \      cache_path: evidence/PF01944/chastanet-2007.txt\n      cache_sha256: debcb337b0a39753df705855fe00841519942be60040aa9736a4e6e841b7db80\n\
    - graph_id: bsub-spoiim-loss-gfp-p-abundance-2007\n  title: SpoIIM loss reduces\
    \ full-length GFP-SpoIIP abundance\n  scope: Chastanet 2007 Figure 2A immunoblot\
    \ comparison.\n  context: PY79 native-promoter GFP-P cells, Abs57 versus Abs49;\
    \ equal amounts of total protein at 130\n    min of sporulation in SM medium.\n\
    \  family_mapping: M disruption, B. subtilis SpoIIM reference P37873 v1 PF01944\
    \ 25-203; the measured band\n    is the partner fusion, not an M activity product.\n\
    \  taxon: NCBITaxon:1423\n  scope_status: PHENOTYPIC\n  limitations: Turnover\
    \ rate and responsible protease are not measured. Protein abundance and localization\n\
    \    are not joined as an experimentally established chain. Figure image unavailable\
    \ to this pass.\n  nodes:\n  - node_id: loss-m\n    label: SpoIIM loss in GFP-SpoIIP\
    \ cells\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:P37873\n\
    \  - node_id: full-p\n    label: Full-length GFP-SpoIIP immunoblot abundance\n\
    \    node_type: STATE\n  edges:\n  - edge_id: m-loss-full-p\n    subject: loss-m\n\
    \    predicate: decreases\n    object: full-p\n    mechanism: The primary text\
    \ reports less full-length GFP-P together with an approximately GFP-sized\n  \
    \    fragment in the M-mutant comparison.\n    directness: UNRESOLVED\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:17376078\n\
    \      source_url: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2007.05652.x\n\
    \      snippet: Immunoblot analysis\n      explanation: Figure 2A Results/caption\
    \ and immunoblot Methods; this is a reported abundance observation,\n        not\
    \ a directly measured degradation rate.\n      cache_path: evidence/PF01944/chastanet-2007.txt\n\
    \      cache_sha256: debcb337b0a39753df705855fe00841519942be60040aa9736a4e6e841b7db80\n\
    - graph_id: bsub-i92t-s108g-localization-suppression-2007\n  title: SpoIIM I92T\
    \ suppresses a GFP-SpoIIP localization defect\n  scope: Chastanet 2007 suppressor\
    \ Results and Figure 3C context.\n  context: PY79, amyE native-P-promoter GFP-SpoIIP\
    \ S108G replacing native P, native M disrupted and gltA\n    expressing WT M or\
    \ I92T M; resuspension microscopy, 130 min.\n  family_mapping: P37873 v1 has I92\
    \ inside PF01944 25-203; K82 is not I. The repeatedly stated I92T allele\n   \
    \ is used while retaining the Figure 3C I82T caption conflict.\n  taxon: NCBITaxon:1423\n\
    \  scope_status: PHENOTYPIC\n  limitations: Genotype-specific suppression is not\
    \ direct M-P binding or a resolved interface. Figure/supplement\n    images were\
    \ not inspected and historical clones were not resequenced. Seventeen representative\
    \ cells\n    are not independent biological replicates.\n  nodes:\n  - node_id:\
    \ suppressor\n    label: I92T instead of WT SpoIIM in GFP-P S108G cells\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:P37873\n  - node_id: septal-p\n\
    \    label: Septal GFP-P S108G enrichment relative to reference\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: i92t-localization-rescue\n    subject: suppressor\n\
    \    predicate: increases\n    object: septal-p\n    mechanism: The suppressor\
    \ comparison raises the reported relative septal enrichment from about 26%\n \
    \     to 78% under the stated reporter assay.\n    directness: UNRESOLVED\n  \
    \  support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:17376078\n      source_url: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2007.05652.x\n\
    \      snippet: Fluorescence microscopy\n      explanation: Suppressor Results\
    \ and Methods quantify background-corrected septal enrichment over\n        17\
    \ representative cells; the I82T caption conflict remains explicit.\n      cache_path:\
    \ evidence/PF01944/chastanet-2007.txt\n      cache_sha256: debcb337b0a39753df705855fe00841519942be60040aa9736a4e6e841b7db80\n\
    - graph_id: bsub-i92t-s108g-sporulation-suppression-2007\n  title: SpoIIM I92T\
    \ improves sporulation in the GFP-SpoIIP S108G background\n  scope: Chastanet\
    \ 2007 Figure 3B and suppressor Results.\n  context: PY79 GFP-P S108G background,\
    \ native M disrupted and gltA expressing WT M or I92T M; liquid-culture\n    sporulation\
    \ scored by survival of 80 C for 20 min.\n  family_mapping: Reference P37873 v1,\
    \ I92 within PF01944 25-203; whole-protein allele substitution in\n    a specific\
    \ defective-partner background.\n  taxon: NCBITaxon:1423\n  scope_status: PHENOTYPIC\n\
    \  limitations: Not a general sporulation gain in WT cells. The allele does not\
    \ rescue all P mutants; image,\n    supplemental genotype table and raw values\
    \ remain to be inspected. Improved targeting and sporulation\n    are separate\
    \ observations, not a proven mediator chain.\n  nodes:\n  - node_id: suppressor\n\
    \    label: I92T instead of WT SpoIIM in GFP-P S108G cells\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:P37873\n  - node_id: spores\n    label: Heat-resistant\
    \ spore production in the suppressor assay\n    node_type: PHENOTYPE\n  edges:\n\
    \  - edge_id: i92t-sporulation-rescue\n    subject: suppressor\n    predicate:\
    \ increases\n    object: spores\n    mechanism: I92T improves heat-resistant spore\
    \ production toward the reference level in the defective\n      GFP-P S108G background.\n\
    \    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:17376078\n      source_url: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2007.05652.x\n\
    \      snippet: Fluorescence microscopy\n      explanation: Distinct heat-resistance\
    \ readout from Figure 3B and suppressor Results; strains/media\n        Methods\
    \ specify 80 C/20 min. No exact rescue ratio is invented.\n      cache_path: evidence/PF01944/chastanet-2007.txt\n\
    \      cache_sha256: debcb337b0a39753df705855fe00841519942be60040aa9736a4e6e841b7db80\n\
    - graph_id: bsub-native-promoter-spoiib-loss-2007\n  title: SpoIIB loss reduces\
    \ native-promoter GFP-SpoIIM targeting\n  scope: Chastanet 2007 Figure 7, native-promoter\
    \ M fusion background.\n  context: PY79, GFP-SpoIIM at the normal M locus, with\
    \ or without spoIIB disruption; Figure 7 specifies\n    2 h after sporulation\
    \ initiation.\n  family_mapping: GFP-SpoIIM contains the protein mapped by P37873\
    \ v1 PF01944 25-203. B is a separate\n    partner, not this family.\n  taxon:\
    \ NCBITaxon:1423\n  scope_status: PHENOTYPIC\n  limitations: This construct differs\
    \ from Aung's PspoIID reporter. Partial fusion functionality in the\n    B-mutant\
    \ background limits transfer. Figure 7 caption Abs292 differs from construction-text\
    \ Abs216;\n    images and Table S3 remain uninspected.\n  nodes:\n  - node_id:\
    \ loss-b\n    label: spoIIB disruption with native-promoter GFP-SpoIIM\n    node_type:\
    \ PERTURBATION\n  - node_id: septal-m\n    label: Native-promoter GFP-SpoIIM septal\
    \ enrichment\n    node_type: STATE\n    grounding:\n    - UniProtKB:P37873\n \
    \ edges:\n  - edge_id: native-b-loss-m-targeting\n    subject: loss-b\n    predicate:\
    \ decreases\n    object: septal-m\n    mechanism: The reported comparison shifts\
    \ M-fusion fluorescence away from the septum toward the peripheral\n      mother-cell\
    \ membrane.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:17376078\n      source_url:\
    \ https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2007.05652.x\n\
    \      snippet: Fluorescence microscopy\n      explanation: Figure 7 Results/caption,\
    \ genotype-scoped because of the strain-label conflict; not\n        an independently\
    \ observed direct B-M interaction.\n      cache_path: evidence/PF01944/chastanet-2007.txt\n\
    \      cache_sha256: debcb337b0a39753df705855fe00841519942be60040aa9736a4e6e841b7db80\n\
    curation_events:\n- timestamp: '2026-10-12T07:00:06Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: needs_followup\n  summary: Curate eight scoped SpoIIM phenotype\
    \ graphs with ten observed effects.\n  history_record: history/records/PF01944/2026-10-12T070006Z-codex-986f23.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: concern
  summary: Frozen SpoIIM/former DUF95, IPR002798, EX_DUF, UNSCORED and all imported
    fields remain unchanged. Reference P37873 v1 maps PF01944 25-203 and verifies
    I92, while position 82 is K. The reference organism is strain 168; tested constructs
    are PY79 derivatives and are not independently resequenced. The repeated I92T
    designation is retained with the I82T caption discrepancy. CD1221 maps by locus
    to Q18B81, but a current Pfam assignment/domain coordinates were not returned,
    so candidate C. difficile effects are not asserted as mapped PF01944 edges. Archaeal
    members are not assigned sporulation functions.
  target_ids:
  - PF01944
  evidence_ids:
  - identity
  - primary
  - native-promoter-suppressor
  - candidate-cdiff-ribis
  - candidate-cdiff-dembek
  - source-coverage
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Reporter targeting, full-length reporter abundance and heat-resistant spore
    production remain separate measured outcomes. PspoIID and native-promoter constructs
    are not merged. Initial septal localization differs from leading-edge positioning.
    GFP fusion synergy with spoIIB limits native transfer; persistent general P membrane
    association prevents a membrane-insertion claim. I92T suppression is conditional
    on GFP-P S108G, not a general WT gain, and localization/rescue are not joined
    as a proven mediator chain. Partner D/P chemistry and physical-association leads
    are not M catalysis. Chastanet primary Results, captions and Methods support retained
    effects, with uninspected figure images disclosed.
  target_ids:
  - PF01944
  evidence_ids:
  - primary
  - native
  - native-promoter-suppressor
  - candidate-cdiff-ribis
  - candidate-cdiff-dembek
  - source-coverage
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Chastanet figures, supplementary strain/suppressor tables and exact historical
    clones remain open. Early engulfment experiments, later secondary targeting and
    SpoIIQ immobilization, other suppressor alleles, LcyD full Methods/member mapping,
    candidate Q18B81 profile mapping and archaeal proteins need further investigation.
    C. difficile studies used distinct assay conditions; no significant liquid-culture
    effect versus a modest plate-culture deficit is not collapsed into one universal
    mechanism. Three reviewed UniProt hits are not a family census.
  target_ids:
  - PF01944
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01944-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve source and construct discrepancies and extend member coverage
  description: Inspect Chastanet Figures 1-3/7 and Tables S3/S4, resolve I92T/I82T
    and Abs292/Abs216 labels, independently verify historical PY79 constructs and
    Aung's Figure 3D strain. Resolve Q18B81 family membership before assigning candidate
    C. difficile effects to PF01944; retain culture-specific outcomes. Obtain LcyD
    Methods, accessions and controls; assess archaeal and remaining bacterial members
    and separate joint perturbations. Append successor evidence-backed reviews without
    promoting this partial pass to REVIEWED.
  target_ids:
  - PF01944
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - native-promoter-suppressor
  - candidate-cdiff-ribis
  - candidate-cdiff-dembek
  - source-coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01944.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Inspect Chastanet Figures 1-3/7 and Tables S3/S4, resolve I92T/I82T
    and Abs292/Abs216 labels, independently verify historical PY79 constructs and
    Aung's Figure 3D strain. Resolve Q18B81 family membership before assigning candidate
    C. difficile effects to PF01944; retain culture-specific outcomes. Obtain LcyD
    Methods, accessions and controls; assess archaeal and remaining bacterial members
    and separate joint perturbations. Append successor evidence-backed reviews without
    promoting this partial pass to REVIEWED.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01944
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Aung Figure 3 and Ribis Figure 2 were visually inspected. Chastanet full primary
  text/Methods/captions and selected Dembek XML sections were read, but their figure
  images and supplement tables were unavailable to this pass. Wiley downloads returned
  HTTP403; one supplementary endpoint returned HTML, another an XML error and another
  timed out. Mu 2014 was inspected only as a primary abstract. No raw-data replication
  or independent expert review.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
