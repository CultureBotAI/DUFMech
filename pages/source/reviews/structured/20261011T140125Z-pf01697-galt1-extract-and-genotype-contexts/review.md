# PF01697 GALT-1 extract biochemistry and genotype-specific causal effects

- Review: 20261011T140125Z-pf01697-galt1-extract-and-genotype-contexts
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T14:01:09Z
- Finished UTC: 2026-10-11T14:01:25Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Eight graphs retain fifteen observed effects from Titz 2009 and Butschi 2010, with ten direct preparation-level biochemical effects and five indirect genotype effects. Whole GALT-1, its current PF01697 interval and historical long RefSeq model are distinguished from isolated-domain sufficiency. Crude-extract activity, unresolved printed units, minor UDP-Glc signal, qualitative acceptor comparisons, joint-marker rescue, different genetic backgrounds and selected glycome fractions remain explicit. Imported identity is unchanged and status remains IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Pending PF01697 within all 8296 frozen families; selected nematode member evidence is not exhaustive family coverage.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01697 | data/families/PF01697.yaml | generated | PF01697 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01697 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01697.

O16374 GALT1_CAEEL is a 425-aa C. elegans reference, sequence version4, with current PF01697 189-394 and exact InterPro sequence identity. RefSeq NP_504545.2 is identical and replaced the incomplete274-aa NP_504545.1 in June2008, before the primary study. The paper's full coding N2 cDNA and N109/N152/D289/D291 positions fit the long model but do not prove every historical clone sequence. Predicted membrane/glycosylation regions lie outside the domain. op497 is an exon2 Mos1 insertion, not a mapped isolated-domain deletion or proven complete null. The two primary genetic backgrounds are not interchangeable.

### Directed effects and limits

graph: supported. Targets: PF01697.

The ten direct edges are scoped to crude-extract biochemical interventions, not autonomous purified GALT-1 catalysis. Product2207-to2369, fragment1273 and beta-galactosidase sensitivity support core-associated beta-galactosylation; the exact beta1,4 supplemental analysis from2009 was not independently inspected. Donor substitutions retain a small unresolved UDP-Glc peak. Acceptor comparisons are qualitative and MMF6 retains activity. Mn/Fe/Co versus water and EDTA replacing Mn affect neutral-fraction radiolabel without proving metal coordination or exact physiological specificity. Five indirect edges retain unc-119 op497, two joint-integrant rescues, pmk-1 op497 developmental resistance and loss of selected glycan peakA. Main Figure7 and supplementS2 support the latter peak's structural assignment. No CGL2-staining edge is attributed to galt-1 because that experiment tested fut-8; no chain joins all contexts as directly observed.

### Remaining family coverage

completeness: concern. Targets: PF01697.

Historical full clone verification, 2009 supplements and printed MES/metal unit resolution remain open. Purified enzyme, residue-specific DXD tests, independent alleles, matched genotype glycome rescue, complete glycome quantification and plant/other-member experiments are not integrated. Pigeon PMID19959475 and Populus GalS1 PMID36849618 are follow-up leads, not adopted edges. Current reference mapping and EX_DUF naming do not establish family-wide nematode core-fucose specificity.

## Findings

### additional-contexts: Resolve extract protocol and historical construct gaps and broaden GT92 coverage

minor / open / confirmed; issue key: pf01697-causal-context-coverage.

Inspect accessible 2009 supplements and an authoritative assay-unit source, verify complete historical constructs, and evaluate purified GALT-1 or additional allele/rescue evidence without upgrading mixture results into isolated-domain chemistry. Extend other GT92 members only after member-specific domain mapping and primary Methods/figure review, including plant galactan/capping and pigeon leads. Keep the partial-review status and exact experimental boundaries in successor curation.

## Recommended Actions And Acceptance Checks

### extend-contexts

