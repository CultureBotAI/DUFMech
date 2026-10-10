from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import socket
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from dufmech import exports
from dufmech.records import RecordError, build_records, write_records
from dufmech.report import ReportError
from dufmech.snapshot import write_worklist_snapshot
from dufmech.worklist import DufFamilyRow

REPO_ROOT = Path(__file__).resolve().parents[1]


def make_corpus(root: Path, *, interpro: str = "IPR000001") -> Path:
    rows = [
        DufFamilyRow(
            pfam_id=pfam, short_name="DUF1", name='"DUF" \\ name',
            interpro_id=interpro if pfam != "PF00003" else "",
            unknown_status="UNKNOWN_CANDIDATE", candidate_reasons=["short_name_matches_duf"],
            proteins=10, matches=11, proteomes=2, taxa=3, structures=0,
            alphafold_models=5, domain_architectures=1,
            description='A\tquoted "description"\nwith\rcarriage \\ escapes.',
        )
        for pfam in ("PF00003", "PF00002", "PF00001")
    ]
    write_worklist_snapshot(
        rows, root / "data/worklists", snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 12, tzinfo=timezone.utc),
    )
    write_records(root, build_records(root), apply=True)
    return root


@pytest.fixture
def corpus(tmp_path):
    return make_corpus(tmp_path.resolve() / "corpus")


def body(payload: bytes) -> str:
    return "\n".join(line for line in payload.decode().splitlines() if not line.startswith("#")) + "\n"


def rows(payload: bytes) -> list[dict[str, str]]:
    return list(csv.DictReader(io.StringIO(body(payload)), delimiter="\t"))


def inventory(root: Path) -> dict[str, bytes]:
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_nonempty_deterministic_projection_preserves_sources_and_unmapped_nodes(corpus, tmp_path):
    before = inventory(corpus)
    first = exports.build_exports(corpus)
    assert first == exports.build_exports(make_corpus(tmp_path / "other"))
    assert inventory(corpus) == before
    assert set(first) == {exports.KGX_NODES, exports.KGX_EDGES, exports.SSSOM}
    nodes = rows(first[exports.KGX_NODES])
    edges = rows(first[exports.KGX_EDGES])
    mappings = rows(first[exports.SSSOM])
    assert len(nodes) == 4
    assert len(edges) == len(mappings) == 2
    assert [r["id"] for r in nodes] == sorted(r["id"] for r in nodes)
    assert [r["subject"] for r in edges] == ["Pfam:PF00001", "Pfam:PF00002"]
    assert {r["predicate"] for r in edges} == {"biolink:related_to"}
    assert {r["predicate_id"] for r in mappings} == {"skos:relatedMatch"}
    assert {r["mapping_justification"] for r in mappings} == {"semapv:UnspecifiedMatching"}
    assert all(r["object_label"] == r["confidence"] == "" for r in mappings)
    assert all(r["category"] == "biolink:NamedThing" for r in nodes)
    interpro = nodes[0]
    assert interpro["id"] == "InterPro:IPR000001"
    assert interpro["name"] == interpro["description"] == interpro["curation_status"] == ""
    assert {r["curation_status"] for r in nodes[1:]} == {"SEEDED"}
    assert {r["characterization_status"] for r in nodes[1:]} == {"UNSCORED"}
    snapshot = corpus / "data/worklists/interpro-pfam-duf-2026-10-01.json"
    digest = hashlib.sha256(snapshot.read_bytes()).hexdigest()
    assert all(r["source_snapshot_sha256"] == digest for r in nodes + edges)
    assert all(r["source_field"] == "interpro_id" for r in edges)
    assert all(f"source_snapshot_sha256={digest}" in r["comment"] for r in mappings)
    assert all(r["mapping_provider"].endswith(r["subject_id"].split(":")[1]) for r in mappings)
    assert all("data/families/" in r["comment"] for r in mappings)


def test_csv_and_literal_readers_agree_on_every_cell(corpus):
    for payload in exports.build_exports(corpus).values():
        text = body(payload)
        literal = [line.split("\t") for line in text.splitlines()]
        assert literal == list(csv.reader(io.StringIO(text), delimiter="\t"))
        assert all(len(row) == len(literal[0]) for row in literal)
        assert "\r" not in text
    awkward = '"quoted"\\\t\n\r\x00\x0b\x0c\x1c\x7f\x85\u2028\u2029'
    escaped = exports._cell(awkward)
    assert '"' not in escaped
    assert len(escaped.splitlines()) == 1
    # The documented escape grammar also forms the contents of a JSON string.
    assert json.loads('"' + escaped + '"') == awkward


