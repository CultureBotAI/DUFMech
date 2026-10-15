# PF01978 TrmB promoter-specific repression and sugar-response evidence

- Review: 20261015T141642Z-pf01978-trmb-causal-evidence
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-15T14:13:22Z
- Finished UTC: 2026-10-15T14:16:42Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Eleven scoped graphs retain 25 observed effects and one hypothesized TBP-occlusion step. Whole-protein repression, sugar response and promoter-selective mutant phenotypes are distinguished from PF01978 sufficiency or direct residue contacts. Three open findings retain construct/deposition discrepancies, assay confounds and unfinished member/promoter coverage. PF01978 remains IN_PROGRESS; this partial review does not complete the 8296-family goal.

## Scope And Provenance

Review all new PF01978 graphs and discussions against Lee2003 primary text/captions, Surma thesis methods and original Figures 45-48/51, Krug2013 structure/construct reports, 3QPH deposition and complete UniProt/InterPro reference responses.

Selection: Continue the sequential family queue after PF01977, using experimentally tested TrmB preparations rather than family-name transfer.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1681f523e90533997fbdc3c42612b66b321ea3e8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01978 | data/families/PF01978.yaml | generated | PF01978 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Baseline and guarded projection | passed | True | PF01978 | Baseline has 8296 schema-valid records with zero drift. Preview and apply change only PF01978 and its manifest after the actual CREATE event. |
| Evidence and corpus preservation | passed | True | PF01978 | All 8296 manifest hashes and 26 edge cache hashes/quotations pass. Imported fields and other tracked families, evidence, reviews/history, snapshots, code and canonical Pages/pins are preserved. Only PF01978 status changes in KGX/SSSOM exports. |
| Exact reference and deposited-residue checks | passed | True | PF01978 | Complete Q7LYW4/Q9HGZ9 bodies are identical; both complete Pfam responses map 11-77/110-234/249-335. Y50/E87 locations and 3QPH actual Val161 atoms verify. This confirms a paper/deposition discrepancy, not full assay construct identity. |
| Thesis quotation occurrence | passed | True | PF01978 | All six retained short thesis quotations occur in primary PDF text after whitespace normalization; the no-dialysis quotation crosses a PDF line break. Original adopted figures were visually inspected. |
| Schema reproduction | passed | True | PF01978 | Zero generated schema differences. |
| Graph and QC regression tests | passed | True | PF01978 | All 52 tests pass in 17.05 seconds. An initial invocation without the shared CLAW dependency setting had 51 passes and one environment-related failure; corrected invocation passed without repository code changes. |
| Structural inventory and status exports | passed | True | PF01978 | All 8296 inventory rows refreshed, only PF01978 changed. Corpus now has 845 graphs and 1824 edges across 128 graph-bearing families, with 8168 graphless. Exports reproduce and differ only by PF01978 SEEDED-to-IN_PROGRESS status. |
| Native unpinned preview and responsive disclosures | passed | True | PF01978 | At 1440px and 390px, 11 graphs/26 edges, 25 observed/one hypothesized labels, 26 source links, three OPEN discussions and working disclosures; no document overflow or JavaScript errors. Selected screenshots visually inspected. Native horizontal table scrolling is retained. Browser/server closed. |
| Canonical source-pin currentness | failed | False | PF01978 | Source-pin bytes differ for data/families/PF01978.yaml. No source checkpoint, fabricated pin, canonical render or publication performed. This release step is outside the local curation scope. |

## Scientific And Domain Assessments

### Tested proteins versus family and domain

identity: supported. Targets: PF01978.

The transcription regulator is distinguished from unrelated TrmB methyltransferases. Whole-protein effects, PF01978 Y50, extra-domain E87 and separate sugar-binding matches remain explicit. Unknown constructs and conflicting species attribution are not replaced by reference assumptions.

### Direction, mechanism and uncertainty

graph: supported. Targets: PF01978.

Twenty-five observed effect entries retain their actual assay and comparison; reused Figure 46 comparisons are not independent experiments. The single TBP-occlusion edge is explicitly hypothesized. Mutant and composite-template molecular routes remain unresolved; no atomic-contact, native-flux or isolated-domain claim is added.

### Contradictory outcomes and preparation limitations

evidence: supported. Targets: PF01978.

Trehalose EMSA/transcription differences, residual mutant repression, glucose-containing stock without dialysis, matched versus unequal DNaseI comparisons, diffuse MD shifts, Figure 51 MD enhancement and paper/deposition sequence differences are retained. No statistical significance or exact affinity is invented.

### Native ownership and reproducibility

provenance: supported. Targets: PF01978.

Minimal quotations and factual summaries retain raw-source hashes/locators without redistributing full sources. Actual CREATE history precedes guarded projection; other records and imported fields are unchanged. Scientific review and release remain independent gates.

### Incomplete family and corpus assessment

completeness: concern. Targets: PF01978.

Remaining promoter, anti-inducer and paralog/taxon experiments, full constructs, raw controls and molecular mechanisms are not finished. IN_PROGRESS and the original 8296-family scope are preserved.

## Findings

### construct-and-domain-boundaries: Resolve full constructs and domain-specific attribution

minor / open / confirmed; issue key: pf01978-construct-and-domain-boundaries.

pSL152 species attribution differs across primary sources despite identical reference bodies. E87 is outside PF01978. Krug2013 V161A and C-tail descriptions conflict with 3QPH. These disclosed gaps limit, but do not invalidate, the scoped endpoint observations; no full insert or isolated-domain mechanism is claimed.

### assay-context-and-residual-activity: Resolve carryover and assay-specific molecular interpretations

minor / open / confirmed; issue key: pf01978-assay-context-and-residual-activity.

Obtain full stock compositions and glucose/imidazole carryover, mutant active fractions, matched-nuclease comparisons, replicate statistics and direct DNA/TBP occupancy measurements. Retain opposite trehalose readouts, residual Y50N/E87A activity and composite-template nonmonotonic/enhanced output; these cannot be flattened into a universal regulatory mechanism.

### family-and-promoter-coverage: Continue remaining promoter, paralog and taxon evidence

minor / open / confirmed; issue key: pf01978-family-and-promoter-coverage.

Inspect full Lee2005 and differential-signals Lee2007, remaining thesis anti-inducer/promoter-engineering/cross-promoter data, and separately mapped TrmBL1/2/4, Tgr and other taxa. Do not equate graph presence or an EX_DUF name with family completion; all 8296 records remain in scope.

## Recommended Actions And Acceptance Checks

### extend-exact-member-assessment

Continue the three open findings with primary construct, assay and member evidence; retain current scoped effects without increasing their evidential strength by inference.

