# Scoped scientific assessment of DUF39 bacterial growth and fitness graphs

- Review: 20261011T061700Z-pf01837-duf39-causal-graphs
- Repository: CultureBotAI/DUFMech
- Started UTC: 2026-10-11T06:15:18Z
- Finished UTC: 2026-10-11T06:17:00Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain three observed indirect phenotype edges in separate Miyazaki F pooled-fitness and G20 individual plate-growth contexts. Exact member identity is established despite a deleted UniProt entry; construct and medium discrepancies remain explicit. This is partial scientific self-review, not a resolved biochemical mechanism or whole-family endorsement.

## Scope And Provenance

Scientific assessment of the retained edges, exact member mapping, primary evidence, context and causal limits.

Selection: PF01837/HcyBio, former DUF39; primary 2018 DvMF_1464 pooled-fitness and 2014 Dde_3007 complemented plate-growth experiments, kept as distinct member/assay contexts.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d7a87f74786813fcdf65801bdf940d79cc7a56e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PF01837 | data/families/PF01837.yaml | generated | PF01837 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native projection and overlay validation | passed | True | PF01837 | Current projection validates and preserves the authored graph and discussion content exactly. |

## Scientific And Domain Assessments

### Protein, domain and experimental scope

identity: supported. Targets: PF01837.

NCBI ACL08412.1 explicitly maps to DvMF_1464 and taxon 883; its 390-aa sequence matches UniParc UPI00018940C6 exactly, with PF01837 at 22-380. B8DLN6 is deleted from UniProtKB because it is not in a reference proteome, not because the gene lacks evidence. G20 Dde_3007 maps to Q30WZ5/ABB39801.1, reference sequence version 1, 421 aa, PF01837 at 53-411. The paper's revised pJK2 start 2993462 is reference residue 32; 390-aa length and interval 22-380 are conditional calculations assuming the same stop, not an independently obtained clone sequence.

### Directed effects and limits

graph: supported. Targets: PF01837.

The Miyazaki graph retains an insertion-dependent decrease and methionine-dependent increase in normalized gene fitness, explicitly conditional on pooled culture. The G20 graph retains decreased visible plate growth of JK00771 and empty-vector control, with pJK2 rescue supporting locus dependence. All three edges are PHENOTYPIC, INDIRECT, OBSERVED and EXPERIMENTAL. Nutritional versus genetic rescue, different species and assay types, and the revised G20 start remain distinct. The G20 image says MOLS4 while the caption says LS4D; neither exact recipe is silently assigned. No O-phosphohomoserine, thioaldehyde, persulfide-transfer or isolated-domain reaction is promoted from a pathway drawing or phenotype.

### Remaining family coverage

completeness: concern. Targets: PF01837.

Incomplete family and biochemical coverage. Exact G20 insertion position, clone junctions, plate recipe and incubation duration, as well as Miyazaki insertion-level contributions and conflicting 5-versus-10-mL method descriptions, remain unresolved. Archaeal MA1821/MJ0100 biochemical studies and other domain architectures need independent full-text/construct review. The 2014 homoserine-route proposal and later alternative model are not combined into an observed chain; cofitness does not establish direct partners.

## Findings

### additional-contexts: Resolve DUF39 assay discrepancies and extend biochemical member coverage

minor / open / confirmed; issue key: pf01837-causal-context-coverage.

Retrieve G20 supplement Table S1 and Data Set S1 to check the JK00771 insertion and pJK2 junctions, resolve the plate image/caption medium discrepancy, and obtain experiment-level Miyazaki metadata. Inspect primary archaeal biochemical assays with exact member/construct mappings before adding reaction steps. Keep phenotype and chemistry distinct, retain condition-specific negatives, and save a successor review stating which gaps were actually resolved.

## Recommended Actions And Acceptance Checks

### extend-contexts

Retrieve G20 supplement Table S1 and Data Set S1 to check the JK00771 insertion and pJK2 junctions, resolve the plate image/caption medium discrepancy, and obtain experiment-level Miyazaki metadata. Inspect primary archaeal biochemical assays with exact member/construct mappings before adding reaction steps. Keep phenotype and chemistry distinct, retain condition-specific negatives, and save a successor review stating which gaps were actually resolved.