def test_dry_run_check_apply_and_unchanged_mtimes(corpus, monkeypatch):
    native_before = inventory(corpus)
    artifacts = exports.build_exports(corpus)
    monkeypatch.setattr(exports, "build_exports", lambda _: artifacts)
    assert exports.write_exports(corpus) == list(artifacts)
    assert inventory(corpus) == native_before
    with pytest.raises(exports.ExportError, match="stale or missing"):
        exports.write_exports(corpus, check=True)
    assert inventory(corpus) == native_before
    assert exports.write_exports(corpus, apply=True) == list(artifacts)
    assert exports.write_exports(corpus, check=True) == []
    mtimes = {name: (corpus / name).stat().st_mtime_ns for name in artifacts}
    assert exports.write_exports(corpus, apply=True) == []
    assert {name: (corpus / name).stat().st_mtime_ns for name in artifacts} == mtimes
    for name, payload in native_before.items():
        assert (corpus / name).read_bytes() == payload
    (corpus / exports.KGX_EDGES).write_text("stale\n")
    assert exports.main(["--root", str(corpus), "--check"]) == 1
    assert exports.main(["--root", str(corpus), "--apply"]) == 0
    assert (corpus / exports.KGX_EDGES).read_bytes() == artifacts[exports.KGX_EDGES]


@pytest.mark.parametrize("damage", [
    "json_hash", "tsv_hash", "manifest", "duplicate_json_key", "overlay_schema",
    "overlay_duplicate_key", "orphan_overlay", "projection", "hidden_projection",
])
def test_invalid_native_inputs_fail_before_any_output(corpus, damage):
    snapshot = corpus / "data/worklists/interpro-pfam-duf-2026-10-01.json"
    manifest_path = snapshot.with_suffix(".manifest.json")
    if damage == "json_hash":
        snapshot.write_bytes(snapshot.read_bytes() + b" ")
    elif damage == "tsv_hash":
        tsv = snapshot.with_suffix(".tsv")
        tsv.write_bytes(tsv.read_bytes() + b" ")
    elif damage == "manifest":
        manifest_path.write_text("{}\n")
    elif damage == "duplicate_json_key":
        payload = snapshot.read_text().replace(
            '"pfam_id": "PF00001"', '"pfam_id": "PF00001", "pfam_id": "PF00001"', 1,
        ).encode()
        assert payload != snapshot.read_bytes()
        snapshot.write_bytes(payload)
        manifest = json.loads(manifest_path.read_text())
        manifest["files"]["json"].update(bytes=len(payload), sha256=hashlib.sha256(payload).hexdigest())
        manifest_path.write_text(json.dumps(manifest))
    elif damage in {"overlay_schema", "overlay_duplicate_key", "orphan_overlay"}:
        directory = corpus / "curation/families"
        directory.mkdir(parents=True)
        name = "PF99999.yaml" if damage == "orphan_overlay" else "PF00001.yaml"
        text = "pfam_id: PF00001\ncuration_status: SEEDED\n"
        if damage == "overlay_schema":
            text += "name: invented override\n"
        if damage == "overlay_duplicate_key":
            text += "curation_status: REVIEWED\n"
        (directory / name).write_text(text)
    elif damage == "hidden_projection":
        (corpus / "data/families/.ignored.yaml").write_text("unexpected: true\n")
    else:
        projection = corpus / "data/families/PF00001.yaml"
        projection.write_text(projection.read_text().replace("SEEDED", "REVIEWED"))
    before = inventory(corpus)
    assert exports.main(["--root", str(corpus), "--apply"]) == 1
    assert inventory(corpus) == before
    assert not (corpus / "exports").exists()


