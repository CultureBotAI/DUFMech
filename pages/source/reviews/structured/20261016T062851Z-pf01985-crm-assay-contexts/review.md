# PF01985 CRM biochemical readouts and qualified bacterial phenotypes

- Review: 20261016T062851Z-pf01985-crm-assay-contexts
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-16T06:14:52Z
- Finished UTC: 2026-10-16T06:28:51Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Eight graphs retain twelve observed assay effects. Two biochemical condition/accessibility effects are DIRECT, five binding-readout mutation/deletion/reassociation effects UNRESOLVED, and five strain/preparation effects INDIRECT. No maturation rescue, atomic loop contact, pseudoknot or CRS1-alone splicing is asserted. Source/member coverage remains partial; IN_PROGRESS is preserved.

## Scope And Provenance

Review of all twelve newly adopted PF01985 relations, exact reference mappings, experimental alternatives and source preservation. Partial scientific coverage within the full-family and 8,296-record objective.

Selection: First PF01985 curation after a hidden/ignored-inclusive search of curation,evidence,history,reviews,reports,docs,.claude,.agents for PF01985/UPF0044/CRS1. The only existing match was the structural inventory. YbeY and YhbO leads were excluded as different proteins.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 47817e4326771c10d2fb909dd69cbbf41faad854.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01985 | data/families/PF01985.yaml | generated | PF01985 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| generation | passed | True | PF01985 | Baseline 8,296 valid records/zero drift. Dry run/apply changed only PF01985 and its ownership-manifest entry; a subsequent whole-corpus check had zero drift. |
| native | passed | True | PF01985 | Native record, history, retained-review and schema gates passed before saving this bundle. Actual REVIEW history and final regeneration are separate subsequent checks. |
| focused | passed | True | PF01985 | 56 tests passed in 111.50 seconds. These verify contracts, not biological truth. |
| derived | passed | True | PF01985 | 8,296-row inventory refreshed and checked: 936 graphs/2,006 edges in 134 families; 8,162 graphless. Only PF01985 export status changes. Counts denote structure, not completed scientific review. |
| integrity-preview | passed | True | PF01985 | All source snippets and cache hashes verified; reference motif and Pfam intervals checked; all 8,296 manifest entries valid; 8,295 other records, frozen sources, prior artifacts and canonical Pages unchanged. Exact preview JSON; 1440px/390px show eight graphs/twelve working disclosures, correct support/source links/qualifiers, no document overflow or JS errors. Six screenshots inspected. |
| publication-prerequisite | failed | False | PF01985 | After completed regeneration, exit1 reports changed data/families/PF01985.yaml. A preceding invocation completed against the old projection and is not treated as validation of the new bytes. |

## Scientific And Domain Assessments

### Former UPF0044 and exact member/reference scope

identity: supported. Targets: PF01985.

PF01985/IPR001890 and frozen former name are grounded. Reference mapping is distinct from physical constructs and from all-family functional transfer.

### Locus, culture and biochemical-addback distinctions

graph: supported. Targets: PF01985.

The original combined coding/promoter deletion is not presented as YhbY-specific necessity. Jiang cold growth is separated from uncertain-temperature profile preparations. Lysate co-IP restoration is not maturation rescue.

### Joint substitution and fitted binding readout

graph: supported. Targets: PF01985.

The mapped four-residue substitution raises apparent Kd in GST-CRM3; lower plateau, protein-folding and active-fraction alternatives remain. Individual-residue and full-length effects are not fabricated.

### Mature CRS1 cofactor, RNA deletion and accessibility readouts

graph: supported. Targets: PF01985.

All three RNA deletions retain separate substrate comparators and intron coordinates. Mg enhancement and radical protection are biochemical endpoints; contact assignments, compaction and proposed pseudoknot are not promoted to observed elementary mechanisms or splicing sufficiency.

### Maintained inputs, history and corpus preservation

provenance: supported. Targets: PF01985.

Only the new overlay/evidence/actual CREATE event own the scientific change. Frozen metadata, previous artifacts and 8,295 other projections remain unchanged; generated views reproduce through native tools.

### Remaining experimental and family-wide coverage

completeness: concern. Targets: PF01985.

Physical constructs, allele/promoter integrity, control temperature, folding controls and additional primary/member contexts remain open. Current qualifiers keep adopted edges bounded but do not finish the family.

## Findings

### bacterial-controls: Resolve bacterial allele and culture-control attribution

minor / open / confirmed; issue key: pf01985-bacterial-controls.

Authenticate promoter-sparing deletion/rescue, identify Barkan panel-specific strains and addback conditions, and resolve Jiang Figure6 BW25113 culture temperature. Current locus/preparation scopes prevent a false YhbY-only mechanism but leave that biological question open.

### construct-and-folding-controls: Authenticate constructs and distinguish contact loss from conformational effects

minor / open / confirmed; issue key: pf01985-construct-and-folding-controls.

Verify complete GST-CRM3 inserts and folding/active fractions, mature-CRS1 stoichiometry at assay concentration, RNA-deletion structural controls and raw footprint coverage. Partial primer matches and reference GRRG mapping are not physical clone authentication.

### primary-and-member-coverage: Extend original genetics and other CRM-family primary contexts

minor / open / confirmed; issue key: pf01985-primary-and-member-coverage.

Inspect Till2001, CAF1/CAF2, CFM2, original bacterial structures, archaeal/newer-member evidence and relevant supplements. Current three-study curation cannot stand for the complete family or all8,296records.

## Recommended Actions And Acceptance Checks

### extend-crm-evidence

Resolve named experimental ambiguities and extend primary/member coverage in evidence-backed successor curation while preserving current assay boundaries.

