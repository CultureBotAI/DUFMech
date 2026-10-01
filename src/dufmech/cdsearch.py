"""Fetch conserved-domain hits from NCBI Batch CD-Search."""

from __future__ import annotations

import csv
import io
import json
import re
import time
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import asdict, dataclass

import httpx

CDSEARCH_URL = "https://www.ncbi.nlm.nih.gov/Structure/bwrpsb/bwrpsb.cgi"
CDSEARCH_CDD_URL = "https://www.ncbi.nlm.nih.gov/Structure/cdd/cddsrv.cgi"
DEFAULT_CDSEARCH_DB = "cdd"
DEFAULT_CDSEARCH_MODE = "all"
DEFAULT_CDSEARCH_BATCH_SIZE = 1000

CDSEARCH_RESPONSE_FIELDNAMES = [
    "Query",
    "Hit type",
    "PSSM-ID",
    "From",
    "To",
    "E-Value",
    "Bitscore",
    "Accession",
    "Short name",
    "Incomplete",
    "Superfamily",
]

CDSEARCH_TSV_FIELDNAMES = [
    "uniprot_accession",
    "query_label",
    "hit_type",
    "pssm_id",
    "start",
    "end",
    "e_value",
    "bitscore",
    "cdd_accession",
    "short_name",
    "incomplete",
    "superfamily_accession",
    "source_url",
]

_QUERY_RE = re.compile(r"^Q#(?P<index>\d+)\s+-\s+")


class CdSearchClientError(RuntimeError):
    """Raised when Batch CD-Search returns an invalid or failing response."""


@dataclass(frozen=True)
class CdSearchDomainRow:
    """One conserved-domain hit for a UniProt accession."""

    uniprot_accession: str
    query_label: str
    hit_type: str
    pssm_id: str
    start: int | None
    end: int | None
    e_value: float | None
    bitscore: float | None
    cdd_accession: str
    short_name: str
    incomplete: str
    superfamily_accession: str

    @property
    def source_url(self) -> str:
        return f"{CDSEARCH_CDD_URL}?uid={self.cdd_accession}"

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["source_url"] = self.source_url
        return row


@dataclass(frozen=True)
class CdSearchStatus:
    """One Batch CD-Search response status."""

    cdsid: str
    status: int | None
    message: str


class CdSearchClient:
    """Small client for NCBI Batch CD-Search."""

    def __init__(
        self,
        *,
        poll_interval: float = 2.0,
        max_polls: int = 20,
        timeout: float = 30.0,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self.poll_interval = poll_interval
        self.max_polls = max_polls
        self.timeout = timeout
        self.transport = transport

    def search_accessions(
        self,
        accessions: Sequence[str],
        *,
        db: str = DEFAULT_CDSEARCH_DB,
        mode: str = DEFAULT_CDSEARCH_MODE,
    ) -> Iterable[Mapping[str, str]]:
        """Submit UniProt accessions and poll until Batch CD-Search completes."""

        if not accessions:
            return

        text = self._fetch(
            {
                "queries": "\n".join(accessions),
                "useid1": "true",
                "tdata": "hits",
                "db": db,
                "dmode": mode,
                "qdefl": "true",
            }
        )
        status = parse_cdsearch_status(text)
        if not status.cdsid:
            raise CdSearchClientError("Batch CD-Search response had no cdsid")

        for poll_index in range(self.max_polls + 1):
            if status.status == 0:
                yield from parse_cdsearch_tsv(text)
                return
            if status.status != 3:
                raise CdSearchClientError(
                    f"Batch CD-Search {status.cdsid} failed with "
                    f"status {status.status}: {status.message}"
                )
            if poll_index >= self.max_polls:
                break

            time.sleep(self.poll_interval)
            text = self._fetch(
                {
                    "cdsid": status.cdsid,
                    "tdata": "hits",
                    "dmode": mode,
                    "qdefl": "true",
                }
            )
            status = parse_cdsearch_status(text)

        raise CdSearchClientError(
            f"Batch CD-Search {status.cdsid} was still running "
            f"after {self.max_polls} polls"
        )

    def _fetch(self, params: Mapping[str, str]) -> str:
        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=True,
            transport=self.transport,
        ) as client:
            response = client.get(CDSEARCH_URL, params=params)
            try:
                response.raise_for_status()
            except httpx.HTTPError as exc:
                raise CdSearchClientError("could not fetch Batch CD-Search") from exc
        return response.text


