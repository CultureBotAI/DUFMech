"""Fetch AlphaFold DB prediction metadata for UniProt accessions."""

from __future__ import annotations

import csv
import io
import json
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from typing import Any

import httpx

ALPHAFOLD_PREDICTION_URL = "https://alphafold.ebi.ac.uk/api/prediction/{accession}"

ALPHAFOLD_TSV_FIELDNAMES = [
    "uniprot_accession",
    "model_entity_id",
    "provider_id",
    "tool_used",
    "entity_type",
    "is_complex",
    "sequence_start",
    "sequence_end",
    "global_metric_value",
    "fraction_plddt_very_low",
    "fraction_plddt_low",
    "fraction_plddt_confident",
    "fraction_plddt_very_high",
    "latest_version",
    "all_versions",
    "model_created_date",
    "sequence_version_date",
    "sequence_checksum",
    "taxon_id",
    "organism",
    "is_uniprot_reviewed",
    "is_uniprot_reference_proteome",
    "pdb_url",
    "cif_url",
    "bcif_url",
    "pae_doc_url",
    "plddt_doc_url",
    "pae_image_url",
    "msa_url",
    "source_url",
]


class AlphaFoldClientError(RuntimeError):
    """Raised when AlphaFold DB returns an invalid or failing response."""


@dataclass(frozen=True)
class AlphaFoldPredictionRow:
    """One AlphaFold DB prediction for a UniProt accession."""

    uniprot_accession: str
    model_entity_id: str
    provider_id: str
    tool_used: str
    entity_type: str
    is_complex: bool | None
    sequence_start: int | None
    sequence_end: int | None
    global_metric_value: float | None
    fraction_plddt_very_low: float | None
    fraction_plddt_low: float | None
    fraction_plddt_confident: float | None
    fraction_plddt_very_high: float | None
    latest_version: int | None
    all_versions: tuple[int, ...]
    model_created_date: str
    sequence_version_date: str
    sequence_checksum: str
    taxon_id: str
    organism: str
    is_uniprot_reviewed: bool | None
    is_uniprot_reference_proteome: bool | None
    pdb_url: str
    cif_url: str
    bcif_url: str
    pae_doc_url: str
    plddt_doc_url: str
    pae_image_url: str
    msa_url: str

    @property
    def source_url(self) -> str:
        return f"https://alphafold.ebi.ac.uk/entry/{self.model_entity_id}"

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["all_versions"] = ";".join(str(version) for version in self.all_versions)
        row["source_url"] = self.source_url
        return row


class AlphaFoldClient:
    """Small client for AlphaFold DB prediction metadata."""

    def __init__(
        self,
        *,
        timeout: float = 30.0,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self.timeout = timeout
        self.transport = transport

    def iter_predictions(
        self,
        accession: str,
    ) -> Iterable[Mapping[str, Any]]:
        url = ALPHAFOLD_PREDICTION_URL.format(accession=accession)
        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=True,
            transport=self.transport,
        ) as client:
            response = client.get(url)
            if response.status_code == 404:
                return
            try:
                response.raise_for_status()
                payload = response.json()
            except (httpx.HTTPError, ValueError) as exc:
                raise AlphaFoldClientError(
                    f"could not fetch AlphaFold DB predictions for {accession}"
                ) from exc
            if not isinstance(payload, list):
                raise AlphaFoldClientError(
                    f"AlphaFold DB predictions for {accession} were not a JSON list"
                )
            for prediction in payload:
                if isinstance(prediction, Mapping):
                    yield prediction


