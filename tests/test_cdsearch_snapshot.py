from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO

from dufmech.cdsearch import CdSearchDomainRow
from dufmech.cdsearch_snapshot import write_cdsearch_snapshot
from dufmech.cdsearch_snapshot_cli import load_member_uniprot_accessions
from dufmech.cdsearch_snapshot_cli import (
    main as freeze_cdsearch_snapshot,
)


def cdsearch_row(cdd_accession: str = "cd08925") -> CdSearchDomainRow:
    superfamily_accession = "" if cdd_accession.startswith("cl") else "cl21461"
    return CdSearchDomainRow(
        uniprot_accession="P68871",
        query_label="Q#1 - P68871[hemoglobin subunit beta [Homo sapiens]]",
        hit_type="specific",
        pssm_id="381262",
        start=8,
        end=146,
        e_value=7.88544e-87,
        bitscore=249.479,
        cdd_accession=cdd_accession,
        short_name="Hb-beta-like",
        incomplete="",
        superfamily_accession=superfamily_accession,
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


def test_write_cdsearch_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    manifest = write_cdsearch_snapshot(
        [
            cdsearch_row("cl21461"),
            cdsearch_row("cd08925"),
        ],
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
        seed_snapshot_id="pfam-uniprot-uniref90-2026-10-01",
        batch_size=5,
    )

    json_path = tmp_path / "uniprot-cdsearch-2026-10-01.json"
    tsv_path = tmp_path / "uniprot-cdsearch-2026-10-01.tsv"
    manifest_path = tmp_path / "uniprot-cdsearch-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "uniprot-cdsearch-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
        "seed_snapshot_id": "pfam-uniprot-uniref90-2026-10-01",
    }
    assert manifest["source"]["batch_size"] == 5
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["unique_cdd_accessions"] == 2
    assert manifest["rows"]["unique_superfamilies"] == 1
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
    assert [row["cdd_accession"] for row in json_rows] == ["cd08925", "cl21461"]
    assert [row["cdd_accession"] for row in tsv_rows] == ["cd08925", "cl21461"]


def test_freeze_cdsearch_snapshot_cli_reads_saved_member_rows(
    tmp_path,
    monkeypatch,
    capsys,
) -> None:
    def fake_collect(accessions, **kwargs) -> list[CdSearchDomainRow]:
        assert accessions == ["P68871"]
        assert kwargs["db"] == "cdd"
        assert kwargs["mode"] == "all"
        assert kwargs["batch_size"] == 3
        return [cdsearch_row()]

    monkeypatch.setattr(
        "dufmech.cdsearch_snapshot_cli.collect_cdsearch_snapshot_rows",
        fake_collect,
    )

    input_path = tmp_path / "pfam-uniprot-uniref90-2026-10-01.json"
    input_path.write_text(
        json.dumps([{"uniprot_accession": "P68871"}]),
        encoding="utf-8",
    )

    assert (
        freeze_cdsearch_snapshot(
            [
                "--input-json",
                str(input_path),
                "--batch-size",
                "3",
                "--snapshot-date",
                "2026-10-01",
                "--out-dir",
                str(tmp_path / "worklists"),
            ]
        )
        == 0
    )

    assert "wrote uniprot-cdsearch-2026-10-01 (1 rows)" in capsys.readouterr().out
    assert (
        tmp_path / "worklists" / "uniprot-cdsearch-2026-10-01.manifest.json"
    ).is_file()
