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
        ScanResult(rows=rows, mechs={"TraitMech": {"commit": "a" * 40}}), out,
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
    assert manifest["source"]["mechs"] == {"TraitMech": {"commit": "a" * 40}}


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
