# PF01732 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review

- Review: 20261025T132033Z-pf01732-c3s4-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-25T13:20:32Z
- Finished UTC: 2026-10-25T13:20:33Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Four graphs retain twenty observed effects, eleven direct joint-preparation effects and nine indirect cellular effects. Purified antibody cleavage and antigen-complex dissociation remain separate from locus deletion and ATPase-mutant phenotypes. Exact GM12 member mapping is verified; residue numbering, protocol, construct, partner and family-transfer limits remain explicit. Partial coverage and IN_PROGRESS status are retained. Cycle 3 Stage 3 (PR #357) grounded the two MIB-MIP two-protein perturbation nodes (omit-mib and whole-locus-deletion) to Mycoplasma mycoides subsp. capri GM12 MIB and MIP (NCBIProtein:ACU78687.1 and NCBIProtein:ACU78312.1); multi-gene ATPase cluster comparison nodes in gm12-atpase-mutant-cellular-effects remain ungrounded at the cluster level. Stage 4 frozen-inventory review verified all causal graphs and grounded nodes against primary evidence caches.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Pending PF01732 within all 8296 frozen families; selected GM12-derived systems are a partial assessment, not completion of the family or corpus.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0e26e9cdab5214d838db4f53ddefbf83772241fb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01732 | data/families/PF01732.yaml | generated | PF01732 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01732 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01732.

GenBank ACU78687.1, 861 aa, MMCAP2_0582 in GM12, exactly matches UniParc UPI0001793D5F and its PF01732 290-776 interval. MIB83 is the separate ACU78312.1 protein. The exact GM12 sequence differs at residue 810 from the retired A0A446C0V0 reference. Whole-protein, partner-system and whole-locus effects are not isolated-domain sufficiency. Historical mutant plasmids and full 2021 strain breakpoints remain incompletely verified.

### Directed effects and limits

graph: supported. Targets: PF01732.

Eleven DIRECT observed edges concern net joint-preparation effects, not MIP-alone sufficiency or atomistic chemistry. Inactive-MIP and MIB-only dissociation controls explicitly prevent a cleavage-required release chain. Nine INDIRECT effects preserve 2021 whole-locus deletion versus WT and 2026 ATPase-cluster deletion versus Mmc 1.1 or K152A-plus-recode versus recode. Single-pair retention is not a reintroduction rescue. Serum doses, timing, detection limits and genotype background are retained; no ATP-hydrolysis or reset transition is promoted from a hypothesis.

### Remaining family coverage

completeness: concern. Targets: PF01732.

Exact historical recombinant sequences, residue numbering, antibody cleavage-bond mapping, protocol discrepancies, full-resolution 2021 panels and inaccessible supplements remain open. Other MIP paralogs, immunoglobulin classes and M. bovis, M. hominis, M. feriruminatoris and M. gallisepticum primary leads remain uncurated. The frozen MIB/Protein M conflation is qualified in maintained discussion without rewriting source bytes. No family-wide functional proof or intact-host causal chain is established.

### Cycle 3 causal-graph and protein-node grounding verification

representation: supported. Targets: PF01732.

Cycle 3 Stage 3 (PR #357) grounded the two MIB-MIP two-protein perturbation nodes (omit-mib and whole-locus-deletion) to Mycoplasma mycoides subsp. capri GM12 MIB and MIP (NCBIProtein:ACU78687.1 and NCBIProtein:ACU78312.1); multi-gene ATPase cluster comparison nodes in gm12-atpase-mutant-cellular-effects remain ungrounded at the cluster level. Stage 4 frozen-inventory review verified all causal graphs and grounded nodes against primary evidence caches.

## Findings

### additional-contexts: Resolve construct and assay discrepancies and extend member-specific MIP coverage

minor / open / confirmed; issue key: pf01732-causal-context-coverage.

Verify the older r-0582A clone and canonical numbering, reconcile antibody sequences and cleavage positions, obtain 2021 strain/assay supplements and full-resolution panels, resolve temperature/time/serum-dose discrepancies and assess remaining family-member studies independently. Distinguish MIB-only dissociation, joint proteolysis, cellular genotype effects and untested ATPase-reset hypotheses. Append a successor review with actual coverage rather than promoting the record from partial evidence.

## Recommended Actions And Acceptance Checks

### extend-contexts

Verify the older r-0582A clone and canonical numbering, reconcile antibody sequences and cleavage positions, obtain 2021 strain/assay supplements and full-resolution panels, resolve temperature/time/serum-dose discrepancies and assess remaining family-member studies independently. Distinguish MIB-only dissociation, joint proteolysis, cellular genotype effects and untested ATPase-reset hypotheses. Append a successor review with actual coverage rather than promoting the record from partial evidence.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC4868467/; Arfi 2016 Results and relevant main/SI Methods; Figures 2, 3, 4 and S5 visually inspected. S4/S7 captions only. | supports | Joint recombinant MIB-MIP preparations cleave goat IgG, Fab and F(ab')2; MIB omission and the published r-0582A preparation reduce IgG product. The 2016 S727A label conflicts with full-reference Y727/S759 and the later S759A label. No exact canonical mutant sequence, atomic catalytic step or universal antibody cleavage bond is asserted. |
| identity | https://rest.uniprot.org/uniparc/UPI0001793D5F.json; Accession and domain locations; paired UniProt identity facts | supports | GenBank ACU78687.1, 861 aa, MMCAP2_0582 in GM12, exactly matches UniParc UPI0001793D5F and its PF01732 290-776 interval. MIB83 is the separate ACU78312.1 protein. The exact GM12 sequence differs at residue 810 from the retired A0A446C0V0 reference. Whole-protein, partner-system and whole-locus effects are not isolated-domain sufficiency. Historical mutant plasmids and full 2021 strain breakpoints remain incompletely verified. |
| dissociation-and-locus-deletion | https://pmc.ncbi.nlm.nih.gov/articles/PMC7935358/; Nottelet 2021 selected Results/Methods; Figure 4A-F and Figure 5B/C/E/F captions and low-resolution main panels. | supports | Active and inactive joint mixtures dissociate three antigen-IgG complexes with MIB-only positive comparisons; whole-locus deletion affects cellular cleavage and immune-serum aggregation under distinct protocols. Supplemental strain validation remains inaccessible. |
| atpase-cellular-context | https://doi.org/10.1371/journal.ppat.1014043; Results 2.4/2.5, Methods 4.8, Discussion; visually inspected Figure 3 and supplement S13. May 2026 acknowledgements correction also read. | supports | ATPase deletion and recode-matched K152A-associated phenotypes affect agglutination and extracellular IgG/IgM product detection. Expression and serum-free controls bound interpretations; direct ATP hydrolysis, localization and release/reset remain unresolved. |
| remaining-member-coverage | https://pmc.ncbi.nlm.nih.gov/articles/PMC8081823/; M. bovis Methods accession lead only; separate ledger labels other species as abstract/search leads, not adopted experiments. | supports | Additional members and construct/protocol discrepancies require follow-up. Retrieved accessions do not substitute for assessment of the M. bovis experiments, other species or the complete family. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| stage4-prior-review | reviews/structured/20261021T114803Z-pf01732-stage4-record-review/review.yaml; Predecessor structured review 20261021T114803Z-pf01732-stage4-record-review | supports | Predecessor review 20261021T114803Z-pf01732-stage4-record-review verified and linked for finding continuity and semantic-digest progression on PF01732. |
| duf-projection-pf01732 | data/families/PF01732.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Arfi 2016 Figures 2/3/4/S5, Nottelet 2021 main Figures 4/5 at 440-pixel PMC resolution, and Berlureau 2026 Figure 3/S13 at large size were visually inspected. Publisher supplements/PDF and PMC enlarged-figure pages were inaccessible; Table S2/S9/S11/S12 and raw data were not independently analyzed. No calibrated densitometry, raw proteomics/genome reanalysis, historical clone resequencing, replication or exhaustive family survey was performed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T132033Z-pf01732-c3s4-record-review
title: PF01732 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review
started_at: '2026-10-25T13:20:32Z'
finished_at: '2026-10-25T13:20:33Z'
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
summary: 'Four graphs retain twenty observed effects, eleven direct joint-preparation
  effects and nine indirect cellular effects. Purified antibody cleavage and antigen-complex
  dissociation remain separate from locus deletion and ATPase-mutant phenotypes. Exact
  GM12 member mapping is verified; residue numbering, protocol, construct, partner
  and family-transfer limits remain explicit. Partial coverage and IN_PROGRESS status
  are retained. Cycle 3 Stage 3 (PR #357) grounded the two MIB-MIP two-protein perturbation
  nodes (omit-mib and whole-locus-deletion) to Mycoplasma mycoides subsp. capri GM12
  MIB and MIP (NCBIProtein:ACU78687.1 and NCBIProtein:ACU78312.1); multi-gene ATPase
  cluster comparison nodes in gm12-atpase-mutant-cellular-effects remain ungrounded
  at the cluster level. Stage 4 frozen-inventory review verified all causal graphs
  and grounded nodes against primary evidence caches.'
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 0e26e9cdab5214d838db4f53ddefbf83772241fb
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01732.yaml
    sha256: e2808d505d77d146313398681f18454c8bcb30704ce52475997883b11e5b3cd1
    role: context
  - path: data/families/PF01732.yaml
    sha256: 9a203bfde22f95e2bb95679e710983da5b6e48adc2cc982a8b8322854e143b20
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
  - path: evidence/PF01732/MIP-identity.txt
    sha256: 97531e7e022bcc8a4e62c54a52343be3000447fef27eaa2fb19c81a3c728a83c
    role: context
  - path: evidence/PF01732/arfi-2016-mib-mip.txt
    sha256: 94a2b2c9903ae218c03c7ed7febaf05b03caed8381203b8e3e833c65d14b3020
    role: context
  - path: evidence/PF01732/berlureau-2026-atpase.txt
    sha256: 8c772520b439afdcb24dbdfccfcd3b9af567ce74040fc288dc7f3dee2967f9ea
    role: context
  - path: evidence/PF01732/mip-followup-ledger.txt
    sha256: e3f517f29224d9c50e55270aa2ccd70e3d916fade28d96203d75cd0780356d32
    role: context
  - path: evidence/PF01732/nottelet-2021-mib-mip.txt
    sha256: 4499aa37aa0e0856bf2e1c6a94cac847ff2cc8692836661088dddfe09b0bb8ff
    role: context
  - path: reviews/structured/20261021T114803Z-pf01732-stage4-record-review/review.yaml
    sha256: d89dabec56bbb02c51429d416d1d73ce37cab153b5c9d0e075c13d1ed8a54571
    role: context
targets:
- target_id: PF01732
  path: data/families/PF01732.yaml
  label: PF01732
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01732.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: c3481857b222f84ec00c685c6d8fa06b3a791843bf858349175024ac5e1d5a4e
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Pending PF01732 within all 8296 frozen families; selected GM12-derived
    systems are a partial assessment, not completion of the family or corpus.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01732
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Exact historical recombinant sequences, residue numbering, antibody cleavage-bond
      mapping, protocol discrepancies, full-resolution 2021 panels and inaccessible
      supplements remain open. Other MIP paralogs, immunoglobulin classes and M. bovis,
      M. hominis, M. feriruminatoris and M. gallisepticum primary leads remain uncurated.
      The frozen MIB/Protein M conflation is qualified in maintained discussion without
      rewriting source bytes. No family-wide functional proof or intact-host causal
      chain is established.
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
  - PF01732
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4868467/
  locator: Arfi 2016 Results and relevant main/SI Methods; Figures 2, 3, 4 and S5
    visually inspected. S4/S7 captions only.
  accessed_at: '2026-10-11T14:36:10Z'
  support: supports
  snapshot_sha256: 94a2b2c9903ae218c03c7ed7febaf05b03caed8381203b8e3e833c65d14b3020
  summary: Joint recombinant MIB-MIP preparations cleave goat IgG, Fab and F(ab')2;
    MIB omission and the published r-0582A preparation reduce IgG product. The 2016
    S727A label conflicts with full-reference Y727/S759 and the later S759A label.
    No exact canonical mutant sequence, atomic catalytic step or universal antibody
    cleavage bond is asserted.
- evidence_id: identity
  kind: database
  reference: https://rest.uniprot.org/uniparc/UPI0001793D5F.json
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T14:36:10Z'
  support: supports
  snapshot_sha256: 97531e7e022bcc8a4e62c54a52343be3000447fef27eaa2fb19c81a3c728a83c
  summary: GenBank ACU78687.1, 861 aa, MMCAP2_0582 in GM12, exactly matches UniParc
    UPI0001793D5F and its PF01732 290-776 interval. MIB83 is the separate ACU78312.1
    protein. The exact GM12 sequence differs at residue 810 from the retired A0A446C0V0
    reference. Whole-protein, partner-system and whole-locus effects are not isolated-domain
    sufficiency. Historical mutant plasmids and full 2021 strain breakpoints remain
    incompletely verified.
- evidence_id: dissociation-and-locus-deletion
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7935358/
  locator: Nottelet 2021 selected Results/Methods; Figure 4A-F and Figure 5B/C/E/F
    captions and low-resolution main panels.
  summary: Active and inactive joint mixtures dissociate three antigen-IgG complexes
    with MIB-only positive comparisons; whole-locus deletion affects cellular cleavage
    and immune-serum aggregation under distinct protocols. Supplemental strain validation
    remains inaccessible.
  accessed_at: '2026-10-11T14:36:10Z'
  support: supports
  snapshot_sha256: 4499aa37aa0e0856bf2e1c6a94cac847ff2cc8692836661088dddfe09b0bb8ff
- evidence_id: atpase-cellular-context
  kind: primary_source
  reference: https://doi.org/10.1371/journal.ppat.1014043
  locator: Results 2.4/2.5, Methods 4.8, Discussion; visually inspected Figure 3 and
    supplement S13. May 2026 acknowledgements correction also read.
  summary: ATPase deletion and recode-matched K152A-associated phenotypes affect agglutination
    and extracellular IgG/IgM product detection. Expression and serum-free controls
    bound interpretations; direct ATP hydrolysis, localization and release/reset remain
    unresolved.
  accessed_at: '2026-10-11T14:36:10Z'
  support: supports
  snapshot_sha256: 8c772520b439afdcb24dbdfccfcd3b9af567ce74040fc288dc7f3dee2967f9ea
- evidence_id: remaining-member-coverage
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8081823/
  locator: M. bovis Methods accession lead only; separate ledger labels other species
    as abstract/search leads, not adopted experiments.
  summary: Additional members and construct/protocol discrepancies require follow-up.
    Retrieved accessions do not substitute for assessment of the M. bovis experiments,
    other species or the complete family.
  accessed_at: '2026-10-11T14:36:10Z'
  support: supports
  snapshot_sha256: e3f517f29224d9c50e55270aa2ccd70e3d916fade28d96203d75cd0780356d32
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T14:36:10Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: stage4-prior-review
  kind: prior_review
  reference: reviews/structured/20261021T114803Z-pf01732-stage4-record-review/review.yaml
  locator: Predecessor structured review 20261021T114803Z-pf01732-stage4-record-review
  accessed_at: '2026-10-25T13:20:33Z'
  support: supports
  snapshot_sha256: d89dabec56bbb02c51429d416d1d73ce37cab153b5c9d0e075c13d1ed8a54571
  summary: Predecessor review 20261021T114803Z-pf01732-stage4-record-review verified
    and linked for finding continuity and semantic-digest progression on PF01732.
- evidence_id: duf-projection-pf01732
  kind: record_content
  reference: data/families/PF01732.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-25T13:20:33Z'
  support: context_only
  snapshot_sha256: 9a203bfde22f95e2bb95679e710983da5b6e48adc2cc982a8b8322854e143b20
  quote: "id: Pfam:PF01732\npfam_id: PF01732\nname: Mycoplasma immunoglobulin protease\n\
    short_name: Myco_protease\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01732\n\
    counters:\n  proteins: 480\n  matches: 483\n  proteomes: 120\n  taxa: 185\n  structures:\
    \ 1\n  alphafold_models: 346\n  domain_architectures: 6\nprovenance:\n  snapshot_id:\
    \ interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR022382\ndescription: This is the serine protease domain\
    \ of MIP (Mycoplasma immunoglobulin protease), a protein\n  that is related to\
    \ pathogenicity of animal and human pathogenic Mycoplasmas [[cite:PUB00098027],[cite:PUB00098028],[cite:PUB00098029],[cite:PUB00151017]].\n\
    \  This protein functions together with the Ig binding protein M (MIB) to evade\
    \ host Ig-mediated defense\n  against the MIB-MIP system, which is a novel mechanism\
    \ that protects mycoplasma against host immune\n  response [[cite:PUB00098028],[cite:PUB00151017]].\
    \ MIB tightly interacts to the antigen-binding fragment\n  (Fab) and recruits\
    \ the MIP protease that is activated and cleaves the IgG heavy chain, disrupting\
    \ the\n  antigen binding site. Therefore, the MIB-MIP system appears to be crucial\
    \ to mycoplasma immune evasion\n  [[cite:PUB00151017]].\ncuration_history: history/records/PF01732\n\
    discussions:\n- discussion_id: mip-member-residue-and-partner-scope\n  prompt:\
    \ Resolve historical construct numbering and distinguish MIP, MIB and Protein\
    \ M.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: The exact GM12 MIP reference\
    \ supports PF01732 membership but not isolated-domain sufficiency.\n    The 2016\
    \ S727A label conflicts with full-length Y727/S759 and the 2021 S759A label; historical\
    \ plasmid\n    sequencing is needed before canonical residue-level claims.\n \
    \ evidence:\n  - reference: PMID:27114507\n    supports: PARTIAL\n    evidence_source:\
    \ inspected_primary_methods_and_figures\n    explanation: Joint cleavage, MIB\
    \ omission and published r-0582A effects are supported; clone numbering\n    \
    \  and exact antibody cleavage bond remain unresolved.\n  - reference: PMID:33674316\n\
    \    supports: PARTIAL\n    evidence_source: inspected_primary_methods_and_figures\n\
    \    explanation: Active and inactive joint mixtures dissociate antigen complexes,\
    \ and MIB alone also acts.\n      Cleavage is not required for this endpoint.\n\
    \  notes: Preserve frozen source bytes but do not repeat its conflation of MIB\
    \ with Protein M. The exact\n    ACU78687.1/UPI0001793D5F sequence maps PF01732\
    \ 290-776. Retired A0A446C0V0 has a different whole-protein\n    reference at\
    \ residue 810; do not use it as an exact GM12 mapping. Reconcile CH numbering\
    \ and antibody\n    sequences before assigning a cleavage bond.\n  posed_by: Codex\n\
    \  posed_date: '2026-10-11'\n- discussion_id: mip-cellular-mechanism-and-family-coverage\n\
    \  prompt: Assess remaining family members and discriminate ATPase-dependent cellular\
    \ mechanisms.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: Four graphs\
    \ retain twenty observed effects in selected GM12-derived systems, eleven direct\n\
    \    preparation effects and nine indirect cellular effects. They do not establish\
    \ universal family activity\n    or a resolved energy-transduction cycle.\n  evidence:\n\
    \  - reference: PMID:33674316\n    supports: PARTIAL\n    evidence_source: inspected_main_methods_and_low_resolution_figures\n\
    \    explanation: Whole-locus deletion affects cleavage and D12-serum agglutination;\
    \ retained single-pair\n      cells are not a reintroduction rescue. Supplements\
    \ and exact strain breakpoints remain unassessed.\n  - reference: PMID:41811866\n\
    \    supports: PARTIAL\n    evidence_source: inspected_primary_methods_main_and_supplement_figures\n\
    \    explanation: ATPase deletion and recode-matched K152A-associated effects\
    \ support system dependence\n      but not measured ATP hydrolysis or the proposed\
    \ opening/reset mechanism.\n  notes: See evidence/PF01732/mip-followup-ledger.txt.\
    \ Obtain 2021 supplements and full-resolution panels,\n    resolve protocol discrepancies\
    \ and exact mutant genotypes, inspect 2016 remaining controls and assess\n   \
    \ M. bovis, M. hominis, M. feriruminatoris and M. gallisepticum evidence with\
    \ independent member mapping.\n    Keep ATPase-mediated release, structural motions\
    \ and host-wide immune evasion as unproven extensions.\n    Remain IN_PROGRESS\
    \ with partial scientific self-review.\n  posed_by: Codex\n  posed_date: '2026-10-11'\n\
    causal_graphs:\n- graph_id: gm12-recombinant-mib-mip-cleavage\n  title: Joint\
    \ recombinant MIB-MIP preparations cleave goat antibody substrates\n  scope: 'Arfi\
    \ 2016 Figures 2C and 3B: purified goat IgG, Fab or F(ab'')2 exposed to GM12 MIP\
    \ r-0582 and\n    MIB r-0583; omission and published r-0582A controls.'\n  context:\
    \ Recombinant N-terminal TM replacements with His tags, expressed in E. coli;\
    \ PBS pH 7.4, MIP\n    added last. Main Methods specify 30 C and SI room temperature.\
    \ Exact doses and time for Figure 2C\n    remain unresolved; Figure 2B's 15-min\
    \ protocol is not silently substituted.\n  family_mapping: MIP82/MMCAP2_0582 reference\
    \ ACU78687.1 (861 aa) exactly matches UniParc UPI0001793D5F,\n    PF01732 290-776.\
    \ MIB83/MMCAP2_0583 is ACU78312.1 (750 aa), a distinct binding protein. Historical\n\
    \    recombinant termini and the r-0582A clone sequence are not independently\
    \ verified.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:436113\n  limitations:\
    \ DIRECT refers to net purified-preparation effects, not an isolated PF01732 domain\
    \ or an\n    atomic catalytic step. The paper's S727A label conflicts with Y727/S759\
    \ in the full-length reference\n    and S759A in 2021; retain r-0582A without\
    \ asserting a canonical residue. Folding effects are not excluded.\n    VH/CH\
    \ numbering and exact cleavage-bond identity remain unresolved; no universal substrate\
    \ or inhibitor\n    rule.\n  nodes:\n  - node_id: joint-igg\n    label: MIB plus\
    \ WT MIP plus purified goat IgG\n    node_type: ACTIVITY\n    grounding:\n   \
    \ - NCBIProtein:ACU78687.1\n    - NCBIProtein:ACU78312.1\n  - node_id: joint-fab\n\
    \    label: MIB plus WT MIP plus goat Fab\n    node_type: ACTIVITY\n    grounding:\n\
    \    - NCBIProtein:ACU78687.1\n    - NCBIProtein:ACU78312.1\n  - node_id: joint-fab2\n\
    \    label: MIB plus WT MIP plus goat F(ab')2\n    node_type: ACTIVITY\n    grounding:\n\
    \    - NCBIProtein:ACU78687.1\n    - NCBIProtein:ACU78312.1\n  - node_id: omit-mib\n\
    \    label: Omit MIB from the MIP-IgG reaction\n    node_type: PERTURBATION\n\
    \    grounding:\n    - NCBIProtein:ACU78687.1\n    - NCBIProtein:ACU78312.1\n\
    \  - node_id: published-r0582a\n    label: Replace WT MIP with published r-0582A\n\
    \    node_type: PERTURBATION\n    grounding:\n    - NCBIProtein:ACU78687.1\n \
    \ - node_id: igg-fragment\n    label: Approximately 44-kDa IgG heavy-chain fragment\n\
    \    node_type: STATE\n  - node_id: fab-fragment\n    label: Cleaved Fab heavy-chain\
    \ product\n    node_type: STATE\n  - node_id: fab2-fragment\n    label: Cleaved\
    \ F(ab')2 product\n    node_type: STATE\n  edges:\n  - edge_id: joint-produces-igg-fragment\n\
    \    subject: joint-igg\n    predicate: produces\n    object: igg-fragment\n \
    \   mechanism: The joint preparation yields a heavy-chain cleavage product absent\
    \ from the substrate-only\n      and MIB-omission controls; this is not MIP-alone\
    \ sufficiency.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:27114507\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC4868467/\n      snippet: Ig Cleavage\
    \ Assay\n      explanation: Figure 2C joint WT lane and immunoblot controls, visually\
    \ inspected; Figure 2B provides\n        corroborating pulled-down serum substrate.\n\
    \      cache_path: evidence/PF01732/arfi-2016-mib-mip.txt\n      cache_sha256:\
    \ 94a2b2c9903ae218c03c7ed7febaf05b03caed8381203b8e3e833c65d14b3020\n  - edge_id:\
    \ omit-mib-decreases-igg-fragment\n    subject: omit-mib\n    predicate: decreases\n\
    \    object: igg-fragment\n    mechanism: Omitting MIB leaves intact IgG heavy\
    \ chain without the joint-reaction product under the\n      tested conditions.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:27114507\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4868467/\n\
    \      snippet: Ig Cleavage Assay\n      explanation: Figure 2C MIP-plus-IgG lane\
    \ versus the joint reaction; necessity is assay-specific.\n      cache_path: evidence/PF01732/arfi-2016-mib-mip.txt\n\
    \      cache_sha256: 94a2b2c9903ae218c03c7ed7febaf05b03caed8381203b8e3e833c65d14b3020\n\
    \  - edge_id: r0582a-decreases-igg-fragment\n    subject: published-r0582a\n \
    \   predicate: decreases\n    object: igg-fragment\n    mechanism: Substituting\
    \ the published mutant preparation removes detectable product compared with\n\
    \      WT MIP in the MIB-containing reaction, without resolving its exact reference-sequence\
    \ lesion.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:27114507\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4868467/\n\
    \      snippet: Ig Cleavage Assay\n      explanation: Figure 2C r-0582A lane,\
    \ Results and Figure S5; residue-numbering discrepancy explicitly\n        retained.\n\
    \      cache_path: evidence/PF01732/arfi-2016-mib-mip.txt\n      cache_sha256:\
    \ 94a2b2c9903ae218c03c7ed7febaf05b03caed8381203b8e3e833c65d14b3020\n  - edge_id:\
    \ joint-produces-fab-fragment\n    subject: joint-fab\n    predicate: produces\n\
    \    object: fab-fragment\n    mechanism: The joint preparation cleaves the Fab\
    \ substrate, producing the displayed antibody-reactive\n      fragment; no exact\
    \ cleavage bond or rate is assigned.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:27114507\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4868467/\n      snippet:\
    \ Ig Cleavage Assay\n      explanation: Figure 3B Fab immunoblot lanes and caption,\
    \ visually inspected.\n      cache_path: evidence/PF01732/arfi-2016-mib-mip.txt\n\
    \      cache_sha256: 94a2b2c9903ae218c03c7ed7febaf05b03caed8381203b8e3e833c65d14b3020\n\
    \  - edge_id: joint-produces-fab2-fragment\n    subject: joint-fab2\n    predicate:\
    \ produces\n    object: fab2-fragment\n    mechanism: The joint preparation cleaves\
    \ F(ab')2 in the corresponding fragment assay, supporting a\n      Fab-region\
    \ event without adopting the paper's nonstandard CH numbering.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:27114507\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4868467/\n\
    \      snippet: Ig Cleavage Assay\n      explanation: Figure 3B F(ab')2 lanes\
    \ and caption; Figure 3C Edman result retained as context, not\n        a universal\
    \ residue coordinate.\n      cache_path: evidence/PF01732/arfi-2016-mib-mip.txt\n\
    \      cache_sha256: 94a2b2c9903ae218c03c7ed7febaf05b03caed8381203b8e3e833c65d14b3020\n\
    - graph_id: gm12-antigen-complex-dissociation\n  title: Active and inactive MIB-MIP\
    \ mixtures dissociate antigen-IgG complexes\n  scope: Nottelet 2021 Figure 4A-F,\
    \ preassembled goat IgG with human transferrin, human albumin or HRP;\n    addition\
    \ of MIB83 plus WT or S759A MIP82.\n  context: SEC assay in 200 ul PBS with 3\
    \ uM IgG, 10 uM antigen and 6 uM each added MIB/MIP. Results/Methods\n    give\
    \ 20-min room-temperature preincubation, caption 30 min. MIB-only positive comparisons\
    \ also dissociate\n    complexes. The separate 15-ul cleavage-assay concentrations\
    \ are not used here.\n  family_mapping: GM12 MIP82 reference ACU78687.1, PF01732\
    \ 290-776; 2021 constructs delete MIP residues\n    1-33 and MIB 1-35 and carry\
    \ N-terminal His tags. The full-length reference has Ser759, but complete\n  \
    \  experimental clone sequences are not independently verified.\n  scope_status:\
    \ MECHANISTIC\n  taxon: NCBITaxon:436113\n  limitations: DIRECT joint-preparation\
    \ effects on SEC separation, not MIP-alone sufficiency or proteolysis-dependent\n\
    \    antigen release. MIB alone and MIB plus inactive MIP also act. WT and inactive\
    \ mixtures remain separate\n    nodes; these effects are not connected as a cleavage-then-release\
    \ chain. Main PMC panels were visually\n    inspected at 440-pixel resolution;\
    \ no calibrated peak integration or affinity measurement.\n  nodes:\n  - node_id:\
    \ active-joint-mixture\n    label: Add MIB83 plus WT MIP82 to the preassembled\
    \ complex\n    node_type: PERTURBATION\n    grounding:\n    - NCBIProtein:ACU78687.1\n\
    \    - NCBIProtein:ACU78312.1\n  - node_id: inactive-joint-mixture\n    label:\
    \ Add MIB83 plus S759A MIP82 to the preassembled complex\n    node_type: PERTURBATION\n\
    \    grounding:\n    - NCBIProtein:ACU78687.1\n    - NCBIProtein:ACU78312.1\n\
    \  - node_id: transferrin-separated\n    label: Transferrin separated from IgG-containing\
    \ fractions\n    node_type: STATE\n  - node_id: albumin-separated\n    label:\
    \ Albumin separated from IgG-containing fractions\n    node_type: STATE\n  - node_id:\
    \ hrp-separated\n    label: HRP separated from IgG-containing fractions\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: active-separates-transferrin\n    subject: active-joint-mixture\n\
    \    predicate: produces\n    object: transferrin-separated\n    mechanism: In\
    \ the transferrin experiment the joint active mixture yields separated antigen\
    \ and Ig-containing\n      fractions instead of the initial high-mass aggregate.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:33674316\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7935358/\n\
    \      snippet: Antigen-bound immunoglobulin cleavage\n      explanation: Figure\
    \ 4A/D SEC profiles and fraction gels.\n      cache_path: evidence/PF01732/nottelet-2021-mib-mip.txt\n\
    \      cache_sha256: 4499aa37aa0e0856bf2e1c6a94cac847ff2cc8692836661088dddfe09b0bb8ff\n\
    \  - edge_id: inactive-separates-transferrin\n    subject: inactive-joint-mixture\n\
    \    predicate: produces\n    object: transferrin-separated\n    mechanism: The\
    \ MIB plus inactive-MIP mixture also separates transferrin, showing that IgG cleavage\n\
    \      is not required for this observed dissociation.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:33674316\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7935358/\n\
    \      snippet: Antigen-bound immunoglobulin cleavage\n      explanation: Figure\
    \ 4A/D inactive-mixture SEC/fraction comparisons; MIB-alone control also positive.\n\
    \      cache_path: evidence/PF01732/nottelet-2021-mib-mip.txt\n      cache_sha256:\
    \ 4499aa37aa0e0856bf2e1c6a94cac847ff2cc8692836661088dddfe09b0bb8ff\n  - edge_id:\
    \ active-separates-albumin\n    subject: active-joint-mixture\n    predicate:\
    \ produces\n    object: albumin-separated\n    mechanism: In the albumin experiment\
    \ the joint active mixture separates antigen from Ig-containing\n      fractions.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:33674316\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7935358/\n\
    \      snippet: Antigen-bound immunoglobulin cleavage\n      explanation: Figure\
    \ 4B/E SEC profiles and fraction gels.\n      cache_path: evidence/PF01732/nottelet-2021-mib-mip.txt\n\
    \      cache_sha256: 4499aa37aa0e0856bf2e1c6a94cac847ff2cc8692836661088dddfe09b0bb8ff\n\
    \  - edge_id: inactive-separates-albumin\n    subject: inactive-joint-mixture\n\
    \    predicate: produces\n    object: albumin-separated\n    mechanism: The inactive-MIP\
    \ joint mixture also separates albumin; the observation does not assign\n    \
    \  dissociation to MIP catalysis.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:33674316\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7935358/\n      snippet:\
    \ Antigen-bound immunoglobulin cleavage\n      explanation: Figure 4B/E inactive-mixture\
    \ comparisons and MIB-only control.\n      cache_path: evidence/PF01732/nottelet-2021-mib-mip.txt\n\
    \      cache_sha256: 4499aa37aa0e0856bf2e1c6a94cac847ff2cc8692836661088dddfe09b0bb8ff\n\
    \  - edge_id: active-separates-hrp\n    subject: active-joint-mixture\n    predicate:\
    \ produces\n    object: hrp-separated\n    mechanism: In the HRP experiment the\
    \ joint active mixture yields separated antigen and Ig-containing\n      fractions;\
    \ the polyclonal heavy-chain product pattern does not define a single antibody\
    \ sequence.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:33674316\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC7935358/\n      snippet: Antigen-bound\
    \ immunoglobulin cleavage\n      explanation: Figure 4C/F SEC profiles and fraction\
    \ gels.\n      cache_path: evidence/PF01732/nottelet-2021-mib-mip.txt\n      cache_sha256:\
    \ 4499aa37aa0e0856bf2e1c6a94cac847ff2cc8692836661088dddfe09b0bb8ff\n  - edge_id:\
    \ inactive-separates-hrp\n    subject: inactive-joint-mixture\n    predicate:\
    \ produces\n    object: hrp-separated\n    mechanism: The MIB plus inactive-MIP\
    \ mixture also separates HRP, retaining a cleavage-independent\n      dissociation\
    \ context.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:33674316\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC7935358/\n      snippet: Antigen-bound\
    \ immunoglobulin cleavage\n      explanation: Figure 4C/F inactive-mixture comparisons\
    \ and MIB-only control.\n      cache_path: evidence/PF01732/nottelet-2021-mib-mip.txt\n\
    \      cache_sha256: 4499aa37aa0e0856bf2e1c6a94cac847ff2cc8692836661088dddfe09b0bb8ff\n\
    - graph_id: gm12-mib-mip-locus-deletion\n  title: MIB-MIP locus deletion changes\
    \ cellular cleavage and immune-serum agglutination\n  scope: Nottelet 2021 Figure\
    \ 5B/C/E/F, GM12-derived Mmc WT versus deletion of all four MIB-MIP pairs;\n \
    \   the single retained MIB83-MIP82 pair is a separate positive comparator, not\
    \ a rescue.\n  context: Cleavage assays use about 1e9 washed late-exponential\
    \ cells in 15 ul SP5 without FBS, 100 ng/ul\n    purified serum IgG or 2% albumin-depleted\
    \ D12 goat serum, 30 min at 37 C, supernatant immunoblot.\n    Agglutination is\
    \ a different overnight static 37 C assay; Methods give 4% serum and caption 2%.\
    \ D0\n    serum does not produce the same cellular IgM cleavage/agglutination\
    \ response.\n  family_mapping: The deleted cluster includes MIP82/MMCAP2_0582,\
    \ ACU78687.1 with PF01732 290-776, but\n    also three other MIPs and four MIBs.\
    \ Whole-locus effects cannot be attributed exclusively to this\n    protein or\
    \ its domain. Main Figure 5B establishes the design; exact strain lineage and\
    \ nucleotide\n    breakpoints in inaccessible supplements remain unverified here.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:436113\n  limitations: INDIRECT\
    \ genotype effects. Single-pair retention is not reintroduction complementation.\n\
    \    Anti-HRP IgG is not detectably cleaved by cells despite purified-system activity.\
    \ OD310 measures settled\n    aggregates, not growth. Results panel cross-references\
    \ are offset; actual Figure 5C/E/F is used. Low-resolution\n    visual inspection\
    \ supports qualitative direction, not numeric effect sizes or a domain-specific\
    \ mechanism.\n  nodes:\n  - node_id: whole-locus-deletion\n    label: Delete all\
    \ four MIB-MIP pairs versus WT\n    node_type: PERTURBATION\n    grounding:\n\
    \    - NCBIProtein:ACU78687.1\n    - NCBIProtein:ACU78312.1\n  - node_id: cellular-igg-product\n\
    \    label: Extracellular IgG heavy-chain cleavage product\n    node_type: STATE\n\
    \  - node_id: cellular-igm-product\n    label: Extracellular D12-serum IgM cleavage\
    \ product\n    node_type: STATE\n  - node_id: d12-agglutination\n    label: D12-serum\
    \ cellular agglutination\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: deletion-decreases-igg-product\n\
    \    subject: whole-locus-deletion\n    predicate: decreases\n    object: cellular-igg-product\n\
    \    mechanism: The deleted strain lacks the serum-IgG cleavage product detected\
    \ in WT and the single-pair\n      comparator in the 30-min cellular assay.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:33674316\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7935358/\n\
    \      snippet: Antigen-bound immunoglobulin cleavage\n      explanation: Figure\
    \ 5C serum-IgG lanes; Methods in cellulo immunoglobulin cleavage.\n      cache_path:\
    \ evidence/PF01732/nottelet-2021-mib-mip.txt\n      cache_sha256: 4499aa37aa0e0856bf2e1c6a94cac847ff2cc8692836661088dddfe09b0bb8ff\n\
    \  - edge_id: deletion-decreases-igm-product\n    subject: whole-locus-deletion\n\
    \    predicate: decreases\n    object: cellular-igm-product\n    mechanism: Deletion\
    \ reduces the IgM cleavage product detected with D12 immune serum; the D0 condition\n\
    \      is not silently pooled with it.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:33674316\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7935358/\n      snippet:\
    \ Antigen-bound immunoglobulin cleavage\n      explanation: Figure 5E D12 IgM\
    \ lanes, compared with WT and the retained-pair strain.\n      cache_path: evidence/PF01732/nottelet-2021-mib-mip.txt\n\
    \      cache_sha256: 4499aa37aa0e0856bf2e1c6a94cac847ff2cc8692836661088dddfe09b0bb8ff\n\
    \  - edge_id: deletion-increases-agglutination\n    subject: whole-locus-deletion\n\
    \    predicate: increases\n    object: d12-agglutination\n    mechanism: Under\
    \ the distinct overnight D12-serum protocol the deleted strain forms visible aggregates\n\
    \      and higher settled-aggregate OD310 than WT.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:33674316\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7935358/\n\
    \      snippet: Antigen-bound immunoglobulin cleavage\n      explanation: Figure\
    \ 5F micrographs and OD310 panel, with D0 and single-pair comparators; 2%/4% serum\n\
    \        discrepancy retained.\n      cache_path: evidence/PF01732/nottelet-2021-mib-mip.txt\n\
    \      cache_sha256: 4499aa37aa0e0856bf2e1c6a94cac847ff2cc8692836661088dddfe09b0bb8ff\n\
    - graph_id: gm12-atpase-mutant-cellular-effects\n  title: ATPase-cluster and recode-matched\
    \ K152A perturbations impair the cellular system\n  scope: Berlureau 2026 Figure\
    \ 3 and supplement S13, GM12-derived Mmc 1.1 versus DeltaATPase, and MMCAP2_0575\n\
    \    G3S/K4R/K152A versus the G3S/K4R recode control.\n  context: Delete ATPase\
    \ loci 0581 through 0575 without deleting the upstream MIB-MIP cluster. Pellet\n\
    \    2 ml late-log culture and resuspend in 1 ml SP5 plus 2% B4J12 immune goat\
    \ serum; 1-h incubation, temperature\n    not specified in Methods 4.8. Image\
    \ aggregates and immunoblot separated supernatant/pellet. Serum-free\n    controls\
    \ remain dispersed and lack antibody signal.\n  family_mapping: MIP82/MMCAP2_0582\
    \ is the PF01732-bearing ACU78687.1 reference, residues 290-776; all\n    four\
    \ MIB/MIP pairs remain in these ATPase mutants. ATPase beta-like 0575 is a partner,\
    \ not the PF01732\n    protein. K152A belongs to 0575 and occurs with G3S/K4R,\
    \ not as an isolated substitution against WT.\n  scope_status: PHENOTYPIC\n  taxon:\
    \ NCBITaxon:436113\n  limitations: INDIRECT cellular effects with one clone per\
    \ genotype, other SNPs/INDELs, no complementation\n    and extra DeltaATPase passages/23S-rRNA\
    \ changes. MIB/MIP abundances are broadly WT-like but localization/assembly\n\
    \    are unresolved. No ATP-hydrolysis rate, transmembrane energy transfer or\
    \ release/reset transition\n    was measured. The proposed model predicts pellet\
    \ cleavage products not clearly observed. May 2026\n    correction concerns acknowledgements,\
    \ not experimental data.\n  nodes:\n  - node_id: atpase-cluster-deletion\n   \
    \ label: Delete ATPase cluster versus Mmc 1.1\n    node_type: PERTURBATION\n \
    \ - node_id: k152a-versus-recode\n    label: Add 0575 K152A in the shared G3S/K4R\
    \ background\n    node_type: PERTURBATION\n  - node_id: one-hour-agglutination\n\
    \    label: Immune-serum agglutination after 1 h\n    node_type: PHENOTYPE\n \
    \ - node_id: supernatant-igg44\n    label: Supernatant IgG approximately 44-kDa\
    \ cleavage product\n    node_type: STATE\n  - node_id: supernatant-igm68\n   \
    \ label: Supernatant IgM approximately 68-kDa cleavage product\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: atpase-deletion-increases-agglutination\n    subject:\
    \ atpase-cluster-deletion\n    predicate: increases\n    object: one-hour-agglutination\n\
    \    mechanism: ATPase-cluster deletion increases visible flocculation and cellular\
    \ aggregates compared\n      with Mmc 1.1 under immune-serum exposure.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:41811866\n      source_url: https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1014043\n\
    \      snippet: Functional assessment of the\n      explanation: Figure 3D and\
    \ S13A, visually inspected; serum-free controls remain dispersed.\n      cache_path:\
    \ evidence/PF01732/berlureau-2026-atpase.txt\n      cache_sha256: 8c772520b439afdcb24dbdfccfcd3b9af567ce74040fc288dc7f3dee2967f9ea\n\
    \  - edge_id: atpase-deletion-decreases-igg44\n    subject: atpase-cluster-deletion\n\
    \    predicate: decreases\n    object: supernatant-igg44\n    mechanism: The deletion\
    \ lacks the detectable supernatant IgG cleavage band present in Mmc 1.1, without\n\
    \      resolving whether processing, localization or product release is impaired.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:41811866\n      source_url: https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1014043\n\
    \      snippet: Functional assessment of the\n      explanation: Figure 3E and\
    \ S13B IgG supernatant lanes.\n      cache_path: evidence/PF01732/berlureau-2026-atpase.txt\n\
    \      cache_sha256: 8c772520b439afdcb24dbdfccfcd3b9af567ce74040fc288dc7f3dee2967f9ea\n\
    \  - edge_id: atpase-deletion-decreases-igm68\n    subject: atpase-cluster-deletion\n\
    \    predicate: decreases\n    object: supernatant-igm68\n    mechanism: The deletion\
    \ lacks the detectable supernatant IgM cleavage band present in Mmc 1.1; intact\n\
    \      pellet IgM is not evidence of successful cleavage.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:41811866\n      source_url: https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1014043\n\
    \      snippet: Functional assessment of the\n      explanation: Figure 3F and\
    \ S13B IgM supernatant/pellet lanes.\n      cache_path: evidence/PF01732/berlureau-2026-atpase.txt\n\
    \      cache_sha256: 8c772520b439afdcb24dbdfccfcd3b9af567ce74040fc288dc7f3dee2967f9ea\n\
    \  - edge_id: k152a-increases-agglutination\n    subject: k152a-versus-recode\n\
    \    predicate: increases\n    object: one-hour-agglutination\n    mechanism:\
    \ The G3S/K4R/K152A strain agglutinates more than the G3S/K4R recode control,\
    \ supporting\n      an additional K152A-associated cellular defect without measuring\
    \ ATP catalysis.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:41811866\n      source_url:\
    \ https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1014043\n\
    \      snippet: Functional assessment of the\n      explanation: Figure 3D and\
    \ S13A matched recode/triple-substitution comparison.\n      cache_path: evidence/PF01732/berlureau-2026-atpase.txt\n\
    \      cache_sha256: 8c772520b439afdcb24dbdfccfcd3b9af567ce74040fc288dc7f3dee2967f9ea\n\
    \  - edge_id: k152a-decreases-igg44\n    subject: k152a-versus-recode\n    predicate:\
    \ decreases\n    object: supernatant-igg44\n    mechanism: The triple-substitution\
    \ strain lacks the IgG product detected with the recode control,\n      despite\
    \ broadly maintained MIB/MIP abundance.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:41811866\n\
    \      source_url: https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1014043\n\
    \      snippet: Functional assessment of the\n      explanation: Figure 3E and\
    \ S13B supernatant lanes; Figure 3B/C supplies expression context.\n      cache_path:\
    \ evidence/PF01732/berlureau-2026-atpase.txt\n      cache_sha256: 8c772520b439afdcb24dbdfccfcd3b9af567ce74040fc288dc7f3dee2967f9ea\n\
    \  - edge_id: k152a-decreases-igm68\n    subject: k152a-versus-recode\n    predicate:\
    \ decreases\n    object: supernatant-igm68\n    mechanism: The triple-substitution\
    \ strain lacks the IgM product detected with the recode control;\n      neither\
    \ this effect nor predicted Walker-A conservation proves an ATP-driven reset step.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:41811866\n      source_url: https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1014043\n\
    \      snippet: Functional assessment of the\n      explanation: Figure 3F and\
    \ S13B IgM lanes; Discussion explicitly bounds the reset hypothesis.\n      cache_path:\
    \ evidence/PF01732/berlureau-2026-atpase.txt\n      cache_sha256: 8c772520b439afdcb24dbdfccfcd3b9af567ce74040fc288dc7f3dee2967f9ea\n\
    curation_events:\n- timestamp: '2026-10-11T14:30:08Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate four scoped PF01732 MIB-MIP causal\
    \ graphs\n  history_record: history/records/PF01732/2026-10-11T143008Z-codex-ef3abd.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-11T14:36:38Z'\n\
    \  curator: Codex\n  action: REVIEW\n  outcome: needs_followup\n  summary: Retain\
    \ partial scientific self-review of PF01732 causal contexts\n  history_record:\
    \ history/records/PF01732/2026-10-11T143638Z-codex-ebbba7.yaml\n  event_index:\
    \ 0\n  llm_assisted: true\n- timestamp: '2026-10-21T09:52:00Z'\n  curator: Antigravity\n\
    \  action: EDIT\n  outcome: changed\n  summary: Ground four MIB-MIP causal-graph\
    \ nodes with verified native NCBIProtein accessions\n  history_record: history/records/PF01732/2026-10-21T095200Z-antigravity-74aa49.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-25T11:15:00Z'\n\
    \  curator: Antigravity\n  action: EDIT\n  outcome: changed\n  summary: Ground\
    \ PF01732 causal-graph protein/gene/complex nodes with NCBIProtein:ACU78687.1,\
    \ NCBIProtein:ACU78312.1\n  history_record: history/records/PF01732/2026-10-25T111500Z-antigravity-7ae81f.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: GenBank ACU78687.1, 861 aa, MMCAP2_0582 in GM12, exactly matches UniParc
    UPI0001793D5F and its PF01732 290-776 interval. MIB83 is the separate ACU78312.1
    protein. The exact GM12 sequence differs at residue 810 from the retired A0A446C0V0
    reference. Whole-protein, partner-system and whole-locus effects are not isolated-domain
    sufficiency. Historical mutant plasmids and full 2021 strain breakpoints remain
    incompletely verified.
  target_ids:
  - PF01732
  evidence_ids:
  - identity
  - primary
  - dissociation-and-locus-deletion
  - atpase-cellular-context
  - remaining-member-coverage
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Eleven DIRECT observed edges concern net joint-preparation effects, not
    MIP-alone sufficiency or atomistic chemistry. Inactive-MIP and MIB-only dissociation
    controls explicitly prevent a cleavage-required release chain. Nine INDIRECT effects
    preserve 2021 whole-locus deletion versus WT and 2026 ATPase-cluster deletion
    versus Mmc 1.1 or K152A-plus-recode versus recode. Single-pair retention is not
    a reintroduction rescue. Serum doses, timing, detection limits and genotype background
    are retained; no ATP-hydrolysis or reset transition is promoted from a hypothesis.
  target_ids:
  - PF01732
  evidence_ids:
  - primary
  - native
  - dissociation-and-locus-deletion
  - atpase-cellular-context
  - remaining-member-coverage
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Exact historical recombinant sequences, residue numbering, antibody cleavage-bond
    mapping, protocol discrepancies, full-resolution 2021 panels and inaccessible
    supplements remain open. Other MIP paralogs, immunoglobulin classes and M. bovis,
    M. hominis, M. feriruminatoris and M. gallisepticum primary leads remain uncurated.
    The frozen MIB/Protein M conflation is qualified in maintained discussion without
    rewriting source bytes. No family-wide functional proof or intact-host causal
    chain is established.
  target_ids:
  - PF01732
  evidence_ids:
  - primary
- assessment_id: cycle3-partner-grounding-verification
  area: representation
  topic: Cycle 3 causal-graph and protein-node grounding verification
  outcome: supported
  summary: 'Cycle 3 Stage 3 (PR #357) grounded the two MIB-MIP two-protein perturbation
    nodes (omit-mib and whole-locus-deletion) to Mycoplasma mycoides subsp. capri
    GM12 MIB and MIP (NCBIProtein:ACU78687.1 and NCBIProtein:ACU78312.1); multi-gene
    ATPase cluster comparison nodes in gm12-atpase-mutant-cellular-effects remain
    ungrounded at the cluster level. Stage 4 frozen-inventory review verified all
    causal graphs and grounded nodes against primary evidence caches.'
  target_ids:
  - PF01732
  evidence_ids:
  - stage4-prior-review
findings:
- finding_id: additional-contexts
  issue_key: pf01732-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve construct and assay discrepancies and extend member-specific MIP
    coverage
  description: Verify the older r-0582A clone and canonical numbering, reconcile antibody
    sequences and cleavage positions, obtain 2021 strain/assay supplements and full-resolution
    panels, resolve temperature/time/serum-dose discrepancies and assess remaining
    family-member studies independently. Distinguish MIB-only dissociation, joint
    proteolysis, cellular genotype effects and untested ATPase-reset hypotheses. Append
    a successor review with actual coverage rather than promoting the record from
    partial evidence.
  target_ids:
  - PF01732
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - dissociation-and-locus-deletion
  - atpase-cellular-context
  - remaining-member-coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01732.yaml
    role: Human-owned scientific overlay
  previous_occurrences:
  - repository: CultureBotAI/DUFMech
    review_id: 20261021T114803Z-pf01732-stage4-record-review
    finding_id: additional-contexts
actions:
- action_id: extend-contexts
  description: Verify the older r-0582A clone and canonical numbering, reconcile antibody
    sequences and cleavage positions, obtain 2021 strain/assay supplements and full-resolution
    panels, resolve temperature/time/serum-dose discrepancies and assess remaining
    family-member studies independently. Distinguish MIB-only dissociation, joint
    proteolysis, cellular genotype effects and untested ATPase-reset hypotheses. Append
    a successor review with actual coverage rather than promoting the record from
    partial evidence.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01732
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Arfi 2016 Figures 2/3/4/S5, Nottelet 2021 main Figures 4/5 at 440-pixel PMC resolution,
  and Berlureau 2026 Figure 3/S13 at large size were visually inspected. Publisher
  supplements/PDF and PMC enlarged-figure pages were inaccessible; Table S2/S9/S11/S12
  and raw data were not independently analyzed. No calibrated densitometry, raw proteomics/genome
  reanalysis, historical clone resequencing, replication or exhaustive family survey
  was performed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
