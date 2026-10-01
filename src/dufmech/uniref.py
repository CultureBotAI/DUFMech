"""Collapse UniProtKB accessions to UniRef clusters."""

from __future__ import annotations

import csv
import io
import json
import time
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from typing import Any

import httpx

UNIPROT_ID_MAPPING_URL = "https://rest.uniprot.org/idmapping/run"
UNIPROT_ID_MAPPING_STATUS_URL = "https://rest.uniprot.org/idmapping/status/{job_id}"
UNIPROT_ACCESSION_SOURCE = "UniProtKB_AC-ID"
DEFAULT_UNIREF_TARGET = "UniRef90"

UNIREF_TSV_FIELDNAMES = [
    "uniprot_accession",
    "uniref_id",
    "uniref_type",
    "name",
    "updated",
    "member_count",
    "organism_count",
    "common_taxon_id",
    "common_taxon_name",
    "representative_accession",
    "representative_member_id",
    "representative_protein_name",
    "representative_taxon_id",
    "representative_length",
    "seed_id",
    "source_url",
]


class UniProtIdMappingError(RuntimeError):
    """Raised when UniProt ID Mapping returns an invalid or failing response."""


@dataclass(frozen=True)
class UniRefMappingRow:
    """One UniProtKB accession collapsed to a UniRef cluster."""

    uniprot_accession: str
    uniref_id: str
    uniref_type: str
    name: str
    updated: str
    member_count: int | None
    organism_count: int | None
    common_taxon_id: str
    common_taxon_name: str
    representative_accession: str
    representative_member_id: str
    representative_protein_name: str
    representative_taxon_id: str
    representative_length: int | None
    seed_id: str

    @property
    def source_url(self) -> str:
        return f"https://rest.uniprot.org/uniref/{self.uniref_id}"

    def tsv_row(self) -> dict[str, object]:
        return {**asdict(self), "source_url": self.source_url}


class UniProtIdMappingClient:
    """Small client for UniProt accession-to-UniRef ID mapping jobs."""

    def __init__(
        self,
        *,
        timeout: float = 30.0,
        poll_interval: float = 1.0,
        max_polls: int = 60,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self.timeout = timeout
        self.poll_interval = poll_interval
        self.max_polls = max_polls
        self.transport = transport

    def map_uniref(
        self,
        accessions: Iterable[str],
        *,
        target: str = DEFAULT_UNIREF_TARGET,
    ) -> Iterable[Mapping[str, Any]]:
        accessions = [accession for accession in accessions if accession]
        if not accessions:
            return

        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=True,
            transport=self.transport,
        ) as client:
            job_id = _submit_mapping_job(client, accessions, target)
            yield from _iter_mapping_results(
                client,
                job_id,
                max_polls=self.max_polls,
                poll_interval=self.poll_interval,
            )


def collect_uniref_mappings(
    mapping_results: Iterable[Mapping[str, Any]],
) -> list[UniRefMappingRow]:
    """Normalize UniProt ID Mapping results into sorted UniRef rows."""

    rows: list[UniRefMappingRow] = []
    seen: set[tuple[str, str]] = set()
    for result in mapping_results:
        row = row_from_uniref_mapping(result)
        if row is None:
            continue
        key = (row.uniprot_accession, row.uniref_id)
        if key in seen:
            continue
        seen.add(key)
        rows.append(row)
    return sorted(rows, key=lambda row: (row.uniref_id, row.uniprot_accession))


def row_from_uniref_mapping(result: Mapping[str, Any]) -> UniRefMappingRow | None:
    """Return a normalized UniRef mapping row, or ``None`` if malformed."""

    uniprot_accession = _string(result.get("from"))
    cluster = _mapping(result.get("to"))
    uniref_id = _string(cluster.get("id"))
    if not uniprot_accession or not uniref_id:
        return None

    common_taxon = _mapping(cluster.get("commonTaxon"))
    representative = _mapping(cluster.get("representativeMember"))

    return UniRefMappingRow(
        uniprot_accession=uniprot_accession,
        uniref_id=uniref_id,
        uniref_type=_string(cluster.get("entryType")),
        name=_string(cluster.get("name")),
        updated=_string(cluster.get("updated")),
        member_count=_int(cluster.get("memberCount")),
        organism_count=_int(cluster.get("organismCount")),
        common_taxon_id=_string(common_taxon.get("taxonId")),
        common_taxon_name=_string(common_taxon.get("scientificName")),
        representative_accession=_first_string(representative.get("accessions")),
        representative_member_id=_string(representative.get("memberId")),
        representative_protein_name=_string(representative.get("proteinName")),
        representative_taxon_id=_string(representative.get("organismTaxId")),
        representative_length=_int(representative.get("sequenceLength")),
        seed_id=_string(cluster.get("seedId")),
    )


