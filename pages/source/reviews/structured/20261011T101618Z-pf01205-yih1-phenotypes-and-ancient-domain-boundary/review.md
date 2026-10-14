# Scoped scientific self-review of Yih1 phenotypes and ancient-domain mapping

- Review: 20261011T101618Z-pf01205-yih1-phenotypes-and-ancient-domain-boundary
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T10:16:05Z
- Finished UTC: 2026-10-11T10:16:18Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Three PHENOTYPIC graphs retain three INDIRECT OBSERVED effects for H1511 phosphorylation and separate H1511/ESY11001b starvation growth. PF01205 maps to the C-terminal ancient domain, not the RWD. Whole-protein overexpression is not promoted to isolated-domain activity. Partial scientific self-review; IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01205 Impact_N, next accession-ordered SEEDED family, assessed through Sattlegger 2011 and exact reference/domain mapping; the 2015 cell-cycle abstract is a separate coverage lead.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01205 | data/families/PF01205.yaml | generated | PF01205 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01205 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01205.

The cited GI 6319904 resolves to NP_009985.1 and exactly matches P25637/YCR059C, 258 aa and sequence version 1. PF01205 is 144-251, in the C-terminal ancient domain; PF05773 RWD is separately 6-108. This contradicts using the preserved Impact_N label as a coordinate definition. P40512/PCI8/CSN11 is an unrelated YIH1 synonym. Experimental H1511 and ESY11001b are retained separately from the S288c reference.

### Directed effects and limits

graph: supported. Targets: PF01205.

All three edges are indirect phenotypes, not purified kinase or phosphatase reactions. Galactose overexpression, GST-only and nonstarved controls are explicit. Liquid 10-mM/1-h treatment is not transferred to plates. The two host backgrounds and phosphorylation endpoint are separate graphs; the deletion-background comparison is not misrepresented as rescue. No isolated PF01205 activity, local translation increase, actin-switch trajectory or bacterial/archaeal mechanism is inferred.

### Remaining family coverage

completeness: concern. Targets: PF01205.

Exact historical host/fusion sequences and plate dose, time and temperature remain unresolved. Full 2004 competition experiments and mammalian studies are unreviewed; 2015 cell-cycle results were assessed only at abstract level. The preserved source label needs separate upstream identity review, and ancient-domain-specific functional evidence remains incomplete. Raw blots, growth kinetics and structural coordinates were not reanalyzed.

## Findings

### additional-contexts: Resolve PF01205 domain-specific mechanism and source-label ambiguity

minor / open / confirmed; issue key: pf01205-causal-context-coverage.

Keep whole-protein phenotypes separate from RWD and ancient-domain activities. Obtain plate conditions and full constructs, investigate the source-maintained N-terminal wording without rewriting frozen snapshots, and assess domain-specific perturbations plus 2004 competition, 2015 cell-cycle and mammalian contexts. Retain a successor review before extending mechanistic claims.

## Recommended Actions And Acceptance Checks

### extend-contexts

