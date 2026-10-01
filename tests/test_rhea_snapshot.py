from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO

from dufmech.rhea import RheaReactionRow
from dufmech.rhea_snapshot import write_rhea_snapshot
from dufmech.rhea_snapshot_cli import (
    load_member_uniprot_accessions,
)
from dufmech.rhea_snapshot_cli import (
    main as freeze_rhea_snapshot,
)


def rhea_row(rhea_id: str = "RHEA:10012") -> RheaReactionRow:
    return RheaReactionRow(
        uniprot_accession="P08159",
        rhea_id=rhea_id,
        equation="A + B = C",
        chebi_ids=("CHEBI:1", "CHEBI:2"),
        ec_numbers=("EC:1.5.3.6",),
        go_terms=("GO:0018530 activity",),
        pubmed_ids=("16095622",),
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


def test_write_rhea_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    manifest = write_rhea_snapshot(
        [rhea_row("RHEA:46988"), rhea_row("RHEA:10012")],
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
        seed_snapshot_id="pfam-uniprot-uniref90-2026-10-01",
        limit_reactions_per_accession=2,
    )

    json_path = tmp_path / "uniprot-rhea-2026-10-01.json"
    tsv_path = tmp_path / "uniprot-rhea-2026-10-01.tsv"
    manifest_path = tmp_path / "uniprot-rhea-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "uniprot-rhea-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
        "seed_snapshot_id": "pfam-uniprot-uniref90-2026-10-01",
    }
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["unique_rhea_reactions"] == 2
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
    assert [row["rhea_id"] for row in json_rows] == ["RHEA:10012", "RHEA:46988"]
    assert [row["rhea_id"] for row in tsv_rows] == ["RHEA:10012", "RHEA:46988"]


def test_freeze_rhea_snapshot_cli_reads_saved_member_rows(
    tmp_path,
    monkeypatch,
    capsys,
) -> None:
    def fake_collect(accessions, **kwargs) -> list[RheaReactionRow]:
        assert accessions == ["P08159"]
        assert kwargs["limit_reactions_per_accession"] == 1
        return [rhea_row()]

    monkeypatch.setattr(
        "dufmech.rhea_snapshot_cli.collect_rhea_snapshot_rows",
        fake_collect,
    )

    input_path = tmp_path / "pfam-uniprot-uniref90-2026-10-01.json"
    input_path.write_text(
        json.dumps([{"uniprot_accession": "P08159"}]),
        encoding="utf-8",
    )

    assert (
        freeze_rhea_snapshot(
            [
                "--input-json",
                str(input_path),
                "--limit-reactions-per-accession",
                "1",
                "--snapshot-date",
                "2026-10-01",
                "--out-dir",
                str(tmp_path / "worklists"),
            ]
        )
        == 0
    )

    assert "wrote uniprot-rhea-2026-10-01 (1 rows)" in capsys.readouterr().out
    assert (tmp_path / "worklists" / "uniprot-rhea-2026-10-01.manifest.json").is_file()
