"""Offline site structure, reachability, contrast-token and byte-budget gate."""

from __future__ import annotations

import argparse
import gzip
import json
import posixpath
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from dufmech.site_files import PENDING


class Page(HTMLParser):
    def __init__(self, content: str):
        super().__init__()
        self.links: list[str] = []
        self.ids: list[str] = []
        self.feed(content)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.append(attributes["id"])
        for key in ("href", "src"):
            if attributes.get(key):
                self.links.append(attributes[key])


def contrast(first: str, second: str) -> float:
    def luminance(color: str) -> float:
        values = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        linear = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in values]
        return sum(v * factor for v, factor in zip(linear, (.2126, .7152, .0722), strict=True))
    a, b = sorted((luminance(first), luminance(second)))
    return (b + .05) / (a + .05)


def check_site(site: Path, budgets: dict) -> tuple[list[str], dict]:
    """Return actionable failures; browser interaction/geometry require the browser suite."""
    errors: list[str] = []
    root = site.resolve()
    if (root / PENDING).exists() or (root / PENDING).is_symlink():
        errors.append("unfinished render: pending ownership journal remains")
    if any(root.glob(".dufmech-stage-*")):
        errors.append("unfinished render: staging directory remains")
    limits = {
        "index_html_bytes": budgets["groups"]["index"]["largest_bytes"],
        "html_bytes": budgets["groups"]["html"]["largest_bytes"],
        "catalogue_gzip_bytes": 400000, "initial_gzip_bytes": 450000,
        "total_bytes": budgets["site_total_bytes"],
    }
    files = {p.relative_to(root).as_posix(): p for p in root.rglob("*") if p.is_file()}
    for required in ("index.html", "index.json", "catalogue.json", "categories.html", "sources.html",
                     "style.css", "dashboard.js", "theme.js"):
        if required not in files:
            errors.append(f"missing required site artifact: {required}")
    if errors:
        return errors, {}
    payload = json.loads(files["index.json"].read_text())
    ids = {row["pfam_id"] for row in payload["families"]}
    if len(ids) != payload["summary"]["families"]["total"]:
        errors.append("corpus count or family uniqueness mismatch")
    data = json.loads(files["catalogue.json"].read_text())
    search_ids = [row[data["fields"].index("pfam_id")] for row in data["rows"]]
    if len(search_ids) != len(ids) or set(search_ids) != ids:
        errors.append("search index does not cover exactly the full catalogue")
    parsed = {name: Page(path.read_text()) for name, path in files.items() if name.endswith(".html")}
    reached = set()
    for name, page in parsed.items():
        if len(page.ids) != len(set(page.ids)):
            errors.append(f"duplicate HTML ID: {name}")
        for href in page.links:
            parts = urlsplit(href)
            if parts.scheme or parts.netloc:
                continue
            relative = (posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(parts.path)))
                        if parts.path else name)
            if relative not in files:
                errors.append(f"broken local link: {name} -> {href}")
                continue
            if relative.startswith("families/") and relative.endswith(".html"):
                reached.add(Path(relative).stem)
            if parts.fragment and relative in parsed and unquote(parts.fragment) not in parsed[relative].ids:
                errors.append(f"missing anchor: {name} -> {href}")
        if name == "index.html" or name.startswith(("browse/", "category/")):
            row_count = len([identifier for identifier in page.ids if re.fullmatch(r"PF[0-9]{5}", identifier)])
            if row_count > 50:
                errors.append(f"too many initial family rows: {name}: {row_count}")
    for pfam in sorted(ids):
        if f"families/{pfam}.html" not in parsed or f"families/{pfam}.json" not in files:
            errors.append(f"missing family detail: {pfam}")
    if reached != ids:
        errors.append("family links do not reach exactly the complete catalogue")
    # Walk only local page edges from the landing page, including static pagination.
    visited, pending = set(), ["index.html"]
    while pending:
        name = pending.pop()
        if name in visited:
            continue
        visited.add(name)
        for href in parsed[name].links:
            parts = urlsplit(href)
            if parts.scheme or parts.netloc:
                continue
            relative = (posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(parts.path)))
                        if parts.path else name)
            if relative in parsed and relative not in visited:
                pending.append(relative)
    unreachable = set(parsed) - visited
    if unreachable:
        errors.append(f"unreachable HTML pages: {', '.join(sorted(unreachable)[:5])}")
    sizes = {name: path.stat().st_size for name, path in files.items()}
    initial = ["index.html", "style.css", "theme.js", "dashboard.js", "catalogue.json"]
    measurements = {
        "index_html_bytes": sizes["index.html"],
        "html_bytes": max(sizes[name] for name in parsed),
        "catalogue_gzip_bytes": len(gzip.compress(files["catalogue.json"].read_bytes(), mtime=0)),
        "initial_gzip_bytes": sum(len(gzip.compress(files[name].read_bytes(), mtime=0)) for name in initial),
        "total_bytes": sum(sizes.values()), "families": len(ids), "html_pages": len(parsed),
    }
    for key in ("index_html_bytes", "html_bytes", "catalogue_gzip_bytes", "initial_gzip_bytes", "total_bytes"):
        if measurements[key] > limits[key]:
            errors.append(f"{key}: {measurements[key]} exceeds {limits[key]}")
    if len(files) > budgets["generated_file_count"] or len(files) < budgets["min_files"]:
        errors.append(f"generated file count outside budget: {len(files)}")
    if sizes["catalogue.json"] > budgets["groups"]["catalogue"]["largest_bytes"]:
        errors.append("uncompressed search index exceeds byte budget")
    css = files["style.css"].read_text()
    schemes = re.findall(r":root[^{}]*\{([^{}]+)\}", css)
    for index, block in enumerate(schemes):
        tokens = dict(re.findall(r"--([a-z]+):\s*(#[0-9a-fA-F]{6})", block))
        for foreground in ("fg", "muted", "accent"):
            for background in ("page", "card"):
                ratio = contrast(tokens[foreground], tokens[background])
                if ratio < 4.5:
                    errors.append(f"theme {index}: {foreground}/{background} contrast {ratio:.2f}")
        if contrast(tokens["bar"], tokens["track"]) < 3:
            errors.append(f"theme {index}: chart contrast below threshold")
    if len(schemes) < 2:
        errors.append("both light and dark theme tokens are required")
    return errors, measurements


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=Path("pages"))
    parser.add_argument("--budgets", type=Path, default=Path("conf/pages_budgets.json"))
    args = parser.parse_args(argv)
    errors, measurements = check_site(args.site, json.loads(args.budgets.read_text()))
    print(json.dumps({"measurements": measurements, "errors": errors}, indent=2, sort_keys=True))
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
