# Stage 4 Record and Cohort Review Report (Cycle 1)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 1, Stage 4 (`record_review`)
- **Repository**: `CultureBotAI/DUFMech`
- **Git Base Revision**: `d658f73e7e618d3938704cdb9c86597bf47fc15e`
- **Frozen Snapshot**: `data/worklists/interpro-pfam-duf-2026-10-10.manifest.json` (8,296 total Pfam records)
- **Maintained Overlays Evaluated**: 141 / 141 (`curation/families/PF*.yaml`; 134 graph-bearing across 942 causal graphs, 7 source-limited without causal graphs)
- **New Structured Reviews Saved in Stage 4**: 18 bundles (17 `kind: record` + 1 `kind: category` cohort review in `reviews/structured/`, bringing total tracked structured reviews in `reviews/structured/` to 223)

## 1. Frozen Inventory & Coverage Accounting

| Population Segment | Count | Stage 4 Review Disposition |
| --- | ---: | --- |
| Cycle 1 Stage 2 causal-graph updated overlays (`PF01680`, `PF01934`, `PF01935`, `PF01936`, `PF01938`, `PF01939`, `PF01951`) | 7 | Saved new versioned per-record structured reviews (`kind: record`) + included in 17-member cohort category review (`kind: category`); Stage 2 partner/substrate UniProtKB groundings verified (`supported`). |
| Cycle 1 Stage 3 protein-grounding updated overlays (`PF01732`, `PF01865`, `PF01875`, `PF01914`, `PF01931`, `PF01956`, `PF01977`) | 7 | Saved new versioned per-record structured reviews (`kind: record`) + included in 17-member cohort category review (`kind: category`); Stage 3 partner/substrate UniProtKB groundings verified (`supported`). |
| Maintained overlays with newly identified Stage 4 open grounding/taxon findings (`PF01980`, `PF01985`, `PF02410`) | 3 | Saved new versioned per-record structured reviews (`kind: record`) + included in 17-member cohort category review (`kind: category`); 3 actionable minor findings recorded with `status: open` and carried forward to Stage 5 (`resolve_review_findings`). |
| Remaining maintained overlays with causal graphs (unchanged in Cycle 1, zero new defects) | 117 | Audited against frozen snapshot and retained per-record structured reviews in `reviews/structured/`; every causal graph has grounded protein nodes and valid provenance (`frozen_inventory_coverage.json`). |
| Maintained source-limited overlays without causal graphs (`PF00473`, `PF01698`, `PF01718`, `PF01810`, `PF01860`, `PF01888`, `PF01919`) | 7 | Audited against frozen snapshot and retained per-record structured reviews in `reviews/structured/`; explicit `NOT_AVAILABLE` / `INFERRED_UNCHANGED` source-limited rationales remain accurate. |
| Snapshot-only `SEED` projections without maintained overlays | 8,155 | Validated via `just records --check`; require primary experimental literature curation before mechanism graph construction. |
| **Total Frozen Snapshot Population** | **8,296** | **100% accounted for in `frozen_inventory_coverage.json`** |

## 2. Newly Saved Stage 4 Structured Review Bundles

| Target | Kind | Structured Review Bundle | Verdict | Native Verdict | Summary of Stage 4 Audit |
| --- | --- | --- | --- | --- | --- |
| `PF01680` | `record` | `reviews/structured/20261021T114801Z-pf01680-stage4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01680 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01732` | `record` | `reviews/structured/20261021T114803Z-pf01732-stage4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01732 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01865` | `record` | `reviews/structured/20261021T114805Z-pf01865-stage4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01865 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01875` | `record` | `reviews/structured/20261021T114807Z-pf01875-stage4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01875 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01914` | `record` | `reviews/structured/20261021T114809Z-pf01914-stage4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01914 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01931` | `record` | `reviews/structured/20261021T114811Z-pf01931-stage4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01931 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01934` | `record` | `reviews/structured/20261021T114813Z-pf01934-stage4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01934 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01935` | `record` | `reviews/structured/20261021T114815Z-pf01935-stage4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01935 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01936` | `record` | `reviews/structured/20261021T114817Z-pf01936-stage4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01936 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01938` | `record` | `reviews/structured/20261021T114819Z-pf01938-stage4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01938 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01939` | `record` | `reviews/structured/20261021T114821Z-pf01939-stage4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01939 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01951` | `record` | `reviews/structured/20261021T114823Z-pf01951-stage4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01951 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01956` | `record` | `reviews/structured/20261021T114825Z-pf01956-stage4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01956 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01977` | `record` | `reviews/structured/20261021T114827Z-pf01977-stage4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01977 Stage 4 frozen-inventory causal-graph and grounding review |
| `PF01980` | `record` | `reviews/structured/20261021T114829Z-pf01980-stage4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01980 Stage 4 frozen-inventory record review and grounding audit |
| `PF01985` | `record` | `reviews/structured/20261021T114831Z-pf01985-stage4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF01985 Stage 4 frozen-inventory record review and grounding audit |
| `PF02410` | `record` | `reviews/structured/20261021T114833Z-pf02410-stage4-record-review/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | PF02410 Stage 4 frozen-inventory record review and grounding audit |
| `17-family cohort` | `category` | `reviews/structured/20261021T114845Z-cycle1-causal-graph-and-grounding-cohort/review.yaml` | `pass_with_limitations` | `NEEDS_FOLLOWUP` | Cycle 1 causal-graph and protein-grounding cohort category review |

