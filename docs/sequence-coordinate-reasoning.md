# Sequence-Coordinate-Aware Reasoning

DUFMech's sequence-coordinate-aware reasoning layer (`src/dufmech/sequence_reasoning.py` and the `RegionReasoningGraph` LinkML model in `src/dufmech/schema/dufmech.yaml`) connects identified protein sequences and explicit residue intervals to standardized experimental and computational observations, deduplicated evidence groups, and evidence-graded functional claims.

## 1. Canonical Sequence Identity and 1-Based Inclusive Coordinates

Every region in a `RegionReasoningGraph` is anchored to an explicit `SequenceIdentity`:

- **`sequence_id`**: Local identifier within the reasoning graph (for example `seq_Q99973_v3`).
- **`uniprot_accession`** and optional **`isoform`** (`Q99973-1`) and **`sequence_version`** (`3`).
- **`sequence_length`**: Exact residue count ($\ge 1$).
- **`sequence_sha256`** (required 64-hex digest) and optional **`sequence_md5`**: Cryptographic sequence checksums verifying that coordinates are evaluated against an identical amino-acid sequence.
- **`taxon_id`**, **`organism`**, **`uniprot_release`**, and **`source_url`**.

### Coordinate Convention

All normalized `SequenceInterval` objects use **1-based inclusive** `[start, end]` coordinates on the referenced `SequenceIdentity`:

- `1 <= start <= end <= sequence_length`.
- Single-residue sites (catalytic residues, point mutations, post-translational modifications) are represented as `start == end` with optional `residue_identity` (verified against the sequence string when provided).
- Boundary fuzziness is preserved via `coordinate_status: UNCERTAIN_BOUNDARY` and interval flags `start_uncertain` / `end_uncertain`.
- Whole-protein assays or unlocalized database annotations are marked `coordinate_status: WHOLE_PROTEIN_UNLOCALIZED` (`region_kind: FULL_LENGTH_PROTEIN`), preventing silent attribution of a full-protein phenotype to an individual domain in a multidomain protein.
- Annotations with unknown sequence boundaries use `coordinate_status: UNKNOWN_LOCALIZATION` (`region_kind: UNKNOWN_LOCALIZATION`) with an empty interval list rather than fabricated coordinates.

### Discontinuous (Multi-Segment) Domains

Split or inserted domains are represented as `region_kind: DISCONTINUOUS_DOMAIN` (`coordinate_status: DISCONTINUOUS`) with two or more strictly ordered, disjoint intervals (`intervals[i].end < intervals[i+1].start`).

- `region_residue_positions(region)` computes the exact union of segment residues, excluding inter-segment gaps.
- `region_inter_segment_gaps(region)` returns the 1-based inclusive `[gap_start, gap_end]` intervals between segments.
- A mutation or structural feature falling inside an inter-segment gap (for example residue `165` between segments `50..120` and `210..290`) is classified as `DISJOINT_OUTSIDE_REGION`, never inside the discontinuous domain.

### Explicit Coordinate Conversions

When a primary paper or upstream database reports non-canonical coordinates, conversion helpers record both `source_coordinate_system`, `source_coordinates_text`, and `conversion_provenance`:

- `convert_construct_to_reference(...)`: Maps 1-based construct-local coordinates `[local_start, local_end]` on a recombinant construct spanning `[construct_start_on_ref, construct_end_on_ref]` to `ref_pos = construct_start_on_ref + local_pos - 1`.
- `convert_mature_peptide_to_reference(...)`: Maps 1-based mature chain numbering after a cleaved signal peptide `1..signal_peptide_end` to precursor coordinates `ref_pos = signal_peptide_end + mature_pos`.
- `convert_zero_based_half_open_to_reference(...)`: Converts 0-based half-open intervals `[zero_start, zero_end)` to 1-based inclusive `[zero_start + 1, zero_end]`.

## 2. Coordinate Mapping and Equivalence Classification

`classify_region_mapping(...)` produces a `CoordinateMapping` between a `source_region` and `target_region`, computing exact residue overlap (`overlap_residues`), `source_coverage`, `target_coverage`, `residue_correspondences` (`ResidueCorrespondence`, including PDB insertion codes and mutation substitutions such as `E1008A`), and a strict `MappingEquivalenceStatus`:

