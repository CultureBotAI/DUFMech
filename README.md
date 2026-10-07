# DUFMech

Domain of Unknown Function mechanism knowledge base.

[Browse the DUFMech dashboard](https://culturebotai.github.io/DUFMech/).

DUFMech starts from Pfam families whose public InterPro metadata still looks
like a domain or protein of unknown function. The first tool builds a
triage worklist from the InterPro Pfam API, normalizes Pfam rows, keeps DUF
short-name hits that may be historically solved, and can render TSV or JSON.

## Records and Reviews

The frozen worklists feed reproducible LinkML family records. Scientific curation
lives in separate overlays; imported descriptions and automated seed labels do
not become functional claims or completed reviews.

```bash
just records                 # dry run
just records --apply         # guarded regeneration
just validate-all            # records, schema, review and history checks
just sources-check           # offline source and writer governance
just qc                      # authoritative local and CI gate
```

See [family records and evidence](docs/records.md), [timestamped reviews](docs/reviews.md),
[append-only history](docs/history.md), and [source adoption and licensing](docs/sources.md).

The stable validation check is `qc`, provided by `.github/workflows/validate.yaml`
(**Validate DUFMech**). Its local equivalent is `just qc` after `uv sync --locked
--extra dev` and `just browser-install`. CLAW's merge-queue policy must reference
this exact workflow and job name; changes to either require a coordinated policy
update. Passing a local command does not establish that GitHub rules are enabled.
Record, category and repository skills are shipped under `.claude/skills/` and
`.agents/skills/`. Review reports preserve source hashes, timestamps, scope,
findings and follow-ups; they do not automatically certify scientific conclusions.

## Quick Start

Use Python 3.13 for development.

```bash
just install
just browser-install  # Node 22+; needed once for the full QC browser gate
just test
just duf-puf-worklist --limit 10 --format tsv
```

The worklist can also read saved InterPro JSON for offline fixture runs:

```bash
just duf-puf-worklist --input-json interpro-page.json --format json
```

Freeze a new InterPro/Pfam seed worklist with a matching manifest (today's UTC date):

```bash
just freeze-duf-puf-worklist
```

The original seed worklist was frozen on 2026-10-01. The current seed worklist
is a versioned classification correction of that metadata, not a newer
InterPro fetch. It retains all 6,532 families
and source counters; 1,621 historical seed labels were corrected to unknown
candidates. See the [correction audit](docs/provenance/seed-classification-correction-2026-10-05.md)
for the classification policy, parent hashes, and limitations.

Reclassify verified frozen metadata into a new snapshot without contacting InterPro:

```bash
just reclassify-duf-puf-worklist \
  --input-json data/worklists/interpro-pfam-duf-2026-10-01.json \
  --snapshot-date 2026-10-05 --out-dir /tmp/dufmech-classification-check
```

Both worklist freezing and reclassification refuse existing output artifacts;
choose a new date or output directory instead of rewriting a published snapshot.
Seed labels reflect frozen
wording, not experimental validation. Scoring remains a separate step.

Expand frozen Pfam rows to UniProtKB protein members through InterPro:

```bash
just duf-puf-members --pfam-id PF01519 --limit-members-per-family 5
```

Freeze a Pfam member snapshot with UniProtKB metadata and UniRef clusters:

```bash
just freeze-duf-puf-members --input-json data/worklists/interpro-pfam-duf-2026-10-01.json --limit-families 1
```

Freeze MGnify Proteins environmental representatives for Pfam rows:

```bash
just freeze-duf-puf-mgnify --input-json data/worklists/interpro-pfam-duf-2026-10-01.json --limit-families 1
```

Freeze AlphaFold DB evidence for UniProt accessions:

```bash
just freeze-duf-puf-alphafold --uniprot-accession B2BDZ3
```

Freeze CATH-Gene3D FunFam evidence for UniProt accessions:

```bash
just freeze-duf-puf-cath --uniprot-accession P68871
```

Freeze NCBI Batch CD-Search conserved-domain evidence for UniProt accessions:

```bash
just freeze-duf-puf-cdsearch --uniprot-accession P68871
```

Freeze a saved NCBIFAM HMM hit table:

```bash
just freeze-duf-puf-ncbifam --hits-tsv ncbifam-hits.tsv
```

Freeze eggNOG-mapper annotations:

```bash
just freeze-duf-puf-eggnog --annotations-tsv out.emapper.annotations
```

Freeze an EFI-GNT Pfam Neighbor Mapping Table:

```bash
just freeze-duf-puf-efi-gnt --pfam-neighbors-tsv pfam-neighbors.tsv
```

Freeze a saved JGI IMG gene-neighborhood table:

```bash
just freeze-duf-puf-jgi-img --gene-neighbors-tsv img-gene-neighbors.tsv
```

Freeze 3D-Beacons structural coverage evidence for UniProt accessions:

```bash
just freeze-duf-puf-threedbeacons --uniprot-accession P75259
```

Freeze RCSB PDB experimental-structure evidence for UniProt accessions:

```bash
just freeze-duf-puf-rcsb --uniprot-accession P68871 --limit-entities-per-accession 5
```

Freeze PDBe-KB residue annotations for RCSB PDB entities:

```bash
just freeze-duf-puf-pdbe-kb --pdb-entity P68871:1A00:2 --endpoint domains
```

Freeze Rhea reactions for UniProt accessions:

```bash
just freeze-duf-puf-rhea --uniprot-accession P08159
```

Freeze QuickGO molecular-function annotations for UniProt accessions:

```bash
just freeze-duf-puf-quickgo --uniprot-accession P08159
```

Freeze STRING interaction partners for UniProt/taxon pairs:

```bash
just freeze-duf-puf-string --uniprot-taxon P68871:9606 --limit-partners-per-protein 5
```

Freeze UniParc permanent sequence archive IDs for UniProt accessions:

```bash
just freeze-duf-puf-uniparc --uniprot-accession P75259
```

Score frozen DUF/Pfam families with evidence snapshots:

```bash
just score-duf-puf --worklist-json data/worklists/interpro-pfam-duf-2026-10-01.json
```

Freeze the DUF/PUF families and proteins already curated in sibling Mechs, then
write the reuse report:

```bash
git -C ../TraitMech fetch origin main   # likewise for each sibling Mech
just freeze-cross-mech --ref origin/main --uniprot-cache data/raw/cross-mech-uniprot-pfam.json
just cross-mech-report
```

The scan reads tracked YAML from each sibling checkout at the given ref, so local
edits never leak in, and records every Mech commit in the manifest. ProteinTraitsMech
links come from its structured trait identifiers and canonical-example family
classifications. In the other Mechs, the scan matches Pfam IDs, DUF/UPF short names
and InterPro IDs in record text, and checks every cited UniProtKB accession for
worklist Pfam cross-references. Bare DUF names that no longer match a worklist
family, usually because Pfam renamed them after characterization, and UPF names,
which are UniProt nomenclature the Pfam-derived worklist never carries, are kept as
`NOT_IN_WORKLIST` rows. Compound names such as `DUF3458_C` match only their exact
worklist family, including next to prose such as `DUF3458_C-containing`. The manifest
records cache input/output checksums, fetch times for cache hits where known, and
the time and count of new UniProtKB requests. Legacy cache entries retain an explicit
unknown fetch age; a new request does not redate existing cached results. Unresolved
accessions, including merged and demerged entries, are listed separately.

A freeze refuses to replace any existing artifact for the selected date. Use a new
snapshot date or a separate output directory for another run. Both the report and
dashboard require cross-Mech evidence to match the selected worklist; a historical
report can select matching `--cross-mech-json` and `--worklist-json` inputs. Dashboard Mech counts
represent distinct source records, with trait-record availability shown separately.
The current cross-Mech snapshot derives from the original scan by applying the
corrected worklist's seed labels; see the [offline derivation record](docs/provenance/cross-mech-worklist-2026-10-06.md).

Freeze the Pfam families that were renamed from DUF/UPF names, using the previous
identifiers (`#=GF PI`) in a pinned Pfam release's seed file:

```bash
just freeze-pfam-previous-names --pfam-release 38.2 --snapshot-date 2026-10-07
```

The download streams `Pfam-A.seed.gz` and keeps only family headers; alignments are
never retained. The manifest records the release, `Last-Modified`, byte count and
SHA-256 of the file read. `just cross-mech-report` uses the latest snapshot to resolve
unmatched DUF names cited by sibling Mechs to their current Pfam families. A former
DUF name is Pfam history, not evidence of characterization. See the
[provenance record](docs/provenance/pfam-previous-unknown-names-2026-10-07.md).

Render and verify the DUFMech family website:

```bash
just render
just render-check
```

The **Validate DUFMech** GitHub Actions workflow runs `just qc`, including Python
and browser checks, on pull requests, pushes, merge groups and manual runs. To
rerun validation and publishing manually, dispatch **Validate DUFMech** on `main`.
Pages has no direct manual dispatch: its serialized deployment workflow accepts
successful same-repository `main` push or manual validation runs. `queue: max`
retains up to 100 pending runs; additional runs are canceled when that queue is full,
so dispatch **Validate DUFMech** on `main` again after capacity becomes available.
This avoids the default single-pending-slot replacement behavior; see
[GitHub's concurrency documentation](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency).
The workflow checks the validated SHA against current `main` before building and
again after Configure Pages, immediately before deployment. It publishes the artifact
from that exact validated SHA, with serialization preventing an older queued run from
overwriting a newer published revision. These checks do not atomically freeze `main`:
it can advance during deployment, and Pages may lag while the newer revision awaits
validation. The final step reports the deployed validated SHA and any main advancement.
Publishing uses committed frozen inputs and does not refresh upstream data. The
repository's Pages source must be set to **GitHub Actions**.

Reports, README statistics, and pages validate the selected snapshot manifests.
New score snapshots bind every input to its verified bytes and companion manifest.
Ad hoc JSON requires explicit `--allow-ad-hoc-inputs` and is marked accordingly;
legacy or ad hoc scores cannot enter the curated family-record publication layer.
Historical snapshot reports still require matching worklist IDs; use matching
`--worklist-json` and `--score-json` paths when selecting older inputs.
Without a score snapshot, families remain `UNSCORED`, with seed status shown separately.
Missing counters remain unavailable rather than becoming zero, and per-family
protein totals are not deduplicated protein counts.

The generated site includes static family HTML/JSON pages, 50-row catalogue pages,
seed-category pages, sources/schema documentation when the record layer is available,
a compact search index (`catalogue.json`), a complete export (`index.json`), and local
CSS/JavaScript assets. Every family remains reachable through static pagination without
JavaScript. Search, filters, sorting and pagination restore from the URL, and the
light/dark/system theme preference persists across pages. Search fetch failures retain
the static catalogue and display an explicit error.

Descriptions and citations come from frozen inputs. InterPro `PUB...` references are
not interpreted as PMIDs: unresolved citations link to their originating InterPro entry.
Own-source links use the explicit, content-verified `conf/site_source_pins.json` ledger,
never checkout history or a moving branch. The repository build reads
generated `data/families/` records and retained history/review artifacts when present;
snapshot-only rendering remains supported. Curation, reviews and history enter through
their validated native loaders; arbitrary supplemental metadata is not accepted by the CLI.
Native corpus builds discover the latest
`data/worklists/pfam-uniprot-uniref90-YYYY-MM-DD.json` member snapshot using the existing
default UniRef target. Explicit worklist/score selections and custom input directories
require `--members-json` to select a member snapshot. Every selected member manifest must
verify and name the selected worklist seed; a mismatched newest snapshot fails the build
instead of silently selecting an older one. Scoring inputs are selected independently.

The bounded `pfam-uniprot-uniref90-2026-10-07` dataset contains two PF04149 proteins.
Family pages plot its actual one-based, inclusive match coordinates; the catalogue links
to these views. Sources links the frozen member JSON, checksum manifest and attribution:
InterPro match data under CC0, and UniProtKB/UniRef metadata from the UniProt Consortium
under CC BY 4.0. These are observed sequence ranges, not inferred protein structures or
functional assignments. The corpus chart uses actual protein counts; records without range
evidence say so explicitly. Builds do not retrieve upstream data.

After publishing a source checkpoint containing the frozen inputs, records, curation,
history, reviews and schema, capture its full immutable SHA offline before final rendering:

```bash
uv run python -m dufmech.site_sources capture --commit FULL_PUBLISHED_SOURCE_SHA
uv run python -m dufmech.site_sources check
just render
```

Capture requires every local file in the website source directories to match that commit,
including ignored files, and records relative paths and SHA-256 hashes without timestamps.
It neither publishes nor checks remote reachability: the checkpoint must already be
published and retained. Commit the ledger with generated pages. Rendering checks pinned
bytes without calling Git, so squash merges and different local histories do not change
the output. Changed or newly consumed sources require an updated checkpoint and ledger.
Unpinned preview builds make no immutable own-source claim; local record/review/schema
and member-dataset downloads remain available. Rendering never generates a ledger.

`just render` serializes writers using a destination-adjacent `.NAME.dufmech-render.lock`
file, independent of `TMPDIR`. Descriptor-relative writes reject symlink traversal.
It stages generated artifacts before replacing them and preserves unrelated files.
Temporary staging directories are also destination-adjacent, so abrupt process exits
cannot leave unpublished staging content inside the Pages artifact.
An ownership manifest permits removal of unchanged obsolete generated pages;
modified obsolete pages cause an error. The ownership manifest is published only after
cleanup succeeds. A pending-ownership journal preserves old and new content hashes after
interrupted replacement or cleanup, including retries with different inputs; edited
pending files cause an error instead of deletion. `just render-check` compares the full output
tree by content. To build and check
an isolated preview without changing the tracked site:

```bash
uv run python scripts/render_pages.py --out /tmp/dufmech-site
uv run python -m dufmech.site_contract --site /tmp/dufmech-site --budgets conf/pages_budgets.json
```

The contract checks complete catalogue reachability, local links, bounded initial rows,
byte budgets, and light/dark color-token contrast. `conf/pages_budgets.json` also follows
the shared `kg-microbe-pages audit` budget format. Browser tests check real layout and
computed contrast at 1440px and 390px, controls, URL/back/reload behavior, theme persistence,
failed data requests, denied storage, and JavaScript-free pagination:

```bash
npm ci
npx playwright install chromium
DUFMECH_PYTHON="$(pwd)/.venv/bin/python" DUFMECH_SITE_DIR=/tmp/dufmech-site npm run test:browser
```

Browser tests require Node.js 20 or newer. Dependency/browser installation needs network
access once. The test run itself uses a
temporary local HTTP server, a synthetic engineering fixture, and the actual generated
`pages/` site. Set `DUFMECH_SITE_DIR` to test a different generated tree. Screenshots
default to the system temporary directory under
`dufmech-browser-screenshots`; set `DUFMECH_SCREENSHOT_DIR` to retain them elsewhere.
`PLAYWRIGHT_CHROMIUM_EXECUTABLE` can select an existing Chrome/Chromium executable.

Run the local quality gate:

```bash
just qc
```

## Current Corpus

<!-- BEGIN GENERATED CORPUS STATS -->
<!-- Generated by scripts/check_docs.py; do not edit this block by hand. -->
**6,532 DUF/Pfam families** are currently committed from frozen InterPro/Pfam snapshots.

6,492 carry InterPro IDs, 820 have InterPro structure counters, and 6,478 have AlphaFold DB model counters.

Latest inputs: `worklist=interpro-pfam-duf-2026-10-05`.

**Unknown-function seed status**

| Value | Families |
|---|---:|
| `KNOWN_HISTORICAL_DUF` | 378 |
| `UNKNOWN_CANDIDATE` | 6,154 |

**Characterization status**

| Value | Families |
|---|---:|
| `UNSCORED` | 6,532 |

**Candidate reasons**

| Value | Families |
|---|---:|
| `description_says_unknown_function` | 1,359 |
| `domain_of_unknown_function` | 2,832 |
| `name_matches_duf` | 155 |
| `name_says_unknown_function` | 6,115 |
| `short_name_matches_duf` | 6,371 |
<!-- END GENERATED CORPUS STATS -->

## Scope

DUFMech records domains, protein families, and evidence layers that help
decide whether a family or representative protein is still uncharacterized.
The initial source stack is:

- InterPro/Pfam for DUF-family discovery.
- UniProtKB and UniRef for reference-proteome members.
- UniParc for permanent sequence IDs and checksums.
- MGnify Proteins for environmental representatives.
- AlphaFold DB, PDB, PDBe-KB, CATH-Gene3D, CDD, NCBIFAM, STRING, eggNOG,
  EFI-GNT, JGI IMG, Rhea, GO, and QuickGO as follow-on structure,
  neighborhood, network, and function-evidence layers.

The first pass deliberately treats a `DUFnnnn` Pfam short name as a clue, not
as proof that the family is still functionally unknown.

## Layout

```text
DUFMech/
├── data/
│   ├── cross_mech/
│   └── worklists/
├── docs/
│   ├── provenance/
│   └── reports/
├── pages/
├── scripts/
├── src/dufmech/
└── tests/
```

## License

Project-authored data and narrative documentation are licensed under
[CC BY 4.0](LICENSE-DATA). Project-authored code, including scripts, tests,
schemas and website templates, is licensed under [BSD-3-Clause](LICENSE-CODE).
Third-party material retains its own licenses and attribution requirements.
See [LICENSE](LICENSE) for scope and attribution.
