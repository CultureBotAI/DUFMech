# PF01958 TM1643 redox observations and separated product and pathway interpretations

- Review: 20261012T143541Z-pf01958-tm1643-redox-and-separated-interpretations
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-12T14:34:42Z
- Finished UTC: 2026-10-12T14:35:41Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Partial same-agent scientific review of five graphs and eight edges. Six observed purified-enzyme redox/inhibition effects are separated from inferred iminoaspartate formation and a hypothetical cellular NAD-biosynthetic contribution. No isolated-domain or human substrate transfer is claimed.

## Scope And Provenance

Assess the curated edges against Yang2003 full text, Methods, TableII and figure legends; verify current TM1643/domain boundaries, product-detection limits and native representation. Inspect Li2017 full XML and selected original PDF figures for follow-up conflicts, plus primary bioRxiv metadata for the human ASPDH divergent-function preprint. Not a full family census or independent review.

Selection: Next ascending uncurated PF01958 record after PF01957; exact frozen identity retained, with mapped TM1643 experiments and explicit additional-member follow-ups.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01958 | data/families/PF01958.yaml | generated | PF01958 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01958 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01958.

Q9X1X6 v1 is the241-aa MSB8 nadX/TM_1643 reference with PF01958 121-234 and PF03447 41-106. These current Pfam hits differ from structural domain boundaries113-241/1-105. The paper assays intact N-terminal His6 protein; tag/plasmid sequence is not reconstructed. A6ND91 v2 maps PF01958 133-266 but its human function cannot be transferred from bacterial assays. Q0K391 isH16, notJMP134. 1H2H is the2.6-A paper structure, distinct from1J5P. Frozen fields remain unchanged.

### Directed effects and limits

graph: supported. Targets: PF01958.

Three MECHANISTIC graphs contain six OBSERVED/EXPERIMENTAL/DIRECT biochemical readout or inhibitor effects. Reactants are joint assay conditions, NAD/NADP and reverse donors are alternatives, and opposite directions retain different buffers and ammonium conditions. Two HYPOTHETICAL graphs retain one INFERRED contextual immediate product and one HYPOTHESIZED contextual cellular contribution, both UNRESOLVED. No transient product, His193 catalytic step, channeling complex, isolated-domain sufficiency or cellular flux is mislabeled observed. Human preprint and unresolved2017 mapping are explicit discussions, not imported causal edges.

### Remaining family coverage

completeness: concern. Targets: PF01958.

Original2003 figures/raw traces, historical construct sequences, inhibitor-specific controls, direct product identification, full archaeal/PAO1/JMP134/nitrogen-fixer studies, exact2017 member/domain mapping and full human2026 preprint/supplements remain open. Selected2017 images confirm source label conflicts; access limits do not prove absence of biology. All8296 records and earlier follow-ups remain within the active goal.

## Findings

### additional-contexts: Extend mapped AspDH contexts and assess divergent human chemistry

minor / open / confirmed; issue key: pf01958-causal-context-coverage.

Inspect remaining2003 original figures and construct controls, map2017 exact sequences before curating its assays and stability experiments, reconcile pH/lane/crude-versus-purified discrepancies, and review other bacterial/archaeal primary experiments. Obtain accessible humanASPDH full text/supplements, verify construct, product and isotope evidence, and preserve preprint status. Do not transfer H16 toJMP134 or bacterial aspartate activity tohumanASPDH. Retain the immediate-product and cellular-role evidence distinctions.

## Recommended Actions And Acceptance Checks

### extend-contexts