def test_checksum_valid_malformed_interpro_is_rejected(corpus):
    snapshot = corpus / "data/worklists/interpro-pfam-duf-2026-10-01.json"
    manifest_path = snapshot.with_suffix(".manifest.json")
    manifest = json.loads(manifest_path.read_text())
    for kind in ("json", "tsv"):
        path = snapshot.with_suffix("." + kind)
        raw = path.read_bytes().replace(b"IPR000001", b"IPRnot-an-accession")
        path.write_bytes(raw)
        manifest["files"][kind].update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
    manifest_path.write_text(json.dumps(manifest))
    with pytest.raises((RecordError, ReportError, ValueError)):
        exports.build_exports(corpus)
    assert not (corpus / "exports").exists()


def test_no_associations_is_an_explicit_failure(tmp_path):
    root = make_corpus(tmp_path / "empty", interpro="")
    with pytest.raises(exports.ExportError, match="no verified Pfam/InterPro associations"):
        exports.write_exports(root, apply=True)
    assert not (root / "exports").exists()


@pytest.mark.parametrize("destination", ["exports", exports.KGX_NODES, exports.SSSOM])
def test_output_symlinks_are_rejected_before_any_write(corpus, tmp_path, destination, monkeypatch):
    artifacts = exports.build_exports(corpus)
    monkeypatch.setattr(exports, "build_exports", lambda _: artifacts)
    outside = tmp_path / "outside"
    outside.mkdir()
    path = corpus / destination
    path.parent.mkdir(parents=True, exist_ok=True)
    path.symlink_to(outside if destination == "exports" else outside / "missing.tsv")
    with pytest.raises(RecordError, match="symlink"):
        exports.write_exports(corpus, apply=True)
    assert not list(outside.iterdir())
    assert path.is_symlink()


def test_source_symlink_is_rejected(corpus, tmp_path):
    path = corpus / "data/worklists/interpro-pfam-duf-2026-10-01.json"
    outside = tmp_path / "source.json"
    path.rename(outside)
    path.symlink_to(outside)
    with pytest.raises((RecordError, ReportError, ValueError)):
        exports.build_exports(corpus)


@pytest.mark.parametrize("mode", ["dry_run", "check", "apply"])
@pytest.mark.parametrize("replacement", ["leaf_symlink", "parent_symlink", "fifo"])
def test_output_reads_reject_replacements_at_open(corpus, tmp_path, monkeypatch, mode, replacement):
    artifacts = exports.build_exports(corpus)
    monkeypatch.setattr(exports, "build_exports", lambda _: artifacts)
    exports.write_exports(corpus, apply=True)
    target = corpus / exports.KGX_NODES
    outside = tmp_path / "outside"
    outside.mkdir()
    for name in (exports.KGX_NODES, exports.KGX_EDGES):
        (outside / Path(name).name).write_bytes(artifacts[name])
    before = inventory(outside)
    original = os.open
    replaced = False

    def replace_before_open(path, flags, *args, **kwargs):
        nonlocal replaced
        component = "kgx" if replacement == "parent_symlink" else target.name
        if path == component and not replaced:
            replaced = True
            assert flags & os.O_NOFOLLOW
            if replacement == "parent_symlink":
                assert flags & os.O_DIRECTORY
                target.parent.rename(corpus / "old-kgx")
                target.parent.symlink_to(outside, target_is_directory=True)
            else:
                assert flags & os.O_NONBLOCK
                target.unlink()
                if replacement == "fifo":
                    os.mkfifo(target)
                else:
                    target.symlink_to(outside / target.name)
        return original(path, flags, *args, **kwargs)

    monkeypatch.setattr(os, "open", replace_before_open)
    options = {"check": True} if mode == "check" else {"apply": mode == "apply"}
    with pytest.raises((OSError, exports.ExportError)):
        exports.write_exports(corpus, **options)
    assert replaced
    assert inventory(outside) == before
    assert (corpus / exports.SSSOM).read_bytes() == artifacts[exports.SSSOM]