- **`EXACT_MATCH`**: Identical residue sets on the same verified sequence.
- **`DISCONTINUOUS_MAPPING`**: Exact multi-segment match across discontinuous intervals.
- **`CONSTRUCT_CONTAINS_DOMAIN`**: An experimental construct or full-length protein completely spans the target domain (`target_coverage == 1.0`, `source_coverage < 1.0`). When the source is `WHOLE_PROTEIN_UNLOCALIZED` without a domain-internal catalytic mutation, localization to the domain is blocked.
- **`DOMAIN_CONTAINS_REGION`**: The target domain completely contains a sub-region or motif.
- **`RESIDUE_INSIDE_REGION`**: A single residue or active-site motif lies inside the target domain (or maps via explicit residue correspondence).
- **`PARTIAL_OVERLAP_NOT_EQUIVALENT`**: Partial coordinate overlap (`0 < source_coverage < 1` and `0 < target_coverage < 1`). Partial overlap never establishes domain equivalence or experimental localization.
- **`DISJOINT_OUTSIDE_REGION`**: Zero shared residues (including sites located in an adjacent domain or in the inter-segment gap of a discontinuous domain).
- **`SEQUENCE_VERSION_MISMATCH`**: Same UniProt accession with differing `sequence_sha256`, `sequence_version`, or `isoform` (without an explicit `ISOFORM_TO_CANONICAL` residue correspondence). Blocks silent coordinate transfer.
- **`UNRESOLVED_MAPPING`**: One or both regions have `UNKNOWN_LOCALIZATION` or lack residue correspondence across sequences.

## 3. Standardized Observations and Non-Interchangeable Scores

`RegionObservation` separates the empirical or computational observation from its functional interpretation:

- **`observed_effect`** vs. **`interpretation`**: Keeps raw assay readouts or HMM hits distinct from mechanistic conclusions.
- **`evidence_kind`** (`EXPERIMENTAL`, `COMPUTATIONAL`, `CONTEXTUAL`), **`source_kind`** (`LITERATURE_ASSAY`, `PDBE_KB`, `INTERPRO_PFAM`, `CDSEARCH`, `CATH_FUNFAM`, `NCBIFAM`, `QUICKGO`, `RHEA`, `ALPHAFOLD`, `CURATED_ANNOTATION`), and **`polarity`** (`POSITIVE`, `NEGATIVE`, `NEUTRAL_OR_UNCHANGED`).
- **`tested_construct_region_id`**, **`mutation_region_ids`**, **`assay_conditions`**, **`limitations`**, and optional **`evidence`** (`EvidenceItem` extracts verified against `evidence/*.txt` SHA-256 hashes and exact quotations).

### Source Normalization Adapters

`src/dufmech/sequence_reasoning.py` provides deterministic normalizers for DUFMech's existing source row formats:

- `normalize_pfam_member_row(...)` (`InterPro/Pfam` single- and multi-fragment hits)
- `normalize_pdbe_kb_row(...)` (`PDBe-KB` ligand/macromolecular/site annotations with SIFTS coordinates, PDB insertion codes, and engineered mutation warnings)
- `normalize_cdsearch_row(...)` (`NCBI CD-Search` RPS-BLAST hits)
- `normalize_cath_row(...)` (`CATH-Gene3D / FunFam` hits)
- `normalize_ncbifam_row(...)` (`NCBIfam` HMM hits)
- `normalize_quickgo_row(...)` (`QuickGO` annotations, classifying experimental vs. contextual vs. computational GO/ECO codes, `NOT` qualifiers, and defaulting unlocalized protein annotations to `WHOLE_PROTEIN_UNLOCALIZED`)
- `normalize_rhea_row(...)` (`Rhea` reaction cross-references)

### Score Metric Separation

Observations may record a numeric `raw_score` paired with an explicit `score_metric` (`E_VALUE`, `BITSCORE`, `CATH_CONFIDENCE`, `PLDDT`, `KM_MM`, `KCAT_PER_S`, `QUALITATIVE`). `combine_scores_strictly(...)` verifies whether scores share a single metric and raises a `ValueError` if heterogeneous metrics (such as `E_VALUE` and `BITSCORE` or `PLDDT`) are combined as interchangeable probabilities.

## 4. Dependent-Evidence Deduplication

`deduplicate_observations(...)` collapses dependent observations into `EvidenceGroup` objects before claim synthesis:

- Observations sharing the same `primary_experiment_key` (for example a primary biochemical assay and a secondary curated/QuickGO/Rhea record citing the same PMID, protein, and construct, or a Pfam HMM hit mirrored by InterPro and CD-Search) are grouped into a single `EvidenceGroup`.
- Observations citing an upstream observation in `derived_from_observation_ids` resolve transitively to the parent observation's `primary_experiment_key` (rejecting derivation cycles).
- Claim synthesis counts independent `EvidenceGroup` units rather than raw `RegionObservation` rows.

