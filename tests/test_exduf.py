from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import httpx
import pytest

from dufmech.exduf import (
    InterProEntryClient,
    MigrationError,
    main,
    plan_migration,
    prepare_migration,
)
from dufmech.pfam_history import PfamPreviousNamesRow, SeedRead
from dufmech.pfam_history_snapshot import write_pfam_previous_names_snapshot
from dufmech.score_inputs import ScoreInputError, load_score_input
from dufmech.scoring import score_families
from dufmech.snapshot import write_worklist_snapshot
from dufmech.worklist import (
    EX_DUF,
    KNOWN_HISTORICAL_DUF,
    PREVIOUS_UNKNOWN_NAME_REASON,
    UNKNOWN_CANDIDATE,
    entry_from_interpro_detail,
    mark_ex_duf,
    reclassify_worklist,
    row_from_interpro_entry,
)
from tests.test_duf_puf_snapshot import interpro_result

T0 = datetime(2026, 10, 5, tzinfo=timezone.utc)


def _row(accession: str, short_name: str, name: str, proteins: int = 10):
    row = row_from_interpro_entry(
        interpro_result(accession=accession, short_name=short_name, name=name, proteins=proteins)
    )
    assert row is not None
    return row


def _detail(accession: str, short: str, name: str) -> dict:
    item = interpro_result(accession=accession, short_name=short, name=name)
    return {
        "metadata": {
            "accession": accession,
            "name": {"name": name, "short": short},
            "integrated": item["metadata"]["integrated"],
            "description": item["extra_fields"]["description"],
            "counters": item["extra_fields"]["counters"],
        }
    }


# A worklist family Pfam renamed, an ordinary DUF, and two renamed families outside it.
PARENT = [
    _row("PF06172", "Cupin_8", "Cupin superfamily (DUF985)"),
    _row("PF01519", "DUF16", "Protein of unknown function DUF16"),
]
PREVIOUS = [
    {"pfam_id": "PF06172", "previous_unknown_names": ["DUF985"], "currently_unknown_name": False},
    {"pfam_id": "PF14337", "previous_unknown_names": ["DUF4393"], "currently_unknown_name": False},
    {"pfam_id": "PF99990", "previous_unknown_names": ["DUF9"], "currently_unknown_name": False},
    # Still DUF-named: not an ex-DUF.
    {"pfam_id": "PF21084", "previous_unknown_names": ["DUF4423"], "currently_unknown_name": True},
]


def _fetch(ids):
    known = {"PF14337": _detail("PF14337", "Abi_alpha", "Abortive infection alpha")}
    return {pfam: known.get(pfam) for pfam in ids}


def test_worklist_helpers_keep_ex_duf_through_reclassification() -> None:
    row = mark_ex_duf(PARENT[0])
    assert row.unknown_status == EX_DUF
    assert row.candidate_reasons[-1] == PREVIOUS_UNKNOWN_NAME_REASON
    assert mark_ex_duf(row) == row
    # Text reclassification recomputes text reasons but keeps EX_DUF.
    assert reclassify_worklist([row])[0].unknown_status == EX_DUF
    assert reclassify_worklist([PARENT[1]])[0].unknown_status == UNKNOWN_CANDIDATE
    detail = row_from_interpro_entry(entry_from_interpro_detail(_detail("PF14337", "Abi_alpha", "Abortive infection alpha")))
    assert (detail.short_name, detail.name, detail.proteins) == ("Abi_alpha", "Abortive infection alpha", 26)


def test_plan_reclassifies_existing_and_adds_renamed_families() -> None:
    plan = plan_migration(PARENT, PREVIOUS, fetch=_fetch)
    by_id = {row.pfam_id: row for row in plan.rows}

    assert by_id["PF06172"].unknown_status == EX_DUF
    assert by_id["PF01519"].unknown_status != EX_DUF
    assert by_id["PF14337"].unknown_status == EX_DUF
    assert plan.added == ["PF14337"]
    assert plan.not_found == ["PF99990"]
    assert "PF21084" not in by_id
    assert [change["pfam_id"] for change in plan.reclassified] == ["PF06172"]


def test_dry_run_lists_families_without_fetching() -> None:
    plan = plan_migration(PARENT, PREVIOUS, fetch=None)
    assert plan.to_fetch == ["PF14337", "PF99990"]
    assert len(plan.rows) == 2


def test_refresh_carries_renamed_and_ex_duf_families_and_refuses_silent_drops() -> None:
    parent = [*PARENT, mark_ex_duf(_row("PF14337", "Abi_alpha", "Abortive infection alpha"))]
    # The new DUF search returns only PF01519; PF06172 (renamed) and PF14337 (already
    # EX_DUF) dropped out and must be carried with re-fetched metadata.
    fetched = {
        "PF06172": _detail("PF06172", "Cupin_8", "Cupin superfamily"),
        "PF14337": _detail("PF14337", "Abi_alpha", "Abortive infection alpha"),
    }
    plan = plan_migration(
        parent, PREVIOUS[:1], fetch=lambda ids: {i: fetched.get(i) for i in ids},
        live_rows=[PARENT[1]],
    )
    assert plan.carried == ["PF06172", "PF14337"]
    assert {row.pfam_id: row.unknown_status for row in plan.rows}["PF06172"] == EX_DUF

    with pytest.raises(MigrationError, match="PF06172"):
        plan_migration(PARENT, [], fetch=_fetch, live_rows=[PARENT[1]])


