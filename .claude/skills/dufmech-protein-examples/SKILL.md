---
name: dufmech-protein-examples
description: Audit DUFMech family coverage and mirror UniProt protein sequence examples from sibling Mechs, preserving pinned provenance and explicit gaps. Use for cross-Mech protein synchronization in DUFMech, not functional curation or edits to sibling repositories.
---

# DUF Protein Examples

Work in DUFMech and read its working agreements. Keep accession discovery,
sequence availability, Pfam membership, and experimentally demonstrated function
separate. This workflow adds reference examples; it does not promote curation
status, function assertions, or causal edges.

## Audit And Discover

- Use the complete verified worklist, not only generated overlays or a UI sample.
  Existing cross-Mech links and example-candidate snapshots contain accessions,
  not necessarily stored sequences. Report those counts separately.
- Inspect sibling committed records through immutable git objects. The checkout
  is named `proteintraitsmech`, while the adapter calls it `ProteinTraitsMech`.
  Read its `data/grounding/protein_registry.jsonl` for actual sequences;
  `data/cross_mech` is a discovery inventory, not blanket trait qualification.
- Inspect the whole pinned protein registry, not only proteins already paired
  with DUFs. Qualified PTM examples can omit legacy `family_classifications`;
  the importer also reads every Pfam-owned record's `canonical_examples`, retains
  qualification labels, and discovers registry carriers using current UniProt
  Pfam cross-references. Registry presence does not qualify a protein for a DUF.
- Reuse `dufmech.cross_mech_snapshot_cli` with an explicit `--mechs-root` and
  source ref. Its configured adapters include TraitMech and CellStructureMech.
  Inspect reported source pins and scan scope; missing/unscanned repositories or
  families are not negative evidence. Do not change a dirty sibling checkout.
- Searches establishing absence include ignored and hidden files. Record the
  scope of a scan rather than claiming every protein in every Mech was found.

## Mirror Verified Examples

Use the repository pipeline after an authorized public-data acquisition:

```bash
python -m dufmech.protein_examples \
  --worklist-json data/worklists/<verified-worklist>.json \
  --cross-mech-json <verified-cross-mech-snapshot>.json \
  --ptm-repo <sibling-root>/proteintraitsmech \
  --checkpoint <staging-directory>/uniprot-sequences.jsonl \
  --snapshot-date YYYY-MM-DD --out-dir data/protein_examples
```

Use `--offline` to reproduce from a complete checkpoint. Freeze a new dated
artifact set; never overwrite retained snapshots. Preserve the checkpoint or
its reproducible minimal extracts, input manifests, and source pins.

The importer checks primary accessions, current Pfam cross-references, amino acid
content, length, SHA-256, sequence version, and a consistent UniProt release. It
mirrors a PTM registry sequence only when sequence hash and version agree with
UniProt; differing versions remain distinguished. Do not collapse isoforms or
silently replace inactive/merged accessions. Preserve every source record and
the originally cited identifier when a discovery tool resolved an accession.
Unreviewed entries may be sequence examples but are not experimental evidence.

Keep all candidates and all family gaps in the snapshot. A missing sibling
candidate is not proof that UniProt lacks a family member. Broader per-family
UniProt discovery is a separate, explicitly scoped acquisition, not a fabricated
completion count. Do not infer domain coordinates from full protein sequences.

## Verify And Present

- Run `tests/test_protein_examples.py`, relevant cross-Mech/site tests, and source
  governance checks. Verify artifact checksums and whole-worklist accounting.
- Render with `python -m dufmech.pages --protein-examples-json <snapshot> --out
  <preview>`. The site retains all examples in family JSON and FASTA, with a
  bounded display table. Check a mirrored example and a gap on desktop/mobile.
  Native default builds discover the latest sequence snapshot but require its
  published source pin; use the lower-level `render_site` for an honestly
  unpinned local preview before publication.
- Retain UniProt Consortium attribution and CC BY 4.0 terms. Do not assume a
  sibling's software license relicenses its scientific text or source datasets.
- Report families covered/total, unique proteins, direct mirrors versus fresh
  UniProt fetches, unresolved candidates, source scope and remaining gaps. Keep
  data enrichment separate from canonical human curation and publication.
- Commit, publish, edit sibling records, or advance source pins only when
  requested. Do not fabricate publication SHAs for a local preview.
