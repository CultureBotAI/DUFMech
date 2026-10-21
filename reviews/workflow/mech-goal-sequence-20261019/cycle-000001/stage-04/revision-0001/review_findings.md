# Stage 4 Unresolved Review Findings for Stage 5 Grouped Remediation

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 1, Stage 4 (`record_review`)
- **Carry-Forward Count**: 3 open findings (`severity: minor`, `status: open`)

## 1. `pf02410-media-shift-graph-missing-taxon`

- **Target**: `curation/families/PF02410.yaml` (`data/families/PF02410.yaml`)
- **Structured Review Bundles**:
  - `reviews/structured/20261021T114833Z-pf02410-stage4-record-review/review.yaml`
  - `reviews/structured/20261021T114845Z-cycle1-causal-graph-and-grounding-cohort/review.yaml`
- **Severity / Status**: `minor` / `open`
- **Evidence**: `curation/families/PF02410.yaml` lines 318-360 (`ecoli-rsfs-deletion-media-shift`) models `b0637` (`rsfS`, `UniProtKB:P0AAT6`, JW5090) deletion in *Escherichia coli* BW25113 (`NCBITaxon:83333`) from Hauser et al. 2012 (`PMID:22829778`), whereas `ecoli-rsfs-preassociation` (lines 286-317) explicitly records `taxon: NCBITaxon:83333`.
- **Proposed Stage 5 Action**: Add `taxon: NCBITaxon:83333` to `ecoli-rsfs-deletion-media-shift` in `curation/families/PF02410.yaml`, record a canonical `EDIT` history event, and regenerate `data/families/PF02410.yaml`.

## 2. `pf01980-ecoli-trmo-graphs-missing-taxon-and-thr-variant-grounding`

- **Target**: `curation/families/PF01980.yaml` (`data/families/PF01980.yaml`)
- **Structured Review Bundles**:
  - `reviews/structured/20261021T114829Z-pf01980-stage4-record-review/review.yaml`
  - `reviews/structured/20261021T114845Z-cycle1-causal-graph-and-grounding-cohort/review.yaml`
- **Severity / Status**: `minor` / `open`
- **Evidence**: In `curation/families/PF01980.yaml`, `family_mapping` maps *Escherichia coli* YaeB/TrmO to `NCBITaxon:83333` and `UniProtKB:P28634`. However, all ten Kimura et al. 2014 (`PMID:24875475`) *E. coli* TrmO causal graphs (`ectrmo-yaeb-knockout-2014`, `ectrmo-yaeb-complementation-2014`, `ectrmo-sam-methyltransfer-2014`, `ectrmo-thr3-identity-loss-2014`, `ectrmo-thr4-identity-gain-2014`, `ectrmo-t6a37-prerequisite-2014`, `ectrmo-cterminal-truncation-2014`, `ectrmo-catalytic-cys-variants-2014`, `ectrmo-sam-pocket-variants-2014`, `ectrmo-basic-patch-variants-2014`) omit `taxon: NCBITaxon:83333`, and `ectrmo-thr3-identity-loss-2014` and `ectrmo-thr4-identity-gain-2014` omit `protein_id: [UniProtKB:P28634]` on their `signal` (`ACTIVITY`) nodes (`m6t6A37 methylation activity by EcTrmO`).
- **Proposed Stage 5 Action**: Add `taxon: NCBITaxon:83333` to all ten Kimura 2014 *E. coli* TrmO causal graphs and add `protein_id: [UniProtKB:P28634]` to `signal` in `ectrmo-thr3-identity-loss-2014` and `ectrmo-thr4-identity-gain-2014` in `curation/families/PF01980.yaml`, record a canonical `EDIT` history event, and regenerate `data/families/PF01980.yaml`.

## 3. `pf01985-mcrs1-retention-state-nodes-missing-q9fyt6-grounding`

- **Target**: `curation/families/PF01985.yaml` (`data/families/PF01985.yaml`)
- **Structured Review Bundles**:
  - `reviews/structured/20261021T114831Z-pf01985-stage4-record-review/review.yaml`
  - `reviews/structured/20261021T114845Z-cycle1-causal-graph-and-grounding-cohort/review.yaml`
- **Severity / Status**: `minor` / `open`
- **Evidence**: In `curation/families/PF01985.yaml`, `maize-mcrs1-magnesium-retention-2005` (`retained-rna`, lines 491-494) and `maize-mcrs1-rna-deletions-2005` (`d1-retention`, `d4-retention`, `loop-retention`, lines 555-571) model retention of *atpF* domain-1/4/loop RNA by recombinant mature *Zea mays* CRS1 (`mCRS1`, `UniProtKB:Q9FYT6`, `NCBITaxon:4577`, Ostersetzer et al. 2005 `PMID:16143104`) on `STATE` nodes without `protein_id: [UniProtKB:Q9FYT6]` grounding.
- **Proposed Stage 5 Action**: Add `protein_id: [UniProtKB:Q9FYT6]` to `retained-rna` in `maize-mcrs1-magnesium-retention-2005` and to `d1-retention`, `d4-retention`, and `loop-retention` in `maize-mcrs1-rna-deletions-2005` in `curation/families/PF01985.yaml`, record a canonical `EDIT` history event, and regenerate `data/families/PF01985.yaml`.
