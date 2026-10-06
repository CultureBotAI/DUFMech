import json

import pytest

from dufmech.provenance import check_manifest
from dufmech.snapshot import write_worklist_snapshot
from dufmech.worklist import DufFamilyRow
from scripts.reclassify_worklist import reclassify
from tests.test_report import worklist_row


def test_reclassification_preserves_source_and_all_nonclassification_fields(tmp_path):
    raw = worklist_row("PF18701", proteins=10, unknown_status="KNOWN_HISTORICAL_DUF")
    raw.update(name="Family of unknown function (DUF5641)", short_name="DUF5641",
               description="A presumed domain.", candidate_reasons=("short_name_matches_duf",))
    raw.pop("source_url")
    write_worklist_snapshot([DufFamilyRow(**raw)], tmp_path, snapshot_date="2026-10-01")
    source = tmp_path / "interpro-pfam-duf-2026-10-01.json"
    frozen = {p.name: p.read_bytes() for p in tmp_path.iterdir()}
    result = reclassify(source, tmp_path, "2026-10-05")
    assert result["changed_statuses"] == 1
    assert {p.name: p.read_bytes() for p in tmp_path.iterdir()} == frozen
    reclassify(source, tmp_path, "2026-10-05", apply=True)
    new = tmp_path / "interpro-pfam-duf-2026-10-05.json"
    old_row, new_row = json.loads(source.read_text())[0], json.loads(new.read_text())[0]
    for key in old_row:
        if key not in {"unknown_status", "candidate_reasons"}:
            assert old_row[key] == new_row[key]
    assert new_row["unknown_status"] == "UNKNOWN_CANDIDATE"
    assert not check_manifest(new.with_suffix(".manifest.json"))
    for name, content in frozen.items():
        assert (tmp_path / name).read_bytes() == content
    with pytest.raises(ValueError, match="overwrite"):
        reclassify(source, tmp_path, "2026-10-05", apply=True)
    with pytest.raises(ValueError, match="newer snapshot date"):
        reclassify(source, tmp_path, "2026-10-01", apply=True)
