"""A labeled, synthetic engineering fixture; never used in published scientific pages."""

import sys
from pathlib import Path

from dufmech.pages import render_site
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
    render_site(rows, [], input_ids={"worklist": "synthetic-browser-fixture"}, out_dir=out)


if __name__ == "__main__":
    build(Path(sys.argv[1]))
