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
candidate reason). Those stay EX_DUF but are scored `UNKNOWN_CANDIDATE` with the extra
reason `pfam_metadata_still_says_unknown_function`. A rename usually
follows published work on some members; it is not experimental evidence for every member.

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
