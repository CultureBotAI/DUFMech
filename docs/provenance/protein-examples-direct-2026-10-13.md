# Direct UniProt DUF Sequence Discovery: 2026-10-13 UTC

All 5,190 `NO_SIBLING_CANDIDATE` families in the
[full-registry parent](protein-examples-2026-10-13.md) were queried directly.
This is sequence-reference enrichment, not functional curation or scoring.
The previous 3,106 covered family rows and all 15 rejected sibling pairings
remain unchanged. No family YAML, reviewed claim, or characterization score
was changed.

## Results

| Measure | Count |
| --- | ---: |
| Worklist families | 8,296 |
| Direct family searches completed | 5,190 |
| Newly covered families | 5,184 |
| Successful zero-result searches | 6 |
| Unfinished family searches | 0 |
| New family-protein example pairs | 15,508 |
| Distinct proteins in direct samples | 14,890 |
| Distinct proteins newly added to the parent | 14,889 |
| Combined covered families | 8,290 |
| Combined distinct proteins | 23,836 |
| Combined family-protein example pairs | 24,886 |

The six zero-result families are PF12976 (DUF3860), PF16424 (DUF5021),
PF20318 (DUF6613), PF24248 (DUF7451), PF25588 (DUF7934), and PF28257
(DUF8378). Each also has zero proteins in the pinned InterPro/Pfam worklist.
That agreement is not proof of biological absence; accession history and
current family definitions remain a separate research task.

There are 5,154 three-example samples, 16 two-example samples, 14 one-example
samples, and six empty samples. One directly discovered accession also occurs
in the parent, so distinct-protein counts must not be summed across inputs.

## Acquisition and Scope

Public GET requests used `https://rest.uniprot.org/uniprotkb/search`, query
`xref:pfam-{pfam_id}`, `size=3`, `format=json`, and
`sort=annotation_score desc,accession asc`. Returned fields were accession,
reviewed status, protein and organism names, organism ID, full sequence,
length, sequence version, Pfam cross-references, and annotation score.

Every response records UniProt release `2026_03`. Acquisition began at
`2026-10-13T04:24:53.475675+00:00` and ended at
`2026-10-13T04:51:20.530314+00:00`. A five-family pilot was resumed into the
same full-cohort checkpoint. The bulk run used at most four concurrent
requests; the command defaults to two. Transient errors receive bounded
retries and provider-directed retry delays.

Samples are neither exhaustive nor taxonomically representative, and are not
restricted to reviewed proteins. Annotation score is not evidence of a tested
function. Exact primary accessions, valid whole-protein sequences, matching
lengths, sequence versions, and exact queried Pfam cross-references are
required. No secondary-accession or isoform substitution is performed.
Domain coordinates are not inferred. New samples explicitly use
`registry_status: NOT_CHECKED`; they are not asserted absent from PTM.

