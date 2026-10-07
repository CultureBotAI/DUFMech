"""Read Pfam previous identifiers to find families renamed from DUF/UPF names."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import zlib
from collections.abc import Iterable, Iterator, Mapping
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import httpx

DEFAULT_PFAM_RELEASE = "38.2"
PFAM_SEED_URL = "https://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam{release}/Pfam-A.seed.gz"

# A previous identifier that is itself an unknown-function name, alone or joined to a
# prefix/suffix the way Pfam builds compound names (DUF1285_N, QueG_DUF1730).
UNKNOWN_NAME_RE = re.compile(
    r"(?:[A-Za-z0-9]+_)?(?:DUF\d{1,5}|UPF\d{4})(?:[_-][A-Za-z0-9]+)*"
)
PFAM_ACCESSION_RE = re.compile(r"(PF\d{5})(?:\.(\d+))?")

PFAM_PREVIOUS_NAMES_TSV_FIELDNAMES = [
    "pfam_id",
    "pfam_version",
    "short_name",
    "description",
    "previous_unknown_names",
    "previous_ids",
    "currently_unknown_name",
    "source_url",
]


class PfamHistoryError(RuntimeError):
    """Raised when the Pfam seed file cannot be read or parsed."""


@dataclass(frozen=True)
class PfamPreviousNamesRow:
    """One Pfam family whose previous identifiers include a DUF/UPF name."""

    pfam_id: str
    pfam_version: str
    short_name: str
    description: str
    previous_unknown_names: tuple[str, ...]
    previous_ids: tuple[str, ...]
    currently_unknown_name: bool

    @property
    def source_url(self) -> str:
        return f"https://www.ebi.ac.uk/interpro/entry/pfam/{self.pfam_id}/"

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["previous_unknown_names"] = ";".join(self.previous_unknown_names)
        row["previous_ids"] = ";".join(self.previous_ids)
        row["currently_unknown_name"] = str(self.currently_unknown_name).lower()
        row["source_url"] = self.source_url
        return row


@dataclass(frozen=True)
class SeedRead:
    """Parsed rows plus the byte-level provenance of the seed file that produced them."""

    rows: list[PfamPreviousNamesRow]
    families_scanned: int
    families_with_previous_ids: int
    compressed_bytes: int
    compressed_sha256: str
    last_modified: str = ""


def is_unknown_name(name: str) -> bool:
    """Return whether a Pfam identifier is a DUF/UPF unknown-function name."""

    return bool(UNKNOWN_NAME_RE.fullmatch(name))


def parse_seed_headers(lines: Iterable[str]) -> tuple[list[PfamPreviousNamesRow], int, int]:
    """Parse Stockholm ``#=GF`` headers; return renamed-unknown rows and counts."""

    rows: list[PfamPreviousNamesRow] = []
    scanned = with_previous = 0
    family: dict[str, Any] = {}
    for line in lines:
        if line.startswith("#=GF "):
            tag, _, value = line[5:].partition(" ")
            value = value.strip()
            if tag == "PI":
                family.setdefault("PI", []).extend(
                    part.strip() for part in value.split(";") if part.strip()
                )
            elif tag in {"ID", "AC", "DE"}:
                family[tag] = value
        elif line.startswith("//"):
            if family:
                scanned += 1
                with_previous += bool(family.get("PI"))
                row = _row(family)
                if row is not None:
                    rows.append(row)
            family = {}
    if family:
        raise PfamHistoryError("Pfam seed ended inside a family record")
    return sorted(rows, key=lambda row: row.pfam_id), scanned, with_previous


