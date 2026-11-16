# Review queue preservation audit, 2026-11-16

Related issues: [#459](https://github.com/CultureBotAI/DUFMech/issues/459) and
[#460](https://github.com/CultureBotAI/DUFMech/issues/460).

The two retained scripts under `scripts/adhoc/` produced these read-only audit
results from the exact public GitHub PR heads listed in the ledger. Their
original helper bytes and output hashes are preserved. The JSON results are
gzip-compressed with a fixed zero timestamp solely to avoid carrying repetitive
uncompressed Git-tree evidence. Decompressed SHA256 values are in
`SHA256SUMS.json`; compression does not change their contents.

Inputs were the full paginated public PR inventory and check/file inventory,
whose hashes are recorded in `ledger.json.gz`, plus the repository Git objects.
The audit includes all changed Git paths, including those omitted by GitHub's
100-path list truncation. Filesystem checks of candidate paths included ignored
files. The source audit preserves historical context rather than declaring a
historical review to cover today's entire repository.

These are structural preservation results. They do not establish scientific
endorsement, an approved merge, a completed deployment, or runtime adoption.
## Helper packaging

On 2026-11-16, packaging for issues #459 and #460 set both helper files to
executable mode, sorted their imports, parenthesized two multiline string entries
in `audit_pr_preservation.py`, and removed the unused `digests` counter in
`audit_review_sources.py`. These edits do not change the audit computations.

The original helpers are retained as `original-audit_pr_preservation.py.gz` and
`original-audit_review_sources.py.gz`, using a fixed zero gzip timestamp. Their
decompressed hashes still match the original `SHA256SUMS.json`; no historical
output or recorded original helper hash was replaced. `helper-packaging.json`
records original, packaged and archive hashes explicitly.

| Helper | Original SHA-256 | Packaged SHA-256 |
|---|---|---|
| `scripts/adhoc/audit_pr_preservation.py` | `49664f3a421131dbd35a8fea6d76439b7ce92f4da0ff4b677242424416cbde25` | `3853092ac90fa5f67970ee5d2d1028fffab9496a1518f5c20370beb8816203f7` |
| `scripts/adhoc/audit_review_sources.py` | `43e8d0d0210229507f7908a9a48a6ac7f7b3d5ded23d991be7c2e77b736b319e` | `39bceaf4d6a3ef4ff9450013404ac05d615d45b35e6bdbcaa83cd007d3a47f26` |

Both packaged helpers were rerun with the same captured input snapshots.
`helper-packaging-validation.json` records that the JSON results are identical
after excluding only `generated_at` and the helper SHA-256 metadata; the Markdown
report is byte-identical. The source-inventory rerun deliberately consumes the
original immutable ledger so its input checksum remains constant. Both helpers
pass the repository Ruff checks, and original compressed helper bytes read back
against their recorded hashes.
