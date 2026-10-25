# Stage 4 Record and Cohort Review Report (Cycle 3)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 3, Stage 4 (`record_review`)
- **Repository**: `CultureBotAI/DUFMech`
- **Git Base Revision**: `0e26e9cdab5214d838db4f53ddefbf83772241fb`
- **Frozen Snapshot**: `data/worklists/interpro-pfam-duf-2026-10-10.manifest.json` (8,296 total Pfam records)
- **Maintained Overlays Evaluated**: 141 / 141 (`curation/families/PF*.yaml`; 134 graph-bearing across 942 causal graphs, 7 source-limited without causal graphs)
- **New Structured Reviews Saved in Stage 4**: 25 bundles (24 `kind: record` + 1 `kind: category` cohort review in `reviews/structured/`, bringing total tracked structured reviews in `reviews/structured/` to 276)

## 1. Frozen Inventory & Coverage Accounting

| Population Segment | Count | Stage 4 Review Disposition |
| --- | ---: | --- |
| Cycle 3 Stage 2 causal-graph updated overlays (`PF01026`, `PF01062`, `PF01121`, `PF01168`, `PF01554`, `PF01861`) | 6 (1 shared with Stage 3: `PF01861`) | Saved new versioned per-record structured reviews (`kind: record`) + included in 24-member cohort category review (`kind: category`); Stage 2 `PR #355` (`c73e2cff9e`) catalytic, transport, and peptide-adduct readout node groundings across 9 causal graphs verified (`supported`). |
| Cycle 3 Stage 3 protein-grounding updated overlays (`PF01060`, `PF01174`, `PF01493`, `PF01638`, `PF01661`, `PF01680`, `PF01732`, `PF01861`, `PF01864`, `PF01867`, `PF01868`, `PF01870`, `PF01875`, `PF01899`, `PF01927`, `PF01970`, `PF01973`, `PF01977`, `PF01978`) | 19 (1 shared with Stage 2: `PF01861`) | Saved new versioned per-record structured reviews (`kind: record`) + included in 24-member cohort category review (`kind: category`); Stage 3 `PR #357` (`0e26e9cdab`) 36 causal-graph protein/gene/complex node groundings across 31 causal graphs verified (`supported`), and open partner-protein grounding findings on `PF01174`, `PF01680`, and `PF01977` recorded for Stage 5. |
| Remaining maintained overlays with causal graphs (unchanged in Cycle 3, zero new defects) | 110 | Audited against frozen snapshot and retained per-record structured reviews in `reviews/structured/`; every causal graph has grounded protein nodes and valid provenance (`frozen_inventory_coverage.json`). |
| Maintained source-limited overlays without causal graphs (`PF01629`, `PF01724`, `PF01886`, `PF01954`, `PF01976`, `PF02621`, `PF20352`) | 7 | Audited against frozen snapshot and retained per-record structured reviews in `reviews/structured/`; explicit `NOT_AVAILABLE` / `INFERRED_UNCHANGED` source-limited rationales remain accurate. |
| Snapshot-only `SEED` projections without maintained overlays | 8,155 | Validated via `just records --check`; require primary experimental literature curation before mechanism graph construction. |
| **Total Frozen Snapshot Population** | **8,296** | **100% accounted for in `frozen_inventory_coverage.json`** |

## 2. Newly Saved Stage 4 Structured Review Bundles

| Target | Kind | Structured Review Bundle | Verdict | Native Verdict | Summary of Stage 4 Audit |
| --- | --- | --- | --- | --- | --- |
| `PF01026` | `record` | `reviews/structured/20261025T132011Z-pf01026-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01026 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01060` | `record` | `reviews/structured/20261025T132013Z-pf01060-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01060 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01062` | `record` | `reviews/structured/20261025T132015Z-pf01062-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01062 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01121` | `record` | `reviews/structured/20261025T132017Z-pf01121-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01121 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01168` | `record` | `reviews/structured/20261025T132019Z-pf01168-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01168 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01174` | `record` | `reviews/structured/20261025T132021Z-pf01174-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01174 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01493` | `record` | `reviews/structured/20261025T132023Z-pf01493-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01493 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01554` | `record` | `reviews/structured/20261025T132025Z-pf01554-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01554 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01638` | `record` | `reviews/structured/20261025T132027Z-pf01638-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01638 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01661` | `record` | `reviews/structured/20261025T132029Z-pf01661-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01661 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01680` | `record` | `reviews/structured/20261025T132031Z-pf01680-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01680 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01732` | `record` | `reviews/structured/20261025T132033Z-pf01732-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01732 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01861` | `record` | `reviews/structured/20261025T132035Z-pf01861-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01861 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01864` | `record` | `reviews/structured/20261025T132037Z-pf01864-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01864 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01867` | `record` | `reviews/structured/20261025T132039Z-pf01867-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01867 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01868` | `record` | `reviews/structured/20261025T132041Z-pf01868-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01868 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01870` | `record` | `reviews/structured/20261025T132043Z-pf01870-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01870 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01875` | `record` | `reviews/structured/20261025T132045Z-pf01875-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01875 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01899` | `record` | `reviews/structured/20261025T132047Z-pf01899-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01899 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01927` | `record` | `reviews/structured/20261025T132049Z-pf01927-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01927 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01970` | `record` | `reviews/structured/20261025T132051Z-pf01970-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01970 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01973` | `record` | `reviews/structured/20261025T132053Z-pf01973-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01973 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01977` | `record` | `reviews/structured/20261025T132055Z-pf01977-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01977 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01978` | `record` | `reviews/structured/20261025T132057Z-pf01978-c3s4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01978 Cycle 3 Stage 4 frozen-inventory causal-graph and grounding review |
| `24-family cohort` | `category` | `reviews/structured/20261025T132115Z-cycle3-causal-graph-and-grounding-cohort/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | Cycle 3 causal-graph and protein-grounding cohort category review |

