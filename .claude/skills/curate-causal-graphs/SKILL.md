---
name: curate-causal-graphs
description: Review and curate DUFMech family mechanism graphs in maintained FamilyCuration
  overlays, preserving tested-protein scope and validated projections.
---

# DUFMech causal graphs

Read [record contract](../../../docs/records.md),
[history](../../../docs/history.md), [reviews](../../../docs/reviews.md),
[the schema](../../../src/dufmech/schema/dufmech.yaml), and
[ground-causal-graph-proteins](../ground-causal-graph-proteins/SKILL.md).
Inventory the complete verified family worklist, canonical projections and
`curation/families/PF*.yaml` overlays. Overlay root `FamilyCuration` is distinct
from generated `FamilyRecord`; never serialize a projection back as an overlay.

Review graph taxon, family mapping, scope, context, limitations, nodes and every
edge against retained, checksummed minimal source extracts. Evidence about a
tested protein, subfamily or construct must not imply family-wide mechanism.
Keep predictions, structures, contextual associations and experiments distinct.
Missing functional evidence is not proof of no function. Do not fabricate a
mechanism for a seed-only family merely to fill graph coverage.

Use narrow text-preserving overlay patches and the exact history/review sequence
in `curate-yaml-record`. Changed content cannot inherit a stale review approval.
Run `just records` preview then authorized `just records --apply`,
`uv run --locked python -m dufmech.causal_graphs --apply`, and verify with
`uv run --locked python -m dufmech.records --check`,
`uv run --locked python -m dufmech.causal_graphs --check`,
`uv run --locked python -m dufmech.history check`,
`uv run --locked python -m dufmech.reviews check` and `just qc`.
Source pins and generated Pages use the native committed-source workflow;
never invent a pin or hand-edit projections/inventories to clear a gate.
## Scope and completion

For one target, read the whole maintained record and its generated projection or
components. For a corpus goal, first freeze an inventory of record IDs, paths,
input hashes and applicable graph/protein elements; resume that ledger after an
interruption. Include hidden and ignored inputs when establishing absence.
Classify each target as checked, changed, evidence-limited, excluded, not
applicable or blocked, with reasons and inspected sources. A sample, a provider
report and a validator pass do not establish whole-corpus scientific completion.

Use [curate-yaml-record](../curate-yaml-record/SKILL.md) for the local evidence,
write, history and status contract; this adapter does not replace its managed
method. Record actual agent identity. Preserve scientific status rules and
unrelated edits. Use inspected primary evidence for mechanistic claims and exact
active identifiers for instances; never infer causality from association or
coverage from an empty query. A quotation is source text; interpretation belongs
in the native notes/explanation field.

Save final scientific assessments through
[review-yaml-record](../review-yaml-record/SKILL.md),
[record reviews](../../../docs/record-reviews.md), and the
[local profile](../../../docs/record-review-profile.md), including their native
persistence exceptions. Keep coverage/checkpoint accounting even when a clean
review should not produce a bundle. Unavailable prerequisites remain blocked;
a skipped target is not a completed enrichment. This skill authorizes no paid
provider call by itself.

After a completed goal, follow the user's authorized commit, push/PR,
adversarial review, issue/fix, merge and branch-cleanup sequence under the current
repository guidance. Carry forward existing authorization without asking again.
Use fresh required checks and native merge-queue rules. Verify actual merge and
landed content before deleting that feature branch or starting the next goal.
Only genuine review findings become issues; a no-diff goal needs a documented
no-op receipt rather than an artificial commit.
