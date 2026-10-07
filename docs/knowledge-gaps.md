# Offline Knowledge-Gap Review

The native adapter reuses CLAW's sentence scoring and shared Discussion shape.
It never contacts Europe PMC, a model, or a paid provider. It scans a bounded
window of validated family records against an explicitly retained abstract
cache, and saves timestamped YAML proposals and Markdown reports under
`reports/knowledge_gap_scan/`. A proposal is not a functional assertion or a
completed scientific review.

Set `CLAW_SRC` to the `src` directory of a published CultureBotAI CLAW checkout.
CI uses immutable `b81580f150d5334841f3eb16434575701607bc81`. Packets retain both
the configuration and shared scanner SHA-256, so a different implementation or
configuration requires a new scan and review. No dependency is downloaded by
the adapter itself.

## Retained Input

Use a UTF-8 JSON file under `evidence/knowledge_gaps/` with this envelope:

```json
{
  "version": 1,
  "source_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search",
  "retrieved_at": "2026-10-07T10:00:00Z",
  "results": [
    {
      "reference": "PMID:123456",
      "title": "Replace with the actual primary-source title",
      "abstract": "Replace with the actual retained plain-text abstract"
    }
  ]
}
```

This is a format illustration, not evidence or an actual literature result.
Use actual references, quotes, retrieval timestamps and source URLs. Keep
source licensing and redistribution restrictions in mind. Duplicate keys and
references, malformed rows, symlinks and caches over 10 MB are rejected.

```bash
CLAW_SRC=/path/to/culturebotai-claw/src just knowledge-gap-scan scan \
  --abstracts evidence/knowledge_gaps/actual-cache.json --limit 25 --offset 0
```

An offset rotates over the complete corpus; limits range from 1 to 100.
Signals must mention an exact family name, short name or accession. Existing
Discussion quotations are indexed across the whole corpus before selecting a
window. Tied candidates resolve deterministically by record ID. Reusing the
same sentence across different records is not accepted silently.

## Review And Acceptance

Read the retained packet and source. Verify the exact family/subfamily scope,
publication identity, quotation and interpretation. Record a canonical family
`REVIEW` / `no_change` event using `just new-history`, targeting exactly this
family's `data/families/PFxxxxx.yaml` or `curation/families/PFxxxxx.yaml`.
After deciding to accept, render the structured event details with:

```bash
CLAW_SRC=/path/to/culturebotai-claw/src just knowledge-gap-scan approval \
  --packet reports/knowledge_gap_scan/ACTUAL-TIMESTAMP-knowledge-gaps.yaml \
  --pfam PF04149 --rationale 'Actual reviewed scope and evidence assessment'
```

Pass that exact JSON as `just new-history --details` (or retain it for
`--details-file`). It binds the affirmative decision to the exact packet SHA-256
and family. Do not generate an ACCEPT decision for rejected proposals. Plain
prose, a packet pathname mention, a different family, or altered packet bytes
cannot authorize acceptance. Its timestamp must not predate the packet. This
event records the proposal review, not a record mutation or functional finding.

```bash
CLAW_SRC=/path/to/culturebotai-claw/src just knowledge-gap-scan accept \
  --packet reports/knowledge_gap_scan/ACTUAL-TIMESTAMP-knowledge-gaps.yaml \
  --pfam PF04149 --history history/records/PF04149/ACTUAL-REVIEW.yaml \
  --actor-name 'Actual curator' --actor-type human
```

Acceptance previews by default. Repeat with `--apply` only after checking the
preview. AI actors must use `--actor-type ai_agent` and identify `--model` and
`--agent-tool`; do not attribute automated changes to a human. The adapter
replays the proposal from its hashed inputs and current corpus, validates the
native overlay, preserves existing fields, invalidates an old review status,
and appends a canonical `EDIT` / `changed` history event. The resulting status
is `IN_PROGRESS`, never `REVIEWED`; characterization remains unchanged.

Run `just records --apply` and regenerate/check the derived pages after an
accepted change, then submit the source, overlay, report and history together
for PR review. Direct edits to generated `data/families/` files are not an
acceptance mechanism. A repeated or stale packet is rejected, not reapplied.

Native writers retain displaced files under `.dufmech/record-recovery/` rather
than discarding concurrent changes. If appending change history fails, prior
overlay content is restored; a newly created overlay may remain as an empty
`SEEDED` overlay. An interrupted write requires inspection of the visible
overlay, history and retained recovery files before retrying. This is not a
cross-file transactional database.