- Each added edge has member-specific primary evidence and explicit conditions.
- Unsupported transfers and conflicting or negative results remain visible.
- Native checks pass and a successor report states actual scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC5764234/; Methionine-synthesis results, Figure 3 visually inspected, Table 2 and strains/media and mutant-fitness methods | supports | DvMF_1464 insertion strains show negative normalized fitness in defined lactate/sulfate medium, and L-methionine supplementation rescues that defect. This is pooled barcode abundance, not a clean deletion, individual growth curve, genetic complementation or direct catalytic measurement. |
| identity | https://rest.uniprot.org/uniparc/UPI00018940C6.json; Accession and domain locations; paired UniProt identity facts | supports | NCBI ACL08412.1 explicitly maps to DvMF_1464 and taxon 883; its 390-aa sequence matches UniParc UPI00018940C6 exactly, with PF01837 at 22-380. B8DLN6 is deleted from UniProtKB because it is not in a reference proteome, not because the gene lacks evidence. G20 Dde_3007 maps to Q30WZ5/ABB39801.1, reference sequence version 1, 421 aa, PF01837 at 53-411. The paper's revised pJK2 start 2993462 is reference residue 32; 390-aa length and interval 22-380 are conditional calculations assuming the same stop, not an independently obtained clone sequence. |
| g20-plate-assay | https://pmc.ncbi.nlm.nih.gov/articles/PMC4045070/; Figure 4C-D visually inspected; Dde_3007 results, strains/media and genetic-complementation methods | supports | JK00771 and empty-vector control have deficient minimal-medium plate growth, whereas wild type and the pJK2-complemented mutant grow. The corrected start and MOLS4-image/LS4D-caption discrepancy are retained. Homocysteine rescue and pooled methionine experiments are separate controls/contexts, not direct biochemical observations. |
| g20-member-identity | https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q30WZ5/entry/pfam/PF01837/; Reference accession, sequence version, Pfam interval and paired NCBI coding coordinates; separately labeled corrected-start calculation | supports | The Dde_3007 locus and PF01837 interval are verified for reference Q30WZ5/ABB39801.1. The primary paper's pJK2 begins 31 residues downstream of that reference start; whole-gene complementation is not an isolated-domain or unchanged-421-aa construct experiment. |
| native | src/dufmech/records.py; Current projection validation and overlay equivalence in this retained-review session | supports | Closed schema, canonical history and applicable graph/evidence checks pass. Curated graphs and discussions match the overlay; scientific validity is assessed separately. |
| duf-projection-pf01837 | data/families/PF01837.yaml; dufmech-reviewed-projection-v1 | context_only | Byte-exact projection retained at save for digest verification, not scientific assessment. |

## Limits And Additional Notes

- The 2018 Figure 3 and 2014 Figure 4 were visually inspected with relevant main methods and results. G20 supplements returned HTML from PMC and HTTP 403 from ASM. Raw barcode, microarray and plate data were not reanalyzed; no supplement contents or independent experimental replication are claimed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion, publication or full publication-QC pass is claimed.
- Assessments were authored from inspected primary evidence. Native inspection supplied provenance, not scientific conclusions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T061700Z-pf01837-duf39-causal-graphs
title: Scoped scientific assessment of DUF39 bacterial growth and fitness graphs
started_at: '2026-10-11T06:15:18Z'
finished_at: '2026-10-11T06:17:00Z'
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
summary: Retain three observed indirect phenotype edges in separate Miyazaki F pooled-fitness
  and G20 individual plate-growth contexts. Exact member identity is established despite
  a deleted UniProt entry; construct and medium discrepancies remain explicit. This
  is partial scientific self-review, not a resolved biochemical mechanism or whole-family
  endorsement.
repository: CultureBotAI/DUFMech
kind: record
source:
  git_revision: 9d7a87f74786813fcdf65801bdf940d79cc7a56e
  state: working_tree
  snapshot_id: interpro-pfam-duf-2026-10-10
  inputs:
  - path: curation/families/PF01837.yaml
    sha256: 45a66e17f09bdaeb9d8aa5df0e45b91ad57e4b14d61d4b032376ce8688ae9ff7
    role: context
  - path: data/families/PF01837.yaml
    sha256: f34b82dac7ac8edf759e694ee7d9d28c9a080cae48b22af20500fe04b920cf82
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
  - path: evidence/PF01837/price-2018-duf39.txt
    role: context
    sha256: 4ea0c146f9c9c538677ffc501d586c07c8a76153c7fc191b27a55d8ec508ead7
  - path: evidence/PF01837/DvMF1464-identity.txt
    role: context
    sha256: e3f1fa5a527f1a142216ccbc40566cdf572c7601b36811e27172046c9df05cd5
  - path: evidence/PF01837/kuehl-2014-duf39.txt
    role: context
    sha256: 6dfff3064a49efa1d8aa1feda776d9b08df2f68e1cc601fc31db53c72111d7b5
  - path: evidence/PF01837/Dde3007-identity.txt
    role: context
    sha256: 2b7b67d20171a0d9ba77b94e8b39e7a183462e8930cc35391f25a3c176ce92a6
