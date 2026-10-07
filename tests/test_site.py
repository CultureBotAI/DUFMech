from __future__ import annotations

import json
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from dufmech.pages import diff_trees, main, render_site
from dufmech.report import ReportError
from dufmech.site_contract import check_site, contrast
from dufmech.site_data import description_html, reference_url, source_link
from dufmech.site_metadata import load_review_site_metadata, metadata_from_records
from tests.test_report import worklist_row


def soup(out: Path, relative: str = "index.html") -> BeautifulSoup:
    return BeautifulSoup((out / relative).read_text(), "html.parser")


def test_static_paging_is_complete_bounded_and_deterministic(tmp_path):
    rows = [worklist_row(f"PF{i:05d}", proteins=i) for i in range(1, 124)]
    a, b = tmp_path / "a", tmp_path / "b"
    for out in (a, b):
        render_site(rows, [], input_ids={}, out_dir=out)
    assert diff_trees(a, b) == []
    assert len(soup(a).select("#family-table tbody tr")) == 50
    catalogue = ["index.html", "browse/2.html", "browse/3.html"]
    ids = [r["id"] for path in catalogue for r in soup(a, path).select("#family-table tbody tr")]
    assert len(ids) == len(set(ids)) == 123
    assert set(ids) == {r["pfam_id"] for r in rows}
    budgets = json.loads(Path("conf/pages_budgets.json").read_text())
    errors, measurements = check_site(a, budgets)
    assert errors == []
    assert measurements["families"] == 123


def test_record_grounding_citations_provenance_and_truthful_fallback(tmp_path):
    row = {**worklist_row("PF00001", proteins=2), "interpro_id": "IPR000001",
           "description": "Imported <script>bad</script> [[cite:PUB00100883]]. [pfam:PF00001]"}
    render_site([row], [], input_ids={"worklist": "frozen"}, out_dir=tmp_path)
    record = soup(tmp_path, "families/PF00001.html")
    assert not record.select(".description script")
    assert "Imported <script>bad</script>" in record.select_one(".description").get_text()
    refs = [a["href"] for a in record.select(".description a")]
    assert refs and all("pubmed" not in href for href in refs)
    assert "not PubMed identifiers" in record.get_text()
    assert record.select_one('a[href="https://www.ebi.ac.uk/interpro/entry/InterPro/IPR000001/"]')
    assert "No retained curation events supplied" in record.get_text()
    assert "No residue-level domain match evidence" in record.get_text()
    assert "SNAPSHOT ONLY" in record.get_text()


def test_resolved_publications_require_explicit_mapping():
    result = description_html("[[cite:PUB00123]]", "PF00001", labels={},
                              publications={"PUB00123": {"id": "PMID:7654321", "label": "Primary paper"}})
    assert 'href="https://pubmed.ncbi.nlm.nih.gov/7654321/"' in result
    assert "Primary paper" in result
    assert "pubmed.ncbi.nlm.nih.gov/00123" not in result
    assert reference_url({"reference": "DOI:10.1234/source"}) == "https://doi.org/10.1234/source"


@pytest.mark.parametrize("path", ["../secret", "/abs", "data/../secret", "data\\secret", "data/\nsecret"])
def test_immutable_sources_reject_unsafe_paths(path):
    assert not source_link("https://github.com/CultureBotAI/DUFMech", "a" * 40, path)