- Document physical alleles and neighboring-promoter integrity or retain the combined-locus interpretation.
- Resolve the Figure6 WT temperature explicitly before asserting a genotype-only profile effect.
- Authenticate clone boundaries and use discriminating folding/active-fraction controls before assigning atomic contact causality.
- Keep RNA accessibility, direct contact, folding, in-vivo requirement and in-vitro sufficiency separate.
- Inspect additional primary Methods/figures and exact member mappings; retain inaccessible/unperformed coverage honestly.
- Append successor reviews/history, preserve stable graph IDs and pass native evidence/generation checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | evidence/PF01985/identity-and-coordinates.txt; Frozen previous-name row; downloaded UniProt/InterPro JSON and AF290414.1 EMBL with SHA256; Biopython CDS translation and exact primer-flank matching. | supports | P0AGK4 maps PF01985 at3-86; Q9FYT6 maps170-254,352-436,564-651. AF290414.1 yields the exact715aa sequence; GRRG586-589 lies in CRM3. Full experimental inserts and strain alleles remain unauthenticated. |
| barkan | https://pmc.ncbi.nlm.nih.gov/articles/PMC1705760/; Results, cloning/filter-binding/strain/gradient/IP Methods; Fig4A,5,8 captions and image inspection; evidence/PF01985/barkan-2007-contexts.txt. | supports | Joint-mutant apparent Kd, locus-deletion sedimentation endpoints and recombinant lysate co-IP are supported as separate observations. Promoter confound, different binding plateaus and absent profile rescue constrain interpretation. |
| jiang | https://pmc.ncbi.nlm.nih.gov/articles/PMC1855874/; Table1, culture/growth/gradient/quantification Methods, Results, Fig5/6 captions and images; evidence/PF01985/jiang-2007-contexts.txt. | supports | Matched cold plating supports the colony phenotype. Relative peak ratios support a preparation comparison, with explicit unresolved BW25113 culture temperature and unverified allele/promoter boundaries. |
| osters | https://pmc.ncbi.nlm.nih.gov/articles/PMC544502/; Previously obtained ordinary HTML Results/Methods, Fig1/2/5-8 captions and images2/5-8; evidence/PF01985/osters-2005-contexts.txt. | supports | Mature CRS1 Mg-dependent RNA retention, three distinct RNA deletion readouts and reduced hydroxyl-radical accessibility are supported. RNA-folding alternatives, unequal plateaus and the reported lack of detected CRS1-promoted splicing remain explicit. |
| coverage | evidence/PF01985/coverage-and-gaps.txt; Named omissions, primary-access outcomes, construct/control gaps and excluded causal leaps. | supports | Partial source/member coverage is not a negative biological result. No family-wide pathway or completion claim is justified. |
| validation | data/families/PF01985.yaml; Native generation, schema/history/review checks,56focused tests, inventory/exports, integrity checks and local desktop/mobile preview. | supports | Representation and source preservation are verified separately from mechanistic completeness and canonical publication. |
| duf-projection-pf01985 | data/families/PF01985.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Same-agent scientific self-review, not independent approval or experimental replication. Completed refers to this scoped review, not full-family completion.
- All twelve edges describe observed assay effects, not twelve independent mechanistic discoveries. Only two are direct biochemical endpoints; five have unresolved molecular explanation and five are indirect strain/preparation phenotypes.
- No raw data re-quantification, independent clone sequencing, exact genomic allele reconstruction or comprehensive new-literature search was performed.
- The Barkan external supplement and additional primary studies remain uninspected. Failed XML/PDF requests were not treated as negative results. The later web-tool Ostersetzer request hit a browser challenge; previously obtained ordinary HTML/figures were used without bypassing it.
- Full articles and copyrighted figures remain in temporary research storage; only brief attributed extracts, factual assay summaries and source hashes are retained in the repository.
- The local preview renders the curated record only and does not claim refreshed frozen member tracks or canonical published Pages. No commit, push, PR or source checkpoint was created this turn.
- A final actual REVIEW history event, regeneration and revalidation follow saving. The 8,296-family goal remains active; structural graph presence is not scientific completion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 47817e4326771c10d2fb909dd69cbbf41faad854
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01985.yaml
    sha256: 909e78593472abb5440f123ab92dc06ee4078558f7e9136cd1716f69decf55ec
    role: context
  - path: data/families/PF01985.yaml
    sha256: 9a557e43079c3be7d373e23d280db81e09948c462e6fe728a796d18153423558
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
  - path: data/worklists/pfam-previous-unknown-names-2026-10-10.json
    role: context
    sha256: a9f70f265bfe7039f5abf8e8a4545f389b66636edaf8e102c7e1a08ca1c1c10e
  - path: evidence/PF01985/barkan-2007-contexts.txt
    role: context
    sha256: 4367c213be7fe19c440de1e422a6371e42fc3049abf674874e75bf56cb2c4675
  - path: evidence/PF01985/coverage-and-gaps.txt
    role: context
    sha256: f1b7f87ed49a0b9a8aceb8fab137947a895c7787b6c9f7fec79b1fcd2541547c
  - path: evidence/PF01985/identity-and-coordinates.txt
    role: context
    sha256: 0b9dc67414bd4ead95cb6ee9c7d0d8fc4707f7b4c10be24a584a28cb32eae36f
  - path: evidence/PF01985/jiang-2007-contexts.txt
    role: context
    sha256: 29c25f7d3274371c2f6ea0d181796fffd8cb98df9b4a7ffc012e6d7c7b9ccec7
  - path: evidence/PF01985/osters-2005-contexts.txt
    role: context
    sha256: 8ef51c123199bdb609c838a7ae8741d42faca54ad5991b3ffe0c556b1b1a7048
  - path: history/records/PF01985/2026-10-16T061452Z-codex-503ce3.yaml
    role: context
    sha256: aad0aa8d1747c0dfbfcdce49d28cb2816a611f041ee350c468ce8d4f8a942091
  - path: reports/causal_graphs/inventory.json
    role: context
    sha256: 50245ce60735b41eb56b08e9842dd50b845241b9b6e8b6173aa4be9da8735596
  - path: src/dufmech/schema/dufmech.yaml
    role: context
    sha256: 5ca9b9cd1fdefdbe8066b08c319b5144a5f2631710f2271e84dc346283b608e9
targets:
- target_id: PF01985
  path: data/families/PF01985.yaml
  label: PF01985
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01985.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 67cfc3df0c542082471839e3eae79cfd47eaa5a05c2b10fc525d46ed80df2065
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
schema_version: 1.0.0
review_id: 20261016T062851Z-pf01985-crm-assay-contexts
title: PF01985 CRM biochemical readouts and qualified bacterial phenotypes
started_at: '2026-10-16T06:14:52Z'
finished_at: '2026-10-16T06:28:51Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Author scientific self-review against three primary papers,
    their Methods/captions, ten figure images and parsed reference records; not independent
    approval or replication.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: true
summary: Eight graphs retain twelve observed assay effects. Two biochemical condition/accessibility
  effects are DIRECT, five binding-readout mutation/deletion/reassociation effects
  UNRESOLVED, and five strain/preparation effects INDIRECT. No maturation rescue,
  atomic loop contact, pseudoknot or CRS1-alone splicing is asserted. Source/member
  coverage remains partial; IN_PROGRESS is preserved.
scope:
  description: Review of all twelve newly adopted PF01985 relations, exact reference
    mappings, experimental alternatives and source preservation. Partial scientific
    coverage within the full-family and 8,296-record objective.
  selection: First PF01985 curation after a hidden/ignored-inclusive search of curation,evidence,history,reviews,reports,docs,.claude,.agents
    for PF01985/UPF0044/CRS1. The only existing match was the structural inventory.
    YbeY and YhbO leads were excluded as different proteins.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01985
  exclusions:
  - target: All family members and additional primary studies/supplements
    reason: Original CRS1 genetics, CAF1/CAF2, CFM2, bacterial structures, archaeal/newer
      contexts and the external Barkan supplement are not fully inspected.
  - target: Gene-only maturation, atomic contacts and in-vitro splicing sufficiency
    reason: Promoter/culture/construct/folding confounds and unmeasured intermediates
      prevent these stronger conclusions.
  - target: Canonical Pages publication and full release QC
    reason: This local curation has no new authorized source checkpoint. The changed-record
      source-pin failure is reproduced, not bypassed.
