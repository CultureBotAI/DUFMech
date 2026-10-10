"""Offline regression contract for the retained issue 165 data correction."""

import json
import shutil
from pathlib import Path

from dufmech import records
from dufmech.cross_mech_snapshot import cross_mech_unscanned, load_cross_mech_snapshot
from dufmech.report import verified_manifest
from dufmech.score_inputs import load_score_input

ROOT = Path(__file__).resolve().parents[1]
WORKLISTS = ROOT / "data/worklists"
CURRENT = "interpro-pfam-duf-2026-10-10"


def rows_by_id(path):
    return {row["pfam_id"]: row for row in json.loads(path.read_text())}


def test_refreeze_changes_only_upf1_current_name_classification():
    old_path = WORKLISTS / "pfam-previous-unknown-names-2026-10-07.json"
    new_path = WORKLISTS / "pfam-previous-unknown-names-2026-10-10.json"
    old_manifest, new_manifest = (verified_manifest(path) for path in (old_path, new_path))
    for key in ("compressed_bytes", "compressed_sha256", "release", "families_scanned"):
        assert new_manifest["source"][key] == old_manifest["source"][key]
    old, new = rows_by_id(old_path), rows_by_id(new_path)
    assert new.keys() == old.keys()
    assert len(new) == 1834
    assert {pfam for pfam in old if old[pfam] != new[pfam]} == {"PF18141"}
    assert new["PF18141"] == {**old["PF18141"], "currently_unknown_name": False}
    assert new["PF18141"]["previous_unknown_names"] == ["DUF5599"]
    assert new_manifest["rows"]["renamed_away_from_unknown"] == 1796


def test_migration_adds_upf1_without_reclassifying_retained_rows():
    path = WORKLISTS / f"{CURRENT}.json"
    loaded = load_score_input(path, "worklist")
    old = rows_by_id(WORKLISTS / "interpro-pfam-duf-2026-10-08.json")
    new = {row["pfam_id"]: row for row in loaded.rows}
    assert len(new) == 8296
    assert new.keys() - old.keys() == {"PF18141"}
    assert all(new[pfam] == row for pfam, row in old.items())
    assert new["PF18141"]["short_name"] == "UPF1_1B_dom"
    assert new["PF18141"]["unknown_status"] == "EX_DUF"
    assert "pfam_previous_unknown_name" in new["PF18141"]["candidate_reasons"]
    manifest = verified_manifest(path)
    assert manifest["derivation"]["added_pfam_ids"] == ["PF18141"]
    assert manifest["derivation"]["changes"] == []
    assert manifest["derivation"]["not_found_in_interpro"] == []
    assert manifest["derivation"]["fetched_live"] is True
    assert manifest["snapshot"]["input_snapshot_ids"]["pfam_previous_names"] == (
        "pfam-previous-unknown-names-2026-10-10"
    )


def test_cross_mech_derivation_preserves_evidence_and_marks_upf1_unscanned():
    old_path = ROOT / "data/cross_mech/cross-mech-duf-examples-2026-10-08.json"
    new_path = ROOT / "data/cross_mech/cross-mech-duf-examples-2026-10-10.json"
    old_manifest = verified_manifest(old_path)
    rows, manifest = load_cross_mech_snapshot(
        new_path,
        worklist_rows=json.loads((WORKLISTS / f"{CURRENT}.json").read_text()),
        worklist_snapshot_id=CURRENT,
    )
    assert rows == json.loads(old_path.read_text())
    assert manifest["source"] == old_manifest["source"]
    old_derivation = old_manifest["snapshot"]["derivation"]
    new_derivation = manifest["snapshot"]["derivation"]
    assert new_derivation["resolved_previous_names"] == old_derivation["resolved_previous_names"]
    assert new_derivation["rows_resolved_by_previous_name"] == 11
    assert new_derivation["rows_with_changed_seed_status"] == 0
    assert cross_mech_unscanned(manifest) == cross_mech_unscanned(old_manifest) | {"PF18141"}
    assert new_derivation["coverage"]["scanned_worklist_snapshot_id"] == (
        "interpro-pfam-duf-2026-10-01"
    )


def test_retained_seed_projects_without_scientific_curation(tmp_path, monkeypatch):
    worklists = tmp_path / "data/worklists"
    worklists.mkdir(parents=True)
    for suffix in ("json", "tsv", "manifest.json"):
        shutil.copy2(WORKLISTS / f"{CURRENT}.{suffix}", worklists)
    family_index = records.family_index
    # Verify the real snapshot, then exercise only this family's projection.
    monkeypatch.setattr(records, "family_index", lambda rows, scores: family_index(
        [row for row in rows if row["pfam_id"] == "PF18141"], scores,
    ))
    record = records.build_records(tmp_path)["PF18141.yaml"]
    assert record["pfam_id"] == "PF18141"
    assert record["seed_status"] == "EX_DUF"
    assert record["curation_status"] == "SEEDED"
    assert record["characterization_status"] == "UNSCORED"
    assert record["provenance"]["snapshot_id"] == CURRENT
    assert not record.get("assertions")
    assert not record.get("review_id")
