"""Write versioned snapshots of DUF/PUF examples found in sibling Mechs."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from collections.abc import Mapping, Sequence
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from dufmech.cross_mech import (
    CROSS_MECH_TSV_FIELDNAMES,
    GITHUB_ORG_URL,
    UNIPROTKB_SEARCH_URL,
    CrossMechRow,
    ScanResult,
    render_cross_mech_json,
    render_cross_mech_tsv,
)
from dufmech.report import ReportError, load_json_rows, verified_manifest

CROSS_MECH_STEM = "cross-mech-duf-examples"
CROSS_MECH_DIR = Path("data/cross_mech")


def load_cross_mech_snapshot(
    path: Path,
    *,
    worklist_rows: Sequence[Mapping[str, Any]],
    worklist_snapshot_id: str,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Verify cross-Mech evidence against the selected worklist for every consumer."""

    manifest = verified_manifest(path)
    worklist_input = manifest["snapshot"].get("input_snapshot_ids", {}).get("worklist")
    if worklist_input != worklist_snapshot_id:
        raise ReportError(
            f"{path.name} was built against {worklist_input}, "
            f"not {worklist_snapshot_id}; regenerate the cross-Mech snapshot"
        )
    rows = [dict(row) for row in load_json_rows(path)]
    families = {row["pfam_id"]: row for row in worklist_rows}
    extra = {row["pfam_id"] for row in rows if row["pfam_id"]} - families.keys()
    if extra:
        raise ReportError(f"cross-Mech families absent from worklist: {', '.join(sorted(extra))}")
    if cross_mech_unscanned(manifest) - families.keys():
        raise ReportError(f"{path.name}: coverage names families absent from the worklist")
    for row in rows:
        if row["pfam_id"] and any(
            row[key] != families[row["pfam_id"]][key] for key in ("short_name", "unknown_status")
        ):
            raise ReportError(
                f"{path.name}: {row['pfam_id']} metadata differs from {worklist_snapshot_id}; "
                "regenerate the cross-Mech snapshot"
            )
    return rows, manifest


