"""CLI for freezing DUF/PUF examples found in sibling Mech repositories."""

from __future__ import annotations

import argparse
import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

from dufmech.cross_mech import (
    DEFAULT_MECH_SOURCES,
    CrossMechError,
    FamilyIndex,
    UniProtPfamClient,
    load_uniprot_cache,
    render_uniprot_cache,
    scan_mechs,
)
from dufmech.cross_mech_snapshot import CROSS_MECH_DIR, write_cross_mech_snapshot
from dufmech.report import ReportError, load_latest_rows

DEFAULT_MECHS_ROOT = Path(__file__).resolve().parents[3]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mechs-root",
        type=Path,
        default=DEFAULT_MECHS_ROOT,
        help="directory holding sibling Mech checkouts",
    )
    parser.add_argument("--worklists-dir", type=Path, default=Path("data/worklists"))
    parser.add_argument("--worklist-json", type=Path)
    parser.add_argument("--out-dir", type=Path, default=CROSS_MECH_DIR)
    parser.add_argument(
        "--ref",
        default="HEAD",
        help="git ref read in every Mech, for example origin/main after a fetch",
    )
    parser.add_argument(
        "--mech",
        action="append",
        choices=[mech.name for mech in DEFAULT_MECH_SOURCES],
        help="limit the scan to one Mech; repeat for several",
    )
    parser.add_argument(
        "--uniprot-cache",
        type=Path,
        help="read accession lookups from this JSON file when present, else write them there",
    )
    parser.add_argument("--no-uniprot", action="store_true", help="skip UniProtKB lookups")
    parser.add_argument("--snapshot-date")
    args = parser.parse_args(argv)

    try:
        worklist_rows, _, input_ids = load_latest_rows(
            args.worklists_dir, worklist_json=args.worklist_json
        )
        families = FamilyIndex.from_rows(worklist_rows)
        mechs = [mech for mech in DEFAULT_MECH_SOURCES if not args.mech or mech.name in args.mech]
        lookup_info: dict[str, object] = {"mode": "none" if args.no_uniprot else "live"}
        lookup = None if args.no_uniprot else _lookup(args.uniprot_cache, lookup_info)
        result = scan_mechs(
            args.mechs_root, families, mechs=mechs, ref=args.ref, uniprot_lookup=lookup
        )
        result.uniprot_lookup = lookup_info
        manifest = write_cross_mech_snapshot(
            result,
            args.out_dir,
            worklist_snapshot_id=input_ids["worklist"],
            source_ref=args.ref,
            snapshot_date=args.snapshot_date,
        )
    except (CrossMechError, ReportError, OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    rows = manifest["rows"]
    print(
        f"wrote {manifest['snapshot']['id']}: {rows['total']} rows, "
        f"{rows['unique_pfam_ids']} families, {rows['unique_uniprot_accessions']} proteins"
    )
    return 0


def _lookup(cache: Path | None, info: dict[str, object]):
    """Return a UniProtKB lookup that records how it was answered in ``info``."""

    client = UniProtPfamClient()

    def live(accessions):
        info["fetched_at"] = _now()
        info["fetched_accessions"] = len(accessions)
        return client(accessions)

    if cache is None:
        return live

    def cached(accessions):
        # Unresolved accessions are refetched; only resolved lookups are cached.
        rows = load_uniprot_cache(cache.read_text(encoding="utf-8")) if cache.is_file() else {}
        missing = [accession for accession in accessions if accession not in rows]
        info.update({"mode": "cache", "cache_path": cache.name, "cache_hits": len(accessions) - len(missing)})
        if missing:
            rows.update(live(missing))
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_text(render_uniprot_cache(rows) + "\n", encoding="utf-8")
        info["cache_sha256"] = hashlib.sha256(cache.read_bytes()).hexdigest()
        return {accession: rows[accession] for accession in accessions if accession in rows}

    return cached


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


if __name__ == "__main__":
    raise SystemExit(main())
