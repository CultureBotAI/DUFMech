# Seed Classification Correction, 2026-10-05

This is an offline correction of the classifier applied to
`interpro-pfam-duf-2026-10-01`, not a new InterPro retrieval or a literature
curation. The original JSON, TSV, and manifest remain unchanged. All 6,532
families, identifiers, names, descriptions, source URLs, and counters are
preserved in the new `interpro-pfam-duf-2026-10-05` snapshot. Only
`unknown_status` and `candidate_reasons` can change. The snapshot published
in PR #93 is retained byte-for-byte, including its original row ordering and
manifest. The hardened correction command produces the same family records
in status/protein-count/accession order, with expanded provenance for new runs.

## Defect And Policy

[Issue #83](https://github.com/CultureBotAI/DUFMech/issues/83) identified
`PF18701`, whose frozen name is `Family of unknown function (DUF5641)` but
whose seed label was `KNOWN_HISTORICAL_DUF`. The original phrase matcher
recognized domain/protein wording but missed family wording. The corpus
audit found 1,618 historical rows with `unknown function` in their names.

Policy `unknown-function-metadata-v2`:

- A family name containing the explicit phrase `unknown function` is a seed
  signal regardless of entity noun, including family, domain, protein,
  repeat, or region. Case, whitespace, HTML formatting, and `unknown-function`
  spelling do not change that signal.
- Descriptions retain the narrower domain/protein phrase rules and now also
  recognize family/families wording and `function of this/the family is unknown`.
  Descriptions can discuss other entities; a bare mention of unknown function
  elsewhere in a paragraph is not sufficient under this policy.
- Recognized unknown-function wording yields `UNKNOWN_CANDIDATE`. A DUF name
  without such wording yields `KNOWN_HISTORICAL_DUF`; no recognized signal
  yields `FALSE_POSITIVE_TEXT_HIT`. Reclassification retains all input rows,
  including false positives, rather than silently deleting them.
- These are lexical triage labels, not biological truth assertions. In
  particular, the historical label is not evidence that a function is known.
  Negation, historical discussion, and conflicting descriptions still require
  curator review. A candidate label does not prove lack of experimental work.

## Audited Changes

| Seed status | Original | Corrected |
| --- | ---: | ---: |
| UNKNOWN_CANDIDATE | 4,533 | 6,154 |
| KNOWN_HISTORICAL_DUF | 1,999 | 378 |
| Total | 6,532 | 6,532 |

All 1,621 status changes are historical-to-candidate transitions. Of these,
1,618 have names containing `unknown function`; three additional rows have
explicit family wording in their descriptions:

| Pfam | Frozen name | Newly recognized statement |
| --- | --- | --- |
| PF16270 | Lipocalin-like domain (DUF4923) | The function of this family is unknown. |
| PF07066 | Lactococcus phage M3 protein | The function of this family is unknown. |
| PF07232 | Putative rep protein (DUF1424) | The function of this family is unknown. |

Candidate-reason lists change for 2,101 rows, including already-candidate
families gaining an additional explanation. No corrected historical row has
the literal phrase `unknown function` in its name. This does not certify the
remaining 378 families as characterized.

## Provenance And Reproduction

The published manifest retains its per-family `reclassification` audit from
PR #93. Newly generated correction manifests use a `derivation` block recording
the parent snapshot identity, its generation time, classifier policy, transition
counts, and the byte size and SHA-256 of all three parent artifacts. Parent
JSON SHA-256:

```text
141fd83d020563444c6498a3f0dc4d7924e7cf759647b449271f4d00c612b689
```

The correction command verifies the parent manifest, rejects malformed or
duplicate worklist rows, requires a later snapshot date, and refuses to
overwrite any existing output artifact. It makes no network requests:

```bash
just reclassify-duf-puf-worklist \
  --input-json data/worklists/interpro-pfam-duf-2026-10-01.json \
  --snapshot-date 2026-10-05 --out-dir /tmp/dufmech-classification-check
```

The output JSON and TSV are deterministic. The manifest generation time records
the actual reclassification run. Regression tests verify byte-identical outputs
for repeated runs with the same inputs and generation time, equality of all
family records with the published correction, preservation of the published
files, and the original JSON hash. Re-running does not reproduce the older
manifest format or row ordering; it must not replace the published snapshot.

The legacy `scripts/reclassify_worklist.py` command retains its `--source`,
`--out`, and `--apply` interface and dry-run default. Both commands now use the
same verified preparation and exclusive writer. Unknown fields and duplicate
families are rejected, and the complete correction manifest is prepared before
any output is opened rather than rewriting a base manifest after publication.

No score snapshot was generated or relabeled by this correction. The current
dashboard therefore still marks all families `UNSCORED`. Scores derived from
the old worklist must be regenerated, not silently attached to the corrected
worklist. PR #68 supplied an explicit cross-Mech lineage update in
`cross-mech-duf-examples-2026-10-06`; that snapshot and its inputs remain unchanged.
