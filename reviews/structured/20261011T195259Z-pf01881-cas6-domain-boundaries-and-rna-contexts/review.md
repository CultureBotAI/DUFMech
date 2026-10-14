# PF01881 Cas6 domain boundaries and RNA-dependent cleavage contexts

- Review: 20261011T195259Z-pf01881-cas6-domain-boundaries-and-rna-contexts
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T19:52:44Z
- Finished UTC: 2026-10-11T19:52:59Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Eight graphs retain sixteen direct observed purified-assay effects and one unresolved wraparound-alignment hypothesis. The four-glycine C-terminal mutant is one intervention; Y31/H46/K52 lie outside PF01881. RNA recognition, linker tolerance and conditional cleavage-site rerouting remain separate contexts. Protocol discrepancies, missing supplements and broader member coverage prevent full-family completion. Retain IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Carte2008 Methods/Results/Discussion and original Figures1/3/7; Carte2010 Methods/Results/Discussion, original Figures2-5 and Tables1/2; Wang2011 Methods/Results/Discussion and original Figures2/5. Current member-specific PF01881/PF21350 APIs, UniProt versioned sequence metadata, original/RefSeq FASTAs and3I4H entity sequence were compared. The frozen previous-name TSV verifies DUF57. Other Cas6 studies are explicitly incomplete leads.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01881 | data/families/PF01881.yaml | generated | PF01881 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01881 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01881.

Q8U1S4 sequenceversion1 equals AAL81255.1 and WP_011012271.1 over264 aa. PF01881 maps121-237 and PF21350 maps17-117. G223/G225/G231/G233 and K188/K190/R191 fall inside PF01881; Y31/H46/K52/R64 do not. 3I4H entity equals MAHHHHHHGS plus reference2-264, but every assay batch's full tag sequence is not independently established. PF0393/Q8U3R3 is a different paralog. Historical DUF57 naming does not characterize all1831 family proteins.

### Directed effects and limits

graph: supported. Targets: PF01881.

Seven MECHANISTIC graphs contain sixteen DIRECT/OBSERVED effects, with no asserted binding-to-cleavage relay or whole-protein-to-domain sufficiency leap. One HYPOTHETICAL graph contains an UNRESOLVED/HYPOTHESIZED positioning edge. Residual K52A and glycine-loop binding, joint substitutions, parallel readouts, reported-but-unshown M/N binding, smaller tolerated linker edits and conditional deoxy-site rerouting remain explicit. No mature-crRNA, antiviral, dimer-necessity or individually assigned chemical catalytic mechanism is added.

### Remaining family coverage

completeness: concern. Targets: PF01881.

All1831 frozen proteins remain in scope. Exact assay insert/tag sequences, individual glycine contributions, folding controls, direct contact tests, published DTT discrepancy and2011 timing/WT-dose details remain unresolved. Original missing main figures and supplements, PF0393 primary functional data, other Cas6 members and cellular processing/antiviral studies require follow-up. These three PF1131 studies are not exhaustive family coverage.

## Findings

### additional-contexts: Resolve Cas6 individual-residue mechanism and member transfer

minor / open / confirmed; issue key: pf01881-causal-context-coverage.

Inspect missing original figures/supplements and exact constructs, resolve75 versus0.75 mM DTT and assay timing/dose details, and distinguish single-glycine effects from joint-mutant conformational changes. Test structural contacts and positioning hypotheses with direct evidence. Review PF0393 and other member-specific primary data, including negative contexts, before transferring cleavage or cellular-defense claims beyond PF1131.

## Recommended Actions And Acceptance Checks

### extend-contexts

Inspect missing original figures/supplements and exact constructs, resolve75 versus0.75 mM DTT and assay timing/dose details, and distinguish single-glycine effects from joint-mutant conformational changes. Test structural contacts and positioning hypotheses with direct evidence. Review PF0393 and other member-specific primary data, including negative contexts, before transferring cleavage or cellular-defense claims beyond PF1131.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC3154685/; Original Figures2C and5A-D, model Figures2B/5E, protein/RNA/assay Methods and revised linker Results | supports | Joint G223A/G225A/G231A/G233A loses detectable cleavage but retains weak binding. Recognition-region RNA substitutions reduce both binding and cleavage; long linker deletions and distal truncation reduce cleavage, unlike smaller edits. A23U shifts the cut, and deoxy-G21 in that background restores the alternative site. The RNA wraparound path remains a model because only RNA2-10 is resolved. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01881/protein/uniprot/Q8U1S4/; Accession and domain locations; paired UniProt identity facts | supports | Q8U1S4 sequenceversion1 equals AAL81255.1 and WP_011012271.1 over264 aa. PF01881 maps121-237 and PF21350 maps17-117. G223/G225/G231/G233 and K188/K190/R191 fall inside PF01881; Y31/H46/K52/R64 do not. 3I4H entity equals MAHHHHHHGS plus reference2-264, but every assay batch's full tag sequence is not independently established. PF0393/Q8U3R3 is a different paralog. Historical DUF57 naming does not characterize all1831 family proteins. |
| initial-cleavage | https://pmc.ncbi.nlm.nih.gov/articles/PMC2607076/; Original Figures1C,3A-D,7A/B and protein/RNA reaction Methods | supports | Purified PF1131 produces repeat-containing RNA cleavage products. Site mapping, paired RNA substitutions and metal-condition assays bound the interpretation; final maturation and cellular antiviral function are not directly measured. The earlier nt9-12 explanation was revised by the later study. |
| triad-and-footprints | https://pmc.ncbi.nlm.nih.gov/articles/PMC2957057/; Original Figures2-5,Tables1/2 and expression/cleavage/footprinting/IP Methods | supports | Y31A/H46A eliminate detectable cleavage and K52A retains reduced output; shifted RNP persists. Cas6 protects recognition-region probe sites in separately specified Pb and RNase A assays. Immune-resin activity and coIP are retained as context, not individual enzyme attribution, stability or trimming edges. The T7 template and synthetic RNA remain distinct. |
| coverage-and-access | evidence/PF01881/cas6-gap-ledger.txt; Scoped search, inspected sources, access limits and remaining member-specific work | supports | No earlier scoped curation was found in the searched owners, including ignored files. Repository and installed-skill reads and skill validation succeeded. An unavailable base-venv dependency worked in the existing offline uv environment; the missing supplement is a remote challenge response, not a repository read denial. Secondary paralog labels are leads only. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01881 | data/families/PF01881.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Original Carte2008 Figures1/3/7, Carte2010 Figures2-5 and Tables1/2, and Wang2011 Figures2/5 were visually inspected. Other original images and supplements were not all inspected; the2011 supplementary DOC endpoint returned challenge HTML, not a readable document. No raw-data refit, construct resequencing, independent replication or exhaustive family survey. Rendered-page checks follow separately.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T195259Z-pf01881-cas6-domain-boundaries-and-rna-contexts
title: PF01881 Cas6 domain boundaries and RNA-dependent cleavage contexts
started_at: '2026-10-11T19:52:44Z'
finished_at: '2026-10-11T19:52:59Z'
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
summary: Eight graphs retain sixteen direct observed purified-assay effects and one
  unresolved wraparound-alignment hypothesis. The four-glycine C-terminal mutant is
  one intervention; Y31/H46/K52 lie outside PF01881. RNA recognition, linker tolerance
  and conditional cleavage-site rerouting remain separate contexts. Protocol discrepancies,
  missing supplements and broader member coverage prevent full-family completion.
  Retain IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01881.yaml
    sha256: ad1486275b4ff2de4f5d30f165373f30fa6ecb3058d9a302f4857d95882ac08f
    role: context
  - path: data/families/PF01881.yaml
    sha256: ca151bdd5ee4797a6f1e6999c086edf51b2f9dc1ea0dad4b3d154efd06e0f64e
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
  - path: evidence/PF01881/wang-2011-rna-loop.txt
    role: context
    sha256: e90cc6af9ddcbefccd0efbd7ec7c947313dd9f29cb0e668adc4b04449dc6c7ba
  - path: evidence/PF01881/cas6-identity.txt
    role: context
    sha256: 059b809ccf7d6e322cb2d7fc447af46cc81dc11607f1d63f92d3d58aa561739a
  - path: evidence/PF01881/carte-2008-cleavage.txt
    role: context
    sha256: 9d6347acce6bbe0480c81ef28719967e9fd05e13715fb13e84beba43a7aebe3d
  - path: evidence/PF01881/carte-2010-mutants-footprints.txt
    role: context
    sha256: 4dc975f398e2be0bdce71c0c4ea75487d99e38d32e4b1a4bc4c6aaad3703c51d
  - path: evidence/PF01881/cas6-gap-ledger.txt
    role: context
    sha256: 3c09f1a5692feaa11dbaa8ebc5a6dfb8552d6721fbcca23cd8d839b9aff18bcf
