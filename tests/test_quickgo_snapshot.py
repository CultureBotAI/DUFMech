from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO

from dufmech.quickgo import QuickGoAnnotationRow
from dufmech.quickgo_snapshot import write_quickgo_snapshot
from dufmech.quickgo_snapshot_cli import (
    load_member_uniprot_accessions,
)
from dufmech.quickgo_snapshot_cli import (
    main as freeze_quickgo_snapshot,
)


def quickgo_row(annotation_id: str = "UniProtKB:P08159!1") -> QuickGoAnnotationRow:
    return QuickGoAnnotationRow(
        uniprot_accession="P08159",
        annotation_id=annotation_id,
        gene_product_id="UniProtKB:P08159",
        qualifier="enables",
        go_id="GO:0018530",
        go_name="oxidase activity",
        go_evidence="EXP",
        go_aspect="molecular_function",
        evidence_code="ECO:0000269",
        reference="PMID:2680607",
        with_from=("RHEA:10012",),
        taxon_id="29320",
        taxon_name="Arthrobacter nicotinovorans",
        assigned_by="UniProt",
        target_sets=("UniProt",),
        symbol="6-hdno",
        date="20260727",
        extensions="",
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


def test_write_quickgo_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    manifest = write_quickgo_snapshot(
        [
            quickgo_row("UniProtKB:P08159!2"),
            quickgo_row("UniProtKB:P08159!1"),
        ],
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
        seed_snapshot_id="pfam-uniprot-uniref90-2026-10-01",
        limit_annotations_per_accession=2,
    )

    json_path = tmp_path / "uniprot-quickgo-mf-2026-10-01.json"
    tsv_path = tmp_path / "uniprot-quickgo-mf-2026-10-01.tsv"
    manifest_path = tmp_path / "uniprot-quickgo-mf-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "uniprot-quickgo-mf-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
        "seed_snapshot_id": "pfam-uniprot-uniref90-2026-10-01",
    }
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["unique_go_terms"] == 1
    assert manifest["rows"]["by_evidence_code"] == {"ECO:0000269": 2}
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
    assert [row["annotation_id"] for row in json_rows] == [
        "UniProtKB:P08159!1",
        "UniProtKB:P08159!2",
    ]
    assert [row["annotation_id"] for row in tsv_rows] == [
        "UniProtKB:P08159!1",
        "UniProtKB:P08159!2",
    ]


def test_freeze_quickgo_snapshot_cli_reads_saved_member_rows(
    tmp_path,
    monkeypatch,
    capsys,
) -> None:
    def fake_collect(accessions, **kwargs) -> list[QuickGoAnnotationRow]:
        assert accessions == ["P08159"]
        assert kwargs["limit_annotations_per_accession"] == 1
        return [quickgo_row()]

    monkeypatch.setattr(
        "dufmech.quickgo_snapshot_cli.collect_quickgo_snapshot_rows",
        fake_collect,
    )

    input_path = tmp_path / "pfam-uniprot-uniref90-2026-10-01.json"
    input_path.write_text(
        json.dumps([{"uniprot_accession": "P08159"}]),
        encoding="utf-8",
    )

    assert (
        freeze_quickgo_snapshot(
            [
                "--input-json",
                str(input_path),
                "--limit-annotations-per-accession",
                "1",
                "--snapshot-date",
                "2026-10-01",
                "--out-dir",
                str(tmp_path / "worklists"),
            ]
        )
        == 0
    )

    assert "wrote uniprot-quickgo-mf-2026-10-01 (1 rows)" in capsys.readouterr().out
    assert (
        tmp_path / "worklists" / "uniprot-quickgo-mf-2026-10-01.manifest.json"
    ).is_file()
