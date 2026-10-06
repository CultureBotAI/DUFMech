"""Render a deterministic static dashboard for DUF/PUF snapshots."""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from html import escape
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from dufmech.cross_mech import PROTEIN_TRAITS_MECH
from dufmech.cross_mech_snapshot import CROSS_MECH_DIR, CROSS_MECH_STEM, load_cross_mech_snapshot
from dufmech.report import (
    ReportError,
    build_report,
    family_index,
    latest_snapshot_path,
    load_latest_rows,
)

PAGES_DIR = Path("pages")
WORKLISTS_DIR = Path("data/worklists")
REPO_ROOT = Path(__file__).resolve().parents[2]


def validate_output_directory(out_dir: Path) -> None:
    """Reject repository roots, ancestors, and symlink destinations before writing."""

    target = out_dir.absolute()
    if target.is_symlink():
        raise ReportError(f"output directory must not be a symlink: {out_dir}")
    resolved = target.resolve()
    for protected in (REPO_ROOT, Path.cwd().resolve(), Path.home().resolve()):
        if resolved == protected or resolved in protected.parents:
            raise ReportError(f"refusing to render into protected directory: {out_dir}")
    if target.exists() and not target.is_dir():
        raise ReportError(f"output is not a directory: {out_dir}")


STYLE_CSS = """
:root {
  color-scheme: light dark;
  --bg: #f7f8fa;
  --panel: #ffffff;
  --text: #20242c;
  --muted: #667085;
  --line: #d9dee7;
  --accent: #166534;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #161616;
    --panel: #242424;
    --text: #f9fafb;
    --muted: #cbd5e1;
    --line: #424242;
    --accent: #86efac;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.5;
}
main {
  max-width: 1280px;
  margin: 0 auto;
  padding: 32px 20px 48px;
}
a { color: var(--accent); }
.lede {
  max-width: 820px;
  color: var(--muted);
  overflow-wrap: anywhere;
}
.metrics {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 190px), 1fr));
  gap: 12px;
  margin: 28px 0;
}
.metric {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
}
.metric {
  padding: 14px 16px;
}
.metric strong {
  display: block;
  font-size: 1.5rem;
  line-height: 1;
}
.metric span,
th {
  color: var(--muted);
  font-size: 0.86rem;
  font-weight: 600;
  text-transform: uppercase;
}
.section {
  margin-top: 18px;
}
.section h2 {
  margin: 0;
  padding: 14px 0;
  border-bottom: 1px solid var(--line);
  font-size: 1rem;
}
.table-wrap { overflow: auto; max-height: 65vh; border: 1px solid var(--line); }
table {
  width: 100%;
  min-width: 1100px;
  border-collapse: collapse;
}
th,
td {
  padding: 10px 12px;
  border-top: 1px solid var(--line);
  text-align: left;
  vertical-align: top;
}
th {
  border-top: 0;
  position: sticky;
  top: 0;
  background: var(--panel);
  z-index: 1;
}
nav, .controls, .pagination { display: flex; flex-wrap: wrap; gap: 12px; align-items: end; }
.controls { margin: 16px 0; }
label { display: grid; gap: 4px; }
input, select, button { font: inherit; color: var(--text); background: var(--panel); border: 1px solid var(--muted); border-radius: 4px; padding: 6px 10px; max-width: 100%; }
button { cursor: pointer; }
button:disabled { opacity: .55; cursor: default; }
.pagination { margin-top: 12px; }
[hidden] { display: none !important; }
tr:target { outline: 2px solid var(--accent); outline-offset: -2px; }
.row-link { display: block; font-size: .85rem; }
.legend dt { font-weight: 600; }
.legend dd { margin: 0 0 10px; max-width: 850px; }
footer { border-top: 1px solid var(--line); margin-top: 28px; padding-top: 16px; }
:focus-visible { outline: 3px solid var(--accent); outline-offset: 2px; }
td.num {
  font-variant-numeric: tabular-nums;
  text-align: right;
  white-space: nowrap;
}
.status {
  overflow-wrap: anywhere;
  min-width: 140px;
  max-width: 200px;
}
@media (max-width: 720px) {
  main { padding: 20px 12px 32px; }
  .metrics { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .metric { padding: 12px; }
  .metric strong { font-size: 1.25rem; }
}
""".strip()


