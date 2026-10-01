from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO

from dufmech.threedbeacons import ThreeDBeaconsStructureRow
from dufmech.threedbeacons_snapshot import write_threedbeacons_snapshot
from dufmech.threedbeacons_snapshot_cli import load_member_uniprot_accessions
from dufmech.threedbeacons_snapshot_cli import (
    main as freeze_threedbeacons_snapshot,
)


def threedbeacons_row(provider: str = "AlphaFold DB") -> ThreeDBeaconsStructureRow:
    return ThreeDBeaconsStructureRow(
        uniprot_accession="P75259",
        uniprot_id="Y139_MYCPN",
        uniprot_checksum="0D8AF31CEC157FAD",
        sequence_length=163,
        segment_start=52,
        segment_end=158,
        model_identifier=(
            "AF-P75259-F1"
            if provider == "AlphaFold DB"
            else "P75259_52-158:7n9f.1.9"
        ),
        model_category="AB-INITIO" if provider == "AlphaFold DB" else "TEMPLATE-BASED",
        provider=provider,
        model_format="MMCIF",
        model_type="" if provider == "AlphaFold DB" else "ATOMIC",
        model_url="https://alphafold.ebi.ac.uk/files/AF-P75259-F1-model_v6.cif",
        model_page_url="https://alphafold.ebi.ac.uk/entry/AF-P75259-F1",
        created="2025-08-01T00:00:00Z",
        sequence_identity=1.0,
        uniprot_start=1,
        uniprot_end=163,
        coverage=1.0,
        experimental_method="",
        resolution=None,
        confidence_type="pLDDT",
        confidence_version="",
        confidence_avg_local_score=83.88,
        oligomeric_state="MONOMER",
        preferred_assembly_id="",
        polymer_identifiers=("UNIPROT:P75259",),
        non_polymer_identifiers=(),
    )


def test_load_member_uniprot_accessions_prefers_representatives() -> None:
    assert load_member_uniprot_accessions(
        [
            {
                "uniprot_accession": "B2BDZ4",
                "representative_accession": "P75259",
            },
            {"uniprot_accession": "B2BDZ3"},
            {
                "uniprot_accession": "A0A000",
                "representative_accession": "P75259",
            },
            {"uniprot_accession": None},
            {},
        ]
    ) == ["P75259", "B2BDZ3"]


def test_write_threedbeacons_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    manifest = write_threedbeacons_snapshot(
        [
            threedbeacons_row("SWISS-MODEL"),
            threedbeacons_row("AlphaFold DB"),
        ],
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
        seed_snapshot_id="pfam-uniprot-uniref90-2026-10-01",
    )

    json_path = tmp_path / "uniprot-3dbeacons-2026-10-01.json"
    tsv_path = tmp_path / "uniprot-3dbeacons-2026-10-01.tsv"
    manifest_path = tmp_path / "uniprot-3dbeacons-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "uniprot-3dbeacons-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
        "seed_snapshot_id": "pfam-uniprot-uniref90-2026-10-01",
    }
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["unique_models"] == 2
    assert manifest["rows"]["by_provider"] == {
        "AlphaFold DB": 1,
        "SWISS-MODEL": 1,
    }
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
    assert [row["provider"] for row in json_rows] == [
        "AlphaFold DB",
        "SWISS-MODEL",
    ]
    assert [row["provider"] for row in tsv_rows] == [
        "AlphaFold DB",
        "SWISS-MODEL",
    ]


def test_freeze_threedbeacons_snapshot_cli_reads_saved_member_rows(
    tmp_path,
    monkeypatch,
    capsys,
) -> None:
    def fake_collect(accessions) -> list[ThreeDBeaconsStructureRow]:
        assert accessions == ["P75259"]
        return [threedbeacons_row()]

    monkeypatch.setattr(
        "dufmech.threedbeacons_snapshot_cli.collect_threedbeacons_snapshot_rows",
        fake_collect,
    )

    input_path = tmp_path / "pfam-uniprot-uniref90-2026-10-01.json"
    input_path.write_text(
        json.dumps([{"uniprot_accession": "B2BDZ3", "representative_accession": "P75259"}]),
        encoding="utf-8",
    )

    assert (
        freeze_threedbeacons_snapshot(
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

    assert "wrote uniprot-3dbeacons-2026-10-01 (1 rows)" in capsys.readouterr().out
    assert (
        tmp_path / "worklists" / "uniprot-3dbeacons-2026-10-01.manifest.json"
    ).is_file()
