# Cycle 3 Stage 5 Remediation Issue Map (`resolve_review_findings`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `3`
- **Stage**: `5` (`resolve_review_findings`)
- **Revision**: `1`
- **Parent Stage 4 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-04/revision-0001/evidence.yaml` (`sha256: 8aebe6ef59eed207165de07b42f41a707192ebe1f137d3b54004dda4d91ee834`)
- **Stage 4 Closure Verification (`reviews/workflow/latest.yaml`)**: PR `#359` merged at `bd496e75654f5c7e8f76061da72f7e21eed98c8e` (`sha256: 38a0632c538216f522929d0354b138ec9d1a190cb3b305a9f5c86a1dd1a5b889`)

## 1. GitHub Issue Deduplication Sweep

Before creating any GitHub issues, we swept all open and closed repository issues (`gh issue list -R CultureBotAI/DUFMech --state all --limit 400 --json number,title,state,labels,url`; 222 total issues, 40 open issues):

- Open `PF01977` issues `#217`, `#218`, and `#219` track literature/causal-extension follow-ups (`AnFdc` mechanism contexts, assay-label discrepancies, and additional member coverage) rather than `ShVdcCD` partner-node grounding.
- Closed issue `#360` tracked the PR `#359` review fixes during Cycle 3 Stage 4.
- None of the 40 open issues or 182 closed issues covered the 4 Cycle 3 Stage 4 `missing_content` partner-grounding findings (`pf01174-pdxst-partner-and-acivicin-nodes-missing-grounding`, `pf01680-joint-pdx1-pdx2-nodes-missing-partner-grounding`, `pf01867-cas2-partner-and-complex-nodes-missing-grounding`, `pf01977-shvdccd-cognate-partner-and-l182v-missing-partner-grounding`).
- Accordingly, four new GitHub issues (`#361`, `#362`, `#363`, `#364`) were created—one per family overlay / repair-ownership group—linking the immutable Stage 4 structured review bundles and workflow evidence.

## 2. Finding Grouping, Issue Mapping, and Dispositions