def _inputs(tmp_path: Path) -> tuple[Path, Path]:
    worklists = tmp_path / "worklists"
    write_worklist_snapshot(PARENT, worklists, snapshot_date="2026-10-05", generated_at=T0)
    rows = [
        PfamPreviousNamesRow(
            pfam_id=item["pfam_id"], pfam_version=f"{item['pfam_id']}.1", short_name="x",
            description="x", previous_unknown_names=tuple(item["previous_unknown_names"]),
            previous_ids=tuple(item["previous_unknown_names"]),
            currently_unknown_name=item["currently_unknown_name"],
        )
        for item in PREVIOUS
    ]
    write_pfam_previous_names_snapshot(
        SeedRead(rows, 4, 4, 1, "0" * 64), worklists, release="38.2", source_url="x",
        snapshot_date="2026-10-07", generated_at=T0,
    )
    return (
        worklists / "interpro-pfam-duf-2026-10-05.json",
        worklists / "pfam-previous-unknown-names-2026-10-07.json",
    )


def test_migrated_snapshot_passes_verified_loader_and_rejects_tampering(tmp_path: Path) -> None:
    parent, previous = _inputs(tmp_path)
    prepared = prepare_migration(
        parent, previous, snapshot_date="2026-10-08", fetch=_fetch,
        generated_at=datetime(2026, 10, 8, tzinfo=timezone.utc),
    )
    out = tmp_path / "out"
    out.mkdir()
    for name, text in prepared.artifacts.items():
        (out / name).write_text(text, encoding="utf-8")

    loaded = load_score_input(out / "interpro-pfam-duf-2026-10-08.json", "worklist")
    assert loaded.provenance["worklist_reclassification"]["profile"] == "exduf-migration-v1"
    manifest = prepared.manifest
    assert manifest["snapshot"]["input_snapshot_ids"] == {
        "worklist": "interpro-pfam-duf-2026-10-05",
        "pfam_previous_names": "pfam-previous-unknown-names-2026-10-07",
    }
    assert manifest["derivation"]["added_pfam_ids"] == ["PF14337"]
    assert manifest["derivation"]["not_found_in_interpro"] == ["PF99990"]
    assert manifest["derivation"]["status_transitions"] == {f"{UNKNOWN_CANDIDATE} -> {EX_DUF}": 1}

    # A row claiming EX_DUF without the migration reason is rejected.
    rows = json.loads((out / "interpro-pfam-duf-2026-10-08.json").read_text("utf-8"))
    rows[-1]["candidate_reasons"] = []
    tampered = tmp_path / "tampered"
    tampered.mkdir()
    import hashlib

    from dufmech.worklist import DufFamilyRow, render_json, render_tsv

    objs = [DufFamilyRow(**{k: (tuple(v) if k == "candidate_reasons" else v)
                            for k, v in row.items() if k != "source_url"}) for row in rows]
    texts = {"json": render_json(objs) + "\n", "tsv": render_tsv(objs) + "\n"}
    bad = json.loads(json.dumps(manifest))
    for kind, text in texts.items():
        (tampered / f"interpro-pfam-duf-2026-10-08.{kind}").write_text(text, encoding="utf-8")
        bad["files"][kind] = {"path": f"interpro-pfam-duf-2026-10-08.{kind}",
                              "bytes": len(text.encode()), "sha256": hashlib.sha256(text.encode()).hexdigest()}
    (tampered / "interpro-pfam-duf-2026-10-08.manifest.json").write_text(json.dumps(bad), "utf-8")
    with pytest.raises(ScoreInputError):
        load_score_input(tampered / "interpro-pfam-duf-2026-10-08.json", "worklist")


def test_migration_requires_newer_date_and_cli_dry_run_writes_nothing(tmp_path: Path, capsys) -> None:
    parent, previous = _inputs(tmp_path)
    with pytest.raises(MigrationError, match="later than the parent"):
        prepare_migration(parent, previous, snapshot_date="2026-10-05", fetch=None)
    out = tmp_path / "out"
    assert main(["--parent-json", str(parent), "--previous-names-json", str(previous),
                 "--snapshot-date", "2026-10-08", "--out-dir", str(out)]) == 0
    assert "dry run" in capsys.readouterr().out
    assert not out.exists()


def test_interpro_entry_client_retries_and_maps_404() -> None:
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.url.path)
        if request.url.path.endswith("PF00002/"):
            return httpx.Response(404)
        if len(calls) == 1:
            return httpx.Response(503)
        return httpx.Response(200, json=_detail("PF00001", "X", "Y"))

    client = InterProEntryClient(transport=httpx.MockTransport(handler), sleep=lambda _: None)
    found = client(["PF00001", "PF00002"])
    assert found["PF00002"] is None
    assert found["PF00001"]["metadata"]["accession"] == "PF00001"
    with pytest.raises(MigrationError, match="not a Pfam family ID"):
        client(["DUF1"])


def test_ex_duf_seed_scores_as_historically_characterized() -> None:
    row = mark_ex_duf(PARENT[0]).tsv_row() | {"candidate_reasons": [PREVIOUS_UNKNOWN_NAME_REASON]}
    scored = score_families([row])[0]
    assert scored.characterization_status == KNOWN_HISTORICAL_DUF
    assert "pfam_renamed_from_unknown_name" in scored.demotion_reasons
