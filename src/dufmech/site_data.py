"""Offline, evidence-preserving adapters for the DUFMech website."""

from __future__ import annotations

import re
from html import escape
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import quote, urlsplit

from dufmech.report import ReportError
from dufmech.site_sources import load_source_pins

COMMIT_RE = re.compile(r"[0-9a-f]{40}")
PFAM_RE = re.compile(r"PF[0-9]{5}")
IPR_RE = re.compile(r"IPR[0-9]{6}")


def safe_url(value: str) -> bool:
    if not isinstance(value, str) or any(ord(char) < 32 for char in value):
        return False
    try:
        parts = urlsplit(value)
        return (parts.scheme in {"http", "https"} and bool(parts.hostname)
                and not parts.username and not parts.password)
    except ValueError:
        return False


def source_link(repository: str, commit: str, path: str) -> str:
    """Construct only immutable links with a validated repository-relative path."""
    parts = PurePosixPath(path)
    if (not safe_url(repository) or not COMMIT_RE.fullmatch(commit) or not path
            or parts.is_absolute() or ".." in parts.parts or "\\" in path
            or any(ord(char) < 32 for char in path)):
        return ""
    return f"{repository.rstrip('/')}/blob/{commit}/{quote(path, safe='/')}"


def tracked_source(
    path: Path, root: Path, *, pins: dict[str, dict[str, str]] | None = None,
) -> dict[str, str]:
    """Read a content-verified explicit pin; never derive links from checkout history."""
    pins = load_source_pins(root) if pins is None else pins
    try:
        relative = path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return {}
    if pins and relative not in pins:
        raise ReportError(f"site source absent from explicit pin ledger: {relative}")
    return pins.get(relative, {})


def tracked_tree(
    directory: Path, root: Path, *, pins: dict[str, dict[str, str]] | None = None,
) -> dict[str, dict[str, str]]:
    """Read explicit source pins for a directory, with no history-sensitive Git lookup."""
    pins = load_source_pins(root) if pins is None else pins
    try:
        relative = directory.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return {}
    return {path: source for path, source in pins.items() if path.startswith(relative + "/")}


def link(url: str, label: str) -> str:
    text = escape(str(label))
    return f'<a href="{escape(url, quote=True)}">{text}</a>' if safe_url(url) else text


def pfam_url(accession: str) -> str:
    return f"https://www.ebi.ac.uk/interpro/entry/pfam/{accession}/"


def reference_url(reference: dict[str, Any]) -> str:
    """Only explicit source URLs and explicit bibliographic IDs become links."""
    if safe_url(reference.get("url", "")):
        return reference["url"]
    identifier = str(reference.get("id", reference.get("reference", "")))
    if re.fullmatch(r"PMID:[0-9]+", identifier):
        return f"https://pubmed.ncbi.nlm.nih.gov/{identifier[5:]}/"
    if re.fullmatch(r"PMC:[0-9]+|PMC[0-9]+", identifier):
        return f"https://pmc.ncbi.nlm.nih.gov/articles/{identifier.replace(':', '')}/"
    if identifier.lower().startswith("doi:") and re.fullmatch(r"10\.\d{4,9}/\S+", identifier[4:]):
        return "https://doi.org/" + quote(identifier[4:], safe="/")
    return identifier if safe_url(identifier) else ""


def description_html(
    description: str, pfam: str, *, labels: dict[str, str],
    publications: dict[str, dict[str, Any]] | None = None,
) -> str:
    """Escape prose and resolve recognized source markup without treating PUB as PMID."""
    publications = publications or {}
    pattern = re.compile(
        r"\[cite:(PUB[0-9]+)\]|\[(pfam|interpro|swissprot):([A-Za-z0-9]+)\]"
        r"|\bPMID:([0-9]+)\b|https?://[^\s<>\[\]]+"
    )
    chunks: list[str] = []
    start = 0
    for match in pattern.finditer(description):
        chunks.append(escape(description[start:match.start()]))
        pub, namespace, accession, pmid = match.groups()
        if pub:
            resolved = publications.get(pub, {})
            url = reference_url(resolved) or pfam_url(pfam)
            label = resolved.get("label") or f"InterPro reference {pub}"
            chunks.append(link(url, label))
        elif namespace == "pfam" and PFAM_RE.fullmatch(accession):
            label = labels.get(accession, "Pfam entry")
            chunks.append(link(pfam_url(accession), f"{accession} ({label})"))
        elif namespace == "interpro" and IPR_RE.fullmatch(accession):
            chunks.append(link(f"https://www.ebi.ac.uk/interpro/entry/InterPro/{accession}/",
                               f"{accession} (InterPro entry)"))
        elif namespace == "swissprot":
            chunks.append(link(f"https://www.uniprot.org/uniprotkb/{accession}/entry",
                               f"{accession} (UniProtKB protein)"))
        elif pmid:
            chunks.append(link(f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", f"PMID:{pmid}"))
        elif match.group(0).startswith("http"):
            url = match.group(0).rstrip(".,;)")
            chunks.append(link(url, url) + escape(match.group(0)[len(url):]))
        else:
            chunks.append(escape(match.group(0)))
        start = match.end()
    chunks.append(escape(description[start:]))
    return "".join(chunks)


def group_members(rows: list[dict[str, Any]], families: set[str]) -> dict[str, list[dict]]:
    """Validate actual residue coordinates; no guessed lengths or synthetic ranges."""
    grouped: dict[str, list[dict]] = {}
    for row in rows:
        pfam = row.get("pfam_id")
        if pfam not in families:
            raise ReportError(f"member family absent from worklist: {pfam}")
        length = row.get("length")
        ranges = row.get("match_ranges", [])
        if not isinstance(ranges, list):
            raise ReportError(f"{pfam}: match_ranges must be a list")
        if not ranges or length is None:
            continue
        if type(length) is not int or length < 1:
            raise ReportError(f"{pfam}: invalid member length")
        parsed = []
        for item in ranges:
            match = re.fullmatch(r"([0-9]+)-([0-9]+)", str(item))
            if not match or not 1 <= int(match[1]) <= int(match[2]) <= length:
                raise ReportError(f"{pfam}: invalid member match range {item!r}")
            parsed.append([int(match[1]), int(match[2])])
        accession = str(row.get("uniprot_accession", ""))
        if not re.fullmatch(r"[A-Z0-9]+", accession):
            raise ReportError(f"{pfam}: invalid member accession")
        grouped.setdefault(pfam, []).append({**row, "ranges": sorted(parsed)})
    for members in grouped.values():
        members.sort(key=lambda row: (row["uniprot_accession"], row["ranges"]))
    return grouped
