# Cycle 3 Stage 5 Remediation Validation Report (`resolve_review_findings`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `3`
- **Stage**: `5` (`resolve_review_findings`)
- **Revision**: `1`

## 1. Native Writers & Validation Gates Executed

1. **Family Record Regeneration & Check**:
   - `uv run --locked python -m dufmech.records --apply` -> `8296 schema-valid records; 5 generated files differ (applied)` (`data/families/PF01174.yaml`, `data/families/PF01680.yaml`, `data/families/PF01867.yaml`, `data/families/PF01977.yaml`, `reports/curation_progress.md`).
   - `uv run --locked python -m dufmech.records --check` -> `8296 schema-valid records; 0 generated files differ`.
2. **Causal Graph Inventory Regeneration & Check**:
   - `uv run --locked python -m dufmech.causal_graphs --apply` -> `Refreshed 8296 family inventory rows`.
   - `uv run --locked python -m dufmech.causal_graphs --check` -> `8296 family inventory rows match canonical records`.
3. **Curation History Validation**:
   - `uv run --locked python -m dufmech.history check` -> `{"valid_history": 488}`.
4. **Structured Review & Record Review Gate Validation**:
   - `uv run --locked python -m dufmech.reviews check` -> passed with 0 errors across all structured reviews, including the 4 new Cycle 3 Stage 5 successor review bundles (`20261025T161300Z-pf01174-c3s5-remediation-review`, `20261025T161310Z-pf01680-c3s5-remediation-review`, `20261025T161320Z-pf01867-c3s5-remediation-review`, `20261025T161330Z-pf01977-c3s5-remediation-review`).
   - `uv run --locked python scripts/record_review.py check` -> passed (`status: ok`).
   - Immutability check: all 14 Cycle 3 Stage 4 structured review bundles (`20261025T1320*-c3s4-*`) retain their exact Stage 4 SHA-256 digests (`PF01174` `1d2126bbc8bb290973977e93154b95e7ba2d2e4b331339cb34006f40a5cf6778`, `PF01680` `07fa82e88766e9314a0e491c1d54d2af52acc361b8836fd522238780c04a0994`, `PF01867` `1e280e9fab049abe25829c2b2fb4c2cf5661fbec2fd4447b4ae0763156a59819`, `PF01977` `635047f3e529caa0f63248183e764bbe7eeab3d020d94895b94afdbbc787740d`).
5. **Workflow Evidence Validation**:
   - `uv run --locked kg_microbe_workflows validate-evidence --root . --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-04/revision-0001/evidence.yaml --required-output issue_map --required-output validation reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-05/revision-0001/evidence.yaml` -> passed.

## 2. Remediated Artifact Digests

| Artifact Path | SHA-256 |
| --- | --- |
| `curation/families/PF01174.yaml` | `2213ec77323fb195edb69548f53795442a888937acd0c8ff03d65384ca52d439` |
| `data/families/PF01174.yaml` | `7910a29b72de114b7c30e62265ccd75fdfe84a16766fe07302ae628d9fa740bc` |
| `history/records/PF01174/2026-10-25T160800Z-antigravity-c3s5a1.yaml` | `ad7b0bc6c71bca73778302d3217e89ea48ee8fc38e6b068a638838ce25ca021a` |
| `reviews/structured/20261025T161300Z-pf01174-c3s5-remediation-review/review.yaml` | `2e0501ffd1fb8928b88024a608cc9a64be0bac52dbd2b47d2089e68fec97f004` |
| `curation/families/PF01680.yaml` | `893c2d48948ee283667dfd2d841f50f111eb5e0e645f3838e990c976e657c5fa` |
| `data/families/PF01680.yaml` | `2c4a5792c323f4b692224b5477b251786e44e90ad2dbf1fa534c53896bef70c4` |
| `history/records/PF01680/2026-10-25T160810Z-antigravity-c3s5a2.yaml` | `14d9aad37085496638676c998fa6200577e1b25a30d5edbc3769f8b18fd77d13` |
| `reviews/structured/20261025T161310Z-pf01680-c3s5-remediation-review/review.yaml` | `30e9a989625a9dafaee771ec64781ee65a5a3dbd22c8b71ac52fb6a3a9457bef` |
| `curation/families/PF01867.yaml` | `b0504f7681579c19eab07b07cbdc8094d4a050cf73352ef1dceaca15af934a14` |
| `data/families/PF01867.yaml` | `7854bd7a109bbd864ef95c0217ba53f020c8bd18a94c1dd84af50ce8189949b8` |
| `history/records/PF01867/2026-10-25T160820Z-antigravity-c3s5a3.yaml` | `6b33b17be3b7912957e09d4798a4cc9c0f09d8a59a00c5be7acfc9102c30c0be` |
| `reviews/structured/20261025T161320Z-pf01867-c3s5-remediation-review/review.yaml` | `4b06cb509d347e2afec826d7d9a456e8d39dade6fca158506638da808ba7eed9` |
| `curation/families/PF01977.yaml` | `76e72aee773737d7bb8d813f3e44db8829dd5a7d73f5745c55708ba402d88506` |
| `data/families/PF01977.yaml` | `8404df8c88527a22f6be5dff0e2e708b1987036604e1ea61dc1a5c1c980337b8` |
| `history/records/PF01977/2026-10-25T160830Z-antigravity-c3s5a4.yaml` | `0dcd1bbdeea700d6aa89367b59baefa4ae1bc09b8ca6e336e378e0d6bc9ca4a5` |
| `reviews/structured/20261025T161330Z-pf01977-c3s5-remediation-review/review.yaml` | `bdbca30db9d1141cc2151ba4040c66cfb8b523f31ad3531f07a6c2501f8e72e9` |
| `reports/causal_graphs/inventory.json` | `11501dec9375751a60b49df1a11f52ddee256107744127784e5310a2d1045f05` |
| `reviews/workflow/latest.yaml` | `38a0632c538216f522929d0354b138ec9d1a190cb3b305a9f5c86a1dd1a5b889` |
