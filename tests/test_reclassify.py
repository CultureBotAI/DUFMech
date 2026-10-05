from __future__ import annotations

import json
from dataclasses import asdict, replace
from datetime import datetime, timezone
from pathlib import Path

import pytest

from dufmech.provenance import check_manifest, sha256
from dufmech.reclassify import main, reclassify_snapshot
from dufmech.report import ReportError
from dufmech.scoring import score_families
from dufmech.snapshot import write_worklist_snapshot
from dufmech.worklist import (
    CLASSIFIER_POLICY,
    KNOWN_HISTORICAL_DUF,
    UNKNOWN_CANDIDATE,
    reclassify_worklist,
    row_from_interpro_entry,
)
from tests.test_duf_puf_worklist import interpro_result


@pytest.fixture
def parent(tmp_path):
    row = row_from_interpro_entry(interpro_result(
        accession="PF18701", short_name="DUF5641",
        name="Family of unknown function (DUF5641)",
        description="This presumed domain is found in a range of retrotransposon polyproteins.",
    ))
    old = replace(row, unknown_status=KNOWN_HISTORICAL_DUF, candidate_reasons=("short_name_matches_duf",))
    write_worklist_snapshot([old], tmp_path, snapshot_date="2026-10-01")
    return tmp_path / "interpro-pfam-duf-2026-10-01.json"


def test_reclassification_changes_only_classification_fields(parent, tmp_path) -> None:
    original_files = {path.name: path.read_bytes() for path in tmp_path.iterdir()}
    manifest = reclassify_snapshot(parent, tmp_path, snapshot_date="2026-10-05")
    for name, content in original_files.items():
        assert (tmp_path / name).read_bytes() == content
    corrected = tmp_path / manifest["files"]["json"]["path"]
    old, new = json.loads(parent.read_text())[0], json.loads(corrected.read_text())[0]
    assert {key for key in old if old[key] != new[key]} == {"candidate_reasons", "unknown_status"}
    assert new["unknown_status"] == UNKNOWN_CANDIDATE
    assert manifest["derivation"]["changed_status_rows"] == 1
    assert manifest["derivation"]["classifier_policy"] == CLASSIFIER_POLICY
    assert manifest["derivation"]["fetched_live"] is False
    assert manifest["derivation"]["input_files"]["json"]["sha256"] == sha256(parent)
    assert manifest["derivation"]["input_files"]["manifest"]["sha256"] == sha256(
        parent.with_suffix(".manifest.json")
    )
    assert check_manifest(corrected.with_suffix(".manifest.json")) == []
    scores = score_families([new])
    assert scores[0].characterization_status == UNKNOWN_CANDIDATE
    assert scores[0].known_evidence_count == 0


def test_reclassification_is_deterministic(parent, tmp_path) -> None:
    timestamp = datetime(2026, 10, 5, tzinfo=timezone.utc)
    a, b = tmp_path / "a", tmp_path / "b"
    for directory in (a, b):
        reclassify_snapshot(parent, directory, snapshot_date="2026-10-05", generated_at=timestamp)
    assert {path.name: path.read_bytes() for path in a.iterdir()} == {
        path.name: path.read_bytes() for path in b.iterdir()
    }


@pytest.mark.parametrize("day", ["2026-10-01", "2026-09-30"])
def test_correction_requires_a_newer_date(parent, tmp_path, day) -> None:
    before = {path.name: path.read_bytes() for path in tmp_path.iterdir()}
    with pytest.raises(ReportError, match="later than"):
        reclassify_snapshot(parent, tmp_path, snapshot_date=day)
    assert before == {path.name: path.read_bytes() for path in tmp_path.iterdir()}


@pytest.mark.parametrize("suffix", ["json", "tsv", "manifest.json"])
def test_correction_refuses_existing_or_symlink_outputs(parent, tmp_path, suffix) -> None:
    target = tmp_path / f"interpro-pfam-duf-2026-10-05.{suffix}"
    target.symlink_to(tmp_path / "nonexistent")
    with pytest.raises(ReportError, match="already exists"):
        reclassify_snapshot(parent, tmp_path, snapshot_date="2026-10-05")
    assert target.is_symlink()
    assert not (tmp_path / "nonexistent").exists()


def test_correction_rejects_corrupted_parent_before_writing(parent, tmp_path) -> None:
    parent.write_text("[]", encoding="utf-8")
    out = tmp_path / "out"
    with pytest.raises(ReportError, match="differs"):
        reclassify_snapshot(parent, out, snapshot_date="2026-10-05")
    assert not out.exists()


def test_reclassify_rows_preserves_metadata_and_retains_false_positive_rows() -> None:
    old = row_from_interpro_entry(interpro_result(short_name="unrelated", name="unrelated", description=""))
    corrected = reclassify_worklist([old])
    assert len(corrected) == 1
    assert asdict(corrected[0]) == asdict(old)


def test_cli_runs_offline_and_reports_new_snapshot(parent, tmp_path, capsys) -> None:
    assert main([
        "--input-json", str(parent), "--out-dir", str(tmp_path), "--snapshot-date", "2026-10-05"
    ]) == 0
    assert "1 seed statuses changed; no live fetch" in capsys.readouterr().out
    with pytest.raises(SystemExit) as exc:
        main(["--input-json", str(parent), "--snapshot-date", "invalid"])
    assert exc.value.code == 1


def test_committed_correction_is_reproducible_and_original_snapshot_is_unchanged(tmp_path) -> None:
    directory = Path("data/worklists")
    old = directory / "interpro-pfam-duf-2026-10-01.json"
    committed_manifest = directory / "interpro-pfam-duf-2026-10-05.manifest.json"
    manifest = json.loads(committed_manifest.read_text())
    timestamp = datetime.fromisoformat(manifest["snapshot"]["generated_at"].replace("Z", "+00:00"))
    regenerated = reclassify_snapshot(old, tmp_path, snapshot_date="2026-10-05", generated_at=timestamp)
    assert manifest == regenerated
    for entry in regenerated["files"].values():
        assert (directory / entry["path"]).read_bytes() == (tmp_path / entry["path"]).read_bytes()
    assert sha256(old) == "141fd83d020563444c6498a3f0dc4d7924e7cf759647b449271f4d00c612b689"
