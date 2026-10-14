# PF01757 SaOatA observed assay effects and hypothetical acetyl relay

- Review: 20261011T145601Z-pf01757-oata-assay-effects-and-hypothetical-relay
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T14:55:48Z
- Finished UTC: 2026-10-11T14:56:01Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Five graphs retain twenty-two observed effects, sixteen direct preparation effects and six indirect cellular effects, plus two explicitly hypothetical relay steps. Product formation, CoASH release, glycan transfer, PG acetylation and tunicamycin-dependent growth remain separate contexts. Deposited untreated Tyr206 acetylation and the MS search-reference extra substitutions limit direct causal attribution. Partial coverage remains IN_PROGRESS.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Pending PF01757 within all 8296 frozen families; selected SaOatA2021 experiments are partial coverage, not family or corpus completion.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01757 | data/families/PF01757.yaml | generated | PF01757 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01757 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01757.

Q2FV54 and USA300 A0A0H2XFE4/SAUSA300_2504 exactly match versioned603-aa ABD21303.1. Current PF01757 is19-344; H36/E154/Y206 lie inside, E357/S453 and isolated C-domain445-601 outside. WT MS search reference is not clone resequencing. The ATCC6538 topology library is not silently conflated with the USA300 cellular strain or a proven purified clone donor. Historical plasmid sequences and exact termini remain unverified.

### Directed effects and limits

graph: supported. Targets: PF01757.

Sixteen DIRECT observed edges concern net purified-preparation effects, six INDIRECT edges concern cellular genotype effects. Acetyl-CoA-to-Tyr206 and Tyr206-to-Ser453 are HYPOTHESIZED/UNRESOLVED, not inferred observed flux. WT/substrate/negative comparisons, residual H36A and E154A behavior, divergent Y136A endpoints, extra-domain S453 comparator and conditional tunicamycin growth are retained. Neither C-domain synthetic-donor use nor modified peptides are joined into a directly observed intramolecular chain. No general family specificity or isolated-PF01757 sufficiency is asserted.

### Remaining family coverage

completeness: concern. Targets: PF01757.

SI clone/strain/primer details, purification conditions and unviewed spectra remain unavailable. Resolve the MS S453A/lysine-mutant search-reference provenance and acetylated untreated control; compare any treatment effects only with appropriate matched quantitation. Reconcile Figure3D R25A/R25K, Figure1A empty-vector genotype, pH/donor/time/solvent discrepancies and assess remaining variants and other family members independently. Listeria OatA, OafA/OafB, OpgC/IcaC and eukaryotic references remain uncurated leads.

## Findings

### additional-contexts: Resolve OatA construct and assay provenance and extend member-specific coverage

minor / open / confirmed; issue key: pf01757-causal-context-coverage.

Obtain SI and clone/search provenance, resolve extra MS reference substitutions and untreated Tyr206 modification, inspect remaining variant assays and reconcile protocol/caption discrepancies. Keep the chemical relay hypothetical until transfer-specific evidence supports it; assess remaining PF01757 members with exact sequence mapping and primary experiments. Append a successor review stating actual coverage rather than promoting the record from partial evidence.

## Recommended Actions And Acceptance Checks

### extend-contexts

Obtain SI and clone/search provenance, resolve extra MS reference substitutions and untreated Tyr206 modification, inspect remaining variant assays and reconcile protocol/caption discrepancies. Keep the chemical relay hypothetical until transfer-specific evidence supports it; assess remaining PF01757 members with exact sequence mapping and primary experiments. Append a successor review stating actual coverage rather than promoting the record from partial evidence.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader; Jones2021 main Results, Discussion and selected Methods; Figures1/3/4/5 visually inspected. SI inaccessible and not independently reviewed. | supports | Full-length preparations acetylate G5 and GM acceptors with acetyl-CoA. Selected substitutions change CoASH release and glycan transfer differently, notably Y136A increases release but lacks G5 product. Cellular deletion/complementation changes PG acetylation and conditional OD growth. Figure5 residue chemistry and intramolecular Tyr206-to-Ser453 transfer remain hypotheses. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/A0A0H2XFE4/entry/pfam/PF01757/; Accession and domain locations; paired UniProt identity facts | supports | Q2FV54 and USA300 A0A0H2XFE4/SAUSA300_2504 exactly match versioned603-aa ABD21303.1. Current PF01757 is19-344; H36/E154/Y206 lie inside, E357/S453 and isolated C-domain445-601 outside. WT MS search reference is not clone resequencing. The ATCC6538 topology library is not silently conflated with the USA300 cellular strain or a proven purified clone donor. Historical plasmid sequences and exact termini remain unverified. |
| deposited-ms-context | https://doi.org/10.6084/m9.figshare.13309463; S453A treated/control protein.html tables and treated coverage image; WT search identity; paired annotated-MS2 deposit13309505 treated and control1 tables. | supports | Tyr206 acetylation appears in both treated and untreated mutant search outputs. The mutant search reference displays S453A/K495A/K496A and LE+His10; this is not proof of every biochemical preparation's exact clone sequence. Unnormalized independent search outputs do not establish treatment-induced acetyl flux. |
| remaining-at3-coverage | https://pmc.ncbi.nlm.nih.gov/articles/PMC9833829/; Retrieved primary OafB computational-study passages; separate ledger labels Listeria and other sources as uncurated leads. | supports | OafB modelling supplies plausible donor-entry and motion hypotheses but does not observe SaOatA bond/proton transfer. Other mapped family members and specificity contexts need independent assessment; the family is not complete. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01757 | data/families/PF01757.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Main Figures1/3/4/5 and treated/control annotated MS2 tables plus WT/treated-mutant search coverage images were visually inspected. Supplement PDF/figures/tables were inaccessible; other spectra, raw MS and all remaining variants were not independently analyzed. No clone resequencing, normalized treatment enrichment, calibrated product quantitation, MD rerun, experimental replication or exhaustive family survey was performed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T145601Z-pf01757-oata-assay-effects-and-hypothetical-relay
title: PF01757 SaOatA observed assay effects and hypothetical acetyl relay
started_at: '2026-10-11T14:55:48Z'
finished_at: '2026-10-11T14:56:01Z'
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
summary: Five graphs retain twenty-two observed effects, sixteen direct preparation
  effects and six indirect cellular effects, plus two explicitly hypothetical relay
  steps. Product formation, CoASH release, glycan transfer, PG acetylation and tunicamycin-dependent
  growth remain separate contexts. Deposited untreated Tyr206 acetylation and the
  MS search-reference extra substitutions limit direct causal attribution. Partial
  coverage remains IN_PROGRESS.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01757.yaml
    sha256: 997ddfed03cfadd9be6a7a2d0664568b8c79bc09b0a7e2d99db664eb6f74c71b
    role: context
  - path: data/families/PF01757.yaml
    sha256: 0a0a402def1f4f1ebafc07ec6a27dda09c7b556954c0a1c389480e44493e3fff
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
  - path: evidence/PF01757/jones-2021-oata.txt
    role: context
    sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0
  - path: evidence/PF01757/OatA-identity.txt
    role: context
    sha256: a21d85334f68301f8b103032ba6af30c11faa11e399317d3d0ecc26fc7753029
  - path: evidence/PF01757/ms-deposit-caveats.txt
    role: context
    sha256: e8337d46b96315e7081c8cc488478899d6cf3d487a30283756cb12505bbca956
  - path: evidence/PF01757/at3-followup-ledger.txt
    role: context
    sha256: 7e406911a142540c0bb0e5aea8202bf90ebe9e5e7a81861587cdb90c962521a9
