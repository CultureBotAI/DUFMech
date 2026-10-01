from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO
from pathlib import Path

from dufmech.snapshot import write_worklist_snapshot
from dufmech.worklist import KNOWN_HISTORICAL_DUF, UNKNOWN_CANDIDATE, collect_worklist
from scripts import freeze_duf_puf_worklist

WORKLIST_DIR = Path("data/worklists")


def interpro_result(
    *,
    accession: str = "PF01519",
    short_name: str = "DUF16",
    name: str = "Protein of unknown function DUF16",
    description: str = "<p>The function of this protein is unknown.</p>",
    integrated: str = "IPR002862",
    proteins: int = 26,
) -> dict:
    return {
        "metadata": {
            "accession": accession,
            "name": name,
            "source_database": "pfam",
            "type": "coiled_coil",
            "integrated": integrated,
        },
        "extra_fields": {
            "entry_id": None,
            "short_name": short_name,
            "description": [{"text": description}],
            "counters": {
                "domain_architectures": 2,
                "matches": 28,
                "proteins": proteins,
                "proteomes": 1,
                "structural_models": {"alphafold": 26},
                "structures": 1,
                "taxa": 10,
            },
        },
    }


def test_write_worklist_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    rows = collect_worklist(
        [
            interpro_result(accession="PF01519", proteins=26),
            interpro_result(
                accession="PF01784",
                short_name="DUF34_NIF3",
                name="Duf34/NIF3 (NGG1p interacting factor 3)",
                description="<p>This entry contains several homologues.</p>",
                proteins=18574,
            ),
        ]
    )

    manifest = write_worklist_snapshot(
        rows,
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
    )

    json_path = tmp_path / "interpro-pfam-duf-2026-10-01.json"
    tsv_path = tmp_path / "interpro-pfam-duf-2026-10-01.tsv"
    manifest_path = tmp_path / "interpro-pfam-duf-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "interpro-pfam-duf-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
    }
    assert manifest["source"]["url"] == (
        "https://www.ebi.ac.uk/interpro/api/entry/pfam/"
    )
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["by_unknown_status"] == {
        KNOWN_HISTORICAL_DUF: 1,
        UNKNOWN_CANDIDATE: 1,
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
    assert [row["pfam_id"] for row in json_rows] == ["PF01519", "PF01784"]
    assert [row["pfam_id"] for row in tsv_rows] == ["PF01519", "PF01784"]


def test_committed_worklist_manifests_match_artifacts() -> None:
    manifests = sorted(WORKLIST_DIR.glob("*.manifest.json"))

    assert manifests
    for manifest_path in manifests:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        json_path = WORKLIST_DIR / manifest["files"]["json"]["path"]
        tsv_path = WORKLIST_DIR / manifest["files"]["tsv"]["path"]

        json_data = json_path.read_bytes()
        tsv_data = tsv_path.read_bytes()
        json_rows = json.loads(json_data)
        tsv_rows = list(
            csv.DictReader(StringIO(tsv_data.decode("utf-8")), dialect="excel-tab")
        )

        assert manifest["files"]["json"]["bytes"] == len(json_data)
        assert manifest["files"]["json"]["sha256"] == hashlib.sha256(
            json_data
        ).hexdigest()
        assert manifest["files"]["tsv"]["bytes"] == len(tsv_data)
        assert manifest["files"]["tsv"]["sha256"] == hashlib.sha256(
            tsv_data
        ).hexdigest()
        assert len(json_rows) == manifest["rows"]["total"]
        assert len(tsv_rows) == manifest["rows"]["total"]
        assert tsv_rows[0].keys() == set(manifest["schema"]["tsv_fieldnames"])


def test_freeze_cli_reads_saved_interpro_page(tmp_path, capsys) -> None:
    page = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [interpro_result(accession="PF01519")],
    }
    input_path = tmp_path / "interpro.json"
    input_path.write_text(json.dumps(page), encoding="utf-8")

    assert (
        freeze_duf_puf_worklist.main(
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

    assert "wrote interpro-pfam-duf-2026-10-01 (1 rows)" in capsys.readouterr().out
    assert (tmp_path / "worklists" / "interpro-pfam-duf-2026-10-01.json").is_file()
