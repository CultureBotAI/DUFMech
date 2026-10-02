from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO

from dufmech.efi_gnt import EfiGntNeighborRow
from dufmech.efi_gnt_snapshot import write_efi_gnt_snapshot
from dufmech.efi_gnt_snapshot_cli import main as freeze_efi_gnt_snapshot
from tests.test_efi_gnt import EFI_GNT_HEADER, efi_gnt_line


def efi_gnt_row(
    query_id: str = "P75259",
    *,
    ssn_query_cluster_number: str = "1",
) -> EfiGntNeighborRow:
    return EfiGntNeighborRow(
        query_id=query_id,
        neighbor_id="Q11111",
        neighbor_pfam="PF00005",
        ssn_query_cluster_number=ssn_query_cluster_number,
        ssn_query_cluster_color="#1f77b4",
        query_neighbor_distance=2,
        query_neighbor_direction="same",
    )


def test_write_efi_gnt_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    source_path = tmp_path / "pfam-neighbors.tsv"
    manifest = write_efi_gnt_snapshot(
        [
            efi_gnt_row("P75259"),
            efi_gnt_row("B2BDZ3", ssn_query_cluster_number=""),
        ],
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
        seed_snapshot_id="pfam-uniprot-uniref90-2026-10-01",
        pfam_neighbors_path=source_path,
    )

    json_path = tmp_path / "efi-gnt-pfam-neighbors-2026-10-01.json"
    tsv_path = tmp_path / "efi-gnt-pfam-neighbors-2026-10-01.tsv"
    manifest_path = tmp_path / "efi-gnt-pfam-neighbors-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "efi-gnt-pfam-neighbors-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
        "seed_snapshot_id": "pfam-uniprot-uniref90-2026-10-01",
    }
    assert manifest["source"]["pfam_neighbors_path"] == "pfam-neighbors.tsv"
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["unique_queries"] == 2
    assert manifest["rows"]["unique_ssn_query_clusters"] == 1
    assert manifest["rows"]["by_neighbor_pfam"] == {"PF00005": 2}
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
    assert [row["query_id"] for row in json_rows] == ["B2BDZ3", "P75259"]
    assert [row["neighbor_pfam"] for row in tsv_rows] == ["PF00005", "PF00005"]


def test_freeze_efi_gnt_snapshot_cli_reads_pfam_neighbor_table(
    tmp_path,
    capsys,
) -> None:
    input_path = tmp_path / "pfam-neighbors.tsv"
    input_path.write_text(
        f"{EFI_GNT_HEADER}\n{efi_gnt_line()}\n",
        encoding="utf-8",
    )

    assert (
        freeze_efi_gnt_snapshot(
            [
                "--pfam-neighbors-tsv",
                str(input_path),
                "--seed-snapshot-id",
                "pfam-uniprot-uniref90-2026-10-01",
                "--snapshot-date",
                "2026-10-01",
                "--out-dir",
                str(tmp_path / "worklists"),
            ]
        )
        == 0
    )

    assert "wrote efi-gnt-pfam-neighbors-2026-10-01 (1 rows)" in (
        capsys.readouterr().out
    )
    assert (
        tmp_path
        / "worklists"
        / "efi-gnt-pfam-neighbors-2026-10-01.manifest.json"
    ).is_file()
