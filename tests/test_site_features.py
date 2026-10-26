"""Reader-facing link, recovery and feedback features shared with the X-Mech sites."""

from __future__ import annotations

import json
import re
from html import escape
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from dufmech.pages import render_site
from dufmech.site import SITE_URL
from dufmech.site_contract import check_site
from dufmech.site_data import autolink, curie_url, description_html
from tests.test_report import worklist_row

# Verified sibling search and record routes (X-Mech unification standard, 2026-10-25).
SIBLING_ROUTES = (
    "https://culturebotai.github.io/mechs/",
    "https://culturebotai.github.io/CultureMech/app/browser.html?q=",
    "https://culturebotai.github.io/MediaIngredientMech/browser.html?q=",
    "https://culturebotai.github.io/CommunityMech/browser.html?q=",
    "https://culturebotai.github.io/TraitMech/pages/browse.html?q=",
    "https://culturebotai.github.io/proteintraitsmech/browse.html?q=",
    "https://culturebotai.github.io/AntibioticMech/pages/browse.html?q=",
    "https://culturebotai.github.io/CellStructureMech/pages/browse.html?q=",
    "https://culturebotai.github.io/HabitatMech/pages/browse.html?q=",
    "https://culturebotai.github.io/NaturalProductMech/pages/browse.html?q=",
    "https://culturebotai.github.io/TaxonMech/pages/browse.html?q=",
    "https://culturebotai.github.io/TaxonMech/pages/taxon.html?id=NCBITaxon:",
    "https://culturebotai.github.io/PathwayMech/pages/browse.html?q=",
    "https://culturebotai.github.io/CMMMech/pages/browse.html?q=",
    "https://culturebotai.github.io/AIMech/pages/browse.html?q=",
)
GROUNDINGS = {
    "UniProtKB:Q9HX69": "https://www.uniprot.org/uniprotkb/Q9HX69/entry",
    "UniProtKB:Q8INK9-2": "https://www.uniprot.org/uniprotkb/Q8INK9-2/entry",
    "NCBIProtein:AAG07334.1": "https://www.ncbi.nlm.nih.gov/protein/AAG07334.1",
    "NCBIProtein:WP_011919637.1": "https://www.ncbi.nlm.nih.gov/protein/WP_011919637.1",
    "RefSeq:WP_164925653.1": "https://www.ncbi.nlm.nih.gov/protein/WP_164925653.1",
    "GenBank:TLY50285.1": "https://www.ncbi.nlm.nih.gov/protein/TLY50285.1",
    "GenBank:AB123456.1": "https://bioregistry.io/GenBank:AB123456.1",
    "WormBase:WBGene00019763": "https://bioregistry.io/WormBase:WBGene00019763",
    "Pfam:PF00002": "../families/PF00002.html",
    "Pfam:PF00001": "https://www.ebi.ac.uk/interpro/entry/pfam/PF00001/",
    "Pfam:PF99999": "https://www.ebi.ac.uk/interpro/entry/pfam/PF99999/",
    "NCBITaxon:562": "https://culturebotai.github.io/TaxonMech/pages/taxon.html?id=NCBITaxon:562",
    "https://example.org/protein/1": "https://example.org/protein/1",
}


def soup(out: Path, relative: str) -> BeautifulSoup:
    return BeautifulSoup((out / relative).read_text(), "html.parser")


def section(page: BeautifulSoup, heading: str):
    found = page.find("h2", string=heading)
    assert found is not None, heading
    return found.find_parent("section")


def graph_record() -> dict:
    evidence = {"reference": "PMID:25114049", "source_url": "https://example.org/paper",
                "snippet": "Fixture excerpt citing PMID:22713871.",
                "explanation": "Contrasted with PMID25707795 ExtendedData3."}
    return {"causal_graphs": [{
        "graph_id": "fixture", "title": "Fixture graph", "scope_status": "SCOPED",
        "scope": "Fixture protein only", "context": "Fixture context",
        "family_mapping": "Maps to UniProtKB:Q9HX69", "limitations": "Later PMID27211867 differs.",
        "nodes": [{"node_id": "protein", "label": "Fixture protein", "node_type": "PROTEIN",
                   "grounding": list(GROUNDINGS)},
                  {"node_id": "effect", "label": "Fixture effect", "node_type": "PHENOTYPE"}],
        "edges": [{"edge_id": "e1", "subject": "protein", "predicate": "CAUSES", "object": "effect",
                   "support": "SUPPORTED", "directness": "DIRECT", "evidence_kind": "EXPERIMENTAL",
                   "mechanism": "Fixture mechanism", "evidence": [evidence]}],
    }]}