targets:
- target_id: PF01881
  path: data/families/PF01881.yaml
  label: PF01881
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01881.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: d7d4c6b4959a5cddddb69af2d3881ee0f321df3fdfb97ae612d97ff41feec579
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Carte2008 Methods/Results/Discussion and original Figures1/3/7; Carte2010
    Methods/Results/Discussion, original Figures2-5 and Tables1/2; Wang2011 Methods/Results/Discussion
    and original Figures2/5. Current member-specific PF01881/PF21350 APIs, UniProt
    versioned sequence metadata, original/RefSeq FASTAs and3I4H entity sequence were
    compared. The frozen previous-name TSV verifies DUF57. Other Cas6 studies are
    explicitly incomplete leads.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01881
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: All1831 frozen proteins remain in scope. Exact assay insert/tag sequences,
      individual glycine contributions, folding controls, direct contact tests, published
      DTT discrepancy and2011 timing/WT-dose details remain unresolved. Original missing
      main figures and supplements, PF0393 primary functional data, other Cas6 members
      and cellular processing/antiviral studies require follow-up. These three PF1131
      studies are not exhaustive family coverage.
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
  - PF01881
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3154685/
  locator: Original Figures2C and5A-D, model Figures2B/5E, protein/RNA/assay Methods
    and revised linker Results
  accessed_at: '2026-10-11T19:52:59Z'
  support: supports
  snapshot_sha256: e90cc6af9ddcbefccd0efbd7ec7c947313dd9f29cb0e668adc4b04449dc6c7ba
  summary: Joint G223A/G225A/G231A/G233A loses detectable cleavage but retains weak
    binding. Recognition-region RNA substitutions reduce both binding and cleavage;
    long linker deletions and distal truncation reduce cleavage, unlike smaller edits.
    A23U shifts the cut, and deoxy-G21 in that background restores the alternative
    site. The RNA wraparound path remains a model because only RNA2-10 is resolved.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01881/protein/uniprot/Q8U1S4/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T19:52:59Z'
  support: supports
  snapshot_sha256: 059b809ccf7d6e322cb2d7fc447af46cc81dc11607f1d63f92d3d58aa561739a
  summary: Q8U1S4 sequenceversion1 equals AAL81255.1 and WP_011012271.1 over264 aa.
    PF01881 maps121-237 and PF21350 maps17-117. G223/G225/G231/G233 and K188/K190/R191
    fall inside PF01881; Y31/H46/K52/R64 do not. 3I4H entity equals MAHHHHHHGS plus
    reference2-264, but every assay batch's full tag sequence is not independently
    established. PF0393/Q8U3R3 is a different paralog. Historical DUF57 naming does
    not characterize all1831 family proteins.
- evidence_id: initial-cleavage
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2607076/
  locator: Original Figures1C,3A-D,7A/B and protein/RNA reaction Methods
  summary: Purified PF1131 produces repeat-containing RNA cleavage products. Site
    mapping, paired RNA substitutions and metal-condition assays bound the interpretation;
    final maturation and cellular antiviral function are not directly measured. The
    earlier nt9-12 explanation was revised by the later study.
  accessed_at: '2026-10-11T19:52:59Z'
  support: supports
  snapshot_sha256: 9d6347acce6bbe0480c81ef28719967e9fd05e13715fb13e84beba43a7aebe3d
- evidence_id: triad-and-footprints
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2957057/
  locator: Original Figures2-5,Tables1/2 and expression/cleavage/footprinting/IP Methods
  summary: Y31A/H46A eliminate detectable cleavage and K52A retains reduced output;
    shifted RNP persists. Cas6 protects recognition-region probe sites in separately
    specified Pb and RNase A assays. Immune-resin activity and coIP are retained as
    context, not individual enzyme attribution, stability or trimming edges. The T7
    template and synthetic RNA remain distinct.
  accessed_at: '2026-10-11T19:52:59Z'
  support: supports
  snapshot_sha256: 4dc975f398e2be0bdce71c0c4ea75487d99e38d32e4b1a4bc4c6aaad3703c51d