The [UniProt license record](https://rest.uniprot.org/help/license), checked
2026-10-13 UTC, assigns CC BY 4.0 to copyrightable database content and
retains caveats about patents and other rights. Sequences and metadata are
attributed to the UniProt Consortium. Retained sibling-derived parent facts
keep their existing source references and attribution.

## Retained Artifacts

The new immutable artifact set is
`data/protein_examples/duf-protein-examples-direct-2026-10-13.{json,tsv,manifest.json,queries.jsonl}`.
It references the untouched
`data/protein_examples/duf-protein-examples-2026-10-13` parent by JSON and
manifest SHA-256. The manifest carries every new artifact hash, the query
contract, release, acquisition interval, and cohort count.

Loading the successor validates the parent and all retained query responses,
then reproduces the complete combined JSON rows. Covered parent rows are not
rewritten or reinterpreted. Missing searches, truncated checkpoints, changed
query contracts, duplicate families, mixed releases, wrong Pfam membership,
invalid sequences, and rehashed-but-inconsistent derived rows fail validation.
Snapshot-owned checkpoints cannot be extended; online resumption requires a
separate staging file. Symlinked staging paths and writable hard-link aliases
are refused. Descriptor identity, directory attachment, file size and manifest
ownership are rechecked after network waits and before appends. These advisory
guards do not protect against a noncooperating process mutating the same inode
concurrently. The combined row validator rejects conflicting sequence hashes or
versions for an accession within one UniProt release; differences across releases
remain valid. No failed request is serialized as a successful empty search.

The native latest-example selector recognizes both sibling and direct snapshot
namespaces and chooses the direct successor on a same-date tie. Site datasets
retain the parent artifact set as well as the new files for portable offline
replay. Family pages expose sequences, FASTA, query provenance, sample totals,
and explicit empty-search states.

## Offline Reproduction

Retain the unchanged parent artifact set alongside the successor in the output
directory. For a fresh output directory, copy that parent set there first;
the writer never overwrites or silently repins it. Run with the repository's
locked environment:

```sh
python -m dufmech.protein_discovery \
  --worklist-json data/worklists/interpro-pfam-duf-2026-10-10.json \
  --parent-json data/protein_examples/duf-protein-examples-2026-10-13.json \
  --checkpoint data/protein_examples/duf-protein-examples-direct-2026-10-13.queries.jsonl \
  --out-dir /path/to/fresh-output-with-parent \
  --snapshot-date 2026-10-13 --offline
```

JSON, TSV, and retained query bytes are deterministic. The new manifest's
generation timestamp describes the replay, so its own bytes may differ.
For a new explicitly authorized online acquisition, use an unfrozen staging
checkpoint and omit `--offline`. `just protein-examples-direct` exposes the
same arguments. `--acquire-only` validates and retains searches without
publishing a snapshot.

## Publication Boundary

[PR 195](https://github.com/CultureBotAI/DUFMech/pull/195) tracks publication,
adversarial self-review, and remediation of issues
[196](https://github.com/CultureBotAI/DUFMech/issues/196) and
[197](https://github.com/CultureBotAI/DUFMech/issues/197). The publication procedure
retains an annotated source tag, captures verified pins, regenerates native Pages,
and requires fresh quality, source-retention, and exact-head CI gates before merge.
The original external-input preview did not establish publication readiness or
bypass those gates. Final release outcomes are recorded in the PR.

## Pre-Publication Development Validation

- The final Python suite passed 1,386 tests with three expected empty-parameter
  skips and one pre-existing LinkML deprecation warning. The focused sequence
  discovery, parent example, and candidate-client tests passed 106 cases.
  A subsequent focused run including site rendering passed 149 tests after
  the final provenance-label wording correction.
- All 15 snapshot manifests validate. Native records remain schema-valid and
  unchanged, KGX/SSSOM exports remain current, and isolated OAK validation
  confirms all 8,296 canonical ID/label pairs.
- Source governance has zero errors and 16 pre-existing license-review
  warnings for other sources. The 14 retained reviews and eight history events
  remain valid.
- A fresh offline replay reproduced JSON, TSV, and query bytes exactly. Its
  manifest matches except for `snapshot.generated_at`. The successor JSON
  SHA-256 is `27e6086d61047e09129bd1b38f7c18697b50c370cfc69a3546efea3f3d9583d4`;
  the retained query SHA-256 is
  `e3a218cbc499637ee07a3c235ff244d3899f02365b1b2d703b6727d721d28ad7`.
- All 3,106 covered parent rows compare equal, all 15 rejected pairings remain,
  and there are no conflicting sequence hash/version/release tuples across
  the 23,836 distinct proteins in this combined snapshot.
- The final external-input preview measures 386,494,179 bytes across 33,556
  files, including 8,633 HTML pages and 8,290 FASTA files. The explicit site
  budgets increase from 250 MB/30,000 files to 420 MB/36,000 files to accommodate
  the additional sequences and replay parent. Per-page and catalogue limits
  are unchanged. The final full-corpus site contract reports zero errors.
- Eight Playwright browser checks passed against the real enriched preview,
  including 1440-pixel and 390-pixel direct-example and zero-result pages,
  sequence downloads, query provenance, themes, catalogue navigation, and
  layout checks. Desktop and mobile screenshots were visually inspected.
- Native QC passed through the cross-Mech report and then stopped at the
  generated-site gate because the new snapshot is absent from the published
  source-pin ledger. This is not a claim of full publication readiness; the
  external preview does not bypass or alter that native gate.