@pytest.fixture
def site(tmp_path):
    rows = [{**worklist_row("PF00001", proteins=10),
             "description": "Preprint DOI: 10.1101/2021.06.03.446962) [[cite:PUB00098320]]."},
            worklist_row("PF00002", proteins=5)]
    cross = [{"pfam_id": "PF00001", "source_mech": "ProteinTraitsMech", "source_path": "data/traits/t.yaml",
              "source_section": "proteins", "source_record_id": "PTM:1", "uniprot_accession": "P75103",
              "link_basis": ["family_mention"]}]
    record = {**graph_record(), "curation_history": "history/records/PF00001", "discussions": [{
        "prompt": "Does it generalize?", "status": "OPEN",
        "notes": "Later alpha-NAD work PMID31599159 and doi10.1038/s41467-020-18981-w remain leads.",
        "evidence": [{"reference": "DOI:10.1234/discussion"}]}]}
    history = [{"timestamp": "2026-10-11T08:27:31Z", "agent": "Fixture curator", "action": "CREATE",
                "summary": "Curated graphs", "outcome": "changed",
                "description": "Grounded nodes in Chen et al. 2014 (PMID:25114049)."}]
    render_site(rows, [], input_ids={"worklist": "frozen"}, out_dir=tmp_path,
                cross_mech_rows=cross, cross_mech_sources={"ProteinTraitsMech": {
                    "repository": "https://github.com/CultureBotAI/proteintraitsmech", "commit": "a" * 40}},
                family_metadata={"PF00001": {"curation_status": "IN_PROGRESS", "record": record,
                                             "history": history}})
    return tmp_path