targets:
- target_id: PF01757
  path: data/families/PF01757.yaml
  label: PF01757
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01757.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 47f77427f0187aa58815badf72fbc4ea9ec77c3582fde9e1d5600f2d2f8565a8
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Pending PF01757 within all 8296 frozen families; selected SaOatA2021
    experiments are partial coverage, not family or corpus completion.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01757
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: SI clone/strain/primer details, purification conditions and unviewed spectra
      remain unavailable. Resolve the MS S453A/lysine-mutant search-reference provenance
      and acetylated untreated control; compare any treatment effects only with appropriate
      matched quantitation. Reconcile Figure3D R25A/R25K, Figure1A empty-vector genotype,
      pH/donor/time/solvent discrepancies and assess remaining variants and other
      family members independently. Listeria OatA, OafA/OafB, OpgC/IcaC and eukaryotic
      references remain uncurated leads.
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
  - PF01757
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader
  locator: Jones2021 main Results, Discussion and selected Methods; Figures1/3/4/5
    visually inspected. SI inaccessible and not independently reviewed.
  accessed_at: '2026-10-11T14:56:01Z'
  support: supports
  snapshot_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0
  summary: Full-length preparations acetylate G5 and GM acceptors with acetyl-CoA.
    Selected substitutions change CoASH release and glycan transfer differently, notably
    Y136A increases release but lacks G5 product. Cellular deletion/complementation
    changes PG acetylation and conditional OD growth. Figure5 residue chemistry and
    intramolecular Tyr206-to-Ser453 transfer remain hypotheses.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/A0A0H2XFE4/entry/pfam/PF01757/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T14:56:01Z'
  support: supports
  snapshot_sha256: a21d85334f68301f8b103032ba6af30c11faa11e399317d3d0ecc26fc7753029
  summary: Q2FV54 and USA300 A0A0H2XFE4/SAUSA300_2504 exactly match versioned603-aa
    ABD21303.1. Current PF01757 is19-344; H36/E154/Y206 lie inside, E357/S453 and
    isolated C-domain445-601 outside. WT MS search reference is not clone resequencing.
    The ATCC6538 topology library is not silently conflated with the USA300 cellular
    strain or a proven purified clone donor. Historical plasmid sequences and exact
    termini remain unverified.
- evidence_id: deposited-ms-context
  kind: primary_source
  reference: https://doi.org/10.6084/m9.figshare.13309463
  locator: S453A treated/control protein.html tables and treated coverage image; WT
    search identity; paired annotated-MS2 deposit13309505 treated and control1 tables.
  summary: Tyr206 acetylation appears in both treated and untreated mutant search
    outputs. The mutant search reference displays S453A/K495A/K496A and LE+His10;
    this is not proof of every biochemical preparation's exact clone sequence. Unnormalized
    independent search outputs do not establish treatment-induced acetyl flux.
  accessed_at: '2026-10-11T14:56:01Z'
  support: supports
  snapshot_sha256: e8337d46b96315e7081c8cc488478899d6cf3d487a30283756cb12505bbca956