@pytest.mark.parametrize("replacement", ["symlink", "fifo"])
def test_staged_destination_reads_reject_replaced_leaves(corpus, tmp_path, monkeypatch, replacement):
    artifacts = exports.build_exports(corpus)
    monkeypatch.setattr(exports, "build_exports", lambda _: artifacts)
    exports.write_exports(corpus, apply=True)
    for name in artifacts:
        (corpus / name).write_bytes(b"previous\n")
    target = corpus / exports.KGX_NODES
    outside = tmp_path / "outside.tsv"
    outside.write_bytes(b"previous\n")
    original_stage = exports._stage_file
    original_open = os.open
    replaced = False

    def replace_after_stage(directory, payload):
        nonlocal replaced
        temporary = original_stage(directory, payload)
        if not replaced:
            replaced = True
            target.unlink()
            if replacement == "fifo":
                os.mkfifo(target)
            else:
                target.symlink_to(outside)
        return temporary

    def guarded_open(path, flags, *args, **kwargs):
        if replaced and path == target.name:
            assert flags & os.O_NOFOLLOW
            assert flags & os.O_NONBLOCK
        return original_open(path, flags, *args, **kwargs)

    monkeypatch.setattr(exports, "_stage_file", replace_after_stage)
    monkeypatch.setattr(os, "open", guarded_open)
    with pytest.raises((OSError, exports.ExportError)):
        exports.write_exports(corpus, apply=True)
    assert replaced
    assert outside.read_bytes() == b"previous\n"
    assert (corpus / exports.KGX_EDGES).read_bytes() == b"previous\n"
    assert (corpus / exports.SSSOM).read_bytes() == b"previous\n"
    assert not list((corpus / "exports").rglob(".dufmech-*"))


@pytest.mark.parametrize("replacement", ["directory_with_edit", "symlink"])
def test_staged_checks_use_the_pinned_publication_directory(corpus, tmp_path, monkeypatch, replacement):
    artifacts = exports.build_exports(corpus)
    monkeypatch.setattr(exports, "build_exports", lambda _: artifacts)
    exports.write_exports(corpus, apply=True)
    for name in artifacts:
        (corpus / name).write_bytes(b"previous\n")
    parent = corpus / "exports/kgx"
    retained = corpus / "retained-kgx"
    outside = tmp_path / "outside"
    outside.mkdir()
    for name in ("nodes.tsv", "edges.tsv"):
        (outside / name).write_bytes(b"previous\n")
    before = inventory(outside)
    original = exports._stage_file

    def replace_parent_after_stage(directory, payload):
        temporary = original(directory, payload)
        if not retained.exists():
            parent.rename(retained)
            if replacement == "symlink":
                parent.symlink_to(outside, target_is_directory=True)
            else:
                parent.mkdir()
                for name in ("nodes.tsv", "edges.tsv"):
                    (parent / name).write_bytes(b"previous\n")
                (retained / "nodes.tsv").write_bytes(b"concurrent edit\n")
        return temporary

    monkeypatch.setattr(exports, "_stage_file", replace_parent_after_stage)
    if replacement == "directory_with_edit":
        with pytest.raises(exports.ExportError, match="changed during staging"):
            exports.write_exports(corpus, apply=True)
        assert (retained / "nodes.tsv").read_bytes() == b"concurrent edit\n"
        assert (retained / "edges.tsv").read_bytes() == b"previous\n"
        assert (parent / "nodes.tsv").read_bytes() == b"previous\n"
        assert (corpus / exports.SSSOM).read_bytes() == b"previous\n"
    else:
        assert exports.write_exports(corpus, apply=True) == list(artifacts)
        for name in (exports.KGX_NODES, exports.KGX_EDGES):
            assert (retained / Path(name).name).read_bytes() == artifacts[name]
        assert (corpus / exports.SSSOM).read_bytes() == artifacts[exports.SSSOM]
    assert inventory(outside) == before
    assert not list(retained.glob(".dufmech-*"))


def test_staging_failure_preserves_entire_previous_generation(corpus, monkeypatch):
    artifacts = exports.build_exports(corpus)
    monkeypatch.setattr(exports, "build_exports", lambda _: artifacts)
    for name in artifacts:
        path = corpus / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"previous\n")
    before = inventory(corpus)
    original = exports._stage_file
    calls = 0

    def fail_second(directory, payload):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("staging failure")
        return original(directory, payload)

    monkeypatch.setattr(exports, "_stage_file", fail_second)
    with pytest.raises(OSError, match="staging failure"):
        exports.write_exports(corpus, apply=True)
    assert inventory(corpus) == before


