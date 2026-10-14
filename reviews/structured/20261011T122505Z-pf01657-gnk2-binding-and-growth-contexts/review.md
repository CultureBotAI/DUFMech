# PF01657 Gnk2 binding and antifungal assays with residue and dose qualifications

- Review: 20261011T122505Z-pf01657-gnk2-binding-and-growth-contexts
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T12:18:17Z
- Finished UTC: 2026-10-11T12:25:05Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Fourteen observed effects in six graphs distinguish four direct SPR binding responses from ten indirect yeast and Fusarium growth effects. Current domain mapping, extra Met, residual activity and the twofold SPR dose discrepancy are explicit; binding is not joined to an unmeasured cell-death mechanism.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Pending PF01657 within the full 8296-family corpus; mature Ginkgo Gnk2 is a sequence-verified protein example, not a family-wide member census.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01657 | data/families/PF01657.yaml | generated | PF01657 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01657 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01657.

A4ZDL6 version-1 sequence is 134 aa; mature chain 27-134 plus extra Met exactly matches PDB 4XRE entity 1, whose primary citation is PMID25139159. Current PF01657 36-131 maps to mature 10-105 and includes N11/R93/E104 at precursor37/119/130, unlike the historical narrow boundary discussed in the paper. No isolated-domain sufficiency or independently resequenced mutant stock is claimed. Formal supersession of paper accession 3W9Q was not verified.

### Directed effects and limits

graph: supported. Targets: PF01657.

The six graphs separate SPR, parental yeast, glycosylation-background dependence, F. culmorum liquid culture and two species-specific disc assays. All fourteen edges are OBSERVED; four DIRECT biochemical and ten INDIRECT phenotypic. Figure5 labels 0.625-10 mM versus Methods1.25-20 mM, so no independently verified KD is asserted. The delta-mnn2 curve's small residual delay qualifies strong no-effect wording. Residual R93A activity, absent displayed saccharide-only controls, protein active-fraction limits and distinct timing origins prevent stronger mechanistic claims.

### Remaining family coverage

completeness: concern. Targets: PF01657.

Supplementary controls were not visually retrieved, exact SPR doses remain unresolved, and later actin-remodeling work, early purification evidence and other CRK/PDLP members remain incompletely assessed. Static structural contacts, mannobiose docking and growth effects do not establish a universal lectin mechanism, cell-wall damage, spore-germination inhibition or plant protection.

## Findings

### additional-contexts: Resolve Gnk2 assay discrepancies and extend member-specific downstream evidence

minor / open / confirmed; issue key: pf01657-causal-context-coverage.

Retrieve and inspect supplementary S5-S7, resolve the factor-two SPR concentration labels and the 3W9Q/4XRE accession relationship, and review PMID26315821 for separately scoped downstream experiments. Preserve current residue mapping, residual responses, genotype baselines, absent saccharide-only controls and lack of family-wide transfer.

## Recommended Actions And Acceptance Checks

### extend-contexts

Retrieve and inspect supplementary S5-S7, resolve the factor-two SPR concentration labels and the 3W9Q/4XRE accession relationship, and review PMID26315821 for separately scoped downstream experiments. Preserve current residue mapping, residual responses, genotype baselines, absent saccharide-only controls and lack of family-wide transfer.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC4213107/; Miyakawa 2014 full-text Results, Discussion and Methods; Figures 5, 7 and 8 visually inspected. Supplementary CD/DSF/NMR controls are author-reported only because the linked DOC did not yield the supplement. | supports | WT mannobiose SPR responses increase with dose and decrease with N11A/R93A/E104A substitutions. WT Gnk2 delays BY4741 growth, attenuated by R93A or mannan; delta-mnn2 retains a much smaller response. WT reduces F. culmorum liquid OD600 and local growth near discs in two Fusarium strains, with diminished R93A effects. The assay endpoints are distinct and residual effects remain visible. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/A4ZDL6/entry/pfam/PF01657/; Accession and domain locations; paired UniProt identity facts | supports | A4ZDL6 version-1 sequence is 134 aa; mature chain 27-134 plus extra Met exactly matches PDB 4XRE entity 1, whose primary citation is PMID25139159. Current PF01657 36-131 maps to mature 10-105 and includes N11/R93/E104 at precursor37/119/130, unlike the historical narrow boundary discussed in the paper. No isolated-domain sufficiency or independently resequenced mutant stock is claimed. Formal supersession of paper accession 3W9Q was not verified. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01657 | data/families/PF01657.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Figures 5, 7 and 8 were visually inspected; NMR and structural evidence was read in text/captions without independent spectral or coordinate reanalysis. Supplementary CD, DSF and R93A mannan NMR panels were unavailable and remain author-reported. No experimental replication or new statistical testing was performed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T122505Z-pf01657-gnk2-binding-and-growth-contexts
title: PF01657 Gnk2 binding and antifungal assays with residue and dose qualifications
started_at: '2026-10-11T12:18:17Z'
finished_at: '2026-10-11T12:25:05Z'
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
summary: Fourteen observed effects in six graphs distinguish four direct SPR binding
  responses from ten indirect yeast and Fusarium growth effects. Current domain mapping,
  extra Met, residual activity and the twofold SPR dose discrepancy are explicit;
  binding is not joined to an unmeasured cell-death mechanism.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01657.yaml
    sha256: 14a38335f84cf7bab085aa9c5cf6b13e08afc556850ebb085b7247ea57784e0c
    role: context
  - path: data/families/PF01657.yaml
    sha256: e835dc4e1415b0b9386419484297eb36ca65fad586b116574519564a50f0aab2
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
  - path: evidence/PF01657/miyakawa-2014-gnk2.txt
    role: context
    sha256: 02c1524555fc066b6344d5d686f0b8e2ddc25f17c910d0940e75815ff33c21a4
  - path: evidence/PF01657/Gnk2-identity.txt
    role: context
    sha256: a5a81f8e8d2ddfbb77ced597cb0fa91f16051f61935aeb63f6b6ffdd90868819