def write_cross_mech_snapshot(
    result: ScanResult,
    out_dir: Path,
    *,
    worklist_snapshot_id: str,
    source_ref: str,
    snapshot_date: str | date | None = None,
    generated_at: datetime | None = None,
    derivation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Write new date-stamped artifacts, refusing to replace any existing evidence."""

    rows = sorted(result.rows, key=lambda row: row.sort_key())
    generated_at = generated_at or datetime.now(timezone.utc)
    if snapshot_date is None:
        snapshot_date = generated_at.astimezone(timezone.utc).date()
    snapshot_date = (
        snapshot_date.isoformat()
        if isinstance(snapshot_date, date)
        else date.fromisoformat(snapshot_date).isoformat()
    )
    snapshot_id = f"{CROSS_MECH_STEM}-{snapshot_date}"
    json_text = render_cross_mech_json(rows) + "\n"
    tsv_text = render_cross_mech_tsv(rows) + "\n"

    proteins = {row.uniprot_accession for row in rows if row.uniprot_accession}
    manifest = {
        "snapshot": {
            "id": snapshot_id,
            "date": snapshot_date,
            "generated_at": _datetime_text(generated_at),
            "input_snapshot_ids": {"worklist": worklist_snapshot_id},
            "source_ref": source_ref,
        },
        "source": {
            "name": "Curated YAML records in sibling CultureBotAI Mech repositories",
            "url": GITHUB_ORG_URL,
            "mechs": result.mechs,
            "uniprotkb_url": UNIPROTKB_SEARCH_URL,
            "uniprotkb_accessions_requested": result.uniprot_requested,
            "uniprotkb_accessions_resolved": result.uniprot_resolved,
            "uniprotkb_accessions_unresolved": result.uniprot_unresolved,
            "uniprotkb_lookup": result.uniprot_lookup,
        },
        "schema": {"tsv_fieldnames": CROSS_MECH_TSV_FIELDNAMES},
        "rows": {
            "total": len(rows),
            "unique_pfam_ids": len({row.pfam_id for row in rows if row.pfam_id}),
            "unlisted_short_names": len({row.short_name for row in rows if not row.pfam_id}),
            "unique_uniprot_accessions": len(proteins),
            "by_source_mech": _counts(row.source_mech for row in rows),
            "by_source_section": _counts(row.source_section for row in rows),
            "by_unknown_status": _counts(row.unknown_status for row in rows),
            "pfam_ids_by_source_mech": {
                mech: len({row.pfam_id for row in rows if row.source_mech == mech and row.pfam_id})
                for mech in sorted({row.source_mech for row in rows})
            },
        },
        "files": {
            "json": _file_manifest(f"{snapshot_id}.json", json_text),
            "tsv": _file_manifest(f"{snapshot_id}.tsv", tsv_text),
        },
    }
    if derivation is not None:
        manifest["snapshot"]["derivation"] = dict(derivation)
    # Encode the complete set before opening anything. Exclusive creation also
    # protects against a destination appearing after the existence check.
    artifacts = {
        out_dir / f"{snapshot_id}.json": json_text.encode("utf-8"),
        out_dir / f"{snapshot_id}.tsv": tsv_text.encode("utf-8"),
        out_dir / f"{snapshot_id}.manifest.json": (
            json.dumps(manifest, indent=2, sort_keys=True) + "\n"
        ).encode("utf-8"),
    }
    for path in artifacts:
        if path.exists() or path.is_symlink():
            raise FileExistsError(f"snapshot artifact already exists: {path}")
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    try:
        for path, data in artifacts.items():
            with path.open("xb") as handle:
                written.append(path)
                handle.write(data)
    except OSError:
        for path in written:
            path.unlink()
        raise
    return manifest


def _counts(values: Any) -> dict[str, int]:
    return dict(sorted(Counter(values).items()))


def _file_manifest(name: str, text: str) -> dict[str, Any]:
    data = text.encode("utf-8")
    return {"path": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def _datetime_text(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


DERIVATION_METHOD = (
    "Offline seed-status relabel against a newer verified worklist; no upstream data refetched"
)
UNLISTED_BASIS = "record_mentions_unlisted_short_name"
PREVIOUS_NAME_BASIS = "record_mentions_previous_pfam_name"


def cross_mech_unscanned(manifest: Mapping[str, Any]) -> set[str]:
    """Worklist families a cross-Mech snapshot's scan never searched (derivations only).

    A direct scan covers every family of its worklist. A relabel derivation onto a
    worklist with families the scan did not search records them as
    ``snapshot.derivation.coverage.unscanned_pfam_ids``; absent links for those families
    are not evidence of absence.
    """

    derivation = manifest.get("snapshot", {}).get("derivation") or {}
    coverage = derivation.get("coverage") or {}
    return set(coverage.get("unscanned_pfam_ids") or ())


def derive_cross_mech_snapshot(
    source_json: Path,
    worklist_json: Path,
    out_dir: Path,
    *,
    snapshot_date: str,
    source_git_commit: str,
    previous_names_json: Path | None = None,
    generated_at: datetime | None = None,
) -> dict[str, Any]:
    """Relabel a cross-Mech snapshot's seed statuses from a newer verified worklist.

    Every row keeps its source record, protein, link bases and biological metadata;
    ``unknown_status`` of resolved rows is replaced from the target worklist. Evidence
    acquisition dates, Mech commits and UniProt lookup provenance remain those of the
    source snapshot. Rows naming a family the worklist lacks are an error: relabeling
    never drops evidence.

    Coverage: target families the source scan never searched (absent from the source's
    worklist, or already unscanned upstream) are recorded as unscanned, so consumers do
    not read missing links as absence.

    With ``previous_names_json`` (a verified Pfam previous-identifier snapshot), a row
    citing an unlisted DUF/UPF name that maps to exactly one target family is resolved to
    that family, with link basis ``record_mentions_previous_pfam_name``.
    """

    source_manifest = verified_manifest(source_json)
    target_manifest = verified_manifest(worklist_json)
    if not target_manifest["snapshot"]["id"].startswith("interpro-pfam-duf-"):
        raise ReportError(f"{worklist_json.name} is not a worklist snapshot")
    if not re_commit(source_git_commit):
        raise ReportError("source_git_commit must be a full lowercase commit SHA")
    families = {row["pfam_id"]: row for row in load_json_rows(worklist_json)}
    source_worklist_id = source_manifest["snapshot"]["input_snapshot_ids"]["worklist"]
    source_worklist = worklist_json.parent / f"{source_worklist_id}.json"
    verified_manifest(source_worklist)
    scanned = {row["pfam_id"] for row in load_json_rows(source_worklist)}
    scanned -= cross_mech_unscanned(source_manifest)
    unscanned = sorted(families.keys() - scanned)

    index: dict[str, list[str]] = {}
    previous_provenance: dict[str, Any] = {}
    if previous_names_json is not None:
        previous_manifest = verified_manifest(previous_names_json)
        for item in load_json_rows(previous_names_json):
            for name in item.get("previous_unknown_names") or ():
                index.setdefault(name, []).append(item["pfam_id"])
        previous_provenance = {
            "previous_names_snapshot_id": previous_manifest["snapshot"]["id"],
            "previous_names_json_sha256": hashlib.sha256(
                previous_names_json.read_bytes()).hexdigest(),
        }

    rows: list[CrossMechRow] = []
    changed = 0
    resolved: dict[str, str] = {}
    ambiguous: set[str] = set()
    backfilled = False
    for item in load_json_rows(source_json):
        values = {**item, "link_basis": tuple(item.get("link_basis") or ())}
        if "cited_uniprot_accession" not in values:
            values["cited_uniprot_accession"] = ""
            backfilled = True
        if not values["pfam_id"] and UNLISTED_BASIS in values["link_basis"] and index:
            targets = sorted({pfam for pfam in index.get(values["short_name"], ()) if pfam in families})
            if len(targets) == 1:
                resolved[values["short_name"]] = targets[0]
                values["pfam_id"] = targets[0]
                values["short_name"] = families[targets[0]]["short_name"]
                values["link_basis"] = tuple(sorted(
                    (set(values["link_basis"]) - {UNLISTED_BASIS}) | {PREVIOUS_NAME_BASIS}
                ))
            elif len(targets) > 1:
                ambiguous.add(values["short_name"])
        if values["pfam_id"]:
            family = families.get(values["pfam_id"])
            if family is None:
                raise ReportError(f"{values['pfam_id']} is absent from {worklist_json.name}")
            if family["unknown_status"] != values["unknown_status"]:
                changed += 1
            values["unknown_status"] = family["unknown_status"]
        rows.append(CrossMechRow(**values))
    keys = [row.sort_key() for row in rows]
    if len(keys) != len(set(keys)):
        raise ReportError("relabeled cross-Mech rows collide; resolve duplicates before deriving")
    source = source_manifest["source"]
    result = ScanResult(
        rows=rows,
        mechs=source["mechs"],
        uniprot_requested=source.get("uniprotkb_accessions_requested", 0),
        uniprot_resolved=source.get("uniprotkb_accessions_resolved", 0),
        uniprot_unresolved=source.get("uniprotkb_accessions_unresolved", []),
        uniprot_lookup=source.get("uniprotkb_lookup", {}),
    )
    derivation = {
        "method": DERIVATION_METHOD,
        "rows_with_changed_seed_status": changed,
        "source_git_commit": source_git_commit,
        "source_json_sha256": hashlib.sha256(source_json.read_bytes()).hexdigest(),
        "source_manifest_sha256": hashlib.sha256(
            source_json.with_suffix(".manifest.json").read_bytes()
        ).hexdigest(),
        "source_snapshot_id": source_manifest["snapshot"]["id"],
        "source_worklist_snapshot_id": source_worklist_id,
        "target_worklist_json_sha256": hashlib.sha256(worklist_json.read_bytes()).hexdigest(),
        "coverage": {
            "scanned_worklist_snapshot_id": source_worklist_id,
            "scanned_families": len(scanned & families.keys()),
            "unscanned_pfam_ids": unscanned,
        },
    }
    if previous_provenance:
        derivation.update(previous_provenance)
        derivation["resolved_previous_names"] = dict(sorted(resolved.items()))
        derivation["rows_resolved_by_previous_name"] = sum(
            PREVIOUS_NAME_BASIS in row.link_basis for row in rows
        )
        derivation["ambiguous_previous_names"] = sorted(ambiguous)
    if backfilled:
        derivation["backfilled_fields"] = {
            "cited_uniprot_accession": "empty: not recorded by the source scan"
        }
    return write_cross_mech_snapshot(
        result,
        out_dir,
        worklist_snapshot_id=target_manifest["snapshot"]["id"],
        source_ref=source_manifest["snapshot"].get("source_ref", ""),
        snapshot_date=snapshot_date,
        generated_at=generated_at,
        derivation=derivation,
    )


def re_commit(value: str) -> bool:
    return bool(re.fullmatch(r"[0-9a-f]{40}", value))


def main(argv: list[str] | None = None) -> int:
    """Derive a relabeled cross-Mech snapshot for a newer worklist (offline)."""

    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument("--source-json", type=Path, required=True)
    parser.add_argument("--worklist-json", type=Path, required=True)
    parser.add_argument("--snapshot-date", required=True)
    parser.add_argument("--source-git-commit", required=True, help="commit holding --source-json")
    parser.add_argument(
        "--previous-names-json", type=Path,
        help="Pfam previous-identifier snapshot used to resolve unlisted DUF/UPF names",
    )
    parser.add_argument("--out-dir", type=Path, default=CROSS_MECH_DIR)
    args = parser.parse_args(argv)
    try:
        manifest = derive_cross_mech_snapshot(
            args.source_json, args.worklist_json, args.out_dir,
            snapshot_date=args.snapshot_date, source_git_commit=args.source_git_commit,
            previous_names_json=args.previous_names_json,
        )
    except (ReportError, OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f"cross-Mech derivation failed: {exc}\n")
    print(
        f"wrote {manifest['snapshot']['id']}: {manifest['rows']['total']} rows; "
        f"{manifest['snapshot']['derivation']['rows_with_changed_seed_status']} seed labels changed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
