# Curation History

History uses the fleet's `HistoryRecord` contract and `kg_microbe_history` layout
and event semantics. The sole schema authority is the fleet-synchronized file
`src/dufmech/schema/history.yaml`. DUFMech validates directly with LinkML; it does
not ship an independently rewritten history schema. A missing canonical file
blocks event creation and `check` with an instruction to run supported fleet sync.

Use `uv run dufmech-history`, or `uv run python -m dufmech.history`. Global
`--repo-root PATH`, when needed, precedes the subcommand. `new-history` (alias
`new`) requires all of:

- `--kind`, `--slug`, `--path`: target kind, stable directory identifier, and
  existing repository-relative target path.
- `--timestamp`: explicit quoted UTC session start, retained verbatim. The native
  validator requires a year from 2000 through 2099, inclusive, on both creation
  and retained-file loading. This deterministic typo guard does not consult the
  current clock or modify the canonical schema.
- `--event`, `--outcome`: an actual event and outcome from the canonical schema.
- `--summary` and `--details` or `--details-file`: actual work, evidence, validation,
  and remaining limits. There are no completed scaffold events.
- `--actor-name`, `--actor-type`: the actual participant. AI actors also require
  `--model` and `--agent-tool`; `--agent-version` is optional when known.

Repeatable optional arguments are `--section`, `--issue`, `--pr`, and `--url`.
URLs must be HTTP(S) without credentials. No provider is contacted by this command.
The shared schema supports record/schema/mapping/report/infrastructure/other
targets, GENERAL/CREATE/EDIT/REVIEW/AUDIT events, and
changed/no_change/needs_followup/blocked outcomes. Those enum values are validated
against the actual canonical file, not a parallel local schema.

For a record review, use a real `REVIEW` event and pass the stable URL returned by
`reviews.review_report_url(review_id)` as `--url`. Explain the scope explicitly in
the summary/details. An implementation change belongs to `infrastructure` or
`report`, not a fabricated scientific curation event. Snapshot-only record audits
can target the frozen JSON path with the Pfam accession as their slug; they do not
satisfy the current-projection `REVIEWED` gate.

Events live at `history/<kind-directory>/<slug>/<UTC>-<actor>-<shortid>.yaml`, with
the filename stem equal to `session.id`. The layout and fields remain compatible
with shared history consumers. Random suffixes and exclusive numeric collision
fallbacks prevent overwrites, including concurrent writers. UTC timestamps do not
change on subsequent loads. Directory symlinks, traversal, unsafe slugs, malformed
records, and known scaffold prose are rejected. No `--force` option is available.

```bash
uv run dufmech-history check
uv run dufmech-history list --pfam-id PF04149
```

`check` (alias `validate`) validates the canonical schema and every retained YAML
or YML sidecar, including ignored/hidden files. `list` returns deterministic JSON.
Exit 0 means success, validation/I/O errors return 1, and argparse errors return 2.
History absence is advisory: an empty history directory is not proof that
scientific curation has occurred. Existing events must pass validation.

`history.load_history_metadata(root, pfam_id=None)` returns full validated record
data plus `path`, `href`, and `target_href`. Hrefs are encoded paths relative to the
repository root; the renderer supplies the GitHub/site base and escapes text.
Removed historical targets have `target_href: null`; unsafe or symlinked targets
are errors. A Pfam-specific load reads and validates only that family's directory;
the unfiltered loader and global `check` validate the whole tree. No persistent
validation cache is used, so newly written or changed sidecars are seen immediately.
Load once and index record targets by `target.slug` for Pages and the generated
family audit export. An empty history list does not require a
schema at render time, but any existing event does. Corrections are new events
that identify the superseded session in their details.

Curated records can carry the stable directory pointer
`curation_history: history/records/PFxxxxx`. The parent record builder may derive
this constant for overlays; it must validate it with
`history.require_record_history(root, pfam_id, history_path)`. The helper requires
at least one actual canonical event targeting this family's overlay or projection.
Create that first event before the initial curated projection is reviewed. Appending
later sidecars leaves the pointer and semantic review digest unchanged.

## Generated Audit Index

Canonical history sidecars are the sole editable history authority. The generated
`FamilyRecord.curation_events` is a read-only machine-readable index of those
events, not another place to curate history. `FamilyCuration` cannot supply it.
The family builder derives it with `history.project_curation_events(root, pfam_id)`;
families without sidecars need no field and the helper returns an empty list.

Every exported event contains exactly `timestamp`, `curator`, `action`, `outcome`,
`summary`, `history_record`, `event_index`, and `llm_assisted`. Timestamp and summary
are retained verbatim. Curator joins session actor names with `, `; `llm_assisted`
is true when any session actor is an AI agent. Action is the canonical event type.
`history_record` is the validated repository-relative sidecar path, and
`event_index` is its zero-based index within `events`. Full details, actor metadata,
and links stay in that sidecar and are retrieved by this pair of references.

The public helper never writes files and always validates the family's sidecars.
It sorts by parsed UTC session time, sidecar path, then original event index.
Internal builders may load history once, group record targets by Pfam slug, and
use the private pure `_project_curation_events(records)` on that already-validated
metadata. This internal path must never carry user input into a public validator
or become a persistent stale cache. Snapshot-targeted audits can appear in the
index, but do not satisfy the stricter history-pointer or REVIEWED target rules.

Append history first, then regenerate the affected family projections. The native
record validator must replay the canonical view and reject forged or stale exports.
Full generated-file integrity checks still include the export, even though the
semantic review digest excludes `curation_events`. Thus an appended REVIEW event
does not invalidate the review it records, while changed scientific content still
requires a new review. The index alone never establishes scientific endorsement.

See [reviews.md](reviews.md) for the exact gate linking a passing retained report,
a canonical REVIEW event, and the digest of the current effective family record.
