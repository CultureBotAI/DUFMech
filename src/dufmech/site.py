"""Deterministic, progressively enhanced family and catalogue pages."""

from __future__ import annotations

import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from collections.abc import Container
from html import escape
from pathlib import Path
from typing import Any

from dufmech.report import ReportError
from dufmech.site_data import (
    IPR_RE,
    autolink,
    curie_url,
    description_html,
    group_members,
    link,
    pfam_url,
    reference_url,
    source_link,
)
from dufmech.site_sources import REPOSITORY

SITE_URL = "https://culturebotai.github.io/DUFMech/"
PAGE_SIZE = 50
SORTS = {
    "proteins-desc": "Proteins: high to low", "proteins-asc": "Proteins: low to high",
    "pfam_id-asc": "Pfam accession", "name-asc": "Family name: A to Z",
    "structures-desc": "Structures: high to low",
}
GUIDE = """<section class="section legend" aria-labelledby="status-guide">
<h2 id="status-guide">Status and evidence</h2><dl>
<dt>Seed status</dt><dd>A name-based classification of frozen InterPro/Pfam metadata.
UNKNOWN CANDIDATE means the metadata explicitly says the function is unknown.
KNOWN HISTORICAL DUF means a DUF name matched without that wording;
this heuristic is not proof of a known function and does not establish experimental
characterization. EX DUF means Pfam renamed the family away from a DUF/UPF name, as
recorded in Pfam's previous identifiers; a rename usually follows published work on some
members but is naming history, not proof of function for every member. Some EX DUF
families' current names or descriptions still say the function is unknown; their
classification basis lists this, and scoring does not treat them as characterized.
FALSE POSITIVE TEXT HIT means the naming rules did not match.</dd>
<dt>Characterization</dt><dd>A separate evidence-scoring result. UNSCORED means no score
has been calculated; it is not evidence that the family lacks a known function.
Missing scores are not negative evidence. PARTIALLY CHARACTERIZED has partial support;
KNOWN HISTORICAL DUF can inherit the seed label or reflect a known-function signal.
Neither label implies experimental validation.</dd>
<dt>Evidence counts</dt><dd>Source-specific signals, not unique proteins, publications,
or confidence scores. Known counts Rhea reactions and experimentally supported GO
molecular-function annotations. Partial counts functional/domain assignments.
Context counts structural, environmental, orthology, interaction and neighborhood signals;
context alone does not assign function. Repeated annotations may not be independent.</dd>
<dt>Curation status</dt><dd>Reported separately from seed classification and characterization.
SNAPSHOT ONLY means no curated metadata was supplied for this build. SEEDED denotes
a source-derived record, not an expert-reviewed functional claim.</dd>
<dt>Missing counts</dt><dd>Not available means the source did not supply that counter.
A zero is a reported count. Not scored means evidence counts are unavailable.</dd>
</dl></section>"""


def text(value: Any) -> str:
    return escape(str(value if value is not None else ""))


def human(value: str) -> str:
    return text(value.replace("_", " "))


def count(value: int | None) -> str:
    return "Not available" if value is None else f"{value:,}"


def json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":")) + "\n"


def term_link(curie: str, *, families: Container[str] = (), pfam: str = "", root: str = "../") -> str:
    """Link a displayed CURIE; one naming another family in this catalogue opens its page.

    The page's own family resolves externally, as its Grounding section does, since a
    link back to the same page goes nowhere.
    """
    prefix, _, local = curie.partition(":")
    if prefix == "Pfam" and local != pfam and local in families:
        return f'<a href="{root}families/{local}.html">{text(curie)}</a>'
    return link(curie_url(curie), curie)


def artifact_link(reference: dict, label: str, root: str = "../") -> str:
    url = reference_url(reference)
    if url:
        return link(url, label)
    local = reference.get("local_source", "")
    if local and re.fullmatch(r"[A-Za-z0-9_./-]+", local) and ".." not in Path(local).parts:
        return f'<a href="{root}{text(local)}">{text(label)}</a>'
    return text(label)


def curated_assertions(record: dict) -> str:
    assertions = []
    for assertion in record.get("assertions", []):
        evidence = "".join(
            f'<li>{link(reference_url(ref) or ref.get("source_url", ""), ref["reference"])}'
            f'<blockquote>{autolink(ref["snippet"])}</blockquote><p>{autolink(ref["explanation"])}</p></li>'
            for ref in assertion.get("evidence", [])
        )
        assertions.append(f'<h3>{text(assertion["assertion_id"])}</h3>'
                          f'<p>{autolink(assertion["statement"])}</p>'
                          f'<p>Scope: {autolink(assertion["scope"])}. '
                          f'Evidence kind: {human(assertion["evidence_kind"])}.</p><ul>{evidence}</ul>')
    return "".join(assertions) or "<p>No curated functional assertions supplied.</p>"


def curated_graphs(record: dict, *, families: Container[str] = (), pfam: str = "") -> str:
    graphs = []
    for graph in record.get("causal_graphs", []):
        labels = {node["node_id"]: node["label"] for node in graph["nodes"]}
        rows = []
        for edge in graph["edges"]:
            evidence = "".join(
                f'<li>{link(ref["source_url"], ref["reference"])}'
                f'<blockquote>{autolink(ref["snippet"])}</blockquote>'
                f'<p>{autolink(ref["explanation"])}</p></li>' for ref in edge["evidence"]
            )
            rows.append(
                f'<tr id="causal-edge.{text(graph["graph_id"])}.{text(edge["edge_id"])}">'
                f'<td><code>{text(edge["subject"])}</code>: {text(labels[edge["subject"]])}</td>'
                f'<td class="causal-relation">{human(edge["predicate"])}</td>'
                f'<td><code>{text(edge["object"])}</code>: '
                f'{text(labels[edge["object"]])}</td>'
                f'<td>{human(edge["support"])} / {human(edge["directness"])} / '
                f'{human(edge["evidence_kind"])}</td><td><details>'
                f'<summary>Evidence ({len(edge["evidence"])})</summary>'
                f'<p>{autolink(edge["mechanism"])}</p><ul>{evidence}</ul></details></td></tr>'
            )
        nodes = "".join(
            f'<li><code>{text(node["node_id"])}</code>: {text(node["label"])}; '
            f'{human(node["node_type"])}; '
            + (", ".join(term_link(curie, families=families, pfam=pfam) for curie in node.get("grounding", []))
               or "Ungrounded")
            + '</li>' for node in graph["nodes"]
        )
        feedback = (f'<p>Feedback: {autolink(graph["feedback_explanation"])}</p>'
                    if graph.get("feedback_explanation") else "")
        graphs.append(
            f'<h3 id="causal-graph-{text(graph["graph_id"])}">{text(graph["title"])}</h3>'
            f'<p>{human(graph["scope_status"])}</p>'
            f'<dl class="record-facts"><dt>Scope</dt><dd>{autolink(graph["scope"])}</dd>'
            f'<dt>Context</dt><dd>{autolink(graph["context"])}</dd>'
            f'<dt>Family mapping</dt><dd>{autolink(graph["family_mapping"])}</dd>'
            f'<dt>Limitations</dt><dd>{autolink(graph["limitations"])}</dd></dl>'
            f'<ul>{nodes}</ul>{feedback}'
            '<div class="table-wrap" tabindex="0" role="region" aria-label="Causal edges">'
            '<table><caption>Directed causal edges</caption><thead><tr>'
            '<th scope="col">Source</th><th scope="col">Relation</th><th scope="col">Target</th>'
            '<th scope="col">Support</th><th scope="col">Mechanism and evidence</th>'
            f'</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'
        )
    return "".join(graphs) or "<p>No curated causal graph supplied. This is not evidence of absence.</p>"


