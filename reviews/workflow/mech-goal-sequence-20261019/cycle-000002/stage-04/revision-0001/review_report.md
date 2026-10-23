# Stage 4 Record and Cohort Review Report (Cycle 2)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 2, Stage 4 (`record_review`)
- **Repository**: `CultureBotAI/DUFMech`
- **Git Base Revision**: `fde7d143a6b952fbc63b390cbfc27de38ac7701b`
- **Frozen Snapshot**: `data/worklists/interpro-pfam-duf-2026-10-10.manifest.json` (8,296 total Pfam records)
- **Maintained Overlays Evaluated**: 141 / 141 (`curation/families/PF*.yaml`; 134 graph-bearing across 942 causal graphs, 7 source-limited without causal graphs)
- **New Structured Reviews Saved in Stage 4**: 21 bundles (20 `kind: record` + 1 `kind: category` cohort review in `reviews/structured/`, bringing total tracked structured reviews in `reviews/structured/` to 247)

## 1. Frozen Inventory & Coverage Accounting

| Population Segment | Count | Stage 4 Review Disposition |
| --- | ---: | --- |
| Cycle 2 Stage 2 causal-graph updated overlay (`PF01973`) | 1 | Saved new versioned per-record structured review (`kind: record`) + included in 20-member cohort category review (`kind: category`); Stage 2 `PR #343` (`2b49c87290`) `NCBITaxon:211586` (*Shewanella oneidensis* MR-1) taxonomy additions on all 18 native MR-1 causal graphs and UniProtKB `Q8EE60` grounding verified (`supported`). |
| Cycle 2 Stage 3 protein-grounding updated overlays (`PF01062`, `PF01345`, `PF01535`, `PF01638`, `PF01709`, `PF01895`, `PF01910`, `PF01918`, `PF01927`, `PF01930`, `PF01934`, `PF01938`, `PF01940`, `PF01978`, `PF01980`, `PF01982`, `PF01984`, `PF02583`) | 18 | Saved new versioned per-record structured reviews (`kind: record`) + included in 20-member cohort category review (`kind: category`); Stage 3 `PR #344` (`fde7d143a6`) 39 causal-graph partner/substrate/target UniProtKB node groundings across 18 families verified (`supported`), and open readout-node grounding findings on `PF01934` and `PF01982` recorded for Stage 5. |
| Additional maintained overlay with newly identified Stage 4 open protein-grounding finding (`PF01923`) | 1 | Saved new versioned per-record structured review (`kind: record`) + included in 20-member cohort category review (`kind: category`); open PduO/EutT assay grounding finding recorded with `status: open` and carried forward to Stage 5 (`resolve_review_findings`). |
| Remaining maintained overlays with causal graphs (unchanged in Cycle 2, zero new defects) | 114 | Audited against frozen snapshot and retained per-record structured reviews in `reviews/structured/`; every causal graph has grounded protein nodes and valid provenance (`frozen_inventory_coverage.json`). |
| Maintained source-limited overlays without causal graphs (`PF01629`, `PF01724`, `PF01886`, `PF01954`, `PF01976`, `PF02621`, `PF20352`) | 7 | Audited against frozen snapshot and retained per-record structured reviews in `reviews/structured/`; explicit `NOT_AVAILABLE` / `INFERRED_UNCHANGED` source-limited rationales remain accurate. |
| Snapshot-only `SEED` projections without maintained overlays | 8,155 | Validated via `just records --check`; require primary experimental literature curation before mechanism graph construction. |
| **Total Frozen Snapshot Population** | **8,296** | **100% accounted for in `frozen_inventory_coverage.json`** |

## 2. Newly Saved Stage 4 Structured Review Bundles

