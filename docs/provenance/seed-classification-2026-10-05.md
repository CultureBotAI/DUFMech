# Seed classification correction, 2026-10-05

The 2026-10-05 worklist reclassifies the frozen 2026-10-01 InterPro/Pfam
metadata; it is **not a new API retrieval**. Names, descriptions, identifiers,
family membership and every numeric counter are unchanged. The October 1 JSON,
TSV and manifest remain byte-identical.

The previous rule recognized domain/protein wording but missed `Family of
unknown function`. Name-based candidate matching now recognizes explicit
`unknown function` wording regardless of whether the name calls the family a
repeat, region, domain or protein. Description matching also recognizes
`the function of this family is unknown`. Capitalization, whitespace and the
`unknown-function` spelling are handled consistently.

Of 6,532 families, 1,621 seed statuses change from `KNOWN_HISTORICAL_DUF` to
`UNKNOWN_CANDIDATE`: all 1,618 historical rows whose names explicitly said
`unknown function`, plus PF16270, PF07066 and PF07232, whose frozen descriptions
say the function of the family is unknown. The resulting counts are 6,154
candidates and 378 historical DUFs. This is a correction to a naming heuristic,
not evidence of experimental characterization; all families remain unscored.

The new manifest records the original input ID and SHA-256, original retrieval
timestamp, classification policy and each changed classification/reason list.
The dashboard and README are generated from the new snapshot. Its download
includes the full index and the source snapshot ID.

Reproduction (the command is a dry run unless `--apply` is supplied):

```bash
uv run python scripts/reclassify_worklist.py \
  --source data/worklists/interpro-pfam-duf-2026-10-01.json \
  --snapshot-date 2026-10-05
```

The writer refuses to overwrite an existing version. To repeat the derivation,
provide `--out` pointing at an empty temporary directory; the source snapshot's
manifest and checksums are verified before any output is written.
