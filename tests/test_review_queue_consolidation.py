"""Regression guards for byte-preserving review consolidation, issues #459/#460."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parents[1] / "scripts/adhoc/consolidate_review_queue_20261116.py"
spec = importlib.util.spec_from_file_location("review_consolidation", SCRIPT)
assert spec and spec.loader
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


@pytest.fixture
def prepared(tmp_path, monkeypatch):
    root = tmp_path / "repository"
    root.mkdir()
    output = {"reviews/structured/example/review.md": b"Retained prose.\n",
              "reviews/structured/example/review.yaml": b"retained: source bytes\n"}
    files = [{"path": name, "status": "A", "mode": "100644",
              "blob": hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest(),
              "sha256": hashlib.sha256(raw).hexdigest(), "size": len(raw)}
             for name, raw in output.items()]
    payload = {"schema_version": 1, "repository": "CultureBotAI/DUFMech", "date": "2026-11-16",
               "issues": [459, 460], "base_main": "a" * 40, "expected_pr_count": 1,
               "expected_file_count": 2, "prs": [{"number": 1, "head": "b" * 40,
               "base": "a" * 40, "merge_base": "a" * 40, "files": files}]}
    inventory = root / "inventory.json"
    inventory.write_text(json.dumps(payload))
    monkeypatch.setattr(helper, "PR_COUNT", 1)
    monkeypatch.setattr(helper, "FILES_PER_PR", 2)
    monkeypatch.setattr(helper, "FILE_COUNT", 2)

    def git(_root, *args, input_bytes=None):
        if args[0] == "remote":
            return b"https://github.com/CultureBotAI/DUFMech.git\n"
        if args[:2] == ("rev-parse", "--show-toplevel"):
            return str(root).encode() + b"\n"
        if args[:2] == ("merge-base", "--is-ancestor") or args[0] == "check-ignore":
            return b""
        if args[0] == "merge-base":
            return b"a" * 40 + b"\n"
        if args[0] == "diff-tree":
            return b"".join(
                f":000000 100644 {'0' * 40} {f['blob']} A\0{f['path']}\0".encode()
                for f in files)
        if args[0] == "cat-file":
            by_id = {f["blob"]: output[f["path"]] for f in files}
            return b"".join(f"{oid} blob {len(by_id[oid])}\n".encode() + by_id[oid] + b"\n"
                            for oid in input_bytes.decode().splitlines())
        raise AssertionError(args)

    monkeypatch.setattr(helper, "git", git)
    return root, inventory, payload, output


def test_dry_run_and_verify_do_not_create_missing_files(prepared):
    root, inventory, _, output = prepared
    receipt = helper.consolidate(root, inventory)
    assert receipt["created"] == 0 and receipt["missing_before"] == 2
    assert all(not (root / name).exists() for name in output)
    with pytest.raises(helper.ConsolidationError, match="2 indexed files are missing"):
        helper.consolidate(root, inventory, verify=True)
    assert not (root / "reviews").exists()


def test_apply_preserves_bytes_and_verify_is_idempotent(prepared):
    root, inventory, _, output = prepared
    assert helper.consolidate(root, inventory, apply=True)["created"] == 2
    assert {name: (root / name).read_bytes() for name in output} == output
    assert helper.consolidate(root, inventory, apply=True)["created"] == 0
    assert helper.consolidate(root, inventory, verify=True)["already_present"] == 2


def test_last_destination_conflict_prevents_every_write(prepared):
    root, inventory, _, output = prepared
    names = list(output)
    conflict = root / names[-1]
    conflict.parent.mkdir(parents=True)
    conflict.write_bytes(b"unrelated local changes")
    with pytest.raises(helper.ConsolidationError, match="existing destination bytes differ"):
        helper.consolidate(root, inventory, apply=True)
    assert not (root / names[0]).exists()
    assert conflict.read_bytes() == b"unrelated local changes"


def test_symlink_parent_is_rejected_without_following_it(prepared):
    root, inventory, _, _ = prepared
    elsewhere = root / "elsewhere"
    elsewhere.mkdir()
    (root / "reviews").symlink_to(elsewhere, target_is_directory=True)
    with pytest.raises(helper.ConsolidationError, match="symlink path refused"):
        helper.consolidate(root, inventory, apply=True)
    assert list(elsewhere.iterdir()) == []


def test_source_hash_mismatch_prevents_all_writes(prepared):
    root, inventory, payload, _ = prepared
    payload["prs"][0]["files"][-1]["sha256"] = "f" * 64
    inventory.write_text(json.dumps(payload))
    with pytest.raises(helper.ConsolidationError, match="source byte proof differs"):
        helper.consolidate(root, inventory, apply=True)
    assert not (root / "reviews").exists()


def test_inventory_requires_exact_pairs_and_unique_paths(prepared):
    _, inventory, payload, _ = prepared
    bad = copy.deepcopy(payload)
    bad["prs"][0]["files"][-1]["path"] = "reviews/structured/other/review.yaml"
    inventory.write_text(json.dumps(bad))
    with pytest.raises(helper.ConsolidationError, match="missing YAML/Markdown partner"):
        helper.load_inventory(inventory)
    bad["prs"][0]["files"][-1]["path"] = bad["prs"][0]["files"][0]["path"]
    inventory.write_text(json.dumps(bad))
    with pytest.raises(helper.ConsolidationError, match="unsafe or duplicate review path"):
        helper.load_inventory(inventory)


def test_duplicate_json_keys_are_rejected(prepared):
    _, inventory, _, _ = prepared
    inventory.write_text('{"schema_version":1,"schema_version":1}')
    with pytest.raises(helper.ConsolidationError, match="duplicate JSON key"):
        helper.load_inventory(inventory)


def test_late_create_failure_rolls_back_only_owned_files(prepared, monkeypatch):
    root, inventory, _, output = prepared
    link = helper.os.link
    calls = 0

    def fail_second(source, destination):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("simulated exclusive creation failure")
        return link(source, destination)

    monkeypatch.setattr(helper.os, "link", fail_second)
    with pytest.raises(OSError, match="simulated exclusive creation"):
        helper.consolidate(root, inventory, apply=True)
    assert all(not (root / name).exists() for name in output)
