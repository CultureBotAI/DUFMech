"""Source adoption requires terms and retained provenance, not just an adapter."""

from __future__ import annotations

import csv
import hashlib
import json
import socket
from pathlib import Path

import pytest
import yaml

from dufmech.source_governance import (
    CORE_COLUMNS,
    QUEUE_EXTENSIONS,
    REQUIRED_WHEN_ADOPTED,
    check_sources,
    main,
    writer_inventory,
)

ROOT = Path(__file__).resolve().parents[1]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def catalogue(root: Path, **overrides) -> dict:
    block = {
        "source": "example", "name": "Example", "url": "https://example.org/data",
        "status": "seeded", "license": "CC0-1.0", "redistribution": "CC0_OK",
        "license_url": "https://example.org/license", "license_verified_on": "2026-10-07",
        "license_note": "Fixture primary terms.", "access": "API",
        "access_note": "Fixture public API.", "implementation": "IMPLEMENTED",
        "reviewed_on": "2026-10-07", "review_basis": "docs/review.md",
        "seeder": "freeze.py", "adapter": "src/dufmech/example_snapshot.py",
        "writer": "write_example", "artifacts": ["data/worklists/example-2026-10-01.manifest.json"],
    }
    block.update(overrides)
    write(root / "download.yaml", yaml.safe_dump([block]))
    return block


def queue(root: Path, block: dict, **overrides) -> None:
    row = {
        "source_id": block["source"], "name": block["name"], "closes_gap": "fixture coverage",
        "use": "SEED", "redistribution": block["redistribution"], "access": block["access"],
        "priority": "1", "status": "ADOPTED", "verified_on": block["license_verified_on"],
        "url": block["url"], "rationale": "Fixture has a retained source freeze.",
        "implementation": block["implementation"], "reviewed_on": block["reviewed_on"],
        "review_basis": block["review_basis"], "script": "scripts/" + block["seeder"],
        "artifacts": ";".join(block["artifacts"]), "license_url": block["license_url"],
    }
    row.update(overrides)
    path = root / "curation/source_queue.tsv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CORE_COLUMNS + QUEUE_EXTENSIONS, delimiter="\t")
        writer.writeheader()
        writer.writerow(row)


@pytest.fixture
def source_root(tmp_path):
    write(tmp_path / "scripts/freeze.py", "# fixture adapter\n")
    write(tmp_path / "src/dufmech/example_snapshot.py", "def write_example():\n    pass\n")
    write(tmp_path / "docs/review.md", "Reviewed source implementation.\n")
    stem = "example-2026-10-01"
    payloads = {"json": '[{"pfam_id": "PF00001"}]\n', "tsv": "pfam_id\nPF00001\n"}
    manifest = {
        "snapshot": {"id": stem, "date": "2026-10-01", "generated_at": "2026-10-01T00:00:00Z"},
        "source": {"name": "Example", "url": "https://example.org/data"},
        "schema": {"tsv_fieldnames": ["pfam_id"]}, "rows": {"total": 1}, "files": {},
    }
    for kind, content in payloads.items():
        write(tmp_path / f"data/worklists/{stem}.{kind}", content)
        manifest["files"][kind] = {
            "path": f"{stem}.{kind}", "bytes": len(content.encode()),
            "sha256": hashlib.sha256(content.encode()).hexdigest(),
        }
    write(tmp_path / f"data/worklists/{stem}.manifest.json", json.dumps(manifest))
    block = catalogue(tmp_path)
    queue(tmp_path, block)
    return tmp_path


def codes(root: Path) -> set[str]:
    return {f.code for f in check_sources(root) if f.severity == "error"}


def test_real_catalogue_covers_all_adapters_and_retained_sources():
    findings = check_sources(ROOT)
    assert not [f.render() for f in findings if f.severity == "error"]
    assert any(f.code == "LEGACY_TERMS_UNRESOLVED" and f.subject == "cross_mech" for f in findings)


def test_verified_source_and_artifacts_pass(source_root):
    assert check_sources(source_root) == []


