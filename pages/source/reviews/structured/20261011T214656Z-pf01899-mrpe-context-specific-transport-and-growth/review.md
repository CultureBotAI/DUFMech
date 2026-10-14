# PF01899 MrpE perturbation effects and unresolved molecular coupling

- Review: 20261011T214656Z-pf01899-mrpe-context-specific-transport-and-growth
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T21:44:49Z
- Finished UTC: 2026-10-11T21:46:56Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Nine PHENOTYPIC graphs retain twelve INDIRECT OBSERVED edges for strain-specific deletion/complementation, OF4 vesicle transport, membrane protein signals, full-complex bands and apparent sodium kinetics. Exact OF4 parent identity is verified. The record preserves T113A abundance/assembly alternatives, T113Y pH dependence, P114A tolerance, reused-row discrepancies and unproven structural ion paths. IN_PROGRESS and partial same-agent scientific review are appropriate.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Frozen PF01899/DUF68 identity; current UniProt/InterPro member endpoints; eight NCBI FASTA references and the EF468713.1 GenBank parent CDS; Kajiyama2007 Methods/Results/Table1/original Figure1; Morino2008 Methods/Results/Discussion/original Figures1,2,4,5; Morino2010 Methods/Results/Discussion/readable original Table1; Steiner2020 relevant text and original Figure4/Figure1-supplement1; Lee2022 relevant text and7QRU entity5 sequence. Remaining homolog papers are leads, not reviewed experiments.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01899 | data/families/PF01899.yaml | generated | PF01899 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01899 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01899.

Frozen PF01899 is MNHE/former DUF68, not DUF69. OF4 Q9RGZ1 sequenceversion1 equals AAF21816.1,ADC50689.1,WP_012958052.1 and deposited ABS70477.1 over158 aa with PF01899 at8-156. EF468713.1 verifies untagged E/F and the final D-His7 parent. Current B. subtilis Q7WY60 equals CAE01465.2/YP_054591.2/WP_003244015.1 but differs from historical versions; UOT1285/TY5/KY11 exact sequence is unresolved, so only strain-level effects are transferred. B7GL97 anchors A. flavithermus negative-control context at8-156.7QRU entity5 differs from Q9RGZ1 at I54V,S62V,K158N despite full SIFTS coverage. No isolated-domain sufficiency or family-wide chemical mechanism is assigned.

### Directed effects and limits

graph: supported. Targets: PF01899.

Twelve directed endpoints have exact assay/source linkage and matching snippets/hashes. Two B. subtilis growth contexts use distinct salt/induction conditions. OF4 deletion retains a small alkaline-pH response. T113A transport loss, E/F/G membrane signals and full-complex bands are distinct outcomes, not an inferred causal chain among readouts. P114G transport and apparent Km are separate; Km is not Kd. T113Y retains detected complexes but its loss magnitude varies with pH. All edges are INDIRECT PHENOTYPIC observations, not direct molecular ion chemistry. Negative substitutions, association-only evidence and structural proposals stay in explicit limits/discussions.

### Remaining family coverage

completeness: concern. Targets: PF01899.

Selected strain/protein contexts do not cover10765 frozen proteins.2008/2010 supplements returned challenge HTML and EuropePMC XML errors; deletion boundaries, growth curves and supplementary blots were not directly inspected. Historical B. subtilis insert identity, antibody peptide discrepancy, reused-row numerical differences and preparation-count mismatch need resolution.2020 L41W evidence concerns retained SEC/growth, not measured mutant vesicle kinetics.2022 raw maps/figures were not reviewed, and2025 publisher access failed.1998S. aureus/R. meliloti,2003/2009B. subtilis and group2 homolog studies require further member-specific assessment. No exhaustive or independent expert review.

## Findings

### additional-contexts: Resolve source and construct ambiguities and extend MrpE family contexts

minor / open / confirmed; issue key: pf01899-causal-context-coverage.

Recover2008/2010 supplements; reconcile reused P114G kinetics, T113A abundance, P114G growth, T113Y pH-specific wording and replication counts. Verify historical B. subtilis inserts and exact structural constructs before residue transfer. Distinguish direct ion occupancy and conformational coupling from fluorescence, growth, association and structural proximity. Review remaining S. aureus,R. meliloti,B. subtilis and group2 homolog evidence with exact PF01899 mappings and preserve negative/contradictory results in successor graphs.

## Recommended Actions And Acceptance Checks

### extend-contexts