## 5. Claim Synthesis, Contradictions, and Scope Discipline

`synthesize_region_claim(...)` evaluates deduplicated `EvidenceGroup` units and `CoordinateMapping` records to produce a `SynthesizedClaim` with a `FunctionAspect`, `SynthesisStatus`, `ClaimScope`, `scope_transfer_blocks`, and `discriminating_experiments`:

- **`EXPERIMENTALLY_DEMONSTRATED`**: Requires at least one localized `POSITIVE` `EXPERIMENTAL` `EvidenceGroup` with no conflicting localized negative experimental group and no disjoint-mutation or coordinate-localization block. Scope defaults to `TESTED_CONSTRUCT` (when assayed on a construct) or `TESTED_REGION_ONLY`, and broader requested scopes (`FAMILY_WIDE`, `CONSERVED_SUBFAMILY`, `SPECIFIC_PROTEIN`) are restricted when `scope_transfer_blocks` are present (for example inactive human paralogues NWD1, NWD2, and NPHP3 in `PF13271`).
- **`SUPPORTED_INFERENCE`**: Supported by homolog experimental evidence with explicit alignment/residue correspondence, without direct assay on the target protein.
- **`COMPUTATIONAL_HYPOTHESIS`**: Supported only by computational predictions (`INTERPRO_PFAM`, `CDSEARCH`, `CATH_FUNFAM`, `NCBIFAM`, `ALPHAFOLD`) or contextual co-occurrence (for example `Q31PW6` in `PF13271`).
- **`CONFLICTING_UNRESOLVED`**: Contradictory positive and negative localized experimental groups, or experimental observations blocked by coordinate non-equivalence (`PARTIAL_OVERLAP_NOT_EQUIVALENT`, `DISJOINT_OUTSIDE_REGION`, `WHOLE_PROTEIN_UNLOCALIZED`, `SEQUENCE_VERSION_MISMATCH`). Preserves both sides and records `discriminating_experiments`.
- **`NEGATIVE_EVIDENCE_ONLY`**: Direct localized experimental assay(s) tested a specific activity and found none (`polarity: NEGATIVE`), with no conflicting positive experimental evidence.
- **`INSUFFICIENT_EVIDENCE`**: No observations are anchored to the region (`function_aspect: UNKNOWN_FUNCTION`). Missing evidence is never conflated with `NEGATIVE_EVIDENCE_ONLY`.

## 6. Epistemic Edges vs. Biological Causal Edges

`ReasoningEdge` enforces a strict boundary between epistemic provenance and biological mechanism:

- **Epistemic edge categories**:
  - `COORDINATE_MAPPING_LINK`: `anchored_to_sequence`, `maps_to_region`
  - `EVIDENCE_LINK`: `observed_on_region`, `grouped_into_evidence_unit`, `supports_claim`, `contradicts_claim`, `constrains_claim_scope`
  - `INFERENCE_LINK`: `inferred_from_homolog_region`, `cooccurs_with_domain`
- **Biological causal edge category**:
  - `CAUSAL_BIOLOGICAL_LINK`: `enables_biological_activity`, `produces_metabolite`, `degrades_substrate`, `required_for_process`
- Validation rejects any `CAUSAL_BIOLOGICAL_LINK` that uses an epistemic predicate or claims `support: OBSERVED` with `evidence_kind != EXPERIMENTAL`, and rejects any epistemic edge that uses a biological causal predicate.
- Curated `FunctionalAssertion` items and `CausalNode` entries in `FamilyCuration` / `FamilyRecord` can optionally reference `sequence_id`, `region_id`, and `synthesized_claim_id`, which `dufmech.records` validates against `sequence_reasoning_graphs`.

## 7. CLI, Region Queries, Evidence Tracing, and Inspectable Views

Run the CLI or `just sequence-reasoning` to inspect, query, and trace representative or record-backed reasoning graphs:

```bash
# Render human-inspectable Markdown views of the 3 representative end-to-end graphs
uv run --locked python -m dufmech.sequence_reasoning --demo --format markdown

# Emit machine-inspectable JSON
uv run --locked python -m dufmech.sequence_reasoning --demo --format json

# Query synthesized claims overlapping a 1-based inclusive coordinate range on a sequence
uv run --locked python -m dufmech.sequence_reasoning --demo \
  --query-sequence seq_Q99973_v3 --start 901 --end 1015

# Trace a synthesized claim back to deduplicated evidence groups, observations, and mappings
uv run --locked python -m dufmech.sequence_reasoning --demo \
  --trace-claim claim_tep1_pf13271_nadase
```