def structured_content(value: Any) -> str:
    """Keep optional governed curation fields visible without inventing their semantics."""
    if isinstance(value, dict):
        return "<dl>" + "".join(f"<dt>{human(key)}</dt><dd>{structured_content(item)}</dd>"
                                for key, item in value.items()) + "</dl>"
    if isinstance(value, list):
        return "<ul>" + "".join(f"<li>{structured_content(item)}</li>" for item in value) + "</ul>"
    url = reference_url({"reference": str(value)})
    return link(url, str(value)) if url else autolink(value)


def page_shell(title: str, body: str, provenance: dict, *, root: str = "", assets: str = "") -> str:
    source = provenance.get("worklist", {})
    pinned = source_link(source.get("repository", REPOSITORY), source.get("commit", ""),
                         source.get("path", ""))
    version = link(pinned, f"Corpus source {source.get('commit', '')[:12]}") if pinned else ""
    inputs = " / ".join(f"{text(k)}: {text(v)}" for k, v in provenance["inputs"].items())
    assets = assets or (f'<script src="{root}theme.js"></script><link rel="stylesheet" href="{root}style.css">\n'
                        f'<script src="{root}dashboard.js" defer></script>')
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{text(title)} | DUFMech</title><link rel="icon" href="data:,">
{assets}</head><body>
<a class="skip-link" href="#main">Skip to content</a><header>
<a class="brand" href="{root}index.html">DUFMech</a>
<nav aria-label="Project navigation"><a href="{root}index.html#families">Browse families</a>
<a href="{root}map.html">Text map</a><a href="{root}sequence-map.html">Sequence map (pLM)</a>
<a href="{root}categories.html">Categories</a><a href="{root}sources.html">Sources &amp; schema</a>
<a href="{REPOSITORY}">Repository</a>
<a href="https://culturebotai.github.io/mechs/">All Mech projects</a></nav>
<form class="header-search" action="{root}index.html#families" method="get" role="search">
<input type="search" name="q" placeholder="Search Pfam, DUF, InterPro…" aria-label="Search DUF/Pfam families">
<button type="submit">Search</button></form>
<label class="theme-label">Theme <select id="theme-control" aria-label="Color theme">
<option value="system">System</option><option value="light">Light</option>
<option value="dark">Dark</option></select></label></header>
<main id="main">{body}</main><footer>
<p>Site build <code>{provenance['build_id']}</code>. {version}<br>{inputs}</p>
<p>Project data: <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>.
Code: <a href="{REPOSITORY}/blob/main/LICENSE-CODE">BSD 3-Clause</a>.
Redistributed source material retains its applicable third-party terms.
<a href="{REPOSITORY}/blob/main/LICENSE">License policy</a>.</p></footer></body></html>"""


def family_row(row: dict, root: str = "") -> str:
    pfam = row["pfam_id"]
    score = row["characterization_status"] or "UNSCORED"
    signals = "Not scored" if score == "UNSCORED" else (
        f"Known: {count(row['known_evidence_count'])}; partial: {count(row['partial_evidence_count'])}; "
        f"context: {count(row['context_evidence_count'])}"
    )
    summary = row["cross_mech"]
    other = "; ".join(f"{mech}: {n}" for mech, n in summary["records_by_mech"].items())
    if summary["protein_traits_record"]:
        other += ("; " if other else "") + "ProteinTraitsMech trait record"
    if summary.get("scanned") is False:
        other += ("; " if other else "") + "not covered by the cross-Mech scan"
    return f"""<tr id="{pfam}"><td><a href="{root}families/{pfam}.html">{pfam}</a></td>
<td><strong>{text(row['name'] or row['short_name'] or pfam)}</strong><br>{text(row['short_name'])}</td>
<td>{human(row['unknown_status'])}</td><td>{human(score)}</td><td>{signals}</td>
<td class="num">{count(row['proteins'])}</td><td class="num">{count(row['structures'])}</td>
<td class="num">{count(row['alphafold_models'])}</td><td>{text(other)}</td>
<td>{human(row['curation_status'])}</td></tr>"""


def table(rows: list[dict], root: str = "") -> str:
    return f"""<div class="table-wrap" tabindex="0" role="region" aria-label="Family catalogue">
<table id="family-table"><thead><tr><th scope="col">Pfam</th><th scope="col">Family</th>
<th scope="col">Seed status</th><th scope="col">Characterization</th><th scope="col">Evidence counts</th>
<th scope="col">Proteins</th><th scope="col">Structures</th><th scope="col">AlphaFold</th>
<th scope="col">Other Mechs</th><th scope="col">Curation status</th></tr></thead>
<tbody>{''.join(family_row(row, root) for row in rows)}</tbody></table></div>"""


def options(values: dict[str, str]) -> str:
    return "".join(f'<option value="{text(key)}">{text(label)}</option>'
                   for key, label in values.items())


def listing(
    rows: list[dict], families: list[dict], *, root: str, page: int,
    page_paths: list[str], category: str = "",
) -> str:
    statuses = {v: v.replace("_", " ") for v in sorted({r["unknown_status"] for r in families})}
    characterizations = {v: v.replace("_", " ") for v in sorted(
        {r["characterization_status"] or "UNSCORED" for r in families})}
    curations = {v: v.replace("_", " ") for v in sorted(
        {r["curation_status"] for r in families})}
    cat_counts = Counter(r["unknown_status"] for r in families)
    cat_links = "".join(
        f'<li><a href="{root}category/{status.lower()}.html">{human(status)}</a> ({n:,})</li>'
        for status, n in sorted(cat_counts.items())
    )
    static_links = "".join(
        f'<a href="{root}{path}" aria-label="Catalogue page {i + 1}"'
        f'{" aria-current=page" if i == page else ""}>{i + 1}</a>'
        for i, path in enumerate(page_paths)
    )
    return f"""<section id="families" class="section" data-catalogue data-root="{root}"
