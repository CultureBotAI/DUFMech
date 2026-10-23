# PF01923 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review

- Review: 20261023T092550Z-pf01923-c2s4-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-23T09:25:49Z
- Finished UTC: 2026-10-23T09:25:50Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Twenty-seven graphs retain77 OBSERVED effects:56 DIRECT biochemical/physical readouts and21 INDIRECT complementation/growth effects, across18 MECHANISTIC and9 PHENOTYPIC contexts. All displayed quotations were checked against primary HTML and all evidence hashes/native graph fields validated. Status remains IN_PROGRESS; this is a same-agent partial scientific assessment, not an independent expert review or exhaustive family characterization. Stage 4 frozen-inventory audit identified an open protein-grounding gap (pf01923-sepduo-and-seeutt-assays-missing-protein-grounding) across three Salmonella enterica LT2 PduO/EutT biochemical causal graphs (sepduo-inhibition-2004, sepduo-metal-additions-2004, seeutt-metal-oxygen-2014) preserved for Stage 5 grouped remediation.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Ascending remaining frozen Pfam accession after PF01918. All8296 families and open context follow-ups remain in the corpus-wide goal.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base fde7d143a6b952fbc63b390cbfc27de38ac7701b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01923 | data/families/PF01923.yaml | generated | PF01923 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01923 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01923.

Frozen PF01923/Cob_adeno_trans/IPR016030/EX_DUF and historical DUF80 identity are unchanged. Q8ZNR5v1 maps3-166, Q9ZFV4v1 maps92-246, Q50EJ2v1 maps3-169, Q96EY8v1 maps58-227, A0A0H3GFM5v1 maps83-242. Listeria10403S mapping is supported by strain-specific reference, primary alignment and terminal primers, not presumed EGD-e identity. SeEutT H67/C79/C80/C83 and LrPduO F187/tail183-188 lie outside PF01923. Modern reference mapping is distinguished from historical recombinant construct verification.

### Directed effects and limits

graph: supported. Targets: PF01923.

Joint assay inputs make cofactors, substrates and reducing systems explicit. SePduO reaction/product, truncation, metal/inhibitor and growth contexts are separate. LrPduO crystal coordination, pre-reduced and reduction-coupled kinetics, and text-only complementation remain separate. SeEutT whole-protein motif effects are not assigned to the mapped Pfam interval. LmEutT cob(I)inamide acceptance is not contradicted by cob(II)inamide negatives; metal-less wording does not remove MgATP. Human FDX1 synthesis, ATP-EPR complexes and ADP-R190H titrations preserve distinct conditions. No direct product-release pathway, native exclusive electron donor, patient-outcome arrow or family-wide catalytic sufficiency is invented.

### Remaining family coverage

completeness: concern. Targets: PF01923.

Eight primary full-text studies plus Costa/Gouda publisher supplements support selected experiments, not every15667 frozen protein or every published context. MMAB product transfer/sequestration/repair/allostery, other EutT coordination and product studies, Lm2020 mutations, further species and exact historical constructs remain open. Moore2014 original supplement is inaccessible through attempted endpoints; described controls are text-only. StMaurice2008 is a structural/mapping lead, and Gouda2021 was inspected for purification only.

### Causal-graph taxon and protein-node grounding consistency

representation: concern. Targets: PF01923.

In curation/families/PF01923.yaml, three causal graphs have zero grounded protein nodes even though family_mapping explicitly maps the tested enzyme to a verified Salmonella enterica LT2 (NCBITaxon:99287) UniProtKB accession in evidence/PF01923/identity.txt: sepduo-inhibition-2004 (activity: AdoCbl-forming activity, lines 335-337) and sepduo-metal-additions-2004 (activity: AdoCbl-forming activity, lines 420-422) omit grounding: [UniProtKB:Q8ZNR5] (S. enterica LT2 PduO STM2050, UniProtKB:Q8ZNR5), whereas sibling graphs sepduo-truncation-activity-2004 and sepduo-triphosphate-2004 ground PduO activity to UniProtKB:Q8ZNR5; and seeutt-metal-oxygen-2014 (activity: Coupled AdoCbl-forming activity, lines 1207-1209) omits grounding: [UniProtKB:Q9ZFV4] (S. enterica LT2 EutT STM2456, UniProtKB:Q9ZFV4), whereas sibling graph seeutt-variant-activity-2014 grounds EutT perturbations to UniProtKB:Q9ZFV4.

## Findings

### additional-contexts: Resolve construct and source discrepancies and extend uncurated ACAT contexts

minor / open / confirmed; issue key: pf01923-causal-context-coverage.

Resolve historical PduO/EutT/MMAB constructs and the retained unit/label discrepancies, inspect Moore2014 supplemental controls and remaining mutant/spectroscopy studies, and curate directly evidenced MMAB cofactor-transfer, sequestration and repair pathways with exact species/partner scope. Inspect other experimentally mapped members; do not infer absent function from unperformed searches or promote to REVIEWED because graph integrity passes.

### sepduo-and-seeutt-assays-missing-protein-grounding: Ground Salmonella enterica PduO and EutT AdoCbl-forming activity nodes in sepduo-inhibition-2004, sepduo-metal-additions-2004, and seeutt-metal-oxygen-2014

minor / open / confirmed; issue key: pf01923-sepduo-and-seeutt-assays-missing-protein-grounding.

In curation/families/PF01923.yaml, three causal graphs have zero grounded protein nodes even though family_mapping explicitly maps the tested enzyme to a verified Salmonella enterica LT2 (NCBITaxon:99287) UniProtKB accession in evidence/PF01923/identity.txt: sepduo-inhibition-2004 (activity: AdoCbl-forming activity, lines 335-337) and sepduo-metal-additions-2004 (activity: AdoCbl-forming activity, lines 420-422) omit grounding: [UniProtKB:Q8ZNR5] (S. enterica LT2 PduO STM2050, UniProtKB:Q8ZNR5), whereas sibling graphs sepduo-truncation-activity-2004 and sepduo-triphosphate-2004 ground PduO activity to UniProtKB:Q8ZNR5; and seeutt-metal-oxygen-2014 (activity: Coupled AdoCbl-forming activity, lines 1207-1209) omits grounding: [UniProtKB:Q9ZFV4] (S. enterica LT2 EutT STM2456, UniProtKB:Q9ZFV4), whereas sibling graph seeutt-variant-activity-2014 grounds EutT perturbations to UniProtKB:Q9ZFV4.

## Recommended Actions And Acceptance Checks

### extend-contexts

Resolve historical PduO/EutT/MMAB constructs and the retained unit/label discrepancies, inspect Moore2014 supplemental controls and remaining mutant/spectroscopy studies, and curate directly evidenced MMAB cofactor-transfer, sequestration and repair pathways with exact species/partner scope. Inspect other experimentally mapped members; do not infer absent function from unperformed searches or promote to REVIEWED because graph integrity passes.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC10507449/; Gouda2023 Figures1-3; publisher supplementMethodsS2-S6/FiguresS1-S4. Separate ledgers retain seven other primary studies. | supports | Recombinant human MMAB supports NADPH/FDXR/FDX1-dependent AdoCbl synthesis; four tested substitutions decrease the coupled activity. Separate ATP-EPR complexes and ADP-R190H redox titrations are not merged into a single observed reaction trajectory. Supplemental ADP methods qualify the conflicting ATP caption; exact MMAB construct endpoints remain open. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01923/; Accession and domain locations; paired UniProt identity facts | supports | Frozen PF01923/Cob_adeno_trans/IPR016030/EX_DUF and historical DUF80 identity are unchanged. Q8ZNR5v1 maps3-166, Q9ZFV4v1 maps92-246, Q50EJ2v1 maps3-169, Q96EY8v1 maps58-227, A0A0H3GFM5v1 maps83-242. Listeria10403S mapping is supported by strain-specific reference, primary alignment and terminal primers, not presumed EGD-e identity. SeEutT H67/C79/C80/C83 and LrPduO F187/tail183-188 lie outside PF01923. Modern reference mapping is distinguished from historical recombinant construct verification. |
| johnson-2001 | https://pmc.ncbi.nlm.nih.gov/articles/PMC95042/; Methods, Results and exact figure/table locators in the retained per-study ledger | supports | Primary experimental readouts, tested constructs, controls, conditional negatives and source discrepancies are retained without family-wide transfer. |
| johnson-2004 | https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/; Methods, Results and exact figure/table locators in the retained per-study ledger | supports | Primary experimental readouts, tested constructs, controls, conditional negatives and source discrepancies are retained without family-wide transfer. |
| stmaurice-2007 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6574208/; Methods, Results and exact figure/table locators in the retained per-study ledger | supports | Primary experimental readouts, tested constructs, controls, conditional negatives and source discrepancies are retained without family-wide transfer. |
| mera-2009 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2666787/; Methods, Results and exact figure/table locators in the retained per-study ledger | supports | Primary experimental readouts, tested constructs, controls, conditional negatives and source discrepancies are retained without family-wide transfer. |
| mera-2010 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2823439/; Methods, Results and exact figure/table locators in the retained per-study ledger | supports | Primary experimental readouts, tested constructs, controls, conditional negatives and source discrepancies are retained without family-wide transfer. |
| moore-2014 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3911174/; Methods, Results and exact figure/table locators in the retained per-study ledger | supports | Primary experimental readouts, tested constructs, controls, conditional negatives and source discrepancies are retained without family-wide transfer. |
| costa-2018 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6113058/; Methods, Results and exact figure/table locators in the retained per-study ledger | supports | Primary experimental readouts, tested constructs, controls, conditional negatives and source discrepancies are retained without family-wide transfer. |
| coverage | evidence/PF01923/coverage.txt; Scoped source discovery, mapping and access ledger | supports | Additional scientific contexts and exact construct/source uncertainties remain open; inaccessible sources are not negative experimental results. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| stage4-prior-review | reviews/structured/20261012T015942Z-pf01923-pduo-eutt-mmab-assay-and-domain-contexts/review.yaml; Predecessor structured review 20261012T015942Z-pf01923-pduo-eutt-mmab-assay-and-domain-contexts | supports | Predecessor review 20261012T015942Z-pf01923-pduo-eutt-mmab-assay-and-domain-contexts verified and linked for finding continuity and semantic-digest progression on PF01923. |
| duf-projection-pf01923 | data/families/PF01923.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Original Johnson2001 Figures2/3/5; Johnson2004 Figures2-4; StMaurice2007 Figure1; Mera2009 Figures1-4; Mera2010 Figures2-4; Moore2014 Figures2/3/5; Costa2018 Figures2-7 and supplementS2/S3/S5/S6; Gouda2023 Figures1-3 and supplementS1-S4 were visually inspected. Relevant Methods/tables and supplement primers were read. No raw-data replication or independent expert endorsement; later renderer and full-corpus checks are reported separately.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261023T092550Z-pf01923-c2s4-record-review
title: PF01923 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review
started_at: '2026-10-23T09:25:49Z'
finished_at: '2026-10-23T09:25:50Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Claude-Opus-4.6
  independence: self_review
  independence_basis: Cycle 2 Stage 4 frozen-inventory record review by Antigravity
    auditing prior Codex/Antigravity curation overlays, primary evidence caches, history
    events, and current projections at Git revision fde7d143a6b952fbc63b390cbfc27de38ac7701b.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: true
summary: Twenty-seven graphs retain77 OBSERVED effects:56 DIRECT biochemical/physical
  readouts and21 INDIRECT complementation/growth effects, across18 MECHANISTIC and9
  PHENOTYPIC contexts. All displayed quotations were checked against primary HTML
  and all evidence hashes/native graph fields validated. Status remains IN_PROGRESS;
  this is a same-agent partial scientific assessment, not an independent expert review
  or exhaustive family characterization. Stage 4 frozen-inventory audit identified
  an open protein-grounding gap (pf01923-sepduo-and-seeutt-assays-missing-protein-grounding)
  across three Salmonella enterica LT2 PduO/EutT biochemical causal graphs (sepduo-inhibition-2004,
  sepduo-metal-additions-2004, seeutt-metal-oxygen-2014) preserved for Stage 5 grouped
  remediation.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: fde7d143a6b952fbc63b390cbfc27de38ac7701b
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01923.yaml
    sha256: 340b31d2b19ecaf5a41364670d9bf88aa964c5b1d96e65d0e4daf552a782a06d
    role: context
  - path: data/families/PF01923.yaml
    sha256: 0ac3ef892888225a3ab063441867ae30c2072e29bb6018b71c784b723ac4908a
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
  - path: evidence/PF01923/costa-2018.txt
    sha256: b4a6fe709c16af5345a5fdb3e7ff0aad52b57029cb08992856c294d41eff54ff
    role: context
  - path: evidence/PF01923/coverage.txt
    sha256: 2d095c7f51f285358905cc011cb219307fe1a864c78f459199cd0b06125c8f06
    role: context
  - path: evidence/PF01923/gouda-2023.txt
    sha256: cbf3e47671a1f40f8c1ebfb7f6246f6d824a015b32d258864c8e84890d150bf3
    role: context
  - path: evidence/PF01923/identity.txt
    sha256: b38fae53a8e45cb8667cfb971fdcc660f533f23a04b1c784a7c3b6cf820b09e3
    role: context
  - path: evidence/PF01923/johnson-2001.txt
    sha256: d9b8342021f75f547d0659325e60c0041bee21f254e6c896fb518359f7ba10a5
    role: context
  - path: evidence/PF01923/johnson-2004.txt
    sha256: 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7
    role: context
  - path: evidence/PF01923/mera-2009.txt
    sha256: 8e210da8e829587bb250ad7b21ed9a09cffaff9f23eea34d48e9316fa3929ba5
    role: context
  - path: evidence/PF01923/mera-2010.txt
    sha256: 5d961468bf6c2c201f8f2d6910725189a1d947b02eee0b2761f586c545b6a482
    role: context
  - path: evidence/PF01923/moore-2014.txt
    sha256: ba545296384ec0ed7f90c7eb0c3ce04a7a3228355db1b5ea068b9a8c4abe6ed4
    role: context
  - path: evidence/PF01923/stmaurice-2007.txt
    sha256: dc1cf8546b6eaa853b460b85f1c327e5a03d15f5516b1af88ce833b9a546429b
    role: context
  - path: reviews/structured/20261012T015942Z-pf01923-pduo-eutt-mmab-assay-and-domain-contexts/review.yaml
    sha256: d847857fe37746df2847a64ae4c949a6324e4da31881375134db3df305d13605
    role: context
targets:
- target_id: PF01923
  path: data/families/PF01923.yaml
  label: PF01923
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01923.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: a19694240f589afe63fc516a15a8ef68030c6b5d550b1b8420c258d27fb373dd
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Ascending remaining frozen Pfam accession after PF01918. All8296 families
    and open context follow-ups remain in the corpus-wide goal.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01923
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Eight primary full-text studies plus Costa/Gouda publisher supplements
      support selected experiments, not every15667 frozen protein or every published
      context. MMAB product transfer/sequestration/repair/allostery, other EutT coordination
      and product studies, Lm2020 mutations, further species and exact historical
      constructs remain open. Moore2014 original supplement is inaccessible through
      attempted endpoints; described controls are text-only. StMaurice2008 is a structural/mapping
      lead, and Gouda2021 was inspected for purification only.
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
  - PF01923
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10507449/
  locator: Gouda2023 Figures1-3; publisher supplementMethodsS2-S6/FiguresS1-S4. Separate
    ledgers retain seven other primary studies.
  accessed_at: '2026-10-12T01:59:42Z'
  support: supports
  snapshot_sha256: cbf3e47671a1f40f8c1ebfb7f6246f6d824a015b32d258864c8e84890d150bf3
  summary: Recombinant human MMAB supports NADPH/FDXR/FDX1-dependent AdoCbl synthesis;
    four tested substitutions decrease the coupled activity. Separate ATP-EPR complexes
    and ADP-R190H redox titrations are not merged into a single observed reaction
    trajectory. Supplemental ADP methods qualify the conflicting ATP caption; exact
    MMAB construct endpoints remain open.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01923/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-12T01:59:42Z'
  support: supports
  snapshot_sha256: b38fae53a8e45cb8667cfb971fdcc660f533f23a04b1c784a7c3b6cf820b09e3
  summary: Frozen PF01923/Cob_adeno_trans/IPR016030/EX_DUF and historical DUF80 identity
    are unchanged. Q8ZNR5v1 maps3-166, Q9ZFV4v1 maps92-246, Q50EJ2v1 maps3-169, Q96EY8v1
    maps58-227, A0A0H3GFM5v1 maps83-242. Listeria10403S mapping is supported by strain-specific
    reference, primary alignment and terminal primers, not presumed EGD-e identity.
    SeEutT H67/C79/C80/C83 and LrPduO F187/tail183-188 lie outside PF01923. Modern
    reference mapping is distinguished from historical recombinant construct verification.
