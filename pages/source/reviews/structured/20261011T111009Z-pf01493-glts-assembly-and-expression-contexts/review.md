# PF01493 GltS assembly readouts and truncation-expression limits

- Review: 20261011T111009Z-pf01493-glts-assembly-and-expression-contexts
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T11:07:13Z
- Finished UTC: 2026-10-11T11:10:09Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Three observed effects are supported in the inspected GltS contexts, with two direct purified-complex size effects and one indirect expression phenotype. The mature/reference numbering offset is resolved; isolated-domain function, complete clones and wider family mechanisms remain open.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Pending PF01493 overlay selected during accession-ordered review of all 8296 frozen families; this is one member/context assessment, not a family census.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01493 | data/families/PF01493.yaml | generated | PF01493 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01493 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01493.

Q05755 sequence version 1 matches InterPro and contains PF01493 at 1249-1496. The 1479-aa 1EA0 polymer exactly equals reference 37-1515. Delta40 overlaps only 21 domain residues and also removes an outside-domain tail; delta7 is outside the domain. Printed primer translations locally support the named deletions, but nucleotide-coordinate prose and full historical constructs remain unresolved.

### Directed effects and limits

graph: supported. Targets: PF01493.

The two DIRECT MECHANISTIC edges retain size measurements, not uniquely resolved stoichiometry or domain-contact rupture. The low-salt dilution arm retains 0.1 M NaCl and is not a zero-salt condition. The INDIRECT PHENOTYPIC edge reports delta40 production failure without converting it into measured misfolding. Contexts, controls, grounding and evidence references remain separated.

### Remaining family coverage

completeness: concern. Targets: PF01493.

Other GltS interventions, taxa, ferredoxin-dependent synthases and FwdC/FmdC members remain uncurated. The exact delta40 detection limit, independent constructs, rescue and domain-specific mediation were not established by the inspected material.

## Findings

### additional-contexts: Extend member and intervention coverage without treating assembly readouts as isolated-domain causality

minor / open / confirmed; issue key: pf01493-causal-context-coverage.

Resolve complete constructs and nucleotide-coordinate conventions; seek measurable expression/stability controls and domain-restricted assembly interventions. Curate additional family members from their own primary assays, preserving separate salt, ligand and kinetic conditions.

## Recommended Actions And Acceptance Checks

### extend-contexts

Resolve complete constructs and nucleotide-coordinate conventions; seek measurable expression/stability controls and domain-restricted assembly interventions. Curate additional family members from their own primary assays, preserving separate salt, ligand and kinetic conditions.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://people.impmc.fr/sjonic/Papers/JBC_GltS.pdf; Main enzyme/SAXS Methods, assembly Results including page 8245, relevant Discussion; supplemental construction/DLS Methods and Figure S3C-D. Main Table 2 and supplemental Methods/Figure S3 visually inspected. | supports | Salt addition and subsequent dilution change DLS-derived particle radius in different experiments; delta40 has a reported negative production endpoint. Kinetic correlations and the proposed folding explanation are not independently established domain-specific mechanisms. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q05755/entry/pfam/PF01493/; Accession and domain locations; paired UniProt identity facts | supports | Q05755 sequence version 1 matches InterPro and contains PF01493 at 1249-1496. The 1479-aa 1EA0 polymer exactly equals reference 37-1515. Delta40 overlaps only 21 domain residues and also removes an outside-domain tail; delta7 is outside the domain. Printed primer translations locally support the named deletions, but nucleotide-coordinate prose and full historical constructs remain unresolved. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01493 | data/families/PF01493.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Rechecked S3C-D visually in this review; prior research visually inspected main Table 2 and supplemental Methods pages 1-2. Raw scattering, reconstruction, unshown delta40 gels and full clones were not independently reanalyzed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T111009Z-pf01493-glts-assembly-and-expression-contexts
title: PF01493 GltS assembly readouts and truncation-expression limits
started_at: '2026-10-11T11:07:13Z'
finished_at: '2026-10-11T11:10:09Z'
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
summary: Three observed effects are supported in the inspected GltS contexts, with
  two direct purified-complex size effects and one indirect expression phenotype.
  The mature/reference numbering offset is resolved; isolated-domain function, complete
  clones and wider family mechanisms remain open.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01493.yaml
    sha256: 82ddc2f676a5cd8d167a425d5fbfea3dd9966544fddf917ab277a5f244f10e13
    role: context
  - path: data/families/PF01493.yaml
    sha256: f3330b5e34066741657bf0bfdd2f5166e31119fcd01405968b0bd63a5b908895
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
  - path: evidence/PF01493/cottevieille-2008-assembly.txt
    role: context
    sha256: cb7d78a923b2aeb774855712227aa70f50c19af66cc12f781b33b86a04f17521
  - path: evidence/PF01493/GltS-identity.txt
    role: context
    sha256: 156cb20252c22d4a17437babc87c16b813dfc77aa7f714b724c9812b21276e1d