@pytest.mark.parametrize("key,value,code", [
    ("status", "MAYBE", "UNKNOWN_VALUE"), ("status", "", "MISSING_FIELD"),
    ("priority", "0", "UNKNOWN_VALUE"), ("access", "LOGIN", "UNKNOWN_VALUE"),
    ("redistribution", "NON_COMMERCIAL", "UNKNOWN_VALUE"),
    ("verified_on", "2026-02-31", "BAD_DATE"),
    ("verified_on", "2026-10-07T12:00:00Z", "BAD_DATE"),
    ("reviewed_on", "", "MISSING_FIELD"),
    ("review_basis", "docs/invented.md", "QUEUE_CATALOGUE_MISMATCH"),
    ("script", "scripts/missing.py", "QUEUE_CATALOGUE_MISMATCH"),
])
def test_bad_queue_rows_fail(source_root, key, value, code):
    queue(source_root, catalogue(source_root), **{key: value})
    assert code in codes(source_root)


@pytest.mark.parametrize("terms", ["UNVERIFIED", "RESTRICTED", "NONCOMMERCIAL"])
def test_adopted_seed_requires_redistribution_rights(source_root, terms):
    queue(source_root, catalogue(source_root), redistribution=terms)
    assert "SEED_UNDER_TERMS_THAT_FORBID_IT" in codes(source_root)


@pytest.mark.parametrize("overrides", [
    {"license_verified_on": ""}, {"license_url": ""},
    {"license": "BSD-3-Clause"}, {"license": "unknown"},
])
def test_license_claim_requires_compatible_data_terms_and_provenance(source_root, overrides):
    block = catalogue(source_root, **overrides)
    queue(source_root, block)
    assert codes(source_root) & {"LICENSE_PROVENANCE", "LICENSE_CLASS"}


def test_unverified_candidate_is_honest_not_adopted(source_root):
    block = catalogue(source_root, status="candidate", redistribution="UNVERIFIED",
                      license="unknown", license_verified_on="", license_url="")
    queue(source_root, block, status="EVALUATING")
    assert codes(source_root) == set()


@pytest.mark.parametrize("relative", [
    "scripts/freeze.py", "docs/review.md", "src/dufmech/example_snapshot.py",
    "data/worklists/example-2026-10-01.json", "data/worklists/example-2026-10-01.tsv",
    "data/worklists/example-2026-10-01.manifest.json",
])
def test_missing_artifacts_or_review_provenance_fail(source_root, relative):
    (source_root / relative).unlink()
    assert codes(source_root) & {"MISSING_ARTIFACT", "MANIFEST_INVALID"}


def test_empty_artifact_list_cannot_support_adoption(source_root):
    queue(source_root, catalogue(source_root, artifacts=[]))
    assert {"MISSING_ARTIFACT", "ADOPTION_PROVENANCE"} <= codes(source_root)


def test_manifest_provenance_is_verified_not_just_listed(source_root):
    path = source_root / "data/worklists/example-2026-10-01.manifest.json"
    payload = json.loads(path.read_text())
    payload["files"]["json"]["sha256"] = "0" * 64
    write(path, json.dumps(payload))
    assert "MANIFEST_INVALID" in codes(source_root)


def test_manifest_row_counts_are_checked(source_root):
    path = source_root / "data/worklists/example-2026-10-01.manifest.json"
    payload = json.loads(path.read_text())
    payload["rows"]["total"] = 500
    write(path, json.dumps(payload))
    assert "MANIFEST_INVALID" in codes(source_root)


def test_ignored_adapter_and_manifest_are_still_discovered(source_root):
    write(source_root / ".gitignore", "*hidden*\n")
    write(source_root / "src/dufmech/hidden_snapshot.py", "def write_hidden():\n    pass\n")
    write(source_root / "data/worklists/.hidden.manifest.json", "{}")
    assert {"UNCATALOGUED_ADAPTER", "UNCATALOGUED_ARTIFACT"} <= codes(source_root)


def test_queue_width_duplicates_and_headers_fail(source_root):
    path = source_root / "curation/source_queue.tsv"
    original = path.read_text()
    write(path, original + original.splitlines()[1] + "\n")
    assert "DUPLICATE_SOURCE_ID" in codes(source_root)
    write(path, original + "missing\tcolumns\n")
    assert "BAD_ROW_WIDTH" in codes(source_root)
    write(path, "source_id\tsource_id\n")
    assert "QUEUE_COLUMNS" in codes(source_root)


def test_wrong_writer_and_unsafe_script_fail(source_root):
    queue(source_root, catalogue(source_root, writer="invented", seeder="../download.yaml"))
    assert {"MISSING_WRITER", "BAD_SEEDER"} <= codes(source_root)