@pytest.mark.parametrize(("value", "links"), [
    ("Chen et al. 2014 (PMID:25114049).", [("https://pubmed.ncbi.nlm.nih.gov/25114049/", "PMID:25114049")]),
    ("Human hPop4 PMID10352175 and", [("https://pubmed.ncbi.nlm.nih.gov/10352175/", "PMID10352175")]),
    ("Af1521 doi10.1038/s41467-020-18981-w remain",
     [("https://doi.org/10.1038/s41467-020-18981-w", "doi10.1038/s41467-020-18981-w")]),
    ("Publisher DOI10.1186/1745-6150-4-19 differs",
     [("https://doi.org/10.1186/1745-6150-4-19", "DOI10.1186/1745-6150-4-19")]),
    ("(bioRxiv DOI: 10.1101/2021.06.03.446962)",
     [("https://doi.org/10.1101/2021.06.03.446962", "DOI: 10.1101/2021.06.03.446962")]),
    ("see PMC4503747.", [("https://pmc.ncbi.nlm.nih.gov/articles/PMC4503747/", "PMC4503747")]),
    ("(see https://example.org/a_(b)).", [("https://example.org/a_(b)", "https://example.org/a_(b)")]),
    ("https://doi.org/10.1093/femsre/fuab043).",
     [("https://doi.org/10.1093/femsre/fuab043", "https://doi.org/10.1093/femsre/fuab043")]),
    ("The2004doi10.1074/jbc.M401879200full paper", []),
    ("format PMIDs are not PMID:1234567890123", []),
    # Markdown around a reference stays text and never leaks into the target.
    ("See [10.1038/x](https://doi.org/10.1038/x).",
     [("https://doi.org/10.1038/x", "10.1038/x"), ("https://doi.org/10.1038/x", "https://doi.org/10.1038/x")]),
    ("Bold **10.1099/y** here", [("https://doi.org/10.1099/y", "10.1099/y")]),
    ("Code `10.1146/z` here", [("https://doi.org/10.1146/z", "10.1146/z")]),
    ("**https://example.org/a** and `PMID:123`",
     [("https://example.org/a", "https://example.org/a"), ("https://pubmed.ncbi.nlm.nih.gov/123/", "PMID:123")]),
    ('Cited "https://example.org/a"(2019)', [("https://example.org/a", "https://example.org/a")]),
    ("Ends 10.1234/abc; then 10.1234/def: and https://example.org/z,",
     [("https://doi.org/10.1234/abc", "10.1234/abc"), ("https://doi.org/10.1234/def", "10.1234/def"),
      ("https://example.org/z", "https://example.org/z")]),
    # The shapes the PR 368 review found (issue 369).
    ("**10.1099/ijs.0.003251-0**", [("https://doi.org/10.1099/ijs.0.003251-0", "10.1099/ijs.0.003251-0")]),
    ("**doi:10.1099/ijs.0.003251-0**",
     [("https://doi.org/10.1099/ijs.0.003251-0", "doi:10.1099/ijs.0.003251-0")]),
    ("`10.1146/annurev-cellbio-101011-155745`",
     [("https://doi.org/10.1146/annurev-cellbio-101011-155745", "10.1146/annurev-cellbio-101011-155745")]),
    ("`https://example.org/code`", [("https://example.org/code", "https://example.org/code")]),
    ("see https://example.org/x** and", [("https://example.org/x", "https://example.org/x")]),
    ("Table|10.1000/cell|next", [("https://doi.org/10.1000/cell", "10.1000/cell")]),
    ("| PMID:123 | https://example.org/t|", [("https://pubmed.ncbi.nlm.nih.gov/123/", "PMID:123"),
                                            ("https://example.org/t", "https://example.org/t")]),
    ('https://example.org/x"onmouseover="alert(1)', [("https://example.org/x", "https://example.org/x")]),
    ("'https://example.org/q'b and \u201chttps://example.org/r\u201d",
     [("https://example.org/q", "https://example.org/q"), ("https://example.org/r", "https://example.org/r")]),
    ("_https://example.org/i_ and ~~https://example.org/s~~",
     [("https://example.org/i", "https://example.org/i"), ("https://example.org/s", "https://example.org/s")]),
    # Issue 377: a closing parenthesis the token never opened ends it, and scanning resumes there.
    ("(https://a.example/x)-(https://b.example/y)",
     [("https://a.example/x", "https://a.example/x"), ("https://b.example/y", "https://b.example/y")]),
    ("see https://en.wikipedia.org/wiki/Foo_(bar) and (https://en.wikipedia.org/wiki/Foo_(bar)).",
     [("https://en.wikipedia.org/wiki/Foo_(bar)", "https://en.wikipedia.org/wiki/Foo_(bar)")] * 2),
    ("(doi:10.1234/abc)-(doi:10.1234/def)",
     [("https://doi.org/10.1234/abc", "doi:10.1234/abc"), ("https://doi.org/10.1234/def", "doi:10.1234/def")]),
    ("(see 10.1016/0005-2744(70)90044-4)",
     [("https://doi.org/10.1016/0005-2744%2870%2990044-4", "10.1016/0005-2744(70)90044-4")]),
    ("(http://)-(https://b.example/y)", [("https://b.example/y", "https://b.example/y")]),
])
def test_reference_tokens_link_exactly_and_keep_the_text(value, links):
    html = autolink(value)
    anchors = BeautifulSoup(html, "html.parser").find_all("a")
    assert [(a["href"], a.get_text()) for a in anchors] == links
    assert BeautifulSoup(html, "html.parser").get_text() == value


def test_free_text_without_references_renders_as_plain_escaping():
    value = 'Imported <script>alert("x")</script> & 10.5 mM, not a citation'
    assert autolink(value) == escape(value)
    linked = autolink("<b>PMID:1</b>")
    assert linked.startswith("&lt;b&gt;") and "<b>" not in linked


def test_source_description_links_a_doi_beside_interpro_markup():
    html = description_html("Preprint DOI: 10.1101/2021.06.03.446962) [[cite:PUB00098320]].",
                            "PF00001", labels={})
    hrefs = [a["href"] for a in BeautifulSoup(html, "html.parser").find_all("a")]
    assert hrefs == ["https://doi.org/10.1101/2021.06.03.446962",
                     "https://www.ebi.ac.uk/interpro/entry/pfam/PF00001/"]


