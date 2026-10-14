# Scoped scientific self-review of TatD nuclease and peroxide-growth effects

- Review: 20261011T083335Z-pf01026-tatd-nuclease-and-peroxide-contexts
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T08:33:19Z
- Finished UTC: 2026-10-11T08:33:35Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Four graphs retain seven OBSERVED edges, six DIRECT biochemical effects and one INDIRECT whole-gene growth effect. Tagged Mg/ssDNA digestion, separate residue substitutions, untagged THF-duplex incision and chronic-peroxide growth remain separate contexts. Source discrepancies and control gaps are explicit; partial coverage and IN_PROGRESS remain.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01026 TatD, the next accession-ordered SEEDED family, using Chen 2014 and Dorival/Eichman 2023 primary experiments.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01026 | data/families/PF01026.yaml | generated | PF01026 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01026 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01026.

K-12 reference P27859 tatD/b4483/JW5931 has 260 residues, sequence version 3, exact UniProt/InterPro sequence agreement and PF01026 at 2-257. All adopted substitution sites match the reference. K-12 donor, BL21 production hosts, 2014 retained C-terminal tag and 2023 untagged preparation are distinguished; complete experimental clone sequences remain unverified.

### Directed effects and limits

graph: supported. Targets: PF01026.

Joint biochemical systems are not split into independently sufficient enzyme, cofactor and substrate causes. Mutant effects concern measured digestion, not observed general-base or metal-coordination microsteps. The later THF-duplex endpoint is not natural-AP proof or a calcium-only switch. Whole-gene spot growth does not establish a direct nuclease-to-repair-to-survival chain.

### Remaining family coverage

completeness: concern. Targets: PF01026.

Complete clones, mutant-panel concentrations, supplementary details and assay controls remain incomplete. The 2023 manuscript/Table S1 site-number discrepancy and the 2014 protease-K unit remain unresolved. Human proteins, other bacterial paralogs, additional damaged substrates, triple-deletion genetics and other family members require separate mapping and curation. Raw data were not independently reanalyzed.

## Findings

### additional-contexts: Resolve TatD assay metadata and expand member-specific causal coverage

minor / open / confirmed; issue key: pf01026-causal-context-coverage.

Obtain complete constructs and mutant-panel methods, assess purification and rescue controls, resolve source discrepancies, and curate additional paralog or cellular contexts with their own primary evidence. Preserve substrate/cofactor distinctions and append a successor review before any status promotion.

## Recommended Actions And Acceptance Checks

### extend-contexts

