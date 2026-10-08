# Source Catalogue, Queue And Writer Audit

`download.yaml` inventories the 20 implemented source pipelines. It was reviewed
against every existing source-freeze module, the source roadmap, the October 1
pilot reports, and the retained manifests on **2026-10-07**. The derived score
writer is covered by the writer audit; it is not a twenty-first upstream source.
No provider data is fetched by the governance checker.

## Status And Provenance

The catalogue uses CLAW's list-of-source-blocks shape, including `source`, `name`,
`url`, `license`, `status`, and bare `seeder` filenames relative to `scripts/`.
DUFMech currently has one block per pipeline. `adapter` and `writer` identify
the actual Python implementation; `scoring` names the consuming score flag or
`NOT_SCORED`. `artifacts` lists retained manifests, whose JSON and TSV content,
sizes, hashes, row counts, and manifest metadata are validated offline.

`curation/source_queue.tsv` uses the eleven shared CLAW columns plus these
declared extensions:

```text
implementation reviewed_on review_basis script artifacts license_url
```

`reviewed_on` dates the implementation/provenance inventory. `verified_on` in
the queue mirrors the catalogue's `license_verified_on` and dates a successful
primary-source license check. A report date is never substituted for a license
check. `review_basis` points to the retained report; `artifacts` contains
semicolon-separated manifest paths and is empty when none are retained.

`IMPLEMENTED` means code exists, not that source data was adopted. `ADOPTED`
requires verified redistribution terms, a verification date, a working script,
retained artifacts, and review provenance. InterPro/Pfam, the Pfam previous-identifier
table, the bounded UniProtKB/UniRef domain-view example and the UniProtKB
example-candidate table currently make that claim. `EVALUATING` retains actual external-pilot history without presenting
those results as a committed evidence release. `CANDIDATE` covers saved-table
pipelines still awaiting inputs. Queue priority 1 is highest, 5 lowest.

The legacy cross-Mech source is `enrichment` in the catalogue because its
artifacts are already present, but `BLOCKED` in the adoption queue because the
combined licensing review is unfinished. The checker warns about both retained
manifests. It does not remove, relicense, redownload, or redate historical data.

## Implemented Inventory

| Pipeline | Implemented input | Retained observation and next gate |
| --- | --- | --- |
| InterPro/Pfam | Pfam entry API | October 1 worklist, October 5 offline label correction and October 8 EX_DUF migration (1,763 added) retained; ADOPTED |
| UniProtKB/UniRef | InterPro members, UniProtKB search, ID mapping | October 7 bounded PF04149 domain-view freeze: 2 rows retained; ADOPTED as reference evidence |
| MGnify | Pfam cluster-representative API | External pilot: 12 rows; data terms unverified |
| AlphaFold DB | Prediction metadata API | External pilot: 12 rows; no committed evidence freeze |
| CATH-Gene3D | Versioned v4_4_0 FunFam API | External pilot: zero rows, four persistent failures; terms unverified |
| CDD/CD-Search | Batch submission and polling | External pilot: zero hits; selected collection terms unverified |
| NCBIFAM | Saved HMM-hit TSV | Parser/freezer/scorer implemented; actual input and data terms needed |
| eggNOG-mapper | Saved annotations TSV | Explicitly omitted from October 1 run for lack of input; data terms unverified |
| EFI-GNT | Saved Pfam Neighbor Mapping Table | Input export and its redistribution terms needed |
| JGI IMG | Saved gene-neighborhood TSV | BLOCKED pending an authorized export and project/release review |
| 3D-Beacons | UniProt summary API | External pilot: 19 AlphaFold rows; aggregated-provider terms unverified |
| RCSB PDB | Search and GraphQL experimental-entity APIs | External pilot: zero entities; no committed evidence freeze |
| PDBe-KB | PDB/entity annotation endpoints | Empty external snapshot from empty RCSB seeds; no live coverage demonstrated |
| Rhea | Reaction REST queries by UniProt | External pilot: zero reactions; primary license page not retrieved |
| QuickGO | Molecular-function annotation API | External pilot: four GO:0003677 rows; annotation contributor terms unverified |
| STRING | Pinned v12.0 API | External pilot: four partners; unsupported taxon was recorded, not treated as absence |
| UniParc | UniProt ID mapping | External pilot: 12 identity rows; no direct characterization score input |
| Pfam previous identifiers | Pinned Pfam 38.2 `Pfam-A.seed.gz` headers | October 7 freeze: 1,834 families with a former DUF/UPF name; ADOPTED as reference |
| UniProtKB example candidates | Per-family UniProtKB search by Pfam cross-reference | October 7 freeze for TraitMech and ProteinTraitsMech DUF gaps; ADOPTED as reference candidates |
| Cross-Mech | Pinned sibling git records and UniProt cache | October 5 scan and October 6 offline derivation retained; combined terms unverified |

Pilot counts above come from
[the expanded freeze report](provenance/expanded-first-pass-freeze-2026-10-01.md),
not a new run. Searches included ignored and hidden files under `data/` and
`docs/` and the two external pilot directories named in the reports. Both
external directories were empty at review time. Nothing in the queue upgrades
a lexical seed, association, structure prediction, or pilot result into
scientific curation. The retained
[cross-Mech derivation record](provenance/cross-mech-worklist-2026-10-06.md)
preserves the original acquisition dates and commits.

