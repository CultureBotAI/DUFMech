from __future__ import annotations

import json
import shutil
import subprocess

import pytest

from dufmech import site_source_publication as publication
from dufmech.report import ReportError
from dufmech.site_sources import LEDGER, capture_source_pins
from tests.test_report import freeze_worklist
from tests.test_site_sources import git


@pytest.fixture
def published(tmp_path, monkeypatch):
    root = tmp_path / "repository"
    root.mkdir()
    git(root, "init", "-q")
    worklist = freeze_worklist(root / "data/worklists")
    git(root, "add", ".")
    git(root, "commit", "-qm", "Frozen sources")
    checkpoint = git(root, "rev-parse", "HEAD")
    remote = tmp_path / "canonical.git"
    git(tmp_path, "init", "--bare", str(remote))
    git(root, "push", str(remote), f"{checkpoint}:refs/heads/main")
    monkeypatch.setattr(publication, "PUBLICATION_URL", str(remote))
    capture_source_pins(root, checkpoint)
    return root, worklist, checkpoint, remote


def new_checkpoint(root, worklist):
    worklist.write_text(worklist.read_text() + "\n")
    git(root, "add", str(worklist))
    git(root, "commit", "-qm", "New source checkpoint")
    checkpoint = git(root, "rev-parse", "HEAD")
    capture_source_pins(root, checkpoint)
    return checkpoint


def test_main_ancestor_and_cli_receipt(published, capsys):
    root, _, checkpoint, remote = published
    git(root, "commit", "--allow-empty", "-qm", "Later main")
    git(root, "push", str(remote), "HEAD:refs/heads/main")
    before = git(root, "show-ref")
    assert publication.main(["--root", str(root)]) == 0
    result = json.loads(capsys.readouterr().out)
    assert result == {"repository": publication.REPOSITORY, "commit": checkpoint,
                      "retained_by": "refs/heads/main", "files": 3}
    assert git(root, "show-ref") == before


@pytest.mark.parametrize("retention", ["branch", "local-tag", "lightweight", "other-namespace",
                                      "descendant-tag"])
def test_branch_local_lightweight_and_indirect_tags_are_not_retention(published, retention):
    root, worklist, _, remote = published
    checkpoint = new_checkpoint(root, worklist)
    git(root, "push", str(remote), f"{checkpoint}:refs/heads/feature")
    tag = "source/dufmech-fixture"
    if retention != "branch":
        if retention == "descendant-tag":
            git(root, "commit", "--allow-empty", "-qm", "Later checkpoint")
        if retention == "other-namespace":
            tag = "unrelated/fixture"
        args = (tag,) if retention == "lightweight" else ("-a", tag, "-m", "Retained source")
        git(root, "tag", *args)
        if retention != "local-tag":
            git(root, "push", str(remote), f"refs/tags/{tag}")
    with pytest.raises(ReportError, match="not retained on canonical main"):
        publication.check_published_source_pins(root)


def test_annotated_checkpoint_survives_squash_and_branch_deletion_but_not_tag_deletion(published):
    root, worklist, _, remote = published
    checkpoint = new_checkpoint(root, worklist)
    tag = "source/dufmech-pr-fixture"
    git(root, "tag", "-a", tag, "-m", "Retained source", checkpoint)
    git(root, "push", str(remote), f"refs/tags/{tag}", f"{checkpoint}:refs/heads/feature")
    git(root, "checkout", "--orphan", "squashed")
    git(root, "add", ".")
    git(root, "commit", "-qm", "Squash merge")
    git(root, "push", "--force", str(remote), "HEAD:refs/heads/main", ":refs/heads/feature")
    result = publication.check_published_source_pins(root)
    assert result["commit"] == checkpoint
    assert result["retained_by"] == f"refs/tags/{tag}"
    git(root, "push", str(remote), f":refs/tags/{tag}")
    with pytest.raises(ReportError, match="not retained"):
        publication.check_published_source_pins(root)


@pytest.mark.parametrize("damage", ["wrong-commit", "missing-file", "symlink-blob"])
def test_published_commit_must_contain_actual_pinned_blobs(published, damage):
    root, worklist, original, remote = published
    if damage == "symlink-blob":
        contents = worklist.read_bytes()
        worklist.unlink()
        worklist.symlink_to("elsewhere.json")
    elif damage == "missing-file":
        worklist.unlink()
    else:
        worklist.write_text(worklist.read_text() + "\n")
    git(root, "add", "data/worklists")
    git(root, "commit", "-qm", "Different published sources")
    changed = git(root, "rev-parse", "HEAD")
    git(root, "push", str(remote), "HEAD:refs/heads/main")
    if damage == "wrong-commit":
        capture_source_pins(root, changed)
        alleged = original
    else:
        if damage == "symlink-blob":
            worklist.unlink()
            worklist.write_bytes(contents)
        else:
            git(root, "restore", f"--source={original}", "--", str(worklist))
        alleged = changed
    ledger = root / LEDGER
    payload = json.loads(ledger.read_text())
    payload["commit"] = alleged
    ledger.write_text(json.dumps(payload))
    with pytest.raises(ReportError, match="published source checkpoint bytes differ"):
        publication.check_published_source_pins(root)


def test_archive_has_no_checkout_dependency_or_inherited_git_proof(published, monkeypatch, tmp_path):
    root, _, checkpoint, _ = published
    # Configuration/environment poisoning must not redirect the independent verification.
    config = tmp_path / "gitconfig"
    config.write_text('[url "file:///nonexistent/"]\n\tinsteadOf = /\n')
    monkeypatch.setenv("GIT_CONFIG_GLOBAL", str(config))
    monkeypatch.setenv("GIT_DIR", str(root / "missing-git-directory"))
    monkeypatch.setenv("GIT_CONFIG_COUNT", "1")
    monkeypatch.setenv("GIT_CONFIG_KEY_0", "core.repositoryFormatVersion")
    monkeypatch.setenv("GIT_CONFIG_VALUE_0", "999")
    shutil.rmtree(root / ".git")
    assert publication.check_published_source_pins(root)["commit"] == checkpoint


def test_offline_or_missing_canonical_main_fails_closed(published, monkeypatch, capsys):
    root, _, _, remote = published
    git(remote, "update-ref", "-d", "refs/heads/main")
    with pytest.raises(SystemExit) as error:
        publication.main(["--root", str(root)])
    assert error.value.code == 1
    assert "git fetch failed" in capsys.readouterr().err
    monkeypatch.setattr(publication, "PUBLICATION_URL", str(remote / "missing"))
    with pytest.raises(ReportError, match="git fetch failed"):
        publication.check_published_source_pins(root)


@pytest.mark.parametrize("failure", [OSError("no git"), subprocess.TimeoutExpired("git", 180)])
def test_git_execution_errors_are_validation_failures(published, monkeypatch, failure):
    root, _, _, _ = published

    def fail(*args, **kwargs):
        raise failure

    monkeypatch.setattr(subprocess, "run", fail)
    with pytest.raises(ReportError, match="git init failed"):
        publication.check_published_source_pins(root)


def test_bad_ledger_is_rejected_before_any_network(published, monkeypatch):
    root, worklist, _, _ = published
    worklist.write_text("modified source\n")
    monkeypatch.setattr(subprocess, "run", lambda *a, **kw: pytest.fail("unexpected Git call"))
    with pytest.raises(ReportError, match="site source pin bytes differ"):
        publication.check_published_source_pins(root)