targets:
- target_id: PF01837
  path: data/families/PF01837.yaml
  label: PF01837
  kind: generated
  record_class: FamilyRecord
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01837.yaml
    role: Maintained scientific overlay; create only with authorized curation.
  - repository: CultureBotAI/DUFMech
    path: src/dufmech/records.py
    role: Projection generator; frozen snapshot identity is not hand-edited.
  semantic_digest:
    algorithm: dufmech-record-content-v1
    sha256: fabaac139880e020c963e8cf219b210633300576e69348368972b6326cb4089f
    description: Canonical JSON SHA-256 of effective FamilyRecord excluding only curation_status,
      review_id and curation_events.
scope:
  description: Scientific assessment of the retained edges, exact member mapping,
    primary evidence, context and causal limits.
  selection: PF01837/HcyBio, former DUF39; primary 2018 DvMF_1464 pooled-fitness and
    2014 Dde_3007 complemented plate-growth experiments, kept as distinct member/assay
    contexts.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - PF01837
  exclusions:
  - target: Remaining family members and uncurated experimental contexts
    reason: Incomplete family and biochemical coverage. Exact G20 insertion position,
      clone junctions, plate recipe and incubation duration, as well as Miyazaki insertion-level
      contributions and conflicting 5-versus-10-mL method descriptions, remain unresolved.
      Archaeal MA1821/MJ0100 biochemical studies and other domain architectures need
      independent full-text/construct review. The 2014 homoserine-route proposal and
      later alternative model are not combined into an observed chain; cofitness does
      not establish direct partners.
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
  - PF01837
  evidence_ids:
  - native
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5764234/
  locator: Methionine-synthesis results, Figure 3 visually inspected, Table 2 and
    strains/media and mutant-fitness methods
  accessed_at: '2026-10-11T06:17:00Z'
  support: supports
  snapshot_sha256: 4ea0c146f9c9c538677ffc501d586c07c8a76153c7fc191b27a55d8ec508ead7
  summary: DvMF_1464 insertion strains show negative normalized fitness in defined
    lactate/sulfate medium, and L-methionine supplementation rescues that defect.
    This is pooled barcode abundance, not a clean deletion, individual growth curve,
    genetic complementation or direct catalytic measurement.
- evidence_id: identity
  kind: database
  reference: https://rest.uniprot.org/uniparc/UPI00018940C6.json
  locator: Accession and domain locations; paired UniProt identity facts
  accessed_at: '2026-10-11T06:17:00Z'
  support: supports
  snapshot_sha256: e3f1fa5a527f1a142216ccbc40566cdf572c7601b36811e27172046c9df05cd5
  summary: NCBI ACL08412.1 explicitly maps to DvMF_1464 and taxon 883; its 390-aa
    sequence matches UniParc UPI00018940C6 exactly, with PF01837 at 22-380. B8DLN6
    is deleted from UniProtKB because it is not in a reference proteome, not because
    the gene lacks evidence. G20 Dde_3007 maps to Q30WZ5/ABB39801.1, reference sequence
    version 1, 421 aa, PF01837 at 53-411. The paper's revised pJK2 start 2993462 is
    reference residue 32; 390-aa length and interval 22-380 are conditional calculations
    assuming the same stop, not an independently obtained clone sequence.
- evidence_id: g20-plate-assay
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4045070/
  locator: Figure 4C-D visually inspected; Dde_3007 results, strains/media and genetic-complementation
    methods
  summary: JK00771 and empty-vector control have deficient minimal-medium plate growth,
    whereas wild type and the pJK2-complemented mutant grow. The corrected start and
    MOLS4-image/LS4D-caption discrepancy are retained. Homocysteine rescue and pooled
    methionine experiments are separate controls/contexts, not direct biochemical
    observations.
  accessed_at: '2026-10-11T06:17:00Z'
  support: supports
  snapshot_sha256: 6dfff3064a49efa1d8aa1feda776d9b08df2f68e1cc601fc31db53c72111d7b5