Keep whole-protein phenotypes separate from RWD and ancient-domain activities. Obtain plate conditions and full constructs, investigate the source-maintained N-terminal wording without rewriting frozen snapshots, and assess domain-specific perturbations plus 2004 competition, 2015 cell-cycle and mammalian contexts. Retain a successor review before extending mechanistic claims.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC3060488/; Main Methods/Table 1, fragment and mutant Results, ancient-domain analysis and Discussion; Figures 2 and 5 visually inspected | supports | GST-Yih1(2-258) overexpression lowers the normalized Ser51-eIF2alpha phosphorylation signal in 3AT-treated H1511 and reduces starvation plate growth in both H1511 and its yih1 deletion derivative. RWD-only 2-132 inhibits despite lacking PF01205; the ancient-domain fragment is insufficient. Binding and inhibition do not correlate for every fragment. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/P25637/entry/pfam/PF01205/; Accession and domain locations; paired UniProt identity facts | supports | The cited GI 6319904 resolves to NP_009985.1 and exactly matches P25637/YCR059C, 258 aa and sequence version 1. PF01205 is 144-251, in the C-terminal ancient domain; PF05773 RWD is separately 6-108. This contradicts using the preserved Impact_N label as a coordinate definition. P40512/PCI8/CSN11 is an unrelated YIH1 synonym. Experimental H1511 and ESY11001b are retained separately from the S288c reference. |
| cited-gi-reference | https://www.ncbi.nlm.nih.gov/protein/NP_009985.1; GI 6319904 FASTA resolution and full sequence comparison with P25637 | supports | Exact current sequence agreement grounds YCR059C identity but does not reconstruct every historical fusion or host genotype. |
| separate-rwd-domain | https://www.ebi.ac.uk/interpro/api/protein/uniprot/P25637/entry/pfam/PF05773/; Current RWD domain interval 6-108, separate from PF01205 144-251 | supports | The kinase-regulating N-terminal RWD is a different Pfam domain; its activity is not assigned to PF01205 merely from the Impact_N name. |
| later-cell-cycle-lead | https://pmc.ncbi.nlm.nih.gov/articles/PMC4503747/; Abstract only | supports | Reports Gcn1/Gcn2-independent deletion-associated cell-cycle behavior and Cdc28 association requiring separate experimental assessment; no adopted edge comes from this abstract. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01205 | data/families/PF01205.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Figures 2 and 5 were visually inspected, alongside main Methods/Table 1 and selected fragment/mutant and ancient-domain Results/Discussion. Other plotted data, raw measurements and full historical clone sequences were not independently checked. Truncated-construct labels and confusing H3 growth wording are retained as limits; no mutant edge is adopted.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T101618Z-pf01205-yih1-phenotypes-and-ancient-domain-boundary
title: Scoped scientific self-review of Yih1 phenotypes and ancient-domain mapping
started_at: '2026-10-11T10:16:05Z'
finished_at: '2026-10-11T10:16:18Z'
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
summary: Three PHENOTYPIC graphs retain three INDIRECT OBSERVED effects for H1511
  phosphorylation and separate H1511/ESY11001b starvation growth. PF01205 maps to
  the C-terminal ancient domain, not the RWD. Whole-protein overexpression is not
  promoted to isolated-domain activity. Partial scientific self-review; IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01205.yaml
    sha256: 74fb2959d23a63bc0885be5ad17855b3c89d452f0f763f9e4d252c35d47b248e
    role: context
  - path: data/families/PF01205.yaml
    sha256: a009d9d1d17ef31518a1b870f94f54434a598a383518fb37727d2e3ebdec35a6
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
  - path: evidence/PF01205/sattlegger-2011-yih1.txt
    role: context
    sha256: f776cf4550f706bfd69a326ac6302e924bae946d206ea3b7f1b7bbfb405e918e
  - path: evidence/PF01205/Yih1-identity.txt
    role: context
    sha256: e71f725f87e8872f3b3b88a93451dcee7bbcc721ad28b04032060d51a3e2f59d
  - path: evidence/PF01205/yih1-2015-coverage-lead.txt
    role: context
    sha256: aa9df65dcf572d354ea4cb2f674104774398916ecf49cf3e162cfc318e3b6e61
targets:
- target_id: PF01205
  path: data/families/PF01205.yaml
  label: PF01205
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01205.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 389211e4cb173634320282308e99355978fb2fcf5dc3e3744863de1ef0d23e7f
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01205 Impact_N, next accession-ordered SEEDED family, assessed through
    Sattlegger 2011 and exact reference/domain mapping; the 2015 cell-cycle abstract
    is a separate coverage lead.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01205
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Exact historical host/fusion sequences and plate dose, time and temperature
      remain unresolved. Full 2004 competition experiments and mammalian studies are
      unreviewed; 2015 cell-cycle results were assessed only at abstract level. The
      preserved source label needs separate upstream identity review, and ancient-domain-specific
      functional evidence remains incomplete. Raw blots, growth kinetics and structural
      coordinates were not reanalyzed.
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
  - PF01205
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3060488/
  locator: Main Methods/Table 1, fragment and mutant Results, ancient-domain analysis
    and Discussion; Figures 2 and 5 visually inspected
  accessed_at: '2026-10-11T10:16:18Z'
  support: supports
  snapshot_sha256: f776cf4550f706bfd69a326ac6302e924bae946d206ea3b7f1b7bbfb405e918e
  summary: GST-Yih1(2-258) overexpression lowers the normalized Ser51-eIF2alpha phosphorylation
    signal in 3AT-treated H1511 and reduces starvation plate growth in both H1511
    and its yih1 deletion derivative. RWD-only 2-132 inhibits despite lacking PF01205;
    the ancient-domain fragment is insufficient. Binding and inhibition do not correlate
    for every fragment.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P25637/entry/pfam/PF01205/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T10:16:18Z'
  support: supports
  snapshot_sha256: e71f725f87e8872f3b3b88a93451dcee7bbcc721ad28b04032060d51a3e2f59d
  summary: The cited GI 6319904 resolves to NP_009985.1 and exactly matches P25637/YCR059C,
    258 aa and sequence version 1. PF01205 is 144-251, in the C-terminal ancient domain;
    PF05773 RWD is separately 6-108. This contradicts using the preserved Impact_N
    label as a coordinate definition. P40512/PCI8/CSN11 is an unrelated YIH1 synonym.
    Experimental H1511 and ESY11001b are retained separately from the S288c reference.