## Terms Review

The following primary statements were checked on 2026-10-07:

- [InterPro's license documentation](https://interpro-documentation.readthedocs.io/en/latest/license.html)
  places InterPro/Pfam downloadable data under CC0. It does not grant the same
  terms for every other member collection.
- [UniProt's license record](https://rest.uniprot.org/help/license) specifies
  CC BY 4.0 for copyrightable database content. This covers the UniProtKB/UniRef
  and UniParc catalogue entries; attribution and external rights remain relevant.
- [AlphaFold DB's data license](https://alphafold.ebi.ac.uk/assets/License-Disclaimer.pdf)
  specifies CC BY 4.0 and supports academic and commercial use.
- [RCSB's usage policy](https://www.rcsb.org/pages/policies) applies CC0 to PDB
  archive and native API data, with separate terms for integrated external data.
- [STRING's access and licensing policy](https://www.string-db.org/cgi/access?footer_active_subpage=licensing)
  specifies CC BY 4.0 for STRING outputs, preserving incorporated providers'
  rights. It calls for limited API use, bulk downloads for large requests, and
  no HTML scraping. The existing adapter pins v12.0.

The remaining twelve source entries stay `UNVERIFIED`, including cross-Mech.
[JGI's policy](https://jgi.doe.gov/data-policy-support/full-data-policy) distinguishes
embargoed and released projects and publication obligations; no particular
export was available for a release/rights review. This does not mean all IMG
data are restricted. The
[eggNOG-mapper software page](https://eggnog-mapper.cgmlab.org/about/) does not
resolve database/output rights. The
[QuickGO API documentation](https://www.ebi.ac.uk/QuickGO/api/index.html) describes
access but did not establish the annotation license. General institute terms,
public endpoints, and software licenses are not substituted for data permission.

## Offline Checks

From the repository root:

```bash
python -m dufmech.source_governance
python -m dufmech.source_governance --sources-only
python -m dufmech.source_governance --writers
python -m pytest tests/test_source_governance.py -q
```

`--root PATH` checks a different checkout. The default checks the catalogue,
queue and writer declarations, reports unresolved licenses as warnings, and
exits 1 on errors. `--writers` emits parseable JSON on stdout and diagnostics
on stderr. There is no online mode and no provider/client construction.

The shared compatibility test directly calls `kg_microbe_sources.validate` and
`kg_microbe_source_queue.check_queue`, with `QUEUE_EXTENSIONS` and
`REQUIRED_WHEN_ADOPTED` passed as `SourceQueueProfile` settings. It skips with an
explicit reason when CLAW is unavailable; local validation still runs. With a
CLAW checkout exposed through `PYTHONPATH`, that test must pass without a skip.
The contracts reviewed were at CLAW commit
`bac7e7bc0b4e05b472bb4ec04395a697acac6e10`; the source, queue and writer modules
are unchanged from the initial review at `7c516fd6d694915a1c2c5829c201251c4d04ac69`.

## Writer Audit Scope

`conf/writer_audit.yaml` is a local multi-format declaration, **not** a CLAW
YAML writer profile. CLAW's current `kg_microbe_writers` audit identifies YAML
writers and cannot certify DUFMech's JSON/TSV/snapshot outputs. The local audit
walks Python ASTs in `src/dufmech/` and `scripts/`, including ignored, hidden,
and untracked files. It reports function-scoped write calls, open modes,
configured output formats, actual validation/history calls, and policy-test
paths. In-memory renderers and supplied streams can also appear as potential
write sites; `unspecified` means the format has not been established.

The source snapshot writers mostly retain their existing
`legacy-replace` behavior. Worklist, cross-Mech, and score artifact sets use
exclusive creation. Score inputs require verified companion manifests by default;
explicit ad hoc inputs retain their byte hashes and unverified status. These
distinct behaviors are visible, not silently certified as a
uniform guarded pipeline.

The new generated writers are `records.write_records` and
`records.write_schema_artifacts`, with `apply=False` defaults. The former owns
only generated family files and their ownership manifest; human-authored YAML
overlays are not generated outputs. `write_records` delegates through an
advisory writer lock to `_write_records`, where validation and ownership checks
occur. `_publish_projection` retains displaced files in recovery directories
and uses exclusive publication. These helpers have separate audit declarations;
validation calls in the implementation are not attributed to its wrapper.
`records._publish` remains an internal atomic single-file replacement primitive
for schema artifacts, not an independent curation guard.

Bohr confirmed `reviews.append_document` as the shared exclusive append
publisher, `reviews.save_review` as the validated Markdown review writer, and
`history.new_history` as the canonical-schema-validated YAML event writer.
Neither review nor history writers replace existing events. Required function
calls, dry-run defaults, real helper definitions, and test-file provenance are
checked for declared policies. AST evidence does not prove control-flow order,
transactional behavior, scientific validity, or test success: the dedicated
record/review/history tests establish those runtime properties.