- evidence_id: g20-member-identity
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q30WZ5/entry/pfam/PF01837/
  locator: Reference accession, sequence version, Pfam interval and paired NCBI coding
    coordinates; separately labeled corrected-start calculation
  summary: The Dde_3007 locus and PF01837 interval are verified for reference Q30WZ5/ABB39801.1.
    The primary paper's pJK2 begins 31 residues downstream of that reference start;
    whole-gene complementation is not an isolated-domain or unchanged-421-aa construct
    experiment.
  accessed_at: '2026-10-11T06:17:00Z'
  support: supports
  snapshot_sha256: 2b7b67d20171a0d9ba77b94e8b39e7a183462e8930cc35391f25a3c176ce92a6
- evidence_id: native
  kind: validation
  reference: src/dufmech/records.py
  locator: Current projection validation and overlay equivalence in this retained-review
    session
  accessed_at: '2026-10-11T06:17:00Z'
  support: supports
  summary: Closed schema, canonical history and applicable graph/evidence checks pass.
    Curated graphs and discussions match the overlay; scientific validity is assessed
    separately.
- evidence_id: duf-projection-pf01837
  kind: record_content
  reference: data/families/PF01837.yaml
  locator: dufmech-reviewed-projection-v1
  accessed_at: '2026-10-11T06:17:00Z'
  support: context_only
  snapshot_sha256: f34b82dac7ac8edf759e694ee7d9d28c9a080cae48b22af20500fe04b920cf82
  quote: "id: Pfam:PF01837\npfam_id: PF01837\nname: Homocysteine biosynthesis enzyme,\
    \ sulfur-incorporation\nshort_name: HcyBio\nseed_status: EX_DUF\ncharacterization_status:\
    \ UNSCORED\ncuration_status: IN_PROGRESS\nsource_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01837\n\
    counters:\n  proteins: 825\n  matches: 827\n  proteomes: 684\n  taxa: 1663\n \
    \ structures: 0\n  alphafold_models: 656\n  domain_architectures: 8\nprovenance:\n\
    \  snapshot_id: interpro-pfam-duf-2026-10-10\n  path: data/worklists/interpro-pfam-duf-2026-10-10.json\n\
    \  sha256: 17fb625876c9326ed284263a47bcd84e0d7844a31c040dc06cd2260c36f1c383\n\
    \  generated_at: '2026-10-10T07:44:21.614711Z'\n  source_url: https://www.ebi.ac.uk/interpro/api/entry/pfam/\n\
    interpro_id: InterPro:IPR002708\ndescription: This presumed domain is about is\
    \ about 360 residues long. The function of this domain is\n  not clear. It is\
    \ found at N terminus in some proteins that have two C-terminal cystathionine\
    \ beta-synthase\n  (CBS) domains, such as MJ0100 from Methanocaldococcus jannaschii.\
    \ This domain can also be found in proteins\n  that contain two C-terminal inserted\
    \ Fe4S domains [[cite:PUB00093781]]. In Methanocaldococcus jannaschii,\n  MJ0100\
    \ and its ortholog MA1821 from Methanosarcina acetivorans are involved in Hcy\
    \ (homocysteine) biosynthesis.\n  MJ0100 CBS domains bind S-adenosyl-l-methionine\
    \ (SAM) and 5'-methylthioadenosine (MTA), which induce\n  a conformational change\
    \ consistent with regulatory function. Another protein in the homocysteine biosynthesis\n\
    \  pathway, MJ0099 and its ortholog MA1822, is involved in the reduction of the\
    \ disulfide formed in MJ0100/MA1821\n  during the conversion of Asa (aspartate\
    \ semialdehyde) to Hcy [[cite:PUB00078766],[cite:PUB00093781]].\n  The DUF39-CBS\
    \ and DUF39-ferredoxin architectures repeatedly occur together in the genomes\
    \ of methanogenic\n  Archaea, suggesting they may be of diverged function. This\
    \ is consistent with a phylogenetic reconstruction\n  of the DUF39 family, which\
    \ clearly distinguishes the CBS-associated and ferredoxin-associated DUF39s\n\
    \  [[cite:PUB00078766]] .\ncuration_history: history/records/PF01837\ndiscussions:\n\
    - discussion_id: duf39-assay-resolution-and-biochemistry\n  prompt: Resolve assay\
    \ and construct details and inspect member-specific biochemical evidence before\n\
    \    adding DUF39 reaction steps.\n  kind: CURATION_TODO\n  status: OPEN\n  rationale:\
    \ The retained graphs establish conditional genetic and nutritional effects in\
    \ two bacterial\n    strains. Neither proves sulfur transfer, a thioaldehyde intermediate,\
    \ isolated-domain catalysis or\n    the functions of archaeal CBS/ferredoxin fusions.\n\
    \  evidence:\n  - reference: PMID:29324779\n    supports: PARTIAL\n    evidence_source:\
    \ full_text\n    explanation: Figure 3 supports pooled fitness and methionine\
    \ rescue; strain-specific and generic methods\n      differ on culture volume.\
    \ Insertion-level data, exact timing and genetic complementation of DvMF_1464\n\
    \      remain outside this assessment.\n  - reference: PMID:24865553\n    supports:\
    \ PARTIAL\n    evidence_source: full_text\n    explanation: Figure 4 and complementation\
    \ methods support the G20 plate phenotype; the image/caption\n      medium discrepancy,\
    \ full pJK2 junctions and insertion coordinate need follow-up. Supplemental PDF/XLSX\n\
    \      retrieval returned HTML or HTTP 403.\n  - reference: PMID:25938369\n  \
    \  supports: PARTIAL\n    evidence_source: abstract\n    explanation: Archaeal\
    \ homocysteine synthesis from aspartate semialdehyde and hydrogen sulfide is a\n\
    \      primary biochemical lead; its full assays and tested constructs were not\
    \ independently inspected\n      here.\n  - reference: PMID:28165724\n    supports:\
    \ PARTIAL\n    evidence_source: abstract\n    explanation: MA1821 persulfide evidence\
    \ is a distinct archaeal lead. The abstract's SepCysS single-turnover\n      result\
    \ must not be transferred to MA1821 or the bacterial proteins.\n  posed_by: Codex\n\
    \  posed_date: '2026-10-11'\n  notes: Preserve the historical UniProt deletion\
    \ and corrected G20 start. Nutritional rescue is not the\n    same as genetic\
    \ rescue. Do not merge the 2014 proposed homoserine route and the later alternate\
    \ model\n    into an observed chain, or infer protein partners from cofitness\
    \ alone.\ncausal_graphs:\n- graph_id: miyazaki-duf39-pooled-fitness\n  title:\
    \ DvMF_1464 insertion mutants have a methionine-rescuable fitness defect\n  scope:\
    \ Pooled barcoded transposon mutants of D. vulgaris Miyazaki F, measuring relative\
    \ abundance of\n    DvMF_1464 insertion strains during lactate/sulfate growth;\
    \ not a clean deletion, individual growth\n    curve or purified DUF39 reaction.\n\
    \  context: Figure 3 compares defined lactate/sulfate medium without added amino\
    \ acids with supplementation,\n    including L-methionine at 1 or 10 mM. Pools\
    \ are recovered in rich medium, transferred at OD600 0.02\n    and assayed at\
    \ saturation by barcode sequencing. Miyazaki-specific methods describe anaerobic,\
    \ unshaken\n    Hungate cultures with 1 mM sulfide and 10 mL medium; generic fitness\
    \ methods say 5 mL. Exact Figure\n    3 volume, temperature and elapsed time remain\
    \ unverified.\n  family_mapping: DvMF_1464 maps to NCBIProtein:ACL08412.1, CP001197.1\
    \ positions 1794909-1796081, and\n    the identical 390-aa sequence in UniParc\
    \ UPI00018940C6, with PF01837 at 22-380. Historical UniProtKB\n    B8DLN6 is deleted\
    \ because it is not in a reference proteome; it is not an unresolved protein identity.\n\
    \    The taxon 883 archive now uses Nitratidesulfovibrio vulgaris for the same\
    \ Miyazaki F strain.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:883\n  limitations:\
    \ Fitness is a normalized change in mutant abundance relative to the pool, not\
    \ an absolute\n    growth rate or a wild-type-versus-deletion monoculture comparison.\
    \ Nutritional rescue is not genetic\n    complementation. Insertion polarity,\
    \ cross-feeding and insertion-level contributions were not independently\n   \
    \ resolved. Partial cysteine rescue and the different homoserine-dehydrogenase\
    \ locus are not proof of\n    this protein's catalytic substrate or a direct sulfur-transfer\
    \ step. No isolated-domain or family-wide\n    mechanism is assigned.\n  nodes:\n\
    \  - node_id: dvmf1464-insertions\n    label: Transposon disruption of DvMF_1464\
    \ in the Miyazaki mutant pool\n    node_type: PERTURBATION\n    grounding:\n \
    \   - NCBIProtein:ACL08412.1\n  - node_id: methionine-added-to-mutant-pool\n \
    \   label: L-methionine addition to the DvMF_1464-containing mutant pool\n   \
    \ node_type: PERTURBATION\n  - node_id: dvmf1464-relative-fitness\n    label:\
    \ Relative fitness of DvMF_1464 insertion mutants during pooled growth\n    node_type:\
    \ PHENOTYPE\n  edges:\n  - edge_id: insertions-decrease-minimal-medium-fitness\n\
    \    subject: dvmf1464-insertions\n    predicate: decreases\n    object: dvmf1464-relative-fitness\n\
    \    mechanism: Without added amino acids, DvMF_1464 insertion mutants decline\
    \ in normalized relative abundance\n      during growth, producing negative gene-fitness\
    \ values. This is a conditional perturbation phenotype\n      measured against\
    \ the pool baseline.\n    directness: INDIRECT\n    support: OBSERVED\n    evidence_kind:\
    \ EXPERIMENTAL\n    evidence:\n    - reference: PMID:29324779\n      source_url:\
    \ https://pmc.ncbi.nlm.nih.gov/articles/PMC5764234/\n      snippet: were important\
    \ for growth in minimal media\n      explanation: The DvMF_1464 row of visually\
    \ inspected Figure 3 and the adjacent results support negative\n        pooled\
    \ fitness; barcode methods define the endpoint. It is not a measurement of homocysteine\
    \ synthesis\n        or an individually complemented deletion.\n      cache_path:\
    \ evidence/PF01837/price-2018-duf39.txt\n      cache_sha256: 4ea0c146f9c9c538677ffc501d586c07c8a76153c7fc191b27a55d8ec508ead7\n\
    \    - reference: https://rest.uniprot.org/uniparc/UPI00018940C6.json\n      source_url:\
    \ https://rest.uniprot.org/uniparc/UPI00018940C6.json\n      snippet: 'database:\
    \ Pfam; databaseId: PF01837; locations: 22-380, inclusive'\n      explanation:\
    \ Exact-sequence archival mapping linked to NCBI ACL08412.1 and the paper's locus/strain;\n\
    \        not experimental evidence for the phenotype.\n      cache_path: evidence/PF01837/DvMF1464-identity.txt\n\
    \      cache_sha256: e3f1fa5a527f1a142216ccbc40566cdf572c7601b36811e27172046c9df05cd5\n\
    \  - edge_id: methionine-increases-mutant-fitness\n    subject: methionine-added-to-mutant-pool\n\
    \    predicate: increases\n    object: dvmf1464-relative-fitness\n    mechanism:\
    \ Adding L-methionine to the defined-medium mutant-pool assay relieves the negative\
    \ DvMF_1464\n      gene-fitness phenotype compared with the unsupplemented condition;\
    \ the source context includes the\n      mutant pool rather than methionine as\
    \ an independently sufficient protein activity.\n    directness: INDIRECT\n  \
    \  support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    - reference:\
    \ PMID:29324779\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5764234/\n\
    \      snippet: mutants in these genes were rescued by added methionine\n    \
    \  explanation: Figure 3's DvMF_1464 row and caption support the nutritional-rescue\
    \ comparison at the\n        stated millimolar doses. The grouped cysteine mean\
    \ is not assigned to this single gene, and a\n        biochemical conversion is\
    \ not inferred.\n      cache_path: evidence/PF01837/price-2018-duf39.txt\n   \
    \   cache_sha256: 4ea0c146f9c9c538677ffc501d586c07c8a76153c7fc191b27a55d8ec508ead7\n\
    \    - reference: https://rest.uniprot.org/uniparc/UPI00018940C6.json\n      source_url:\
    \ https://rest.uniprot.org/uniparc/UPI00018940C6.json\n      snippet: 'locus_tag:\
    \ DvMF_1464'\n      explanation: Identifies the focal mutant gene and its family;\
    \ shared-sequence records from other\n        taxa are not substituted for Miyazaki\
    \ F.\n      cache_path: evidence/PF01837/DvMF1464-identity.txt\n      cache_sha256:\
    \ e3f1fa5a527f1a142216ccbc40566cdf572c7601b36811e27172046c9df05cd5\n- graph_id:\
    \ g20-duf39-individual-mutant-growth\n  title: Dde_3007 disruption reduces minimal-medium\
    \ plate growth in G20\n  scope: Individual D. alaskensis G20 transposon mutant\
    \ JK00771, wild type and plasmid controls in Figure\n    4C; separate from the\
    \ 2014 and 2018 pooled-fitness assays.\n  context: JK00771 Dde_3007::Tn5 and its\
    \ empty-vector pMO9075 derivative are compared with G20 and JK00771\n    carrying\
    \ pJK2. The plate image says MOLS4, whereas the caption says LS4D; the exact minimal\
    \ lactate/sulfate\n    formulation remains unresolved. General culture conditions\
    \ are anaerobic 30 C, but the plate assay\n    duration is not established. Figure\
    \ 4D separately shows homocysteine rescue without establishing its\n    dose here.\n\
    \  family_mapping: Dde_3007 is reference UniProtKB:Q30WZ5, sequence version 1,\
    \ 421 aa, PF01837 at 53-411,\n    and NCBI ABB39801.1 on CP000112.1 positions\
    \ 2993369-2994634. The paper's sequence-verified pJK2 uses\n    revised start\
    \ 2993462, corresponding to reference residue 32. Assuming the same stop predicts\
    \ a 390-aa\n    product and interval 22-380; this calculation is not an independently\
    \ retrieved full clone sequence.\n    The taxon 207559 current name is Oleidesulfovibrio\
    \ alaskensis G20.\n  scope_status: PHENOTYPIC\n  taxon: NCBITaxon:207559\n  limitations:\
    \ The endpoint is visible plate growth, not a quantitative colony count, direct\
    \ reaction\n    assay or proof of an isolated-domain function. pJK2 complementation\
    \ supports gene dependence; exact\n    insertion position and clone junctions\
    \ remain unverified because supplements were inaccessible. The\n    source's O-phosphohomoserine\
    \ pathway is proposed, and later work questions homoserine participation.\n  \
    \  No such catalytic step or universal persulfide mechanism is adopted.\n  nodes:\n\
    \  - node_id: dde3007-disruption\n    label: Dde_3007 transposon disruption in\
    \ JK00771\n    node_type: PERTURBATION\n    grounding:\n    - UniProtKB:Q30WZ5\n\
    \  - node_id: minimal-plate-growth\n    label: Visible growth on the Figure 4C\
    \ minimal lactate/sulfate plate\n    node_type: PHENOTYPE\n  edges:\n  - edge_id:\
    \ disruption-decreases-plate-growth\n    subject: dde3007-disruption\n    predicate:\
    \ decreases\n    object: minimal-plate-growth\n    mechanism: The insertion mutant\
    \ and empty-vector control show deficient plate growth relative to wild\n    \
    \  type, while pJK2 restores growth, supporting a locus-dependent cellular phenotype\
    \ without resolving\n      the metabolic reaction.\n    directness: INDIRECT\n\
    \    support: OBSERVED\n    evidence_kind: EXPERIMENTAL\n    evidence:\n    -\
    \ reference: PMID:24865553\n      source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4045070/\n\
    \      snippet: we complemented the methionine auxotrophy\n      explanation:\
    \ Visually inspected Figure 4C and genetic-complementation methods establish the\
    \ insertion\n        phenotype and rescue. The MOLS4-image versus LS4D-caption\
    \ discrepancy and revised construct start\n        are retained rather than silently\
    \ normalized.\n      cache_path: evidence/PF01837/kuehl-2014-duf39.txt\n     \
    \ cache_sha256: 6dfff3064a49efa1d8aa1feda776d9b08df2f68e1cc601fc31db53c72111d7b5\n\
    \    - reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q30WZ5/entry/pfam/PF01837/\n\
    \      source_url: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q30WZ5/entry/pfam/PF01837/\n\
    \      snippet: 'entry accession: PF01837; family interval: 53-411, inclusive'\n\
    \      explanation: Maps the reference locus, with the paper's revised-start distinction\
    \ explicitly retained;\n        not evidence that the complementation product\
    \ is the unchanged 421-aa annotation.\n      cache_path: evidence/PF01837/Dde3007-identity.txt\n\
    \      cache_sha256: 2b7b67d20171a0d9ba77b94e8b39e7a183462e8930cc35391f25a3c176ce92a6\n\
    curation_events:\n- timestamp: '2026-10-11T06:13:40Z'\n  curator: Codex\n  action:\
    \ CREATE\n  outcome: changed\n  summary: Add separate DUF39 bacterial fitness\
    \ and plate-growth causal graphs\n  history_record: history/records/PF01837/2026-10-11T061340Z-codex-7ee727.yaml\n\
    \  event_index: 0\n  llm_assisted: true\n"
  summary: Byte-exact projection retained at save for digest verification, not scientific
    assessment.