def test_metadata_and_exact_sibling_source_links(tmp_path):
    row = worklist_row("PF00001", proteins=10)
    path = "data/traits/nested/real family.yaml"
    cross = {"pfam_id": "PF00001", "source_mech": "ProteinTraitsMech", "source_path": path,
             "source_section": "trait_identifier", "source_record_id": "Pfam:PF00001"}
    render_site([row], [], input_ids={}, out_dir=tmp_path,
                cross_mech_rows=[cross], cross_mech_sources={"ProteinTraitsMech": {
                    "repository": "https://github.com/CultureBotAI/proteintraitsmech", "commit": "a" * 40}},
                family_metadata={"PF00001": {"curation_status": "SEEDED", "source": {
                    "repository": "https://github.com/CultureBotAI/DUFMech", "commit": "b" * 40,
                    "path": "data/families/PF00001.yaml"}, "history": [{
                        "timestamp": "2026-10-07T12:00:00Z", "agent": "Fixture curator",
                        "action": "seed", "summary": "Imported snapshot metadata."}]}})
    record = soup(tmp_path, "families/PF00001.html")
    hrefs = [a["href"] for a in record.select("a[href]")]
    assert f"https://github.com/CultureBotAI/proteintraitsmech/blob/{'a' * 40}/data/traits/nested/real%20family.yaml" in hrefs
    assert f"https://github.com/CultureBotAI/DUFMech/blob/{'b' * 40}/data/families/PF00001.yaml" in hrefs
    assert "Fixture curator" in record.get_text()
    assert "Imported snapshot metadata." in record.get_text()


def test_domain_plot_uses_coordinates_without_fabrication(tmp_path):
    render_site([worklist_row("PF00001", proteins=10)], [], input_ids={}, out_dir=tmp_path,
                member_rows=[{"pfam_id": "PF00001", "uniprot_accession": "P12345", "length": 200,
                              "match_ranges": ["21-60", "101-140"], "member_source_url": "https://example.org/frozen"}])
    record = soup(tmp_path, "families/PF00001.html")
    assert "21-60, 101-140 of 200" in record.select_one(".domain-track")["aria-label"]
    assert record.select_one(".domain-match")["style"] == "left:10.0000%;width:20.0000%"


@pytest.mark.parametrize("ranges", [["0-10"], ["20-10"], ["1-201"], ["inferred"]])
def test_invalid_domain_ranges_fail_before_publication(tmp_path, ranges):
    with pytest.raises(ReportError, match="invalid member match range"):
        render_site([worklist_row("PF00001", proteins=10)], [], input_ids={}, out_dir=tmp_path,
                    member_rows=[{"pfam_id": "PF00001", "uniprot_accession": "P12345",
                                  "length": 200, "match_ranges": ranges}])
    assert not (tmp_path / "index.html").exists()


def test_nested_symlink_is_rejected_without_modifying_prior_site(tmp_path):
    out, external = tmp_path / "site", tmp_path / "external"
    out.mkdir()
    external.mkdir()
    (out / "families").symlink_to(external, target_is_directory=True)
    with pytest.raises(ReportError, match="not a regular directory"):
        render_site([worklist_row("PF00001", proteins=10)], [], input_ids={}, out_dir=out)
    assert list(external.iterdir()) == []


def test_parent_record_adapter_checks_snapshot_identity():
    record = {"pfam_id": "PF00001", "curation_status": "SEEDED", "provenance": {"snapshot_id": "frozen"}}
    result = metadata_from_records([record], input_ids={"worklist": "frozen"}, sources={})
    assert result["PF00001"]["curation_status"] == "SEEDED"
    with pytest.raises(ReportError, match="disagree"):
        metadata_from_records([record], input_ids={"worklist": "newer"}, sources={})


def test_supplemental_metadata_input_is_not_a_publication_path(tmp_path):
    metadata = tmp_path / "metadata.json"
    metadata.write_text(json.dumps({"families": {"PF00001": {
        "reviews": [{"scientific_review": True}], "curation_status": "REVIEWED",
    }}, "provenance": {"worklist": {"commit": "a" * 40}}}))
    with pytest.raises(SystemExit) as exc:
        main(["--out", str(tmp_path / "site"), "--metadata-json", str(metadata)])
    assert exc.value.code == 2
    assert not (tmp_path / "site").exists()