data-category="{text(category)}" data-page="{page + 1}">
<h2>Families</h2><p><a href="{root}index.json" download>Download the complete family index (JSON)</a></p>
<div class="browse-layout">
<aside class="facet-sidebar" aria-label="Catalogue filters">
<form id="family-controls" class="controls" role="search" hidden>
<label>Search accession or family <input id="family-query" type="search" name="q"></label>
<label>Seed status <select id="seed-filter"><option value="">All seed statuses</option>
{options(statuses)}</select></label>
<label>Characterization <select id="characterization-filter"><option value="">All characterizations</option>
{options(characterizations)}</select></label>
<label>Curation status <select id="curation-filter"><option value="">All curation statuses</option>
{options(curations)}</select></label>
<label>Sort by <select id="family-sort">{options(SORTS)}</select></label>
<button id="reset-families" type="button">Clear search and filters</button></form>
<div class="static-facets"><h3>Seed categories</h3><ul>
<li><a href="{root}index.html#families">All families</a> ({len(families):,})</li>
{cat_links}</ul>
<h3>Embedding browsers</h3><ul>
<li><a href="{root}map.html">Text embedding map</a></li>
<li><a href="{root}sequence-map.html">Sequence map (ESM-2 pLM)</a></li></ul></div>
</aside>
<div class="browse-results">
<p id="family-count" role="status" aria-live="polite">{len(rows):,} of {len(families):,} families.
Page {page + 1} of {len(page_paths)}.</p>
<p id="catalogue-error" role="alert" hidden></p>
<noscript><p>All families are available through the numbered catalogue pages and JSON download.</p></noscript>
{table(rows[page * PAGE_SIZE:(page + 1) * PAGE_SIZE], root)}
<p id="family-empty" hidden>No matching families. Clear the search or filters to try again.</p>
<div class="pagination" id="family-pagination" hidden>
<button id="previous-families" type="button" aria-label="Previous page">Previous</button>
<span id="family-page"></span><button id="next-families" type="button" aria-label="Next page">Next</button>
</div><nav id="static-pagination" class="pagination" aria-label="Catalogue pages">{static_links}</nav>
</div></div></section>"""


def corpus_visual(families: list[dict]) -> str:
    buckets = [("0", 0, 0), ("1-99", 1, 99), ("100-999", 100, 999),
               ("1,000-9,999", 1000, 9999), ("10,000+", 10000, math.inf)]
    counts = [(label, sum(1 for r in families if r["proteins"] is not None
                         and low <= r["proteins"] <= high)) for label, low, high in buckets]
    counts.append(("Not available", sum(r["proteins"] is None for r in families)))
    maximum = max([n for _, n in counts] + [1])
    bars = "".join(f'<div class="histogram-row"><span>{label}</span>'
                   f'<span class="bar-track"><span class="bar" style="width:{n / maximum * 100:.3f}%"></span>'
                   f'</span><span>{n:,}</span></div>' for label, n in counts)
    return f"""<figure class="corpus-visual"><figcaption><strong>Protein family sizes</strong><br>
Families by reported InterPro protein count</figcaption>{bars}
<p>Each family contributes once. Proteins can belong to multiple families.</p></figure>"""


def cross_row(row: dict, sources: dict, root: str = "") -> str:
    pfam = row.get("pfam_id", "")
    family = text(row.get("short_name") or pfam)
    family = (f'<a href="{root}families/{pfam}.html">{family} ({pfam})</a>' if pfam
              else f"{family}<br>not in worklist")
    source = sources.get(row["source_mech"], {})
    url = source_link(source.get("repository", ""), source.get("commit", ""), row["source_path"])
    record = link(url, row.get("source_record_label") or row.get("source_record_id") or row["source_path"])
    accession = row.get("uniprot_accession", "")
    protein = link(f"https://www.uniprot.org/uniprotkb/{accession}/entry", accession) if accession else ""
    return (f'<tr><td>{family}</td><td>{text(row["source_mech"])}</td><td>{record}</td>'
            f'<td>{protein}<br>{text(row.get("protein_label", ""))}</td>'
            f'<td>{human(", ".join(row.get("link_basis", [])))}</td></tr>')


UNSCANNED_NOTE = ("<p>This family joined the worklist after the frozen cross-Mech scan, so "
                  "other Mechs were not searched for it. Missing links here are not evidence "
                  "that other Mechs lack it; rows shown come from mentions of a former DUF/UPF "
                  "name.</p>")


def cross_table(rows: list[dict], sources: dict, root: str = "") -> str:
    if not rows:
        return "<p>No cross-Mech examples are present in the supplied snapshot.</p>"
    return ('<div class="table-wrap" tabindex="0" role="region" aria-label="Cross-Mech records">'
            '<table><thead><tr><th>Family</th><th>Mech</th><th>Record</th><th>Protein</th>'
            '<th>Link basis</th></tr></thead><tbody>'
            + "".join(cross_row(row, sources, root) for row in rows) + "</tbody></table></div>")


def domain_visual(members: list[dict], *, dataset: bool = False) -> str:
    if not members:
        return ("<p>No residue-level domain match evidence is available in this build. "
                "Structure and AlphaFold counters do not supply coordinates or establish function.</p>")
    figures = []
    for member in members:
        length = member["length"]
        accession = member["uniprot_accession"]
        ranges = ", ".join(f"{a}-{b}" for a, b in member["ranges"])
        bars = "".join(
            f'<span class="domain-match" style="left:{(a - 1) / length * 100:.4f}%;'
            f'width:{(b - a + 1) / length * 100:.4f}%"></span>' for a, b in member["ranges"]
        )
        figures.append(f'<figure class="domain-figure"><figcaption>'
                       f'{link(f"https://www.uniprot.org/uniprotkb/{accession}/entry", accession)}'
                       f' ({length:,} amino acids): residues {ranges}</figcaption>'
                       f'<div class="domain-track" role="img" '
                       f'aria-label="{accession}: matches at residues {ranges} of {length}">{bars}</div>'
                       f'<p>{link(member.get("member_source_url", member.get("source_url", "")), "Match source")}'
                       '</p></figure>')
    attribution = ('<p><a href="../sources.html#member-dataset">Frozen member dataset and attribution</a></p>'
                   if dataset else "")
    return ("<p>Observed Pfam match ranges on supplied protein sequences; "
            "these are sequence coordinates, not a three-dimensional structure. "
            "Coordinates are one-based and inclusive. Only members in the supplied snapshot are shown; "
            "this is not a complete family alignment.</p>" + "".join(figures) + attribution)


def member_dataset(provenance: dict) -> str:
    dataset = provenance.get("members", {})
    if not dataset:
        return ""
    source = dataset.get("source", {})
    return f"""<section id="member-dataset"><h2>Protein domain match dataset</h2>