assessments:
- assessment_id: member-identity
  area: identity
  topic: Protein, domain and experimental scope
  outcome: supported
  summary: NCBI ACL08412.1 explicitly maps to DvMF_1464 and taxon 883; its 390-aa
    sequence matches UniParc UPI00018940C6 exactly, with PF01837 at 22-380. B8DLN6
    is deleted from UniProtKB because it is not in a reference proteome, not because
    the gene lacks evidence. G20 Dde_3007 maps to Q30WZ5/ABB39801.1, reference sequence
    version 1, 421 aa, PF01837 at 53-411. The paper's revised pJK2 start 2993462 is
    reference residue 32; 390-aa length and interval 22-380 are conditional calculations
    assuming the same stop, not an independently obtained clone sequence.
  target_ids:
  - PF01837
  evidence_ids:
  - identity
  - primary
  - g20-plate-assay
  - g20-member-identity
- assessment_id: causal-scope
  area: graph
  topic: Directed effects and limits
  outcome: supported
  summary: The Miyazaki graph retains an insertion-dependent decrease and methionine-dependent
    increase in normalized gene fitness, explicitly conditional on pooled culture.
    The G20 graph retains decreased visible plate growth of JK00771 and empty-vector
    control, with pJK2 rescue supporting locus dependence. All three edges are PHENOTYPIC,
    INDIRECT, OBSERVED and EXPERIMENTAL. Nutritional versus genetic rescue, different
    species and assay types, and the revised G20 start remain distinct. The G20 image
    says MOLS4 while the caption says LS4D; neither exact recipe is silently assigned.
    No O-phosphohomoserine, thioaldehyde, persulfide-transfer or isolated-domain reaction
    is promoted from a pathway drawing or phenotype.
  target_ids:
  - PF01837
  evidence_ids:
  - primary
  - native
  - g20-plate-assay
  - g20-member-identity
