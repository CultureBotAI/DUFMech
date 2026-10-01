from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO

from dufmech.cath import CathFunFamRow
from dufmech.cath_snapshot import write_cath_snapshot
from dufmech.cath_snapshot_cli import load_member_uniprot_accessions
from dufmech.cath_snapshot_cli import main as freeze_cath_snapshot


def cath_row(member_id: str = "P68871/2-147") -> CathFunFamRow:
    return CathFunFamRow(
        uniprot_accession="P68871",
        cath_uniprot_accession="P68871",
        member_id=member_id,
        member_accession=member_id.split("/")[0],
        member_start=2,
        member_end=147,
        uniprot_start=None,
        superfamily_id="1.10.490.10",
        funfam_number="1",
        sequence_md5="209d686939d0b8d1ea089368150140e2",
        confidence="1",
        taxon_id="9606",
        species_name="Homo sapiens",
        taxon_division_id="5",
        taxon_division_name="Primates",
        gene_id="HBB_HUMAN",
        gene_name="HBB",
        description="Hemoglobin subunit beta",
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


def test_write_cath_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    manifest = write_cath_snapshot(
        [
            cath_row("P68873/2-147"),
            cath_row("P68871/2-147"),
        ],
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
        seed_snapshot_id="pfam-uniprot-uniref90-2026-10-01",
    )

    json_path = tmp_path / "uniprot-cath-funfam-v4_4_0-2026-10-01.json"
    tsv_path = tmp_path / "uniprot-cath-funfam-v4_4_0-2026-10-01.tsv"
    manifest_path = tmp_path / "uniprot-cath-funfam-v4_4_0-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "uniprot-cath-funfam-v4_4_0-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
        "seed_snapshot_id": "pfam-uniprot-uniref90-2026-10-01",
    }
    assert manifest["source"]["cath_version"] == "v4_4_0"
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["unique_funfams"] == 1
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
    assert [row["member_id"] for row in json_rows] == [
        "P68871/2-147",
        "P68873/2-147",
    ]
    assert [row["member_id"] for row in tsv_rows] == [
        "P68871/2-147",
        "P68873/2-147",
    ]


def test_freeze_cath_snapshot_cli_reads_saved_member_rows(
    tmp_path,
    monkeypatch,
    capsys,
) -> None:
    def fake_collect(accessions, **kwargs) -> list[CathFunFamRow]:
        assert accessions == ["P75259"]
        assert kwargs["client"].version == "v4_4_0"
        return [cath_row()]

    monkeypatch.setattr(
        "dufmech.cath_snapshot_cli.collect_cath_snapshot_rows",
        fake_collect,
    )

    input_path = tmp_path / "pfam-uniprot-uniref90-2026-10-01.json"
    input_path.write_text(
        json.dumps([{"uniprot_accession": "B2BDZ3", "representative_accession": "P75259"}]),
        encoding="utf-8",
    )

    assert (
        freeze_cath_snapshot(
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

    assert "wrote uniprot-cath-funfam-v4_4_0-2026-10-01 (1 rows)" in (
        capsys.readouterr().out
    )
    assert (
        tmp_path
        / "worklists"
        / "uniprot-cath-funfam-v4_4_0-2026-10-01.manifest.json"
    ).is_file()
