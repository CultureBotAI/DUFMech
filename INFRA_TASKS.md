# DUFMech infrastructure tasks

This versioned ledger collects repository requirements and upgrades discovered
during every goal. The workflow profile and its parent govern intake, stage 6
implementation, closure and cycle restart.

## Intake protocol

- Give each actionable task a stable ID such as `dufmech-infra-0001` and retain it
  across cycles. Record the originating run, cycle and goal, observation,
  desired outcome, evidence paths, priority, dependencies and status.
- Link each task to an actual issue in https://github.com/CultureBotAI/DUFMech/issues.
  Search existing open and closed issues before creating one. If access fails,
  retain an explicit pending-link blocker; never invent an issue number or URL.
- Preserve resolved and deferred entries with their issue, implementation PR,
  validation and disposition. Do not overwrite previous cycle evidence.
- At stage 6, freeze a bounded snapshot, write a dependency-aware plan and
  acceptance criteria, implement selected work, validate, and complete the
  commit sequence, write the closure receipt and stop; only the supervisor
  dispatches another goal. New arrivals after the cutoff enter the next cycle;
  never expand the frozen task-ID scope. A new blocking prerequisite requires
  an explicit deferred disposition for the selected task. Carry unfinished work
  forward explicitly.

## Machine-readable task inventory

This fenced mapping is the inventory stage 6 freezes and reconciles. Each task
uses `task_id`, `summary`, `status` (`note`, `open`, `deferred`, or `resolved`),
optional `issue_url`, and optional `disposition`. Status `note` may have a
pending issue link; all other statuses require a real issue URL. Keep richer
notes below keyed by the same stable task ID.

<!-- mech-infra-tasks:start -->
```yaml
schema_version: '1.0.0'
tasks:
  - task_id: dufmech-infra-0001
    summary: Include curated FamilyCuration UniProtKB accessions in protein_examples snapshots and FamilyRecord projection
    status: resolved
    issue_url: https://github.com/CultureBotAI/DUFMech/issues/333
    disposition: Implemented curation_overlay_mentions and curation_overlay_candidates in src/dufmech/protein_examples.py (with --dufmech-repo / --dufmech-commit CLI integration and unit tests in tests/test_protein_examples.py) and documented the governed FamilyRecord vs site-render projection boundary.
  - task_id: dufmech-infra-0002
    summary: Include currently-named UPF\d{4} Pfam families and underscore-joined DUF short names (PF21084 WHD_DUF4423_like) in worklist harvesting
    status: open
    issue_url: https://github.com/CultureBotAI/DUFMech/issues/341
```
<!-- mech-infra-tasks:end -->

## Tasks

### `dufmech-infra-0001` — Include curated `FamilyCuration` `UniProtKB` accessions in `protein_examples` snapshots and `FamilyRecord` projection

- **Originating run / cycle / goal**: `mech-goal-sequence-20261019`, cycle `1`, stage `3` (`protein_examples`, `goal-2456`)
- **Status**: `resolved`
- **Issue**: https://github.com/CultureBotAI/DUFMech/issues/333
- **Priority**: Medium
- **Dependencies**: None
- **Evidence paths**:
  - `src/dufmech/protein_examples.py`
  - `src/dufmech/protein_discovery.py`
  - `src/dufmech/schema/dufmech.yaml`
  - `tests/test_protein_examples.py`
  - `data/protein_examples/duf-protein-examples-direct-2026-10-13.json`
  - `curation/families/PF*.yaml`
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/implementation_plan.md`
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/validation.md`
- **Observation**:
  - Across the `141` curated `curation/families/PF*.yaml` overlays, `271` unique verified `UniProtKB:...` accessions are referenced in `causal_graphs[].nodes[].grounding` (`243` unique accessions) and `assertions` (`271` total unique). However, only `59` of those `271` experimentally curated `UniProtKB:...` accessions appear in `data/protein_examples/duf-protein-examples-direct-2026-10-13.json`, leaving `212` curated `UniProtKB:...` accessions absent from the retained `protein_examples` snapshot.
  - `src/dufmech/protein_examples.py` and `src/dufmech/protein_discovery.py` currently draw exclusively from sibling-Mech accession candidates (`data/cross_mech/`, covering `3,106` families) and top-3 annotation-score UniProt queries for `NO_SIBLING_CANDIDATE` families (`5,190` families), without harvesting or prioritizing the verified `UniProtKB:...` accessions curated in `curation/families/PF*.yaml`.
  - Additionally, `FamilyRecord` in `src/dufmech/schema/dufmech.yaml` has no slot or summary pointer for `protein_examples`, so generated `data/families/PF*.yaml` projections do not surface verified sequence examples directly on the family record.
