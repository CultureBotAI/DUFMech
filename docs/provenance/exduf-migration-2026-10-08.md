# EX_DUF migration, 2026-10-08

`interpro-pfam-duf-2026-10-08` applies the EX_DUF migration (`dufmech.exduf`, added in
PR #146) to `interpro-pfam-duf-2026-10-05`, using the Pfam 38.2 previous-identifier
snapshot `pfam-previous-unknown-names-2026-10-07`.

```bash
just migrate-exduf \
  --parent-json data/worklists/interpro-pfam-duf-2026-10-05.json \
  --previous-names-json data/worklists/pfam-previous-unknown-names-2026-10-07.json \
  --snapshot-date 2026-10-08 --apply
```

A dry run of the same command came first, followed by a canary that fetched two
entries (PF14337, PF09369) through the same InterPro client and adapter. Then the
full run made 1,763 anonymous per-accession requests to the InterPro Pfam entry API
(`fetched_at 2026-10-08T02:48:09Z`, about five minutes). Every requested family
was found.

| Seed status | 2026-10-05 | 2026-10-08 |
| --- | ---: | ---: |
| UNKNOWN_CANDIDATE | 6,154 | 6,127 |
| KNOWN_HISTORICAL_DUF | 378 | 373 |
| EX_DUF | — | 1,795 |
| **Families** | **6,532** | **8,295** |

- **32 existing families became EX_DUF** (27 from UNKNOWN_CANDIDATE and 5 from
  KNOWN_HISTORICAL_DUF). Pfam renamed these away from a DUF/UPF name, although a
  DUF number can remain in their descriptive names (e.g. "Cupin superfamily (DUF985)").
  Their names, descriptions, identifiers and counters are unchanged.
- **1,763 families were added as EX_DUF**, with metadata from the InterPro entry API.
  Of the 1,795 EX_DUF families, 1,777 are integrated into an InterPro entry.
- Two still DUF/UPF-named families with a former DUF name (PF18141 UPF1_1B_dom and
  PF21084 WHD_DUF4423_like) are not ex-DUFs, so they are not added.

The manifest records both parents with file hashes, every status change, the added
families, and the live fetch. The verified-input loader accepts it as lineage profile
`exduf-migration-v1`.

## Downstream regeneration

- `data/families/` now holds 8,295 projections (`just records --apply`), all SEEDED.
- `conf/id_labels/` was regenerated with the pinned CLAW OAK runtime: 8,295 `OK_CANONICAL`.
- KGX/SSSOM exports: 16,532 nodes and 8,237 InterPro mappings.
- `cross-mech-duf-examples-2026-10-08` relabels the 10-06 snapshot's seed statuses from
  this worklist with `python -m dufmech.cross_mech_snapshot`. This is offline, with no
  new scan or UniProt retrieval; 190 rows changed. Source Mech commits and lookup times
  remain those of the October 5 acquisition. Unmatched-name rows (e.g. DUF1998) keep
  `NOT_IN_WORKLIST`, because resolving them would mean a new scan of a source that is
  still `BLOCKED`. The report maps them through Pfam previous identifiers instead.
- The `pfam-uniprot-uniref90-2026-10-07` member snapshot, seeded on 10-05, still
  applies. The site now accepts members seeded on a metadata-preserving ancestor (text
  reclassification, or a migration without a live refresh), provided every member
  family is still in the worklist.
- `conf/pages_budgets.json` raises `generated_file_count` from 25,000 to 30,000. Each
  family adds three site files.

## Interpretation limits

EX_DUF records Pfam naming history. A rename usually follows published work on some
members, but it is not experimental evidence of function for every member, and the
added families have not been individually reviewed. Scoring treats an EX_DUF seed like a
historical DUF (`KNOWN_HISTORICAL_DUF`, reason `pfam_renamed_from_unknown_name`).
