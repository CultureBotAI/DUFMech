from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from threading import Event

import pytest

from dufmech import pages
from dufmech.report import ReportError
from dufmech.site_contract import check_site
from dufmech.site_files import (
    MANIFEST,
    PENDING,
    SiteTree,
    output_lock,
    prepare_files,
    remove_obsolete,
)
from tests.test_report import worklist_row


def render(out, count):
    pages.render_site([worklist_row(f"PF{i:05d}", proteins=i) for i in range(1, count + 1)],
                      [], input_ids={}, out_dir=out)


def assert_manifest_matches(out):
    manifest = json.loads((out / MANIFEST).read_text())
    assert all(hashlib.sha256((out / name).read_bytes()).hexdigest() == digest
               for name, digest in manifest.items())


def test_concurrent_render_waits_for_full_ownership_and_cleanup_transaction(tmp_path, monkeypatch):
    out = tmp_path / "site"
    render(out, 2)
    first_prepared, second_prepared, release = Event(), Event(), Event()

    def paused_prepare(artifacts, target, *, tree=None):
        result = prepare_files(artifacts, target, tree=tree)
        if "families/PF00002.html" not in artifacts:
            first_prepared.set()
            assert release.wait(10)
        else:
            second_prepared.set()
        return result

    monkeypatch.setattr(pages, "prepare_files", paused_prepare)
    with ThreadPoolExecutor(max_workers=2) as pool:
        first = pool.submit(render, out, 1)
        assert first_prepared.wait(10)
        second = pool.submit(render, out, 3)
        try:
            assert not second_prepared.wait(1), "second writer bypassed the transaction lock"
        finally:
            release.set()
        first.result(timeout=10)
        second.result(timeout=10)
    assert_manifest_matches(out)
    assert (out / "families/PF00002.html").exists()
    assert (out / "families/PF00003.html").exists()


def test_failed_partial_cleanup_retains_ownership_and_retry_removes_remaining_pages(tmp_path, monkeypatch):
    out = tmp_path / "site"
    render(out, 3)
    previous_manifest = (out / MANIFEST).read_bytes()

    def failing_cleanup(stale, target, *, tree=None):
        remove_obsolete(stale[:1], target, tree=tree)
        raise OSError("injected cleanup failure")

    monkeypatch.setattr(pages, "remove_obsolete", failing_cleanup)
    with pytest.raises(OSError, match="injected cleanup failure"):
        render(out, 1)
    assert (out / MANIFEST).read_bytes() == previous_manifest
    assert not (out / "families/PF00002.html").exists()
    assert (out / "families/PF00003.html").exists()
    monkeypatch.setattr(pages, "remove_obsolete", remove_obsolete)
    render(out, 1)
    assert not list((out / "families").glob("PF0000[23].*"))
    assert_manifest_matches(out)


def test_obsolete_file_is_rechecked_immediately_before_deletion(tmp_path, monkeypatch):
    out = tmp_path / "site"
    render(out, 2)
    previous_manifest = (out / MANIFEST).read_bytes()
    obsolete = out / "families/PF00002.html"

    def changed_after_prepare(stale, target, *, tree=None):
        obsolete.write_text("user changed this during rendering")
        remove_obsolete(stale, target, tree=tree)

    monkeypatch.setattr(pages, "remove_obsolete", changed_after_prepare)
    with pytest.raises(ReportError, match="changed obsolete page"):
        render(out, 1)
    assert obsolete.read_text() == "user changed this during rendering"
    assert (out / MANIFEST).read_bytes() == previous_manifest


def test_stale_file_parent_symlink_is_rechecked(tmp_path):
    out = tmp_path / "site"
    render(out, 2)
    path = out / "families/PF00002.html"
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    external = tmp_path / "external"
    (out / "families").rename(external)
    (out / "families").symlink_to(external, target_is_directory=True)
    with pytest.raises(ReportError, match="symlink"):
        remove_obsolete([(path, digest)], out)
    assert (external / "PF00002.html").exists()


@pytest.mark.parametrize("existing", [False, True])
def test_failed_manifest_publication_reconciles_new_files_on_different_target(tmp_path, monkeypatch, existing):
    out = tmp_path / "site"
    if existing:
        render(out, 1)
    original = SiteTree.replace_from

    def fail_manifest(self, staged, relative):
        if relative == MANIFEST:
            raise OSError("injected final manifest failure")
        original(self, staged, relative)

    monkeypatch.setattr(SiteTree, "replace_from", fail_manifest)
    with pytest.raises(OSError, match="injected final manifest"):
        render(out, 2)
    assert (out / PENDING).exists()
    assert (out / "families/PF00002.html").exists()
    monkeypatch.setattr(SiteTree, "replace_from", original)
    render(out, 1)
    assert not (out / PENDING).exists()
    assert not list((out / "families").glob("PF00002.*"))
    assert_manifest_matches(out)