- **Desired outcome**:
  - Extend `dufmech.protein_examples` / `dufmech.protein_discovery` candidate harvesting to include verified `UniProtKB:...` accessions curated in `curation/families/PF*.yaml` (`causal_graphs[].nodes[].grounding` and `assertions`) when matching the family's Pfam domain and organism scope.
  - Evaluate adding a governed read-only projection or pointer from `FamilyRecord` (`src/dufmech/schema/dufmech.yaml`) to verified `protein_examples` snapshot entries.
- **Resolution / Disposition** (`mech-goal-sequence-20261019`, cycle `1`, stage `6`):
  - **Implemented in `src/dufmech/protein_examples.py` and `tests/test_protein_examples.py`**:
    - Added `curation_overlay_mentions(repo, pin, families)` to harvest `UniProtKB:...` CURIEs and member-specific InterPro/UniProt reference URLs across pinned `curation/families/PF*.yaml` overlays (`causal_graphs.family_mapping`, `causal_graphs.nodes.grounding`, `assertions`, `assertions.evidence`, `discussions`, and `discussions.evidence`) at an immutable 40-hex `DUFMech` commit.
    - Added `curation_overlay_candidates(mentions, entries)` to filter harvested mentions against resolved UniProt entries: confirmed target-family carriers (`pfam_id in current["pfam_ids"]`) are promoted as `CURATED_MECHANISM_OVERLAY` candidates with immutable `DUFMech` commit/blob provenance; missing/isoform accessions and mismatched explicit `family_mapping`/identity claims surface in `unresolved`; and verified interacting partner node groundings belonging to other families are counted in `partner_or_non_member_pairs_skipped` without polluting target-family `unresolved` buckets.
    - Wired `--dufmech-repo`, `--dufmech-commit`, and `--dufmech-repository-url` into `dufmech.protein_examples.main()` and recorded `dufmech_curation_overlays` scope counts in snapshot manifests.
  - **Evaluated `FamilyRecord` (`src/dufmech/schema/dufmech.yaml`) projection boundary**:
    - `FamilyRecord` (`data/families/PF*.yaml`) validates strictly against `data/worklists/` (`SnapshotProvenance.path` pattern `^data/worklists/[A-Za-z0-9_-]+[.]json$`) and `curation/families/PF*.yaml` overlays, whereas `dufmech.pages.render_site` (`src/dufmech/pages.py`) and `dufmech.site` (`src/dufmech/site.py`) already join `data/protein_examples/` snapshots with `FamilyRecord` at site-render time into `pages/families/PF*.json`, `pages/families/PF*.html`, and `pages/families/PF*.fasta`. Keeping `data/protein_examples/` joined at the site/JSON projection layer avoids rewriting all `8,296` `data/families/PF*.yaml` records on every `protein_examples` snapshot refresh while preserving `evidence_scope: FAMILY_MEMBERSHIP_NOT_FUNCTION`.

### `dufmech-infra-0002` — Include currently-named `UPF\d{4}` Pfam families and underscore-joined DUF short names (`PF21084` `WHD_DUF4423_like`) in worklist harvesting