- evidence_id: cited-gi-reference
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/protein/NP_009985.1
  locator: GI 6319904 FASTA resolution and full sequence comparison with P25637
  summary: Exact current sequence agreement grounds YCR059C identity but does not
    reconstruct every historical fusion or host genotype.
  accessed_at: '2026-10-11T10:16:18Z'
  support: supports
  snapshot_sha256: e71f725f87e8872f3b3b88a93451dcee7bbcc721ad28b04032060d51a3e2f59d
- evidence_id: separate-rwd-domain
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P25637/entry/pfam/PF05773/
  locator: Current RWD domain interval 6-108, separate from PF01205 144-251
  summary: The kinase-regulating N-terminal RWD is a different Pfam domain; its activity
    is not assigned to PF01205 merely from the Impact_N name.
  accessed_at: '2026-10-11T10:16:18Z'
  support: supports
  snapshot_sha256: e71f725f87e8872f3b3b88a93451dcee7bbcc721ad28b04032060d51a3e2f59d
- evidence_id: later-cell-cycle-lead
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4503747/
  locator: Abstract only
  summary: Reports Gcn1/Gcn2-independent deletion-associated cell-cycle behavior and
    Cdc28 association requiring separate experimental assessment; no adopted edge
    comes from this abstract.
  accessed_at: '2026-10-11T10:16:18Z'
  support: supports
  snapshot_sha256: aa9df65dcf572d354ea4cb2f674104774398916ecf49cf3e162cfc318e3b6e61
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T10:16:18Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01205
  kind: record_content
  reference: data/families/PF01205.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T10:16:18Z'
  support: context_only
  snapshot_sha256: a009d9d1d17ef31518a1b870f94f54434a598a383518fb37727d2e3ebdec35a6
  quote: "id: Pfam:PF01205\npfam_id: PF01205\nname: Impact N-terminal domain\nshort_name:\
    \ Impact_N\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01205\n\
    counters:\n  proteins: 18592\n  matches: 18629\n  proteomes: 16361\n  taxa: 26223\n\
    \  structures: 5\n  alphafold_models: 12878\n  domain_architectures: 121\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR001498\ndescription: This entry represents the N-terminal\
    \ domain of the Impact proteins. The Impact protein is\n  a translational regulator\
    \ that ensures constant high levels of translation under amino acid starvation.\n\
    \  It acts by interacting with Gcn1/Gcn1L1, thereby preventing activation of Gcn2\
    \ protein kinases (EIF2AK1\n  to 4) and subsequent down-regulation of protein\
    \ synthesis [[cite:PUB00161305],[cite:PUB00158485]]. It\n  is evolutionary conserved\
    \ from eukaryotes to archaea [[cite:PUB00046141]].\ncuration_history: history/records/PF01205\n\
    discussions:\n- discussion_id: impact-ancient-domain-mechanism-and-name-boundary\n\
    \  prompt: Resolve the ancient-domain mechanism separately from RWD-driven Yih1\
    \ phenotypes.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: PF01205 maps\
    \ to C-terminal residues 144-251 despite the frozen Impact_N name. Three whole-protein\n\
    \    phenotypes do not establish this domain's isolated mechanism.\n  evidence:\n\
    \  - reference: PMID:21239490\n    supports: PARTIAL\n    evidence_source: inspected_primary_methods_and_results\n\
    \    explanation: RWD-only fragments inhibit without PF01205, while the ancient-domain\
    \ fragment is insufficient.\n      Binding alone and modeled actin switching are\
    \ not directed causal proof.\n  - reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4503747/\n\
    \    supports: PARTIAL\n    evidence_source: primary_abstract_only\n    explanation:\
    \ A later study reports Gcn1/Gcn2-independent cell-cycle effects requiring separate\
    \ full-text\n      and construct review.\n  notes: Preserve frozen identity metadata\
    \ but investigate its N-terminal wording in the source-maintained\n    workflow.\
    \ Obtain exact fusion/host sequences and plate conditions; review 2004 competition,\
    \ 2015 cell-cycle\n    and mammalian studies separately. Do not generalize to\
    \ bacterial YigZ or archaea. The PCI8/CSN11 YIH1\n    synonym is excluded. Partial\
    \ same-agent scientific assessment; remain IN_PROGRESS.\n  posed_by: Codex\n \
    \ posed_date: '2026-10-11'\ncausal_graphs:\n- graph_id: yih1-h1511-starvation-phosphorylation\n\
    \  title: GST-Yih1 overexpression lowers starvation-induced eIF2alpha phosphorylation\n\
    \  scope: Saccharomyces cerevisiae H1511 expressing N-terminal GST-Yih1(2-258)\
    \ from pES187-B1 versus GST\n    alone in Sattlegger 2011 Figure 5C/D. This is\
    \ a whole-protein overexpression phenotype.\n  context: Galactose-induced exponential\
    \ cultures are treated with 10 mM 3AT for 1 h before harvesting.\n    Immunoblots\
    \ measure Ser51-phosphorylated eIF2alpha relative to total eIF2alpha; at least\
    \ two independent\n    transformants and SE are reported. Plate-growth conditions\
    \ are separate.\n  family_mapping: P25637/YIH1_YEAST is YCR059C, 258 aa, sequence\
    \ version 1; the cited GI 6319904 resolves\n    to matching NP_009985.1. PF01205\
    \ maps to 144-251 in the C-terminal ancient domain, despite the preserved\n  \
    \  Impact_N label. PF05773 RWD is separately at 6-108. The 2-258 fusion retains\
    \ both; exact historical\n    junctions remain unverified. P40512/PCI8 is an unrelated\
    \ YIH1 synonym.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:4932\n  limitations:\
    \ Figure 2 confirms overexpression, not physiological dosage. RWD-only 2-132 lacks\
    \ PF01205\n    yet inhibits, whereas 133-258 retains PF01205 but has little effect.\
    \ This does not establish isolated\n    PF01205 inhibition, direct eIF2alpha dephosphorylation\
    \ or increased total translation. Binding and\n    modeled actin switching are\
    \ not an observed causal chain.\n  nodes:\n  - node_id: overexpress-gst-yih1-h1511\n\
    \    label: Express GST-Yih1(2-258) instead of GST alone in H1511\n    node_type:\
    \ PERTURBATION\n    grounding:\n    - UniProtKB:P25637\n  - node_id: starvation-eif2alpha-phosphorylation\n\
    \    label: Ser51-phosphorylated eIF2alpha relative to total eIF2alpha after 3AT\n\
    \    node_type: STATE\n  edges:\n  - edge_id: yih1-overexpression-decreases-eif2alpha-phosphorylation\n\
    \    subject: overexpress-gst-yih1-h1511\n    predicate: decreases\n    object:\
    \ starvation-eif2alpha-phosphorylation\n    mechanism: The overexpressed multidomain\
    \ fusion decreases the normalized phosphorylation signal under\n      the specified\
    \ starvation treatment. Gcn2 regulation is the mechanistic interpretation, not\
    \ a directly\n      measured isolated-domain reaction in this assay.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:21239490\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3060488/\n\
    \      snippet: phosphorylation\n      explanation: Visually inspected Figures\
    \ 2 and 5C/D, main Methods and fragment Results; GST and total-eIF2alpha\n   \
    \     controls constrain the endpoint.\n      cache_path: evidence/PF01205/sattlegger-2011-yih1.txt\n\
    \      cache_sha256: f776cf4550f706bfd69a326ac6302e924bae946d206ea3b7f1b7bbfb405e918e\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P25637/entry/pfam/PF01205/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P25637/entry/pfam/PF01205/\n\
    \      snippet: 'P25637 Pfam:PF01205 interval: 144-251, inclusive.'\n      explanation:\
    \ Exact reference mapping places this family in the ancient domain, not in the\
    \ separate\n        N-terminal RWD. Whole-protein effects cannot be assigned to\
    \ PF01205 alone.\n      cache_path: evidence/PF01205/Yih1-identity.txt\n     \
    \ cache_sha256: e71f725f87e8872f3b3b88a93451dcee7bbcc721ad28b04032060d51a3e2f59d\n\
    - graph_id: yih1-h1511-starvation-growth\n  title: GST-Yih1 overexpression reduces\
    \ H1511 growth under 3AT starvation\n  scope: H1511 with endogenous YIH1 and plasmid-borne\
    \ GST-Yih1(2-258) versus GST-only control in Figure\n    5A.\n  context: Spot\
    \ 5 ul of tenfold serial dilutions of overnight cultures on synthetic minimal\
    \ galactose\n    medium with or without 3AT. The inspected 2011 caption does not\
    \ specify plate 3AT concentration, incubation\n    temperature or duration; the\
    \ liquid 10-mM/1-h protocol is not transferred.\n  family_mapping: The YCR059C\
    \ fusion maps to P25637 with PF01205 at 144-251 and separate RWD at 6-108.\n \
    \   Endogenous Yih1 remains present in this host. Current reference identity does\
    \ not reconstruct every\n    historical host or plasmid sequence.\n  scope_status:\
    \ PHENOTYPIC\n  taxon: NCBITaxon:4932\n  limitations: Growth is an indirect integrated\
    \ phenotype, not direct kinase activity, viability loss\n    or a quantified growth\
    \ rate. Nonstarved plates constrain starvation specificity. This is not a normal-expression\n\
    \    loss-of-function assay or an isolated ancient-domain effect.\n  nodes:\n\
    \  - node_id: overexpress-yih1-wt-background\n    label: Overexpress GST-Yih1(2-258)\
    \ versus GST alone in H1511\n    node_type: PERTURBATION\n    grounding:\n   \
    \ - UniProtKB:P25637\n  - node_id: h1511-3at-plate-growth\n    label: H1511 dilution-series\
    \ growth on galactose plus 3AT\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ overexpression-decreases-h1511-starvation-growth\n    subject: overexpress-yih1-wt-background\n\
    \    predicate: decreases\n    object: h1511-3at-plate-growth\n    mechanism:\
    \ The full multidomain fusion reduces colony growth under the starvation challenge\
    \ compared\n      with GST alone. The effect is consistent with impaired starvation\
    \ adaptation, without assigning\n      direct toxicity or domain-local catalysis.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:21239490\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3060488/\n\
    \      snippet: 3AT\n      explanation: Visually inspected Figure 5A with its\
    \ nonstarved control, Figure 2 expression analysis,\n        Methods/Table 1 and\
    \ corresponding Results.\n      cache_path: evidence/PF01205/sattlegger-2011-yih1.txt\n\
    \      cache_sha256: f776cf4550f706bfd69a326ac6302e924bae946d206ea3b7f1b7bbfb405e918e\n\
    - graph_id: yih1-deletion-background-starvation-growth\n  title: GST-Yih1 expression\
    \ reduces starvation growth without endogenous Yih1\n  scope: ESY11001b, the H1511-derived\
    \ yih1 deletion strain, expressing GST-Yih1(2-258) versus GST alone\n    in Figure\
    \ 5B.\n  context: The same 5-ul tenfold dilution plate assay uses galactose minimal\
    \ medium with or without 3AT.\n    Plate dose, time and temperature remain unverified;\
    \ the deletion background is not combined with the\n    H1511 phosphorylation\
    \ assay.\n  family_mapping: The expressed P25637-mapped 2-258 fusion contains\
    \ PF01205 144-251 and RWD 6-108. Endogenous\n    YIH1 is deleted by the reported\
    \ PCR-based construction; exact deletion junctions and fusion scars\n    were\
    \ not reconstructed.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:4932\n  limitations:\
    \ This comparison shows that the overexpression-associated growth effect does\
    \ not require\n    endogenous Yih1. It is not rescue of a deletion defect. Figure\
    \ 5B's truncated-construct labels differ\n    from Table 1, but its adopted 2-258\
    \ row is unambiguous; those truncated rows are not new edges.\n  nodes:\n  - node_id:\
    \ express-yih1-in-deletion-background\n    label: Express GST-Yih1(2-258) versus\
    \ GST in ESY11001b\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:P25637\n\
    \  - node_id: esy11001b-3at-plate-growth\n    label: ESY11001b dilution-series\
    \ growth on galactose plus 3AT\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ fusion-decreases-deletion-background-starvation-growth\n    subject: express-yih1-in-deletion-background\n\
    \    predicate: decreases\n    object: esy11001b-3at-plate-growth\n    mechanism:\
    \ Expressing the multidomain fusion reduces the starvation-growth endpoint even\
    \ when endogenous\n      Yih1 is absent. This limits an endogenous-protein bridging\
    \ explanation for this phenotype, but does\n      not resolve the biochemical\
    \ role of PF01205.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:21239490\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC3060488/\n      snippet: 3AT\n    \
    \  explanation: Figure 5B was visually inspected separately from panel A; Methods\
    \ identify ESY11001b\n        as the H1511-derived yih1 deletion strain.\n   \
    \   cache_path: evidence/PF01205/sattlegger-2011-yih1.txt\n      cache_sha256:\
    \ f776cf4550f706bfd69a326ac6302e924bae946d206ea3b7f1b7bbfb405e918e\ncuration_events:\n\
    - timestamp: '2026-10-11T10:08:17Z'\n  curator: Codex\n  action: CREATE\n  outcome:\
    \ changed\n  summary: Curate three scoped Yih1 overexpression phenotypes with\
    \ ancient-domain mapping\n  history_record: history/records/PF01205/2026-10-11T100817Z-codex-2487b9.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: The cited GI 6319904 resolves to NP_009985.1 and exactly matches P25637/YCR059C,
    258 aa and sequence version 1. PF01205 is 144-251, in the C-terminal ancient domain;
    PF05773 RWD is separately 6-108. This contradicts using the preserved Impact_N
    label as a coordinate definition. P40512/PCI8/CSN11 is an unrelated YIH1 synonym.
    Experimental H1511 and ESY11001b are retained separately from the S288c reference.
  target_ids:
  - PF01205
  evidence_ids:
  - identity
  - primary
  - cited-gi-reference
  - separate-rwd-domain
  - later-cell-cycle-lead
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: All three edges are indirect phenotypes, not purified kinase or phosphatase
    reactions. Galactose overexpression, GST-only and nonstarved controls are explicit.
    Liquid 10-mM/1-h treatment is not transferred to plates. The two host backgrounds
    and phosphorylation endpoint are separate graphs; the deletion-background comparison
    is not misrepresented as rescue. No isolated PF01205 activity, local translation
    increase, actin-switch trajectory or bacterial/archaeal mechanism is inferred.
  target_ids:
  - PF01205
  evidence_ids:
  - primary
  - native
  - cited-gi-reference
  - separate-rwd-domain
  - later-cell-cycle-lead
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Exact historical host/fusion sequences and plate dose, time and temperature
    remain unresolved. Full 2004 competition experiments and mammalian studies are
    unreviewed; 2015 cell-cycle results were assessed only at abstract level. The
    preserved source label needs separate upstream identity review, and ancient-domain-specific
    functional evidence remains incomplete. Raw blots, growth kinetics and structural
    coordinates were not reanalyzed.
  target_ids:
  - PF01205
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01205-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve PF01205 domain-specific mechanism and source-label ambiguity
  description: Keep whole-protein phenotypes separate from RWD and ancient-domain
    activities. Obtain plate conditions and full constructs, investigate the source-maintained
    N-terminal wording without rewriting frozen snapshots, and assess domain-specific
    perturbations plus 2004 competition, 2015 cell-cycle and mammalian contexts. Retain
    a successor review before extending mechanistic claims.
  target_ids:
  - PF01205
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - cited-gi-reference
  - separate-rwd-domain
  - later-cell-cycle-lead
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01205.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Keep whole-protein phenotypes separate from RWD and ancient-domain
    activities. Obtain plate conditions and full constructs, investigate the source-maintained
    N-terminal wording without rewriting frozen snapshots, and assess domain-specific
    perturbations plus 2004 competition, 2015 cell-cycle and mammalian contexts. Retain
    a successor review before extending mechanistic claims.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01205
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Figures 2 and 5 were visually inspected, alongside main Methods/Table 1 and selected
  fragment/mutant and ancient-domain Results/Discussion. Other plotted data, raw measurements
  and full historical clone sequences were not independently checked. Truncated-construct
  labels and confusing H3 growth wording are retained as limits; no mutant edge is
  adopted.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