def render_uniref_tsv(rows: Iterable[UniRefMappingRow]) -> str:
    """Render UniRef mapping rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=UNIREF_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_uniref_json(rows: Iterable[UniRefMappingRow]) -> str:
    """Render UniRef mapping rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def _submit_mapping_job(
    client: httpx.Client,
    accessions: list[str],
    target: str,
) -> str:
    response = client.post(
        UNIPROT_ID_MAPPING_URL,
        data={
            "from": UNIPROT_ACCESSION_SOURCE,
            "to": target,
            "ids": ",".join(accessions),
        },
    )
    try:
        response.raise_for_status()
        payload = response.json()
    except (httpx.HTTPError, ValueError) as exc:
        raise UniProtIdMappingError("could not submit UniProt ID Mapping job") from exc
    if not isinstance(payload, Mapping):
        raise UniProtIdMappingError("UniProt ID Mapping submission was not a JSON object")
    job_id = _string(payload.get("jobId"))
    if not job_id:
        raise UniProtIdMappingError("UniProt ID Mapping submission had no jobId")
    return job_id


def _iter_mapping_results(
    client: httpx.Client,
    job_id: str,
    *,
    max_polls: int,
    poll_interval: float,
) -> Iterable[Mapping[str, Any]]:
    status_url = UNIPROT_ID_MAPPING_STATUS_URL.format(job_id=job_id)
    for _ in range(max_polls):
        response = client.get(status_url)
        try:
            response.raise_for_status()
            payload = response.json()
        except (httpx.HTTPError, ValueError) as exc:
            raise UniProtIdMappingError(
                f"could not fetch UniProt ID Mapping status {job_id}"
            ) from exc
        if not isinstance(payload, Mapping):
            raise UniProtIdMappingError(
                f"UniProt ID Mapping status {job_id} was not a JSON object"
            )

        messages = payload.get("messages")
        if isinstance(messages, list) and messages:
            raise UniProtIdMappingError("; ".join(str(message) for message in messages))

        failed_ids = payload.get("failedIds")
        if isinstance(failed_ids, list) and failed_ids:
            raise UniProtIdMappingError(
                "UniProt ID Mapping failed for "
                + ", ".join(str(failed_id) for failed_id in failed_ids)
            )

        results = payload.get("results")
        if isinstance(results, list):
            yield from _iter_mapping_result_pages(client, response, results)
            return
        time.sleep(poll_interval)

    raise UniProtIdMappingError(f"UniProt ID Mapping job {job_id} did not finish")


def _iter_mapping_result_pages(
    client: httpx.Client,
    response: httpx.Response,
    results: list[Any],
) -> Iterable[Mapping[str, Any]]:
    while True:
        for result in results:
            if isinstance(result, Mapping):
                yield result

        next_url = _next_link(response)
        if next_url is None:
            return

        response = client.get(next_url)
        try:
            response.raise_for_status()
            payload = response.json()
        except (httpx.HTTPError, ValueError) as exc:
            raise UniProtIdMappingError(
                f"could not fetch UniProt ID Mapping results page {next_url}"
            ) from exc
        if not isinstance(payload, Mapping):
            raise UniProtIdMappingError(
                f"UniProt ID Mapping results page {next_url} was not a JSON object"
            )
        raw_results = payload.get("results")
        if not isinstance(raw_results, list):
            raise UniProtIdMappingError(
                f"UniProt ID Mapping results page {next_url} had no results list"
            )
        results = raw_results


def _next_link(response: httpx.Response) -> str | None:
    next_link = response.links.get("next")
    if not isinstance(next_link, Mapping):
        return None
    next_url = next_link.get("url")
    return next_url if isinstance(next_url, str) and next_url else None


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _int(value: object) -> int | None:
    return value if type(value) is int else None


def _string(value: object) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, int):
        return str(value)
    return ""


def _first_string(value: object) -> str:
    if not isinstance(value, list):
        return ""
    for item in value:
        text = _string(item)
        if text:
            return text
    return ""