<p>{text(dataset.get('snapshot_id', ''))}: {text(dataset.get('row_count', ''))} frozen member rows
across {text(dataset.get('family_count', ''))} families. This subset is not a complete family membership census.</p>
<p>Generated: {text(dataset.get('generated_at', ''))}. Worklist seed: {text(dataset.get('seed_snapshot_id', ''))}.
SHA-256: <code>{text(dataset.get('sha256', ''))}</code>.</p>
<p>{artifact_link(dataset, 'Download frozen member rows (JSON)', '')} |
{artifact_link({'local_source': dataset.get('local_manifest', '')}, 'Download checksum manifest (JSON)', '')}</p>
{('<p>' + artifact_link({'local_source': dataset['local_tsv']}, 'Download member table (TSV)', '') + '</p>') if dataset.get('local_tsv') else ''}
<p>Source: {link(source.get('url', ''), source.get('name', 'InterPro, UniProtKB and UniRef'))}.
Pfam membership and match coordinates: InterPro,
<a href="https://interpro-documentation.readthedocs.io/en/latest/license.html">CC0</a>.
Protein metadata and UniRef mappings: the UniProt Consortium,
<a href="https://rest.uniprot.org/help/license">CC BY 4.0</a>.
The figures render the recorded coordinates without inferring structure or function.</p></section>"""


def protein_example_dataset(provenance: dict) -> str:
    dataset = provenance.get("protein_examples", {})
    if not dataset:
        return ""
    counts = dataset.get("counts", {})
    return (f'<section><h2>Protein sequence example dataset</h2>'
            f'<p>{text(dataset.get("snapshot_id", ""))}: {count(counts.get("proteins"))} proteins; '
            f'{count(counts.get("by_status", {}).get("HAS_SEQUENCE_EXAMPLE"))} families with '
            f'sequences out of {count(counts.get("total"))} audited families.</p><p>'
            + artifact_link(dataset, "Frozen examples (JSON)", "") + ' | '
            + artifact_link({"local_source": dataset.get("local_manifest", "")}, "Manifest", "")
            + '</p><p>UniProt Consortium, '
            '<a href="https://rest.uniprot.org/help/license">CC BY 4.0</a>. '
            'Sequence examples are family-membership references, not functional claims.</p></section>')


def protein_examples_section(row: dict | None) -> str:
    if row is None:
        return ""
    examples = row["examples"]
    if examples:
        rendered = []
        for example in examples[:10]:
            origin_links = []
            for origin in example["origins"]:
                label = (f'UniProt family search, rank {origin["rank"]}'
                         if origin.get("kind") == "UNIPROT_FAMILY_SEARCH"
                         else origin["mech"] + ": " + origin["record_id"])
                origin_links.append(f'<li>{link(origin["url"], label)}</li>')
            origins = "".join(origin_links)
            accession = example["uniprot_accession"]
            rendered.append(
                f'<tr><td data-label="UniProt">{link(example["source_url"], accession)}</td>'
                f'<td data-label="Protein / organism">{text(example["protein_name"])}<br>{text(example["organism"])}</td>'
                f'<td data-label="Sequence">{example["sequence_length"]} aa; version {example["sequence_version"]}'
                f'<br>UniProt {text(example["uniprot_release"])}</td>'
                f'<td data-label="Provenance">{human(example["sequence_origin"])}'
                f'<details><summary>{len(example["origins"])} source '
                f'{"reference" if len(example["origins"]) == 1 else "references"}</summary>'
                f'<ul>{origins}</ul></details></td></tr>'
            )
        body = (f'<p>{len(examples)} verified sequence {"example" if len(examples) == 1 else "examples"}. '
                f'<a href="{row["pfam_id"]}.fasta" download>FASTA</a></p>'
                '<div class="table-wrap"><table class="protein-examples-table"><thead><tr><th>UniProt</th><th>Protein / organism</th>'
                '<th>Sequence</th><th>Provenance</th></tr></thead><tbody>'
                + "".join(rendered) + '</tbody></table></div>')
        if len(examples) > 10:
            body += '<p>First 10 shown; the FASTA and family JSON contain all examples.</p>'
    else:
        body = ('<p>No sibling protein candidate in the scanned commits.</p>'
                if row["status"] == "NO_SIBLING_CANDIDATE" else
                '<p>Family not scanned in the discovery snapshot.</p>'
                if row["status"] == "NOT_SCANNED" else
                '<p>The frozen UniProt family search returned zero members.</p>'
                if row["status"] == "NO_UNIPROT_MEMBERS" else
                '<p>No candidate passed exact-accession and current Pfam checks.</p>')
    if "direct_discovery" in row:
        search = row["direct_discovery"]
        body += (f'<p>{len(examples)} sampled from {count(search["total"])} UniProt family members; '
                 f'release {text(search["release"])}. Ranked by annotation score, then accession. '
                 'This is not a representative or reviewed-only sample. '
                 f'{link(search["url"], "UniProt family query")}</p>')
    if row["unresolved"]:
        body += (f'<details><summary>{len(row["unresolved"])} unresolved candidates</summary><ul>'
                 + "".join(f'<li>{text(item["uniprot_accession"])}: {human(item["reason"])}</li>'
                           for item in row["unresolved"]) + '</ul></details>')
    return ('<section id="protein-examples"><h2>Protein sequence examples</h2>' + body
            + '<p>Pfam membership is not functional evidence. Whole-protein sequences do not '
            'establish domain boundaries. A coverage gap here is not absence from UniProt.</p>'
            '<p>Sequences and metadata: UniProt Consortium, '
            '<a href="https://rest.uniprot.org/help/license">CC BY 4.0</a>.</p></section>')


def record_page(row: dict, metadata: dict, context: dict) -> str:
    pfam = row["pfam_id"]
    interpro = row["interpro_id"]
    label = row["name"] or row["short_name"] or pfam
    grounding = link(pfam_url(pfam), f"{pfam}: {label}")
    if IPR_RE.fullmatch(interpro):
        ipr_label = metadata.get("interpro_label") or f"integrated entry for {label}"
        grounding += "<br>" + link(f"https://www.ebi.ac.uk/interpro/entry/InterPro/{interpro}/",
                                   f"{interpro}: {ipr_label}")
    elif not interpro:
        grounding += "<br>No integrated InterPro identifier in the snapshot."
    description = description_html(row["description"], pfam, labels=context["labels"],
                                   publications=metadata.get("publications"))
    refs = []
    for ref in metadata.get("evidence", []):
        refs.append(f'<li>{link(reference_url(ref), ref.get("label") or ref.get("id") or ref.get("reference") or ref.get("url", "Source"))}'
                    f' {autolink(ref.get("description", ""))}</li>')
    if "[cite:PUB" in row["description"]:
        refs.append(f'<li>{link(pfam_url(pfam), "InterPro entry and its literature references")}. '
                    'PUB identifiers are internal InterPro references, not PubMed identifiers. '
                    'Unresolved citations link to the originating entry.</li>')
    source_api = row["source_url"]
    if source_api:
        refs.append(f'<li>{link(source_api, "Frozen description source: InterPro/Pfam API")}</li>')
    evidence = "<ul>" + "".join(refs) + "</ul>" if refs else "<p>No evidence references supplied.</p>"
    evidence += "<p>Source descriptions and links are provenance, not independent functional validation.</p>"
    if row["characterization_status"]:
        evidence += (f"<p>Scored signals: known {count(row['known_evidence_count'])}; "
                     f"partial {count(row['partial_evidence_count'])}; "
                     f"context {count(row['context_evidence_count'])}.</p>")
    else:
        evidence += "<p>Evidence counts: not scored.</p>"
    events = []
    for event in metadata.get("history", []):
        events.append(f'<li><time>{text(event.get("timestamp", event.get("date", "")))}</time> '
                      f'{text(event.get("agent", event.get("curator", "")))}: '
                      f'{text(event.get("action", event.get("event_type", "")))}. '
                      f'{autolink(event.get("summary", event.get("description", "")))}'
                      f' {artifact_link(event, event.get("source_path", "History artifact"))}'
                      f'<p>{autolink(event.get("description", ""))} {text(event.get("outcome", ""))}</p></li>')
    history = "<ol>" + "".join(events) + "</ol>" if events else "<p>No retained curation events supplied.</p>"
    reviews = "".join(f'<li>{artifact_link(ref, ref.get("label", "Retained review"))}'
                      f'<p>Scope: {autolink(ref.get("scope", "Not supplied"))}. '
                      f'Scientific review: {text(ref.get("scientific_review", "Not supplied"))}.</p></li>'
                      for ref in metadata.get("reviews", []))
    history += f"<ul>{reviews}</ul>" if reviews else "<p>No retained review supplied.</p>"
    source = metadata.get("source", context["provenance"].get("worklist", {}))
    source_url = source_link(source.get("repository", REPOSITORY), source.get("commit", ""),
                             source.get("path", ""))
    own_source = (link(source_url, source.get("path", "Record source")) if source_url else
                  "No verified immutable repository source supplied.")
    if metadata.get("local_source"):
        own_source += "<br>" + artifact_link(metadata, "Family YAML in this build")
    if metadata.get("record", {}).get("curation_history"):
        # data/families is a generated projection; curation is edited in the overlay,
        # which is the only source of curation_history.
        own_source += "<br>" + link(f"{REPOSITORY}/edit/main/curation/families/{pfam}.yaml",
                                    "Edit the curation overlay on GitHub")
    counters = "".join(f'<dt>{human(key)}</dt><dd>{count(row[key])}</dd>' for key in (
        "proteins", "matches", "proteomes", "taxa", "structures", "alphafold_models", "domain_architectures",
    ))
    seed_reasons = "; ".join(row["candidate_reasons"])
    related = "".join(f"<section><h2>{human(key)}</h2>{structured_content(metadata['record'][key])}</section>"
                      for key in ("discussions", "datasets", "cross_corpus_links")
                      if metadata.get("record", {}).get(key))
    body = f"""<p><a href="../index.html">All families</a> / {pfam}</p>
