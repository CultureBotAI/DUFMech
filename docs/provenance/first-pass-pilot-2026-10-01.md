# First-Pass DUF Evidence Snapshot Pilot, 2026-10-01

This bounded live pilot expanded one InterPro/Pfam DUF family from the frozen
`interpro-pfam-duf-2026-10-01` worklist, joined the resulting UniProt accessions
against the available evidence snapshotters, and scored the full 6,532-family
DUF worklist against the evidence that was successfully frozen.

The pilot outputs were written outside the repository to:

```text
/private/tmp/dufmech-first-pass-pilot-2026-10-01
```

## Seed Slices

| Snapshot ID | Seed snapshot | Limits | Rows | Notes |
| --- | --- | --- | ---: | --- |
| `pfam-uniprot-uniref90-2026-10-01` | `interpro-pfam-duf-2026-10-01` | `--limit-families 1`, `--limit-members-per-family 3` | 3 | Three `PF04149` UniProt accessions with UniRef90 clusters |
| `pfam-mgnify-proteins-2026-10-01` | `interpro-pfam-duf-2026-10-01` | `--limit-families 1`, `--limit-proteins-per-family 3` | 3 | Two full-length and one fragment MGnify protein rows |

The UniProt/UniRef seed selected these unreviewed
`Cryptosporangium arvum DSM 44712` proteins:

- `A0A010YFW0`, `UniRef90_A0A010YFW0`, `CryarDRAFT_0138`
- `A0A010YYK3`, `UniRef90_A0A010YYK3`, `CryarDRAFT_1344`
- `A0A010Z1I9`, `UniRef90_A0A010Z1I9`, `CryarDRAFT_2378`

## Evidence Snapshots

| Snapshot ID | Seed snapshot | Limits | Rows | Notes |
| --- | --- | --- | ---: | --- |
| `uniprot-alphafold-2026-10-01` | `pfam-uniprot-uniref90-2026-10-01` | `--limit-accessions 3` | 3 | Three AlphaFold DB monomer rows |
| `uniprot-cdsearch-2026-10-01` | `pfam-uniprot-uniref90-2026-10-01` | `--limit-accessions 3` | 0 | NCBI Batch CD-Search returned no CDD rows |
| `uniprot-3dbeacons-2026-10-01` | `pfam-uniprot-uniref90-2026-10-01` | `--limit-accessions 3` | 5 | Five AlphaFold DB rows from 3D-Beacons |
| `uniprot-uniparc-2026-10-01` | `pfam-uniprot-uniref90-2026-10-01` | `--limit-accessions 3` | 3 | Three UniParc rows with Pfam features and no Gene3D features |
| `uniprot-rcsb-pdb-2026-10-01` | `pfam-uniprot-uniref90-2026-10-01` | `--limit-accessions 3`, `--limit-entities-per-accession 3` | 0 | RCSB found no experimental PDB polymer entities |
| `uniprot-rhea-2026-10-01` | `pfam-uniprot-uniref90-2026-10-01` | `--limit-accessions 3`, `--limit-reactions-per-accession 3` | 0 | Rhea found no cross-referenced reactions |
| `uniprot-quickgo-mf-2026-10-01` | `pfam-uniprot-uniref90-2026-10-01` | `--limit-accessions 3`, `--limit-annotations-per-accession 3` | 0 | QuickGO found no molecular-function annotations |
| `uniprot-pdbe-kb-2026-10-01` | `uniprot-rcsb-pdb-2026-10-01` | `--limit-structures 3` | 0 | The empty RCSB snapshot produced an empty, valid PDBe-KB snapshot |

No explicit rate-limit responses were observed from the successful API-backed
snapshotters.

## Score Snapshot

