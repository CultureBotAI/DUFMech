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
  KNOWN_HISTORICAL_DUF). Pfam renamed their short names away from a DUF/UPF name.
  Their names, descriptions, identifiers and counters are unchanged.
- **Some EX_DUF families still mention "unknown function".** 27 of the 32 have an
  unknown-function candidate reason from their current Pfam name or description (e.g.
  PF01865, "Protein of unknown function DUF47"). Across all 1,795 EX_DUF families, 88
  have one, 29 of them from the name. A few match only because the description cites the
  former DUF name (e.g. PF14298, "previously annotated as DUF4374 (domain of unknown
  function 4374)"); refining that is tracked in issue #173. These rows keep their text
  candidate reasons. Scoring does not count the rename alone as characterization for them:
  without other known or partial evidence they get `UNKNOWN_CANDIDATE`, with reason
  `pfam_metadata_still_says_unknown_function`.
- **1,763 families were added as EX_DUF**, with metadata from the InterPro entry API.
  Of the 1,795 EX_DUF families, 1,777 are integrated into an InterPro entry.
- **Two families with a former DUF name were not added**, because the previous-names
  snapshot marks their current short names as unknown-function names:
  - PF21084 (WHD_DUF4423_like) correctly.
  - PF18141 (UPF1_1B_dom, formerly DUF5599) by mistake: the name pattern treats the
    UPF1 gene name like a UniProt UPF family. The pattern fix, a follow-up freeze and a
    migration are tracked in issue #165.

The manifest records both parents with file hashes, every status change, the added
families, and the live fetch. The verified-input loader accepts it as lineage profile
`exduf-migration-v1`.

## Downstream regeneration

- `data/families/` now holds 8,295 projections (`just records --apply`), all SEEDED.
- `conf/id_labels/` was regenerated with the pinned CLAW OAK runtime: 8,295 `OK_CANONICAL`.
- KGX/SSSOM exports: 16,532 nodes and 8,237 InterPro mappings.
- `cross-mech-duf-examples-2026-10-08` is derived offline from the 10-06 snapshot with
  `python -m dufmech.cross_mech_snapshot ... --previous-names-json`. There was no new
  scan or UniProt retrieval; source Mech commits and lookup times remain those of the
  October 5 acquisition. Every Pfam-linked row carries its family's seed label from this
  worklist, and 201 rows changed label:
  - **190 rows** keep their family and change seed status.
  - **11 rows resolved through former names.** They cited a former DUF name (DUF1814,
    DUF1998, DUF262, DUF4201, DUF4263, DUF4297, DUF4338 and DUF4393) and are resolved
    through the frozen Pfam previous identifiers to their now-EX_DUF families, with
    link basis `record_mentions_previous_pfam_name`. 11 rows that cite UniProt UPF
    names stay `NOT_IN_WORKLIST`.
  - **Coverage.** The October 5 scan searched only the 6,532 families of
    `interpro-pfam-duf-2026-10-01` (the same families as 10-05). The 1,763 added families
    were never searched. The
    manifest lists them in `coverage.unscanned_pfam_ids`. The site marks them "not
    covered by the cross-Mech scan", and the report counts them separately and lists them
    as "not scanned". Missing links for these families are not
    evidence of absence. That includes ProteinTraitsMech trait records, which do exist
    for them at the recorded commit. A new scan waits on the cross-Mech licensing review.
  - **Backfill.** Relabeled legacy rows carry an empty `cited_uniprot_accession`,
    meaning "not recorded"; the manifest records this backfill.
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
historical DUF (`KNOWN_HISTORICAL_DUF`, reason `pfam_renamed_from_unknown_name`), except
where the current Pfam metadata still says the function is unknown (see above).
