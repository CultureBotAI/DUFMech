from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO

from dufmech.alphafold import AlphaFoldPredictionRow
from dufmech.alphafold_snapshot import write_alphafold_snapshot
from dufmech.alphafold_snapshot_cli import (
    load_member_uniprot_accessions,
)
from dufmech.alphafold_snapshot_cli import (
    main as freeze_alphafold_snapshot,
)


def alphafold_row(accession: str = "B2BDZ3") -> AlphaFoldPredictionRow:
    return AlphaFoldPredictionRow(
        uniprot_accession=accession,
        model_entity_id=f"AF-{accession}-F1",
        provider_id="GDM",
        tool_used="AlphaFold Monomer v2.0 pipeline",
        entity_type="protein",
        is_complex=False,
        sequence_start=1,
        sequence_end=191,
        global_metric_value=83.12,
        fraction_plddt_very_low=0.105,
        fraction_plddt_low=0.22,
        fraction_plddt_confident=0.042,
        fraction_plddt_very_high=0.634,
        latest_version=6,
        all_versions=(3, 4, 5, 6),
        model_created_date="2022-06-01T00:00:00Z",
        sequence_version_date="2008-05-20T00:00:00Z",
        sequence_checksum="a4a46513b17e1b2c9d65664bc529db40",
        taxon_id="2104",
        organism="Mycoplasmoides pneumoniae",
        is_uniprot_reviewed=False,
        is_uniprot_reference_proteome=True,
        pdb_url=f"https://alphafold.ebi.ac.uk/files/AF-{accession}-F1-model_v6.pdb",
        cif_url=f"https://alphafold.ebi.ac.uk/files/AF-{accession}-F1-model_v6.cif",
        bcif_url=f"https://alphafold.ebi.ac.uk/files/AF-{accession}-F1-model_v6.bcif",
        pae_doc_url=(
            f"https://alphafold.ebi.ac.uk/files/"
            f"AF-{accession}-F1-predicted_aligned_error_v6.json"
        ),
        plddt_doc_url=(
            f"https://alphafold.ebi.ac.uk/files/AF-{accession}-F1-confidence_v6.json"
        ),
        pae_image_url=(
            f"https://alphafold.ebi.ac.uk/files/"
            f"AF-{accession}-F1-predicted_aligned_error_v6.png"
        ),
        msa_url=f"https://alphafold.ebi.ac.uk/files/msa/AF-{accession}-F1-msa_v6.a3m",
    )


def test_load_member_uniprot_accessions_preserves_first_seen_order() -> None:
    assert load_member_uniprot_accessions(
        [
            {"uniprot_accession": "B2BDZ4"},
            {"uniprot_accession": "B2BDZ3"},
            {"uniprot_accession": "B2BDZ4"},
            {"uniprot_accession": None},
            {},
        ]
    ) == ["B2BDZ4", "B2BDZ3"]


def test_write_alphafold_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    manifest = write_alphafold_snapshot(
        [alphafold_row("B2BDZ4"), alphafold_row("B2BDZ3")],
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
        seed_snapshot_id="pfam-uniprot-uniref90-2026-10-01",
    )

    json_path = tmp_path / "uniprot-alphafold-2026-10-01.json"
    tsv_path = tmp_path / "uniprot-alphafold-2026-10-01.tsv"
    manifest_path = tmp_path / "uniprot-alphafold-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "uniprot-alphafold-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
        "seed_snapshot_id": "pfam-uniprot-uniref90-2026-10-01",
    }
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["unique_uniprot_accessions"] == 2
    assert manifest["rows"]["by_provider"] == {"GDM": 2}
    assert manifest["files"]["json"]["sha256"] == hashlib.sha256(
        json_path.read_bytes()
    ).hexdigest()
    assert manifest["files"]["tsv"]["sha256"] == hashlib.sha256(
        tsv_path.read_bytes()
    ).hexdigest()

    json_rows = json.loads(json_path.read_text(encoding="utf-8"))
    tsv_rows = list(
        csv.DictReader(StringIO(tsv_path.read_text(encoding="utf-8")), dialect="excel-tab")
    )
    assert [row["uniprot_accession"] for row in json_rows] == ["B2BDZ3", "B2BDZ4"]
    assert [row["all_versions"] for row in tsv_rows] == ["3;4;5;6", "3;4;5;6"]


def test_freeze_alphafold_snapshot_cli_reads_saved_member_rows(
    tmp_path,
    monkeypatch,
    capsys,
) -> None:
    def fake_collect(accessions) -> list[AlphaFoldPredictionRow]:
        assert accessions == ["B2BDZ3"]
        return [alphafold_row()]

    monkeypatch.setattr(
        "dufmech.alphafold_snapshot_cli.collect_alphafold_snapshot_rows",
        fake_collect,
    )

    input_path = tmp_path / "pfam-uniprot-uniref90-2026-10-01.json"
    input_path.write_text(
        json.dumps([{"uniprot_accession": "B2BDZ3"}]),
        encoding="utf-8",
    )

    assert (
        freeze_alphafold_snapshot(
            [
                "--input-json",
                str(input_path),
                "--snapshot-date",
                "2026-10-01",
                "--out-dir",
                str(tmp_path / "worklists"),
            ]
        )
        == 0
    )

    assert "wrote uniprot-alphafold-2026-10-01 (1 rows)" in capsys.readouterr().out
    assert (
        tmp_path
        / "worklists"
        / "uniprot-alphafold-2026-10-01.manifest.json"
    ).is_file()
