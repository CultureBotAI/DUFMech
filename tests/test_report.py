from __future__ import annotations

import json

from dufmech.report import (
    WORKLIST_STEM,
    build_report,
    family_index,
    latest_snapshot_path,
    load_latest_rows,
    render_report_text,
)


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


def test_load_latest_rows_reads_latest_worklist_and_optional_score(tmp_path) -> None:
    older = tmp_path / f"{WORKLIST_STEM}-2026-09-30.json"
    latest = tmp_path / f"{WORKLIST_STEM}-2026-10-01.json"
    older.write_text(json.dumps([worklist_row("PF00001", proteins=1)]), encoding="utf-8")
    latest.write_text(json.dumps([worklist_row("PF00002", proteins=2)]), encoding="utf-8")
    (tmp_path / f"{WORKLIST_STEM}-2026-10-01.manifest.json").write_text(
        "{}",
        encoding="utf-8",
    )

    assert latest_snapshot_path(tmp_path, WORKLIST_STEM) == latest

    worklist_rows, score_rows, input_ids = load_latest_rows(tmp_path)

    assert [row["pfam_id"] for row in worklist_rows] == ["PF00002"]
    assert score_rows == []
    assert input_ids == {"worklist": latest.stem}