<h1>{pfam}: {text(row['short_name'] or label)}</h1><p class="lede">{text(label)}</p>
<dl class="record-facts"><dt>Curation status</dt><dd>{human(row['curation_status'])}</dd>
<dt>Seed status</dt><dd>{human(row['unknown_status'])}</dd><dt>Characterization</dt>
<dd>{human(row['characterization_status'] or 'UNSCORED')}</dd></dl>
<section><h2>Grounding</h2><p>{grounding}</p></section>
<section><h2>Source description</h2><p class="description">{description or 'No description supplied.'}</p></section>
<section><h2>Evidence and references</h2>{evidence}</section>
<section><h2>Curated functional assertions</h2>{curated_assertions(metadata.get('record', {}))}</section>
<section id="causal-graphs"><h2>Causal graphs</h2>{curated_graphs(metadata.get('record', {}), families=context['labels'], pfam=pfam)}</section>
{protein_examples_section(context['protein_examples'].get(pfam))}
<section id="domain-matches"><h2>Domain matches</h2>{domain_visual(context['members'].get(pfam, []), dataset=bool(context['provenance'].get('members')))}</section>
<section><h2>Snapshot counters</h2><dl class="record-facts">{counters}</dl></section>
<section><h2>Classification basis</h2><p>{human(seed_reasons) or 'No seed reasons supplied.'}</p>
<p>{human('; '.join(row['demotion_reasons'])) or 'No scoring reasons supplied.'}</p></section>
<section><h2>Related Mech records</h2>{UNSCANNED_NOTE if row['cross_mech'].get('scanned') is False else ''}
{cross_table(context['cross'].get(pfam, []), context['cross_sources'], '../')}</section>
{related}
<section><h2>Curation history and reviews</h2>{history}</section>
<section><h2>Record source</h2><p>{own_source}</p>
<p><a href="{pfam}.json" download>Download this family (JSON)</a></p></section>{GUIDE}"""
    return page_shell(f"{pfam}: {row['short_name'] or label}", body, context["provenance"], root="../")


def default_text_map(families: list[dict]) -> str:
    seed_statuses = sorted({r["unknown_status"] for r in families})
    curation_statuses = sorted({r["curation_status"] for r in families})
    cross_mech_bins = ["Cross-Mech linked", "DUFMech only"]
    s_idx = {v: i for i, v in enumerate(seed_statuses)}
    c_idx = {v: i for i, v in enumerate(curation_statuses)}
    points = []
    total = max(1, len(families))
    for idx, row in enumerate(families):
        angle = 2.0 * math.pi * idx / total
        radius = 0.25 + 0.7 * ((idx % 17) / 16.0)
        x = round(radius * math.cos(angle), 4)
        y = round(radius * math.sin(angle), 4)
        cm = row.get("cross_mech", {})
        has_cm = bool(cm.get("records_by_mech")) or bool(cm.get("protein_traits_record"))
        points.append([
            x, y, row["pfam_id"], row.get("short_name") or row["pfam_id"],
            row.get("name") or row.get("short_name") or row["pfam_id"],
            s_idx[row["unknown_status"]], c_idx[row["curation_status"]],
            0 if has_cm else 1,
            int(row.get("proteins") or 0), int(row.get("structures") or 0),
        ])
    return json_text({
        "model": "BAAI/bge-small-en-v1.5", "dim": 384, "method": "pacmap", "neighbors": 10,
        "n": len(points), "seed_statuses": seed_statuses, "curation_statuses": curation_statuses,
        "cross_mech_bins": cross_mech_bins, "points": points,
    })


def default_sequence_map(families: list[dict], protein_examples: list[dict] | None) -> str:
    fam_by_id = {r["pfam_id"]: r for r in families}
    seed_statuses = sorted({r["unknown_status"] for r in families})
    curation_statuses = sorted({r["curation_status"] for r in families})
    length_bins = ["<150 aa", "150–399 aa", "400–799 aa", "≥800 aa"]
    by_acc: dict[str, dict] = {}
    records_with_seq = set()
    mentions = 0
    for prow in protein_examples or []:
        pfam = prow["pfam_id"]
        fam = fam_by_id.get(pfam, {})
        seed = fam.get("unknown_status", "UNKNOWN_CANDIDATE")
        cur = fam.get("curation_status", "SNAPSHOT_ONLY")
        for ex in prow.get("examples", []):
            acc = ex["uniprot_accession"]
            records_with_seq.add(pfam)
            mentions += 1
            length = int(ex.get("sequence_length") or len(ex.get("sequence", "")))
            lbin = ("<150 aa" if length < 150 else "150–399 aa" if length < 400
                    else "400–799 aa" if length < 800 else "≥800 aa")
            entry = by_acc.setdefault(acc, {
                "id": f"UniProtKB:{acc}", "uniprot_accession": acc,
                "label": ex.get("protein_name") or acc,
                "organism": ex.get("organism") or "", "taxon_id": str(ex.get("taxon_id") or ""),
                "length": length, "length_bin": lbin, "truncated": length > 1022,
                "x": 0.0, "y": 0.0, "primary_seed_status": seed, "primary_curation_status": cur,
                "seed_statuses": [], "curation_statuses": [],
                "sequence_origin": ex.get("sequence_origin", "UNIPROT_FETCH"),
                "reviewed": bool(ex.get("reviewed", False)), "records": [],
            })
            if seed not in entry["seed_statuses"]:
                entry["seed_statuses"].append(seed)
            if cur not in entry["curation_statuses"]:
                entry["curation_statuses"].append(cur)
            entry["records"].append({
                "id": pfam, "short_name": fam.get("short_name") or pfam,
                "label": fam.get("name") or fam.get("short_name") or pfam,
                "seed_status": seed, "curation_status": cur, "page": f"families/{pfam}.html",
            })
    proteins = list(by_acc.values())
    total = max(1, len(proteins))
    for idx, p in enumerate(proteins):
        angle = 2.0 * math.pi * idx / total
        p["x"] = round(0.8 * math.cos(angle), 4)
        p["y"] = round(0.8 * math.sin(angle), 4)
    channels = sorted({p["sequence_origin"] for p in proteins}) or ["UNIPROT_FETCH"]
    return json_text({
        "model": "facebook/esm2_t33_650M_UR50D", "revision": "08e4846e5371", "dim": 1280,
        "pooling": "mean_excluding_bos_eos", "max_residues": 1022, "method": "PaCMAP",
        "neighbors": 10, "n_proteins": len(proteins), "n_records": len(records_with_seq),
        "n_mentions": mentions, "seed_statuses": seed_statuses,
        "curation_statuses": curation_statuses, "channels": channels,
        "length_bins": length_bins, "proteins": proteins,
    })


def map_data_table(prefix: str, label: str, columns: tuple[str, ...]) -> str:
    """An empty, labelled table that dashboard.js fills from the map's own JSON when opened."""
    head = "".join(f'<th scope="col">{text(column)}</th>' for column in columns)
    return (f'<details class="map-data" id="{prefix}"><summary>View data as table</summary>'
            f'<p id="{prefix}-count" role="status">Rows appear once the map data has loaded.</p>'
            f'<div class="table-wrap" tabindex="0" role="region" aria-label="{text(label)}">'
            f'<table><thead><tr>{head}</tr></thead><tbody></tbody></table></div>'
            f'<button id="{prefix}-more" type="button" hidden>Show more rows</button></details>')