checks:
- check_id: generation
  name: generation
  command: just records-check; just records; just records --apply
  status: passed
  required: true
  exit_code: 0
  summary: Baseline 8,296 valid records/zero drift. Dry run/apply changed only PF01985
    and its ownership-manifest entry; a subsequent whole-corpus check had zero drift.
  target_ids:
  - PF01985
  evidence_ids:
  - validation
- check_id: native
  name: native
  command: just validate-all validate-schema
  status: passed
  required: true
  exit_code: 0
  summary: Native record, history, retained-review and schema gates passed before
    saving this bundle. Actual REVIEW history and final regeneration are separate
    subsequent checks.
  target_ids:
  - PF01985
  evidence_ids:
  - validation
- check_id: focused
  name: focused
  command: uv run --locked pytest -q tests/test_causal_graphs.py tests/test_qc.py
    tests/test_record_review_contract.py
  status: passed
  required: true
  exit_code: 0
  summary: 56 tests passed in 111.50 seconds. These verify contracts, not biological
    truth.
  target_ids:
  - PF01985
  evidence_ids:
  - validation
- check_id: derived
  name: derived
  command: just causal-graphs --apply; just causal-graphs --check; just exports --apply;
    just exports --check
  status: passed
  required: true
  exit_code: 0
  summary: '8,296-row inventory refreshed and checked: 936 graphs/2,006 edges in 134
    families; 8,162 graphless. Only PF01985 export status changes. Counts denote structure,
    not completed scientific review.'
  target_ids:
  - PF01985
  evidence_ids:
  - validation
- check_id: integrity-preview
  name: integrity-preview
  command: uv run --locked python /private/tmp/duf-pf01985-20261016-uyyvlg/verify_preview.py;
    node /private/tmp/duf-pf01985-20261016-uyyvlg/browser.cjs
  status: passed
  required: true
  exit_code: 0
  summary: All source snippets and cache hashes verified; reference motif and Pfam
    intervals checked; all 8,296 manifest entries valid; 8,295 other records, frozen
    sources, prior artifacts and canonical Pages unchanged. Exact preview JSON; 1440px/390px
    show eight graphs/twelve working disclosures, correct support/source links/qualifiers,
    no document overflow or JS errors. Six screenshots inspected.
  target_ids:
  - PF01985
  evidence_ids:
  - validation
- check_id: publication-prerequisite
  name: publication-prerequisite
  command: uv run --locked python -m dufmech.site_sources check
  status: failed
  required: false
  exit_code: 1
  summary: After completed regeneration, exit1 reports changed data/families/PF01985.yaml.
    A preceding invocation completed against the old projection and is not treated
    as validation of the new bytes.
  target_ids:
  - PF01985
  evidence_ids:
  - validation
evidence:
- evidence_id: identity
  kind: primary_source
  reference: evidence/PF01985/identity-and-coordinates.txt
  locator: Frozen previous-name row; downloaded UniProt/InterPro JSON and AF290414.1
    EMBL with SHA256; Biopython CDS translation and exact primer-flank matching.
  accessed_at: '2026-10-16T06:28:51Z'
  support: supports
  summary: P0AGK4 maps PF01985 at3-86; Q9FYT6 maps170-254,352-436,564-651. AF290414.1
    yields the exact715aa sequence; GRRG586-589 lies in CRM3. Full experimental inserts
    and strain alleles remain unauthenticated.
- evidence_id: barkan
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1705760/
  locator: Results, cloning/filter-binding/strain/gradient/IP Methods; Fig4A,5,8 captions
    and image inspection; evidence/PF01985/barkan-2007-contexts.txt.
  accessed_at: '2026-10-16T06:28:51Z'
  support: supports
  summary: Joint-mutant apparent Kd, locus-deletion sedimentation endpoints and recombinant
    lysate co-IP are supported as separate observations. Promoter confound, different
    binding plateaus and absent profile rescue constrain interpretation.
- evidence_id: jiang
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1855874/
  locator: Table1, culture/growth/gradient/quantification Methods, Results, Fig5/6
    captions and images; evidence/PF01985/jiang-2007-contexts.txt.
  accessed_at: '2026-10-16T06:28:51Z'
  support: supports
  summary: Matched cold plating supports the colony phenotype. Relative peak ratios
    support a preparation comparison, with explicit unresolved BW25113 culture temperature
    and unverified allele/promoter boundaries.
- evidence_id: osters
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC544502/
  locator: Previously obtained ordinary HTML Results/Methods, Fig1/2/5-8 captions
    and images2/5-8; evidence/PF01985/osters-2005-contexts.txt.
  accessed_at: '2026-10-16T06:28:51Z'
  support: supports
  summary: Mature CRS1 Mg-dependent RNA retention, three distinct RNA deletion readouts
    and reduced hydroxyl-radical accessibility are supported. RNA-folding alternatives,
    unequal plateaus and the reported lack of detected CRS1-promoted splicing remain
    explicit.
- evidence_id: coverage
  kind: record_content
  reference: evidence/PF01985/coverage-and-gaps.txt
  locator: Named omissions, primary-access outcomes, construct/control gaps and excluded
    causal leaps.
  accessed_at: '2026-10-16T06:28:51Z'
  support: supports
  summary: Partial source/member coverage is not a negative biological result. No
    family-wide pathway or completion claim is justified.
- evidence_id: validation
  kind: validation
  reference: data/families/PF01985.yaml
  locator: Native generation, schema/history/review checks,56focused tests, inventory/exports,
    integrity checks and local desktop/mobile preview.
  accessed_at: '2026-10-16T06:28:51Z'
  support: supports
  summary: Representation and source preservation are verified separately from mechanistic
    completeness and canonical publication.
