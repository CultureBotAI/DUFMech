# PF02130 YbeY RNA-cleavage and conjunctive ribosome-assay review

- Review: 20261011T055552Z-pf02130-ybey-causal-graphs
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T05:55:42Z
- Finished UTC: 2026-10-11T05:55:52Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Three direct observed edges retain model-RNA cleavage and rRNA degradation by joint YbeY plus RNase R in two distinct defective-70S preparations, without inventing ordered catalytic microsteps.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: Former UPF0054 selected for primary E. coli biochemistry and to separate it from DUF6647 structural analogies.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF02130 | data/families/PF02130.yaml | generated | PF02130 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF02130 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF02130.

The paper's historical P77385 identifier is now demerged. E. coli context resolves it to P0A898 (b0659/JW0656; sequence version 1; 155 residues; PF02130 at 21-144), not the identical-sequence Shigella successor P0A899. Exact purified tag, construct sequence and expression host remain unverified because the extended methods were not retrieved. Reference mapping does not imply an isolated-domain experiment.

### Directed effects and limits

graph: supported. Targets: PF02130.

Two MECHANISTIC graphs retain three DIRECT OBSERVED edges. One produces short-RNA cleavage fragments; two degrade rRNA in separately sourced 70S preparations. Joint YbeY/RNase R is represented as a single conjunctive activity, not independently sufficient inputs. The graph endpoint is rRNA degradation, not destruction of ribosomal proteins. No physiological maturation site, residue chemistry, specific metal, protease substrate, in vivo flux or family-wide function is inferred. Quotations were checked against the retrieved full text and images were inspected; the kasugamycin quotation belongs to that precise comparison.

### Remaining family coverage

completeness: concern. Targets: PF02130.

Obtain the supplement for exact construct and assay parameters; assess purification controls and additional primary contexts before broadening the graph. Cellular heat-shock maturation, polysomes, subunit mixing, reciprocal complementation and homolog-specific metal/substrate studies remain incompletely covered. PMID:31777930 was inspected only as abstract/discussion context concerning S. meliloti substrate specificity and contamination risks; its experiments were not adopted.

## Findings

### additional-contexts: Resolve extended assay details and review additional YbeY contexts

minor / open / confirmed; issue key: pf02130-causal-context-coverage.

Retrieve the 2013 extended methods to verify tags, construct sequence and exact Figure 3 reaction conditions, then separately assess cellular maturation, polysomes and homolog-specific studies. Preserve the distinction between purified biochemical effects, cellular outcomes and inferred catalytic steps; test any cross-family transfer against direct member evidence.

## Recommended Actions And Acceptance Checks

### extend-contexts

Retrieve the 2013 extended methods to verify tags, construct sequence and exact Figure 3 reaction conditions, then separately assess cellular maturation, polysomes and homolog-specific studies. Preserve the distinction between purified biochemical effects, cellular outcomes and inferred catalytic steps; test any cross-family transfer against direct member evidence.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC3570609/; Results and Experimental Procedures; Figures 1 and 3 captions and images visually inspected | supports | Figure 1C shows purified YbeY cleavage of a labeled 30-nt ssRNA. Figure 3B/C show rRNA-band loss from delta-ybeY-derived and kasugamycin-derived 70S under joint YbeY/RNase R treatment, not either enzyme alone. Resistant 30S, wild-type 70S and mutant-YbeY controls constrain the interpretation. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0A898/entry/pfam/PF02130/; Accession and domain locations; paired UniProt identity facts | supports | The paper's historical P77385 identifier is now demerged. E. coli context resolves it to P0A898 (b0659/JW0656; sequence version 1; 155 residues; PF02130 at 21-144), not the identical-sequence Shigella successor P0A899. Exact purified tag, construct sequence and expression host remain unverified because the extended methods were not retrieved. Reference mapping does not imply an isolated-domain experiment. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf02130 | data/families/PF02130.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- Figures 1 and 3 were visually inspected. Supplement retrieval returned HTML and Europe PMC reported the manuscript outside its open-access subset; extended methods were not read. No raw gel quantification, replication, model reanalysis or full review of the 2020 S. meliloti assays was performed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T055552Z-pf02130-ybey-causal-graphs
title: PF02130 YbeY RNA-cleavage and conjunctive ribosome-assay review
started_at: '2026-10-11T05:55:42Z'
finished_at: '2026-10-11T05:55:52Z'
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
summary: Three direct observed edges retain model-RNA cleavage and rRNA degradation
  by joint YbeY plus RNase R in two distinct defective-70S preparations, without inventing
  ordered catalytic microsteps.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF02130.yaml
    sha256: b259eb858ca49fd3cdc786d7cf4c1eee496f02cd26a849d8e04c14a5bff036fb
    role: context
  - path: data/families/PF02130.yaml
    sha256: 5191ac527f226c32c9601380860525b03059a2a1778ba26c17e1f9357372f0e5
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
  - path: evidence/PF02130/jacob-2013-ybey.txt
    role: context
    sha256: fe3cf50767a65d379fa67d38befd7752f53dde5d6df5016710d148412719735e
  - path: evidence/PF02130/P0A898-identity.txt
    role: context
    sha256: f4fbda590fc64aa60eeff6f6e95cd8bcaf3f47a34b42cc66835a20bbcdd13bff
