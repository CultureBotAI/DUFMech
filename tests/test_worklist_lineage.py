from __future__ import annotations

import json
import os
import shutil
from dataclasses import replace
from pathlib import Path

import pytest

from dufmech.exduf import prepare_migration
from dufmech.reclassify import prepare_reclassification
from dufmech.report import ReportError, verified_manifest
from dufmech.score_inputs import ScoreInputError, load_score_input
from dufmech.snapshot import write_worklist_snapshot
from tests.test_exduf import PARENT, T0, _fetch, _inputs, _rewrite, _row, _write


def _derived(tmp_path: Path, kind: str) -> tuple[Path, Path]:
    parent, previous = _inputs(tmp_path)
    if kind == "reclassification":
        prepared = prepare_reclassification(parent, snapshot_date="2026-10-08", generated_at=T0)
    else:
        prepared = prepare_migration(parent, previous, snapshot_date="2026-10-08",
                                     fetch=_fetch, generated_at=T0)
    return parent, _write(parent.parent, prepared.artifacts)


def _reject(path: Path, match: str) -> None:
    with pytest.raises(ScoreInputError, match=match):
        load_score_input(path, "worklist")
    with pytest.raises(ReportError, match=match):
        verified_manifest(path)


@pytest.mark.parametrize("kind", ["reclassification", "migration"])
@pytest.mark.parametrize("field,value", [("description", "changed"), ("short_name", "DUF999"),
                                         ("proteins", 999)])
def test_changed_metadata_cannot_hide_behind_consistent_child_hashes(tmp_path, kind, field, value):
    _, child = _derived(tmp_path, kind)
    rows = json.loads(child.read_text())
    rows[0][field] = value
    _rewrite(child, rows=rows)
    _reject(child, "derived metadata differs")


@pytest.mark.parametrize("kind", ["reclassification", "migration"])
@pytest.mark.parametrize("operation", ["add", "drop"])
def test_parent_membership_is_verified(tmp_path, kind, operation):
    _, child = _derived(tmp_path, kind)
    rows = json.loads(child.read_text())
    if operation == "drop":
        rows = [row for row in rows if row["pfam_id"] != "PF01519"]
    else:
        rows.append({**rows[0], "pfam_id": "PF99991",
                     "source_url": "https://www.ebi.ac.uk/interpro/entry/pfam/PF99991/"})
    _rewrite(child, rows=rows, mutate=lambda m: m["rows"].update(total=len(rows)))
    _reject(child, "membership differs")


@pytest.mark.parametrize("kind", ["reclassification", "migration"])
def test_parent_hash_is_verified_and_detached_snapshots_remain_portable(tmp_path, kind):
    parent, child = _derived(tmp_path, kind)
    detached = tmp_path / "detached"
    detached.mkdir()
    for suffix in (".json", ".tsv", ".manifest.json"):
        shutil.copyfile(child.with_suffix(suffix), detached / child.with_suffix(suffix).name)
    assert load_score_input(detached / child.name, "worklist")
    assert verified_manifest(detached / child.name)
    parent.write_bytes(parent.read_bytes() + b"\n")
    _reject(child, "recorded parent hash")


@pytest.mark.parametrize("replacement", ["symlink", "dangling_symlink", "directory", "fifo"])
def test_nonregular_parents_are_rejected_without_blocking(tmp_path, replacement):
    parent, child = _derived(tmp_path, "migration")
    backup = parent.with_suffix(".saved")
    parent.rename(backup)
    if replacement.endswith("symlink"):
        parent.symlink_to(backup if replacement == "symlink" else tmp_path / "absent")
    elif replacement == "directory":
        parent.mkdir()
    else:
        os.mkfifo(parent)
    _reject(child, "worklist parent")


@pytest.mark.parametrize("key", ["added_pfam_ids", "carried_pfam_ids", "refreshed_pfam_ids"])
def test_migration_cannot_exempt_unchanged_rows_with_false_bookkeeping(tmp_path, key):
    _, child = _derived(tmp_path, "migration")
    _rewrite(child, mutate=lambda m: m["derivation"][key].append("PF06172"))
    _reject(child, "membership|requires a live")


def test_reclassification_change_counts_are_checked_against_parent(tmp_path):
    _, child = _derived(tmp_path, "reclassification")
    _rewrite(child, mutate=lambda m: m["derivation"].update(changed_reason_rows=999))
    _reject(child, "change summary differs")


def test_migration_before_reasons_are_checked_against_parent(tmp_path):
    _, child = _derived(tmp_path, "migration")
    _rewrite(child, mutate=lambda m: m["derivation"]["changes"][0].update(before_reasons=[]))
    _reject(child, "change log differs")


def test_live_refresh_uses_live_metadata_and_checks_membership_logs(tmp_path):
    parent, previous = _inputs(tmp_path)
    live_rows = [replace(PARENT[1], proteins=42), _row("PF99991", "DUF999", "DUF999")]
    write_worklist_snapshot(live_rows, parent.parent, snapshot_date="2026-10-06", generated_at=T0)
    live = parent.parent / "interpro-pfam-duf-2026-10-06.json"
    from tests.test_exduf import _detail

    def fetch(ids):
        return {p: (_detail(p, "Cupin_8", "Cupin") if p == "PF06172" else _fetch([p])[p])
                for p in ids}

    prepared = prepare_migration(parent, previous, snapshot_date="2026-10-08", fetch=fetch,
                                 live_json=live, generated_at=T0)
    child = _write(parent.parent, prepared.artifacts)
    assert load_score_input(child, "worklist")
    assert verified_manifest(child)
    rows = json.loads(child.read_text())
    next(row for row in rows if row["pfam_id"] == "PF01519")["proteins"] = 43
    _rewrite(child, rows=rows)
    _reject(child, "derived metadata differs")


def test_real_frozen_worklists_still_validate():
    directory = Path(__file__).resolve().parents[1] / "data/worklists"
    for path in directory.glob("interpro-pfam-duf-*.json"):
        if not path.name.endswith(".manifest.json"):
            assert load_score_input(path, "worklist")
            assert verified_manifest(path)


@pytest.mark.parametrize("section", ["snapshot", "input_snapshot_ids"])
@pytest.mark.parametrize("value", [None, [], "not-an-object"])
def test_malformed_parent_metadata_returns_validation_errors(tmp_path, section, value):
    _, child = _derived(tmp_path, "migration")
    def mutate(manifest):
        if section == "snapshot":
            manifest[section] = value
        else:
            manifest["snapshot"][section] = value
    _rewrite(child, mutate=mutate)
    _reject(child, "snapshot|parent")


@pytest.mark.parametrize("value", [{}, [], None, True, 1])
def test_malformed_derivation_method_returns_validation_errors(tmp_path, value):
    _, child = _derived(tmp_path, "migration")
    _rewrite(child, mutate=lambda m: m["derivation"].update(method=value))
    _reject(child, "method|reclassification")
