import json
from pathlib import Path

import pytest

from dufmech.provenance import check_manifest, sha256
from dufmech.snapshot import write_worklist_snapshot
from dufmech.worklist import DufFamilyRow
from scripts.reclassify_worklist import reclassify
from tests.test_report import freeze_worklist, worklist_row


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


@pytest.mark.parametrize("apply", [False, True])
def test_legacy_reclassification_refuses_to_drop_extra_metadata(tmp_path, apply):
    source = freeze_worklist(tmp_path)
    payload = json.loads(source.read_text())
    payload[0]["curator_note"] = "Preserve this evidence"
    source.write_text(json.dumps(payload))
    manifest_path = source.with_suffix(".manifest.json")
    manifest = json.loads(manifest_path.read_text())
    manifest["files"]["json"].update(bytes=source.stat().st_size, sha256=sha256(source))
    manifest_path.write_text(json.dumps(manifest))
    assert check_manifest(manifest_path) == []
    out = tmp_path / "out"
    with pytest.raises(ValueError, match="unexpected or missing worklist fields"):
        reclassify(source, out, "2026-10-05", apply=apply)
    assert not out.exists()


@pytest.mark.parametrize("apply", [False, True])
def test_legacy_reclassification_rejects_duplicate_families(tmp_path, apply):
    raw = worklist_row("PF18701", proteins=10)
    raw.pop("source_url")
    row = DufFamilyRow(**raw)
    write_worklist_snapshot([row, row], tmp_path, snapshot_date="2026-10-01")
    source = tmp_path / "interpro-pfam-duf-2026-10-01.json"
    out = tmp_path / "out"
    with pytest.raises(ValueError, match="duplicate"):
        reclassify(source, out, "2026-10-05", apply=apply)
    assert not out.exists()


def test_legacy_reclassification_writes_the_complete_manifest_once(tmp_path, monkeypatch):
    source = freeze_worklist(tmp_path)
    original_open = Path.open

    def reject_manifest_rewrite(path, mode="r", *args, **kwargs):
        if path.name == "interpro-pfam-duf-2026-10-05.manifest.json" and "w" in mode:
            raise AssertionError("Reclassification must not rewrite a published base manifest")
        return original_open(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", reject_manifest_rewrite)
    reclassify(source, tmp_path, "2026-10-05", apply=True)
    manifest = json.loads((tmp_path / "interpro-pfam-duf-2026-10-05.manifest.json").read_text())
    assert manifest["derivation"]["fetched_live"] is False
    assert manifest["derivation"]["input_files"]["json"]["sha256"] == sha256(source)
