# PF01936 Stage 4 frozen-inventory causal-graph and grounding review

- Review: 20261021T114817Z-pf01936-stage4-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-21T11:48:16Z
- Finished UTC: 2026-10-21T11:48:17Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Eight graphs retain22 OBSERVED effects:2 DIRECT,2 INDIRECT and18 UNRESOLVED across2 MECHANISTIC and6 PHENOTYPIC contexts. Four ledgers and two OPEN discussions retain mapping,experimental and coverage limits. Same-agent partial scientific review; IN_PROGRESS,not family-wide completion or publication. Stage 2 (PR #319) grounded Homo sapiens MARF1/EDC4/DCP1A P-body localization nodes edc4-localization (UniProtKB:Q9Y4F3, UniProtKB:Q6P2E9) and dcp1a-pbodies (UniProtKB:Q9NPI6) in human-marf1-edc4-decapping-localization, preserving all domain-mapping and separated mRNA reporter graphs.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Ascending uncurated Pfam after PF01935; all8296 records and existing follow-ups remain in scope.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d658f73e7e618d3938704cdb9c86597bf47fc15e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01936 | data/families/PF01936.yaml | generated | PF01936 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01936 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01936.

Frozen DUF88/NYN/IPR021139/UNSCORED identity is preserved. Human Q9Y4F3v6 PF01936 353-490 lies inside assayed238-510,not just crystallized352-500. Mouse Q8BJ34v3 maps352-489. PDB5YAA source158-320 matches canonical337-499 at161/163 positions,with only the two deposited L-to-M crystallization substitutions; source D178/D215/D246/D272 therefore map locally to D357/D394/D425/D451. No whole-isoform constant offset is assumed. Current N4BP1/KHNYN mapPF11977 and Rae1/YacP PF05991,so historical NYN wording does not authorize their transfer to this family.

### Directed effects and limits

graph: supported. Targets: PF01936.

Each directed relation retains its measured comparator. Human WT/delta-C versus LacZ RNA reduction is distinct from delta-NYN or tandem-mutant increases versus WT; residual activities are not called abolished. The active mouse biochemical preparation includes LOTUS/RRM regions,with expression-host differences retained for the shorter construct. Whole-oocyte Ppp2cb resupply effects are not direct substrate identification. Female mating and oocyte-stage phenotypes remain indirect; Line1/Iap RNA and gammaH2AX foci are unresolved parallel genotype effects,not a transposition-to-damage-to-infertility chain. Increased knockin protein abundance and synonymous marker substitutions remain visible. No decapping/TUT4/7 association is promoted to an experimentally established ordered pathway.

### Remaining family coverage

completeness: concern. Targets: PF01936.

Bacterial CRISPR NYN primary text was read but exact accession/Pfam mapping remains unresolved. LabA clock-output,HspA/HspB with sequence caution,Arabidopsis DNE1 and later EDC4/P-body/MARF1 contexts require followup. Ten reviewed UniProt examples are not all25419 proteins or329 architectures. Other biochemical substrates,metal comparisons,native targets and whole-construct isoforms are not exhaustively curated. Partial source-access failures are not negative research results.

### Cycle 1 causal-graph partner and substrate protein grounding

identity: supported. Targets: PF01936.

Stage 2 (PR #319) grounded Homo sapiens MARF1/EDC4/DCP1A P-body localization nodes edc4-localization (UniProtKB:Q9Y4F3, UniProtKB:Q6P2E9) and dcp1a-pbodies (UniProtKB:Q9NPI6) in human-marf1-edc4-decapping-localization, preserving all domain-mapping and separated mRNA reporter graphs.

## Findings

### additional-contexts: Extend accession-mapped nonmammalian and native-target contexts

minor / open / confirmed; issue key: pf01936-causal-context-coverage.

Resolve the bacterial CRISPR NYN accession and domain before adding its biochemical edges; inspect LabA,DNE1 and HspA primary studies with exact protein mapping; inspect later MARF1/EDC4/P-body assays. Verify full-construct sequences without extending the local mouse NYN offset blindly. Preserve residual activities,expression-host differences,marker alleles and unresolved native targets; retain IN_PROGRESS and all existing followups.

## Recommended Actions And Acceptance Checks

### extend-contexts

Resolve the bacterial CRISPR NYN accession and domain before adding its biochemical edges; inspect LabA,DNE1 and HspA primary studies with exact protein mapping; inspect later MARF1/EDC4/P-body assays. Verify full-construct sequences without extending the local mouse NYN offset blindly. Preserve residual activities,expression-host differences,marker alleles and unresolved native targets; retain IN_PROGRESS and all existing followups.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC6294520/; Human2018 Figures3,5,6 visually inspected and relevant primary Results/Methods read. | supports | Purified human238-510 produces U30 cleavage products,with joint D426A/D427A lowering processing. Full-protein,N-terminal-fragment and protected-poly(A) tethering effects are distinct cellular comparisons; RNA levels are not direct measurements of every decay intermediate or translation-specific effects. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01936/; Accession and domain locations; paired UniProt identity facts | supports | Frozen DUF88/NYN/IPR021139/UNSCORED identity is preserved. Human Q9Y4F3v6 PF01936 353-490 lies inside assayed238-510,not just crystallized352-500. Mouse Q8BJ34v3 maps352-489. PDB5YAA source158-320 matches canonical337-499 at161/163 positions,with only the two deposited L-to-M crystallization substitutions; source D178/D215/D246/D272 therefore map locally to D357/D394/D425/D451. No whole-isoform constant offset is assumed. Current N4BP1/KHNYN mapPF11977 and Rae1/YacP PF05991,so historical NYN wording does not authorize their transfer to this family. |
| mouse-assays-and-genotypes | https://pmc.ncbi.nlm.nih.gov/articles/PMC6217404/; Figures1-5,S5,S6 and supplement pp2-7; local PDB5YAA mapping in identity ledger. | supports | Mouse purified preparations,resupply and knockin outcomes are separate contexts with exact numbering and assay limits. S5 gel/caption and Results2C/actual2D discrepancies are retained. |
| source-coverage | evidence/PF01936/coverage.txt; Scoped source,exclusion,access and followup ledger. | supports | Historical-name cross-family transfers are excluded; uncurated contexts and source-access limits remain explicit rather than family-wide absence claims. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| stage4-prior-review | reviews/structured/20261012T050509Z-pf01936-marf1-domain-mapping-and-separated-rna-phenotypes/review.yaml; Predecessor structured review 20261012T050509Z-pf01936-marf1-domain-mapping-and-separated-rna-phenotypes | supports | Predecessor review 20261012T050509Z-pf01936-marf1-domain-mapping-and-separated-rna-phenotypes verified and linked for finding continuity and semantic-digest progression on PF01936. |
| duf-projection-pf01936 | data/families/PF01936.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Human Figures3/5/6 and mouse Figures1-5/S5/S6 were visually inspected,with relevant primary Results/Methods and mouse supplement pp2-7 read. Human supplemental interaction tables and SEC figures were not inspected; no graph relies on their independent validation. Mouse raw RNA-seq datasets were not reanalyzed. Bacterial figures/supplement and other-member primary sources remain incomplete. Initial PMC attachments returned HTML and short EuropePMC downloads timed out; the longer mouse download succeeded. No experimental replication,clone resequencing or exhaustive family review.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T114817Z-pf01936-stage4-record-review
title: PF01936 Stage 4 frozen-inventory causal-graph and grounding review
started_at: '2026-10-21T11:48:16Z'
finished_at: '2026-10-21T11:48:17Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Claude-Opus-4.6
  independence: self_review
  independence_basis: Stage 4 frozen-inventory record review by Antigravity auditing
    prior Codex/Antigravity curation overlays, primary evidence caches, history events,
    and current projections at Git revision d658f73e7e618d3938704cdb9c86597bf47fc15e.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: true
summary: 'Eight graphs retain22 OBSERVED effects:2 DIRECT,2 INDIRECT and18 UNRESOLVED
  across2 MECHANISTIC and6 PHENOTYPIC contexts. Four ledgers and two OPEN discussions
  retain mapping,experimental and coverage limits. Same-agent partial scientific review;
  IN_PROGRESS,not family-wide completion or publication. Stage 2 (PR #319) grounded
  Homo sapiens MARF1/EDC4/DCP1A P-body localization nodes edc4-localization (UniProtKB:Q9Y4F3,
  UniProtKB:Q6P2E9) and dcp1a-pbodies (UniProtKB:Q9NPI6) in human-marf1-edc4-decapping-localization,
  preserving all domain-mapping and separated mRNA reporter graphs.'
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: d658f73e7e618d3938704cdb9c86597bf47fc15e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01936.yaml
    sha256: d60d81f570b0e665a060010e1cf9d3ffb872adb588e4fa90ec40c53a32d667a5
    role: context
  - path: data/families/PF01936.yaml
    sha256: 2a6707e170dcdbc70daf516da03884db41f4186d90746d1c645b0fd1f7df962f
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
  - path: evidence/PF01936/coverage.txt
    sha256: 3b09628b48989da4946468241ee8696bb44a64768ae0d1a734a07c21d6a2efe2
    role: context
  - path: evidence/PF01936/identity.txt
    sha256: 4aacf75a337b9b27a0f67c6099bc9bf2dda9e008e4e7c6677e85b9f4a67d31e4
    role: context
  - path: evidence/PF01936/nishimura-2018.txt
    sha256: 786f9c70f0e6ccad8a1ba266063a7f8c157e37b8f37fd8bc182eaca5fd5d56f1
    role: context
  - path: evidence/PF01936/yao-2018.txt
    sha256: faafa5f14ac0ec0f9ebfa25438dcd9fc6b03e65566b8d6939233c0805c00a2b6
    role: context
  - path: reviews/structured/20261012T050509Z-pf01936-marf1-domain-mapping-and-separated-rna-phenotypes/review.yaml
    sha256: 5b46425672e65e8facc387ae96c159ce0b106498a4498fff5047d7ee0b6e5e36
    role: context
targets:
- target_id: PF01936
  path: data/families/PF01936.yaml
  label: PF01936
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01936.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: ba54928836a107b1a3229209486efa1eb0d0d3c63e3f300a81b571cd1f846943
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Ascending uncurated Pfam after PF01935; all8296 records and existing
    follow-ups remain in scope.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01936
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Bacterial CRISPR NYN primary text was read but exact accession/Pfam mapping
      remains unresolved. LabA clock-output,HspA/HspB with sequence caution,Arabidopsis
      DNE1 and later EDC4/P-body/MARF1 contexts require followup. Ten reviewed UniProt
      examples are not all25419 proteins or329 architectures. Other biochemical substrates,metal
      comparisons,native targets and whole-construct isoforms are not exhaustively
      curated. Partial source-access failures are not negative research results.
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
  - PF01936
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6294520/
  locator: Human2018 Figures3,5,6 visually inspected and relevant primary Results/Methods
    read.
  accessed_at: '2026-10-12T05:05:09Z'
  support: supports
  snapshot_sha256: 786f9c70f0e6ccad8a1ba266063a7f8c157e37b8f37fd8bc182eaca5fd5d56f1
  summary: Purified human238-510 produces U30 cleavage products,with joint D426A/D427A
    lowering processing. Full-protein,N-terminal-fragment and protected-poly(A) tethering
    effects are distinct cellular comparisons; RNA levels are not direct measurements
    of every decay intermediate or translation-specific effects.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01936/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-12T05:05:09Z'
  support: supports
  snapshot_sha256: 4aacf75a337b9b27a0f67c6099bc9bf2dda9e008e4e7c6677e85b9f4a67d31e4
  summary: Frozen DUF88/NYN/IPR021139/UNSCORED identity is preserved. Human Q9Y4F3v6
    PF01936 353-490 lies inside assayed238-510,not just crystallized352-500. Mouse
    Q8BJ34v3 maps352-489. PDB5YAA source158-320 matches canonical337-499 at161/163
    positions,with only the two deposited L-to-M crystallization substitutions; source
    D178/D215/D246/D272 therefore map locally to D357/D394/D425/D451. No whole-isoform
    constant offset is assumed. Current N4BP1/KHNYN mapPF11977 and Rae1/YacP PF05991,so
    historical NYN wording does not authorize their transfer to this family.
- evidence_id: mouse-assays-and-genotypes
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6217404/
  locator: Figures1-5,S5,S6 and supplement pp2-7; local PDB5YAA mapping in identity
    ledger.
  summary: Mouse purified preparations,resupply and knockin outcomes are separate
    contexts with exact numbering and assay limits. S5 gel/caption and Results2C/actual2D
    discrepancies are retained.
  accessed_at: '2026-10-12T05:05:09Z'
  support: supports
  snapshot_sha256: faafa5f14ac0ec0f9ebfa25438dcd9fc6b03e65566b8d6939233c0805c00a2b6
- evidence_id: source-coverage
  kind: search
  reference: evidence/PF01936/coverage.txt
  locator: Scoped source,exclusion,access and followup ledger.
  search_scope: PF01936,DUF88,NYN,MARF1,N4BP1,KHNYN,Rae1,LabA,DNE1,bacterial CRISPR
    NYN and current primary family/member records; scoped ignored/hidden-inclusive
    local text search with inputs/JSON excluded.
  summary: Historical-name cross-family transfers are excluded; uncurated contexts
    and source-access limits remain explicit rather than family-wide absence claims.
  accessed_at: '2026-10-12T05:05:09Z'
  support: supports
  snapshot_sha256: 3b09628b48989da4946468241ee8696bb44a64768ae0d1a734a07c21d6a2efe2
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-12T05:05:09Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: stage4-prior-review
  kind: prior_review
  reference: reviews/structured/20261012T050509Z-pf01936-marf1-domain-mapping-and-separated-rna-phenotypes/review.yaml
  locator: Predecessor structured review 20261012T050509Z-pf01936-marf1-domain-mapping-and-separated-rna-phenotypes
  accessed_at: '2026-10-21T11:48:17Z'
  support: supports
  snapshot_sha256: 5b46425672e65e8facc387ae96c159ce0b106498a4498fff5047d7ee0b6e5e36
  summary: Predecessor review 20261012T050509Z-pf01936-marf1-domain-mapping-and-separated-rna-phenotypes
    verified and linked for finding continuity and semantic-digest progression on
    PF01936.
- evidence_id: duf-projection-pf01936
  kind: record_content
  reference: data/families/PF01936.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-21T11:48:17Z'
  support: context_only
  snapshot_sha256: 2a6707e170dcdbc70daf516da03884db41f4186d90746d1c645b0fd1f7df962f
  quote: "id: Pfam:PF01936\npfam_id: PF01936\nname: NYN domain\nshort_name: NYN\n\
    seed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status: IN_PROGRESS\n\
    source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01936\ncounters:\n\
    \  proteins: 25419\n  matches: 25756\n  proteomes: 13584\n  taxa: 22386\n  structures:\
    \ 3\n  alphafold_models: 16110\n  domain_architectures: 329\nprovenance:\n  snapshot_id:\
    \ interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR021139\ndescription: These domains are found in the eukaryotic\
    \ proteins typified by the Nedd4-binding protein\n  1 and the bacterial YacP-like\
    \ proteins (Nedd4-BP1, YacP nucleases; NYN domains). The NYN domain shares\n \
    \ a common protein fold with two other previously characterized groups of nucleases,\
    \ namely the PIN (PilT\n  N-terminal) and FLAP/5' --> 3' exonuclease superfamilies.\
    \ These proteins share a common set of 4 acidic\n  conserved residues that are\
    \ predicted to constitute their active site. Based on the conservation of\n  the\
    \ acidic residues and structural elements Aravind and colleagues suggest that\
    \ PIN and NYN domains\n  are likely to bind only a single metal ion, unlike the\
    \ FLAP/5' --> 3' exonuclease superfamily, which\n  binds two metal ions. Based\
    \ on conserved gene neighborhoods Aravind and colleagues infer that the bacterial\n\
    \  members are likely to be components of the processome/degradsome that process\
    \ tRNAs or ribosomal RNAs.\ncuration_history: history/records/PF01936\ndiscussions:\n\
    - discussion_id: pf01936-member-mapping-and-native-targets\n  prompt: Resolve\
    \ native RNA targets and construct-specific effects without transferring historical\
    \ NYN\n    names across Pfam families.\n  kind: CURATION_TODO\n  status: OPEN\n\
    \  rationale: Human tethering and mouse genotype effects do not directly establish\
    \ every downstream cleavage\n    step or family-wide substrate specificity.\n\
    \  evidence:\n  - reference: PMID:30364987\n    supports: PARTIAL\n    evidence_source:\
    \ primary_biochemical_and_tethering_assays\n    explanation: Human238-510 cleavage\
    \ differs from crystallized352-500 and full-protein tethering. Decapping\n   \
    \   interactions alone do not establish a required catalytic chain.\n  - reference:\
    \ PMID:30333187\n    supports: PARTIAL\n    evidence_source: primary_assays_and_supplement\n\
    \    explanation: Mouse source D272 maps locally to canonical D451; increased\
    \ mutant protein abundance,\n      expression-host differences and direct-target\
    \ uncertainty remain material.\n  posed_by: Codex\n  posed_date: '2026-10-12'\n\
    \  notes: N4BP1/KHNYN map to PF11977 and Rae1/YacP to PF05991 in inspected current\
    \ records. Preserve frozen\n    description. Inspect later EDC4/P-body studies\
    \ and sequence-verify whole constructs before extending\n    mappings beyond the\
    \ local NYN interval.\n- discussion_id: pf01936-other-member-contexts\n  prompt:\
    \ Extend accession-mapped bacterial, plant and clock-output contexts.\n  kind:\
    \ CURATION_TODO\n  status: OPEN\n  rationale: Two mammalian examples do not characterize25419\
    \ proteins and329 architectures.\n  evidence:\n  - reference: PMID:38785320\n\
    \    supports: PARTIAL\n    evidence_source: primary_text_and_figure_captions\n\
    \    explanation: Bacterial CRISPR-associated NYN cleavage is a lead; exact tested\
    \ accession/Pfam mapping\n      remains unresolved here. Physiological crRNA maturation\
    \ is not established by free-RNA digestion.\n  - reference: PMID:17210789\n  \
    \  supports: PARTIAL\n    evidence_source: mapped_member_and_primary_source_lead\n\
    \    explanation: LabA clock-output phenotypes need inspection and must not be\
    \ converted into an assumed\n      RNase mechanism.\n  posed_by: Codex\n  posed_date:\
    \ '2026-10-12'\n  notes: Also resolve HspA/HspB and HspA N-terminal sequence caution,\
    \ Arabidopsis DNE1, other architectures\n    and omitted mammalian contexts. Failed\
    \ source access is not negative evidence; see coverage ledger.\ncausal_graphs:\n\
    - graph_id: human-marf1-fragment-cleavage-2018\n  title: Human MARF1 fragment\
    \ cleaves U30 RNA\n  scope: Nishimura2018 Figure5B-D; purified WT238-510 and D426A/D427A\
    \ fragment.\n  context: 1uM protein,10pmol cold and0.1pmol labeled U30 in10uL,3mM\
    \ MnCl2,20mM HEPES pH7.5,150mM NaCl,10%glycerol,1mM\n    DTT; room temperature,1-60min.\
    \ GST removed; no-protein controls and5-prime/3-prime labels.\n  family_mapping:\
    \ Human Q9Y4F3v6,1742aa,PF01936 353-490 inside assayed238-510. D426/D427 are within\
    \ the\n    match. This is not the352-500 crystallization construct or an assay\
    \ of full-length MARF1.\n  taxon: NCBITaxon:9606\n  scope_status: MECHANISTIC\n\
    \  limitations: Internal cleavage is supported by paired end-label patterns, not\
    \ resolved atomic chemistry.\n    D426A/D427A is one double-mutant test and retains\
    \ residual activity. No-added-metal activity is not\n    absent; Mg also supports5B\
    \ cleavage. Folding and natural-target specificity remain unresolved.\n  nodes:\n\
    \  - node_id: reaction\n    label: WT238-510 plus U30 and Mn under assay conditions\n\
    \    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:Q9Y4F3\n  - node_id:\
    \ products\n    label: Shorter labeled U30 RNA products\n    node_type: STATE\n\
    \  - node_id: mutant\n    label: D426A/D427A instead of WT fragment\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:Q9Y4F3\n  - node_id: processing\n\
    \    label: U30 processing relative to WT in Mn\n    node_type: PHENOTYPE\n  edges:\n\
    \  - edge_id: fragment-rna-cleavage\n    subject: reaction\n    predicate: produces\n\
    \    object: products\n    mechanism: The purified fragment-containing reaction\
    \ cleaves U30 to shorter products; both end-label\n      orientations support\
    \ endoribonuclease activity.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:30364987\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6294520/\n      snippet:\
    \ strongly reduced as compared to\n      explanation: Figure5B,D and recombinant/ribonuclease\
    \ Methods; complete protein-substrate-cofactor\n        context retained.\n  \
    \    cache_path: evidence/PF01936/nishimura-2018.txt\n      cache_sha256: 786f9c70f0e6ccad8a1ba266063a7f8c157e37b8f37fd8bc182eaca5fd5d56f1\n\
    \  - edge_id: tandem-mutation-processing-reduction\n    subject: mutant\n    predicate:\
    \ decreases\n    object: processing\n    mechanism: Joint alanine replacement\
    \ lowers RNA processing compared with the matched WT preparation\n      without\
    \ isolating either residue's individual contribution.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:30364987\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6294520/\n\
    \      snippet: strongly reduced as compared to\n      explanation: Figure5C WT/MUT\
    \ timecourses;5A purification gel. Residual cleavage is not called complete\n\
    \        inactivity.\n      cache_path: evidence/PF01936/nishimura-2018.txt\n\
    \      cache_sha256: 786f9c70f0e6ccad8a1ba266063a7f8c157e37b8f37fd8bc182eaca5fd5d56f1\n\
    - graph_id: human-marf1-full-tethering-2018\n  title: Tethered human MARF1 lowers\
    \ reporter RNA\n  scope: Nishimura2018 Figure3; full-length and deletion constructs\
    \ in HeLa.\n  context: lambdaN-HA fusions tethered to RL-5BoxB3-primeUTR;24h transfection,firefly\
    \ normalization,Northern\n    blot and expression controls,at least3 experiments.\
    \ LacZ and WT are explicitly different comparators.\n  family_mapping: Q9Y4F3v6,1742aa,PF01936\
    \ 353-490. Full-length and delta-C1-1563 retain the NYN domain;\n    delta-NYN\
    \ removes it. Exact NYN deletion junction not sequence-verified here.\n  taxon:\
    \ NCBITaxon:9606\n  scope_status: PHENOTYPIC\n  limitations: RNA abundance is\
    \ measured, not native target recognition, cleavage position or necessity\n  \
    \  of decapping partners. Delta-NYN only partially restores levels. Luciferase\
    \ changes are not recast\n    as translation-specific mechanisms.\n  nodes:\n\
    \  - node_id: wt\n    label: Tethered full MARF1 instead of LacZ\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:Q9Y4F3\n  - node_id: dc\n    label:\
    \ Tethered delta-C MARF1 instead of LacZ\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q9Y4F3\n  - node_id: dn\n    label: Delta-NYN instead of tethered\
    \ WT MARF1\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q9Y4F3\n\
    \  - node_id: rna\n    label: Normalized RL-5BoxB RNA abundance\n    node_type:\
    \ PHENOTYPE\n  edges:\n  - edge_id: wt-reporter-reduction\n    subject: wt\n \
    \   predicate: decreases\n    object: rna\n    mechanism: Tethering full MARF1\
    \ lowers reporter RNA relative to the LacZ fusion control.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:30364987\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6294520/\n\
    \      snippet: strongly reduced as compared to\n      explanation: Figure3D RNA\
    \ bars and3E Northern;3C expression controls.\n      cache_path: evidence/PF01936/nishimura-2018.txt\n\
    \      cache_sha256: 786f9c70f0e6ccad8a1ba266063a7f8c157e37b8f37fd8bc182eaca5fd5d56f1\n\
    \  - edge_id: dc-reporter-reduction\n    subject: dc\n    predicate: decreases\n\
    \    object: rna\n    mechanism: The tethered construct lacking the decapping-factor\
    \ interaction region still lowers reporter\n      RNA relative to LacZ.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:30364987\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6294520/\n\
    \      snippet: strongly reduced as compared to\n      explanation: Figure3B defines1-1563;3D,E\
    \ show reduced RNA, arguing against obligatory C-terminal\n        recruitment\
    \ in this tethering assay.\n      cache_path: evidence/PF01936/nishimura-2018.txt\n\
    \      cache_sha256: 786f9c70f0e6ccad8a1ba266063a7f8c157e37b8f37fd8bc182eaca5fd5d56f1\n\
    \  - edge_id: nyn-deletion-reporter-increase\n    subject: dn\n    predicate:\
    \ increases\n    object: rna\n    mechanism: Removing NYN increases steady-state\
    \ reporter RNA compared with tethered full WT MARF1,\n      without establishing\
    \ complete restoration to LacZ.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:30364987\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6294520/\n      snippet:\
    \ strongly reduced as compared to\n      explanation: Figure3D,E delta-NYN versus\
    \ WT, not versus LacZ.\n      cache_path: evidence/PF01936/nishimura-2018.txt\n\
    \      cache_sha256: 786f9c70f0e6ccad8a1ba266063a7f8c157e37b8f37fd8bc182eaca5fd5d56f1\n\
    - graph_id: human-marf1-nterm-tethering-2018\n  title: NYN variants impair N-terminal-fragment\
    \ reporter silencing\n  scope: Nishimura2018 Figure6A-C; tethered human N-terminal\
    \ fragment, not full-length variants.\n  context: HeLa RL-5BoxB Northern normalized\
    \ to firefly,24h,at least3 experiments; LacZ fusion and anti-HA/actin\n    expression\
    \ controls.\n  family_mapping: Human Q9Y4F3v6,PF01936 353-490 retained in WT N-terminal\
    \ fragment; D426A/D427A is a\n    joint in-domain substitution. Deletion construct\
    \ boundaries are not sequence-verified in this pass.\n  taxon: NCBITaxon:9606\n\
    \  scope_status: PHENOTYPIC\n  limitations: Effects on RNA abundance do not resolve\
    \ cleavage versus downstream decay or protein-folding\n    alternatives. Do not\
    \ transfer the N-terminal mutant outcome to an untested full-length variant.\n\
    \  nodes:\n  - node_id: wt\n    label: WT N-terminal fragment instead of LacZ\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q9Y4F3\n  - node_id:\
    \ dn\n    label: NYN-deleted instead of WT N-terminal fragment\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:Q9Y4F3\n  - node_id: mut\n   \
    \ label: D426A/D427A instead of WT N-terminal fragment\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q9Y4F3\n  - node_id: rna\n    label: Normalized\
    \ RL-5BoxB RNA abundance\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: nterm-rna-reduction\n\
    \    subject: wt\n    predicate: decreases\n    object: rna\n    mechanism: Tethering\
    \ the WT N-terminal fragment lowers reporter RNA relative to LacZ.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:30364987\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6294520/\n\
    \      snippet: strongly reduced as compared to\n      explanation: Figure6B RNA\
    \ bars,6C Northern,6A expression.\n      cache_path: evidence/PF01936/nishimura-2018.txt\n\
    \      cache_sha256: 786f9c70f0e6ccad8a1ba266063a7f8c157e37b8f37fd8bc182eaca5fd5d56f1\n\
    \  - edge_id: nterm-deletion-rna-increase\n    subject: dn\n    predicate: increases\n\
    \    object: rna\n    mechanism: NYN deletion increases reporter RNA relative\
    \ to the intact N-terminal fragment under tethering\n      conditions.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:30364987\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6294520/\n\
    \      snippet: strongly reduced as compared to\n      explanation: Figure6B,C\
    \ delta-NYN versus N-term WT.\n      cache_path: evidence/PF01936/nishimura-2018.txt\n\
    \      cache_sha256: 786f9c70f0e6ccad8a1ba266063a7f8c157e37b8f37fd8bc182eaca5fd5d56f1\n\
    \  - edge_id: nterm-tandem-mutation-rna-increase\n    subject: mut\n    predicate:\
    \ increases\n    object: rna\n    mechanism: Joint D426A/D427A replacement increases\
    \ reporter RNA relative to the WT N-terminal fragment.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:30364987\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6294520/\n\
    \      snippet: strongly reduced as compared to\n      explanation: Figure6B,C\
    \ N-term MUT versus N-term WT; not two single-residue tests.\n      cache_path:\
    \ evidence/PF01936/nishimura-2018.txt\n      cache_sha256: 786f9c70f0e6ccad8a1ba266063a7f8c157e37b8f37fd8bc182eaca5fd5d56f1\n\
    - graph_id: human-marf1-internal-polya-reporter-2018\n  title: MARF1 lowers an\
    \ internally polyadenylated reporter RNA\n  scope: Nishimura2018 Figure6D-G; protected-poly(A)\
    \ reporter in HeLa.\n  context: RL-5BoxB-A114-N40-HHR with self-cleaved ribozyme,lambdaN-HA\
    \ MARF1 or delta-C,LacZ control,firefly\n    normalization,24h,at least3 experiments.\n\
    \  family_mapping: Human Q9Y4F3v6,PF01936 353-490 in full-length and1-1563 delta-C\
    \ constructs; no mutation-specific\n    comparison in this reporter panel.\n \
    \ taxon: NCBITaxon:9606\n  scope_status: PHENOTYPIC\n  limitations: Protected\
    \ internal poly(A) supports a route not requiring usual terminal deadenylation,\n\
    \    not a directly observed complete decay chain. GW182-SD lowers luciferase\
    \ but does not lower reporter\n    RNA here.\n  nodes:\n  - node_id: wt\n    label:\
    \ Full MARF1 tethering instead of LacZ\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q9Y4F3\n  - node_id: dc\n    label: Delta-C MARF1 tethering instead\
    \ of LacZ\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q9Y4F3\n\
    \  - node_id: rna\n    label: Normalized A114-N40-HHR reporter RNA\n    node_type:\
    \ PHENOTYPE\n  edges:\n  - edge_id: wt-internal-polya-rna-reduction\n    subject:\
    \ wt\n    predicate: decreases\n    object: rna\n    mechanism: Tethered full\
    \ MARF1 lowers the reporter with an internal protected poly(A) tract relative\n\
    \      to LacZ.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:30364987\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC6294520/\n      snippet: strongly reduced\
    \ as compared to\n      explanation: Figure6D reporter design,6F RNA bars,6G Northern\
    \ and6E expression.\n      cache_path: evidence/PF01936/nishimura-2018.txt\n \
    \     cache_sha256: 786f9c70f0e6ccad8a1ba266063a7f8c157e37b8f37fd8bc182eaca5fd5d56f1\n\
    \  - edge_id: dc-internal-polya-rna-reduction\n    subject: dc\n    predicate:\
    \ decreases\n    object: rna\n    mechanism: Delta-C MARF1 retains RNA-lowering\
    \ activity in the protected-poly(A) context relative to\n      LacZ.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:30364987\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6294520/\n\
    \      snippet: strongly reduced as compared to\n      explanation: Figure6F,G\
    \ delta-C versus LacZ, with GW182-SD distinguishing RNA abundance from luciferase\n\
    \        activity.\n      cache_path: evidence/PF01936/nishimura-2018.txt\n  \
    \    cache_sha256: 786f9c70f0e6ccad8a1ba266063a7f8c157e37b8f37fd8bc182eaca5fd5d56f1\n\
    - graph_id: mouse-marf1-fragment-cleavage-2018\n  title: Mouse multidomain MARF1\
    \ preparation cleaves H49 RNA\n  scope: Yao2018 Figures1B,C and2D; source158-1381\
    \ WT and individual aspartate variants.\n  context: Sf9-expressed purified preparation,20nM49nt\
    \ H49 RNA,20mM Tris-HCl pH7.5,150mM NaCl,1mM DTT,1mM\n    MgCl2,37C. Standard5min;\
    \ Figure1B0-1uM and1C0.05uM timecourse; Figure2D enzyme concentration not explicit.\n\
    \  family_mapping: Mouse Q8BJ34v3,1730aa,PF01936 352-489. PDB5YAA source158-320\
    \ maps to canonical337-499\n    with only two known crystallization substitutions.\
    \ Source D178/D215/D246/D272 map to D357/D394/D425/D451\n    within PF01936; do\
    \ not extend the local offset to whole isoforms.\n  taxon: NCBITaxon:10090\n \
    \ scope_status: MECHANISTIC\n  limitations: Active source158-1381 includes RRM/LOTUS\
    \ regions, not isolated NYN or full canonical1730aa.\n    Mutant purification\
    \ gel does not exclude folding effects; lowered products are not an atomic catalytic\n\
    \    model. Main2D is the activity panel despite a Results2C citation; S5 gel\
    \ is visiblyB despite captionC.\n  nodes:\n  - node_id: reaction\n    label: WT\
    \ source158-1381 plus H49 and Mg\n    node_type: ACTIVITY\n    grounding:\n  \
    \  - UniProtKB:Q8BJ34\n  - node_id: products\n    label: Shorter labeled H49 products\n\
    \    node_type: STATE\n  - node_id: d178a\n    label: Source D178A replacing WT\
    \ in158-1381\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q8BJ34\n\
    \  - node_id: d215a\n    label: Source D215A replacing WT in158-1381\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:Q8BJ34\n  - node_id: d246a\n \
    \   label: Source D246A replacing WT in158-1381\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q8BJ34\n  - node_id: d272a\n    label: Source\
    \ D272A replacing WT in158-1381\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q8BJ34\n  - node_id: processing\n    label: H49 processing relative\
    \ to WT preparation\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: mouse-fragment-rna-cleavage\n\
    \    subject: reaction\n    predicate: produces\n    object: products\n    mechanism:\
    \ The purified multidomain preparation cleaves H49 RNA under the specified Mg-containing\n\
    \      conditions.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:30333187\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC6217404/\n      snippet: D178, D215,\
    \ D246, and D272\n      explanation: Figure1B,C no-protein,dose and time comparisons;\
    \ supplement pp3-5 purification and\n        buffer.1E separately supports internal\
    \ cleavage of circular RNA.\n      cache_path: evidence/PF01936/yao-2018.txt\n\
    \      cache_sha256: faafa5f14ac0ec0f9ebfa25438dcd9fc6b03e65566b8d6939233c0805c00a2b6\n\
    \  - edge_id: d178a-rna-processing-reduction\n    subject: d178a\n    predicate:\
    \ decreases\n    object: processing\n    mechanism: Source D178A lowers H49 cleavage\
    \ relative to WT; local sequence mapping identifies canonical\n      D357.\n \
    \   directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:30333187\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6217404/\n\
    \      snippet: D178, D215, D246, and D272\n      explanation: Figure2D D178A\
    \ versus WT,with purification gel inS5 and mapping in identity ledger.\n     \
    \ cache_path: evidence/PF01936/yao-2018.txt\n      cache_sha256: faafa5f14ac0ec0f9ebfa25438dcd9fc6b03e65566b8d6939233c0805c00a2b6\n\
    \  - edge_id: d215a-rna-processing-reduction\n    subject: d215a\n    predicate:\
    \ decreases\n    object: processing\n    mechanism: Source D215A lowers H49 cleavage\
    \ relative to WT; local mapping identifies canonical D394.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:30333187\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6217404/\n\
    \      snippet: D178, D215, D246, and D272\n      explanation: Figure2D D215A\
    \ versus WT; purified variant is not proof of equal folding.\n      cache_path:\
    \ evidence/PF01936/yao-2018.txt\n      cache_sha256: faafa5f14ac0ec0f9ebfa25438dcd9fc6b03e65566b8d6939233c0805c00a2b6\n\
    \  - edge_id: d246a-rna-processing-reduction\n    subject: d246a\n    predicate:\
    \ decreases\n    object: processing\n    mechanism: Source D246A lowers H49 cleavage\
    \ relative to WT; local mapping identifies canonical D425.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:30333187\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6217404/\n\
    \      snippet: D178, D215, D246, and D272\n      explanation: Figure2D D246A\
    \ versus WT under the source nuclease-assay protocol.\n      cache_path: evidence/PF01936/yao-2018.txt\n\
    \      cache_sha256: faafa5f14ac0ec0f9ebfa25438dcd9fc6b03e65566b8d6939233c0805c00a2b6\n\
    \  - edge_id: d272a-rna-processing-reduction\n    subject: d272a\n    predicate:\
    \ decreases\n    object: processing\n    mechanism: Source D272A lowers H49 cleavage\
    \ relative to WT; local mapping identifies canonical D451.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:30333187\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6217404/\n\
    \      snippet: D178, D215, D246, and D272\n      explanation: Figure2D D272A\
    \ versus WT; the biochemical fragment is not the mouse knockin genotype.\n   \
    \   cache_path: evidence/PF01936/yao-2018.txt\n      cache_sha256: faafa5f14ac0ec0f9ebfa25438dcd9fc6b03e65566b8d6939233c0805c00a2b6\n\
    - graph_id: mouse-marf1-lotus-truncation-2018\n  title: A shorter mouse construct\
    \ has reduced RNA-processing activity\n  scope: Yao2018 Figure1F; source158-690\
    \ compared with158-1381.\n  context: Matched0.1/0.5uM preparations,20nM H49,1mM\
    \ MgCl2,Tris pH7.5,150mM NaCl,1mM DTT,37C5min. Longer\n    fragment from Sf9;\
    \ shorter fragment from E.coli with His6-SUMO removed.\n  family_mapping: Q8BJ34v3\
    \ PF01936 352-489 maps within source158-320 in both constructs. The deleted source691-1381\n\
    \    segment includes LOTUS domains and lies outside NYN; whole-construct comparison,not\
    \ an isolated-domain\n    knockout.\n  taxon: NCBITaxon:10090\n  scope_status:\
    \ PHENOTYPIC\n  limitations: The experiment supports a preparation-dependent activity\
    \ difference,not a direct LOTUS-catalysis\n    step. Different expression hosts,folding\
    \ and RNA recruitment may contribute. Do not contradict human238-510\n    activity\
    \ by generalizing this negative result.\n  nodes:\n  - node_id: shorter\n    label:\
    \ Source158-690 instead of158-1381 preparation\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q8BJ34\n  - node_id: processing\n    label: H49\
    \ cleavage products at matched protein concentration\n    node_type: PHENOTYPE\n\
    \  edges:\n  - edge_id: shortened-preparation-processing-reduction\n    subject:\
    \ shorter\n    predicate: decreases\n    object: processing\n    mechanism: The\
    \ shorter preparation yields much less cleaved RNA than the LOTUS-containing preparation\n\
    \      at matched protein concentration.\n    directness: UNRESOLVED\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:30333187\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6217404/\n      snippet:\
    \ D178, D215, D246, and D272\n      explanation: Figure1F158-690 versus158-1381\
    \ lanes and supplement pp3-5 expression/purification conditions;\n        not\
    \ LOTUS-only sufficiency.\n      cache_path: evidence/PF01936/yao-2018.txt\n \
    \     cache_sha256: faafa5f14ac0ec0f9ebfa25438dcd9fc6b03e65566b8d6939233c0805c00a2b6\n\
    - graph_id: mouse-marf1-oocyte-resupply-2018\n  title: WT Marf1 resupply lowers\
    \ Ppp2cb RNA in gene-trap oocytes\n  scope: Yao2018 Figure3C; fully-grown GV-stage\
    \ Marf1GT/GT oocytes.\n  context: Approximately10pL WT Marf1 mRNA at500ng/uL per\
    \ oocyte;40h culture with5uM milrinone maintaining\n    GV arrest;qRT-PCR,three\
    \ sample sets. D272A mRNA is a non-rescuing comparison.\n  family_mapping: Mouse\
    \ Marf1 Q8BJ34v3 carries PF01936 352-489; source D272 maps locally to canonical\n\
    \    D451. Whole Marf1 mRNA resupply,not isolated NYN delivery; whole-isoform\
    \ sequence equivalence remains\n    unchecked.\n  taxon: NCBITaxon:10090\n  scope_status:\
    \ PHENOTYPIC\n  limitations: Steady-state Ppp2cb RNA reduction is not direct proof\
    \ of cleavage of that transcript. Native\n    targets and possible transcriptional\
    \ effects remain unresolved; no edge joins this readout to meiotic\n    rescue\
    \ under GV-arrest culture.\n  nodes:\n  - node_id: wt\n    label: WT Marf1 mRNA\
    \ resupply versus untreated gene-trap oocytes\n    node_type: PERTURBATION\n \
    \   grounding:\n    - UniProtKB:Q8BJ34\n  - node_id: ppp2cb\n    label: Ppp2cb\
    \ steady-state RNA abundance\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ resupply-ppp2cb-reduction\n    subject: wt\n    predicate: decreases\n    object:\
    \ ppp2cb\n    mechanism: WT Marf1 resupply lowers the validated Ppp2cb RNA readout\
    \ relative to untreated gene-trap\n      oocytes; D272A resupply does not reproduce\
    \ the decrease.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:30333187\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC6217404/\n      snippet: D178, D215,\
    \ D246, and D272\n      explanation: Figure3C Ppp2cb bars; supplement pp6-7 mRNA\
    \ injection,culture and qPCR. RNA-seq population\n        effects are not all\
    \ treated as direct substrates.\n      cache_path: evidence/PF01936/yao-2018.txt\n\
    \      cache_sha256: faafa5f14ac0ec0f9ebfa25438dcd9fc6b03e65566b8d6939233c0805c00a2b6\n\
    - graph_id: mouse-marf1-knockin-phenotypes-2018\n  title: Marf1 D272A knockin\
    \ changes reproductive and oocyte readouts\n  scope: Yao2018 Figures4,5A-B andS6;\
    \ homozygous knockin versus WT females.\n  context: B6DBA2-background engineered\
    \ allele includes two synonymous marker changes. Three females/genotype\n    mated\
    \ from6weeks to proven-fertile males; main4C8months versus supplement8-10months.\
    \ Fully-grown GV\n    oocytes for RNA/foci; ovulated complexes for stage assessment.\n\
    \  family_mapping: Source Marf1 D272A maps to canonical Q8BJ34v3 D451 within PF01936\
    \ 352-489 through local\n    PDB5YAA mapping. Whole-animal allele is not purified\
    \ NYN and is distinct from the crystallographic\n    substitutions.\n  taxon:\
    \ NCBITaxon:10090\n  scope_status: PHENOTYPIC\n  limitations: These are parallel\
    \ genotype effects,not a LINE1-to-damage-to-infertility causal chain.\n    MARF1\
    \ protein increases despite unchanged Marf1 RNA. Ovulation is not abolished; compound\
    \ GT/D272A\n    also has the reproductive phenotype but does not exclude every\
    \ background alternative. GammaH2AX is\n    a marker,not direct transposition\
    \ measurement.\n  nodes:\n  - node_id: knockin\n    label: Homozygous source D272A\
    \ knockin instead of WT\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q8BJ34\n\
    \  - node_id: offspring\n    label: Offspring production during female mating\
    \ assay\n    node_type: PHENOTYPE\n  - node_id: maturation\n    label: Meiotic\
    \ maturation of ovulated oocytes beyond GV\n    node_type: PHENOTYPE\n  - node_id:\
    \ line1\n    label: Line1 RNA abundance in GV oocytes\n    node_type: PHENOTYPE\n\
    \  - node_id: iap\n    label: Iap RNA abundance in GV oocytes\n    node_type:\
    \ PHENOTYPE\n  - node_id: foci\n    label: GammaH2AX-positive focus counts in\
    \ GV oocytes\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: knockin-offspring-reduction\n\
    \    subject: knockin\n    predicate: decreases\n    object: offspring\n    mechanism:\
    \ The homozygous knockin females produce no offspring in the tested mating interval;\
    \ this\n      is a distal organism-level consequence,not direct nuclease chemistry.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:30333187\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6217404/\n\
    \      snippet: D178, D215, D246, and D272\n      explanation: Figure4C mating\
    \ outcome and supplement pp2-3; GT/D272A comparator supports locus association\n\
    \        without proving all intermediates.\n      cache_path: evidence/PF01936/yao-2018.txt\n\
    \      cache_sha256: faafa5f14ac0ec0f9ebfa25438dcd9fc6b03e65566b8d6939233c0805c00a2b6\n\
    \  - edge_id: knockin-meiotic-maturation-reduction\n    subject: knockin\n   \
    \ predicate: decreases\n    object: maturation\n    mechanism: Ovulated knockin\
    \ oocytes retain immature GV features rather than normal mature features,indicating\n\
    \      impaired meiotic progression without an asserted RNA-to-meiosis intermediate.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:30333187\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6217404/\n\
    \      snippet: D178, D215, D246, and D272\n      explanation: Figure4D-G andS6C\
    \ histology; ovulation occurs and is not modeled as absent.\n      cache_path:\
    \ evidence/PF01936/yao-2018.txt\n      cache_sha256: faafa5f14ac0ec0f9ebfa25438dcd9fc6b03e65566b8d6939233c0805c00a2b6\n\
    \  - edge_id: knockin-line1-rna-increase\n    subject: knockin\n    predicate:\
    \ increases\n    object: line1\n    mechanism: The knockin increases steady-state\
    \ Line1 RNA in sampled GV oocytes without demonstrating\n      direct RNA cleavage\
    \ or transposition frequency.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:30333187\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6217404/\n      snippet:\
    \ D178, D215, D246, and D272\n      explanation: Figure5A Line1 qRT-PCR,knockin\
    \ versus WT; supplement p7 sampling.\n      cache_path: evidence/PF01936/yao-2018.txt\n\
    \      cache_sha256: faafa5f14ac0ec0f9ebfa25438dcd9fc6b03e65566b8d6939233c0805c00a2b6\n\
    \  - edge_id: knockin-iap-rna-increase\n    subject: knockin\n    predicate: increases\n\
    \    object: iap\n    mechanism: The knockin increases steady-state Iap RNA in\
    \ GV oocytes; the causal molecular path remains\n      unresolved.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:30333187\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6217404/\n\
    \      snippet: D178, D215, D246, and D272\n      explanation: Figure5A Iap qRT-PCR,knockin\
    \ versus WT; distinct from the gene-trap comparison.\n      cache_path: evidence/PF01936/yao-2018.txt\n\
    \      cache_sha256: faafa5f14ac0ec0f9ebfa25438dcd9fc6b03e65566b8d6939233c0805c00a2b6\n\
    \  - edge_id: knockin-gammah2ax-foci-increase\n    subject: knockin\n    predicate:\
    \ increases\n    object: foci\n    mechanism: Knockin GV oocytes have more gammaH2AX-positive\
    \ foci under matched imaging conditions;\n      no direct edge from retrotransposon\
    \ RNA or measured transposition is inferred.\n    directness: UNRESOLVED\n   \
    \ support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:30333187\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6217404/\n\
    \      snippet: D178, D215, D246, and D272\n      explanation: Figure5B images/focus-count\
    \ bins and supplement p7 staining; explicitly a DNA-damage-associated\n      \
    \  marker.\n      cache_path: evidence/PF01936/yao-2018.txt\n      cache_sha256:\
    \ faafa5f14ac0ec0f9ebfa25438dcd9fc6b03e65566b8d6939233c0805c00a2b6\ncuration_events:\n\
    - timestamp: '2026-10-12T04:50:30Z'\n  curator: Codex\n  action: CREATE\n  outcome:\
    \ changed\n  summary: Add scoped MARF1 causal contexts for PF01936 without historical\
    \ NYN cross-family transfers.\n  history_record: history/records/PF01936/2026-10-12T045030Z-codex-eba42f.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-12T05:05:20Z'\n\
    \  curator: Codex\n  action: REVIEW\n  outcome: needs_followup\n  summary: Retain\
    \ partial scientific review of mapped MARF1 causal contexts for PF01936.\n  history_record:\
    \ history/records/PF01936/2026-10-12T050520Z-codex-4654b7.yaml\n  event_index:\
    \ 0\n  llm_assisted: true\n- timestamp: '2026-10-18T02:54:46Z'\n  curator: Antigravity\n\
    \  action: EDIT\n  outcome: changed\n  summary: Ground causal graph gene and protein\
    \ nodes in PF01936 with verified UniProtKB accessions (UniProtKB:Q9Y4F3,\n   \
    \ UniProtKB:Q8BJ34)\n  history_record: history/records/PF01936/2026-10-18T025446Z-antigravity-b04c48.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-21T07:32:29Z'\n\
    \  curator: Antigravity\n  action: EDIT\n  outcome: changed\n  summary: Ground\
    \ human and mouse MARF1 perturbation nodes to UniProtKB:Q9Y4F3 and UniProtKB:Q8BJ34\n\
    \  history_record: history/records/PF01936/2026-10-21T073229Z-antigravity-e3e5a7.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Frozen DUF88/NYN/IPR021139/UNSCORED identity is preserved. Human Q9Y4F3v6
    PF01936 353-490 lies inside assayed238-510,not just crystallized352-500. Mouse
    Q8BJ34v3 maps352-489. PDB5YAA source158-320 matches canonical337-499 at161/163
    positions,with only the two deposited L-to-M crystallization substitutions; source
    D178/D215/D246/D272 therefore map locally to D357/D394/D425/D451. No whole-isoform
    constant offset is assumed. Current N4BP1/KHNYN mapPF11977 and Rae1/YacP PF05991,so
    historical NYN wording does not authorize their transfer to this family.
  target_ids:
  - PF01936
  evidence_ids:
  - identity
  - primary
  - mouse-assays-and-genotypes
  - source-coverage
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Each directed relation retains its measured comparator. Human WT/delta-C
    versus LacZ RNA reduction is distinct from delta-NYN or tandem-mutant increases
    versus WT; residual activities are not called abolished. The active mouse biochemical
    preparation includes LOTUS/RRM regions,with expression-host differences retained
    for the shorter construct. Whole-oocyte Ppp2cb resupply effects are not direct
    substrate identification. Female mating and oocyte-stage phenotypes remain indirect;
    Line1/Iap RNA and gammaH2AX foci are unresolved parallel genotype effects,not
    a transposition-to-damage-to-infertility chain. Increased knockin protein abundance
    and synonymous marker substitutions remain visible. No decapping/TUT4/7 association
    is promoted to an experimentally established ordered pathway.
  target_ids:
  - PF01936
  evidence_ids:
  - primary
  - native
  - mouse-assays-and-genotypes
  - source-coverage
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Bacterial CRISPR NYN primary text was read but exact accession/Pfam mapping
    remains unresolved. LabA clock-output,HspA/HspB with sequence caution,Arabidopsis
    DNE1 and later EDC4/P-body/MARF1 contexts require followup. Ten reviewed UniProt
    examples are not all25419 proteins or329 architectures. Other biochemical substrates,metal
    comparisons,native targets and whole-construct isoforms are not exhaustively curated.
    Partial source-access failures are not negative research results.
  target_ids:
  - PF01936
  evidence_ids:
  - primary
- assessment_id: cycle1-partner-grounding-verification
  area: identity
  topic: Cycle 1 causal-graph partner and substrate protein grounding
  outcome: supported
  summary: 'Stage 2 (PR #319) grounded Homo sapiens MARF1/EDC4/DCP1A P-body localization
    nodes edc4-localization (UniProtKB:Q9Y4F3, UniProtKB:Q6P2E9) and dcp1a-pbodies
    (UniProtKB:Q9NPI6) in human-marf1-edc4-decapping-localization, preserving all
    domain-mapping and separated mRNA reporter graphs.'
  target_ids:
  - PF01936
  evidence_ids:
  - stage4-prior-review
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01936-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Extend accession-mapped nonmammalian and native-target contexts
  description: Resolve the bacterial CRISPR NYN accession and domain before adding
    its biochemical edges; inspect LabA,DNE1 and HspA primary studies with exact protein
    mapping; inspect later MARF1/EDC4/P-body assays. Verify full-construct sequences
    without extending the local mouse NYN offset blindly. Preserve residual activities,expression-host
    differences,marker alleles and unresolved native targets; retain IN_PROGRESS and
    all existing followups.
  target_ids:
  - PF01936
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - mouse-assays-and-genotypes
  - source-coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01936.yaml
    role: Human-owned scientific overlay
  previous_occurrences:
  - repository: CultureBotAI/DUFMech
    review_id: 20261012T050509Z-pf01936-marf1-domain-mapping-and-separated-rna-phenotypes
    finding_id: additional-contexts
actions:
- action_id: extend-contexts
  description: Resolve the bacterial CRISPR NYN accession and domain before adding
    its biochemical edges; inspect LabA,DNE1 and HspA primary studies with exact protein
    mapping; inspect later MARF1/EDC4/P-body assays. Verify full-construct sequences
    without extending the local mouse NYN offset blindly. Preserve residual activities,expression-host
    differences,marker alleles and unresolved native targets; retain IN_PROGRESS and
    all existing followups.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01936
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Human Figures3/5/6 and mouse Figures1-5/S5/S6 were visually inspected,with relevant
  primary Results/Methods and mouse supplement pp2-7 read. Human supplemental interaction
  tables and SEC figures were not inspected; no graph relies on their independent
  validation. Mouse raw RNA-seq datasets were not reanalyzed. Bacterial figures/supplement
  and other-member primary sources remain incomplete. Initial PMC attachments returned
  HTML and short EuropePMC downloads timed out; the longer mouse download succeeded.
  No experimental replication,clone resequencing or exhaustive family review.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
