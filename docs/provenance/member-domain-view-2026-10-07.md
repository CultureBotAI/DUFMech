# Bounded Domain-Range Example

On 2026-10-07 the existing member-freeze pipeline retrieved two PF04149 proteins
from the public InterPro API and joined their UniProtKB/UniRef metadata. The
purpose is a real-data residue-range view, not scientific characterization,
representative sampling or a comprehensive family membership refresh.

```bash
uv run duf-puf-freeze-members --pfam-id PF04149 \
  --input-json data/worklists/interpro-pfam-duf-2026-10-05.json \
  --limit-families 1 --limit-members-per-family 2 --page-size 2 \
  --snapshot-date 2026-10-07 --out-dir data/worklists
```

The explicitly selected family precedes the worklist IDs; the one-family limit
therefore selects PF04149 while retaining the current worklist's seed snapshot ID.
This snapshot does not update the October 1 family counters or resolve their unknown
function. Do not interpret the API's first two members as curated representatives.

| Accession | Reported length | Reported inclusive Pfam range | UniRef cluster |
| --- | --- | --- | --- |
| A0A010YFW0 | 67 | 9-60 | UniRef90_A0A010YFW0 |
| A0A010YYK3 | 65 | 5-57 | UniRef90_A0A010YYK3 |

Retained JSON, TSV and manifest:
`data/worklists/pfam-uniprot-uniref90-2026-10-07.*`.
The manifest records UTC acquisition completion, endpoints, selection lineage,
counts and byte checksums. Native manifest validation passes. The renderer checks
that the member snapshot belongs to the selected worklist and bounds every plotted
range by the reported protein length. No residue geometry is invented from counters.

Attribution: Pfam annotations are supplied through
[InterPro](https://www.ebi.ac.uk/interpro/entry/pfam/PF04149/), with metadata from
[UniProtKB](https://www.uniprot.org/uniprotkb/A0A010YFW0/entry) and
[UniRef](https://www.uniprot.org/uniref/UniRef90_A0A010YFW0).
[InterPro/Pfam terms](https://interpro-documentation.readthedocs.io/en/latest/license.html)
are CC0; copyrightable UniProt content is retained under
[CC BY 4.0](https://www.uniprot.org/help/license). This is a normalized subset of
those sources, not an endorsement by their providers. Original per-record source
URLs remain in the frozen rows. The older external pilot remains separately documented.
