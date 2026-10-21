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
    status: open
    issue_url: https://github.com/CultureBotAI/DUFMech/issues/333
```
<!-- mech-infra-tasks:end -->

## Tasks

### `dufmech-infra-0001` — Include curated `FamilyCuration` `UniProtKB` accessions in `protein_examples` snapshots and `FamilyRecord` projection

- **Originating run / cycle / goal**: `mech-goal-sequence-20261019`, cycle `1`, stage `3` (`protein_examples`, `goal-2456`)
- **Status**: `open`
- **Issue**: https://github.com/CultureBotAI/DUFMech/issues/333
- **Priority**: Medium
- **Dependencies**: None
- **Evidence paths**:
  - `src/dufmech/protein_examples.py`
  - `src/dufmech/protein_discovery.py`
  - `src/dufmech/schema/dufmech.yaml`
  - `data/protein_examples/duf-protein-examples-direct-2026-10-13.json`
  - `curation/families/PF*.yaml`
- **Observation**:
  - Across the `141` curated `curation/families/PF*.yaml` overlays, `271` unique verified `UniProtKB:...` accessions are referenced in `causal_graphs[].nodes[].grounding` (`243` unique accessions) and `assertions` (`271` total unique). However, only `59` of those `271` experimentally curated `UniProtKB:...` accessions appear in `data/protein_examples/duf-protein-examples-direct-2026-10-13.json`, leaving `212` curated `UniProtKB:...` accessions absent from the retained `protein_examples` snapshot.
  - `src/dufmech/protein_examples.py` and `src/dufmech/protein_discovery.py` currently draw exclusively from sibling-Mech accession candidates (`data/cross_mech/`, covering `3,106` families) and top-3 annotation-score UniProt queries for `NO_SIBLING_CANDIDATE` families (`5,190` families), without harvesting or prioritizing the verified `UniProtKB:...` accessions curated in `curation/families/PF*.yaml`.
  - Additionally, `FamilyRecord` in `src/dufmech/schema/dufmech.yaml` has no slot or summary pointer for `protein_examples`, so generated `data/families/PF*.yaml` projections do not surface verified sequence examples directly on the family record.
- **Desired outcome**:
  - Extend `dufmech.protein_examples` / `dufmech.protein_discovery` candidate harvesting to include verified `UniProtKB:...` accessions curated in `curation/families/PF*.yaml` (`causal_graphs[].nodes[].grounding` and `assertions`) when matching the family's Pfam domain and organism scope.
  - Evaluate adding a governed read-only projection or pointer from `FamilyRecord` (`src/dufmech/schema/dufmech.yaml`) to verified `protein_examples` snapshot entries.

