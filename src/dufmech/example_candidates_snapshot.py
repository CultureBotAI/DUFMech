"""Freeze UniProtKB example-protein candidates for DUF families that lack one."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.cross_mech_snapshot import (
    CROSS_MECH_DIR,
    CROSS_MECH_STEM,
    cross_mech_unscanned,
    load_cross_mech_snapshot,
)
from dufmech.example_candidates import (
    CANDIDATE_FIELDS,
    CANDIDATE_SORT,
    EXAMPLE_CANDIDATE_TSV_FIELDNAMES,
    UNIPROTKB_SEARCH_URL,
    CandidateRun,
    ExampleCandidateError,
    UniProtExampleClient,
    render_candidates_json,
    render_candidates_tsv,
    select_target_families,
)
from dufmech.report import ReportError, latest_snapshot_path, load_latest_rows
from dufmech.snapshot import write_snapshot_artifacts

EXAMPLE_CANDIDATES_STEM = "uniprot-duf-example-candidates"


def write_example_candidates_snapshot(
    run: CandidateRun,
    targets: dict[str, set[str]],
    out_dir: Path,
    *,
    per_family: int,
    input_snapshot_ids: dict[str, str],
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    checkpoint_name: str = "",
    limit_families: int | None = None,
    targets_before_limit: int | None = None,
) -> dict[str, Any]:
    """Write a new date-stamped JSON/TSV/manifest set; never replace existing files."""

    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = (
        snapshot_date.isoformat()
        if isinstance(snapshot_date, date)
        else date.fromisoformat(snapshot_date).isoformat()
    )
    snapshot_id = f"{EXAMPLE_CANDIDATES_STEM}-{snapshot_date}"
    rows = sorted(run.rows, key=lambda row: (row.pfam_id, row.rank))
    json_text = render_candidates_json(rows) + "\n"
    tsv_text = render_candidates_tsv(rows) + "\n"
    with_rows = {row.pfam_id for row in rows}
    reviewed_families = {row.pfam_id for row in rows if row.reviewed}
    manifest = {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
            "input_snapshot_ids": input_snapshot_ids,
        },
        "source": {
            "name": "UniProtKB search by Pfam cross-reference",
            "url": UNIPROTKB_SEARCH_URL,
            "query": "xref:pfam-<PFAM_ID>",
            "fields": CANDIDATE_FIELDS,
            "sort": CANDIDATE_SORT,
            "per_family": per_family,
            "uniprot_releases": sorted(run.uniprot_releases),
            "families_fetched": run.families_fetched,
            "checkpoint": {
                "path": checkpoint_name,
                "families_reused": run.families_from_checkpoint,
                "reused_fetch_times": (
                    [min(run.checkpoint_fetch_times), max(run.checkpoint_fetch_times)]
                    if run.checkpoint_fetch_times
                    else []
                ),
            },
            "selection": (
                "Top-ranked UniProtKB entries by annotation score, ties by accession. "
                "Candidates for review, not curated or representative examples."
            ),
        },
        "schema": {"tsv_fieldnames": EXAMPLE_CANDIDATE_TSV_FIELDNAMES},
        "targets": {
            "families": len(targets),
            "limit_families": limit_families,
            "families_before_limit": (
                targets_before_limit if targets_before_limit is not None else len(targets)
            ),
            "by_reason": dict(sorted(Counter(r for v in targets.values() for r in v).items())),
            "families_queried": run.families_queried,
            "families_without_members": sorted(run.families_without_members),
        },
        "rows": {
            "total": len(rows),
            "families_with_candidates": len(with_rows),
            "families_with_reviewed_candidate": len(reviewed_families),
            "reviewed_rows": sum(bool(row.reviewed) for row in rows),
            "unique_uniprot_accessions": len({row.uniprot_accession for row in rows}),
        },
        "files": {
            "json": _file_manifest(f"{snapshot_id}.json", json_text),
            "tsv": _file_manifest(f"{snapshot_id}.tsv", tsv_text),
        },
    }
    write_snapshot_artifacts(
        out_dir,
        {
            f"{snapshot_id}.json": json_text,
            f"{snapshot_id}.tsv": tsv_text,
            f"{snapshot_id}.manifest.json": json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        },
    )
    return manifest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cross-mech-dir", type=Path, default=CROSS_MECH_DIR)
    parser.add_argument("--worklists-dir", type=Path, default=Path("data/worklists"))
    parser.add_argument("--out-dir", type=Path, default=Path("data/worklists"))
    parser.add_argument(
        "--renamed-traitmech-pfam-id",
        action="append",
        default=[],
        help="current Pfam family of a former DUF name cited by TraitMech; repeatable",
    )
    parser.add_argument("--per-family", type=int, default=3)
    parser.add_argument(
        "--limit-families", type=int, help="query only the first N targets (canary runs)"
    )
    parser.add_argument(
        "--checkpoint",
        type=Path,
        default=Path("data/raw/uniprot-duf-example-candidates.jsonl"),
        help="append raw per-family responses here and skip families already present",
    )
    parser.add_argument("--retries", type=int, default=6)
    parser.add_argument("--snapshot-date")
    args = parser.parse_args(argv)
    try:
        worklist_rows, _, input_ids = load_latest_rows(args.worklists_dir)
        cross_path = latest_snapshot_path(args.cross_mech_dir, CROSS_MECH_STEM)
        assert cross_path is not None
        cross_rows, cross_manifest = load_cross_mech_snapshot(
            cross_path, worklist_rows=worklist_rows, worklist_snapshot_id=input_ids["worklist"]
        )
        targets = select_target_families(
            cross_rows, renamed_traitmech_families=args.renamed_traitmech_pfam_id,
            unscanned=cross_mech_unscanned(cross_manifest),
        )
        all_targets = len(targets)
        if args.limit_families is not None:
            if args.out_dir.resolve() == Path("data/worklists").resolve():
                raise ValueError(
                    "--limit-families is for canaries; write them to another --out-dir"
                )
            targets = {key: targets[key] for key in sorted(targets)[: args.limit_families]}
        client = UniProtExampleClient(per_family=args.per_family, retries=args.retries)
        run = client.collect(targets, progress=_progress, checkpoint=args.checkpoint)
        manifest = write_example_candidates_snapshot(
            run,
            targets,
            args.out_dir,
            per_family=args.per_family,
            input_snapshot_ids={"worklist": input_ids["worklist"], "cross_mech": cross_path.stem},
            snapshot_date=args.snapshot_date,
            checkpoint_name=args.checkpoint.name if args.checkpoint else "",
            limit_families=args.limit_families,
            targets_before_limit=all_targets,
        )
    except (ExampleCandidateError, ReportError, OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    rows = manifest["rows"]
    print(
        f"wrote {manifest['snapshot']['id']}: {rows['total']} rows for "
        f"{rows['families_with_candidates']} of {len(targets)} families "
        f"({rows['families_with_reviewed_candidate']} with a reviewed candidate)"
    )
    return 0


def _progress(done: int, total: int) -> None:
    if done == total or done % 250 == 0:
        print(f"queried {done}/{total} families", file=sys.stderr, flush=True)


def _file_manifest(name: str, text: str) -> dict[str, Any]:
    data = text.encode("utf-8")
    return {"path": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def _datetime_text(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


if __name__ == "__main__":
    raise SystemExit(main())
