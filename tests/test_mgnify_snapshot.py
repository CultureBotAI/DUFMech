from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO

from dufmech.mgnify import MgnifyProteinRow
from dufmech.mgnify_snapshot import write_mgnify_snapshot
from dufmech.mgnify_snapshot_cli import main as freeze_mgnify_snapshot


def mgnify_row(mgyp: str = "MGYP000000000166") -> MgnifyProteinRow:
    return MgnifyProteinRow(
        pfam_id="PF01519",
        mgyp=mgyp,
        full_length=True,
        cluster_size=3,
        sequence_length=8,
        biome_ids=(132, 433),
        biome_names=(
            "root:Environmental:Aquatic:Marine",
            "root:Engineered:Wastewater",
        ),
        biome_counts=(2, 1),
        pfam_match_count=1,
        pfam_match_ranges=("2-7",),
    )


def test_write_mgnify_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    manifest = write_mgnify_snapshot(
        [mgnify_row("MGYP000000000617"), mgnify_row("MGYP000000000166")],
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
        seed_snapshot_id="interpro-pfam-duf-2026-10-01",
        limit_proteins_per_family=2,
    )

    json_path = tmp_path / "pfam-mgnify-proteins-2026-10-01.json"
    tsv_path = tmp_path / "pfam-mgnify-proteins-2026-10-01.tsv"
    manifest_path = tmp_path / "pfam-mgnify-proteins-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "pfam-mgnify-proteins-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
        "seed_snapshot_id": "interpro-pfam-duf-2026-10-01",
    }
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["unique_mgyp_accessions"] == 2
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
    assert [row["mgyp"] for row in json_rows] == [
        "MGYP000000000166",
        "MGYP000000000617",
    ]
    assert tsv_rows[0]["biome_names"] == (
        "root:Environmental:Aquatic:Marine;root:Engineered:Wastewater"
    )


def test_freeze_mgnify_snapshot_cli_reads_saved_worklist(
    tmp_path,
    monkeypatch,
    capsys,
) -> None:
    def fake_collect(pfam_ids, **kwargs) -> list[MgnifyProteinRow]:
        assert pfam_ids == ["PF01519"]
        assert kwargs["limit_proteins_per_family"] == 1
        return [mgnify_row()]

    monkeypatch.setattr(
        "dufmech.mgnify_snapshot_cli.collect_mgnify_snapshot_rows",
        fake_collect,
    )

    input_path = tmp_path / "interpro-pfam-duf-2026-10-01.json"
    input_path.write_text(json.dumps([{"pfam_id": "PF01519"}]), encoding="utf-8")

    assert (
        freeze_mgnify_snapshot(
            [
                "--input-json",
                str(input_path),
                "--limit-proteins-per-family",
                "1",
                "--snapshot-date",
                "2026-10-01",
                "--out-dir",
                str(tmp_path / "worklists"),
            ]
        )
        == 0
    )

    assert "wrote pfam-mgnify-proteins-2026-10-01 (1 rows)" in capsys.readouterr().out
    assert (
        tmp_path
        / "worklists"
        / "pfam-mgnify-proteins-2026-10-01.manifest.json"
    ).is_file()