- evidence_id: duf-projection-pf01985
  kind: record_content
  reference: data/families/PF01985.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-16T06:28:51Z'
  support: context_only
  snapshot_sha256: 9a557e43079c3be7d373e23d280db81e09948c462e6fe728a796d18153423558
  quote: "id: Pfam:PF01985\npfam_id: PF01985\nname: CRS1 / YhbY (CRM) domain\nshort_name:\
    \ CRS1_YhbY\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01985\n\
    counters:\n  proteins: 15752\n  matches: 23182\n  proteomes: 8486\n  taxa: 12703\n\
    \  structures: 6\n  alphafold_models: 11674\n  domain_architectures: 130\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR001890\ndescription: Escherichia coli YhbY is associated\
    \ with pre-50S ribosomal subunits, which implies a function\n  in ribosome assembly.\
    \ GFP fused to a single-domain CRM protein from maize localises to the nucleolus,\n\
    \  suggesting that an analogous activity may have been retained in plants [[cite:PUB00043747]].\
    \ A CRM domain\n  containing protein in plant chloroplasts has been shown to function\
    \ in group I and II intron splicing\n  [[cite:PUB00044700]]. In vitro experiments\
    \ with an isolated maize CRM domain have shown it to have RNA\n  binding activity.\
    \ These and other results suggest that the CRM domain evolved in the context of\
    \ ribosome\n  function prior to the divergence of Archaea and Bacteria, that this\
    \ function has been maintained in\n  extant prokaryotes, and that the domain was\
    \ recruited to serve as an RNA binding module during the evolution\n  of plant\
    \ genomes [[cite:PUB00043747]]. YhbY has a fold similar to that of the C-terminal\
    \ domain of translation\n  initiation factor 3 (IF3C), which binds to 16S rRNA\
    \ in the 30S ribosome [[cite:PUB00019352]][[cite:PUB00019353]].\ncuration_history:\
    \ history/records/PF01985\ndiscussions:\n- discussion_id: pf01985-bacterial-allele-and-preparation-controls\n\
    \  prompt: Resolve deletion alleles, neighboring-promoter effects and culture\
    \ matching before assigning\n    a YhbY-specific maturation mechanism.\n  kind:\
    \ CURATION_TODO\n  status: OPEN\n  rationale: The original deletion also removes\
    \ an rrmJ promoter region; the later preparation comparison\n    does not explicitly\
    \ resolve control growth temperature.\n  evidence:\n  - reference: PMID:17105995\n\
    \    supports: PARTIAL\n    evidence_source: primary_results_methods_and_figures\n\
    \    explanation: Figure5 supports a locus-deletion phenotype, while Figure4A\
    \ addback restores co-IP rather\n      than ribosome maturation.\n  - reference:\
    \ PMID:17337586\n    supports: PARTIAL\n    evidence_source: primary_methods_table1_and_figures5_6\n\
    \    explanation: JM4690 has a cold-growth phenotype; Figure6 peak ratios are\
    \ relative readouts with unresolved\n      BW25113 culture-temperature matching.\n\
    \  posed_by: Codex\n  posed_date: '2026-10-16'\n  notes: evidence/PF01985/coverage-and-gaps.txt\
    \ retains exact allele, panel-strain, promoter-sparing rescue\n    and addback-dose\
    \ follow-ups. Do not conflate YhbY with YbeY or YhbO.\n- discussion_id: pf01985-crm-constructs-and-family-coverage\n\
    \  prompt: Authenticate CRM constructs and extend primary-source coverage before\
    \ connecting binding, folding\n    and in-vivo splicing.\n  kind: CURATION_TODO\n\
    \  status: OPEN\n  rationale: Joint CRM3 substitutions and RNA deletions do not\
    \ isolate atomic contacts; multivalent mature\n    CRS1 and isolated GST-CRM3\
    \ are different reagents.\n  evidence:\n  - reference: PMID:17105995\n    supports:\
    \ PARTIAL\n    evidence_source: primary_figure8_and_cloning_methods\n    explanation:\
    \ The mutant has a higher apparent Kd and lower plateau, without demonstrated\
    \ fold preservation;\n      reference GRRG586-589 mapping is not physical-insert\
    \ authentication.\n  - reference: PMID:15598799\n    supports: PARTIAL\n    evidence_source:\
    \ primary_results_methods_and_figures2_5_6_7_8\n    explanation: RNA retention\
    \ and accessibility change, but RNA-deletion folding alternatives and missing\n\
    \      CRS1-alone splicing remain explicit.\n  posed_by: Codex\n  posed_date:\
    \ '2026-10-16'\n  notes: Original CRS1 genetics, CAF1/CAF2, CFM2, bacterial structures,\
    \ archaeal contexts, newer studies\n    and supplements remain incomplete. See\
    \ identity-and-coordinates.txt and coverage-and-gaps.txt; no\n    full-family\
    \ scientific approval.\ncausal_graphs:\n- graph_id: maize-crm3-joint-loop-substitution-2007\n\
    \  title: Joint CRM3 loop substitution raises the apparent RNA-binding Kd\n  scope:\
    \ Barkan2007 Figure8; isolated maize CRS1 third CRM domain fused to GST, WT versus\
    \ joint GxxG-to-AAAA\n    substitution.\n  context: Complete atpF intron plus22/24nt\
    \ exon flanks,25pM RNA;0-1uM protein,15min25C,10mMTris pH7,150mMKOAc,10mMMgOAc,5mMDTT,10ug/mLBSA,1U/uL\n\
    \    RNase inhibitor. Stacked nitrocellulose/nylon; GST control; nine experiments/four\
    \ preparations,SD.\n  family_mapping: Q9FYT6 sequence1,715aa,PF01985 matches170-254,352-436,564-651.\
    \ AF290414.1 translation\n    matches exactly; reference GRRG586-589 and mutagenic-primer\
    \ flanks ground the joint substitution inside\n    CRM3. Complete fusion boundaries\
    \ are not authenticated.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:4577\n\
    \  limitations: Single-site fits allow different maxima; the mutant also has a\
    \ lower plateau. Folding,\n    active fraction and filter behavior are not independently\
    \ excluded. No individual-residue necessity,\n    atomic contact mechanism, native\
    \ full-length CRS1 effect or splicing effect is asserted.\n  nodes:\n  - node_id:\
    \ joint-aaaa\n    label: Replace GST-CRM3 WT by joint GRRG586-589-to-AAAA mutant\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q9FYT6\n  - node_id:\
    \ apparent-kd\n    label: Fitted apparent atpF RNA-binding Kd\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: aaaa-raises-apparent-kd\n    subject: joint-aaaa\n\
    \    predicate: increases\n    object: apparent-kd\n    mechanism: The joint-mutant\
    \ preparation shifts the fitted apparent Kd from21.4+/-4.3 to79.3+/-14.4nM.\n\
    \      This is a binding-readout effect; the molecular cause of the changed curve\
    \ and plateau remains unresolved.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:17105995\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC1705760/\n      snippet:\
    \ RNA binding activity\n      explanation: Figure8 curve/caption and filter-binding/cloning\
    \ Methods; WT, mutant and GST were compared,\n        but the authors' expected\
    \ fold preservation is not a measured control.\n      cache_path: evidence/PF01985/barkan-2007-contexts.txt\n\
    \      cache_sha256: 4367c213be7fe19c440de1e422a6371e42fc3049abf674874e75bf56cb2c4675\n\
    - graph_id: ecoli-yhby-locus-deletion-profile-2007\n  title: Original yhbY-region\
    \ deletion changes pre50S and mature50S profiles\n  scope: Barkan2007 Figure5;\
    \ original locus deletion versus its progenitor, not a promoter-sparing YhbY\n\
    \    knockout.\n  context: EMG2 and K38 deletions are listed; panel-specific strain\
    \ remains unresolved. Internal yhbY\n    codons removed, start/stop retained.\
    \ LB37C,OD6000.4;10-40%sucrose dissociating gradient,20mMTris pH7.8,1mMMgCl2,100mMNH4Cl,35krpm7h.\n\
    \  family_mapping: E.coli K12 reference P0AGK4 sequence1,97aa,PF01985 match3-86.\
    \ Reference mapping does\n    not authenticate the experimental strain allele.\
    \ The perturbation also removes the -35 region of an\n    upstream rrmJ promoter\
    \ within yhbY.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:83333\n  limitations:\
    \ These are relative sedimentation-profile effects, not absolute particles per\
    \ cell or a\n    YhbY-only causal mechanism. RrmJ abundance and incomplete plasmid\
    \ rescue are reported without displayed\n    data. Recombinant YhbY added before\
    \ sedimentation does not restore the A260 profile.\n  nodes:\n  - node_id: combined-locus-deletion\n\
    \    label: Delete internal yhbY coding region and overlapping rrmJ promoter segment\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:P0AGK4\n  - node_id:\
    \ pre50s-peak\n    label: Relative pre50S sedimentation peak\n    node_type: PHENOTYPE\n\
    \  - node_id: mature50s-peak\n    label: Relative mature50S sedimentation peak\n\
    \    node_type: PHENOTYPE\n  edges:\n  - edge_id: locus-deletion-raises-pre50s\n\
    \    subject: combined-locus-deletion\n    predicate: increases\n    object: pre50s-peak\n\
    \    mechanism: The locus-deletion preparation has a larger precursor-particle\
    \ peak than its progenitor.\n      Loss of YhbY, altered neighboring expression\
    \ and their combination are not separated by this experiment.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:17105995\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC1705760/\n\
    \      snippet: increased levels\n      explanation: Figure5 profile and the adjoining\
    \ Results paragraph explicitly state the rrmJ-promoter\n        confound; the\
    \ graph retains the combined perturbation.\n      cache_path: evidence/PF01985/barkan-2007-contexts.txt\n\
    \      cache_sha256: 4367c213be7fe19c440de1e422a6371e42fc3049abf674874e75bf56cb2c4675\n\
    \  - edge_id: locus-deletion-lowers-mature50s\n    subject: combined-locus-deletion\n\
    \    predicate: decreases\n    object: mature50s-peak\n    mechanism: The same\
    \ locus-deletion comparison has a smaller mature50S peak. It does not identify\
    \ an\n      elementary YhbY-catalyzed processing step or prove domain-specific\
    \ necessity.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:17105995\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC1705760/\n      snippet: reduced levels\n\
    \      explanation: Figure5 and Results; this second endpoint belongs to the same\
    \ preparation comparison,\n        not an independent mechanistic discovery.\n\
    \      cache_path: evidence/PF01985/barkan-2007-contexts.txt\n      cache_sha256:\
    \ 4367c213be7fe19c440de1e422a6371e42fc3049abf674874e75bf56cb2c4675\n- graph_id:\
    \ ecoli-yhby-lysate-reassociation-2007\n  title: Recombinant YhbY addback restores\
    \ antibody-pellet 23S recovery\n  scope: Barkan2007 Figure4A; biochemical addition\
    \ to deletion lysate, not living-cell complementation\n    or maturation rescue.\n\
    \  context: E.coli deletion lysate plus recombinant full-length YhbY and affinity-purified\
    \ anti-YhbY antibody;\n    slot-blot23S hybridization of equal pellet/supernatant\
    \ proportions. WT, deletion and no-antibody controls;\n    four reported repetitions\
    \ with different extracts. Addback dose/incubation and panel-specific EMG2/K38\n\
    \    attribution remain unresolved.\n  family_mapping: P0AGK4 sequence1,97aa,PF01985\
    \ match3-86 grounds the E.coli reference. Recombinant protein\n    was expressed\
    \ from pET28; exact physical insert/tag residues are not independently authenticated.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:83333\n  limitations: Whole lysate\
    \ contains RNP partners. Increased co-IP does not prove direct YhbY-RNA contact,\n\
    \    de-novo ribosome assembly or correction of the deletion phenotype. Figure5\
    \ addback leaves the sedimentation\n    profile unchanged.\n  nodes:\n  - node_id:\
    \ ryhby-addition\n    label: Add recombinant YhbY to deletion lysate with anti-YhbY\
    \ antibody\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:P0AGK4\n\
    \  - node_id: pellet-23s\n    label: 23S RNA recovered in the antibody pellet\n\
    \    node_type: STATE\n  edges:\n  - edge_id: ryhby-increases-23s-recovery\n \
    \   subject: ryhby-addition\n    predicate: increases\n    object: pellet-23s\n\
    \    mechanism: Recombinant-protein addition restores antibody-mediated recovery\
    \ of23S-containing particles\n      from the deletion extract. The observed association-readout\
    \ effect leaves direct contact and intervening\n      RNP components unresolved.\n\
    \    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:17105995\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC1705760/\n\
    \      snippet: reconstituted\n      explanation: Figure4A lanes/caption and immunoprecipitation\
    \ Methods; recovery is the measured endpoint,\n        not a claim of restored50S\
    \ maturation.\n      cache_path: evidence/PF01985/barkan-2007-contexts.txt\n \
    \     cache_sha256: 4367c213be7fe19c440de1e422a6371e42fc3049abf674874e75bf56cb2c4675\n\
    - graph_id: ecoli-jm4690-cold-growth-2007\n  title: JM4690 yhbY-deletion strain\
    \ has reduced colony growth at18C\n  scope: Jiang2007 Figure5; Keio-derived JM4690\
    \ versus isogenic BW25113 under matched18C plating conditions.\n  context: Two\
    \ overnight cultures per strain,37C regrowth,OD6000.15, four tenfold serial dilutions,5uL\n\
    \    duplicate LB spots;18C three days in Figure5,37C overnight comparison. Methods\
    \ permits3-5days for\n    cold incubation.\n  family_mapping: P0AGK4 sequence1\
    \ is the97aa E.coli K12 YhbY reference with PF01985 at3-86. Table1 identifies\n\
    \    JM4690 as the deletion strain; it is not the SPA-tagged JM4199 association\
    \ construct.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:83333\n  limitations:\
    \ Colony spot growth is not a quantitative instantaneous growth rate. Exact deletion/promoter\n\
    \    boundaries and a target-specific rescue are not established in the inspected\
    \ material; do not assume\n    the neighboring rrmJ-promoter concern is excluded\
    \ for this allele.\n  nodes:\n  - node_id: jm4690-line\n    label: Use JM4690\
    \ deletion strain rather than BW25113\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:P0AGK4\n  - node_id: cold-colony-growth\n    label: Colony growth\
    \ in equal serial spots after18C incubation\n    node_type: PHENOTYPE\n  edges:\n\
    \  - edge_id: jm4690-lowers-cold-growth\n    subject: jm4690-line\n    predicate:\
    \ decreases\n    object: cold-colony-growth\n    mechanism: Under matched cold\
    \ plating conditions, JM4690 gives weaker colony growth than BW25113.\n      This\
    \ indirect strain phenotype does not resolve a YhbY-domain-dependent ribosome\
    \ assembly pathway.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:17337586\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC1855874/\n      snippet: impaired in\
    \ the cold\n      explanation: Figure5 spots/caption, Table1 and growth Methods\
    \ distinguish the cold phenotype from\n        the separately prepared Figure6\
    \ lysates.\n      cache_path: evidence/PF01985/jiang-2007-contexts.txt\n     \
    \ cache_sha256: 29c25f7d3274371c2f6ea0d181796fffd8cb98df9b4a7ffc012e6d7c7b9ccec7\n\
    - graph_id: ecoli-jm4690-profile-preparations-2007\n  title: Reported JM4690 preparation\
    \ has higher free-subunit-to70S peak ratios\n  scope: Jiang2007 Figure6; composite\
    \ strain/culture-preparation comparison, not an isolated gene or temperature\n\
    \    intervention.\n  context: Methods assigns deletion strains18C and remaining\
    \ strains37C; the Figure6 BW25113 culture temperature\n    is not explicitly resolved.\
    \ HarvestOD6000.4-0.8;7-47%sucrose,10mMTris pH7.5,10mMMgCl2,100mMNH4Cl,13OD260\n\
    \    units,41krpm3h;A254 peak heights above post70S trough. At least three independent\
    \ profiles;SEM.\n  family_mapping: JM4690 deletion is linked to E.coli K12 YhbY\
    \ reference P0AGK4 sequence1,PF01985 match3-86;\n    physical allele and promoter\
    \ integrity are not authenticated by this mapping.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:83333\n  limitations: Unresolved temperature matching precludes\
    \ attributing the comparison solely to genotype.\n    Ratios are peak heights,\
    \ not areas, absolute subunit abundance, processing rates or particles per\n \
    \   cell. No promoter-sparing rescue establishes a YhbY-specific mechanism.\n\
    \  nodes:\n  - node_id: jm4690-preparation\n    label: Use reported JM4690 preparation\
    \ instead of reported BW25113 preparation\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:P0AGK4\n  - node_id: ratio30s70s\n    label: 30S-to70S A254 peak-height\
    \ ratio\n    node_type: PHENOTYPE\n  - node_id: ratio50s70s\n    label: 50S-to70S\
    \ A254 peak-height ratio\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: preparation-raises-30s70s\n\
    \    subject: jm4690-preparation\n    predicate: increases\n    object: ratio30s70s\n\
    \    mechanism: The reported mutant preparation has a larger30S/70S ratio. Genotype\
    \ and potentially different\n      culture temperature are not separated; no single\
    \ causal component is assigned.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:17337586\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC1855874/\n      snippet:\
    \ relative peak height ratios\n      explanation: Figure6A/B dark-gray series,\
    \ its caption and quantification Methods; cell-preparation\n        Methods impose\
    \ the explicit temperature-matching limitation.\n      cache_path: evidence/PF01985/jiang-2007-contexts.txt\n\
    \      cache_sha256: 29c25f7d3274371c2f6ea0d181796fffd8cb98df9b4a7ffc012e6d7c7b9ccec7\n\
    \  - edge_id: preparation-raises-50s70s\n    subject: jm4690-preparation\n   \
    \ predicate: increases\n    object: ratio50s70s\n    mechanism: The same preparation\
    \ comparison has a larger50S/70S ratio. This second endpoint is not\n      independent\
    \ proof of defective50S maturation or an absolute increase in50S particles.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:17337586\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC1855874/\n\
    \      snippet: relative peak height ratios\n      explanation: Figure6B light-gray\
    \ series and Methods; retain the composite preparation scope and\n        shared70S\
    \ denominator.\n      cache_path: evidence/PF01985/jiang-2007-contexts.txt\n \
    \     cache_sha256: 29c25f7d3274371c2f6ea0d181796fffd8cb98df9b4a7ffc012e6d7c7b9ccec7\n\
    - graph_id: maize-mcrs1-magnesium-retention-2005\n  title: MgCl2 increase enhances\
    \ RNA retention with mature CRS1\n  scope: Ostersetzer2005 Figure2B;0-to10mM MgCl2\
    \ range in a purified mature CRS1/atpF RNA binding assay.\n  context: 2.5nM mature\
    \ CRS1 monomer units,25pM atpF RNA,150mMKOAc,50mMTris pH7,5mMDTT,10ug/mLBSA,0.5U/uL\n\
    \    RNase inhibitor;15min25C; stacked nitrocellulose/nylon retention. Four experiments,SD;\
    \ protein and\n    RNA are both present.\n  family_mapping: Q9FYT6 sequence1,715aa,PF01985\
    \ matches170-254,352-436,564-651. Recombinant mature protein\n    starts at40;\
    \ GST removed, C-terminalHis6 retained. All three CRM domains remain, not isolated\
    \ CRM3.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:4577\n  limitations:\
    \ DIRECT denotes the measured biochemical condition effect, not a proven Mg-binding\
    \ site\n    or atomic folding mechanism. Retention plateaus around10-20mM; no\
    \ monotonic extrapolation beyond the\n    chosen range. This is not Mg-alone RNA\
    \ binding or evidence of splicing.\n  nodes:\n  - node_id: magnesium-increase\n\
    \    label: Raise MgCl2 from0 to10mM with fixed mature CRS1 and RNA\n    node_type:\
    \ PERTURBATION\n  - node_id: retained-rna\n    label: Fraction of atpF RNA retained\
    \ with protein\n    node_type: STATE\n  edges:\n  - edge_id: magnesium-increases-retention\n\
    \    subject: magnesium-increase\n    predicate: increases\n    object: retained-rna\n\
    \    mechanism: Raising MgCl2 over the stated range increases the nitrocellulose-retained\
    \ RNA fraction\n      with fixed protein/RNA inputs. RNA conformation, ionic effects\
    \ and protein interactions are not\n      separately resolved.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:15598799\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC544502/\n\
    \      snippet: increasing\n      explanation: Figure2B curve/caption and binding\
    \ Methods establish the conditional direction and\n        plateau; the graph\
    \ does not assert an intrinsic affinity constant for all preparations.\n     \
    \ cache_path: evidence/PF01985/osters-2005-contexts.txt\n      cache_sha256: 8ef51c123199bdb609c838a7ae8741d42faca54ad5991b3ffe0c556b1b1a7048\n\
    - graph_id: maize-mcrs1-rna-deletions-2005\n  title: Separate atpF RNA deletions\
    \ reduce mature CRS1 binding readouts\n  scope: Ostersetzer2005 Figures5A and8A/B;\
    \ three separate RNA-fragment perturbations, not sequential\n    edits or protein\
    \ mutations.\n  context: Purified mature CRS1,25pM RNA,150mMKOAc,10mMMgCl2,50mMTris\
    \ pH7,50ug/mL tRNA,15min25C. D1 comparison\n    at2.5nMCRS1 in Figure5A; D4/111nt\
    \ titrations through50nM in Figure8, at least three experiments. Figure8\n   \
    \ fractions normalize to intact-fragment saturation near80%.\n  family_mapping:\
    \ Q9FYT6 sequence1 with PF01985 matches170-254,352-436,564-651; mature40-715 reference\n\
    \    region, cleaved GST and retainedHis6. RNA coordinates are published intron-relative\
    \ nucleotides, not\n    protein residues or independently verified genome coordinates.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:4577\n  limitations: Loss of retention\
    \ can reflect altered RNA structure or active fraction as well as contact-site\n\
    \    removal. No necessity of every deleted nucleotide, CRM3-specific recognition,\
    \ zero residual binding,\n    or observed pseudoknot is inferred. Each branch\
    \ has its own RNA and matched intact-fragment comparator.\n  nodes:\n  - node_id:\
    \ d1-delete111\n    label: Delete RNA nucleotides446-556 from D1(1-570)\n    node_type:\
    \ PERTURBATION\n  - node_id: d1-retention\n    label: D1 RNA retention at2.5nM\
    \ mature CRS1\n    node_type: STATE\n  - node_id: d4-delete16\n    label: Delete\
    \ RNA nucleotides687-702 from D4(673-747)\n    node_type: PERTURBATION\n  - node_id:\
    \ d4-retention\n    label: D4 normalized RNA retention during CRS1 titration\n\
    \    node_type: STATE\n  - node_id: loop-delete30\n    label: Delete RNA nucleotides500-529\
    \ from111nt fragment(446-556)\n    node_type: PERTURBATION\n  - node_id: loop-retention\n\
    \    label: 111nt-fragment normalized retention during CRS1 titration\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: d1-deletion-lowers-retention\n    subject: d1-delete111\n\
    \    predicate: decreases\n    object: d1-retention\n    mechanism: Removing the\
    \ accessory111nt segment lowers retention relative to intact D1 at2.5nMCRS1.\n\
    \      The supporting titration also loses high-affinity binding, but a contact-only\
    \ mechanism is unresolved.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:15598799\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC544502/\n      snippet:\
    \ low-affinity nonspecific binding\n      explanation: Figure5A fixed-concentration\
    \ comparison, Figure5B and Results; D1 joins1-445 to557-570,\n        independently\
    \ of the Figure8 constructs.\n      cache_path: evidence/PF01985/osters-2005-contexts.txt\n\
    \      cache_sha256: 8ef51c123199bdb609c838a7ae8741d42faca54ad5991b3ffe0c556b1b1a7048\n\
    \  - edge_id: d4-deletion-lowers-retention\n    subject: d4-delete16\n    predicate:\
    \ decreases\n    object: d4-retention\n    mechanism: Removing687-702 lowers the\
    \ normalized retained fraction over the displayed nonzero titration\n      range\
    \ relative to intact D4. Binding is not abolished at all concentrations, and RNA-folding\
    \ alternatives\n      remain.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:15598799\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC544502/\n      snippet:\
    \ dramatic reduction\n      explanation: Figure8A left curve/caption and Results;\
    \ D4 joins673-686 to703-747. Competition and\n        footprinting are contextual\
    \ support, not proof that all16bases directly contact protein.\n      cache_path:\
    \ evidence/PF01985/osters-2005-contexts.txt\n      cache_sha256: 8ef51c123199bdb609c838a7ae8741d42faca54ad5991b3ffe0c556b1b1a7048\n\
    \  - edge_id: loop-deletion-lowers-retention\n    subject: loop-delete30\n   \
    \ predicate: decreases\n    object: loop-retention\n    mechanism: Removing500-529\
    \ lowers retention of the isolated111nt RNA region relative to its intact\n  \
    \    counterpart. Distinct terminal deletions also alter plateaus, consistent\
    \ with unresolved structural\n      contributions rather than a demonstrated contact\
    \ map.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:15598799\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC544502/\n      snippet: eliminated\
    \ specific binding\n      explanation: Figure8B left curve/caption and Results;\
    \ the deletion joins446-499 to530-556. The proposed\n        pseudoknot remains\
    \ unverified and is not an observed edge.\n      cache_path: evidence/PF01985/osters-2005-contexts.txt\n\
    \      cache_sha256: 8ef51c123199bdb609c838a7ae8741d42faca54ad5991b3ffe0c556b1b1a7048\n\
    - graph_id: maize-mcrs1-intron-accessibility-2005\n  title: Mature CRS1 reduces\
    \ hydroxyl-radical accessibility of atpF RNA\n  scope: Ostersetzer2005 Figure6\
    \ matched10mMMgCl2 lanes and Figure7 summary; purified mature CRS1 addition\n\
    \    to intron RNA.\n  context: 40nM intron RNA,0 versus100nM mature CRS1 monomer\
    \ units,50mMHEPES pH7,150mMKOAc,10mMMgCl2;10min25C\n    then30min on ice. Fe/EDTA/ascorbate/peroxide\
    \ cleavage10min on ice, primer-extension mapping; protein-free\n    and sequencing\
    \ controls.\n  family_mapping: Q9FYT6 sequence1,PF01985 matches170-254,352-436,564-651;\
    \ mature protein begins40 with\n    all three CRM domains, GST removed and His6\
    \ retained. RNA positions use published atpF intron numbering.\n  scope_status:\
    \ MECHANISTIC\n  taxon: NCBITaxon:4577\n  limitations: DIRECT denotes measured\
    \ biochemical protection, not direct contact at every protected nucleotide.\n\
    \    Compaction and contact assignments are inferred; several intron regions lack\
    \ high-resolution data.\n    No detected CRS1-promoted splicing was reported in\
    \ vitro or in E.coli, so no protection-to-splicing\n    edge is asserted.\n  nodes:\n\
    \  - node_id: mature-crs1-addition\n    label: Add100nM mature CRS1 to40nM intron\
    \ RNA at10mMMgCl2\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q9FYT6\n\
    \  - node_id: radical-cleavage\n    label: Hydroxyl-radical cleavage at protected\
    \ intron segments\n    node_type: STATE\n  edges:\n  - edge_id: crs1-lowers-cleavage\n\
    \    subject: mature-crs1-addition\n    predicate: decreases\n    object: radical-cleavage\n\
    \    mechanism: Addition reduces cleavage/accessibility in observed segments including445-462,498-557\
    \ and684-710,\n      with additional weaker protections. RNA shielding and conformational\
    \ reorganization are consistent\n      explanations, not independently resolved\
    \ elementary steps.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:15598799\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC544502/\n      snippet: widespread\
    \ protection\n      explanation: Figure6 lanes/caption, Figure7 map and hydroxyl-radical\
    \ Methods; the graph uses the\n        measured accessibility endpoint rather\
    \ than catalytic folding or splicing sufficiency.\n      cache_path: evidence/PF01985/osters-2005-contexts.txt\n\
    \      cache_sha256: 8ef51c123199bdb609c838a7ae8741d42faca54ad5991b3ffe0c556b1b1a7048\n\
    curation_events:\n- timestamp: '2026-10-16T06:14:52Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate PF01985 CRM assay-context causal\
    \ graphs from three primary studies\n  history_record: history/records/PF01985/2026-10-16T061452Z-codex-503ce3.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Former UPF0044 and exact member/reference scope
  outcome: supported
  summary: PF01985/IPR001890 and frozen former name are grounded. Reference mapping
    is distinct from physical constructs and from all-family functional transfer.
  target_ids:
  - PF01985
  evidence_ids:
  - identity
