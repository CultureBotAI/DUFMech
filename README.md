# DUFMech

Domain of Unknown Function mechanism knowledge base.

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

## Scope

DUFMech records domains, protein families, and evidence layers that help
decide whether a family or representative protein is still uncharacterized.
The initial source stack is:

- InterPro/Pfam for DUF-family discovery.
- UniProtKB and UniRef for reference-proteome members.
- MGnify Proteins for environmental representatives.
- AlphaFold DB, PDB, PDBe-KB, CATH-Gene3D, CDD, STRING, eggNOG, EFI-GNT, JGI
  IMG, Rhea, GO, and QuickGO as follow-on structure, neighborhood, network,
  and function-evidence layers.

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
├── scripts/
├── src/dufmech/
└── tests/
```
