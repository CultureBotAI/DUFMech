"""DUFMech #400/#401, 2026-11-07: offline helper safety regressions.

Run in the separate locked CLAW runtime, where native repository/lock adapters
are supported. Inputs: this PR's helper, release and retained candidate context.
Outputs: six unittest results; all writes use disposable synthetic repositories.
No providers, remote Git requests, real leases, source edits or session inputs.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[1]
CLAW = Path(os.environ["CLAW_ROOT"]).resolve(strict=True)
sys.path.insert(0, str(CLAW))
from plugins.lock_manager import LockManager

BASE = "5642a645349854802748ae387c0e2df121c5e83f"


def initialize_repository(root, repository):
    root.mkdir(parents=True, exist_ok=True)
    for args in (("init", "-b", "feat/cycle-v2-canary-20261107"),
                 ("config", "user.name", "Contract fixture"),
                 ("config", "user.email", "fixture@example.invalid"),
                 ("remote", "add", "origin", f"https://github.com/{repository}.git")):
        subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)


def fixture_commit(root):
    subprocess.run(["git", "add", "."], cwd=root, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", "Contract fixture"], cwd=root,
                   check=True, capture_output=True)
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()


class PreparationSafety(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="duf-cycle-v2-contract-")
        self.addCleanup(temporary.cleanup)
        self.temporary = Path(temporary.name)
        path = ROOT / "scripts/adhoc/prepare_cycle_v2_canary.py"
        spec = importlib.util.spec_from_file_location("cycle_v2_preparation", path)
        self.helper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.helper)

    def assert_interference_refused(self, interference):
        helper = self.helper
        target = self.temporary / "target"
        initialize_repository(target, "CultureBotAI/DUFMech")
        relatives = (helper.PROFILE, "workflow/parent/mech-cycle.yaml",
                     "workflow/parent/workflow.yaml", helper.TRIAGE)
        desired = {p: (ROOT / p).read_text() for p in relatives}
        for stage in yaml.safe_load(desired[helper.PROFILE])["stages"]:
            for relative in stage["skill_paths"]:
                if relative != helper.TRIAGE:
                    path = target / relative
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes((ROOT / relative).read_bytes())
        profile = target / helper.PROFILE
        profile.parent.mkdir(parents=True, exist_ok=True)
        original = desired[helper.PROFILE] + "\n# original context\n"
        profile.write_text(original)
        base = fixture_commit(target)
        concurrent = "# preserve this concurrent writer's note\n"

        @contextmanager
        def competing_writer(_self, *_args, **_kwargs):
            if interference == "edit":
                profile.write_text(original + concurrent)
            elif interference == "new-file":
                path = target / helper.TRIAGE
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(concurrent)
            elif interference == "branch":
                subprocess.run(["git", "switch", "-c", "other-owner"], cwd=target,
                               check=True, capture_output=True)
            else:
                subprocess.run(["git", "remote", "set-url", "origin",
                                "https://github.com/Example/Other.git"], cwd=target,
                               check=True, capture_output=True)
            yield

        argv = ["prepare", "--claw-root", str(CLAW), "--target-root", str(target),
                "--issue-context", "unused", "--pr-context", "unused",
                "--report-dir", str(self.temporary / "report"), "--apply"]
        with (patch.object(helper, "BASE", base),
              patch.object(helper, "OUTPUT_PATHS", relatives, create=True),
              patch.object(helper, "INPUT_PATHS", relatives, create=True),
              patch.object(helper, "prepare", return_value=desired),
              patch.object(LockManager, "lock", competing_writer),
              patch.object(sys, "argv", argv),
              self.assertRaisesRegex((RuntimeError, ValueError), "Concurrent|branch|origin|identity")):
            helper.main()
        self.assertEqual(profile.read_text(), original + (concurrent if interference == "edit" else ""))
        self.assertFalse((target / "workflow/parent/mech-cycle.yaml").exists())
        if interference == "new-file":
            self.assertEqual((target / helper.TRIAGE).read_text(), concurrent)

    def test_concurrent_edit_preserved(self):
        self.assert_interference_refused("edit")

    def test_new_destination_preserved(self):
        self.assert_interference_refused("new-file")

    def test_changed_branch_refused(self):
        self.assert_interference_refused("branch")

    def test_changed_origin_refused(self):
        self.assert_interference_refused("origin")

    def test_release_blob_ignores_mutable_checkout(self):
        root = self.temporary / "release"
        initialize_repository(root, "CultureBotAI/culturebotai-claw")
        path = root / "asset.md"
        path.write_text("committed canonical bytes\n")
        revision = fixture_commit(root)
        path.write_text("unreviewed working-tree bytes\n")
        with patch.object(self.helper, "RELEASE", revision):
            self.assertEqual(self.helper.release_blob(root, "asset.md"), "committed canonical bytes\n")

    def test_prepare_rejects_dirty_release_at_unchanged_head(self):
        helper = self.helper
        source = self.temporary / "release"
        initialize_repository(source, "CultureBotAI/culturebotai-claw")
        assets = ("src/kg_microbe_workflows/templates/mech-cycle.yaml",
                  "src/kg_microbe_workflows/schema/workflow.yaml",
                  "src/kg_microbe_skills/canonical/evolve-mech-workflow.md",
                  "src/kg_microbe_skills/canonical/triage-and-resolve-issues.md")
        for relative in assets:
            path = source / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes((CLAW / relative).read_bytes())
        revision = fixture_commit(source)
        target = self.temporary / "target"
        initialize_repository(target, "CultureBotAI/DUFMech")
        for relative in (helper.PROFILE, helper.ADAPTATION, ".github/workflows/validate.yaml"):
            path = target / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(subprocess.check_output(["git", "show", f"{BASE}:{relative}"], cwd=ROOT))
        pin = target / "scripts/.vendored_canon_ref"
        pin.parent.mkdir(parents=True, exist_ok=True)
        pin.write_text(revision + "\n")
        base = fixture_commit(target)
        context = json.loads((ROOT / helper.REVIEW / "backlog-context.json").read_text())
        for filename, key in (("issues", "issues"), ("prs", "open_prs")):
            (self.temporary / filename).write_text(json.dumps({
                "observed_at": context["issues_observed_at"], "data": context[key],
            }))
        path = source / assets[0]
        original = path.read_text()
        changed = original.replace("deferred_budget_seconds: 14400", "deferred_budget_seconds: 28800")
        self.assertNotEqual(original, changed)
        path.write_text(changed)
        self.assertEqual(subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source,
                                                text=True).strip(), revision)
        args = argparse.Namespace(claw_root=source, target_root=target,
                                  issue_context=self.temporary / "issues", pr_context=self.temporary / "prs")
        with (patch.object(helper, "RELEASE", revision), patch.object(helper, "BASE", base),
              self.assertRaisesRegex(RuntimeError, "released CLAW source checkout must be clean")):
            helper.prepare(args)


if __name__ == "__main__":
    unittest.main(verbosity=2)