- assessment_id: bacterial
  area: graph
  topic: Locus, culture and biochemical-addback distinctions
  outcome: supported
  summary: The original combined coding/promoter deletion is not presented as YhbY-specific
    necessity. Jiang cold growth is separated from uncertain-temperature profile preparations.
    Lysate co-IP restoration is not maturation rescue.
  target_ids:
  - PF01985
  evidence_ids:
  - barkan
  - jiang
- assessment_id: crm3
  area: graph
  topic: Joint substitution and fitted binding readout
  outcome: supported
  summary: The mapped four-residue substitution raises apparent Kd in GST-CRM3; lower
    plateau, protein-folding and active-fraction alternatives remain. Individual-residue
    and full-length effects are not fabricated.
  target_ids:
  - PF01985
  evidence_ids:
  - barkan
  - identity
- assessment_id: rna
  area: graph
  topic: Mature CRS1 cofactor, RNA deletion and accessibility readouts
  outcome: supported
  summary: All three RNA deletions retain separate substrate comparators and intron
    coordinates. Mg enhancement and radical protection are biochemical endpoints;
    contact assignments, compaction and proposed pseudoknot are not promoted to observed
    elementary mechanisms or splicing sufficiency.
  target_ids:
  - PF01985
  evidence_ids:
  - osters
  - identity
