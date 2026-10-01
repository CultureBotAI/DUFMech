set dotenv-load := true

default:
    @just --list --unsorted

# Install package + dev tools.
install:
    uv sync --extra dev

# Run the test suite.
test:
    uv run --extra dev pytest

# Run Ruff over source, scripts, and tests.
lint:
    uv run --extra dev ruff check src scripts tests

# Build the first InterPro/Pfam DUF-family worklist.
duf-puf-worklist *args="":
    uv run python scripts/duf_puf_worklist.py {{args}}

# Freeze the first InterPro/Pfam DUF-family worklist snapshot.
freeze-duf-puf-worklist *args="":
    uv run python scripts/freeze_duf_puf_worklist.py {{args}}

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

# Score frozen DUF/Pfam families with evidence snapshots.
score-duf-puf *args="":
    uv run python scripts/score_duf_puf.py {{args}}
