set dotenv-load := true

default:
    @just --list --unsorted

# Install package + dev tools.
install:
    uv sync --extra dev

# Install the locked browser-test dependency and Chromium for full QC.
browser-install:
    npm ci
    npx playwright install chromium

# Run the test suite.
test:
    uv run --extra dev pytest

# Run Ruff over source, scripts, and tests.
lint:
    uv run --extra dev ruff check src scripts tests

# Run the authoritative local quality gate.
qc: require-claw require-claw-root
    PYTHONPATH="$CLAW_SRC${PYTHONPATH:+:$PYTHONPATH}" uv run --locked --extra dev python scripts/run_qc.py

# Shared adapters run against an explicit published CLAW source checkout.
[private]
require-claw:
    test -d "${CLAW_SRC:-/nonexistent}/kg_microbe_kgscan" || { printf '%s\n' 'Set CLAW_SRC to the published culturebotai-claw src directory.' >&2; exit 2; }

[private]
require-claw-root:
    test -f "${CLAW_ROOT:-/nonexistent}/pyproject.toml" && test -f "${CLAW_ROOT:-/nonexistent}/uv.lock" || { printf '%s\n' 'Set CLAW_ROOT to the published culturebotai-claw checkout with its separate locked OAK environment.' >&2; exit 2; }

[positional-arguments]
research *args: require-claw
    PYTHONPATH="$CLAW_SRC${PYTHONPATH:+:$PYTHONPATH}" uv run --locked python -m dufmech.research "$@"

[positional-arguments]
exports *args:
    uv run --locked python -m dufmech.exports "$@"

[positional-arguments]
id-labels *args:
    uv run --locked python -m dufmech.id_labels "$@"

id-labels-check: require-claw-root
    uv run --locked python -m dufmech.id_labels --check --claw-root "$CLAW_ROOT"

id-labels-oak-test: require-claw-root
    env -u VIRTUAL_ENV -u UV_PROJECT_ENVIRONMENT -u PYTHONPATH -u PYTHONHOME uv run --project "$CLAW_ROOT" --locked --offline python -I -B "$PWD/tests/test_id_labels.py" --oak-regression --repo-root "$PWD"

[positional-arguments]
knowledge-gap-scan *args: require-claw
    PYTHONPATH="$CLAW_SRC${PYTHONPATH:+:$PYTHONPATH}" uv run --locked python -m dufmech.knowledge_gaps "$@"

# Preview or apply deterministic family/schema projections.
records *args="":
    uv run --locked python -m dufmech.records {{args}}

# Closed schema, frozen ID/label correspondence, quotes, and generated drift.
records-check:
    uv run --locked python -m dufmech.records --check

# Shared fleet interfaces backed by the native closed-schema pipeline.
validate-data: records-check

validate-schema:
    uv run --locked python -m dufmech.records --schema-only --check

validate-all: records-check history-check reviews-check

gen-python:
    uv run --locked python -m dufmech.records --schema-only --apply

# Retain timestamped, scoped review artifacts.
[positional-arguments]
review *args:
    uv run --locked python -m dufmech.reviews "$@"

# Append or validate canonical curation history.
[positional-arguments]
history *args:
    uv run --locked python -m dufmech.history "$@"

# Append one explicit, validated curation event (the fleet recipe contract).
[positional-arguments]
new-history *args:
    uv run --locked python -m dufmech.history new "$@"

# Validate retained review and history artifacts without creating scaffolds.
history-check:
    uv run --locked python -m dufmech.history check

reviews-check: record-reviews-check
    uv run --locked python -m dufmech.reviews check

# Validate the shared profile, immutable bundles, and synthetic saver roundtrip.
record-reviews-check:
    uv run --locked --extra dev pytest -q tests/test_record_review_contract.py
    uv run --locked python scripts/record_review.py check

# Check generated HTML links, accessibility tokens and repository-selected budgets.
site-check *args="":
    uv run --locked python -m dufmech.site_contract {{args}}

# Explicit online publication gate; offline QC and rendering never fetch refs.
[positional-arguments]
site-sources-published *args:
    uv run --locked python -m dufmech.site_source_publication "$@"

# Playwright interaction and mobile/desktop regression suite.
browser-test:
    npm run test:browser

# Validate source catalogue, adoption queue and native writer inventory offline.
sources-check:
    uv run --locked python -m dufmech.source_governance

# Refresh the generated current-corpus block in README.md.
docs-stats:
    uv run python scripts/check_docs.py --write

# Fail if README.md's current-corpus block is stale.
docs-check:
    uv run python scripts/check_docs.py --check

# Verify every frozen worklist artifact matches its manifest.
provenance-check:
    uv run python scripts/check_provenance.py

# Build the first InterPro/Pfam DUF-family worklist.
duf-puf-worklist *args="":
    uv run python scripts/duf_puf_worklist.py {{args}}

# Freeze the first InterPro/Pfam DUF-family worklist snapshot.
freeze-duf-puf-worklist *args="":
    uv run python scripts/freeze_duf_puf_worklist.py {{args}}

