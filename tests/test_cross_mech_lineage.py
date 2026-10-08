from __future__ import annotations

import json
from pathlib import Path

import pytest

from dufmech.cross_mech import CrossMechRow
from dufmech.cross_mech_snapshot import derive_cross_mech_snapshot, load_cross_mech_snapshot
from dufmech.report import ReportError
from tests.test_exduf_apply import T, _cross, _migrate, _previous_names


def _first(tmp_path: Path, *, extra_rows=()):
    worklist = _migrate(tmp_path)
    source = _cross(tmp_path, extra_rows)
    names = _previous_names(tmp_path / "names", [
        {"pfam_id": "PF14337", "short_name": "Abi_alpha", "names": ["DUF1814"]},
    ])
    manifest = derive_cross_mech_snapshot(
        source, worklist, tmp_path / "first", snapshot_date="2026-10-08",
        source_git_commit="a" * 40, previous_names_json=names, generated_at=T,
    )
    first = tmp_path / "first/cross-mech-duf-examples-2026-10-08.json"
    return worklist, names, first, manifest["snapshot"]["derivation"]


@pytest.mark.parametrize("repeat_names", [False, True])
@pytest.mark.parametrize("legacy", [False, True])
def test_chained_derivations_preserve_aliases_and_original_source(tmp_path, repeat_names, legacy):
    worklist, names, source, original = _first(tmp_path)
    if legacy:
        manifest_path = source.with_suffix(".manifest.json")
        manifest = json.loads(manifest_path.read_text())
        del manifest["snapshot"]["derivation"]["previous_name_sources"]
        manifest_path.write_text(json.dumps(manifest))
    original_bytes = source.with_suffix(".manifest.json").read_bytes()
    for day in ("2026-10-09", "2026-10-10"):
        out = tmp_path / day
        result = derive_cross_mech_snapshot(
            source, worklist, out, snapshot_date=day, source_git_commit="b" * 40,
            previous_names_json=names if repeat_names else None, generated_at=T,
        )
        info = result["snapshot"]["derivation"]
        for key in ("resolved_previous_names", "rows_resolved_by_previous_name",
                    "previous_names_snapshot_id", "previous_names_json_sha256"):
            assert info[key] == original[key]
        assert len(info["previous_name_sources"]) == 1
        source = out / f"cross-mech-duf-examples-{day}.json"
        load_cross_mech_snapshot(source, worklist_rows=json.loads(worklist.read_text()),
                                 worklist_snapshot_id=worklist.stem)
    assert (tmp_path / "first/cross-mech-duf-examples-2026-10-08.manifest.json").read_bytes() == original_bytes


def test_chains_keep_separate_provenance_for_different_releases(tmp_path):
    extra = CrossMechRow("", "DUF985", "NOT_IN_WORKLIST", "TraitMech", "genomics", "z.yaml",
                        "t:3", "Z", "record_text", ("record_mentions_unlisted_short_name",))
    worklist, _, source, original = _first(tmp_path, extra_rows=[extra])
    names = _previous_names(tmp_path / "later-names", [
        {"pfam_id": "PF06172", "short_name": "Cupin_8", "names": ["DUF985"]},
    ], day="2026-10-08")
    result = derive_cross_mech_snapshot(
        source, worklist, tmp_path / "second", snapshot_date="2026-10-09",
        source_git_commit="b" * 40, previous_names_json=names, generated_at=T,
    )
    info = result["snapshot"]["derivation"]
    assert "previous_names_snapshot_id" not in info
    assert "previous_names_json_sha256" not in info
    assert info["rows_resolved_by_previous_name"] == 2
    assert info["resolved_previous_names"] == {"DUF1814": "PF14337", "DUF985": "PF06172"}
    assert info["previous_name_sources"][0] == original["previous_name_sources"][0]
    assert info["previous_name_sources"][1]["resolved_previous_names"] == {"DUF985": "PF06172"}
    source = tmp_path / "second/cross-mech-duf-examples-2026-10-09.json"
    rows, manifest = load_cross_mech_snapshot(
        source, worklist_rows=json.loads(worklist.read_text()), worklist_snapshot_id=worklist.stem)
    from dufmech.cross_mech_report import render_cross_mech_report

    report = render_cross_mech_report(rows, manifest)
    assert "`pfam-previous-unknown-names-2026-10-07`, `pfam-previous-unknown-names-2026-10-08`" in report
    assert "`None`" not in report
    result = derive_cross_mech_snapshot(
        source, worklist, tmp_path / "third", snapshot_date="2026-10-10",
        source_git_commit="c" * 40, generated_at=T,
    )
    assert result["snapshot"]["derivation"]["previous_name_sources"] == info["previous_name_sources"]


