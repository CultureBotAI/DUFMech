# UniProtKB example-protein candidates, 2026-10-07

`uniprot-duf-example-candidates-2026-10-07` answers issue #79. It lists up to three
UniProtKB entries for each DUF family that a sibling Mech discusses without an example
protein carrying that family. These are **candidates for review in those Mechs, not
curated, representative or functionally characterized examples.**

```bash
uv run python scripts/freeze_example_candidates.py --snapshot-date 2026-10-07 \
  --renamed-traitmech-pfam-id PF08843 --renamed-traitmech-pfam-id PF09369 \
  --renamed-traitmech-pfam-id PF03235 --renamed-traitmech-pfam-id PF13870 \
  --renamed-traitmech-pfam-id PF14082 --renamed-traitmech-pfam-id PF14130 \
  --renamed-traitmech-pfam-id PF14236 --renamed-traitmech-pfam-id PF14337
```

## Target families

Targets come from `cross-mech-duf-examples-2026-10-06` against
`interpro-pfam-duf-2026-10-05`. Both manifests are verified before selection. Only
family IDs and reason labels are taken from the cross-Mech snapshot, whose source
row is `BLOCKED` pending its combined license review; every retained candidate
field comes from UniProtKB.

| Reason | Families |
| --- | ---: |
| ProteinTraitsMech trait record, but no canonical example carries the family | 4,786 |
| TraitMech names the family, but no TraitMech or ProteinTraitsMech protein carries it | 14 |
| TraitMech cites a former DUF name of the family (resolved via Pfam previous identifiers, issue #78) | 8 |
| **Distinct families** | **4,794** |

Reasons overlap: all 14 TraitMech-named families are also ProteinTraitsMech gaps, so
the rows sum to 4,808.

The eight renamed families are those Pfam 38.2 lists for DUF1814, DUF1998, DUF262,
DUF4201, DUF4263, DUF4297, DUF4338 and DUF4393. They are passed explicitly because
they are outside the worklist.

## Retrieval

One UniProtKB search per family: `xref:pfam-<ID>`, sorted by
`annotation_score desc,accession asc`, three results, UniProt release `2026_03`.
Raw responses were checkpointed in ignored `data/raw/` so an interrupted run resumes.
The first attempt was stopped while the UniProt REST API returned 503 for all
requests; nothing was written. After the service recovered, a one-family canary ran
through the same CLI, then the full run (107 minutes). Every response in this
snapshot was fetched in that single run: the checkpoint did not exist before it, and
all 4,794 checkpoint lines are release `2026_03` with three results per family. This
snapshot predates the manifest's `checkpoint` and `limit_families` fields. Later runs
record checkpoint reuse and fetch times, refuse to mix UniProt releases or reuse
responses made with other query settings, and refuse `--limit-families` runs into
`data/worklists/`.

| Measure | Count |
| --- | ---: |
| Families queried | 4,794 |
| Families with candidates | 4,788 |
| Families with no UniProtKB 2026_03 entry carrying the cross-reference | 6 (PF12976, PF16424, PF20318, PF24248, PF25588, PF28257) |
| Candidate rows | 14,320 |
| Distinct accessions | 13,751 |
| Families with a reviewed (Swiss-Prot) candidate | 24 |

## Interpretation limits

- **Ranking is not selection.** For 3,266 of 4,788 families the top candidate's annotation
  score is 1 (the minimum), and ties are broken by accession. Such picks are
  effectively arbitrary members.
- **Large multi-domain families surface proteins whose main identity is another
  domain.** For example, the top PF03235 (GmrSD_N) candidate is annotated as a fungal
  guanine deaminase, and PF08843 (AbiEii) as a phosphoserine phosphatase. A candidate
  carries the Pfam family according to UniProtKB cross-references; it does not show that
  the family defines the protein.
- **Reviewed candidates are rare (24 families).** Five are renamed TraitMech families,
  for example PF14130 Cap4 → C0VHC9, PF14236 DruA → P0DW34, PF14082 SduA → B7HFR2 and
  PF09369 MZB → A0R5E2 (SftH). The other 19 are ProteinTraitsMech gaps. None of the 14
  TraitMech-named DUF families has a reviewed candidate.
- Nothing is written to TraitMech or ProteinTraitsMech, and no DUFMech score, seed status
  or family record changes. Proposing examples to those repositories needs review there.

## Terms and attribution

[UniProt's license](https://rest.uniprot.org/help/license), checked on 2026-10-07,
applies CC BY 4.0 to copyrightable database content. Each row links to its UniProtKB
entry. Please cite UniProt when reusing these rows. Pfam membership comes from
UniProtKB cross-references to Pfam (CC0 via InterPro).
