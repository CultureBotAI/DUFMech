from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO

from dufmech.pdbe_kb import PdbeKbAnnotationRow, PdbeKbSeed
from dufmech.pdbe_kb_snapshot import write_pdbe_kb_snapshot
from dufmech.pdbe_kb_snapshot_cli import (
    load_rcsb_pdb_seeds,
    parse_pdb_entity_seed,
)
from dufmech.pdbe_kb_snapshot_cli import (
    main as freeze_pdbe_kb_snapshot,
)


def pdbe_row(
    *,
    endpoint: str = "uniprot_mapping",
    start_index: int = 1,
) -> PdbeKbAnnotationRow:
    return PdbeKbAnnotationRow(
        seed_uniprot_accession="P68871",
        pdb_id="1A00",
        entity_id="2",
        endpoint=endpoint,
        page_data_type="UNIPROT MAPPING",
        annotation_data_type="UniProt",
        annotation_name="HBB_HUMAN",
        annotation_accession="P68871",
        best_chain_id="D",
        start_index=start_index,
        end_index=146,
        uniprot_start=2,
        uniprot_end=147,
        start_code="MET",
        end_code="HIS",
        index_type="PDB",
        group_label="",
        detail_id="",
        bound_molecule_id="",
        resource_url="",
        confidence_level="",
        confidence_score=None,
        raw_score=None,
        mutation=None,
        pdb_code="",
        group_additional_data='{"bestChainId":"D","entityId":2}',
        residue_additional_data="",
    )


def test_parse_pdb_entity_seed_reads_uniprot_pdb_entity_tuple() -> None:
    assert parse_pdb_entity_seed("P68871:1A00:2") == PdbeKbSeed(
        uniprot_accession="P68871",
        pdb_id="1A00",
        entity_id="2",
    )


def test_load_rcsb_pdb_seeds_preserves_first_seen_order() -> None:
    assert load_rcsb_pdb_seeds(
        [
            {"uniprot_accession": "P68871", "pdb_id": "1A00", "entity_id": "2"},
            {"uniprot_accession": "P68871", "pdb_id": "1A01", "entity_id": "2"},
            {"uniprot_accession": "P68871", "pdb_id": "1A00", "entity_id": "2"},
            {"uniprot_accession": "P68871", "pdb_id": "", "entity_id": "2"},
            {},
        ]
    ) == [
        PdbeKbSeed(uniprot_accession="P68871", pdb_id="1A00", entity_id="2"),
        PdbeKbSeed(uniprot_accession="P68871", pdb_id="1A01", entity_id="2"),
    ]


def test_write_pdbe_kb_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    manifest = write_pdbe_kb_snapshot(
        [
            pdbe_row(endpoint="uniprot_mapping", start_index=2),
            pdbe_row(endpoint="domains", start_index=1),
        ],
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
        seed_snapshot_id="uniprot-rcsb-pdb-2026-10-01",
        endpoints=("uniprot_mapping", "domains"),
    )

    json_path = tmp_path / "uniprot-pdbe-kb-2026-10-01.json"
    tsv_path = tmp_path / "uniprot-pdbe-kb-2026-10-01.tsv"
    manifest_path = tmp_path / "uniprot-pdbe-kb-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "uniprot-pdbe-kb-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
        "seed_snapshot_id": "uniprot-rcsb-pdb-2026-10-01",
    }
    assert manifest["source"]["endpoints"] == ["uniprot_mapping", "domains"]
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["unique_pdb_entries"] == 1
    assert manifest["rows"]["by_endpoint"] == {
        "domains": 1,
        "uniprot_mapping": 1,
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
    assert [row["endpoint"] for row in json_rows] == [
        "domains",
        "uniprot_mapping",
    ]
    assert [row["start_index"] for row in tsv_rows] == ["1", "2"]


def test_freeze_pdbe_kb_snapshot_cli_reads_saved_rcsb_rows(
    tmp_path,
    monkeypatch,
    capsys,
) -> None:
    def fake_collect(seeds, **kwargs) -> list[PdbeKbAnnotationRow]:
        assert seeds == [PdbeKbSeed("P68871", "1A00", "2")]
        assert kwargs["endpoints"] == ("domains",)
        return [pdbe_row(endpoint="domains")]

    monkeypatch.setattr(
        "dufmech.pdbe_kb_snapshot_cli.collect_pdbe_kb_snapshot_rows",
        fake_collect,
    )

    input_path = tmp_path / "uniprot-rcsb-pdb-2026-10-01.json"
    input_path.write_text(
        json.dumps(
            [
                {
                    "uniprot_accession": "P68871",
                    "pdb_id": "1A00",
                    "entity_id": "2",
                }
            ]
        ),
        encoding="utf-8",
    )

    assert (
        freeze_pdbe_kb_snapshot(
            [
                "--input-json",
                str(input_path),
                "--endpoint",
                "domains",
                "--snapshot-date",
                "2026-10-01",
                "--out-dir",
                str(tmp_path / "worklists"),
            ]
        )
        == 0
    )

    assert "wrote uniprot-pdbe-kb-2026-10-01 (1 rows)" in capsys.readouterr().out
    assert (
        tmp_path / "worklists" / "uniprot-pdbe-kb-2026-10-01.manifest.json"
    ).is_file()
