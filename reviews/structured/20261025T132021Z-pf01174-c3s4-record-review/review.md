# PF01174 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review

- Review: 20261025T132021Z-pf01174-c3s4-record-review
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-25T13:20:20Z
- Finished UTC: 2026-10-25T13:20:21Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Five MECHANISTIC graphs retain five DIRECT OBSERVED biochemical effects for partner-dependent glutaminase readout, joint PLP production, a ribulose/ammonium context and two separate acivicin readouts. Exact reference mapping, untagged versus tagged preparations, primary-source discrepancies and strain boundaries remain explicit. Partial scientific self-review; IN_PROGRESS. Cycle 3 Stage 3 (PR #357) grounded node add-yaad-to-yaae-glutamine in pdxt-untagged-partner-dependent-glutaminase to Bacillus subtilis 168 YaaD/PdxS and YaaE/PdxT (UniProtKB:P37527 and UniProtKB:P37528). Stage 4 frozen-inventory audit also identified an open grounding finding (pf01174-pdxst-partner-and-acivicin-nodes-missing-grounding) across four graphs (pdxst-glutamine-dependent-plp-product node joint-pdxst-glutamine-carbohydrate-reaction, pdxt-ribulose-ammonium-dependent-synthase-readout node add-yaae-ribulose-ammonium, pdxt-acivicin-glutaminase-inhibition nodes acivicin-pretreat-glutaminase-mixture and acivicin-assay-glutaminase-readout, and pdxst-acivicin-plp-signal-inhibition nodes acivicin-pretreat-plp-mixture and residual-glutamine-plp-signal) where partner YaaD (UniProtKB:P37527) or joint [UniProtKB:P37527, UniProtKB:P37528] grounding is omitted, preserved for Stage 5 grouped remediation.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01174 SNO, the next accession-ordered SEEDED family after SBDS_N, using Raschle 2005 main/supplement experiments and the earlier Belitsky 2004 study to check strain and preparation boundaries.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0e26e9cdab5214d838db4f53ddefbf83772241fb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01174 | data/families/PF01174.yaml | generated | PF01174 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01174 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01174.

P37528/PDXT_BACSU, 196 aa and sequence version 1, matches InterPro exactly with PF01174 at 6-188. The study specifies strain-168 genomic cloning, construct sequencing and N-terminal sequencing. Primer ends match the reference, and the C79 peptide maps to residues 74-87 inside the family interval. Untagged biochemical preparations are distinct from C-terminal His6 pull-out protein. The earlier SMY constructs are not assumed identical to strain 168.

### Directed effects and limits

graph: supported. Targets: PF01174.

Inputs retain both proteins and substrates where required; the product graph does not attribute PLP synthesis to PdxT alone. APAD and A414 are named as coupled/product-associated readouts, with orthogonal product identification separately retained. The external-ammonium effect is bounded to ribulose 5-phosphate because ribose works without YaaE. Acivicin effects are measured independently, not joined transitively or transferred to cellular efficacy. C79 labeling and physical association are supporting context, not a fully observed atomic cycle.

### Remaining family coverage

completeness: concern. Targets: PF01174.

Glutamine concentration differs between kinetic captions and Methods/Results, inhibition rate units differ between captions and text, and acivicin dose/mass descriptions also conflict. Raw spectra, exact adduct chemistry, full clones, reporter interference controls and quantitative uncertainties need further assessment. SMY identity and its pBB1181 penultimate-residue discrepancy remain unresolved. Other microbial, plant and fungal members, later structures and intermediates remain outside this partial review.

### Causal-graph taxon and protein-node grounding consistency

representation: concern. Targets: PF01174.

In curation/families/PF01174.yaml, four causal graphs omit verified Bacillus subtilis 168 (NCBITaxon:224308) YaaD/PdxS (UniProtKB:P37527) and/or YaaE/PdxT (UniProtKB:P37528) protein grounding that is explicitly established in their family_mapping and in sibling graph pdxt-untagged-partner-dependent-glutaminase (which grounds add-yaad-to-yaae-glutamine to [UniProtKB:P37527, UniProtKB:P37528]): (1) in pdxst-glutamine-dependent-plp-product (lines 47-79), node joint-pdxst-glutamine-carbohydrate-reaction ('Joint YaaD, YaaE, glutamine, ribose 5-phosphate and DHAP reaction', lines 56-60) grounds only to [UniProtKB:P37528] and omits partner YaaD (UniProtKB:P37527); (2) in pdxt-ribulose-ammonium-dependent-synthase-readout (lines 80-112), node add-yaae-ribulose-ammonium ('Add YaaE to YaaD with ribulose 5-phosphate and ammonium', lines 89-93) grounds only to [UniProtKB:P37528] and omits partner YaaD (UniProtKB:P37527); (3) in pdxt-acivicin-glutaminase-inhibition (lines 113-145), node acivicin-pretreat-glutaminase-mixture ('Increase 5-mM acivicin pretreatment time relative to zero-time control', lines 122-124) omits grounding: [UniProtKB:P37527, UniProtKB:P37528] and node acivicin-assay-glutaminase-readout ('Residual coupled glutaminase readout of YaaD/YaaE', lines 125-129) grounds only to [UniProtKB:P37528] and omits partner YaaD (UniProtKB:P37527); and (4) in pdxst-acivicin-plp-signal-inhibition (lines 146-176), node acivicin-pretreat-plp-mixture ('Expose the YaaD/YaaE synthesis mixture to increasing acivicin', lines 155-157) omits grounding: [UniProtKB:P37527, UniProtKB:P37528] and node residual-glutamine-plp-signal ('Residual glutamine-dependent 414-nm PLP signal', lines 158-160) grounds only to [UniProtKB:P37528] and omits partner YaaD (UniProtKB:P37527).

## Findings

### additional-contexts: Reconcile PdxT quantitative discrepancies and extend exact-member coverage

minor / open / confirmed; issue key: pf01174-causal-context-coverage.

Inspect raw kinetic/MS data and original clones to resolve concentration, time-unit and adduct discrepancies before adding quantitative or atomic claims. Evaluate reporter controls and later intermediate/structural studies. Resolve the SMY genotype/reference boundary and curate its phenotype separately; keep alternative nitrogen/substrate conditions and other organisms distinct. Save an evidence-backed successor review for extensions.

### pdxst-partner-and-acivicin-nodes-missing-grounding: Add partner YaaD (UniProtKB:P37527) and joint [UniProtKB:P37527, UniProtKB:P37528] grounding to six YaaD/YaaE PLP synthase and acivicin assay nodes in PF01174

minor / open / confirmed; issue key: pf01174-pdxst-partner-and-acivicin-nodes-missing-grounding.

In curation/families/PF01174.yaml, four causal graphs omit verified Bacillus subtilis 168 (NCBITaxon:224308) YaaD/PdxS (UniProtKB:P37527) and/or YaaE/PdxT (UniProtKB:P37528) protein grounding that is explicitly established in their family_mapping and in sibling graph pdxt-untagged-partner-dependent-glutaminase (which grounds add-yaad-to-yaae-glutamine to [UniProtKB:P37527, UniProtKB:P37528]): (1) in pdxst-glutamine-dependent-plp-product (lines 47-79), node joint-pdxst-glutamine-carbohydrate-reaction ('Joint YaaD, YaaE, glutamine, ribose 5-phosphate and DHAP reaction', lines 56-60) grounds only to [UniProtKB:P37528] and omits partner YaaD (UniProtKB:P37527); (2) in pdxt-ribulose-ammonium-dependent-synthase-readout (lines 80-112), node add-yaae-ribulose-ammonium ('Add YaaE to YaaD with ribulose 5-phosphate and ammonium', lines 89-93) grounds only to [UniProtKB:P37528] and omits partner YaaD (UniProtKB:P37527); (3) in pdxt-acivicin-glutaminase-inhibition (lines 113-145), node acivicin-pretreat-glutaminase-mixture ('Increase 5-mM acivicin pretreatment time relative to zero-time control', lines 122-124) omits grounding: [UniProtKB:P37527, UniProtKB:P37528] and node acivicin-assay-glutaminase-readout ('Residual coupled glutaminase readout of YaaD/YaaE', lines 125-129) grounds only to [UniProtKB:P37528] and omits partner YaaD (UniProtKB:P37527); and (4) in pdxst-acivicin-plp-signal-inhibition (lines 146-176), node acivicin-pretreat-plp-mixture ('Expose the YaaD/YaaE synthesis mixture to increasing acivicin', lines 155-157) omits grounding: [UniProtKB:P37527, UniProtKB:P37528] and node residual-glutamine-plp-signal ('Residual glutamine-dependent 414-nm PLP signal', lines 158-160) grounds only to [UniProtKB:P37528] and omits partner YaaD (UniProtKB:P37527).

## Recommended Actions And Acceptance Checks

### extend-contexts

Inspect raw kinetic/MS data and original clones to resolve concentration, time-unit and adduct discrepancies before adding quantitative or atomic claims. Evaluate reporter controls and later intermediate/structural studies. Resolve the SMY genotype/reference boundary and curate its phenotype separately; keep alternative nitrogen/substrate conditions and other organisms distinct. Save an evidence-backed successor review for extensions.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://archive-ouverte.unige.ch/unige:89531; Published article pages 32291-32300 and appended supplemental S1-S3; visually inspected Figures 1-4, 6/7 and S2/S3 | supports | Untagged strain-168 YaaE/PdxT has partner-dependent glutamine turnover and contributes jointly with YaaD and carbohydrate substrates to PLP formation supported by HPLC, MS and NMR. YaaE additionally enhances the ribulose-phosphate/ammonium product readout in a distinct assay. Acivicin pretreatment reduces separate glutaminase and synthesis signals. No native cellular drug effect or directly observed ammonia-channel trajectory follows from these data. |
| identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/P37528/entry/pfam/PF01174/; Accession and domain locations; paired UniProt identity facts | supports | P37528/PDXT_BACSU, 196 aa and sequence version 1, matches InterPro exactly with PF01174 at 6-188. The study specifies strain-168 genomic cloning, construct sequencing and N-terminal sequencing. Primer ends match the reference, and the C79 peptide maps to residues 74-87 inside the family interval. Untagged biochemical preparations are distinct from C-terminal His6 pull-out protein. The earlier SMY constructs are not assumed identical to strain 168. |
| deposited-fulltext-and-supplement | https://access.archive-ouverte.unige.ch/access/metadata/c66582c3-73ec-4477-9a53-cfbe4f2f0f2c/download; PDF pages 3-12 are main article; pages 13-16 are appended supplemental figures and captions | supports | Supplies product NMR and coupled glutaminase controls in the same author-deposited published document. The 3.75-ppm NMR contaminant and caption/text discrepancies remain explicit. |
| earlier-smy-preparation-boundary | https://pmc.ncbi.nlm.nih.gov/articles/PMC344226/; Main text, Figure 1 construct caption, visually inspected Figures 2 and 4 | supports | Earlier SMY growth and His6-protein results use different strains, buffers and temperatures. The pBB1181 penultimate Gly-to-Ser description is not reconciled with the strain-168 terminus and is not assigned to independently amplified expression constructs. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| stage4-prior-review | reviews/structured/20261011T100219Z-pf01174-pdxt-partner-and-substrate-contexts/review.yaml; Predecessor structured review 20261011T100219Z-pf01174-pdxt-partner-and-substrate-contexts | supports | Predecessor review 20261011T100219Z-pf01174-pdxt-partner-and-substrate-contexts verified and linked for finding continuity and semantic-digest progression on PF01174. |
| duf-projection-pf01174 | data/families/PF01174.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- All main text and supplemental captions of the 16-page author-archived PDF were read; Figures 1-4, 6/7, S2/S3 and cloning Methods were visually checked. Raw spectra were not reprocessed, and no full independent chemical reassignment is claimed. Belitsky 2004 main text/captions and Figures 2/4 were inspected for context, not adopted as strain-168 edges.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T132021Z-pf01174-c3s4-record-review
title: PF01174 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review
started_at: '2026-10-25T13:20:20Z'
finished_at: '2026-10-25T13:20:21Z'
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
summary: 'Five MECHANISTIC graphs retain five DIRECT OBSERVED biochemical effects
  for partner-dependent glutaminase readout, joint PLP production, a ribulose/ammonium
  context and two separate acivicin readouts. Exact reference mapping, untagged versus
  tagged preparations, primary-source discrepancies and strain boundaries remain explicit.
  Partial scientific self-review; IN_PROGRESS. Cycle 3 Stage 3 (PR #357) grounded
  node add-yaad-to-yaae-glutamine in pdxt-untagged-partner-dependent-glutaminase to
  Bacillus subtilis 168 YaaD/PdxS and YaaE/PdxT (UniProtKB:P37527 and UniProtKB:P37528).
  Stage 4 frozen-inventory audit also identified an open grounding finding (pf01174-pdxst-partner-and-acivicin-nodes-missing-grounding)
  across four graphs (pdxst-glutamine-dependent-plp-product node joint-pdxst-glutamine-carbohydrate-reaction,
  pdxt-ribulose-ammonium-dependent-synthase-readout node add-yaae-ribulose-ammonium,
  pdxt-acivicin-glutaminase-inhibition nodes acivicin-pretreat-glutaminase-mixture
  and acivicin-assay-glutaminase-readout, and pdxst-acivicin-plp-signal-inhibition
  nodes acivicin-pretreat-plp-mixture and residual-glutamine-plp-signal) where partner
  YaaD (UniProtKB:P37527) or joint [UniProtKB:P37527, UniProtKB:P37528] grounding
  is omitted, preserved for Stage 5 grouped remediation.'
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 0e26e9cdab5214d838db4f53ddefbf83772241fb
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01174.yaml
    sha256: 1358a063812a30acd4ce56495937ee4420eb5eab29c6be92702a361a7900f35d
    role: context
  - path: data/families/PF01174.yaml
    sha256: 67f79bb709893b108d365404939b91aeb6a35877872aa127b19661d08a57adb7
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
  - path: evidence/PF01174/PdxT-identity.txt
    sha256: 18dba408806b8fe2efcb37eeb790aca7be688125551a2db10ec004b875a94389
    role: context
  - path: evidence/PF01174/belitsky-2004-context-boundary.txt
    sha256: 73ece6efb723d59c1a687a5c60e2216edd3598ab511c1e298428464501e9a544
    role: context
  - path: evidence/PF01174/raschle-2005-pdxt.txt
    sha256: d7f446303a58a75715c784a08baf140e0e1544ad165f1c4f7fd2d27873c4b197
    role: context
  - path: reviews/structured/20261011T100219Z-pf01174-pdxt-partner-and-substrate-contexts/review.yaml
    sha256: 25b4e978d1b043cfbfb42e6d023a1d6b5ffe572154acd541c27ca54d7f0a88ba
    role: context
targets:
- target_id: PF01174
  path: data/families/PF01174.yaml
  label: PF01174
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01174.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: 5e78922ea16ee5d620c7f8dd1530e885e92e85e09dcbdbc9e3d688159d4b3d05
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01174 SNO, the next accession-ordered SEEDED family after SBDS_N, using
    Raschle 2005 main/supplement experiments and the earlier Belitsky 2004 study to
    check strain and preparation boundaries.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01174
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Glutamine concentration differs between kinetic captions and Methods/Results,
      inhibition rate units differ between captions and text, and acivicin dose/mass
      descriptions also conflict. Raw spectra, exact adduct chemistry, full clones,
      reporter interference controls and quantitative uncertainties need further assessment.
      SMY identity and its pBB1181 penultimate-residue discrepancy remain unresolved.
      Other microbial, plant and fungal members, later structures and intermediates
      remain outside this partial review.
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
  - PF01174
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://archive-ouverte.unige.ch/unige:89531
  locator: Published article pages 32291-32300 and appended supplemental S1-S3; visually
    inspected Figures 1-4, 6/7 and S2/S3
  accessed_at: '2026-10-11T10:02:19Z'
  support: supports
  snapshot_sha256: d7f446303a58a75715c784a08baf140e0e1544ad165f1c4f7fd2d27873c4b197
  summary: Untagged strain-168 YaaE/PdxT has partner-dependent glutamine turnover
    and contributes jointly with YaaD and carbohydrate substrates to PLP formation
    supported by HPLC, MS and NMR. YaaE additionally enhances the ribulose-phosphate/ammonium
    product readout in a distinct assay. Acivicin pretreatment reduces separate glutaminase
    and synthesis signals. No native cellular drug effect or directly observed ammonia-channel
    trajectory follows from these data.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P37528/entry/pfam/PF01174/
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T10:02:19Z'
  support: supports
  snapshot_sha256: 18dba408806b8fe2efcb37eeb790aca7be688125551a2db10ec004b875a94389
  summary: P37528/PDXT_BACSU, 196 aa and sequence version 1, matches InterPro exactly
    with PF01174 at 6-188. The study specifies strain-168 genomic cloning, construct
    sequencing and N-terminal sequencing. Primer ends match the reference, and the
    C79 peptide maps to residues 74-87 inside the family interval. Untagged biochemical
    preparations are distinct from C-terminal His6 pull-out protein. The earlier SMY
    constructs are not assumed identical to strain 168.
- evidence_id: deposited-fulltext-and-supplement
  kind: primary_source
  reference: https://access.archive-ouverte.unige.ch/access/metadata/c66582c3-73ec-4477-9a53-cfbe4f2f0f2c/download
  locator: PDF pages 3-12 are main article; pages 13-16 are appended supplemental
    figures and captions
  summary: Supplies product NMR and coupled glutaminase controls in the same author-deposited
    published document. The 3.75-ppm NMR contaminant and caption/text discrepancies
    remain explicit.
  accessed_at: '2026-10-11T10:02:19Z'
  support: supports
  snapshot_sha256: d7f446303a58a75715c784a08baf140e0e1544ad165f1c4f7fd2d27873c4b197
- evidence_id: earlier-smy-preparation-boundary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC344226/
  locator: Main text, Figure 1 construct caption, visually inspected Figures 2 and
    4
  summary: Earlier SMY growth and His6-protein results use different strains, buffers
    and temperatures. The pBB1181 penultimate Gly-to-Ser description is not reconciled
    with the strain-168 terminus and is not assigned to independently amplified expression
    constructs.
  accessed_at: '2026-10-11T10:02:19Z'
  support: supports
  snapshot_sha256: 73ece6efb723d59c1a687a5c60e2216edd3598ab511c1e298428464501e9a544
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T10:02:19Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: stage4-prior-review
  kind: prior_review
  reference: reviews/structured/20261011T100219Z-pf01174-pdxt-partner-and-substrate-contexts/review.yaml
  locator: Predecessor structured review 20261011T100219Z-pf01174-pdxt-partner-and-substrate-contexts
  accessed_at: '2026-10-25T13:20:21Z'
  support: supports
  snapshot_sha256: 25b4e978d1b043cfbfb42e6d023a1d6b5ffe572154acd541c27ca54d7f0a88ba
  summary: Predecessor review 20261011T100219Z-pf01174-pdxt-partner-and-substrate-contexts
    verified and linked for finding continuity and semantic-digest progression on
    PF01174.
- evidence_id: duf-projection-pf01174
  kind: record_content
  reference: data/families/PF01174.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-25T13:20:21Z'
  support: context_only
  snapshot_sha256: 67f79bb709893b108d365404939b91aeb6a35877872aa127b19661d08a57adb7
  quote: "id: Pfam:PF01174\npfam_id: PF01174\nname: SNO glutamine amidotransferase\
    \ family\nshort_name: SNO\nseed_status: EX_DUF\ncharacterization_status: UNSCORED\n\
    curation_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01174\n\
    counters:\n  proteins: 9115\n  matches: 9939\n  proteomes: 8607\n  taxa: 14067\n\
    \  structures: 12\n  alphafold_models: 6364\n  domain_architectures: 34\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002161\ndescription: This family and its amidotransferase\
    \ domain was first described in [[cite:PUB00020352]].\n  It is predicted that\
    \ members of this family are involved in the pyridoxine biosynthetic pathway,\
    \ based\n  on the proximity and co-regulation of the corresponding genes and physical\
    \ interaction between the members\n  of [pfam:PF01174] and [pfam:PF01680] [[cite:PUB00007176]].\n\
    curation_history: history/records/PF01174\ndiscussions:\n- discussion_id: pdxt-kinetic-discrepancies-and-other-contexts\n\
    \  prompt: Reconcile source discrepancies and extend PdxT mechanisms with exact\
    \ constructs and orthogonal\n    controls.\n  kind: CURATION_TODO\n  status: OPEN\n\
    \  rationale: Five direct biochemical effects cover partner-dependent hydrolysis,\
    \ PLP formation, a ribulose/ammonium\n    context and two inhibitor readouts.\
    \ They do not establish every atomic step, strain phenotype or family\n    member's\
    \ function.\n  evidence:\n  - reference: PMID:16030023\n    supports: PARTIAL\n\
    \    evidence_source: inspected_primary_full_text_and_supplement\n    explanation:\
    \ Main paper and appended supplement support the adopted reactions, while conflicting\
    \ concentrations,\n      rate units and mass descriptions constrain quantitative\
    \ interpretation.\n  - reference: PMID:14762015\n    supports: PARTIAL\n    evidence_source:\
    \ inspected_primary_full_text\n    explanation: Earlier SMY growth and His6 biochemical\
    \ experiments were inspected but are not transferred\n      to the strain-168\
    \ untagged preparations.\n  notes: Obtain full historical clones and raw inhibition/MS\
    \ data, reconcile 1/10-mM glutamine, minute/second\n    rate units, acivicin dose\
    \ lists and peptide/intact-adduct masses. Inspect reporter controls and later\n\
    \    structural/intermediate studies before adding an atomic channeling cycle.\
    \ Resolve SMY identity and\n    the pBB1181 penultimate-residue discrepancy before\
    \ adopting its separate genotype/growth context.\n    Review plant, fungal and\
    \ other microbial members independently. Partial scientific self-review; remain\n\
    \    IN_PROGRESS.\n  posed_by: Codex\n  posed_date: '2026-10-11'\ncausal_graphs:\n\
    - graph_id: pdxt-untagged-partner-dependent-glutaminase\n  title: PdxS increases\
    \ the glutaminase readout of untagged PdxT\n  scope: Purified untagged Bacillus\
    \ subtilis 168 YaaE/PdxT with YaaD/PdxS in Raschle 2005 supplement S2A\n    and\
    \ main Results. The bovine reporter enzyme is a separate component.\n  context:\
    \ 300 ul, 4 uM YaaE, 4 uM YaaD when present, 10 mM glutamine, 50 mM Tris-Cl pH\
    \ 8.0, 0.5 mM APAD\n    and 7 U bovine glutamate dehydrogenase; 37 C. Measure\
    \ the increase at 363 nm after glutamine addition.\n  family_mapping: P37528/PDXT_BACSU,\
    \ 196 aa, sequence version 1, matches InterPro exactly with PF01174\n    at 6-188.\
    \ The study cloned strain-168 genomic yaaE, verified constructs by sequencing\
    \ and purified\n    proteins by N-terminal sequencing. Primer ends match MLTIGVL\
    \ and EYKQKALV. Untagged activity preparations\n    differ from His6-YaaE used\
    \ for pull-out assays.\n  scope_status: MECHANISTIC\n  taxon: NCBITaxon:224308\n\
    \  limitations: APAD reduction is a coupled glutamate readout, not direct observation\
    \ of ammonia channeling.\n    Individual-protein controls remain near background;\
    \ this is an assay-specific bound, not universal\n    absence of intrinsic activity.\
    \ The 2004 SMY His6 preparations and their pH/temperature are not transferred.\n\
    \  nodes:\n  - node_id: add-yaad-to-yaae-glutamine\n    label: Add 4 uM YaaD to\
    \ untagged YaaE and glutamine\n    node_type: PERTURBATION\n    grounding:\n \
    \   - UniProtKB:P37527\n    - UniProtKB:P37528\n  - node_id: yaae-coupled-glutaminase-readout\n\
    \    label: Glutamate-dependent APAD reduction in the coupled YaaE assay\n   \
    \ node_type: ACTIVITY\n    grounding:\n    - UniProtKB:P37528\n  edges:\n  - edge_id:\
    \ partner-increases-yaae-glutaminase-readout\n    subject: add-yaad-to-yaae-glutamine\n\
    \    predicate: increases\n    object: yaae-coupled-glutaminase-readout\n    mechanism:\
    \ The joint YaaD/YaaE preparation shows greater glutamine-dependent reporter turnover\
    \ than\n      YaaE alone. The causal intervention is partner addition; atomic\
    \ allostery and ammonia transport\n      are not independently observed here.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:16030023\n      source_url: https://archive-ouverte.unige.ch/unige:89531\n\
    \      snippet: glutaminase activity\n      explanation: Supplement S2A/B, main\
    \ Results on page 32294 and coupled-assay Methods on page 32292,\n        with\
    \ untagged protein preparation controls.\n      cache_path: evidence/PF01174/raschle-2005-pdxt.txt\n\
    \      cache_sha256: d7f446303a58a75715c784a08baf140e0e1544ad165f1c4f7fd2d27873c4b197\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P37528/entry/pfam/PF01174/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/P37528/entry/pfam/PF01174/\n\
    \      snippet: 'P37528 Pfam:PF01174 interval: 6-188, inclusive.'\n      explanation:\
    \ Exact reference mapping and strain-168 cloning evidence, not proof of identical\
    \ SMY\n        or other-species preparations.\n      cache_path: evidence/PF01174/PdxT-identity.txt\n\
    \      cache_sha256: 18dba408806b8fe2efcb37eeb790aca7be688125551a2db10ec004b875a94389\n\
    - graph_id: pdxst-glutamine-dependent-plp-product\n  title: Joint PdxS and PdxT\
    \ reactions produce PLP\n  scope: Untagged strain-168 YaaD/YaaE with glutamine\
    \ and phosphorylated carbohydrate substrates. Product\n    identity is supported\
    \ by orthogonal analyses, not only the Tris-dependent absorbance signal.\n  context:\
    \ 40 uM each protein, 50 mM Tris-Cl pH 8.0, 37 C, 10 mM glutamine, 0.5 mM ribose\
    \ 5-phosphate\n    and 0.5 mM dihydroxyacetone phosphate. A414 monitors the product-associated\
    \ Tris Schiff base; deproteinized\n    product is additionally examined by HPLC,\
    \ MS, chemical spectral shifts and supplemental 600-MHz NMR.\n  family_mapping:\
    \ YaaE/PdxT is P37528-associated strain-168 protein, PF01174 6-188; YaaD is the\
    \ separate\n    synthase. Both whole proteins and all listed substrates form a\
    \ joint input, not a claim that PdxT\n    alone synthesizes PLP.\n  scope_status:\
    \ MECHANISTIC\n  taxon: NCBITaxon:224308\n  limitations: No directly tracked ammonia\
    \ channel or atomic catalytic sequence is inferred. Figure 1A/B\n    captions\
    \ say 1 mM glutamine whereas Methods/Results say 10 mM; exact fitted kinetics\
    \ are not assigned\n    to this graph. Supplemental NMR identifies an unknown\
    \ 3.75-ppm contaminant. Raw spectra and historical\n    clones were not independently\
    \ reanalyzed.\n  nodes:\n  - node_id: joint-pdxst-glutamine-carbohydrate-reaction\n\
    \    label: Joint YaaD, YaaE, glutamine, ribose 5-phosphate and DHAP reaction\n\
    \    node_type: ACTIVITY\n    grounding:\n    - UniProtKB:P37528\n  - node_id:\
    \ identified-plp-product\n    label: Reaction product identified as pyridoxal\
    \ 5-phosphate\n    node_type: STATE\n  edges:\n  - edge_id: pdxst-joint-reaction-produces-plp\n\
    \    subject: joint-pdxst-glutamine-carbohydrate-reaction\n    predicate: produces\n\
    \    object: identified-plp-product\n    mechanism: The reconstituted reaction\
    \ produces material matching authentic PLP by chromatography,\n      spectral\
    \ behavior, mass and NMR. This establishes net product formation under joint-input\
    \ conditions\n      without treating each biochemical intermediate as observed.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:16030023\n      source_url: https://archive-ouverte.unige.ch/unige:89531\n\
    \      snippet: pyridoxal\n      explanation: Product Methods and Results on pages\
    \ 32293-32296, Figure 2 and visually inspected supplemental\n        S3 distinguish\
    \ PLP from pyridoxine/pyridoxal standards.\n      cache_path: evidence/PF01174/raschle-2005-pdxt.txt\n\
    \      cache_sha256: d7f446303a58a75715c784a08baf140e0e1544ad165f1c4f7fd2d27873c4b197\n\
    - graph_id: pdxt-ribulose-ammonium-dependent-synthase-readout\n  title: PdxT supports\
    \ the ribulose-phosphate reaction with external ammonium\n  scope: Figure 1C's\
    \ specific ribulose 5-phosphate comparison with external ammonium sulfate, not\
    \ a universal\n    requirement for PdxT in ammonia-supported synthesis.\n  context:\
    \ 20 uM untagged YaaD with or without 20 uM YaaE, 1 mM ribulose 5-phosphate, 2\
    \ mM DL-glyceraldehyde\n    3-phosphate and 10 mM ammonium sulfate; 50 mM Tris-Cl\
    \ pH 8.0, 37 C; A414 time course. The ribose 5-phosphate\n    condition is a separate\
    \ specificity control.\n  family_mapping: Strain-168 YaaE/PdxT maps to P37528\
    \ and PF01174 6-188. The coupled product readout still\n    requires YaaD and\
    \ the listed substrates; no isolated-domain claim is made.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:224308\n  limitations: Ribose 5-phosphate supports synthesis\
    \ without YaaE in the same external-ammonium experiment.\n    A414 is a product-associated\
    \ readout, not direct identification of an isomerase step. A role in pentulose\n\
    \    isomerization is a proposal, not an observed edge.\n  nodes:\n  - node_id:\
    \ add-yaae-ribulose-ammonium\n    label: Add YaaE to YaaD with ribulose 5-phosphate\
    \ and ammonium\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:P37528\n\
    \  - node_id: ribulose-ammonium-a414\n    label: A414 product-associated signal\
    \ in the ribulose/ammonium reaction\n    node_type: ACTIVITY\n  edges:\n  - edge_id:\
    \ yaae-increases-ribulose-ammonium-product-signal\n    subject: add-yaae-ribulose-ammonium\n\
    \    predicate: increases\n    object: ribulose-ammonium-a414\n    mechanism:\
    \ Adding YaaE increases the product-associated signal for this substrate combination.\
    \ Because\n      the ribose comparison works without YaaE, the effect is bounded\
    \ to the ribulose context and is not\n      explained solely as provision of nitrogen\
    \ from glutamine.\n    directness: DIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:16030023\n      source_url:\
    \ https://archive-ouverte.unige.ch/unige:89531\n      snippet: pyridoxal\n   \
    \   explanation: Visually inspected Figure 1C with its own 20-uM protocol, and\
    \ substrate Results on\n        page 32295; distinct from the 40-uM product-preparation\
    \ assay.\n      cache_path: evidence/PF01174/raschle-2005-pdxt.txt\n      cache_sha256:\
    \ d7f446303a58a75715c784a08baf140e0e1544ad165f1c4f7fd2d27873c4b197\n- graph_id:\
    \ pdxt-acivicin-glutaminase-inhibition\n  title: Acivicin exposure reduces the\
    \ coupled glutaminase readout\n  scope: Figure 3A's 5-mM acivicin preincubation\
    \ of untagged YaaD/YaaE, assayed by glutamate-dependent\n    APAD reduction. This\
    \ is a biochemical treatment, not a cellular antimicrobial effect.\n  context:\
    \ 4 uM each YaaD/YaaE in the pH-8.0 coupled-assay buffer, 5 mM acivicin at 37\
    \ C for the displayed\n    0-10 min pretreatments; add glutamine to 10 mM and\
    \ monitor A363. The selected figure protocol is explicit\n    despite the Methods\
    \ concentration-list discrepancy.\n  family_mapping: YaaE/PdxT corresponds to\
    \ P37528 with PF01174 6-188. The C79-containing peptide 74-87\n    matches the\
    \ reference and is separately assigned as an acivicin target by MS/MS; this does\
    \ not make\n    every proposed atomic step observed.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:224308\n  limitations: Methods list 1/2/10 mM while Figure\
    \ 3 uses 5 mM and 2/5/10 mM. Caption s^-1 conflicts with\n    minute-based Results/time\
    \ axes; no precise inactivation rate is adopted. Raw mass/adduct chemistry\n \
    \   and reporter-specific interference controls remain incompletely assessed;\
    \ covalent-modification evidence\n    supports, but does not replace, assay scope.\n\
    \  nodes:\n  - node_id: acivicin-pretreat-glutaminase-mixture\n    label: Increase\
    \ 5-mM acivicin pretreatment time relative to zero-time control\n    node_type:\
    \ PERTURBATION\n  - node_id: acivicin-assay-glutaminase-readout\n    label: Residual\
    \ coupled glutaminase readout of YaaD/YaaE\n    node_type: ACTIVITY\n    grounding:\n\
    \    - UniProtKB:P37528\n  edges:\n  - edge_id: acivicin-exposure-decreases-glutaminase-readout\n\
    \    subject: acivicin-pretreat-glutaminase-mixture\n    predicate: decreases\n\
    \    object: acivicin-assay-glutaminase-readout\n    mechanism: Longer preincubation\
    \ lowers subsequent APAD-reduction activity relative to zero-time exposure.\n\
    \      The directly observed comparison is the treated biochemical mixture; precise\
    \ inhibition kinetics\n      and a universal drug mechanism are not inferred.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:16030023\n      source_url: https://archive-ouverte.unige.ch/unige:89531\n\
    \      snippet: acivicin\n      explanation: Visually inspected Figure 3A and\
    \ inhibition Methods/Results. Figure 6's peptide assignment\n        is supporting\
    \ chemical context, not a new assumed intermediate.\n      cache_path: evidence/PF01174/raschle-2005-pdxt.txt\n\
    \      cache_sha256: d7f446303a58a75715c784a08baf140e0e1544ad165f1c4f7fd2d27873c4b197\n\
    - graph_id: pdxst-acivicin-plp-signal-inhibition\n  title: Acivicin exposure reduces\
    \ the glutamine-supported PLP synthesis signal\n  scope: Figure 3C's separate\
    \ 40-uM YaaD/YaaE product assay with glutamine as nitrogen donor, not the\n  \
    \  lower-concentration glutaminase assay or an external-ammonium comparison.\n\
    \  context: 40 uM each untagged protein, 0.04-5 mM acivicin in 50 mM Tris-Cl pH\
    \ 8.0 at 37 C; Methods describe\n    60 min exposure. Measure A414 synthesis with\
    \ 0.5 mM ribose 5-phosphate, 0.5 mM DHAP and 10 mM glutamine,\n    relative to\
    \ untreated activity.\n  family_mapping: Strain-168 YaaE is P37528-associated\
    \ PdxT, PF01174 6-188. YaaD supplies the separate\n    synthase activity. Both\
    \ proteins remain in the treated assay mixture.\n  scope_status: MECHANISTIC\n\
    \  taxon: NCBITaxon:224308\n  limitations: The graph does not assign the entire\
    \ loss specifically to one covalent bond, exclude all\n    effects on YaaD/reporting\
    \ chemistry, or demonstrate inhibition in cells. The A414 signal is a relative\n\
    \    activity readout; product identity is independently supported in the untreated\
    \ preparative experiment.\n  nodes:\n  - node_id: acivicin-pretreat-plp-mixture\n\
    \    label: Expose the YaaD/YaaE synthesis mixture to increasing acivicin\n  \
    \  node_type: PERTURBATION\n  - node_id: residual-glutamine-plp-signal\n    label:\
    \ Residual glutamine-supported A414 synthesis activity\n    node_type: ACTIVITY\n\
    \  edges:\n  - edge_id: acivicin-decreases-glutamine-plp-signal\n    subject:\
    \ acivicin-pretreat-plp-mixture\n    predicate: decreases\n    object: residual-glutamine-plp-signal\n\
    \    mechanism: Increasing acivicin exposure reduces the normalized product-associated\
    \ signal in the joint\n      glutamine-supported reaction. It is a separate measured\
    \ endpoint, not a transitive edge inferred\n      only from glutaminase inhibition.\n\
    \    directness: DIRECT\n    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n\
    \    evidence:\n    - reference: PMID:16030023\n      source_url: https://archive-ouverte.unige.ch/unige:89531\n\
    \      snippet: acivicin\n      explanation: Visually inspected Figure 3C and\
    \ its distinct 40-uM enzyme and carbohydrate conditions\n        in the inhibition\
    \ Methods.\n      cache_path: evidence/PF01174/raschle-2005-pdxt.txt\n      cache_sha256:\
    \ d7f446303a58a75715c784a08baf140e0e1544ad165f1c4f7fd2d27873c4b197\ncuration_events:\n\
    - timestamp: '2026-10-11T09:52:07Z'\n  curator: Codex\n  action: CREATE\n  outcome:\
    \ changed\n  summary: Curate partner-dependent PdxT reactions and scoped inhibition\
    \ effects.\n  history_record: history/records/PF01174/2026-10-11T095207Z-codex-f1c1da.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n- timestamp: '2026-10-11T10:02:28Z'\n\
    \  curator: Codex\n  action: REVIEW\n  outcome: needs_followup\n  summary: Retain\
    \ partial scientific self-review of PdxT partner and substrate contexts.\n  history_record:\
    \ history/records/PF01174/2026-10-11T100228Z-codex-196448.yaml\n  event_index:\
    \ 0\n  llm_assisted: true\n- timestamp: '2026-10-25T11:15:00Z'\n  curator: Antigravity\n\
    \  action: EDIT\n  outcome: changed\n  summary: Ground PF01174 causal-graph protein/gene/complex\
    \ nodes with UniProtKB:P37527, UniProtKB:P37528\n  history_record: history/records/PF01174/2026-10-25T111500Z-antigravity-701c9e.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: P37528/PDXT_BACSU, 196 aa and sequence version 1, matches InterPro exactly
    with PF01174 at 6-188. The study specifies strain-168 genomic cloning, construct
    sequencing and N-terminal sequencing. Primer ends match the reference, and the
    C79 peptide maps to residues 74-87 inside the family interval. Untagged biochemical
    preparations are distinct from C-terminal His6 pull-out protein. The earlier SMY
    constructs are not assumed identical to strain 168.
  target_ids:
  - PF01174
  evidence_ids:
  - identity
  - primary
  - deposited-fulltext-and-supplement
  - earlier-smy-preparation-boundary
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: Inputs retain both proteins and substrates where required; the product
    graph does not attribute PLP synthesis to PdxT alone. APAD and A414 are named
    as coupled/product-associated readouts, with orthogonal product identification
    separately retained. The external-ammonium effect is bounded to ribulose 5-phosphate
    because ribose works without YaaE. Acivicin effects are measured independently,
    not joined transitively or transferred to cellular efficacy. C79 labeling and
    physical association are supporting context, not a fully observed atomic cycle.
  target_ids:
  - PF01174
  evidence_ids:
  - primary
  - native
  - deposited-fulltext-and-supplement
  - earlier-smy-preparation-boundary
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Glutamine concentration differs between kinetic captions and Methods/Results,
    inhibition rate units differ between captions and text, and acivicin dose/mass
    descriptions also conflict. Raw spectra, exact adduct chemistry, full clones,
    reporter interference controls and quantitative uncertainties need further assessment.
    SMY identity and its pBB1181 penultimate-residue discrepancy remain unresolved.
    Other microbial, plant and fungal members, later structures and intermediates
    remain outside this partial review.
  target_ids:
  - PF01174
  evidence_ids:
  - primary
- assessment_id: stage4-grounding-and-taxon-audit
  area: representation
  topic: Causal-graph taxon and protein-node grounding consistency
  outcome: concern
  summary: 'In curation/families/PF01174.yaml, four causal graphs omit verified Bacillus
    subtilis 168 (NCBITaxon:224308) YaaD/PdxS (UniProtKB:P37527) and/or YaaE/PdxT
    (UniProtKB:P37528) protein grounding that is explicitly established in their family_mapping
    and in sibling graph pdxt-untagged-partner-dependent-glutaminase (which grounds
    add-yaad-to-yaae-glutamine to [UniProtKB:P37527, UniProtKB:P37528]): (1) in pdxst-glutamine-dependent-plp-product
    (lines 47-79), node joint-pdxst-glutamine-carbohydrate-reaction (''Joint YaaD,
    YaaE, glutamine, ribose 5-phosphate and DHAP reaction'', lines 56-60) grounds
    only to [UniProtKB:P37528] and omits partner YaaD (UniProtKB:P37527); (2) in pdxt-ribulose-ammonium-dependent-synthase-readout
    (lines 80-112), node add-yaae-ribulose-ammonium (''Add YaaE to YaaD with ribulose
    5-phosphate and ammonium'', lines 89-93) grounds only to [UniProtKB:P37528] and
    omits partner YaaD (UniProtKB:P37527); (3) in pdxt-acivicin-glutaminase-inhibition
    (lines 113-145), node acivicin-pretreat-glutaminase-mixture (''Increase 5-mM acivicin
    pretreatment time relative to zero-time control'', lines 122-124) omits grounding:
    [UniProtKB:P37527, UniProtKB:P37528] and node acivicin-assay-glutaminase-readout
    (''Residual coupled glutaminase readout of YaaD/YaaE'', lines 125-129) grounds
    only to [UniProtKB:P37528] and omits partner YaaD (UniProtKB:P37527); and (4)
    in pdxst-acivicin-plp-signal-inhibition (lines 146-176), node acivicin-pretreat-plp-mixture
    (''Expose the YaaD/YaaE synthesis mixture to increasing acivicin'', lines 155-157)
    omits grounding: [UniProtKB:P37527, UniProtKB:P37528] and node residual-glutamine-plp-signal
    (''Residual glutamine-dependent 414-nm PLP signal'', lines 158-160) grounds only
    to [UniProtKB:P37528] and omits partner YaaD (UniProtKB:P37527).'
  target_ids:
  - PF01174
  evidence_ids:
  - stage4-prior-review
findings:
- finding_id: additional-contexts
  issue_key: pf01174-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Reconcile PdxT quantitative discrepancies and extend exact-member coverage
  description: Inspect raw kinetic/MS data and original clones to resolve concentration,
    time-unit and adduct discrepancies before adding quantitative or atomic claims.
    Evaluate reporter controls and later intermediate/structural studies. Resolve
    the SMY genotype/reference boundary and curate its phenotype separately; keep
    alternative nitrogen/substrate conditions and other organisms distinct. Save an
    evidence-backed successor review for extensions.
  target_ids:
  - PF01174
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - deposited-fulltext-and-supplement
  - earlier-smy-preparation-boundary
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01174.yaml
    role: Human-owned scientific overlay
  previous_occurrences:
  - repository: CultureBotAI/DUFMech
    review_id: 20261011T100219Z-pf01174-pdxt-partner-and-substrate-contexts
    finding_id: additional-contexts
- finding_id: pdxst-partner-and-acivicin-nodes-missing-grounding
  issue_key: pf01174-pdxst-partner-and-acivicin-nodes-missing-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Add partner YaaD (UniProtKB:P37527) and joint [UniProtKB:P37527, UniProtKB:P37528]
    grounding to six YaaD/YaaE PLP synthase and acivicin assay nodes in PF01174
  description: 'In curation/families/PF01174.yaml, four causal graphs omit verified
    Bacillus subtilis 168 (NCBITaxon:224308) YaaD/PdxS (UniProtKB:P37527) and/or YaaE/PdxT
    (UniProtKB:P37528) protein grounding that is explicitly established in their family_mapping
    and in sibling graph pdxt-untagged-partner-dependent-glutaminase (which grounds
    add-yaad-to-yaae-glutamine to [UniProtKB:P37527, UniProtKB:P37528]): (1) in pdxst-glutamine-dependent-plp-product
    (lines 47-79), node joint-pdxst-glutamine-carbohydrate-reaction (''Joint YaaD,
    YaaE, glutamine, ribose 5-phosphate and DHAP reaction'', lines 56-60) grounds
    only to [UniProtKB:P37528] and omits partner YaaD (UniProtKB:P37527); (2) in pdxt-ribulose-ammonium-dependent-synthase-readout
    (lines 80-112), node add-yaae-ribulose-ammonium (''Add YaaE to YaaD with ribulose
    5-phosphate and ammonium'', lines 89-93) grounds only to [UniProtKB:P37528] and
    omits partner YaaD (UniProtKB:P37527); (3) in pdxt-acivicin-glutaminase-inhibition
    (lines 113-145), node acivicin-pretreat-glutaminase-mixture (''Increase 5-mM acivicin
    pretreatment time relative to zero-time control'', lines 122-124) omits grounding:
    [UniProtKB:P37527, UniProtKB:P37528] and node acivicin-assay-glutaminase-readout
    (''Residual coupled glutaminase readout of YaaD/YaaE'', lines 125-129) grounds
    only to [UniProtKB:P37528] and omits partner YaaD (UniProtKB:P37527); and (4)
    in pdxst-acivicin-plp-signal-inhibition (lines 146-176), node acivicin-pretreat-plp-mixture
    (''Expose the YaaD/YaaE synthesis mixture to increasing acivicin'', lines 155-157)
    omits grounding: [UniProtKB:P37527, UniProtKB:P37528] and node residual-glutamine-plp-signal
    (''Residual glutamine-dependent 414-nm PLP signal'', lines 158-160) grounds only
    to [UniProtKB:P37528] and omits partner YaaD (UniProtKB:P37527).'
  target_ids:
  - PF01174
  field_paths:
  - causal_graphs
  evidence_ids:
  - stage4-prior-review
  - primary
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01174.yaml
    role: Maintained scientific overlay; update in Stage 5 grouped remediation and
      regenerate projection.
actions:
- action_id: extend-contexts
  description: Inspect raw kinetic/MS data and original clones to resolve concentration,
    time-unit and adduct discrepancies before adding quantitative or atomic claims.
    Evaluate reporter controls and later intermediate/structural studies. Resolve
    the SMY genotype/reference boundary and curate its phenotype separately; keep
    alternative nitrogen/substrate conditions and other organisms distinct. Save an
    evidence-backed successor review for extensions.
  finding_ids:
  - additional-contexts
  - pdxst-partner-and-acivicin-nodes-missing-grounding
  target_ids:
  - PF01174
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- All main text and supplemental captions of the 16-page author-archived PDF were
  read; Figures 1-4, 6/7, S2/S3 and cloning Methods were visually checked. Raw spectra
  were not reprocessed, and no full independent chemical reassignment is claimed.
  Belitsky 2004 main text/captions and Figures 2/4 were inspected for context, not
  adopted as strain-168 edges.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
