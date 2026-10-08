from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import pytest

from dufmech.cross_mech import CrossMechRow, ScanResult
from dufmech.cross_mech_snapshot import derive_cross_mech_snapshot, write_cross_mech_snapshot
from dufmech.exduf import prepare_migration
from dufmech.report import ReportError, metadata_preserving_ancestors
from dufmech.worklist import EX_DUF
from tests.test_exduf import PARENT, _fetch, _inputs, _write

T = datetime(2026, 10, 8, tzinfo=timezone.utc)


def _migrate(tmp_path: Path, live_json: Path | None = None) -> Path:
    parent, previous = _inputs(tmp_path)
    prepared = prepare_migration(parent, previous, snapshot_date="2026-10-08", fetch=_fetch,
                                 live_json=live_json, generated_at=T)
    return _write(parent.parent, prepared.artifacts)


def test_ancestors_follow_metadata_preserving_derivations(tmp_path: Path) -> None:
    migrated = _migrate(tmp_path)
    assert metadata_preserving_ancestors(migrated.parent, migrated.stem) == [
        "interpro-pfam-duf-2026-10-05"
    ]
    # A live-search worklist has no parent; it has no ancestors.
    assert metadata_preserving_ancestors(migrated.parent, "interpro-pfam-duf-2026-10-05") == []


def test_refresh_migration_stops_the_ancestor_walk(tmp_path: Path) -> None:
    from dufmech.snapshot import write_worklist_snapshot

    parent, _ = _inputs(tmp_path)
    # A refresh migration, written next to its parents, whose live parent is 10-06.
    parent_dir = parent.parent
    write_worklist_snapshot(PARENT, parent_dir, snapshot_date="2026-10-06", generated_at=T)
    prepared = prepare_migration(
        parent, parent_dir / "pfam-previous-unknown-names-2026-10-07.json",
        snapshot_date="2026-10-08", fetch=_fetch,
        live_json=parent_dir / "interpro-pfam-duf-2026-10-06.json", generated_at=T,
    )
    out = _write(parent_dir, prepared.artifacts)
    assert metadata_preserving_ancestors(parent_dir, out.stem) == []


def _cross(tmp_path: Path) -> Path:
    rows = [
        CrossMechRow("PF06172", "Cupin_8", "UNKNOWN_CANDIDATE", "TraitMech", "genomics",
                     "data/traits/genomics/x.yaml", "traitmech:1", "X", "record_text",
                     ("record_mentions_short_name",)),
        CrossMechRow("", "DUF1814", "NOT_IN_WORKLIST", "TraitMech", "genomics",
                     "data/traits/genomics/y.yaml", "traitmech:2", "Y", "record_text",
                     ("record_mentions_unlisted_short_name",)),
    ]
    out = tmp_path / "cross"
    write_cross_mech_snapshot(
        ScanResult(rows=rows, mechs={"TraitMech": {"commit": "a" * 40, "records_scanned": 2}}), out,
        worklist_snapshot_id="interpro-pfam-duf-2026-10-05", source_ref="origin/main",
        snapshot_date="2026-10-06", generated_at=T,
    )
    return out / "cross-mech-duf-examples-2026-10-06.json"


