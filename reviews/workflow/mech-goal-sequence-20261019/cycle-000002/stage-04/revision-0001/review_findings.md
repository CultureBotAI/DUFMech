# Stage 4 Unresolved Review Findings for Stage 5 Grouped Remediation (Cycle 2)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 2, Stage 4 (`record_review`)
- **Carry-Forward Count**: 3 open findings (`severity: minor`, `status: open`)

## 1. `pf01923-sepduo-and-seeutt-assays-missing-protein-grounding`

- **Target**: `curation/families/PF01923.yaml` (`data/families/PF01923.yaml`)
- **Structured Review Bundles**:
  - `reviews/structured/20261023T092550Z-pf01923-c2s4-record-review/review.yaml`
  - `reviews/structured/20261023T092618Z-cycle2-causal-graph-and-grounding-cohort/review.yaml`
- **Severity / Status**: `minor` / `open`
- **Evidence**: In `curation/families/PF01923.yaml`, `sepduo-inhibition-2004` (`activity`: `AdoCbl-forming activity`, lines 335-337) and `sepduo-metal-additions-2004` (`activity`: `AdoCbl-forming activity`, lines 420-422) model *Salmonella enterica* LT2 PduO (`STM2050`, `UniProtKB:Q8ZNR5`, `NCBITaxon:99287`) in vitro assays from Johnson et al. 2004 (`PMID:15090527`) without `grounding: [UniProtKB:Q8ZNR5]`, and `seeutt-metal-oxygen-2014` (`activity`: `Coupled AdoCbl-forming activity`, lines 1207-1209) models *S. enterica* LT2 EutT (`STM2456`, `UniProtKB:Q9ZFV4`, `NCBITaxon:99287`) assays from Moore et al. 2014 (`PMID:25002542`) without `grounding: [UniProtKB:Q9ZFV4]`.
- **Proposed Stage 5 Action**: Add `grounding: [UniProtKB:Q8ZNR5]` to `activity` in `sepduo-inhibition-2004` and `sepduo-metal-additions-2004`, and `grounding: [UniProtKB:Q9ZFV4]` to `activity` in `seeutt-metal-oxygen-2014` in `curation/families/PF01923.yaml`, record a canonical `EDIT` history event, and regenerate `data/families/PF01923.yaml`.

## 2. `pf01934-fhepta-native-cfu-uniprot-grounding-and-cleavage-nodes`

- **Target**: `curation/families/PF01934.yaml` (`data/families/PF01934.yaml`)
- **Structured Review Bundles**:
  - `reviews/structured/20261023T092556Z-pf01934-c2s4-record-review/review.yaml`
  - `reviews/structured/20261023T092618Z-cycle2-causal-graph-and-grounding-cohort/review.yaml`
- **Severity / Status**: `minor` / `open`
- **Evidence**: In `curation/families/PF01934.yaml`, `fhepta-fragment-native-cfu-2026` (`fragment`, lines 585-603) grounds only to `[RefSeq:WP_164925653.1]` and omits `UniProtKB:Q8EGZ7` unlike sibling FhepTA136-276 graphs `fhepta-fragment-ecoli-cfu-2026` and `fhepta-fragment-rna-redox-2026`; additionally, `fhepta-fragment-rna-redox-2026` node `cleavage` (lines 771-773) and `so3166-modified-preparation-rnase-2020` node `cleavage` (lines 316-318) omit protein grounding (`[RefSeq:WP_164925653.1, UniProtKB:Q8EGZ7]` and `[UniProtKB:Q8ECH6]`, respectively).
- **Proposed Stage 5 Action**: Add `UniProtKB:Q8EGZ7` to `fragment` in `fhepta-fragment-native-cfu-2026`, ground `cleavage` in `fhepta-fragment-rna-redox-2026` to `[RefSeq:WP_164925653.1, UniProtKB:Q8EGZ7]`, and ground `cleavage` in `so3166-modified-preparation-rnase-2020` to `[UniProtKB:Q8ECH6]` in `curation/families/PF01934.yaml`, record a canonical `EDIT` history event, and regenerate `data/families/PF01934.yaml`.

## 3. `pf01982-pyrbkr-effectors-and-temperature-grounding`

- **Target**: `curation/families/PF01982.yaml` (`data/families/PF01982.yaml`)
- **Structured Review Bundles**:
  - `reviews/structured/20261023T092608Z-pf01982-c2s4-record-review/review.yaml`
  - `reviews/structured/20261023T092618Z-cycle2-causal-graph-and-grounding-cohort/review.yaml`
- **Severity / Status**: `minor` / `open`
- **Evidence**: In `curation/families/PF01982.yaml` (lines 705-812), *Pyrobaculum* sp. WP30 pyRbkR (`GenBank:AKT35049.1`) graphs `pyrbkr-flavin-binding-2017` (`fp`) and `pyrbkr-temperature-response-2017` (`activity`) omit `grounding: [GenBank:AKT35049.1]`, leaving both graphs with zero grounded protein nodes, and `myrbkr-effector-binding-2017` (*Methanocaldococcus vulcanius* M7 myRbkR, `UniProtKB:H2C8H2`, lines 616-640) omits `grounding: [UniProtKB:H2C8H2]` on `ribb` and `ribt`.
- **Proposed Stage 5 Action**: Add `grounding: [GenBank:AKT35049.1]` to `fp` in `pyrbkr-flavin-binding-2017` and `activity` in `pyrbkr-temperature-response-2017`, and `grounding: [UniProtKB:H2C8H2]` to `ribb` and `ribt` in `myrbkr-effector-binding-2017` in `curation/families/PF01982.yaml`, record a canonical `EDIT` history event, and regenerate `data/families/PF01982.yaml`.