def text_map_page(text_map: dict, provenance: dict) -> str:
    seed_opts = options({v: v.replace("_", " ") for v in text_map.get("seed_statuses", [])})
    cur_opts = options({v: v.replace("_", " ") for v in text_map.get("curation_statuses", [])})
    cm_opts = options({v: v for v in text_map.get("cross_mech_bins", [])})
    n_points = text_map.get("n", 0)
    model = text(text_map.get("model", "BAAI/bge-small-en-v1.5"))
    dim = text(text_map.get("dim", 384))
    body = f"""<h1>Text embedding map</h1>
<p class="lede">Interactive 2D PaCMAP projection of {n_points:,} DUF/Pfam family records embedded with
<code>{model}</code> ({dim}-dimensional text vectors over family accession, name, status, and frozen InterPro/Pfam descriptions).</p>
<p><a href="index.html#families">Catalogue table</a> | <a href="sequence-map.html">Sequence embedding map (ESM-2 pLM)</a> |
<a href="text-map.json" download>Download text map coordinates (JSON)</a></p>
<div class="browse-layout" data-text-map data-src="text-map.json">
<aside class="facet-sidebar" aria-label="Text map filters">
<form id="map-controls" class="controls" role="search">
<label>Search Pfam, DUF, or name <input id="map-search" type="search" name="q" placeholder="e.g. PF01951, DUF100, radical SAM…"></label>
<label>Color by <select id="map-color">
<option value="seed">Seed status</option>
<option value="curation">Curation status</option>
<option value="cross_mech">Cross-Mech linkage</option>
</select></label>
<label>Seed status <select id="map-seed"><option value="">All seed statuses</option>{seed_opts}</select></label>
<label>Curation status <select id="map-curation"><option value="">All curation statuses</option>{cur_opts}</select></label>
<label>Cross-Mech linkage <select id="map-cross-mech"><option value="">All records</option>{cm_opts}</select></label>
<button id="map-reset" type="button">Reset view and filters</button>
</form>
<div id="map-legend" class="map-legend" aria-label="Color legend"></div>
</aside>
<div class="browse-results map-panel">
<p id="map-status" role="status" aria-live="polite">Loading {n_points:,} family embeddings…</p>
<div class="map-canvas-wrap">
<canvas id="corpus-map" width="900" height="620" role="img" aria-label="2D PaCMAP scatter plot of DUFMech family text embeddings"></canvas>
</div>
<div id="map-selection" class="map-selection" aria-live="polite">
<p>Click or hover any point to inspect the Pfam/DUF family and open its detail page. Drag to pan; scroll or pinch to zoom.</p>
</div>
<noscript><p>This map needs JavaScript. The <a href="index.html#families">catalogue table</a> lists every family without it.</p></noscript>
{map_data_table("map-data", "Families plotted on the text map",
                ("Pfam", "Family", "Seed status", "Curation status", "Cross-Mech linkage"))}
</div></div>{GUIDE}"""
    return page_shell("Text embedding map", body, provenance)


def sequence_map_page(seq_map: dict, provenance: dict) -> str:
    seed_opts = options({v: v.replace("_", " ") for v in seq_map.get("seed_statuses", [])})
    cur_opts = options({v: v.replace("_", " ") for v in seq_map.get("curation_statuses", [])})
    chan_opts = options({v: v.replace("_", " ") for v in seq_map.get("channels", [])})
    len_opts = options({v: v for v in seq_map.get("length_bins", [])})
    n_proteins = seq_map.get("n_proteins", 0)
    n_records = seq_map.get("n_records", 0)
    model = text(seq_map.get("model", "facebook/esm2_t33_650M_UR50D"))
    dim = text(seq_map.get("dim", 1280))
    body = f"""<h1>Protein sequence embedding map (pLM)</h1>
<p class="lede">Interactive 2D PaCMAP projection of {n_proteins:,} verified UniProtKB protein sequence examples across {n_records:,} DUF/Pfam families,
embedded with protein language model <code>{model}</code> ({dim}-dimensional mean-pooled residue representations).</p>
<p><a href="index.html#families">Catalogue table</a> | <a href="map.html">Text embedding map</a> |
<a href="sequence-map.json" download>Download sequence map coordinates (JSON)</a></p>
<div class="browse-layout" data-sequence-map data-src="sequence-map.json">
<aside class="facet-sidebar" aria-label="Sequence map filters">
<form id="seq-controls" class="controls" role="search">
<label>Search UniProt, Pfam, protein, or organism <input id="seq-search" type="search" name="q" placeholder="e.g. P0A855, PF01951, Escherichia…"></label>
<label>Color by <select id="seq-color">
<option value="seed">Primary seed status</option>
<option value="curation">Primary curation status</option>
<option value="channel">Discovery channel</option>
<option value="length_bin">Sequence length</option>
</select></label>
<label>Seed status <select id="seq-seed"><option value="">All seed statuses</option>{seed_opts}</select></label>
<label>Curation status <select id="seq-curation"><option value="">All curation statuses</option>{cur_opts}</select></label>
<label>Discovery channel <select id="seq-channel"><option value="">All channels</option>{chan_opts}</select></label>
<label>Sequence length <select id="seq-length"><option value="">All lengths</option>{len_opts}</select></label>
<button id="seq-reset" type="button">Reset view and filters</button>
</form>
<div id="seq-legend" class="map-legend" aria-label="Color legend"></div>
</aside>
<div class="browse-results map-panel">
<p id="seq-status" role="status" aria-live="polite">Loading {n_proteins:,} protein sequence embeddings…</p>
<div class="map-canvas-wrap">
<canvas id="seq-canvas" width="900" height="620" role="img" aria-label="2D PaCMAP scatter plot of ESM-2 protein sequence embeddings"></canvas>
</div>
<div id="seq-selection" class="map-selection" aria-live="polite">
<p>Click or hover any protein point to inspect its UniProtKB accession, organism, length, and linked DUF/Pfam families.</p>
</div>
<noscript><p>This map needs JavaScript. Each family page, reached from the <a href="index.html#families">catalogue table</a>, lists its protein sequence examples without it.</p></noscript>
{map_data_table("seq-data", "Proteins plotted on the sequence map",
                ("UniProt", "Protein", "Organism", "Length", "DUF/Pfam families"))}
</div></div>{GUIDE}"""
    return page_shell("Sequence map (pLM)", body, provenance)


