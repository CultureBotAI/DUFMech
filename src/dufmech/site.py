"""Deterministic, progressively enhanced family and catalogue pages."""

from __future__ import annotations

import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from html import escape
from pathlib import Path
from typing import Any

from dufmech.report import ReportError
from dufmech.site_data import (
    IPR_RE,
    description_html,
    group_members,
    link,
    pfam_url,
    reference_url,
    source_link,
)
from dufmech.site_sources import REPOSITORY

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
members but is naming history, not proof of function for every member.
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
            f'<blockquote>{text(ref["snippet"])}</blockquote><p>{text(ref["explanation"])}</p></li>'
            for ref in assertion.get("evidence", [])
        )
        assertions.append(f'<h3>{text(assertion["assertion_id"])}</h3>'
                          f'<p>{text(assertion["statement"])}</p>'
                          f'<p>Scope: {text(assertion["scope"])}. '
                          f'Evidence kind: {human(assertion["evidence_kind"])}.</p><ul>{evidence}</ul>')
    return "".join(assertions) or "<p>No curated functional assertions supplied.</p>"


def structured_content(value: Any) -> str:
    """Keep optional governed curation fields visible without inventing their semantics."""
    if isinstance(value, dict):
        return "<dl>" + "".join(f"<dt>{human(key)}</dt><dd>{structured_content(item)}</dd>"
                                for key, item in value.items()) + "</dl>"
    if isinstance(value, list):
        return "<ul>" + "".join(f"<li>{structured_content(item)}</li>" for item in value) + "</ul>"
    return link(reference_url({"reference": str(value)}), str(value))


