# Family Records

DUFMech distinguishes imported identity, automated evidence scoring, and scientific
curation. They are not interchangeable review states.

- `data/worklists/` retains immutable, checksummed source snapshots.
  Scores used by this layer must bind every input to verified byte/manifest hashes.
  Legacy filename-only scores and explicitly ad hoc scoring inputs are rejected.
- `data/families/PFxxxxx.yaml` is a reproducible projection of the latest verified
  snapshot. All imported families begin as `SEEDED`, not scientifically reviewed.
- `curation/families/PFxxxxx.yaml` holds human-owned overlays. The closed
  `FamilyCuration` schema permits assertions, discussions, datasets and cross-corpus
  links, but cannot override the Pfam identity, source label or counters.
- A non-seed status or any curated assertion, discussion, dataset or cross-corpus
  link requires `curation_history: history/records/PFxxxxx` and at least one actual
  canonical event about that family's overlay or projection. Append it through
  `just new-history`; the generator does not invent actors or events.
- `evidence/*.txt` contains appropriately licensed, minimal source extracts for
  assertion quotation checks. Never commit restricted full-text publications.
- Timestamped review Markdown and canonical history YAML remain separate retained
  artifacts; a source freeze or regeneration is not a scientific review.
- `curation_events` is a generated, read-only index of actual canonical sidecar
  events. Each entry identifies its source file and zero-based event index.
  Overlays cannot supply it; validation replays it from the authoritative sidecars.
  Records without history have no index. Append history first, then regenerate
  the affected projections; do not hand-edit the exported events.

`REVIEWED` requires a retained `review_id` with an explicit PASS for the exact
current record content and a linked canonical REVIEW history event. PASS is scoped:
the report's separate `scientific_review` flag and `review_scope` must be read before
treating a validation or identity audit as functional characterization. Editing the
scientific content invalidates this gate until a new review is completed.
The generated history index, curation status and review pointer are bookkeeping,
excluded from the semantic review digest. Their exclusion never bypasses the
independent checks on history validity, index freshness or the linked REVIEW event.

Run `just records` for a dry run, `just records --apply` to regenerate, and
`just records-check` for the CI gate. Generation validates the entire batch before
writing. A hash inventory limits replacement to unchanged generated files; edited,
unowned, symlinked or unexpected paths are refused. Stale families are not silently
deleted: reconcile and preserve their curation before adopting a changed inventory.
Native writers coordinate through an advisory lock and pin directory descriptors
so concurrent symlink replacement cannot redirect publication. Bytes are staged
before any existing file is displaced. Publication retains displaced files in
ignored `.dufmech/record-recovery/` and refuses a destination created by
another writer; concurrent edits remain recoverable. On an interrupted batch,
resolve the reported conflict and rerun before committing. Do not discard recovery
copies until any concurrent editor's changes have been reconciled.

## EX_DUF Families And Migration

`EX_DUF` is the seed status for families Pfam renamed away from a DUF/UPF name. The
evidence is Pfam's own previous-identifier history (`#=GF PI`, frozen as
`pfam-previous-unknown-names-*`), not the current name or description, so text
reclassification never undoes it. Candidate reason `pfam_previous_unknown_name` marks
these rows. Scoring treats an EX_DUF seed like a historical DUF: characterization
`KNOWN_HISTORICAL_DUF` with reason `pfam_renamed_from_unknown_name`, unless the current
Pfam name or description still says the function is unknown (any `*_unknown_function`
candidate reason). For those the rename alone does not count: they stay EX_DUF and, absent
other known or partial evidence, score `UNKNOWN_CANDIDATE`, with the extra reason
`pfam_metadata_still_says_unknown_function`. A rename usually
follows published work on some members; it is not experimental evidence for every member.

Classifier policy `unknown-function-metadata-v3` distinguishes explicit former
numbered DUF/UPF labels from current unknown-function statements. For example,
"previously annotated as DUF4374 (domain of unknown function 4374)" is naming
history, while a separate "function is still unknown" remains an unknown signal.
The original description is preserved; only candidate reasons are recomputed.
The v2 policy remains available to the Python reclassification API for exact
historical replay, and verified-input loading accepts both versions.

Pfam previous-name parsing also distinguishes four-digit UPF family labels from
UPF1/UPF2 gene names. A family such as PF18141 (`UPF1_1B_dom`, formerly DUF5599)
is eligible for EX_DUF migration after a new previous-names freeze. These are
metadata corrections, not newly curated functional evidence.

### Adopting Classifier Corrections

Code changes do not rewrite existing snapshots, projections, scores or Pages.
For the corrections tracked in issues #165 and #173:

1. Freeze the pinned Pfam seed again with the corrected UPF-name parser, under
   a new previous-names snapshot ID; retain the old files and manifests.
