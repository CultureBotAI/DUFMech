from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import threading
from dataclasses import replace
from pathlib import Path

import httpx
import pytest
from bs4 import BeautifulSoup

from dufmech import cross_mech, cross_mech_snapshot_cli
from dufmech.cross_mech import (
    CrossMechError,
    FamilyIndex,
    ScanResult,
    SourceRecord,
    UniProtPfamClient,
    load_uniprot_cache,
    render_uniprot_cache,
    scan_mechs,
)
from dufmech.cross_mech_report import main as report_main
from dufmech.cross_mech_snapshot import write_cross_mech_snapshot
from dufmech.pages import render_site
from tests.test_cross_mech import FAMILIES, MECHS, _lookup, _repo, mechs_root  # noqa: F401
from tests.test_report import worklist_row


@pytest.mark.parametrize("text,expected", [
    ("DUF3458_C-family", {"PF17432"}),
    ("QueG_DUF1730-containing", {"PF08331"}),
    ("DUF3329-like-family", {"PF11794"}),
    ("DUF3458abc", set()),
    ("DUF3458_C_extra", set()),
])
def test_exact_names_with_prose_boundaries(text: str, expected: set[str]) -> None:
    families = FamilyIndex.from_rows([
        {"pfam_id": "PF11940", "short_name": "DUF3458"},
        {"pfam_id": "PF17432", "short_name": "DUF3458_C"},
        {"pfam_id": "PF08331", "short_name": "QueG_DUF1730"},
        {"pfam_id": "PF11794", "short_name": "DUF3329-like"},
    ])
    assert set(families.text_matches(text)) == expected
    assert families.unlisted_short_names(text) == set()


def test_dashboard_counts_records_once_and_shows_trait_flag(tmp_path: Path) -> None:
    base = {
        "pfam_id": "PF06226", "short_name": "DUF1007", "source_mech": "ProteinTraitsMech",
        "source_path": "data/traits/example.yaml", "source_section": "canonical_examples",
        "uniprot_accession": "P22041",
    }
    render_site(
        [worklist_row("PF06226", proteins=1), worklist_row("PF04363", proteins=1)], [],
        input_ids={}, out_dir=tmp_path,
        cross_mech_rows=[
            base, {**base, "uniprot_accession": "Q99999"},
            {**base, "source_section": "trait_identifier", "uniprot_accession": ""},
            {**base, "pfam_id": "PF04363", "source_section": "trait_identifier",
             "uniprot_accession": ""},
        ],
    )
    payload = json.loads((tmp_path / "index.json").read_text())
    families = {row["pfam_id"]: row for row in payload["families"]}
    summary = families["PF06226"]["cross_mech"]
    assert summary["records_by_mech"] == {"ProteinTraitsMech": 1}
    assert summary["example_proteins"] == 2
    assert payload["summary"]["cross_mech"]["families"] == 1
    soup = BeautifulSoup((tmp_path / "index.html").read_text(), "html.parser")
    for pfam in families:
        row = next(row for row in soup.select("tr") if pfam in row.get_text())
        assert "ProteinTraitsMech trait record" in row.get_text()


def test_scan_closes_reader_after_record_error(monkeypatch: pytest.MonkeyPatch) -> None:
    closed = []

    def records():
        try:
            yield SourceRecord(MECHS[2], "a" * 40, "data/traits/bad.yaml",
                               "identifier: Pfam:PF06226\ncanonical_examples: [")
        finally:
            closed.append(True)

    reader = records()
    monkeypatch.setattr(cross_mech, "iter_mech_records", lambda *a, **kw: ("a" * 40, reader))
    with pytest.raises(CrossMechError, match="invalid YAML"):
        scan_mechs(Path("unused"), FAMILIES, mechs=MECHS[2:])
    assert closed == [True]