- assessment_id: remaining-coverage
  area: completeness
  topic: Remaining family coverage
  outcome: concern
  summary: Incomplete family and biochemical coverage. Exact G20 insertion position,
    clone junctions, plate recipe and incubation duration, as well as Miyazaki insertion-level
    contributions and conflicting 5-versus-10-mL method descriptions, remain unresolved.
    Archaeal MA1821/MJ0100 biochemical studies and other domain architectures need
    independent full-text/construct review. The 2014 homoserine-route proposal and
    later alternative model are not combined into an observed chain; cofitness does
    not establish direct partners.
  target_ids:
  - PF01837
  evidence_ids:
  - primary
findings:
- finding_id: additional-contexts
  issue_key: pf01837-causal-context-coverage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve DUF39 assay discrepancies and extend biochemical member coverage
  description: Retrieve G20 supplement Table S1 and Data Set S1 to check the JK00771
    insertion and pJK2 junctions, resolve the plate image/caption medium discrepancy,
    and obtain experiment-level Miyazaki metadata. Inspect primary archaeal biochemical
    assays with exact member/construct mappings before adding reaction steps. Keep
    phenotype and chemistry distinct, retain condition-specific negatives, and save
    a successor review stating which gaps were actually resolved.
  target_ids:
  - PF01837
  field_paths:
  - causal_graphs
  evidence_ids:
  - primary
  - identity
  - g20-plate-assay
  - g20-member-identity
  owner_paths:
  - repository: CultureBotAI/DUFMech
    path: curation/families/PF01837.yaml
    role: Human-owned scientific overlay
