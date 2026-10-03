from __future__ import annotations

import json

import pytest

from dufmech.report import (
    WORKLIST_STEM,
    ReportError,
    build_report,
    family_index,
    latest_snapshot_path,
    load_json_rows,
    load_latest_rows,
    render_report_text,
)
from dufmech.scoring_snapshot import SCORE_STEM, write_score_snapshot
from dufmech.snapshot import write_worklist_snapshot
from dufmech.worklist import DufFamilyRow
from scripts.duf_puf_report import main as report_main
from tests.test_scoring_snapshot import score_row


def worklist_row(
    pfam_id: str,
    *,
    proteins: int,
    unknown_status: str = "UNKNOWN_CANDIDATE",
) -> dict[str, object]:
    return {
        "pfam_id": pfam_id,
        "short_name": f"DUF{pfam_id[-1]}",
        "name": f"Domain of unknown function {pfam_id}",
        "interpro_id": f"IPR{pfam_id[-5:]}",
        "unknown_status": unknown_status,
        "candidate_reasons": ["short_name_matches_duf"],
        "proteins": proteins,
        "matches": proteins + 1,
        "proteomes": 2,
        "taxa": 3,
        "structures": 1,
        "alphafold_models": proteins,
        "domain_architectures": 4,
        "description": "unknown",
        "source_url": f"https://www.ebi.ac.uk/interpro/api/entry/pfam/{pfam_id}",
    }


def test_family_index_joins_scores_and_sorts_by_proteins() -> None:
    rows = family_index(
        [
            worklist_row("PF00001", proteins=10),
            worklist_row("PF00002", proteins=20),
        ],
        [
            {
                "pfam_id": "PF00001",
                "characterization_status": "PARTIALLY_CHARACTERIZED",
                "demotion_reasons": ["has_ncbifam_hit"],
                "known_evidence_count": 0,
                "partial_evidence_count": 1,
                "context_evidence_count": 2,
            }
        ],
    )

    assert [row["pfam_id"] for row in rows] == ["PF00002", "PF00001"]
    assert rows[1]["characterization_status"] == "PARTIALLY_CHARACTERIZED"
    assert rows[1]["partial_evidence_count"] == 1
    assert rows[1]["demotion_reasons"] == ["has_ncbifam_hit"]


def test_build_report_counts_worklist_and_score_facets() -> None:
    report = build_report(
        [
            worklist_row("PF00001", proteins=10),
            worklist_row(
                "PF00002",
                proteins=20,
                unknown_status="KNOWN_HISTORICAL_DUF",
            ),
        ],
        [
            {
                "pfam_id": "PF00001",
                "characterization_status": "PARTIALLY_CHARACTERIZED",
                "demotion_reasons": ["has_ncbifam_hit"],
            }
        ],
        top_n=1,
    )

    assert report["families"]["total"] == 2
    assert report["families"]["interpro_proteins"] == 30
    assert report["by_unknown_status"] == {
        "KNOWN_HISTORICAL_DUF": 1,
        "UNKNOWN_CANDIDATE": 1,
    }
    assert report["by_characterization_status"] == {
        "PARTIALLY_CHARACTERIZED": 1,
        "UNSCORED": 1,
    }
    assert report["by_candidate_reason"] == {"short_name_matches_duf": 2}
    assert report["by_demotion_reason"] == {"has_ncbifam_hit": 1}
    assert [row["pfam_id"] for row in report["top_by_proteins"]] == ["PF00002"]


def test_render_report_text_includes_input_ids() -> None:
    text = render_report_text(
        build_report([worklist_row("PF00001", proteins=10)]),
        input_ids={"worklist": "interpro-pfam-duf-2026-10-01"},
    )

    assert "DUFMech corpus report" in text
    assert "worklist interpro-pfam-duf-2026-10-01" in text
    assert "1 DUF/Pfam worklist families" in text


def freeze_worklist(tmp_path, *, snapshot_date="2026-10-01", pfam_id="PF00001"):
    row = worklist_row(pfam_id, proteins=10)
    del row["source_url"]
    write_worklist_snapshot(
        [DufFamilyRow(**row)], tmp_path, snapshot_date=snapshot_date
    )
    return tmp_path / f"{WORKLIST_STEM}-{snapshot_date}.json"


def test_load_latest_rows_reads_latest_worklist_and_optional_score(tmp_path) -> None:
    freeze_worklist(tmp_path, snapshot_date="2026-09-30")
    latest = freeze_worklist(tmp_path, pfam_id="PF00002")

    assert latest_snapshot_path(tmp_path, WORKLIST_STEM) == latest

    worklist_rows, score_rows, input_ids = load_latest_rows(tmp_path)

    assert [row["pfam_id"] for row in worklist_rows] == ["PF00002"]
    assert score_rows == []
    assert input_ids == {"worklist": latest.stem}


def test_load_latest_rows_accepts_matching_score_lineage(tmp_path) -> None:
    worklist = freeze_worklist(tmp_path)
    write_score_snapshot(
        [score_row()], tmp_path, snapshot_date="2026-10-02",
        input_snapshot_ids={"worklist": worklist.stem},
    )
    rows, scores, ids = load_latest_rows(tmp_path)
    assert len(rows) == len(scores) == 1
    assert ids["scores"] == f"{SCORE_STEM}-2026-10-02"