def not_found_page(families: list[dict], provenance: dict, assets: dict[str, str]) -> str:
    """GitHub Pages serves 404.html for every missing path, at that path's depth.

    A relative reference would resolve against the mistyped URL, so every link is
    absolute and the stylesheet and theme script are inlined rather than fetched.
    """
    body = ('<h1>Page not found</h1><p class="lede">No DUFMech page exists at this address.</p>'
            '<p>Family pages are named by Pfam accession, as <code>families/PF00001.html</code>; '
            'a family outside the current worklist snapshot has no page.</p>'
            f'<form class="hero-search" action="{SITE_URL}index.html#families" method="get" role="search">'
            f'<label for="not-found-query">Search the DUFMech catalogue ({len(families):,} families)</label>'
            '<div class="hero-search-row"><input id="not-found-query" type="search" name="q" '
            'placeholder="Pfam accession, DUF name, InterPro ID or family name">'
            '<button type="submit">Search families</button></div></form>'
            f'<ul><li><a href="{SITE_URL}index.html#families">Browse all families</a></li>'
            f'<li><a href="{SITE_URL}categories.html">Seed categories</a></li>'
            f'<li><a href="{SITE_URL}map.html">Text embedding map</a></li>'
            f'<li><a href="{SITE_URL}sources.html">Sources and schema</a></li></ul>')
    inline = f'<script>{assets["theme.js"]}</script><style>{assets["style.css"]}</style>'
    return page_shell("Page not found", body, provenance, root=SITE_URL, assets=inline)


