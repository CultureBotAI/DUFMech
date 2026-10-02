from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO

from dufmech.jgi_img import JgiImgNeighborRow
from dufmech.jgi_img_snapshot import write_jgi_img_snapshot
from dufmech.jgi_img_snapshot_cli import main as freeze_jgi_img_snapshot
from tests.test_jgi_img import JGI_IMG_HEADER, jgi_img_line


def jgi_img_row(
    query_id: str = "P75259",
    *,
    img_genome_id: str = "3300000123",
) -> JgiImgNeighborRow:
    return JgiImgNeighborRow(
        query_id=query_id,
        img_genome_id=img_genome_id,
        query_gene_oid="3300049500",
        neighbor_gene_oid="3300049538",
        neighbor_pfam="PF00005",
        scaffold_id="Ga0123456_101",
        neighbor_locus_tag="DUF_0001",
        neighbor_product="ABC transporter ATP-binding protein",
        query_neighbor_distance=2,
        query_neighbor_direction="downstream",
    )


def test_write_jgi_img_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    source_path = tmp_path / "img-gene-neighbors.tsv"
    manifest = write_jgi_img_snapshot(
        [
            jgi_img_row("P75259"),
            jgi_img_row("B2BDZ3", img_genome_id="3300000456"),
        ],
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
        seed_snapshot_id="pfam-uniprot-uniref90-2026-10-01",
        gene_neighbors_path=source_path,
    )

    json_path = tmp_path / "jgi-img-gene-neighborhoods-2026-10-01.json"
    tsv_path = tmp_path / "jgi-img-gene-neighborhoods-2026-10-01.tsv"
    manifest_path = tmp_path / "jgi-img-gene-neighborhoods-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "jgi-img-gene-neighborhoods-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
        "seed_snapshot_id": "pfam-uniprot-uniref90-2026-10-01",
    }
    assert manifest["source"]["gene_neighbors_path"] == "img-gene-neighbors.tsv"
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["unique_queries"] == 2
    assert manifest["rows"]["unique_img_genomes"] == 2
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


def test_freeze_jgi_img_snapshot_cli_reads_gene_neighborhood_table(
    tmp_path,
    capsys,
) -> None:
    input_path = tmp_path / "img-gene-neighbors.tsv"
    input_path.write_text(
        f"{JGI_IMG_HEADER}\n{jgi_img_line()}\n",
        encoding="utf-8",
    )

    assert (
        freeze_jgi_img_snapshot(
            [
                "--gene-neighbors-tsv",
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

    assert "wrote jgi-img-gene-neighborhoods-2026-10-01 (1 rows)" in (
        capsys.readouterr().out
    )
    assert (
        tmp_path
        / "worklists"
        / "jgi-img-gene-neighborhoods-2026-10-01.manifest.json"
    ).is_file()