- Verify exact constructs and current Pfam intervals before assigning domain/residue effects; retain source disagreements until primary sequence evidence resolves them.
- Assess each new perturbation, measured outcome, control, preparation and promoter independently; distinguish phenotype from direct molecular mechanism.
- Resolve carryover, residual activity and raw comparison limits without treating different assays or taxa as interchangeable.
- Preserve stable finding IDs, actual history, validated projection and full family/corpus scope in successor reviews.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | evidence/PF01978/trmb-primary-assays.txt; Identity section; exact Q7LYW4/Q9HGZ9 and complete InterPro response hashes | supports | PF01978 11-77 is not the complete structural DNA-binding/coiled-coil region or sugar-binding region. Reference identity does not establish pSL152 provenance or its full insert. E87 and the major sugar contacts are outside PF01978. |
| lee | https://doi.org/10.1074/jbc.M210236200; Primary text/captions on the ResearchGate article page; Figures 4/6/8, Methods and Discussion; ledger S1 | supports | Reconstituted transcription, EMSA and footprint results retain distinct protocols and opposite trehalose readouts. TBP obstruction is an interpretation, not a directly measured recruitment step. No original figure image inspection is claimed. |
| thesis | https://doi.org/10.5283/epub.14529; Methods printed pp.31/33/38-42/51-53; Results pp.105-115; original Figures 45-48/51; ledger S2 | supports | Original gel images and numeric tables support scoped promoter-specific endpoints, residual repression and composite-template enhancement. Preparation glucose, omitted dialysis, unequal nuclease lanes, diffuse shifts and nonmonotonic values limit molecular interpretations. Thesis publication is 2011; preparation/examination was 2010. |
| structure | https://doi.org/10.1002/pro.2263; Krug2013 Results/Methods/Figures, institutional PDF; RCSB 3QPH entity and atom_site residue 161; ledger S3 | supports | Sucrose complex lacks DNA and maltose comparator lacks residues 2-109. V161A text and Ala161 figure conflict with deposited Val161 atoms; C-tail descriptions differ. This cannot establish a tested atomic trajectory or resolve the full constructs. |
| native | src/dufmech/records.py; Executed baseline/generation, integrity script, schema, focused tests, inventory/exports and native browser preview | supports | Native representation and preservation checks pass separately from scientific completeness. Final save, actual REVIEW event, audit-index regeneration and full native validation follow this retained assessment. |
| search | evidence/PF01978/trmb-primary-assays.txt; Scoped ignored-inclusive repository search and public primary-source access assessment | context_only | Before curation, only docs queue/publication mentions were found in that scoped search; ignored/hidden files were included. No global absence claim is made. Public access failures and uninspected sources remain coverage limitations. |
| duf-projection-pf01978 | data/families/PF01978.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Partial scientific self-review, not independent expert approval, experimental replication or complete family/corpus assessment.
- Lee2003 original figure images were unavailable through attempted routes; primary text and captions were inspected. Only the named thesis original figures were visually assessed; remaining thesis results are not certified.
- Full assay inserts, exact strains, mutant-specific folding/active fractions, final buffer carryover and replicate statistics remain unverified. Reference identity and general sequencing methods do not close those gaps.
- The first focused test invocation omitted the pinned shared dependency configuration; rerun passed. The first scratch browser check incorrectly expected values inside collapsed disclosures in visible text; explicit expansion and content checks then passed. No scientific content was changed to satisfy either check.
- Canonical Pages/pins and full release QC remain unperformed publication work. Source-pin currentness fails for the changed projection; the local preview is explicitly unpinned.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T141642Z-pf01978-trmb-causal-evidence
kind: record
repository: CultureBotAI/DUFMech
source:
  git_revision: 1681f523e90533997fbdc3c42612b66b321ea3e8
  inputs:
  - path: curation/families/PF01978.yaml
    role: context
    sha256: 55ad6312a9b6c6a0d3b7806840b1d5101e5615abbc197e8b1ebcf06b1ad3af4c
  - path: data/families/PF01978.yaml
    role: target
    sha256: a4f6c35feeaddb6dac032713168e97de3ebc89efce6c7fba990cd37634b5476e
  - path: data/worklists/interpro-pfam-duf-2026-10-10.json
    role: context
    sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383
  - path: data/worklists/interpro-pfam-duf-2026-10-10.manifest.json
    role: context
    sha256: 31c07ffb6a169c851ea0e6e9dd527a10c04028eafeb29187bd62dc2ae848696e
  - path: data/worklists/interpro-pfam-duf-2026-10-10.tsv
    role: context
    sha256: be023c8dd9d8d3864926b5032d6f7e87a884b1a567391696822dbbecc692dae7
  - path: evidence/PF01978/trmb-primary-assays.txt
    role: context
    sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62
  - path: history/records/PF01978/2026-10-15T140002Z-codex-211131.yaml
    role: context
    sha256: 4a5c6639ed25fb8a17448fc986af5761ee751d99af91ff821ea5792f19dbedd8
  snapshot_id: interpro-pfam-duf-2026-10-10
  state: working_tree
targets:
- kind: generated
  label: PF01978
  owner_paths:
  - path: curation/families/PF01978.yaml
    repository: CultureBotAI/DUFMech
    role: Maintained scientific overlay; create only with authorized curation.
  - path: src/dufmech/records.py
    repository: CultureBotAI/DUFMech
    role: Projection generator; frozen snapshot identity is not hand-edited.
  path: data/families/PF01978.yaml
  record_class: FamilyRecord
  semantic_digest:
    algorithm: dufmech-record-content-v1
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
    sha256: 9f0d9472055392c3286704593c2427b244f1c94dc46f98d1c6038e443e72cb07
  target_id: PF01978
title: PF01978 TrmB promoter-specific repression and sugar-response evidence
started_at: '2026-10-15T14:13:22Z'
finished_at: '2026-10-15T14:16:42Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent researched, curated and challenged the claims; no
    independent expert approval or experimental replication.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: NEEDS_FOLLOWUP
scientific_review: true
summary: Eleven scoped graphs retain 25 observed effects and one hypothesized TBP-occlusion
  step. Whole-protein repression, sugar response and promoter-selective mutant phenotypes
  are distinguished from PF01978 sufficiency or direct residue contacts. Three open
  findings retain construct/deposition discrepancies, assay confounds and unfinished
  member/promoter coverage. PF01978 remains IN_PROGRESS; this partial review does
  not complete the 8296-family goal.
scope:
  description: Review all new PF01978 graphs and discussions against Lee2003 primary
    text/captions, Surma thesis methods and original Figures 45-48/51, Krug2013 structure/construct
    reports, 3QPH deposition and complete UniProt/InterPro reference responses.
  selection: Continue the sequential family queue after PF01977, using experimentally
    tested TrmB preparations rather than family-name transfer.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01978
  exclusions:
  - target: Remaining PF01978 members and regulatory contexts
    reason: Anti-inducer, promoter-engineering, cross-promoter, TrmBL1/2/4, Tgr and
      other-taxon experiments need separate primary assessment and reference mapping.
  - target: Original Lee2003 figure images, complete constructs and raw replicated
      measurements
    reason: Readable primary text/captions were available but publisher/ResearchGate
      PDF and image access failed. Complete inserts, mutant folding/active fractions
      and raw replicate statistics were not verified.
  - target: Canonical Pages publication and full release QC
    reason: Only an unpinned local preview is checked. Source pins fail for the changed
      projection; canonical Pages and pins remain unchanged, with no new publication
      authorization.
checks:
- check_id: native-generation
  name: Baseline and guarded projection
  command: just records-check; just records; just records --apply
  status: passed
  required: true
  exit_code: 0
  summary: Baseline has 8296 schema-valid records with zero drift. Preview and apply
    change only PF01978 and its manifest after the actual CREATE event.
  target_ids:
  - PF01978
  evidence_ids:
  - native
- check_id: integrity
  name: Evidence and corpus preservation
  command: uv run --locked --offline python /private/tmp/duf-pf01978-integrity.py
    --inventory
  status: passed
  required: true
  exit_code: 0
  summary: All 8296 manifest hashes and 26 edge cache hashes/quotations pass. Imported
    fields and other tracked families, evidence, reviews/history, snapshots, code
    and canonical Pages/pins are preserved. Only PF01978 status changes in KGX/SSSOM
    exports.
  target_ids:
  - PF01978
  evidence_ids:
  - native
- check_id: mapping
  name: Exact reference and deposited-residue checks
  command: Structured JSON checks and Biopython MMCIF2Dict inspection of retained
    public API/CIF responses
  status: passed
  required: true
  exit_code: 0
  summary: Complete Q7LYW4/Q9HGZ9 bodies are identical; both complete Pfam responses
    map 11-77/110-234/249-335. Y50/E87 locations and 3QPH actual Val161 atoms verify.
    This confirms a paper/deposition discrepancy, not full assay construct identity.
  target_ids:
  - PF01978
  evidence_ids:
  - identity
  - structure
- check_id: primary-quotations
  name: Thesis quotation occurrence
  command: PyMuPDF extraction and whitespace-normalized quotation comparison
  status: passed
  required: true
  exit_code: 0
  summary: All six retained short thesis quotations occur in primary PDF text after
    whitespace normalization; the no-dialysis quotation crosses a PDF line break.
    Original adopted figures were visually inspected.
  target_ids:
  - PF01978
  evidence_ids:
  - thesis
- check_id: schema
  name: Schema reproduction
  command: just validate-schema
  status: passed
  required: true
  exit_code: 0
  summary: Zero generated schema differences.
  target_ids:
  - PF01978
  evidence_ids:
  - native
- check_id: focused-tests
  name: Graph and QC regression tests
  command: env CLAW_ROOT=/private/tmp/duf-pr220-claw CLAW_SRC=/private/tmp/duf-pr220-claw/src
    PYTHONPATH=src:/private/tmp/duf-pr220-claw/src uv run --locked --offline --extra
    dev pytest -q tests/test_causal_graphs.py tests/test_qc.py
  status: passed
  required: true
  exit_code: 0
  summary: All 52 tests pass in 17.05 seconds. An initial invocation without the shared
    CLAW dependency setting had 51 passes and one environment-related failure; corrected
    invocation passed without repository code changes.
  target_ids:
  - PF01978
  evidence_ids:
  - native
- check_id: inventory-exports
  name: Structural inventory and status exports
  command: just causal-graphs --apply; just exports --apply; just exports --check
  status: passed
  required: true
  exit_code: 0
  summary: All 8296 inventory rows refreshed, only PF01978 changed. Corpus now has
    845 graphs and 1824 edges across 128 graph-bearing families, with 8168 graphless.
    Exports reproduce and differ only by PF01978 SEEDED-to-IN_PROGRESS status.
  target_ids:
  - PF01978
  evidence_ids:
  - native
- check_id: preview
  name: Native unpinned preview and responsive disclosures
  command: uv run --locked --offline python /private/tmp/duf-pf01978-preview.py; node
    /private/tmp/duf-pf01978-browser.cjs
  status: passed
  required: true
  exit_code: 0
  summary: At 1440px and 390px, 11 graphs/26 edges, 25 observed/one hypothesized labels,
    26 source links, three OPEN discussions and working disclosures; no document overflow
    or JavaScript errors. Selected screenshots visually inspected. Native horizontal
    table scrolling is retained. Browser/server closed.
  target_ids:
  - PF01978
  evidence_ids:
  - native