def render_artifacts(
    families: list[dict], report: dict, *, input_ids: dict, cross_rows: list[dict],
    cross_sources: dict, family_metadata: dict | None = None, member_rows: list[dict] | None = None,
    protein_examples: list[dict] | None = None,
    provenance: dict | None = None,
    text_map_json: str | None = None,
    sequence_map_json: str | None = None,
) -> dict[str, str]:
    """Return the complete output tree, without I/O, network access or wall-clock data.

    ``family_metadata`` is keyed by Pfam accession. Entries may supply curation_status,
    source {repository, commit, path}, interpro_label, evidence, publications (PUB ->
    explicit reference), history, and reviews. Provenance may supply worklist/source
    objects and schema {url, label}; absent material is explicitly reported as absent.
    """
    metadata = family_metadata or {}
    if protein_examples is not None:
        from dufmech.protein_examples import validate_rows

        validate_rows(protein_examples, families)
    extra = metadata.keys() - {row["pfam_id"] for row in families}
    if extra:
        raise ReportError(f"metadata families absent from worklist: {', '.join(sorted(extra))}")
    for row in families:
        row["curation_status"] = metadata.get(row["pfam_id"], {}).get("curation_status", "SNAPSHOT_ONLY")
    assets = {"style.css": Path(__file__).with_name("site.css").read_text(),
              "dashboard.js": Path(__file__).with_name("dashboard.js").read_text(),
              "theme.js": Path(__file__).with_name("site_theme.js").read_text()}
    provenance = {**(provenance or {}), "inputs": dict(sorted(input_ids.items()))}
    provenance["renderer_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    fingerprint = json_text([families, metadata, member_rows, protein_examples,
                             cross_rows, cross_sources, provenance, assets])
    provenance["build_id"] = hashlib.sha256(fingerprint.encode()).hexdigest()[:16]
    cross: dict[str, list[dict]] = defaultdict(list)
    for row in cross_rows:
        cross[row.get("pfam_id", "")].append(row)
    context = {"provenance": provenance, "cross": cross, "cross_sources": cross_sources,
               "protein_examples": {r["pfam_id"]: r for r in protein_examples or []},
               "labels": {r["pfam_id"]: r["name"] or r["short_name"] for r in families},
               "members": group_members(member_rows or [], {r["pfam_id"] for r in families})}
    artifacts = {".nojekyll": "", **assets}
    payload = {"inputs": provenance["inputs"], "provenance": provenance, "summary": report,
               "families": families, "metadata": metadata}
    artifacts["index.json"] = json_text(payload)
    # Search omits long source descriptions and per-record references. Those stay on detail pages.
    fields = ["pfam_id", "short_name", "name", "interpro_id", "unknown_status",
              "characterization_status", "proteins", "structures", "alphafold_models",
              "known_evidence_count", "partial_evidence_count", "context_evidence_count",
              "curation_status", "cross_mech"]
    artifacts["catalogue.json"] = json_text({"version": 1, "fields": fields,
                                            "rows": [[row[k] for k in fields] for row in families]})
    text_map_obj = json.loads(text_map_json or default_text_map(families))
    seq_map_obj = json.loads(sequence_map_json or default_sequence_map(families, protein_examples))
    artifacts["text-map.json"] = json_text(text_map_obj)
    artifacts["sequence-map.json"] = json_text(seq_map_obj)
    artifacts["map.html"] = text_map_page(text_map_obj, provenance)
    artifacts["sequence-map.html"] = sequence_map_page(seq_map_obj, provenance)
    categories = Counter(r["unknown_status"] for r in families)
    category_links = "".join(f'<li><a href="category/{status.lower()}.html">{human(status)}</a>: {n:,}</li>'
                             for status, n in sorted(categories.items()))
    metrics = report["families"]
    metric_labels = {"total": "Families", "with_interpro_id": "Families with InterPro IDs",
                     "with_structures": "Families with structures",
                     "with_alphafold_models": "Families with AlphaFold models",
                     "interpro_proteins": "Per-family protein total", "interpro_matches": "Per-family match total"}
    metric_html = '<section class="metrics" aria-label="Corpus metrics">' + "".join(
        f'<div class="metric"><strong>{metrics[key]:,}</strong><span>{label}</span></div>'
        for key, label in metric_labels.items()) + "</section>"
    curated = [r for r in cross_rows if r["source_mech"] != "ProteinTraitsMech"]
    examples = ('<section><details><summary>DUF examples curated in other Mechs</summary>'
                '<p>Family mentions and protein associations are contextual links, not functional validation.</p>'
                f'{cross_table(curated[:20], cross_sources)}'
                '<p><a href="cross-mech.html">All frozen cross-Mech examples</a></p></details></section>')
    hero_search = (
        '<form class="hero-search" id="hero-search-form" action="#families" method="get" role="search">'
        f'<label for="hero-search-input">Search the DUFMech catalogue ({len(families):,} families)</label>'
        '<div class="hero-search-row">'
        '<input id="hero-search-input" type="search" name="q" '
        'placeholder="Search by Pfam accession (PF00001), DUF short name (DUF1), InterPro ID, or family name…">'
        '<button type="submit">Search families</button></div>'
        '<p class="hero-search-links">Or explore visually: '
        '<a href="map.html">Text embedding map</a> · '
        '<a href="sequence-map.html">Protein sequence map (ESM-2 pLM)</a> · '
        '<a href="categories.html">Seed categories</a></p></form>'
    )
    intro = ('<h1>DUFMech</h1><p class="lede">Domain and protein families of unknown function, '
             'including historical DUFs.</p>' + hero_search + metric_html + examples
             + '<p>Per-family totals are sums of reported InterPro counters, not unique proteins or matches. '
             f'{metrics["missing_protein_counts"]:,} families lack protein counts; '
             f'{metrics["missing_match_counts"]:,} lack match counts.</p>'
             + '<p><a href="categories.html">Browse by seed category</a></p>'
             + f'<ul class="category-list">{category_links}</ul>')
    if context["members"]:
        domain_links = "".join(
            f'<li><a href="families/{pfam}.html#domain-matches">{pfam}: '
            f'{text(context["labels"][pfam])}</a> ({len(rows):,} supplied protein members)</li>'
            for pfam, rows in sorted(context["members"].items())
        )
        intro += '<section><h2>Residue-level domain matches</h2><ul>' + domain_links + '</ul></section>'
    total_pages = max(1, math.ceil(len(families) / PAGE_SIZE))
    paths = ["index.html"] + [f"browse/{i + 1}.html" for i in range(1, total_pages)]
    for page, path in enumerate(paths):
        root = "" if page == 0 else "../"
        body = intro if page == 0 else "<h1>DUFMech families</h1>"
        body += listing(families, families, root=root, page=page, page_paths=paths)
        body += corpus_visual(families) if page == 0 else ""
        body += GUIDE
        artifacts[path] = page_shell("Family catalogue", body, provenance, root=root)
    artifacts["categories.html"] = page_shell("Categories", '<h1>Family categories</h1><ul>'
                                             + category_links + "</ul>" + GUIDE, provenance)
    for status in sorted(categories):
        rows = [r for r in families if r["unknown_status"] == status]
        slug = status.lower()
        if not re.fullmatch(r"[a-z_]+", slug):
            raise ReportError("invalid category name")
        pages = max(1, math.ceil(len(rows) / PAGE_SIZE))
        paths = [f"category/{slug}.html"] + [f"category/{slug}-{i + 1}.html" for i in range(1, pages)]
        for page, path in enumerate(paths):
            body = f'<h1>{human(status)}</h1><p><a href="../categories.html">All categories</a></p>'
            body += listing(rows, families, root="../", page=page, page_paths=paths, category=status)
            artifacts[path] = page_shell(status.replace("_", " "), body, provenance, root="../")
    artifacts["cross-mech.html"] = page_shell("Cross-Mech examples", '<h1>Cross-Mech examples</h1>'
        '<p>Records outside ProteinTraitsMech. ProteinTraitsMech links appear on each family page.</p>'
        + cross_table(curated, cross_sources), provenance)
    artifacts["404.html"] = not_found_page(families, provenance, assets)
    for row in families:
        pfam = row["pfam_id"]
        artifacts[f"families/{pfam}.html"] = record_page(row, metadata.get(pfam, {}), context)
        artifacts[f"families/{pfam}.json"] = json_text({"family": row, "metadata": metadata.get(pfam, {}),
                                                       "inputs": provenance["inputs"],
                                                       "members": context["members"].get(pfam, []),
                                                       "protein_examples": context["protein_examples"].get(pfam),
                                                       "cross_mech": cross.get(pfam, [])})
        examples = context["protein_examples"].get(pfam, {}).get("examples", [])
        if examples:
            fasta = []
            for example in examples:
                fasta.append(f'>{example["uniprot_accession"]} {pfam} '
                             f'UniProt={example["uniprot_release"]} '
                             f'sequence_version={example["sequence_version"]}')
                sequence = example["sequence"]
                fasta.extend(sequence[i:i + 70] for i in range(0, len(sequence), 70))
            artifacts[f"families/{pfam}.fasta"] = "\n".join(fasta) + "\n"
    schema = provenance.get("schema", {})
    if schema.get("document"):
        schema_html = '<a href="schema.html">LinkML family schema documentation</a>'
        document = schema["document"]
        classes = []
        for name, definition in document.get("classes", {}).items():
            rows = "".join(f'<tr><th scope="row">{text(key)}</th>'
                           f'<td>{text(value.get("range", document.get("default_range", "string")))}</td>'
                           f'<td>{"Required" if value.get("required") else "Optional"}</td>'
                           f'<td>{text(value.get("description", ""))} '
                           f'<code>{text(value.get("pattern", ""))}</code></td></tr>'
                           for key, value in definition.get("attributes", {}).items())
            classes.append(f'<section><h2>{text(name)}</h2><p>{text(definition.get("description", ""))}</p>'
                           '<div class="table-wrap" tabindex="0" role="region" aria-label="Schema fields">'
                           '<table><thead><tr><th>Field</th><th>Range</th><th>Cardinality</th><th>Description</th>'
                           f'</tr></thead><tbody>{rows}</tbody></table></div></section>')
        enums = "".join(f'<dt>{text(name)}</dt><dd>{text(", ".join(value["permissible_values"]))}</dd>'
                        for name, value in document.get("enums", {}).items())
        artifacts["schema.html"] = page_shell("LinkML schema", '<h1>DUFMech LinkML schema</h1>'
            '<p><a href="schema/dufmech.yaml" download>Download LinkML schema</a></p>'
            + "".join(classes) + f"<h2>Enumerations</h2><dl>{enums}</dl>", provenance)
    else:
        schema_html = (link(schema.get("url", ""), schema.get("label", "LinkML family schema"))
                       if schema else "No LinkML schema documentation supplied for this snapshot-only build.")
    source_items = "".join(f'<li>{text(key)}: {link(source_link(source.get("repository", REPOSITORY), source.get("commit", ""), source.get("path", "")), source.get("path", ""))}</li>'
                           for key, source in sorted(provenance.items())
                           if isinstance(source, dict) and source.get("path"))
    review_items = "".join(f'<li>{artifact_link(ref, ref["label"], "")}'
                           f'<p>Scope: {text(ref["scope"])}. '
                           f'Scientific review: {text(ref["scientific_review"])}.</p></li>'
                           for ref in provenance.get("retained_reviews", []))
    artifacts["sources.html"] = page_shell("Sources and schema", f"""<h1>Sources and schema</h1>
<p><a href="index.json" download>Complete family index, metadata and provenance (JSON)</a></p>
<h2>Frozen inputs</h2><ul>{source_items}</ul>
{member_dataset(provenance)}
{protein_example_dataset(provenance)}
<p>Site build {provenance['build_id']}. Source links are pinned to the supplied or verified source commits.
Input snapshot identifiers are listed in the footer. No live scientific data is fetched by these pages.</p>
<h2>Retained reviews</h2>{f'<ul>{review_items}</ul>' if review_items else '<p>No retained reviews supplied.</p>'}
<h2>Record schema</h2><p>{schema_html}</p>{GUIDE}""", provenance)
    return artifacts
