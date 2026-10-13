"""A labeled, synthetic engineering fixture; never used in published scientific pages."""

import sys
from pathlib import Path

from dufmech.pages import render_site
from dufmech.protein_examples import build_rows, normalize_entry
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
    render_site(rows, [], input_ids={"worklist": "synthetic-browser-fixture"}, out_dir=out,
                protein_examples=examples)


if __name__ == "__main__":
    build(Path(sys.argv[1]))
