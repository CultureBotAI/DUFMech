"""Bounded retained-review source pages for DUFMech issue #464."""
from __future__ import annotations

import json
import math
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from dufmech.pages import diff_trees, render_site
from dufmech.site_contract import check_site
from tests.test_report import worklist_row


def review_references(count):
    return [{"label": f"Review {index:04d} <script>literal label</script>",
             "scope": f"Scope {index:04d} <img src=x onerror=bad()>",
             "scientific_review": bool(index % 2),
             "url": (f"https://github.com/CultureBotAI/DUFMech/blob/{'a' * 40}/"
                     f"reviews/structured/review-{index}/review.yaml") if index % 2 else "",
             "local_source": f"source/reports/yaml_record_review/review-{index}.md"}
            for index in range(count)]


def build_review_site(out, count):
    refs = review_references(count)
    provenance = {"retained_reviews": refs,
                  "worklist": {"repository": "https://github.com/CultureBotAI/DUFMech",
                               "commit": "a" * 40, "path": "data/worklists/frozen.json"},
                  "schema": {"document": {"classes": {}, "enums": {}}}}
    extra = {ref["local_source"]: f"Synthetic retained source {index}.\n"
             for index, ref in enumerate(refs)}
    extra["schema/dufmech.yaml"] = "id: https://example.org/engineering-fixture\n"
    render_site([worklist_row("PF00001", proteins=1)], [], input_ids={"worklist": "fixture"},
                out_dir=out, provenance=provenance, extra_artifacts=extra)
    return refs


def parse(out, relative):
    return BeautifulSoup((out / relative).read_text(), "html.parser")


@pytest.mark.parametrize("count", [0, 1, 49, 50, 51, 100, 101, 1237])
def test_review_pages_are_bounded_complete_and_preserve_all_fields(tmp_path, count):
    refs = build_review_site(tmp_path / "site", count)
    root = tmp_path / "site"
    paths = ["sources.html"] + [f"sources/{n}.html" for n in range(2, math.ceil(count / 50) + 1)]
    assert len(list((root / "sources").glob("*.html"))) == len(paths) - 1
    found = []
    for page, relative in enumerate(paths):
        soup = parse(root, relative)
        items = soup.select("#retained-review-list > li")
        assert len(items) == min(50, max(0, count - page * 50))
        assert len((root / relative).read_bytes()) <= 300000
        assert not soup.select("#retained-review-list script, #retained-review-list img")
        for index, item in enumerate(items, page * 50):
            ref = refs[index]
            assert item.find("a").get_text() == ref["label"]
            assert item.find("p").get_text() == (
                f'Scope: {ref["scope"]}. Scientific review: {ref["scientific_review"]}.')
            expected = ref["url"] or (("../" if page else "") + ref["local_source"])
            assert item.find("a")["href"] == expected
            found.append(item.find("a").get_text())
        start = page * 50 + 1 if count else 0
        end = min((page + 1) * 50, count)
        assert soup.select_one("#review-count").get_text() == (
            f"Reviews {start:,}–{end:,} of {count:,}. Page {page + 1} of {len(paths)}.")
        nav = soup.find("nav", attrs={"aria-label": "Retained review pages"})
        if len(paths) == 1:
            assert nav is None
        else:
            assert nav is not None and not nav.has_attr("hidden")
            assert nav.select_one('[aria-current="page"]').get_text() == str(page + 1)
            assert bool(nav.select('a[rel="prev"]')) == (page > 0)
            assert bool(nav.select('a[rel="next"]')) == (page + 1 < len(paths))
    assert found == [ref["label"] for ref in refs]
    assert len(found) == len(set(found))
    if not count:
        assert "No retained reviews supplied." in parse(root, "sources.html").get_text()


def test_nested_links_assets_context_and_entire_site_remain_valid(tmp_path):
    root = tmp_path / "site"
    build_review_site(root, 101)
    second = parse(root, "sources/2.html")
    assert second.select_one('link[rel="stylesheet"]')["href"] == "../style.css"
    assert {script["src"] for script in second.select("script[src]")} == {
        "../theme.js", "../dashboard.js"}
    assert second.select_one('a[rel="prev"]')["href"] == "../sources.html#retained-reviews"
    assert second.select_one('a[rel="next"]')["href"] == "../sources/3.html#retained-reviews"
    assert second.select_one('#retained-review-list > li a')["href"].startswith("../source/")
    assert second.select_one('a[href="../sources.html#record-schema"]')
    assert second.select_one('a[href="../sources.html#frozen-inputs"]')
    assert second.select_one("#status-guide")
    entry = parse(root, "sources.html")
    assert entry.select_one('a[href="schema.html"]')
    assert entry.select_one("#record-schema") and entry.select_one("#frozen-inputs")
    assert entry.select_one("#status-guide")
    budgets = json.loads((Path(__file__).parents[1] / "conf/pages_budgets.json").read_text())
    assert budgets["groups"]["html"]["largest_bytes"] == 300000
    errors, _ = check_site(root, budgets)
    assert errors == []


def test_review_pagination_is_deterministic(tmp_path):
    build_review_site(tmp_path / "first", 51)
    build_review_site(tmp_path / "second", 51)
    assert diff_trees(tmp_path / "first", tmp_path / "second") == []


def test_numbered_review_artifact_scope_is_narrow_and_stale_pages_are_owned(tmp_path):
    from dufmech.site_files import GENERATED

    for path in ("sources/0.html", "sources/1.html", "sources/02.html", "sources/name.html",
                 "sources/2.js", "sources/../2.html", "../sources/2.html"):
        assert GENERATED.fullmatch(path) is None
    root = tmp_path / "site"
    build_review_site(root, 101)
    assert (root / "sources/3.html").is_file()
    note = root / "sources/reader-note.txt"
    note.write_text("Unrelated reader note.")
    build_review_site(root, 51)
    assert not (root / "sources/3.html").exists()
    assert (root / "sources/2.html").is_file()
    assert note.read_text() == "Unrelated reader note."


def test_shrink_refuses_to_remove_edited_page_before_replacing_entry(tmp_path):
    from dufmech.report import ReportError

    root = tmp_path / "site"
    build_review_site(root, 101)
    entry = (root / "sources.html").read_bytes()
    edited = root / "sources/3.html"
    edited.write_text("Reader edits that must survive.")
    with pytest.raises(ReportError, match="refusing to remove modified obsolete page: sources/3.html"):
        build_review_site(root, 51)
    assert edited.read_text() == "Reader edits that must survive."
    assert (root / "sources.html").read_bytes() == entry
