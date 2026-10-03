"""Render a deterministic static dashboard for DUF/PUF snapshots."""

from __future__ import annotations

import argparse
import filecmp
import json
import shutil
import tempfile
from html import escape
from pathlib import Path
from typing import Any

from dufmech.report import build_report, family_index, load_latest_rows

PAGES_DIR = Path("pages")
WORKLISTS_DIR = Path("data/worklists")

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
    --bg: #111827;
    --panel: #1f2937;
    --text: #f9fafb;
    --muted: #cbd5e1;
    --line: #374151;
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
}
.metrics {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 12px;
  margin: 28px 0;
}
.metric,
.section {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
}
.metric {
  padding: 14px 16px;
}
.metric strong {
  display: block;
  font-size: 1.7rem;
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
  overflow: hidden;
}
.section h2 {
  margin: 0;
  padding: 14px 16px;
  border-bottom: 1px solid var(--line);
  font-size: 1rem;
}
table {
  width: 100%;
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
  white-space: nowrap;
}
@media (max-width: 720px) {
  main { padding: 20px 12px 32px; }
  .table-wrap { overflow-x: auto; }
  table { min-width: 760px; }
}
""".strip()


def render_site(
    worklist_rows: list[dict[str, Any]],
    score_rows: list[dict[str, Any]],
    *,
    input_ids: dict[str, str],
    out_dir: Path,
) -> None:
    """Render a static DUFMech dashboard into ``out_dir``."""

    families = family_index(worklist_rows, score_rows)
    report = build_report(worklist_rows, score_rows, top_n=20)

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")
    (out_dir / "style.css").write_text(STYLE_CSS + "\n", encoding="utf-8")
    (out_dir / "index.json").write_text(
        json.dumps(
            {
                "inputs": dict(sorted(input_ids.items())),
                "summary": report,
                "families": families,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    (out_dir / "index.html").write_text(
        _index_html(report, families, input_ids),
        encoding="utf-8",
    )


def render_from_paths(
    *,
    out_dir: Path,
    worklists_dir: Path = WORKLISTS_DIR,
    worklist_json: Path | None = None,
    score_json: Path | None = None,
) -> None:
    """Load frozen snapshots and render pages."""

    worklist_rows, score_rows, input_ids = load_latest_rows(
        worklists_dir,
        worklist_json=worklist_json,
        score_json=score_json,
    )
    render_site(
        [dict(row) for row in worklist_rows],
        [dict(row) for row in score_rows],
        input_ids=input_ids,
        out_dir=out_dir,
    )


def diff_trees(expected: Path, actual: Path) -> list[str]:
    """Return deterministic relative paths that differ between two trees."""

    diffs: list[str] = []

    def walk(cmp: filecmp.dircmp, prefix: str) -> None:
        names = sorted(cmp.left_only + cmp.right_only + cmp.diff_files)
        diffs.extend(f"{prefix}{name}" for name in names)
        for name in sorted(cmp.subdirs):
            walk(cmp.subdirs[name], f"{prefix}{name}/")

    walk(filecmp.dircmp(expected, actual), "")
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

    if args.out.exists():
        shutil.rmtree(args.out)
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
) -> str:
    metrics = report["families"]
    rows = "\n".join(_family_row(row) for row in families)
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
      First-pass Domain of Unknown Function and Protein of Unknown Function
      families from frozen InterPro/Pfam snapshots, with optional evidence
      scores folded into a reproducible corpus dashboard.
    </p>
    <p class="lede">{inputs}</p>

    <section class="metrics" aria-label="Corpus metrics">
      {_metric("Families", metrics["total"])}
      {_metric("InterPro IDs", metrics["with_interpro_id"])}
      {_metric("Structures", metrics["with_structures"])}
      {_metric("AlphaFold", metrics["with_alphafold_models"])}
      {_metric("Proteins", metrics["interpro_proteins"])}
      {_metric("Matches", metrics["interpro_matches"])}
    </section>

    <section class="section">
      <h2>Families</h2>
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Pfam</th>
              <th>Family</th>
              <th>Status</th>
              <th>Scores</th>
              <th class="num">Proteins</th>
              <th class="num">Structures</th>
              <th class="num">AlphaFold</th>
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
    source_url = escape(row["source_url"], quote=True)
    characterization_status = row["characterization_status"] or "UNSCORED"
    score_text = (
        f"K {row['known_evidence_count']} / "
        f"P {row['partial_evidence_count']} / "
        f"C {row['context_evidence_count']}"
    )
    return f"""<tr>
  <td><a href="{source_url}">{escape(row["pfam_id"])}</a></td>
  <td><strong>{name}</strong><br>{short_name}</td>
  <td class="status">{escape(characterization_status)}</td>
  <td>{escape(score_text)}</td>
  <td class="num">{row["proteins"]:,}</td>
  <td class="num">{row["structures"]:,}</td>
  <td class="num">{row["alphafold_models"]:,}</td>
</tr>"""


if __name__ == "__main__":
    raise SystemExit(main())