@pytest.mark.parametrize("damage", ["map", "count", "hash", "aggregate"])
def test_incomplete_or_inconsistent_inherited_provenance_is_rejected(tmp_path, damage):
    worklist, _, source, _ = _first(tmp_path)
    manifest_path = source.with_suffix(".manifest.json")
    manifest = json.loads(manifest_path.read_text())
    info = manifest["snapshot"]["derivation"]
    if damage == "map":
        info["resolved_previous_names"] = {}
        info["previous_name_sources"][0]["resolved_previous_names"] = {}
    elif damage == "count":
        info["rows_resolved_by_previous_name"] = 0
    elif damage == "hash":
        info["previous_name_sources"][0]["json_sha256"] = "bad"
    else:
        info["previous_names_json_sha256"] = "0" * 64
    manifest_path.write_text(json.dumps(manifest))
    with pytest.raises(ReportError, match="previous-name"):
        load_cross_mech_snapshot(source, worklist_rows=json.loads(worklist.read_text()),
                                 worklist_snapshot_id=worklist.stem)
    out = tmp_path / "rejected"
    with pytest.raises(ReportError, match="previous-name"):
        derive_cross_mech_snapshot(source, worklist, out, snapshot_date="2026-10-09",
                                   source_git_commit="b" * 40, generated_at=T)
    assert not out.exists()


def test_same_snapshot_identity_with_different_bytes_is_rejected(tmp_path):
    worklist, _, source, _ = _first(tmp_path)
    names = _previous_names(tmp_path / "different", [
        {"pfam_id": "PF06172", "short_name": "Cupin_8", "names": ["DUF1814"]},
    ])
    with pytest.raises(ReportError, match="changed its recorded hash"):
        derive_cross_mech_snapshot(source, worklist, tmp_path / "rejected",
                                   snapshot_date="2026-10-09", source_git_commit="b" * 40,
                                   previous_names_json=names, generated_at=T)
    assert not (tmp_path / "rejected").exists()


def test_ambiguity_history_survives_but_resolved_names_leave_active_ambiguity(tmp_path):
    worklist = _migrate(tmp_path)
    source = _cross(tmp_path)
    names = _previous_names(tmp_path / "ambiguous", [
        {"pfam_id": pfam, "short_name": "x", "names": ["DUF1814"]}
        for pfam in ("PF06172", "PF14337")
    ])
    derive_cross_mech_snapshot(source, worklist, tmp_path / "first", snapshot_date="2026-10-08",
                               source_git_commit="a" * 40, previous_names_json=names, generated_at=T)
    source = tmp_path / "first/cross-mech-duf-examples-2026-10-08.json"
    names = _previous_names(tmp_path / "resolved", [
        {"pfam_id": "PF14337", "short_name": "Abi_alpha", "names": ["DUF1814"]},
    ], day="2026-10-08")
    manifest = derive_cross_mech_snapshot(
        source, worklist, tmp_path / "second", snapshot_date="2026-10-09",
        source_git_commit="b" * 40, previous_names_json=names, generated_at=T,
    )
    info = manifest["snapshot"]["derivation"]
    assert info["ambiguous_previous_names"] == []
    assert info["previous_name_sources"][0]["ambiguous_previous_names"] == ["DUF1814"]
    assert info["resolved_previous_names"] == {"DUF1814": "PF14337"}


def test_conflicting_alias_resolution_stops_before_writing(tmp_path):
    worklist, _, source, _ = _first(tmp_path)
    manifest_path = source.with_suffix(".manifest.json")
    manifest = json.loads(manifest_path.read_text())
    info = manifest["snapshot"]["derivation"]
    info["previous_name_sources"].append({
        "snapshot_id": "pfam-previous-unknown-names-2026-10-08", "json_sha256": "0" * 64,
        "resolved_previous_names": {"DUF1814": "PF06172"}, "ambiguous_previous_names": [],
    })
    manifest_path.write_text(json.dumps(manifest))
    with pytest.raises(ReportError, match="conflicting previous-name mapping"):
        derive_cross_mech_snapshot(source, worklist, tmp_path / "rejected",
                                   snapshot_date="2026-10-09", source_git_commit="b" * 40,
                                   generated_at=T)
    assert not (tmp_path / "rejected").exists()