- check_id: publication
  name: Canonical source-pin currentness
  command: uv run --locked --offline python -m dufmech.site_sources check
  status: failed
  required: false
  exit_code: 1
  summary: Source-pin bytes differ for data/families/PF01978.yaml. No source checkpoint,
    fabricated pin, canonical render or publication performed. This release step is
    outside the local curation scope.
  target_ids:
  - PF01978
  evidence_ids:
  - native
evidence:
- evidence_id: identity
  kind: database
  reference: evidence/PF01978/trmb-primary-assays.txt
  locator: Identity section; exact Q7LYW4/Q9HGZ9 and complete InterPro response hashes
  accessed_at: '2026-10-15T14:16:42Z'
  support: supports
  summary: PF01978 11-77 is not the complete structural DNA-binding/coiled-coil region
    or sugar-binding region. Reference identity does not establish pSL152 provenance
    or its full insert. E87 and the major sugar contacts are outside PF01978.
- evidence_id: lee
  kind: primary_source
  reference: https://doi.org/10.1074/jbc.M210236200
  locator: Primary text/captions on the ResearchGate article page; Figures 4/6/8,
    Methods and Discussion; ledger S1
  accessed_at: '2026-10-15T14:16:42Z'
  support: supports
  summary: Reconstituted transcription, EMSA and footprint results retain distinct
    protocols and opposite trehalose readouts. TBP obstruction is an interpretation,
    not a directly measured recruitment step. No original figure image inspection
    is claimed.
- evidence_id: thesis
  kind: primary_source
  reference: https://doi.org/10.5283/epub.14529
  locator: Methods printed pp.31/33/38-42/51-53; Results pp.105-115; original Figures
    45-48/51; ledger S2
  accessed_at: '2026-10-15T14:16:42Z'
  support: supports
  summary: Original gel images and numeric tables support scoped promoter-specific
    endpoints, residual repression and composite-template enhancement. Preparation
    glucose, omitted dialysis, unequal nuclease lanes, diffuse shifts and nonmonotonic
    values limit molecular interpretations. Thesis publication is 2011; preparation/examination
    was 2010.
- evidence_id: structure
  kind: primary_source
  reference: https://doi.org/10.1002/pro.2263
  locator: Krug2013 Results/Methods/Figures, institutional PDF; RCSB 3QPH entity and
    atom_site residue 161; ledger S3
  accessed_at: '2026-10-15T14:16:42Z'
  support: supports
  summary: Sucrose complex lacks DNA and maltose comparator lacks residues 2-109.
    V161A text and Ala161 figure conflict with deposited Val161 atoms; C-tail descriptions
    differ. This cannot establish a tested atomic trajectory or resolve the full constructs.
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Executed baseline/generation, integrity script, schema, focused tests,
    inventory/exports and native browser preview
  accessed_at: '2026-10-15T14:16:42Z'
  support: supports
  summary: Native representation and preservation checks pass separately from scientific
    completeness. Final save, actual REVIEW event, audit-index regeneration and full
    native validation follow this retained assessment.
- evidence_id: search
  kind: search
  reference: evidence/PF01978/trmb-primary-assays.txt
  locator: Scoped ignored-inclusive repository search and public primary-source access
    assessment
  accessed_at: '2026-10-15T14:16:42Z'
  support: context_only
  search_scope: rg --no-ignore --hidden for PF01978/TrmB/trmB in curation/families,
    evidence, reviews/structured, history/records and docs/causal-graphs.md before
    curation. Primary coverage is the named sources and references, not exhaustive
    family literature.
  summary: Before curation, only docs queue/publication mentions were found in that
    scoped search; ignored/hidden files were included. No global absence claim is
    made. Public access failures and uninspected sources remain coverage limitations.