# Migrate Pfam-renamed DUF/UPF families into EX_DUF (dry run unless --apply).
migrate-exduf *args="":
    uv run python scripts/migrate_exduf_worklist.py {{args}}

# Version a classification correction using verified, frozen metadata only.
reclassify-duf-puf-worklist *args="":
    uv run python scripts/reclassify_duf_puf_worklist.py {{args}}

# Expand Pfam worklist rows to UniProtKB protein members.
duf-puf-members *args="":
    uv run python scripts/duf_puf_members.py {{args}}

# Freeze Pfam members with UniProtKB metadata and UniRef clusters.
freeze-duf-puf-members *args="":
    uv run python scripts/freeze_duf_puf_members.py {{args}}

# Freeze Pfam families with MGnify Proteins representatives.
freeze-duf-puf-mgnify *args="":
    uv run python scripts/freeze_duf_puf_mgnify.py {{args}}

# Freeze UniProt accessions with AlphaFold DB prediction metadata.
freeze-duf-puf-alphafold *args="":
    uv run python scripts/freeze_duf_puf_alphafold.py {{args}}

# Freeze UniProt accessions with CATH-Gene3D FunFam metadata.
freeze-duf-puf-cath *args="":
    uv run python scripts/freeze_duf_puf_cath.py {{args}}

# Freeze UniProt accessions with NCBI Batch CD-Search domain metadata.
freeze-duf-puf-cdsearch *args="":
    uv run python scripts/freeze_duf_puf_cdsearch.py {{args}}

# Freeze a saved NCBIFAM HMM hit table.
freeze-duf-puf-ncbifam *args="":
    uv run python scripts/freeze_duf_puf_ncbifam.py {{args}}

# Freeze a saved eggNOG-mapper annotation table.
freeze-duf-puf-eggnog *args="":
    uv run python scripts/freeze_duf_puf_eggnog.py {{args}}

# Freeze a saved EFI-GNT Pfam Neighbor Mapping Table.
freeze-duf-puf-efi-gnt *args="":
    uv run python scripts/freeze_duf_puf_efi_gnt.py {{args}}

# Freeze a saved JGI IMG gene-neighborhood table.
freeze-duf-puf-jgi-img *args="":
    uv run python scripts/freeze_duf_puf_jgi_img.py {{args}}

# Freeze UniProt accessions with 3D-Beacons structural coverage metadata.
freeze-duf-puf-threedbeacons *args="":
    uv run python scripts/freeze_duf_puf_threedbeacons.py {{args}}

# Freeze UniProt accessions with RCSB PDB experimental structure metadata.
freeze-duf-puf-rcsb *args="":
    uv run python scripts/freeze_duf_puf_rcsb.py {{args}}

# Freeze RCSB PDB entities with PDBe-KB annotation metadata.
freeze-duf-puf-pdbe-kb *args="":
    uv run python scripts/freeze_duf_puf_pdbe_kb.py {{args}}

# Freeze UniProt accessions with Rhea reaction metadata.
freeze-duf-puf-rhea *args="":
    uv run python scripts/freeze_duf_puf_rhea.py {{args}}

# Freeze UniProt accessions with QuickGO molecular-function annotations.
freeze-duf-puf-quickgo *args="":
    uv run python scripts/freeze_duf_puf_quickgo.py {{args}}

# Freeze UniProt accessions with STRING interaction partner metadata.
freeze-duf-puf-string *args="":
    uv run python scripts/freeze_duf_puf_string.py {{args}}

# Freeze UniProt accessions with UniParc sequence archive metadata.
freeze-duf-puf-uniparc *args="":
    uv run python scripts/freeze_duf_puf_uniparc.py {{args}}

# Freeze Pfam families renamed from DUF/UPF names (Pfam-A.seed previous IDs).
freeze-pfam-previous-names *args="":
    uv run python scripts/freeze_pfam_previous_names.py {{args}}

# Freeze UniProtKB example-protein candidates for DUF families that lack one.
freeze-example-candidates *args="":
    uv run python scripts/freeze_example_candidates.py {{args}}

# Freeze DUF/PUF families and proteins already curated in sibling Mechs.
freeze-cross-mech *args="":
    uv run python scripts/freeze_cross_mech_examples.py {{args}}

# Write docs/reports/ for the latest cross-Mech snapshot.
cross-mech-report *args="":
    uv run python scripts/cross_mech_report.py {{args}}

# Score frozen DUF/Pfam families with evidence snapshots.
score-duf-puf *args="":
    uv run python scripts/score_duf_puf.py {{args}}

# Print a corpus report from frozen DUF/Pfam snapshots.
report *args="":
    uv run python scripts/duf_puf_report.py {{args}}

# Render the browsable static dashboard under pages/.
render *args="":
    uv run python scripts/render_pages.py {{args}}

# Fail if pages/ is out of step with frozen snapshots.
render-check:
    uv run python scripts/render_pages.py --check