targets:
- target_id: PF02130
  path: data/families/PF02130.yaml
  label: PF02130
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF02130.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 8d7a31325fe09a0727db959c415e6d445e2b8bdb55aa50014cadf9966ca48ad3
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: Former UPF0054 selected for primary E. coli biochemistry and to separate
    it from DUF6647 structural analogies.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF02130
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Obtain the supplement for exact construct and assay parameters; assess
      purification controls and additional primary contexts before broadening the
      graph. Cellular heat-shock maturation, polysomes, subunit mixing, reciprocal
      complementation and homolog-specific metal/substrate studies remain incompletely
      covered. PMID:31777930 was inspected only as abstract/discussion context concerning
      S. meliloti substrate specificity and contamination risks; its experiments were
      not adopted.
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
  - PF02130
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3570609/
  locator: Results and Experimental Procedures; Figures 1 and 3 captions and images
    visually inspected
  accessed_at: '2026-10-11T05:55:52Z'
  support: supports
  snapshot_sha256: fe3cf50767a65d379fa67d38befd7752f53dde5d6df5016710d148412719735e
  summary: Figure 1C shows purified YbeY cleavage of a labeled 30-nt ssRNA. Figure
    3B/C show rRNA-band loss from delta-ybeY-derived and kasugamycin-derived 70S under
    joint YbeY/RNase R treatment, not either enzyme alone. Resistant 30S, wild-type
    70S and mutant-YbeY controls constrain the interpretation.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0A898/entry/pfam/PF02130/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T05:55:52Z'
  support: supports
  snapshot_sha256: f4fbda590fc64aa60eeff6f6e95cd8bcaf3f47a34b42cc66835a20bbcdd13bff
  summary: The paper's historical P77385 identifier is now demerged. E. coli context
    resolves it to P0A898 (b0659/JW0656; sequence version 1; 155 residues; PF02130
    at 21-144), not the identical-sequence Shigella successor P0A899. Exact purified
    tag, construct sequence and expression host remain unverified because the extended
    methods were not retrieved. Reference mapping does not imply an isolated-domain
    experiment.
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T05:55:52Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf02130
  kind: record_content
  reference: data/families/PF02130.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T05:55:52Z'
  support: context_only
  snapshot_sha256: 5191ac527f226c32c9601380860525b03059a2a1778ba26c17e1f9357372f0e5
  quote: "id: Pfam:PF02130\npfam_id: PF02130\nname: Endoribonuclease YbeY\nshort_name:\
    \ YbeY\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\ncuration_status:\
    \ IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF02130\n\
    counters:\n  proteins: 20178\n  matches: 20283\n  proteomes: 19123\n  taxa: 29306\n\
    \  structures: 5\n  alphafold_models: 13642\n  domain_architectures: 53\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002036\ndescription: YbeY is a single strand-specific\
    \ metallo-endoribonuclease involved in late-stage 70S ribosome\n  quality control\
    \ and in maturation of the 3' terminus of the 16S rRNA. It acts together with\
    \ the RNase\n  R to eliminate defective 70S ribosomes, but not properly maturated\
    \ 70S ribosomes or individual subunits,\n  by a process mediated specifically\
    \ by the 30S ribosomal subunit. It is involved in the processing of\n  16S, 23S\
    \ and 5S rRNAs, with a particularly strong effect on maturation at both the 5'-and\
    \ 3'-ends of\n  16S rRNA as well as maturation of the 5'-end of 23S and 5S rRNAs\
    \ [[cite:PUB00064743],[cite:PUB00064742],[cite:PUB00096939]].\n  The crystal structure\
    \ of the protein from Aquifex aeolicus showed an overall fold consisting of one\n\
    \  central alpha-helix surrounded by a four-stranded beta-sheet and four other\
    \ alpha-helices [[cite:PUB00027806]].\ncuration_history: history/records/PF02130\n\
    discussions:\n- discussion_id: ybey-assay-details-and-context-coverage\n  prompt:\
    \ Obtain the 2013 extended methods and review additional YbeY contexts before\
    \ extending the synthetic-RNA\n    and joint-enzyme graphs.\n  kind: CURATION_TODO\n\
    \  status: OPEN\n  rationale: Main-text assays support scoped effects, but exact\
    \ construct and incubation details remain\n    incomplete. Cellular maturation,\
    \ polysomes, substrate selection and homolog-specific metal dependence\n    are\
    \ separate causal questions.\n  evidence:\n  - reference: PMID:23273979\n    supports:\
    \ PARTIAL\n    evidence_source: full_text\n    explanation: Figures 1 and 3 were\
    \ visually inspected. Supplement retrieval returned HTML or a non-open-access-subset\n\
    \      error, so missing extended methods are not assumed.\n  - reference: PMID:31777930\n\
    \    supports: PARTIAL\n    evidence_source: abstract_and_discussion\n    explanation:\
    \ The S. meliloti study highlights condition and RNase-contamination concerns\
    \ in disputed\n      double-stranded-RNA activity. Its assays and member identity\
    \ were not independently curated in this\n      session.\n  posed_by: Codex\n\
    \  posed_date: '2026-10-11'\n  notes: Retain historical P77385 demerger context.\
    \ No exact metal identity, residue chemistry, physiological\n    16S cleavage\
    \ site, protease function or cross-species transfer is inferred solely from the\
    \ family\n    label or a structural analogy.\ncausal_graphs:\n- graph_id: ecoli-ybey-synthetic-ssrna\n\
    \  title: Purified E. coli YbeY cleaves a synthetic single-stranded RNA\n  scope:\
    \ Purified E. coli YbeY acting on a 30-nt synthetic RNA containing 18 nt of the\
    \ mature 16S 3' end\n    and 12 nt of precursor trailer; not intact pre-16S maturation\
    \ or isolated-domain catalysis.\n  context: Figure 1C uses 5 uM YbeY and 5 uM\
    \ 5'-32P-labeled RNA, with buffer control and 30, 90 and 120\n    second samples.\
    \ Main methods specify 20 uL and 50 mM HEPES pH 7.5. The text describes efficient\
    \ cleavage\n    at 37 C; exact extended assay and construct details remain unverified\
    \ because the supplement was inaccessible.\n  family_mapping: The paper's E. coli\
    \ YbeY identifier P77385 has demerged into P0A898 (E. coli K12) and\n    P0A899\
    \ (Shigella flexneri). The E. coli reference is P0A898, b0659/JW0656, sequence\
    \ version 1, 155\n    residues, PF02130 at 21-144. The purified protein's exact\
    \ tag and expression construct are not established\n    by the inspected main\
    \ text.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:83333\n  limitations:\
    \ The observed endpoint is cleavage of a short model RNA. It does not establish\
    \ physiological\n    cleavage specificity, turnover kinetics, a direct 16S maturation\
    \ site, protein-substrate proteolysis\n    or family-wide activity. Duplex resistance\
    \ is condition-specific. Mutant activity loss is supportive\n    but does not\
    \ exclude folding or preparation effects; no residue-level chemical step is claimed.\n\
    \  nodes:\n  - node_id: purified-ybey\n    label: Purified E. coli YbeY in the\
    \ synthetic-RNA assay\n    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:P0A898\n\
    \  - node_id: short-rna-fragments\n    label: Cleavage fragments of the labeled\
    \ 30-nt single-stranded RNA\n    node_type: STATE\n  edges:\n  - edge_id: ybey-produces-rna-fragments\n\
    \    subject: purified-ybey\n    predicate: produces\n    object: short-rna-fragments\n\
    \    mechanism: The purified YbeY preparation cleaves the single-stranded model\
    \ RNA, yielding shorter labeled\n      products on a denaturing gel relative to\
    \ buffer control.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:23273979\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC3570609/\n      snippet: YbeY cleaved\
    \ the 30 nt ssRNA substrate\n      explanation: Results, main assay methods and\
    \ visually inspected Figure 1C support the direct cleavage\n        endpoint.\
    \ Figure 1D retains a duplex negative condition; uninspected supplemental methods\
    \ are\n        not silently supplied.\n      cache_path: evidence/PF02130/jacob-2013-ybey.txt\n\
    \      cache_sha256: fe3cf50767a65d379fa67d38befd7752f53dde5d6df5016710d148412719735e\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0A898/entry/pfam/PF02130/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0A898/entry/pfam/PF02130/\n\
    \      snippet: 'entry accession: PF02130'\n      explanation: Reference-protein\
    \ family mapping after resolving the old accession by organism; not\n        independent\
    \ biochemical evidence or proof of an isolated-domain construct.\n      cache_path:\
    \ evidence/PF02130/P0A898-identity.txt\n      cache_sha256: f4fbda590fc64aa60eeff6f6e95cd8bcaf3f47a34b42cc66835a20bbcdd13bff\n\
    - graph_id: ecoli-ybey-rnaser-defective-70s\n  title: Joint YbeY and RNase R treatment\
    \ degrades rRNA in defective 70S preparations\n  scope: In vitro treatment of\
    \ separate 70S preparations from E. coli MC4100 delta-ybeY and kasugamycin-treated\n\
    \    MC4100; the two substrate contexts are distinct comparisons within Figure\
    \ 3, not independent replications.\n  context: Isolated 70S at 5.5 uM with YbeY\
    \ and commercial RNase R at 5 uM each; the kasugamycin culture\n    condition\
    \ is 200 ug/mL. Main reaction methods specify 20 uL and 50 mM HEPES pH 7.5. rRNA\
    \ is extracted\n    after treatment and resolved by Synergel/agarose electrophoresis.\
    \ Exact Figure 3 incubation time,\n    temperature and additional buffer components\
    \ require the unavailable extended methods.\n  family_mapping: E. coli YbeY maps\
    \ from historical P77385 to UniProtKB:P0A898, b0659/JW0656, reference\n    sequence\
    \ version 1, PF02130 at 21-144 of 155 residues. The graph concerns the intact-protein\
    \ preparation\n    in conjunction with RNase R, not a sufficient isolated PF02130\
    \ domain.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:83333\n  limitations:\
    \ Neither enzyme alone nor H114A/H124A YbeY plus RNase R gives the adopted rRNA-band-loss\n\
    \    endpoint. Matched wild-type 70S and 30S controls resist treatment. Ordered\
    \ initiation and exonucleolytic\n    microsteps remain proposed, and gel band\
    \ loss does not demonstrate degradation of ribosomal proteins.\n    Purification\
    \ tag and full construct details remain unresolved; in vivo quality-control flux\
    \ and polysome\n    endpoints are not adopted here.\n  nodes:\n  - node_id: joint-ybey-rnaser\n\
    \    label: Joint purified YbeY and RNase R treatment\n    node_type: ACTIVITY\n\
    \    grounding:\n    - UniProtKB:P0A898\n  - node_id: deletion-70s-rrna\n    label:\
    \ rRNA in 70S preparations from MC4100 delta-ybeY\n    node_type: STATE\n  - node_id:\
    \ kasugamycin-70s-rrna\n    label: rRNA in 70S preparations from kasugamycin-treated\
    \ MC4100\n    node_type: STATE\n  edges:\n  - edge_id: joint-enzymes-degrade-deletion-70s-rrna\n\
    \    subject: joint-ybey-rnaser\n    predicate: degrades\n    object: deletion-70s-rrna\n\
    \    mechanism: Addition of both enzymes to the deletion-derived 70S preparation\
    \ causes loss of the extracted\n      rRNA bands; the matched single-enzyme and\
    \ mutant-YbeY controls do not.\n    directness: DIRECT\n    support: OBSERVED\n\
    \    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference: PMID:23273979\n\
    \      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3570609/\n      snippet:\
    \ the rRNA in these 70S ribosomes was completely degraded\n      explanation:\
    \ This quotation concerns the delta-ybeY-derived 70S experiment. Figure 3B was\
    \ visually\n        inspected with its 30S and enzyme controls; the cause is conjunctive\
    \ treatment, not two independently\n        sufficient enzyme arrows.\n      cache_path:\
    \ evidence/PF02130/jacob-2013-ybey.txt\n      cache_sha256: fe3cf50767a65d379fa67d38befd7752f53dde5d6df5016710d148412719735e\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0A898/entry/pfam/PF02130/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0A898/entry/pfam/PF02130/\n\
    \      snippet: 'entry accession: PF02130'\n      explanation: YbeY component\
    \ identity and family interval only; the commercial partner is not assigned\n\
    \        an unverified accession.\n      cache_path: evidence/PF02130/P0A898-identity.txt\n\
    \      cache_sha256: f4fbda590fc64aa60eeff6f6e95cd8bcaf3f47a34b42cc66835a20bbcdd13bff\n\
    \  - edge_id: joint-enzymes-degrade-kasugamycin-70s-rrna\n    subject: joint-ybey-rnaser\n\
    \    predicate: degrades\n    object: kasugamycin-70s-rrna\n    mechanism: In\
    \ the separately prepared kasugamycin-treated-cell substrate, joint enzyme addition\
    \ causes\n      rRNA-band loss while either enzyme alone and mutant-YbeY plus\
    \ RNase R do not.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:23273979\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC3570609/\n      snippet: kasugamycin-treated\
    \ cells was completely degraded\n      explanation: Figure 3C and its adjacent\
    \ results paragraph separately support degradation of rRNA\n        from kasugamycin-derived\
    \ 70S by the joint treatment. The quotation fragment belongs to that specific\n\
    \        substrate context; its full endpoint and controls are retained in the\
    \ cache's assay notes.\n      cache_path: evidence/PF02130/jacob-2013-ybey.txt\n\
    \      cache_sha256: fe3cf50767a65d379fa67d38befd7752f53dde5d6df5016710d148412719735e\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0A898/entry/pfam/PF02130/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P0A898/entry/pfam/PF02130/\n\
    \      snippet: 'entry accession: PF02130'\n      explanation: Resolves the E.\
    \ coli YbeY component and PF02130 interval only, not the treatment outcome.\n\
    \      cache_path: evidence/PF02130/P0A898-identity.txt\n      cache_sha256: f4fbda590fc64aa60eeff6f6e95cd8bcaf3f47a34b42cc66835a20bbcdd13bff\n\
    curation_events:\n- timestamp: '2026-10-11T05:52:06Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Curate YbeY model-RNA and joint-enzyme\
    \ rRNA degradation graphs\n  history_record: history/records/PF02130/2026-10-11T055206Z-codex-8f4345.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: The paper's historical P77385 identifier is now demerged. E. coli context
    resolves it to P0A898 (b0659/JW0656; sequence version 1; 155 residues; PF02130
    at 21-144), not the identical-sequence Shigella successor P0A899. Exact purified
    tag, construct sequence and expression host remain unverified because the extended
    methods were not retrieved. Reference mapping does not imply an isolated-domain
    experiment.
  target_ids:
  - PF02130
  evidence_ids:
  - identity
  - primary
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Two MECHANISTIC graphs retain three DIRECT OBSERVED edges. One produces
    short-RNA cleavage fragments; two degrade rRNA in separately sourced 70S preparations.
    Joint YbeY/RNase R is represented as a single conjunctive activity, not independently
    sufficient inputs. The graph endpoint is rRNA degradation, not destruction of
    ribosomal proteins. No physiological maturation site, residue chemistry, specific
    metal, protease substrate, in vivo flux or family-wide function is inferred. Quotations
    were checked against the retrieved full text and images were inspected; the kasugamycin
    quotation belongs to that precise comparison.
  target_ids:
  - PF02130
  evidence_ids:
  - primary
  - native
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Obtain the supplement for exact construct and assay parameters; assess
    purification controls and additional primary contexts before broadening the graph.
    Cellular heat-shock maturation, polysomes, subunit mixing, reciprocal complementation
    and homolog-specific metal/substrate studies remain incompletely covered. PMID:31777930
    was inspected only as abstract/discussion context concerning S. meliloti substrate
    specificity and contamination risks; its experiments were not adopted.
  target_ids:
  - PF02130
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf02130-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve extended assay details and review additional YbeY contexts
  description: Retrieve the 2013 extended methods to verify tags, construct sequence
    and exact Figure 3 reaction conditions, then separately assess cellular maturation,
    polysomes and homolog-specific studies. Preserve the distinction between purified
    biochemical effects, cellular outcomes and inferred catalytic steps; test any
    cross-family transfer against direct member evidence.
  target_ids:
  - PF02130
  field_paths:
  - causal_graphs
  - discussions
  evidence_ids:
  - primary
  - identity
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF02130.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Retrieve the 2013 extended methods to verify tags, construct sequence
    and exact Figure 3 reaction conditions, then separately assess cellular maturation,
    polysomes and homolog-specific studies. Preserve the distinction between purified
    biochemical effects, cellular outcomes and inferred catalytic steps; test any
    cross-family transfer against direct member evidence.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF02130
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- Figures 1 and 3 were visually inspected. Supplement retrieval returned HTML and
  Europe PMC reported the manuscript outside its open-access subset; extended methods
  were not read. No raw gel quantification, replication, model reanalysis or full
  review of the 2020 S. meliloti assays was performed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
