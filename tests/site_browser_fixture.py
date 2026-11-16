"""A labeled, synthetic engineering fixture; never used in published scientific pages."""

import sys
from pathlib import Path

from dufmech.pages import render_site
from dufmech.protein_discovery import enrich_rows
from dufmech.protein_examples import build_rows, normalize_entry
from tests.test_protein_discovery import observation
from tests.test_report import worklist_row


def build(out: Path) -> None:
    rows = [{**worklist_row(f"PF{i:05d}", proteins=i), "name": f"Fixture family {i:03d}",
             "short_name": f"DUF{i}", "interpro_id": f"IPR{i:06d}",
             "unknown_status": "UNKNOWN_CANDIDATE" if i <= 100 else "KNOWN_HISTORICAL_DUF",
             "structures": i % 3}
            for i in range(1, 124)]
    rows[0]["proteins"] = None
    rows[1]["proteins"] = 0
    rows[0]["description"] = "Synthetic browser fixture. [[cite:PUB00100883]]."
    protein = normalize_entry({
        "primaryAccession": "P0A8M6", "entryAudit": {"sequenceVersion": 1},
        "sequence": {"value": "MACDEFGHIK", "length": 10},
        "uniProtKBCrossReferences": [{"database": "Pfam", "id": "PF00001"}],
    }, "2026_03")
    examples = build_rows(rows, [{
        "pfam_id": "PF00001", "uniprot_accession": "P0A8M6", "source_mech": "FixtureMech",
        "source_record_id": "fixture:1", "source_path": "data/fixture.yaml",
        "source_section": "fixture", "link_basis": ["synthetic_fixture"],
    }], {"FixtureMech": {"repository": "https://example.org/fixture", "commit": "a" * 40}},
        {"P0A8M6": protein}, {}, {})
    direct = {row["pfam_id"]: row for row in enrich_rows(
        [row for row in examples if row["pfam_id"] in {"PF00003", "PF00004"}],
        {"PF00003": observation("PF00003", empty=True), "PF00004": observation("PF00004")},
    )}
    examples = [direct.get(row["pfam_id"], row) for row in examples]
    reviews = [{"label": f"Synthetic retained review {index:03d}",
                "scope": f"Engineering fixture scope {index}; no scientific assessment",
                "scientific_review": bool(index % 2),
                "local_source": f"source/reports/yaml_record_review/browser-fixture-{index}.md"}
               for index in range(101)]
    review_sources = {ref["local_source"]: f"Synthetic retained review {index}.\n"
                      for index, ref in enumerate(reviews)}
    render_site(rows, [], input_ids={"worklist": "synthetic-browser-fixture"}, out_dir=out,
                protein_examples=examples, provenance={"retained_reviews": reviews},
                extra_artifacts=review_sources)


if __name__ == "__main__":
    build(Path(sys.argv[1]))