def test_snapshot_review_adapter_uses_validated_loader_without_promoting_status(tmp_path, monkeypatch):
    path = "reports/yaml_record_review/fixture.md"
    source = tmp_path / path
    source.parent.mkdir(parents=True)
    source.write_text("Fixture retained report")
    def captured_review(root, *, source_bytes):
        source_bytes[path] = b"Fixture retained report"
        return [{
            "path": path, "finished_utc": "2026-10-07T12:00:00Z", "verdict": "SEED_ONLY",
            "reviewer": "Fixture reviewer", "review_scope": "Imported identity only",
            "scientific_review": False, "context": {"members": ["PF00001"]},
        }]

    monkeypatch.setattr("dufmech.reviews.load_review_metadata", captured_review)
    metadata, provenance, copies = load_review_site_metadata(tmp_path, {"PF00001"})
    assert "curation_status" not in metadata["PF00001"]
    assert metadata["PF00001"]["reviews"][0]["scientific_review"] is False
    assert copies[f"source/{path}"] == "Fixture retained report"
    out = tmp_path / "site"
    render_site([worklist_row("PF00001", proteins=1)], [], input_ids={}, out_dir=out,
                family_metadata=metadata, provenance=provenance, extra_artifacts=copies)
    assert "SNAPSHOT ONLY" in soup(out, "families/PF00001.html").get_text()
    assert "Imported identity only" in soup(out, "sources.html").get_text()


def test_optional_curated_content_keeps_scope_evidence_and_discussion_distinct(tmp_path):
    record = {"assertions": [{"assertion_id": "scoped", "statement": "Fixture claim",
              "scope": "Only the tested fixture protein", "evidence_kind": "EXPERIMENTAL",
              "evidence": [{"reference": "PMID:12345", "source_url": "https://example.org/paper",
                            "snippet": "Fixture supporting excerpt", "explanation": "Fixture support"}]}],
              "discussions": [{"prompt": "Does the observation generalize?", "status": "OPEN",
                               "evidence": [{"reference": "DOI:10.1234/discussion"}]}]}
    render_site([worklist_row("PF00001", proteins=10)], [], input_ids={}, out_dir=tmp_path,
                family_metadata={"PF00001": {"curation_status": "IN_PROGRESS", "record": record}})
    page = soup(tmp_path, "families/PF00001.html")
    assert "Only the tested fixture protein" in page.get_text()
    assert "Does the observation generalize?" in page.get_text()
    assert page.select_one('a[href="https://pubmed.ncbi.nlm.nih.gov/12345/"]')
    assert page.select_one('a[href="https://doi.org/10.1234/discussion"]')


def test_rebuild_removes_only_unchanged_owned_obsolete_pages(tmp_path):
    out = tmp_path / "site"
    rows = [worklist_row(f"PF{i:05d}", proteins=i) for i in range(1, 52)]
    render_site(rows, [], input_ids={}, out_dir=out)
    (out / "CNAME").write_text("custom.example")
    render_site(rows[:1], [], input_ids={}, out_dir=out)
    assert not (out / "browse").exists()
    assert not (out / "families/PF00002.html").exists()
    assert (out / "families/PF00001.html").is_file()
    assert (out / "CNAME").read_text() == "custom.example"
    clean = tmp_path / "clean"
    render_site(rows[:1], [], input_ids={}, out_dir=clean)
    assert diff_trees(clean, out) == ["CNAME"]


def test_rebuild_refuses_to_remove_user_modified_obsolete_page(tmp_path):
    rows = [worklist_row("PF00001", proteins=1), worklist_row("PF00002", proteins=2)]
    render_site(rows, [], input_ids={}, out_dir=tmp_path)
    (tmp_path / "families/PF00002.html").write_text("user changes")
    before = (tmp_path / "index.html").read_bytes()
    with pytest.raises(ReportError, match="modified obsolete page"):
        render_site(rows[:1], [], input_ids={}, out_dir=tmp_path)
    assert (tmp_path / "index.html").read_bytes() == before


def test_contract_rejects_broken_links_and_budget_overrun(tmp_path):
    render_site([worklist_row("PF00001", proteins=10)], [], input_ids={}, out_dir=tmp_path)
    (tmp_path / "families/PF00001.html").unlink()
    budgets = json.loads(Path("conf/pages_budgets.json").read_text())
    budgets["groups"]["index"]["largest_bytes"] = 1
    errors, _ = check_site(tmp_path, budgets)
    assert any("broken local link" in error for error in errors)
    assert any("index_html_bytes" in error for error in errors)
    assert contrast("#000000", "#ffffff") == 21
