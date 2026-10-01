from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO

from dufmech.stringdb import StringDbInteractionRow, StringDbSeed
from dufmech.stringdb_snapshot import write_stringdb_snapshot
from dufmech.stringdb_snapshot_cli import (
    load_member_stringdb_seeds,
    parse_uniprot_taxon_seed,
)
from dufmech.stringdb_snapshot_cli import (
    main as freeze_stringdb_snapshot,
)


def stringdb_row(partner_string_id: str = "9606.ENSP00000251595") -> StringDbInteractionRow:
    return StringDbInteractionRow(
        uniprot_accession="P68871",
        taxon_id="9606",
        string_id="9606.ENSP00000494175",
        string_taxon_id="9606",
        taxon_name="Homo sapiens",
        preferred_name="HBB",
        annotation="Hemoglobin subunit beta",
        partner_string_id=partner_string_id,
        partner_preferred_name="HBA2",
        score=0.999,
        neighborhood_score=0.0,
        fusion_score=0.0,
        cooccurrence_score=0.064,
        coexpression_score=0.686,
        experimental_score=0.998,
        database_score=0.9,
        textmining_score=0.9,
    )


def test_parse_uniprot_taxon_seed_reads_uniprot_taxon_tuple() -> None:
    assert parse_uniprot_taxon_seed("P68871:9606") == StringDbSeed(
        uniprot_accession="P68871",
        taxon_id="9606",
    )


def test_load_member_stringdb_seeds_preserves_first_seen_order() -> None:
    assert load_member_stringdb_seeds(
        [
            {"uniprot_accession": "B2BDZ4", "taxon_id": "1"},
            {"uniprot_accession": "B2BDZ3", "uniprot_taxon_id": "2"},
            {
                "uniprot_accession": "B2BDZ4",
                "taxon_id": "1",
                "uniprot_taxon_id": "",
            },
            {"uniprot_accession": None, "taxon_id": "1"},
            {},
        ]
    ) == [
        StringDbSeed(uniprot_accession="B2BDZ4", taxon_id="1"),
        StringDbSeed(uniprot_accession="B2BDZ3", taxon_id="2"),
    ]


def test_write_stringdb_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    manifest = write_stringdb_snapshot(
        [
            stringdb_row("9606.ENSP00000322421"),
            stringdb_row("9606.ENSP00000251595"),
        ],
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
        seed_snapshot_id="pfam-uniprot-uniref90-2026-10-01",
        limit_partners_per_protein=2,
        required_score=500,
    )

    json_path = tmp_path / "uniprot-string-2026-10-01.json"
    tsv_path = tmp_path / "uniprot-string-2026-10-01.tsv"
    manifest_path = tmp_path / "uniprot-string-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "uniprot-string-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
        "seed_snapshot_id": "pfam-uniprot-uniref90-2026-10-01",
    }
    assert manifest["source"]["required_score"] == 500
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["unique_partner_string_ids"] == 2
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
    assert [row["partner_string_id"] for row in json_rows] == [
        "9606.ENSP00000251595",
        "9606.ENSP00000322421",
    ]
    assert [row["partner_string_id"] for row in tsv_rows] == [
        "9606.ENSP00000251595",
        "9606.ENSP00000322421",
    ]


def test_freeze_stringdb_snapshot_cli_reads_saved_member_rows(
    tmp_path,
    monkeypatch,
    capsys,
) -> None:
    def fake_collect(seeds, **kwargs) -> list[StringDbInteractionRow]:
        assert seeds == [StringDbSeed("P68871", "9606")]
        assert kwargs["limit_partners_per_protein"] == 1
        assert kwargs["required_score"] == 700
        return [stringdb_row()]

    monkeypatch.setattr(
        "dufmech.stringdb_snapshot_cli.collect_stringdb_snapshot_rows",
        fake_collect,
    )

    input_path = tmp_path / "pfam-uniprot-uniref90-2026-10-01.json"
    input_path.write_text(
        json.dumps([{"uniprot_accession": "P68871", "taxon_id": "9606"}]),
        encoding="utf-8",
    )

    assert (
        freeze_stringdb_snapshot(
            [
                "--input-json",
                str(input_path),
                "--limit-partners-per-protein",
                "1",
                "--required-score",
                "700",
                "--snapshot-date",
                "2026-10-01",
                "--out-dir",
                str(tmp_path / "worklists"),
            ]
        )
        == 0
    )

    assert "wrote uniprot-string-2026-10-01 (1 rows)" in capsys.readouterr().out
    assert (
        tmp_path / "worklists" / "uniprot-string-2026-10-01.manifest.json"
    ).is_file()
