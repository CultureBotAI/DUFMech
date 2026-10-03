from __future__ import annotations

import json

import pytest

from dufmech.provenance import check_manifest, check_worklist_manifests, sha256
from dufmech.snapshot import write_worklist_snapshot
from dufmech.worklist import collect_worklist
from tests.test_duf_puf_snapshot import interpro_result


@pytest.fixture
def snapshot(tmp_path):
    manifest = write_worklist_snapshot(
        collect_worklist([interpro_result()]), tmp_path, snapshot_date="2026-10-01"
    )
    return tmp_path / f"{manifest['snapshot']['id']}.manifest.json", manifest


def test_check_manifest_accepts_matching_files(snapshot, tmp_path) -> None:
    path, _ = snapshot
    assert check_manifest(path) == []
    assert check_worklist_manifests(tmp_path) == []


def test_check_manifest_reports_size_hash_and_missing_files(snapshot) -> None:
    path, manifest = snapshot
    (path.parent / manifest["files"]["json"]["path"]).write_text("[]", encoding="utf-8")
    (path.parent / manifest["files"]["tsv"]["path"]).unlink()
    messages = [issue.message for issue in check_manifest(path)]
    assert any("files.json.bytes differs" in message for message in messages)
    assert any("files.json.sha256 differs" in message for message in messages)
    assert any("files.tsv.path is missing" in message for message in messages)


@pytest.mark.parametrize("label", ["json", "tsv"])
def test_manifest_requires_both_file_declarations(snapshot, label) -> None:
    path, manifest = snapshot
    del manifest["files"][label]
    path.write_text(json.dumps(manifest), encoding="utf-8")
    assert any(f"files.{label}.path must be" in issue.message for issue in check_manifest(path))


def test_orphans_are_detected_including_ignored_and_hidden_files(snapshot, tmp_path) -> None:
    (tmp_path / ".gitignore").write_text("*.tsv\n.hidden/\n", encoding="utf-8")
    (tmp_path / "orphan.tsv").write_text("pfam_id\n", encoding="utf-8")
    hidden = tmp_path / ".hidden"
    hidden.mkdir()
    (hidden / "orphan.json").write_text("[]", encoding="utf-8")
    issues = check_worklist_manifests(tmp_path)
    assert {issue.manifest for issue in issues} == {"orphan.tsv", "orphan.json"}
    assert all(issue.message == "artifact has no manifest" for issue in issues)


@pytest.mark.parametrize(
    ("section", "key", "value", "message"),
    [
        ("snapshot", "id", "unrelated", "snapshot.id"),
        ("snapshot", "date", "2026-02-30", "snapshot.date"),
        ("snapshot", "date", "2026-10-02", "snapshot.date"),
        ("snapshot", "generated_at", "2026-10-01T00:00:00", "snapshot.generated_at"),
        ("source", "name", "", "source.name"),
        ("rows", "total", True, "rows.total"),
        ("rows", "total", 2, "row count differs"),
        ("schema", "tsv_fieldnames", ["wrong"], "TSV header differs"),
        ("schema", "tsv_fieldnames", ["pfam_id", "pfam_id"], "unique nonempty"),
        ("schema", "tsv_fieldnames", [{}], "unique nonempty"),
    ],
)
def test_manifest_metadata_matches_artifacts(snapshot, section, key, value, message) -> None:
    path, manifest = snapshot
    manifest[section][key] = value
    path.write_text(json.dumps(manifest), encoding="utf-8")
    assert any(message in issue.message for issue in check_manifest(path))


@pytest.mark.parametrize(
    ("label", "text", "message"),
    [
        ("json", "[42]", "list of objects"),
        ("json", "[]", "JSON row count differs"),
        ("tsv", "wrong\n", "TSV header differs"),
    ],
)
def test_checksums_do_not_replace_row_validation(snapshot, label, text, message) -> None:
    path, manifest = snapshot
    artifact = path.parent / manifest["files"][label]["path"]
    artifact.write_text(text, encoding="utf-8")
    manifest["files"][label].update(bytes=artifact.stat().st_size, sha256=sha256(artifact))
    path.write_text(json.dumps(manifest), encoding="utf-8")
    assert any(message in issue.message for issue in check_manifest(path))


def test_manifest_rejects_symlink_artifact(snapshot, tmp_path) -> None:
    path, manifest = snapshot
    artifact = path.parent / manifest["files"]["json"]["path"]
    other = tmp_path / "external"
    artifact.rename(other)
    artifact.symlink_to(other)
    assert any("symlink" in issue.message for issue in check_manifest(path))


def test_manifest_rejects_escaping_path(snapshot) -> None:
    path, manifest = snapshot
    manifest["files"]["json"]["path"] = "../outside.json"
    path.write_text(json.dumps(manifest), encoding="utf-8")
    assert any("must be a filename" in issue.message for issue in check_manifest(path))


def test_no_manifests_is_an_error(tmp_path) -> None:
    assert check_worklist_manifests(tmp_path)[0].message == "no manifest files found"
