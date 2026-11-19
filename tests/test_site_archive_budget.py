"""Archive-capacity regressions for measured review preservation, issue #463."""
from __future__ import annotations

import gzip
import importlib.util
import json
from pathlib import Path

import pytest

from dufmech.pages import render_site
from dufmech.site_contract import check_site
from tests.test_report import worklist_row

ROOT = Path(__file__).resolve().parents[1]
BUDGETS = ROOT / "conf/pages_budgets.json"
ACCOUNTING = ROOT / "docs/provenance/review-queue-archive-budget-20261116.json.gz"


def budgets() -> dict:
    return json.loads(BUDGETS.read_text())


@pytest.fixture
def archive_site(tmp_path):
    render_site([worklist_row("PF00001", proteins=10)], [], input_ids={}, out_dir=tmp_path,
                extra_artifacts={"source/reports/yaml_record_review/archive.md": "x" * 4096})
    return tmp_path


@pytest.mark.parametrize("excess", [0, 1])
def test_archive_bytes_accept_boundary_and_reject_one_over(archive_site, excess):
    total = sum(path.stat().st_size for path in archive_site.rglob("*") if path.is_file())
    limits = budgets()
    limits["site_total_bytes"] = total - excess
    errors, measurements = check_site(archive_site, limits)
    assert measurements["total_bytes"] == total
    assert errors == ([f"total_bytes: {total} exceeds {total - 1}"] if excess else [])


@pytest.mark.parametrize("excess", [0, 1])
def test_archive_files_accept_boundary_and_reject_one_over(archive_site, excess):
    count = sum(path.is_file() for path in archive_site.rglob("*"))
    limits = budgets()
    limits["generated_file_count"] = count - excess
    errors, _ = check_site(archive_site, limits)
    assert errors == ([f"generated file count outside budget: {count}"] if excess else [])


def test_measured_candidate_requires_archive_capacity_only():
    measured = json.loads(gzip.decompress(ACCOUNTING.read_bytes()))
    candidate = measured["accounting"]["head"]
    previous = measured["head_budgets"]
    current = budgets()
    assert candidate["bytes"] > previous["site_total_bytes"]
    assert candidate["files"] > previous["generated_file_count"]
    assert candidate["bytes"] <= current["site_total_bytes"]
    assert candidate["files"] <= current["generated_file_count"]
    assert {key: value for key, value in current.items()
            if key not in {"site_total_bytes", "generated_file_count"}} == {
                key: value for key, value in previous.items()
                if key not in {"site_total_bytes", "generated_file_count"}}


def test_accounting_covers_added_modified_deleted_and_unchanged_files():
    path = ROOT / "scripts/adhoc/audit_site_archive_growth.py"
    spec = importlib.util.spec_from_file_location("archive_growth_audit", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    def entry(size, oid):
        return {"mode": "100644", "size": size, "oid": oid}
    before = {"pages/a.txt": entry(10, "old"), "pages/obsolete.txt": entry(7, "removed"),
              "pages/same.txt": entry(3, "same"), "outside.txt": entry(10000, "outside")}
    added = "pages/source/reviews/new.md"
    after = {"pages/a.txt": entry(12, "new"), "pages/same.txt": entry(3, "same"),
             added: entry(41, "review"), "outside.txt": entry(99999, "outside-changed")}
    result = module.account(before, after, "pages/", {added})
    assert result["base"] == {"files": 3, "bytes": 20}
    assert result["head"] == {"files": 3, "bytes": 56}
    assert result["delta"] == {"files": 0, "bytes": 36}
    assert result["changed_counts"] == {"modified": 1, "deleted": 1, "added": 1}
    assert result["unchanged_files"] == 1
    assert result["groups"]["preserved_source_downloads"]["delta_bytes"] == 41
    assert sum(row["delta_bytes"] for row in result["changed_files"]) == 36


def test_accounting_refuses_nonblob_site_entries():
    path = ROOT / "scripts/adhoc/audit_site_archive_growth.py"
    spec = importlib.util.spec_from_file_location("archive_growth_nonblob", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with pytest.raises(ValueError, match="non-blob Git entry"):
        module.account({}, {"pages/submodule": {"mode": "160000", "oid": "commit", "size": None}},
                       "pages/", set())
