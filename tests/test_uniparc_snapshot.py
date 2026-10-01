from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO

from dufmech.uniparc import UniParcMappingRow
from dufmech.uniparc_snapshot import write_uniparc_snapshot
from dufmech.uniparc_snapshot_cli import load_member_uniprot_accessions
from dufmech.uniparc_snapshot_cli import main as freeze_uniparc_snapshot


def uniparc_row(
    accession: str = "P75259",
    uniparc_id: str = "UPI000013A20F",
) -> UniParcMappingRow:
    return UniParcMappingRow(
        uniprot_accession=accession,
        uniparc_id=uniparc_id,
        cross_reference_count=181,
        sequence_length=163,
        molecular_weight=19116,
        crc64="0D8AF31CEC157FAD",
        md5="0BB3B8E600BB8B2AC3C92B70609AA020",
        uniprotkb_accessions=("B2BDZ4", "P75259"),
        common_taxon_ids=("2104",),
        common_taxon_names=("Mycoplasmoides pneumoniae",),
        common_taxon_top_levels=("cellular organisms",),
        interpro_ids=("IPR002862",),
        pfam_ids=("PF01519",),
        gene3d_ids=("G3DSA:6.10.250.40",),
        sequence_feature_count=2,
    )


def test_load_member_uniprot_accessions_uses_source_accessions() -> None:
    assert load_member_uniprot_accessions(
        [
            {
                "uniprot_accession": "B2BDZ4",
                "representative_accession": "P75259",
            },
            {"uniprot_accession": "B2BDZ3"},
            {
                "uniprot_accession": "B2BDZ4",
                "representative_accession": "P75259",
            },
            {"uniprot_accession": None},
            {},
        ]
    ) == ["B2BDZ4", "B2BDZ3"]


def test_write_uniparc_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    manifest = write_uniparc_snapshot(
        [
            uniparc_row("P75259", "UPI000013A20F"),
            uniparc_row("B2BDZ3", "UPI000013A20E"),
        ],
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
        seed_snapshot_id="pfam-uniprot-uniref90-2026-10-01",
        batch_size=50,
    )

    json_path = tmp_path / "uniprot-uniparc-2026-10-01.json"
    tsv_path = tmp_path / "uniprot-uniparc-2026-10-01.tsv"
    manifest_path = tmp_path / "uniprot-uniparc-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "uniprot-uniparc-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
        "seed_snapshot_id": "pfam-uniprot-uniref90-2026-10-01",
    }
    assert manifest["source"]["target"] == "UniParc"
    assert manifest["source"]["batch_size"] == 50
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["unique_uniparc_ids"] == 2
    assert manifest["rows"]["with_sequence_checksum"] == 2
    assert manifest["rows"]["by_common_taxon_top_level"] == {"cellular organisms": 2}
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
    assert [row["uniparc_id"] for row in json_rows] == [
        "UPI000013A20E",
        "UPI000013A20F",
    ]
    assert [row["pfam_ids"] for row in tsv_rows] == ["PF01519", "PF01519"]


def test_freeze_uniparc_snapshot_cli_reads_saved_member_rows(
    tmp_path,
    monkeypatch,
    capsys,
) -> None:
    def fake_collect(accessions, **kwargs) -> list[UniParcMappingRow]:
        assert accessions == ["B2BDZ3", "B2BDZ4"]
        assert kwargs["batch_size"] == 50
        return [uniparc_row("B2BDZ3")]

    monkeypatch.setattr(
        "dufmech.uniparc_snapshot_cli.collect_uniparc_snapshot_rows",
        fake_collect,
    )

    input_path = tmp_path / "pfam-uniprot-uniref90-2026-10-01.json"
    input_path.write_text(
        json.dumps(
            [
                {
                    "uniprot_accession": "B2BDZ3",
                    "representative_accession": "P75259",
                },
                {"uniprot_accession": "B2BDZ4"},
            ]
        ),
        encoding="utf-8",
    )

    assert (
        freeze_uniparc_snapshot(
            [
                "--input-json",
                str(input_path),
                "--batch-size",
                "50",
                "--snapshot-date",
                "2026-10-01",
                "--out-dir",
                str(tmp_path / "worklists"),
            ]
        )
        == 0
    )

    assert "wrote uniprot-uniparc-2026-10-01 (1 rows)" in (
        capsys.readouterr().out
    )
    assert (
        tmp_path
        / "worklists"
        / "uniprot-uniparc-2026-10-01.manifest.json"
    ).is_file()