def test_cross_mech_derivation_relabels_and_records_provenance(tmp_path: Path) -> None:
    migrated = _migrate(tmp_path)
    source = _cross(tmp_path)
    manifest = derive_cross_mech_snapshot(
        source, migrated, tmp_path / "derived", snapshot_date="2026-10-08",
        source_git_commit="b" * 40, generated_at=T,
    )
    rows = json.loads((tmp_path / "derived/cross-mech-duf-examples-2026-10-08.json").read_text())
    assert [row["unknown_status"] for row in rows] == ["NOT_IN_WORKLIST", EX_DUF]
    derivation = manifest["snapshot"]["derivation"]
    assert derivation["rows_with_changed_seed_status"] == 1
    assert derivation["source_json_sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()
    assert derivation["target_worklist_json_sha256"] == hashlib.sha256(
        migrated.read_bytes()).hexdigest()
    assert manifest["snapshot"]["input_snapshot_ids"] == {"worklist": migrated.stem}
    assert manifest["source"]["mechs"] == {"TraitMech": {"commit": "a" * 40, "records_scanned": 2}}


def test_cross_mech_derivation_never_drops_evidence(tmp_path: Path) -> None:
    migrated = _migrate(tmp_path)
    rows = [CrossMechRow("PF77777", "DUF7", "UNKNOWN_CANDIDATE", "TraitMech", "g", "p.yaml",
                         "t:1", "Z", "record_text", ("record_mentions_short_name",))]
    out = tmp_path / "cross2"
    write_cross_mech_snapshot(ScanResult(rows=rows), out,
                              worklist_snapshot_id="interpro-pfam-duf-2026-10-05",
                              source_ref="origin/main", snapshot_date="2026-10-06", generated_at=T)
    with pytest.raises(ReportError, match="PF77777 is absent"):
        derive_cross_mech_snapshot(out / "cross-mech-duf-examples-2026-10-06.json", migrated,
                                   tmp_path / "d2", snapshot_date="2026-10-08",
                                   source_git_commit="c" * 40)


REPO = Path(__file__).resolve().parents[1]


def test_real_migration_preserves_every_existing_family_and_logs_each_change() -> None:
    before = {r["pfam_id"]: r for r in json.loads(
        (REPO / "data/worklists/interpro-pfam-duf-2026-10-05.json").read_text())}
    after = {r["pfam_id"]: r for r in json.loads(
        (REPO / "data/worklists/interpro-pfam-duf-2026-10-08.json").read_text())}
    manifest = json.loads(
        (REPO / "data/worklists/interpro-pfam-duf-2026-10-08.manifest.json").read_text())
    classification = {"unknown_status", "candidate_reasons"}
    assert before.keys() <= after.keys()
    for pfam, old in before.items():
        new = after[pfam]
        assert {k: v for k, v in old.items() if k not in classification} == {
            k: v for k, v in new.items() if k not in classification}
    changed = {p for p in before if before[p]["unknown_status"] != after[p]["unknown_status"]}
    assert changed == {c["pfam_id"] for c in manifest["derivation"]["changes"]}
    assert set(after) - set(before) == set(manifest["derivation"]["added_pfam_ids"])
    assert metadata_preserving_ancestors(REPO / "data/worklists", "interpro-pfam-duf-2026-10-08") == [
        "interpro-pfam-duf-2026-10-05", "interpro-pfam-duf-2026-10-01"]


def test_ancestor_walk_checks_parent_hash_and_stops_lazily(tmp_path: Path) -> None:
    from dufmech.report import iter_metadata_preserving_ancestors

    migrated = _migrate(tmp_path)
    directory = migrated.parent
    # The seed is found before any further ancestor is needed.
    assert "interpro-pfam-duf-2026-10-05" in iter_metadata_preserving_ancestors(
        directory, migrated.stem)
    # A parent replaced after derivation (consistent manifest, different bytes) fails.
    from dufmech.snapshot import write_worklist_snapshot

    for name in ("json", "tsv", "manifest.json"):
        (directory / f"interpro-pfam-duf-2026-10-05.{name}").unlink()
    write_worklist_snapshot(PARENT[:1], directory, snapshot_date="2026-10-05", generated_at=T)
    with pytest.raises(ReportError, match="recorded parent hash"):
        metadata_preserving_ancestors(directory, migrated.stem)


def test_reclassification_v2_is_a_metadata_preserving_step(tmp_path: Path) -> None:
    from dufmech.reclassify import reclassify_snapshot

    migrated = _migrate(tmp_path)
    reclassify_snapshot(migrated, migrated.parent, snapshot_date="2026-10-09", generated_at=T)
    assert metadata_preserving_ancestors(migrated.parent, "interpro-pfam-duf-2026-10-09") == [
        migrated.stem, "interpro-pfam-duf-2026-10-05"]


def test_member_seed_check_accepts_ancestor_and_rejects_absent_families(tmp_path: Path) -> None:
    from dufmech.pages import check_member_seed

    migrated = _migrate(tmp_path)
    rows = json.loads(migrated.read_text())
    members = [{"pfam_id": "PF01519", "uniprot_accession": "A1"}]
    check_member_seed(members, "interpro-pfam-duf-2026-10-05", rows, migrated.stem, migrated.parent)
    check_member_seed(members, migrated.stem, rows, migrated.stem, migrated.parent)
    with pytest.raises(ReportError, match="seeded against"):
        check_member_seed(members, "interpro-pfam-duf-1999-01-01", rows, migrated.stem,
                          migrated.parent)
    with pytest.raises(ReportError, match="absent from the worklist"):
        check_member_seed([{"pfam_id": "PF99999"}], "interpro-pfam-duf-2026-10-05", rows,
                          migrated.stem, migrated.parent)


def _previous_names(directory: Path, rows: list[dict]) -> Path:
    from dufmech.pfam_history import PfamPreviousNamesRow, SeedRead
    from dufmech.pfam_history_snapshot import write_pfam_previous_names_snapshot

    objs = [PfamPreviousNamesRow(r["pfam_id"], f"{r['pfam_id']}.1", r["short_name"], "x",
                                 tuple(r["names"]), tuple(r["names"]), False) for r in rows]
    write_pfam_previous_names_snapshot(SeedRead(objs, 9, 9, 1, "0" * 64), directory,
                                       release="38.2", source_url="x",
                                       snapshot_date="2026-10-07", generated_at=T)
    return directory / "pfam-previous-unknown-names-2026-10-07.json"


def test_derivation_records_coverage_and_resolves_former_names(tmp_path: Path) -> None:
    migrated = _migrate(tmp_path)
    source = _cross(tmp_path)
    previous = _previous_names(tmp_path / "prev", [
        {"pfam_id": "PF14337", "short_name": "Abi_alpha", "names": ["DUF1814"]},
    ])
    manifest = derive_cross_mech_snapshot(
        source, migrated, tmp_path / "derived", snapshot_date="2026-10-08",
        source_git_commit="b" * 40, previous_names_json=previous, generated_at=T,
    )
    derivation = manifest["snapshot"]["derivation"]
    # PF14337 joined in the migration; the October scan never searched it.
    assert derivation["coverage"]["unscanned_pfam_ids"] == ["PF14337"]
    assert derivation["coverage"]["scanned_worklist_snapshot_id"] == "interpro-pfam-duf-2026-10-05"
    assert derivation["resolved_previous_names"] == {"DUF1814": "PF14337"}
    assert derivation["rows_resolved_by_previous_name"] == 1
    # Fixture rows already carry cited_uniprot_accession, so nothing is backfilled.
    assert "backfilled_fields" not in derivation
    rows = json.loads((tmp_path / "derived/cross-mech-duf-examples-2026-10-08.json").read_text())
    resolved = next(r for r in rows if r["pfam_id"] == "PF14337")
    assert resolved["short_name"] == "Abi_alpha" and resolved["unknown_status"] == EX_DUF
    assert resolved["link_basis"] == ["record_mentions_previous_pfam_name"]

    # The loader accepts it against the migrated worklist and exposes coverage.
    from dufmech.cross_mech_snapshot import cross_mech_unscanned, load_cross_mech_snapshot

    _, loaded = load_cross_mech_snapshot(
        tmp_path / "derived/cross-mech-duf-examples-2026-10-08.json",
        worklist_rows=json.loads(migrated.read_text()), worklist_snapshot_id=migrated.stem)
    assert cross_mech_unscanned(loaded) == {"PF14337"}


def test_derivation_cli_and_ambiguous_names(tmp_path: Path, capsys) -> None:
    from dufmech.cross_mech_snapshot import main as derive_main

    migrated = _migrate(tmp_path)
    source = _cross(tmp_path)
    previous = _previous_names(tmp_path / "prev", [
        {"pfam_id": "PF14337", "short_name": "Abi_alpha", "names": ["DUF1814"]},
        {"pfam_id": "PF06172", "short_name": "Cupin_8", "names": ["DUF1814"]},
    ])
    assert derive_main([
        "--source-json", str(source), "--worklist-json", str(migrated),
        "--snapshot-date", "2026-10-08", "--source-git-commit", "d" * 40,
        "--previous-names-json", str(previous), "--out-dir", str(tmp_path / "cli"),
    ]) == 0
    assert "1 seed labels changed" in capsys.readouterr().out
    manifest = json.loads(
        (tmp_path / "cli/cross-mech-duf-examples-2026-10-08.manifest.json").read_text())
    derivation = manifest["snapshot"]["derivation"]
    assert derivation["ambiguous_previous_names"] == ["DUF1814"]
    assert derivation["resolved_previous_names"] == {}


def test_site_marks_unscanned_families(tmp_path: Path) -> None:
    from dufmech.pages import _attach_cross_mech
    from dufmech.site import family_row

    families = [{"pfam_id": "PF14337"}, {"pfam_id": "PF01519"}]
    summary = _attach_cross_mech(families, [], {"PF14337"})
    assert summary["unscanned_families"] == 1
    assert families[0]["cross_mech"]["scanned"] is False
    assert families[1]["cross_mech"]["scanned"] is True
    row = {"pfam_id": "PF14337", "characterization_status": "", "known_evidence_count": None,
           "partial_evidence_count": None, "context_evidence_count": None, "name": "n",
           "short_name": "s", "unknown_status": EX_DUF, "proteins": 1, "structures": 0,
           "alphafold_models": 0, "curation_status": "SEEDED", "cross_mech": families[0]["cross_mech"]}
    assert "not covered by the cross-Mech scan" in family_row(row)


def test_real_cross_mech_relabel_keeps_evidence_and_records_coverage() -> None:
    source = json.loads((REPO / "data/cross_mech/cross-mech-duf-examples-2026-10-06.json").read_text())
    target_path = REPO / "data/cross_mech/cross-mech-duf-examples-2026-10-08.json"
    target = json.loads(target_path.read_text())
    derivation = json.loads(target_path.with_suffix(".manifest.json").read_text())["snapshot"]["derivation"]
    worklist = {r["pfam_id"]: r for r in json.loads(
        (REPO / "data/worklists/interpro-pfam-duf-2026-10-08.json").read_text())}
    resolved = derivation["resolved_previous_names"]
    assert len(source) == len(target)
    kept = {"source_mech", "source_category", "source_path", "source_record_id",
            "source_record_label", "source_section", "uniprot_accession", "protein_label",
            "reviewed", "taxon_id", "taxon_label", "family_mentioned_in_record"}
    from collections import Counter

    source_records = Counter(tuple(r[k] for k in sorted(kept)) for r in source)
    target_by_record = {}
    for row in target:
        assert row["cited_uniprot_accession"] == ""
        if row["pfam_id"]:
            assert row["unknown_status"] == worklist[row["pfam_id"]]["unknown_status"]
            assert row["short_name"] == worklist[row["pfam_id"]]["short_name"]
        if "record_mentions_previous_pfam_name" in row["link_basis"]:
            assert row["pfam_id"] in resolved.values()
        target_by_record.setdefault(tuple(row[k] for k in sorted(kept)), []).append(row)
    # Every source row survives with its record/protein fields intact.
    assert Counter({key: len(rows) for key, rows in target_by_record.items()}) == source_records
    assert derivation["rows_resolved_by_previous_name"] == 11
    assert len(resolved) == 8
    assert {r["short_name"] for r in target if not r["pfam_id"]} == {
        "UPF0014", "UPF0018", "UPF0037", "UPF0265"}
    coverage = derivation["coverage"]
    assert coverage["scanned_families"] == 6532
    assert coverage["scanned_worklist_snapshot_id"] == "interpro-pfam-duf-2026-10-01"
    assert len(coverage["unscanned_pfam_ids"]) == 1763
    added = json.loads((REPO / "data/worklists/interpro-pfam-duf-2026-10-08.manifest.json")
                       .read_text())["derivation"]["added_pfam_ids"]
    assert coverage["unscanned_pfam_ids"] == sorted(added)
    assert derivation["backfilled_fields"] == {
        "cited_uniprot_accession": "empty: not recorded by the source scan"}


def test_ancestor_walk_stops_at_the_seed_without_verifying_further(tmp_path: Path) -> None:
    from dufmech.reclassify import reclassify_snapshot
    from dufmech.report import iter_metadata_preserving_ancestors

    migrated = _migrate(tmp_path)
    directory = migrated.parent
    reclassify_snapshot(migrated, directory, snapshot_date="2026-10-09", generated_at=T)
    for name in ("json", "tsv", "manifest.json"):
        (directory / f"interpro-pfam-duf-2026-10-05.{name}").unlink()
    # The seed is the immediate parent; the missing grandparent is never touched.
    assert migrated.stem in iter_metadata_preserving_ancestors(directory, "interpro-pfam-duf-2026-10-09")
    with pytest.raises(ReportError):
        metadata_preserving_ancestors(directory, "interpro-pfam-duf-2026-10-09")


def test_v1_reclassification_parent_hash_is_checked(tmp_path: Path) -> None:
    import shutil

    from dufmech.snapshot import write_worklist_snapshot

    directory = tmp_path / "w"
    directory.mkdir()
    for name in ("json", "tsv", "manifest.json"):
        shutil.copy(REPO / f"data/worklists/interpro-pfam-duf-2026-10-05.{name}", directory)
    # A self-consistent but different 10-01 parent: the v1 child's source_sha256 disagrees.
    write_worklist_snapshot(PARENT, directory, snapshot_date="2026-10-01", generated_at=T)
    with pytest.raises(ReportError, match="recorded parent hash"):
        metadata_preserving_ancestors(directory, "interpro-pfam-duf-2026-10-05")


def test_coverage_carries_through_chained_derivations(tmp_path: Path) -> None:
    from dufmech.cross_mech_snapshot import cross_mech_unscanned
    from dufmech.reclassify import reclassify_snapshot

    migrated = _migrate(tmp_path)
    first = derive_cross_mech_snapshot(
        _cross(tmp_path), migrated, tmp_path / "c1", snapshot_date="2026-10-08",
        source_git_commit="b" * 40, generated_at=T)
    reclassify_snapshot(migrated, migrated.parent, snapshot_date="2026-10-09", generated_at=T)
    second = derive_cross_mech_snapshot(
        tmp_path / "c1/cross-mech-duf-examples-2026-10-08.json",
        migrated.parent / "interpro-pfam-duf-2026-10-09.json", tmp_path / "c2",
        snapshot_date="2026-10-09", source_git_commit="e" * 40, generated_at=T)
    assert cross_mech_unscanned(first) == cross_mech_unscanned(second) == {"PF14337"}
    # The label names the worklist the original scan searched, not an intermediate one.
    coverage = second["snapshot"]["derivation"]["coverage"]
    assert coverage["scanned_worklist_snapshot_id"] == "interpro-pfam-duf-2026-10-05"
    assert coverage["scanned_families"] == 2


def test_report_does_not_claim_absence_for_unscanned_families(tmp_path: Path) -> None:
    from dufmech.cross_mech_report import render_cross_mech_report

    migrated = _migrate(tmp_path)
    previous = _previous_names(tmp_path / "prev", [
        {"pfam_id": "PF14337", "short_name": "Abi_alpha", "names": ["DUF1814"]},
    ])
    manifest = derive_cross_mech_snapshot(
        _cross(tmp_path), migrated, tmp_path / "d", snapshot_date="2026-10-08",
        source_git_commit="b" * 40, previous_names_json=previous, generated_at=T)
    rows = json.loads((tmp_path / "d/cross-mech-duf-examples-2026-10-08.json").read_text())
    text = render_cross_mech_report(rows, manifest)
    assert "| PF14337 |  | not scanned (joined after the cross-Mech scan) |" in text
    assert "| PF06172 |  | none; needs a DUFMech member example |" in text
    assert "0 of 1 scanned linked families have a ProteinTraitsMech trait record. 1 linked" in text
    assert "1 worklist families joined later and were never searched" in text


def test_targeting_does_not_claim_missing_examples_for_unscanned_families() -> None:
    from dufmech.example_candidates import (
        TRAITMECH_NAMED,
        TRAITMECH_RENAMED,
        select_target_families,
    )

    rows = [
        {"pfam_id": "PF14337", "source_mech": "TraitMech", "source_section": "record_text",
         "uniprot_accession": ""},
        {"pfam_id": "PF06172", "source_mech": "TraitMech", "source_section": "record_text",
         "uniprot_accession": ""},
    ]
    targets = select_target_families(rows, unscanned={"PF14337"})
    assert targets == {"PF14337": {TRAITMECH_RENAMED}, "PF06172": {TRAITMECH_NAMED}}