## 3. Cohort Boundary Decisions (`kind: category`)

- **Action**: `retain` across all 24 cohort members (`PF01026`, `PF01060`, `PF01062`, `PF01121`, `PF01168`, `PF01174`, `PF01493`, `PF01554`, `PF01638`, `PF01661`, `PF01680`, `PF01732`, `PF01861`, `PF01864`, `PF01867`, `PF01868`, `PF01870`, `PF01875`, `PF01899`, `PF01927`, `PF01970`, `PF01973`, `PF01977`, `PF01978`).
- **Rationale**: Each Pfam entry represents a distinct evolutionary domain family anchored to an immutable InterPro/Pfam accession and distinct biochemical/cellular mechanism. Within each family overlay, separate experimental assays (biochemical reconstitution, mutagenesis/kinetic series, dynamic light scattering, ITC/NMR/EMSAs, whole-operon deletion/complementation) remain separated into distinct `CausalGraph` entries rather than lumped into unsupported cross-assay chains.

## 4. Open Actionable Findings Preserved for Stage 5 (`resolve_review_findings`)

Three actionable `minor` findings were identified during the Stage 4 audit of all 141 maintained overlays and are preserved as `status: open` in both the native structured reviews (`reviews/structured/`) and the Stage 4 parent workflow manifest (`carry_forward_ids`) for grouped remediation in Stage 5:

1. **`pf01174-pdxst-partner-and-acivicin-nodes-missing-grounding`** (`curation/families/PF01174.yaml`): Two *Bacillus subtilis* 168 (`NCBITaxon:224308`) causal graphs omit verified YaaD/PdxS (`UniProtKB:P37527`) and/or YaaE/PdxT (`UniProtKB:P37528`) protein grounding established in `family_mapping` and sibling graphs: `pdxst-glutamine-dependent-plp-product` node `joint-pdxst-glutamine-carbohydrate-reaction` (lines 56-60) grounds only to `[UniProtKB:P37528]` and omits partner `UniProtKB:P37527`, and `pdxst-acivicin-plp-signal-inhibition` node `acivicin-pretreat-plp-mixture` (lines 155-157) omits `grounding: [UniProtKB:P37527, UniProtKB:P37528]`.
2. **`pf01680-joint-pdx1-pdx2-nodes-missing-partner-grounding`** (`curation/families/PF01680.yaml`): Two *Bacillus subtilis* 168 (`NCBITaxon:224308`) joint Pdx1/Pdx2 reconstitution and reaction nodes ground only to Pdx1 (`UniProtKB:P37527`) and omit the co-present partner Pdx2 (`UniProtKB:P37528`): `pdxs-chromophore-and-partner-h170n` node `joint-chromophore-reconstitution` (lines 261-265) and `pdxs-joint-phosphate-release` node `joint-r5p-phosphate-reaction` (lines 387-391).
3. **`pf01977-shvdccd-cognate-partner-and-l182v-missing-partner-grounding`** (`curation/families/PF01977.yaml`): Three *Sedimentibacter hydroxybenzoicus* ShVdcCD (`NCBITaxon:29345`; ShC `UniProtKB:Q9S4M7`, ShD `UniProtKB:Q4R102`) causal graphs ground only one subunit of the two-protein ShCD complex on nodes that explicitly represent the joint ShCD reconstitution or holocomplex: `shvdccd-cognate-partner-2021` node `add_d` (lines 1237-1241) omits `UniProtKB:Q9S4M7`, `shvdccd-l182v-syringate-2021` node `l182v` (lines 1783-1787) omits `UniProtKB:Q4R102`, and `shvdccd-domain-closure-model-2021` nodes `closure_int2`, `strained_int2`, and `quinoid` (lines 1825-1839) omit `UniProtKB:Q4R102`.
