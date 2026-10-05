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
from dufmech.cross_mech_snapshot import CROSS_MECH_DIR, CROSS_MECH_STEM
from dufmech.report import (
    ReportError,
    build_report,
    family_index,
    latest_snapshot_path,
    load_json_rows,
    load_latest_rows,
    verified_manifest,
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
.table-wrap { overflow-x: auto; }
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
}
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
        manifest = verified_manifest(cross_mech_path)
        worklist_input = manifest["snapshot"].get("input_snapshot_ids", {}).get("worklist")
        if worklist_input != input_ids["worklist"]:
            raise ReportError(
                f"{cross_mech_path.name} was built against {worklist_input}, "
                f"not {input_ids['worklist']}; regenerate the cross-Mech snapshot"
            )
        input_ids["cross_mech"] = cross_mech_path.stem
        cross_mech_rows = [dict(row) for row in load_json_rows(cross_mech_path)]
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
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main>
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
      {_metric("Families linked from other Mechs", cross["families"])}
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
        canonical-example links are counted per family below.
        Names marked "not in worklist" are DUF/UPF names that no longer match a current
        Pfam short name.</p>
      <div class="table-wrap">
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
      <h2>Families</h2>
      <div class="table-wrap">
        <table>
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
    </section>
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
    if _safe_url(source_url):
        pfam = f'<a href="{escape(source_url, quote=True)}">{pfam}</a>'
    characterization_status = row["characterization_status"] or "UNSCORED"
    score_text = (
        f"Known: {_count(row['known_evidence_count'])}; "
        f"partial: {_count(row['partial_evidence_count'])}; "
        f"context: {_count(row['context_evidence_count'])}"
    )
    if characterization_status == "UNSCORED":
        score_text = "Not scored"
    return f"""<tr>
  <td>{pfam}</td>
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

    by_pfam: dict[str, dict[str, Any]] = {}
    for row in rows:
        pfam_id = row.get("pfam_id") or ""
        if not pfam_id:
            continue
        entry = by_pfam.setdefault(pfam_id, {"mechs": {}, "proteins": set()})
        entry["mechs"][row["source_mech"]] = entry["mechs"].get(row["source_mech"], 0) + 1
        if row.get("uniprot_accession"):
            entry["proteins"].add(row["uniprot_accession"])
    known = {family["pfam_id"] for family in families}
    extra = by_pfam.keys() - known
    if extra:
        raise ReportError(f"cross-Mech families absent from worklist: {', '.join(sorted(extra))}")
    for family in families:
        entry = by_pfam.get(family["pfam_id"], {"mechs": {}, "proteins": set()})
        family["cross_mech"] = {
            "records_by_mech": dict(sorted(entry["mechs"].items())),
            "example_proteins": len(entry["proteins"]),
        }
    return {
        "rows": len(rows),
        "families": len(by_pfam),
        "proteins": len({row["uniprot_accession"] for row in rows if row.get("uniprot_accession")}),
    }


def _other_mechs(summary: dict[str, Any]) -> str:
    mechs = summary["records_by_mech"]
    if not mechs:
        return ""
    text = "<br>".join(f"{escape(name)}: {count:,}" for name, count in mechs.items())
    proteins = summary["example_proteins"]
    if proteins:
        text += f"<br>{proteins:,} example protein{'s' if proteins != 1 else ''}"
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