- evidence_id: johnson-2001
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC95042/
  locator: Methods, Results and exact figure/table locators in the retained per-study
    ledger
  summary: Primary experimental readouts, tested constructs, controls, conditional
    negatives and source discrepancies are retained without family-wide transfer.
  accessed_at: '2026-10-12T01:59:42Z'
  support: supports
  snapshot_sha256: d9b8342021f75f547d0659325e60c0041bee21f254e6c896fb518359f7ba10a5
- evidence_id: johnson-2004
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/
  locator: Methods, Results and exact figure/table locators in the retained per-study
    ledger
  summary: Primary experimental readouts, tested constructs, controls, conditional
    negatives and source discrepancies are retained without family-wide transfer.
  accessed_at: '2026-10-12T01:59:42Z'
  support: supports
  snapshot_sha256: 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7
- evidence_id: stmaurice-2007
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6574208/
  locator: Methods, Results and exact figure/table locators in the retained per-study
    ledger
  summary: Primary experimental readouts, tested constructs, controls, conditional
    negatives and source discrepancies are retained without family-wide transfer.
  accessed_at: '2026-10-12T01:59:42Z'
  support: supports
  snapshot_sha256: dc1cf8546b6eaa853b460b85f1c327e5a03d15f5516b1af88ce833b9a546429b
- evidence_id: mera-2009
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2666787/
  locator: Methods, Results and exact figure/table locators in the retained per-study
    ledger
  summary: Primary experimental readouts, tested constructs, controls, conditional
    negatives and source discrepancies are retained without family-wide transfer.
  accessed_at: '2026-10-12T01:59:42Z'
  support: supports
  snapshot_sha256: 8e210da8e829587bb250ad7b21ed9a09cffaff9f23eea34d48e9316fa3929ba5
- evidence_id: mera-2010
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2823439/
  locator: Methods, Results and exact figure/table locators in the retained per-study
    ledger
  summary: Primary experimental readouts, tested constructs, controls, conditional
    negatives and source discrepancies are retained without family-wide transfer.
  accessed_at: '2026-10-12T01:59:42Z'
  support: supports
  snapshot_sha256: 5d961468bf6c2c201f8f2d6910725189a1d947b02eee0b2761f586c545b6a482
- evidence_id: moore-2014
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3911174/
  locator: Methods, Results and exact figure/table locators in the retained per-study
    ledger
  summary: Primary experimental readouts, tested constructs, controls, conditional
    negatives and source discrepancies are retained without family-wide transfer.
  accessed_at: '2026-10-12T01:59:42Z'
  support: supports
  snapshot_sha256: ba545296384ec0ed7f90c7eb0c3ce04a7a3228355db1b5ea068b9a8c4abe6ed4
- evidence_id: costa-2018
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6113058/
  locator: Methods, Results and exact figure/table locators in the retained per-study
    ledger
  summary: Primary experimental readouts, tested constructs, controls, conditional
    negatives and source discrepancies are retained without family-wide transfer.
  accessed_at: '2026-10-12T01:59:42Z'
  support: supports
  snapshot_sha256: b4a6fe709c16af5345a5fdb3e7ff0aad52b57029cb08992856c294d41eff54ff
- evidence_id: coverage
  kind: search
  reference: evidence/PF01923/coverage.txt
  locator: Scoped source discovery, mapping and access ledger
  search_scope: PF01923/DUF80 and selected PduO/EutT/MMAB primary experiments; ignored/hidden-inclusive
    local inspection and documented unreviewed branches/access gaps.
  summary: Additional scientific contexts and exact construct/source uncertainties
    remain open; inaccessible sources are not negative experimental results.
  accessed_at: '2026-10-12T01:59:42Z'
  support: supports
  snapshot_sha256: 2d095c7f51f285358905cc011cb219307fe1a864c78f459199cd0b06125c8f06
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-12T01:59:42Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: stage4-prior-review
  kind: prior_review
  reference: reviews/structured/20261012T015942Z-pf01923-pduo-eutt-mmab-assay-and-domain-contexts/review.yaml
  locator: Predecessor structured review 20261012T015942Z-pf01923-pduo-eutt-mmab-assay-and-domain-contexts
  accessed_at: '2026-10-23T09:25:50Z'
  support: supports
  snapshot_sha256: d847857fe37746df2847a64ae4c949a6324e4da31881375134db3df305d13605
  summary: Predecessor review 20261012T015942Z-pf01923-pduo-eutt-mmab-assay-and-domain-contexts
    verified and linked for finding continuity and semantic-digest progression on
    PF01923.
