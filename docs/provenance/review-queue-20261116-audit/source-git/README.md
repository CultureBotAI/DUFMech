# Historical review source object inventory

Date: 2026-11-16. Related infrastructure issues: [#459](https://github.com/CultureBotAI/DUFMech/issues/459) and [#460](https://github.com/CultureBotAI/DUFMech/issues/460).

The retained diagnostic helper is `scripts/adhoc/inventory_review_git_refs.py`.
It reads every authoritative structured review YAML and legacy review Markdown,
including hidden and ignored files, and checks whether each declared source Git
commit is available locally. It reads a saved public remote-tag snapshot; it does
not fetch objects, change Git refs, edit reviews, or make a scientific assessment.

The initial inventory covers 1,237 reviews and 68 source revisions, of which 33
were absent from this local object store. This was an incomplete local checkout
of historical provenance, not an instruction to alter or waive source evidence.
The original compressed inventory is byte-preserved. Fetching the 77 verified
public `source/dufmech-*` tag histories restored 32 of those commits. The remaining
legacy PF04149 source commit is retained by historical PR #109's public head,
`48c82308e7187ff9f39039541a54a9c933c984e1`, as established by the retained ancestry
proof. No review YAML, derived Markdown, record, status, or provenance assertion
was changed to repair local object availability.

`remote-tags.txt` contains the exact public tag snapshot. The public ancestry
proof omits local ref names while retaining remote tag names, tag-object hashes,
peeled commit hashes and the tested source ancestry. `packaging.json` records the
original and projected output hashes and explains that projection. The original
private diagnostic evidence remains retained separately.

The original helper is preserved in `original-inventory_review_git_refs.py.gz`.
Packaging sets executable mode and makes the existing `subprocess.run`
`check=False` behavior explicit for lint. The original and packaged helper hashes,
validation, and decompressed output hashes are recorded beside these files.
Gzip timestamps are fixed at zero; compression does not alter the retained bytes.

The helper's only outputs are JSON diagnostics and a stdout summary. Supply an
explicit repository root, `--remote-tags` snapshot and durable `--output`
directory. Run it using the repository's existing Python environment. Repository
writes, fetches and any later publication remain separate authorized operations.

Final readback verifies all **68 source commits for 1,237 reviews** are available,
with zero parse errors. Both original and packaged helpers produce identical
results after excluding only the timestamp and helper-hash metadata. The final
inventories, validation receipt and original helper bytes are retained here;
`SHA256SUMS.json` records archive and decompressed hashes.
