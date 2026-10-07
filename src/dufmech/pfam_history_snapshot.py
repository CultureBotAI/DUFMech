"""Write versioned snapshots of Pfam families renamed from DUF/UPF names."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.pfam_history import (
    DEFAULT_PFAM_RELEASE,
    PFAM_PREVIOUS_NAMES_TSV_FIELDNAMES,
    PFAM_SEED_URL,
    PfamHistoryError,
    SeedRead,
    read_seed,
    render_previous_names_json,
    render_previous_names_tsv,
)
from dufmech.snapshot import write_snapshot_artifacts

PFAM_PREVIOUS_NAMES_STEM = "pfam-previous-unknown-names"


def write_pfam_previous_names_snapshot(
    read: SeedRead,
    out_dir: Path,
    *,
    release: str,
    source_url: str,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
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
    snapshot_id = f"{PFAM_PREVIOUS_NAMES_STEM}-{snapshot_date}"
    rows = sorted(read.rows, key=lambda row: row.pfam_id)
    json_text = render_previous_names_json(rows) + "\n"
    tsv_text = render_previous_names_tsv(rows) + "\n"
    names = {name for row in rows for name in row.previous_unknown_names}
    manifest = {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
        },
        "source": {
            "name": f"Pfam-A.seed (Pfam release {release})",
            "url": source_url,
            "release": release,
            "last_modified": read.last_modified,
            "compressed_bytes": read.compressed_bytes,
            "compressed_sha256": read.compressed_sha256,
            "families_scanned": read.families_scanned,
            "families_with_previous_ids": read.families_with_previous_ids,
            "selection": (
                "families whose #=GF PI previous identifiers include a DUF/UPF name; "
                "alignments are not retained"
            ),
        },
        "schema": {"tsv_fieldnames": PFAM_PREVIOUS_NAMES_TSV_FIELDNAMES},
        "rows": {
            "total": len(rows),
            "unique_previous_unknown_names": len(names),
            "currently_unknown_name": sum(row.currently_unknown_name for row in rows),
            "renamed_away_from_unknown": sum(not row.currently_unknown_name for row in rows),
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
    parser.add_argument("--pfam-release", default=DEFAULT_PFAM_RELEASE)
    parser.add_argument(
        "--seed-gz", type=Path, help="read a saved Pfam-A.seed.gz instead of downloading it"
    )
    parser.add_argument("--out-dir", type=Path, default=Path("data/worklists"))
    parser.add_argument("--snapshot-date")
    args = parser.parse_args(argv)
    url = PFAM_SEED_URL.format(release=args.pfam_release)
    try:
        read = read_seed(seed_gz=args.seed_gz, release=args.pfam_release)
        manifest = write_pfam_previous_names_snapshot(
            read,
            args.out_dir,
            release=args.pfam_release,
            source_url=url,
            snapshot_date=args.snapshot_date,
        )
    except (PfamHistoryError, OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    rows = manifest["rows"]
    print(
        f"wrote {manifest['snapshot']['id']}: {rows['total']} families, "
        f"{rows['renamed_away_from_unknown']} renamed away from DUF/UPF names "
        f"(scanned {read.families_scanned})"
    )
    return 0


def _file_manifest(name: str, text: str) -> dict[str, Any]:
    data = text.encode("utf-8")
    return {"path": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def _datetime_text(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


if __name__ == "__main__":
    raise SystemExit(main())
