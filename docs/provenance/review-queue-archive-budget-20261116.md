# Measured retained-review archive capacity, 2026-11-16

[Issue #463](https://github.com/CultureBotAI/DUFMech/issues/463) applies the evidence-preserving procedure from [closed issue #238](https://github.com/CultureBotAI/DUFMech/issues/238): account for legitimate archive growth, retain the evidence, and change only the measured archive capacity with rejection regressions. Sources-list pagination remains the separate [issue #464](https://github.com/CultureBotAI/DUFMech/issues/464).

## Complete committed-tree accounting

The read-only helper `scripts/adhoc/audit_site_archive_growth.py` compares every Git-tracked Pages entry at main `a030cca0dae2771e961ae12474c24c47a32b1363` and the pre-pagination consolidation `c7de1a2a1f4d552e196f7da5fe0d280682c3c5a1`. It records every added, modified and deleted path, sizes, modes and blob IDs in `review-queue-archive-budget-20261116.json.gz`. Gzip has a fixed zero timestamp; its decompressed SHA-256 is `a41fc6a72a9b454a22ae25605a98474ad4179d130c3127c6f92c3777d737b6f6`. The helper SHA-256 recorded by that result is `c56c291e4c72bb3e17858d023fa8574a2855ee59a5d03fb244ea9c06988944b7`.

| Measurement | Published main | Consolidation | Growth |
|---|---:|---:|---:|
| Generated files | 34,579 | 36,479 | 1,900 |
| Total bytes | 446,484,860 | 493,450,196 | 46,965,336 |

There are 1,900 added files, 16,933 modified files and **zero deletions**. Another 17,646 files totaling 218,087,552 bytes are unchanged. All 1,900 original review YAML/Markdown downloads match both their retained source blobs and their copied Pages blobs, with SHA-256 and byte-count proof. None of the immutable review observations is removed, restamped or promoted.

| Accounted change | Added bytes |
|---|---:|
| 1,900 exact retained review source downloads | 43,580,615 |
| Family HTML metadata | 484,089 |
| Family JSON metadata | 608,523 |
| `index.json` metadata | 1,490,702 |
| Sources listing HTML | 508,763 |
| `site-files.json` ownership inventory | 292,644 |
| Remaining navigation HTML with updated source pins | 0 |
| **Complete net growth** | **46,965,336** |

The non-download growth is 3,384,721 bytes. Source-pin rebinding also changes existing navigation bytes without changing their lengths; those modified files remain in the complete accounting. Git-tree accounting includes all tracked paths regardless of ignore rules and refuses non-blob entries under the site prefix.

## Bounded limits and retained guards

Only `site_total_bytes` changes from 450,000,000 to **500,000,000**, and `generated_file_count` from 36,000 to **37,000**. Against the measured pre-pagination site, the resulting headroom is **6,549,804 bytes and 521 files**. Final pagination adds generated pages and must be remeasured before the final-head site/QC gate; these are explicitly pre-pagination figures.

Unchanged guards are: largest HTML 300,000 bytes; landing HTML 140,000 bytes; uncompressed catalogue 3,000,000 bytes; compressed catalogue 400,000 bytes; compressed initial load 450,000 bytes; minimum site size 10 files; and each declared group minimum of 1. The site checker and scientific/source data are unchanged by this capacity fix.

The retained `review-queue-archive-budget-20261116-native.json` records an actual native check of the measured generated site. Old caps reject both 493,450,196 bytes and 36,479 files. The proposed archive caps remove exactly those two errors and leave the **640,788-byte sources HTML failure** in place for #464. It is not a claim that the pre-pagination site passes the complete contract. The measured compressed initial load is 233,029 bytes and compressed catalogue is 214,163 bytes.

## Reproduction and verification

```bash
uv run --locked python scripts/adhoc/audit_site_archive_growth.py \
  --repo "$REVIEW_ROOT" \
  --base a030cca0dae2771e961ae12474c24c47a32b1363 \
  --head c7de1a2a1f4d552e196f7da5fe0d280682c3c5a1 \
  --preserved-source-index docs/provenance/review-queue-20261116.json \
  --budgets-relative conf/pages_budgets.json \
  --output .temp/review-queue-archive-accounting.json.gz
```

Set `REVIEW_ROOT` to the explicit repository path and run from that worktree. The helper reads commit objects and writes only its requested diagnostic output; it does not fetch, render, mutate Git, change guards or perform research.

`tests/test_site_archive_budget.py` exercises native byte and file-count acceptance at the exact boundary and rejection one unit over. It also binds this real candidate measurement to the revised capacity, preserves all other configuration guards, and distinguishes added, modified, deleted and unchanged files in the accounting helper. Mutation controls and full final-head checks remain explicit validation steps; no deployment, merge or scientific approval follows from a capacity adjustment.

## Retained diagnostics and mutation controls

Independent review identified that the original native capacity receipt was generated inline. Its exact bytes are preserved in `review-queue-archive-budget-20261116-native-original.json.gz`; the original hash and explicit replay details are in `review-queue-archive-budget-20261116-native-provenance.json`. The retained `scripts/adhoc/diagnose_site_archive_budget.py` verifies every frozen generated file against the measured commit, rejects symlink/nonregular/mode differences, and checks that the actually executed native contract bytes match the verified source. Its rerun preserves every computed result; only actual execution-time/helper/provenance metadata is added or refreshed. No historical receipt is silently restamped.

The seven focused regressions pass. `scripts/adhoc/verify_archive_budget_mutations.py` runs private copies in separate Python processes outside the source checkout, with fresh bytecode caches and explicit durable fixtures. The unchanged control passes all seven tests; all seven mutations fail their intended assertion: rejecting byte/file equality, accepting byte/file excess, restoring old caps, omitting modified-file growth, and ignoring a non-blob site entry. Checksummed results and copied-input hashes are in `review-queue-archive-budget-20261116-mutations.json`. Private per-process logs remain retained outside the public repository.

## Final regenerated-site capacity readback

After the separate #464 pagination, the maintained native command
`uv run --no-sync python -m dufmech.site_contract --site pages --budgets conf/pages_budgets.json`
passes with **zero errors**. Its exact JSON stdout is retained as
`review-queue-archive-budget-20261116-final-native.json` (SHA-256 `2c4970c8937104a16736fd29f008723b7dc3569362fcb840f313478c6a7fcff8`).

The resulting archive has **36,503 files and 493,620,712 bytes**, an additional
24 files and 170,516 bytes versus the measured pre-pagination consolidation.
Final remaining capacity is **497 files and 6,379,288 bytes**. There are 8,659
HTML pages; the largest is 236,321 bytes, within the unchanged 300,000-byte limit.
Compressed initial load remains 233,029 bytes and compressed catalogue remains
214,163 bytes. These are readbacks of the regenerated working tree, not a claim
that the earlier c7de commit already contains pagination. Final committed-tree
accounting can be repeated with the generic auditor against the resulting commit.

The retained generator for this final receipt is the existing unchanged
`src/dufmech/site_contract.py`; it performs no rendering or mutation. No additional
guard is loosened. Full exact-head QC, independent review and hosted checks remain
required before closure or any separately authorized publication.