Obtain complete constructs and mutant-panel methods, assess purification and rescue controls, resolve source discrepancies, and curate additional paralog or cellular contexts with their own primary evidence. Preserve substrate/cofactor distinctions and append a successor review before any status promotion.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC4176340/; Expression, nuclease and cell-survival Methods; relevant Results and mechanism Discussion; Figures 2, 3 and 5 visually inspected | supports | Figure 2B supports tagged TatD/Mg/ssDNA digestion; Figure 5C supports H62A, E91A, E201A and D203A decreases without proving their chemical mechanism. Figure 3B supports a separate chronic-peroxide colony-growth effect of whole-gene deletion. Unknown mutant-panel units, quench notation, strain metadata and absent adopted genetic rescue remain explicit. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/P27859/entry/pfam/PF01026/; Accession and domain locations; paired UniProt identity facts | supports | K-12 reference P27859 tatD/b4483/JW5931 has 260 residues, sequence version 3, exact UniProt/InterPro sequence agreement and PF01026 at 2-257. All adopted substitution sites match the reference. K-12 donor, BL21 production hosts, 2014 retained C-terminal tag and 2023 untagged preparation are distinguished; complete experimental clone sequences remain unverified. |
| internal-thf-incision | https://pmc.ncbi.nlm.nih.gov/articles/PMC10085689/; Published purification and nuclease Methods, bacterial Figure 6 Results and Discussion; author-manuscript Figure 6 and Table S1 | supports | Untagged EcTatD preparation yields discrete product from a THF-containing duplex in 5 mM calcium. Exact sequence and conditions are retained; no bacterial mock-purification control is labeled, human BH110 controls are not transferred, and calcium/substrate changes are not conflated. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01026 | data/families/PF01026.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Chen 2014 Figures 2, 3 and 5 were visually inspected. The Dorival author-manuscript Figure 6 and Table S1 were visually inspected and checked against published Methods and bacterial Results; the manuscript is not the publisher PDF. Other supplements, raw replicate gels, kinetic fits and atomic mechanisms were not independently reviewed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T083335Z-pf01026-tatd-nuclease-and-peroxide-contexts
title: Scoped scientific self-review of TatD nuclease and peroxide-growth effects
started_at: '2026-10-11T08:33:19Z'
finished_at: '2026-10-11T08:33:35Z'
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
summary: Four graphs retain seven OBSERVED edges, six DIRECT biochemical effects and
  one INDIRECT whole-gene growth effect. Tagged Mg/ssDNA digestion, separate residue
  substitutions, untagged THF-duplex incision and chronic-peroxide growth remain separate
  contexts. Source discrepancies and control gaps are explicit; partial coverage and
  IN_PROGRESS remain.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01026.yaml
    sha256: 9599e9a994e6379811b9ef210fce86d538ff238916c5152aac622d1efb64f496
    role: context
  - path: data/families/PF01026.yaml
    sha256: 78efe148c90e3f2baf2261e020193bb1741b8c369b53968385048ccbd379d99b
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
  - path: evidence/PF01026/chen-2014-tatD.txt
    role: context
    sha256: aff44a1ab44a7681a75281878d4bd1d8dc76d03cec37c4a09960084bd7d4618f
  - path: evidence/PF01026/TatD-identity.txt
    role: context
    sha256: 6ac10bdd28f4cb55c0068f6cd6e3e81f8030e0cfa5f17df3c536c1259215b197
  - path: evidence/PF01026/dorival-2023-tatD.txt
    role: context
    sha256: fc60ebd8e94557fe95b9482cbb73c26c50ea336aae3b38c6983d6b9d5d6cdd70
targets:
- target_id: PF01026
  path: data/families/PF01026.yaml
  label: PF01026
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01026.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: ab5d4a4011ba57cf4bac50a233585a6a3f71c3f86ae1b92ac735af20939a081e
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01026 TatD, the next accession-ordered SEEDED family, using Chen 2014
    and Dorival/Eichman 2023 primary experiments.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01026
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Complete clones, mutant-panel concentrations, supplementary details and
      assay controls remain incomplete. The 2023 manuscript/Table S1 site-number discrepancy
      and the 2014 protease-K unit remain unresolved. Human proteins, other bacterial
      paralogs, additional damaged substrates, triple-deletion genetics and other
      family members require separate mapping and curation. Raw data were not independently
      reanalyzed.
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
  - PF01026
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4176340/
  locator: Expression, nuclease and cell-survival Methods; relevant Results and mechanism
    Discussion; Figures 2, 3 and 5 visually inspected
  accessed_at: '2026-10-11T08:33:35Z'
  support: supports
  snapshot_sha256: aff44a1ab44a7681a75281878d4bd1d8dc76d03cec37c4a09960084bd7d4618f
  summary: Figure 2B supports tagged TatD/Mg/ssDNA digestion; Figure 5C supports H62A,
    E91A, E201A and D203A decreases without proving their chemical mechanism. Figure
    3B supports a separate chronic-peroxide colony-growth effect of whole-gene deletion.
    Unknown mutant-panel units, quench notation, strain metadata and absent adopted
    genetic rescue remain explicit.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P27859/entry/pfam/PF01026/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T08:33:35Z'
  support: supports
  snapshot_sha256: 6ac10bdd28f4cb55c0068f6cd6e3e81f8030e0cfa5f17df3c536c1259215b197
  summary: K-12 reference P27859 tatD/b4483/JW5931 has 260 residues, sequence version
    3, exact UniProt/InterPro sequence agreement and PF01026 at 2-257. All adopted
    substitution sites match the reference. K-12 donor, BL21 production hosts, 2014
    retained C-terminal tag and 2023 untagged preparation are distinguished; complete
    experimental clone sequences remain unverified.
