# Stage 5 Grouped Remediation Validation Report (`mech-goal-sequence-20261019`, Cycle 1, Stage 5)

## Native Writer & Projection Regeneration

All three Stage 4 carried-forward findings (`pf02410-media-shift-graph-missing-taxon`, `pf01980-ecoli-trmo-graphs-missing-taxon-and-thr-variant-grounding`, `pf01985-mcrs1-retention-state-nodes-missing-q9fyt6-grounding`) were remediated in their authoritative `curation/families/*.yaml` overlays, backed by append-only canonical `EDIT` history sidecars, and projected through native writers without hand-editing generated records:

1. **Canonical History Validation (`python -m dufmech.history check`)**:
   - Appended:
     - `history/records/PF02410/2026-10-21T133500Z-antigravity-a13360.yaml` (Issue `#336`)
     - `history/records/PF01980/2026-10-21T133501Z-antigravity-a13370.yaml` (Issue `#337`)
     - `history/records/PF01985/2026-10-21T133502Z-antigravity-a13380.yaml` (Issue `#338`)
   - Result: `{"valid_history": 437}` (exit code `0`).

2. **Family Record Projection (`python -m dufmech.records --apply` and `--check`)**:
   - Regenerated `data/families/PF02410.yaml`, `data/families/PF01980.yaml`, `data/families/PF01985.yaml`, and `data/families/manifest.json`.
   - Result: `8296 schema-valid records; 4 generated files differ (applied)` (exit code `0`).

3. **Causal Graph Inventory & Exports (`python -m dufmech.causal_graphs --apply` and `python -m dufmech.exports --apply`)**:
   - Regenerated `reports/causal_graphs/inventory.json` and `reports/causal_graphs/summary.md` (`Refreshed 8296 family inventory rows`).
   - Verified `exports current` (exit code `0`).
   - Across all 141 maintained overlays (`1,020` causal graphs total), `PF02410`, `PF01980`, and `PF01985` now have `0` causal graphs lacking `taxon` and `0` causal graphs lacking grounded gene/protein nodes.

4. **Fresh Successor Structured Reviews (`scripts/record_review.py check` and `python -m dufmech.reviews check`)**:
   - Saved versioned successor structured review bundles:
     - `reviews/structured/20261021T134500Z-pf02410-stage5-remediation-review/review.yaml` (and `review.md`)
     - `reviews/structured/20261021T134501Z-pf01980-stage5-remediation-review/review.yaml` (and `review.md`)
     - `reviews/structured/20261021T134502Z-pf01985-stage5-remediation-review/review.yaml` (and `review.md`)
   - Each successor bundle links its immutable Stage 4 predecessor (`20261021T114833Z-pf02410-stage4-record-review`, `20261021T114829Z-pf01980-stage4-record-review`, `20261021T114831Z-pf01985-stage4-record-review`), binds the updated `dufmech-record-content-v1` semantic digest and byte-exact projection quote, preserves open scientific follow-ups (`status: open`), and transitions the remediated grounding/taxon finding to `status: resolved` with an explicit `disposition_reason` and `previous_occurrences`.
   - Result: `{"coverage": "declared_scopes_only", "repository": "CultureBotAI/DUFMech", "valid_reviews": 227}` and `Total validated reviews: 235` (exit code `0`).
