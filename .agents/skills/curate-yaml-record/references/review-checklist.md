# DUFMech Record Review Checklist

Use this checklist for the requested record or category scope. A review records
findings; it does not authorize scientific edits, source downloads, status promotion,
or outbound publication. The native review command retains the timestamped report
and exact source context as a common YAML/derived Markdown bundle under
`reviews/structured/<timestamp>-<slug>/`; follow `docs/record-reviews.md`. An inspection alone is not a saved review.

## Identity and Ownership

| Surface | What to verify |
| --- | --- |
| `pfam_id`, `id`, names, InterPro integration | Exact Pfam accession and frozen source correspondence; names are not proof of function. Do not conflate a family with a particular protein. |
| `data/worklists/`, `provenance`, `score_provenance` | Existing snapshot manifests and input hashes; acquisition, offline reclassification, scoring and review dates are distinct. |
| `curation/families/` | Human-owned `FamilyCuration` input, with no attempt to override source identity, counters or generated audit events. |
| `data/families/`, schemas, Pages | Derived outputs that reproduce from their maintained inputs; never the direct correction surface. |

## Evidence and Interpretation

- Check each assertion independently: stable assertion ID, exact statement,
  EXPERIMENTAL/COMPUTATIONAL/CONTEXTUAL evidence kind, and protein/subfamily/family
  scope justified by the inspected source. A database description is imported
  evidence, not automatically a primary experiment or a curated functional claim.
- Resolve the actual reference and URL, inspect the original source, and verify
  that the verbatim snippet occurs in the hash-matching local evidence extract.
  Keep interpretation in `explanation`; a valid quotation can still support a
  narrower conclusion than the proposed assertion. Retain only permitted extracts.
- Separate experimental characterization from sequence similarity, predicted
  structure, co-occurrence and genomic context. Keep contradictory results and
  tested conditions. Missing evidence and an unperformed search are not negatives.
- Treat member tracks as coordinates for the supplied frozen proteins, not an
  alignment, 3D structure, complete member census, or family-wide functional proof.
- Check discussions, datasets and cross-corpus links for exact target identity,
  evidence and rights. Empty optional fields are acceptable; do not create data to
  raise completeness counts. Include ignored/hidden files in absence searches.

## Status, History and Retained Reports

- `seed_status` is imported classification; `characterization_status` is a separate
  scoring result. Neither establishes `curation_status` or scientific endorsement.
- For actual curation, check the stable history directory, canonical-schema-valid
  sidecars, target path, actual actor, timestamps and outcome. The generated
  `curation_events` index must replay those sidecars exactly, not replace them.
- A REVIEWED projection needs a current-content per-record PASS and its linked
  REVIEW event. Check the report's scope and `scientific_review` boolean separately.
  Category/repository reports and SEED_ONLY verdicts cannot promote a record.
- Saved reviews need the inspected context, exact input hashes, real start/end,
  actual reviewer, scoped verdict, findings and all required sections. Corrections
  append a new report rather than rewriting history. Verify the artifact is not
  ignored, and cite its exact path in the response.
- For category reviews, retain the selection rule and exact member set. Explain
  lump/split decisions from family identity and evidence scope; a shared name or
  prediction is insufficient to collapse biologically distinct families.

## Checks and Limits

Run the checks appropriate to the actual scope and report their exact outcomes.
`just records-check`, `just history-check`, and `just reviews-check` validate distinct
contracts; `just qc` adds source governance, schema/site reproduction and browser
checks. Do not describe a skipped, stale-pin-blocked or unavailable check as passed.
Frozen ID/label validation does not certify current upstream taxonomy, and passing
schema or quotation checks does not certify scientific interpretation. State what
was supported, corrected, unresolved, and not investigated.