| Target | Kind | Structured Review Bundle | Verdict | Native Verdict | Summary of Stage 4 Audit |
| --- | --- | --- | --- | --- | --- |
| `PF01062` | `record` | `reviews/structured/20261023T092534Z-pf01062-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01062 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01345` | `record` | `reviews/structured/20261023T092536Z-pf01345-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01345 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01535` | `record` | `reviews/structured/20261023T092538Z-pf01535-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01535 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01638` | `record` | `reviews/structured/20261023T092540Z-pf01638-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01638 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01709` | `record` | `reviews/structured/20261023T092542Z-pf01709-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01709 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01895` | `record` | `reviews/structured/20261023T092544Z-pf01895-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01895 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01910` | `record` | `reviews/structured/20261023T092546Z-pf01910-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01910 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01918` | `record` | `reviews/structured/20261023T092548Z-pf01918-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01918 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01923` | `record` | `reviews/structured/20261023T092550Z-pf01923-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01923 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01927` | `record` | `reviews/structured/20261023T092552Z-pf01927-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01927 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01930` | `record` | `reviews/structured/20261023T092554Z-pf01930-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01930 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01934` | `record` | `reviews/structured/20261023T092556Z-pf01934-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01934 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01938` | `record` | `reviews/structured/20261023T092558Z-pf01938-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01938 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01940` | `record` | `reviews/structured/20261023T092600Z-pf01940-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01940 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01973` | `record` | `reviews/structured/20261023T092602Z-pf01973-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01973 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01978` | `record` | `reviews/structured/20261023T092604Z-pf01978-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01978 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01980` | `record` | `reviews/structured/20261023T092606Z-pf01980-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01980 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01982` | `record` | `reviews/structured/20261023T092608Z-pf01982-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01982 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01984` | `record` | `reviews/structured/20261023T092610Z-pf01984-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01984 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF02583` | `record` | `reviews/structured/20261023T092612Z-pf02583-c2s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF02583 Cycle 2 Stage 4 frozen-inventory causal-graph and grounding review |
| `20-family cohort` | `category` | `reviews/structured/20261023T092618Z-cycle2-causal-graph-and-grounding-cohort/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | Cycle 2 causal-graph and protein-grounding cohort category review |

## 3. Cohort Boundary Decisions (`kind: category`)

- **Action**: `retain` across all 20 cohort members (`PF01062`, `PF01345`, `PF01535`, `PF01638`, `PF01709`, `PF01895`, `PF01910`, `PF01918`, `PF01923`, `PF01927`, `PF01930`, `PF01934`, `PF01938`, `PF01940`, `PF01973`, `PF01978`, `PF01980`, `PF01982`, `PF01984`, `PF02583`).
- **Rationale**: Each Pfam entry represents a distinct evolutionary domain family anchored to an immutable InterPro/Pfam accession and distinct biochemical/cellular mechanism. Within each family overlay, separate experimental assays (biochemical reconstitution, genetic deletion/complementation, domain truncation, localization/reporter readouts) remain separated into distinct `CausalGraph` entries rather than lumped into unsupported cross-assay chains.

## 4. Open Actionable Findings Preserved for Stage 5 (`resolve_review_findings`)

Three actionable `minor` findings were identified during the Stage 4 audit of all 141 maintained overlays and are preserved as `status: open` in both the native structured reviews (`reviews/structured/`) and the Stage 4 parent workflow manifest (`carry_forward_ids`) for grouped remediation in Stage 5:

1. **`pf01923-sepduo-and-seeutt-assays-missing-protein-grounding`** (`curation/families/PF01923.yaml`): Three *Salmonella enterica* LT2 (`NCBITaxon:99287`) biochemical causal graphs (`sepduo-inhibition-2004`, `sepduo-metal-additions-2004`, and `seeutt-metal-oxygen-2014`) have zero grounded protein nodes because their AdoCbl-forming `activity` (`STATE`) nodes omit `grounding: [UniProtKB:Q8ZNR5]` (PduO) and `grounding: [UniProtKB:Q9ZFV4]` (EutT), despite explicit `family_mapping` and sibling graph groundings in `curation/families/PF01923.yaml`.
2. **`pf01934-fhepta-native-cfu-uniprot-grounding-and-cleavage-nodes`** (`curation/families/PF01934.yaml`): Causal graph `fhepta-fragment-native-cfu-2026` grounds `fragment` (`Induce FhepTA136-276 rather than vector`) only to `[RefSeq:WP_164925653.1]` and omits `UniProtKB:Q8EGZ7` unlike sibling FhepTA136-276 graphs (`fhepta-fragment-ecoli-cfu-2026` and `fhepta-fragment-rna-redox-2026`), and the RNase readout nodes `fhepta-fragment-rna-redox-2026.nodes[3]` (`cleavage`) and `so3166-modified-preparation-rnase-2020.nodes[1]` (`cleavage`) omit protein grounding (`[RefSeq:WP_164925653.1, UniProtKB:Q8EGZ7]` and `[UniProtKB:Q8ECH6]`, respectively).
3. **`pf01982-pyrbkr-effectors-and-temperature-grounding`** (`curation/families/PF01982.yaml`): Two *Pyrobaculum* sp. WP30 pyRbkR (`GenBank:AKT35049.1`) causal graphs (`pyrbkr-flavin-binding-2017` node `fp` and `pyrbkr-temperature-response-2017` node `activity`) omit `grounding: [GenBank:AKT35049.1]`, leaving both graphs with zero grounded protein nodes, and `myrbkr-effector-binding-2017` (*Methanocaldococcus vulcanius* M7 myRbkR, `UniProtKB:H2C8H2`) omits `grounding: [UniProtKB:H2C8H2]` on its DNA-binding FP readout nodes (`ribb` and `ribt`).
