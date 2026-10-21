# Stage 6 Infrastructure Validation Report (`mech-goal-sequence-20261019`, Cycle 1)

## 1. Validated Task Summary

- **Task ID**: `dufmech-infra-0001`
- **Issue**: [CultureBotAI/DUFMech#333](https://github.com/CultureBotAI/DUFMech/issues/333)
- **Status**: `resolved`
- **Source Revision at Freeze**: `1795e5229d2d91cfdc34abe9e44838716587c1d8`
- **Cutoff Timestamp (`scope_frozen_at`)**: `2026-10-21T18:40:51Z`

## 2. Implementation & Corpus Verification

1. **`curation_overlay_mentions` & `curation_overlay_candidates` (`src/dufmech/protein_examples.py`)**:
   - Executed against all `141` `curation/families/PF*.yaml` overlays at `1795e5229d2d91cfdc34abe9e44838716587c1d8` and the `interpro-pfam-duf-2026-10-10` worklist (`8,296` families):
     - `overlays_inspected`: `141`
     - `families_with_mentions`: `138`
     - `mentions`: `306`
     - `unique_accessions`: `262` (`130` already present in `2026-10-13` lookup checkpoints; `132` queued for acquisition whenever a `protein_examples` snapshot refreshes with `--dufmech-repo` and `--dufmech-commit`).
2. **Unit & Regression Test Suite (`tests/test_protein_examples.py`)**:
   - Command: `.venv/bin/python -m pytest tests/test_protein_examples.py`
   - Result: `44 passed in 0.56s`
   - Verified:
     - `test_curation_overlay_harvests_member_groundings_skips_partners_and_flags_mismatched_claims`: promotes verified target-family groundings (`P0A8M6` in `PF04363`, `Q58031` in `PF00001`) to `examples` with immutable `DUFMech` commit/blob provenance, skips non-member interacting partner groundings (`P37528` in `PF04363`) without polluting `unresolved`, and flags mismatched `family_mapping` claims (`P99999` in `PF00002`) in `unresolved` (`PFAM_NOT_IN_CURRENT_ENTRY`).
     - `test_curation_overlay_requires_immutable_commit_and_worklist_membership`: rejects non-40-hex commits and out-of-worklist overlay families.
3. **Lint & Schema / Notebook Validation**:
   - Command: `.venv/bin/python -m ruff check --no-cache src scripts tests` -> `All checks passed!`
   - `kg_microbe_workflows.read_infra_notebook("INFRA_TASKS.md", "CultureBotAI/DUFMech")` -> passed (`dufmech-infra-0001` `status: resolved`, `issue_url: https://github.com/CultureBotAI/DUFMech/issues/333`).
   - `kg_microbe_workflows` `validate-evidence` on `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/evidence.yaml` -> passed.