- evidence_id: duf-projection-pf01923
  kind: record_content
  reference: data/families/PF01923.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-23T09:25:50Z'
  support: context_only
  snapshot_sha256: 0ac3ef892888225a3ab063441867ae30c2072e29bb6018b71c784b723ac4908a
  quote: "id: Pfam:PF01923\npfam_id: PF01923\nname: Cobalamin adenosyltransferase\n\
    short_name: Cob_adeno_trans\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01923\n\
    counters:\n  proteins: 15667\n  matches: 15721\n  proteomes: 13951\n  taxa: 21483\n\
    \  structures: 52\n  alphafold_models: 10554\n  domain_architectures: 37\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR016030\ndescription: Cobalamin adenosyltransferase This\
    \ family contains the gene products of PduO and EutT which\n  are both cobalamin\
    \ adenosyltransferases. PduO is a protein with ATP:cob(I)alamin adenosyltransferase\n\
    \  activity. The main role of this protein is the conversion of inactive cobalamins\
    \ to AdoCbl for 1,2-propanediol\n  degradation [[cite:PUB00013593]].The EutT enzyme\
    \ appears to be an adenosyl transferase, converting CNB12\n  to AdoB12 [[cite:PUB00009955]].\n\
    curation_history: history/records/PF01923\ndiscussions:\n- discussion_id: pf01923-domain-and-assay-boundaries\n\
    \  prompt: Resolve exact constructs and source discrepancies before extending\
    \ mechanistic attribution.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale:\
    \ Whole proteins, Pfam intervals, different reduction states and coupled versus\
    \ pre-reduced\n    assays support different claims.\n  evidence:\n  - reference:\
    \ PMID:24336938\n    supports: PARTIAL\n    evidence_source: primary_mutation_and_metal_assays\n\
    \    explanation: SeEutT metal-motif residues lie outside PF01923; assembly changes\
    \ and source inconsistencies\n      remain.\n  - reference: PMID:30071718\n  \
    \  supports: PARTIAL\n    evidence_source: primary_oxidation_state_and_growth_controls\n\
    \    explanation: LmEutT accepts cob(I)inamide but not cob(II)inamide in the tested\
    \ biological reducing\n      systems; transition-metal independence does not exclude\
    \ MgATP.\n  - reference: PMID:37526260\n    supports: PARTIAL\n    evidence_source:\
    \ primary_text_and_publisher_supplement\n    explanation: ADP redox Methods conflict\
    \ with the ATP figure caption; donor truncations and exact MMAB\n      construct\
    \ assignment matter.\n  posed_by: Codex\n  posed_date: '2026-10-12'\n  notes:\
    \ PF01923 is former DUF80, currently Cob_adeno_trans/IPR016030. Separate PduO,\
    \ EutT and MMAB experimental\n    systems must not be joined into one observed\
    \ chain. The active SePduO1-185 construct includes flanking\n    sequence; SeEutT\
    \ H67/C79/C80/C83 and LrPduO F187/tail183-188 fall outside their PF01923 matches.\
    \ Historical\n    tags and clone endpoints remain qualified. No-added-metal SePduO\
    \ retains activity; Zn-loaded SeEutT\n    resists the oxidation that disables\
    \ Fe-loaded protein; LmEutT has no demonstrated transition-metal\n    requirement\
    \ but still uses MgATP. LmEutT accepts cob(I)inamide but not cob(II)inamide with\
    \ the tested\n    biological reducing systems. Human MMAB ADP supports bound product\
    \ in FigureS1 without sustained release;\n    AMP spectra cannot distinguish absent\
    \ binding from unchanged coordination. These negatives do not\n    generalize\
    \ across all members. Retain Johnson2001 dose-unit conflicts; Johnson2004 1-193/1-293\
    \ label\n    and PPPi percentage discrepancy; Mera2009 reduction versus adenosylation-lag\
    \ wording; Moore2014 C83A\n    zinc, extinction units, reconstitution ratio and\
    \ arabinose concentration conflicts; Costa2018 supplement\n    numbering and catalytic-efficiency\
    \ arithmetic; Gouda2023 ATP-caption versus ADP-methods discrepancy.\n    No silent\
    \ source corrections. Gouda2023 ADP single-turnover spectra are retained in the\
    \ ledger; the\n    specific panel's reductant details require further verification\
    \ before a graph is added.\n- discussion_id: pf01923-remaining-causal-contexts\n\
    \  prompt: Extend uncurated member-specific pathways and inspect remaining primary\
    \ mechanistic studies.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: The\
    \ selected PduO/EutT/MMAB assays do not characterize all15667 frozen proteins\
    \ or complete\n    their catalytic and chaperone cycles.\n  evidence:\n  - reference:\
    \ PMID:19236001\n    supports: PARTIAL\n    evidence_source: primary_structures_and_kinetics\n\
    \    explanation: F112 effects do not directly resolve product-release chemistry;\
    \ outside-domain tail substitutions\n      and data-not-shown complementation\
    \ are qualified.\n  - reference: PMID:34757128\n    supports: PARTIAL\n    evidence_source:\
    \ purification_methods_only\n    explanation: 2021 human MMAB paper was inspected\
    \ for cited construct preparation, not fully reviewed\n      for its catalytic/chaperone\
    \ claims.\n  posed_by: Codex\n  posed_date: '2026-10-12'\n  notes: 'The current\
    \ graphs retain measured assay effects, not a complete atomic catalytic cycle,\
    \ native\n    exclusive electron-donor network or clinical mechanism. MMAB product\
    \ transfer/sequestration/repair,\n    exact assay constructs, EutT spectroscopy/product\
    \ variants, other primary mutant studies and unexamined\n    family members remain\
    \ follow-up work. Source and access ledger: evidence/PF01923/coverage.txt. No\n\
    \    unexamined branch is declared causally empty. Same-agent scientific curation\
    \ is partial and remains\n    IN_PROGRESS. Native validation establishes schema/evidence\
    \ integrity, not independent expert endorsement,\n    full-family experimental\
    \ proof, website publication or whole-corpus completion.'\ncausal_graphs:\n- graph_id:\
    \ sepduo-product-2001\n  title: Salmonella PduO supports AdoCbl formation\n  scope:\
    \ Johnson2001 inclusion-body-enriched recombinant PduO from the LT2 gene.\n  context:\
    \ Anoxic37C; Tris200mM pH8, ATP0.4mM, MgCl2 2.8mM, phosphate1.6mM, HOCbl50uM and\
    \ Ti(III)citrate1mM.\n    Reductant supplies cob(I)alamin before enzymatic transfer.\n\
    \  family_mapping: SeLT2 STM2050 PduO Q8ZNR5 sequence v1, 336 aa; PF01923 3-166\
    \ and separate PF03928 201-328.\n    Tested full-length protein unless a construct\
    \ is named. Current reference mapping, not independent\n    historical clone resequencing.\n\
    \  scope_status: MECHANISTIC\n  taxon: NCBITaxon:99287\n  limitations: This is\
    \ joint-input biochemical activity, not direct reduction of cyanocobalamin by\
    \ PduO\n    or isolated-domain sufficiency. Partially purified preparation; empty-vector\
    \ and omission controls\n    are retained.\n  nodes:\n  - node_id: reaction\n\
    \    label: PduO with ATP, reduced cob(I)alamin and assay buffer\n    node_type:\
    \ ACTIVITY\n    grounding:\n    - UniProtKB:Q8ZNR5\n  - node_id: product\n   \
    \ label: AdoCbl product\n    node_type: STATE\n  edges:\n  - edge_id: reaction-produces-product\n\
    \    subject: reaction\n    predicate: produces\n    object: product\n    mechanism:\
    \ Adding the PduO preparation yields the product spectrum; photolysis and ATP/substrate/reductant/enzyme\n\
    \      omission controls support adenosyltransferase activity.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:11160088\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC95042/\n\
    \      snippet: encodes a protein with ATP:cob(I)alamin adenosyltransferase activity.\n\
    \      explanation: Figure5 and enzyme-assay Results/Methods; photolysis occurs\
    \ in the presence of Ti(III),\n        not the later EutT assay.\n      cache_path:\
    \ evidence/PF01923/johnson-2001.txt\n      cache_sha256: d9b8342021f75f547d0659325e60c0041bee21f254e6c896fb518359f7ba10a5\n\
    - graph_id: sepduo-growth-2001\n  title: PduO genotype alters propanediol growth\n\
    \  scope: Johnson2001 LT2 whole-gene perturbations and pDP1 complementation.\n\
    \  context: NCE0.4% 1,2-propanediol with cyanocobalamin,37C, OD600; plasmids induced\
    \ with0.02mM IPTG. delta-pduO651\n    removes nt19-981; cobA366::Tn10dCam is distinct.\n\
    \  family_mapping: SeLT2 STM2050 PduO Q8ZNR5 sequence v1, 336 aa; PF01923 3-166\
    \ and separate PF03928 201-328.\n    Tested full-length protein unless a construct\
    \ is named. Current reference mapping, not independent\n    historical clone resequencing.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:99287\n  limitations: Growth is\
    \ INDIRECT. The cobA single mutant resembles WT under these conditions; no claim\n\
    \    that PduO is the only ACAT or that the double mutant lacks every ACAT. Vector\
    \ does not rescue.\n  nodes:\n  - node_id: pduo\n    label: delta-pduO651 in the\
    \ cobA-positive host\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q8ZNR5\n\
    \  - node_id: double\n    label: Combined pduO/cobA lesions\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q8ZNR5\n  - node_id: rescue\n    label: pDP1\
    \ expressing PduO in the double mutant\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q8ZNR5\n  - node_id: overexpression\n    label: pDP1 expressing\
    \ PduO in WT\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q8ZNR5\n\
    \  - node_id: growth\n    label: Growth on 1,2-propanediol\n    node_type: PHENOTYPE\n\
    \  edges:\n  - edge_id: pduo-decreases-growth\n    subject: pduo\n    predicate:\
    \ decreases\n    object: growth\n    mechanism: Generation time rises from about8.4h\
    \ WT to12.2h.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:11160088\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC95042/\n      snippet: optimal growth\
    \ of S. enterica on 1,2-propanediol required a functional pduO gene.\n      explanation:\
    \ Figure2, matched strain growth curves.\n      cache_path: evidence/PF01923/johnson-2001.txt\n\
    \      cache_sha256: d9b8342021f75f547d0659325e60c0041bee21f254e6c896fb518359f7ba10a5\n\
    \  - edge_id: double-decreases-growth\n    subject: double\n    predicate: decreases\n\
    \    object: growth\n    mechanism: The double mutant fails to grow in this medium,\
    \ unlike either single-mutant comparison.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:11160088\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC95042/\n      snippet:\
    \ optimal growth of S. enterica on 1,2-propanediol required a functional pduO\
    \ gene.\n      explanation: Figure2 and Table1 strain genotypes.\n      cache_path:\
    \ evidence/PF01923/johnson-2001.txt\n      cache_sha256: d9b8342021f75f547d0659325e60c0041bee21f254e6c896fb518359f7ba10a5\n\
    \  - edge_id: rescue-increases-growth\n    subject: rescue\n    predicate: increases\n\
    \    object: growth\n    mechanism: pDP1 restores growth, with reported generation\
    \ time about5.8h.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:11160088\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC95042/\n      snippet: optimal growth\
    \ of S. enterica on 1,2-propanediol required a functional pduO gene.\n      explanation:\
    \ Figure2, BE114 complementation and vector-control Results.\n      cache_path:\
    \ evidence/PF01923/johnson-2001.txt\n      cache_sha256: d9b8342021f75f547d0659325e60c0041bee21f254e6c896fb518359f7ba10a5\n\
    \  - edge_id: overexpression-increases-growth\n    subject: overexpression\n \
    \   predicate: increases\n    object: growth\n    mechanism: pDP1 accelerates\
    \ growth of the WT background in the same experiment.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:11160088\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC95042/\n\
    \      snippet: optimal growth of S. enterica on 1,2-propanediol required a functional\
    \ pduO gene.\n      explanation: Figure2, BE122 versus WT.\n      cache_path:\
    \ evidence/PF01923/johnson-2001.txt\n      cache_sha256: d9b8342021f75f547d0659325e60c0041bee21f254e6c896fb518359f7ba10a5\n\
    - graph_id: sepduo-cofactor-bypass-2001\n  title: Supplied AdoCbl partially bypasses\
    \ the double-mutant defect\n  scope: Johnson2001 external-cofactor bypass in the\
    \ pduO/cobA double mutant.\n  context: Figure3 minimal1,2-propanediol medium;\
    \ cyanocobalamin and AdoCbl supplements compared.\n  family_mapping: SeLT2 STM2050\
    \ PduO Q8ZNR5 sequence v1, 336 aa; PF01923 3-166 and separate PF03928 201-328.\n\
    \    Tested full-length protein unless a construct is named. Current reference\
    \ mapping, not independent\n    historical clone resequencing.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:99287\n  limitations: Dose units conflict between\
    \ prose and caption (uM versus ug/mL, with one g/mL entry). No\n    exact dose-response\
    \ conversion or full rescue claim. Intracellular accumulation explanations remain\n\
    \    hypotheses.\n  nodes:\n  - node_id: adocbl\n    label: Supply AdoCbl to the\
    \ pduO/cobA double mutant\n    node_type: PERTURBATION\n  - node_id: growth\n\
    \    label: Growth on 1,2-propanediol\n    node_type: PHENOTYPE\n  edges:\n  -\
    \ edge_id: adocbl-increases-growth\n    subject: adocbl\n    predicate: increases\n\
    \    object: growth\n    mechanism: AdoCbl permits slow growth where cyanocobalamin\
    \ does not; reported generation time23h versus\n      WT8.5h.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:11160088\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC95042/\n\
    \      snippet: optimal growth of S. enterica on 1,2-propanediol required a functional\
    \ pduO gene.\n      explanation: Figure3 and accompanying bypass Results.\n  \
    \    cache_path: evidence/PF01923/johnson-2001.txt\n      cache_sha256: d9b8342021f75f547d0659325e60c0041bee21f254e6c896fb518359f7ba10a5\n\
    - graph_id: sepduo-truncation-activity-2004\n  title: N-terminal PduO constructs\
    \ retain transferase activity\n  scope: Johnson2004 untagged purified full-length\
    \ and1-90/1-185/1-230/1-293 constructs.\n  context: Table2; anoxic37C Tris200mM\
    \ pH8, KCl5mM, MgCl2 2.5mM, ATP0.5mM, HOCbl50uM, Ti(III)citrate1mM.\n  family_mapping:\
    \ SeLT2 STM2050 PduO Q8ZNR5 sequence v1, 336 aa; PF01923 3-166 and separate PF03928\
    \ 201-328.\n    Tested full-length protein unless a construct is named. Current\
    \ reference mapping, not independent\n    historical clone resequencing.\n  scope_status:\
    \ MECHANISTIC\n  taxon: NCBITaxon:99287\n  limitations: The shortest active1-185\
    \ construct extends beyond PF01923 3-166. Inactive1-90 is not proof\n    that\
    \ every missing residue is catalytic. One prose1-193 label conflicts with1-293\
    \ in construct/table/primer\n    descriptions.\n  nodes:\n  - node_id: c185\n\
    \    label: PduO1-185 with ATP and reduced substrate\n    node_type: ACTIVITY\n\
    \    grounding:\n    - UniProtKB:Q8ZNR5\n  - node_id: c230\n    label: PduO1-230\
    \ with ATP and reduced substrate\n    node_type: ACTIVITY\n    grounding:\n  \
    \  - UniProtKB:Q8ZNR5\n  - node_id: c293\n    label: PduO1-293 with ATP and reduced\
    \ substrate\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:Q8ZNR5\n\
    \  - node_id: c90\n    label: Replace full PduO with1-90\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q8ZNR5\n  - node_id: product\n    label: AdoCbl\
    \ formation\n    node_type: STATE\n  edges:\n  - edge_id: c185-produces-product\n\
    \    subject: c185\n    predicate: produces\n    object: product\n    mechanism:\
    \ Reported specific activity433nmol/min/mg, compared with full-length262; different\
    \ molecular\n      masses prevent equating this to the same change in kcat.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:15547259\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n\
    \      snippet: associated with its N-terminal domain.\n      explanation: Table2;\
    \ Figure2 construct sizes; standard biochemical assay.\n      cache_path: evidence/PF01923/johnson-2004.txt\n\
    \      cache_sha256: 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n\
    \  - edge_id: c230-produces-product\n    subject: c230\n    predicate: produces\n\
    \    object: product\n    mechanism: Reported specific activity366nmol/min/mg,\
    \ compared with full-length262; different molecular\n      masses prevent equating\
    \ this to the same change in kcat.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:15547259\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n      snippet:\
    \ associated with its N-terminal domain.\n      explanation: Table2; Figure2 construct\
    \ sizes; standard biochemical assay.\n      cache_path: evidence/PF01923/johnson-2004.txt\n\
    \      cache_sha256: 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n\
    \  - edge_id: c293-produces-product\n    subject: c293\n    predicate: produces\n\
    \    object: product\n    mechanism: Reported specific activity284nmol/min/mg,\
    \ compared with full-length262; different molecular\n      masses prevent equating\
    \ this to the same change in kcat.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:15547259\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n      snippet:\
    \ associated with its N-terminal domain.\n      explanation: Table2; Figure2 construct\
    \ sizes; standard biochemical assay.\n      cache_path: evidence/PF01923/johnson-2004.txt\n\
    \      cache_sha256: 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n\
    \  - edge_id: c90-decreases-product\n    subject: c90\n    predicate: decreases\n\
    \    object: product\n    mechanism: Activity is not detected for1-90 under the\
    \ assay used for active longer constructs.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:15547259\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n      snippet:\
    \ associated with its N-terminal domain.\n      explanation: Table2 negative construct\
    \ result.\n      cache_path: evidence/PF01923/johnson-2004.txt\n      cache_sha256:\
    \ 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n- graph_id:\
    \ sepduo-triphosphate-2004\n  title: PduO reaction releases triphosphate\n  scope:\
    \ Johnson2004 full-length purified PduO reaction product analysis.\n  context:\
    \ 31P NMR after2h37C, ATP/HOCbl2mM, Ti(III)citrate5mM; EDTA added for analysis.\n\
    \  family_mapping: SeLT2 STM2050 PduO Q8ZNR5 sequence v1, 336 aa; PF01923 3-166\
    \ and separate PF03928 201-328.\n    Tested full-length protein unless a construct\
    \ is named. Current reference mapping, not independent\n    historical clone resequencing.\n\
    \  scope_status: MECHANISTIC\n  taxon: NCBITaxon:99287\n  limitations: NMR identifies\
    \ a phosphate product, not an observed atomic reaction trajectory or whether\n\
    \    substrate binding is ordered.\n  nodes:\n  - node_id: reaction\n    label:\
    \ PduO, ATP and chemically reduced corrinoid reaction\n    node_type: ACTIVITY\n\
    \    grounding:\n    - UniProtKB:Q8ZNR5\n  - node_id: pppi\n    label: Triphosphate\
    \ reaction product\n    node_type: STATE\n  edges:\n  - edge_id: reaction-produces-pppi\n\
    \    subject: reaction\n    predicate: produces\n    object: pppi\n    mechanism:\
    \ The product phosphorus spectrum matches the triphosphate standard rather than\
    \ pyrophosphate.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:15547259\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n      snippet: triphosphate\
    \ was a product\n      explanation: Figure3 and phosphorus-NMR Methods.\n    \
    \  cache_path: evidence/PF01923/johnson-2004.txt\n      cache_sha256: 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n\
    - graph_id: sepduo-inhibition-2004\n  title: ADP and phosphate products inhibit\
    \ PduO in vitro\n  scope: Johnson2004 additions to the full-length PduO enzyme\
    \ assay.\n  context: ADP100uM with ATP50uM; separate PPi/PPPi4mM additions. Matched\
    \ no-addition assays are comparators.\n  family_mapping: SeLT2 STM2050 PduO Q8ZNR5\
    \ sequence v1, 336 aa; PF01923 3-166 and separate PF03928 201-328.\n    Tested\
    \ full-length protein unless a construct is named. Current reference mapping,\
    \ not independent\n    historical clone resequencing.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:99287\n  limitations: ADP inhibition is condition-specific,\
    \ not proven cellular feedback. Pi has no comparable\n    effect. Reported PPPi71%\
    \ and165/222 rates disagree numerically; retain only partial inhibition.\n  nodes:\n\
    \  - node_id: adp\n    label: Add100uM ADP at50uM ATP\n    node_type: PERTURBATION\n\
    \  - node_id: ppi\n    label: Add4mM pyrophosphate\n    node_type: PERTURBATION\n\
    \  - node_id: pppi\n    label: Add4mM triphosphate\n    node_type: PERTURBATION\n\
    \  - node_id: activity\n    label: AdoCbl-forming activity\n    node_type: STATE\n\
    \  edges:\n  - edge_id: adp-decreases-activity\n    subject: adp\n    predicate:\
    \ decreases\n    object: activity\n    mechanism: About10% activity remains; reported\
    \ Ki4.9uM derives from experiments not plotted.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:15547259\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n      snippet:\
    \ only 10% activity remained\n      explanation: Figure4 and nucleotide-inhibition\
    \ Results.\n      cache_path: evidence/PF01923/johnson-2004.txt\n      cache_sha256:\
    \ 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n  - edge_id:\
    \ ppi-decreases-activity\n    subject: ppi\n    predicate: decreases\n    object:\
    \ activity\n    mechanism: Activity falls to29% of the no-addition control.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:15547259\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n\
    \      snippet: pyrophosphate or triphosphate\n      explanation: 'Results: phosphate\
    \ and pyrophosphate additions.'\n      cache_path: evidence/PF01923/johnson-2004.txt\n\
    \      cache_sha256: 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n\
    \  - edge_id: pppi-decreases-activity\n    subject: pppi\n    predicate: decreases\n\
    \    object: activity\n    mechanism: Triphosphate partially inhibits activity;\
    \ exact percentage remains qualified by inconsistent\n      reported numbers.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:15547259\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n\
    \      snippet: pyrophosphate or triphosphate\n      explanation: 'Results: phosphate-product\
    \ inhibition.'\n      cache_path: evidence/PF01923/johnson-2004.txt\n      cache_sha256:\
    \ 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n- graph_id:\
    \ sepduo-metal-additions-2004\n  title: Divalent metals change PduO assay activity\n\
    \  scope: Johnson2004 full-length PduO with added divalent salts.\n  context:\
    \ Standard biochemical assay except Mg is omitted or replaced with a2.5mM test\
    \ metal; compare\n    no-added-metal rate91nmol/min/mg.\n  family_mapping: SeLT2\
    \ STM2050 PduO Q8ZNR5 sequence v1, 336 aa; PF01923 3-166 and separate PF03928\
    \ 201-328.\n    Tested full-length protein unless a construct is named. Current\
    \ reference mapping, not independent\n    historical clone resequencing.\n  scope_status:\
    \ MECHANISTIC\n  taxon: NCBITaxon:99287\n  limitations: No-added-metal preparation\
    \ retains32% of Mg-supported activity; this does not prove metal-free\n    protein.\
    \ Ca has little effect. High-concentration inhibition does not establish physiological\
    \ toxicity\n    or exact metal binding.\n  nodes:\n  - node_id: mg\n    label:\
    \ Add2.5mM Mg(II)\n    node_type: PERTURBATION\n  - node_id: mn\n    label: Add2.5mM\
    \ Mn(II)\n    node_type: PERTURBATION\n  - node_id: co\n    label: Add2.5mM Co(II)\n\
    \    node_type: PERTURBATION\n  - node_id: cd\n    label: Add2.5mM Cd(II)\n  \
    \  node_type: PERTURBATION\n  - node_id: zn\n    label: Add2.5mM Zn(II)\n    node_type:\
    \ PERTURBATION\n  - node_id: ni\n    label: Add2.5mM Ni(II)\n    node_type: PERTURBATION\n\
    \  - node_id: cu\n    label: Add2.5mM Cu(II)\n    node_type: PERTURBATION\n  -\
    \ node_id: activity\n    label: AdoCbl-forming activity\n    node_type: STATE\n\
    \  edges:\n  - edge_id: mg-increases-activity\n    subject: mg\n    predicate:\
    \ increases\n    object: activity\n    mechanism: Reported rate285nmol/min/mg\
    \ versus91 without added divalent metal.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:15547259\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n      snippet:\
    \ highest activities\n      explanation: Divalent-metal Results; matched metal-replacement\
    \ assays.\n      cache_path: evidence/PF01923/johnson-2004.txt\n      cache_sha256:\
    \ 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n  - edge_id:\
    \ mn-increases-activity\n    subject: mn\n    predicate: increases\n    object:\
    \ activity\n    mechanism: Reported rate277nmol/min/mg versus91 without added\
    \ divalent metal.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:15547259\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n      snippet: highest activities\n\
    \      explanation: Divalent-metal Results; matched metal-replacement assays.\n\
    \      cache_path: evidence/PF01923/johnson-2004.txt\n      cache_sha256: 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n\
    \  - edge_id: co-increases-activity\n    subject: co\n    predicate: increases\n\
    \    object: activity\n    mechanism: Reported rate266nmol/min/mg versus91 without\
    \ added divalent metal.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:15547259\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n      snippet: highest activities\n\
    \      explanation: Divalent-metal Results; matched metal-replacement assays.\n\
    \      cache_path: evidence/PF01923/johnson-2004.txt\n      cache_sha256: 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n\
    \  - edge_id: cd-decreases-activity\n    subject: cd\n    predicate: decreases\n\
    \    object: activity\n    mechanism: The added metal reduces activity below detection\
    \ under these assay conditions.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:15547259\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n      snippet:\
    \ abolished measurable activity\n      explanation: Divalent-metal Results; activity\
    \ not detected.\n      cache_path: evidence/PF01923/johnson-2004.txt\n      cache_sha256:\
    \ 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n  - edge_id:\
    \ zn-decreases-activity\n    subject: zn\n    predicate: decreases\n    object:\
    \ activity\n    mechanism: The added metal reduces activity below detection under\
    \ these assay conditions.\n    directness: DIRECT\n    support: OBSERVED\n   \
    \ evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:15547259\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n      snippet:\
    \ abolished measurable activity\n      explanation: Divalent-metal Results; activity\
    \ not detected.\n      cache_path: evidence/PF01923/johnson-2004.txt\n      cache_sha256:\
    \ 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n  - edge_id:\
    \ ni-decreases-activity\n    subject: ni\n    predicate: decreases\n    object:\
    \ activity\n    mechanism: The added metal reduces activity below detection under\
    \ these assay conditions.\n    directness: DIRECT\n    support: OBSERVED\n   \
    \ evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:15547259\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n      snippet:\
    \ abolished measurable activity\n      explanation: Divalent-metal Results; activity\
    \ not detected.\n      cache_path: evidence/PF01923/johnson-2004.txt\n      cache_sha256:\
    \ 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n  - edge_id:\
    \ cu-decreases-activity\n    subject: cu\n    predicate: decreases\n    object:\
    \ activity\n    mechanism: The added metal reduces activity below detection under\
    \ these assay conditions.\n    directness: DIRECT\n    support: OBSERVED\n   \
    \ evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:15547259\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n      snippet:\
    \ abolished measurable activity\n      explanation: Divalent-metal Results; activity\
    \ not detected.\n      cache_path: evidence/PF01923/johnson-2004.txt\n      cache_sha256:\
    \ 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n- graph_id:\
    \ sepduo-truncation-complementation-2004\n  title: Longer N-terminal constructs\
    \ restore degradation\n  scope: Johnson2004 BE121 cobA/pduO double mutant with\
    \ pLAC22 constructs.\n  context: Reported1,2-propanediol degradation complementation\
    \ by1-185/1-230/1-293 compared with1-90.\n  family_mapping: SeLT2 STM2050 PduO\
    \ Q8ZNR5 sequence v1, 336 aa; PF01923 3-166 and separate PF03928 201-328.\n  \
    \  Tested full-length protein unless a construct is named. Current reference mapping,\
    \ not independent\n    historical clone resequencing.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:99287\n  limitations: Phenotypic results are reported in text\
    \ without a plotted growth series. Do not assign\n    numerical growth rescue,\
    \ intracellular AdoCbl levels or isolated3-166 sufficiency.\n  nodes:\n  - node_id:\
    \ c185\n    label: Express PduO1-185 in BE121\n    node_type: PERTURBATION\n \
    \   grounding:\n    - UniProtKB:Q8ZNR5\n  - node_id: c230\n    label: Express\
    \ PduO1-230 in BE121\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q8ZNR5\n\
    \  - node_id: c293\n    label: Express PduO1-293 in BE121\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q8ZNR5\n  - node_id: degradation\n    label:\
    \ 1,2-propanediol degradation phenotype\n    node_type: PHENOTYPE\n  edges:\n\
    \  - edge_id: c185-increases-degradation\n    subject: c185\n    predicate: increases\n\
    \    object: degradation\n    mechanism: The construct restores the degradation\
    \ phenotype;1-90 fails in the reported comparison.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:15547259\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n\
    \      snippet: associated with its N-terminal domain.\n      explanation: Truncated-protein\
    \ complementation Results; no displayed quantitative growth data.\n      cache_path:\
    \ evidence/PF01923/johnson-2004.txt\n      cache_sha256: 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n\
    \  - edge_id: c230-increases-degradation\n    subject: c230\n    predicate: increases\n\
    \    object: degradation\n    mechanism: The construct restores the degradation\
    \ phenotype;1-90 fails in the reported comparison.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:15547259\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n\
    \      snippet: associated with its N-terminal domain.\n      explanation: Truncated-protein\
    \ complementation Results; no displayed quantitative growth data.\n      cache_path:\
    \ evidence/PF01923/johnson-2004.txt\n      cache_sha256: 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n\
    \  - edge_id: c293-increases-degradation\n    subject: c293\n    predicate: increases\n\
    \    object: degradation\n    mechanism: The construct restores the degradation\
    \ phenotype;1-90 fails in the reported comparison.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:15547259\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC529089/\n\
    \      snippet: associated with its N-terminal domain.\n      explanation: Truncated-protein\
    \ complementation Results; no displayed quantitative growth data.\n      cache_path:\
    \ evidence/PF01923/johnson-2004.txt\n      cache_sha256: 7b06b92e2b8c68157e60eddd1c39aad86cc667758c588d712ddccb635c6defb7\n\
    - graph_id: lrpduo-complementation-2007\n  title: LrPduO supports heterologous\
    \ cofactor-dependent growth\n  scope: StMaurice2007 LrPduO expressed in a Salmonella\
    \ LT2 metE/cobA host.\n  context: metE205 ara-9 cobA366::Tn10dCat; NCE22mM glycerol,0.2uM\
    \ dicyanocobinamide,37C; OD650.\n  family_mapping: L. reuteri CRL1098 LrPduO from\
    \ AY780645/AAX14514.1; current Q50EJ2 sequence v1 (gene\n    label cobA), 188\
    \ aa, PF01923 3-169. PDB3CI1 maps reference2-188 to entity8-194 with a nonidentical\n\
    \    N terminus. F112/F163 are inside PF01923; F187 and tail183-188 are outside.\
    \ TEV-cleaved preparation\n    is not an isolated domain.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:99287\n  limitations: Figure caption calls cobA a deletion\
    \ but the strain table records an insertion. This is\n    heterologous growth,\
    \ not native LrPduO necessity or direct cellular cofactor quantification.\n  nodes:\n\
    \  - node_id: plasmid\n    label: Express LrPduO in the Salmonella test host\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q50EJ2\n  - node_id:\
    \ growth\n    label: Cofactor-dependent growth\n    node_type: PHENOTYPE\n  edges:\n\
    \  - edge_id: plasmid-increases-growth\n    subject: plasmid\n    predicate: increases\n\
    \    object: growth\n    mechanism: Growth rate0.105+/-0.009 OD/h versus vector0.001;\
    \ Salmonella CobA positive control0.11+/-0.006.\n    directness: INDIRECT\n  \
    \  support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:17121823\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6574208/\n\
    \      snippet: demanded adenosylation of the precursor cobinamide prior to its\
    \ conversion to AdoCbl.\n      explanation: Original Figure1, Methods and strain\
    \ table.\n      cache_path: evidence/PF01923/stmaurice-2007.txt\n      cache_sha256:\
    \ dc1cf8546b6eaa853b460b85f1c327e5a03d15f5516b1af88ce833b9a546429b\n- graph_id:\
    \ lrpduo-variant-coordination-2009\n  title: Variant complexes contain different\
    \ cobalt ligands\n  scope: Mera2009 crystallized LrPduO F112A and F112H complexes.\n\
    \  context: Anoxic ATP/corrinoid crystallization with reduced-flavin system; F112A\
    \ and F112H use different\n    crystallization buffers. Ligand assignments compared\
    \ with WT structure.\n  family_mapping: L. reuteri CRL1098 LrPduO from AY780645/AAX14514.1;\
    \ current Q50EJ2 sequence v1 (gene\n    label cobA), 188 aa, PF01923 3-169. PDB3CI1\
    \ maps reference2-188 to entity8-194 with a nonidentical\n    N terminus. F112/F163\
    \ are inside PF01923; F187 and tail183-188 are outside. TEV-cleaved preparation\n\
    \    is not an isolated domain.\n  scope_status: MECHANISTIC\n  limitations: These\
    \ are observed prepared-complex structures, not a time-resolved displacement movie\n\
    \    or a fully controlled single-variable crystallization comparison.\n  nodes:\n\
    \  - node_id: f112a\n    label: Crystallize F112A with ATP and cob(II)alamin\n\
    \    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:Q50EJ2\n  - node_id:\
    \ f112h\n    label: Crystallize F112H with ATP and cob(II)alamin\n    node_type:\
    \ ACTIVITY\n    grounding:\n    - UniProtKB:Q50EJ2\n  - node_id: dmb\n    label:\
    \ Five-coordinate DMB-on corrinoid complex\n    node_type: STATE\n    grounding:\n\
    \    - UniProtKB:Q50EJ2\n  - node_id: his\n    label: Five-coordinate His-on corrinoid\
    \ complex\n    node_type: STATE\n    grounding:\n    - UniProtKB:Q50EJ2\n  edges:\n\
    \  - edge_id: f112a-produces-dmb\n    subject: f112a\n    predicate: produces\n\
    \    object: dmb\n    mechanism: The variant complex retains DMB as the fifth\
    \ ligand, unlike the four-coordinate WT comparison.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:19236001\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2666787/\n\
    \      snippet: a five-coordinate species\n      explanation: Figure1 and structural\
    \ Results; X-ray ligand assignment.\n      cache_path: evidence/PF01923/mera-2009.txt\n\
    \      cache_sha256: 8e210da8e829587bb250ad7b21ed9a09cffaff9f23eea34d48e9316fa3929ba5\n\
    \  - edge_id: f112h-produces-his\n    subject: f112h\n    predicate: produces\n\
    \    object: his\n    mechanism: The complex uses His112 as the fifth ligand with\
    \ DMB displaced.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:19236001\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC2666787/\n      snippet: a five-coordinate\
    \ species\n      explanation: Figure2 and structural Results.\n      cache_path:\
    \ evidence/PF01923/mera-2009.txt\n      cache_sha256: 8e210da8e829587bb250ad7b21ed9a09cffaff9f23eea34d48e9316fa3929ba5\n\
    - graph_id: lrpduo-cobi-kinetics-2009\n  title: F112 substitutions lower activity\
    \ with pre-reduced substrate\n  scope: Mera2009 LrPduO substitutions tested in\
    \ the cob(I)alamin assay.\n  context: Ti(III)citrate supplies cob(I)alamin; anoxic37C;\
    \ Table3 substrate-varied kinetic fits.\n  family_mapping: L. reuteri CRL1098\
    \ LrPduO from AY780645/AAX14514.1; current Q50EJ2 sequence v1 (gene\n    label\
    \ cobA), 188 aa, PF01923 3-169. PDB3CI1 maps reference2-188 to entity8-194 with\
    \ a nonidentical\n    N terminus. F112/F163 are inside PF01923; F187 and tail183-188\
    \ are outside. TEV-cleaved preparation\n    is not an isolated domain.\n  scope_status:\
    \ MECHANISTIC\n  limitations: These kcat changes are not the same experiment as\
    \ the Fpr/FldA reduction-coupled assay.\n    Residual activity is retained; mutation\
    \ effects do not uniquely identify product release.\n  nodes:\n  - node_id: f112a\n\
    \    label: F112A substitution in LrPduO\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q50EJ2\n  - node_id: f112h\n    label: F112H substitution in\
    \ LrPduO\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q50EJ2\n\
    \  - node_id: f112y\n    label: F112Y substitution in LrPduO\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q50EJ2\n  - node_id: f112w\n    label: F112W\
    \ substitution in LrPduO\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q50EJ2\n\
    \  - node_id: turnover\n    label: Cob(I)alamin-dependent turnover\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: f112a-decreases-turnover\n    subject: f112a\n\
    \    predicate: decreases\n    object: turnover\n    mechanism: kcat0.0066/s versus\
    \ WT0.024/s under substrate variation.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:19236001\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2666787/\n      snippet:\
    \ was catalytically competent\n      explanation: Table3, Co(I) assay Methods;\
    \ comparison within the same assay.\n      cache_path: evidence/PF01923/mera-2009.txt\n\
    \      cache_sha256: 8e210da8e829587bb250ad7b21ed9a09cffaff9f23eea34d48e9316fa3929ba5\n\
    \  - edge_id: f112h-decreases-turnover\n    subject: f112h\n    predicate: decreases\n\
    \    object: turnover\n    mechanism: kcat0.00042/s versus WT0.024/s under substrate\
    \ variation.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:19236001\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC2666787/\n      snippet: was catalytically\
    \ competent\n      explanation: Table3, Co(I) assay Methods; comparison within\
    \ the same assay.\n      cache_path: evidence/PF01923/mera-2009.txt\n      cache_sha256:\
    \ 8e210da8e829587bb250ad7b21ed9a09cffaff9f23eea34d48e9316fa3929ba5\n  - edge_id:\
    \ f112y-decreases-turnover\n    subject: f112y\n    predicate: decreases\n   \
    \ object: turnover\n    mechanism: kcat0.0017/s versus WT0.024/s under substrate\
    \ variation.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:19236001\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC2666787/\n      snippet: was catalytically\
    \ competent\n      explanation: Table3, Co(I) assay Methods; comparison within\
    \ the same assay.\n      cache_path: evidence/PF01923/mera-2009.txt\n      cache_sha256:\
    \ 8e210da8e829587bb250ad7b21ed9a09cffaff9f23eea34d48e9316fa3929ba5\n  - edge_id:\
    \ f112w-decreases-turnover\n    subject: f112w\n    predicate: decreases\n   \
    \ object: turnover\n    mechanism: kcat0.0020/s versus WT0.024/s under substrate\
    \ variation.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:19236001\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC2666787/\n      snippet: was catalytically\
    \ competent\n      explanation: Table3, Co(I) assay Methods; comparison within\
    \ the same assay.\n      cache_path: evidence/PF01923/mera-2009.txt\n      cache_sha256:\
    \ 8e210da8e829587bb250ad7b21ed9a09cffaff9f23eea34d48e9316fa3929ba5\n- graph_id:\
    \ lrpduo-cobii-kinetics-2009\n  title: F112 and F163 substitutions alter the coupled\
    \ assay\n  scope: Mera2009 LrPduO variants in the cob(II)alamin reduction/adenosylation\
    \ assay.\n  context: Anoxic37C; Tris200mM pH8, KCl0.1M, MgCl2 1.5mM, Fpr73ug/mL,\
    \ FldA0.6mg/mL, NADPH1mM;525nm initial-rate\n    readout.\n  family_mapping: L.\
    \ reuteri CRL1098 LrPduO from AY780645/AAX14514.1; current Q50EJ2 sequence v1\
    \ (gene\n    label cobA), 188 aa, PF01923 3-169. PDB3CI1 maps reference2-188 to\
    \ entity8-194 with a nonidentical\n    N terminus. F112/F163 are inside PF01923;\
    \ F187 and tail183-188 are outside. TEV-cleaved preparation\n    is not an isolated\
    \ domain.\n  scope_status: MECHANISTIC\n  limitations: F112A is very low, not\
    \ proven zero. Apparent Km is not Kd; reductant coupling and mutation-induced\n\
    \    structural changes remain possible contributors. Do not join crystal structures\
    \ to an observed atomic\n    reaction chain.\n  nodes:\n  - node_id: f112a\n \
    \   label: F112A substitution in LrPduO\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q50EJ2\n  - node_id: f112h\n    label: F112H substitution in\
    \ LrPduO\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q50EJ2\n\
    \  - node_id: f112y\n    label: F112Y substitution in LrPduO\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q50EJ2\n  - node_id: f112w\n    label: F112W\
    \ substitution in LrPduO\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q50EJ2\n\
    \  - node_id: f163a\n    label: F163A substitution\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q50EJ2\n  - node_id: activity\n    label: Coupled\
    \ AdoCbl-forming activity\n    node_type: STATE\n  - node_id: km\n    label: Apparent\
    \ cob(II)alamin Km\n    node_type: STATE\n  edges:\n  - edge_id: f112a-decreases-activity\n\
    \    subject: f112a\n    predicate: decreases\n    object: activity\n    mechanism:\
    \ Activity is extremely low and kinetic constants were not determined.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:19236001\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2666787/\n\
    \      snippet: extremely low activity\n      explanation: Table2 and F112A Results.\n\
    \      cache_path: evidence/PF01923/mera-2009.txt\n      cache_sha256: 8e210da8e829587bb250ad7b21ed9a09cffaff9f23eea34d48e9316fa3929ba5\n\
    \  - edge_id: f112h-decreases-activity\n    subject: f112h\n    predicate: decreases\n\
    \    object: activity\n    mechanism: kcat0.00067/s versus WT0.038/s.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:19236001\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2666787/\n\
    \      snippet: extremely low activity\n      explanation: Table2, coupled-assay\
    \ kinetic parameters.\n      cache_path: evidence/PF01923/mera-2009.txt\n    \
    \  cache_sha256: 8e210da8e829587bb250ad7b21ed9a09cffaff9f23eea34d48e9316fa3929ba5\n\
    \  - edge_id: f112y-decreases-activity\n    subject: f112y\n    predicate: decreases\n\
    \    object: activity\n    mechanism: kcat0.0027/s versus WT0.038/s.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:19236001\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2666787/\n\
    \      snippet: extremely low activity\n      explanation: Table2, coupled-assay\
    \ kinetic parameters.\n      cache_path: evidence/PF01923/mera-2009.txt\n    \
    \  cache_sha256: 8e210da8e829587bb250ad7b21ed9a09cffaff9f23eea34d48e9316fa3929ba5\n\
    \  - edge_id: f112w-decreases-activity\n    subject: f112w\n    predicate: decreases\n\
    \    object: activity\n    mechanism: kcat0.0032/s versus WT0.038/s.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:19236001\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2666787/\n\
    \      snippet: extremely low activity\n      explanation: Table2, coupled-assay\
    \ kinetic parameters.\n      cache_path: evidence/PF01923/mera-2009.txt\n    \
    \  cache_sha256: 8e210da8e829587bb250ad7b21ed9a09cffaff9f23eea34d48e9316fa3929ba5\n\
    \  - edge_id: f163a-increases-km\n    subject: f163a\n    predicate: increases\n\
    \    object: km\n    mechanism: Apparent Km rises to134+/-13uM from7.8+/-1.1uM\
    \ WT; this is not a directly measured binding\n      affinity.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:19236001\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2666787/\n\
    \      snippet: was catalytically competent\n      explanation: Table2; F163A\
    \ ATP kinetics additionally use subsaturating corrinoid.\n      cache_path: evidence/PF01923/mera-2009.txt\n\
    \      cache_sha256: 8e210da8e829587bb250ad7b21ed9a09cffaff9f23eea34d48e9316fa3929ba5\n\
    - graph_id: lrpduo-variant-growth-2009\n  title: Tested LrPduO variants fail growth\
    \ complementation\n  scope: Mera2009 individual F112A/H/Y/W, F163A, F187A and\
    \ deletion183-188 constructs.\n  context: Heterologous Salmonella cobA host,30mM\
    \ glycerol/150nM dicyanocobinamide; compare WT LrPduO\n    complementation.\n\
    \  family_mapping: L. reuteri CRL1098 LrPduO from AY780645/AAX14514.1; current\
    \ Q50EJ2 sequence v1 (gene\n    label cobA), 188 aa, PF01923 3-169. PDB3CI1 maps\
    \ reference2-188 to entity8-194 with a nonidentical\n    N terminus. F112/F163\
    \ are inside PF01923; F187 and tail183-188 are outside. TEV-cleaved preparation\n\
    \    is not an isolated domain.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:99287\n\
    \  limitations: The paper reports this result without showing raw growth data.\
    \ F187 and the six-residue\n    tail lie outside PF01923; deletion183-188 is not\
    \ a single S183 deletion. In-vitro activity retained\n    by some variants does\
    \ not guarantee this growth phenotype.\n  nodes:\n  - node_id: variants\n    label:\
    \ Replace WT LrPduO with an individually tested variant\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q50EJ2\n  - node_id: growth\n    label: Heterologous\
    \ growth complementation\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: variants-decreases-growth\n\
    \    subject: variants\n    predicate: decreases\n    object: growth\n    mechanism:\
    \ None of the tested variants supports the reported growth rescue, despite several\
    \ retaining\n      substantial biochemical activity.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:19236001\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2666787/\n\
    \      snippet: none of the variant enzymes analyzed in this work\n      explanation:\
    \ In-vivo analysis Methods and Results; data not shown.\n      cache_path: evidence/PF01923/mera-2009.txt\n\
    \      cache_sha256: 8e210da8e829587bb250ad7b21ed9a09cffaff9f23eea34d48e9316fa3929ba5\n\
    - graph_id: lr-free-flavin-2010\n  title: LrPduO uses supplied reduced flavins\
    \ in vitro\n  scope: Mera2010 separate recombinant LrPduO preparation; TEV-cleaved.\n\
    \  context: Anoxic37C MgATP assay; FMNH2/FADH2 generated with NADH before the\
    \ reaction. Fre can regenerate\n    donor but pre-reduced flavin also works without\
    \ it.\n  family_mapping: L. reuteri CRL1098 LrPduO from AY780645/AAX14514.1; current\
    \ Q50EJ2 sequence v1 (gene\n    label cobA), 188 aa, PF01923 3-169. PDB3CI1 maps\
    \ reference2-188 to entity8-194 with a nonidentical\n    N terminus. F112/F163\
    \ are inside PF01923; F187 and tail183-188 are outside. TEV-cleaved preparation\n\
    \    is not an isolated domain.\n  scope_status: MECHANISTIC\n  limitations: This\
    \ does not establish a unique physiological donor or an autonomous reductase.\
    \ Free corrinoid\n    and LrF112A negatives are reported without displayed traces;\
    \ Fig4 and Table1 donor ratios differ.\n  nodes:\n  - node_id: fmnh2\n    label:\
    \ LrPduO, MgATP, cob(II)alamin and FMNH2\n    node_type: ACTIVITY\n    grounding:\n\
    \    - UniProtKB:Q50EJ2\n  - node_id: fadh2\n    label: LrPduO, MgATP, cob(II)alamin\
    \ and FADH2\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:Q50EJ2\n\
    \  - node_id: product\n    label: AdoCbl product\n    node_type: STATE\n  edges:\n\
    \  - edge_id: fmnh2-produces-product\n    subject: fmnh2\n    predicate: produces\n\
    \    object: product\n    mechanism: The complete donor/enzyme reaction forms\
    \ AdoCbl; enzyme/ATP/donor omissions prevent product.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:19933577\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2823439/\n\
    \      snippet: presence of free dihydroflavins\n      explanation: Figures2-4;\
    \ spectral, photolysis and product-bioassay controls.\n      cache_path: evidence/PF01923/mera-2010.txt\n\
    \      cache_sha256: 5d961468bf6c2c201f8f2d6910725189a1d947b02eee0b2761f586c545b6a482\n\
    \  - edge_id: fadh2-produces-product\n    subject: fadh2\n    predicate: produces\n\
    \    object: product\n    mechanism: Reduced FAD likewise supports the coupled\
    \ reduction/adenosylation reaction in this preparation.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:19933577\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2823439/\n\
    \      snippet: presence of free dihydroflavins\n      explanation: 'Results:\
    \ FMNH2 and FADH2 donor comparison; conditions not an in-vivo donor assignment.'\n\
    \      cache_path: evidence/PF01923/mera-2010.txt\n      cache_sha256: 5d961468bf6c2c201f8f2d6910725189a1d947b02eee0b2761f586c545b6a482\n\
    - graph_id: hu-free-flavin-2010\n  title: human ATR uses supplied reduced flavins\
    \ in vitro\n  scope: Mera2010 separate recombinant human ATR preparation; TEV-cleaved.\n\
    \  context: Anoxic37C MgATP assay; FMNH2/FADH2 generated with NADH before the\
    \ reaction. Fre can regenerate\n    donor but pre-reduced flavin also works without\
    \ it.\n  family_mapping: Human MMAB Q96EY8 sequence v1, 250 aa, PF01923 58-227.\
    \ F170/R186/R190/E193 verified\n    in the reference. Exact assay-specific recombinant\
    \ endpoints remain unresolved; cited purification\n    methods include full-length\
    \ and deltaN18 constructs with cleaved His tags. Reference mapping is not\n  \
    \  proof of an isolated-domain effect.\n  scope_status: MECHANISTIC\n  taxon:\
    \ NCBITaxon:9606\n  limitations: This does not establish a unique physiological\
    \ donor or an autonomous reductase. Free corrinoid\n    and LrF112A negatives\
    \ are reported without displayed traces; Fig4 and Table1 donor ratios differ.\n\
    \  nodes:\n  - node_id: fmnh2\n    label: human ATR, MgATP, cob(II)alamin and\
    \ FMNH2\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:Q96EY8\n  -\
    \ node_id: fadh2\n    label: human ATR, MgATP, cob(II)alamin and FADH2\n    node_type:\
    \ ACTIVITY\n    grounding:\n    - UniProtKB:Q96EY8\n  - node_id: product\n   \
    \ label: AdoCbl product\n    node_type: STATE\n  edges:\n  - edge_id: fmnh2-produces-product\n\
    \    subject: fmnh2\n    predicate: produces\n    object: product\n    mechanism:\
    \ The complete donor/enzyme reaction forms AdoCbl; enzyme/ATP/donor omissions\
    \ prevent product.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:19933577\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC2823439/\n      snippet: dihydroflavins\
    \ quantitatively drove the adenosylation of cob(II)alamin by the human adenosyltransferase\n\
    \        enzyme\n      explanation: Figures2-4; spectral, photolysis and product-bioassay\
    \ controls.\n      cache_path: evidence/PF01923/mera-2010.txt\n      cache_sha256:\
    \ 5d961468bf6c2c201f8f2d6910725189a1d947b02eee0b2761f586c545b6a482\n  - edge_id:\
    \ fadh2-produces-product\n    subject: fadh2\n    predicate: produces\n    object:\
    \ product\n    mechanism: Reduced FAD likewise supports the coupled reduction/adenosylation\
    \ reaction in this preparation.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:19933577\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2823439/\n      snippet:\
    \ dihydroflavins quantitatively drove the adenosylation of cob(II)alamin by the\
    \ human adenosyltransferase\n        enzyme\n      explanation: 'Results: FMNH2\
    \ and FADH2 donor comparison; conditions not an in-vivo donor assignment.'\n \
    \     cache_path: evidence/PF01923/mera-2010.txt\n      cache_sha256: 5d961468bf6c2c201f8f2d6910725189a1d947b02eee0b2761f586c545b6a482\n\
    - graph_id: seeutt-product-2014\n  title: EutT forms AdoCbl in a coupled flavin\
    \ assay\n  scope: Moore2014 purified LT2 EutT.\n  context: Anoxic37C PIPES50mM\
    \ pH7; MgATP1mM,FADH2 20uM,Fre0.005mg/mL,NADH1mM;15-20min corrinoid pre-reduction.\n\
    \  family_mapping: SeLT2 STM2467 EutT Q9ZFV4 sequence v1, 267 aa, PF01923 92-246.\
    \ H67/C79/C80/C83 are verified\n    reference residues OUTSIDE the domain. Purified\
    \ protein retains GT before M1; whole-protein effects\n    cannot be attributed\
    \ to isolated PF01923.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:99287\n\
    \  limitations: Reaction requires the combined enzyme, substrates and reducing\
    \ system. This is not direct\n    ATP-independent conversion of cyanocobalamin.\
    \ Printed extinction-coefficient units are unresolved.\n  nodes:\n  - node_id:\
    \ reaction\n    label: EutT, MgATP, cob(II)alamin and reduced-flavin system\n\
    \    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:Q9ZFV4\n  - node_id:\
    \ product\n    label: AdoCbl product\n    node_type: STATE\n  edges:\n  - edge_id:\
    \ reaction-produces-product\n    subject: reaction\n    predicate: produces\n\
    \    object: product\n    mechanism: Product has a525nm absorbance maximum and\
    \ photolyzes to the cob(II)alamin spectrum.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:24336938\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3911174/\n      snippet:\
    \ free dihydroflavins drive the adenosylation\n      explanation: Figure2 and\
    \ modified Co(II) assay Methods.\n      cache_path: evidence/PF01923/moore-2014.txt\n\
    \      cache_sha256: ba545296384ec0ed7f90c7eb0c3ce04a7a3228355db1b5ea068b9a8c4abe6ed4\n\
    - graph_id: seeutt-metal-oxygen-2014\n  title: Metalation changes EutT activity\
    \ and oxygen sensitivity\n  scope: Moore2014 demetalated and reconstituted purified\
    \ EutT.\n  context: EDTA demetalation followed by buffer exchange and Fe(II) or\
    \ Zn(II) reconstitution; Figure3\n    anoxic/oxic assays. Separate0.3% H2O2 challenge\
    \ followed by catalase.\n  family_mapping: SeLT2 STM2467 EutT Q9ZFV4 sequence\
    \ v1, 267 aa, PF01923 92-246. H67/C79/C80/C83 are verified\n    reference residues\
    \ OUTSIDE the domain. Purified protein retains GT before M1; whole-protein effects\n\
    \    cannot be attributed to isolated PF01923.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:99287\n  limitations: The text's fold-excess label disagrees\
    \ with stated reconstitution concentrations. Zn-supported\n    activity survives\
    \ the tested oxidation conditions, so universal oxygen lability is unsupported.\
    \ Native\n    metal occupancy is not directly established.\n  nodes:\n  - node_id:\
    \ fe\n    label: Fe(II) reconstitution of the demetalated preparation\n    node_type:\
    \ PERTURBATION\n  - node_id: zn\n    label: Zn(II) reconstitution of the demetalated\
    \ preparation\n    node_type: PERTURBATION\n  - node_id: air\n    label: Expose\
    \ Fe-loaded EutT to air\n    node_type: PERTURBATION\n  - node_id: peroxide\n\
    \    label: Expose Fe-loaded EutT to H2O2\n    node_type: PERTURBATION\n  - node_id:\
    \ activity\n    label: Coupled AdoCbl-forming activity\n    node_type: STATE\n\
    \  edges:\n  - edge_id: fe-increases-activity\n    subject: fe\n    predicate:\
    \ increases\n    object: activity\n    mechanism: Ferrous reconstitution gives\
    \ the highest measured activity compared with the water/no-metal\n      treatment.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:24336938\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3911174/\n\
    \      snippet: metalation with ferrous ions\n      explanation: Figure3 and metal-reconstitution\
    \ Results.\n      cache_path: evidence/PF01923/moore-2014.txt\n      cache_sha256:\
    \ ba545296384ec0ed7f90c7eb0c3ce04a7a3228355db1b5ea068b9a8c4abe6ed4\n  - edge_id:\
    \ zn-increases-activity\n    subject: zn\n    predicate: increases\n    object:\
    \ activity\n    mechanism: Zinc reconstitution restores substantial activity compared\
    \ with demetalated material.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:24336938\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3911174/\n      snippet:\
    \ metalation with ferrous ions\n      explanation: Figure3 oxic and anoxic comparisons.\n\
    \      cache_path: evidence/PF01923/moore-2014.txt\n      cache_sha256: ba545296384ec0ed7f90c7eb0c3ce04a7a3228355db1b5ea068b9a8c4abe6ed4\n\
    \  - edge_id: air-decreases-activity\n    subject: air\n    predicate: decreases\n\
    \    object: activity\n    mechanism: Air exposure abolishes measurable activity\
    \ of the Fe-loaded preparation, unlike Zn-loaded\n      material.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:24336938\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3911174/\n\
    \      snippet: metalation with ferrous ions\n      explanation: Figure3 and oxidation\
    \ Results.\n      cache_path: evidence/PF01923/moore-2014.txt\n      cache_sha256:\
    \ ba545296384ec0ed7f90c7eb0c3ce04a7a3228355db1b5ea068b9a8c4abe6ed4\n  - edge_id:\
    \ peroxide-decreases-activity\n    subject: peroxide\n    predicate: decreases\n\
    \    object: activity\n    mechanism: The peroxide challenge abolishes Fe-loaded\
    \ activity; Zn-loaded activity remains, under\n      the reported treatment.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:24336938\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3911174/\n\
    \      snippet: metalation with ferrous ions\n      explanation: Oxidant-treatment\
    \ Methods and Results; peroxide comparison described in text.\n      cache_path:\
    \ evidence/PF01923/moore-2014.txt\n      cache_sha256: ba545296384ec0ed7f90c7eb0c3ce04a7a3228355db1b5ea068b9a8c4abe6ed4\n\
    - graph_id: seeutt-variant-activity-2014\n  title: EutT motif substitutions lower\
    \ biochemical activity\n  scope: Moore2014 individual H67A/C79A/C80A/C83A variants\
    \ of whole EutT.\n  context: Fe-reconstituted proteins in the Table2 FADH2-supported\
    \ cob(II)alamin assay.\n  family_mapping: SeLT2 STM2467 EutT Q9ZFV4 sequence v1,\
    \ 267 aa, PF01923 92-246. H67/C79/C80/C83 are verified\n    reference residues\
    \ OUTSIDE the domain. Purified protein retains GT before M1; whole-protein effects\n\
    \    cannot be attributed to isolated PF01923.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:99287\n  limitations: All four positions are outside PF01923.\
    \ H67A changes oligomer distribution; neither the\n    activity effect nor elemental\
    \ analysis alone proves exact metal-ligand chemistry. Table1 C83A zinc\n    value\
    \ conflicts with prose saying undetectable.\n  nodes:\n  - node_id: h67a\n   \
    \ label: H67A substitution in full EutT\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q9ZFV4\n  - node_id: c79a\n    label: C79A substitution in full\
    \ EutT\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q9ZFV4\n\
    \  - node_id: c80a\n    label: C80A substitution in full EutT\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:Q9ZFV4\n  - node_id: c83a\n  \
    \  label: C83A substitution in full EutT\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:Q9ZFV4\n  - node_id: activity\n    label: Coupled AdoCbl-forming\
    \ activity\n    node_type: STATE\n  edges:\n  - edge_id: h67a-decreases-activity\n\
    \    subject: h67a\n    predicate: decreases\n    object: activity\n    mechanism:\
    \ kcat0.0083/s versus WT0.022/s; altered assembly remains an alternative contributor.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:24336938\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3911174/\n\
    \      snippet: kinetic parameters of EutT variants\n      explanation: Table2\
    \ and native-PAGE discussion.\n      cache_path: evidence/PF01923/moore-2014.txt\n\
    \      cache_sha256: ba545296384ec0ed7f90c7eb0c3ce04a7a3228355db1b5ea068b9a8c4abe6ed4\n\
    \  - edge_id: c79a-decreases-activity\n    subject: c79a\n    predicate: decreases\n\
    \    object: activity\n    mechanism: kcat0.0042/s versus WT0.022/s, despite near-WT\
    \ growth rescue in a different assay.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:24336938\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3911174/\n      snippet:\
    \ kinetic parameters of EutT variants\n      explanation: Table2, not a growth\
    \ measurement.\n      cache_path: evidence/PF01923/moore-2014.txt\n      cache_sha256:\
    \ ba545296384ec0ed7f90c7eb0c3ce04a7a3228355db1b5ea068b9a8c4abe6ed4\n  - edge_id:\
    \ c80a-decreases-activity\n    subject: c80a\n    predicate: decreases\n    object:\
    \ activity\n    mechanism: Activity is not detected in the reconstituted preparation.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:24336938\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3911174/\n\
    \      snippet: kinetic parameters of EutT variants\n      explanation: Table2\
    \ and variant Results.\n      cache_path: evidence/PF01923/moore-2014.txt\n  \
    \    cache_sha256: ba545296384ec0ed7f90c7eb0c3ce04a7a3228355db1b5ea068b9a8c4abe6ed4\n\
    \  - edge_id: c83a-decreases-activity\n    subject: c83a\n    predicate: decreases\n\
    \    object: activity\n    mechanism: kcat0.0022/s versus WT0.022/s, with residual\
    \ activity retained.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:24336938\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC3911174/\n      snippet: kinetic parameters\
    \ of EutT variants\n      explanation: Table2.\n      cache_path: evidence/PF01923/moore-2014.txt\n\
    \      cache_sha256: ba545296384ec0ed7f90c7eb0c3ce04a7a3228355db1b5ea068b9a8c4abe6ed4\n\
    - graph_id: seeutt-complementation-2014\n  title: EutT variants differ in ethanolamine-growth\
    \ rescue\n  scope: Moore2014 JE13176 cobA343::MudJ delta-eut114 delta-pduO523.\n\
    \  context: pBAD24 alleles,90mM ethanolamine carbon plus HOCbl; Methods supplements\
    \ include methionine0.5mM\n    and glycerol0.5mM.\n  family_mapping: SeLT2 STM2467\
    \ EutT Q9ZFV4 sequence v1, 267 aa, PF01923 92-246. H67/C79/C80/C83 are verified\n\
    \    reference residues OUTSIDE the domain. Purified protein retains GT before\
    \ M1; whole-protein effects\n    cannot be attributed to isolated PF01923.\n \
    \ scope_status: PHENOTYPIC\n  taxon: NCBITaxon:99287\n  limitations: Methods print500mM\
    \ arabinose; do not silently correct it or invent an HOCbl dose. No intracellular\n\
    \    AdoCbl measurement. Mutant effects are whole-protein and indirect.\n  nodes:\n\
    \  - node_id: wt\n    label: Express WT EutT in JE13176\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q9ZFV4\n  - node_id: c79a\n    label: Express\
    \ C79A EutT in JE13176\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q9ZFV4\n\
    \  - node_id: h67a\n    label: Replace WT with H67A EutT\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q9ZFV4\n  - node_id: c80a\n    label: Replace\
    \ WT with C80A EutT\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q9ZFV4\n\
    \  - node_id: c83a\n    label: Replace WT with C83A EutT\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q9ZFV4\n  - node_id: growth\n    label: Growth\
    \ on ethanolamine\n    node_type: PHENOTYPE\n  edges:\n  - edge_id: wt-increases-growth\n\
    \    subject: wt\n    predicate: increases\n    object: growth\n    mechanism:\
    \ WT plasmid restores growth relative to the empty vector.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24336938\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3911174/\n\
    \      snippet: complemented almost as well\n      explanation: Original Figure5;\
    \ plasmid and genotype Methods.\n      cache_path: evidence/PF01923/moore-2014.txt\n\
    \      cache_sha256: ba545296384ec0ed7f90c7eb0c3ce04a7a3228355db1b5ea068b9a8c4abe6ed4\n\
    \  - edge_id: c79a-increases-growth\n    subject: c79a\n    predicate: increases\n\
    \    object: growth\n    mechanism: C79A complements nearly as well as WT despite\
    \ reduced in-vitro kcat.\n    directness: INDIRECT\n    support: OBSERVED\n  \
    \  evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:24336938\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3911174/\n      snippet:\
    \ complemented almost as well\n      explanation: Original Figure5.\n      cache_path:\
    \ evidence/PF01923/moore-2014.txt\n      cache_sha256: ba545296384ec0ed7f90c7eb0c3ce04a7a3228355db1b5ea068b9a8c4abe6ed4\n\
    \  - edge_id: h67a-decreases-growth\n    subject: h67a\n    predicate: decreases\n\
    \    object: growth\n    mechanism: The variant fails to restore the WT-plasmid\
    \ growth phenotype under these conditions.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:24336938\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3911174/\n      snippet:\
    \ did not restore growth\n      explanation: Original Figure5; direct observation\
    \ is growth, not its proposed cofactor explanation.\n      cache_path: evidence/PF01923/moore-2014.txt\n\
    \      cache_sha256: ba545296384ec0ed7f90c7eb0c3ce04a7a3228355db1b5ea068b9a8c4abe6ed4\n\
    \  - edge_id: c80a-decreases-growth\n    subject: c80a\n    predicate: decreases\n\
    \    object: growth\n    mechanism: The variant fails to restore the WT-plasmid\
    \ growth phenotype under these conditions.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:24336938\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3911174/\n      snippet:\
    \ did not restore growth\n      explanation: Original Figure5; direct observation\
    \ is growth, not its proposed cofactor explanation.\n      cache_path: evidence/PF01923/moore-2014.txt\n\
    \      cache_sha256: ba545296384ec0ed7f90c7eb0c3ce04a7a3228355db1b5ea068b9a8c4abe6ed4\n\
    \  - edge_id: c83a-decreases-growth\n    subject: c83a\n    predicate: decreases\n\
    \    object: growth\n    mechanism: The variant fails to restore the WT-plasmid\
    \ growth phenotype under these conditions.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:24336938\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3911174/\n      snippet:\
    \ did not restore growth\n      explanation: Original Figure5; direct observation\
    \ is growth, not its proposed cofactor explanation.\n      cache_path: evidence/PF01923/moore-2014.txt\n\
    \      cache_sha256: ba545296384ec0ed7f90c7eb0c3ce04a7a3228355db1b5ea068b9a8c4abe6ed4\n\
    - graph_id: lmeutt-product-2018\n  title: Listeria EutT activity depends on corrinoid\
    \ reduction state\n  scope: Costa2018 TEV-cleaved LmEutT from10403S, about90%\
    \ pure.\n  context: 'Figure6/S6 MgATP assays: Ti(III)citrate supplies cob(I) substrates,\
    \ whereas Fre/FAD or FldA/Fpr\n    supplies the cob(II) reduction-coupled systems.\
    \ Figure5 independently checks product bioactivity/photolysis.'\n  family_mapping:\
    \ L. monocytogenes10403S EutT maps to A0A0H3GFM5 sequence v1, LMRG_00627/AEO06164.1,\
    \ 251\n    aa, PF01923 83-242. Costa2018 Figure2/S3 and terminal primers support\
    \ the strain-matched reference;\n    no independent full clone sequence/tag-remnant\
    \ verification. This is not EGD-e or either of the other10403S\n    PF01923 proteins.\n\
    \  scope_status: MECHANISTIC\n  taxon: NCBITaxon:393133\n  limitations: Cob(II)inamide\
    \ is negative with both tested biological reducing systems while CobA positive\n\
    \    control works; cob(I)inamide is a substrate. 'Metal-less' excludes a required\
    \ transition-metal cofactor,\n    not assay Mg. No-added-ATP Figure5 reaction\
    \ has residual bioactivity.\n  nodes:\n  - node_id: cobi\n    label: LmEutT, MgATP\
    \ and chemically reduced cob(I)alamin\n    node_type: ACTIVITY\n    grounding:\n\
    \    - UniProtKB:A0A0H3GFM5\n  - node_id: cobii-fre\n    label: LmEutT, MgATP,\
    \ cob(II)alamin and Fre/FAD system\n    node_type: ACTIVITY\n    grounding:\n\
    \    - UniProtKB:A0A0H3GFM5\n  - node_id: cobii-flda\n    label: LmEutT, MgATP,\
    \ cob(II)alamin and FldA/Fpr system\n    node_type: ACTIVITY\n    grounding:\n\
    \    - UniProtKB:A0A0H3GFM5\n  - node_id: cbii\n    label: LmEutT, MgATP and chemically\
    \ reduced cob(I)inamide\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:A0A0H3GFM5\n\
    \  - node_id: adocbl\n    label: AdoCbl formation\n    node_type: STATE\n  - node_id:\
    \ adocbi\n    label: Adenosylcobinamide formation\n    node_type: STATE\n  edges:\n\
    \  - edge_id: cobi-produces-adocbl\n    subject: cobi\n    predicate: produces\n\
    \    object: adocbl\n    mechanism: The complete reaction produces the cobalamin\
    \ adenosylation readout; spectra and appropriate\n      no-protein controls support\
    \ product assignment.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:30071718\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC6113058/\n      snippet: adenosylated\
    \ cobalamin\n      explanation: Figure6 and original supplementFigureS6; Figure5\
    \ product validation.\n      cache_path: evidence/PF01923/costa-2018.txt\n   \
    \   cache_sha256: b4a6fe709c16af5345a5fdb3e7ff0aad52b57029cb08992856c294d41eff54ff\n\
    \  - edge_id: cobii-fre-produces-adocbl\n    subject: cobii-fre\n    predicate:\
    \ produces\n    object: adocbl\n    mechanism: The complete reaction produces\
    \ the cobalamin adenosylation readout; spectra and appropriate\n      no-protein\
    \ controls support product assignment.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:30071718\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6113058/\n      snippet:\
    \ adenosylated cobalamin\n      explanation: Figure6 and original supplementFigureS6;\
    \ Figure5 product validation.\n      cache_path: evidence/PF01923/costa-2018.txt\n\
    \      cache_sha256: b4a6fe709c16af5345a5fdb3e7ff0aad52b57029cb08992856c294d41eff54ff\n\
    \  - edge_id: cobii-flda-produces-adocbl\n    subject: cobii-flda\n    predicate:\
    \ produces\n    object: adocbl\n    mechanism: The complete reaction produces\
    \ the cobalamin adenosylation readout; spectra and appropriate\n      no-protein\
    \ controls support product assignment.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:30071718\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6113058/\n      snippet:\
    \ adenosylated cobalamin\n      explanation: Figure6 and original supplementFigureS6;\
    \ Figure5 product validation.\n      cache_path: evidence/PF01923/costa-2018.txt\n\
    \      cache_sha256: b4a6fe709c16af5345a5fdb3e7ff0aad52b57029cb08992856c294d41eff54ff\n\
    \  - edge_id: cbii-produces-adocbi\n    subject: cbii\n    predicate: produces\n\
    \    object: adocbi\n    mechanism: Chemically pre-reduced cob(I)inamide is adenosylated,\
    \ unlike the cob(II)inamide tests.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:30071718\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6113058/\n      snippet:\
    \ adenosylated cobalamin\n      explanation: Figure6 right panel and original\
    \ supplementFigureS6 bottom-right.\n      cache_path: evidence/PF01923/costa-2018.txt\n\
    \      cache_sha256: b4a6fe709c16af5345a5fdb3e7ff0aad52b57029cb08992856c294d41eff54ff\n\
    - graph_id: lmeutt-triphosphate-2018\n  title: Listeria EutT releases triphosphate\n\
    \  scope: Costa2018 LmEutT reaction followed by31P NMR.\n  context: Tris100mM\
    \ pH7.5 at37C,KCl500mM,MgCl2 2mM,Ti(III)1mM,HOCbl100uM,ATP3mM,enzyme20ug/mL;5h\
    \ in light\n    to recycle corrinoid.\n  family_mapping: L. monocytogenes10403S\
    \ EutT maps to A0A0H3GFM5 sequence v1, LMRG_00627/AEO06164.1, 251\n    aa, PF01923\
    \ 83-242. Costa2018 Figure2/S3 and terminal primers support the strain-matched\
    \ reference;\n    no independent full clone sequence/tag-remnant verification.\
    \ This is not EGD-e or either of the other10403S\n    PF01923 proteins.\n  scope_status:\
    \ MECHANISTIC\n  taxon: NCBITaxon:393133\n  limitations: Light recycling differs\
    \ from the dark product bioassay. Product identity does not establish\n    that\
    \ every EutT homolog releases the same phosphate products.\n  nodes:\n  - node_id:\
    \ reaction\n    label: LmEutT, ATP and reduced-corrinoid cycling reaction\n  \
    \  node_type: ACTIVITY\n    grounding:\n    - UniProtKB:A0A0H3GFM5\n  - node_id:\
    \ pppi\n    label: Triphosphate product\n    node_type: STATE\n  edges:\n  - edge_id:\
    \ reaction-produces-pppi\n    subject: reaction\n    predicate: produces\n   \
    \ object: pppi\n    mechanism: Phosphorus signals match PPPi standards; no-cobalamin\
    \ control lacks those product signals.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:30071718\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6113058/\n      snippet:\
    \ triphosphate was the by-product of the reaction\n      explanation: Original\
    \ Figure7 and NMR Methods.\n      cache_path: evidence/PF01923/costa-2018.txt\n\
    \      cache_sha256: b4a6fe709c16af5345a5fdb3e7ff0aad52b57029cb08992856c294d41eff54ff\n\
    - graph_id: lmeutt-carbon-growth-2018\n  title: Listeria EutT supports ethanolamine-carbon\
    \ growth\n  scope: Costa2018 heterologous Salmonella JE23613 delta-pduO522 delta-cobA1465\
    \ delta-eutT1141.\n  context: 90mM ethanolamine as carbon/energy source; cyanocobalamin200nM,IPTG100uM,37C,\
    \ OD630; pTAC85\n    alleles in TableS3.\n  family_mapping: L. monocytogenes10403S\
    \ EutT maps to A0A0H3GFM5 sequence v1, LMRG_00627/AEO06164.1, 251\n    aa, PF01923\
    \ 83-242. Costa2018 Figure2/S3 and terminal primers support the strain-matched\
    \ reference;\n    no independent full clone sequence/tag-remnant verification.\
    \ This is not EGD-e or either of the other10403S\n    PF01923 proteins.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:99287\n  limitations: Host is Salmonella, not\
    \ native Listeria. Codon optimization can change expression; growth\n    alone\
    \ does not measure enzyme-specific flux or intracellular cofactor concentrations.\n\
    \  nodes:\n  - node_id: native\n    label: Express native LmEutT coding sequence\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:A0A0H3GFM5\n  -\
    \ node_id: optimized\n    label: Express codon-optimized LmEutT coding sequence\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:A0A0H3GFM5\n  -\
    \ node_id: growth\n    label: Growth with ethanolamine as carbon source\n    node_type:\
    \ PHENOTYPE\n  edges:\n  - edge_id: native-increases-growth\n    subject: native\n\
    \    predicate: increases\n    object: growth\n    mechanism: Native Lm allele\
    \ gives weak delayed rescue; codon optimization improves yield but retains\n \
    \     about10h lag and does not reach SeEutT performance.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:30071718\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6113058/\n\
    \      snippet: restored growth with ethanolamine\n      explanation: Original\
    \ Figure3A, growth Methods and supplementTableS3.\n      cache_path: evidence/PF01923/costa-2018.txt\n\
    \      cache_sha256: b4a6fe709c16af5345a5fdb3e7ff0aad52b57029cb08992856c294d41eff54ff\n\
    \  - edge_id: optimized-increases-growth\n    subject: optimized\n    predicate:\
    \ increases\n    object: growth\n    mechanism: Native Lm allele gives weak delayed\
    \ rescue; codon optimization improves yield but retains\n      about10h lag and\
    \ does not reach SeEutT performance.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:30071718\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6113058/\n      snippet:\
    \ restored growth with ethanolamine\n      explanation: Original Figure3A, growth\
    \ Methods and supplementTableS3.\n      cache_path: evidence/PF01923/costa-2018.txt\n\
    \      cache_sha256: b4a6fe709c16af5345a5fdb3e7ff0aad52b57029cb08992856c294d41eff54ff\n\
    - graph_id: lmeutt-nitrogen-growth-2018\n  title: Listeria EutT supports ethanolamine-nitrogen\
    \ growth\n  scope: Costa2018 heterologous Salmonella JE23613 delta-pduO522 delta-cobA1465\
    \ delta-eutT1141.\n  context: 22mM glycerol carbon plus30mM ethanolamine nitrogen;\
    \ cyanocobalamin200nM,IPTG100uM,37C, OD630;\n    pTAC85 alleles in TableS3.\n\
    \  family_mapping: L. monocytogenes10403S EutT maps to A0A0H3GFM5 sequence v1,\
    \ LMRG_00627/AEO06164.1, 251\n    aa, PF01923 83-242. Costa2018 Figure2/S3 and\
    \ terminal primers support the strain-matched reference;\n    no independent full\
    \ clone sequence/tag-remnant verification. This is not EGD-e or either of the\
    \ other10403S\n    PF01923 proteins.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:99287\n\
    \  limitations: Host is Salmonella, not native Listeria. Codon optimization can\
    \ change expression; growth\n    alone does not measure enzyme-specific flux or\
    \ intracellular cofactor concentrations.\n  nodes:\n  - node_id: native\n    label:\
    \ Express native LmEutT coding sequence\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:A0A0H3GFM5\n  - node_id: optimized\n    label: Express codon-optimized\
    \ LmEutT coding sequence\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:A0A0H3GFM5\n\
    \  - node_id: growth\n    label: Growth with ethanolamine as nitrogen source\n\
    \    node_type: PHENOTYPE\n  edges:\n  - edge_id: native-increases-growth\n  \
    \  subject: native\n    predicate: increases\n    object: growth\n    mechanism:\
    \ Both Lm alleles restore growth; delayed onset remains, with the native allele\
    \ about8h behind\n      the SeEutT comparison.\n    directness: INDIRECT\n   \
    \ support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:30071718\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6113058/\n\
    \      snippet: restored growth with ethanolamine\n      explanation: Original\
    \ Figure3B, growth Methods and supplementTableS3.\n      cache_path: evidence/PF01923/costa-2018.txt\n\
    \      cache_sha256: b4a6fe709c16af5345a5fdb3e7ff0aad52b57029cb08992856c294d41eff54ff\n\
    \  - edge_id: optimized-increases-growth\n    subject: optimized\n    predicate:\
    \ increases\n    object: growth\n    mechanism: Both Lm alleles restore growth;\
    \ delayed onset remains, with the native allele about8h behind\n      the SeEutT\
    \ comparison.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:30071718\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC6113058/\n      snippet: restored growth\
    \ with ethanolamine\n      explanation: Original Figure3B, growth Methods and\
    \ supplementTableS3.\n      cache_path: evidence/PF01923/costa-2018.txt\n    \
    \  cache_sha256: b4a6fe709c16af5345a5fdb3e7ff0aad52b57029cb08992856c294d41eff54ff\n\
    - graph_id: lmeutt-reporter-growth-2018\n  title: Listeria EutT enables a cofactor-dependent\
    \ reporter phenotype\n  scope: Costa2018 JE22174 ACAT-deficient Salmonella with\
    \ eutE::MudJ lacZ reporter.\n  context: Lactose29mM,ethanolamine1mM,cyanocobalamin50nM,IPTG10uM,37C;\
    \ native or codon-optimized Lm allele.\n  family_mapping: L. monocytogenes10403S\
    \ EutT maps to A0A0H3GFM5 sequence v1, LMRG_00627/AEO06164.1, 251\n    aa, PF01923\
    \ 83-242. Costa2018 Figure2/S3 and terminal primers support the strain-matched\
    \ reference;\n    no independent full clone sequence/tag-remnant verification.\
    \ This is not EGD-e or either of the other10403S\n    PF01923 proteins.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:99287\n  limitations: The measured endpoint is\
    \ lactose growth driven by a transcriptional reporter, not direct\n    EutR binding,\
    \ transcription quantification or intracellular AdoCbl concentration.\n  nodes:\n\
    \  - node_id: native\n    label: Express native LmEutT in the reporter host\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:A0A0H3GFM5\n  -\
    \ node_id: optimized\n    label: Express codon-optimized LmEutT in the reporter\
    \ host\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:A0A0H3GFM5\n\
    \  - node_id: growth\n    label: Lactose reporter growth\n    node_type: PHENOTYPE\n\
    \  edges:\n  - edge_id: native-increases-growth\n    subject: native\n    predicate:\
    \ increases\n    object: growth\n    mechanism: The expressed allele enables robust\
    \ reporter growth relative to the ACAT-deficient vector\n      control.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:30071718\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6113058/\n\
    \      snippet: supported robust growth with lactose\n      explanation: Original\
    \ Figure4 and reporter-assay Methods.\n      cache_path: evidence/PF01923/costa-2018.txt\n\
    \      cache_sha256: b4a6fe709c16af5345a5fdb3e7ff0aad52b57029cb08992856c294d41eff54ff\n\
    \  - edge_id: optimized-increases-growth\n    subject: optimized\n    predicate:\
    \ increases\n    object: growth\n    mechanism: The expressed allele enables robust\
    \ reporter growth relative to the ACAT-deficient vector\n      control.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:30071718\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6113058/\n\
    \      snippet: supported robust growth with lactose\n      explanation: Original\
    \ Figure4 and reporter-assay Methods.\n      cache_path: evidence/PF01923/costa-2018.txt\n\
    \      cache_sha256: b4a6fe709c16af5345a5fdb3e7ff0aad52b57029cb08992856c294d41eff54ff\n\
    - graph_id: mmab-fdx1-coupled-2023\n  title: Human MMAB supports FDX1-dependent\
    \ AdoCbl synthesis\n  scope: Gouda2023 recombinant human MMAB and individual R186Q/R190H/R190C/E193K\
    \ variants.\n  context: Anoxic25C BufferA:HEPES50mM pH7.5,KCl150mM,MgCl2 2mM,glycerol5%;\
    \ ATP1mM,Cbl40uM,FDXR4uM,NADPH500uM,variableFDX1;\n    WT MMAB1uM trimer and mutants1-5uM.\n\
    \  family_mapping: Human MMAB Q96EY8 sequence v1, 250 aa, PF01923 58-227. F170/R186/R190/E193\
    \ verified\n    in the reference. Exact assay-specific recombinant endpoints remain\
    \ unresolved; cited purification\n    methods include full-length and deltaN18\
    \ constructs with cleaved His tags. Reference mapping is not\n    proof of an\
    \ isolated-domain effect.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:9606\n\
    \  limitations: FDX1 lacks61N-terminal residues and retains His6; FDXR lacks4-33\
    \ and has a C-terminal tag.\n    Donor cofactor occupancies are partial. These\
    \ coupled rates do not identify the exclusive physiological\n    donor, elementary\
    \ electron-transfer rates or patient outcomes.\n  nodes:\n  - node_id: reaction\n\
    \    label: MMAB, MgATP, cob(II)alamin, FDX1, FDXR and NADPH\n    node_type: ACTIVITY\n\
    \    grounding:\n    - UniProtKB:Q96EY8\n  - node_id: product\n    label: AdoCbl\
    \ production\n    node_type: STATE\n  - node_id: no-fdx1\n    label: Omit FDX1\
    \ from the complete assay\n    node_type: PERTURBATION\n  - node_id: no-fdxr\n\
    \    label: Omit FDXR from the complete assay\n    node_type: PERTURBATION\n \
    \ - node_id: r186q\n    label: Replace WT MMAB with R186Q\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q96EY8\n  - node_id: r190h\n    label: Replace\
    \ WT MMAB with R190H\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q96EY8\n\
    \  - node_id: r190c\n    label: Replace WT MMAB with R190C\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q96EY8\n  - node_id: e193k\n    label: Replace\
    \ WT MMAB with E193K\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q96EY8\n\
    \  edges:\n  - edge_id: reaction-produces-product\n    subject: reaction\n   \
    \ predicate: produces\n    object: product\n    mechanism: The complete system\
    \ supports AdoCbl synthesis; WT kcat4.66+/-0.48/min and apparent FDX1\n      Km135+/-24nM.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:37526260\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10507449/\n\
    \      snippet: FDX1 supports NADPH-dependent AdoCbl synthesis by MMAB.\n    \
    \  explanation: Original Figure3A/C and supplementS2-S6.\n      cache_path: evidence/PF01923/gouda-2023.txt\n\
    \      cache_sha256: cbf3e47671a1f40f8c1ebfb7f6246f6d824a015b32d258864c8e84890d150bf3\n\
    \  - edge_id: no-fdx1-decreases-product\n    subject: no-fdx1\n    predicate:\
    \ decreases\n    object: product\n    mechanism: Product is not detected after\
    \ omission of the indicated electron-transfer component.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:37526260\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10507449/\n\
    \      snippet: FDX1 supports NADPH-dependent AdoCbl synthesis by MMAB.\n    \
    \  explanation: Main-text omission controls following Figure3 discussion.\n  \
    \    cache_path: evidence/PF01923/gouda-2023.txt\n      cache_sha256: cbf3e47671a1f40f8c1ebfb7f6246f6d824a015b32d258864c8e84890d150bf3\n\
    \  - edge_id: no-fdxr-decreases-product\n    subject: no-fdxr\n    predicate:\
    \ decreases\n    object: product\n    mechanism: Product is not detected after\
    \ omission of the indicated electron-transfer component.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:37526260\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10507449/\n\
    \      snippet: FDX1 supports NADPH-dependent AdoCbl synthesis by MMAB.\n    \
    \  explanation: Main-text omission controls following Figure3 discussion.\n  \
    \    cache_path: evidence/PF01923/gouda-2023.txt\n      cache_sha256: cbf3e47671a1f40f8c1ebfb7f6246f6d824a015b32d258864c8e84890d150bf3\n\
    \  - edge_id: r186q-decreases-product\n    subject: r186q\n    predicate: decreases\n\
    \    object: product\n    mechanism: AdoCbl formation is not detectable in the\
    \ coupled assay.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:37526260\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC10507449/\n      snippet: FDX1 supports\
    \ NADPH-dependent AdoCbl synthesis by MMAB.\n      explanation: Original Figure3C;\
    \ lower rates retain assay-specific interpretation.\n      cache_path: evidence/PF01923/gouda-2023.txt\n\
    \      cache_sha256: cbf3e47671a1f40f8c1ebfb7f6246f6d824a015b32d258864c8e84890d150bf3\n\
    \  - edge_id: r190h-decreases-product\n    subject: r190h\n    predicate: decreases\n\
    \    object: product\n    mechanism: kcat0.02+/-0.01/min versus WT4.66+/-0.48/min.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:37526260\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10507449/\n\
    \      snippet: FDX1 supports NADPH-dependent AdoCbl synthesis by MMAB.\n    \
    \  explanation: Original Figure3C; lower rates retain assay-specific interpretation.\n\
    \      cache_path: evidence/PF01923/gouda-2023.txt\n      cache_sha256: cbf3e47671a1f40f8c1ebfb7f6246f6d824a015b32d258864c8e84890d150bf3\n\
    \  - edge_id: r190c-decreases-product\n    subject: r190c\n    predicate: decreases\n\
    \    object: product\n    mechanism: kcat0.03+/-0.02/min versus WT4.66+/-0.48/min.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:37526260\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10507449/\n\
    \      snippet: FDX1 supports NADPH-dependent AdoCbl synthesis by MMAB.\n    \
    \  explanation: Original Figure3C; lower rates retain assay-specific interpretation.\n\
    \      cache_path: evidence/PF01923/gouda-2023.txt\n      cache_sha256: cbf3e47671a1f40f8c1ebfb7f6246f6d824a015b32d258864c8e84890d150bf3\n\
    \  - edge_id: e193k-decreases-product\n    subject: e193k\n    predicate: decreases\n\
    \    object: product\n    mechanism: AdoCbl formation is not detectable in the\
    \ coupled assay.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:37526260\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC10507449/\n      snippet: FDX1 supports\
    \ NADPH-dependent AdoCbl synthesis by MMAB.\n      explanation: Original Figure3C;\
    \ lower rates retain assay-specific interpretation.\n      cache_path: evidence/PF01923/gouda-2023.txt\n\
    \      cache_sha256: cbf3e47671a1f40f8c1ebfb7f6246f6d824a015b32d258864c8e84890d150bf3\n\
    - graph_id: mmab-corrinoid-coordination-2023\n  title: MMAB complexes contain\
    \ four-coordinate cob(II)alamin\n  scope: Gouda2023 separately prepared WT and\
    \ R190H human MMAB complexes.\n  context: 'EPR: WT100uM trimer/Cbl100uM/ATP5mM\
    \ or R190H1mM/Cbl250uM/ATP20mM, HEPES50mM pH7.5,KCl150mM,Mg2mM,TCEP2mM,glycerol15%;\n\
    \    samples frozen and measured80K.'\n  family_mapping: Human MMAB Q96EY8 sequence\
    \ v1, 250 aa, PF01923 58-227. F170/R186/R190/E193 verified\n    in the reference.\
    \ Exact assay-specific recombinant endpoints remain unresolved; cited purification\n\
    \    methods include full-length and deltaN18 constructs with cleaved His tags.\
    \ Reference mapping is not\n    proof of an isolated-domain effect.\n  scope_status:\
    \ MECHANISTIC\n  taxon: NCBITaxon:9606\n  limitations: Different concentrations\
    \ and ATP are used here, not the ADP redox-titration mixture. EPR\n    and spectra\
    \ report coordination state, not an experimentally observed F170 displacement\
    \ trajectory\n    or an isolated-domain effect.\n  nodes:\n  - node_id: wt\n \
    \   label: Prepare WT MMAB with ATP and cob(II)alamin\n    node_type: ACTIVITY\n\
    \    grounding:\n    - UniProtKB:Q96EY8\n  - node_id: r190h\n    label: Prepare\
    \ R190H MMAB with ATP and cob(II)alamin\n    node_type: ACTIVITY\n    grounding:\n\
    \    - UniProtKB:Q96EY8\n  - node_id: four\n    label: Four-coordinate enzyme-bound\
    \ corrinoid state\n    node_type: STATE\n    grounding:\n    - UniProtKB:Q96EY8\n\
    \  edges:\n  - edge_id: wt-produces-four\n    subject: wt\n    predicate: produces\n\
    \    object: four\n    mechanism: The prepared complex has the EPR signature assigned\
    \ to four-coordinate cob(II)alamin, distinct\n      from the water-liganded control.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:37526260\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10507449/\n\
    \      snippet: 4-c state\n      explanation: Main Figure2B and supplementMethodsS5/FigureS2.\n\
    \      cache_path: evidence/PF01923/gouda-2023.txt\n      cache_sha256: cbf3e47671a1f40f8c1ebfb7f6246f6d824a015b32d258864c8e84890d150bf3\n\
    \  - edge_id: r190h-produces-four\n    subject: r190h\n    predicate: produces\n\
    \    object: four\n    mechanism: The prepared complex has the EPR signature assigned\
    \ to four-coordinate cob(II)alamin, distinct\n      from the water-liganded control.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:37526260\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10507449/\n\
    \      snippet: 4-c state\n      explanation: Main Figure2B and supplementMethodsS5/FigureS2.\n\
    \      cache_path: evidence/PF01923/gouda-2023.txt\n      cache_sha256: cbf3e47671a1f40f8c1ebfb7f6246f6d824a015b32d258864c8e84890d150bf3\n\
    - graph_id: mmab-r190h-redox-2023\n  title: Reduced donors generate cob(I)alamin\
    \ in R190H complexes\n  scope: Gouda2023 R190H-bound corrinoid, not a direct WT\
    \ redox-potential measurement.\n  context: Anoxic25C BufferA; R190H600uM,Cbl40uM,ADP5mM.\
    \ Ti(III)citrate200uM gives reference spectra;\n    reduced benzyl viologen is\
    \ titrated in separate reactions.\n  family_mapping: Human MMAB Q96EY8 sequence\
    \ v1, 250 aa, PF01923 58-227. F170/R186/R190/E193 verified\n    in the reference.\
    \ Exact assay-specific recombinant endpoints remain unresolved; cited purification\n\
    \    methods include full-length and deltaN18 constructs with cleaved His tags.\
    \ Reference mapping is not\n    proof of an isolated-domain effect.\n  scope_status:\
    \ MECHANISTIC\n  taxon: NCBITaxon:9606\n  limitations: Main Figure2C caption says\
    \ ATP; supplementS4 explicitly specifies ADP twice and governs\n    this context.\
    \ No AdoCbl detected by post-titration HPLC. The measured potential cannot be\
    \ silently\n    assigned to all WT/family proteins.\n  nodes:\n  - node_id: ti\n\
    \    label: Add Ti(III)citrate to the R190H-ADP corrinoid complex\n    node_type:\
    \ PERTURBATION\n  - node_id: bv\n    label: Titrate reduced benzyl viologen into\
    \ that complex\n    node_type: PERTURBATION\n  - node_id: cobi\n    label: Enzyme-bound\
    \ cob(I)alamin accumulation\n    node_type: STATE\n    grounding:\n    - UniProtKB:Q96EY8\n\
    \  edges:\n  - edge_id: ti-produces-cobi\n    subject: ti\n    predicate: produces\n\
    \    object: cobi\n    mechanism: The spectrum shifts from the cob(II) complex\
    \ to the reference cob(I)alamin spectrum.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:37526260\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10507449/\n      snippet:\
    \ cob(I)alamin accumulation is observed\n      explanation: Original Figure2A\
    \ and supplementS4 reference-spectrum Methods.\n      cache_path: evidence/PF01923/gouda-2023.txt\n\
    \      cache_sha256: cbf3e47671a1f40f8c1ebfb7f6246f6d824a015b32d258864c8e84890d150bf3\n\
    \  - edge_id: bv-produces-cobi\n    subject: bv\n    predicate: produces\n   \
    \ object: cobi\n    mechanism: Redox titration populates cob(I)alamin; the Nernst\
    \ analysis yields -325+/-9mV for this\n      prepared R190H complex.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:37526260\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10507449/\n\
    \      snippet: cob(I)alamin accumulation is observed\n      explanation: Original\
    \ Figure2C/D and supplementS4-S5/S4 HPLC control.\n      cache_path: evidence/PF01923/gouda-2023.txt\n\
    \      cache_sha256: cbf3e47671a1f40f8c1ebfb7f6246f6d824a015b32d258864c8e84890d150bf3\n\
    curation_events:\n- timestamp: '2026-10-12T01:50:22Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate scoped PduO, EutT and MMAB causal\
    \ assay graphs for PF01923\n  history_record: history/records/PF01923/2026-10-12T015022Z-codex-3c429b.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-12T01:56:58Z'\n\
    \  curator: Codex\n  action: REVIEW\n  outcome: needs_followup\n  summary: Retain\
    \ partial scientific review of PF01923 causal assay graphs\n  history_record:\
    \ history/records/PF01923/2026-10-12T015658Z-codex-194a79.yaml\n  event_index:\
    \ 0\n  llm_assisted: true\n- timestamp: '2026-10-18T02:54:46Z'\n  curator: Antigravity\n\
    \  action: EDIT\n  outcome: changed\n  summary: Ground causal graph gene and protein\
    \ nodes in PF01923 with verified UniProtKB accessions (UniProtKB:Q8ZNR5,\n   \
    \ UniProtKB:Q50EJ2, UniProtKB:Q9ZFV4, UniProtKB:A0A0H3GFM5, UniProtKB:Q96EY8)\n\
    \  history_record: history/records/PF01923/2026-10-18T025446Z-antigravity-1ae74e.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Frozen PF01923/Cob_adeno_trans/IPR016030/EX_DUF and historical DUF80 identity
    are unchanged. Q8ZNR5v1 maps3-166, Q9ZFV4v1 maps92-246, Q50EJ2v1 maps3-169, Q96EY8v1
    maps58-227, A0A0H3GFM5v1 maps83-242. Listeria10403S mapping is supported by strain-specific
    reference, primary alignment and terminal primers, not presumed EGD-e identity.
    SeEutT H67/C79/C80/C83 and LrPduO F187/tail183-188 lie outside PF01923. Modern
    reference mapping is distinguished from historical recombinant construct verification.
  target_ids:
  - PF01923
  evidence_ids:
  - identity
  - primary
  - johnson-2001
  - johnson-2004
  - stmaurice-2007
  - mera-2009
  - mera-2010
  - moore-2014
  - costa-2018
  - coverage
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Joint assay inputs make cofactors, substrates and reducing systems explicit.
    SePduO reaction/product, truncation, metal/inhibitor and growth contexts are separate.
    LrPduO crystal coordination, pre-reduced and reduction-coupled kinetics, and text-only
    complementation remain separate. SeEutT whole-protein motif effects are not assigned
    to the mapped Pfam interval. LmEutT cob(I)inamide acceptance is not contradicted
    by cob(II)inamide negatives; metal-less wording does not remove MgATP. Human FDX1
    synthesis, ATP-EPR complexes and ADP-R190H titrations preserve distinct conditions.
    No direct product-release pathway, native exclusive electron donor, patient-outcome
    arrow or family-wide catalytic sufficiency is invented.
  target_ids:
  - PF01923
  evidence_ids:
  - primary
  - native
  - johnson-2001
  - johnson-2004
  - stmaurice-2007
  - mera-2009
  - mera-2010
  - moore-2014
  - costa-2018
  - coverage
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Eight primary full-text studies plus Costa/Gouda publisher supplements
    support selected experiments, not every15667 frozen protein or every published
    context. MMAB product transfer/sequestration/repair/allostery, other EutT coordination
    and product studies, Lm2020 mutations, further species and exact historical constructs
    remain open. Moore2014 original supplement is inaccessible through attempted endpoints;
    described controls are text-only. StMaurice2008 is a structural/mapping lead,
    and Gouda2021 was inspected for purification only.
  target_ids:
  - PF01923
  evidence_ids:
  - primary