def test_cat_file_early_close_joins_feeder(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = _repo(tmp_path, "TraitMech", {"data/traits/a.yaml": "name: " + "x" * 65536})
    sha = subprocess.check_output(
        ["git", "-C", str(repo), "rev-parse", "HEAD:data/traits/a.yaml"], text=True,
    ).strip()
    errors = []
    monkeypatch.setattr(threading, "excepthook", errors.append)
    before = set(threading.enumerate())
    records = cross_mech._cat_blobs(repo, "HEAD", MECHS[0], [(sha, "data/traits/a.yaml")] * 4000)
    assert next(records).text.startswith("name:")
    records.close()
    assert not errors
    assert set(threading.enumerate()) <= before


def test_cat_file_rejects_nonzero_exit(monkeypatch: pytest.MonkeyPatch) -> None:
    original = subprocess.Popen
    sha = "a" * 40

    def failed_git(*args, **kwargs):
        return original([sys.executable, "-c", (
            "import sys; sys.stdin.buffer.read(); "
            f"sys.stdout.buffer.write(b'{sha} blob 2\\nx\\n\\n'); sys.exit(17)"
        )], **kwargs)

    monkeypatch.setattr(cross_mech.subprocess, "Popen", failed_git)
    with pytest.raises(CrossMechError, match="17"):
        list(cross_mech._cat_blobs(Path("unused"), "HEAD", MECHS[0], [(sha, "data/traits/a.yaml")]))


@pytest.mark.parametrize("data", [b"x", b"xy!", b"xy"])
def test_cat_file_rejects_truncated_blob_or_delimiter(
    data: bytes, monkeypatch: pytest.MonkeyPatch,
) -> None:
    original = subprocess.Popen
    sha = "a" * 40
    output = f"{sha} blob 2\n".encode() + data

    def truncated_git(*args, **kwargs):
        return original([sys.executable, "-c", (
            f"import sys; sys.stdin.buffer.read(); sys.stdout.buffer.write({output!r})"
        )], **kwargs)

    monkeypatch.setattr(cross_mech.subprocess, "Popen", truncated_git)
    with pytest.raises(CrossMechError, match="could not read"):
        list(cross_mech._cat_blobs(Path("unused"), "HEAD", MECHS[0], [(sha, "data/traits/a.yaml")]))


@pytest.mark.parametrize("check", [False, True])
def test_report_rejects_obsolete_worklist(
    mechs_root: Path, tmp_path: Path, capsys, check: bool,  # noqa: F811
) -> None:
    cross = tmp_path / "cross"
    result = scan_mechs(mechs_root, FAMILIES, mechs=MECHS)
    write_cross_mech_snapshot(result, cross, worklist_snapshot_id="interpro-pfam-duf-1999-01-01",
                              source_ref="HEAD", snapshot_date="2026-10-05")
    args = ["--cross-mech-dir", str(cross), "--out-dir", str(tmp_path / "reports")]
    assert report_main([*args, *(["--check"] if check else [])]) == 1
    assert "regenerate the cross-Mech snapshot" in capsys.readouterr().err
    assert not (tmp_path / "reports").exists()


@pytest.mark.parametrize("change,error", [
    ({"pfam_id": "PF99999"}, "absent from worklist"),
    ({"unknown_status": "KNOWN_HISTORICAL_DUF"}, "metadata differs"),
])
def test_report_validates_family_metadata(tmp_path: Path, capsys, change, error: str) -> None:
    rows = cross_mech.family_mention_rows(
        SourceRecord(MECHS[0], "a" * 40, "data/traits/a.yaml", "id: example"),
        FAMILIES, {"PF06226": {"record_mentions_pfam_id"}},
    )
    write_cross_mech_snapshot(
        ScanResult(rows=[replace(rows[0], **change)]), tmp_path,
        worklist_snapshot_id="interpro-pfam-duf-2026-10-01", source_ref="HEAD",
        snapshot_date="2026-10-05",
    )
    assert report_main([
        "--cross-mech-dir", str(tmp_path), "--check", "--worklist-json",
        "data/worklists/interpro-pfam-duf-2026-10-01.json",
    ]) == 1
    assert error in capsys.readouterr().err


def test_cache_merge_preserves_fetch_age_and_unrelated_rows(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    cache = tmp_path / "cache.json"
    seed = _lookup(["P22041", "Q99999"])
    old = replace(seed["P22041"], fetched_at="2026-10-01T00:00:00Z")
    other = replace(old, requested_accession="P99999", uniprot_accession="P99999")
    cache.write_text(render_uniprot_cache({"P22041": old, "P99999": other}))
    before = hashlib.sha256(cache.read_bytes()).hexdigest()
    monkeypatch.setattr(cross_mech_snapshot_cli, "_now", lambda: "2026-10-05T00:00:00Z")
    calls = []

    class Client:
        def __call__(self, accessions):
            calls.append(accessions)
            return {"Q99999": seed["Q99999"]}

    monkeypatch.setattr(cross_mech_snapshot_cli, "UniProtPfamClient", Client)
    info = {}
    rows = cross_mech_snapshot_cli._lookup(cache, info)(["P22041", "Q99999"])
    assert calls == [["Q99999"]]
    assert rows["P22041"].fetched_at == "2026-10-01T00:00:00Z"
    assert rows["Q99999"].fetched_at == "2026-10-05T00:00:00Z"
    assert info["cache_input_sha256"] == before
    assert info["cache_hit_fetch_times"] == ["2026-10-01T00:00:00Z"]
    assert info["cache_hits_without_fetch_time"] == 0
    assert load_uniprot_cache(cache.read_text())["P99999"] == other
    replay_info = {}
    assert cross_mech_snapshot_cli._lookup(cache, replay_info)(list(rows)) == rows
    assert len(calls) == 1
    assert replay_info["cache_hit_fetch_times"] == ["2026-10-01T00:00:00Z", "2026-10-05T00:00:00Z"]


def test_legacy_cache_reports_unknown_age(tmp_path: Path) -> None:
    cache = tmp_path / "cache.json"
    values = json.loads(render_uniprot_cache(_lookup(["P22041", "Q99999"])))
    for value in values:
        value.pop("fetched_at", None)
    cache.write_text(json.dumps(values))
    info = {}
    assert len(cross_mech_snapshot_cli._lookup(cache, info)(["P22041", "Q99999"])) == 2
    assert info["cache_hits_without_fetch_time"] == 2
    assert info["cache_hit_fetch_times"] == []


def test_uniprot_transport_failure_is_a_domain_error() -> None:
    def fail(request):
        raise httpx.ConnectError("offline", request=request)

    with pytest.raises(CrossMechError, match="could not fetch UniProtKB"):
        UniProtPfamClient(transport=httpx.MockTransport(fail))(["P22041"])


@pytest.mark.parametrize("suffix", ["json", "tsv", "manifest.json"])
def test_snapshot_cannot_replace_existing_artifact(tmp_path: Path, suffix: str) -> None:
    existing = tmp_path / f"cross-mech-duf-examples-2026-10-05.{suffix}"
    existing.write_bytes(b"existing evidence")
    with pytest.raises(FileExistsError):
        write_cross_mech_snapshot(ScanResult(), tmp_path, worklist_snapshot_id="worklist",
                                  source_ref="HEAD", snapshot_date="2026-10-05")
    assert list(tmp_path.iterdir()) == [existing]
    assert existing.read_bytes() == b"existing evidence"


def test_snapshot_preflights_all_metadata_before_writing(tmp_path: Path) -> None:
    rows = cross_mech.family_mention_rows(
        SourceRecord(MECHS[0], "a" * 40, "data/traits/a.yaml", "id: example\nname: \ud800"),
        FAMILIES, {"PF06226": {"record_mentions_pfam_id"}},
    )
    with pytest.raises(UnicodeError):
        write_cross_mech_snapshot(ScanResult(rows=rows), tmp_path, worklist_snapshot_id="worklist",
                                  source_ref="HEAD", snapshot_date="2026-10-05")
    assert list(tmp_path.iterdir()) == []


def test_snapshot_refuses_dangling_symlink(tmp_path: Path) -> None:
    target = tmp_path / "cross-mech-duf-examples-2026-10-05.tsv"
    target.symlink_to(tmp_path / "missing")
    with pytest.raises(FileExistsError):
        write_cross_mech_snapshot(ScanResult(), tmp_path, worklist_snapshot_id="worklist",
                                  source_ref="HEAD", snapshot_date="2026-10-05")
    assert target.is_symlink()
    assert not target.exists()
    assert list(tmp_path.iterdir()) == [target]


def test_snapshot_rolls_back_only_its_own_files(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    original = Path.open

    def fail_second_file(path, mode="r", *args, **kwargs):
        if path.suffix == ".tsv" and mode == "xb":
            # Model an output created concurrently, after our preflight check.
            with original(path, "wb") as handle:
                handle.write(b"other invocation")
        return original(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", fail_second_file)
    with pytest.raises(FileExistsError):
        write_cross_mech_snapshot(ScanResult(), tmp_path, worklist_snapshot_id="worklist",
                                  source_ref="HEAD", snapshot_date="2026-10-05")
    assert [path.name for path in tmp_path.iterdir()] == ["cross-mech-duf-examples-2026-10-05.tsv"]
    assert next(tmp_path.iterdir()).read_bytes() == b"other invocation"


def test_cli_no_lookup_and_missing_repository(tmp_path: Path, capsys) -> None:
    root = tmp_path / "Mechs"
    _repo(root, "TraitMech", {"data/traits/a.yaml": "id: test\ndescription: DUF1007 UniProtKB:P22041"})
    out = tmp_path / "cross"
    args = ["--mechs-root", str(root), "--mech", "TraitMech", "--no-uniprot",
            "--out-dir", str(out), "--snapshot-date", "2026-10-05"]
    assert cross_mech_snapshot_cli.main(args) == 0
    source = json.loads(next(out.glob("*.manifest.json")).read_text())["source"]
    assert source["uniprotkb_lookup"] == {"mode": "none"}
    assert source["uniprotkb_accessions_requested"] == 1
    assert source["uniprotkb_accessions_resolved"] == 0
    assert cross_mech_snapshot_cli.main(args) == 1
    assert "already exists" in capsys.readouterr().err
    missing_out = tmp_path / "missing-cross"
    assert cross_mech_snapshot_cli.main([
        "--mechs-root", str(tmp_path / "missing"), "--mech", "TraitMech", "--no-uniprot",
        "--out-dir", str(missing_out),
    ]) == 1
    assert "not a git checkout" in capsys.readouterr().err
    assert not missing_out.exists()


@pytest.mark.parametrize("payload", [[None], [{"requested_accession": "P22041"}]])
def test_malformed_cache_is_a_domain_error(payload) -> None:
    with pytest.raises(CrossMechError, match="invalid UniProt cache row"):
        load_uniprot_cache(json.dumps(payload))


def test_worklist_correction_preserves_cross_mech_evidence() -> None:
    root = Path(__file__).resolve().parents[1]
    source = root / "data/cross_mech/cross-mech-duf-examples-2026-10-05.json"
    target = root / "data/cross_mech/cross-mech-duf-examples-2026-10-06.json"
    before = json.loads(source.read_text())
    after = json.loads(target.read_text())
    manifest = json.loads(target.with_suffix(".manifest.json").read_text())
    lineage = manifest["snapshot"]["derivation"]
    worklist = root / "data/worklists/interpro-pfam-duf-2026-10-05.json"
    families = {row["pfam_id"]: row for row in json.loads(worklist.read_text())}
    assert len(before) == len(after) == 16298
    changed = 0
    for old, new in zip(before, after):
        assert {key: value for key, value in old.items() if key != "unknown_status"} == {
            key: value for key, value in new.items() if key != "unknown_status"
        }
        if new["pfam_id"]:
            assert new["unknown_status"] == families[new["pfam_id"]]["unknown_status"]
        changed += old["unknown_status"] != new["unknown_status"]
    assert changed == lineage["rows_with_changed_seed_status"] == 2479
    assert lineage["source_json_sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()
    assert lineage["source_manifest_sha256"] == hashlib.sha256(
        source.with_suffix(".manifest.json").read_bytes()
    ).hexdigest()
    assert lineage["target_worklist_json_sha256"] == hashlib.sha256(worklist.read_bytes()).hexdigest()
    assert manifest["snapshot"]["input_snapshot_ids"]["worklist"] == worklist.stem
