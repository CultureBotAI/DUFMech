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