def test_detected_concurrent_edit_is_preserved(corpus, monkeypatch):
    artifacts = exports.build_exports(corpus)
    monkeypatch.setattr(exports, "build_exports", lambda _: artifacts)
    original = exports._stage_file

    def concurrent_edit(directory, payload):
        temporary = original(directory, payload)
        (corpus / exports.KGX_NODES).write_bytes(b"concurrent edit\n")
        return temporary

    monkeypatch.setattr(exports, "_stage_file", concurrent_edit)
    with pytest.raises(exports.ExportError, match="changed during staging"):
        exports.write_exports(corpus, apply=True)
    assert (corpus / exports.KGX_NODES).read_bytes() == b"concurrent edit\n"
    assert not (corpus / exports.KGX_EDGES).exists()
    assert not list((corpus / "exports").rglob(".dufmech-*"))


def test_interrupted_replacement_leaves_whole_files_and_can_be_repaired(corpus, monkeypatch):
    artifacts = exports.build_exports(corpus)
    monkeypatch.setattr(exports, "build_exports", lambda _: artifacts)
    original = exports.os.replace
    calls = 0

    def interrupt_second(*args, **kwargs):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("interrupted publication")
        return original(*args, **kwargs)

    monkeypatch.setattr(exports.os, "replace", interrupt_second)
    with pytest.raises(OSError, match="interrupted publication"):
        exports.write_exports(corpus, apply=True)
    assert (corpus / exports.KGX_NODES).read_bytes() == artifacts[exports.KGX_NODES]
    assert not (corpus / exports.KGX_EDGES).exists()
    assert not list((corpus / "exports").rglob(".dufmech-*"))
    with pytest.raises(exports.ExportError, match="stale or missing"):
        exports.write_exports(corpus, check=True)
    monkeypatch.setattr(exports.os, "replace", original)
    exports.write_exports(corpus, apply=True)
    assert exports.write_exports(corpus, check=True) == []


def test_regular_file_destination_required(corpus, monkeypatch):
    artifacts = exports.build_exports(corpus)
    monkeypatch.setattr(exports, "build_exports", lambda _: artifacts)
    (corpus / exports.KGX_EDGES).mkdir(parents=True)
    with pytest.raises(exports.ExportError, match="regular file"):
        exports.write_exports(corpus, apply=True)
    assert not (corpus / exports.KGX_NODES).exists()


def test_invalid_cli_options_and_missing_corpus(tmp_path):
    with pytest.raises(SystemExit) as exc:
        exports.main(["--check", "--apply"])
    assert exc.value.code == 2
    assert exports.main(["--root", str(tmp_path)]) == 1
    with pytest.raises(exports.ExportError, match="mutually exclusive"):
        exports.write_exports(tmp_path, apply=True, check=True)
    assert not list(tmp_path.iterdir())


def test_real_corpus_exports_match_committed_artifacts_without_network(monkeypatch):
    def no_network(*args, **kwargs):
        raise AssertionError("offline exporter attempted network access")

    monkeypatch.setattr(socket, "create_connection", no_network)
    monkeypatch.setattr(socket.socket, "connect", no_network)
    before = inventory(REPO_ROOT / "data/families")
    artifacts = exports.build_exports(REPO_ROOT)
    assert inventory(REPO_ROOT / "data/families") == before
    assert len(rows(artifacts[exports.KGX_NODES])) == 16534
    assert len(rows(artifacts[exports.KGX_EDGES])) == 8238
    assert len(rows(artifacts[exports.SSSOM])) == 8238
    for name, payload in artifacts.items():
        assert (REPO_ROOT / name).read_bytes() == payload
        table = body(payload)
        assert list(csv.reader(io.StringIO(table), delimiter="\t")) == [
            line.split("\t") for line in table.splitlines()
        ]
    family_nodes = [r for r in rows(artifacts[exports.KGX_NODES]) if r["id"].startswith("Pfam:")]
    assert len(family_nodes) == 8296
    assert {r["curation_status"] for r in family_nodes} == {"SEEDED"}
    native = [yaml.safe_load(raw) for name, raw in before.items() if name.endswith(".yaml")]
    assert sum(len(record.get("assertions", [])) for record in native) == 0


def test_shared_contracts_on_real_artifacts():
    from kg_microbe_kgx import contract as kgx
    from kg_microbe_sssom import contract as sssom

    assert sssom._slot_names(), "sssom-schema must be installed; empty-slot fallback is not validation"
    assert kgx.check_graph(REPO_ROOT / exports.KGX_NODES, REPO_ROOT / exports.KGX_EDGES) == []
    assert sssom.check_file(REPO_ROOT / exports.SSSOM) == []