- evidence_id: duf-projection-pf01978
  kind: record_content
  reference: data/families/PF01978.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-15T14:16:42Z'
  support: context_only
  snapshot_sha256: a4f6c35feeaddb6dac032713168e97de3ebc89efce6c7fba990cd37634b5476e
  quote: "id: Pfam:PF01978\npfam_id: PF01978\nname: Sugar-specific transcriptional\
    \ regulator TrmB\nshort_name: TrmB\nseed_status: EX_DUF\ncharacterization_status:\
    \ UNSCORED\ncuration_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01978\n\
    counters:\n  proteins: 8669\n  matches: 8670\n  proteomes: 3373\n  taxa: 5343\n\
    \  structures: 15\n  alphafold_models: 6625\n  domain_architectures: 86\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002831\ndescription: One member of this family, TrmB,\
    \ has been shown to be a sugar-specific transcriptional regulator\n  of the trehalose/maltose\
    \ ABC transporter [[cite:PUB00015607]] in Thermococcus litoralis.\ncuration_history:\
    \ history/records/PF01978\ndiscussions:\n- discussion_id: trmb-construct-and-domain-boundaries\n\
    \  prompt: Resolve complete constructs and distinguish PF01978-dependent effects\
    \ from other-domain and\n    whole-protein effects.\n  kind: CURATION_TODO\n \
    \ status: OPEN\n  rationale: Q7LYW4 and Q9HGZ9 have identical reference bodies\
    \ and PF01978 at 11-77, but the pSL152 species\n    attribution differs between\
    \ Lee2003 and the Surma thesis. Y50 is within PF01978; E87 and the sugar-binding\n\
    \    domains are not. Reference equivalence cannot establish identical experimental\
    \ inserts or strains.\n  evidence:\n  - reference: PMID:12426307\n    supports:\
    \ PARTIAL\n    evidence_source: primary_publication\n    explanation: The original\
    \ cloning methods identify T. litoralis chromosomal DNA and C-terminal His6\n\
    \      pSL152; full inserted sequence was not independently inspected.\n  - reference:\
    \ doi:10.5283/epub.14529\n    supports: PARTIAL\n    evidence_source: doctoral_thesis\n\
    \    explanation: Methods calls the same plasmid PF1743 and Chapter 7 uses supplied\
    \ mutant plasmids; complete\n      inserts and mutant-specific folding controls\
    \ remain unresolved.\n  - reference: PMID:23576322\n    supports: PARTIAL\n  \
    \  evidence_source: primary_publication_and_deposition\n    explanation: Reported\
    \ V161A and inconsistent C-terminal tails disagree with the 3QPH sequence and\n\
    \      actual Val161 atoms. No silent sequence correction or neutrality assumption\
    \ is made.\n  posed_by: Codex\n  posed_date: '2026-10-15'\n  notes: See evidence/PF01978/trmb-primary-assays.txt\
    \ for versioned references, complete Pfam mappings,\n    deposition hashes and\
    \ construct discrepancies. No isolated PF01978 sufficiency or universal sugar-regulator\n\
    \    role is asserted.\n- discussion_id: trmb-assay-context-and-residual-activity\n\
    \  prompt: Resolve preparation carryover and assay-specific outcomes before assigning\
    \ a single sugar-to-DNA\n    regulatory mechanism.\n  kind: CURATION_TODO\n  status:\
    \ OPEN\n  rationale: Trehalose relieves transcriptional repression but increases\
    \ region-1 EMSA retardation under\n    different conditions. The thesis stores\
    \ proteins in glucose-containing buffer without dialysis; no-added-sugar\n   \
    \ assays are not established sugar-free. Y50N and E87A retain concentration-dependent\
    \ repression.\n  evidence:\n  - reference: PMID:12426307\n    supports: SUPPORT\n\
    \    evidence_source: primary_text_and_captions\n    explanation: Figures 6 and\
    \ 8 describe different trehalose effects; original figure images were not\n  \
    \    available through the attempted access routes.\n  - reference: doi:10.5283/epub.14529\n\
    \    supports: SUPPORT\n    evidence_source: doctoral_thesis_and_original_figures\n\
    \    explanation: Methods pp.39-41, Figures 45-48 and 51 retain glucose carryover,\
    \ residual/nonmonotonic\n      activity, unequal footprint nuclease amounts and\
    \ a diffuse MD shift. These prevent exact affinity,\n      stoichiometry and atomic-contact\
    \ claims.\n  posed_by: Codex\n  posed_date: '2026-10-15'\n  notes: Obtain complete\
    \ stock compositions, matched nuclease comparisons, replicate/error estimates\
    \ and\n    direct occupancy/competition measurements. Retain Figure 45 residual\
    \ repression and Figure 51 low-dose\n    MD enhancement; do not flatten them into\
    \ uniform inhibition or a native activation claim.\n- discussion_id: trmb-family-and-promoter-coverage\n\
    \  prompt: Extend primary-assay coverage to remaining promoters, anti-inducers,\
    \ paralogs and taxa with\n    separate reference mapping.\n  kind: CURATION_TODO\n\
    \  status: OPEN\n  rationale: These scoped whole-protein experiments do not review\
    \ all PF01978 proteins or establish a\n    universal DNA-binding, sugar-response\
    \ or transcriptional mechanism.\n  evidence:\n  - reference: doi:10.5283/epub.14529\n\
    \    supports: PARTIAL\n    evidence_source: doctoral_thesis\n    explanation:\
    \ Remaining promoter-engineering, anti-inducer, cross-promoter and TrmBL1 results\
    \ need\n      their own methods, figure and identity assessment.\n  - reference:\
    \ PMID:23576322\n    supports: PARTIAL\n    evidence_source: primary_publication\n\
    \    explanation: The sucrose-bound structure lacks DNA, while its maltose comparator\
    \ lacks residues 2-109.\n      Proposed allosteric motion is not directly observed\
    \ and older/unpublished assays are not new measurements\n      in this paper.\n\
    \  posed_by: Codex\n  posed_date: '2026-10-15'\n  notes: Inspect full Lee2005\
    \ and differential-signals Lee2007 sources, distinguish the separate PF0124\n\
    \    paper, and assess Tgr/TrmBL1/2/4 and other taxa without transferring TrmB\
    \ endpoints by similarity\n    alone. Native physiology and residue-level DNA\
    \ contacts remain open.\ncausal_graphs:\n- graph_id: tl-trmb-tm-transcription-2003\n\
    \  title: TrmB represses reconstituted malE transcription with sugar-specific\
    \ relief\n  scope: Full-length T. litoralis pSL152 TrmB with a C-terminal His6\
    \ tag; whole-protein activity in a\n    heterologous reconstituted transcription\
    \ system.\n  context: Linearized pMLP malE template, P. furiosus TBP/TFB/RNAP,\
    \ 80 C; 0.8-3.2 ug TrmB. At 3.2 ug TrmB,\n    added maltose at 100 uM or trehalose\
    \ at 2.5 mM relieves repression. Buffer and component amounts are\n    retained\
    \ in ledger S1a; reaction duration and volume remain unresolved.\n  family_mapping:\
    \ Q7LYW4 sequence 1/entry 91 is the 338-aa T. litoralis reference, with PF01978\
    \ 11-77,\n    PF11495 110-234 and PF31112 249-335. The exact study strain and\
    \ full insert were not independently\n    established; this is not isolated PF01978\
    \ activity.\n  scope_status: MECHANISTIC\n  limitations: Primary methods, results\
    \ and Figure 8 caption inspected, not its original image. The gdh\n    lane controls\
    \ the transcription system, not a full TrmB specificity series. Relief of repression\
    \ does\n    not establish DNA release or native transporter flux; trehalose prose/caption\
    \ threshold wording differs.\n  nodes:\n  - node_id: protein\n    label: Added\
    \ full-length TrmB in the reconstituted malE system\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q7LYW4\n  - node_id: transcript\n    label: 110-nt\
    \ malE transcript output\n    node_type: PROCESS\n  - node_id: maltose\n    label:\
    \ Added 100 uM maltose with 3.2 ug TrmB\n    node_type: PERTURBATION\n  - node_id:\
    \ trehalose\n    label: Added 2.5 mM trehalose with 3.2 ug TrmB\n    node_type:\
    \ PERTURBATION\n  edges:\n  - edge_id: represses-transcript\n    subject: protein\n\
    \    predicate: decreases\n    object: transcript\n    mechanism: Increasing added\
    \ TrmB reduces the runoff transcript in the reconstituted assay. This is\n   \
    \   direct whole-protein repression at the process level, not a measured elementary\
    \ TBP-displacement\n      step.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:12426307\n\
    \      source_url: https://www.researchgate.net/publication/11041114_TrmB_a_Sugar-specific_Transcriptional_Regulator_of_the_TrehaloseMaltose_ABC_Transporter_from_the_Hyperthermophilic_Archaeon_Thermococcus_litoralis\n\
    \      snippet: the transcript of malE\n      explanation: Figure 8 lanes 4-6,\
    \ results and transcription methods; ledger S1a. No exact densitometry\n     \
    \   or native-cell repression is inferred.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    \  - edge_id: maltose-relieves-repression\n    subject: maltose\n    predicate:\
    \ increases\n    object: transcript\n    mechanism: Added maltose restores transcript\
    \ relative to the TrmB-containing no-added-sugar reaction;\n      the intervening\
    \ conformational and DNA-binding steps are unresolved in this assay.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:12426307\n      source_url: https://www.researchgate.net/publication/11041114_TrmB_a_Sugar-specific_Transcriptional_Regulator_of_the_TrehaloseMaltose_ABC_Transporter_from_the_Hyperthermophilic_Archaeon_Thermococcus_litoralis\n\
    \      snippet: the transcript of malE\n      explanation: Figure 8A lane 8 and\
    \ results; ledger S1a. The source includes both TrmB and the transcription\n \
    \       machinery.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    \  - edge_id: trehalose-relieves-repression\n    subject: trehalose\n    predicate:\
    \ increases\n    object: transcript\n    mechanism: Added trehalose restores transcription\
    \ in the reported lane condition. This endpoint is\n      kept separate from the\
    \ increased EMSA retardation observed at higher trehalose concentrations under\n\
    \      another protocol.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:12426307\n\
    \      source_url: https://www.researchgate.net/publication/11041114_TrmB_a_Sugar-specific_Transcriptional_Regulator_of_the_TrehaloseMaltose_ABC_Transporter_from_the_Hyperthermophilic_Archaeon_Thermococcus_litoralis\n\
    \      snippet: the transcript of malE\n      explanation: Figure 8B lane 11 caption\
    \ and results; ledger S1a. Prose also says above 2.5 mM; no\n        universal\
    \ threshold is assigned.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    - graph_id: tl-trmb-sugar-emsa-2003\n  title: Maltose and trehalose have opposite\
    \ effects on TrmB-associated DNA retardation\n  scope: Purified full-length T.\
    \ litoralis TrmB and labeled intergenic region 1 in EMSA, not a native\n    transcription\
    \ assay.\n  context: 1.25 uM TrmB, 70 C for 10 min then 8% native PAGE at room\
    \ temperature; maltose 5-50 uM or trehalose\n    1-10 mM in separate reactions.\
    \ Buffer and competitor are retained in ledger S1b.\n  family_mapping: Q7LYW4\
    \ version 1 reference, PF01978 11-77 within a 338-aa multidomain protein; the\
    \ sugar-binding\n    matches PF11495 and PF31112 are separate. Complete assay\
    \ insert remains unverified.\n  scope_status: MECHANISTIC\n  limitations: Original\
    \ Figure 6 image unavailable; primary text/caption inspected. Shift intensity\
    \ is\n    not a measured off-rate, binding stoichiometry or transcriptional activity.\
    \ Do not join these sugar-specific\n    effects into a universal dissociation\
    \ model.\n  nodes:\n  - node_id: maltose\n    label: Added maltose up to 50 uM\
    \ in the TrmB-region-1 reaction\n    node_type: PERTURBATION\n  - node_id: trehalose\n\
    \    label: Added trehalose at 5-10 mM in the TrmB-region-1 reaction\n    node_type:\
    \ PERTURBATION\n  - node_id: retarded\n    label: Retarded TrmB-associated region-1\
    \ DNA\n    node_type: STATE\n  edges:\n  - edge_id: maltose-reduces-retardation\n\
    \    subject: maltose\n    predicate: decreases\n    object: retarded\n    mechanism:\
    \ Maltose reduces DNA retardation, with a reported half-effect at 20-50 uM in\
    \ this assay.\n      The direct complex-level response does not identify its atomic\
    \ allosteric route.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:12426307\n      source_url:\
    \ https://www.researchgate.net/publication/11041114_TrmB_a_Sugar-specific_Transcriptional_Regulator_of_the_TrehaloseMaltose_ABC_Transporter_from_the_Hyperthermophilic_Archaeon_Thermococcus_litoralis\n\
    \      snippet: TrmB-mediated EMSA\n      explanation: Figure 6 and sugar-dependent\
    \ EMSA results/methods; ledger S1b.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    \  - edge_id: trehalose-increases-retardation\n    subject: trehalose\n    predicate:\
    \ increases\n    object: retarded\n    mechanism: At 5-10 mM trehalose the source\
    \ reports greater stability/retardation of the complex. This\n      does not establish\
    \ increased transcriptional repression, since transcription behaves differently\n\
    \      under its own conditions.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:12426307\n\
    \      source_url: https://www.researchgate.net/publication/11041114_TrmB_a_Sugar-specific_Transcriptional_Regulator_of_the_TrehaloseMaltose_ABC_Transporter_from_the_Hyperthermophilic_Archaeon_Thermococcus_litoralis\n\
    \      snippet: complex was clearly increased\n      explanation: Figure 6 results\
    \ and caption; ledger S1b. A complex-level gel effect, not a fitted\n        kinetic\
    \ stability constant.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    - graph_id: tl-trmb-maltose-footprint-2003\n  title: Maltose removes TrmB-associated\
    \ promoter protection\n  scope: Full-length T. litoralis TrmB, coding and noncoding\
    \ strands of the intergenic promoter region,\n    DNaseI protection assay.\n \
    \ context: 5 uM TrmB with or without 100 uM maltose; binding 70 C for 10 min followed\
    \ by 0.005 U DNaseI\n    for 5 min at 37 C. BRE/TATA and inverted-repeat-associated\
    \ regions are assessed.\n  family_mapping: Q7LYW4 version 1 reference, PF01978\
    \ 11-77; whole-protein pSL152 preparation. Neither\n    exact study strain nor\
    \ complete tag/insert is inferred from reference taxonomy.\n  scope_status: MECHANISTIC\n\
    \  limitations: Primary Figure 4 caption and text, not original image, inspected.\
    \ Loss of nuclease protection\n    is not direct measurement of TBP recruitment.\
    \ Trehalose footprint loss is reported data-not-shown\n    and is not an independently\
    \ inspected edge.\n  nodes:\n  - node_id: maltose\n    label: 100 uM maltose added\
    \ to 5 uM TrmB-DNA reaction\n    node_type: PERTURBATION\n  - node_id: protection\n\
    \    label: TrmB-associated DNaseI protection of promoter regions\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: reduces-protection\n    subject: maltose\n   \
    \ predicate: decreases\n    object: protection\n    mechanism: The protected regions\
    \ lose protection after maltose addition in the matched protein-containing\n \
    \     footprint condition; exact DNA-release kinetics are not measured.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:12426307\n      source_url: https://www.researchgate.net/publication/11041114_TrmB_a_Sugar-specific_Transcriptional_Regulator_of_the_TrehaloseMaltose_ABC_Transporter_from_the_Hyperthermophilic_Archaeon_Thermococcus_litoralis\n\
    \      snippet: TrmB no longer protected\n      explanation: Figure 4 M lane,\
    \ results and footprint methods; ledger S1c. The digestion is at 37\n        C,\
    \ not the transcription assay's 80 C.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    - graph_id: trmb-tm-repression-and-maltose-thesis\n  title: WT and E87A TrmB repress\
    \ TM transcription and retain maltose response\n  scope: Full-length pSL152-derived\
    \ WT and E87A preparations in Surma's doctoral thesis, separate 484-bp\n    TM\
    \ template.\n  context: Figure 46A; 0.5 uM regulator, 150 fmol template, P. furiosus\
    \ TBP/TFB/RNAP, 25 uL buffer III,\n    80 C for 30 min; 1 mM added maltose where\
    \ indicated. Ledger S2 specifies salt, nucleotides and glucose-containing\n  \
    \  protein preparation.\n  family_mapping: Thesis calls pSL152 PF1743; Q9HGZ9\
    \ version 1 and T. litoralis Q7LYW4 version 1 have\n    identical bodies and PF01978\
    \ 11-77. Plasmid taxonomy conflicts with Lee2003 and remains unresolved.\n   \
    \ E87 is outside PF01978; no domain-specific E87 mechanism is asserted.\n  scope_status:\
    \ MECHANISTIC\n  limitations: Public thesis evidence, not a new peer-reviewed\
    \ 2007 result. No-added-sugar is not sugar-free\n    because stock glucose was\
    \ not dialyzed away. Complete constructs, final carryover and mutant folding/active\n\
    \    fractions remain unresolved.\n  nodes:\n  - node_id: wt\n    label: 0.5 uM\
    \ WT TrmB added to TM transcription reaction\n    node_type: PERTURBATION\n  -\
    \ node_id: e87a\n    label: 0.5 uM E87A TrmB added to TM transcription reaction\n\
    \    node_type: PERTURBATION\n  - node_id: maltose_wt\n    label: 1 mM added maltose\
    \ with 0.5 uM WT TrmB\n    node_type: PERTURBATION\n  - node_id: maltose_e87a\n\
    \    label: 1 mM added maltose with 0.5 uM E87A TrmB\n    node_type: PERTURBATION\n\
    \  - node_id: transcript\n    label: 156-nt TM runoff transcript output\n    node_type:\
    \ PROCESS\n  edges:\n  - edge_id: wt-represses\n    subject: wt\n    predicate:\
    \ decreases\n    object: transcript\n    mechanism: WT addition reduces transcript\
    \ relative to the no-regulator lane, demonstrating whole-protein\n      reconstituted\
    \ repression without resolving initiation microsteps.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: doi:10.5283/epub.14529\n      source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: Transkriptionspuffer III.\n      explanation: Original Figure\
    \ 46A lanes 1/2 visually inspected with methods; ledger S2a.\n      cache_path:\
    \ evidence/PF01978/trmb-primary-assays.txt\n      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    \  - edge_id: e87a-represses\n    subject: e87a\n    predicate: decreases\n  \
    \  object: transcript\n    mechanism: E87A addition still reduces TM transcript.\
    \ Its weaker MD response must not be generalized\n      to a globally inactive\
    \ protein.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: doi:10.5283/epub.14529\n     \
    \ source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: TrmB E87A\n      explanation: Original Figure 46A lanes 1/6 and\
    \ Figure 45B/C; ledger S2a. Figure 45 provides dose-specific\n        residual\
    \ values, not an affinity measurement.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    \  - edge_id: wt-maltose-relief\n    subject: maltose_wt\n    predicate: increases\n\
    \    object: transcript\n    mechanism: Added maltose restores TM transcript relative\
    \ to WT without added maltose; the causal intermediate\n      is not directly\
    \ tracked in this transcription assay.\n    directness: UNRESOLVED\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: doi:10.5283/epub.14529\n\
    \      source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: Transkriptionspuffer III.\n      explanation: Original Figure\
    \ 46A lanes 2/3; ledger S2a. This differs from Lee2003 in preparation,\n     \
    \   template and buffer.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    \  - edge_id: e87a-maltose-relief\n    subject: maltose_e87a\n    predicate: increases\n\
    \    object: transcript\n    mechanism: Added maltose restores TM transcript in\
    \ the E87A reaction, preserving promoter-specific\n      responsiveness despite\
    \ the MD repression defect.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: doi:10.5283/epub.14529\n\
    \      source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: TrmB E87A\n      explanation: Original Figure 46A lanes 6/7; ledger\
    \ S2a. No isolated E87-region or sugar-binding-domain\n        sufficiency follows.\n\
    \      cache_path: evidence/PF01978/trmb-primary-assays.txt\n      cache_sha256:\
    \ e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n- graph_id:\
    \ trmb-md-repression-and-maltotriose-thesis\n  title: WT and Y50N TrmB repress\
    \ MD transcription and retain maltotriose response\n  scope: Full-length pSL152-derived\
    \ WT and Y50N preparations in the thesis, separate 348-bp MD template.\n  context:\
    \ Figure 46B; 1.5 uM regulator and 1 mM added maltotriose where indicated; 150\
    \ fmol template,\n    25 uL buffer III, P. furiosus TBP/TFB/RNAP, 80 C for 30\
    \ min. Glucose carryover is unresolved.\n  family_mapping: Q9HGZ9 and Q7LYW4 version\
    \ 1 references have PF01978 11-77 and Y50 within the match;\n    PF11495 and PF31112\
    \ are separate. Thesis PF1743 attribution and Lee2003 pSL152 origin conflict;\
    \ reference\n    bodies are identical but exact constructs are unverified.\n \
    \ scope_status: MECHANISTIC\n  limitations: MD conditions differ from the 0.5-uM\
    \ TM assay. Retained MD repression does not prove Y50\n    directly recognizes\
    \ either promoter or that the entire protein is structurally unchanged. Thesis\
    \ evidence\n    and no-added-sugar conditions remain explicitly scoped.\n  nodes:\n\
    \  - node_id: wt\n    label: 1.5 uM WT TrmB added to MD transcription reaction\n\
    \    node_type: PERTURBATION\n  - node_id: y50n\n    label: 1.5 uM Y50N TrmB added\
    \ to MD transcription reaction\n    node_type: PERTURBATION\n  - node_id: maltotriose_wt\n\
    \    label: 1 mM added maltotriose with 1.5 uM WT TrmB\n    node_type: PERTURBATION\n\
    \  - node_id: maltotriose_y50n\n    label: 1 mM added maltotriose with 1.5 uM\
    \ Y50N TrmB\n    node_type: PERTURBATION\n  - node_id: transcript\n    label:\
    \ 168-nt MD runoff transcript output\n    node_type: PROCESS\n  edges:\n  - edge_id:\
    \ wt-represses\n    subject: wt\n    predicate: decreases\n    object: transcript\n\
    \    mechanism: WT addition lowers the MD runoff transcript relative to no regulator,\
    \ a whole-protein biochemical\n      repression effect without a resolved atomic\
    \ route.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: doi:10.5283/epub.14529\n      source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: Transkriptionspuffer III.\n      explanation: Original Figure\
    \ 46B lanes 1/2 and methods; ledger S2b.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    \  - edge_id: y50n-represses\n    subject: y50n\n    predicate: decreases\n  \
    \  object: transcript\n    mechanism: Y50N retains MD transcript repression; the\
    \ TM defect is not a universal loss of repressor\n      function. Figure 45 quantification\
    \ retains residual transcript rather than imposing zero output.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: doi:10.5283/epub.14529\n      source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: TrmB Y50N\n      explanation: Original Figure 46B lanes 1/4, Figure\
    \ 45A/C and text pp.105-108; ledger S2b.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    \  - edge_id: wt-maltotriose-relief\n    subject: maltotriose_wt\n    predicate:\
    \ increases\n    object: transcript\n    mechanism: Added maltotriose relieves\
    \ WT-associated MD repression in this reaction; no observed allosteric\n     \
    \ trajectory is asserted.\n    directness: UNRESOLVED\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: doi:10.5283/epub.14529\n\
    \      source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: Transkriptionspuffer III.\n      explanation: Original Figure\
    \ 46B lanes 2/3; ledger S2b.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    \  - edge_id: y50n-maltotriose-relief\n    subject: maltotriose_y50n\n    predicate:\
    \ increases\n    object: transcript\n    mechanism: Added maltotriose restores\
    \ MD transcript in the Y50N reaction, showing retained promoter-specific\n   \
    \   regulation without establishing isolated-domain activity.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: doi:10.5283/epub.14529\n      source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: TrmB Y50N\n      explanation: Original Figure 46B lanes 4/5; ledger\
    \ S2b.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n      cache_sha256:\
    \ e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n- graph_id:\
    \ trmb-promoter-selective-mutant-effects-thesis\n  title: Y50N and E87A weaken\
    \ repression of different isolated promoters\n  scope: Same-dose comparisons of\
    \ full-length WT and mutant preparations in Figure 46, not a domain-fragment\n\
    \    experiment or a mutant potency ranking across promoters.\n  context: TM at\
    \ 0.5 uM regulator and MD at 1.5 uM, no added inducer, 25 uL buffer III with P.\
    \ furiosus\n    transcription components, 80 C for 30 min. Figures 45/46 and ledger\
    \ S2a-b preserve dose dependence\n    and protein-stock glucose.\n  family_mapping:\
    \ Reference Y50 is inside PF01978 11-77; E87 is outside it in identical 338-aa\
    \ Q9HGZ9/Q7LYW4\n    version 1 bodies. Complete WT/mutant inserts and the pSL152\
    \ species attribution remain unresolved.\n  scope_status: PHENOTYPIC\n  limitations:\
    \ Endpoint changes are observed, but folding, active abundance, oligomerization\
    \ and altered\n    DNA affinity are not separated. Figure 45 retains Y50N TM repression\
    \ at 2.5-3 uM and E87A MD repression\n    at 2.5-3 uM. Occasional Y50D prose is\
    \ not silently adopted over Y50N figure labels.\n  nodes:\n  - node_id: y50n\n\
    \    label: Replace WT with Y50N at 0.5 uM on TM template\n    node_type: PERTURBATION\n\
    \  - node_id: tm\n    label: TM runoff transcript relative to same-dose WT\n \
    \   node_type: PROCESS\n  - node_id: e87a\n    label: Replace WT with E87A at\
    \ 1.5 uM on MD template\n    node_type: PERTURBATION\n  - node_id: md\n    label:\
    \ MD runoff transcript relative to same-dose WT\n    node_type: PROCESS\n  edges:\n\
    \  - edge_id: y50n-weakens-tm-repression\n    subject: y50n\n    predicate: increases\n\
    \    object: tm\n    mechanism: Y50N produces much more TM transcript than WT\
    \ at the same low dose. This is a mutation-associated\n      loss of repression,\
    \ not proof of a direct Tyr50-DNA contact or total inactivity at all concentrations.\n\
    \    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: doi:10.5283/epub.14529\n      source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: TrmB Y50N\n      explanation: Original Figure 46A lanes 2/4 and\
    \ Figure 45 residual-activity series; ledger S2a. This\n        reuses the same\
    \ experiment, not independent replication of the TM graph.\n      cache_path:\
    \ evidence/PF01978/trmb-primary-assays.txt\n      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    \  - edge_id: e87a-weakens-md-repression\n    subject: e87a\n    predicate: increases\n\
    \    object: md\n    mechanism: E87A yields more MD transcript than WT at the\
    \ same dose. E87 lies outside PF01978, and\n      the affected molecular route\
    \ is unresolved.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: doi:10.5283/epub.14529\n     \
    \ source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: TrmB E87A\n      explanation: Original Figure 46B lanes 2/6 and\
    \ Figure 45B/C; ledger S2b. Do not convert retained\n        residual repression\
    \ into an absolute requirement claim.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    - graph_id: trmb-tm-maltose-footprints-thesis\n  title: Maltose removes WT and\
    \ E87A protection of the TM promoter\n  scope: Full-length WT or E87A pSL152-derived\
    \ protein, separate matched-nuclease comparisons in thesis\n    Figure 47.\n \
    \ context: 1.5 uM regulator, 100 ng labeled TM DNA, 25 uL footprint buffer I;\
    \ 70 C for 15 min binding,\n    then 0.02 U DNaseI at 40 C for 5 min. Added maltose\
    \ is 1 mM. Full buffer and glucose-carryover caveat\n    are in ledger S2c.\n\
    \  family_mapping: PF01978 is 11-77 in Q9HGZ9/Q7LYW4 version 1 reference bodies;\
    \ E87 is outside that match.\n    Plasmid lineage and complete constructs are\
    \ not independently resolved.\n  scope_status: MECHANISTIC\n  limitations: No-protein\
    \ and Y50N lanes use 0.01 U DNaseI, so they are not used as matched-nuclease mutant\n\
    \    causal comparisons. Protection loss does not directly measure TBP competition\
    \ or a structural transition.\n    MD mutant footprinting failed in this source.\n\
    \  nodes:\n  - node_id: maltose_wt\n    label: 1 mM added maltose with WT TrmB\
    \ at matched DNaseI dose\n    node_type: PERTURBATION\n  - node_id: wt_protection\n\
    \    label: WT-associated TM BRE/TATA-region protection\n    node_type: STATE\n\
    \  - node_id: maltose_e87a\n    label: 1 mM added maltose with E87A TrmB at matched\
    \ DNaseI dose\n    node_type: PERTURBATION\n  - node_id: e87a_protection\n   \
    \ label: E87A-associated TM BRE/TATA-region protection\n    node_type: STATE\n\
    \  edges:\n  - edge_id: removes-wt-protection\n    subject: maltose_wt\n    predicate:\
    \ decreases\n    object: wt_protection\n    mechanism: Adding maltose eliminates\
    \ the marked WT footprint at unchanged protein and nuclease amounts;\n      a\
    \ direct protection response, not a measured DNA-release rate.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: doi:10.5283/epub.14529\n      source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: DNaseI\n      explanation: Original Figure 47 lanes 2/3 visually\
    \ inspected, with explicit 0.02-U caption conditions;\n        ledger S2c.\n \
    \     cache_path: evidence/PF01978/trmb-primary-assays.txt\n      cache_sha256:\
    \ e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n  - edge_id:\
    \ removes-e87a-protection\n    subject: maltose_e87a\n    predicate: decreases\n\
    \    object: e87a_protection\n    mechanism: Adding maltose eliminates the E87A\
    \ footprint at matched 0.02-U nuclease dose, retaining\n      a TM-specific response\
    \ despite the MD-associated defect.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: doi:10.5283/epub.14529\n\
    \      source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: TrmB E87A\n      explanation: Original Figure 47 lanes 5/6; ledger\
    \ S2c. The Y50N lane has a different nuclease amount\n        and is not substituted\
    \ into this comparison.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    - graph_id: trmb-e87a-md-retardation-thesis\n  title: E87A reduces detectable\
    \ MD DNA retardation\n  scope: Full-length WT versus E87A preparations in thesis\
    \ Figure 48, with Y50N and no-protein comparison\n    lanes.\n  context: 3 uM\
    \ protein, 25 ng MD template per figure caption, 25 uL EMSA buffer; 70 C for 15\
    \ min, cool\n    to 40 C, then 6% native PAGE at room temperature. The generic\
    \ method says 30 ng, a retained discrepancy.\n  family_mapping: E87 is outside\
    \ PF01978 11-77 in the identical Q9HGZ9/Q7LYW4 version 1 reference bodies.\n \
    \   Exact mutant insert and pSL152 lineage remain unresolved; reference mapping\
    \ is not a verified mutant\n    structure.\n  scope_status: PHENOTYPIC\n  limitations:\
    \ WT and Y50N shifts are diffuse, explicitly not cleanly resolved. The endpoint\
    \ is detectable\n    retardation, not Kd, zero binding, oligomer stoichiometry\
    \ or an E87-DNA contact. Stock glucose and\n    mutant folding/active fractions\
    \ remain unresolved.\n  nodes:\n  - node_id: e87a\n    label: Replace WT with\
    \ E87A at 3 uM in the MD EMSA\n    node_type: PERTURBATION\n  - node_id: retarded\n\
    \    label: Detectably retarded MD DNA\n    node_type: STATE\n  edges:\n  - edge_id:\
    \ reduces-md-retardation\n    subject: e87a\n    predicate: decreases\n    object:\
    \ retarded\n    mechanism: E87A yields predominantly free-DNA-like migration relative\
    \ to the diffuse retarded WT lane;\n      the preparation-dependent molecular\
    \ cause is unresolved.\n    directness: UNRESOLVED\n    support: OBSERVED\n  \
    \  evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: doi:10.5283/epub.14529\n\
    \      source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: EMSA\n      explanation: Original Figure 48 lanes 2/3, with lanes\
    \ 1/4 as no-protein/Y50N context; ledger S2d.\n        The failed MD footprint\
    \ experiment is not evidence of absent binding.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    - graph_id: trmb-composite-promoter-dose-thesis\n  title: WT TrmB shifts TM and\
    \ MD output differently on a composite template\n  scope: Artificial 589-bp TMMD\
    \ template and full-length WT TrmB; distinct from isolated promoters and\n   \
    \ native operons.\n  context: Figure 51, 150 fmol template, 25 uL buffer III,\
    \ P. furiosus TBP/TFB/RNAP, 80 C for 30 min;\n    WT 0/1.5/3/4.5 uM. Each promoter\
    \ is independently normalized to its own no-regulator output.\n  family_mapping:\
    \ Thesis pSL152 preparation, mapped by identical Q9HGZ9/Q7LYW4 version 1 reference\
    \ bodies\n    with PF01978 11-77. Complete construct and taxonomy conflict remain\
    \ unresolved.\n  scope_status: PHENOTYPIC\n  limitations: No added inducer does\
    \ not mean no glucose. Percentages are published gel quantifications\n    without\
    \ established replicate statistics. Apparent MD enhancement is not proof of native\
    \ activation;\n    competition for machinery is an unmeasured explanation. Reported\
    \ zero is a gel endpoint, not exact\n    absence of molecular transcription.\n\
    \  nodes:\n  - node_id: low\n    label: Add 1.5 uM WT TrmB to the composite-template\
    \ reaction\n    node_type: PERTURBATION\n  - node_id: high\n    label: Increase\
    \ WT TrmB from 1.5 to 4.5 uM on the composite template\n    node_type: PERTURBATION\n\
    \  - node_id: tm\n    label: Composite-template TM transcript output\n    node_type:\
    \ PROCESS\n  - node_id: md\n    label: Composite-template MD transcript output\n\
    \    node_type: PROCESS\n  edges:\n  - edge_id: low-dose-lowers-tm\n    subject:\
    \ low\n    predicate: decreases\n    object: tm\n    mechanism: TM output decreases\
    \ from its own 100% no-regulator baseline to 10% at 1.5 uM WT. The net\n     \
    \ output is observed; occupancy and competition are not directly quantified.\n\
    \    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: doi:10.5283/epub.14529\n      source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: Transkriptionspuffer III.\n      explanation: Original Figure\
    \ 51 gel and TM numeric table, lanes 1/2; ledger S2e.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    \  - edge_id: low-dose-raises-md\n    subject: low\n    predicate: increases\n\
    \    object: md\n    mechanism: MD output rises from its own 100% baseline to\
    \ 140% at 1.5 uM WT in this joint-promoter\n      system. The source proposes\
    \ redistribution of shared transcription machinery, but this was not directly\n\
    \      measured.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: doi:10.5283/epub.14529\n     \
    \ source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: Transkriptionspuffer III.\n      explanation: Original Figure\
    \ 51 MD numeric table, lanes 1/2, and p.113 interpretation; ledger S2e.\n    \
    \    A context-specific endpoint, not direct activation by isolated PF01978.\n\
    \      cache_path: evidence/PF01978/trmb-primary-assays.txt\n      cache_sha256:\
    \ e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n  - edge_id:\
    \ higher-dose-lowers-tm\n    subject: high\n    predicate: decreases\n    object:\
    \ tm\n    mechanism: Increasing WT from 1.5 to 4.5 uM lowers TM output from 10%\
    \ to the reported 0% gel endpoint.\n      The intermediate 3-uM condition is 5%;\
    \ no molecular zero or affinity constant is inferred.\n    directness: UNRESOLVED\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: doi:10.5283/epub.14529\n      source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: Transkriptionspuffer III.\n      explanation: Original Figure\
    \ 51 TM numeric table, lanes 2-4; ledger S2e. Baselines differ from the\n    \
    \    low-dose versus no-regulator edge.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    \  - edge_id: higher-dose-lowers-md\n    subject: high\n    predicate: decreases\n\
    \    object: md\n    mechanism: Raising WT from 1.5 to 4.5 uM lowers MD output\
    \ from 140% to 52%, crossing below its no-regulator\n      baseline. This preserves\
    \ the initial enhancement instead of claiming uniform inhibition at every\n  \
    \    dose.\n    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: doi:10.5283/epub.14529\n     \
    \ source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: Transkriptionspuffer III.\n      explanation: Original Figure\
    \ 51 MD numeric table, lanes 2-4, values 140/88/52; ledger S2e.\n      cache_path:\
    \ evidence/PF01978/trmb-primary-assays.txt\n      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    - graph_id: trmb-composite-promoter-mutants-thesis\n  title: Mutant effects remain\
    \ promoter-dependent on the composite template\n  scope: Same-dose WT versus Y50N\
    \ or E87A on the artificial TMMD template, not separate native operons.\n  context:\
    \ Figure 51, 4.5 uM regulator, 150 fmol 589-bp template, 25 uL buffer III, P.\
    \ furiosus TBP/TFB/RNAP,\n    80 C for 30 min. Compare lanes 4/7/10, with each\
    \ promoter's no-regulator output normalized to 100%.\n  family_mapping: Y50 lies\
    \ within PF01978 11-77 and E87 outside it in the identical Q9HGZ9/Q7LYW4 version\n\
    \    1 references. Exact pSL152 construct lineage, inserted mutations and active\
    \ fractions remain independently\n    unverified.\n  scope_status: PHENOTYPIC\n\
    \  limitations: Y50N MD values are nonmonotonic across doses and E87A retains\
    \ TM repression; ledger S2e\n    preserves all values. No replicate significance,\
    \ matched native-cell phenotype, direct DNA contact\n    or regulator stoichiometry\
    \ follows. Protein-stock glucose is unresolved.\n  nodes:\n  - node_id: y50n\n\
    \    label: Replace 4.5 uM WT with Y50N on composite template\n    node_type:\
    \ PERTURBATION\n  - node_id: tm\n    label: Composite-template TM output relative\
    \ to same-dose WT\n    node_type: PROCESS\n  - node_id: e87a\n    label: Replace\
    \ 4.5 uM WT with E87A on composite template\n    node_type: PERTURBATION\n  -\
    \ node_id: md\n    label: Composite-template MD output relative to same-dose WT\n\
    \    node_type: PROCESS\n  edges:\n  - edge_id: y50n-raises-tm\n    subject: y50n\n\
    \    predicate: increases\n    object: tm\n    mechanism: The Y50N preparation\
    \ yields 102% TM output versus the WT lane's reported 0%, relative to\n      the\
    \ shared TM baseline. Its MD output is 77%, not a claim of complete MD repression.\n\
    \    directness: UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: doi:10.5283/epub.14529\n      source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: TrmB Y50N\n      explanation: Original Figure 51 numeric tables\
    \ and gel, lanes 4/7; ledger S2e. This is separate\n        from the 0.5-uM isolated-TM\
    \ comparison.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n  \
    \    cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    \  - edge_id: e87a-raises-md\n    subject: e87a\n    predicate: increases\n  \
    \  object: md\n    mechanism: E87A yields 180% MD output versus WT's 52% at the\
    \ same dose, while TM remains at 14%. The\n      joint-template phenotype does\
    \ not prove direct MD activation or an E87 contact with DNA.\n    directness:\
    \ UNRESOLVED\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: doi:10.5283/epub.14529\n      source_url: https://epub.uni-regensburg.de/14529/1/Dissertation_Melanie_Surma.pdf\n\
    \      snippet: TrmB E87A\n      explanation: Original Figure 51 numeric tables\
    \ and gel, lanes 4/10, plus text p.115; ledger S2e.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    - graph_id: tl-trmb-tbp-occlusion-model\n  title: TrmB promoter occupancy may\
    \ obstruct TBP recruitment\n  scope: Proposed interpretation of T. litoralis TrmB\
    \ footprints and reconstituted malE repression; not\n    a directly observed recruitment\
    \ experiment.\n  context: TrmB protects a BRE/TATA-overlapping region and represses\
    \ transcription in separate Lee2003\n    assays. The graph does not join their\
    \ different temperatures and readouts into an observed atomic\n    trajectory.\n\
    \  family_mapping: Q7LYW4 version 1 reference, PF01978 11-77 in full-length multidomain\
    \ TrmB. Neither an\n    isolated-domain interaction nor a DNA-bound residue contact\
    \ is established.\n  scope_status: HYPOTHETICAL\n  limitations: No direct TBP\
    \ competition, recruitment kinetics or TrmB-DNA structure was inspected. Krug2013\n\
    \    contains sucrose-bound protein without DNA and has unresolved construct/deposition\
    \ discrepancies;\n    it does not convert this proposal into an observed mechanism.\n\
    \  nodes:\n  - node_id: occupancy\n    label: Proposed TrmB occupancy overlapping\
    \ the TM BRE/TATA region\n    node_type: STATE\n  - node_id: tbp\n    label: TBP\
    \ recruitment to the TM promoter\n    node_type: PROCESS\n  edges:\n  - edge_id:\
    \ proposed-tbp-occlusion\n    subject: occupancy\n    predicate: decreases\n \
    \   object: tbp\n    mechanism: The source proposes that overlapping TrmB occupancy\
    \ obstructs TBP binding and subsequent\n      initiation-complex formation; footprint\
    \ overlap and repression motivate but do not directly measure\n      this competition.\n\
    \    directness: DIRECT\n    support: HYPOTHESIZED\n    evidence_kind: CONTEXTUAL\n\
    \    evidence:\n    - reference: PMID:12426307\n      source_url: https://www.researchgate.net/publication/11041114_TrmB_a_Sugar-specific_Transcriptional_Regulator_of_the_TrehaloseMaltose_ABC_Transporter_from_the_Hyperthermophilic_Archaeon_Thermococcus_litoralis\n\
    \      snippet: prevention of TBP binding\n      explanation: Discussion interpretation\
    \ following Figures 4/8; ledger S1c. Proposed directness describes\n        the\
    \ model, not experimental proof.\n      cache_path: evidence/PF01978/trmb-primary-assays.txt\n\
    \      cache_sha256: e15a096c12490afde76bbd6367bcdabd42b7103faac3a2db1147f79093aaed62\n\
    curation_events:\n- timestamp: '2026-10-15T14:00:02Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate scoped TrmB repression, sugar-response\
    \ and promoter-selective mutant graphs\n  history_record: history/records/PF01978/2026-10-15T140002Z-codex-211131.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: identity
  area: identity
  topic: Tested proteins versus family and domain
  outcome: supported
  target_ids:
  - PF01978
  evidence_ids:
  - identity
  - lee
  - thesis
  - structure
  summary: The transcription regulator is distinguished from unrelated TrmB methyltransferases.
    Whole-protein effects, PF01978 Y50, extra-domain E87 and separate sugar-binding
    matches remain explicit. Unknown constructs and conflicting species attribution
    are not replaced by reference assumptions.