Inspect accessible 2009 supplements and an authoritative assay-unit source, verify complete historical constructs, and evaluate purified GALT-1 or additional allele/rescue evidence without upgrading mixture results into isolated-domain chemistry. Extend other GT92 members only after member-specific domain mapping and primary Methods/figure review, including plant galactan/capping and pigeon leads. Keep the partial-review status and exact experimental boundaries in successor curation.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC2794738/; Titz 2009 primary HTML Methods, Results and Discussion; visually inspected Figures2-6, particularly product MS, donor HPLC, acceptor spectra, metal radiolabel and genetic rescue. | supports | GALT-1 expression extract jointly with UDP-Gal and core-fucosylated glycopeptide produces a core-associated beta-galactosylated product; donor, acceptor and metal replacements alter measured outputs. op497 raises the CGL2-fed L4 fraction in unc-119, while two integrated galt-1-mCherry plus marker constructs lower it. Raw extracts rather than purified protein were assayed; rescue co-restores the selection-marker phenotype. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/O16374/entry/pfam/PF01697/; Accession and domain locations; paired UniProt identity facts | supports | O16374 GALT1_CAEEL is a 425-aa C. elegans reference, sequence version4, with current PF01697 189-394 and exact InterPro sequence identity. RefSeq NP_504545.2 is identical and replaced the incomplete274-aa NP_504545.1 in June2008, before the primary study. The paper's full coding N2 cDNA and N109/N152/D289/D291 positions fit the long model but do not prove every historical clone sequence. Predicted membrane/glycosylation regions lie outside the domain. op497 is an exon2 Mos1 insertion, not a mapped isolated-domain deletion or proven complete null. The two primary genetic backgrounds are not interchangeable. |
| companion-genotype-and-glycome | https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1000717; Butschi 2010 genotype/glycome Results; strain, developmental, Mos1 and glycan Methods; visually inspected Figures4/7 and supplementS2. | supports | Exon2 op497 in pmk-1 raises the CGL2-fed L4 fraction and separately removes selected core-galactosylated peakA in OP50-grown glycome preparations. MS/MS and sequential glycosidases support the peak structure. Figure6 tests fut-8 rather than galt-1, and published genotype statistics do not claim a formal comparison against zero-valued pmk-1. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01697 | data/families/PF01697.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Titz 2009 Figures2-6 and Butschi 2010 Figures4/7 plus one-page supplementS2 were visually inspected. The 2009 supplemental primer/MS data and Figure8 alignment were not independently visually assessed. PMC's 2009 PDF request returned HTML, publisher access returned403 and ETH returned429; the primary PMC HTML was readable. No raw data reprocessing, calibrated digitization, clone resequencing, independent experimental replication or exhaustive family survey was performed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T140125Z-pf01697-galt1-extract-and-genotype-contexts
title: PF01697 GALT-1 extract biochemistry and genotype-specific causal effects
started_at: '2026-10-11T14:01:09Z'
finished_at: '2026-10-11T14:01:25Z'
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
summary: Eight graphs retain fifteen observed effects from Titz 2009 and Butschi 2010,
  with ten direct preparation-level biochemical effects and five indirect genotype
  effects. Whole GALT-1, its current PF01697 interval and historical long RefSeq model
  are distinguished from isolated-domain sufficiency. Crude-extract activity, unresolved
  printed units, minor UDP-Glc signal, qualitative acceptor comparisons, joint-marker
  rescue, different genetic backgrounds and selected glycome fractions remain explicit.
  Imported identity is unchanged and status remains IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01697.yaml
    sha256: 5926c53977bc50838b08ead6b7d0f3e2a550ddf4b7130c62d3bf4f574ac33ab5
    role: context
  - path: data/families/PF01697.yaml
    sha256: 9601df2885c2e7ec95d6afc30169e48a2df21b17d5f26dda4b0c5c3ff53b17a6
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
  - path: evidence/PF01697/titz-2009-galt1.txt
    role: context
    sha256: f0ead8cfc1653edd653af10e4036c499223c3beeed159a9d829a688a29cb9038
  - path: evidence/PF01697/GALT1-identity.txt
    role: context
    sha256: a1386323e150be935e395d5ecccdc9fef248744613b18f2ac46062538988cb48
  - path: evidence/PF01697/butschi-2010-galt1.txt
    role: context
    sha256: 5a614d50bcb2ca9673a0330b8a74394729d4fd748db926e61e0e5dcdac391024
targets:
- target_id: PF01697
  path: data/families/PF01697.yaml
  label: PF01697
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01697.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: ee81c6933043eb67382d4909f7c279ff6886272441bcffe144d8723c25077bc9
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Pending PF01697 within all 8296 frozen families; selected nematode member
    evidence is not exhaustive family coverage.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01697
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Historical full clone verification, 2009 supplements and printed MES/metal
      unit resolution remain open. Purified enzyme, residue-specific DXD tests, independent
      alleles, matched genotype glycome rescue, complete glycome quantification and
      plant/other-member experiments are not integrated. Pigeon PMID19959475 and Populus
      GalS1 PMID36849618 are follow-up leads, not adopted edges. Current reference
      mapping and EX_DUF naming do not establish family-wide nematode core-fucose
      specificity.
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
  - PF01697
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2794738/
  locator: Titz 2009 primary HTML Methods, Results and Discussion; visually inspected
    Figures2-6, particularly product MS, donor HPLC, acceptor spectra, metal radiolabel
    and genetic rescue.
  accessed_at: '2026-10-11T14:01:25Z'
  support: supports
  snapshot_sha256: f0ead8cfc1653edd653af10e4036c499223c3beeed159a9d829a688a29cb9038
  summary: GALT-1 expression extract jointly with UDP-Gal and core-fucosylated glycopeptide
    produces a core-associated beta-galactosylated product; donor, acceptor and metal
    replacements alter measured outputs. op497 raises the CGL2-fed L4 fraction in
    unc-119, while two integrated galt-1-mCherry plus marker constructs lower it.
    Raw extracts rather than purified protein were assayed; rescue co-restores the
    selection-marker phenotype.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/O16374/entry/pfam/PF01697/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T14:01:25Z'
  support: supports
  snapshot_sha256: a1386323e150be935e395d5ecccdc9fef248744613b18f2ac46062538988cb48
  summary: O16374 GALT1_CAEEL is a 425-aa C. elegans reference, sequence version4,
    with current PF01697 189-394 and exact InterPro sequence identity. RefSeq NP_504545.2
    is identical and replaced the incomplete274-aa NP_504545.1 in June2008, before
    the primary study. The paper's full coding N2 cDNA and N109/N152/D289/D291 positions
    fit the long model but do not prove every historical clone sequence. Predicted
    membrane/glycosylation regions lie outside the domain. op497 is an exon2 Mos1
    insertion, not a mapped isolated-domain deletion or proven complete null. The
    two primary genetic backgrounds are not interchangeable.