Recover2008/2010 supplements; reconcile reused P114G kinetics, T113A abundance, P114G growth, T113Y pH-specific wording and replication counts. Verify historical B. subtilis inserts and exact structural constructs before residue transfer. Distinguish direct ion occupancy and conformational coupling from fluorescence, growth, association and structural proximity. Review remaining S. aureus,R. meliloti,B. subtilis and group2 homolog evidence with exact PF01899 mappings and preserve negative/contradictory results in successor graphs.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC2945585/; Table1 original zoom image and footnotes; Experimental Procedures; mutant-group and module-interaction Results/Discussion | supports | T113Y lowers antiport across pH8-9 and fails salt-growth complementation despite comparable detected protein/complex levels. At pH9 its response is about11.8% WT, not below5%. P114A retains function. Footnoted reuse of T113A/P114G differs numerically from2008 and does not establish independent replication; P114G growth prose conflicts with positive table scores. Two-versus-three preparation wording remains unresolved. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01899/protein/uniprot/Q9RGZ1/; Accession and domain locations; paired UniProt identity facts | supports | Frozen PF01899 is MNHE/former DUF68, not DUF69. OF4 Q9RGZ1 sequenceversion1 equals AAF21816.1,ADC50689.1,WP_012958052.1 and deposited ABS70477.1 over158 aa with PF01899 at8-156. EF468713.1 verifies untagged E/F and the final D-His7 parent. Current B. subtilis Q7WY60 equals CAE01465.2/YP_054591.2/WP_003244015.1 but differs from historical versions; UOT1285/TY5/KY11 exact sequence is unresolved, so only strain-level effects are transferred. B7GL97 anchors A. flavithermus negative-control context at8-156.7QRU entity5 differs from Q9RGZ1 at I54V,S62V,K158N despite full SIFTS coverage. No isolated-domain sufficiency or family-wide chemical mechanism is assigned. |
| bs-genetic-effects | https://pmc.ncbi.nlm.nih.gov/articles/PMC2168430/; Construction section,Table1 and original Figure1A/B; association/BN text | supports | TY5 deletion loses plate growth at0.2M NaCl; KY11His6 complementation grows at1M plusIPTG. Different salt conditions prohibit a quantitative matched rescue claim. Co-purification and co-migration are associations, not direct activation edges. |
| of4-deletion-and-variants | https://pmc.ncbi.nlm.nih.gov/articles/PMC2446749/; Relevant Methods/Results/Discussion and original Figures1,2,4,5 | supports | Delta-mrpE retains a small response but greatly reduces vesicle antiport. T113A reduces transport,E/F/G membrane signals and full-complex bands. P114G retains complex forms while lowering response and raising apparent Km. Reused2010 numbers are discrepant, not pooled replications; growth data were not shown here. |
| structural-and-negative-controls | https://pmc.ncbi.nlm.nih.gov/articles/PMC7419157/; Relevant2020 text,original Figure4/Figure1-supplement1; linked2022 Methods/Results and7QRU polymer identity | supports | Two short TM helices and a cytoplasmic domain supersede older predicted topology. L41W retains dimer SEC and salt growth, so no dimer-loss edge is warranted. Sodium entry and membrane-thinning mechanisms remain proposed;2022 found no strong evidence for Na/Mg occupancy and uses a distinct MrpE sequence. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01899 | data/families/PF01899.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Eight distinct original images were inspected: Kajiyama2007 Figure1; Morino2008 Figures1,2,4,5; Morino2010 Table1 reconstructed from54 public zoom tiles; Steiner2020 Figure4 and Figure1-supplement1. No raw data,2022 maps or2008/2010 supplements were reanalyzed. Web opens and some direct supplement URLs returned challenges, but direct public PMC/Nature HTML and CDN images supplied the stated primary evidence. The filesystem and offline UV reads succeeded without escalation; public downloads required approved network access. Rendered page checks follow separately.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T214656Z-pf01899-mrpe-context-specific-transport-and-growth
title: PF01899 MrpE perturbation effects and unresolved molecular coupling
started_at: '2026-10-11T21:44:49Z'
finished_at: '2026-10-11T21:46:56Z'
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
summary: Nine PHENOTYPIC graphs retain twelve INDIRECT OBSERVED edges for strain-specific
  deletion/complementation, OF4 vesicle transport, membrane protein signals, full-complex
  bands and apparent sodium kinetics. Exact OF4 parent identity is verified. The record
  preserves T113A abundance/assembly alternatives, T113Y pH dependence, P114A tolerance,
  reused-row discrepancies and unproven structural ion paths. IN_PROGRESS and partial
  same-agent scientific review are appropriate.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01899.yaml
    sha256: f844aa5715d1bf52ad464071676686c22bd64214a657ae3376c11b376495aa63
    role: context
  - path: data/families/PF01899.yaml
    sha256: 2411d886fe92d6e38c50e793467fb2010e2241a73784593aac019d25e5ced8ae
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
  - path: evidence/PF01899/morino-2010-t113y-and-controls.txt
    role: context
    sha256: 23cb518de168e70a7c44ddc858a45bd34bdc2d9f627cf80f1f899665e70e7e28
  - path: evidence/PF01899/mrpe-identity.txt
    role: context
    sha256: e37327fc0597d27902e7c0da02bd316e0f291f23a87f36ee218bb64367298caf
  - path: evidence/PF01899/kajiyama-2007-complementation.txt
    role: context
    sha256: ba25f141d8e82575650a60079ef63bbc22dc28dece24ac7e6fed1ad0e76b6f93
  - path: evidence/PF01899/morino-2008-deletion-and-substitutions.txt
    role: context
    sha256: 8ec23c4d31545adb0858209cf4c4cdbc2e2d3dedbf2b80e031f39807adac44d7
  - path: evidence/PF01899/mrpe-structural-limits.txt
    role: context
    sha256: 1038c5f597c17396797bd1e308a26e81c52bb27bc4f665be7ffde7a5fb842f84
targets:
- target_id: PF01899
  path: data/families/PF01899.yaml
  label: PF01899
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01899.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: b3abd4ca3fcd6539dc777991398362bf70f848550675f5d068dd920da198e5d0
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Frozen PF01899/DUF68 identity; current UniProt/InterPro member endpoints;
    eight NCBI FASTA references and the EF468713.1 GenBank parent CDS; Kajiyama2007
    Methods/Results/Table1/original Figure1; Morino2008 Methods/Results/Discussion/original
    Figures1,2,4,5; Morino2010 Methods/Results/Discussion/readable original Table1;
    Steiner2020 relevant text and original Figure4/Figure1-supplement1; Lee2022 relevant
    text and7QRU entity5 sequence. Remaining homolog papers are leads, not reviewed
    experiments.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01899
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Selected strain/protein contexts do not cover10765 frozen proteins.2008/2010
      supplements returned challenge HTML and EuropePMC XML errors; deletion boundaries,
      growth curves and supplementary blots were not directly inspected. Historical
      B. subtilis insert identity, antibody peptide discrepancy, reused-row numerical
      differences and preparation-count mismatch need resolution.2020 L41W evidence
      concerns retained SEC/growth, not measured mutant vesicle kinetics.2022 raw
      maps/figures were not reviewed, and2025 publisher access failed.1998S. aureus/R.
      meliloti,2003/2009B. subtilis and group2 homolog studies require further member-specific
      assessment. No exhaustive or independent expert review.
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
  - PF01899
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2945585/
  locator: Table1 original zoom image and footnotes; Experimental Procedures; mutant-group
    and module-interaction Results/Discussion
  accessed_at: '2026-10-11T21:46:56Z'
  support: supports
  snapshot_sha256: 23cb518de168e70a7c44ddc858a45bd34bdc2d9f627cf80f1f899665e70e7e28
  summary: T113Y lowers antiport across pH8-9 and fails salt-growth complementation
    despite comparable detected protein/complex levels. At pH9 its response is about11.8%
    WT, not below5%. P114A retains function. Footnoted reuse of T113A/P114G differs
    numerically from2008 and does not establish independent replication; P114G growth
    prose conflicts with positive table scores. Two-versus-three preparation wording
    remains unresolved.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01899/protein/uniprot/Q9RGZ1/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T21:46:56Z'
  support: supports
  snapshot_sha256: e37327fc0597d27902e7c0da02bd316e0f291f23a87f36ee218bb64367298caf
  summary: Frozen PF01899 is MNHE/former DUF68, not DUF69. OF4 Q9RGZ1 sequenceversion1
    equals AAF21816.1,ADC50689.1,WP_012958052.1 and deposited ABS70477.1 over158 aa
    with PF01899 at8-156. EF468713.1 verifies untagged E/F and the final D-His7 parent.
    Current B. subtilis Q7WY60 equals CAE01465.2/YP_054591.2/WP_003244015.1 but differs
    from historical versions; UOT1285/TY5/KY11 exact sequence is unresolved, so only
    strain-level effects are transferred. B7GL97 anchors A. flavithermus negative-control
    context at8-156.7QRU entity5 differs from Q9RGZ1 at I54V,S62V,K158N despite full
    SIFTS coverage. No isolated-domain sufficiency or family-wide chemical mechanism
    is assigned.
