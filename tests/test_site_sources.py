from __future__ import annotations

import json
import shutil
import subprocess

import pytest

from dufmech import pages
from dufmech.report import ReportError
from dufmech.site_data import tracked_source, tracked_tree
from dufmech.site_sources import LEDGER, capture_source_pins, load_source_pins, main
from tests.test_report import freeze_worklist


def git(root, *args):
    return subprocess.run(
        ["git", "-C", str(root), "-c", "user.name=Site test", "-c", "user.email=site@example.invalid",
         "-c", "commit.gpgsign=false", *args], check=True, capture_output=True, text=True,
    ).stdout.strip()


@pytest.fixture
def repository(tmp_path):
    root = tmp_path / "repository"
    root.mkdir()
    git(root, "init", "-q")
    worklist = freeze_worklist(root / "data/worklists")
    git(root, "add", ".")
    git(root, "commit", "-qm", "Frozen sources")
    return root, worklist, git(root, "rev-parse", "HEAD")


def test_render_pins_survive_source_render_commits_and_squashed_history(repository, monkeypatch):
    root, worklist, checkpoint = repository
    monkeypatch.setattr(pages, "REPO_ROOT", root)
    capture_source_pins(root, checkpoint)
    out = root / "pages"

    def render():
        pages.render_from_paths(out_dir=out, worklists_dir=worklist.parent,
                                cross_mech_dir=root / "data/cross_mech")

    render()
    first = {path.relative_to(out): path.read_bytes() for path in out.rglob("*") if path.is_file()}
    assert f"/blob/{checkpoint}/" in (out / "index.html").read_text()
    git(root, "add", ".")
    git(root, "commit", "-qm", "Rendered site and ledger")
    render()
    assert first == {path.relative_to(out): path.read_bytes() for path in out.rglob("*") if path.is_file()}
    git(root, "checkout", "--orphan", "squashed")
    git(root, "commit", "-qm", "Squashed sources, ledger and website")
    assert git(root, "log", "-1", "--format=%H", "--", str(worklist.relative_to(root))) != checkpoint
    render()
    assert first == {path.relative_to(out): path.read_bytes() for path in out.rglob("*") if path.is_file()}
    # A source archive with no Git metadata must be equally reproducible.
    shutil.rmtree(root / ".git")
    monkeypatch.setattr(subprocess, "run", lambda *args, **kwargs: pytest.fail("render invoked Git"))
    render()
    assert first == {path.relative_to(out): path.read_bytes() for path in out.rglob("*") if path.is_file()}


def test_capture_rejects_moving_refs_missing_commits_and_changed_bytes(repository):
    root, worklist, checkpoint = repository
    with pytest.raises(ReportError, match="full lowercase commit SHA"):
        capture_source_pins(root, "HEAD")
    with pytest.raises(ReportError, match="not available"):
        capture_source_pins(root, "a" * 40)
    capture_source_pins(root, checkpoint)
    original = (root / LEDGER).read_bytes()
    worklist.write_text(worklist.read_text() + " ")
    with pytest.raises(ReportError, match="does not match local bytes"):
        capture_source_pins(root, checkpoint)
    assert (root / LEDGER).read_bytes() == original
    with pytest.raises(ReportError, match="pin bytes differ"):
        load_source_pins(root)


def test_capture_checks_ignored_files_and_ledger_missing_new_consumed_source(repository):
    root, _, checkpoint = repository
    capture_source_pins(root, checkpoint)
    extra = root / "data/worklists/ignored.json"
    (root / ".gitignore").write_text("ignored.json\n")
    extra.write_text("[]\n")
    with pytest.raises(ReportError, match="does not match local bytes: data/worklists/ignored.json"):
        capture_source_pins(root, checkpoint)
    with pytest.raises(ReportError, match="absent from explicit pin ledger"):
        tracked_source(extra, root)


@pytest.mark.parametrize("damage", ["path", "hash", "revision", "symlink", "missing"])
def test_invalid_source_ledger_never_silently_falls_back(repository, damage):
    root, worklist, checkpoint = repository
    capture_source_pins(root, checkpoint)
    ledger = root / LEDGER
    payload = json.loads(ledger.read_text())
    if damage == "path":
        payload["files"]["data/worklists/../../secret"] = "0" * 64
    elif damage == "hash":
        payload["files"][str(worklist.relative_to(root))] = "0" * 64
    elif damage == "revision":
        payload["commit"] = "main"
    elif damage == "symlink":
        content = worklist.read_bytes()
        worklist.unlink()
        target = root / "elsewhere.json"
        target.write_bytes(content)
        worklist.symlink_to(target)
    else:
        worklist.unlink()
    ledger.write_text(json.dumps(payload))
    with pytest.raises(ReportError):
        load_source_pins(root)


def test_source_tree_and_cli_pin_record_review_history_schema_bytes(repository, capsys):
    root, _, _ = repository
    sources = ["data/families/PF00001.yaml", "history/PF00001.yaml",
               "reports/yaml_record_review/PF00001.md", "src/dufmech/schema/dufmech.yaml"]
    for relative in sources:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("test fixture\n")
    git(root, "add", ".")
    git(root, "commit", "-qm", "Record fixture sources")
    checkpoint = git(root, "rev-parse", "HEAD")
    assert main(["capture", "--root", str(root), "--commit", checkpoint]) == 0
    assert main(["check", "--root", str(root)]) == 0
    assert "verified" in capsys.readouterr().out
    pins = load_source_pins(root)
    for relative in sources:
        assert tracked_source(root / relative, root, pins=pins)["commit"] == checkpoint
    assert set(tracked_tree(root / "data/families", root, pins=pins)) == {sources[0]}
    ledger_text = (root / LEDGER).read_text()
    assert str(root) not in ledger_text
    assert "generated_at" not in ledger_text


def test_no_ledger_is_explicitly_unpinned_not_auto_generated(repository):
    root, worklist, _ = repository
    assert tracked_source(worklist, root) == {}
    assert not (root / LEDGER).exists()
    with pytest.raises(ReportError, match="cannot read"):
        load_source_pins(root, required=True)