def test_history_discussion_and_graph_text_link_their_citations(site):
    page = soup(site, "families/PF00001.html")
    history = {a["href"] for a in section(page, "Curation history and reviews").select("a[href]")}
    assert "https://pubmed.ncbi.nlm.nih.gov/25114049/" in history
    discussion = {a["href"] for a in section(page, "discussions").select("a[href]")}
    assert {"https://pubmed.ncbi.nlm.nih.gov/31599159/", "https://doi.org/10.1038/s41467-020-18981-w",
            "https://doi.org/10.1234/discussion"} <= discussion
    graphs = page.select_one("#causal-graphs")
    limitations = graphs.find("dt", string="Limitations").find_next_sibling("dd")
    assert [a["href"] for a in limitations.select("a")] == ["https://pubmed.ncbi.nlm.nih.gov/27211867/"]
    details = graphs.select_one("details")
    assert {a["href"] for a in details.select("blockquote a, p a")} == {
        "https://pubmed.ncbi.nlm.nih.gov/22713871/", "https://pubmed.ncbi.nlm.nih.gov/25707795/"}


def test_causal_graph_groundings_link_resolvers_and_other_family_pages(site):
    nodes = soup(site, "families/PF00001.html").select("#causal-graphs > ul > li")
    assert len(nodes) == 2
    anchors = {a.get_text(): a["href"] for a in nodes[0].select("a")}
    assert anchors == GROUNDINGS
    assert nodes[1].get_text().endswith("Ungrounded")
    assert not soup(site, "families/PF00001.html").select('a[href="#"]')


@pytest.mark.parametrize(("value", "expected"), [
    ("https://example.org/protein/1", "https://example.org/protein/1"),
    ("http://example.org/protein/2", "http://example.org/protein/2"),
    ("ftp://example.org/protein/3", ""),
    ("WormBase:WBGene00019763", "https://bioregistry.io/WormBase:WBGene00019763"),
    ("not a curie", ""),
])
def test_url_shaped_groundings_never_reach_bioregistry(value, expected):
    assert curie_url(value) == expected


def test_related_mech_proteins_open_the_uniprot_entry_page(site):
    table = soup(site, "families/PF00001.html").select_one('[aria-label="Cross-Mech records"]')
    proteins = [a["href"] for a in table.select("a") if a.get_text() == "P75103"]
    assert proteins == ["https://www.uniprot.org/uniprotkb/P75103/entry"]


def test_family_pages_keep_the_hook_the_feedback_route_attaches_to(site):
    """dashboard.js adds the prefilled issue link beside this download (browser-tested)."""
    for pfam in ("PF00001", "PF00002"):
        page = soup(site, f"families/{pfam}.html")
        hooks = page.select(f'a[download][href="{pfam}.json"]')
        assert len(hooks) == 1 and hooks[0].find_parent("section") is section(page, "Record source")
        assert page.select_one('script[src="../dashboard.js"]')
    script = (site / "dashboard.js").read_text()
    assert "https://github.com/CultureBotAI/DUFMech/issues/new" in script
    assert "\n  initFeedback();\n" in script


def test_only_overlay_families_link_their_curation_overlay_for_editing(site):
    curated = section(soup(site, "families/PF00001.html"), "Record source")
    edits = [a["href"] for a in curated.select("a") if a.get_text() == "Edit the curation overlay on GitHub"]
    assert edits == ["https://github.com/CultureBotAI/DUFMech/edit/main/curation/families/PF00001.yaml"]
    seeded = section(soup(site, "families/PF00002.html"), "Record source")
    assert not [a for a in seeded.select("a") if "/edit/" in a["href"]]


def test_family_pages_keep_the_hooks_the_breadcrumb_trail_extends(site):
    """dashboard.js turns this trail into a Breadcrumb nav through the seed category (browser-tested)."""
    for pfam in ("PF00001", "PF00002"):
        page = soup(site, f"families/{pfam}.html")
        trail = page.select_one("main").find(True)
        assert trail.name == "p" and trail.select_one('a[href="../index.html"]')
        seed = page.select_one("main .record-facts").find("dt", string="Seed status").find_next_sibling("dd")
        assert (site / "category" / (seed.get_text().strip().lower().replace(" ", "_") + ".html")).is_file()
    assert "\n  initBreadcrumbs();\n" in (site / "dashboard.js").read_text()