- evidence_id: coverage-and-access
  kind: search
  reference: evidence/PF01881/cas6-gap-ledger.txt
  locator: Scoped search, inspected sources, access limits and remaining member-specific
    work
  search_scope: Ignored/hidden-inclusive search of maintained curation/evidence/history/review
    owners for PF01881/DUF57/Cas6; primary literature and identity searches for PF1131,Cas6
    glycine-loop/RNA variants,PF0393 and3UFC on2026-10-11. Not an exhaustive literature
    or member survey.
  summary: No earlier scoped curation was found in the searched owners, including
    ignored files. Repository and installed-skill reads and skill validation succeeded.
    An unavailable base-venv dependency worked in the existing offline uv environment;
    the missing supplement is a remote challenge response, not a repository read denial.
    Secondary paralog labels are leads only.
  accessed_at: '2026-10-11T19:52:59Z'
  support: supports
  snapshot_sha256: 3c09f1a5692feaa11dbaa8ebc5a6dfb8552d6721fbcca23cd8d839b9aff18bcf
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T19:52:59Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01881
  kind: record_content
  reference: data/families/PF01881.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T19:52:59Z'
  support: context_only
  snapshot_sha256: ca151bdd5ee4797a6f1e6999c086edf51b2f9dc1ea0dad4b3d154efd06e0f64e
  quote: "id: Pfam:PF01881\npfam_id: PF01881\nname: CRISPR associated protein Cas6,\
    \ C-terminal\nshort_name: Cas_Cas6_C\nseed_status: EX_DUF\ncharacterization_status:\
    \ UNSCORED\ncuration_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01881\n\
    counters:\n  proteins: 1831\n  matches: 1832\n  proteomes: 1415\n  taxa: 2926\n\
    \  structures: 7\n  alphafold_models: 1415\n  domain_architectures: 4\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR049435\ndescription: 'This group of families is one of\
    \ several protein families that are always found associated\n  with prokaryotic\
    \ CRISPRs, themselves a family of clustered regularly interspaced short palindromic\
    \ repeats,\n  DNA repeats found in nearly half of all bacterial and archaeal genomes.\
    \ These DNA repeat regions have\n  a remarkably regular structure: unique sequences\
    \ of constant size, called spacers, sit between each\n  pair of repeats [[cite:PUB00020781]].\
    \ It has been shown that the CRISPRs are virus-derived sequences\n  acquired by\
    \ the host to enable them to resist viral infection. The Cas proteins from the\
    \ host use the\n  CRISPRs to mediate an antiviral response. After transcription\
    \ of the CRISPR, a complex of Cas proteins\n  termed Cascade cleaves a CRISPR\
    \ RNA precursor in each repeat and retains the cleavage products containing\n\
    \  the virus-derived sequence. Assisted by the helicase Cas3, these mature CRISPR\
    \ RNAs then serve as small\n  guide RNAs that enable Cascade to interfere with\
    \ virus proliferation [[cite:PUB00106643]]. Cas5 contains\n  an endonuclease motif,\
    \ whose inactivation leads to loss of resistance, even in the presence of phage-derived\n\
    \  spacers [[cite:PUB00109113]]. In Type I and III CRISPR/Cas systems, the Cas6\
    \ family of endoribonucleases\n  generates functional CRISPR-derived RNAs by site-specific\
    \ cleavage of repeat sequences in precursor\n  transcripts. The structure of Cas6\
    \ [[cite:PUB00098896]] showed it adopts a tandem ferredoxin/RRM fold.\n  This\
    \ entry represents the C-terminal domain.'\ncuration_history: history/records/PF01881\n\
    discussions:\n- discussion_id: cas6-domain-residue-and-protocol-limits\n  prompt:\
    \ Resolve individual C-terminal contributions and the exact assay recipes.\n \
    \ kind: CURATION_TODO\n  status: OPEN\n  rationale: PF01881 is121-237, whereas\
    \ Y31/H46/K52 lie in the N-terminal domain. The C-terminal glycine-loop\n    intervention\
    \ changes four residues together, and the2011 DTT concentration differs100-fold\
    \ from2008.\n  evidence:\n  - reference: PMID:20884784\n    supports: PARTIAL\n\
    \    evidence_source: primary_mutant_assays_and_domain_mapping\n    explanation:\
    \ Original Figures3/4 and Tables1/2 show whole-protein mutant effects and retained\
    \ binding;\n      they do not assign C-terminal catalytic residues or exact chemical\
    \ roles.\n  - reference: PMID:21300293\n    supports: PARTIAL\n    evidence_source:\
    \ primary_structure_and_original_mutant_figures\n    explanation: Figure2C tests\
    \ a joint four-glycine mutant; K188/K190/R191 contacts are structural observations,\n\
    \      not causal substitution tests. Missing RNA coordinates leave the path hypothetical.\n\
    \  notes: Test individual glycines with expression/folding/binding controls; resolve\
    \ printed75 versus0.75\n    mM DTT,2011 incubation duration and Figure2C WT dose.\
    \ Inspect missing original figures and supplements.\n    The2010 synthetic oligo\
    \ and transcribed template must remain distinct, and K52A residual output must\n\
    \    not become a zero-activity claim.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n\
    - discussion_id: cas6-family-and-cellular-transfer\n  prompt: Extend exact-member\
    \ coverage without turning association or a rename into a universal mechanism.\n\
    \  kind: CURATION_TODO\n  status: OPEN\n  rationale: PF1131 purified assays do\
    \ not establish PF0393 paralog activity, mature crRNA production\n    or cellular\
    \ antiviral effects across1831 frozen family proteins. The broad imported description\
    \ also\n    mentions distinct Cas5/Cas3 systems.\n  evidence:\n  - reference:\
    \ PMID:19141480\n    supports: PARTIAL\n    evidence_source: primary_purified_rna_processing\n\
    \    explanation: Figure1C establishes repeat cleavage, not final crRNA maturation\
    \ or resistance in cells.\n      Figure7 supports cleavage without added magnesium\
    \ and in EDTA under the tested assay.\n  - reference: PMID:20884784\n    supports:\
    \ PARTIAL\n    evidence_source: primary_immunoprecipitation_and_northern\n   \
    \ explanation: Figure5 immune resin carries cleavage activity and Cas6 associates\
    \ with intermediates;\n      coIP does not measure direct retention, stability\
    \ or the later trimming reaction.\n  - reference: PMID:21300293\n    supports:\
    \ PARTIAL\n    evidence_source: primary_substrate_variants\n    explanation: Smaller\
    \ linker edits retain cleavage and A23U/deoxy variants redirect its position.\
    \ The2011\n      Results revise the earlier nt9-12 interpretation while preserving\
    \ its underlying assays.\n  notes: PF0393/Q8U3R3/3UFC is a distinct paralog; PMID22447673\
    \ metadata has been checked but primary\n    functional data remain uninspected.\
    \ Investigate other archaeal members and cellular processing with\n    exact PF01881\
    \ mapping, including positive and negative contexts. No negative edge is adopted\
    \ from\n    a secondary noncatalytic label. Coverage remains partial and IN_PROGRESS.\n\
    \  posed_by: Codex\n  posed_date: '2026-10-11'\ncausal_graphs:\n- graph_id: pfu-cas6-repeat-cleavage\n\
    \  title: Purified Pfu Cas6 produces CRISPR-repeat cleavage products\n  scope:\
    \ Carte2008 Figure1C, repeat-only and repeat-guide-repeat substrates tested separately.\n\
    \  context: 500 nM N-terminal His6 PF1131,50 fmol RNA in20 ul,20 mM HEPES pH7,250\
    \ mM KCl,0.75 mM DTT,1.5\n    mM MgCl2,5 ug E. coli tRNA,10% glycerol,70 C30 min;\
    \ denaturing PAGE after deproteinization.\n  family_mapping: P. furiosus DSM3638\
    \ PF1131/Q8U1S4 sequence version1,264 aa,equals AAL81255.1 and WP_011012271.1.\n\
    \    PF01881 maps121-237; N-terminal PF21350 maps17-117. Intact His6 protein,\
    \ not isolated PF01881.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:186497\n\
    \  limitations: Figure3A separately maps the synthetic-repeat cut after A22; uniformly\
    \ transcribed substrates\n    can contain extra bases. Guide-containing products\
    \ are processing intermediates, not mature crRNAs.\n    No cellular antiviral\
    \ effect or family-wide sufficiency is demonstrated.\n  nodes:\n  - node_id: cas6-plus-rna\n\
    \    label: Add purified PF1131 to the specified repeat-containing RNA reaction\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q8U1S4\n  - node_id:\
    \ cleavage-products\n    label: Repeat-containing RNA cleavage products\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: cas6-produces-products\n    subject: cas6-plus-rna\n\
    \    predicate: produces\n    object: cleavage-products\n    mechanism: Cleavage\
    \ products appear with the purified protein and are absent from matched no-protein\n\
    \      reactions for each substrate. The assay establishes whole-protein endoribonuclease\
    \ activity, without\n      assigning isolated-domain sufficiency or later trimming.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:19141480\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2607076/\n\
    \      snippet: Cas6 is an endoribonuclease\n      explanation: Original Figures1C\
    \ and3A with protein and reaction Methods; substrate-labeling differences\n  \
    \      and no-protein controls are retained.\n      cache_path: evidence/PF01881/carte-2008-cleavage.txt\n\
    \      cache_sha256: 9d6347acce6bbe0480c81ef28719967e9fd05e13715fb13e84beba43a7aebe3d\n\
    - graph_id: pfu-cas6-n-terminal-substitutions\n  title: N-terminal substitutions\
    \ reduce whole-protein Cas6 cleavage\n  scope: Carte2010 Figures3/4, three separately\
    \ tested single substitutions outside PF01881.\n  context: WT or single mutant10,50,500\
    \ nM;50 fmol uniformly labeled T7 repeat RNA,20 mM HEPES pH7,500\n    mM KCl,20\
    \ mM EDTA,65-70 C30 min. Cleavage15% denaturing PAGE; separate binding doses1,50,200,500\
    \ nM\n    and8% native PAGE.\n  family_mapping: PF1131/Q8U1S4/AAL81255.1,PF01881\
    \ 121-237. Y31/H46/K52 are outside PF01881 in PF21350\n    17-117. N-terminal\
    \ His6 pET24d proteins expressed in E. coli; mutant DNA sequencing reported.\n\
    \  scope_status: MECHANISTIC\n  taxon: NCBITaxon:186497\n  limitations: These\
    \ are not PF01881 catalytic residues. SDS-PAGE purity is not a folding control.\
    \ All\n    variants retain shifted RNP, with somewhat reduced K52A binding; WT\
    \ can bind cleavage product. T7\n    template oligos7+8 differ from synthetic\
    \ RNA oligo9. Endpoint losses do not assign acid/base chemistry.\n  nodes:\n \
    \ - node_id: y31a\n    label: Substitute Y31A in intact PF1131\n    node_type:\
    \ PERTURBATION\n  - node_id: h46a\n    label: Substitute H46A in intact PF1131\n\
    \    node_type: PERTURBATION\n  - node_id: k52a\n    label: Substitute K52A in\
    \ intact PF1131\n    node_type: PERTURBATION\n  - node_id: product-yield\n   \
    \ label: Repeat-RNA cleavage product yield\n    node_type: ACTIVITY\n  edges:\n\
    \  - edge_id: y31a-decreases-cleavage\n    subject: y31a\n    predicate: decreases\n\
    \    object: product-yield\n    mechanism: Y31A eliminates detectable cleavage\
    \ over the tested enzyme range while retaining a stable\n      RNA-containing\
    \ complex. The result does not resolve a chemical role or exclude all conformational\n\
    \      effects.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:20884784\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC2957057/\n      snippet: RNA binding\
    \ and cleavage reactions\n      explanation: Original Figure3A Y31A lanes, Figure3B\
    \ purity, Figure4 binding and Tables1/2; comparison\n        is with WT in the2010\
    \ EDTA/high-salt assay.\n      cache_path: evidence/PF01881/carte-2010-mutants-footprints.txt\n\
    \      cache_sha256: 4dc975f398e2be0bdce71c0c4ea75487d99e38d32e4b1a4bc4c6aaad3703c51d\n\
    \  - edge_id: h46a-decreases-cleavage\n    subject: h46a\n    predicate: decreases\n\
    \    object: product-yield\n    mechanism: H46A eliminates detectable cleavage\
    \ in this assay while retaining shifted RNP. Loss of\n      the endpoint is not\
    \ direct observation of proton donation by H46.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:20884784\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2957057/\n      snippet:\
    \ RNA binding and cleavage reactions\n      explanation: Original Figures3/4 and\
    \ mutant Methods; this substitution is separately assayed and\n        outside\
    \ the curated C-terminal domain.\n      cache_path: evidence/PF01881/carte-2010-mutants-footprints.txt\n\
    \      cache_sha256: 4dc975f398e2be0bdce71c0c4ea75487d99e38d32e4b1a4bc4c6aaad3703c51d\n\
    \  - edge_id: k52a-decreases-cleavage\n    subject: k52a\n    predicate: decreases\n\
    \    object: product-yield\n    mechanism: K52A lowers cleavage yield, with residual\
    \ output and an approximately40-fold endpoint reduction\n      at500 nM reported\
    \ by the authors. This is not a40-fold kcat change or a complete loss of binding.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:20884784\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2957057/\n\
    \      snippet: RNA binding and cleavage reactions\n      explanation: Original\
    \ Figure3A residual K52A bands, Figure4 somewhat reduced binding and Results\n\
    \        quantitation; no fitted kinetic rate is adopted.\n      cache_path: evidence/PF01881/carte-2010-mutants-footprints.txt\n\
    \      cache_sha256: 4dc975f398e2be0bdce71c0c4ea75487d99e38d32e4b1a4bc4c6aaad3703c51d\n\
    - graph_id: pfu-cas6-c-terminal-glycine-loop\n  title: Joint C-terminal glycine-loop\
    \ substitutions reduce Cas6 cleavage\n  scope: Wang2011 Figure2C, one four-site\
    \ mutant in full-length Cas6.\n  context: G223A/G225A/G231A/G233A mutant0.5,1,10\
    \ uM versus WT positive lane. Standard reaction uses50\n    fmol RNA/20 ul,20\
    \ mM HEPES pH7,250 mM KCl,1.5 mM MgCl2,5 ug E. coli tRNA,10% glycerol,70 C. Printed\n\
    \    DTT75 mM differs from2008 0.75 mM; duration and Figure2C-specific WT dose\
    \ remain unresolved.\n  family_mapping: PF1131/Q8U1S4/AAL81255.1,PF01881 121-237;\
    \ G223/G225/G231/G233 all lie inside PF01881.\n    This is a joint mutant of intact\
    \ His-tagged protein, not four independently tested glycines or a domain-only\n\
    \    preparation.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:186497\n  limitations:\
    \ Weak RNA binding remains. No independent folding/stability assay is shown for\
    \ the joint\n    mutant. Loss of cleavage does not prove a glycine-specific chemical\
    \ catalytic role or an observed\n    RNA trajectory.\n  nodes:\n  - node_id: four-glycine-mutant\n\
    \    label: Jointly substitute G223A/G225A/G231A/G233A in PF1131\n    node_type:\
    \ PERTURBATION\n  - node_id: cleavage-signal\n    label: Cas6-dependent repeat-RNA\
    \ cleavage signal\n    node_type: ACTIVITY\n  edges:\n  - edge_id: four-glycine-mutant-decreases-cleavage\n\
    \    subject: four-glycine-mutant\n    predicate: decreases\n    object: cleavage-signal\n\
    \    mechanism: The four-site mutant has no detectable cleavage at the tested\
    \ doses relative to the WT\n      positive lane. Retained weak binding separates\
    \ complete loss of detectable binding from the cleavage\n      defect, without\
    \ identifying which glycine or structural property matters.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:21300293\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3154685/\n\
    \      snippet: RNA-binding and cleavage reactions\n      explanation: Original\
    \ Figure2C cleavage and binding panels, mutant description and Methods; four\n\
    \        substitutions are one intervention and assay-recipe uncertainties remain\
    \ visible.\n      cache_path: evidence/PF01881/wang-2011-rna-loop.txt\n      cache_sha256:\
    \ e90cc6af9ddcbefccd0efbd7ec7c947313dd9f29cb0e668adc4b04449dc6c7ba\n- graph_id:\
    \ pfu-cas6-rna-protection\n  title: Cas6 occupancy protects the repeat recognition\
    \ region from probes\n  scope: Carte2010 Figure2, separate Pb(II) and RNase A\
    \ footprinting reactions.\n  context: 0.1 pmol end-labeled synthetic repeat,0.001-1\
    \ uM Cas6,20 mM HEPES pH7/500 mM KCl,65-70 C30\n    min preincubation. Then15\
    \ mM Pb(II),room temperature10 min,or10 pg RNase A,37 C15 min; denaturing\n  \
    \  PAGE after deproteinization.\n  family_mapping: Intact PF1131/Q8U1S4,PF01881\
    \ 121-237 plus PF21350 17-117. The footprint localizes protected\n    RNA, not\
    \ independent C-domain sufficiency or a causal role for individual contacting\
    \ residues.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:186497\n  limitations:\
    \ Cas6's own cleavage occurs during the preparation. Probe protection does not\
    \ establish\n    a physiological RNA-stability mechanism. No protection detected\
    \ elsewhere does not exclude contacts;2011\n    structure resolves RNA2-10.\n\
    \  nodes:\n  - node_id: cas6-preincubation\n    label: Preincubate repeat RNA\
    \ with increasing Cas6\n    node_type: PERTURBATION\n  - node_id: lead-fragments\n\
    \    label: Pb-induced cleavage signals across RNA nucleotides2-8\n    node_type:\
    \ STATE\n  - node_id: rnase-a-fragments\n    label: RNase A cleavage signals at\
    \ U3/C5/U8\n    node_type: STATE\n  edges:\n  - edge_id: cas6-decreases-lead-probe-cleavage\n\
    \    subject: cas6-preincubation\n    predicate: decreases\n    object: lead-fragments\n\
    \    mechanism: Added Cas6 reduces the mapped Pb-sensitive bands in the recognition\
    \ region compared with\n      the protein-free probe reaction. This is a direct\
    \ reconstituted protection readout, not a claim\n      that Cas6 chemically inhibits\
    \ lead.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:20884784\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2957057/\n\
    \      snippet: RNA binding and cleavage reactions\n      explanation: Original\
    \ Figure2A/B right panels and2C map, footprinting Methods and free-RNA controls;\n\
    \        Pb quench uses20 mM EDTA after the probe incubation.\n      cache_path:\
    \ evidence/PF01881/carte-2010-mutants-footprints.txt\n      cache_sha256: 4dc975f398e2be0bdce71c0c4ea75487d99e38d32e4b1a4bc4c6aaad3703c51d\n\
    \  - edge_id: cas6-decreases-rnase-a-probe-cleavage\n    subject: cas6-preincubation\n\
    \    predicate: decreases\n    object: rnase-a-fragments\n    mechanism: Cas6\
    \ lowers RNase A-generated band intensities at U3,C5,U8 under the separately specified\n\
    \      probe conditions. The graph does not connect footprint protection to an\
    \ unmeasured cellular half-life.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:20884784\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2957057/\n      snippet:\
    \ RNA binding and cleavage reactions\n      explanation: Original Figure2A/B left\
    \ panels and2C map plus footprinting Methods; RNase A and Pb\n        assays are\
    \ separate interventions, not sequential steps.\n      cache_path: evidence/PF01881/carte-2010-mutants-footprints.txt\n\
    \      cache_sha256: 4dc975f398e2be0bdce71c0c4ea75487d99e38d32e4b1a4bc4c6aaad3703c51d\n\
    - graph_id: pfu-cas6-recognition-sequence-variants\n  title: Repeat recognition-region\
    \ substitutions reduce binding and cleavage\n  scope: Wang2011 Figure5A/B variants\
    \ G and H, each tested separately against WT repeat A.\n  context: 1 uM Cas6,50\
    \ fmol5'-labeled RNA in20 ul,20 mM HEPES pH7,250 mM KCl,1.5 mM MgCl2,5 ug E. coli\n\
    \    tRNA,10% glycerol,70 C;10% native and15% denaturing PAGE. Printed DTT75 mM\
    \ and unstated incubation\n    duration remain unresolved.\n  family_mapping:\
    \ PF1131/Q8U1S4,PF01881 121-237. Perturbations are in synthetic RNA, not protein\
    \ residues.\n    WT RNA is GUUACAAUAAGACUAAAAUAGAAUUGAAAG; variant G changes U2/U3\
    \ to AA, variant H changes C5/A6/A7\n    to GUU.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:186497\n  limitations: Multi-base changes do not establish\
    \ the necessity of each nucleotide independently. Binding\n    and cleavage are\
    \ parallel measured endpoints, not an observed binding-to-cleavage causal relay;\
    \ sequence\n    and local folding can both change.\n  nodes:\n  - node_id: u2-u3-aa\n\
    \    label: Change RNA U2/U3 to AA\n    node_type: PERTURBATION\n  - node_id:\
    \ c5-a6-a7-guu\n    label: Change RNA C5/A6/A7 to GUU\n    node_type: PERTURBATION\n\
    \  - node_id: shifted-rnp\n    label: Shifted RNA-protein complex signal\n   \
    \ node_type: STATE\n  - node_id: cleaved-rna\n    label: RNA cleavage product\
    \ signal\n    node_type: STATE\n  edges:\n  - edge_id: u2-u3-change-decreases-binding\n\
    \    subject: u2-u3-aa\n    predicate: decreases\n    object: shifted-rnp\n  \
    \  mechanism: Variant G has no detectable shifted complex in the shown protein-containing\
    \ reaction, unlike\n      WT. This is a combined two-base sequence intervention,\
    \ not two separately resolved recognition contacts.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:21300293\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3154685/\n\
    \      snippet: RNA-binding and cleavage reactions\n      explanation: Original\
    \ Figure5A G sequence and5B lower G lanes compared with WT A, including protein-minus\n\
    \        controls.\n      cache_path: evidence/PF01881/wang-2011-rna-loop.txt\n\
    \      cache_sha256: e90cc6af9ddcbefccd0efbd7ec7c947313dd9f29cb0e668adc4b04449dc6c7ba\n\
    \  - edge_id: u2-u3-change-decreases-cleavage\n    subject: u2-u3-aa\n    predicate:\
    \ decreases\n    object: cleaved-rna\n    mechanism: Variant G also lacks detectable\
    \ cleavage product in the corresponding denaturing gel. The\n      endpoint alone\
    \ does not separate deficient recognition from a subsequent catalytic effect.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:21300293\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3154685/\n\
    \      snippet: RNA-binding and cleavage reactions\n      explanation: Original\
    \ Figure5A G and5B upper cleavage panel; measured separately from the native\n\
    \        binding readout.\n      cache_path: evidence/PF01881/wang-2011-rna-loop.txt\n\
    \      cache_sha256: e90cc6af9ddcbefccd0efbd7ec7c947313dd9f29cb0e668adc4b04449dc6c7ba\n\
    \  - edge_id: c5-a6-a7-change-decreases-binding\n    subject: c5-a6-a7-guu\n \
    \   predicate: decreases\n    object: shifted-rnp\n    mechanism: Variant H loses\
    \ detectable shifted-complex signal in the shown assay. Three bases change\n \
    \     together and individual base contributions remain unresolved.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:21300293\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3154685/\n\
    \      snippet: RNA-binding and cleavage reactions\n      explanation: Original\
    \ Figure5A H and5B lower binding panel with matched protein-minus and WT lanes.\n\
    \      cache_path: evidence/PF01881/wang-2011-rna-loop.txt\n      cache_sha256:\
    \ e90cc6af9ddcbefccd0efbd7ec7c947313dd9f29cb0e668adc4b04449dc6c7ba\n  - edge_id:\
    \ c5-a6-a7-change-decreases-cleavage\n    subject: c5-a6-a7-guu\n    predicate:\
    \ decreases\n    object: cleaved-rna\n    mechanism: Variant H lacks detectable\
    \ cleavage product relative to WT A. This does not prove that\n      any one altered\
    \ base directly participates in chemical catalysis.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:21300293\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3154685/\n\
    \      snippet: RNA-binding and cleavage reactions\n      explanation: Original\
    \ Figure5A H and5B upper cleavage panel; no mechanistic arrow is inferred between\n\
    \        the separately measured binding and cleavage endpoints.\n      cache_path:\
    \ evidence/PF01881/wang-2011-rna-loop.txt\n      cache_sha256: e90cc6af9ddcbefccd0efbd7ec7c947313dd9f29cb0e668adc4b04449dc6c7ba\n\
    - graph_id: pfu-cas6-linker-and-distal-rna\n  title: Long linker deletions and\
    \ distal truncation reduce repeat cleavage\n  scope: Wang2011 Figure5A-C variants\
    \ D,M,N; each RNA variant assayed separately.\n  context: 1 uM Cas6 and2.5 nM5'-labeled\
    \ RNA,70 C,2011 buffer with printed75 mM DTT; incubation duration\n    unstated.\
    \ Native binding and denaturing cleavage readouts use separate gel aliquots.\n\
    \  family_mapping: Intact PF1131/Q8U1S4,PF01881 121-237. Variant D removes RNA25-30;\
    \ M/N remove five/six\n    bases in the intervening linker. These are substrate\
    \ edits, not PF01881 deletions.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:186497\n\
    \  limitations: D retains shown binding; M/N binding is reported without shown\
    \ data. Smaller two-to-four-base\n    linker deletions and a two-base insertion\
    \ retain cleavage. The earlier nt9-12 experiment also changed\n    recognition\
    \ bases A9/A10 and does not establish a universal four-base length threshold.\n\
    \  nodes:\n  - node_id: delete25-30\n    label: Remove repeat RNA nucleotides25-30\n\
    \    node_type: PERTURBATION\n  - node_id: five-base-linker-deletion\n    label:\
    \ Use five-base linker deletion RNA M\n    node_type: PERTURBATION\n  - node_id:\
    \ six-base-linker-deletion\n    label: Use six-base linker deletion RNA N\n  \
    \  node_type: PERTURBATION\n  - node_id: cleavage-output\n    label: Repeat-RNA\
    \ cleavage output\n    node_type: ACTIVITY\n  edges:\n  - edge_id: distal-deletion-decreases-cleavage\n\
    \    subject: delete25-30\n    predicate: decreases\n    object: cleavage-output\n\
    \    mechanism: Variant D has no detectable cleavage despite retained binding.\
    \ Deleting only27-30 in variant\n      C retains cleavage, implicating U25/G26\
    \ or their context without isolating either nucleotide's necessity.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:21300293\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3154685/\n\
    \      snippet: RNA-binding and cleavage reactions\n      explanation: Original\
    \ Figure5A sequences and5B C/D cleavage and binding lanes; qualitative plus/minus\n\
    \        summary is not a kinetic rate.\n      cache_path: evidence/PF01881/wang-2011-rna-loop.txt\n\
    \      cache_sha256: e90cc6af9ddcbefccd0efbd7ec7c947313dd9f29cb0e668adc4b04449dc6c7ba\n\
    \  - edge_id: five-base-deletion-decreases-cleavage\n    subject: five-base-linker-deletion\n\
    \    predicate: decreases\n    object: cleavage-output\n    mechanism: Variant\
    \ M loses detectable cleavage compared with WT and shorter linker-deletion controls.\n\
    \      Binding retention is an author-reported unshown result, not a newly inspected\
    \ binding gel.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:21300293\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC3154685/\n      snippet: RNA-binding\
    \ and cleavage reactions\n      explanation: Original Figure5A M and5C protein-minus/plus\
    \ lanes; the revised linker interpretation\n        is in the Results.\n     \
    \ cache_path: evidence/PF01881/wang-2011-rna-loop.txt\n      cache_sha256: e90cc6af9ddcbefccd0efbd7ec7c947313dd9f29cb0e668adc4b04449dc6c7ba\n\
    \  - edge_id: six-base-deletion-decreases-cleavage\n    subject: six-base-linker-deletion\n\
    \    predicate: decreases\n    object: cleavage-output\n    mechanism: Variant\
    \ N likewise loses detectable cleavage, with WT and shorter-deletion reactions\
    \ retaining\n      product. The result supports a condition-specific substrate\
    \ constraint, not a universal Cas6 molecular\n      ruler.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:21300293\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3154685/\n\
    \      snippet: RNA-binding and cleavage reactions\n      explanation: Original\
    \ Figure5A N and5C matched cleavage lanes; no unobserved binding-to-positioning\n\
    \        intermediate is added.\n      cache_path: evidence/PF01881/wang-2011-rna-loop.txt\n\
    \      cache_sha256: e90cc6af9ddcbefccd0efbd7ec7c947313dd9f29cb0e668adc4b04449dc6c7ba\n\
    - graph_id: pfu-cas6-rna-cleavage-site-selection\n  title: Substrate base and\
    \ ribose changes redirect the Cas6 cleavage site\n  scope: Wang2011 Figure5D,\
    \ WT A and variants P,Q,R with cleavage-site mapping.\n  context: 1 uM Cas6,5'-labeled\
    \ synthetic repeat in the2011 70 C assay with unresolved printed DTT/time.\n \
    \   Denaturing PAGE; recovered WT and A23U products additionally analyzed by MALDI-TOF.\n\
    \  family_mapping: Intact PF1131/Q8U1S4,PF01881 121-237. A23U and2'-deoxy substitutions\
    \ refer to RNA bases/riboses,\n    not protein residues.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:186497\n  limitations: This is altered product-site selection,\
    \ not a measured change in catalytic rate. A23U+dA22\n    still yields21 nt; deoxy\
    \ substitution can reroute cleavage rather than eliminate all activity. Site\n\
    \    plasticity does not establish the complete wraparound trajectory.\n  nodes:\n\
    \  - node_id: a23u\n    label: Change repeat A23 to U in the Cas6 reaction\n \
    \   node_type: PERTURBATION\n  - node_id: dg21-on-a23u\n    label: Add2'-deoxy\
    \ G21 to the A23U repeat\n    node_type: PERTURBATION\n  - node_id: product21\n\
    \    label: 21-nt5' cleavage product\n    node_type: STATE\n  - node_id: product22\n\
    \    label: 22-nt5' cleavage product\n    node_type: STATE\n  edges:\n  - edge_id:\
    \ a23u-increases-product21\n    subject: a23u\n    predicate: increases\n    object:\
    \ product21\n    mechanism: Variant Q shifts the major5' product from22 to21 nt\
    \ compared with WT A, supported by gel\n      and product-mass analysis. The intervention\
    \ changes cleavage position in a complete enzyme-substrate\n      reaction.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:21300293\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3154685/\n\
    \      snippet: RNA-binding and cleavage reactions\n      explanation: Original\
    \ Figure5A Q and5D gel/MALDI panel; WT22 and A23U21 masses are consistent with\n\
    \        cyclic-phosphate products, without claiming kinetic constants.\n    \
    \  cache_path: evidence/PF01881/wang-2011-rna-loop.txt\n      cache_sha256: e90cc6af9ddcbefccd0efbd7ec7c947313dd9f29cb0e668adc4b04449dc6c7ba\n\
    \  - edge_id: dg21-restores-product22\n    subject: dg21-on-a23u\n    predicate:\
    \ increases\n    object: product22\n    mechanism: In the A23U background, replacing\
    \ G21's2'-OH with H redirects the detected cleavage back\n      after position22.\
    \ The A23U+dA22 comparison still cuts after21; the conditional substrate context\n\
    \      is essential.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:21300293\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC3154685/\n      snippet: RNA-binding\
    \ and cleavage reactions\n      explanation: Original Figure5A P/Q/R sequences\
    \ and5D gel; no independent deoxy-G21 WT-substrate\n        result or universal\
    \ loss-of-cleavage rule is inferred.\n      cache_path: evidence/PF01881/wang-2011-rna-loop.txt\n\
    \      cache_sha256: e90cc6af9ddcbefccd0efbd7ec7c947313dd9f29cb0e668adc4b04449dc6c7ba\n\
    - graph_id: pfu-cas6-hypothetical-wraparound-alignment\n  title: HYPOTHETICAL\
    \ RNA wraparound alignment across the Cas6 glycine loop\n  scope: Wang2011 Figure2B/5E\
    \ model and Results interpretation, not an observed full RNA path.\n  context:\
    \ RNA-bound structure resolves nucleotides2-10; the cleavage-site segment is disordered.\
    \ The\n    model combines structural surface geometry, a joint glycine-loop mutant\
    \ and RNA linker/site perturbations.\n  family_mapping: PF1131/Q8U1S4,PF01881\
    \ 121-237 contains the tested glycine loop and K188/K190/R191 structural\n   \
    \ contacts. N-terminal putative catalytic residues Y31/H46/K52 are in PF21350,\
    \ not PF01881.\n  scope_status: HYPOTHETICAL\n  taxon: NCBITaxon:186497\n  limitations:\
    \ RNA positioning over this surface is not directly observed. Joint mutant effects\
    \ can include\n    conformational changes; no single-glycine causal assignment,\
    \ obligatory dimer or processing order\n    is established. Acid/base roles remain\
    \ separately unresolved.\n  nodes:\n  - node_id: proposed-wraparound-context\n\
    \    label: Proposed RNA recognition plus linker passage over the intact glycine-loop\
    \ surface\n    node_type: STATE\n  - node_id: proposed-scissile-alignment\n  \
    \  label: Proposed positioning of the scissile bond near the catalytic region\n\
    \    node_type: STATE\n  edges:\n  - edge_id: wraparound-may-enable-alignment\n\
    \    subject: proposed-wraparound-context\n    predicate: enables\n    object:\
    \ proposed-scissile-alignment\n    mechanism: The authors propose that the bound5'\
    \ recognition segment tethers downstream RNA along the\n      positive surface\
    \ and across the glycine loop toward the opposite-face cleavage region. This explains\n\
    \      several perturbations but does not observe the missing segment or exclude\
    \ other conformational routes.\n    directness: UNRESOLVED\n    support: HYPOTHESIZED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:21300293\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3154685/\n      snippet:\
    \ hypothetical path\n      explanation: Original Figure2B dashed path and5E schematic\
    \ with structural/mutational Results; experimental\n        constraints motivate\
    \ a model, not an experimentally demonstrated alignment step.\n      cache_path:\
    \ evidence/PF01881/wang-2011-rna-loop.txt\n      cache_sha256: e90cc6af9ddcbefccd0efbd7ec7c947313dd9f29cb0e668adc4b04449dc6c7ba\n\
    curation_events:\n- timestamp: '2026-10-11T19:41:55Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate PF01881 Cas6 assay-scoped causal\
    \ graphs\n  history_record: history/records/PF01881/2026-10-11T194155Z-codex-06c2b4.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Q8U1S4 sequenceversion1 equals AAL81255.1 and WP_011012271.1 over264 aa.
    PF01881 maps121-237 and PF21350 maps17-117. G223/G225/G231/G233 and K188/K190/R191
    fall inside PF01881; Y31/H46/K52/R64 do not. 3I4H entity equals MAHHHHHHGS plus
    reference2-264, but every assay batch's full tag sequence is not independently
    established. PF0393/Q8U3R3 is a different paralog. Historical DUF57 naming does
    not characterize all1831 family proteins.
  target_ids:
  - PF01881
  evidence_ids:
  - identity
  - primary
  - initial-cleavage
  - triad-and-footprints
  - coverage-and-access
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Seven MECHANISTIC graphs contain sixteen DIRECT/OBSERVED effects, with
    no asserted binding-to-cleavage relay or whole-protein-to-domain sufficiency leap.
    One HYPOTHETICAL graph contains an UNRESOLVED/HYPOTHESIZED positioning edge. Residual
    K52A and glycine-loop binding, joint substitutions, parallel readouts, reported-but-unshown
    M/N binding, smaller tolerated linker edits and conditional deoxy-site rerouting
    remain explicit. No mature-crRNA, antiviral, dimer-necessity or individually assigned
    chemical catalytic mechanism is added.
  target_ids:
  - PF01881
  evidence_ids:
  - primary
  - native
  - initial-cleavage
  - triad-and-footprints
  - coverage-and-access
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: All1831 frozen proteins remain in scope. Exact assay insert/tag sequences,
    individual glycine contributions, folding controls, direct contact tests, published
    DTT discrepancy and2011 timing/WT-dose details remain unresolved. Original missing
    main figures and supplements, PF0393 primary functional data, other Cas6 members
    and cellular processing/antiviral studies require follow-up. These three PF1131
    studies are not exhaustive family coverage.
  target_ids:
  - PF01881
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01881-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve Cas6 individual-residue mechanism and member transfer
  description: Inspect missing original figures/supplements and exact constructs,
    resolve75 versus0.75 mM DTT and assay timing/dose details, and distinguish single-glycine
    effects from joint-mutant conformational changes. Test structural contacts and
    positioning hypotheses with direct evidence. Review PF0393 and other member-specific
    primary data, including negative contexts, before transferring cleavage or cellular-defense
    claims beyond PF1131.
  target_ids:
  - PF01881
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - initial-cleavage
  - triad-and-footprints
  - coverage-and-access
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01881.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Inspect missing original figures/supplements and exact constructs,
    resolve75 versus0.75 mM DTT and assay timing/dose details, and distinguish single-glycine
    effects from joint-mutant conformational changes. Test structural contacts and
    positioning hypotheses with direct evidence. Review PF0393 and other member-specific
    primary data, including negative contexts, before transferring cleavage or cellular-defense
    claims beyond PF1131.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01881
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Original Carte2008 Figures1/3/7, Carte2010 Figures2-5 and Tables1/2, and Wang2011
  Figures2/5 were visually inspected. Other original images and supplements were not
  all inspected; the2011 supplementary DOC endpoint returned challenge HTML, not a
  readable document. No raw-data refit, construct resequencing, independent replication
  or exhaustive family survey. Rendered-page checks follow separately.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