def read_seed(
    *,
    seed_gz: Path | None = None,
    release: str = DEFAULT_PFAM_RELEASE,
    transport: httpx.BaseTransport | None = None,
    timeout: float = 120.0,
) -> SeedRead:
    """Read a local or downloaded ``Pfam-A.seed.gz`` without keeping alignments."""

    digest = hashlib.sha256()
    counter = {"bytes": 0}
    last_modified = ""

    def tracked(chunks: Iterable[bytes]) -> Iterator[bytes]:
        for chunk in chunks:
            digest.update(chunk)
            counter["bytes"] += len(chunk)
            yield chunk

    if seed_gz is not None:
        with seed_gz.open("rb") as handle:
            rows, scanned, with_previous = parse_seed_headers(
                _gunzip_lines(tracked(iter(lambda: handle.read(1 << 20), b"")))
            )
    else:
        url = PFAM_SEED_URL.format(release=release)
        try:
            with (
                httpx.Client(
                    timeout=timeout, transport=transport, follow_redirects=True
                ) as client,
                client.stream("GET", url) as response,
            ):
                response.raise_for_status()
                last_modified = response.headers.get("last-modified", "")
                expected = response.headers.get("content-length")
                rows, scanned, with_previous = parse_seed_headers(
                    _gunzip_lines(tracked(response.iter_raw()))
                )
        except httpx.HTTPError as exc:
            raise PfamHistoryError(f"could not download {url}: {exc!r}") from exc
        if expected is not None and int(expected) != counter["bytes"]:
            raise PfamHistoryError(
                f"{url} returned {counter['bytes']} bytes, expected {expected}"
            )
    return SeedRead(
        rows=rows,
        families_scanned=scanned,
        families_with_previous_ids=with_previous,
        compressed_bytes=counter["bytes"],
        compressed_sha256=digest.hexdigest(),
        last_modified=last_modified,
    )


def previous_name_index(rows: Iterable[Mapping[str, Any]]) -> dict[str, list[Mapping[str, Any]]]:
    """Map each previous DUF/UPF name to the current families that list it."""

    index: dict[str, list[Mapping[str, Any]]] = {}
    for row in rows:
        for name in row.get("previous_unknown_names") or ():
            index.setdefault(name, []).append(row)
    return index


def render_previous_names_tsv(rows: Iterable[PfamPreviousNamesRow]) -> str:
    """Render rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=PFAM_PREVIOUS_NAMES_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_previous_names_json(rows: Iterable[PfamPreviousNamesRow]) -> str:
    """Render rows as stable JSON."""

    return json.dumps(
        [
            {
                **asdict(row),
                "previous_unknown_names": list(row.previous_unknown_names),
                "previous_ids": list(row.previous_ids),
                "source_url": row.source_url,
            }
            for row in rows
        ],
        indent=2,
        sort_keys=True,
    )


def _row(family: Mapping[str, Any]) -> PfamPreviousNamesRow | None:
    previous = tuple(dict.fromkeys(family.get("PI", ())))
    unknown = tuple(name for name in previous if is_unknown_name(name))
    if not unknown:
        return None
    match = PFAM_ACCESSION_RE.fullmatch(family.get("AC", ""))
    short_name = family.get("ID", "")
    if match is None or not short_name:
        raise PfamHistoryError(f"Pfam seed family lacks ID/AC: {family.get('AC')!r}")
    return PfamPreviousNamesRow(
        pfam_id=match.group(1),
        pfam_version=family["AC"],
        short_name=short_name,
        description=family.get("DE", ""),
        previous_unknown_names=unknown,
        previous_ids=previous,
        currently_unknown_name=is_unknown_name(short_name),
    )


def _gunzip_lines(chunks: Iterable[bytes]) -> Iterator[str]:
    decompressor = zlib.decompressobj(16 + zlib.MAX_WBITS)
    pending = b""
    for chunk in chunks:
        data = decompressor.decompress(chunk)
        # Pfam-A.seed.gz is a concatenation of gzip members; continue into each one.
        while decompressor.eof and decompressor.unused_data:
            rest = decompressor.unused_data
            decompressor = zlib.decompressobj(16 + zlib.MAX_WBITS)
            data += decompressor.decompress(rest)
        pending += data
        *lines, pending = pending.split(b"\n")
        for line in lines:
            if line.startswith((b"#=GF ", b"//")):
                yield line.decode("utf-8", errors="replace")
    if not decompressor.eof:
        raise PfamHistoryError("Pfam seed gzip stream is truncated")
    if pending.startswith((b"#=GF ", b"//")):
        yield pending.decode("utf-8", errors="replace")