def page_shell(title: str, body: str, provenance: dict, *, root: str = "") -> str:
    source = provenance.get("worklist", {})
    pinned = source_link(source.get("repository", REPOSITORY), source.get("commit", ""),
                         source.get("path", ""))
    version = link(pinned, f"Corpus source {source.get('commit', '')[:12]}") if pinned else ""
    inputs = " / ".join(f"{text(k)}: {text(v)}" for k, v in provenance["inputs"].items())
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{text(title)} | DUFMech</title><link rel="icon" href="data:,">
<script src="{root}theme.js"></script><link rel="stylesheet" href="{root}style.css">
<script src="{root}dashboard.js" defer></script></head><body>
<a class="skip-link" href="#main">Skip to content</a><header>
<a class="brand" href="{root}index.html">DUFMech</a>
<nav aria-label="Project navigation"><a href="{root}index.html#families">Browse families</a>
<a href="{root}categories.html">Categories</a><a href="{root}sources.html">Sources &amp; schema</a>
<a href="{REPOSITORY}">Repository</a>
<a href="https://culturebotai.github.io/mechs/">All Mech projects</a></nav>
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
    static_links = "".join(
        f'<a href="{root}{path}" aria-label="Catalogue page {i + 1}"'
        f'{" aria-current=page" if i == page else ""}>{i + 1}</a>'
        for i, path in enumerate(page_paths)
    )
    return f"""<section id="families" class="section" data-catalogue data-root="{root}"
data-category="{text(category)}" data-page="{page + 1}">
<h2>Families</h2><p><a href="{root}index.json" download>Download the complete family index (JSON)</a></p>
<form id="family-controls" class="controls" role="search" hidden>
<label>Search accession or family <input id="family-query" type="search" name="q"></label>
<label>Seed status <select id="seed-filter"><option value="">All seed statuses</option>
{options(statuses)}</select></label>
<label>Characterization <select id="characterization-filter"><option value="">All characterizations</option>
{options(characterizations)}</select></label>
<label>Sort by <select id="family-sort">{options(SORTS)}</select></label>
<button id="reset-families" type="button">Clear search and filters</button></form>
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
</section>"""


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
    protein = link(f"https://rest.uniprot.org/uniprotkb/{accession}", accession) if accession else ""
    return (f'<tr><td>{family}</td><td>{text(row["source_mech"])}</td><td>{record}</td>'
            f'<td>{protein}<br>{text(row.get("protein_label", ""))}</td>'
            f'<td>{human(", ".join(row.get("link_basis", [])))}</td></tr>')


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
                    f' {text(ref.get("description", ""))}</li>')
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
                      f'{text(event.get("summary", event.get("description", "")))}'
                      f' {artifact_link(event, event.get("source_path", "History artifact"))}'
                      f'<p>{text(event.get("description", ""))} {text(event.get("outcome", ""))}</p></li>')
    history = "<ol>" + "".join(events) + "</ol>" if events else "<p>No retained curation events supplied.</p>"
    reviews = "".join(f'<li>{artifact_link(ref, ref.get("label", "Retained review"))}'
                      f'<p>Scope: {text(ref.get("scope", "Not supplied"))}. '
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
<section id="domain-matches"><h2>Domain matches</h2>{domain_visual(context['members'].get(pfam, []), dataset=bool(context['provenance'].get('members')))}</section>
<section><h2>Snapshot counters</h2><dl class="record-facts">{counters}</dl></section>
<section><h2>Classification basis</h2><p>{human(seed_reasons) or 'No seed reasons supplied.'}</p>
<p>{human('; '.join(row['demotion_reasons'])) or 'No scoring reasons supplied.'}</p></section>
<section><h2>Related Mech records</h2>
{cross_table(context['cross'].get(pfam, []), context['cross_sources'], '../')}</section>
{related}
<section><h2>Curation history and reviews</h2>{history}</section>
<section><h2>Record source</h2><p>{own_source}</p>
<p><a href="{pfam}.json" download>Download this family (JSON)</a></p></section>{GUIDE}"""
    return page_shell(f"{pfam}: {row['short_name'] or label}", body, context["provenance"], root="../")


def render_artifacts(
    families: list[dict], report: dict, *, input_ids: dict, cross_rows: list[dict],
    cross_sources: dict, family_metadata: dict | None = None, member_rows: list[dict] | None = None,
    provenance: dict | None = None,
) -> dict[str, str]:
    """Return the complete output tree, without I/O, network access or wall-clock data.

    ``family_metadata`` is keyed by Pfam accession. Entries may supply curation_status,
    source {repository, commit, path}, interpro_label, evidence, publications (PUB ->
    explicit reference), history, and reviews. Provenance may supply worklist/source
    objects and schema {url, label}; absent material is explicitly reported as absent.
    """
    metadata = family_metadata or {}
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
    fingerprint = json_text([families, metadata, member_rows, cross_rows, cross_sources, provenance, assets])
    provenance["build_id"] = hashlib.sha256(fingerprint.encode()).hexdigest()[:16]
    cross: dict[str, list[dict]] = defaultdict(list)
    for row in cross_rows:
        cross[row.get("pfam_id", "")].append(row)
    context = {"provenance": provenance, "cross": cross, "cross_sources": cross_sources,
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
    intro = ('<h1>DUFMech</h1><p class="lede">Domain and protein families of unknown function, '
             'including historical DUFs.</p>' + metric_html + examples
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
    for row in families:
        pfam = row["pfam_id"]
        artifacts[f"families/{pfam}.html"] = record_page(row, metadata.get(pfam, {}), context)
        artifacts[f"families/{pfam}.json"] = json_text({"family": row, "metadata": metadata.get(pfam, {}),
                                                       "inputs": provenance["inputs"],
                                                       "members": context["members"].get(pfam, []),
                                                       "cross_mech": cross.get(pfam, [])})
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
<p>Site build {provenance['build_id']}. Source links are pinned to the supplied or verified source commits.
Input snapshot identifiers are listed in the footer. No live scientific data is fetched by these pages.</p>
<h2>Retained reviews</h2>{f'<ul>{review_items}</ul>' if review_items else '<p>No retained reviews supplied.</p>'}
<h2>Record schema</h2><p>{schema_html}</p>{GUIDE}""", provenance)
    return artifacts
