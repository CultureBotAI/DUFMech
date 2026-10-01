# Expanded First-Pass DUF Evidence Freeze, 2026-10-01

This expanded live run froze three InterPro/Pfam DUF families from
`interpro-pfam-duf-2026-10-01`, joined twelve UniProt accessions against the
API-backed evidence sources, and scored all 6,532 frozen DUF/Pfam families.

The live outputs were written outside the repository to:

```text
/private/tmp/dufmech-expanded-first-pass-2026-10-01
```

## Bounds

The root slices used these limits:

| Slice | Limits | Rows | Families |
| --- | --- | ---: | --- |
| Pfam to UniProtKB/UniRef90 | `--limit-families 3`, `--limit-members-per-family 4` | 12 | `PF01882`, `PF04149`, `PF19054` |
| Pfam to MGnify Proteins | `--limit-families 3`, `--limit-proteins-per-family 4` | 12 | `PF01882`, `PF04149`, `PF19054` |

The UniProt/UniRef90 slice covered:

| Pfam | UniProt accession | Taxon | Gene | UniRef90 |
| --- | --- | --- | --- | --- |
| `PF01882` | `A0A010YI93` | `927661` | `CryarDRAFT_1045` | `UniRef90_A0A010YI93` |
| `PF01882` | `A0A010Z4E0` | `927661` | `CryarDRAFT_3399` | `UniRef90_A0A010Z4E0` |
| `PF01882` | `A0A011AEU5` | `927661` | `CryarDRAFT_1641` | `UniRef90_A0A011AEU5` |
| `PF01882` | `A0A011PM99` | `1454001` | `AW08_02010` | `UniRef90_A0A011PM99` |
| `PF04149` | `A0A010YFW0` | `927661` | `CryarDRAFT_0138` | `UniRef90_A0A010YFW0` |
| `PF04149` | `A0A010YYK3` | `927661` | `CryarDRAFT_1344` | `UniRef90_A0A010YYK3` |
| `PF04149` | `A0A010Z1I9` | `927661` | `CryarDRAFT_2378` | `UniRef90_A0A010Z1I9` |
| `PF04149` | `A0A010ZQS5` | `927661` | `CryarDRAFT_0603` | `UniRef90_A0A010ZQS5` |
| `PF19054` | `A0A010YLD5` | `927661` | `CryarDRAFT_2140` | `UniRef90_A0A010YLD5` |
| `PF19054` | `A0A010YX02` | `927661` | `CryarDRAFT_0726` | `UniRef90_A0A010YX02` |
| `PF19054` | `A0A010ZSU9` | `927661` | `CryarDRAFT_1343` | `UniRef90_A0A010ZSU9` |
| `PF19054` | `A0A011AAR5` | `927661` | `CryarDRAFT_0139` | `UniRef90_A0A011AAR5` |

The MGnify slice found 12 unique MGYP accessions: eight full-length proteins
and four fragments.

## Evidence Snapshots

| Snapshot ID | Seed snapshot | Limits | Rows | Notes |
| --- | --- | --- | ---: | --- |
| `uniprot-alphafold-2026-10-01` | `pfam-uniprot-uniref90-2026-10-01` | `--limit-accessions 12` | 12 | One AlphaFold DB model per accession |
| `uniprot-3dbeacons-2026-10-01` | `pfam-uniprot-uniref90-2026-10-01` | `--limit-accessions 12` | 19 | 3D-Beacons AlphaFold DB rows for all 12 accessions |
| `uniprot-uniparc-2026-10-01` | `pfam-uniprot-uniref90-2026-10-01` | `--limit-accessions 12` | 12 | One UniParc row per accession |
| `uniprot-cdsearch-2026-10-01` | `pfam-uniprot-uniref90-2026-10-01` | `--limit-accessions 12` | 0 | NCBI Batch CD-Search found no CDD rows |
| `uniprot-cath-funfam-v4_4_0-2026-10-01` | `pfam-uniprot-uniref90-2026-10-01` | `--limit-accessions 12`, `--skip-failures` | 0 | CATH returned no rows and recorded four persistent fetch failures |
| `uniprot-rcsb-pdb-2026-10-01` | `pfam-uniprot-uniref90-2026-10-01` | `--limit-accessions 12`, `--limit-entities-per-accession 4` | 0 | RCSB found no experimental PDB polymer entities |
| `uniprot-rhea-2026-10-01` | `pfam-uniprot-uniref90-2026-10-01` | `--limit-accessions 12`, `--limit-reactions-per-accession 4` | 0 | Rhea found no cross-referenced reactions |
| `uniprot-quickgo-mf-2026-10-01` | `pfam-uniprot-uniref90-2026-10-01` | `--limit-accessions 12`, `--limit-annotations-per-accession 4` | 4 | Four `GO:0003677` annotations for `PF19054` accessions |
| `uniprot-string-2026-10-01` | `pfam-uniprot-uniref90-2026-10-01` | `--limit-seeds 12`, `--limit-partners-per-protein 4`, `--required-score 400` | 4 | Four partners for `A0A011PM99` in taxon `1454001` |
| `uniprot-pdbe-kb-2026-10-01` | `uniprot-rcsb-pdb-2026-10-01` | `--limit-structures 4` | 0 | The empty RCSB snapshot produced an empty, valid PDBe-KB snapshot |

