# DUFMech Cycle 2 Stage 6 (`infrastructure`) Validation Report

## 1. Scope Verified

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `2`, **Stage**: `6` (`infrastructure`)
- **Task**: `dufmech-infra-0002` ([CultureBotAI/DUFMech#341](https://github.com/CultureBotAI/DUFMech/issues/341)) — *Include currently-named `UPF\d{4}` Pfam families and underscore-joined DUF short names (`PF21084` `WHD_DUF4423_like`) in worklist harvesting*
- **Prior resolved task retained**: `dufmech-infra-0001` ([CultureBotAI/DUFMech#333](https://github.com/CultureBotAI/DUFMech/issues/333))
- **Frozen `INFRA_TASKS.md` snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/infra_snapshot.md` (`sha256: 81980542d697234a109bc4cc55554aec064d1434928ad57d0ef86af30793b0d3`, `frozen_at: 2026-10-25T07:04:09Z`)

## 2. Automated Test & Lint Gates

### 2.1 Targeted Worklist, Reclassification, and History Suites
- **Command**:
  ```bash
  uv run python -m pytest tests/test_duf_puf_worklist.py tests/test_duf_puf_snapshot.py tests/test_reclassify.py tests/test_reclassify_worklist.py tests/test_exduf.py tests/test_pfam_history.py tests/test_upf1_migration_release.py
  ```
- **Result**: `127 passed` (`52 passed` in `tests/test_duf_puf_worklist.py`, `3 passed` in `tests/test_duf_puf_snapshot.py`, `20 passed` in `tests/test_reclassify.py`, `6 passed` in `tests/test_reclassify_worklist.py`, `18 passed` in `tests/test_exduf.py`, `25 passed` in `tests/test_pfam_history.py`, `4 passed` in `tests/test_upf1_migration_release.py`).
- **New unit tests verified in `tests/test_duf_puf_worklist.py`**:
  1. `test_underscore_joined_duf_short_name_and_upf_four_digit_families_are_classified`:
     - `PF21084` (`short_name="WHD_DUF4423_like"`, `name="Winged Helix-turn-helix domain"`) classifies as `KNOWN_HISTORICAL_DUF` (`("short_name_matches_duf",)`) under `CLASSIFIER_POLICY` and replays as `FALSE_POSITIVE_TEXT_HIT` under `LEGACY_CLASSIFIER_POLICY`.
     - `PF03649` (`short_name="UPF0014"`, `name="Uncharacterised protein family (UPF0014)"`) classifies as `UNKNOWN_CANDIDATE` (`("short_name_matches_duf", "name_says_unknown_function", "description_says_unknown_function")`).
     - `PF01709` (`short_name="UPF0054"`, `name="Ribosome maturation protein RimP"`) classifies as `KNOWN_HISTORICAL_DUF` (`("short_name_matches_duf",)`).
  2. `test_non_four_digit_upf_and_hupf_gene_names_are_dropped_as_false_positives`:
     - Verifies `PF01455` (`HupF_HypC`), `PF03467` (`Smg4_UPF3`), `PF04050` (`Upf2`), `PF09416` (`UPF1_Zn_bind`), and `PF24722` (`UPF1_1B_dom`) classify as `FALSE_POSITIVE_TEXT_HIT` and are dropped by `collect_worklist(...)`.
  3. `test_interpro_client_iter_worklist_entries_combines_duf_and_upf_queries`:
     - Verifies `InterProPfamClient.iter_worklist_entries()` queries `("DUF", "UPF")`, deduplicates overlapping entries (`PF21084`), retains `PF03649` (`UNKNOWN_CANDIDATE`) and `PF21084` (`KNOWN_HISTORICAL_DUF`), and drops `PF09416` (`UPF1_Zn_bind`).
  4. `test_normalize_search_terms_handles_comma_separated_and_sequence_inputs`:
     - Verifies `normalize_search_terms` handles single terms, comma-separated strings (`"DUF, UPF, DUF"`), and sequences while rejecting empty search specifications.

### 2.2 Ruff Lint Check
- **Command**:
  ```bash
  uv run --no-sync python -m ruff check src/dufmech/worklist.py src/dufmech/cli.py src/dufmech/snapshot_cli.py tests/test_duf_puf_worklist.py
  ```
- **Result**: `All checks passed!` (`0` findings).

## 3. Ledger & Workflow Evidence Validation

- **Frozen Snapshot Hash Check**:
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/infra_snapshot.md` matches the supervisor-frozen `status.json` `infra_scope.sha256` (`81980542d697234a109bc4cc55554aec064d1434928ad57d0ef86af30793b0d3`).
- **`INFRA_TASKS.md` Machine-Readable Block**:
  - Validated with `kg_microbe_workflows.infra.read_infra_notebook(Path("INFRA_TASKS.md"))`: both `dufmech-infra-0001` ([CultureBotAI/DUFMech#333](https://github.com/CultureBotAI/DUFMech/issues/333)) and `dufmech-infra-0002` ([CultureBotAI/DUFMech#341](https://github.com/CultureBotAI/DUFMech/issues/341)) are `status: resolved` with non-empty dispositions.
- **Workflow Evidence Manifest (`evidence.yaml`)**:
  - Validated with `kg_microbe_workflows validate-evidence --workflow-file /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/dufmech/effective-workflow.json --evidence-file reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/evidence.yaml --repo-root /Users/marcin/Documents/VIMSS/ontology/Mechs/DUFMech`.