## 3. Cohort Boundary Decisions (`kind: category`)

- **Action**: `retain` across all 17 cohort members (`PF01680`, `PF01732`, `PF01865`, `PF01875`, `PF01914`, `PF01931`, `PF01934`, `PF01935`, `PF01936`, `PF01938`, `PF01939`, `PF01951`, `PF01956`, `PF01977`, `PF01980`, `PF01985`, `PF02410`).
- **Rationale**: Each Pfam entry represents a distinct evolutionary domain family anchored to an immutable InterPro/Pfam accession and distinct biochemical/cellular mechanism. Within each family overlay, separate experimental assays (biochemical reconstitution, genetic deletion/complementation, domain truncation, localization/reporter readouts) remain separated into distinct `CausalGraph` entries rather than lumped into unsupported cross-assay chains.

## 4. Open Actionable Findings Preserved for Stage 5 (`resolve_review_findings`)

Three actionable `minor` findings were identified during the Stage 4 audit of all 141 maintained overlays and are preserved as `status: open` in both the native structured reviews (`reviews/structured/`) and the Stage 4 parent workflow manifest (`carry_forward_ids`) for grouped remediation in Stage 5:

1. **`pf02410-media-shift-graph-missing-taxon`** (`curation/families/PF02410.yaml`): Causal graph `ecoli-rsfs-deletion-media-shift` models whole-gene `b0637` (`rsfS`, `UniProtKB:P0AAT6`, JW5090) deletion in *Escherichia coli* BW25113 derivatives (`NCBITaxon:83333`) from Hauser et al. 2012 (`PMID:22829778`), but omits `taxon: NCBITaxon:83333` even though sibling graph `ecoli-rsfs-preassociation` in the same overlay explicitly specifies `taxon: NCBITaxon:83333`.
2. **`pf01980-ecoli-trmo-graphs-missing-taxon-and-thr-variant-grounding`** (`curation/families/PF01980.yaml`): Ten *Escherichia coli* TrmO (`YaeB`, `UniProtKB:P28634`) causal graphs from Kimura et al. 2014 (`PMID:24875475`) omit `taxon: NCBITaxon:83333` even though `family_mapping` pins `Escherichia coli` to `NCBITaxon:83333` (`UniProtKB:P28634`), and two graphs (`ectrmo-thr3-identity-loss-2014` and `ectrmo-thr4-identity-gain-2014`) omit `UniProtKB:P28634` grounding on their `signal` (`ACTIVITY`) nodes (`m6t6A37 methylation activity by EcTrmO`).
3. **`pf01985-mcrs1-retention-state-nodes-missing-q9fyt6-grounding`** (`curation/families/PF01985.yaml`): Two *Zea mays* mCRS1 (`UniProtKB:Q9FYT6`, `NCBITaxon:4577`) causal graphs (`maize-mcrs1-magnesium-retention-2005` and `maize-mcrs1-rna-deletions-2005`, PMID:16143104) omit `UniProtKB:Q9FYT6` grounding on their mature CRS1-bound RNA retention `STATE` nodes (`retained-rna`, `d1-retention`, `d4-retention`, `loop-retention`).