@pytest.mark.parametrize("explicit", [False, True])
def test_load_latest_rows_rejects_mismatched_lineage(tmp_path, explicit) -> None:
    worklist = freeze_worklist(tmp_path)
    freeze_worklist(tmp_path, snapshot_date="2026-10-03")
    write_score_snapshot(
        [score_row()], tmp_path, snapshot_date="2026-10-02",
        input_snapshot_ids={"worklist": worklist.stem},
    )
    kwargs = {"score_json": tmp_path / f"{SCORE_STEM}-2026-10-02.json"} if explicit else {}
    with pytest.raises(ReportError, match="was scored against.*select matching"):
        load_latest_rows(tmp_path, **kwargs)


def test_load_latest_rows_rejects_missing_score_lineage(tmp_path) -> None:
    freeze_worklist(tmp_path)
    write_score_snapshot([score_row()], tmp_path, snapshot_date="2026-10-02")
    with pytest.raises(ReportError, match="input_snapshot_ids.worklist is required"):
        load_latest_rows(tmp_path)


def test_load_latest_rows_rejects_missing_manifest(tmp_path) -> None:
    path = freeze_worklist(tmp_path)
    path.with_suffix(".manifest.json").unlink()
    with pytest.raises(ReportError, match="could not read manifest"):
        load_latest_rows(tmp_path)


def test_latest_snapshot_rejects_invalid_calendar_dates(tmp_path) -> None:
    (tmp_path / f"{WORKLIST_STEM}-2026-99-99.json").write_text("[]", encoding="utf-8")
    with pytest.raises(ReportError, match="invalid snapshot date"):
        latest_snapshot_path(tmp_path, WORKLIST_STEM)


def test_load_rows_rejects_non_objects(tmp_path) -> None:
    path = tmp_path / "rows.json"
    path.write_text(json.dumps([{"pfam_id": "PF00001"}, 42]), encoding="utf-8")
    with pytest.raises(ReportError, match="every row"):
        load_json_rows(path)


@pytest.mark.parametrize("pfam_id", [None, "", "PF1", " PF00001", 42])
def test_family_index_rejects_invalid_identifiers(pfam_id) -> None:
    with pytest.raises(ReportError, match="invalid worklist pfam_id"):
        family_index([{"pfam_id": pfam_id}])


@pytest.mark.parametrize("label", ["worklist", "scores"])
def test_family_index_rejects_duplicate_families(label) -> None:
    row = worklist_row("PF00001", proteins=10)
    worklist, scores = ([row, row], []) if label == "worklist" else ([row], [row, row])
    with pytest.raises(ReportError, match=f"duplicate {label}"):
        family_index(worklist, scores)


def test_family_index_rejects_foreign_score_families() -> None:
    with pytest.raises(ReportError, match="score families absent from worklist"):
        family_index([worklist_row("PF00001", proteins=10)], [{"pfam_id": "PF00002"}])


@pytest.mark.parametrize("value", [None, [], {}, "UNRECOGNIZED"])
def test_family_index_rejects_invalid_statuses(value) -> None:
    row = worklist_row("PF00001", proteins=10)
    with pytest.raises(ReportError, match="invalid unknown_status"):
        family_index([{**row, "unknown_status": value}])
    with pytest.raises(ReportError, match="invalid characterization_status"):
        family_index([row], [{"pfam_id": "PF00001", "characterization_status": value}])


def test_family_index_preserves_missing_counts_and_zero() -> None:
    row = worklist_row("PF00001", proteins=0)
    missing = {**row, "pfam_id": "PF00002", "proteins": None, "structures": None}
    families = family_index([missing, row])
    assert families[0]["proteins"] == 0
    assert families[1]["proteins"] is None
    assert families[1]["structures"] is None
    assert families[0]["known_evidence_count"] is None
    report = build_report([missing, row])
    assert report["families"]["missing_protein_counts"] == 1
    assert report["families"]["with_structures"] == 1


@pytest.mark.parametrize("value", [-1, True, 1.5, "1"])
def test_family_index_rejects_invalid_counts(value) -> None:
    with pytest.raises(ReportError, match="proteins must be a non-negative integer or null"):
        family_index([{**worklist_row("PF00001", proteins=10), "proteins": value}])


def test_report_cli_renders_top_limit_and_rejects_negative(tmp_path, capsys) -> None:
    freeze_worklist(tmp_path)
    assert report_main(["--worklists-dir", str(tmp_path), "--top", "1"]) == 0
    text = capsys.readouterr().out
    assert "Top families by protein count:" in text
    assert "PF00001" in text
    assert "not counts of unique proteins" in text
    assert report_main(["--worklists-dir", str(tmp_path), "--top", "0"]) == 0
    assert "Top families" not in capsys.readouterr().out
    with pytest.raises(SystemExit) as exc:
        report_main(["--top", "-1"])
    assert exc.value.code == 2
    with pytest.raises(ReportError, match="top_n"):
        build_report([], top_n=-1)
