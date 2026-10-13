# DUF Protein Sequence Examples

This is the first freeze. The [complete-registry follow-up](protein-examples-2026-10-13.md)
adds 57 proteins while retaining this artifact set unchanged.

## Answer And Scope

No: DUFMech did not have a stored UniProt sequence example on every family.
All 8,296 generated family records were inspected; their schema and projections
had no sequence-example field. The existing cross-Mech and example-candidate
snapshots contained accessions, not amino acid sequences. This is a statement
about those canonical records and retained candidate tables, not a claim that
no ignored research file anywhere contains a sequence.

The new reference dataset accounts for every family in
`interpro-pfam-duf-2026-10-10`:

| Measure | Count |
| --- | ---: |
| Families audited | 8,296 |
| Families with verified sequence examples | 3,106 |
| Families without a sibling protein candidate | 5,190 |
| Protein-family example pairs | 9,313 |
| Distinct UniProt proteins with retained sequences | 8,890 |
| Distinct proteins exactly mirrored from the PTM registry | 1,359 |
| Other distinct proteins acquired directly from UniProt | 7,531 |
| Candidate pairs failing current Pfam cross-reference checks | 15 |

The 15 rejected pairings remain in `unresolved`, including their source links;
they are not deleted or interpreted as evidence against family function.
Every such family also has a passing example. The 5,190 gaps mean no candidate
was found by this sibling-discovery workflow, not that UniProt lacks members.

## Sibling Sources

The scan read pinned committed YAML, never dirty sibling worktrees. It covered
the 11 repositories configured by `cross_mech.DEFAULT_MECH_SOURCES`, including
all three requested examples. AIMech and CMMMech are not configured adapters and
are outside this scan. Exact commits, paths, record counts, and per-example source
links are retained in the manifest and dataset.

| Source with passing examples | Families | Distinct proteins |
| --- | ---: | ---: |
| ProteinTraitsMech (`proteintraitsmech` checkout) | 3,093 | 8,769 |
| TraitMech | 12 | 11 |
| CellStructureMech | 16 | 29 |
| AntibioticMech | 8 | 11 |
| NaturalProductMech | 28 | 75 |
| PathwayMech | 44 | 64 |

Counts overlap across repositories. CommunityMech, CultureMech, HabitatMech,
MediaIngredientMech and TaxonMech were also scanned but supplied no passing
protein examples for this worklist through the configured adapters.

The native discovery table alone missed some PTM examples: inspecting all 8,296
Pfam-owned records found 7,393 canonical-example entries, including 58 marked
`QUALIFIED`. There were 212 record/protein/family entries absent from the legacy
`family_classifications` discovery route. The sequence importer therefore reads
the pinned Pfam-owned examples as well, and preserves qualification labels rather
than treating every field named `canonical_examples` as qualified evidence.

## Evidence And Reproduction

The acquisition uses exact primary UniProt accessions and requires a current
Pfam cross-reference, valid amino acid content, matching length and SHA-256,
sequence version, and one consistent UniProt release (`2026_03`). PTM sequences
are copied only when their hash and version match the current UniProt entry.
Inactive, merged and isoform identifiers are never silently substituted.

Retained artifact set:

- `data/protein_examples/duf-protein-examples-2026-10-12.json`
- Companion `.tsv`, `.manifest.json`, and `.queries.jsonl` files.

The manifest records all artifact hashes, the input worklist, sibling commits,
the PTM registry blob SHA-256, discovery-input hash, direct-record audit, and
actual UTC acquisition timestamps. The snapshot date uses the working date in
America/Los_Angeles; acquisition timestamps cross into October 13 UTC.
The checkpoint retains normalized API responses, including unmatched outcomes,
for offline reproduction of sequence checks. The original full cross-Mech scan
is a staging input, not an adopted replacement for older discovery snapshots;
its hash and acquisition scope are retained. Reconstruct discovery from the
manifest's exact sibling commits when the staging input is unavailable.

```bash
python -m dufmech.protein_examples \
  --worklist-json data/worklists/interpro-pfam-duf-2026-10-10.json \
  --cross-mech-json <verified-discovery-input>.json \
  --ptm-repo <mechs-root>/proteintraitsmech \
  --checkpoint data/protein_examples/duf-protein-examples-2026-10-12.queries.jsonl \
  --offline --registry-scope referenced --snapshot-date 2026-10-12 --out-dir <fresh-directory>
python scripts/check_provenance.py
```

The output is a reference dataset, not human functional curation. It does not
modify generated family YAML, overlays, curation history, scoring, or sibling
records. For example, CellStructureMech's TmaR/P0A8M6 is available for
DUF496/PF04363, while DUF397/PF04149 remains an explicit sibling-discovery gap.
Domain boundaries are not inferred from whole-protein sequences.

## Terms And Publication

The [UniProt license record](https://rest.uniprot.org/help/license) was retrieved
on October 12 (Pacific). It licenses copyrightable UniProt content under
CC BY 4.0; the dataset and sequence pages retain UniProt Consortium attribution.
Only factual sibling identifiers, commit/path references, discovery bases and
qualification labels are copied, not scientific prose or full sibling records.
This does not relicense or resolve the older combined cross-Mech source bundle.

Native site builds discover this dataset and require its explicit source pin.
Family JSON and FASTA retain all examples; the HTML table displays at most ten.
Publication remains separate: do not invent a commit or advance the source-pin
ledger until an authorized source checkpoint has actually been published.
Local previews use the lower-level renderer without claiming repository pins.

Next coverage work is direct per-family UniProt discovery for the 5,190 sibling
gaps, followed by the same sequence and Pfam checks. Existing accession-only
candidate snapshots can provide leads, but are not counted as sequence coverage.