def collect_cdsearch_rows(
    accessions: Iterable[str],
    client: CdSearchClient,
    *,
    db: str = DEFAULT_CDSEARCH_DB,
    mode: str = DEFAULT_CDSEARCH_MODE,
    batch_size: int = DEFAULT_CDSEARCH_BATCH_SIZE,
) -> list[CdSearchDomainRow]:
    """Collect conserved-domain hits for ordered, unique UniProt accessions."""

    rows: list[CdSearchDomainRow] = []
    seen_rows: set[tuple[str, str, str, int | None, int | None, str]] = set()
    for batch in _batches(_unique_accessions(accessions), size=batch_size):
        accessions_by_query = {
            index: accession for index, accession in enumerate(batch, start=1)
        }
        for record in client.search_accessions(batch, db=db, mode=mode):
            query_index = _query_index(record.get("Query"))
            if query_index is None:
                continue
            row = row_from_cdsearch_record(
                accessions_by_query.get(query_index, ""),
                record,
            )
            if row is None:
                continue
            key = (
                row.uniprot_accession,
                row.hit_type,
                row.cdd_accession,
                row.start,
                row.end,
                row.pssm_id,
            )
            if key in seen_rows:
                continue
            seen_rows.add(key)
            rows.append(row)

    return sorted(
        rows,
        key=lambda row: (
            row.uniprot_accession,
            row.start or 0,
            row.end or 0,
            row.cdd_accession,
            row.hit_type,
        ),
    )


def parse_cdsearch_status(text: str) -> CdSearchStatus:
    """Parse the comment-prefixed Batch CD-Search status block."""

    cdsid = ""
    status: int | None = None
    message = ""
    for line in text.splitlines():
        if not line.startswith("#"):
            continue
        parts = [part.strip() for part in line[1:].split("\t")]
        if len(parts) < 2:
            continue
        if parts[0] == "cdsid":
            cdsid = parts[1]
        if parts[0] == "status" and parts[1].isdigit():
            status = int(parts[1])
            try:
                message = parts[parts.index("msg") + 1]
            except (ValueError, IndexError):
                message = ""

    return CdSearchStatus(cdsid=cdsid, status=status, message=message)


def parse_cdsearch_tsv(text: str) -> list[Mapping[str, str]]:
    """Parse a Batch CD-Search hits TSV response into records."""

    payload = "\n".join(
        line for line in text.splitlines() if line and not line.startswith("#")
    )
    if not payload:
        return []

    reader = csv.DictReader(io.StringIO(payload), dialect="excel-tab")
    if reader.fieldnames != CDSEARCH_RESPONSE_FIELDNAMES:
        raise CdSearchClientError(
            "Batch CD-Search result had unexpected TSV fieldnames"
        )
    return [
        {key: value or "" for key, value in row.items() if key is not None}
        for row in reader
    ]


def row_from_cdsearch_record(
    accession: str,
    record: Mapping[str, str],
) -> CdSearchDomainRow | None:
    """Return a normalized conserved-domain hit, or ``None`` if malformed."""

    accession = _string(accession)
    cdd_accession = _blank_dash(record.get("Accession"))
    if not accession or not cdd_accession:
        return None

    return CdSearchDomainRow(
        uniprot_accession=accession,
        query_label=_string(record.get("Query")),
        hit_type=_string(record.get("Hit type")),
        pssm_id=_blank_dash(record.get("PSSM-ID")),
        start=_int(record.get("From")),
        end=_int(record.get("To")),
        e_value=_float(record.get("E-Value")),
        bitscore=_float(record.get("Bitscore")),
        cdd_accession=cdd_accession,
        short_name=_blank_dash(record.get("Short name")),
        incomplete=_blank_dash(record.get("Incomplete")),
        superfamily_accession=_blank_dash(record.get("Superfamily")),
    )


def render_cdsearch_tsv(rows: Iterable[CdSearchDomainRow]) -> str:
    """Render conserved-domain hits as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=CDSEARCH_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_cdsearch_json(rows: Iterable[CdSearchDomainRow]) -> str:
    """Render conserved-domain hits as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def _unique_accessions(accessions: Iterable[str]) -> list[str]:
    rows: list[str] = []
    seen: set[str] = set()
    for accession in accessions:
        accession = _string(accession)
        if not accession or accession in seen:
            continue
        seen.add(accession)
        rows.append(accession)
    return rows


def _batches(accessions: Sequence[str], *, size: int) -> Iterable[Sequence[str]]:
    for index in range(0, len(accessions), size):
        yield accessions[index : index + size]


def _query_index(value: object) -> int | None:
    if not isinstance(value, str):
        return None
    match = _QUERY_RE.match(value)
    if match is None:
        return None
    return int(match.group("index"))


def _int(value: object) -> int | None:
    try:
        return int(value) if isinstance(value, str) and value else None
    except ValueError:
        return None


def _float(value: object) -> float | None:
    try:
        return float(value) if isinstance(value, str) and value else None
    except ValueError:
        return None


def _blank_dash(value: object) -> str:
    value = _string(value)
    return "" if value == "-" else value


def _string(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""