def collect_alphafold_predictions(
    accessions: Iterable[str],
    client: AlphaFoldClient,
) -> list[AlphaFoldPredictionRow]:
    """Collect AlphaFold DB predictions for ordered, unique UniProt accessions."""

    rows: list[AlphaFoldPredictionRow] = []
    seen_accessions: set[str] = set()
    seen_predictions: set[tuple[str, str]] = set()
    for accession in accessions:
        if not accession or accession in seen_accessions:
            continue
        seen_accessions.add(accession)
        for prediction in client.iter_predictions(accession):
            row = row_from_alphafold_prediction(accession, prediction)
            if row is None:
                continue
            key = (row.uniprot_accession, row.model_entity_id)
            if key in seen_predictions:
                continue
            seen_predictions.add(key)
            rows.append(row)
    return sorted(rows, key=lambda row: (row.uniprot_accession, row.model_entity_id))


def row_from_alphafold_prediction(
    accession: str,
    prediction: Mapping[str, Any],
) -> AlphaFoldPredictionRow | None:
    """Return normalized AlphaFold DB metadata, or ``None`` if malformed."""

    model_entity_id = _string(prediction.get("modelEntityId")) or _string(
        prediction.get("entryId")
    )
    uniprot_accession = _string(prediction.get("uniprotAccession")) or accession
    if not model_entity_id or not uniprot_accession:
        return None

    return AlphaFoldPredictionRow(
        uniprot_accession=uniprot_accession,
        model_entity_id=model_entity_id,
        provider_id=_string(prediction.get("providerId")),
        tool_used=_string(prediction.get("toolUsed")),
        entity_type=_string(prediction.get("entityType")),
        is_complex=_bool(prediction.get("isComplex")),
        sequence_start=_int(prediction.get("sequenceStart"))
        or _int(prediction.get("uniprotStart")),
        sequence_end=_int(prediction.get("sequenceEnd"))
        or _int(prediction.get("uniprotEnd")),
        global_metric_value=_float(prediction.get("globalMetricValue")),
        fraction_plddt_very_low=_float(prediction.get("fractionPlddtVeryLow")),
        fraction_plddt_low=_float(prediction.get("fractionPlddtLow")),
        fraction_plddt_confident=_float(prediction.get("fractionPlddtConfident")),
        fraction_plddt_very_high=_float(prediction.get("fractionPlddtVeryHigh")),
        latest_version=_int(prediction.get("latestVersion")),
        all_versions=_int_tuple(prediction.get("allVersions")),
        model_created_date=_string(prediction.get("modelCreatedDate")),
        sequence_version_date=_string(prediction.get("sequenceVersionDate")),
        sequence_checksum=_string(prediction.get("sequenceChecksum")),
        taxon_id=_string(prediction.get("taxId")),
        organism=_string(prediction.get("organismScientificName")),
        is_uniprot_reviewed=_bool(
            prediction.get("isUniProtReviewed"),
            prediction.get("isReviewed"),
        ),
        is_uniprot_reference_proteome=_bool(
            prediction.get("isUniProtReferenceProteome"),
            prediction.get("isReferenceProteome"),
        ),
        pdb_url=_string(prediction.get("pdbUrl")),
        cif_url=_string(prediction.get("cifUrl")),
        bcif_url=_string(prediction.get("bcifUrl")),
        pae_doc_url=_string(prediction.get("paeDocUrl")),
        plddt_doc_url=_string(prediction.get("plddtDocUrl")),
        pae_image_url=_string(prediction.get("paeImageUrl")),
        msa_url=_string(prediction.get("msaUrl")),
    )


def render_alphafold_tsv(rows: Iterable[AlphaFoldPredictionRow]) -> str:
    """Render AlphaFold DB rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=ALPHAFOLD_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_alphafold_json(rows: Iterable[AlphaFoldPredictionRow]) -> str:
    """Render AlphaFold DB rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def _bool(*values: object) -> bool | None:
    for value in values:
        if type(value) is bool:
            return value
    return None


def _float(value: object) -> float | None:
    if type(value) in (float, int):
        return float(value)
    return None


def _int(value: object) -> int | None:
    return value if type(value) is int else None


def _int_tuple(value: object) -> tuple[int, ...]:
    if not isinstance(value, list):
        return ()
    return tuple(item for item in value if type(item) is int)


def _string(value: object) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, int):
        return str(value)
    return ""
