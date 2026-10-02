from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO

from dufmech.scoring import UNKNOWN_CANDIDATE, FamilyScoreRow
from dufmech.scoring_cli import main as score_duf_puf
from dufmech.scoring_snapshot import write_score_snapshot


def score_row(pfam_id: str = "PF00001") -> FamilyScoreRow:
    return FamilyScoreRow(
        pfam_id=pfam_id,
        short_name="DUF1",
        seed_unknown_status=UNKNOWN_CANDIDATE,
        characterization_status=UNKNOWN_CANDIDATE,
        member_count=2,
        representative_count=1,
        known_evidence_count=0,
        partial_evidence_count=0,
        context_evidence_count=1,
        rhea_reaction_count=0,
        experimental_go_mf_count=0,
        specific_cdd_hit_count=0,
        quickgo_mf_count=0,
        cdd_superfamily_count=1,
        eggnog_function_count=0,
        cath_funfam_count=0,
        mgnify_protein_count=0,
        mgnify_full_length_count=0,
        mgnify_biome_count=0,
        rcsb_structure_count=0,
        pdbe_kb_annotation_count=0,
        alphafold_model_count=0,
        threedbeacons_model_count=0,
        string_edge_count=0,
        eggnog_ortholog_count=0,
        efi_gnt_neighbor_pfam_count=0,
        demotion_reasons=(),
        context_sources=("cdd_superfamily",),
        source_url="https://www.ebi.ac.uk/interpro/api/entry/pfam/PF00001",
    )


def test_write_score_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    manifest = write_score_snapshot(
        [score_row("PF00002"), score_row("PF00001")],
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
        input_snapshot_ids={
            "worklist": "interpro-pfam-duf-2026-10-01",
            "members": "pfam-uniprot-uniref90-2026-10-01",
        },
    )

    json_path = tmp_path / "duf-characterization-scores-2026-10-01.json"
    tsv_path = tmp_path / "duf-characterization-scores-2026-10-01.tsv"
    manifest_path = tmp_path / "duf-characterization-scores-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "duf-characterization-scores-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
        "input_snapshot_ids": {
            "members": "pfam-uniprot-uniref90-2026-10-01",
            "worklist": "interpro-pfam-duf-2026-10-01",
        },
    }
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["with_context_evidence"] == 2
    assert manifest["files"]["json"]["sha256"] == hashlib.sha256(
        json_path.read_bytes()
    ).hexdigest()
    assert manifest["files"]["tsv"]["sha256"] == hashlib.sha256(
        tsv_path.read_bytes()
    ).hexdigest()

    tsv_rows = list(
        csv.DictReader(StringIO(tsv_path.read_text(encoding="utf-8")), dialect="excel-tab")
    )
    assert [row["pfam_id"] for row in tsv_rows] == ["PF00001", "PF00002"]


def test_score_cli_reads_frozen_json_inputs(tmp_path, capsys) -> None:
    worklist_path = tmp_path / "interpro-pfam-duf-2026-10-01.json"
    worklist_path.write_text(
        json.dumps(
            [
                {
                    "pfam_id": "PF00001",
                    "short_name": "DUF1",
                    "unknown_status": UNKNOWN_CANDIDATE,
                    "source_url": (
                        "https://www.ebi.ac.uk/interpro/api/entry/pfam/PF00001"
                    ),
                }
            ]
        ),
        encoding="utf-8",
    )
    members_path = tmp_path / "pfam-uniprot-uniref90-2026-10-01.json"
    members_path.write_text(
        json.dumps([{"pfam_id": "PF00001", "uniprot_accession": "P11111"}]),
        encoding="utf-8",
    )
    rhea_path = tmp_path / "uniprot-rhea-2026-10-01.json"
    rhea_path.write_text(
        json.dumps([{"uniprot_accession": "P11111", "rhea_id": "RHEA:10012"}]),
        encoding="utf-8",
    )
    cath_path = tmp_path / "uniprot-cath-funfam-v4_4_0-2026-10-01.json"
    cath_path.write_text(
        json.dumps(
            [
                {
                    "uniprot_accession": "P11111",
                    "superfamily_id": "1.10.490.10",
                    "funfam_number": "1",
                }
            ]
        ),
        encoding="utf-8",
    )
    eggnog_path = tmp_path / "eggnog-mapper-2026-10-01.json"
    eggnog_path.write_text(
        json.dumps(
            [
                {
                    "query_id": "P11111",
                    "seed_ortholog": "1234.seed",
                    "ec_numbers": ["1.1.1.1"],
                }
            ]
        ),
        encoding="utf-8",
    )
    mgnify_path = tmp_path / "pfam-mgnify-proteins-2026-10-01.json"
    mgnify_path.write_text(
        json.dumps(
            [
                {
                    "pfam_id": "PF00001",
                    "mgyp": "MGYP000000000166",
                    "full_length": True,
                    "biome_names": ["root:Environmental:Aquatic:Marine"],
                }
            ]
        ),
        encoding="utf-8",
    )
    efi_gnt_path = tmp_path / "efi-gnt-pfam-neighbors-2026-10-01.json"
    efi_gnt_path.write_text(
        json.dumps(
            [
                {
                    "query_id": "P11111",
                    "neighbor_id": "Q11111",
                    "neighbor_pfam": "PF00005",
                }
            ]
        ),
        encoding="utf-8",
    )

    assert (
        score_duf_puf(
            [
                "--worklist-json",
                str(worklist_path),
                "--member-json",
                str(members_path),
                "--rhea-json",
                str(rhea_path),
                "--cath-json",
                str(cath_path),
                "--eggnog-json",
                str(eggnog_path),
                "--mgnify-json",
                str(mgnify_path),
                "--efi-gnt-json",
                str(efi_gnt_path),
                "--snapshot-date",
                "2026-10-01",
                "--out-dir",
                str(tmp_path / "worklists"),
            ]
        )
        == 0
    )

    assert "wrote duf-characterization-scores-2026-10-01 (1 rows)" in (
        capsys.readouterr().out
    )
    manifest_path = (
        tmp_path / "worklists" / "duf-characterization-scores-2026-10-01.manifest.json"
    )
    assert manifest_path.is_file()

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"]["input_snapshot_ids"]["eggnog"] == (
        "eggnog-mapper-2026-10-01"
    )
    assert manifest["snapshot"]["input_snapshot_ids"]["mgnify"] == (
        "pfam-mgnify-proteins-2026-10-01"
    )
    assert manifest["snapshot"]["input_snapshot_ids"]["efi_gnt"] == (
        "efi-gnt-pfam-neighbors-2026-10-01"
    )
