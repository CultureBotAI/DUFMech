"""Fetch STRING functional-association evidence for UniProt accessions."""

from __future__ import annotations

import csv
import io
import json
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass

import httpx

STRING_BASE_URL = "https://version-12-0.string-db.org"
STRING_API_URL = f"{STRING_BASE_URL}/api/tsv"
STRING_CALLER_IDENTITY = "dufmech"

STRING_MAPPING_FIELDNAMES = [
    "queryItem",
    "queryIndex",
    "stringId",
    "ncbiTaxonId",
    "taxonName",
    "preferredName",
    "annotation",
]
STRING_INTERACTION_FIELDNAMES = [
    "stringId_A",
    "stringId_B",
    "preferredName_A",
    "preferredName_B",
    "ncbiTaxonId",
    "score",
    "nscore",
    "fscore",
    "pscore",
    "ascore",
    "escore",
    "dscore",
    "tscore",
]

STRING_TSV_FIELDNAMES = [
    "uniprot_accession",
    "taxon_id",
    "string_id",
    "string_taxon_id",
    "taxon_name",
    "preferred_name",
    "annotation",
    "partner_string_id",
    "partner_preferred_name",
    "score",
    "neighborhood_score",
    "fusion_score",
    "cooccurrence_score",
    "coexpression_score",
    "experimental_score",
    "database_score",
    "textmining_score",
    "source_url",
]


class StringDbClientError(RuntimeError):
    """Raised when STRING returns an invalid or failing response."""


@dataclass(frozen=True)
class StringDbSeed:
    """One UniProt accession scoped to one NCBI taxon for STRING mapping."""

    uniprot_accession: str
    taxon_id: str

    @property
    def key(self) -> tuple[str, str]:
        return (self.uniprot_accession, self.taxon_id)


@dataclass(frozen=True)
class StringDbMappingRow:
    """One UniProt accession resolved to a STRING identifier."""

    uniprot_accession: str
    taxon_id: str
    string_id: str
    string_taxon_id: str
    taxon_name: str
    preferred_name: str
    annotation: str


@dataclass(frozen=True)
class StringDbInteractionRow:
    """One STRING interaction partner edge for a mapped UniProt accession."""

    uniprot_accession: str
    taxon_id: str
    string_id: str
    string_taxon_id: str
    taxon_name: str
    preferred_name: str
    annotation: str
    partner_string_id: str
    partner_preferred_name: str
    score: float | None
    neighborhood_score: float | None
    fusion_score: float | None
    cooccurrence_score: float | None
    coexpression_score: float | None
    experimental_score: float | None
    database_score: float | None
    textmining_score: float | None

    @property
    def source_url(self) -> str:
        return f"{STRING_BASE_URL}/network/{self.string_id}"

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["source_url"] = self.source_url
        return row


class StringDbClient:
    """Small client for STRING identifier mapping and interaction TSV APIs."""

    def __init__(
        self,
        *,
        timeout: float = 30.0,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self.timeout = timeout
        self.transport = transport

    def map_uniprot(self, seed: StringDbSeed) -> Iterable[Mapping[str, str]]:
        text = self._post_tsv(
            "get_string_ids",
            {
                "identifiers": seed.uniprot_accession,
                "species": seed.taxon_id,
                "echo_query": "1",
            },
            empty_on_404=True,
        )
        yield from parse_string_tsv(
            text,
            expected_fieldnames=STRING_MAPPING_FIELDNAMES,
            context=f"STRING mapping for {seed.uniprot_accession}/{seed.taxon_id}",
        )

    def interaction_partners(
        self,
        string_id: str,
        *,
        taxon_id: str,
        limit: int = 10,
        required_score: int = 400,
    ) -> Iterable[Mapping[str, str]]:
        text = self._post_tsv(
            "interaction_partners",
            {
                "identifiers": string_id,
                "species": taxon_id,
                "limit": str(limit),
                "required_score": str(required_score),
            },
            empty_on_404=True,
        )
        yield from parse_string_tsv(
            text,
            expected_fieldnames=STRING_INTERACTION_FIELDNAMES,
            context=f"STRING interaction partners for {string_id}",
        )

    def _post_tsv(
        self,
        method: str,
        data: Mapping[str, str],
        *,
        empty_on_404: bool = False,
    ) -> str:
        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=True,
            transport=self.transport,
        ) as client:
            response = client.post(
                f"{STRING_API_URL}/{method}",
                data={**data, "caller_identity": STRING_CALLER_IDENTITY},
            )
            if empty_on_404 and response.status_code == 404:
                return "\t".join(STRING_ERROR_FIELDNAMES) + "\n"
            if response.status_code == 400 and is_unknown_organism_tsv(response.text):
                return response.text
            try:
                response.raise_for_status()
            except httpx.HTTPError as exc:
                raise StringDbClientError(f"could not fetch STRING {method}") from exc
        return response.text