- assessment_id: preservation
  area: provenance
  topic: Maintained inputs, history and corpus preservation
  outcome: supported
  summary: Only the new overlay/evidence/actual CREATE event own the scientific change.
    Frozen metadata, previous artifacts and 8,295 other projections remain unchanged;
    generated views reproduce through native tools.
  target_ids:
  - PF01985
  evidence_ids:
  - identity
  - validation
- assessment_id: coverage
  area: completeness
  topic: Remaining experimental and family-wide coverage
  outcome: concern
  summary: Physical constructs, allele/promoter integrity, control temperature, folding
    controls and additional primary/member contexts remain open. Current qualifiers
    keep adopted edges bounded but do not finish the family.
  target_ids:
  - PF01985
  evidence_ids:
  - coverage
  - barkan
  - jiang
  - osters
findings:
- finding_id: bacterial-controls
  issue_key: pf01985-bacterial-controls
  title: Resolve bacterial allele and culture-control attribution
  description: Authenticate promoter-sparing deletion/rescue, identify Barkan panel-specific
    strains and addback conditions, and resolve Jiang Figure6 BW25113 culture temperature.
    Current locus/preparation scopes prevent a false YhbY-only mechanism but leave
    that biological question open.
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - PF01985
  field_paths:
  - causal_graphs
  - discussions
  evidence_ids:
  - barkan
  - jiang
  - coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01985.yaml
    role: Maintained scientific overlay; regenerate the projection after evidence-backed
      edits.