- assessment_id: stage4-grounding-and-taxon-audit
  area: representation
  topic: Causal-graph taxon and protein-node grounding consistency
  outcome: concern
  summary: 'In curation/families/PF01923.yaml, three causal graphs have zero grounded
    protein nodes even though family_mapping explicitly maps the tested enzyme to
    a verified Salmonella enterica LT2 (NCBITaxon:99287) UniProtKB accession in evidence/PF01923/identity.txt:
    sepduo-inhibition-2004 (activity: AdoCbl-forming activity, lines 335-337) and
    sepduo-metal-additions-2004 (activity: AdoCbl-forming activity, lines 420-422)
    omit grounding: [UniProtKB:Q8ZNR5] (S. enterica LT2 PduO STM2050, UniProtKB:Q8ZNR5),
    whereas sibling graphs sepduo-truncation-activity-2004 and sepduo-triphosphate-2004
    ground PduO activity to UniProtKB:Q8ZNR5; and seeutt-metal-oxygen-2014 (activity:
    Coupled AdoCbl-forming activity, lines 1207-1209) omits grounding: [UniProtKB:Q9ZFV4]
    (S. enterica LT2 EutT STM2456, UniProtKB:Q9ZFV4), whereas sibling graph seeutt-variant-activity-2014
    grounds EutT perturbations to UniProtKB:Q9ZFV4.'
  target_ids:
  - PF01923
  evidence_ids:
  - stage4-prior-review
