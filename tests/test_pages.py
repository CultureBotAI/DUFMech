from __future__ import annotations

import json

from dufmech.pages import diff_trees, render_site
from tests.test_report import worklist_row


def test_render_site_writes_deterministic_dashboard(tmp_path) -> None:
    out = tmp_path / "pages"
    render_site(
        [
            {
                **worklist_row("PF00001", proteins=10),
                "name": "DUF <escape> & friends",
            }
        ],
        [
            {
                "pfam_id": "PF00001",
                "characterization_status": "UNKNOWN_CANDIDATE",
                "known_evidence_count": 0,
                "partial_evidence_count": 0,
                "context_evidence_count": 0,
            }
        ],
        input_ids={"worklist": "interpro-pfam-duf-2026-10-01"},
        out_dir=out,
    )

    html = (out / "index.html").read_text(encoding="utf-8")
    payload = json.loads((out / "index.json").read_text(encoding="utf-8"))

    assert (out / ".nojekyll").is_file()
    assert (out / "style.css").is_file()
    assert "DUF &lt;escape&gt; &amp; friends" in html
    assert payload["summary"]["families"]["total"] == 1
    assert payload["families"][0]["pfam_id"] == "PF00001"


def test_diff_trees_reports_stale_files(tmp_path) -> None:
    expected = tmp_path / "expected"
    actual = tmp_path / "actual"
    expected.mkdir()
    actual.mkdir()
    (expected / "index.html").write_text("fresh", encoding="utf-8")
    (actual / "index.html").write_text("stale", encoding="utf-8")

    assert diff_trees(expected, actual) == ["index.html"]