- **Originating run / cycle / goal**: `mech-goal-sequence-20261019`, cycle `2`, stage `1` (`add_records`)
- **Status**: `open`
- **Issue**: https://github.com/CultureBotAI/DUFMech/issues/341 (coordinates with https://github.com/CultureBotAI/DUFMech/issues/96)
- **Priority**: Medium
- **Dependencies**: Coordinate with [#96](https://github.com/CultureBotAI/DUFMech/issues/96) (`UPF0014` / `PF03649`)
- **Evidence paths**:
  - `src/dufmech/worklist.py`
  - `src/dufmech/pfam_history.py`
  - `src/dufmech/exduf.py`
  - `data/worklists/interpro-pfam-duf-2026-10-10.json`
  - `data/worklists/pfam-previous-unknown-names-2026-10-10.json`
  - `reports/cross-mech-duf-audit-2026-10-08.tsv`
  - `tests/test_exduf.py`
  - `tests/test_upf1_migration_release.py`
  - `tests/test_exports.py`
- **Observation**:
  - During the Cycle 2 Stage 1 (`add_records`) bounded-frontier discovery audit across the InterPro Pfam API (`search=DUF` and `search=UPF`) and Pfam 38.2 previous-identifier history (`data/worklists/pfam-previous-unknown-names-2026-10-10.json`), two worklist harvester/classifier boundary gaps were identified in `src/dufmech/worklist.py`:
    1. `src/dufmech/pfam_history.py` (`UNKNOWN_NAME_RE = re.compile(r"(?:[A-Za-z0-9]+[_-])*(?:DUF(?:DUF)?_?[A-Z]?\d+|UPF\d{4})(?:[_-][A-Za-z0-9]+)*")`) includes `UPF\d{4}` when Pfam has *renamed* a family away from `UPF\d{4}` in `#=GF PI` (`84` `EX_DUF` families in `data/worklists/interpro-pfam-duf-2026-10-10.json`). However, `src/dufmech/worklist.py` (`InterProPfamClient.iter_entries(search="DUF")` and `DUF_SHORT_NAME_RE = re.compile(r"\bDUF\d+\b", re.IGNORECASE)`) only queries `search=DUF` and only matches `DUF\d+` in short names. Consequently, `86` Pfam 38.2 families that are *still* named `UPF\d{4}` (out of `95` total `search=UPF` entries on InterPro, where `5` are already `EX_DUF` in the worklist and `4` are genuine non-`UPF\d{4}` false positives: `PF01455` `HupF_HypC`, `PF03467` `Smg4_UPF3`, `PF04050` `Upf2`, `PF09416` `UPF1_Zn_bind`) are absent from the worklist snapshot, including `PF03649` (`UPF0014`, `Uncharacterised protein family (UPF0014)`), which is one of the four unresolved `UPF` tokens tracked in [#96](https://github.com/CultureBotAI/DUFMech/issues/96).
    2. In `data/worklists/pfam-previous-unknown-names-2026-10-10.json` (`1,834` rows), `1,833` rows are present in `data/worklists/interpro-pfam-duf-2026-10-10.json` (`1,796` `EX_DUF`, `30` `UNKNOWN_CANDIDATE`, `7` `KNOWN_HISTORICAL_DUF`). The single non-overlapping row is `PF21084` (`short_name: WHD_DUF4423_like`, `name: Winged Helix-turn-helix domain`, `previous_unknown_names: ["DUF4423_like"]`, `currently_unknown_name: true`). `src/dufmech/exduf.py` (`plan_migration`) skips `PF21084` because `currently_unknown_name: true` (assuming it is already in the parent DUF worklist), while `src/dufmech/worklist.py` classifies `PF21084` as `FALSE_POSITIVE_TEXT_HIT` because `_` is a word character (`\w`) under `\bDUF\d+\b` and `PF21084`'s long `name` (`Winged Helix-turn-helix domain`) does not repeat `DUF4423` with non-underscore boundaries.
- **Desired outcome**:
  - Align `src/dufmech/worklist.py` harvesting and short-name/name classification with `src/dufmech/pfam_history.py` (`UNKNOWN_NAME_RE`) so that `UPF\d{4}` families (while excluding `UPF1`/`UPF2`/`UPF3`/`HupF` gene names) and underscore-joined `DUF\d+` short names (`PF21084` `WHD_DUF4423_like`) are classified consistently.
  - Coordinate with [#96](https://github.com/CultureBotAI/DUFMech/issues/96) so `PF03649` (`UPF0014`) and any newly harvested `UPF\d{4}` / `PF21084` worklist snapshot and family records (`data/families/PF*.yaml`) are regenerated together with updated snapshot regression tests (`tests/test_exduf.py`, `tests/test_upf1_migration_release.py`, `tests/test_exports.py`).