findings:
- finding_id: additional-contexts
  issue_key: pf01923-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve construct and source discrepancies and extend uncurated ACAT contexts
  description: Resolve historical PduO/EutT/MMAB constructs and the retained unit/label
    discrepancies, inspect Moore2014 supplemental controls and remaining mutant/spectroscopy
    studies, and curate directly evidenced MMAB cofactor-transfer, sequestration and
    repair pathways with exact species/partner scope. Inspect other experimentally
    mapped members; do not infer absent function from unperformed searches or promote
    to REVIEWED because graph integrity passes.
  target_ids:
  - PF01923
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - johnson-2001
  - johnson-2004
  - stmaurice-2007
  - mera-2009
  - mera-2010
  - moore-2014
  - costa-2018
  - coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01923.yaml
    role: Human-owned scientific overlay
  previous_occurrences:
  - repository: CultureBotAI/DUFMech
    review_id: 20261012T015942Z-pf01923-pduo-eutt-mmab-assay-and-domain-contexts
    finding_id: additional-contexts
- finding_id: sepduo-and-seeutt-assays-missing-protein-grounding
  issue_key: pf01923-sepduo-and-seeutt-assays-missing-protein-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground Salmonella enterica PduO and EutT AdoCbl-forming activity nodes in
    sepduo-inhibition-2004, sepduo-metal-additions-2004, and seeutt-metal-oxygen-2014
  description: 'In curation/families/PF01923.yaml, three causal graphs have zero grounded
    protein nodes even though family_mapping explicitly maps the tested enzyme to
    a verified Salmonella enterica LT2 (NCBITaxon:99287) UniProtKB accession in evidence/PF01923/identity.txt:
    sepduo-inhibition-2004 (activity: AdoCbl-forming activity, lines 335-337) and
    sepduo-metal-additions-2004 (activity: AdoCbl-forming activity, lines 420-422)
    omit grounding: [UniProtKB:Q8ZNR5] (S. enterica LT2 PduO STM2050, UniProtKB:Q8ZNR5),
    whereas sibling graphs sepduo-truncation-activity-2004 and sepduo-triphosphate-2004
    ground PduO activity to UniProtKB:Q8ZNR5; and seeutt-metal-oxygen-2014 (activity:
    Coupled AdoCbl-forming activity, lines 1207-1209) omits grounding: [UniProtKB:Q9ZFV4]
    (S. enterica LT2 EutT STM2456, UniProtKB:Q9ZFV4), whereas sibling graph seeutt-variant-activity-2014
    grounds EutT perturbations to UniProtKB:Q9ZFV4.'
  target_ids:
  - PF01923
  field_paths:
  - causal_graphs
  evidence_ids:
  - stage4-prior-review
  - identity
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01923.yaml
    role: Maintained scientific overlay; update in Stage 5 grouped remediation and
      regenerate projection.
actions:
- action_id: extend-contexts
  description: Resolve historical PduO/EutT/MMAB constructs and the retained unit/label
    discrepancies, inspect Moore2014 supplemental controls and remaining mutant/spectroscopy
    studies, and curate directly evidenced MMAB cofactor-transfer, sequestration and
    repair pathways with exact species/partner scope. Inspect other experimentally
    mapped members; do not infer absent function from unperformed searches or promote
    to REVIEWED because graph integrity passes.
  finding_ids:
  - additional-contexts
  - sepduo-and-seeutt-assays-missing-protein-grounding
  target_ids:
  - PF01923
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Original Johnson2001 Figures2/3/5; Johnson2004 Figures2-4; StMaurice2007 Figure1;
  Mera2009 Figures1-4; Mera2010 Figures2-4; Moore2014 Figures2/3/5; Costa2018 Figures2-7
  and supplementS2/S3/S5/S6; Gouda2023 Figures1-3 and supplementS1-S4 were visually
  inspected. Relevant Methods/tables and supplement primers were read. No raw-data
  replication or independent expert endorsement; later renderer and full-corpus checks
  are reported separately.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
