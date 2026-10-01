from __future__ import annotations

import csv
import json
from io import StringIO

from dufmech.scoring import (
    KNOWN_HISTORICAL_DUF,
    PARTIALLY_CHARACTERIZED,
    UNKNOWN_CANDIDATE,
    EvidenceBundle,
    render_scores_json,
    render_scores_tsv,
    score_families,
)


def family(pfam_id: str, status: str = UNKNOWN_CANDIDATE) -> dict:
    return {
        "pfam_id": pfam_id,
        "short_name": pfam_id.replace("PF", "DUF"),
        "unknown_status": status,
        "source_url": f"https://www.ebi.ac.uk/interpro/api/entry/pfam/{pfam_id}",
    }


def member(pfam_id: str, accession: str, representative: str = "") -> dict:
    return {
        "pfam_id": pfam_id,
        "uniprot_accession": accession,
        "representative_accession": representative,
    }


def test_score_families_demotes_known_partial_and_contextual_families() -> None:
    rows = score_families(
        [
            family("PF00001"),
            family("PF00002"),
            family("PF00003", KNOWN_HISTORICAL_DUF),
        ],
        member_rows=[
            member("PF00001", "P11111", "R11111"),
            member("PF00001", "P22222", "R11111"),
            member("PF00002", "P33333"),
        ],
        evidence=EvidenceBundle(
            rhea=({"uniprot_accession": "P11111", "rhea_id": "RHEA:10012"},),
            quickgo=(
                {
                    "uniprot_accession": "P11111",
                    "go_id": "GO:0003824",
                    "go_evidence": "EXP",
                },
                {
                    "uniprot_accession": "P33333",
                    "go_id": "GO:0016491",
                    "go_evidence": "IEA",
                },
            ),
            cdsearch=(
                {
                    "uniprot_accession": "P33333",
                    "hit_type": "specific",
                    "cdd_accession": "cd08925",
                },
                {
                    "uniprot_accession": "P33333",
                    "hit_type": "superfamily",
                    "cdd_accession": "cl21461",
                },
            ),
            alphafold=(
                {"uniprot_accession": "R11111", "model_identifier": "AF-R11111-F1"},
            ),
            cath=(
                {
                    "uniprot_accession": "P33333",
                    "superfamily_id": "1.10.490.10",
                    "funfam_number": "1",
                },
                {
                    "uniprot_accession": "P33333",
                    "superfamily_id": "1.10.490.10",
                    "funfam_number": "1",
                },
            ),
            stringdb=(
                {
                    "uniprot_accession": "P33333",
                    "partner_string_id": "1234.partner",
                },
            ),
        ),
    )

    by_pfam = {row.pfam_id: row for row in rows}
    assert by_pfam["PF00001"].characterization_status == KNOWN_HISTORICAL_DUF
    assert by_pfam["PF00001"].known_evidence_count == 2
    assert by_pfam["PF00001"].member_count == 2
    assert by_pfam["PF00001"].representative_count == 1
    assert by_pfam["PF00001"].alphafold_model_count == 1
    assert by_pfam["PF00001"].demotion_reasons == (
        "has_rhea_reaction",
        "has_experimental_go_molecular_function",
    )

    assert by_pfam["PF00002"].characterization_status == PARTIALLY_CHARACTERIZED
    assert by_pfam["PF00002"].partial_evidence_count == 2
    assert by_pfam["PF00002"].context_evidence_count == 3
    assert by_pfam["PF00002"].cdd_superfamily_count == 1
    assert by_pfam["PF00002"].cath_funfam_count == 1
    assert by_pfam["PF00002"].string_edge_count == 1
    assert by_pfam["PF00002"].context_sources == (
        "cdd_superfamily",
        "cath_gene3d",
        "string",
    )

    assert by_pfam["PF00003"].characterization_status == KNOWN_HISTORICAL_DUF
    assert by_pfam["PF00003"].demotion_reasons == (
        "historical_interpro_annotation",
    )


def test_render_scores_tsv_and_json_are_stable() -> None:
    rows = score_families(
        [family("PF00002"), family("PF00001")],
        member_rows=[member("PF00001", "P11111")],
        evidence=EvidenceBundle(
            rhea=({"uniprot_accession": "P11111", "rhea_id": "RHEA:10012"},),
        ),
    )

    tsv = render_scores_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert [row["pfam_id"] for row in parsed] == ["PF00001", "PF00002"]
    assert parsed[0]["demotion_reasons"] == "has_rhea_reaction"

    payload = json.loads(render_scores_json(rows))
    assert payload[0]["pfam_id"] == "PF00001"