- evidence_id: remaining-at3-coverage
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC9833829/
  locator: Retrieved primary OafB computational-study passages; separate ledger labels
    Listeria and other sources as uncurated leads.
  summary: OafB modelling supplies plausible donor-entry and motion hypotheses but
    does not observe SaOatA bond/proton transfer. Other mapped family members and
    specificity contexts need independent assessment; the family is not complete.
  accessed_at: '2026-10-11T14:56:01Z'
  support: supports
  snapshot_sha256: 7e406911a142540c0bb0e5aea8202bf90ebe9e5e7a81861587cdb90c962521a9
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T14:56:01Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01757
  kind: record_content
  reference: data/families/PF01757.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T14:56:01Z'
  support: context_only
  snapshot_sha256: 0a0a402def1f4f1ebafc07ec6a27dda09c7b556954c0a1c389480e44493e3fff
  quote: "id: Pfam:PF01757\npfam_id: PF01757\nname: Acyltransferase domain\nshort_name:\
    \ Acyl_transf_3\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01757\n\
    counters:\n  proteins: 79491\n  matches: 80016\n  proteomes: 17243\n  taxa: 26410\n\
    \  structures: 0\n  alphafold_models: 51499\n  domain_architectures: 429\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002656\ndescription: This family includes a range of\
    \ acyltransferase enzymes. This domain is found in a wide range\n  of acyltransferase\
    \ enzymes, including, mainly, bacterial proteins which catalyse the transfer of\
    \ acyl\n  groups, other than amino-acyl, from one compound to another, such as\
    \ Glucans biosynthesis protein C\n  (OPGC) or protein OatA from Listeria monocytogenes\
    \ serovar 1/2a and Staphylococcus aureus, an integral\n  membrane protein which\
    \ is responsible for O-acetylation at the C6-hydroxyl group of N-acetylmuramyl\n\
    \  residues, forming the corresponding N,6-O-diacetylmuramic acid of the peptidoglycan,\
    \ a modification\n  that determines lysozyme resistance [[cite:PUB00097284],[cite:PUB00097283]].\
    \ This domain is also present\n  in eukaryotic proteins, namely O-acyltransferase\
    \ like protein (OACYL) from mouse and RHY1 (Regulator\n  of hypoxia-inducible\
    \ factor 1) [[cite:PUB00097285]] and NRF6 (Nose resistant to fluoxetine protein\
    \ 6)\n  from Caenorhabditis elegans [[cite:PUB00097286]].\ncuration_history: history/records/PF01757\n\
    discussions:\n- discussion_id: oata-construct-and-acetyl-origin\n  prompt: Resolve\
    \ MS construct provenance and distinguish modified-residue detection from acetyl\
    \ flux.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale: The deposited mutant\
    \ search includes extra lysine replacements and detects acetylated Tyr206\n  \
    \  in both treated and untreated samples. These observations limit a treatment-specific\
    \ causal claim\n    without disproving every possible acetyl-relay mechanism.\n\
    \  evidence:\n  - reference: doi:10.6084/m9.figshare.13309463\n    supports: PARTIAL\n\
    \    evidence_source: inspected_deposited_peptide_search_tables_and_coverage_image\n\
    \    explanation: Parsed treated/control protein.html and visually inspected treated\
    \ coverage image; search\n      reference S453A/K495A/K496A with LE+His10 is not\
    \ clone resequencing. No normalized treatment-enrichment\n      analysis or new\
    \ raw-data search.\n  - reference: doi:10.6084/m9.figshare.13309505\n    supports:\
    \ PARTIAL\n    evidence_source: inspected_treated_and_control_annotated_ms2_tables\n\
    \    explanation: Both selected ion tables annotate Tyr206 acetylation; its acquisition\
    \ during the added-donor\n      step remains unproven.\n  notes: See evidence/PF01757/ms-deposit-caveats.txt\
    \ and OatA-identity.txt. Verify supplemental clone/strain\n    records and experimental\
    \ material provenance before applying the MS genotype to Figure1 S453A preparations.\n\
    \    Distinguish USA300 cells, ATCC6538 topology library and Q2FV54 search reference.\
    \ Preserve PF01757\n    19-344 and extra-domain S453/E357 boundaries.\n  posed_by:\
    \ Codex\n  posed_date: '2026-10-11'\n- discussion_id: oata-assay-and-family-coverage\n\
    \  prompt: Reconcile assay discrepancies and assess remaining PF01757 member mechanisms.\n\
    \  kind: CURATION_TODO\n  status: OPEN\n  rationale: Twenty-two observed effects\
    \ in four assay-context graphs and two hypothetical relay edges\n    provide partial\
    \ SaOatA coverage. They do not characterize all Acyl_transf_3 members or establish\
    \ the\n    proposed chemical relay.\n  evidence:\n  - reference: PMID:34480000\n\
    \    supports: PARTIAL\n    evidence_source: inspected_main_methods_results_and_figures\n\
    \    explanation: Full-length glycan product, divergent esterase/transferase variant\
    \ behavior, PG acetylation\n      and conditional growth are supported. Supplementary\
    \ recipes, clone details, remaining variants and\n      raw MS remain incomplete.\n\
    \  - reference: doi:10.7554/eLife.81547\n    supports: PARTIAL\n    evidence_source:\
    \ primary_computational_article_retrieved_passages\n    explanation: OafB structural/MD\
    \ work supplies mechanistic hypotheses, not directly measured SaOatA\n      chemistry\
    \ or proof of conserved topology.\n  notes: See evidence/PF01757/at3-followup-ledger.txt.\
    \ Resolve pH/donor/time/solvent differences, Figure3D\n    R25A/R25K and Figure1A\
    \ empty-vector labels; obtain inaccessible SI. Inspect Listeria OatA, OafA/OafB,\n\
    \    OpgC/IcaC, RHY1/NRF6 and other mapped family members independently. Preserve\
    \ negative and residual\n    results and distinct donor/acceptor specificity.\
    \ Remain IN_PROGRESS with partial scientific self-review.\n  posed_by: Codex\n\
    \  posed_date: '2026-10-11'\ncausal_graphs:\n- graph_id: saoata-acetylcoa-glycan-products\n\
    \  title: Full-length SaOatA produces acetylated glycans with acetyl-CoA\n  scope:\
    \ 'Jones 2021 Figure 1D/E: purified full-length SaOatA versus enzyme-free, published\
    \ S453A and\n    isolated C-domain preparations.'\n  context: 5 uM enzyme, 1 mM\
    \ acetyl-CoA, 50 mM sodium phosphate pH 6.5, 18 h; either 1 mM G5 or 10 ug/ml\n\
    \    semisynthetic GM-pentapeptide oligomers of 4-10 repeats. GM products are\
    \ mutanolysin-digested for\n    QTOF-MS. Recombinant full-length protein is expressed\
    \ in E. coli C43(DE3); exact detergent recipe\n    remains unavailable.\n  family_mapping:\
    \ 603-aa Q2FV54/NCTC8325 and A0A0H2XFE4/USA300 references are identical to versioned\
    \ ABD21303.1;\n    PF01757 19-344. WT MS searches use Q2FV54, not a resequenced\
    \ clone. S453 and the isolated C-domain\n    445-601 are outside current PF01757.\
    \ Full-length clone donor strain/termini require SI verification.\n  scope_status:\
    \ MECHANISTIC\n  taxon: NCBITaxon:1280\n  limitations: DIRECT describes net purified-preparation\
    \ effects, not isolated-domain sufficiency. The\n    MS S453A search reference\
    \ also has K495A/K496A and LE+His10; whether the Figure1 preparation shared\n\
    \    those changes is unresolved. Treat it as the published S453A preparation,\
    \ not an independently verified\n    single mutant. The C-domain negative comparator\
    \ is plotted only for GM-penta. No atomic relay, exact\n    acceptor bond or calibrated\
    \ product yield is inferred from these spectra.\n  nodes:\n  - node_id: wt-g5-reaction\n\
    \    label: Full-length WT SaOatA plus acetyl-CoA and G5\n    node_type: ACTIVITY\n\
    \    grounding:\n    - UniProtKB:Q2FV54\n  - node_id: wt-gm-reaction\n    label:\
    \ Full-length WT SaOatA plus acetyl-CoA and GM oligomers\n    node_type: ACTIVITY\n\
    \  - node_id: substitute-s453a-g5\n    label: Substitute the published S453A preparation\
    \ in the G5 assay\n    node_type: PERTURBATION\n  - node_id: substitute-s453a-gm\n\
    \    label: Substitute the published S453A preparation in the GM assay\n    node_type:\
    \ PERTURBATION\n  - node_id: substitute-c-domain-gm\n    label: Substitute isolated\
    \ C-domain in the GM assay\n    node_type: PERTURBATION\n  - node_id: acetyl-g5-product\n\
    \    label: Detected acetyl-G5 product\n    node_type: STATE\n  - node_id: acetyl-gm-product\n\
    \    label: Detected acetyl-GM-penta product after digestion\n    node_type: STATE\n\
    \  edges:\n  - edge_id: wt-produces-acetyl-g5\n    subject: wt-g5-reaction\n \
    \   predicate: produces\n    object: acetyl-g5-product\n    mechanism: Joint enzyme/donor/acceptor\
    \ incubation produces the 1076.42 [M+H]+ and 1098.40 sodium-adduct\n      peaks\
    \ absent from the enzyme-free control.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:34480000\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: OatA Utilizes Acetyl-CoA for PG O-Acetylation.\n      explanation:\
    \ Figure1D visually inspected; Results and caption distinguish substrate and acetylated\n\
    \        product. SupplementS4 confirmation is reported but not independently\
    \ inspected.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n      cache_sha256:\
    \ 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n  - edge_id:\
    \ wt-produces-acetyl-gm\n    subject: wt-gm-reaction\n    predicate: produces\n\
    \    object: acetyl-gm-product\n    mechanism: Joint incubation yields the 1009.4\
    \ acetyl-GM-penta signal after digestion, compared with\n      substrate 967.4\
    \ and the enzyme-free control.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:34480000\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: OatA Utilizes Acetyl-CoA for PG O-Acetylation.\n      explanation:\
    \ Figure1E product and control spectra, Results and main transferase Methods.\n\
    \      cache_path: evidence/PF01757/jones-2021-oata.txt\n      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    \  - edge_id: s453a-preparation-decreases-g5-product\n    subject: substitute-s453a-g5\n\
    \    predicate: decreases\n    object: acetyl-g5-product\n    mechanism: The published\
    \ S453A preparation lacks the acetyl-G5 product detected with WT; complete\n \
    \     construct equivalence except S453A is not independently established.\n \
    \   directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:34480000\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: OatA Utilizes Acetyl-CoA for PG O-Acetylation.\n      explanation:\
    \ Figure1D WT versus published S453A spectra; separate deposit caveats prevent\
    \ a verified\n        single-lesion claim.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n\
    \      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    \  - edge_id: s453a-preparation-decreases-gm-product\n    subject: substitute-s453a-gm\n\
    \    predicate: decreases\n    object: acetyl-gm-product\n    mechanism: Replacing\
    \ WT with the published S453A preparation removes detectable acetyl-GM-penta under\n\
    \      this assay, not proof of an isolated PF01757 catalytic residue.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:34480000\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: OatA Utilizes Acetyl-CoA for PG O-Acetylation.\n      explanation:\
    \ Figure1E WT/S453A spectra and construct limitations.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n\
    \      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    \  - edge_id: isolated-c-domain-decreases-gm-product\n    subject: substitute-c-domain-gm\n\
    \    predicate: decreases\n    object: acetyl-gm-product\n    mechanism: The isolated\
    \ C-domain does not produce the acetyl-GM-penta signal from acetyl-CoA seen\n\
    \      with full-length protein. This is donor- and preparation-specific, not\
    \ inactivity with all donors.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:34480000\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: OatA Utilizes Acetyl-CoA for PG O-Acetylation.\n      explanation:\
    \ Figure1E C-domain negative comparator; Figure4 synthetic-donor activity prevents\
    \ an\n        unconditional inactivity claim.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n\
    \      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    - graph_id: saoata-substitution-assays\n  title: SaOatA substitutions distinguish\
    \ CoASH release from glycan transfer\n  scope: 'Jones 2021 Figure3C: full-length\
    \ recombinant WT and selected R25A/R25K/H36A/R86A/Y136A/E154A/Y206A\n    preparations.\
    \ Separate CoASH-release and G5-transfer measurements.'\n  context: C43(DE3) expression,\
    \ fresh-resin IMAC per preparation. Figure3C specifies 50 mM sodium phosphate\n\
    \    pH 7, 5% DMSO, 25 C, 0.1 mM acetyl-CoA and 0.2 mM DTDP; transfer assays include\
    \ 1 mM G5. This differs\n    from Figure1's pH 6.5/1 mM donor/18 h recipe; transfer\
    \ endpoint time and exact DTDP use need SI reconciliation.\n  family_mapping:\
    \ Full-length reference Q2FV54 equals A0A0H2XFE4 and ABD21303.1; PF01757 19-344\
    \ includes\n    all seven selected substitution sites. The experimental object\
    \ still includes the distinct C-terminal\n    domain; clone sequence and tag details\
    \ are not independently verified.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:1280\n\
    \  limitations: DIRECT concerns net preparation effects. Comparable expression/purity\
    \ is not proof of unchanged\n    folding or a particular proton-transfer role.\
    \ CoASH release is not synonymous with productive glycan\n    transfer. S453A's\
    \ 5.4% rate uses ethanol rather than DMSO and is excluded from matched-rate edges.\n\
    \    Figure3D's R25A caption conflicts with R25K Results; no R25A fitted kinetics\
    \ are adopted. Remaining\n    variants and quantitative G5 yields are unassessed.\n\
    \  nodes:\n  - node_id: wt-acetylcoa-reaction\n    label: Full-length WT SaOatA\
    \ with acetyl-CoA\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:Q2FV54\n\
    \  - node_id: r25a-preparation\n    label: Substitute R25A for WT in the matched\
    \ assay\n    node_type: PERTURBATION\n  - node_id: r25k-preparation\n    label:\
    \ Substitute R25K for WT in the matched assay\n    node_type: PERTURBATION\n \
    \ - node_id: h36a-preparation\n    label: Substitute H36A for WT in the matched\
    \ assay\n    node_type: PERTURBATION\n  - node_id: r86a-preparation\n    label:\
    \ Substitute R86A for WT in the matched assay\n    node_type: PERTURBATION\n \
    \ - node_id: y136a-preparation\n    label: Substitute Y136A for WT in the matched\
    \ assay\n    node_type: PERTURBATION\n  - node_id: e154a-preparation\n    label:\
    \ Substitute E154A for WT in the matched assay\n    node_type: PERTURBATION\n\
    \  - node_id: y206a-preparation\n    label: Substitute Y206A for WT in the matched\
    \ assay\n    node_type: PERTURBATION\n  - node_id: coash-release\n    label: DTDP-detected\
    \ CoASH release from acetyl-CoA\n    node_type: PROCESS\n  - node_id: g5-acetyl-product\n\
    \    label: Acetyl-G5 detected in the separate transfer assay\n    node_type:\
    \ STATE\n  edges:\n  - edge_id: wt-produces-coash\n    subject: wt-acetylcoa-reaction\n\
    \    predicate: produces\n    object: coash-release\n    mechanism: WT preparation\
    \ releases CoASH, reported specific activity 28.8 +/-0.20 nmol/min/mg, establishing\n\
    \      the comparator without proving a particular protein-acetyl intermediate.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:34480000\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: In vitro studies.\n      explanation: Figure3C WT row and esterase\
    \ Methods; Figure1C separate donor-titration corroboration.\n      cache_path:\
    \ evidence/PF01757/jones-2021-oata.txt\n      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    \  - edge_id: r25a-decreases-coash\n    subject: r25a-preparation\n    predicate:\
    \ decreases\n    object: coash-release\n    mechanism: R25A retains 18.4% of WT\
    \ release; its separate G5-transfer result remains positive.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:34480000\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: In vitro studies.\n      explanation: Figure3C R25A versus WT,\
    \ not the inconsistently labeled Figure3D kinetics.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n\
    \      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    \  - edge_id: r25k-increases-coash\n    subject: r25k-preparation\n    predicate:\
    \ increases\n    object: coash-release\n    mechanism: R25K gives 178% of WT release\
    \ in this assay and retains detected G5 transfer; no universal\n      gain-of-function\
    \ or binding-affinity claim.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:34480000\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: In vitro studies.\n      explanation: Figure3C R25K row and in-vitro\
    \ Results.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n      cache_sha256:\
    \ 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n  - edge_id:\
    \ h36a-decreases-coash\n    subject: h36a-preparation\n    predicate: decreases\n\
    \    object: coash-release\n    mechanism: H36A retains 0.64% apparent release,\
    \ a large reduction but not complete absence.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:34480000\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: In vitro studies.\n      explanation: Figure3C H36A relative and\
    \ specific activity entries.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n\
    \      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    \  - edge_id: h36a-decreases-g5-product\n    subject: h36a-preparation\n    predicate:\
    \ decreases\n    object: g5-acetyl-product\n    mechanism: No G5 acetyl-product\
    \ is detected with H36A compared with WT, despite residual CoASH release\n   \
    \   in the separate assay.\n    directness: DIRECT\n    support: OBSERVED\n  \
    \  evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:34480000\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: In vitro studies.\n      explanation: Figure3C H36A transferase-negative\
    \ entry and Results; S7 raw spectra uninspected.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n\
    \      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    \  - edge_id: r86a-decreases-coash\n    subject: r86a-preparation\n    predicate:\
    \ decreases\n    object: coash-release\n    mechanism: R86A retains 22.1% of WT\
    \ release; the separate G5-transfer assay remains positive.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:34480000\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: In vitro studies.\n      explanation: Figure3C R86A row and in-vitro\
    \ Results.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n      cache_sha256:\
    \ 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n  - edge_id:\
    \ y136a-increases-coash\n    subject: y136a-preparation\n    predicate: increases\n\
    \    object: coash-release\n    mechanism: Y136A gives 155% of WT release at the\
    \ specified donor concentration. This is not increased\n      glycan acetylation.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:34480000\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: In vitro studies.\n      explanation: Figure3C Y136A rate44.6\
    \ +/-0.48 nmol/min/mg and relative155%.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n\
    \      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    \  - edge_id: y136a-decreases-g5-product\n    subject: y136a-preparation\n   \
    \ predicate: decreases\n    object: g5-acetyl-product\n    mechanism: Y136A removes\
    \ detectable G5 acetylation compared with WT, in contrast to its higher CoASH-release\n\
    \      rate. The molecular reason for this divergence is unresolved.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:34480000\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: In vitro studies.\n      explanation: Figure3C Y136A transferase-negative\
    \ entry and Results.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n\
    \      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    \  - edge_id: e154a-decreases-coash\n    subject: e154a-preparation\n    predicate:\
    \ decreases\n    object: coash-release\n    mechanism: E154A retains 4.76% of\
    \ WT release and remains positive for G5 transfer; the assay does\n      not establish\
    \ its proposed acid-base role.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:34480000\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: In vitro studies.\n      explanation: Figure3C E154A row and Results.\n\
    \      cache_path: evidence/PF01757/jones-2021-oata.txt\n      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    \  - edge_id: y206a-decreases-coash\n    subject: y206a-preparation\n    predicate:\
    \ decreases\n    object: coash-release\n    mechanism: Y206A has no detectable\
    \ release compared with WT; this supports preparation-level dependence,\n    \
    \  not direct observation of Tyr206 attacking acetyl-CoA.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:34480000\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: In vitro studies.\n      explanation: Figure3C Y206A N.D. entry\
    \ and in-vitro Results.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n\
    \      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    \  - edge_id: y206a-decreases-g5-product\n    subject: y206a-preparation\n   \
    \ predicate: decreases\n    object: g5-acetyl-product\n    mechanism: Y206A lacks\
    \ the G5 acetyl-product detected with WT in the separate transfer assay.\n   \
    \ directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:34480000\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: In vitro studies.\n      explanation: Figure3C Y206A transferase-negative\
    \ entry and Results.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n\
    \      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    - graph_id: usa300-oata-pg-acetylation\n  title: USA300 oatA genotype changes\
    \ cellular PG acetylation\n  scope: 'Jones 2021 Figure1B: USA300 WT, markerless\
    \ oatA deletion, and deletion complemented with WT,\n    H36A or Y206A pACCJ3.'\n\
    \  context: Base-labile acetyl groups normalized to muramic acid in isolated PG;\
    \ three replicates with\n    SD. Constitutive His-tagged complementation. PG-isolation\
    \ conditions are not assumed identical to\n    the tunicamycin growth assay.\n\
    \  family_mapping: USA300 reference SAUSA300_2504/A0A0H2XFE4 equals ABD21303.1\
    \ and Q2FV54, PF01757 19-344.\n    H36 and Y206 are inside that interval, but\
    \ these are whole-gene/whole-protein cellular interventions.\n    Exact experimental\
    \ clone strain and supplementary plasmid sequences are not independently verified.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:367830\n  limitations: INDIRECT\
    \ cellular genotype effects, not isolated-domain chemistry. Membrane anti-His\
    \ detection\n    in Figure3A supports expression of impaired variants but does\
    \ not exclude folding/localization effects.\n    Other variants, including residual\
    \ R83A activity, remain contextual. No measured mediation from this\n    endpoint\
    \ to the separate growth experiment.\n  nodes:\n  - node_id: delete-oata\n   \
    \ label: Delete oatA relative to USA300 WT\n    node_type: PERTURBATION\n    grounding:\n\
    \    - UniProtKB:A0A0H2XFE4\n  - node_id: complement-wt\n    label: Add WT pACCJ3\
    \ to the oatA deletion strain\n    node_type: PERTURBATION\n  - node_id: complement-h36a\n\
    \    label: Replace WT complement with H36A pACCJ3\n    node_type: PERTURBATION\n\
    \  - node_id: complement-y206a\n    label: Replace WT complement with Y206A pACCJ3\n\
    \    node_type: PERTURBATION\n  - node_id: pg-acetyl-fraction\n    label: PG base-labile\
    \ acetyl groups per muramic acid\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ deletion-decreases-pg-acetylation\n    subject: delete-oata\n    predicate:\
    \ decreases\n    object: pg-acetyl-fraction\n    mechanism: Deletion reduces the\
    \ measured fraction from about 40% in WT to undetectable levels.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:34480000\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: PG O-acetylation levels\n      explanation: Figure1B WT/deletion\
    \ bars and cellular PG Results.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n\
    \      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    \  - edge_id: wt-complement-increases-pg-acetylation\n    subject: complement-wt\n\
    \    predicate: increases\n    object: pg-acetyl-fraction\n    mechanism: WT complementation\
    \ restores measurable PG acetylation to about 35%, without claiming exact\n  \
    \    equality to WT.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:34480000\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n      snippet:\
    \ PG O-acetylation levels\n      explanation: Figure1B deletion versus WT-pACCJ3\
    \ complemented deletion and cellular PG Results.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n\
    \      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    \  - edge_id: h36a-complement-decreases-pg-acetylation\n    subject: complement-h36a\n\
    \    predicate: decreases\n    object: pg-acetyl-fraction\n    mechanism: H36A\
    \ complementation leaves no detectable PG acetylation compared with the WT complement.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:34480000\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: PG O-acetylation levels\n      explanation: Figure1B H36A bar\
    \ and in-situ variant Results; Figure3A expression-control context.\n      cache_path:\
    \ evidence/PF01757/jones-2021-oata.txt\n      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    \  - edge_id: y206a-complement-decreases-pg-acetylation\n    subject: complement-y206a\n\
    \    predicate: decreases\n    object: pg-acetyl-fraction\n    mechanism: Y206A\
    \ complementation leaves about 1.3% PG acetylation, markedly below WT complement\
    \ but\n      not an absolute zero.\n    directness: INDIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:34480000\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: PG O-acetylation levels\n      explanation: Figure1B Y206A bar\
    \ and in-situ variant Results; residual level retained.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n\
    \      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    - graph_id: usa300-oata-tunicamycin-lysozyme-growth\n  title: oatA deletion and\
    \ complementation alter growth with lysozyme and tunicamycin\n  scope: 'Jones\
    \ 2021 Figure1A: USA300 WT, oatA deletion and deletion complemented with WT pACCJ3;\
    \ unambiguous\n    blue, green and orange curves.'\n  context: TSB, 37 C, 0.4\
    \ ug/ml tunicamycin, 1% DMSO and 0.25-4 mg/ml hen egg-white lysozyme. Figure1A\n\
    \    plots 12-h relative delta-OD600, n=3 with SD; Methods monitor 20 h at 20-min\
    \ intervals. Compare matched\n    lysozyme doses, particularly 1-4 mg/ml.\n  family_mapping:\
    \ USA300 OatA reference A0A0H2XFE4/ABD21303.1, PF01757 19-344; gene deletion and\
    \ full-length\n    trans complementation, not isolated-domain interventions.\n\
    \  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:367830\n  limitations: INDIRECT\
    \ conditional growth effects, not death or a directly observed PG-to-growth chain.\n\
    \    The no-tunicamycin assay instead shows a lag in the main-text description.\
    \ Figure1A's gray empty-vector\n    caption names WT+pALC2073 whereas Results\
    \ describe deletion+empty vector; those ambiguous gray comparisons\n    are not\
    \ encoded. Exact clone background requires SI.\n  nodes:\n  - node_id: delete-oata\n\
    \    label: Delete oatA relative to WT under matched exposure\n    node_type:\
    \ PERTURBATION\n  - node_id: restore-wt-oata\n    label: Complement the deletion\
    \ with WT pACCJ3\n    node_type: PERTURBATION\n  - node_id: twelve-hour-growth\n\
    \    label: Relative delta-OD600 after 12 h with lysozyme and tunicamycin\n  \
    \  node_type: PHENOTYPE\n  edges:\n  - edge_id: deletion-decreases-conditional-growth\n\
    \    subject: delete-oata\n    predicate: decreases\n    object: twelve-hour-growth\n\
    \    mechanism: Deletion removes the OD increase at 1 mg/ml lysozyme and above\
    \ while WT retains growth,\n      conditional on the tunicamycin-containing assay.\n\
    \    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:34480000\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: Lysozyme resistance was restored\n      explanation: Figure1A\
    \ green versus blue curves and cellular lysozyme Results/Methods; no killing\n\
    \        measurement.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n\
    \      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    \  - edge_id: complementation-increases-conditional-growth\n    subject: restore-wt-oata\n\
    \    predicate: increases\n    object: twelve-hour-growth\n    mechanism: WT trans\
    \ complementation restores substantial OD increase at the same lysozyme doses,\
    \ including\n      4 mg/ml, compared with the deletion.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:34480000\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: Lysozyme resistance was restored\n      explanation: Figure1A\
    \ orange versus green curves, not the ambiguous empty-vector gray curve.\n   \
    \   cache_path: evidence/PF01757/jones-2021-oata.txt\n      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    - graph_id: saoata-proposed-acetyl-relay\n  title: Hypothesized Tyr206-to-Ser453\
    \ acetyl relay in full-length SaOatA\n  scope: Jones 2021 Figure5 and Discussion\
    \ proposal for full-length SaOatA; not a directly observed sequence\n    of intermediates\
    \ or a family-wide mechanism.\n  context: Proposed membrane-associated donor acquisition\
    \ from acetyl-CoA, followed by intramolecular\n    transfer from an acetylated\
    \ Tyr206 to the cognate C-terminal Ser453. Full-length OatA supplies both\n  \
    \  sites; these are joint protein/substrate states, not independently sufficient\
    \ residues.\n  family_mapping: PF01757 19-344 in the matched Q2FV54/A0A0H2XFE4/ABD21303.1\
    \ references includes H36,E154,Y206\n    but excludes S453 and the isolated445-601\
    \ partner. E357 is also outside current PF01757 and must not\n    be confused\
    \ with proposed E154. Topology-library ATCC6538 and purified-clone provenance\
    \ remain distinct.\n  scope_status: HYPOTHETICAL\n  taxon: NCBITaxon:1280\n  limitations:\
    \ Both edges are HYPOTHESIZED and directness UNRESOLVED. Deposited treated and\
    \ untreated\n    S453A samples both contain acetylated Tyr206; the search reference\
    \ includes K495A/K496A. This is not\n    treatment-specific flux proof. Synthetic\
    \ acetyl-Tyr donor use by isolated C-domain does not observe\n    an intramolecular\
    \ relay. No atomic OatA structure or proton-transfer trajectory is established\
    \ by\n    Figure5; OafB modelling is not SaOatA experimental validation.\n  nodes:\n\
    \  - node_id: donor-and-unmodified-oata\n    label: Acetyl-CoA with full-length\
    \ OatA carrying unacetylated Tyr206\n    node_type: STATE\n  - node_id: tyr206-acetylated-oata\n\
    \    label: Full-length OatA carrying O-acetyl-Tyr206 and available Ser453\n \
    \   node_type: STATE\n  - node_id: ser453-acetylated-oata\n    label: OatA carrying\
    \ acetyl-Ser453 after release of the Tyr206 acetyl group\n    node_type: STATE\n\
    \  edges:\n  - edge_id: proposed-donor-to-tyr206\n    subject: donor-and-unmodified-oata\n\
    \    predicate: produces\n    object: tyr206-acetylated-oata\n    mechanism: The\
    \ authors propose H36/E154-assisted activation of Tyr206 to acquire acetyl from\
    \ acetyl-CoA.\n      Mutation phenotypes and modified peptides motivate this hypothesis\
    \ but do not observe its acid-base\n      steps or identify the origin of each\
    \ detected acetyl group.\n    directness: UNRESOLVED\n    support: HYPOTHESIZED\n\
    \    evidence_kind: CONTEXTUAL\n    evidence:\n    - reference: PMID:34480000\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n\
    \      snippet: Postulated mechanism\n      explanation: Figure5B and Discussion\
    \ explicitly propose the catalytic triad; MS deposit limitations\n        are\
    \ retained in the paired evidence ledger.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n\
    \      cache_sha256: 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\n\
    \    - reference: doi:10.6084/m9.figshare.13309463\n      source_url: https://api.figshare.com/v2/articles/13309463\n\
    \      snippet: protein1|FLSaOatA_S453A_lysinemutant_AcCoA\n      explanation:\
    \ Limitation on causal attribution, not positive relay proof; both treated and\
    \ untreated\n        search outputs identify acetylated Tyr206, and the search\
    \ reference includes additional lysine\n        substitutions.\n      cache_path:\
    \ evidence/PF01757/ms-deposit-caveats.txt\n      cache_sha256: e8337d46b96315e7081c8cc488478899d6cf3d487a30283756cb12505bbca956\n\
    \  - edge_id: proposed-tyr206-to-ser453\n    subject: tyr206-acetylated-oata\n\
    \    predicate: converts_to\n    object: ser453-acetylated-oata\n    mechanism:\
    \ The proposed intramolecular relay passes acetyl from Tyr206 to C-domain Ser453.\
    \ Separate\n      acetyl-peptide detections and synthetic-donor assays are compatible\
    \ with this model but do not directly\n      track this transfer or exclude alternative\
    \ paths.\n    directness: UNRESOLVED\n    support: HYPOTHESIZED\n    evidence_kind:\
    \ CONTEXTUAL\n    evidence:\n    - reference: PMID:34480000\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC8433495/?report=reader\n      snippet:\
    \ Postulated mechanism\n      explanation: Trapping Results, Figure4 partner-domain\
    \ assay and Discussion; Figure4E caption18 h\n        versus Results2 h remains\
    \ unresolved.\n      cache_path: evidence/PF01757/jones-2021-oata.txt\n      cache_sha256:\
    \ 6948fedc8e2be5e1ca67e38d33c5b538595efe1054f31c167182d570808f6ac0\ncuration_events:\n\
    - timestamp: '2026-10-11T14:49:00Z'\n  curator: Codex\n  action: CREATE\n  outcome:\
    \ changed\n  summary: Curate SaOatA assay effects and explicitly hypothetical\
    \ acetyl relay\n  history_record: history/records/PF01757/2026-10-11T144900Z-codex-2e8634.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Q2FV54 and USA300 A0A0H2XFE4/SAUSA300_2504 exactly match versioned603-aa
    ABD21303.1. Current PF01757 is19-344; H36/E154/Y206 lie inside, E357/S453 and
    isolated C-domain445-601 outside. WT MS search reference is not clone resequencing.
    The ATCC6538 topology library is not silently conflated with the USA300 cellular
    strain or a proven purified clone donor. Historical plasmid sequences and exact
    termini remain unverified.
  target_ids:
  - PF01757
  evidence_ids:
  - identity
  - primary
  - deposited-ms-context
  - remaining-at3-coverage
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Sixteen DIRECT observed edges concern net purified-preparation effects,
    six INDIRECT edges concern cellular genotype effects. Acetyl-CoA-to-Tyr206 and
    Tyr206-to-Ser453 are HYPOTHESIZED/UNRESOLVED, not inferred observed flux. WT/substrate/negative
    comparisons, residual H36A and E154A behavior, divergent Y136A endpoints, extra-domain
    S453 comparator and conditional tunicamycin growth are retained. Neither C-domain
    synthetic-donor use nor modified peptides are joined into a directly observed
    intramolecular chain. No general family specificity or isolated-PF01757 sufficiency
    is asserted.
  target_ids:
  - PF01757
  evidence_ids:
  - primary
  - native
  - deposited-ms-context
  - remaining-at3-coverage
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: SI clone/strain/primer details, purification conditions and unviewed spectra
    remain unavailable. Resolve the MS S453A/lysine-mutant search-reference provenance
    and acetylated untreated control; compare any treatment effects only with appropriate
    matched quantitation. Reconcile Figure3D R25A/R25K, Figure1A empty-vector genotype,
    pH/donor/time/solvent discrepancies and assess remaining variants and other family
    members independently. Listeria OatA, OafA/OafB, OpgC/IcaC and eukaryotic references
    remain uncurated leads.
  target_ids:
  - PF01757
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01757-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve OatA construct and assay provenance and extend member-specific coverage
  description: Obtain SI and clone/search provenance, resolve extra MS reference substitutions
    and untreated Tyr206 modification, inspect remaining variant assays and reconcile
    protocol/caption discrepancies. Keep the chemical relay hypothetical until transfer-specific
    evidence supports it; assess remaining PF01757 members with exact sequence mapping
    and primary experiments. Append a successor review stating actual coverage rather
    than promoting the record from partial evidence.
  target_ids:
  - PF01757
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - deposited-ms-context
  - remaining-at3-coverage
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01757.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Obtain SI and clone/search provenance, resolve extra MS reference substitutions
    and untreated Tyr206 modification, inspect remaining variant assays and reconcile
    protocol/caption discrepancies. Keep the chemical relay hypothetical until transfer-specific
    evidence supports it; assess remaining PF01757 members with exact sequence mapping
    and primary experiments. Append a successor review stating actual coverage rather
    than promoting the record from partial evidence.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01757
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Main Figures1/3/4/5 and treated/control annotated MS2 tables plus WT/treated-mutant
  search coverage images were visually inspected. Supplement PDF/figures/tables were
  inaccessible; other spectra, raw MS and all remaining variants were not independently
  analyzed. No clone resequencing, normalized treatment enrichment, calibrated product
  quantitation, MD rerun, experimental replication or exhaustive family survey was
  performed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
