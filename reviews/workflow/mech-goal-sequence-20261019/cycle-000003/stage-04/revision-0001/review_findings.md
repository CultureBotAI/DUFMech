# Stage 4 Unresolved Review Findings for Stage 5 Grouped Remediation (Cycle 3)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 3, Stage 4 (`record_review`)
- **Carry-Forward Count**: 3 open findings (`severity: minor`, `status: open`)

## 1. `pf01174-pdxst-partner-and-acivicin-nodes-missing-grounding`

- **Target**: `curation/families/PF01174.yaml` (`data/families/PF01174.yaml`)
- **Structured Review Bundles**:
  - `reviews/structured/20261025T132021Z-pf01174-c3s4-record-review/review.yaml`
  - `reviews/structured/20261025T132115Z-cycle3-causal-graph-and-grounding-cohort/review.yaml`
- **Severity / Status**: `minor` / `open`
- **Evidence**: In `curation/families/PF01174.yaml`, two *Bacillus subtilis* 168 (`NCBITaxon:224308`) causal graphs omit verified protein grounding that is explicitly established in `family_mapping` and sibling graphs: (1) in `pdxst-glutamine-dependent-plp-product` (lines 47-79), node `joint-pdxst-glutamine-carbohydrate-reaction` (`Joint YaaD, YaaE, glutamine, ribose 5-phosphate and DHAP reaction`, lines 56-60) grounds only to `[UniProtKB:P37528]` and omits partner YaaD/PdxS (`UniProtKB:P37527`), whereas sibling graph `pdxt-untagged-partner-dependent-glutaminase` grounds `add-yaad-to-yaae-glutamine` to `[UniProtKB:P37527, UniProtKB:P37528]`; and (2) in `pdxst-acivicin-plp-signal-inhibition` (lines 146-176), node `acivicin-pretreat-plp-mixture` (`Expose the YaaD/YaaE synthesis mixture to increasing acivicin`, lines 155-157) omits `grounding: [UniProtKB:P37527, UniProtKB:P37528]`.
- **Proposed Stage 5 Action**: Add `UniProtKB:P37527` to `joint-pdxst-glutamine-carbohydrate-reaction` in `pdxst-glutamine-dependent-plp-product` and `grounding: [UniProtKB:P37527, UniProtKB:P37528]` to `acivicin-pretreat-plp-mixture` in `pdxst-acivicin-plp-signal-inhibition` in `curation/families/PF01174.yaml`, record a canonical `EDIT` history event, and regenerate `data/families/PF01174.yaml`.

## 2. `pf01680-joint-pdx1-pdx2-nodes-missing-partner-grounding`

- **Target**: `curation/families/PF01680.yaml` (`data/families/PF01680.yaml`)
- **Structured Review Bundles**:
  - `reviews/structured/20261025T132031Z-pf01680-c3s4-record-review/review.yaml`
  - `reviews/structured/20261025T132115Z-cycle3-causal-graph-and-grounding-cohort/review.yaml`
- **Severity / Status**: `minor` / `open`
- **Evidence**: In `curation/families/PF01680.yaml`, two *Bacillus subtilis* 168 (`NCBITaxon:224308`) joint Pdx1/Pdx2 reconstitution and reaction nodes ground only to Pdx1 (`UniProtKB:P37527`) and omit the co-present partner Pdx2 (`UniProtKB:P37528`): (1) in `pdxs-chromophore-and-partner-h170n` (lines 244-309), node `joint-chromophore-reconstitution` (`Joint Pdx1, Pdx2, R5P and glutamine reconstitution`, lines 261-265) grounds only to `[UniProtKB:P37527]`, omitting `UniProtKB:P37528` even though sibling node `partner-h170n-preparation` in the same graph grounds to `[UniProtKB:P37528]`; and (2) in `pdxs-joint-phosphate-release` (lines 372-413), node `joint-r5p-phosphate-reaction` (`Joint Pdx1, Pdx2, glutamine and R5P reaction`, lines 387-391) grounds only to `[UniProtKB:P37527]`, omitting `UniProtKB:P37528` even though sibling graph `pdxs-joint-plp-product` (lines 69-74) grounds `joint-pdxst-reaction` to `[UniProtKB:P37527, UniProtKB:P37528]`.
- **Proposed Stage 5 Action**: Add `UniProtKB:P37528` to `joint-chromophore-reconstitution` in `pdxs-chromophore-and-partner-h170n` and to `joint-r5p-phosphate-reaction` in `pdxs-joint-phosphate-release` in `curation/families/PF01680.yaml`, record a canonical `EDIT` history event, and regenerate `data/families/PF01680.yaml`.

## 3. `pf01977-shvdccd-cognate-partner-and-l182v-missing-partner-grounding`

- **Target**: `curation/families/PF01977.yaml` (`data/families/PF01977.yaml`)
- **Structured Review Bundles**:
  - `reviews/structured/20261025T132055Z-pf01977-c3s4-record-review/review.yaml`
  - `reviews/structured/20261025T132115Z-cycle3-causal-graph-and-grounding-cohort/review.yaml`
- **Severity / Status**: `minor` / `open`
- **Evidence**: In `curation/families/PF01977.yaml`, three *Sedimentibacter hydroxybenzoicus* ShVdcCD (`NCBITaxon:29345`; ShC `UniProtKB:Q9S4M7`, ShD `UniProtKB:Q4R102`) causal graphs ground only one subunit of the two-protein ShCD complex on nodes that explicitly represent the joint ShCD reconstitution or holocomplex: (1) in `shvdccd-cognate-partner-2021` (lines 1223-1280), node `add_d` (`Add cognate ShD before C-prFMN-Mn reconstitution`, lines 1237-1241) grounds only to `[UniProtKB:Q4R102]` and omits `UniProtKB:Q9S4M7`, whereas sibling graph `bsvdccd-cognate-partner-2021` grounds `add_d` to both subunits `[UniProtKB:P94405, UniProtKB:C0H3U9]`; (2) in `shvdccd-l182v-syringate-2021` (lines 1767-1808), node `l182v` (`ShC L182V in reconstituted ShCD`, lines 1783-1787) grounds only to `[UniProtKB:Q9S4M7]` and omits partner ShD (`UniProtKB:Q4R102`); and (3) in `shvdccd-domain-closure-model-2021` (lines 1809-1897), nodes `closure_int2`, `strained_int2`, and `quinoid` (lines 1825-1839) ground only to `[UniProtKB:Q9S4M7]` and omit partner ShD (`UniProtKB:Q4R102`).
- **Proposed Stage 5 Action**: Add `UniProtKB:Q9S4M7` to `add_d` in `shvdccd-cognate-partner-2021`, and add `UniProtKB:Q4R102` to `l182v` in `shvdccd-l182v-syringate-2021` and `closure_int2`, `strained_int2`, and `quinoid` in `shvdccd-domain-closure-model-2021` in `curation/families/PF01977.yaml`, record a canonical `EDIT` history event, and regenerate `data/families/PF01977.yaml`.