- evidence_id: companion-genotype-and-glycome
  kind: primary_source
  reference: https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1000717
  locator: Butschi 2010 genotype/glycome Results; strain, developmental, Mos1 and
    glycan Methods; visually inspected Figures4/7 and supplementS2.
  summary: Exon2 op497 in pmk-1 raises the CGL2-fed L4 fraction and separately removes
    selected core-galactosylated peakA in OP50-grown glycome preparations. MS/MS and
    sequential glycosidases support the peak structure. Figure6 tests fut-8 rather
    than galt-1, and published genotype statistics do not claim a formal comparison
    against zero-valued pmk-1.
  accessed_at: '2026-10-11T14:01:25Z'
  support: supports
  snapshot_sha256: 5a614d50bcb2ca9673a0330b8a74394729d4fd748db926e61e0e5dcdac391024
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T14:01:25Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01697
  kind: record_content
  reference: data/families/PF01697.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T14:01:25Z'
  support: context_only
  snapshot_sha256: 9601df2885c2e7ec95d6afc30169e48a2df21b17d5f26dda4b0c5c3ff53b17a6
  quote: "id: Pfam:PF01697\npfam_id: PF01697\nname: Glycosyltransferase family 92\n\
    short_name: Glyco_transf_92\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01697\n\
    counters:\n  proteins: 12672\n  matches: 12970\n  proteomes: 2717\n  taxa: 6960\n\
    \  structures: 2\n  alphafold_models: 10516\n  domain_architectures: 229\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR008166\ndescription: Members of this family act as galactosyltransferases,\
    \ belonging to glycosyltransferase family\n  92 [[cite:PUB00075505],[cite:PUB00075506],[cite:PUB00075507]].\
    \ The aligned region contains several conserved\n  cysteine residues and several\
    \ charged residues that may be catalytic residues. This is supported by\n  the\
    \ inclusion of this family in the GT-A glycosyl transferase superfamily.\ncuration_history:\
    \ history/records/PF01697\ndiscussions:\n- discussion_id: galt1-purified-enzyme-and-family-coverage\n\
    \  prompt: Resolve GALT-1 assay and construct gaps, and extend GT92 member coverage\
    \ independently.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: Eight graphs\
    \ retain fifteen observed effects across crude-extract biochemistry, two genetic\n\
    \    backgrounds, joint-construct rescue and a selected glycan fraction. Neither\
    \ the full protein's isolated\n    PF01697 domain nor every GT92 member has a\
    \ resolved causal mechanism.\n  evidence:\n  - reference: PMID:19858195\n    supports:\
    \ PARTIAL\n    evidence_source: inspected_primary_html_and_main_figures\n    explanation:\
    \ Product, donor, acceptor, metal and rescue comparisons are supported, but the\
    \ printed\n      MES/metal units, historical clone and supplemental beta1,4 analysis\
    \ need further inspection. All\n      biochemical assays use raw Sf9 extract.\n\
    \  - reference: PMID:20062796\n    supports: PARTIAL\n    evidence_source: inspected_primary_full_text_figures_and_supplement\n\
    \    explanation: The pmk-1 phenotype and selected glycan deficit are supported\
    \ with exon2 allele mapping\n      and peak structural analysis. Lectin staining\
    \ used fut-8 and cannot be transferred to galt-1.\n  notes: Verify 2009 supplemental\
    \ primers/S3 and assay units using an accessible primary copy; current\n    PMC\
    \ PDF returned HTML, publisher403 and ETH429. Distinguish exact long NP_504545.2\
    \ mapping from unverified\n    historical clones, putative DXD chemistry from\
    \ residue tests, and apparent crude-extract Km from intrinsic\n    constants.\
    \ Inspect purified enzyme, other alleles and matched glycome rescue when available.\
    \ Pigeon\n    PMID19959475 and Populus GalS1 PMID36849618 are unintegrated family\
    \ leads; do not transfer nematode\n    core-fucose specificity to plant galactan\
    \ extension/capping. Status remains IN_PROGRESS with partial\n    scientific self-review,\
    \ not family completion.\n  posed_by: Codex\n  posed_date: '2026-10-11'\ncausal_graphs:\n\
    - graph_id: galt1-extract-core-galactosylation\n  title: GALT-1 expression extract\
    \ supports core-fucose-associated galactosylation\n  scope: Titz 2009 Figure 2,\
    \ untagged full-coding-region C. elegans GALT-1 expressed in Sf9 cells; raw\n\
    \    postnuclear extract, not purified protein or isolated domain.\n  context:\
    \ Joint reaction of 0.5 ul extract, 1 mM UDP-Gal and 40 uM dabsyl-GEN[GnGnF6]R\
    \ in 2.5 ul, MES\n    pH6.5 with MnCl2, 2 h at room temperature. HTML prints MES\
    \ 40 uM and MnCl2 10 uM; those unusual units\n    remain unresolved, not silently\
    \ corrected to mM.\n  family_mapping: GALT-1/M03F8.4 maps to O16374, 425 aa, current\
    \ PF01697 189-394. Historical NP_504545.2\n    matches the reference and predates\
    \ the study; the complete experimental clone is not independently\n    verified.\
    \ N-terminal membrane/glycosylation regions extend outside the domain.\n  scope_status:\
    \ MECHANISTIC\n  taxon: NCBITaxon:6239\n  limitations: DIRECT describes the joint\
    \ biochemical preparation-to-product observation, not autonomous\n    purified\
    \ GALT-1 chemistry. Figure 2B's caption reverses the displayed precursor order;\
    \ use parent\n    masses. The exact beta1,4 assignment additionally cites uninspected\
    \ 2009 supplement S3. No elementary\n    catalytic steps or family-wide substrate\
    \ specificity are established.\n  nodes:\n  - node_id: galt1-extract-donor-acceptor\n\
    \    label: Joint GALT-1 expression extract, UDP-Gal and GnGnF6 glycopeptide reaction\n\
    \    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:O16374\n  - node_id:\
    \ core-beta-galactosylated-product\n    label: Core-fucose-associated beta-galactosylated\
    \ glycopeptide product\n    node_type: STATE\n  edges:\n  - edge_id: joint-extract-reaction-produces-product\n\
    \    subject: galt1-extract-donor-acceptor\n    predicate: produces\n    object:\
    \ core-beta-galactosylated-product\n    mechanism: The complete reaction adds\
    \ 162 Da to parent2207, yielding2369; MS/MS fragment1273 locates\n      the added\
    \ hexose with core fucose, and beta-galactosidase removes it. Empty-vector and\
    \ donor-omission\n      controls lack the product.\n    directness: DIRECT\n \
    \   support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:19858195\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2794738/\n\
    \      snippet: postnuclear supernatant\n      explanation: Expression/transferase\
    \ Methods and visually inspected Figure 2A-C support the net extract\n       \
    \ reaction and product assignment; no purified enzyme or independently inspected\
    \ S3 claim.\n      cache_path: evidence/PF01697/titz-2009-galt1.txt\n      cache_sha256:\
    \ f0ead8cfc1653edd653af10e4036c499223c3beeed159a9d829a688a29cb9038\n- graph_id:\
    \ galt1-extract-donor-substitutions\n  title: Donor substitutions lower the product-associated\
    \ HPLC peak\n  scope: Titz 2009 Figure 3A, Sf9 GALT-1 expression extract with\
    \ dansyl-N[GnGnF6]ST, distinct from the\n    dabsylated MS acceptor and lower-extract\
    \ kinetics experiment.\n  context: Standard 0.5-ul raw-extract reaction, 40 uM\
    \ acceptor, 1 mM donor, 2 h at room temperature in\n    2.5 ul MES pH6.5/MnCl2.\
    \ Each indicated UDP sugar replaces UDP-Gal equimolarly. MES40uM/MnCl2-10uM\n\
    \    are the unresolved printed units.\n  family_mapping: Full GALT-1/M03F8.4\
    \ corresponds to O16374/NP_504545.2; PF01697 189-394 within the 425-aa\n    reference.\
    \ These are donor changes to the complete extract reaction, not domain substitutions.\n\
    \  scope_status: MECHANISTIC\n  taxon: NCBITaxon:6239\n  limitations: The 8.06-min\
    \ peak with UDP-Glc is small but nonzero and not chemically identified. Donor\n\
    \    contamination or extract interconversion is not excluded. No universal exclusive\
    \ specificity, purified-enzyme\n    Km or binding affinity is claimed.\n  nodes:\n\
    \  - node_id: replace-with-udp-glc\n    label: Replace UDP-Gal with UDP-Glc\n\
    \    node_type: PERTURBATION\n  - node_id: replace-with-udp-glcnac\n    label:\
    \ Replace UDP-Gal with UDP-GlcNAc\n    node_type: PERTURBATION\n  - node_id: replace-with-udp-galnac\n\
    \    label: Replace UDP-Gal with UDP-GalNAc\n    node_type: PERTURBATION\n  -\
    \ node_id: hplc-product-peak\n    label: Product-associated 8.06-min HPLC peak\n\
    \    node_type: STATE\n  edges:\n  - edge_id: udp-glc-decreases-product-peak\n\
    \    subject: replace-with-udp-glc\n    predicate: decreases\n    object: hplc-product-peak\n\
    \    mechanism: Relative to UDP-Gal, the UDP-Glc reaction gives only a minor peak\
    \ at the product retention\n      time, reported below ten percent; it does not\
    \ establish intrinsic glucosyltransferase activity.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:19858195\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2794738/\n\
    \      snippet: donor specificity\n      explanation: Figure 3A donor-comparison\
    \ traces, associated Results and equimolar-substitution Methods;\n        retain\
    \ the small unresolved UDP-Glc peak.\n      cache_path: evidence/PF01697/titz-2009-galt1.txt\n\
    \      cache_sha256: f0ead8cfc1653edd653af10e4036c499223c3beeed159a9d829a688a29cb9038\n\
    \  - edge_id: udp-glcnac-decreases-product-peak\n    subject: replace-with-udp-glcnac\n\
    \    predicate: decreases\n    object: hplc-product-peak\n    mechanism: The UDP-GlcNAc\
    \ reaction retains the substrate trace without the product peak visible with\n\
    \      UDP-Gal under the matched assay.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:19858195\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2794738/\n      snippet:\
    \ donor specificity\n      explanation: Visually inspected Figure 3A, UDP-GlcNAc\
    \ versus UDP-Gal; limited to this assay's detection\n        and preparation.\n\
    \      cache_path: evidence/PF01697/titz-2009-galt1.txt\n      cache_sha256: f0ead8cfc1653edd653af10e4036c499223c3beeed159a9d829a688a29cb9038\n\
    \  - edge_id: udp-galnac-decreases-product-peak\n    subject: replace-with-udp-galnac\n\
    \    predicate: decreases\n    object: hplc-product-peak\n    mechanism: The UDP-GalNAc\
    \ reaction lacks the product peak visible with UDP-Gal under the matched assay.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:19858195\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2794738/\n\
    \      snippet: donor specificity\n      explanation: Visually inspected Figure\
    \ 3A, UDP-GalNAc versus UDP-Gal; no claim of absolute inactivity\n        in every\
    \ context.\n      cache_path: evidence/PF01697/titz-2009-galt1.txt\n      cache_sha256:\
    \ f0ead8cfc1653edd653af10e4036c499223c3beeed159a9d829a688a29cb9038\n- graph_id:\
    \ galt1-extract-acceptor-substitutions\n  title: Acceptor glycan substitutions\
    \ alter qualitative conversion\n  scope: Titz 2009 Figure 4, dabsyl-GENR glycopeptides\
    \ bearing GnGnF6, MMF6 or MMF3, assayed with whole\n    GALT-1 expression extract.\n\
    \  context: 0.5 ul raw extract, 1 mM UDP-Gal, 40 uM supplied glycopeptide, 2 h\
    \ at room temperature in 2.5\n    ul MES pH6.5/MnCl2. Compare each indicated replacement\
    \ with its named parent substrate; printed buffer/metal\n    units remain unresolved.\n\
    \  family_mapping: Whole O16374-associated GALT-1 contains PF01697 189-394; no\
    \ purified or isolated-domain\n    activity is established by the substrate substitutions.\n\
    \  scope_status: MECHANISTIC\n  taxon: NCBITaxon:6239\n  limitations: Product\
    \ and parent MALDI patterns support qualitative conversion, not absolute rates\
    \ or\n    equivalent ionization efficiencies. MMF6 remains a substrate, so antennal\
    \ GlcNAcs are not strictly\n    required. MMF3 changes the fucose linkage as a\
    \ positional isomer; no cellular glycan necessity is\n    inferred.\n  nodes:\n\
    \  - node_id: gngnf6-to-mmf6\n    label: Replace GnGnF6 with MMF6 lacking antennal\
    \ GlcNAcs\n    node_type: PERTURBATION\n  - node_id: mmf6-to-mmf3\n    label:\
    \ Replace MMF6 with its alpha1,3-core-fucose isomer MMF3\n    node_type: PERTURBATION\n\
    \  - node_id: supplied-acceptor-galactosylation\n    label: Qualitative galactosylation\
    \ of the supplied glycopeptide\n    node_type: ACTIVITY\n  edges:\n  - edge_id:\
    \ mmf6-decreases-conversion-versus-gngnf6\n    subject: gngnf6-to-mmf6\n    predicate:\
    \ decreases\n    object: supplied-acceptor-galactosylation\n    mechanism: GnGnF6\
    \ shows product2369 without visible parent2207, whereas MMF6 retains parent1801\
    \ alongside\n      product1963. The latter is partial conversion, not a lack of\
    \ activity.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:19858195\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC2794738/\n      snippet: acceptor specificity\n\
    \      explanation: Figure 4 first two spectra and 2-h protocol; endpoint represents\
    \ conversion of each\n        supplied substrate, not an identical product mass\
    \ across conditions.\n      cache_path: evidence/PF01697/titz-2009-galt1.txt\n\
    \      cache_sha256: f0ead8cfc1653edd653af10e4036c499223c3beeed159a9d829a688a29cb9038\n\
    \  - edge_id: mmf3-decreases-conversion-versus-mmf6\n    subject: mmf6-to-mmf3\n\
    \    predicate: decreases\n    object: supplied-acceptor-galactosylation\n   \
    \ mechanism: Switching the core fucose from alpha1,6 to alpha1,3 leaves the parent1801\
    \ peak without\n      the product1963 observed for MMF6.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:19858195\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2794738/\n\
    \      snippet: acceptor specificity\n      explanation: Visually inspected Figure\
    \ 4 MMF6/MMF3 spectra, retaining the positional-isomer comparison\n        and\
    \ detection limit.\n      cache_path: evidence/PF01697/titz-2009-galt1.txt\n \
    \     cache_sha256: f0ead8cfc1653edd653af10e4036c499223c3beeed159a9d829a688a29cb9038\n\
    - graph_id: galt1-free-glycan-metal-comparisons\n  title: Metal and EDTA substitutions\
    \ alter the radiolabel readout\n  scope: Titz 2009 Figure 5B, raw GALT-1 expression\
    \ extract, free GnGnF6 glycan and UDP-[14C]Gal; not\n    the peptide assays or\
    \ 12-h TLC comparison.\n  context: Standard 2-h room-temperature reaction with\
    \ 40 uM free acceptor, 1 mM UDP-Gal at 28.5 mCi/mmol,\n    0.5 ul extract in 2.5\
    \ ul. Neutral products counted after AG1-X8 removal of charged donor. MnCl2 is\n\
    \    replaced by equal nominal concentrations of metal chloride, water or Na2EDTA;\
    \ HTML prints 10 uM metal\n    and 40 uM MES, unresolved.\n  family_mapping: The\
    \ extract contains whole C. elegans GALT-1/O16374-associated protein, PF01697\
    \ 189-394\n    in a 425-aa reference. Altering the reaction environment is not\
    \ residue-specific evidence for D289/D291\n    coordination.\n  scope_status:\
    \ MECHANISTIC\n  taxon: NCBITaxon:6239\n  limitations: Readout is product-associated\
    \ neutral-fraction radioactivity, with possible hydrolysis\n    background. Water-added\
    \ extract retains residual cofactors and is not metal-free. Three to seven independent\n\
    \    experiments with SD do not establish a significant Mn/Fe/Co ranking, an exclusive\
    \ Mn requirement or\n    a purified-enzyme metal-binding mechanism.\n  nodes:\n\
    \  - node_id: add-mn-versus-water\n    label: Supply MnCl2 instead of water to\
    \ the extract reaction\n    node_type: PERTURBATION\n  - node_id: add-fe-versus-water\n\
    \    label: Supply Fe(II) chloride instead of water to the extract reaction\n\
    \    node_type: PERTURBATION\n  - node_id: add-co-versus-water\n    label: Supply\
    \ Co(II) chloride instead of water to the extract reaction\n    node_type: PERTURBATION\n\
    \  - node_id: replace-mn-with-edta\n    label: Replace MnCl2 with Na2EDTA\n  \
    \  node_type: PERTURBATION\n  - node_id: neutral-fraction-counts\n    label: Product-associated\
    \ neutral-fraction radiolabel counts\n    node_type: STATE\n  edges:\n  - edge_id:\
    \ mn-increases-counts-versus-water\n    subject: add-mn-versus-water\n    predicate:\
    \ increases\n    object: neutral-fraction-counts\n    mechanism: Mn addition produces\
    \ a higher normalized radiolabel readout than the water-added extract\n      containing\
    \ residual cofactors.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:19858195\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC2794738/\n      snippet: co-factor\
    \ dependence\n      explanation: Figure 5B Mn versus aq bars and assay Methods;\
    \ Figure 5A separately checks radiolabel\n        product migration.\n      cache_path:\
    \ evidence/PF01697/titz-2009-galt1.txt\n      cache_sha256: f0ead8cfc1653edd653af10e4036c499223c3beeed159a9d829a688a29cb9038\n\
    \  - edge_id: fe-increases-counts-versus-water\n    subject: add-fe-versus-water\n\
    \    predicate: increases\n    object: neutral-fraction-counts\n    mechanism:\
    \ The Fe(II) condition produces a higher normalized radiolabel readout than the\
    \ water-added\n      extract; the enzyme's molecular metal occupancy is not measured.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:19858195\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2794738/\n\
    \      snippet: co-factor dependence\n      explanation: Visually inspected Figure\
    \ 5B Fe versus aq; no statistically supported advantage over\n        Mn or Co\
    \ is asserted.\n      cache_path: evidence/PF01697/titz-2009-galt1.txt\n     \
    \ cache_sha256: f0ead8cfc1653edd653af10e4036c499223c3beeed159a9d829a688a29cb9038\n\
    \  - edge_id: co-increases-counts-versus-water\n    subject: add-co-versus-water\n\
    \    predicate: increases\n    object: neutral-fraction-counts\n    mechanism:\
    \ The Co(II) condition produces a higher normalized radiolabel readout than the\
    \ water-added\n      extract; this is not a universal physiological cofactor assignment.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:19858195\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2794738/\n\
    \      snippet: co-factor dependence\n      explanation: Visually inspected Figure\
    \ 5B Co versus aq, mean and SD for the stated extract assay.\n      cache_path:\
    \ evidence/PF01697/titz-2009-galt1.txt\n      cache_sha256: f0ead8cfc1653edd653af10e4036c499223c3beeed159a9d829a688a29cb9038\n\
    \  - edge_id: edta-replacement-decreases-counts\n    subject: replace-mn-with-edta\n\
    \    predicate: decreases\n    object: neutral-fraction-counts\n    mechanism:\
    \ EDTA replacing MnCl2 lowers the readout near the vector-control baseline. It\
    \ is not an\n      EDTA-on-top-of-Mn experiment or proof of literally zero transfer.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:19858195\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2794738/\n\
    \      snippet: co-factor dependence\n      explanation: Figure 5B EDTA/Mn/vector\
    \ bars and Methods specifying replacement at equal concentration.\n      cache_path:\
    \ evidence/PF01697/titz-2009-galt1.txt\n      cache_sha256: f0ead8cfc1653edd653af10e4036c499223c3beeed159a9d829a688a29cb9038\n\
    - graph_id: galt1-unc119-cgl2-development\n  title: The op497 allele increases\
    \ development on CGL2 food in unc-119 animals\n  scope: Titz 2009 Figure 6A, unc-119(ed3);galt-1(op497)\
    \ compared with unc-119(ed3), distinct from the\n    companion pmk-1 experiment.\n\
    \  context: 50-100 newly hatched L1 on NGM containing 1 mM IPTG and 50 ug/ml kanamycin,\
    \ seeded with CGL2-producing\n    BL21(DE3); fraction reaching L4 after72h, three\
    \ replicates with SD. Overnight37C is plate preparation,\n    not an established\
    \ worm assay temperature.\n  family_mapping: M03F8.4/galt-1 corresponds to O16374,\
    \ PF01697 189-394. Companion primary Figure4B maps\n    op497 to a Mos1 insertion\
    \ in exon2; neither exact mutant protein nor domain-specific disruption is\n \
    \   established.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:6239\n  limitations:\
    \ Whole-genotype developmental response is indirect. No toxin-free comparison\
    \ for every line\n    is displayed in this panel; development is not a quantitative\
    \ mortality or binding assay. The separate\n    joint-construct rescue is informative\
    \ but does not make the DUF domain autonomously causal.\n  nodes:\n  - node_id:\
    \ op497-in-unc119\n    label: Add galt-1(op497) to the unc-119(ed3) background\n\
    \    node_type: PERTURBATION\n    grounding:\n    - WormBase:WBGene00019763\n\
    \  - node_id: unc119-cgl2-l4-fraction\n    label: Fraction reaching L4 at72h on\
    \ CGL2 food in the unc-119 comparison\n    node_type: PHENOTYPE\n  edges:\n  -\
    \ edge_id: op497-increases-unc119-l4-fraction\n    subject: op497-in-unc119\n\
    \    predicate: increases\n    object: unc119-cgl2-l4-fraction\n    mechanism:\
    \ The double mutant has a higher L4 fraction than the unc-119 single mutant under\
    \ CGL2 exposure,\n      consistent with reduced developmental sensitivity without\
    \ resolving the intervening molecular sequence.\n    directness: INDIRECT\n  \
    \  support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:19858195\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2794738/\n\
    \      snippet: rescue of CGL2 sensitivity\n      explanation: Figure 6A untransformed\
    \ single/double-mutant bars and developmental Methods, not the\n        separate\
    \ fluorescence endpoint.\n      cache_path: evidence/PF01697/titz-2009-galt1.txt\n\
    \      cache_sha256: f0ead8cfc1653edd653af10e4036c499223c3beeed159a9d829a688a29cb9038\n\
    - graph_id: galt1-joint-construct-cgl2-rescue\n  title: Two integrated joint constructs\
    \ restore CGL2 developmental sensitivity\n  scope: Titz 2009 Figure 6A, opIs444\
    \ and opIs445 in unc-119(ed3);galt-1(op497), each compared with the\n    untransformed\
    \ double mutant.\n  context: pAB15 carries genomic galt-1 with1843bp upstream\
    \ fused to mCherry/let-858 plus the unc-119\n    transformation marker; integrants\
    \ selected by rescue of the unc-119 dauer defect. CGL2-fed L1-to-L4\n    assay\
    \ after72h uses the Figure6 conditions, three replicates with SD.\n  family_mapping:\
    \ Complete GALT-1/M03F8.4 coding region in the fusion maps to O16374-associated\
    \ protein\n    with PF01697 189-394, plus non-domain regions and reporter. The\
    \ integrated arrays additionally rescue\n    the selection-marker phenotype.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:6239\n  limitations: Retain the\
    \ joint intervention, not a pure single-gene rescue. opIs444 is incompletely restored;\n\
    \    no formal equivalence of opIs445 to WT is claimed. The unc-119 single mutant\
    \ is itself CGL2-sensitive.\n    Expression images do not establish marker-verified\
    \ Golgi localization or a resolved toxic mechanism.\n  nodes:\n  - node_id: integrate-opis444\n\
    \    label: Introduce joint galt-1-mCherry and unc-119 marker array opIs444\n\
    \    node_type: PERTURBATION\n  - node_id: integrate-opis445\n    label: Introduce\
    \ joint galt-1-mCherry and unc-119 marker array opIs445\n    node_type: PERTURBATION\n\
    \  - node_id: rescued-cgl2-l4-fraction\n    label: L4 fraction after72h on CGL2\
    \ food relative to the double mutant\n    node_type: PHENOTYPE\n  edges:\n  -\
    \ edge_id: opis444-decreases-l4-fraction\n    subject: integrate-opis444\n   \
    \ predicate: decreases\n    object: rescued-cgl2-l4-fraction\n    mechanism: The\
    \ opIs444 line has a lower L4 fraction than the untransformed double mutant, indicating\n\
    \      partial restoration of CGL2 sensitivity with the joint construct.\n   \
    \ directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:19858195\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2794738/\n\
    \      snippet: rescue of CGL2 sensitivity\n      explanation: Figure 6A opIs444\
    \ comparison and genomic fusion/selection Methods; preserve residual\n       \
    \ development and marker co-rescue.\n      cache_path: evidence/PF01697/titz-2009-galt1.txt\n\
    \      cache_sha256: f0ead8cfc1653edd653af10e4036c499223c3beeed159a9d829a688a29cb9038\n\
    \  - edge_id: opis445-decreases-l4-fraction\n    subject: integrate-opis445\n\
    \    predicate: decreases\n    object: rescued-cgl2-l4-fraction\n    mechanism:\
    \ The opIs445 line has a lower L4 fraction than the untransformed double mutant,\
    \ restoring\n      developmental sensitivity in this joint-construct comparison.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:19858195\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2794738/\n\
    \      snippet: rescue of CGL2 sensitivity\n      explanation: Figure 6A opIs445\
    \ comparison; no demonstrated statistical equality with WT or independent\n  \
    \      control of every insertion effect.\n      cache_path: evidence/PF01697/titz-2009-galt1.txt\n\
    \      cache_sha256: f0ead8cfc1653edd653af10e4036c499223c3beeed159a9d829a688a29cb9038\n\
    - graph_id: galt1-pmk1-cgl2-development\n  title: The op497 allele increases development\
    \ on CGL2 food in pmk-1 animals\n  scope: Butschi 2010 Figure 4A/B, pmk-1(km25);galt-1(op497)\
    \ compared with the CGL2-hypersensitive pmk-1(km25)\n    parent.\n  context: Mos1-selected\
    \ insertion mutants were outcrossed two to six times; 50-100 newly hatched L1\
    \ on\n    CGL2-producing BL21(DE3), fraction reaching L4 after72h. Plates were\
    \ prepared overnight at23C; assay-specific\n    animal temperature is not restated.\n\
    \  family_mapping: Figure4B identifies op497 in the second exon of M03F8.4/galt-1,\
    \ O16374-associated 425-aa\n    protein with PF01697 189-394. No domain-specific\
    \ knockout or mutant protein length is established.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:6239\n  limitations: Published statistical comparisons are\
    \ to N2, not the zero-L4 pmk-1 population. The observation\n    is developmental\
    \ resistance in this genetic background, not a direct glycan-binding measurement.\
    \ Figure6\n    lectin staining tests fut-8, not galt-1. Rescue from the unc-119\
    \ study is not a matched rescue in\n    pmk-1.\n  nodes:\n  - node_id: op497-in-pmk1\n\
    \    label: Add galt-1(op497) to the pmk-1(km25) background\n    node_type: PERTURBATION\n\
    \    grounding:\n    - WormBase:WBGene00019763\n  - node_id: pmk1-cgl2-l4-fraction\n\
    \    label: Fraction reaching L4 at72h on CGL2 food in the pmk-1 comparison\n\
    \    node_type: PHENOTYPE\n  edges:\n  - edge_id: op497-increases-pmk1-l4-fraction\n\
    \    subject: op497-in-pmk1\n    predicate: increases\n    object: pmk1-cgl2-l4-fraction\n\
    \    mechanism: The insertion-bearing double mutant develops to L4 at a higher\
    \ fraction than pmk-1 alone\n      under CGL2 feeding; the intermediate molecular\
    \ events are not tracked in this assay.\n    directness: INDIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:20062796\n\
    \      source_url: https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1000717\n\
    \      snippet: fraction of animals\n      explanation: Visually inspected Figure4A/B\
    \ and developmental/Mos1 Methods; no genotype-wide mortality\n        or lectin-staining\
    \ inference.\n      cache_path: evidence/PF01697/butschi-2010-galt1.txt\n    \
    \  cache_sha256: 5a614d50bcb2ca9673a0330b8a74394729d4fd748db926e61e0e5dcdac391024\n\
    - graph_id: galt1-pmk1-selected-glycan-peak\n  title: The op497 genotype reduces\
    \ a selected core-galactosylated glycan peak\n  scope: Butschi 2010 Figure7, pmk-1(km25);galt-1(op497)\
    \ versus pmk-1(km25); selected PNGaseF-resistant/PNGaseA-sensitive\n    N-glycan\
    \ fraction, not the entire glycome.\n  context: Five-day room-temperature liquid\
    \ OP50 cultures, no CGL2 exposure in this preparation. Sequential\n    PNGase\
    \ release, PA labeling, NP-HPLC fraction34.0-35.5min followed by RP-HPLC; selected\
    \ peakA near14.5min\n    is characterized by MS/MS and exoglycosidases, including\
    \ supplement FigureS2.\n  family_mapping: Whole-gene Mos1 op497 perturbs M03F8.4/galt-1,\
    \ associated with O16374 and its PF01697\n    interval189-394. This indirect whole-animal\
    \ glycan change does not locate the intervention within\n    the domain or prove\
    \ purified-domain catalysis.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:6239\n\
    \  limitations: Qualitative selected-peak comparison, not calibrated total glycan\
    \ abundance, replicated\n    quantitative glycomics or a matched glycome rescue.\
    \ The analogous fut-8 mutant is a separate perturbation.\n    The biochemical\
    \ extract product and toxin-development readouts are not joined into an entirely\
    \ observed\n    causal sequence.\n  nodes:\n  - node_id: op497-pmk1-glycome-preparation\n\
    \    label: Substitute pmk-1;galt-1(op497) for pmk-1 in the glycome comparison\n\
    \    node_type: PERTURBATION\n    grounding:\n    - WormBase:WBGene00019763\n\
    \  - node_id: selected-core-galactosylated-peak\n    label: Selected core-galactosylated\
    \ Hex5dHex2HexNAc2-PA peakA\n    node_type: STATE\n  edges:\n  - edge_id: op497-decreases-selected-peak\n\
    \    subject: op497-pmk1-glycome-preparation\n    predicate: decreases\n    object:\
    \ selected-core-galactosylated-peak\n    mechanism: PeakA present in pmk-1 is\
    \ not detected in the double-mutant selected fraction. Parent1605/core\n     \
    \ fragment753 and sequential galactosidase/fucosidase changes support its core-galactosylated\
    \ assignment,\n      without making the genotype effect direct chemistry.\n  \
    \  directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:20062796\n      source_url: https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1000717\n\
    \      snippet: Peak A\n      explanation: Figure7A-C, glycan preparation/analysis\
    \ Methods, and visually inspected one-page supplement\n        FigureS2; the supplement\
    \ characterizes the isolated peak, not quantitative genotype replication.\n  \
    \    cache_path: evidence/PF01697/butschi-2010-galt1.txt\n      cache_sha256:\
    \ 5a614d50bcb2ca9673a0330b8a74394729d4fd748db926e61e0e5dcdac391024\ncuration_events:\n\
    - timestamp: '2026-10-11T13:53:53Z'\n  curator: Codex\n  action: CREATE\n  outcome:\
    \ changed\n  summary: Curate scoped GALT-1 biochemical, developmental and glycan\
    \ effects\n  history_record: history/records/PF01697/2026-10-11T135353Z-codex-ae67e3.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: O16374 GALT1_CAEEL is a 425-aa C. elegans reference, sequence version4,
    with current PF01697 189-394 and exact InterPro sequence identity. RefSeq NP_504545.2
    is identical and replaced the incomplete274-aa NP_504545.1 in June2008, before
    the primary study. The paper's full coding N2 cDNA and N109/N152/D289/D291 positions
    fit the long model but do not prove every historical clone sequence. Predicted
    membrane/glycosylation regions lie outside the domain. op497 is an exon2 Mos1
    insertion, not a mapped isolated-domain deletion or proven complete null. The
    two primary genetic backgrounds are not interchangeable.
  target_ids:
  - PF01697
  evidence_ids:
  - identity
  - primary
  - companion-genotype-and-glycome
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: The ten direct edges are scoped to crude-extract biochemical interventions,
    not autonomous purified GALT-1 catalysis. Product2207-to2369, fragment1273 and
    beta-galactosidase sensitivity support core-associated beta-galactosylation; the
    exact beta1,4 supplemental analysis from2009 was not independently inspected.
    Donor substitutions retain a small unresolved UDP-Glc peak. Acceptor comparisons
    are qualitative and MMF6 retains activity. Mn/Fe/Co versus water and EDTA replacing
    Mn affect neutral-fraction radiolabel without proving metal coordination or exact
    physiological specificity. Five indirect edges retain unc-119 op497, two joint-integrant
    rescues, pmk-1 op497 developmental resistance and loss of selected glycan peakA.
    Main Figure7 and supplementS2 support the latter peak's structural assignment.
    No CGL2-staining edge is attributed to galt-1 because that experiment tested fut-8;
    no chain joins all contexts as directly observed.
  target_ids:
  - PF01697
  evidence_ids:
  - primary
  - native
  - companion-genotype-and-glycome
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Historical full clone verification, 2009 supplements and printed MES/metal
    unit resolution remain open. Purified enzyme, residue-specific DXD tests, independent
    alleles, matched genotype glycome rescue, complete glycome quantification and
    plant/other-member experiments are not integrated. Pigeon PMID19959475 and Populus
    GalS1 PMID36849618 are follow-up leads, not adopted edges. Current reference mapping
    and EX_DUF naming do not establish family-wide nematode core-fucose specificity.
  target_ids:
  - PF01697
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01697-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve extract protocol and historical construct gaps and broaden GT92 coverage
  description: Inspect accessible 2009 supplements and an authoritative assay-unit
    source, verify complete historical constructs, and evaluate purified GALT-1 or
    additional allele/rescue evidence without upgrading mixture results into isolated-domain
    chemistry. Extend other GT92 members only after member-specific domain mapping
    and primary Methods/figure review, including plant galactan/capping and pigeon
    leads. Keep the partial-review status and exact experimental boundaries in successor
    curation.
  target_ids:
  - PF01697
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - companion-genotype-and-glycome
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01697.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Inspect accessible 2009 supplements and an authoritative assay-unit
    source, verify complete historical constructs, and evaluate purified GALT-1 or
    additional allele/rescue evidence without upgrading mixture results into isolated-domain
    chemistry. Extend other GT92 members only after member-specific domain mapping
    and primary Methods/figure review, including plant galactan/capping and pigeon
    leads. Keep the partial-review status and exact experimental boundaries in successor
    curation.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01697
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Titz 2009 Figures2-6 and Butschi 2010 Figures4/7 plus one-page supplementS2 were
  visually inspected. The 2009 supplemental primer/MS data and Figure8 alignment were
  not independently visually assessed. PMC's 2009 PDF request returned HTML, publisher
  access returned403 and ETH returned429; the primary PMC HTML was readable. No raw
  data reprocessing, calibrated digitization, clone resequencing, independent experimental
  replication or exhaustive family survey was performed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