2. Run a follow-up EX_DUF migration with that snapshot, to include PF18141 using
   fetched InterPro metadata. Verify its planned additions before applying it.
3. Reclassify the migrated worklist with the default v3 policy, so previously
   frozen descriptions also receive corrected candidate reasons. Migration
   preserves existing rows and does not itself reclassify all their text.
4. Derive compatible cross-Mech artifacts, verify score inputs, then regenerate
   records, reports and Pages with valid published source pins. Only adopted,
   appropriately scoped evidence may contribute to scientific assertions.

Each worklist derivation requires a date later than its parent. Do not overwrite
an existing date's snapshot, fabricate future acquisition dates, or score an old
worklist as though its candidate reasons had already been updated. These steps
remain required for the retained October 8, 2026 corpus; an in-memory classifier
test is not a published migration or scored release.

`just migrate-exduf` derives a new worklist snapshot (dry run unless `--apply`):

```bash
just migrate-exduf --parent-json data/worklists/interpro-pfam-duf-<date>.json \
  --previous-names-json data/worklists/pfam-previous-unknown-names-<date>.json \
  --snapshot-date <new-date> [--live-json <fresh DUF-search worklist>] --apply
```

- Families in the worklist that Pfam renamed become `EX_DUF`; their frozen metadata is
  unchanged.
- Renamed families outside the worklist are added with metadata fetched from the
  InterPro Pfam entry API.
- For future cases: freeze the previous identifiers of a new Pfam release, freeze a
  fresh DUF search, and pass it as `--live-json`. A family that left the search is
  carried forward as `EX_DUF` when Pfam renamed it or it was already `EX_DUF`. Any
  other departure stops the migration and names the family, so nothing is dropped
  silently.

The manifest records both (or all three) parents with file hashes. Every status or
reason change is logged against the parent row; a family new to a live search is logged
as `ABSENT -> <status>`. Added, carried, retained `EX_DUF`, refreshed (metadata changed
in the live search), live-new and not-found families are listed, and `fetched_live`
records whether InterPro lookups were made. The output date must be later than the parent
and any live worklist, and not earlier than the previous-names snapshot, so it is always
the newest worklist.

The verified-input loader accepts it as lineage profile `exduf-migration-v1`. It requires
the migration source identity and the live parent's file provenance when present, rejects
malformed change entries, and checks that the `EX_DUF` rows are exactly those logged as
changed to `EX_DUF` plus the added, carried and retained families, each carrying the
migration reason. A later text reclassification of a migrated worklist (`derivation-v2`)
remains loadable and keeps `EX_DUF`.

Both scoring and report loaders compare `derivation-v2` and `exduf-migration-v1`
rows with co-located parent JSON when available. They verify the recorded parent
hash and byte size, retained family membership and metadata, and classification
change bookkeeping. Refresh migrations compare against the live worklist as well;
carried families have explicitly re-fetched metadata. Symlink and non-regular
parent files are rejected. Detached artifact sets remain portable, but an absent
parent cannot be content-compared. These checks read only direct parents, not the
entire ancestry, and do not certify scientific classification.

Cross-Mech derivations retain former-name mappings and their original Pfam
snapshot IDs and hashes through subsequent derivations, even without another
`--previous-names-json` input. `previous_name_sources` records mappings separately
when several snapshots contribute; the aggregate map and resolved-row count remain
available. A chain with missing mapping provenance or inconsistent counts is
rejected rather than propagating that loss. Neither this bookkeeping nor an
offline name resolution constitutes a new Mech scan or functional evidence.
Already-resolved rows follow the selected worklist's current Pfam short name as
well as its seed status; name changes are counted separately in the derivation.
The source rows and cited former-name mappings remain retained.

## Evidence Contract

Each functional assertion states its experimental, computational or contextual
basis and the exact scope of the inference. It requires at least one source URL,
reference, supporting quotation, explanation, cache path and SHA-256. Validation
checks source shape, cache integrity and quotation occurrence. These checks do not
prove the interpretation or justify generalizing one protein's activity to a family;
that remains the reviewer's responsibility. Imported descriptions and InterPro
`[[cite:...]]` identifiers are not treated as verified claims or invented PMIDs.

The LinkML schema imports governed shared discussion, dataset and cross-corpus
types. Generated Python dataclasses, closed JSON schemas and the schema reference are
checked for drift. Native ID/label validation compares generated records with their
verified frozen Pfam source, offline and reproducibly; it does not claim to validate
unmodeled GO or other ontology terms.

## Applicability

KGX, SSSOM, paid/provider-specific research and embedding services are optional
products without a committed downstream consumer here. Disease-specific exports,
clinical metadata and causal graph rendering do not apply to a family seed corpus.
The source adapters remain available, and curated discussions can hold unresolved
questions without pretending that automated seed classification resolves them.