- assessment_id: causal-claims
  area: graph
  topic: Direction, mechanism and uncertainty
  outcome: supported
  target_ids:
  - PF01978
  evidence_ids:
  - lee
  - thesis
  - structure
  summary: Twenty-five observed effect entries retain their actual assay and comparison;
    reused Figure 46 comparisons are not independent experiments. The single TBP-occlusion
    edge is explicitly hypothesized. Mutant and composite-template molecular routes
    remain unresolved; no atomic-contact, native-flux or isolated-domain claim is
    added.
- assessment_id: contradictions
  area: evidence
  topic: Contradictory outcomes and preparation limitations
  outcome: supported
  target_ids:
  - PF01978
  evidence_ids:
  - lee
  - thesis
  - structure
  summary: Trehalose EMSA/transcription differences, residual mutant repression, glucose-containing
    stock without dialysis, matched versus unequal DNaseI comparisons, diffuse MD
    shifts, Figure 51 MD enhancement and paper/deposition sequence differences are
    retained. No statistical significance or exact affinity is invented.
- assessment_id: provenance
  area: provenance
  topic: Native ownership and reproducibility
  outcome: supported
  target_ids:
  - PF01978
  evidence_ids:
  - native
  - search
  summary: Minimal quotations and factual summaries retain raw-source hashes/locators
    without redistributing full sources. Actual CREATE history precedes guarded projection;
    other records and imported fields are unchanged. Scientific review and release
    remain independent gates.
