from __future__ import annotations

import csv
import json
from io import StringIO

import httpx

from dufmech.alphafold import (
    AlphaFoldClient,
    collect_alphafold_predictions,
    render_alphafold_json,
    render_alphafold_tsv,
    row_from_alphafold_prediction,
)


def alphafold_prediction(
    *,
    accession: str = "B2BDZ3",
    model_entity_id: str = "AF-B2BDZ3-F1",
) -> dict:
    return {
        "toolUsed": "AlphaFold Monomer v2.0 pipeline",
        "providerId": "GDM",
        "entityType": "protein",
        "modelEntityId": model_entity_id,
        "modelCreatedDate": "2022-06-01T00:00:00Z",
        "sequenceVersionDate": "2008-05-20T00:00:00Z",
        "globalMetricValue": 83.12,
        "fractionPlddtVeryLow": 0.105,
        "fractionPlddtLow": 0.22,
        "fractionPlddtConfident": 0.042,
        "fractionPlddtVeryHigh": 0.634,
        "latestVersion": 6,
        "allVersions": [3, 4, 5, 6],
        "sequenceStart": 1,
        "sequenceEnd": 191,
        "sequenceChecksum": "a4a46513b17e1b2c9d65664bc529db40",
        "isUniProtReviewed": False,
        "uniprotAccession": accession,
        "taxId": 2104,
        "organismScientificName": "Mycoplasmoides pneumoniae",
        "isUniProtReferenceProteome": True,
        "bcifUrl": (
            "https://alphafold.ebi.ac.uk/files/AF-B2BDZ3-F1-model_v6.bcif"
        ),
        "cifUrl": "https://alphafold.ebi.ac.uk/files/AF-B2BDZ3-F1-model_v6.cif",
        "pdbUrl": "https://alphafold.ebi.ac.uk/files/AF-B2BDZ3-F1-model_v6.pdb",
        "paeImageUrl": (
            "https://alphafold.ebi.ac.uk/files/"
            "AF-B2BDZ3-F1-predicted_aligned_error_v6.png"
        ),
        "msaUrl": "https://alphafold.ebi.ac.uk/files/msa/AF-B2BDZ3-F1-msa_v6.a3m",
        "plddtDocUrl": (
            "https://alphafold.ebi.ac.uk/files/AF-B2BDZ3-F1-confidence_v6.json"
        ),
        "paeDocUrl": (
            "https://alphafold.ebi.ac.uk/files/"
            "AF-B2BDZ3-F1-predicted_aligned_error_v6.json"
        ),
        "isComplex": False,
    }


def test_row_from_alphafold_prediction_normalizes_current_schema() -> None:
    row = row_from_alphafold_prediction("B2BDZ3", alphafold_prediction())

    assert row is not None
    assert row.uniprot_accession == "B2BDZ3"
    assert row.model_entity_id == "AF-B2BDZ3-F1"
    assert row.provider_id == "GDM"
    assert row.global_metric_value == 83.12
    assert row.fraction_plddt_very_high == 0.634
    assert row.latest_version == 6
    assert row.all_versions == (3, 4, 5, 6)
    assert row.taxon_id == "2104"
    assert row.is_uniprot_reviewed is False
    assert row.is_uniprot_reference_proteome is True
    assert row.pae_doc_url.endswith("predicted_aligned_error_v6.json")
    assert row.source_url.endswith("/AF-B2BDZ3-F1")


def test_row_from_alphafold_prediction_accepts_legacy_aliases() -> None:
    payload = alphafold_prediction()
    payload["entryId"] = payload.pop("modelEntityId")
    payload["uniprotStart"] = payload.pop("sequenceStart")
    payload["uniprotEnd"] = payload.pop("sequenceEnd")
    payload["isReviewed"] = payload.pop("isUniProtReviewed")
    payload["isReferenceProteome"] = payload.pop("isUniProtReferenceProteome")

    row = row_from_alphafold_prediction("B2BDZ3", payload)

    assert row is not None
    assert row.model_entity_id == "AF-B2BDZ3-F1"
    assert row.sequence_start == 1
    assert row.sequence_end == 191
    assert row.is_uniprot_reference_proteome is True


def test_alphafold_client_fetches_predictions_and_skips_404s() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/B2BDZ4"):
            return httpx.Response(404, json={"detail": "not found"})
        assert request.url.path.endswith("/B2BDZ3")
        return httpx.Response(200, json=[alphafold_prediction()])

    client = AlphaFoldClient(transport=httpx.MockTransport(handler))
    rows = collect_alphafold_predictions(["B2BDZ3", "B2BDZ4"], client)

    assert [(row.uniprot_accession, row.model_entity_id) for row in rows] == [
        ("B2BDZ3", "AF-B2BDZ3-F1")
    ]


def test_render_alphafold_tsv_and_json_are_stable() -> None:
    client = AlphaFoldClient(
        transport=httpx.MockTransport(
            lambda request: httpx.Response(
                200,
                json=[
                    alphafold_prediction(
                        accession=request.url.path.rsplit("/", 1)[-1],
                        model_entity_id=(
                            "AF-" + request.url.path.rsplit("/", 1)[-1] + "-F1"
                        ),
                    )
                ],
            )
        )
    )
    rows = collect_alphafold_predictions(["B2BDZ4", "B2BDZ3"], client)

    tsv = render_alphafold_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert [row["uniprot_accession"] for row in parsed] == ["B2BDZ3", "B2BDZ4"]
    assert parsed[0]["all_versions"] == "3;4;5;6"

    payload = json.loads(render_alphafold_json(rows))
    assert payload[0]["source_url"].endswith("/AF-B2BDZ3-F1")
