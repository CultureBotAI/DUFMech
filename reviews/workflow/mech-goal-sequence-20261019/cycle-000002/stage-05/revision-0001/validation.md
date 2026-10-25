# Stage 5 Grouped Remediation Validation Report (`mech-goal-sequence-20261019`, Cycle 2, Stage 5)

## Native Writer & Projection Regeneration

All three Stage 4 carried-forward findings (`pf01923-sepduo-and-seeutt-assays-missing-protein-grounding`, `pf01934-fhepta-native-cfu-uniprot-grounding-and-cleavage-nodes`, `pf01982-pyrbkr-effectors-and-temperature-grounding`) were remediated in their authoritative `curation/families/*.yaml` overlays, backed by append-only canonical `EDIT` history sidecars, and projected through native writers without hand-editing generated records:

1. **Canonical History Validation (`python -m dufmech.history check`)**:
   - Appended:
     - `history/records/PF01923/2026-10-25T052900Z-antigravity-674c5b.yaml` (Issue `#347`)
     - `history/records/PF01934/2026-10-25T052910Z-antigravity-75b3fc.yaml` (Issue `#348`)
     - `history/records/PF01982/2026-10-25T052920Z-antigravity-557286.yaml` (Issue `#349`)
   - Result: `{"valid_history": 459}` (exit code `0`).

2. **Family Record Projection (`python -m dufmech.records --apply` and `--check`)**:
   - Regenerated `data/families/PF01923.yaml`, `data/families/PF01934.yaml`, `data/families/PF01982.yaml`, and `data/families/manifest.json`.
   - Result: `8296 schema-valid records; 4 generated files differ (applied)` and `8296 schema-valid records; generated projections current` (exit code `0`).

3. **Causal Graph Inventory & Exports (`python -m dufmech.causal_graphs --apply` and `python -m dufmech.exports --apply`)**:
   - Regenerated `reports/causal_graphs/inventory.json` and `reports/causal_graphs/summary.md` (`Refreshed 8296 family inventory rows`).
   - Verified `exports current` (exit code `0`).
   - Across all 141 maintained overlays (`1,234` causal graphs total), `PF01923`, `PF01934`, and `PF01982` now have `0` causal graphs lacking `taxon` and `0` causal graphs lacking grounded gene/protein nodes.

4. **Fresh Successor Structured Reviews (`scripts/record_review.py check --require-reviews --base main` and `python -m dufmech.reviews check`)**:
   - Saved versioned successor structured review bundles:
     - `reviews/structured/20261025T053500Z-pf01923-c2s5-remediation-review/review.yaml` (and `review.md`)
     - `reviews/structured/20261025T053505Z-pf01934-c2s5-remediation-review/review.yaml` (and `review.md`)
     - `reviews/structured/20261025T053510Z-pf01982-c2s5-remediation-review/review.yaml` (and `review.md`)
   - Each successor bundle links its immutable Stage 4 predecessor (`20261023T092550Z-pf01923-c2s4-record-review`, `20261023T092556Z-pf01934-c2s4-record-review`, `20261023T092608Z-pf01982-c2s4-record-review`), binds the updated `dufmech-record-content-v1` semantic digest and byte-exact projection quote, preserves open scientific follow-ups (`status: open`), and transitions the remediated grounding finding to `status: resolved` with an explicit `disposition_reason` and `previous_occurrences`.
   - Result: `{"coverage": "declared_scopes_only", "repository": "CultureBotAI/DUFMech", "valid_reviews": 251}` and `{"valid_reports": 259}` (exit code `0`).