actions:
- action_id: extend-contexts
  description: Retrieve G20 supplement Table S1 and Data Set S1 to check the JK00771
    insertion and pJK2 junctions, resolve the plate image/caption medium discrepancy,
    and obtain experiment-level Miyazaki metadata. Inspect primary archaeal biochemical
    assays with exact member/construct mappings before adding reaction steps. Keep
    phenotype and chemistry distinct, retain condition-specific negatives, and save
    a successor review stating which gaps were actually resolved.
  finding_ids:
  - additional-contexts
  target_ids:
  - PF01837
  ownership_note: Curate overlay and minimal evidence; append actual history, regenerate
    and retain successor review.
  acceptance_checks:
  - Each added edge has member-specific primary evidence and explicit conditions.
  - Unsupported transfers and conflicting or negative results remain visible.
  - Native checks pass and a successor report states actual scope.
limitations:
- The 2018 Figure 3 and 2014 Figure 4 were visually inspected with relevant main methods
  and results. G20 supplements returned HTML from PMC and HTTP 403 from ASM. Raw barcode,
  microarray and plate data were not reanalyzed; no supplement contents or independent
  experimental replication are claimed.
- Same-agent assessment, not independent expert review or experimental replication.
- Partial family coverage; status remains IN_PROGRESS. No full-corpus completion,
  publication or full publication-QC pass is claimed.
notes:
- Assessments were authored from inspected primary evidence. Native inspection supplied
  provenance, not scientific conclusions.
```
