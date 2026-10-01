from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO

from dufmech.rcsb import RcsbPdbRow
from dufmech.rcsb_snapshot import write_rcsb_snapshot
from dufmech.rcsb_snapshot_cli import (
    load_member_uniprot_accessions,
)
from dufmech.rcsb_snapshot_cli import (
    main as freeze_rcsb_snapshot,
)


def rcsb_row(pdb_id: str = "1A00") -> RcsbPdbRow:
    return RcsbPdbRow(
        uniprot_accession="P68871",
        pdb_id=pdb_id,
        entity_id="2",
        rcsb_id=f"{pdb_id}_2",
        experimental_method="X-ray",
        resolution=2.0,
        polymer_type="Protein",
        sequence_length=146,
        chain_ids=("B", "D"),
        taxon_id="9606",
        organism="Homo sapiens",
        entity_names=("Hemoglobin subunit beta",),
        reference_accessions=("P68871",),
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


def test_write_rcsb_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    manifest = write_rcsb_snapshot(
        [rcsb_row("1A01"), rcsb_row("1A00")],
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
        seed_snapshot_id="pfam-uniprot-uniref90-2026-10-01",
        limit_entities_per_accession=2,
    )

    json_path = tmp_path / "uniprot-rcsb-pdb-2026-10-01.json"
    tsv_path = tmp_path / "uniprot-rcsb-pdb-2026-10-01.tsv"
    manifest_path = tmp_path / "uniprot-rcsb-pdb-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "uniprot-rcsb-pdb-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
        "seed_snapshot_id": "pfam-uniprot-uniref90-2026-10-01",
    }
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["unique_pdb_entries"] == 2
    assert manifest["rows"]["by_experimental_method"] == {"X-ray": 2}
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
    assert [row["pdb_id"] for row in json_rows] == ["1A00", "1A01"]
    assert [row["chain_ids"] for row in tsv_rows] == ["B;D", "B;D"]


def test_freeze_rcsb_snapshot_cli_reads_saved_member_rows(
    tmp_path,
    monkeypatch,
    capsys,
) -> None:
    def fake_collect(accessions, **kwargs) -> list[RcsbPdbRow]:
        assert accessions == ["P68871"]
        assert kwargs["limit_entities_per_accession"] == 1
        return [rcsb_row()]

    monkeypatch.setattr(
        "dufmech.rcsb_snapshot_cli.collect_rcsb_snapshot_rows",
        fake_collect,
    )

    input_path = tmp_path / "pfam-uniprot-uniref90-2026-10-01.json"
    input_path.write_text(
        json.dumps([{"uniprot_accession": "P68871"}]),
        encoding="utf-8",
    )

    assert (
        freeze_rcsb_snapshot(
            [
                "--input-json",
                str(input_path),
                "--limit-entities-per-accession",
                "1",
                "--snapshot-date",
                "2026-10-01",
                "--out-dir",
                str(tmp_path / "worklists"),
            ]
        )
        == 0
    )

    assert "wrote uniprot-rcsb-pdb-2026-10-01 (1 rows)" in capsys.readouterr().out
    assert (
        tmp_path / "worklists" / "uniprot-rcsb-pdb-2026-10-01.manifest.json"
    ).is_file()
