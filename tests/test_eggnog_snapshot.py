from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO

from dufmech.eggnog import EggNogAnnotationRow
from dufmech.eggnog_snapshot import write_eggnog_snapshot
from dufmech.eggnog_snapshot_cli import main as freeze_eggnog_snapshot
from tests.test_eggnog import EMAPPER_HEADER, emapper_line


def eggnog_row(query_id: str = "P75259") -> EggNogAnnotationRow:
    return EggNogAnnotationRow(
        query_id=query_id,
        seed_ortholog="1224.MPN139",
        seed_evalue="1e-80",
        seed_score="250.5",
        eggnog_ogs=("COG4004@1|root", "arCOG01234@2157|Archaea"),
        tax_ceiling="2157",
        farthest_donor_lineage="Archaea",
        cog_category="S",
        preferred_name="upf0134",
        go_terms=("GO:0003674", "GO:0008150"),
        ec_numbers=("1.2.3.4",),
        kegg_kos=("ko:K00001",),
        kegg_pathways=("map00010",),
        kegg_modules=("M00001",),
        kegg_reactions=("R00001",),
        kegg_rclasses=("RC00001",),
        brite_terms=("ko00001",),
        kegg_tcs=("1.A.1",),
        cazy_terms=("GH1",),
        bigg_reactions=("RXN-1",),
        pfams=("PF01519",),
        annotation_confidence="1111111111111111111111",
    )


def test_write_eggnog_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    source_path = tmp_path / "out.emapper.annotations"
    manifest = write_eggnog_snapshot(
        [
            eggnog_row("P75259"),
            eggnog_row("B2BDZ3"),
        ],
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
        seed_snapshot_id="pfam-uniprot-uniref90-2026-10-01",
        annotations_path=source_path,
    )

    json_path = tmp_path / "eggnog-mapper-2026-10-01.json"
    tsv_path = tmp_path / "eggnog-mapper-2026-10-01.tsv"
    manifest_path = tmp_path / "eggnog-mapper-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "eggnog-mapper-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
        "seed_snapshot_id": "pfam-uniprot-uniref90-2026-10-01",
    }
    assert manifest["source"]["annotations_path"] == "out.emapper.annotations"
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["with_eggnog_ogs"] == 2
    assert manifest["rows"]["by_cog_category"] == {"S": 2}
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
    assert [row["pfams"] for row in tsv_rows] == ["PF01519", "PF01519"]


def test_freeze_eggnog_snapshot_cli_reads_annotations(
    tmp_path,
    capsys,
) -> None:
    input_path = tmp_path / "out.emapper.annotations"
    input_path.write_text(
        f"{EMAPPER_HEADER}\n{emapper_line()}\n",
        encoding="utf-8",
    )

    assert (
        freeze_eggnog_snapshot(
            [
                "--annotations-tsv",
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

    assert "wrote eggnog-mapper-2026-10-01 (1 rows)" in (
        capsys.readouterr().out
    )
    assert (
        tmp_path
        / "worklists"
        / "eggnog-mapper-2026-10-01.manifest.json"
    ).is_file()