def test_symlink_review_provenance_is_refused(source_root):
    path = source_root / "docs/review.md"
    path.unlink()
    path.symlink_to(source_root / "download.yaml")
    assert "MISSING_ARTIFACT" in codes(source_root)


@pytest.mark.parametrize("content", ["[]", "{}", "- [", "- null"])
def test_bad_catalogue_has_diagnostics(source_root, content):
    write(source_root / "download.yaml", content)
    assert codes(source_root)


@pytest.mark.parametrize("key", ["status", "writer", "license", "url", "reviewed_on"])
def test_wrong_catalogue_field_types_report_instead_of_crashing(source_root, key):
    catalogue(source_root, **{key: []})
    assert codes(source_root)


@pytest.mark.parametrize("options", [[], ["--sources-only"], ["--writers"]])
def test_offline_cli_never_connects(source_root, monkeypatch, capsys, options):
    def forbidden(*args, **kwargs):
        raise AssertionError("offline governance attempted network access")

    monkeypatch.setattr(socket, "socket", forbidden)
    writer_fixture(source_root, 'def save(out):\n    out.write_text("{}")\n')
    assert main(["--root", str(source_root), *options]) == 0
    captured = capsys.readouterr()
    assert "offline" in captured.out + captured.err


def test_shared_claw_contract_compatibility():
    catalogue_contract = pytest.importorskip("kg_microbe_sources.catalogue")
    queue_contract = pytest.importorskip("kg_microbe_source_queue.contract")
    assert CORE_COLUMNS == queue_contract.CORE_COLUMNS
    report = catalogue_contract.validate(
        catalogue_contract.load_blocks(ROOT / "download.yaml"), seeder_dir=ROOT / "scripts",
    )
    assert report.ok, [str(f) for f in report.errors]
    profile = queue_contract.SourceQueueProfile(
        extensions=QUEUE_EXTENSIONS, required_when_adopted=REQUIRED_WHEN_ADOPTED,
    )
    assert queue_contract.check_queue(ROOT / "curation/source_queue.tsv", profile) == []


def writer_fixture(root: Path, text: str) -> None:
    write(root / "src/dufmech/writer.py", text)
    write(root / "tests/test_writer.py", "# policy test fixture\n")
    config = {
        "version": 1, "validators": ["validate_record"], "history_helpers": ["new_history"],
        "helpers": {"save": {
            "path": "src/dufmech/writer.py", "formats": ["json", "tsv"],
            "policy": "fixture", "tests": ["tests/test_writer.py"],
        }},
    }
    write(root / "conf/writer_audit.yaml", yaml.safe_dump(config))


def test_real_writer_inventory_includes_json_tsv_records_and_append_helpers():
    rows, findings = writer_inventory(ROOT)
    assert findings == []
    by_key = {(r["path"], r["function"]): r for r in rows}
    snapshot = by_key["src/dufmech/alphafold_snapshot.py", "write_alphafold_snapshot"]
    assert set(snapshot["formats"]) == {"json", "tsv", "manifest.json"}
    assert snapshot["policy"] == "legacy-replace"
    assert snapshot["validation_calls"] == []
    records = by_key["src/dufmech/records.py", "write_records"]
    assert records["validation_calls"] == []
    assert "helper:_write_records" in records["write_evidence"]
    assert "helper:_writer_lock" in records["write_evidence"]
    assert records["policy"] == "generated-owned-files-apply-only"
    implementation = by_key["src/dufmech/records.py", "_write_records"]
    assert "validate_record" in implementation["validation_calls"]
    assert "helper:_publish_projection" in implementation["write_evidence"]
    assert implementation["policy"] == "validated-owned-projection-internal"
    publisher = by_key["src/dufmech/records.py", "_publish_projection"]
    assert publisher["policy"] == "retained-recovery-exclusive-publish-internal"
    assert by_key["src/dufmech/reviews.py", "append_document"]["policy"] == "exclusive-append"
    assert by_key["src/dufmech/history.py", "new_history"]["policy"] == "validated-append"