- evidence_id: bs-genetic-effects
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2168430/
  locator: Construction section,Table1 and original Figure1A/B; association/BN text
  summary: TY5 deletion loses plate growth at0.2M NaCl; KY11His6 complementation grows
    at1M plusIPTG. Different salt conditions prohibit a quantitative matched rescue
    claim. Co-purification and co-migration are associations, not direct activation
    edges.
  accessed_at: '2026-10-11T21:46:56Z'
  support: supports
  snapshot_sha256: ba25f141d8e82575650a60079ef63bbc22dc28dece24ac7e6fed1ad0e76b6f93
- evidence_id: of4-deletion-and-variants
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2446749/
  locator: Relevant Methods/Results/Discussion and original Figures1,2,4,5
  summary: Delta-mrpE retains a small response but greatly reduces vesicle antiport.
    T113A reduces transport,E/F/G membrane signals and full-complex bands. P114G retains
    complex forms while lowering response and raising apparent Km. Reused2010 numbers
    are discrepant, not pooled replications; growth data were not shown here.
  accessed_at: '2026-10-11T21:46:56Z'
  support: supports
  snapshot_sha256: 8ec23c4d31545adb0858209cf4c4cdbc2e2d3dedbf2b80e031f39807adac44d7
- evidence_id: structural-and-negative-controls
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7419157/
  locator: Relevant2020 text,original Figure4/Figure1-supplement1; linked2022 Methods/Results
    and7QRU polymer identity
  summary: Two short TM helices and a cytoplasmic domain supersede older predicted
    topology. L41W retains dimer SEC and salt growth, so no dimer-loss edge is warranted.
    Sodium entry and membrane-thinning mechanisms remain proposed;2022 found no strong
    evidence for Na/Mg occupancy and uses a distinct MrpE sequence.
  accessed_at: '2026-10-11T21:46:56Z'
  support: supports
  snapshot_sha256: 1038c5f597c17396797bd1e308a26e81c52bb27bc4f665be7ffde7a5fb842f84
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T21:46:56Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01899
  kind: record_content
  reference: data/families/PF01899.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T21:46:56Z'
  support: context_only
  snapshot_sha256: 2411d886fe92d6e38c50e793467fb2010e2241a73784593aac019d25e5ced8ae
  quote: "id: Pfam:PF01899\npfam_id: PF01899\nname: Na+/H+ ion antiporter subunit\n\
    short_name: MNHE\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01899\n\
    counters:\n  proteins: 10765\n  matches: 10765\n  proteomes: 8482\n  taxa: 12249\n\
    \  structures: 5\n  alphafold_models: 7110\n  domain_architectures: 9\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002758\ndescription: Subunit of a Na+/H+ Prokaryotic\
    \ antiporter complex ([[cite:PUB00010583]],[[cite:PUB00010603]]).\ncuration_history:\
    \ history/records/PF01899\ndiscussions:\n- discussion_id: mrpe-mechanism-and-source-discrepancies\n\
    \  prompt: Resolve construct and numerical discrepancies before assigning a direct\
    \ MrpE ion-binding or\n    conformational mechanism.\n  kind: CURATION_TODO\n\
    \  status: OPEN\n  rationale: T113A changes abundance and complex signals, whereas\
    \ T113Y and P114G lose much transport\n    despite retained detected complexes.\
    \ These distinct perturbations do not directly observe sodium occupancy\n    or\
    \ the proposed E-G-to-A-D activation step. P114A retains function; whole-gene\
    \ deletion retains a\n    small alkaline-pH response.\n  evidence:\n  - reference:\
    \ PMID:18408029\n    supports: PARTIAL\n    evidence_source: primary_methods_results_and_original_figures\n\
    \    explanation: Figure5 provides the scoped transport/abundance/complex/kinetic\
    \ endpoints. The antibody\n      peptide discrepancy, unavailable deletion-boundary\
    \ supplement and intermediate His10 wording need\n      resolution; EF468713.1\
    \ verifies the final His7 parent.\n  - reference: PMID:20624916\n    supports:\
    \ PARTIAL\n    evidence_source: primary_methods_results_and_readable_original_table\n\
    \    explanation: Footnoted T113A/P114G reuse differs from2008 values. P114G growth\
    \ is positive in Table1\n      despite reduced-resistance prose, and T113Y is\
    \ not below5% WT at pH9. Preserve the discrepancies\n      and obtain S2-S6.\n\
    \  - reference: PMID:32735215\n    supports: PARTIAL\n    evidence_source: primary_structure_text_and_original_figures\n\
    \    explanation: Two-TM/cytoplasmic MrpE topology supersedes the earlier prediction.\
    \ L41W retains a dimer\n      peak and salt-growth complementation; its mutant\
    \ transport kinetics were not displayed. Proposed\n      H131/partner-histidine\
    \ sodium entry is not an observed binding edge.\n  - reference: PMID:36241630\n\
    \    supports: PARTIAL\n    evidence_source: primary_methods_results_and_deposited_polymer_sequence\n\
    \    explanation: The7QRU MrpE sequence differs from the2008 parent at54,62,158.\
    \ No strong Na/Mg density\n      was found by the authors; competing paths and\
    \ conformational gating remain models. No raw map reanalysis\n      was performed.\n\
    \  posed_by: Codex\n  posed_date: '2026-10-11'\n  notes: Retained source assessments\
    \ are in evidence/PF01899. Measure ion occupancy and transport under\n    matched\
    \ abundance/assembly conditions before adding molecular edges. Do not replace\
    \ apparent Km with\n    Kd, turn association into activation, or count reused\
    \ rows as independent experiments.\n- discussion_id: mrpe-family-and-host-coverage\n\
    \  prompt: Extend the review to other MrpE/MnhE/PhaE homologs with exact member\
    \ and host mapping.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: Selected\
    \ B. subtilis and OF4 phenotypes plus structural context do not characterize all10765\n\
    \    frozen proteins. B. subtilis current reference sequence differs from its\
    \ historical version; native-host\n    and KNabc phenotypes are not interchangeable.\n\
    \  evidence:\n  - reference: PMID:17693497\n    supports: PARTIAL\n    evidence_source:\
    \ primary_methods_results_and_original_figure\n    explanation: Strain-level deletion\
    \ and His6 complementation support growth effects but not exact current-reference\n\
    \      residue assignments or isolated-domain function.\n  - reference: PMID:9852009\n\
    \    supports: PARTIAL\n    evidence_source: current_family_record_primary_citation_lead\n\
    \    explanation: S. aureus multisubunit antiporter study is an identified lead,\
    \ not a completed member-specific\n      causal review.\n  - reference: PMID:9680201\n\
    \    supports: PARTIAL\n    evidence_source: current_family_record_primary_citation_lead\n\
    \    explanation: R. meliloti pH/symbiosis/K-efflux study needs primary-assay\
    \ and individual-subunit attribution\n      before graph transfer.\n  posed_by:\
    \ Codex\n  posed_date: '2026-10-11'\n  notes: Also review the2003 B. subtilis\
    \ deletion phenotypes,2009 acidic-residue study,group2/Dietzia\n    homologs and\
    \ later primary work. The2025 histidine-switch paper was only a search lead. This\
    \ is partial\n    same-agent curation; status remains IN_PROGRESS and no publication\
    \ or whole-family completion is claimed.\ncausal_graphs:\n- graph_id: bs-mrpe-deletion-growth\n\
    \  title: MrpE deletion reduces salt-tolerant growth in B. subtilis\n  scope:\
    \ Kajiyama2007 Figure1A; TY5 delta-mrpE/shaE versus UOT1285.\n  context: LB agar\
    \ containing 0.2 M NaCl. UOT1285 has trpC2 lys1 aprE-delta3 nprE18 nprR2. The\
    \ figure's\n    plate duration, temperature and replicate count were not established;\
    \ membrane-preparation conditions\n    are not substituted.\n  family_mapping:\
    \ B. subtilis reference Q7WY60/BSU31640 is 158 aa with PF01899 at 8-156. Current\
    \ sequence\n    version2 matches CAE01465.2/YP_054591.2, but differs from historical\
    \ version1 and was revised in2009.\n    UOT1285/TY5 were not independently sequenced;\
    \ this is whole-gene, strain-specific evidence, not exact-residue\n    transfer\
    \ to strain168.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:1423\n  limitations:\
    \ Qualitative plate growth, not a measured transport rate. The host retains other\
    \ Mrp components.\n    Whole-gene loss does not isolate PF01899 chemistry or establish\
    \ an autonomous MrpE antiporter.\n  nodes:\n  - node_id: delete-mrpe\n    label:\
    \ Delete mrpE in the UOT1285 background\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q7WY60\n  - node_id: salt-plate-growth\n    label: Growth on\
    \ LB agar with 0.2 M NaCl\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: deletion-decreases-growth\n\
    \    subject: delete-mrpe\n    predicate: decreases\n    object: salt-plate-growth\n\
    \    mechanism: The TY5 sector lacks comparable growth to WT on the same plate.\
    \ This supports a salt-growth\n      contribution of the intact gene in this strain,\
    \ without resolving transport, abundance or assembly\n      intermediates.\n \
    \   directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:17693497\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2168430/\n\
    \      snippet: complemented\n      explanation: Construction section, Table1\
    \ and visually inspected Figure1A establish TY5 identity\n        and its qualitative\
    \ WT comparison. The separate complementation panel is retained in its own salt/induction\n\
    \        context.\n      cache_path: evidence/PF01899/kajiyama-2007-complementation.txt\n\
    \      cache_sha256: ba25f141d8e82575650a60079ef63bbc22dc28dece24ac7e6fed1ad0e76b6f93\n\
    - graph_id: bs-mrpe-complementation\n  title: MrpE-His6 complementation supports\
    \ high-salt growth\n  scope: Kajiyama2007 Figure1B; KY11 derived from TY5.\n \
    \ context: KY11 is TY5 aprE::Pspac-mrpE-His6 spc. LB agar contains 1 M NaCl and\
    \ 1 mM IPTG; chromosomal\n    integration was PCR-confirmed. The other Mrp genes\
    \ remain present.\n  family_mapping: Q7WY60/BSU31640, PF01899 8-156 of158 aa,\
    \ is the B. subtilis reference, not a verified\n    sequence of the2007 UOT1285-derived\
    \ insert. The tag is C-terminal His6; complementation is at aprE,\n    not a scarless\
    \ native-locus repair.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:1423\n\
    \  limitations: Deletion Figure1A uses0.2 M NaCl, whereas complementation Figure1B\
    \ uses1 M plus IPTG. Do\n    not calculate a matched-condition rescue magnitude.\
    \ An empty-aprE vector control and figure-specific\n    replication were not established.\
    \ MrpE alone is not sufficient outside the remaining Mrp system.\n  nodes:\n \
    \ - node_id: complement-mrpe\n    label: Supply induced MrpE-His6 in TY5 with\
    \ the other Mrp genes intact\n    node_type: PERTURBATION\n    grounding:\n  \
    \  - UniProtKB:Q7WY60\n  - node_id: high-salt-growth\n    label: Growth on LB\
    \ agar with 1 M NaCl and IPTG\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ complementation-enables-growth\n    subject: complement-mrpe\n    predicate:\
    \ enables\n    object: high-salt-growth\n    mechanism: KY11 grows under the displayed\
    \ high-salt induction condition, supporting genetic complementation\n      of\
    \ the deleted subunit. The edge is conditional on the host's remaining machinery,\
    \ not autonomous\n      MrpE transport.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:17693497\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2168430/\n      snippet:\
    \ complemented\n      explanation: Original Figure1B delta-E/E-His sector, its\
    \ caption and Table1 define the complemented\n        strain and distinct assay\
    \ condition. Association experiments do not supply additional causal edges.\n\
    \      cache_path: evidence/PF01899/kajiyama-2007-complementation.txt\n      cache_sha256:\
    \ ba25f141d8e82575650a60079ef63bbc22dc28dece24ac7e6fed1ad0e76b6f93\n- graph_id:\
    \ of4-mrpe-deletion-antiport\n  title: Removing OF4 MrpE reduces coupled vesicle\
    \ antiport\n  scope: Morino2008 Figure1B; delta-mrpE operon versus tagged pGEMmrpTFCHS7\
    \ in E. coli KNabc.\n  context: Everted vesicles from LBK plus50 mM NaCl cultures\
    \ at37 C. Assay pH7.0-9.0,2 ml,50 mM BTP-sulfate,140\n    mM choline chloride,5\
    \ mM MgCl2,1 uM acridine orange,66 ug protein,2.5 mM succinate and Methods-default2.5\n\
    \    mM NaCl. Duplicate assays from at least three preparations.\n  family_mapping:\
    \ OF4 MrpE Q9RGZ1 sequence version1 equals AAF21816.1/ADC50689.1/WP_012958052.1\
    \ and EF468713.1\n    CDS ABS70477.1 over158 aa; PF01899 maps8-156. Paper organism\
    \ Bacillus pseudofirmus OF4, now Alkalihalophilus\n    pseudofirmus. Whole-gene\
    \ deletion, not an isolated-domain perturbation.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:398511\n  limitations: A small alkaline-pH response remains.\
    \ Figure2 retains the other six subunits; a weak Figure4\n    upper band does\
    \ not establish an active six-subunit complex. Exact deletion boundaries in the\
    \ unavailable\n    supplement were not inspected. Both parent and mutant are near\
    \ baseline at pH6.5, excluded from the\n    decreasing-edge range.\n  nodes:\n\
    \  - node_id: delete-of4-mrpe\n    label: Remove mrpE from the expressed OF4 operon\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q9RGZ1\n  - node_id:\
    \ sodium-dependent-dequenching\n    label: Sodium-dependent acridine-orange dequenching\
    \ at pH7-9\n    node_type: ACTIVITY\n  edges:\n  - edge_id: deletion-decreases-antiport-readout\n\
    \    subject: delete-of4-mrpe\n    predicate: decreases\n    object: sodium-dependent-dequenching\n\
    \    mechanism: Deleting mrpE strongly lowers the sodium-induced dissipation of\
    \ the respiratory delta-pH\n      compared with the tagged parent, while retaining\
    \ a small response. The assay measures whole-complex\n      behavior in host membranes,\
    \ not direct MrpE ion translocation.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:18408029\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2446749/\n      snippet:\
    \ dequenching\n      explanation: Original Figure1B supplies the pH series and\
    \ deletion-versus-parent contrast. Methods\n        specifies reagent concentrations;\
    \ original Figures2 and4B constrain abundance/complex interpretations.\n     \
    \ cache_path: evidence/PF01899/morino-2008-deletion-and-substitutions.txt\n  \
    \    cache_sha256: 8ec23c4d31545adb0858209cf4c4cdbc2e2d3dedbf2b80e031f39807adac44d7\n\
    - graph_id: of4-mrpe-t113a-antiport\n  title: MrpE T113A abolishes the detected\
    \ vesicle response\n  scope: Morino2008 Figure5B; T113A versus tagged OF4 parent\
    \ in KNabc.\n  context: Everted-vesicle assay at pH8.5 with10 mM NaCl,2.5 mM succinate,66\
    \ ug protein and1 uM acridine\n    orange in BTP-sulfate/choline chloride/MgCl2\
    \ buffer. Figure5's10 mM Na overrides the general Methods2.5\n    mM default;\
    \ empty vector is the negative control.\n  family_mapping: T113 is verified in\
    \ Q9RGZ1/ABS70477.1 and lies in PF01899 residues8-156 of158 aa. MrpE\n    is untagged\
    \ within the A-T7/B-FLAG/C-c-myc/D-His7/G-S parent. Other subunits and host membranes\
    \ are\n    present.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:398511\n \
    \ limitations: T113A also reduces membrane protein signals and full-complex bands;\
    \ transport loss cannot\n    identify a direct ion-binding role. The older four-TM\
    \ cartoon is a prediction. The2010 footnoted reuse\n    is not independent replication\
    \ and has different reported abundance values.\n  nodes:\n  - node_id: t113a\n\
    \    label: Substitute MrpE T113A in the expressed OF4 complex\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:Q9RGZ1\n  - node_id: vesicle-dequenching\n\
    \    label: Sodium-triggered vesicle dequenching at pH8.5\n    node_type: ACTIVITY\n\
    \  edges:\n  - edge_id: t113a-decreases-antiport\n    subject: t113a\n    predicate:\
    \ decreases\n    object: vesicle-dequenching\n    mechanism: The T113A trace lacks\
    \ the tagged parent's detectable Na-dependent response. Changed protein\n    \
    \  abundance, complex stability and catalytic behavior remain alternative or joint\
    \ explanations.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:18408029\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC2446749/\n      snippet: dequenching\n\
    \      explanation: Original Figure5B traces and caption define pH8.5/10 mM Na.\
    \ The separately retained\n        Figure5C/D controls prevent an unsupported\
    \ atomic mechanism.\n      cache_path: evidence/PF01899/morino-2008-deletion-and-substitutions.txt\n\
    \      cache_sha256: 8ec23c4d31545adb0858209cf4c4cdbc2e2d3dedbf2b80e031f39807adac44d7\n\
    - graph_id: of4-mrpe-t113a-protein-and-complex-signals\n  title: T113A reduces\
    \ membrane subunit and full-complex signals\n  scope: Morino2008 Figure5C/D; T113A\
    \ versus tagged OF4 parent in KNabc.\n  context: Membranes from LBK plus50 mM\
    \ NaCl cultures at37 C. SDS immunoblots use20 ug membrane protein;\n    blue-native\
    \ immunoblots use30 ug solubilized protein and display MrpA/MrpD probes. Comparisons\
    \ are\n    within each assay, not across different protein loads.\n  family_mapping:\
    \ Whole Q9RGZ1/ABS70477.1 MrpE,158 aa,PF01899 8-156; T113 lies inside the match.\
    \ The changed\n    MrpE protein and partner MrpF/MrpG signals are different measured\
    \ entities, not additional PF01899\n    proteins.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:398511\n  limitations: WT-normalized densitometry is not a\
    \ protein turnover rate. Epitope recognition, folding,\n    localization and detergent\
    \ stability are not independently resolved. The printed antibody peptide\n   \
    \ omits a T relative to reference92-104. No arrow from lower MrpE abundance to\
    \ partner loss is inferred\n    from their co-occurrence.\n  nodes:\n  - node_id:\
    \ t113a\n    label: Substitute MrpE T113A in the OF4 operon\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q9RGZ1\n  - node_id: mrpe-membrane-signal\n \
    \   label: Membrane MrpE immunoblot signal\n    node_type: STATE\n  - node_id:\
    \ mrpf-membrane-signal\n    label: Membrane MrpF immunoblot signal\n    node_type:\
    \ STATE\n  - node_id: mrpg-membrane-signal\n    label: Membrane MrpG immunoblot\
    \ signal\n    node_type: STATE\n  - node_id: full-complex-bands\n    label: Blue-native\
    \ bands assigned to full MrpA-G complexes\n    node_type: STATE\n  edges:\n  -\
    \ edge_id: t113a-decreases-mrpe-signal\n    subject: t113a\n    predicate: decreases\n\
    \    object: mrpe-membrane-signal\n    mechanism: Figure5C reports a T113A MrpE\
    \ signal of0.07 relative to parent1. This is a membrane-fraction\n      immunoblot\
    \ endpoint, not proof of a specific degradation or assembly pathway.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:18408029\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2446749/\n\
    \      snippet: dequenching\n      explanation: Original Figure5C MrpE row and\
    \ SDS-immunoblot Methods. The2010 reused row gives0.11;\n        this edge retains\
    \ the2008 result without pooling the discrepant values.\n      cache_path: evidence/PF01899/morino-2008-deletion-and-substitutions.txt\n\
    \      cache_sha256: 8ec23c4d31545adb0858209cf4c4cdbc2e2d3dedbf2b80e031f39807adac44d7\n\
    \  - edge_id: t113a-decreases-mrpf-signal\n    subject: t113a\n    predicate:\
    \ decreases\n    object: mrpf-membrane-signal\n    mechanism: Figure5C reports\
    \ a T113A MrpF signal of0.12 relative to parent1. The changed partner signal\n\
    \      does not demonstrate direct physical stabilization by MrpE.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:18408029\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2446749/\n\
    \      snippet: dequenching\n      explanation: Original Figure5C MrpF row; the2010\
    \ reused row instead gives0.07. One experiment supplies\n        several endpoints,\
    \ not independent replications.\n      cache_path: evidence/PF01899/morino-2008-deletion-and-substitutions.txt\n\
    \      cache_sha256: 8ec23c4d31545adb0858209cf4c4cdbc2e2d3dedbf2b80e031f39807adac44d7\n\
    \  - edge_id: t113a-decreases-mrpg-signal\n    subject: t113a\n    predicate:\
    \ decreases\n    object: mrpg-membrane-signal\n    mechanism: Figure5C reports\
    \ a T113A MrpG signal of0.02 relative to parent1. Its causal molecular explanation\n\
    \      is unresolved despite the genetic perturbation-to-readout relationship.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:18408029\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2446749/\n\
    \      snippet: dequenching\n      explanation: Original Figure5C MrpG row; the2010\
    \ reused row instead gives0.20. Both describe a reduction,\n        but no exact\
    \ common value or independent repetition is assumed.\n      cache_path: evidence/PF01899/morino-2008-deletion-and-substitutions.txt\n\
    \      cache_sha256: 8ec23c4d31545adb0858209cf4c4cdbc2e2d3dedbf2b80e031f39807adac44d7\n\
    \  - edge_id: t113a-decreases-full-complex-bands\n    subject: t113a\n    predicate:\
    \ decreases\n    object: full-complex-bands\n    mechanism: Full-complex bands\
    \ detected for the tagged parent are absent in the T113A lane while the\n    \
    \  A-D subcomplex remains. This is a detergent-extracted complex pattern, not\
    \ direct observation of\n      assembly kinetics or an active isolated A-D transporter.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:18408029\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2446749/\n\
    \      snippet: dequenching\n      explanation: Original Figure5D lanes2/3 and\
    \ caption; only A/D probes are displayed. Detergent/dye-inflated\n        apparent\
    \ sizes do not independently prove exact stoichiometry.\n      cache_path: evidence/PF01899/morino-2008-deletion-and-substitutions.txt\n\
    \      cache_sha256: 8ec23c4d31545adb0858209cf4c4cdbc2e2d3dedbf2b80e031f39807adac44d7\n\
    - graph_id: of4-mrpe-p114g-antiport\n  title: P114G lowers transport despite retained\
    \ full-complex bands\n  scope: Morino2008 Figure5B-D; P114G versus tagged OF4\
    \ parent in KNabc.\n  context: Everted-vesicle fluorescence at pH8.5,10 mM NaCl,2.5\
    \ mM succinate,66 ug protein and1 uM acridine\n    orange. Parallel membrane and\
    \ native-gel controls are distinct assays, not a single observed temporal\n  \
    \  chain.\n  family_mapping: P114 is verified in Q9RGZ1/ABS70477.1 within PF01899\
    \ 8-156. The whole158-aa MrpE variant\n    is expressed with the other six OF4\
    \ subunits. A Results typo T114G does not define another allele.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:398511\n  limitations: Figure5C/D retains substantial\
    \ subunit signals and full-complex forms, but does not prove\n    identical folding\
    \ or conformation. P114A is tolerated in2010, so proline identity is not absolutely\n\
    \    required. Growth claims conflict across sources; no P114G growth edge is\
    \ included.\n  nodes:\n  - node_id: p114g\n    label: Substitute MrpE P114G in\
    \ the OF4 complex\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q9RGZ1\n\
    \  - node_id: vesicle-dequenching\n    label: Sodium-triggered dequenching at\
    \ pH8.5\n    node_type: ACTIVITY\n  edges:\n  - edge_id: p114g-decreases-antiport\n\
    \    subject: p114g\n    predicate: decreases\n    object: vesicle-dequenching\n\
    \    mechanism: P114G gives a much smaller response than the tagged parent despite\
    \ retaining the detected\n      full-complex pattern. The result distinguishes\
    \ transport function from gross complex loss without\n      locating a sodium-binding\
    \ atom or proving a conformational activation pathway.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:18408029\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2446749/\n\
    \      snippet: dequenching\n      explanation: Original Figure5B trace,5C protein\
    \ signals and5D lane4 supply the effect and controls.\n        The later reused\
    \ row is not counted as a second experimental origin.\n      cache_path: evidence/PF01899/morino-2008-deletion-and-substitutions.txt\n\
    \      cache_sha256: 8ec23c4d31545adb0858209cf4c4cdbc2e2d3dedbf2b80e031f39807adac44d7\n\
    - graph_id: of4-mrpe-p114g-apparent-km\n  title: P114G raises the apparent sodium\
    \ requirement for half-maximal response\n  scope: Morino2008 Figure5B inset; sodium-dependent\
    \ vesicle response at three pH values.\n  context: Apparent Km derived from Na-dependent\
    \ acridine-orange dequenching in everted KNabc vesicles\n    expressing tagged\
    \ OF4 complexes. Separate titrations at pH8.0,8.5,9.0; the fixed10 mM Na trace\
    \ is\n    not itself the complete titration.\n  family_mapping: Q9RGZ1/ABS70477.1\
    \ P114G in whole MrpE,158 aa,PF01899 residues8-156. Other subunits,\n    membrane\
    \ environment and respiratory energization contribute to the measured kinetic\
    \ response.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:398511\n  limitations:\
    \ Apparent Km is not equilibrium sodium-binding Kd or direct occupancy at P114.\
    \ The2010 table's\n    attributed reuse gives2.4/1.6/1.4 mM rather than the2008\
    \ inset1.67/1.30/1.29 mM at pH8/8.5/9. The\n    discrepancy remains unresolved;\
    \ values are neither averaged nor treated as independent replication.\n  nodes:\n\
    \  - node_id: p114g\n    label: Substitute MrpE P114G instead of parental Pro114\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q9RGZ1\n  - node_id:\
    \ apparent-na-km\n    label: Apparent sodium Km of the vesicle fluorescence response\n\
    \    node_type: STATE\n  edges:\n  - edge_id: p114g-increases-apparent-km\n  \
    \  subject: p114g\n    predicate: increases\n    object: apparent-na-km\n    mechanism:\
    \ The2008 inset reports P114G1.67/1.30/1.29 mM versus parent0.084/0.079/0.060\
    \ mM at pH8.0/8.5/9.0.\n      The approximately16.5-21.5-fold shift is a whole-system\
    \ kinetic phenotype, not isolated MrpE binding\n      affinity.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:18408029\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2446749/\n\
    \      snippet: dequenching\n      explanation: Original Figure5B inset supplies\
    \ all six values and corresponding pH labels; Methods\n        defines the half-maximal\
    \ response. The higher Km remains distinct from lower response amplitude.\n  \
    \    cache_path: evidence/PF01899/morino-2008-deletion-and-substitutions.txt\n\
    \      cache_sha256: 8ec23c4d31545adb0858209cf4c4cdbc2e2d3dedbf2b80e031f39807adac44d7\n\
    - graph_id: of4-mrpe-t113y-antiport\n  title: T113Y reduces antiport without gross\
    \ loss of detected complexes\n  scope: Morino2010 Table1; T113Y versus tagged\
    \ OF4 parent in KNabc.\n  context: Vesicle assays at pH8.0,8.5,9.0;2 ml,50 mM\
    \ BTP-chloride,140 mM choline chloride,5 mM MgCl2,1\n    uM acridine orange,66\
    \ ug protein,2.5 mM succinate and10 mM NaCl. Methods specifies two independent\n\
    \    preparations; Table1 footnote specifies three experiments, both in duplicate.\n\
    \  family_mapping: Q9RGZ1/ABS70477.1 T113Y lies within PF01899 8-156 of158 aa.\
    \ The substituted MrpE is\n    part of the complete OF4 heterologous complex.\
    \ The deposited parent matches the reference; every mutant\n    plasmid was not\
    \ independently resequenced by this review.\n  scope_status: PHENOTYPIC\n  taxon:\
    \ NCBITaxon:398511\n  limitations: Table1 gives comparable A-G abundance ratios\
    \ and positive complex columns, not proof of\n    unchanged conformation. Complex\
    \ scoring need not resolve every subunit. The less-than5%-WT prose does\n    not\
    \ apply at pH9.0. Supplementary traces/blots were not inspected; Km is not determined,\
    \ not zero\n    affinity.\n  nodes:\n  - node_id: t113y\n    label: Substitute\
    \ MrpE T113Y in the OF4 complex\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q9RGZ1\n  - node_id: sodium-dependent-response\n    label: Sodium-dependent\
    \ vesicle dequenching at pH8-9\n    node_type: ACTIVITY\n  edges:\n  - edge_id:\
    \ t113y-decreases-antiport\n    subject: t113y\n    predicate: decreases\n   \
    \ object: sodium-dependent-response\n    mechanism: T113Y gives0.1/2.0/4.9% dequenching\
    \ at pH8.0/8.5/9.0 versus parent44.5/48.9/41.6%. The\n      pH9 mutant response\
    \ is about11.8% of parent, not below5%. Comparable protein and complex readouts\n\
    \      weaken a gross-loss explanation but leave molecular coupling unresolved.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:20624916\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2945585/\n\
    \      snippet: antiport\n      explanation: Readable original Table1 T113Y and\
    \ positive-control rows with Methods and footnotes\n        supply the means,\
    \ SD, abundance ratios and complex scoring. P114A's retained function is a substitution-specific\n\
    \        control, not an identical mutant.\n      cache_path: evidence/PF01899/morino-2010-t113y-and-controls.txt\n\
    \      cache_sha256: 23cb518de168e70a7c44ddc858a45bd34bdc2d9f627cf80f1f899665e70e7e28\n\
    - graph_id: of4-mrpe-t113y-growth\n  title: T113Y fails to confer the parent's\
    \ salt-growth phenotype\n  scope: Morino2010 Table1; KNabc expressing T113Y versus\
    \ tagged OF4 parent.\n  context: LBK culture pH7.5,37 C,200 rpm; Table1 scores\
    \ growth with200 or500 mM added NaCl. Detailed\n    S2 growth curves and a figure-specific\
    \ duration/replicate count were not inspected.\n  family_mapping: Whole OF4 MrpE\
    \ Q9RGZ1/ABS70477.1,PF01899 8-156, carries T113Y within the expressed seven-subunit\n\
    \    complex. The organism supplying the protein differs from the E. coli assay\
    \ host.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:398511\n  limitations:\
    \ Categorical growth score, not a survival percentage or fitted growth rate. This\
    \ is separate\n    from vesicle transport; no measured transport-to-growth causal\
    \ chain is claimed. Do not import the16h\n    MrpG Figure4 protocol as an established\
    \ T113Y condition.\n  nodes:\n  - node_id: t113y\n    label: Express the T113Y\
    \ OF4 complex instead of tagged parent\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q9RGZ1\n  - node_id: salt-growth\n    label: KNabc growth with200\
    \ or500 mM added NaCl\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: t113y-decreases-salt-growth\n\
    \    subject: t113y\n    predicate: decreases\n    object: salt-growth\n    mechanism:\
    \ T113Y is scored growth-negative at both salt concentrations where the parent\
    \ is positive.\n      The system-level outcome does not establish a specific sodium-binding\
    \ site or isolated-domain sufficiency.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:20624916\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2945585/\n      snippet:\
    \ antiport\n      explanation: Original Table1 growth columns and corresponding\
    \ Results define the categorical contrast.\n        The supplemental time courses\
    \ remain an explicit access/coverage limit.\n      cache_path: evidence/PF01899/morino-2010-t113y-and-controls.txt\n\
    \      cache_sha256: 23cb518de168e70a7c44ddc858a45bd34bdc2d9f627cf80f1f899665e70e7e28\n\
    curation_events:\n- timestamp: '2026-10-11T21:40:44Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate MrpE strain-specific growth, vesicle\
    \ antiport, abundance and complex-pattern effects\n  history_record: history/records/PF01899/2026-10-11T214044Z-codex-650d92.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Frozen PF01899 is MNHE/former DUF68, not DUF69. OF4 Q9RGZ1 sequenceversion1
    equals AAF21816.1,ADC50689.1,WP_012958052.1 and deposited ABS70477.1 over158 aa
    with PF01899 at8-156. EF468713.1 verifies untagged E/F and the final D-His7 parent.
    Current B. subtilis Q7WY60 equals CAE01465.2/YP_054591.2/WP_003244015.1 but differs
    from historical versions; UOT1285/TY5/KY11 exact sequence is unresolved, so only
    strain-level effects are transferred. B7GL97 anchors A. flavithermus negative-control
    context at8-156.7QRU entity5 differs from Q9RGZ1 at I54V,S62V,K158N despite full
    SIFTS coverage. No isolated-domain sufficiency or family-wide chemical mechanism
    is assigned.
  target_ids:
  - PF01899
  evidence_ids:
  - identity
  - primary
  - bs-genetic-effects
  - of4-deletion-and-variants
  - structural-and-negative-controls
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Twelve directed endpoints have exact assay/source linkage and matching
    snippets/hashes. Two B. subtilis growth contexts use distinct salt/induction conditions.
    OF4 deletion retains a small alkaline-pH response. T113A transport loss, E/F/G
    membrane signals and full-complex bands are distinct outcomes, not an inferred
    causal chain among readouts. P114G transport and apparent Km are separate; Km
    is not Kd. T113Y retains detected complexes but its loss magnitude varies with
    pH. All edges are INDIRECT PHENOTYPIC observations, not direct molecular ion chemistry.
    Negative substitutions, association-only evidence and structural proposals stay
    in explicit limits/discussions.
  target_ids:
  - PF01899
  evidence_ids:
  - primary
  - native
  - bs-genetic-effects
  - of4-deletion-and-variants
  - structural-and-negative-controls
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Selected strain/protein contexts do not cover10765 frozen proteins.2008/2010
    supplements returned challenge HTML and EuropePMC XML errors; deletion boundaries,
    growth curves and supplementary blots were not directly inspected. Historical
    B. subtilis insert identity, antibody peptide discrepancy, reused-row numerical
    differences and preparation-count mismatch need resolution.2020 L41W evidence
    concerns retained SEC/growth, not measured mutant vesicle kinetics.2022 raw maps/figures
    were not reviewed, and2025 publisher access failed.1998S. aureus/R. meliloti,2003/2009B.
    subtilis and group2 homolog studies require further member-specific assessment.
    No exhaustive or independent expert review.
  target_ids:
  - PF01899
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01899-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve source and construct ambiguities and extend MrpE family contexts
  description: Recover2008/2010 supplements; reconcile reused P114G kinetics, T113A
    abundance, P114G growth, T113Y pH-specific wording and replication counts. Verify
    historical B. subtilis inserts and exact structural constructs before residue
    transfer. Distinguish direct ion occupancy and conformational coupling from fluorescence,
    growth, association and structural proximity. Review remaining S. aureus,R. meliloti,B.
    subtilis and group2 homolog evidence with exact PF01899 mappings and preserve
    negative/contradictory results in successor graphs.
  target_ids:
  - PF01899
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - bs-genetic-effects
  - of4-deletion-and-variants
  - structural-and-negative-controls
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01899.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Recover2008/2010 supplements; reconcile reused P114G kinetics, T113A
    abundance, P114G growth, T113Y pH-specific wording and replication counts. Verify
    historical B. subtilis inserts and exact structural constructs before residue
    transfer. Distinguish direct ion occupancy and conformational coupling from fluorescence,
    growth, association and structural proximity. Review remaining S. aureus,R. meliloti,B.
    subtilis and group2 homolog evidence with exact PF01899 mappings and preserve
    negative/contradictory results in successor graphs.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01899
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- 'Eight distinct original images were inspected: Kajiyama2007 Figure1; Morino2008
  Figures1,2,4,5; Morino2010 Table1 reconstructed from54 public zoom tiles; Steiner2020
  Figure4 and Figure1-supplement1. No raw data,2022 maps or2008/2010 supplements were
  reanalyzed. Web opens and some direct supplement URLs returned challenges, but direct
  public PMC/Nature HTML and CDN images supplied the stated primary evidence. The
  filesystem and offline UV reads succeeded without escalation; public downloads required
  approved network access. Rendered page checks follow separately.'
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