def render_site(
    worklist_rows: list[dict[str, Any]],
    score_rows: list[dict[str, Any]],
    *,
    input_ids: dict[str, str],
    out_dir: Path,
    cross_mech_rows: list[dict[str, Any]] | None = None,
    cross_mech_sources: dict[str, Any] | None = None,
) -> None:
    """Render a static DUFMech dashboard into ``out_dir``."""

    families = family_index(worklist_rows, score_rows)
    report = build_report(worklist_rows, score_rows, top_n=20)
    cross_mech_rows = cross_mech_rows or []
    report["cross_mech"] = _attach_cross_mech(families, cross_mech_rows)

    artifacts = {
        ".nojekyll": "",
        "style.css": STYLE_CSS + "\n",
        "dashboard.js": Path(__file__).with_name("dashboard.js").read_text(encoding="utf-8"),
        "index.html": _index_html(
            report, families, input_ids, cross_mech_rows, cross_mech_sources or {}
        ),
        "index.json": json.dumps(
            {
                "inputs": dict(sorted(input_ids.items())),
                "summary": report,
                "families": families,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
    }
    validate_output_directory(out_dir)
    for name in artifacts:
        target = out_dir / name
        if target.is_symlink() or (target.exists() and not target.is_file()):
            raise ReportError(f"generated output is not a regular file: {target}")
    out_dir.mkdir(parents=True, exist_ok=True)
    # Stage every artifact before replacing generated files; never remove the output tree.
    with tempfile.TemporaryDirectory(dir=out_dir) as tmp:
        for name, content in artifacts.items():
            (Path(tmp) / name).write_text(content, encoding="utf-8")
        for name in artifacts:
            os.replace(Path(tmp) / name, out_dir / name)


def render_from_paths(
    *,
    out_dir: Path,
    worklists_dir: Path = WORKLISTS_DIR,
    worklist_json: Path | None = None,
    score_json: Path | None = None,
    cross_mech_dir: Path = CROSS_MECH_DIR,
) -> None:
    """Load frozen snapshots and render pages."""

    for input_path in (worklists_dir, worklist_json, score_json, cross_mech_dir):
        if input_path is not None:
            source = input_path.resolve()
            target = out_dir.resolve()
            if source == target or target in source.parents or source in target.parents:
                raise ReportError(f"output directory overlaps snapshot inputs: {out_dir}")
    worklist_rows, score_rows, input_ids = load_latest_rows(
        worklists_dir,
        worklist_json=worklist_json,
        score_json=score_json,
    )
    cross_mech_rows: list[dict[str, Any]] = []
    cross_mech_sources: dict[str, Any] = {}
    cross_mech_path = (
        latest_snapshot_path(cross_mech_dir, CROSS_MECH_STEM, required=False)
        if cross_mech_dir.is_dir()
        else None
    )
    if cross_mech_path is not None:
        cross_mech_rows, manifest = load_cross_mech_snapshot(
            cross_mech_path, worklist_rows=worklist_rows, worklist_snapshot_id=input_ids["worklist"]
        )
        input_ids["cross_mech"] = cross_mech_path.stem
        cross_mech_sources = dict(manifest["source"].get("mechs", {}))
    render_site(
        [dict(row) for row in worklist_rows],
        [dict(row) for row in score_rows],
        input_ids=input_ids,
        out_dir=out_dir,
        cross_mech_rows=cross_mech_rows,
        cross_mech_sources=cross_mech_sources,
    )


def diff_trees(expected: Path, actual: Path) -> list[str]:
    """Return deterministic relative paths that differ between two trees."""

    if actual.is_symlink() or not actual.is_dir():
        return ["."]
    left = {path.relative_to(expected): path for path in expected.rglob("*")}
    right = {path.relative_to(actual): path for path in actual.rglob("*")}
    diffs: list[str] = []
    for name in sorted(left.keys() | right.keys()):
        a, b = left.get(name), right.get(name)
        if a is None or b is None or a.is_symlink() or b.is_symlink():
            diffs.append(name.as_posix())
        elif a.is_dir() and b.is_dir():
            continue
        elif not a.is_file() or not b.is_file() or a.read_bytes() != b.read_bytes():
            diffs.append(name.as_posix())
    return diffs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Render the DUFMech static dashboard from frozen snapshots."
    )
    parser.add_argument("--out", type=Path, default=PAGES_DIR)
    parser.add_argument("--worklists-dir", type=Path, default=WORKLISTS_DIR)
    parser.add_argument("--worklist-json", type=Path)
    parser.add_argument("--score-json", type=Path)
    parser.add_argument(
        "--check",
        action="store_true",
        help="render to a temp dir and fail if --out is stale",
    )
    args = parser.parse_args(argv)

    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            render_from_paths(
                out_dir=Path(tmp),
                worklists_dir=args.worklists_dir,
                worklist_json=args.worklist_json,
                score_json=args.score_json,
            )
            if not args.out.exists():
                parser.exit(1, f"{args.out} does not exist; run `just render`\n")
            diffs = diff_trees(Path(tmp), args.out)
        if diffs:
            parser.exit(
                1,
                (
                    f"{args.out} is stale ({len(diffs)} file(s) differ), "
                    f"including {', '.join(diffs[:5])}; run `just render`\n"
                ),
            )
        print(f"{args.out} is current")
        return 0

    render_from_paths(
        out_dir=args.out,
        worklists_dir=args.worklists_dir,
        worklist_json=args.worklist_json,
        score_json=args.score_json,
    )
    print(f"rendered DUFMech site under {args.out}")
    return 0


def _index_html(
    report: dict[str, Any],
    families: list[dict[str, Any]],
    input_ids: dict[str, str],
    cross_mech_rows: list[dict[str, Any]],
    cross_mech_sources: dict[str, Any],
) -> str:
    metrics = report["families"]
    cross = report["cross_mech"]
    rows = "\n".join(_family_row(row) for row in families)
    curated = [row for row in cross_mech_rows if row["source_mech"] != PROTEIN_TRAITS_MECH]
    curated_rows = "\n".join(_cross_mech_row(row, cross_mech_sources) for row in curated)
    inputs = " / ".join(
        f"{escape(key)}: {escape(value)}"
        for key, value in sorted(input_ids.items())
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>DUFMech</title>
  <link rel="icon" href="data:,">
  <link rel="stylesheet" href="style.css">
  <script src="dashboard.js" defer></script>
</head>
<body>
  <main>
    <nav aria-label="Project navigation"><a href="#families">Browse families</a>
      <a href="https://github.com/CultureBotAI/DUFMech">Repository</a>
      <a href="https://culturebotai.github.io/mechs/">All Mech projects</a></nav>
    <h1>DUFMech</h1>
    <p class="lede">
      Domain and protein families of unknown function, including historical DUFs.
    </p>
    <p class="lede">{inputs}</p>

    <section class="metrics" aria-label="Corpus metrics">
      {_metric("Families", metrics["total"])}
      {_metric("Families with InterPro IDs", metrics["with_interpro_id"])}
      {_metric("Families with structures", metrics["with_structures"])}
      {_metric("Families with AlphaFold models", metrics["with_alphafold_models"])}
      {_metric("Per-family protein total", metrics["interpro_proteins"])}
      {_metric("Per-family match total", metrics["interpro_matches"])}
      {_metric("Families with examples or mentions in other Mechs", cross["families"])}
      {_metric("DUF example proteins in other Mechs", cross["proteins"])}
    </section>
    <p class="lede">Per-family totals are sums of reported InterPro counters,
      not unique proteins or matches. Missing counts are excluded:
      {metrics["missing_protein_counts"]:,} families lack protein counts and
      {metrics["missing_match_counts"]:,} lack match counts.</p>

    <section class="section">
      <h2>DUF examples curated in other Mechs</h2>
      <p class="lede">Records outside ProteinTraitsMech that name a DUF/PUF family or
        cite a protein whose UniProtKB entry carries one. ProteinTraitsMech trait and
        canonical-example links appear per family below. Counts represent distinct
        records with examples or mentions; trait-record availability is shown separately.
        Names marked "not in worklist" are DUF names that no longer match a current Pfam
        short name, or UniProt UPF names, which the Pfam worklist never carries.</p>
      <div class="table-wrap" tabindex="0" role="region" aria-label="Cross-Mech examples; scroll to read all columns">
        <table>
          <thead>
            <tr>
              <th>Family</th>
              <th>Mech</th>
              <th>Record</th>
              <th>Protein</th>
              <th>Link basis</th>
            </tr>
          </thead>
          <tbody>
            {curated_rows}
          </tbody>
        </table>
      </div>
    </section>

    <section class="section">
      <h2 id="families">Families</h2>
      <p><a href="index.json" download>Download the complete family index (JSON)</a>
        — all {len(families):,} families, source snapshot IDs, summary and evidence counts.</p>
      <div class="controls" id="family-controls" hidden>
        <label>Search accession or family <input id="family-query" type="search"></label>
        <label>Seed status <select id="seed-filter"><option value="">All seed statuses</option></select></label>
        <button id="reset-families" type="button">Clear search and filters</button>
      </div>
      <p id="family-count" role="status" aria-live="polite">{len(families):,} families.</p>
      <noscript><p>Search and paging require JavaScript. All families remain available in the
        scrollable table and complete JSON download.</p></noscript>
      <div class="table-wrap" tabindex="0" role="region" aria-label="Family worklist; scroll to read all columns">
        <table id="family-table">
          <thead>
            <tr>
              <th>Pfam</th>
              <th>Family</th>
              <th>Seed status</th>
              <th>Characterization</th>
              <th>Evidence counts</th>
              <th class="num">Proteins</th>
              <th class="num">Structures</th>
              <th class="num">AlphaFold</th>
              <th>Other Mechs</th>
            </tr>
          </thead>
          <tbody>
            {rows}
          </tbody>
        </table>
      </div>
      <div class="pagination" id="family-pagination" hidden>
        <button id="previous-families" type="button">Previous page</button>
        <span id="family-page"></span>
        <button id="next-families" type="button">Next page</button>
      </div>
    </section>
    <section class="section legend" aria-labelledby="status-guide">
      <h2 id="status-guide">How to read this worklist</h2>
      <dl>
        <dt>Seed status</dt><dd>A name-based classification of the frozen InterPro/Pfam metadata.
          UNKNOWN CANDIDATE means the name or description explicitly says the function is unknown.
          KNOWN HISTORICAL DUF means a DUF name matched without that unknown-function wording;
          this heuristic is not proof of a known function and does not establish experimental
          characterization. FALSE POSITIVE TEXT HIT means
          the metadata did not meet the DUF or unknown-function naming rules.</dd>
        <dt>Characterization</dt><dd>A separate evidence-scoring result, when a matching score
          snapshot is available. UNSCORED means no score has been calculated for this family;
          it is not evidence that the family lacks a known function.
          Missing scores are not negative evidence. A scored UNKNOWN CANDIDATE has no counted
          known or partial signal; context may still be present. PARTIALLY CHARACTERIZED has
          partial support without a known signal or inherited historical seed label.
          KNOWN HISTORICAL DUF can inherit the seed label or reflect a known-function signal;
          neither implies experimental validation by itself.</dd>
        <dt>Evidence counts</dt><dd>Counts of source-specific signals, not unique proteins,
          publications, or confidence scores. Known counts Rhea reactions and experimentally
          supported GO molecular-function annotations. Partial counts specific domain/family
          assignments and other functional annotations. Context counts structural, environmental,
          orthology, interaction, and neighborhood signals; context alone does not assign function.
          Repeated annotations are not necessarily independent experiments.
          Not scored means those counts are unavailable.</dd>
        <dt>Missing counts</dt><dd>Not available means the source did not supply that counter.
          A displayed zero is a reported count, not a missing value.</dd>
      </dl>
    </section>
    <footer>Project data: <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a> ·
      Code: <a href="https://github.com/CultureBotAI/DUFMech/blob/main/LICENSE-CODE">BSD 3-Clause</a>.
      Redistributed source material retains its applicable third-party terms.
      <a href="https://github.com/CultureBotAI/DUFMech/blob/main/LICENSE">License policy</a>.</footer>
  </main>
</body>
</html>
"""


def _metric(label: str, value: int) -> str:
    return (
        f'<div class="metric"><strong>{value:,}</strong>'
        f"<span>{escape(label)}</span></div>"
    )


def _family_row(row: dict[str, Any]) -> str:
    name = escape(row["name"] or row["short_name"] or row["pfam_id"])
    short_name = escape(row["short_name"])
    pfam = escape(row["pfam_id"])
    source_url = row["source_url"]
    # family_index validates the accession, so the human entry URL is independent
    # of an optional API/source URL supplied by a snapshot.
    pfam = f'<a href="https://www.ebi.ac.uk/interpro/entry/pfam/{pfam}/">{pfam}</a>'
    source = (f' <a href="{escape(source_url, quote=True)}">Source API</a>'
              if _safe_url(source_url) else "")
    characterization_status = row["characterization_status"] or "UNSCORED"
    score_text = (
        f"Known: {_count(row['known_evidence_count'])}; "
        f"partial: {_count(row['partial_evidence_count'])}; "
        f"context: {_count(row['context_evidence_count'])}"
    )
    if characterization_status == "UNSCORED":
        score_text = "Not scored"
    search = escape(" ".join(str(row[k]) for k in ("pfam_id", "short_name", "name", "interpro_id")), quote=True)
    return f"""<tr id="{escape(row['pfam_id'], quote=True)}" data-search="{search}" data-status="{escape(row['unknown_status'], quote=True)}">
  <td>{pfam}<a class="row-link" href="#{escape(row['pfam_id'], quote=True)}">Link to this family</a>{source}</td>
  <td><strong>{name}</strong><br>{short_name}</td>
  <td class="status">{escape(row["unknown_status"].replace("_", " "))}</td>
  <td class="status">{escape(characterization_status.replace("_", " "))}</td>
  <td>{escape(score_text)}</td>
  <td class="num">{_count(row["proteins"])}</td>
  <td class="num">{_count(row["structures"])}</td>
  <td class="num">{_count(row["alphafold_models"])}</td>
  <td>{_other_mechs(row["cross_mech"])}</td>
</tr>"""


def _attach_cross_mech(
    families: list[dict[str, Any]], rows: list[dict[str, Any]]
) -> dict[str, int]:
    """Attach per-family cross-Mech links and return dashboard totals."""

    known = {family["pfam_id"] for family in families}
    extra = {row["pfam_id"] for row in rows if row.get("pfam_id")} - known
    if extra:
        raise ReportError(f"cross-Mech families absent from worklist: {', '.join(sorted(extra))}")
    by_pfam: dict[str, dict[str, Any]] = {}
    for row in rows:
        pfam_id = row.get("pfam_id") or ""
        if not pfam_id:
            continue
        entry = by_pfam.setdefault(pfam_id, {"mechs": {}, "proteins": set(), "trait": False})
        # Every worklist family has a ProteinTraitsMech trait record; report it as a flag
        # so it does not swamp the per-Mech counts and the headline metric.
        if (row["source_mech"] == PROTEIN_TRAITS_MECH
                and row["source_section"] == "trait_identifier"):
            entry["trait"] = True
            continue
        entry["mechs"].setdefault(row["source_mech"], set()).add(row["source_path"])
        if row.get("uniprot_accession"):
            entry["proteins"].add(row["uniprot_accession"])
    for family in families:
        entry = by_pfam.get(family["pfam_id"], {"mechs": {}, "proteins": set(), "trait": False})
        family["cross_mech"] = {
            "records_by_mech": {mech: len(paths) for mech, paths in sorted(entry["mechs"].items())},
            "example_proteins": len(entry["proteins"]),
            "protein_traits_record": entry["trait"],
        }
    return {
        "rows": len(rows),
        "families": sum(1 for entry in by_pfam.values() if entry["mechs"]),
        "proteins": len({row["uniprot_accession"] for row in rows if row.get("uniprot_accession")}),
    }


def _other_mechs(summary: dict[str, Any]) -> str:
    mechs = summary["records_by_mech"]
    text = "<br>".join(f"{escape(name)}: {count:,}" for name, count in mechs.items())
    proteins = summary["example_proteins"]
    if proteins:
        text += f"<br>{proteins:,} example protein{'s' if proteins != 1 else ''}"
    if summary["protein_traits_record"]:
        text += ("<br>" if text else "") + "ProteinTraitsMech trait record"
    return text


def _cross_mech_row(row: dict[str, Any], sources: dict[str, Any]) -> str:
    family = escape(row["short_name"] or row["pfam_id"])
    if row["pfam_id"]:
        family = f"{family}<br>{escape(row['pfam_id'])}"
    else:
        family = f"{family}<br>not in worklist"
    source = sources.get(row["source_mech"], {})
    record = escape(row["source_record_label"] or row["source_record_id"])
    url = f"{source.get('repository', '')}/blob/{source.get('commit', '')}/{row['source_path']}"
    if source and _safe_url(url):
        record = f'<a href="{escape(url, quote=True)}">{record}</a>'
    protein = ""
    if row["uniprot_accession"]:
        accession = escape(row["uniprot_accession"])
        protein = (
            f'<a href="https://rest.uniprot.org/uniprotkb/{accession}">{accession}</a>'
            f"<br>{escape(row['protein_label'])}"
        )
    return f"""<tr>
  <td>{family}</td>
  <td>{escape(row["source_mech"])}</td>
  <td>{record}</td>
  <td>{protein}</td>
  <td class="status">{escape(", ".join(row["link_basis"]).replace("_", " "))}</td>
</tr>"""


def _count(value: int | None) -> str:
    return "Not available" if value is None else f"{value:,}"


def _safe_url(value: str) -> bool:
    if any(ord(char) < 32 for char in value):
        return False
    try:
        parts = urlsplit(value)
        return parts.scheme in {"http", "https"} and bool(parts.hostname)
    except ValueError:
        return False


if __name__ == "__main__":
    raise SystemExit(main())
