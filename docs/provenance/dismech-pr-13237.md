# Transferred From DisMech PR 13237

DUFMech was accidentally initialized in `monarch-initiative/dismech` as
monarch-initiative/dismech#13237, `Add first DUF/Pfam worklist`. Chris Mungall
noticed the wrong repository on 2026-10-01 and opened
monarch-initiative/dismech#13251 to revert it.

The useful work transferred here was:

- the InterPro/Pfam data-source decision report;
- `src/dismech/dufmech/worklist.py`, ported to `src/dufmech/worklist.py`;
- `scripts/duf_puf_worklist.py`, kept as a checkout-local wrapper;
- `tests/test_duf_puf_worklist.py`, ported to the standalone package; and
- the `duf-puf-worklist` recipe.

The DisMech review found and resolved three small issues before merge:

- `scripts/duf_puf_worklist.py` needed to bootstrap `<repo>/src` before imports
  so direct script execution did not depend on an editable install.
- the script had an unused shebang while the file was not executable and was
  invoked with `uv run python`;
- the `--limit` help text needed to be explicit that the limit is applied to
  the first normalized InterPro rows fetched, before final sorting.

The original offline checks all passed:

```bash
uv run pytest tests/test_duf_puf_worklist.py
uv run python -m compileall -q src/dismech/dufmech scripts/duf_puf_worklist.py
uvx ruff check .
```
