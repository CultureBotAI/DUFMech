# DUFMech

Domain of Unknown Function mechanism knowledge base.

[Browse the DUFMech dashboard](https://culturebotai.github.io/DUFMech/).

DUFMech starts from Pfam families whose public InterPro metadata still looks
like a domain or protein of unknown function. The first tool builds a
triage worklist from the InterPro Pfam API, normalizes Pfam rows, keeps DUF
short-name hits that may be historically solved, and can render TSV or JSON.

## Quick Start

Use Python 3.13 for development.

```bash
just install
just test
just duf-puf-worklist --limit 10 --format tsv
```

The worklist can also read saved InterPro JSON for offline fixture runs:

```bash
just duf-puf-worklist --input-json interpro-page.json --format json
```

Freeze the canonical InterPro/Pfam seed worklist with a matching manifest:

```bash
just freeze-duf-puf-worklist --snapshot-date 2026-10-01
```

The current seed worklist is a versioned classification correction of that
original metadata, not a newer InterPro fetch. It retains all 6,532 families
and source counters; 1,621 historical seed labels were corrected to unknown
candidates. See the [correction audit](docs/provenance/seed-classification-correction-2026-10-05.md)
for the classification policy, parent hashes, and limitations.

Reclassify verified frozen metadata into a new snapshot without contacting InterPro:

```bash
just reclassify-duf-puf-worklist \
  --input-json data/worklists/interpro-pfam-duf-2026-10-01.json \
  --snapshot-date 2026-10-05 --out-dir /tmp/dufmech-classification-check
```

Existing output artifacts are never overwritten. Seed labels reflect frozen
wording, not experimental validation. Scoring remains a separate step.

Expand frozen Pfam rows to UniProtKB protein members through InterPro:

```bash
just duf-puf-members --pfam-id PF01519 --limit-members-per-family 5
```

Freeze a Pfam member snapshot with UniProtKB metadata and UniRef clusters:

```bash
just freeze-duf-puf-members --input-json data/worklists/interpro-pfam-duf-2026-10-01.json --limit-families 1
```

Freeze MGnify Proteins environmental representatives for Pfam rows:

```bash
just freeze-duf-puf-mgnify --input-json data/worklists/interpro-pfam-duf-2026-10-01.json --limit-families 1
```

Freeze AlphaFold DB evidence for UniProt accessions:

```bash
just freeze-duf-puf-alphafold --uniprot-accession B2BDZ3
```

Freeze CATH-Gene3D FunFam evidence for UniProt accessions:

```bash
just freeze-duf-puf-cath --uniprot-accession P68871
```

Freeze NCBI Batch CD-Search conserved-domain evidence for UniProt accessions:

```bash
just freeze-duf-puf-cdsearch --uniprot-accession P68871
```

Freeze a saved NCBIFAM HMM hit table:

```bash
just freeze-duf-puf-ncbifam --hits-tsv ncbifam-hits.tsv
```

Freeze eggNOG-mapper annotations:

```bash
just freeze-duf-puf-eggnog --annotations-tsv out.emapper.annotations
```

Freeze an EFI-GNT Pfam Neighbor Mapping Table:

```bash
just freeze-duf-puf-efi-gnt --pfam-neighbors-tsv pfam-neighbors.tsv
```

Freeze a saved JGI IMG gene-neighborhood table:

```bash
just freeze-duf-puf-jgi-img --gene-neighbors-tsv img-gene-neighbors.tsv
```

Freeze 3D-Beacons structural coverage evidence for UniProt accessions:

```bash
just freeze-duf-puf-threedbeacons --uniprot-accession P75259
```

Freeze RCSB PDB experimental-structure evidence for UniProt accessions:

```bash
just freeze-duf-puf-rcsb --uniprot-accession P68871 --limit-entities-per-accession 5
```

Freeze PDBe-KB residue annotations for RCSB PDB entities:

```bash
just freeze-duf-puf-pdbe-kb --pdb-entity P68871:1A00:2 --endpoint domains
```

Freeze Rhea reactions for UniProt accessions:

```bash
just freeze-duf-puf-rhea --uniprot-accession P08159
```

Freeze QuickGO molecular-function annotations for UniProt accessions:

```bash
just freeze-duf-puf-quickgo --uniprot-accession P08159
```

Freeze STRING interaction partners for UniProt/taxon pairs:

```bash
just freeze-duf-puf-string --uniprot-taxon P68871:9606 --limit-partners-per-protein 5
```

Freeze UniParc permanent sequence archive IDs for UniProt accessions:

```bash
just freeze-duf-puf-uniparc --uniprot-accession P75259
```

Score frozen DUF/Pfam families with evidence snapshots:

```bash
just score-duf-puf --worklist-json data/worklists/interpro-pfam-duf-2026-10-01.json
```

Render and verify the committed DUFMech dashboard:

```bash
just render
just render-check
```

GitHub Actions runs the offline quality gate and builds the dashboard on pull
requests and pushes to `main`. After those checks pass, current `main` commits
publish the generated site to GitHub Pages. The workflow can also be run manually
on `main`. Publishing uses the committed frozen snapshots and does not refresh
upstream data. The repository's Pages source must be set to **GitHub Actions**.

Reports, README statistics, and pages validate the selected snapshot manifests.
Score snapshots must name the selected worklist in their input provenance;
use matching `--worklist-json` and `--score-json` paths when selecting older inputs.
Without a score snapshot, families remain `UNSCORED`, with seed status shown separately.
Missing counters remain unavailable rather than becoming zero, and per-family
protein totals are not deduplicated protein counts.

`just render` replaces only its four generated files and preserves unrelated files
in the output directory. `just render-check` compares the full output tree by content.

Run the local quality gate:

```bash
just qc
```

## Current Corpus

<!-- BEGIN GENERATED CORPUS STATS -->
<!-- Generated by scripts/check_docs.py; do not edit this block by hand. -->
**6,532 DUF/Pfam families** are currently committed from frozen InterPro/Pfam snapshots.

6,492 carry InterPro IDs, 820 have InterPro structure counters, and 6,478 have AlphaFold DB model counters.

Latest inputs: `worklist=interpro-pfam-duf-2026-10-05`.

**Unknown-function seed status**

| Value | Families |
|---|---:|
| `KNOWN_HISTORICAL_DUF` | 378 |
| `UNKNOWN_CANDIDATE` | 6,154 |

**Characterization status**

| Value | Families |
|---|---:|
| `UNSCORED` | 6,532 |

**Candidate reasons**

| Value | Families |
|---|---:|
| `description_says_unknown_function` | 1,359 |
| `domain_of_unknown_function` | 2,832 |
| `name_matches_duf` | 155 |
| `name_says_unknown_function` | 6,115 |
| `short_name_matches_duf` | 6,371 |
<!-- END GENERATED CORPUS STATS -->

## Scope

DUFMech records domains, protein families, and evidence layers that help
decide whether a family or representative protein is still uncharacterized.
The initial source stack is:

- InterPro/Pfam for DUF-family discovery.
- UniProtKB and UniRef for reference-proteome members.
- UniParc for permanent sequence IDs and checksums.
- MGnify Proteins for environmental representatives.
- AlphaFold DB, PDB, PDBe-KB, CATH-Gene3D, CDD, NCBIFAM, STRING, eggNOG,
  EFI-GNT, JGI IMG, Rhea, GO, and QuickGO as follow-on structure,
  neighborhood, network, and function-evidence layers.

The first pass deliberately treats a `DUFnnnn` Pfam short name as a clue, not
as proof that the family is still functionally unknown.

## Layout

```text
DUFMech/
├── data/
│   └── worklists/
├── docs/
│   ├── provenance/
│   └── reports/
├── pages/
├── scripts/
├── src/dufmech/
└── tests/
```

## License

Project-authored data and narrative documentation are licensed under
[CC BY 4.0](LICENSE-DATA). Project-authored code, including scripts, tests,
schemas and website templates, is licensed under [BSD-3-Clause](LICENSE-CODE).
Third-party material retains its own licenses and attribution requirements.
See [LICENSE](LICENSE) for scope and attribution.
