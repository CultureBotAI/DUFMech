# Complete PTM Registry Follow-Up

This successor extends the [initial reference-based freeze](protein-examples-2026-10-12.md)
without replacing it. Its date is October 13 UTC, still October 12 in the user's
America/Los_Angeles working timezone. Both freezes use UniProt release `2026_03`.

## Final Coverage

| Measure | Count |
| --- | ---: |
| Worklist families audited | 8,296 |
| Families with verified sequence examples | 3,106 |
| Families without a candidate in the scanned sources | 5,190 |
| Protein-family example pairs | 9,378 |
| Distinct proteins | 8,947 |
| Exact PTM registry sequence/version mirrors | 1,416 |
| Other proteins acquired from UniProt | 7,531 |
| Rejected protein-family pairings retained | 15 |

All 12,699 proteins in the pinned PTM registry were checked, not only the ones
already linked to DUFs by trait records. All had exact current UniProt entries.
Of those, 1,416 proteins carried worklist Pfam cross-references (1,495 pairings);
11,283 had no target-family cross-reference in that release. This added 57
proteins and 65 pairings but no additional families. It also supplied an additional
PTM origin for one family already covered by another source. PTM now contributes
8,839 distinct proteins across 3,094 families; other per-Mech counts are unchanged.

The preceding discovery scan requested 2,564 non-PTM accession lookups, resolved
2,450 and retained 114 unresolved accession leads. Those unmapped leads are not
family-specific sequence examples and are not evidence of biological absence.
The complete acquisition metadata and unresolved list are retained in
`docs/provenance/protein-examples-discovery-2026-10-12.json`; this is the original
discovery manifest, not a separately adopted cross-Mech data release.

## Retention And Reproduction

The current artifact set is
`data/protein_examples/duf-protein-examples-2026-10-13.{json,tsv,manifest.json,queries.jsonl}`.
It retains the same 11 pinned sibling scans and the direct audit of all 8,296
PTM Pfam records, plus the complete registry acquisition. The first freeze is
retained unchanged. No generated family record, overlay, history event, source
pin, or sibling repository was edited.

```bash
python -m dufmech.protein_examples \
  --worklist-json data/worklists/interpro-pfam-duf-2026-10-10.json \
  --cross-mech-json <verified-discovery-input>.json \
  --ptm-repo <mechs-root>/proteintraitsmech \
  --checkpoint data/protein_examples/duf-protein-examples-2026-10-13.queries.jsonl \
  --offline --snapshot-date 2026-10-13 --out-dir <fresh-directory>
```

Registry scope defaults to `all`. `--registry-scope referenced` reproduces the
first freeze's narrower acquisition. Both datasets retain only reference
examples: membership is not evidence of biochemical function, causal mechanism,
or a specific residue's role. Rejected pairings and unreviewed metadata remain
explicit. UniProt Consortium attribution and CC BY 4.0 terms are unchanged.

## Remaining Work

- Discover direct UniProt candidates for the 5,190 family gaps and apply the
  same exact-accession, release, sequence and Pfam checks.
- Assess the 15 source/current-Pfam disagreements before promoting those pairs.
- Revisit the 114 unresolved discovery-accession leads without silently replacing
  inactive accessions or collapsing isoforms.
- Publish an authorized source checkpoint, then capture its real source pin and
  regenerate the committed site. Local previews do not claim such a checkpoint.

The reusable `dufmech-protein-examples` skill is maintained in
`.claude/skills/dufmech-protein-examples/SKILL.md` and installed in the user's
Codex skills directory. Scientific functional curation remains a separate task.

## Verification

- Full regression run: 1,311 passed, three empty-parameter skill tests skipped.
  The final focused protein-example and shell-boundary checks passed (45 tests).
- Ruff and whitespace checks passed. Both skill copies validate and are identical.
- All 14 native snapshot manifests passed integrity checks; both sequence freezes'
  JSON and TSV bytes reproduced exactly from their retained checkpoints.
- Source governance: zero errors, 16 pre-existing unresolved-license warnings.
- Seven Playwright tests passed; real Q21626 sequence-example screenshots were
  inspected at 1440px and 390px. The complete 8,296-family local preview passed
  link, reachability, contrast-token and size checks with zero errors.
- The original checkout, sibling repositories, source pins, family YAML,
  overlays and canonical history were left unchanged. No Git publication was performed.

These checks do not certify a new functional assertion or replace the publication
gate. The full `just qc` publication workflow is not claimed complete: the new
native sequence dataset still needs its published source checkpoint and the
corresponding committed-site regeneration.