| Snapshot ID | Inputs | Rows | Notes |
| --- | --- | ---: | --- |
| `duf-characterization-scores-2026-10-01` | `interpro-pfam-duf-2026-10-01`, `pfam-uniprot-uniref90-2026-10-01`, AlphaFold, CD-Search, PDBe-KB, QuickGO, RCSB, Rhea, 3D-Beacons | 6,532 | 1,999 `KNOWN_HISTORICAL_DUF`, 4,533 `UNKNOWN_CANDIDATE`, one family with context evidence |

The score run intentionally omitted CATH-Gene3D and STRING because the pilot did
not produce frozen CATH or STRING files.

## Service Failures

### CATH-Gene3D

The bounded CATH snapshot failed before writing a snapshot:

```bash
just freeze-duf-puf-cath \
  --input-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-accessions 3 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-first-pass-pilot-2026-10-01
```

CATH returned HTTP 504 while fetching:

```text
https://www.cathdb.info/version/v4_4_0/api/rest/uniprot_to_funfam/A0A010YFW0?content-type=application%2Fjson
```

The snapshotter exited with:

```text
CathClientError: could not fetch CATH FunFam assignments for A0A010YFW0
```

### STRING

The bounded STRING snapshot also failed before writing a snapshot:

```bash
just freeze-duf-puf-string \
  --input-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-seeds 3 \
  --limit-partners-per-protein 3 \
  --required-score 400 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-first-pass-pilot-2026-10-01
```

STRING returned HTTP 400 from `get_string_ids` for accession `A0A010YFW0` in
taxon `927661`. A direct replay showed that STRING v12 does not know organism
`927661`, so the failure is a seed taxon coverage miss rather than an API rate
limit.

## Commands

```bash
just freeze-duf-puf-members \
  --input-json data/worklists/interpro-pfam-duf-2026-10-01.json \
  --limit-families 1 \
  --limit-members-per-family 3 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-first-pass-pilot-2026-10-01

just freeze-duf-puf-mgnify \
  --input-json data/worklists/interpro-pfam-duf-2026-10-01.json \
  --limit-families 1 \
  --limit-proteins-per-family 3 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-first-pass-pilot-2026-10-01

just freeze-duf-puf-alphafold \
  --input-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-accessions 3 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-first-pass-pilot-2026-10-01

just freeze-duf-puf-cdsearch \
  --input-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-accessions 3 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-first-pass-pilot-2026-10-01

just freeze-duf-puf-threedbeacons \
  --input-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-accessions 3 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-first-pass-pilot-2026-10-01

just freeze-duf-puf-uniparc \
  --input-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-accessions 3 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-first-pass-pilot-2026-10-01

just freeze-duf-puf-rcsb \
  --input-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-accessions 3 \
  --limit-entities-per-accession 3 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-first-pass-pilot-2026-10-01

just freeze-duf-puf-rhea \
  --input-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-accessions 3 \
  --limit-reactions-per-accession 3 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-first-pass-pilot-2026-10-01

just freeze-duf-puf-quickgo \
  --input-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-accessions 3 \
  --limit-annotations-per-accession 3 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-first-pass-pilot-2026-10-01

just freeze-duf-puf-pdbe-kb \
  --input-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/uniprot-rcsb-pdb-2026-10-01.json \
  --limit-structures 3 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-first-pass-pilot-2026-10-01

just score-duf-puf \
  --worklist-json data/worklists/interpro-pfam-duf-2026-10-01.json \
  --member-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --alphafold-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/uniprot-alphafold-2026-10-01.json \
  --cdsearch-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/uniprot-cdsearch-2026-10-01.json \
  --pdbe-kb-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/uniprot-pdbe-kb-2026-10-01.json \
  --quickgo-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/uniprot-quickgo-mf-2026-10-01.json \
  --rcsb-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/uniprot-rcsb-pdb-2026-10-01.json \
  --rhea-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/uniprot-rhea-2026-10-01.json \
  --threedbeacons-json /private/tmp/dufmech-first-pass-pilot-2026-10-01/uniprot-3dbeacons-2026-10-01.json \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-first-pass-pilot-2026-10-01
```