targets:
- target_id: PF01657
  path: data/families/PF01657.yaml
  label: PF01657
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01657.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 24efd0e13a54544dc86f50607ede74c263ea7c1a044b155717971c2ba434b2d1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Pending PF01657 within the full 8296-family corpus; mature Ginkgo Gnk2
    is a sequence-verified protein example, not a family-wide member census.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01657
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Supplementary controls were not visually retrieved, exact SPR doses remain
      unresolved, and later actin-remodeling work, early purification evidence and
      other CRK/PDLP members remain incompletely assessed. Static structural contacts,
      mannobiose docking and growth effects do not establish a universal lectin mechanism,
      cell-wall damage, spore-germination inhibition or plant protection.
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
  - PF01657
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4213107/
  locator: Miyakawa 2014 full-text Results, Discussion and Methods; Figures 5, 7 and
    8 visually inspected. Supplementary CD/DSF/NMR controls are author-reported only
    because the linked DOC did not yield the supplement.
  accessed_at: '2026-10-11T12:25:05Z'
  support: supports
  snapshot_sha256: 02c1524555fc066b6344d5d686f0b8e2ddc25f17c910d0940e75815ff33c21a4
  summary: WT mannobiose SPR responses increase with dose and decrease with N11A/R93A/E104A
    substitutions. WT Gnk2 delays BY4741 growth, attenuated by R93A or mannan; delta-mnn2
    retains a much smaller response. WT reduces F. culmorum liquid OD600 and local
    growth near discs in two Fusarium strains, with diminished R93A effects. The assay
    endpoints are distinct and residual effects remain visible.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/A4ZDL6/entry/pfam/PF01657/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T12:25:05Z'
  support: supports
  snapshot_sha256: a5a81f8e8d2ddfbb77ced597cb0fa91f16051f61935aeb63f6b6ffdd90868819
  summary: A4ZDL6 version-1 sequence is 134 aa; mature chain 27-134 plus extra Met
    exactly matches PDB 4XRE entity 1, whose primary citation is PMID25139159. Current
    PF01657 36-131 maps to mature 10-105 and includes N11/R93/E104 at precursor37/119/130,
    unlike the historical narrow boundary discussed in the paper. No isolated-domain
    sufficiency or independently resequenced mutant stock is claimed. Formal supersession
    of paper accession 3W9Q was not verified.
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T12:25:05Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01657
  kind: record_content
  reference: data/families/PF01657.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T12:25:05Z'
  support: context_only
  snapshot_sha256: e835dc4e1415b0b9386419484297eb36ca65fad586b116574519564a50f0aab2
  quote: "id: Pfam:PF01657\npfam_id: PF01657\nname: Salt stress response/antifungal\n\
    short_name: Stress-antifung\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01657\n\
    counters:\n  proteins: 28393\n  matches: 54024\n  proteomes: 377\n  taxa: 1070\n\
    \  structures: 4\n  alphafold_models: 22295\n  domain_architectures: 587\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002902\ndescription: This domain is often found in association\
    \ with the kinase domains [pfam:PF00069] or [pfam:PF07714].\n  In many proteins\
    \ it is duplicated. It contains six conserved cysteines which are involved in\
    \ disulphide\n  bridges [[cite:PUB00052808]]. It has a role in salt stress response\
    \ [[cite:PUB00109166]] and has antifungal\n  activity [[cite:PUB00109167]].\n\
    curation_history: history/records/PF01657\ndiscussions:\n- discussion_id: pf01657-gnk2-causal-coverage\n\
    \  prompt: Resolve the SPR dose discrepancy and supplement access, then assess\
    \ later Gnk2 actin work and\n    other DUF26 members without assuming a common\
    \ mechanism.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: Four direct\
    \ binding-assay effects and ten indirect growth effects support a scoped Gnk2\
    \ example,\n    not a complete binding-to-cell-death trajectory or universal function\
    \ of PF01657.\n  evidence:\n  - reference: PMID:25139159\n    supports: PARTIAL\n\
    \    evidence_source: full_text_and_visually_inspected_figures_5_7_8\n    explanation:\
    \ Preserve Methods 1.25-20 versus Figure 5 0.625-10 mM mannobiose, small delta-mnn2\
    \ and\n      R93A residual delays, lack of displayed saccharide-only controls,\
    \ and separate disc/36-h endpoints.\n      Supplementary CD/DSF/NMR controls are\
    \ author-reported, not independently visually inspected. Historical\n      domain\
    \ 56-108 differs from current mature PF01657 10-105; all three tested residues\
    \ lie within the\n      current interval.\n  - reference: PMID:26315821\n    supports:\
    \ PARTIAL\n    evidence_source: uniprot_citation_lead_only\n    explanation: Later\
    \ actin-remodeling study is a follow-up lead, not reviewed evidence for an added\n\
    \      actin or cell-death edge. Early purification and other CRK/PDLP contexts\
    \ also remain incomplete.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n  notes:\
    \ NMR text reports mannose, glucose and N-acetylglucosamine responses, not exclusive\
    \ mannose recognition;\n    mannobiose docking, spore germination, wall damage,\
    \ biofilm prevention and plant protection are not\n    directly measured here.\
    \ PDB 4XRE matches the reference and publication, but formal supersession of\n\
    \    paper accession 3W9Q was not verified. Partial scientific self-review; IN_PROGRESS.\n\
    causal_graphs:\n- graph_id: gnk2-mannobiose-spr\n  title: Gnk2 substitutions reduce\
    \ alpha1,2-mannobiose binding responses\n  scope: Purified mature Ginkgo biloba\
    \ Gnk2 WT, N11A, R93A and E104A; Miyakawa 2014 Figure 5. Not the\n    His-tagged\
    \ NMR screening construct or a family-wide lectin mechanism.\n  context: Mature\
    \ Ala1-Phe108 plus an extra N-terminal Met, expressed periplasmically in E. coli\
    \ BL21(DE3)\n    using pET26b and pDsbABCD1. Untagged protein purified by SP Sepharose,\
    \ Mono S and Superdex 75. Immobilize\n    from 50 ug/ml acetate pH6 onto a noncarbohydrate\
    \ GLH chip at approximately 10000 RU; ProteOn XPR36\n    running buffer is 10\
    \ mM HEPES pH7 and 150 mM NaCl. Methods give analyte 1.25-20 mM, whereas Figure\n\
    \    5 labels 0.625-10 mM; the twofold discrepancy remains unresolved. Assays\
    \ described as triplicate.\n  family_mapping: A4ZDL6 sequence version 1 is 134\
    \ aa; mature 1-108 corresponds to precursor 27-134. UniProt/InterPro\n    sequences\
    \ match, with current PF01657 36-131, or mature 10-105. N11/R93/E104 correspond\
    \ to precursor\n    N37/R119/E130, all within that interval. PDB 4XRE entity 1\
    \ exactly matches Met plus the mature reference.\n    This is a domain-bearing\
    \ mature protein, not an isolated Pfam-interval construct.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:3311\n  limitations: Responses are directly observed binding-assay\
    \ effects, not activation of another protein\n    or fungal killing. N11A retains\
    \ visible response; low mutant signals do not establish zero affinity.\n    The\
    \ reported WT KD of 5.9 +/- 0.2 mM is not independently verified, especially given\
    \ the dose discrepancy.\n    The authors report similar mutant CD spectra, but\
    \ supplementary S5 was not visually accessible here;\n    immobilized active fractions\
    \ and local folding are not independently established. Static mannose contacts\n\
    \    do not directly observe the mannobiose binding trajectory.\n  nodes:\n  -\
    \ node_id: wt-mannobiose-dose\n    label: Increase alpha1,2-mannobiose over immobilized\
    \ WT Gnk2\n    node_type: PERTURBATION\n  - node_id: spr-binding-response\n  \
    \  label: Alpha1,2-mannobiose SPR response\n    node_type: STATE\n  - node_id:\
    \ n11a\n    label: N11A instead of WT mature Gnk2\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:A4ZDL6\n  - node_id: r93a\n    label: R93A instead\
    \ of WT mature Gnk2\n    node_type: PERTURBATION\n  - node_id: e104a\n    label:\
    \ E104A instead of WT mature Gnk2\n    node_type: PERTURBATION\n  edges:\n  -\
    \ edge_id: dose-increases-wt-binding-response\n    subject: wt-mannobiose-dose\n\
    \    predicate: increases\n    object: spr-binding-response\n    mechanism: Higher\
    \ labeled mannobiose doses yield larger WT sensor responses. This directly supports\n\
    \      a concentration-dependent biochemical interaction, with no precise affinity\
    \ recalculation or claim\n      that monosaccharide mannose was measured by SPR.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:25139159\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4213107/\n\
    \      snippet: dose-dependent\n      explanation: Figure 5 WT dose series was\
    \ visually inspected with SPR Results and Methods. The figure\n        and Methods\
    \ concentration ranges disagree by twofold.\n      cache_path: evidence/PF01657/miyakawa-2014-gnk2.txt\n\
    \      cache_sha256: 02c1524555fc066b6344d5d686f0b8e2ddc25f17c910d0940e75815ff33c21a4\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/A4ZDL6/entry/pfam/PF01657/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/A4ZDL6/entry/pfam/PF01657/\n\
    \      snippet: A4ZDL6 Pfam:PF01657; interval 36-131 inclusive.\n      explanation:\
    \ Current domain coordinates and exact UniProt/InterPro/4XRE sequence comparisons\
    \ verify\n        mature-protein scope and the three residue offsets.\n      cache_path:\
    \ evidence/PF01657/Gnk2-identity.txt\n      cache_sha256: a5a81f8e8d2ddfbb77ced597cb0fa91f16051f61935aeb63f6b6ffdd90868819\n\
    \  - edge_id: n11a-decreases-binding-response\n    subject: n11a\n    predicate:\
    \ decreases\n    object: spr-binding-response\n    mechanism: N11A gives smaller\
    \ mannobiose sensor responses than WT over the displayed matched dose\n      series,\
    \ but retains nonzero responses. This is the net substitution effect, not proof\
    \ that only\n      one hydrogen bond or the isolated Pfam domain changed.\n  \
    \  directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:25139159\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4213107/\n\
    \      snippet: markedly decreased compared with the wild-type protein\n     \
    \ explanation: Figure 5 N11A and WT sensorgrams visually support reduced responses\
    \ with residual binding;\n        Results reports CD controls whose supplementary\
    \ figure was not visually inspected.\n      cache_path: evidence/PF01657/miyakawa-2014-gnk2.txt\n\
    \      cache_sha256: 02c1524555fc066b6344d5d686f0b8e2ddc25f17c910d0940e75815ff33c21a4\n\
    \  - edge_id: r93a-decreases-binding-response\n    subject: r93a\n    predicate:\
    \ decreases\n    object: spr-binding-response\n    mechanism: R93A strongly reduces\
    \ the mannobiose sensor response relative to WT. Low signals prevent\n      a\
    \ fitted mutant affinity, rather than establishing mathematically zero binding\
    \ or direct fungal\n      lethality.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:25139159\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4213107/\n      snippet:\
    \ markedly decreased compared with the wild-type protein\n      explanation: Figure\
    \ 5 R93A versus WT, SPR Methods and Results; the separate yeast/Fusarium assays\n\
    \        are not a continuous molecular trajectory.\n      cache_path: evidence/PF01657/miyakawa-2014-gnk2.txt\n\
    \      cache_sha256: 02c1524555fc066b6344d5d686f0b8e2ddc25f17c910d0940e75815ff33c21a4\n\
    \  - edge_id: e104a-decreases-binding-response\n    subject: e104a\n    predicate:\
    \ decreases\n    object: spr-binding-response\n    mechanism: E104A produces smaller\
    \ mannobiose sensor responses than WT. The assay supports the substitution's\n\
    \      biochemical effect but not a measured E104A antifungal phenotype or a unique\
    \ atomic explanation.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:25139159\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC4213107/\n      snippet: markedly decreased\
    \ compared with the wild-type protein\n      explanation: Figure 5 E104A/WT comparison\
    \ was visually inspected; no N11A/E104A growth curves are\n        supplied by\
    \ this study.\n      cache_path: evidence/PF01657/miyakawa-2014-gnk2.txt\n   \
    \   cache_sha256: 02c1524555fc066b6344d5d686f0b8e2ddc25f17c910d0940e75815ff33c21a4\n\
    - graph_id: gnk2-by4741-growth-delay\n  title: WT Gnk2 delays BY4741 growth, with\
    \ attenuation by R93A or soluble mannan\n  scope: S. cerevisiae BY4741 exposed\
    \ to purified mature Ginkgo Gnk2; Miyakawa 2014 Figure 7A, not the\n    delta-mnn2\
    \ culture or an in-plant infection test.\n  context: BY4741 MATa his3delta1 leu2delta0\
    \ met15delta0 ura3delta0, potato dextrose broth at 25 C. Transfer\n    pre-culture\
    \ at OD600 1 into fresh medium at OD600 0.01 with 2 uM WT/R93A or no protein.\
    \ Monitor OD600\n    until 2.55. The WT-plus-saccharide arms contain 0.5% w/v\
    \ yeast mannan or 50 mM D-mannose. Methods\n    state two repetitions; Figure\
    \ 7 shows growth curves without statistical confidence intervals.\n  family_mapping:\
    \ Purified mature A4ZDL6 residues 27-134 plus extra N-terminal Met; current PF01657\
    \ 36-131\n    corresponds to mature 10-105. Mature R93 maps to precursor R119\
    \ inside the domain. The yeast is the\n    assay organism, not the source of this\
    \ Ginkgo protein.\n  scope_status: PHENOTYPIC\n  limitations: Turbidity delay\
    \ is indirect physiology, not direct cell-wall damage, killing or measured\n \
    \   spore germination. The Discussion specifies longer lag rather than reduced\
    \ log-phase growth rate.\n    R93A and mannan attenuation are not complete null\
    \ effects. Saccharide-only controls are not displayed,\n    so competitive sequestration\
    \ is an interpretation, not a uniquely established causal step. Similar\n    R93A\
    \ thermal stability and mannan NMR results are author-reported supplementary controls,\
    \ not visually\n    inspected here.\n  nodes:\n  - node_id: wt-treatment\n   \
    \ label: Add 2 uM WT Gnk2 to BY4741\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:A4ZDL6\n  - node_id: yeast-growth-delay\n    label: Delay in\
    \ BY4741 OD600 growth curves\n    node_type: PHENOTYPE\n  - node_id: r93a-treatment\n\
    \    label: Substitute 2 uM R93A for WT Gnk2\n    node_type: PERTURBATION\n  -\
    \ node_id: soluble-mannan\n    label: Add 0.5% yeast mannan during WT Gnk2 treatment\n\
    \    node_type: PERTURBATION\n  edges:\n  - edge_id: wt-increases-growth-delay\n\
    \    subject: wt-treatment\n    predicate: increases\n    object: yeast-growth-delay\n\
    \    mechanism: WT-treated cultures enter their OD600 rise much later than the\
    \ no-protein control. The\n      measured effect is lag extension, not an inferred\
    \ molecular lesion or a permanently lower exponential\n      growth rate.\n  \
    \  directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:25139159\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4213107/\n\
    \      snippet: Gnk2 prolonged the lag phase of yeast growth\n      explanation:\
    \ Figure 7A curves visually inspected with yeast Methods and Discussion; baseline,\
    \ dose,\n        medium and timing are explicit.\n      cache_path: evidence/PF01657/miyakawa-2014-gnk2.txt\n\
    \      cache_sha256: 02c1524555fc066b6344d5d686f0b8e2ddc25f17c910d0940e75815ff33c21a4\n\
    \  - edge_id: r93a-decreases-growth-delay\n    subject: r93a-treatment\n    predicate:\
    \ decreases\n    object: yeast-growth-delay\n    mechanism: R93A-treated cultures\
    \ have much less delay than WT-treated cultures, with a small residual\n     \
    \ delay relative to the untreated control. Loss of all activity or equal binding-site-specific\
    \ effects\n      on every other protein property are not asserted.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:25139159\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4213107/\n\
    \      snippet: Gnk2 prolonged the lag phase of yeast growth\n      explanation:\
    \ Figure 7A WT/R93A/no-protein comparisons and Results; the residual delay remains\
    \ visible\n        rather than being labeled complete inactivity.\n      cache_path:\
    \ evidence/PF01657/miyakawa-2014-gnk2.txt\n      cache_sha256: 02c1524555fc066b6344d5d686f0b8e2ddc25f17c910d0940e75815ff33c21a4\n\
    \  - edge_id: mannan-decreases-wt-growth-delay\n    subject: soluble-mannan\n\
    \    predicate: decreases\n    object: yeast-growth-delay\n    mechanism: Soluble\
    \ yeast mannan strongly attenuates the growth delay seen with WT Gnk2 alone. The\n\
    \      result is consistent with ligand competition, but the cellular assay does\
    \ not uniquely distinguish\n      it from other effects of added mannan.\n   \
    \ directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:25139159\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4213107/\n\
    \      snippet: Gnk2 prolonged the lag phase of yeast growth\n      explanation:\
    \ Figure 7A WT-plus-mannan versus WT-alone curves and 0.5% Methods condition;\
    \ the 50\n        mM mannose arm has little attenuation and is retained as a condition-specific\
    \ negative.\n      cache_path: evidence/PF01657/miyakawa-2014-gnk2.txt\n     \
    \ cache_sha256: 02c1524555fc066b6344d5d686f0b8e2ddc25f17c910d0940e75815ff33c21a4\n\
    - graph_id: gnk2-mnn2-dependent-growth-response\n  title: The delta-mnn2 yeast\
    \ background strongly attenuates the Gnk2 growth delay\n  scope: S. cerevisiae\
    \ BY4741 and its separately supplied delta-mnn2 variant, each compared with its\
    \ own\n    no-Gnk2 control; Miyakawa 2014 Figure 7A/B.\n  context: Potato dextrose\
    \ broth, 25 C, initial OD600 0.01, 2 uM WT Gnk2, OD600 followed to 2.55. MNN2\n\
    \    encodes an N-linked-glycan alpha1,2-mannosyltransferase; deletion alters\
    \ those mannosylated branches,\n    not all cell-wall mannan. No MNN2 complementation\
    \ is shown.\n  family_mapping: The applied protein is mature Ginkgo A4ZDL6 plus\
    \ extra Met, with PF01657 at precursor\n    36-131. The genetic perturbation is\
    \ in the target yeast, not in Gnk2 or its Pfam domain.\n  scope_status: PHENOTYPIC\n\
    \  limitations: The edge compares treatment responses against each strain's own\
    \ baseline, not simply absolute\n    treated-culture growth. Figure 7B has a small\
    \ residual delay, so the Results' no-influence wording\n    is not adopted literally.\
    \ No rescue or direct glycan occupancy measurement isolates the deleted gene's\n\
    \    immediate molecular effect. Delta-och1 was too growth impaired to assay and\
    \ is not evidence of Gnk2\n    resistance.\n  nodes:\n  - node_id: mnn2-deletion-background\n\
    \    label: Delta-mnn2 background instead of parental BY4741\n    node_type: PERTURBATION\n\
    \  - node_id: gnk2-dependent-delay\n    label: Gnk2-dependent delay relative to\
    \ each strain's untreated control\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ mnn2-deletion-decreases-delay-response\n    subject: mnn2-deletion-background\n\
    \    predicate: decreases\n    object: gnk2-dependent-delay\n    mechanism: The\
    \ additional growth delay caused by WT Gnk2 is markedly smaller in delta-mnn2\
    \ than in\n      the parental strain. This supports a glycosylation-background-dependent\
    \ phenotype, not total mannan\n      absence or a directly observed binding-to-wall-damage\
    \ chain.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:25139159\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC4213107/\n      snippet: Gnk2 prolonged\
    \ the lag phase of yeast growth\n      explanation: Figure 7A/B were visually\
    \ compared with yeast Methods and Results; the small residual\n        delta-mnn2\
    \ delay qualifies the text's no-effect statement.\n      cache_path: evidence/PF01657/miyakawa-2014-gnk2.txt\n\
    \      cache_sha256: 02c1524555fc066b6344d5d686f0b8e2ddc25f17c910d0940e75815ff33c21a4\n\
    - graph_id: gnk2-fculmorum-liquid-growth\n  title: WT Gnk2 reduces the F. culmorum\
    \ liquid-culture endpoint more than R93A\n  scope: F. culmorum IFM50210 exposed\
    \ to WT or R93A mature Gnk2, Miyakawa 2014 Figure 8C; separate from\n    disc\
    \ diffusion and yeast lag assays.\n  context: Potato dextrose broth at 25 C, initial\
    \ OD600 0.005; 2 or 10 uM WT/R93A; measure OD600 after\n    36 h. Inhibition is\
    \ relative to the no-protein endpoint. Figure 8C gives means and SD with n=3;\
    \ no\n    new statistical analysis is performed.\n  family_mapping: Ginkgo A4ZDL6\
    \ mature 1-108 corresponds to precursor 27-134, plus expression-derived\n    Met.\
    \ PF01657 36-131 contains R119, the precursor coordinate of mature R93. Whole\
    \ mature protein is\n    tested against F. culmorum, not an isolated domain or\
    \ a fungal homolog.\n  scope_status: PHENOTYPIC\n  limitations: A 36-h turbidity\
    \ endpoint is not a measured instantaneous growth rate, viability count\n    or\
    \ fungicidal mechanism. WT inhibits by 22.1% at 2 uM and 68.2% at 10 uM; R93A\
    \ retains 7.6% inhibition\n    at 10 uM. The reported 2-10-uM IC50 bracket is\
    \ not a fitted exact value. Similar R93A stability is\n    author-reported; no\
    \ unique cellular lesion is demonstrated.\n  nodes:\n  - node_id: wt-liquid-treatment\n\
    \    label: Add 10 uM WT Gnk2 to F. culmorum liquid culture\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:A4ZDL6\n  - node_id: liquid-growth-endpoint\n\
    \    label: F. culmorum OD600 after 36 h\n    node_type: PHENOTYPE\n  - node_id:\
    \ r93a-liquid-treatment\n    label: Substitute 10 uM R93A for WT Gnk2\n    node_type:\
    \ PERTURBATION\n  - node_id: liquid-growth-inhibition\n    label: Inhibition of\
    \ the 36-h OD600 endpoint\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: wt-decreases-liquid-growth\n\
    \    subject: wt-liquid-treatment\n    predicate: decreases\n    object: liquid-growth-endpoint\n\
    \    mechanism: WT Gnk2 lowers the 36-h OD600 endpoint relative to the no-protein\
    \ control, corresponding\n      to 68.2% inhibition at 10 uM. The lower 2-uM dose\
    \ shows a smaller effect; neither measurement identifies\n      a unique downstream\
    \ molecular mechanism.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:25139159\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC4213107/\n      snippet: Growth-inhibitory\
    \ ratio\n      explanation: Figure 8C bars were visually inspected with fungal\
    \ Methods and the numerical Results;\n        the assay is a 36-h endpoint despite\
    \ the Methods' growth-rate terminology.\n      cache_path: evidence/PF01657/miyakawa-2014-gnk2.txt\n\
    \      cache_sha256: 02c1524555fc066b6344d5d686f0b8e2ddc25f17c910d0940e75815ff33c21a4\n\
    \  - edge_id: r93a-decreases-liquid-growth-inhibition\n    subject: r93a-liquid-treatment\n\
    \    predicate: decreases\n    object: liquid-growth-inhibition\n    mechanism:\
    \ At 10 uM, R93A produces much less endpoint inhibition than WT, 7.6% versus 68.2%.\
    \ Residual\n      activity prevents a complete-null claim, and this net protein-substitution\
    \ effect is not a direct\n      observation of cell-wall disruption.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:25139159\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4213107/\n\
    \      snippet: Growth-inhibitory ratio\n      explanation: Figure 8C WT/R93A\
    \ bars at matched 10-uM dose and the explicit Results values support\n       \
    \ attenuated, not abolished, inhibition.\n      cache_path: evidence/PF01657/miyakawa-2014-gnk2.txt\n\
    \      cache_sha256: 02c1524555fc066b6344d5d686f0b8e2ddc25f17c910d0940e75815ff33c21a4\n\
    - graph_id: gnk2-foxysporum-disc-growth\n  title: WT Gnk2 produces local growth\
    \ exclusion in the F. oxysporum disc assay\n  scope: F. oxysporum IAM5009 on potato\
    \ dextrose agar, Miyakawa 2014 Figure 8A; not the liquid F. culmorum\n    experiment.\n\
    \  context: Incubate at 25 C. Place 6-mm discs 5 mm from a roughly 30-mm colony,\
    \ adding 30 ul of 10 mg/ml\n    WT/R93A Gnk2 (300 ug) or 10 mM Tris pH7 buffer.\
    \ Methods score 3 days after disc placement, whereas\n    the caption reports\
    \ 8 days after seeding; these timing origins can differ and are not assumed contradictory.\n\
    \  family_mapping: Mature Ginkgo A4ZDL6 27-134 plus extra Met; current PF01657\
    \ 36-131, including mature\n    R93 at precursor119. This is a protein-dose experiment\
    \ on a named fungal strain, not a family-wide\n    antifungal claim.\n  scope_status:\
    \ PHENOTYPIC\n  limitations: Qualitative plate morphology, without a reported\
    \ zone diameter or independent viability\n    measurement. Diffusion, stability\
    \ and effective local concentration are not isolated. Figure 8A does\n    not\
    \ establish killing, a precise potency or the immediate cellular mechanism.\n\
    \  nodes:\n  - node_id: wt-disc\n    label: Place a 300-ug WT Gnk2 disc beside\
    \ F. oxysporum\n    node_type: PERTURBATION\n  - node_id: local-growth-exclusion\n\
    \    label: Local mycelial growth exclusion around the disc\n    node_type: PHENOTYPE\n\
    \  - node_id: r93a-disc\n    label: Substitute a 300-ug R93A disc for WT\n   \
    \ node_type: PERTURBATION\n  edges:\n  - edge_id: wt-increases-local-growth-exclusion\n\
    \    subject: wt-disc\n    predicate: increases\n    object: local-growth-exclusion\n\
    \    mechanism: The WT disc has a local crescent of reduced mycelial advance compared\
    \ with the buffer disc\n      on the same plate. This is a spatial growth phenotype,\
    \ not a measured cell-wall degradation reaction.\n    directness: INDIRECT\n \
    \   support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:25139159\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4213107/\n\
    \      snippet: R93A mutant did not inhibit\n      explanation: Figure 8A supplies\
    \ the visually inspected WT-versus-buffer disc phenotype; Results\n        contrasts\
    \ it with R93A. The caption and Methods identify the 300-ug dose, strain and buffer\
    \ control.\n      cache_path: evidence/PF01657/miyakawa-2014-gnk2.txt\n      cache_sha256:\
    \ 02c1524555fc066b6344d5d686f0b8e2ddc25f17c910d0940e75815ff33c21a4\n  - edge_id:\
    \ r93a-decreases-local-growth-exclusion\n    subject: r93a-disc\n    predicate:\
    \ decreases\n    object: local-growth-exclusion\n    mechanism: The R93A disc\
    \ lacks the prominent WT-associated growth-exclusion crescent at the matched\n\
    \      nominal dose. This qualitative comparison does not prove identical diffusion\
    \ or absolute absence\n      of activity.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:25139159\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4213107/\n      snippet:\
    \ R93A mutant did not inhibit\n      explanation: Figure 8A WT/R93A/control discs\
    \ were visually inspected with its Results and fungal\n        Methods; no numerical\
    \ zone value is inferred from the photograph.\n      cache_path: evidence/PF01657/miyakawa-2014-gnk2.txt\n\
    \      cache_sha256: 02c1524555fc066b6344d5d686f0b8e2ddc25f17c910d0940e75815ff33c21a4\n\
    - graph_id: gnk2-fculmorum-disc-growth\n  title: WT Gnk2 produces local growth\
    \ exclusion in the F. culmorum disc assay\n  scope: F. culmorum IFM50210 on potato\
    \ dextrose agar, Miyakawa 2014 Figure 8B; distinct from this strain's\n    liquid\
    \ endpoint and the F. oxysporum plate.\n  context: Incubate at 25 C. Place 6-mm\
    \ discs 5 mm from a roughly 30-mm colony; each carries 300 ug WT/R93A\n    in\
    \ 30 ul or 10 mM Tris pH7 buffer. Methods specify 3 days after disc placement,\
    \ caption 8 days after\n    seeding. Local delivery is not a uniform 10-uM liquid\
    \ treatment.\n  family_mapping: Ginkgo A4ZDL6 mature 27-134 plus added Met contains\
    \ PF01657 36-131. R93A uses mature\n    numbering, corresponding to precursor\
    \ R119. No kinase-containing plant receptor or fungal homolog\n    is tested by\
    \ this graph.\n  scope_status: PHENOTYPIC\n  limitations: A qualitative disc-associated\
    \ growth pattern does not establish killing or a unique molecular\n    target.\
    \ No quantitative zone diameter is reported and local diffusion or stability differences\
    \ remain\n    possible. Liquid-culture inhibition percentages must not be assigned\
    \ to this plate.\n  nodes:\n  - node_id: wt-disc\n    label: Place a 300-ug WT\
    \ Gnk2 disc beside F. culmorum\n    node_type: PERTURBATION\n  - node_id: local-growth-exclusion\n\
    \    label: Local mycelial growth exclusion around the disc\n    node_type: PHENOTYPE\n\
    \  - node_id: r93a-disc\n    label: Substitute a 300-ug R93A disc for WT\n   \
    \ node_type: PERTURBATION\n  edges:\n  - edge_id: wt-increases-local-growth-exclusion\n\
    \    subject: wt-disc\n    predicate: increases\n    object: local-growth-exclusion\n\
    \    mechanism: The WT disc is associated with a local growth-exclusion crescent\
    \ relative to the buffer\n      disc on the same plate. The intervention supports\
    \ a local antifungal phenotype, not an observed\n      chemical wall-cleavage\
    \ step.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:25139159\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4213107/\n\
    \      snippet: R93A mutant did not inhibit\n      explanation: Figure 8B WT-versus-buffer\
    \ discs were visually inspected, with Results contrasting\n        R93A and the\
    \ caption and Methods assigning the strain and disc dose.\n      cache_path: evidence/PF01657/miyakawa-2014-gnk2.txt\n\
    \      cache_sha256: 02c1524555fc066b6344d5d686f0b8e2ddc25f17c910d0940e75815ff33c21a4\n\
    \  - edge_id: r93a-decreases-local-growth-exclusion\n    subject: r93a-disc\n\
    \    predicate: decreases\n    object: local-growth-exclusion\n    mechanism:\
    \ R93A produces much less local growth exclusion than WT at the same nominal 300-ug\
    \ dose.\n      No completely inactive allele, identical diffusion or mechanistic\
    \ link to the liquid-culture endpoint\n      is assumed.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:25139159\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4213107/\n\
    \      snippet: R93A mutant did not inhibit\n      explanation: Figure 8B WT/R93A/control\
    \ disc comparison and Results, inspected separately from Figure\n        8C's\
    \ quantitative liquid-culture bars.\n      cache_path: evidence/PF01657/miyakawa-2014-gnk2.txt\n\
    \      cache_sha256: 02c1524555fc066b6344d5d686f0b8e2ddc25f17c910d0940e75815ff33c21a4\n\
    curation_events:\n- timestamp: '2026-10-11T12:18:17Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate six Gnk2 causal graphs with residue\
    \ and assay boundaries\n  history_record: history/records/PF01657/2026-10-11T121817Z-codex-c6d515.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: A4ZDL6 version-1 sequence is 134 aa; mature chain 27-134 plus extra Met
    exactly matches PDB 4XRE entity 1, whose primary citation is PMID25139159. Current
    PF01657 36-131 maps to mature 10-105 and includes N11/R93/E104 at precursor37/119/130,
    unlike the historical narrow boundary discussed in the paper. No isolated-domain
    sufficiency or independently resequenced mutant stock is claimed. Formal supersession
    of paper accession 3W9Q was not verified.
  target_ids:
  - PF01657
  evidence_ids:
  - identity
  - primary
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: The six graphs separate SPR, parental yeast, glycosylation-background dependence,
    F. culmorum liquid culture and two species-specific disc assays. All fourteen
    edges are OBSERVED; four DIRECT biochemical and ten INDIRECT phenotypic. Figure5
    labels 0.625-10 mM versus Methods1.25-20 mM, so no independently verified KD is
    asserted. The delta-mnn2 curve's small residual delay qualifies strong no-effect
    wording. Residual R93A activity, absent displayed saccharide-only controls, protein
    active-fraction limits and distinct timing origins prevent stronger mechanistic
    claims.
  target_ids:
  - PF01657
  evidence_ids:
  - primary
  - native
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Supplementary controls were not visually retrieved, exact SPR doses remain
    unresolved, and later actin-remodeling work, early purification evidence and other
    CRK/PDLP members remain incompletely assessed. Static structural contacts, mannobiose
    docking and growth effects do not establish a universal lectin mechanism, cell-wall
    damage, spore-germination inhibition or plant protection.
  target_ids:
  - PF01657
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01657-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve Gnk2 assay discrepancies and extend member-specific downstream evidence
  description: Retrieve and inspect supplementary S5-S7, resolve the factor-two SPR
    concentration labels and the 3W9Q/4XRE accession relationship, and review PMID26315821
    for separately scoped downstream experiments. Preserve current residue mapping,
    residual responses, genotype baselines, absent saccharide-only controls and lack
    of family-wide transfer.
  target_ids:
  - PF01657
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01657.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Retrieve and inspect supplementary S5-S7, resolve the factor-two SPR
    concentration labels and the 3W9Q/4XRE accession relationship, and review PMID26315821
    for separately scoped downstream experiments. Preserve current residue mapping,
    residual responses, genotype baselines, absent saccharide-only controls and lack
    of family-wide transfer.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01657
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Figures 5, 7 and 8 were visually inspected; NMR and structural evidence was read
  in text/captions without independent spectral or coordinate reanalysis. Supplementary
  CD, DSF and R93A mannan NMR panels were unavailable and remain author-reported.
  No experimental replication or new statistical testing was performed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