Inspect remaining2003 original figures and construct controls, map2017 exact sequences before curating its assays and stability experiments, reconcile pH/lane/crude-versus-purified discrepancies, and review other bacterial/archaeal primary experiments. Obtain accessible humanASPDH full text/supplements, verify construct, product and isotope evidence, and preserve preprint status. Do not transfer H16 toJMP134 or bacterial aspartate activity tohumanASPDH. Retain the immediate-product and cellular-role evidence distinctions.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://doi.org/10.1074/jbc.M211892200; Yang2003 pp8804-8807 Expression/Purification, Enzymatic Studies, Characterization Results, Figure2/5 legends, TableII and Possible Role discussion; author-uploaded full text/PDF text | supports | Full purified TM1643 supports separate oxidative/reductive cofactor readouts and reported inhibition by L-malate/ammonium. Immediate iminoaspartate is inferred from chemistry and downstream coupled assays; cellular NAD synthesis and channeling are proposed. Original2003 plot images were not inspected. |
| identity | https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/Q9X1X6/; Accession and domain locations; paired UniProt identity facts | supports | Q9X1X6 v1 is the241-aa MSB8 nadX/TM_1643 reference with PF01958 121-234 and PF03447 41-106. These current Pfam hits differ from structural domain boundaries113-241/1-105. The paper assays intact N-terminal His6 protein; tag/plasmid sequence is not reconstructed. A6ND91 v2 maps PF01958 133-266 but its human function cannot be transferred from bacterial assays. Q0K391 isH16, notJMP134. 1H2H is the2.6-A paper structure, distinct from1J5P. Frozen fields remain unchanged. |
| mesophilic-mapping | https://pmc.ncbi.nlm.nih.gov/articles/PMC5554190/; Li2017 full XML Results/Methods/tables and visually inspected publisher PDF pages2/4/5 | supports | Purified tagged Kpn/Del enzyme assays use different conditions fromThermotoga. Figure2 supports Results pH assignments contradicted byDiscussion; lane labels, Reu/Bja values and crude-versus-purifiedKpnNADH results need reconciliation. Exact current construct/domain crosswalk remains open. |
| human-preprint | https://api.biorxiv.org/details/biorxiv/10.64898/2026.06.05.730449; Version1 metadata and abstract retrieved2026-10-12; related institutional thesis abstract and access-attempt ledger | supports | The primary preprint abstract reports human2-aminomuconate reduction to a novel amino-acid product. Version1 is dated2026-06-09 and published statusNA; source.xml429 and article403 leave the detailed evidence unreviewed. No human observed graph is added from abstract-only coverage. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01958 | data/families/PF01958.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Yang2003 author-uploaded primary full text and PDF text were read, including relevant Methods, TableII and Figure2/5 legends; original plot screenshots timed out and direct downloads returned403. Li2017 PDF pages2/4/5 were visually inspected, including Figure1 and Figures2/3, not Figure4 sequence alignment or all pages. Human2026 primary API abstract/metadata and institutional thesis abstract were read, not full preprint assays/spectra or embargoed thesis. No experimental replication.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.
- Ignored and hidden curation/evidence/history/structured-review files were included in the pre-addition collision search; none containedPF01958. The existing progress document already named it as next.
- A first history command used a malformed timestamp without time colons and was rejected; the same actual session start was then supplied in validISO8601. No generated record or history was manually patched to bypass validation.
- Original2003 primary content was accessible through the author's public upload despite publisher403 responses. The inability to retrieve images is retained as a visual-review limitation, not a filesystem denial.
- Minimal retained excerpts and all identity/context ledgers are hash-bound to this review. The frozen source snapshot and main checkout are untouched.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T143541Z-pf01958-tm1643-redox-and-separated-interpretations
title: PF01958 TM1643 redox observations and separated product and pathway interpretations
started_at: '2026-10-12T14:34:42Z'
finished_at: '2026-10-12T14:35:41Z'
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
summary: Partial same-agent scientific review of five graphs and eight edges. Six
  observed purified-enzyme redox/inhibition effects are separated from inferred iminoaspartate
  formation and a hypothetical cellular NAD-biosynthetic contribution. No isolated-domain
  or human substrate transfer is claimed.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01958.yaml
    sha256: 6c8462b6bdfcc165f5d2f4d8ac17cfe85fe9855d3d150eab4a28ea77af4f81b5
    role: context
  - path: data/families/PF01958.yaml
    sha256: f352c1ec2ce3ef2f434d37bf980e411ff9d2e0d2706c0f97138071af6e29b9b2
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
  - path: evidence/PF01958/yang-2003-tm1643-assays.txt
    role: context
    sha256: c7e0f39a854454c83b9db5359852dfa2679df8d08cc53e78357469f9a6da1ee0
  - path: evidence/PF01958/identity-and-domain-boundaries.txt
    role: context
    sha256: 7e5c42dc830779e2b8bffc6caf46e72bc62fc2e4400b98938c26ec60197877cc
  - path: evidence/PF01958/li-2017-mapping-and-assay-followups.txt
    role: context
    sha256: a64ed6682ef2d75e06bac5bb7a6fbe743bc8a0872dcf51d352eb69e83d21959d
  - path: evidence/PF01958/human-aspdh-preprint-followup.txt
    role: context
    sha256: e58ec3a1e588f13e7e10e3ed8a6eb798b7e719d5a78147cb2c7676f3224388bd