targets:
- target_id: PF01493
  path: data/families/PF01493.yaml
  label: PF01493
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01493.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: e464dbf423a797bb769ddc4a9fe8dfdd24278289e9461a439cf4f7e4b242970f
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Pending PF01493 overlay selected during accession-ordered review of all
    8296 frozen families; this is one member/context assessment, not a family census.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01493
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Other GltS interventions, taxa, ferredoxin-dependent synthases and FwdC/FmdC
      members remain uncurated. The exact delta40 detection limit, independent constructs,
      rescue and domain-specific mediation were not established by the inspected material.
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
  - PF01493
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://people.impmc.fr/sjonic/Papers/JBC_GltS.pdf
  locator: Main enzyme/SAXS Methods, assembly Results including page 8245, relevant
    Discussion; supplemental construction/DLS Methods and Figure S3C-D. Main Table
    2 and supplemental Methods/Figure S3 visually inspected.
  accessed_at: '2026-10-11T11:10:09Z'
  support: supports
  snapshot_sha256: cb7d78a923b2aeb774855712227aa70f50c19af66cc12f781b33b86a04f17521
  summary: Salt addition and subsequent dilution change DLS-derived particle radius
    in different experiments; delta40 has a reported negative production endpoint.
    Kinetic correlations and the proposed folding explanation are not independently
    established domain-specific mechanisms.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q05755/entry/pfam/PF01493/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T11:10:09Z'
  support: supports
  snapshot_sha256: 156cb20252c22d4a17437babc87c16b813dfc77aa7f714b724c9812b21276e1d
  summary: Q05755 sequence version 1 matches InterPro and contains PF01493 at 1249-1496.
    The 1479-aa 1EA0 polymer exactly equals reference 37-1515. Delta40 overlaps only
    21 domain residues and also removes an outside-domain tail; delta7 is outside
    the domain. Printed primer translations locally support the named deletions, but
    nucleotide-coordinate prose and full historical constructs remain unresolved.
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T11:10:09Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01493
  kind: record_content
  reference: data/families/PF01493.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T11:10:09Z'
  support: context_only
  snapshot_sha256: f3330b5e34066741657bf0bfdd2f5166e31119fcd01405968b0bd63a5b908895
  quote: "id: Pfam:PF01493\npfam_id: PF01493\nname: GXGXG motif\nshort_name: GXGXG\n\
    seed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status: IN_PROGRESS\n\
    source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01493\ncounters:\n\
    \  proteins: 21023\n  matches: 21244\n  proteomes: 17485\n  taxa: 27304\n  structures:\
    \ 13\n  alphafold_models: 1560\n  domain_architectures: 158\nprovenance:\n  snapshot_id:\
    \ interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002489\ndescription: This domain is found in glutamate\
    \ synthase, tungsten formylmethanofuran dehydrogenase subunit\n  c (FwdC) and\
    \ molybdenum formylmethanofuran dehydrogenase subunit c (FmdC). A repeated G-XX-G-XXX-G\
    \ motif\n  is seen in the alignment.\ncuration_history: history/records/PF01493\n\
    discussions:\n- discussion_id: gxgxg-domain-boundaries-and-assembly-causality\n\
    \  prompt: Resolve complete GltS constructs and domain-specific interventions\
    \ before extending GXGXG assembly\n    mechanisms.\n  kind: CURATION_TODO\n  status:\
    \ OPEN\n  rationale: Whole-complex salt effects and a partly overlapping truncation\
    \ phenotype do not isolate PF01493\n    function. The mature-protein offset is\
    \ resolved, but nucleotide coordinate prose, delta40 expression\n    detection\
    \ and causal intermediates remain uncertain.\n  evidence:\n  - reference: PMID:18199747\n\
    \    supports: PARTIAL\n    evidence_source: full_text_and_supplement\n    explanation:\
    \ Main assembly/kinetic Results, relevant Methods/Discussion and supplemental\
    \ construction/DLS\n      information were inspected. Figure S3 and Table 2 were\
    \ visually checked. Salt preincubation, assay\n      salt and oligomer composition\
    \ are not interchangeable interventions; the kinetic correlation and\n      structural\
    \ electron-transfer scheme are not adopted as observed domain-specific edges.\n\
    \  - reference: https://files.rcsb.org/download/1EA0.cif\n    supports: SUPPORT\n\
    \    evidence_source: deposited_sequence\n    explanation: Exact polymer-reference\
    \ matching resolves precursor versus mature numbering but does\n      not reconstruct\
    \ every later assay construct or prove a folding mechanism.\n  posed_by: Codex\n\
    \  posed_date: '2026-10-11'\n  notes: FwdC/FmdC, plant/ferredoxin-dependent synthases,\
    \ other taxa and later experimental studies remain\n    uncurated. Current UniProt\
    \ oligomer prose is not substituted for the source's heterogeneous hexamer/protomer\n\
    \    model. No native physiological regulation or isolated-domain sufficiency\
    \ is claimed. Partial scientific\n    self-review; IN_PROGRESS.\ncausal_graphs:\n\
    - graph_id: azospirillum-glts-salt-radius\n  title: Added NaCl lowers the measured\
    \ radius of purified GltSHis particles\n  scope: Recombinant A. brasilense glutamate\
    \ synthase containing wild-type alpha and C-terminally His6-tagged\n    beta in\
    \ Cottevieille 2008 Figure S3C; not an isolated GXGXG domain.\n  context: Compare\
    \ 1 mg/ml GltSHis after 17 h at 15 C with 1 M added NaCl or no added NaCl in 25\
    \ mM HEPES/KOH\n    pH 7.5, 1 mM EDTA and 1 mM DTT. The plotted DLS radius is\
    \ measured on the treated preparation. General\n    DLS Methods describe a 50-ul\
    \ cuvette and twenty 30-s acquisitions; these acquisitions are not independent\n\
    \    preparations. The untagged enzyme is reported to behave similarly, but its\
    \ unshown experiment is not\n    a separate edge.\n  family_mapping: Alpha-subunit\
    \ reference UniProtKB:Q05755 is 1515 aa, sequence version 1; PF01493 spans\n \
    \   1249-1496. UniProt and InterPro sequences agree. PDB 1EA0 polymer 1-1479 exactly\
    \ matches reference\n    37-1515, establishing the mature-protein offset of 36\
    \ and a mature-domain interval of 1213-1460. The\n    tested complex retains the\
    \ other alpha domains and beta partner. The reference sequence paper identifies\n\
    \    Sp7, but the complete 2008 clones and original donor strain were not independently\
    \ reconstructed.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:192\n  limitations:\
    \ DLS measures particle-size behavior, not domain-specific contact rupture or\
    \ unique oligomer\n    composition. SAXS and cryo-EM support an assembly interpretation\
    \ but use separate measurements and\n    mixture models. Some irreversible subunit\
    \ loss and activity decrease occur on prolonged salt treatment.\n    This is not\
    \ salt-dependent cellular regulation, isolated-domain sufficiency or an observed\
    \ electron-transfer\n    trajectory.\n  nodes:\n  - node_id: gltshis-one-molar-nacl\n\
    \    label: GltSHis incubated with 1 M added NaCl rather than no added NaCl for\
    \ 17 h\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q05755\n\
    \  - node_id: gltshis-dls-radius\n    label: DLS-derived radius of the purified\
    \ GltSHis particles\n    node_type: STATE\n  edges:\n  - edge_id: salt-decreases-gltshis-radius\n\
    \    subject: gltshis-one-molar-nacl\n    predicate: decreases\n    object: gltshis-dls-radius\n\
    \    mechanism: The 1-M-NaCl endpoint has a smaller measured particle radius than\
    \ the matched no-added-salt\n      preparation. The directly observed purified-complex\
    \ effect is retained without equating the DLS\n      readout with an atomically\
    \ resolved PF01493 interface transition.\n    directness: DIRECT\n    support:\
    \ OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:18199747\n\
    \      source_url: https://people.impmc.fr/sjonic/Papers/JBC_GltS.pdf\n      snippet:\
    \ calculated radius\n      explanation: Visually inspected supplemental Figure\
    \ 3C and its caption on supplement page 9 establish\n        the 17-h salt comparison;\
    \ main enzyme Methods and supplemental DLS Methods define the preparation\n  \
    \      and measurement.\n      cache_path: evidence/PF01493/cottevieille-2008-assembly.txt\n\
    \      cache_sha256: cb7d78a923b2aeb774855712227aa70f50c19af66cc12f781b33b86a04f17521\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q05755/entry/pfam/PF01493/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q05755/entry/pfam/PF01493/\n\
    \      snippet: 'Q05755 Pfam:PF01493; domain interval: 1249-1496, inclusive.'\n\
    \      explanation: Reference mapping and the exact 1EA0 sequence alignment distinguish\
    \ the mature alpha-subunit\n        numbering from precursor coordinates and from\
    \ the partner beta subunit.\n      cache_path: evidence/PF01493/GltS-identity.txt\n\
    \      cache_sha256: 156cb20252c22d4a17437babc87c16b813dfc77aa7f714b724c9812b21276e1d\n\
    - graph_id: azospirillum-glts-salt-dilution-radius\n  title: Salt dilution increases\
    \ particle radius after GltSHis salt treatment\n  scope: Purified wild-type-alpha/His6-beta\
    \ GltSHis in Cottevieille 2008 Figure S3D; a separate dilution\n    experiment,\
    \ not full recovery of all original complexes.\n  context: A 1.2-mg/ml sample\
    \ previously incubated for 17 h with 1 M NaCl is diluted tenfold into the\n  \
    \  same HEPES/EDTA/DTT buffer without NaCl. The matched control is diluted tenfold\
    \ into buffer containing\n    1 M NaCl. Calculated final protein is 0.12 mg/ml\
    \ in both; residual NaCl in the low-salt arm is 0.1\n    M, not zero. DLS follows\
    \ radius over approximately 500 s using 10-s acquisitions. General DLS temperature\n\
    \    is 15 C; the caption does not separately establish the pretreatment temperature\
    \ for this panel.\n  family_mapping: Q05755 alpha contains PF01493 at precursor\
    \ 1249-1496, corresponding to mature 1213-1460\n    after removal of residues\
    \ 1-36. The exact deposited mature sequence matches the current reference.\n \
    \   This assay uses intact alpha/beta complexes with beta, not alpha, carrying\
    \ the His6 extension.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:192\n \
    \ limitations: The two arms have matched dilution but different salt concentrations.\
    \ Increased hydrodynamic\n    size supports reassociation without proving exact\
    \ stoichiometry, complete recovery, a unique GXGXG-mediated\n    contact or a\
    \ cellular mechanism. A fitted single-exponential curve and repeated acquisitions\
    \ are not\n    independent biological replications or an atomistic rate constant.\n\
    \  nodes:\n  - node_id: salt-treated-gltshis-low-salt-dilution\n    label: Tenfold\
    \ dilution of salt-treated GltSHis into NaCl-free buffer instead of 1-M-NaCl buffer\n\
    \    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q05755\n  - node_id:\
    \ post-dilution-gltshis-radius\n    label: DLS-derived particle radius after dilution\n\
    \    node_type: STATE\n  edges:\n  - edge_id: low-salt-dilution-increases-radius\n\
    \    subject: salt-treated-gltshis-low-salt-dilution\n    predicate: increases\n\
    \    object: post-dilution-gltshis-radius\n    mechanism: The low-salt-dilution\
    \ trace increases while the equal-dilution high-salt control remains\n      near\
    \ its starting size. The net reassembly-associated size change is observed in\
    \ the purified preparation,\n      without asserting which domain supplies an\
    \ independently sufficient interface.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:18199747\n\
    \      source_url: https://people.impmc.fr/sjonic/Papers/JBC_GltS.pdf\n      snippet:\
    \ re-association\n      explanation: Visually inspected supplemental Figure 3D\
    \ and its caption distinguish both dilution\n        arms, the 17-h pretreatment,\
    \ starting concentration and 10-s measurement interval. Supplemental\n       \
    \ Table 1 supplies separate reversibility context, not identical conditions.\n\
    \      cache_path: evidence/PF01493/cottevieille-2008-assembly.txt\n      cache_sha256:\
    \ cb7d78a923b2aeb774855712227aa70f50c19af66cc12f781b33b86a04f17521\n- graph_id:\
    \ azospirillum-glts-delta40-expression\n  title: The delta40 alpha construct lacks\
    \ detectable production in the reported expression attempts\n  scope: A. brasilense\
    \ gltB C-terminal truncation coexpressed with His6-tagged beta in E. coli BL21(DE3),\n\
    \    as reported in Cottevieille 2008; an expression phenotype, not directly measured\
    \ folding failure.\n  context: pETGltSHis-derived T7 coproduction constructs encode\
    \ either wild-type, delta7 or delta40 alpha.\n    Supplemental Methods describe\
    \ 30-C growth to absorbance about 2 followed by 25 C without IPTG, with\n    delta40\
    \ attempts also using 25 C for 6-7 h or 15 C with 0.1 mM IPTG for 17 h. Delta7\
    \ production/purification\n    is retained, whereas no truncated delta40 polypeptide\
    \ production was observed. The main text compares\n    with the productive full-length\
    \ preparation. No plotted expression gel or detection threshold is supplied\n\
    \    for delta40 in the inspected material.\n  family_mapping: Q05755 precursor\
    \ 37-1515 matches mature 1EA0 residues 1-1479. The delta40 deletion maps\n   \
    \ to precursor 1476-1515, overlapping PF01493 at 1476-1496 and also removing an\
    \ outside-domain tail.\n    Reverse-complement translation of printed Oligo 3\
    \ ends at reference EEHVTETQSRF, residues 1465-1475,\n    followed by two stops.\
    \ Delta7 removes 1509-1515 outside PF01493; Oligo 2 locally matches the retained\n\
    \    terminus. Printed nucleotide stop-position prose does not fully agree with\
    \ this mapping; whole clones\n    remain unverified.\n  scope_status: PHENOTYPIC\n\
    \  taxon: NCBITaxon:192\n  limitations: This is a reported negative production\
    \ endpoint in a heterologous host, not a direct protein-folding,\n    degradation\
    \ or translation assay. Detection method, quantitative limits, independent clone\
    \ counts\n    and rescue are not established. The authors' exposed-hydrophobic-core\
    \ explanation remains an interpretation.\n    The deletion is not restricted to\
    \ PF01493, and the unaffected delta7 is outside its match; neither\n    result\
    \ proves isolated-domain assembly function.\n  nodes:\n  - node_id: gltb-delta40-coproduction\n\
    \    label: Reported delta40 alpha construct rather than productive full-length\
    \ alpha in the beta-His6\n      coproduction system\n    node_type: PERTURBATION\n\
    \    grounding:\n    - UniProtKB:Q05755\n  - node_id: detectable-alpha-polypeptide\n\
    \    label: Reported detectable alpha-polypeptide production in BL21(DE3)\n  \
    \  node_type: PHENOTYPE\n  edges:\n  - edge_id: delta40-decreases-detectable-alpha\n\
    \    subject: gltb-delta40-coproduction\n    predicate: decreases\n    object:\
    \ detectable-alpha-polypeptide\n    mechanism: The source reports no detectable\
    \ production of the delta40 alpha polypeptide across the\n      attempted expression\
    \ conditions, unlike the productive full-length and delta7 constructs. The observed\n\
    \      expression outcome is indirect with respect to folding or assembly and\
    \ is not converted into a uniquely\n      resolved molecular mechanism.\n    directness:\
    \ INDIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:18199747\n      source_url: https://people.impmc.fr/sjonic/Papers/JBC_GltS.pdf\n\
    \      snippet: no production\n      explanation: Main page 8245 and supplemental\
    \ construction/expression Methods on pages 1-2 report\n        the negative production\
    \ result. The Methods and printed primers were visually checked; a delta40\n \
    \       protein gel was not independently available for assessment.\n      cache_path:\
    \ evidence/PF01493/cottevieille-2008-assembly.txt\n      cache_sha256: cb7d78a923b2aeb774855712227aa70f50c19af66cc12f781b33b86a04f17521\n\
    \    - reference: https://files.rcsb.org/download/1EA0.cif\n      source_url:\
    \ https://files.rcsb.org/download/1EA0.cif\n      snippet: The deposited 1EA0\
    \ polymer is exactly Q05755 residues 37-1515.\n      explanation: Exact sequence\
    \ comparison and deposited alignment resolve the 36-residue numbering\n      \
    \  offset; only 21 deleted residues lie in the current Pfam interval.\n      cache_path:\
    \ evidence/PF01493/GltS-identity.txt\n      cache_sha256: 156cb20252c22d4a17437babc87c16b813dfc77aa7f714b724c9812b21276e1d\n\
    curation_events:\n- timestamp: '2026-10-11T10:58:40Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curated scoped GltS assembly and truncation\
    \ graphs for PF01493.\n  history_record: history/records/PF01493/2026-10-11T105840Z-codex-e03f25.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Q05755 sequence version 1 matches InterPro and contains PF01493 at 1249-1496.
    The 1479-aa 1EA0 polymer exactly equals reference 37-1515. Delta40 overlaps only
    21 domain residues and also removes an outside-domain tail; delta7 is outside
    the domain. Printed primer translations locally support the named deletions, but
    nucleotide-coordinate prose and full historical constructs remain unresolved.
  target_ids:
  - PF01493
  evidence_ids:
  - identity
  - primary
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: The two DIRECT MECHANISTIC edges retain size measurements, not uniquely
    resolved stoichiometry or domain-contact rupture. The low-salt dilution arm retains
    0.1 M NaCl and is not a zero-salt condition. The INDIRECT PHENOTYPIC edge reports
    delta40 production failure without converting it into measured misfolding. Contexts,
    controls, grounding and evidence references remain separated.
  target_ids:
  - PF01493
  evidence_ids:
  - primary
  - native
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Other GltS interventions, taxa, ferredoxin-dependent synthases and FwdC/FmdC
    members remain uncurated. The exact delta40 detection limit, independent constructs,
    rescue and domain-specific mediation were not established by the inspected material.
  target_ids:
  - PF01493
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01493-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Extend member and intervention coverage without treating assembly readouts
    as isolated-domain causality
  description: Resolve complete constructs and nucleotide-coordinate conventions;
    seek measurable expression/stability controls and domain-restricted assembly interventions.
    Curate additional family members from their own primary assays, preserving separate
    salt, ligand and kinetic conditions.
  target_ids:
  - PF01493
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01493.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Resolve complete constructs and nucleotide-coordinate conventions;
    seek measurable expression/stability controls and domain-restricted assembly interventions.
    Curate additional family members from their own primary assays, preserving separate
    salt, ligand and kinetic conditions.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01493
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Rechecked S3C-D visually in this review; prior research visually inspected main
  Table 2 and supplemental Methods pages 1-2. Raw scattering, reconstruction, unshown
  delta40 gels and full clones were not independently reanalyzed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