def test_writer_validation_evidence_is_function_scoped_and_ast_based(tmp_path):
    writer_fixture(tmp_path, '''
def save(out):
    """validate_record(data); new_history(data)"""
    out.write_text("{}"); out.write_bytes(b"x")

def validate_elsewhere():
    validate_record(data)

def checked(out):
    validate_record(data)
    new_history(data)
    save(out)
''')
    rows, findings = writer_inventory(tmp_path)
    assert findings == []
    by_name = {r["function"]: r for r in rows}
    assert by_name["save"]["validation_calls"] == []
    assert by_name["save"]["history_calls"] == []
    assert by_name["checked"]["validation_calls"] == ["validate_record"]
    assert by_name["checked"]["history_calls"] == ["new_history"]
    assert "validate_elsewhere" not in by_name


def test_writer_detection_sees_module_writes_aliases_and_open_modes(tmp_path):
    writer_fixture(tmp_path, '''
import json as js
from x import save as persist
def save():
    with open("rows.tsv", "x") as f:
        f.write("id\\n")
def wrapper(out):
    persist(out)
with open("a.json", mode="w") as stream:
    js.dump({}, stream)
''')
    rows, findings = writer_inventory(tmp_path)
    assert findings == []
    by_name = {r["function"]: r for r in rows}
    assert "helper:save" in by_name["wrapper"]["write_evidence"]
    assert "open:x" in by_name["save"]["write_evidence"]
    assert "serialize:json" in by_name["<module>"]["write_evidence"]


def test_writer_cannot_claim_nonexistent_helper_or_test_provenance(tmp_path):
    writer_fixture(tmp_path, "def renamed():\n    pass\n")
    (tmp_path / "tests/test_writer.py").unlink()
    _, findings = writer_inventory(tmp_path)
    assert {f.code for f in findings} == {"MISSING_WRITER_HELPER", "WRITER_POLICY_PROVENANCE"}


def test_ignored_python_writer_is_in_inventory(tmp_path):
    writer_fixture(tmp_path, 'def save(out):\n    out.write_text("{}")\n')
    write(tmp_path / ".gitignore", "hidden.py\n")
    write(tmp_path / "src/dufmech/hidden.py", 'target.write_bytes(b"x")\n')
    rows, _ = writer_inventory(tmp_path)
    assert any(r["path"] == "src/dufmech/hidden.py" for r in rows)


def test_removed_validation_and_changed_apply_default_fail(tmp_path):
    writer_fixture(tmp_path, 'def save(out, *, apply=True):\n    out.write_text("{}")\n')
    path = tmp_path / "conf/writer_audit.yaml"
    config = yaml.safe_load(path.read_text())
    config["helpers"]["save"].update(required_calls=["validate_record"], apply_default=False)
    write(path, yaml.safe_dump(config))
    _, findings = writer_inventory(tmp_path)
    assert {f.code for f in findings} == {"WRITER_VALIDATION_MISSING", "WRITER_DEFAULT"}


def test_delegated_writer_checks_the_actual_validation_scope(tmp_path):
    source = '''
def save(out, *, apply=False):
    return _save(out)
def _save(out):
    validate_record(data)
    out.write_text("{}")
'''
    writer_fixture(tmp_path, source)
    path = tmp_path / "conf/writer_audit.yaml"
    config = yaml.safe_load(path.read_text())
    config["helpers"]["save"].update(required_calls=["_save"], apply_default=False)
    config["helpers"]["_save"] = {
        "path": "src/dufmech/writer.py", "formats": ["json"],
        "policy": "validated-internal", "tests": ["tests/test_writer.py"],
        "required_calls": ["validate_record"],
    }
    write(path, yaml.safe_dump(config))
    rows, findings = writer_inventory(tmp_path)
    assert findings == []
    by_name = {r["function"]: r for r in rows}
    assert by_name["save"]["validation_calls"] == []
    assert by_name["_save"]["validation_calls"] == ["validate_record"]
    write(tmp_path / "src/dufmech/writer.py", source.replace("    validate_record(data)\n", ""))
    _, findings = writer_inventory(tmp_path)
    assert [(f.code, f.subject) for f in findings] == [("WRITER_VALIDATION_MISSING", "_save")]


def test_writer_json_is_parseable_and_diagnostics_are_separate(source_root, capsys):
    writer_fixture(source_root, 'def save(out):\n    out.write_text("{}")\n')
    assert main(["--root", str(source_root), "--writers"]) == 0
    captured = capsys.readouterr()
    assert any(row["function"] == "save" for row in json.loads(captured.out))
    assert "offline" in captured.err