targets:
- target_id: PF01958
  path: data/families/PF01958.yaml
  label: PF01958
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01958.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 4304878e5b386368131f2e5c039492ad606ff9f56c699b3e329ad2de419de24a
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Assess the curated edges against Yang2003 full text, Methods, TableII
    and figure legends; verify current TM1643/domain boundaries, product-detection
    limits and native representation. Inspect Li2017 full XML and selected original
    PDF figures for follow-up conflicts, plus primary bioRxiv metadata for the human
    ASPDH divergent-function preprint. Not a full family census or independent review.
  selection: Next ascending uncurated PF01958 record after PF01957; exact frozen identity
    retained, with mapped TM1643 experiments and explicit additional-member follow-ups.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01958
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Original2003 figures/raw traces, historical construct sequences, inhibitor-specific
      controls, direct product identification, full archaeal/PAO1/JMP134/nitrogen-fixer
      studies, exact2017 member/domain mapping and full human2026 preprint/supplements
      remain open. Selected2017 images confirm source label conflicts; access limits
      do not prove absence of biology. All8296 records and earlier follow-ups remain
      within the active goal.
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
  - PF01958
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1074/jbc.M211892200
  locator: Yang2003 pp8804-8807 Expression/Purification, Enzymatic Studies, Characterization
    Results, Figure2/5 legends, TableII and Possible Role discussion; author-uploaded
    full text/PDF text
  accessed_at: '2026-10-12T14:35:41Z'
  support: supports
  snapshot_sha256: c7e0f39a854454c83b9db5359852dfa2679df8d08cc53e78357469f9a6da1ee0
  summary: Full purified TM1643 supports separate oxidative/reductive cofactor readouts
    and reported inhibition by L-malate/ammonium. Immediate iminoaspartate is inferred
    from chemistry and downstream coupled assays; cellular NAD synthesis and channeling
    are proposed. Original2003 plot images were not inspected.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/Q9X1X6/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-12T14:35:41Z'
  support: supports
  snapshot_sha256: 7e5c42dc830779e2b8bffc6caf46e72bc62fc2e4400b98938c26ec60197877cc
  summary: Q9X1X6 v1 is the241-aa MSB8 nadX/TM_1643 reference with PF01958 121-234
    and PF03447 41-106. These current Pfam hits differ from structural domain boundaries113-241/1-105.
    The paper assays intact N-terminal His6 protein; tag/plasmid sequence is not reconstructed.
    A6ND91 v2 maps PF01958 133-266 but its human function cannot be transferred from
    bacterial assays. Q0K391 isH16, notJMP134. 1H2H is the2.6-A paper structure, distinct
    from1J5P. Frozen fields remain unchanged.
- evidence_id: mesophilic-mapping
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5554190/
  locator: Li2017 full XML Results/Methods/tables and visually inspected publisher
    PDF pages2/4/5
  summary: Purified tagged Kpn/Del enzyme assays use different conditions fromThermotoga.
    Figure2 supports Results pH assignments contradicted byDiscussion; lane labels,
    Reu/Bja values and crude-versus-purifiedKpnNADH results need reconciliation. Exact
    current construct/domain crosswalk remains open.
  accessed_at: '2026-10-12T14:35:41Z'
  support: supports
  snapshot_sha256: a64ed6682ef2d75e06bac5bb7a6fbe743bc8a0872dcf51d352eb69e83d21959d
