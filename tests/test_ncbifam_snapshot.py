from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO

from dufmech.ncbifam import NcbifamHitRow
from dufmech.ncbifam_snapshot import write_ncbifam_snapshot
from dufmech.ncbifam_snapshot_cli import main as freeze_ncbifam_snapshot
from tests.test_ncbifam import NCBIFAM_HEADER, ncbifam_line


def ncbifam_row(
    query_id: str = "P75259",
    *,
    ncbifam_accession: str = "NF002448",
) -> NcbifamHitRow:
    return NcbifamHitRow(
        query_id=query_id,
        ncbifam_accession=ncbifam_accession,
        source_accession="TIGR00001",
        model_name="UPF0134 protein family",
        product_name="UPF0134 protein",
        gene_symbol="upf0134",
        ec_numbers=("1.2.3.4",),
        go_terms=("GO:0003674",),
        query_start=39,
        query_end=154,
        e_value=1e-80,
        bitscore=250.5,
    )


def test_write_ncbifam_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    source_path = tmp_path / "ncbifam-hits.tsv"
    manifest = write_ncbifam_snapshot(
        [
            ncbifam_row("P75259"),
            ncbifam_row("B2BDZ3", ncbifam_accession="NF009946"),
        ],
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
        seed_snapshot_id="pfam-uniprot-uniref90-2026-10-01",
        hmm_hits_path=source_path,
    )

    json_path = tmp_path / "uniprot-ncbifam-2026-10-01.json"
    tsv_path = tmp_path / "uniprot-ncbifam-2026-10-01.tsv"
    manifest_path = tmp_path / "uniprot-ncbifam-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "uniprot-ncbifam-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
        "seed_snapshot_id": "pfam-uniprot-uniref90-2026-10-01",
    }
    assert manifest["source"]["hmm_hits_path"] == "ncbifam-hits.tsv"
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["unique_queries"] == 2
    assert manifest["rows"]["unique_ncbifam_accessions"] == 2
    assert manifest["rows"]["with_gene_symbol"] == 2
    assert manifest["rows"]["by_ncbifam_accession"] == {
        "NF002448": 1,
        "NF009946": 1,
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
    assert [row["query_id"] for row in json_rows] == ["B2BDZ3", "P75259"]
    assert [row["ncbifam_accession"] for row in tsv_rows] == ["NF009946", "NF002448"]


def test_freeze_ncbifam_snapshot_cli_reads_hmm_hit_table(
    tmp_path,
    capsys,
) -> None:
    input_path = tmp_path / "ncbifam-hits.tsv"
    input_path.write_text(
        f"{NCBIFAM_HEADER}\n{ncbifam_line()}\n",
        encoding="utf-8",
    )

    assert (
        freeze_ncbifam_snapshot(
            [
                "--hits-tsv",
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

    assert "wrote uniprot-ncbifam-2026-10-01 (1 rows)" in (
        capsys.readouterr().out
    )
    assert (
        tmp_path / "worklists" / "uniprot-ncbifam-2026-10-01.manifest.json"
    ).is_file()