The CATH run recorded persistent fetch failures for:

- `A0A010YI93`
- `A0A010Z4E0`
- `A0A011AEU5`
- `A0A011PM99`

No explicit rate-limit responses were observed from the successful API-backed
snapshotters.

## eggNOG

This run did not include eggNOG-mapper annotations because no saved
`.emapper.annotations` table was present in the checkout. The absence check used
an ignored-file-inclusive search:

```bash
rg --files --no-ignore --hidden -g '!.git' -g '*emapper*' -g '*eggnog*' .
```

The only matches were the eggNOG freezer source, tests, Python bytecode caches,
and the installed `.venv/bin/duf-puf-freeze-eggnog` wrapper.

## Score Snapshot

| Snapshot ID | Rows | Inputs | Notes |
| --- | ---: | --- | --- |
| `duf-characterization-scores-2026-10-01` | 6,532 | InterPro/Pfam, UniProt/UniRef90, MGnify, AlphaFold, CATH-Gene3D, CD-Search, PDBe-KB, QuickGO, RCSB, Rhea, STRING, 3D-Beacons | 1,999 `KNOWN_HISTORICAL_DUF`, one `PARTIALLY_CHARACTERIZED`, 4,532 `UNKNOWN_CANDIDATE` |

The three seeded families received these counts:

| Pfam | Status | Members | MGYPs | MGnify biomes | QuickGO MF terms | AlphaFold models | 3D-Beacons models | STRING edges | Context sources |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `PF19054` | `PARTIALLY_CHARACTERIZED` | 4 | 4 | 2 | 1 | 4 | 8 | 0 | `mgnify`, `alphafold`, `3dbeacons` |
| `PF01882` | `UNKNOWN_CANDIDATE` | 4 | 4 | 9 | 0 | 4 | 4 | 4 | `mgnify`, `alphafold`, `3dbeacons`, `string` |
| `PF04149` | `UNKNOWN_CANDIDATE` | 4 | 4 | 3 | 0 | 4 | 7 | 0 | `mgnify`, `alphafold`, `3dbeacons` |

## Commands

```bash
just freeze-duf-puf-members \
  --input-json data/worklists/interpro-pfam-duf-2026-10-01.json \
  --limit-families 3 \
  --limit-members-per-family 4 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-expanded-first-pass-2026-10-01

just freeze-duf-puf-mgnify \
  --input-json data/worklists/interpro-pfam-duf-2026-10-01.json \
  --limit-families 3 \
  --limit-proteins-per-family 4 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-expanded-first-pass-2026-10-01

just freeze-duf-puf-alphafold \
  --input-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-accessions 12 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-expanded-first-pass-2026-10-01

just freeze-duf-puf-threedbeacons \
  --input-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-accessions 12 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-expanded-first-pass-2026-10-01

just freeze-duf-puf-uniparc \
  --input-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-accessions 12 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-expanded-first-pass-2026-10-01

just freeze-duf-puf-cath \
  --input-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-accessions 12 \
  --skip-failures \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-expanded-first-pass-2026-10-01

just freeze-duf-puf-cdsearch \
  --input-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-accessions 12 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-expanded-first-pass-2026-10-01

just freeze-duf-puf-rcsb \
  --input-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-accessions 12 \
  --limit-entities-per-accession 4 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-expanded-first-pass-2026-10-01

just freeze-duf-puf-rhea \
  --input-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-accessions 12 \
  --limit-reactions-per-accession 4 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-expanded-first-pass-2026-10-01

just freeze-duf-puf-quickgo \
  --input-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-accessions 12 \
  --limit-annotations-per-accession 4 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-expanded-first-pass-2026-10-01

just freeze-duf-puf-string \
  --input-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --limit-seeds 12 \
  --limit-partners-per-protein 4 \
  --required-score 400 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-expanded-first-pass-2026-10-01

just freeze-duf-puf-pdbe-kb \
  --input-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/uniprot-rcsb-pdb-2026-10-01.json \
  --limit-structures 4 \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-expanded-first-pass-2026-10-01

just score-duf-puf \
  --worklist-json data/worklists/interpro-pfam-duf-2026-10-01.json \
  --member-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/pfam-uniprot-uniref90-2026-10-01.json \
  --alphafold-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/uniprot-alphafold-2026-10-01.json \
  --cath-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/uniprot-cath-funfam-v4_4_0-2026-10-01.json \
  --cdsearch-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/uniprot-cdsearch-2026-10-01.json \
  --mgnify-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/pfam-mgnify-proteins-2026-10-01.json \
  --pdbe-kb-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/uniprot-pdbe-kb-2026-10-01.json \
  --quickgo-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/uniprot-quickgo-mf-2026-10-01.json \
  --rcsb-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/uniprot-rcsb-pdb-2026-10-01.json \
  --rhea-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/uniprot-rhea-2026-10-01.json \
  --string-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/uniprot-string-2026-10-01.json \
  --threedbeacons-json /private/tmp/dufmech-expanded-first-pass-2026-10-01/uniprot-3dbeacons-2026-10-01.json \
  --snapshot-date 2026-10-01 \
  --out-dir /private/tmp/dufmech-expanded-first-pass-2026-10-01
```