- evidence_id: human-preprint
  kind: primary_source
  reference: https://api.biorxiv.org/details/biorxiv/10.64898/2026.06.05.730449
  locator: Version1 metadata and abstract retrieved2026-10-12; related institutional
    thesis abstract and access-attempt ledger
  summary: The primary preprint abstract reports human2-aminomuconate reduction to
    a novel amino-acid product. Version1 is dated2026-06-09 and published statusNA;
    source.xml429 and article403 leave the detailed evidence unreviewed. No human
    observed graph is added from abstract-only coverage.
  accessed_at: '2026-10-12T14:35:41Z'
  support: supports
  snapshot_sha256: e58ec3a1e588f13e7e10e3ed8a6eb798b7e719d5a78147cb2c7676f3224388bd
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-12T14:35:41Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01958
  kind: record_content
  reference: data/families/PF01958.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-12T14:35:41Z'
  support: context_only
  snapshot_sha256: f352c1ec2ce3ef2f434d37bf980e411ff9d2e0d2706c0f97138071af6e29b9b2
  quote: "id: Pfam:PF01958\npfam_id: PF01958\nname: Aspartate dehydrogenase, C-terminal\n\
    short_name: Asp_DH_C\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01958\n\
    counters:\n  proteins: 3184\n  matches: 3195\n  proteomes: 2698\n  taxa: 5585\n\
    \  structures: 3\n  alphafold_models: 2258\n  domain_architectures: 31\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002811\ndescription: This entry represents the C-terminal\
    \ domain of aspartate dehydrogenases that belong to a\n  unique class of amino\
    \ acid dehydrogenases. The structure of Thermotoga maritima TM1643 has been found\n\
    \  to contain an N-terminal Rossmann fold domain (which binds the NAD(P)+ cofactor)\
    \ and a C-terminal alpha/beta\n  domain [[cite:PUB00014412]]. Enzymatic characterisation\
    \ of TM1643 revealed that it possesses NAD or\n  NADP-dependent dehydrogenase\
    \ activity toward L-aspartate but no aspartate oxidase activity [[cite:PUB00014412]].\n\
    \  Members of this group share some structural similarity to several other NAD(P)+-dependent\
    \ oxidoreductases,\n  including inositol 1-phosphate synthase, dihydrodipicolinate\
    \ reductase, and ASA-DH [[cite:PUB00014412]].\n  It has been proposed that in\
    \ Thermotoga maritima, TM1643 catalyses the first reaction of de novo biosynthesis\n\
    \  of NAD from aspartate, and it produces iminoaspartate required for this pathway.\n\
    curation_history: history/records/PF01958\ndiscussions:\n- discussion_id: pf01958-causal-context-coverage\n\
    \  prompt: Extend verified AspDH member contexts and resolve construct, product\
    \ and source-label uncertainties.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale:\
    \ TM1643 assays support cofactor redox activity, but neither an isolated PF01958\
    \ mechanism\n    nor complete family coverage. Other bacterial and archaeal experiments\
    \ require their own mapping and\n    primary-source assessment.\n  evidence:\n\
    \  - reference: PMID:12496312\n    supports: PARTIAL\n    evidence_source: primary_publication\n\
    \    explanation: Full text/Methods/TableII were inspected; original Figure5 plots\
    \ were not visually available.\n      Iminoaspartate and cellular NAD synthesis\
    \ are not directly demonstrated.\n  - reference: PMID:28801651\n    supports:\
    \ PARTIAL\n    evidence_source: primary_publication\n    explanation: Full text\
    \ and selected original figures expose label/condition conflicts; exact 2017\n\
    \      constructs have not been mapped to current Pfam coordinates.\n  posed_by:\
    \ Codex\n  posed_date: '2026-10-12'\n  notes: Inspect 2003 original figures/raw\
    \ data, 2006/2007 archaeal studies, PAO1/JMP1342011, nitrogen-fixer2013\n    and\
    \ further member experiments. Resolve 2017 Figure1 lane labels, reversed pH and\
    \ Reu/Bja activity\n    assignments, purified-versus-crude NADH differences and\
    \ Figure4 sequences. Q0K391 is H16, not JMP134.\n    No family-wide substrate\
    \ specificity, catalytic His193 proof or NAD-channeling complex is established\n\
    \    here. All earlier corpus follow-ups remain open.\n- discussion_id: pf01958-human-aspdh-divergence\n\
    \  prompt: Assess the human 2-aminomuconate reductase preprint independently of\
    \ bacterial aspartate dehydrogenation.\n  kind: CURATION_TODO\n  status: OPEN\n\
    \  rationale: Human ASPDH contains PF01958 but a primary 2026 preprint reports\
    \ a different substrate and\n    product; conserved domains do not justify transferring\
    \ the bacterial physiological assignment.\n  evidence:\n  - reference: doi:10.64898/2026.06.05.730449\n\
    \    supports: PARTIAL\n    evidence_source: primary_publication\n    explanation:\
    \ bioRxiv version1 abstract/API metadata were inspected, not full assays, spectra,\
    \ controls\n      or construct sequence. Published field was NA.\n  - reference:\
    \ https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/A6ND91/\n    supports:\
    \ SUPPORT\n    evidence_source: database\n    explanation: Human reference A6ND91\
    \ v2 is 283 aa; PF01958 133-266 and PF03447 13-123.\n  posed_by: Codex\n  posed_date:\
    \ '2026-10-12'\n  notes: Obtain accessible full text and supplements; inspect\
    \ product identification, isotope/stereochemical\n    evidence and exact tested\
    \ construct before adding a separate human graph. Preprint status remains\n  \
    \  explicit. Primary article/source requests returned403/429; the related 2026\
    \ thesis is embargoed. No\n    access bypass or inferred human AspDH activity.\n\
    causal_graphs:\n- graph_id: thermotoga-tm1643-oxidative-redox-2003\n  title: TM1643\
    \ reduces NAD or NADP in separate L-aspartate assays\n  scope: Purified full-length\
    \ Thermotoga maritima TM1643 with an N-terminal His6 tag, expressed in E.\n  \
    \  coli BL21(DE3); not an isolated C-terminal domain.\n  context: Yang2003 Enzymatic\
    \ Studies, Figure5A-C/legend and TableII; 70C, 50mM diethanolamine pH9.8,\n  \
    \  5mM L-Asp and 1mM NAD+ or NADP+ for the individual-amino-acid assay. Kinetic\
    \ substrate concentrations\n    are varied separately; A340 increase is the measured\
    \ redox readout.\n  family_mapping: Q9X1X6 v1 is the 241-aa MSB8 nadX/TM_1643\
    \ reference; PF01958 121-234 and PF03447 41-106.\n    Paper structural boundaries\
    \ 113-241 and 1-105 differ from current Pfam hits. Historical tagged construct\n\
    \    sequence was not independently reconstructed.\n  taxon: NCBITaxon:243274\n\
    \  scope_status: MECHANISTIC\n  limitations: No activity was reported with D-Asp,\
    \ L-Glu or Asn in these tests. No direct identification\n    of the immediate\
    \ iminoaspartate product, isolated-domain sufficiency or cellular flux follows.\
    \ Figure5\n    text/legend and TableII were read but original plots were not visually\
    \ inspected. Replicate counts\n    and primary traces remain unreviewed.\n  nodes:\n\
    \  - node_id: nad-mix\n    label: Purified TM1643 with L-Asp and NAD+ at pH9.8\
    \ and 70C\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:Q9X1X6\n \
    \ - node_id: nadh\n    label: NADH accumulation measured by increasing A340\n\
    \    node_type: STATE\n  - node_id: nadp-mix\n    label: Purified TM1643 with\
    \ L-Asp and NADP+ at pH9.8 and 70C\n    node_type: ACTIVITY\n    grounding:\n\
    \    - UniProtKB:Q9X1X6\n  - node_id: nadph\n    label: NADPH accumulation measured\
    \ by increasing A340\n    node_type: STATE\n  edges:\n  - edge_id: nad-reduction\n\
    \    subject: nad-mix\n    predicate: produces\n    object: nadh\n    mechanism:\
    \ Purified full-protein activity couples L-Asp-dependent oxidation to NAD reduction;\
    \ the\n      graph claims the cofactor readout, not direct detection of the unstable\
    \ amino-acid-derived product.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:12496312\n\
    \      source_url: https://doi.org/10.1074/jbc.M211892200\n      snippet: robust\
    \ dehydrogenase activity\n      explanation: Enzymatic Studies, Characterization\
    \ Results, Figure5B/C legend and TableII distinguish\n        the NAD assay and\
    \ its substrate-dependent kinetics.\n      cache_path: evidence/PF01958/yang-2003-tm1643-assays.txt\n\
    \      cache_sha256: c7e0f39a854454c83b9db5359852dfa2679df8d08cc53e78357469f9a6da1ee0\n\
    \  - edge_id: nadp-reduction\n    subject: nadp-mix\n    predicate: produces\n\
    \    object: nadph\n    mechanism: A separate NADP-containing reaction supports\
    \ L-Asp-dependent NADPH production; this does\n      not establish the preferred\
    \ physiological cofactor or an independent domain reaction.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:12496312\n      source_url: https://doi.org/10.1074/jbc.M211892200\n\
    \      snippet: robust dehydrogenase activity\n      explanation: Enzymatic Studies,\
    \ Characterization Results, Figure5A/C legend and TableII distinguish\n      \
    \  NADP-dependent reduction from the NAD condition.\n      cache_path: evidence/PF01958/yang-2003-tm1643-assays.txt\n\
    \      cache_sha256: c7e0f39a854454c83b9db5359852dfa2679df8d08cc53e78357469f9a6da1ee0\n\
    - graph_id: thermotoga-tm1643-reverse-redox-2003\n  title: TM1643 reverse-assay\
    \ mixtures consume NADH or NADPH\n  scope: The same purified full-length N-terminal\
    \ His6 TM1643 preparation, in separate reductive-direction\n    assays.\n  context:\
    \ Yang2003 reverse assay at70C; 1ml with 50mM Tris-HCl pH8.0, 100mM ammonium sulfate,\
    \ 0.1mM EDTA,\n    5mM oxaloacetate and 0.15mM NADH or NADPH; decreasing A340\
    \ is monitored. These conditions are distinct\n    from the oxidative pH9.8 assays.\n\
    \  family_mapping: Q9X1X6 v1; PF01958 121-234 within the intact 241-aa TM1643\
    \ reference, alongside PF03447\n    41-106. No isolated PF01958 reaction or historical\
    \ tag-sequence reconstruction.\n  taxon: NCBITaxon:243274\n  scope_status: MECHANISTIC\n\
    \  limitations: The text reports both donors effective but does not supply a reverse-reaction\
    \ figure, full\n    kinetic comparison or product-specific L-Asp quantification.\
    \ No equality of all donor kinetic parameters,\n    individual-reagent sufficiency\
    \ or physiological reductive flux is claimed.\n  nodes:\n  - node_id: nadh-mix\n\
    \    label: TM1643 with oxaloacetate and ammonium sulfate in the NADH assay\n\
    \    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:Q9X1X6\n  - node_id:\
    \ nadh\n    label: NADH pool measured by A340\n    node_type: STATE\n  - node_id:\
    \ nadph-mix\n    label: TM1643 with oxaloacetate and ammonium sulfate in the NADPH\
    \ assay\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:Q9X1X6\n  -\
    \ node_id: nadph\n    label: NADPH pool measured by A340\n    node_type: STATE\n\
    \  edges:\n  - edge_id: nadh-consumption\n    subject: nadh-mix\n    predicate:\
    \ decreases\n    object: nadh\n    mechanism: The complete purified-enzyme reaction\
    \ consumes reduced cofactor in the reported reductive-amination\n      assay;\
    \ its amino-acid product is not separately measured in this graph.\n    directness:\
    \ DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n\
    \    - reference: PMID:12496312\n      source_url: https://doi.org/10.1074/jbc.M211892200\n\
    \      snippet: NADPH and NADH were equally effective as electron donors.\n  \
    \    explanation: Enzymatic Studies defines the joint reaction mixture and A340\
    \ decrease; Characterization\n        Results reports the reverse reaction with\
    \ NADH.\n      cache_path: evidence/PF01958/yang-2003-tm1643-assays.txt\n    \
    \  cache_sha256: c7e0f39a854454c83b9db5359852dfa2679df8d08cc53e78357469f9a6da1ee0\n\
    \  - edge_id: nadph-consumption\n    subject: nadph-mix\n    predicate: decreases\n\
    \    object: nadph\n    mechanism: The separate complete NADPH-containing reaction\
    \ consumes reduced cofactor; no direct L-Asp\n      yield or cellular reverse-pathway\
    \ claim is added.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:12496312\n      source_url:\
    \ https://doi.org/10.1074/jbc.M211892200\n      snippet: NADPH and NADH were equally\
    \ effective as electron donors.\n      explanation: The same Methods and Results\
    \ explicitly test NADPH as an alternative donor, not simultaneous\n        NADH-plus-NADPH\
    \ dependence.\n      cache_path: evidence/PF01958/yang-2003-tm1643-assays.txt\n\
    \      cache_sha256: c7e0f39a854454c83b9db5359852dfa2679df8d08cc53e78357469f9a6da1ee0\n\
    - graph_id: thermotoga-tm1643-oxidative-inhibition-2003\n  title: L-malate and\
    \ ammonium reduce TM1643 oxidative activity\n  scope: Purified full-length TM1643\
    \ oxidative L-aspartate dehydrogenase assays; inhibitors tested separately.\n\
    \  context: Yang2003 Characterization Results reports competitive inhibition by\
    \ L-malate and ammonium with\n    Ki4.02+/-0.48mM and32.5+/-4.9mM respectively.\
    \ General oxidative assay conditions are70C/pH9.8; inhibitor-specific\n    donor\
    \ assignment and complete assay matrices are not supplied in the inspected passage.\n\
    \  family_mapping: Intact Q9X1X6/TM1643 reference contains PF01958 121-234 and\
    \ PF03447 41-106; inhibitor\n    effects are not assigned to an isolated domain\
    \ or residue.\n  taxon: NCBITaxon:243274\n  scope_status: MECHANISTIC\n  limitations:\
    \ Purified-enzyme rate effects support biochemical inhibition, but no binding-site\
    \ occupancy,\n    inhibitor plot, counterion control or cellular effect was inspected.\
    \ Competitive classification is\n    the authors' reported kinetic interpretation.\
    \ Ammonium has a different role in the reverse assay;\n    these graphs do not\
    \ form a feedback cycle.\n  nodes:\n  - node_id: malate\n    label: L-malate added\
    \ to the purified TM1643 oxidative assay\n    node_type: PERTURBATION\n  - node_id:\
    \ ammonium\n    label: Ammonium added to the purified TM1643 oxidative assay\n\
    \    node_type: PERTURBATION\n  - node_id: rate\n    label: TM1643 L-Asp-dependent\
    \ oxidative dehydrogenase rate\n    node_type: ACTIVITY\n    grounding:\n    -\
    \ UniProtKB:Q9X1X6\n  edges:\n  - edge_id: malate-inhibition\n    subject: malate\n\
    \    predicate: decreases\n    object: rate\n    mechanism: L-malate reduces the\
    \ purified enzyme's measured oxidative activity; direct biochemical\n      inhibition\
    \ does not establish a particular binding geometry.\n    directness: DIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:12496312\n      source_url: https://doi.org/10.1074/jbc.M211892200\n\
    \      snippet: were competitive inhibitors\n      explanation: Characterization\
    \ Results distinguishes L-malate inhibition from the tested D-malate\n       \
    \ and other noninhibiting compounds; underlying curves were not inspected.\n \
    \     cache_path: evidence/PF01958/yang-2003-tm1643-assays.txt\n      cache_sha256:\
    \ c7e0f39a854454c83b9db5359852dfa2679df8d08cc53e78357469f9a6da1ee0\n  - edge_id:\
    \ ammonium-inhibition\n    subject: ammonium\n    predicate: decreases\n    object:\
    \ rate\n    mechanism: Ammonium reduces oxidative activity under the reported\
    \ inhibition test; it is not a claim\n      that ammonium blocks all TM1643 reaction\
    \ conditions.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:12496312\n      source_url:\
    \ https://doi.org/10.1074/jbc.M211892200\n      snippet: were competitive inhibitors\n\
    \      explanation: The same Results passage reports ammonium inhibition and its\
    \ Ki separately from the\n        reverse reaction containing ammonium sulfate.\n\
    \      cache_path: evidence/PF01958/yang-2003-tm1643-assays.txt\n      cache_sha256:\
    \ c7e0f39a854454c83b9db5359852dfa2679df8d08cc53e78357469f9a6da1ee0\n- graph_id:\
    \ thermotoga-tm1643-iminoaspartate-interpretation-2003\n  title: Inferred immediate\
    \ product of TM1643 aspartate oxidation\n  scope: Interpretation of the purified\
    \ full-length TM1643 oxidative assay, not direct product identification.\n  context:\
    \ Yang2003 Figure2/legend and Characterization Results. NAD(P)H formation is measured;\
    \ ammonium\n    and pyruvate are reported from coupled assays with data not shown.\
    \ Oxaloacetate was not detected atpH9.8/70C.\n  family_mapping: Q9X1X6/TM1643\
    \ contains PF01958 121-234 and PF03447 41-106; the inference concerns the\n  \
    \  intact enzyme only.\n  taxon: NCBITaxon:243274\n  scope_status: HYPOTHETICAL\n\
    \  limitations: Iminoaspartate is inferred from redox chemistry and downstream\
    \ product evidence, not directly\n    measured. Hydrolysis and decarboxylation\
    \ are not asserted as TM1643-catalyzed steps. No residue-level\n    acid/base\
    \ sequence or domain sufficiency is demonstrated.\n  nodes:\n  - node_id: oxidation\n\
    \    label: TM1643 L-Asp oxidation coupled to NAD(P)+ reduction\n    node_type:\
    \ ACTIVITY\n    grounding:\n    - UniProtKB:Q9X1X6\n  - node_id: imine\n    label:\
    \ Proposed transient iminoaspartate product\n    node_type: STATE\n  edges:\n\
    \  - edge_id: inferred-imine\n    subject: oxidation\n    predicate: produces\n\
    \    object: imine\n    mechanism: The authors interpret the redox and downstream\
    \ coupled-assay observations as transient\n      iminoaspartate formation before\
    \ aqueous decomposition; direct chemical identification remains missing.\n   \
    \ directness: UNRESOLVED\n    support: INFERRED\n    evidence_kind: CONTEXTUAL\n\
    \    evidence:\n    - reference: PMID:12496312\n      source_url: https://doi.org/10.1074/jbc.M211892200\n\
    \      snippet: expected to produce iminoaspartate\n      explanation: The Results\
    \ wording qualifies the immediate product; the abstract alone would overstate\n\
    \        the directness of product identification.\n      cache_path: evidence/PF01958/yang-2003-tm1643-assays.txt\n\
    \      cache_sha256: c7e0f39a854454c83b9db5359852dfa2679df8d08cc53e78357469f9a6da1ee0\n\
    - graph_id: thermotoga-tm1643-nad-biosynthesis-proposal-2003\n  title: Proposed\
    \ contribution of TM1643 to cellular NAD biosynthesis\n  scope: A physiological\
    \ hypothesis for Thermotoga maritima TM1643, separate from purified-enzyme observations\n\
    \    and other family members.\n  context: Yang2003 Possible Role discussion combines\
    \ the enzyme results with predicted nadA/nadC genomic\n    context and the authors'\
    \ reported absence of an identified NadB homolog. No current exhaustive genome-absence\n\
    \    search was performed here.\n  family_mapping: The mapped reference Q9X1X6\
    \ contains PF01958 121-234, but physiological assignment belongs\n    to the intact\
    \ protein and organism. Human ASPDH must be evaluated separately.\n  taxon: NCBITaxon:243274\n\
    \  scope_status: HYPOTHETICAL\n  limitations: No in vivo knockout/rescue, flux\
    \ experiment, NadA-coupled product assay or physical channeling-complex\n    demonstration\
    \ was inspected. The proposed contribution does not establish essentiality, isolated-domain\n\
    \    sufficiency or conservation throughout PF01958.\n  nodes:\n  - node_id: supply\n\
    \    label: Proposed TM1643-dependent iminoaspartate supply in the cell\n    node_type:\
    \ ACTIVITY\n    grounding:\n    - UniProtKB:Q9X1X6\n  - node_id: pathway\n   \
    \ label: Downstream NAD biosynthesis through the proposed NadA/NadC pathway\n\
    \    node_type: PROCESS\n  edges:\n  - edge_id: proposed-nad-contribution\n  \
    \  subject: supply\n    predicate: enables\n    object: pathway\n    mechanism:\
    \ The authors propose that the enzyme provides the unstable substrate for downstream\
    \ NAD\n      synthesis; this cellular contribution remains a contextual hypothesis,\
    \ not an observed pathway chain.\n    directness: UNRESOLVED\n    support: HYPOTHESIZED\n\
    \    evidence_kind: CONTEXTUAL\n    evidence:\n    - reference: PMID:12496312\n\
    \      source_url: https://doi.org/10.1074/jbc.M211892200\n      snippet: We propose\
    \ therefore\n      explanation: Possible Role discussion explicitly proposes the\
    \ physiological assignment and possible\n        channeling; neither is converted\
    \ into an observed cellular effect.\n      cache_path: evidence/PF01958/yang-2003-tm1643-assays.txt\n\
    \      cache_sha256: c7e0f39a854454c83b9db5359852dfa2679df8d08cc53e78357469f9a6da1ee0\n\
    curation_events:\n- timestamp: '2026-10-12T14:30:32Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate scoped TM1643 redox graphs and\
    \ distinguish product and physiological interpretations\n  history_record: history/records/PF01958/2026-10-12T143032Z-codex-f1e6ef.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: Q9X1X6 v1 is the241-aa MSB8 nadX/TM_1643 reference with PF01958 121-234
    and PF03447 41-106. These current Pfam hits differ from structural domain boundaries113-241/1-105.
    The paper assays intact N-terminal His6 protein; tag/plasmid sequence is not reconstructed.
    A6ND91 v2 maps PF01958 133-266 but its human function cannot be transferred from
    bacterial assays. Q0K391 isH16, notJMP134. 1H2H is the2.6-A paper structure, distinct
    from1J5P. Frozen fields remain unchanged.
  target_ids:
  - PF01958
  evidence_ids:
  - identity
  - primary
  - mesophilic-mapping
  - human-preprint
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Three MECHANISTIC graphs contain six OBSERVED/EXPERIMENTAL/DIRECT biochemical
    readout or inhibitor effects. Reactants are joint assay conditions, NAD/NADP and
    reverse donors are alternatives, and opposite directions retain different buffers
    and ammonium conditions. Two HYPOTHETICAL graphs retain one INFERRED contextual
    immediate product and one HYPOTHESIZED contextual cellular contribution, both
    UNRESOLVED. No transient product, His193 catalytic step, channeling complex, isolated-domain
    sufficiency or cellular flux is mislabeled observed. Human preprint and unresolved2017
    mapping are explicit discussions, not imported causal edges.
  target_ids:
  - PF01958
  evidence_ids:
  - primary
  - native
  - mesophilic-mapping
  - human-preprint
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Original2003 figures/raw traces, historical construct sequences, inhibitor-specific
    controls, direct product identification, full archaeal/PAO1/JMP134/nitrogen-fixer
    studies, exact2017 member/domain mapping and full human2026 preprint/supplements
    remain open. Selected2017 images confirm source label conflicts; access limits
    do not prove absence of biology. All8296 records and earlier follow-ups remain
    within the active goal.
  target_ids:
  - PF01958
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01958-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Extend mapped AspDH contexts and assess divergent human chemistry
  description: Inspect remaining2003 original figures and construct controls, map2017
    exact sequences before curating its assays and stability experiments, reconcile
    pH/lane/crude-versus-purified discrepancies, and review other bacterial/archaeal
    primary experiments. Obtain accessible humanASPDH full text/supplements, verify
    construct, product and isotope evidence, and preserve preprint status. Do not
    transfer H16 toJMP134 or bacterial aspartate activity tohumanASPDH. Retain the
    immediate-product and cellular-role evidence distinctions.
  target_ids:
  - PF01958
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - mesophilic-mapping
  - human-preprint
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01958.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Inspect remaining2003 original figures and construct controls, map2017
    exact sequences before curating its assays and stability experiments, reconcile
    pH/lane/crude-versus-purified discrepancies, and review other bacterial/archaeal
    primary experiments. Obtain accessible humanASPDH full text/supplements, verify
    construct, product and isotope evidence, and preserve preprint status. Do not
    transfer H16 toJMP134 or bacterial aspartate activity tohumanASPDH. Retain the
    immediate-product and cellular-role evidence distinctions.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01958
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Yang2003 author-uploaded primary full text and PDF text were read, including relevant
  Methods, TableII and Figure2/5 legends; original plot screenshots timed out and
  direct downloads returned403. Li2017 PDF pages2/4/5 were visually inspected, including
  Figure1 and Figures2/3, not Figure4 sequence alignment or all pages. Human2026 primary
  API abstract/metadata and institutional thesis abstract were read, not full preprint
  assays/spectra or embargoed thesis. No experimental replication.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
- Ignored and hidden curation/evidence/history/structured-review files were included
  in the pre-addition collision search; none containedPF01958. The existing progress
  document already named it as next.
- A first history command used a malformed timestamp without time colons and was rejected;
  the same actual session start was then supplied in validISO8601. No generated record
  or history was manually patched to bypass validation.
- Original2003 primary content was accessible through the author's public upload despite
  publisher403 responses. The inability to retrieve images is retained as a visual-review
  limitation, not a filesystem denial.
- Minimal retained excerpts and all identity/context ledgers are hash-bound to this
  review. The frozen source snapshot and main checkout are untouched.
```