def test_pending_updated_file_can_be_removed_but_user_edits_are_never_deleted(tmp_path, monkeypatch):
    out = tmp_path / "site"
    render(out, 2)
    original = SiteTree.replace_from

    def fail_manifest(self, staged, relative):
        if relative == MANIFEST:
            raise OSError("injected final manifest failure")
        original(self, staged, relative)

    monkeypatch.setattr(SiteTree, "replace_from", fail_manifest)
    with pytest.raises(OSError):
        pages.render_site([worklist_row("PF00002", proteins=987)], [], input_ids={}, out_dir=out)
    updated = out / "families/PF00002.html"
    retained = updated.read_bytes()
    updated.write_text("user modification after interrupted render")
    monkeypatch.setattr(SiteTree, "replace_from", original)
    with pytest.raises(ReportError, match="modified pending page"):
        render(out, 1)
    assert updated.read_text() == "user modification after interrupted render"
    updated.write_bytes(retained)
    render(out, 1)
    assert not updated.exists()
    assert_manifest_matches(out)


def test_processes_with_different_tmpdirs_share_destination_lock(tmp_path):
    out = tmp_path / "site"
    alternate = tmp_path / "different-tmpdir"
    alternate.mkdir()
    code = """from pathlib import Path
import sys
from dufmech.site_files import output_lock
print('WAITING', flush=True)
with output_lock(Path(sys.argv[1])):
    print('ACQUIRED', flush=True)
"""
    with output_lock(out):
        process = subprocess.Popen(
            [sys.executable, "-c", code, str(out)], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, env={**os.environ, "TMPDIR": str(alternate),
                            "PYTHONPATH": str(Path(__file__).resolve().parents[1] / "src")},
        )
        try:
            assert process.stdout.readline().strip() == "WAITING"
            with pytest.raises(subprocess.TimeoutExpired):
                process.wait(timeout=0.3)
        except BaseException:
            process.kill()
            process.communicate()
            raise
    stdout, stderr = process.communicate(timeout=10)
    assert process.returncode == 0, stderr
    assert "ACQUIRED" in stdout


@pytest.mark.parametrize("component", ["family-parent", "site-root"])
def test_parent_swap_at_replace_never_writes_to_symlink_target(tmp_path, monkeypatch, component):
    out, external = tmp_path / "site", tmp_path / "external"
    render(out, 1)
    external.mkdir()
    (external / "sentinel").write_text("untouched")
    original = os.replace
    swapped = False

    def swap_parent(source, target, **kwargs):
        nonlocal swapped
        if target == "PF00001.html" and not swapped:
            swapped = True
            parent = out / "families" if component == "family-parent" else out
            parent.rename(tmp_path / "displaced")
            parent.symlink_to(external, target_is_directory=True)
        return original(source, target, **kwargs)

    monkeypatch.setattr(os, "replace", swap_parent)
    with pytest.raises(ReportError, match="symlink|replaced during rendering"):
        render(out, 2)
    assert swapped
    assert sorted(path.name for path in external.iterdir()) == ["sentinel"]
    assert (external / "sentinel").read_text() == "untouched"


@pytest.mark.parametrize("leftover", [PENDING, ".dufmech-stage-interrupted"])
def test_site_contract_rejects_interrupted_transactions(tmp_path, leftover):
    out = tmp_path / "site"
    render(out, 1)
    (out / leftover).write_text("{}")
    errors, _ = check_site(out, json.loads(Path("conf/pages_budgets.json").read_text()))
    assert any("unfinished render" in error for error in errors)


@pytest.mark.parametrize("existing", [False, True])
@pytest.mark.parametrize("stop_at", ["BEFORE_PENDING", PENDING, "families/PF00002.html", MANIFEST])
def test_abrupt_process_exit_leaves_no_staging_inside_recovered_publication(tmp_path, stop_at, existing):
    out = tmp_path / "site"
    if existing:
        render(out, 1)
    code = """from pathlib import Path
import os, sys
from dufmech.site_files import PENDING, SiteTree
from tests.test_site_writes import render
original = SiteTree.replace_from
def interrupted(self, staged, relative):
    if relative == PENDING and sys.argv[2] == 'BEFORE_PENDING':
        os._exit(73)
    original(self, staged, relative)
    if relative == sys.argv[2]:
        os._exit(73)
SiteTree.replace_from = interrupted
render(Path(sys.argv[1]), 2)
"""
    root = Path(__file__).resolve().parents[1]
    process = subprocess.run([sys.executable, "-c", code, str(out), stop_at], check=False,
                             capture_output=True, text=True, cwd=root,
                             env={**os.environ, "PYTHONPATH": f"{root / 'src'}{os.pathsep}{root}"})
    assert process.returncode == 73, process.stderr
    assert (out / PENDING).exists() == (stop_at != "BEFORE_PENDING")
    assert not list(out.glob("*dufmech-stage*"))
    render(out, 1)
    clean = tmp_path / "clean"
    render(clean, 1)
    assert pages.diff_trees(clean, out) == []
    assert_manifest_matches(out)


def test_staging_failure_never_displaces_existing_output(tmp_path, monkeypatch):
    out, clean = tmp_path / "site", tmp_path / "clean"
    render(out, 1)
    render(clean, 1)
    original = SiteTree.write_new

    def fail_staging(self, relative, content):
        original(self, relative, content)
        if relative == "families/PF00002.html":
            raise OSError("injected staging failure")

    monkeypatch.setattr(SiteTree, "write_new", fail_staging)
    with pytest.raises(OSError, match="injected staging failure"):
        render(out, 2)
    assert pages.diff_trees(clean, out) == []
    assert not list(tmp_path.glob(".site.dufmech-stage-*"))
