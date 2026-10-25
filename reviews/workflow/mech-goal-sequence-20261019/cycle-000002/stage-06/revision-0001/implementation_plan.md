# DUFMech Cycle 2 Stage 6 (`infrastructure`) Implementation Plan

## 1. Frozen Intake Scope

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `2`
- **Stage**: `6` (`infrastructure`)
- **Cutoff timestamp (`frozen_at`)**: `2026-10-25T07:04:09Z`
- **Frozen `INFRA_TASKS.md` snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/infra_snapshot.md`
- **Frozen `INFRA_TASKS.md` SHA-256**: `81980542d697234a109bc4cc55554aec064d1434928ad57d0ef86af30793b0d3`
- **Task count at cutoff**: `2`
  - `dufmech-infra-0001`: `resolved` in Cycle `1` Stage `6` ([CultureBotAI/DUFMech#333](https://github.com/CultureBotAI/DUFMech/issues/333))
  - `dufmech-infra-0002`: `open` at cutoff ([CultureBotAI/DUFMech#341](https://github.com/CultureBotAI/DUFMech/issues/341))

| Task ID | Originating Cycle / Goal | GitHub Issue | Status at Cutoff | Selected Action in Cycle 2 Stage 6 |
|---|---|---|---|---|
| `dufmech-infra-0001` | `mech-goal-sequence-20261019` / Cycle 1 / Stage 3 (`protein_examples`, `goal-2456`) | [CultureBotAI/DUFMech#333](https://github.com/CultureBotAI/DUFMech/issues/333) | `resolved` | Retained as resolved from Cycle 1 Stage 6 (`PR #340`). |
| `dufmech-infra-0002` | `mech-goal-sequence-20261019` / Cycle 2 / Stage 1 (`add_records`) | [CultureBotAI/DUFMech#341](https://github.com/CultureBotAI/DUFMech/issues/341) | `open` | Implement worklist short-name/name alignment with `pfam_history.py` (`UNKNOWN_NAME_RE`), `UPF\d{4}` unknown-function classification, and multi-query `DUF`/`UPF` harvesting in `src/dufmech/worklist.py`, `src/dufmech/cli.py`, and `src/dufmech/snapshot_cli.py`, plus unit tests in `tests/test_duf_puf_worklist.py`. |

## 2. Dependency & Design Analysis for `dufmech-infra-0002` ([#341](https://github.com/CultureBotAI/DUFMech/issues/341))

### 2.1 Root Cause of the Two Harvester/Classifier Boundary Gaps
During the Cycle 2 Stage 1 (`add_records`) bounded-frontier discovery audit across the InterPro Pfam API (`search=DUF` and `search=UPF`) and Pfam 38.2 previous-identifier history (`data/worklists/pfam-previous-unknown-names-2026-10-10.json`), two gaps were identified in `src/dufmech/worklist.py`:

1. **Underscore-joined `DUF` short names (`PF21084` `WHD_DUF4423_like`)**:
   - `src/dufmech/pfam_history.py` defines `UNKNOWN_NAME_RE = re.compile(r"(?:[A-Za-z0-9]+[_-])*(?:DUF(?:DUF)?_?[A-Z]?\d+|UPF\d{4})(?:[_-][A-Za-z0-9]+)*")` and marks `PF21084` (`WHD_DUF4423_like`, previous name `DUF4423_like`) as `currently_unknown_name: true`, so `src/dufmech/exduf.py` (`plan_migration`) skips `PF21084` assuming the parent worklist already retains it.
   - However, `src/dufmech/worklist.py` used `DUF_SHORT_NAME_RE = re.compile(r"\bDUF\d+\b", re.IGNORECASE)`, where `_` is a regex word character (`\w`). Because `PF21084`'s long `name` (`"Winged Helix-turn-helix domain"`) and `description` do not repeat `DUF4423`, `worklist.py` classified `PF21084` as `FALSE_POSITIVE_TEXT_HIT` and dropped it.
2. **Currently-named `UPF\d{4}` families (`PF03649` `UPF0014`)**:
   - `src/dufmech/pfam_history.py` includes `UPF\d{4}` when Pfam has renamed a family away from `UPF\d{4}` (`EX_DUF`), but `src/dufmech/worklist.py` (`DUF_SHORT_NAME_RE`) only matched `DUF\d+` and `InterProPfamClient.iter_entries()` only queried `search=DUF`.
   - Furthermore, InterPro names uncharacterised `UPF\d{4}` families `"Uncharacterised protein family (UPF0014)"` (using `"uncharacterised"` rather than `"unknown function"`), while `search=UPF` also returns 4 genuine false-positive gene-name hits (`PF01455` `HupF_HypC`, `PF03467` `Smg4_UPF3`, `PF04050` `Upf2`, `PF09416` `UPF1_Zn_bind`, plus `PF24722` `UPF1_1B_dom`).

### 2.2 Backward-Compatibility & Replay Constraints
- `tests/test_reclassify.py::test_correction_matches_published_records_without_rewriting_snapshots` replays `reclassify_snapshot(..., classifier_policy=LEGACY_CLASSIFIER_POLICY)` (`"unknown-function-metadata-v2"`) on `data/worklists/interpro-pfam-duf-2026-10-01.json` and verifies byte-for-byte identity against `data/worklists/interpro-pfam-duf-2026-10-05.json` (`1,621` status transitions, `2,101` reason changes).
  - Under `LEGACY_CLASSIFIER_POLICY`, `122` underscore-joined short names in `2026-10-01.json` (such as `QueG_DUF1730`, `DUF3458_C`, `DUF1285_N`) recorded `name_matches_duf` rather than `short_name_matches_duf`.
  - Therefore, `LEGACY_DUF_SHORT_NAME_RE = re.compile(r"\bDUF\d+\b", re.IGNORECASE)` must be preserved when `classifier_policy == LEGACY_CLASSIFIER_POLICY`, while `CLASSIFIER_POLICY` (`"unknown-function-metadata-v3"`) uses the aligned non-alphanumeric-bounded regexes.
- `tests/test_reclassify.py::test_current_corpus_historical_labels_are_fixed_without_metadata_or_evidence_changes` replays `reclassify_worklist` under `CLASSIFIER_POLICY` on `data/worklists/interpro-pfam-duf-2026-10-08.json` and verifies that `score_families` characterization status transitions match `historical | still_unknown`.
  - In `2026-10-08.json`, `PF03690` (`MYG1_exonuc`, an `EX_DUF` renamed from `UPF0160`) retains `name: "Uncharacterised protein family (UPF0160)"` even though its short name is `MYG1_exonuc` and its description characterizes it as a 3'-5' exonuclease.
  - Gating `UNCHARACTERIZED_UPF_NAME_RE` and `UNCHARACTERIZED_UPF_DESCRIPTION_RE` on `is_current_upf_short_name` (`bool(UPF_SHORT_NAME_RE.search(short_name))`) ensures that currently-named `UPF\d{4}` families like `PF03649` (`short_name: "UPF0014"`, `name: "Uncharacterised protein family (UPF0014)"`) are classified as `UNKNOWN_CANDIDATE`, while renamed `EX_DUF` families like `PF03690` (`short_name: "MYG1_exonuc"`) keep their exact characterization status.

### 2.3 Implementation Steps
1. **Align `src/dufmech/worklist.py` classification**:
   - Define `DUF_SHORT_NAME_RE = re.compile(r"(?<![A-Za-z0-9])(?:DUF(?:DUF)?_?[A-Z]?\d+|UPF\d{4})(?![A-Za-z0-9])", re.IGNORECASE)` and `DUF_NAME_RE = re.compile(r"(?<![A-Za-z0-9])DUF(?:DUF)?_?[A-Z]?\d+(?![A-Za-z0-9])", re.IGNORECASE)` for `CLASSIFIER_POLICY`, while retaining `LEGACY_DUF_SHORT_NAME_RE = re.compile(r"\bDUF\d+\b", re.IGNORECASE)` for `LEGACY_CLASSIFIER_POLICY`.
   - Define `UPF_SHORT_NAME_RE`, `UNCHARACTERIZED_UPF_NAME_RE`, and `UNCHARACTERIZED_UPF_DESCRIPTION_RE` so currently-named `UPF\d{4}` families with `"Uncharacterised protein family"` metadata receive `name_says_unknown_function` / `description_says_unknown_function` (`UNKNOWN_CANDIDATE`), functionally characterized `UPF\d{4}` short names receive `KNOWN_HISTORICAL_DUF`, and non-4-digit `UPF1`/`UPF2`/`UPF3`/`HupF` gene names receive `FALSE_POSITIVE_TEXT_HIT`.
2. **Add multi-query `DUF`/`UPF` harvesting**:
   - Add `DEFAULT_SEARCH = "DUF"`, `DEFAULT_WORKLIST_SEARCHES = ("DUF", "UPF")`, `normalize_search_terms(search)`, and `InterProPfamClient.iter_worklist_entries()` in `src/dufmech/worklist.py`.
   - Extend `InterProPfamClient.iter_entries(search=...)` to accept a single term, comma-separated terms (`"DUF,UPF"`), or a sequence of terms (`("DUF", "UPF")`), while preserving `search="DUF"` as the default.
   - Add `--include-upf` (and comma-separated `--search` normalization) to `src/dufmech/cli.py` and `src/dufmech/snapshot_cli.py`.
3. **Add unit tests in `tests/test_duf_puf_worklist.py`**:
   - Test `PF21084` (`WHD_DUF4423_like`) under both `CLASSIFIER_POLICY` (`KNOWN_HISTORICAL_DUF`) and `LEGACY_CLASSIFIER_POLICY` (`FALSE_POSITIVE_TEXT_HIT`).
   - Test `PF03649` (`UPF0014`) as `UNKNOWN_CANDIDATE` and characterized `UPF0054` (`RimP`) as `KNOWN_HISTORICAL_DUF`.
   - Test exclusion of `PF01455` (`HupF_HypC`), `PF03467` (`Smg4_UPF3`), `PF04050` (`Upf2`), `PF09416` (`UPF1_Zn_bind`), and `PF24722` (`UPF1_1B_dom`) as `FALSE_POSITIVE_TEXT_HIT`.
   - Test `InterProPfamClient.iter_worklist_entries()` and `normalize_search_terms()` across `("DUF", "UPF")` with deduplication in `collect_worklist`.

## 3. Acceptance Criteria
1. `uv run python -m pytest` passes across the entire repository test suite, including `tests/test_duf_puf_worklist.py`, `tests/test_duf_puf_snapshot.py`, `tests/test_reclassify.py`, `tests/test_reclassify_worklist.py`, `tests/test_exduf.py`, `tests/test_pfam_history.py`, `tests/test_upf1_migration_release.py`, and `tests/test_exports.py`.
2. `uv run ruff check src/dufmech/worklist.py src/dufmech/cli.py src/dufmech/snapshot_cli.py tests/test_duf_puf_worklist.py` passes with zero lint findings.
3. `INFRA_TASKS.md` machine-readable inventory parses cleanly via `kg_microbe_workflows.infra.read_infra_notebook`, and `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/evidence.yaml` validates cleanly via `kg_microbe_workflows validate-evidence`.
