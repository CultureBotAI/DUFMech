from __future__ import annotations

import json
import os
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from dufmech.pages import diff_trees, main, render_from_paths, render_site
from dufmech.report import ReportError
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


def test_diff_trees_compares_bytes_even_when_stats_match(tmp_path) -> None:
    expected, actual = tmp_path / "expected", tmp_path / "actual"
    expected.mkdir()
    actual.mkdir()
    a, b = expected / "index.html", actual / "index.html"
    a.write_text("fresh", encoding="utf-8")
    b.write_text("stale", encoding="utf-8")
    os.utime(b, ns=(a.stat().st_atime_ns, a.stat().st_mtime_ns))
    assert diff_trees(expected, actual) == ["index.html"]


def test_diff_trees_checks_entry_types_and_hidden_files(tmp_path) -> None:
    expected, actual = tmp_path / "expected", tmp_path / "actual"
    expected.mkdir()
    actual.mkdir()
    (expected / "index.html").write_text("fresh", encoding="utf-8")
    (actual / "index.html").mkdir()
    (actual / ".hidden").write_text("stale", encoding="utf-8")
    assert diff_trees(expected, actual) == [".hidden", "index.html"]


def test_render_failure_does_not_delete_existing_output(tmp_path) -> None:
    out = tmp_path / "pages"
    out.mkdir()
    previous = out / "index.html"
    previous.write_text("previous good site", encoding="utf-8")
    with pytest.raises(ReportError, match="no .* snapshots found"):
        main(["--out", str(out), "--worklists-dir", str(tmp_path / "missing")])
    assert previous.read_text(encoding="utf-8") == "previous good site"


def test_render_preserves_unrelated_output_files(tmp_path) -> None:
    out = tmp_path / "pages"
    out.mkdir()
    sentinel = out / "CNAME"
    sentinel.write_text("custom.example", encoding="utf-8")
    render_site([], [], input_ids={}, out_dir=out)
    assert sentinel.read_text(encoding="utf-8") == "custom.example"


@pytest.mark.parametrize("out", [Path.cwd(), Path.cwd().parent, Path.home(), Path("/")])
def test_render_rejects_protected_directories(out) -> None:
    with pytest.raises(ReportError, match="protected directory"):
        render_site([], [], input_ids={}, out_dir=out)


def test_render_rejects_input_overlap(tmp_path) -> None:
    with pytest.raises(ReportError, match="overlaps snapshot inputs"):
        render_from_paths(out_dir=tmp_path, worklists_dir=tmp_path / "worklists")


@pytest.mark.parametrize("symlink_output", [False, True])
def test_render_rejects_symlink_destinations(tmp_path, symlink_output) -> None:
    target = tmp_path / "target"
    out = tmp_path / "pages"
    if symlink_output:
        target.mkdir()
        out.symlink_to(target, target_is_directory=True)
    else:
        out.mkdir()
        target.write_text("preserve", encoding="utf-8")
        (out / "index.html").symlink_to(target)
    with pytest.raises(ReportError, match="symlink|not a regular file"):
        render_site([], [], input_ids={}, out_dir=out)
    if not symlink_output:
        assert target.read_text(encoding="utf-8") == "preserve"


@pytest.mark.parametrize(
    "url", ["javascript:alert(1)", "data:text/html,test", "//example.com", "https://[", "java\nscript:alert(1)"]
)
def test_dashboard_does_not_link_unsafe_sources(tmp_path, url) -> None:
    out = tmp_path / "pages"
    render_site(
        [{**worklist_row("PF00001", proteins=10), "source_url": url}], [],
        input_ids={}, out_dir=out,
    )
    soup = BeautifulSoup((out / "index.html").read_text(encoding="utf-8"), "html.parser")
    assert [a["href"] for a in soup.select("tbody a")] == [
        "https://www.ebi.ac.uk/interpro/entry/pfam/PF00001/", "#PF00001"
    ]
    assert "PF00001" in soup.get_text()


def test_dashboard_distinguishes_missing_counts_seed_status_and_unscored(tmp_path) -> None:
    out = tmp_path / "pages"
    render_site(
        [{
            **worklist_row("PF00001", proteins=0, unknown_status="KNOWN_HISTORICAL_DUF"),
            "structures": None,
        }], [], input_ids={}, out_dir=out,
    )
    soup = BeautifulSoup((out / "index.html").read_text(encoding="utf-8"), "html.parser")
    cells = [cell.get_text() for cell in soup.select("tbody tr td")]
    assert cells[2:] == ["KNOWN HISTORICAL DUF", "UNSCORED", "Not scored", "0", "Not available", "0", ""]
    assert soup.select_one("tbody a")["href"].startswith("https://")
    assert "not unique proteins or matches" in soup.get_text()
    assert "Families with structures" in soup.get_text()


def test_status_legend_is_visible_and_distinguishes_missing_evidence(tmp_path) -> None:
    render_site([], [], input_ids={}, out_dir=tmp_path / "pages")
    soup = BeautifulSoup((tmp_path / "pages/index.html").read_text(), "html.parser")
    legend = soup.select_one("section.legend")
    assert legend is not None and not legend.has_attr("hidden")
    assert len(soup.select('[aria-labelledby="status-guide"]')) == 1
    text = " ".join(legend.get_text().split())
    assert "Missing scores are not negative evidence" in text
    assert "this heuristic is not proof of a known function" in text
    assert "context alone does not assign function" in text
    assert "not unique proteins, publications, or confidence scores" in text


def test_family_discovery_navigation_and_provenance(tmp_path) -> None:
    out = tmp_path / "pages"
    render_site([worklist_row("PF18701", proteins=10), worklist_row("PF04149", proteins=20)], [],
                input_ids={"worklist": "frozen-input"}, out_dir=out)
    soup = BeautifulSoup((out / "index.html").read_text(), "html.parser")
    assert {row["id"] for row in soup.select("tbody tr")} == {"PF18701", "PF04149"}
    assert soup.select_one('a[download][href="index.json"]')
    assert soup.select_one('nav a[href="https://culturebotai.github.io/mechs/"]')
    assert soup.select_one('nav a[href="https://github.com/CultureBotAI/DUFMech"]')
    assert "CC BY 4.0" in soup.footer.get_text() and "BSD 3-Clause" in soup.footer.get_text()
    assert soup.select_one('link[rel="icon"]')["href"] == "data:,"
    assert soup.select_one('label input[type="search"]')
    assert soup.select_one('#family-count[role="status"]')
    assert "not establish experimental characterization" in " ".join(soup.get_text().split())
    assert "not evidence that the family lacks a known function" in soup.get_text()
    assert "position: sticky" in (out / "style.css").read_text()
    assert (out / "dashboard.js").is_file()