- assessment_id: coverage
  area: completeness
  topic: Incomplete family and corpus assessment
  outcome: concern
  target_ids:
  - PF01978
  evidence_ids:
  - identity
  - thesis
  - structure
  - search
  summary: Remaining promoter, anti-inducer and paralog/taxon experiments, full constructs,
    raw controls and molecular mechanisms are not finished. IN_PROGRESS and the original
    8296-family scope are preserved.
findings:
- finding_id: construct-and-domain-boundaries
  issue_key: pf01978-construct-and-domain-boundaries
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve full constructs and domain-specific attribution
  description: pSL152 species attribution differs across primary sources despite identical
    reference bodies. E87 is outside PF01978. Krug2013 V161A and C-tail descriptions
    conflict with 3QPH. These disclosed gaps limit, but do not invalidate, the scoped
    endpoint observations; no full insert or isolated-domain mechanism is claimed.
  target_ids:
  - PF01978
  field_paths:
  - causal_graphs
  - discussions
  evidence_ids:
  - identity
  - lee
  - thesis
  - structure
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01978.yaml
    role: Maintained scientific graph/discussion overlay with minimal evidence, native
      history and guarded regeneration.
- finding_id: assay-context-and-residual-activity
  issue_key: pf01978-assay-context-and-residual-activity
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve carryover and assay-specific molecular interpretations
  description: Obtain full stock compositions and glucose/imidazole carryover, mutant
    active fractions, matched-nuclease comparisons, replicate statistics and direct
    DNA/TBP occupancy measurements. Retain opposite trehalose readouts, residual Y50N/E87A
    activity and composite-template nonmonotonic/enhanced output; these cannot be
    flattened into a universal regulatory mechanism.
  target_ids:
  - PF01978
  field_paths:
  - causal_graphs
  - discussions
  evidence_ids:
  - lee
  - thesis
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01978.yaml
    role: Maintained scientific graph/discussion overlay with minimal evidence, native
      history and guarded regeneration.
