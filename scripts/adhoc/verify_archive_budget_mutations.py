#!/usr/bin/env python3
"""Offline mutation controls for archive budget regressions, #463 (2026-11-16).

Inputs: repository and a new durable output directory outside the source checkout.
Output: copied controls, per-process pytest logs, and checksum-bound results.json.
Only private copies are mutated. No network, provider, Git or live-source writes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root, output = args.repo.resolve(), args.output.resolve()
    if output.exists() or output == root or root in output.parents:
        raise ValueError("output must be a new durable directory outside the source checkout")
    output.mkdir(parents=True)
    shared = ["pyproject.toml", "conf/pages_budgets.json", "tests/test_site_archive_budget.py",
              "tests/test_report.py", "tests/test_scoring_snapshot.py", "scripts/duf_puf_report.py",
              "scripts/adhoc/audit_site_archive_growth.py",
              "docs/provenance/review-queue-archive-budget-20261116.json.gz"]
    cases = {
        "control": None,
        "byte_boundary_rejected": ("src/dufmech/site_contract.py", "if measurements[key] > limits[key]:", "if measurements[key] >= limits[key]:", "test_archive_bytes_accept_boundary_and_reject_one_over"),
        "byte_excess_ignored": ("src/dufmech/site_contract.py", "if measurements[key] > limits[key]:", 'if key != "total_bytes" and measurements[key] > limits[key]:', "test_archive_bytes_accept_boundary_and_reject_one_over"),
        "file_boundary_rejected": ("src/dufmech/site_contract.py", 'len(files) > budgets["generated_file_count"]', 'len(files) >= budgets["generated_file_count"]', "test_archive_files_accept_boundary_and_reject_one_over"),
        "file_excess_ignored": ("src/dufmech/site_contract.py", 'len(files) > budgets["generated_file_count"] or ', "", "test_archive_files_accept_boundary_and_reject_one_over"),
        "old_caps_restored": ("conf/pages_budgets.json", "500000000", "450000000", "test_measured_candidate_requires_archive_capacity_only"),
        "modified_file_omitted": ("scripts/adhoc/audit_site_archive_growth.py", "if old == new:", "if old == new or (old is not None and new is not None):", "test_accounting_covers_added_modified_deleted_and_unchanged_files"),
        "nonblob_guard_removed": ("scripts/adhoc/audit_site_archive_growth.py", 'if any(item["size"] is None for item in [*before.values(), *after.values()]):', "if False:", "test_accounting_refuses_nonblob_site_entries"),
    }
    results = []
    for name, mutation in cases.items():
        case = output / name
        shutil.copytree(root / "src/dufmech", case / "src/dufmech",
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        for relative in shared:
            target = case / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / relative, target)
        (case / "tests/__init__.py").write_text("")
        if mutation:
            relative, old, new, _expected = mutation
            path = case / relative
            text = path.read_text()
            if text.count(old) != 1:
                raise ValueError("mutation anchor not unique: " + name)
            text = text.replace(old, new, 1)
            if name == "old_caps_restored":
                text = text.replace("37000", "36000", 1)
            path.write_text(text)
        env = dict(os.environ)
        env["PYTHONPATH"] = os.pathsep.join([str(case / "src"), str(case)])
        env["PYTHONPYCACHEPREFIX"] = str(case / "fresh-pycache")
        env["TMPDIR"] = str(case / "scratch")
        (case / "scratch").mkdir()
        process = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", "tests/test_site_archive_budget.py",
             "--basetemp", str(case / "fixtures"), "-o", "cache_dir=" + str(case / "pytest-cache")],
            cwd=case, env=env, capture_output=True, text=True, check=False,
        )
        log = process.stdout + process.stderr
        (case / "pytest.log").write_text(log)
        passed = (process.returncode == 0 if mutation is None else
                  process.returncode == 1 and mutation[3] in log and "FAILED" in log)
        results.append({"case": name, "exit_code": process.returncode,
                        "expected_result_observed": passed,
                        "log_sha256": hashlib.sha256(log.encode()).hexdigest(),
                        "expected_failing_test": mutation[3] if mutation else None})
    report = {"issue": 463, "helper_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "input_hashes": {path: hashlib.sha256((root / path).read_bytes()).hexdigest()
                               for path in [*shared, "src/dufmech/site_contract.py"]},
              "all_expected_results_observed": all(row["expected_result_observed"] for row in results),
              "results": results}
    (output / "results.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if not report["all_expected_results_observed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
