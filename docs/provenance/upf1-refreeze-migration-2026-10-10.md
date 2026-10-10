# UPF1 previous-name re-freeze and migration, 2026-10-10

This addresses the data-adoption portion of issue #165. PR #180 corrected the
parser; this run applies it to a fresh download of the same pinned Pfam 38.2
release and adds the formerly excluded PF18141 family. Historical snapshots
remain unchanged. This is source metadata maintenance, not scientific curation.

## Source Re-Freeze

```bash
just freeze-pfam-previous-names --pfam-release 38.2 --snapshot-date 2026-10-10
```

The native downloader read
`https://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam38.2/Pfam-A.seed.gz`
and finished at `2026-10-10T07:43:56.378519Z`. Its 194,369,799 compressed bytes
and SHA-256 `c53a1397f6741c3501f21db2179ad7810d98ddf9f3b3172257bd71ca07ba8c3b`
match the October 7 acquisition. `Last-Modified` remains January 22, 2026;
this is not a new Pfam release. All 30,134 families were scanned; only headers
were retained, not alignments.

The normalized table retains exactly the same 1,834 families and 1,845 distinct
previous unknown-function names. Exactly one field changes: PF18141's
`currently_unknown_name` is now `false`. Its current name `UPF1_1B_dom` refers to
the UPF1 gene, not a four-digit UPF family. Its retained previous identifier is
`DUF5599`. Renamed-away rows increase from 1,795 to 1,796; current unknown-name
rows decrease from 39 to 38. No names, descriptions or memberships changed.

## Worklist Migration

The same command without `--apply` first reported only one entry to fetch,
with zero changes to existing rows. The applied command was:

```bash
just migrate-exduf \
  --parent-json data/worklists/interpro-pfam-duf-2026-10-08.json \
  --previous-names-json data/worklists/pfam-previous-unknown-names-2026-10-10.json \
  --snapshot-date 2026-10-10 --apply
```

One anonymous request to the InterPro Pfam entry API retrieved PF18141,
integrated into IPR040812. The manifest records the fetch start as
`2026-10-10T07:44:21.614711Z`. All 8,295 parent rows, including their metadata,
counters, statuses and candidate reasons, are unchanged. PF18141 is the only
added family; there are no carried, missing or reclassified families.

| Seed status | October 8 | October 10 |
| --- | ---: | ---: |
| EX_DUF | 1,795 | 1,796 |
| UNKNOWN_CANDIDATE | 6,127 | 6,127 |
| KNOWN_HISTORICAL_DUF | 373 | 373 |
| Total | 8,295 | 8,296 |

The new projection remains `SEEDED` and `UNSCORED`, with no assertions or
scientific-review promotion. InterPro's description is retained as imported
metadata, not a curator-verified mechanism claim.

## Cross-Mech Compatibility

```bash
python -m dufmech.cross_mech_snapshot \
  --source-json data/cross_mech/cross-mech-duf-examples-2026-10-08.json \
  --worklist-json data/worklists/interpro-pfam-duf-2026-10-10.json \
  --snapshot-date 2026-10-10 \
  --source-git-commit 4e02d244b82862bc4b1326299822df4532078531 \
  --out-dir data/cross_mech
```

The new compatible snapshot preserves all 16,298 reference rows and their
original source metadata. Zero family labels change. Former-name mappings
retain their October 7 snapshot identity and hash; this derivation does not
claim a new mapping search. The October 5 scan's actual searched worklist
remains `interpro-pfam-duf-2026-10-01`. Unscanned families increase from 1,763
to 1,764 by adding PF18141. No missing link is treated as evidence of absence,
and no blocked sibling-source acquisition is performed.

## Remaining Classifier Adoption

The v3 text-classifier correction is intentionally not applied to the inherited
rows. Migration preserves their candidate reasons. Reclassifying this worklist
requires a new snapshot on an actual date later than October 10, followed by
another compatible cross-Mech derivation and downstream regeneration. Neither
future acquisition dates nor overwritten snapshots are used to combine the steps.

## Validation And Publication Boundary

The four release-specific tests in `tests/test_upf1_migration_release.py` verify
the exact one-field re-freeze delta, unchanged parent worklist rows, preserved
cross-Mech evidence and unscanned coverage, and the uncurated new projection.
They pass, as do the 91 existing parser/migration/lineage tests and all 12
snapshot manifest checks. Native regeneration produces 8,296 schema-valid
records, 16,534 KGX nodes and 8,238 KGX/SSSOM associations. Source governance
reports zero errors and 16 warnings; the additional warning is the new offline
derivation of the already-unverified cross-Mech source, not a license upgrade.
The subsequent record check has zero generated drift. Native export
reproducibility and the shared KGX/SSSOM contracts pass. The isolated, locked
CLAW OAK runtime returns `OK_CANONICAL` for all 8,296 ID/label pairs with network
denied. All six history records and eleven existing review reports validate.

The initial complete Python run finished with 1,280 passes, three skips and
four failures. Two failures were release-dependent test expectations: the
export census still described 8,295 families, and the report-pinning test
hard-coded the October 7 previous-name table. Both were corrected; the latter
now pins the baseline before adding a synthetic next-day snapshot. The command
recipe test also needed `CLAW_SRC` in the invoking environment, not a code fix.
After those corrections, the 95-test parser/migration/lineage/release suite,
the real-corpus offline export regression, and the actual research-recipe
regression pass. The revised projection test uses an isolated frozen-input
build so it does not prevent future curation of the live PF18141 record.
The initial full run predates these test corrections; no fresh full-green
suite, browser run or deployment is claimed.

Public release is still pending. The old source-pin ledger and generated site
are intentionally untouched at this stage. The renderer rejects changed source
bytes until the normal publication workflow retains a new checkpoint, captures
its pins and regenerates Pages. That check currently prevents a full green QC
run; it must not be bypassed or represented as passing. Publish and retain the
checkpoint only within the separately authorized PR/release workflow. The
historical snapshots, review bundles and checkpoint tags are not rewritten.

## Terms

The [official InterPro license statement](https://interpro-documentation.readthedocs.io/en/latest/license.html)
was rechecked on October 10, 2026: InterPro and Pfam downloadable data are
available under CC0 1.0. Cite the source resources. Cross-Mech terms remain
unverified; the offline derivation does not change their adoption status.