- finding_id: family-and-promoter-coverage
  issue_key: pf01978-family-and-promoter-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Continue remaining promoter, paralog and taxon evidence
  description: Inspect full Lee2005 and differential-signals Lee2007, remaining thesis
    anti-inducer/promoter-engineering/cross-promoter data, and separately mapped TrmBL1/2/4,
    Tgr and other taxa. Do not equate graph presence or an EX_DUF name with family
    completion; all 8296 records remain in scope.
  target_ids:
  - PF01978
  field_paths:
  - causal_graphs
  - discussions
  evidence_ids:
  - identity
  - thesis
  - structure
  - search
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01978.yaml
    role: Maintained scientific graph/discussion overlay with minimal evidence, native
      history and guarded regeneration.
actions:
- action_id: extend-exact-member-assessment
  description: Continue the three open findings with primary construct, assay and
    member evidence; retain current scoped effects without increasing their evidential
    strength by inference.
  finding_ids:
  - construct-and-domain-boundaries
  - assay-context-and-residual-activity
  - family-and-promoter-coverage
  target_ids:
  - PF01978
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01978.yaml
    role: Maintained scientific graph/discussion overlay with minimal evidence, native
      history and guarded regeneration.
  acceptance_checks:
  - Verify exact constructs and current Pfam intervals before assigning domain/residue
    effects; retain source disagreements until primary sequence evidence resolves
    them.
  - Assess each new perturbation, measured outcome, control, preparation and promoter
    independently; distinguish phenotype from direct molecular mechanism.
  - Resolve carryover, residual activity and raw comparison limits without treating
    different assays or taxa as interchangeable.
  - Preserve stable finding IDs, actual history, validated projection and full family/corpus
    scope in successor reviews.
limitations:
- Partial scientific self-review, not independent expert approval, experimental replication
  or complete family/corpus assessment.
- Lee2003 original figure images were unavailable through attempted routes; primary
  text and captions were inspected. Only the named thesis original figures were visually
  assessed; remaining thesis results are not certified.
- Full assay inserts, exact strains, mutant-specific folding/active fractions, final
  buffer carryover and replicate statistics remain unverified. Reference identity
  and general sequencing methods do not close those gaps.
- The first focused test invocation omitted the pinned shared dependency configuration;
  rerun passed. The first scratch browser check incorrectly expected values inside
  collapsed disclosures in visible text; explicit expansion and content checks then
  passed. No scientific content was changed to satisfy either check.
- Canonical Pages/pins and full release QC remain unperformed publication work. Source-pin
  currentness fails for the changed projection; the local preview is explicitly unpinned.
tags:
- causal-graphs
- pf01978
- trmb
- promoter-specificity
- scientific-self-review
```