| Group ID | Finding ID | Target Family | Stage 4 Review Bundle | GitHub Issue | Root Cause & Repair Ownership | Disposition | Successor Stage 5 Review Bundle |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `c3s5-pf01174-grounding` | `pf01174-pdxst-partner-and-acivicin-nodes-missing-grounding` | `PF01174` (`SNO`, `EX_DUF` `DUF91`) | `reviews/structured/20261025T132021Z-pf01174-c3s4-record-review/review.yaml` | [#361](https://github.com/CultureBotAI/DUFMech/issues/361) | Heteromeric `YaaD`/`PdxS` (`UniProtKB:P37527`) + `YaaE`/`PdxT` (`UniProtKB:P37528`) PLP synthase reaction and acivicin inhibition nodes in `curation/families/PF01174.yaml` omitted `UniProtKB:P37527` or node `grounding` (`PMID:16030023`). Repaired in `curation/families/PF01174.yaml` and projected to `data/families/PF01174.yaml`. | `resolved` | `reviews/structured/20261025T161300Z-pf01174-c3s5-remediation-review/review.yaml` |
| `c3s5-pf01680-grounding` | `pf01680-joint-pdx1-pdx2-nodes-missing-partner-grounding` | `PF01680` (`SOR_SNZ`, `EX_DUF` `UPF0019`) | `reviews/structured/20261025T132031Z-pf01680-c3s4-record-review/review.yaml` | [#362](https://github.com/CultureBotAI/DUFMech/issues/362) | Joint `Pdx1`/`PdxS` (`UniProtKB:P37527`) + `Pdx2`/`PdxT` (`UniProtKB:P37528`) complex nodes in 4 `PF01680` graphs grounded to only one subunit (`PMID:16030023`, `PMID:17189272`). Repaired in `curation/families/PF01680.yaml` and projected to `data/families/PF01680.yaml`. | `resolved` | `reviews/structured/20261025T161310Z-pf01680-c3s5-remediation-review/review.yaml` |
| `c3s5-pf01867-grounding` | `pf01867-cas2-partner-and-complex-nodes-missing-grounding` | `PF01867` (`Cas_Cas1`, `EX_DUF` `DUF48`) | `reviews/structured/20261025T132039Z-pf01867-c3s4-record-review/review.yaml` | [#363](https://github.com/CultureBotAI/DUFMech/issues/363) | Joint `Cas1` (`UniProtKB:Q46896`) + `Cas2` (`UniProtKB:P45956`) complex nodes and `cas2-deletion` in 4 `PF01867` graphs omitted `UniProtKB:P45956` (`PMID:25707795`, `PMID:24793649`). Repaired in `curation/families/PF01867.yaml` and projected to `data/families/PF01867.yaml`. | `resolved` | `reviews/structured/20261025T161320Z-pf01867-c3s5-remediation-review/review.yaml` |
| `c3s5-pf01977-grounding` | `pf01977-shvdccd-cognate-partner-and-l182v-missing-partner-grounding` | `PF01977` (`UbiD`, `EX_DUF` `DUF117`) | `reviews/structured/20261025T132055Z-pf01977-c3s4-record-review/review.yaml` | [#364](https://github.com/CultureBotAI/DUFMech/issues/364) | Joint `ShVdcCD` (`ShC` `UniProtKB:Q9S4M7` + `ShD` `UniProtKB:Q4R102`) complex nodes in 3 `PF01977` graphs grounded to only one subunit (`PMID:34417452`). Repaired in `curation/families/PF01977.yaml` and projected to `data/families/PF01977.yaml`. | `resolved` | `reviews/structured/20261025T161330Z-pf01977-c3s5-remediation-review/review.yaml` |

## 3. Detailed Node-Level Remediation Summary

### Group 1 (`#361`): `PF01174` (`curation/families/PF01174.yaml`)
- `pdxst-glutamine-dependent-plp-product` (`PMID:16030023`, `NCBITaxon:224308`): node `joint-pdxst-glutamine-carbohydrate-reaction` (`ACTIVITY`) updated from `[UniProtKB:P37528]` to `[UniProtKB:P37527, UniProtKB:P37528]`.
- `pdxt-ribulose-ammonium-dependent-synthase-readout` (`PMID:16030023`, `NCBITaxon:224308`): node `add-yaae-ribulose-ammonium` (`PERTURBATION`) updated from `[UniProtKB:P37528]` to `[UniProtKB:P37527, UniProtKB:P37528]`.
- `pdxt-acivicin-glutaminase-inhibition` (`PMID:16030023`, `NCBITaxon:224308`): node `acivicin-pretreat-glutaminase-mixture` (`PERTURBATION`) grounded to `[UniProtKB:P37527, UniProtKB:P37528]` and node `acivicin-assay-glutaminase-readout` (`ACTIVITY`) updated from `[UniProtKB:P37528]` to `[UniProtKB:P37527, UniProtKB:P37528]`.
- `pdxst-acivicin-plp-signal-inhibition` (`PMID:16030023`, `NCBITaxon:224308`): nodes `acivicin-pretreat-plp-mixture` (`PERTURBATION`) and `residual-glutamine-plp-signal` (`ACTIVITY`) grounded to `[UniProtKB:P37527, UniProtKB:P37528]`.
- History sidecar: `history/records/PF01174/2026-10-25T160800Z-antigravity-c3s5a1.yaml`.

### Group 2 (`#362`): `PF01680` (`curation/families/PF01680.yaml`)
- `pdxs-partner-glutaminase-readout` (`PMID:16030023`, `NCBITaxon:224308`): node `add-pdxs-to-pdxt-glutamine` (`PERTURBATION`) updated from `[UniProtKB:P37527]` to `[UniProtKB:P37527, UniProtKB:P37528]`.
- `pdxs-ribulose-partner-effect` (`PMID:16030023`, `NCBITaxon:224308`): node `add-pdxt-ribulose-ammonium` (`PERTURBATION`) updated from `[UniProtKB:P37528]` to `[UniProtKB:P37527, UniProtKB:P37528]`.
- `pdxs-chromophore-and-partner-h170n` (`PMID:17189272`, `NCBITaxon:224308`): node `joint-chromophore-reconstitution` (`ACTIVITY`) updated from `[UniProtKB:P37527]` to `[UniProtKB:P37527, UniProtKB:P37528]`.
- `pdxs-joint-phosphate-release` (`PMID:17189272`, `NCBITaxon:224308`): node `joint-r5p-phosphate-reaction` (`ACTIVITY`) updated from `[UniProtKB:P37527]` to `[UniProtKB:P37527, UniProtKB:P37528]`.
- History sidecar: `history/records/PF01680/2026-10-25T160810Z-antigravity-c3s5a2.yaml`.

### Group 3 (`#363`): `PF01867` (`curation/families/PF01867.yaml`)
- `cas1-cas2-purified-integration` (`PMID:25707795`, `NCBITaxon:83333`): node `joint-reaction` (`ACTIVITY`) updated from `[UniProtKB:Q46896]` to `[UniProtKB:Q46896, UniProtKB:P45956]`; node `cas2-deletion` (`PERTURBATION`) grounded to `[UniProtKB:P45956]`.
- `cas2-enhancement-in-manganese` (`PMID:25707795`, `NCBITaxon:83333`): node `add-cas2` (`PERTURBATION`) updated from `[UniProtKB:Q46896]` to `[UniProtKB:Q46896, UniProtKB:P45956]`.
- `cas1-cas2-cellular-acquisition` (`PMID:24793649`, `NCBITaxon:83333`): node `coexpress-cas1-cas2` (`PERTURBATION`) updated from `[UniProtKB:Q46896]` to `[UniProtKB:Q46896, UniProtKB:P45956]`.
- `cas1-r252e-lysate-coisolation` (`PMID:24793649`, `NCBITaxon:83333`): node `r252e` (`PERTURBATION`) updated from `[UniProtKB:Q46896]` to `[UniProtKB:Q46896, UniProtKB:P45956]`; node `cas2-recovery` (`PHENOTYPE`) grounded to `[UniProtKB:Q46896, UniProtKB:P45956]`.
- History sidecar: `history/records/PF01867/2026-10-25T160820Z-antigravity-c3s5a3.yaml`.

### Group 4 (`#364`): `PF01977` (`curation/families/PF01977.yaml`)
- `shvdccd-cognate-partner-2021` (`PMID:34417452`, `NCBITaxon:29345`): node `add_d` (`PERTURBATION`) updated from `[UniProtKB:Q4R102]` to `[UniProtKB:Q9S4M7, UniProtKB:Q4R102]`.
- `shvdccd-l182v-syringate-2021` (`PMID:34417452`, `NCBITaxon:29345`): node `l182v` (`PERTURBATION`) updated from `[UniProtKB:Q9S4M7]` to `[UniProtKB:Q9S4M7, UniProtKB:Q4R102]`.
- `shvdccd-domain-closure-model-2021` (`PMID:34417452`, `NCBITaxon:29345`): nodes `closure_int2` (`PROCESS`), `strained_int2` (`STATE`), and `quinoid` (`STATE`) updated from `[UniProtKB:Q9S4M7]` to `[UniProtKB:Q9S4M7, UniProtKB:Q4R102]`.
- History sidecar: `history/records/PF01977/2026-10-25T160830Z-antigravity-c3s5a4.yaml`.

## 4. Unresolved Blockers

- **Unresolved findings**: `0` (all 4 carried-forward Cycle 3 Stage 4 findings are resolved and verified by fresh successor structured reviews).