- finding_id: construct-and-folding-controls
  issue_key: pf01985-construct-and-folding-controls
  title: Authenticate constructs and distinguish contact loss from conformational
    effects
  description: Verify complete GST-CRM3 inserts and folding/active fractions, mature-CRS1
    stoichiometry at assay concentration, RNA-deletion structural controls and raw
    footprint coverage. Partial primer matches and reference GRRG mapping are not
    physical clone authentication.
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - PF01985
  field_paths:
  - causal_graphs
  - discussions
  evidence_ids:
  - identity
  - barkan
  - osters
  - coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01985.yaml
    role: Maintained scientific overlay; regenerate the projection after evidence-backed
      edits.
- finding_id: primary-and-member-coverage
  issue_key: pf01985-primary-and-member-coverage
  title: Extend original genetics and other CRM-family primary contexts
  description: Inspect Till2001, CAF1/CAF2, CFM2, original bacterial structures, archaeal/newer-member
    evidence and relevant supplements. Current three-study curation cannot stand for
    the complete family or all8,296records.
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - PF01985
  field_paths:
  - causal_graphs
  - discussions
  evidence_ids:
  - identity
  - coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01985.yaml
    role: Maintained scientific overlay; regenerate the projection after evidence-backed
      edits.
actions:
- action_id: extend-crm-evidence
  description: Resolve named experimental ambiguities and extend primary/member coverage
    in evidence-backed successor curation while preserving current assay boundaries.
  finding_ids:
  - bacterial-controls
  - construct-and-folding-controls
  - primary-and-member-coverage
  target_ids:
  - PF01985
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01985.yaml
    role: Maintained scientific overlay; regenerate the projection after evidence-backed
      edits.
  acceptance_checks:
  - Document physical alleles and neighboring-promoter integrity or retain the combined-locus
    interpretation.
  - Resolve the Figure6 WT temperature explicitly before asserting a genotype-only
    profile effect.
  - Authenticate clone boundaries and use discriminating folding/active-fraction controls
    before assigning atomic contact causality.
  - Keep RNA accessibility, direct contact, folding, in-vivo requirement and in-vitro
    sufficiency separate.
  - Inspect additional primary Methods/figures and exact member mappings; retain inaccessible/unperformed
    coverage honestly.
  - Append successor reviews/history, preserve stable graph IDs and pass native evidence/generation
    checks.
limitations:
- Same-agent scientific self-review, not independent approval or experimental replication.
  Completed refers to this scoped review, not full-family completion.
- All twelve edges describe observed assay effects, not twelve independent mechanistic
  discoveries. Only two are direct biochemical endpoints; five have unresolved molecular
  explanation and five are indirect strain/preparation phenotypes.
- No raw data re-quantification, independent clone sequencing, exact genomic allele
  reconstruction or comprehensive new-literature search was performed.
- The Barkan external supplement and additional primary studies remain uninspected.
  Failed XML/PDF requests were not treated as negative results. The later web-tool
  Ostersetzer request hit a browser challenge; previously obtained ordinary HTML/figures
  were used without bypassing it.
- Full articles and copyrighted figures remain in temporary research storage; only
  brief attributed extracts, factual assay summaries and source hashes are retained
  in the repository.
- The local preview renders the curated record only and does not claim refreshed frozen
  member tracks or canonical published Pages. No commit, push, PR or source checkpoint
  was created this turn.
- A final actual REVIEW history event, regeneration and revalidation follow saving.
  The 8,296-family goal remains active; structural graph presence is not scientific
  completion.
```