@pytest.mark.parametrize(("page", "prefix", "label"), [
    ("map.html", "map-data", "Families plotted on the text map"),
    ("sequence-map.html", "seq-data", "Proteins plotted on the sequence map"),
])
def test_map_pages_offer_a_table_alternative_and_a_noscript_route(site, page, prefix, label):
    html = soup(site, page)
    details = html.select_one(f"details#{prefix}")
    assert details.summary.get_text() == "View data as table"
    region = details.select_one(f'.table-wrap[role="region"][tabindex="0"][aria-label="{label}"]')
    assert region.select_one("table tbody") is not None and not region.select("tbody tr")
    assert details.select_one(f'#{prefix}-count[role="status"]')
    assert details.select_one(f"button#{prefix}-more").has_attr("hidden")
    assert html.select_one('noscript a[href="index.html#families"]')
    assert f"mapDataTable('{prefix}'" in (site / "dashboard.js").read_text()


def test_not_found_page_is_self_contained_absolute_and_checked(site):
    page = soup(site, "404.html")
    assert page.h1.get_text() == "Page not found"
    assert not page.select("link[rel=stylesheet], script[src]")
    assert page.select_one("style") and "--accent" in page.select_one("style").get_text()
    assert "mech-theme" in page.select_one("script").get_text()
    references = [element.get(key) for element in page.find_all(True)
                  for key in ("href", "src", "action") if element.get(key)]
    relative = [ref for ref in references if not re.match(r"(https?:|data:|#)", ref)]
    assert relative == []
    form = page.select_one("main form[role=search]")
    assert form["action"] == SITE_URL + "index.html#families"
    assert form.select_one("input[name=q]")
    assert page.select_one(f'main a[href="{SITE_URL}index.html#families"]')
    assert page.select_one('a.skip-link[href="#main"]') and page.select_one("main#main")
    budgets = json.loads(Path("conf/pages_budgets.json").read_text())
    assert check_site(site, budgets)[0] == []


def test_contract_requires_an_absolute_not_found_page(site):
    budgets = json.loads(Path("conf/pages_budgets.json").read_text())
    not_found = site / "404.html"
    original = not_found.read_text()
    not_found.write_text(original.replace(f'href="{SITE_URL}categories.html"', 'href="categories.html"', 1))
    errors = check_site(site, budgets)[0]
    assert errors == ["relative reference in 404.html, which is served at missing paths: categories.html"]
    # Own-site absolute links are resolved against the build, not skipped as external (issue 370).
    not_found.write_text(original.replace(f'href="{SITE_URL}categories.html"', f'href="{SITE_URL}nope.html"', 1))
    assert check_site(site, budgets)[0] == [f"broken local link: 404.html -> {SITE_URL}nope.html"]
    not_found.write_text(original.replace(f'href="{SITE_URL}index.html#families"',
                                          f'href="{SITE_URL}index.html#nowhere"', 1))
    assert check_site(site, budgets)[0] == [f"missing anchor: 404.html -> {SITE_URL}index.html#nowhere"]
    not_found.write_text(original.replace(f'href="{SITE_URL}map.html"', f'href="{SITE_URL}../map.html"', 1))
    assert check_site(site, budgets)[0] == [f"broken local link: 404.html -> {SITE_URL}../map.html"]
    not_found.write_text(original.replace(f'href="{SITE_URL}map.html"', f'href="{SITE_URL}families/../map.html"', 1))
    assert check_site(site, budgets)[0] == []
    not_found.unlink()
    assert "missing required site artifact: 404.html" in check_site(site, budgets)[0]
    not_found.write_text(original)
    (site / "orphan.html").write_text("<!doctype html><title>Unlinked</title>")
    assert check_site(site, budgets)[0] == ["unreachable HTML pages: orphan.html"]


def test_every_sibling_url_uses_a_verified_route(site):
    seen = []
    for path in site.rglob("*.html"):
        for element in soup(site, str(path.relative_to(site))).find_all(True):
            for key in ("href", "src", "action"):
                value = element.get(key) or ""
                if "culturebotai.github.io" in value and not value.startswith(SITE_URL):
                    seen.append(value)
    assert seen and all(value.startswith(SIBLING_ROUTES) for value in seen), sorted(set(seen))
    assert any(value.startswith("https://culturebotai.github.io/TaxonMech/pages/taxon.html?id=")
               for value in seen)