STRING_ERROR_FIELDNAMES = ["Error", "ErrorMessage"]
STRING_UNKNOWN_ORGANISM_ERROR = "unknown organism"


def collect_stringdb_rows(
    seeds: Iterable[StringDbSeed],
    client: StringDbClient,
    *,
    limit_partners_per_protein: int = 10,
    required_score: int = 400,
) -> list[StringDbInteractionRow]:
    """Collect STRING interaction partners for ordered, unique UniProt/taxon seeds."""

    rows: list[StringDbInteractionRow] = []
    seen_seeds: set[tuple[str, str]] = set()
    seen_edges: set[tuple[str, str, str]] = set()
    for seed in seeds:
        if not seed.uniprot_accession or not seed.taxon_id or seed.key in seen_seeds:
            continue
        seen_seeds.add(seed.key)
        for mapping_record in client.map_uniprot(seed):
            mapping = mapping_row_from_string_record(seed, mapping_record)
            if mapping is None:
                continue
            partners = client.interaction_partners(
                mapping.string_id,
                taxon_id=mapping.string_taxon_id or seed.taxon_id,
                limit=limit_partners_per_protein,
                required_score=required_score,
            )
            for partner_record in partners:
                row = row_from_string_interaction(mapping, partner_record)
                if row is None:
                    continue
                key = (row.uniprot_accession, row.string_id, row.partner_string_id)
                if key in seen_edges:
                    continue
                seen_edges.add(key)
                rows.append(row)

    return sorted(
        rows,
        key=lambda row: (
            row.uniprot_accession,
            row.string_id,
            row.partner_string_id,
        ),
    )


def parse_string_tsv(
    text: str,
    *,
    expected_fieldnames: list[str],
    context: str,
) -> list[Mapping[str, str]]:
    """Parse one STRING TSV response."""

    reader = csv.DictReader(io.StringIO(text), dialect="excel-tab")
    if reader.fieldnames == STRING_ERROR_FIELDNAMES:
        return []
    if reader.fieldnames != expected_fieldnames:
        raise StringDbClientError(f"{context} had unexpected TSV fieldnames")
    return [
        {key: value or "" for key, value in row.items() if key is not None}
        for row in reader
    ]


def is_unknown_organism_tsv(text: str) -> bool:
    """Return whether one STRING error TSV reports an unindexed organism."""

    reader = csv.DictReader(io.StringIO(text), dialect="excel-tab")
    if reader.fieldnames != STRING_ERROR_FIELDNAMES:
        return False
    return any(row.get("Error") == STRING_UNKNOWN_ORGANISM_ERROR for row in reader)


def mapping_row_from_string_record(
    seed: StringDbSeed,
    record: Mapping[str, str],
) -> StringDbMappingRow | None:
    """Return a normalized STRING mapping row, or ``None`` if malformed."""

    string_id = _string(record.get("stringId"))
    if not string_id:
        return None

    return StringDbMappingRow(
        uniprot_accession=seed.uniprot_accession,
        taxon_id=seed.taxon_id,
        string_id=string_id,
        string_taxon_id=_string(record.get("ncbiTaxonId")),
        taxon_name=_string(record.get("taxonName")),
        preferred_name=_string(record.get("preferredName")),
        annotation=_string(record.get("annotation")),
    )


def row_from_string_interaction(
    mapping: StringDbMappingRow,
    record: Mapping[str, str],
) -> StringDbInteractionRow | None:
    """Return a normalized STRING interaction partner row, or ``None`` if malformed."""

    string_id = _string(record.get("stringId_A"))
    partner_string_id = _string(record.get("stringId_B"))
    if not string_id or not partner_string_id:
        return None

    return StringDbInteractionRow(
        uniprot_accession=mapping.uniprot_accession,
        taxon_id=mapping.taxon_id,
        string_id=string_id,
        string_taxon_id=_string(record.get("ncbiTaxonId"))
        or mapping.string_taxon_id,
        taxon_name=mapping.taxon_name,
        preferred_name=_string(record.get("preferredName_A"))
        or mapping.preferred_name,
        annotation=mapping.annotation,
        partner_string_id=partner_string_id,
        partner_preferred_name=_string(record.get("preferredName_B")),
        score=_float(record.get("score")),
        neighborhood_score=_float(record.get("nscore")),
        fusion_score=_float(record.get("fscore")),
        cooccurrence_score=_float(record.get("pscore")),
        coexpression_score=_float(record.get("ascore")),
        experimental_score=_float(record.get("escore")),
        database_score=_float(record.get("dscore")),
        textmining_score=_float(record.get("tscore")),
    )


def render_stringdb_tsv(rows: Iterable[StringDbInteractionRow]) -> str:
    """Render STRING rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=STRING_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_stringdb_json(rows: Iterable[StringDbInteractionRow]) -> str:
    """Render STRING rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def _float(value: object) -> float | None:
    try:
        return float(value) if isinstance(value, str) and value else None
    except ValueError:
        return None


def _string(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""