- evidence_id: internal-thf-incision
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10085689/
  locator: Published purification and nuclease Methods, bacterial Figure 6 Results
    and Discussion; author-manuscript Figure 6 and Table S1
  summary: Untagged EcTatD preparation yields discrete product from a THF-containing
    duplex in 5 mM calcium. Exact sequence and conditions are retained; no bacterial
    mock-purification control is labeled, human BH110 controls are not transferred,
    and calcium/substrate changes are not conflated.
  accessed_at: '2026-10-11T08:33:35Z'
  support: supports
  snapshot_sha256: fc60ebd8e94557fe95b9482cbb73c26c50ea336aae3b38c6983d6b9d5d6cdd70
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T08:33:35Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01026
  kind: record_content
  reference: data/families/PF01026.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T08:33:35Z'
  support: context_only
  snapshot_sha256: 78efe148c90e3f2baf2261e020193bb1741b8c369b53968385048ccbd379d99b
  quote: "id: Pfam:PF01026\npfam_id: PF01026\nname: TatD related DNase\nshort_name:\
    \ TatD_DNase\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01026\n\
    counters:\n  proteins: 42146\n  matches: 42379\n  proteomes: 21954\n  taxa: 35333\n\
    \  structures: 16\n  alphafold_models: 29396\n  domain_architectures: 259\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR001130\ndescription: This family of proteins are related\
    \ to a large superfamily of metalloenzymes [[cite:PUB00004994]].\n  TatD, a member\
    \ of this family has been shown experimentally to be a DNase enzyme.\ncuration_history:\
    \ history/records/PF01026\ndiscussions:\n- discussion_id: tatd-context-controls-and-family-coverage\n\
    \  prompt: Resolve assay metadata and nuclease-to-cellular-function links before\
    \ expanding TatD mechanisms.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale:\
    \ Biochemical endpoints, point substitutions and deletion growth are distinct\
    \ causal contexts.\n    The 2014 terminal-abasic substrate and 2023 internal-THF\
    \ duplex differ; human catalytic proposals\n    and bacterial paralog phenotypes\
    \ are not interchangeable.\n  evidence:\n  - reference: PMID:25114049\n    supports:\
    \ PARTIAL\n    evidence_source: full_text\n    explanation: Main methods and Figures\
    \ 2/3/5 support the adopted effects but leave mutant-panel doses,\n      clone\
    \ details, quench units and molecular microsteps unresolved.\n  - reference: PMID:36881763\n\
    \    supports: PARTIAL\n    evidence_source: full_text\n    explanation: Bacterial\
    \ Figure 6 supports internal-THF incision; Table S1 and the manuscript caption\n\
    \      disagree on site numbering. Human proteins, YcfH/YjjV and triple-knockout\
    \ contexts need separately\n      mapped curation.\n  posed_by: Codex\n  posed_date:\
    \ '2026-10-11'\n  notes: Retrieve complete construct and supplemental details;\
    \ assess purification controls, genetic rescue\n    and other family members with\
    \ their own evidence. No precise catalytic metal count or family-wide\n    function\
    \ follows from these graphs. Partial same-agent scientific review; keep IN_PROGRESS.\n\
    causal_graphs:\n- graph_id: tatd-magnesium-ssdna-digestion\n  title: Purified\
    \ tagged TatD digests ssDNA in a magnesium-containing reaction\n  scope: Full-length\
    \ E. coli TatD with a C-terminal His tag, not an isolated Pfam domain or a cellular\n\
    \    repair pathway.\n  context: K-12 tatD in pET22b expressed in BL21-CodonPlus-RIPL\
    \ and purified by Ni-NTA and Q-Sepharose.\n    Figure 2B uses 40 nM 5'-32P-labeled\
    \ 20-nt ssDNA, 0-0.5 uM TatD, 2 mM Mg2+, 3 mM MOPS, 75 mM NaCl,\n    pH 7.2, 10\
    \ uL, 37 C for 1 h. Substrate sequence is CAAACTCTCTCTCTCTCAAC.\n  family_mapping:\
    \ UniProtKB:P27859, tatD/b4483/JW5931, K-12 reference of 260 residues, sequence\
    \ version\n    3; exact UniProt/InterPro sequence agreement and PF01026 at 2-257\
    \ inclusive. Native reference, DNA\n    donor and expression host are distinct;\
    \ the complete tagged clone sequence is not independently reconstructed.\n  scope_status:\
    \ MECHANISTIC\n  taxon: NCBITaxon:562\n  limitations: This is a joint enzyme/substrate/cofactor\
    \ assay, not magnesium sufficiency or all-family\n    activity. No-metal, Ca2+\
    \ and Zn2+ negatives apply only to the tested ssDNA conditions; they do not\n\
    \    exclude AP endonuclease activity on another substrate. Proposed metal stoichiometry\
    \ and catalytic\n    microsteps remain unresolved. The source's 20 mM protease-K\
    \ quench unit is questionable and not silently\n    corrected.\n  nodes:\n  -\
    \ node_id: tatd-magnesium-ssdna-system\n    label: Tagged TatD plus 20-nt ssDNA\
    \ and 2 mM Mg2+\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:P27859\n\
    \  - node_id: shorter-ssdna-products\n    label: Shorter labeled DNA products\
    \ from the 20-nt substrate\n    node_type: STATE\n  edges:\n  - edge_id: tatd-magnesium-produces-shorter-dna\n\
    \    subject: tatd-magnesium-ssdna-system\n    predicate: produces\n    object:\
    \ shorter-ssdna-products\n    mechanism: The enzyme concentration series in the\
    \ magnesium-containing reaction converts the 20-nt\n      substrate into shorter\
    \ gel-resolved products. Separate 5'- versus 3'-labeling and terminal-blocking\n\
    \      tests support 3'-5' exonucleolysis without resolving the chemical microsteps.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:25114049\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4176340/\n\
    \      snippet: cleaved DNA most efficiently\n      explanation: Figure 2B is\
    \ the adopted WT magnesium-dependent digestion experiment; 2C/D support\n    \
    \    direction. The cache records the exact Figure 2B assay, concentration series\
    \ and metal controls.\n      cache_path: evidence/PF01026/chen-2014-tatD.txt\n\
    \      cache_sha256: aff44a1ab44a7681a75281878d4bd1d8dc76d03cec37c4a09960084bd7d4618f\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P27859/entry/pfam/PF01026/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P27859/entry/pfam/PF01026/\n\
    \      snippet: 'P27859 Pfam:PF01026 interval: 2-257, inclusive'\n      explanation:\
    \ Establishes native TatD family membership, not isolated-domain sufficiency or\
    \ experimental\n        clone sequencing.\n      cache_path: evidence/PF01026/TatD-identity.txt\n\
    \      cache_sha256: 6ac10bdd28f4cb55c0068f6cd6e3e81f8030e0cfa5f17df3c536c1259215b197\n\
    - graph_id: tatd-residue-substitution-digestion-effects\n  title: TatD H62A and\
    \ acidic substitutions reduce ssDNA digestion\n  scope: Separate purified single-residue\
    \ variants of the full-length C-terminally tagged E. coli TatD\n    preparation\
    \ in Figure 5C.\n  context: WT and QuikChange mutants use the same purification\
    \ workflow and 20-nt ssDNA assay. Figure\n    5C displays a 0.5/1/2 concentration\
    \ series without units in its image or caption. General methods\n    specify 37\
    \ C in MOPS/NaCl pH 7.2, but this panel's duration, DNA dose and metal concentration\
    \ are\n    not resolved; Figure 2B values are not substituted.\n  family_mapping:\
    \ P27859 sequence version 3 contains H62, E91, E201 and D203, all within PF01026\
    \ residues\n    2-257. H64, H127 and H152 are also verified and their alanine\
    \ mutants retain activity. These are intact-protein\n    perturbations, not isolated-domain\
    \ tests.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:562\n  limitations:\
    \ Directness refers to the measured biochemical digestion endpoint, not a demonstrated\
    \ histidine\n    general base, exact metal ligation or proton transfer. Altered\
    \ folding or effective protein concentration\n    is not excluded for every variant.\
    \ Panel-specific dose units and complete clone sequences require\n    follow-up.\n\
    \  nodes:\n  - node_id: h62a-substitution\n    label: H62A substitution in tagged\
    \ TatD\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:P27859\n\
    \  - node_id: e91a-substitution\n    label: E91A substitution in tagged TatD\n\
    \    node_type: PERTURBATION\n  - node_id: e201a-substitution\n    label: E201A\
    \ substitution in tagged TatD\n    node_type: PERTURBATION\n  - node_id: d203a-substitution\n\
    \    label: D203A substitution in tagged TatD\n    node_type: PERTURBATION\n \
    \ - node_id: mutant-assay-ssdna-digestion\n    label: Digestion of 20-nt ssDNA\
    \ relative to the WT preparation\n    node_type: ACTIVITY\n  edges:\n  - edge_id:\
    \ h62a-decreases-ssdna-digestion\n    subject: h62a-substitution\n    predicate:\
    \ decreases\n    object: mutant-assay-ssdna-digestion\n    mechanism: H62A shows\
    \ substantially reduced digestion relative to WT in the same upper-panel concentration\n\
    \      series, while H64A, H127A and H152A retain digestion. This establishes\
    \ a substitution effect, not\n      its unique chemical explanation.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:25114049\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4176340/\n\
    \      snippet: significant reduced exonuclease activity\n      explanation: Figure\
    \ 5C upper panel and active-site Results distinguish H62A from WT and the three\n\
    \        other histidine substitutions; exact concentration units remain unresolved.\n\
    \      cache_path: evidence/PF01026/chen-2014-tatD.txt\n      cache_sha256: aff44a1ab44a7681a75281878d4bd1d8dc76d03cec37c4a09960084bd7d4618f\n\
    \  - edge_id: e91a-decreases-ssdna-digestion\n    subject: e91a-substitution\n\
    \    predicate: decreases\n    object: mutant-assay-ssdna-digestion\n    mechanism:\
    \ E91A leaves little residual digestion compared with the lower-panel WT series.\
    \ The effect\n      does not independently identify how many metal ions bind or\
    \ distinguish catalytic from structural\n      disruption.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:25114049\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4176340/\n\
    \      snippet: lost their exonuclease activity\n      explanation: Figure 5C\
    \ lower panel directly compares E91A and WT; acidic-mutant Results qualify\n \
    \       the caption's loss language as little residual activity, not an absolute\
    \ zero-rate determination.\n      cache_path: evidence/PF01026/chen-2014-tatD.txt\n\
    \      cache_sha256: aff44a1ab44a7681a75281878d4bd1d8dc76d03cec37c4a09960084bd7d4618f\n\
    \  - edge_id: e201a-decreases-ssdna-digestion\n    subject: e201a-substitution\n\
    \    predicate: decreases\n    object: mutant-assay-ssdna-digestion\n    mechanism:\
    \ E201A leaves little residual digestion compared with the matched WT concentration\
    \ series,\n      without establishing a specific metal-coordination mechanism.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:25114049\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4176340/\n\
    \      snippet: lost their exonuclease activity\n      explanation: Figure 5C\
    \ lower panel and its Results support the E201A decrease; mutant purification\n\
    \        is described but folding and exact panel doses are not independently\
    \ resolved.\n      cache_path: evidence/PF01026/chen-2014-tatD.txt\n      cache_sha256:\
    \ aff44a1ab44a7681a75281878d4bd1d8dc76d03cec37c4a09960084bd7d4618f\n  - edge_id:\
    \ d203a-decreases-ssdna-digestion\n    subject: d203a-substitution\n    predicate:\
    \ decreases\n    object: mutant-assay-ssdna-digestion\n    mechanism: D203A leaves\
    \ little residual digestion compared with the lower-panel WT preparation. A\n\
    \      direct effect on the measured reaction is retained without asserting a\
    \ resolved catalytic-water\n      pathway.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:25114049\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4176340/\n      snippet:\
    \ lost their exonuclease activity\n      explanation: Figure 5C lower panel and\
    \ active-site Results support the D203A decrease. Metal positions\n        in\
    \ structural superpositions remain proposals rather than observed causal edges.\n\
    \      cache_path: evidence/PF01026/chen-2014-tatD.txt\n      cache_sha256: aff44a1ab44a7681a75281878d4bd1d8dc76d03cec37c4a09960084bd7d4618f\n\
    - graph_id: tatd-internal-thf-duplex-incision\n  title: Untagged TatD preparation\
    \ incises an internal AP-site analogue in duplex DNA\n  scope: Purified E. coli\
    \ TatD in the 2023 bacterial Figure 6 assay, not the human TATDN proteins or the\n\
    \    2014 tagged preparation.\n  context: Synthetic tatD in modified pET-21 produces\
    \ untagged protein in BL21(DE3). Reaction contains\n    10 uM protein, 100 nM\
    \ FAM-labeled THF duplex, 5 mM CaCl2, 20 mM EPPS pH 8.0, 50 mM NaCl and 2.5% glycerol\n\
    \    at 37 C; gel time points are 1, 30 and 120 min. Table S1 gives FAM-CGTCTCCTGAAC/(THF)/GTGCTATCGCTC\n\
    \    annealed with GAGCGATAGCACAGTTCAGGAGACG.\n  family_mapping: E. coli TatD\
    \ reference P27859 maps to PF01026 residues 2-257. The synthetic gene's exact\n\
    \    sequence/version and full clone junctions are not independently supplied\
    \ here; current native mapping\n    is not a tag or strain assertion about all\
    \ bacterial paralogs.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:562\n \
    \ limitations: The measured substrate contains THF, not a natural AP site. No\
    \ matched no-enzyme/mock-purification\n    control is labeled for the bacterial\
    \ Figure 6 lanes; human BH110 controls are not transferred. Substrate\n    and\
    \ metal both differ between Mg/exonuclease and Ca/AP panels, so calcium alone\
    \ is not shown to switch\n    activity. Table S1 places THF after 12 bases while\
    \ the manuscript Figure 5 caption says position 12.\n    No cellular repair chain\
    \ or metal microstep is asserted.\n  nodes:\n  - node_id: tatd-calcium-thf-duplex-system\n\
    \    label: Untagged TatD preparation plus THF duplex and 5 mM CaCl2\n    node_type:\
    \ ACTIVITY\n    grounding:\n    - UniProtKB:P27859\n  - node_id: thf-incision-product\n\
    \    label: Discrete shorter labeled product from the internal-THF duplex\n  \
    \  node_type: STATE\n  edges:\n  - edge_id: tatd-thf-assay-produces-incision-product\n\
    \    subject: tatd-calcium-thf-duplex-system\n    predicate: produces\n    object:\
    \ thf-incision-product\n    mechanism: The TatD THF-duplex time course accumulates\
    \ the discrete product assigned to AP-site-analogue\n      incision. The complete\
    \ preparation and reaction are the observed cause; the graph does not promote\n\
    \      structural catalytic proposals or untested natural-AP activity to direct\
    \ observations.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:36881763\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC10085689/\n      snippet: robust AP\
    \ endo activity on dsDNA\n      explanation: Published Figure 6 bacterial Results\
    \ and nuclease Methods, checked against the visually\n        inspected author-manuscript\
    \ gel and Table S1, support this THF-duplex incision endpoint. Human\n       \
    \ and other bacterial paralog experiments are separate contexts.\n      cache_path:\
    \ evidence/PF01026/dorival-2023-tatD.txt\n      cache_sha256: fc60ebd8e94557fe95b9482cbb73c26c50ea336aae3b38c6983d6b9d5d6cdd70\n\
    - graph_id: tatd-deletion-chronic-peroxide-growth\n  title: Whole-gene TatD deletion\
    \ reduces colony growth under chronic peroxide\n  scope: E. coli K-12 WT and DeltaTatD\
    \ cells from the Keio collection; a whole-gene growth phenotype,\n    not direct\
    \ proof of a particular DNA-repair reaction.\n  context: Serial dilution spots\
    \ with chronic 1 mM H2O2, incubated overnight at 37 C in Figure 3B. Drug-free\n\
    \    spots are the unstressed comparator; separate MMS, MMC and UV-C tests do\
    \ not display the same defect.\n    Basal plate-medium details and exact deletion\
    \ stock identity remain unresolved.\n  family_mapping: K-12 tatD reference P27859/b4483/JW5931\
    \ contains PF01026 at 2-257, within 260 residues.\n    Deleting the gene perturbs\
    \ the whole protein; the tested stock's deletion boundaries are not independently\n\
    \    reconstructed.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:83333\n  limitations:\
    \ No genetic rescue is shown for this adopted comparison. Spot growth is not a\
    \ quantified\n    survival probability, and impaired peroxide growth does not\
    \ establish a direct nuclease-to-repair-to-survival\n    chain. Acute outgrowth\
    \ and the later three-paralog deletion are different experiments.\n  nodes:\n\
    \  - node_id: tatd-deletion-under-peroxide\n    label: DeltaTatD compared with\
    \ WT during chronic 1 mM H2O2 exposure\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:P27859\n  - node_id: peroxide-colony-growth\n    label: Colony\
    \ growth in the peroxide serial-spot assay\n    node_type: PHENOTYPE\n  edges:\n\
    \  - edge_id: tatd-deletion-decreases-peroxide-growth\n    subject: tatd-deletion-under-peroxide\n\
    \    predicate: decreases\n    object: peroxide-colony-growth\n    mechanism:\
    \ DeltaTatD spots grow less well than WT during chronic peroxide exposure. Whole-gene\
    \ dependence\n      is retained while the molecular cause of the growth defect\
    \ remains unresolved.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:25114049\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC4176340/\n      snippet: The TatD-knockout\
    \ strain was sensitive\n      explanation: Figure 3B and cell-survival Methods\
    \ establish the scoped chronic-peroxide phenotype.\n        Drug-free and alternative-stressor\
    \ comparisons limit generalization; no genetic rescue is shown\n        for the\
    \ adopted endpoint.\n      cache_path: evidence/PF01026/chen-2014-tatD.txt\n \
    \     cache_sha256: aff44a1ab44a7681a75281878d4bd1d8dc76d03cec37c4a09960084bd7d4618f\n\
    curation_events:\n- timestamp: '2026-10-11T08:27:31Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate four scoped TatD graphs with seven\
    \ observed biochemical or growth effects\n  history_record: history/records/PF01026/2026-10-11T082731Z-codex-4b2dfa.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: K-12 reference P27859 tatD/b4483/JW5931 has 260 residues, sequence version
    3, exact UniProt/InterPro sequence agreement and PF01026 at 2-257. All adopted
    substitution sites match the reference. K-12 donor, BL21 production hosts, 2014
    retained C-terminal tag and 2023 untagged preparation are distinguished; complete
    experimental clone sequences remain unverified.
  target_ids:
  - PF01026
  evidence_ids:
  - identity
  - primary
  - internal-thf-incision
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Joint biochemical systems are not split into independently sufficient enzyme,
    cofactor and substrate causes. Mutant effects concern measured digestion, not
    observed general-base or metal-coordination microsteps. The later THF-duplex endpoint
    is not natural-AP proof or a calcium-only switch. Whole-gene spot growth does
    not establish a direct nuclease-to-repair-to-survival chain.
  target_ids:
  - PF01026
  evidence_ids:
  - primary
  - native
  - internal-thf-incision
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Complete clones, mutant-panel concentrations, supplementary details and
    assay controls remain incomplete. The 2023 manuscript/Table S1 site-number discrepancy
    and the 2014 protease-K unit remain unresolved. Human proteins, other bacterial
    paralogs, additional damaged substrates, triple-deletion genetics and other family
    members require separate mapping and curation. Raw data were not independently
    reanalyzed.
  target_ids:
  - PF01026
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01026-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve TatD assay metadata and expand member-specific causal coverage
  description: Obtain complete constructs and mutant-panel methods, assess purification
    and rescue controls, resolve source discrepancies, and curate additional paralog
    or cellular contexts with their own primary evidence. Preserve substrate/cofactor
    distinctions and append a successor review before any status promotion.
  target_ids:
  - PF01026
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - internal-thf-incision
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01026.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Obtain complete constructs and mutant-panel methods, assess purification
    and rescue controls, resolve source discrepancies, and curate additional paralog
    or cellular contexts with their own primary evidence. Preserve substrate/cofactor
    distinctions and append a successor review before any status promotion.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01026
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Chen 2014 Figures 2, 3 and 5 were visually inspected. The Dorival author-manuscript
  Figure 6 and Table S1 were visually inspected and checked against published Methods
  and bacterial Results; the manuscript is not the publisher PDF. Other supplements,
  raw replicate gels, kinetic fits and atomic mechanisms were not independently reviewed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
