"""Render a deterministic, offline static website for DUF/PUF snapshots."""

from __future__ import annotations

import argparse
import hashlib
import tempfile
from pathlib import Path
from typing import Any

from dufmech.cross_mech import PROTEIN_TRAITS_MECH
from dufmech.cross_mech_snapshot import (
    CROSS_MECH_DIR,
    CROSS_MECH_STEM,
    cross_mech_unscanned,
    load_cross_mech_snapshot,
)
from dufmech.member_snapshot import MEMBER_UNIREF_STEM
from dufmech.report import (
    ReportError,
    build_report,
    family_index,
    iter_metadata_preserving_ancestors,
    latest_snapshot_path,
    load_json_rows,
    load_latest_rows,
    verified_manifest,
)
from dufmech.site import render_artifacts
from dufmech.site_data import tracked_source
from dufmech.site_files import (
    MANIFEST,
    PENDING,
    output_lock,
    output_tree,
    pending_ownership,
    prepare_files,
    remove_obsolete,
)
from dufmech.site_sources import load_source_pins
from dufmech.uniref import DEFAULT_UNIREF_TARGET

PAGES_DIR = Path("pages")
WORKLISTS_DIR = Path("data/worklists")
REPO_ROOT = Path(__file__).resolve().parents[2]


def validate_output_directory(out_dir: Path) -> None:
    """Reject repository roots, ancestors, and symlink destinations before writing."""
    target = out_dir.absolute()
    if target.is_symlink():
        raise ReportError(f"output directory must not be a symlink: {out_dir}")
    resolved = target.resolve()
    for protected in (REPO_ROOT, Path.cwd().resolve(), Path.home().resolve()):
        if resolved == protected or resolved in protected.parents:
            raise ReportError(f"refusing to render into protected directory: {out_dir}")
    if target.exists() and not target.is_dir():
        raise ReportError(f"output is not a directory: {out_dir}")


def render_site(
    worklist_rows: list[dict[str, Any]], score_rows: list[dict[str, Any]], *,
    input_ids: dict[str, str], out_dir: Path,
    cross_mech_rows: list[dict[str, Any]] | None = None,
    cross_mech_sources: dict[str, Any] | None = None,
    cross_mech_unscanned: set[str] | None = None,
    family_metadata: dict[str, dict[str, Any]] | None = None,
    member_rows: list[dict[str, Any]] | None = None,
    provenance: dict[str, Any] | None = None,
    extra_artifacts: dict[str, str] | None = None,
) -> None:
    """Render snapshots with optional curated metadata and actual history artifacts.

    See ``dufmech.site.render_artifacts`` for the metadata adapter contract. Snapshot-only
    callers remain supported and never imply expert review or fabricate history.
    """
    validate_output_directory(out_dir)
    out_dir = out_dir.resolve()
    families = family_index(worklist_rows, score_rows)
    report = build_report(worklist_rows, score_rows, top_n=20)
    cross_mech_rows = cross_mech_rows or []
    report["cross_mech"] = _attach_cross_mech(families, cross_mech_rows, cross_mech_unscanned or set())
    provenance = dict(provenance or {})
    if extra_artifacts:
        provenance["artifact_sha256"] = {
            path: hashlib.sha256(content.encode()).hexdigest()
            for path, content in sorted(extra_artifacts.items())
        }
    artifacts = render_artifacts(
        families, report, input_ids=input_ids, cross_rows=cross_mech_rows,
        cross_sources=cross_mech_sources or {}, family_metadata=family_metadata,
        member_rows=member_rows, provenance=provenance,
    )
    for name, content in (extra_artifacts or {}).items():
        relative = Path(name)
        if relative.is_absolute() or ".." in relative.parts or name in artifacts:
            raise ReportError(f"unsafe or conflicting site artifact: {name}")
        artifacts[name] = content
    with output_lock(out_dir), output_tree(out_dir) as tree:
        stale = prepare_files(artifacts, out_dir, tree=tree)
        # Journal both possible contents before displacement; retries may use different inputs.
        journal = pending_ownership(artifacts, tree)
        with tree.stage() as staged:
            for name, content in artifacts.items():
                staged.write_new(name, content.encode())
            staged.write_new(PENDING, journal.encode())
            tree.replace_from(staged, PENDING)
            for name in artifacts:
                if name != MANIFEST:
                    tree.replace_from(staged, name)
            remove_obsolete(stale, out_dir, tree=tree)
            tree.assert_attached()
            tree.replace_from(staged, MANIFEST)
            tree.remove(PENDING, hashlib.sha256(journal.encode()).hexdigest())


def render_from_paths(
    *, out_dir: Path, worklists_dir: Path = WORKLISTS_DIR,
    worklist_json: Path | None = None, score_json: Path | None = None,
    cross_mech_dir: Path = CROSS_MECH_DIR,
    members_json: Path | None = None,
    records_root: Path | None = None,
) -> None:
    """Load and validate frozen inputs. This build performs no network requests.

    A members JSON input uses the existing pfam-uniprot snapshot format and verified manifest.
    Only the default native corpus discovers its latest default-UniRef member snapshot;
    explicit worklist/score selections and custom directories require ``members_json``.
    """
    record_inputs = (() if records_root is None else tuple(
        records_root / part for part in ("data/families", "curation/families", "history", "reports")
    ))
    for input_path in (worklists_dir, worklist_json, score_json, cross_mech_dir,
                       members_json, *record_inputs):
        if input_path is not None:
            source, target = input_path.resolve(), out_dir.resolve()
            if source == target or target in source.parents or source in target.parents:
                raise ReportError(f"output directory overlaps snapshot inputs: {out_dir}")
    worklist_rows, score_rows, input_ids = load_latest_rows(
        worklists_dir, worklist_json=worklist_json, score_json=score_json,
    )
    provenance = {}
    source_pins = load_source_pins(REPO_ROOT)
    for key in ("worklist", "scores"):
        if key not in input_ids:
            continue
        path = worklist_json if key == "worklist" else score_json
        path = path or worklists_dir / f"{input_ids[key]}.json"
        provenance[key] = tracked_source(path, REPO_ROOT, pins=source_pins)
    cross_mech_rows: list[dict[str, Any]] = []
    cross_mech_sources: dict[str, Any] = {}
    unscanned: set[str] = set()
    cross_mech_path = (latest_snapshot_path(cross_mech_dir, CROSS_MECH_STEM, required=False)
                       if cross_mech_dir.is_dir() else None)
    if cross_mech_path is not None:
        cross_mech_rows, manifest = load_cross_mech_snapshot(
            cross_mech_path, worklist_rows=worklist_rows, worklist_snapshot_id=input_ids["worklist"],
        )
        input_ids["cross_mech"] = cross_mech_path.stem
        cross_mech_sources = dict(manifest["source"].get("mechs", {}))
        unscanned = cross_mech_unscanned(manifest)
        provenance["cross_mech"] = tracked_source(cross_mech_path, REPO_ROOT, pins=source_pins)
    metadata, extra_artifacts = {}, {}
    default_corpus = (worklist_json is None and score_json is None
                      and worklists_dir.resolve() == (REPO_ROOT / WORKLISTS_DIR).resolve())
    if records_root is None and default_corpus:
        if (REPO_ROOT / "data/families").is_dir():
            records_root = REPO_ROOT
        else:
            from dufmech.site_metadata import load_review_site_metadata

            metadata, review_provenance, extra_artifacts = load_review_site_metadata(
                REPO_ROOT, {row["pfam_id"] for row in worklist_rows}, source_pins=source_pins,
            )
            provenance.update(review_provenance)
    if records_root is not None:
        from dufmech.site_metadata import load_site_metadata

        metadata, record_provenance, extra_artifacts = load_site_metadata(
            records_root, input_ids,
            source_pins=source_pins if records_root.resolve() == REPO_ROOT.resolve() else None,
        )
        if set(metadata) != {row["pfam_id"] for row in worklist_rows}:
            raise ReportError("family projections do not cover the complete snapshot catalogue")
        provenance.update(record_provenance)
    members = []
    if members_json is None and default_corpus:
        member_stem = f"{MEMBER_UNIREF_STEM}-{DEFAULT_UNIREF_TARGET.lower()}"
        members_json = latest_snapshot_path(worklists_dir, member_stem, required=False)
    if members_json is not None:
        manifest = verified_manifest(members_json)
        seed = manifest["snapshot"].get("seed_snapshot_id")
        members = [dict(row) for row in load_json_rows(members_json)]
        check_member_seed(
            members, seed, worklist_rows, input_ids["worklist"],
            worklist_json.parent if worklist_json is not None else worklists_dir,
        )
        input_ids["members"] = members_json.stem
        provenance["members"] = {
            **tracked_source(members_json, REPO_ROOT, pins=source_pins),
            "snapshot_id": manifest["snapshot"]["id"],
            "seed_snapshot_id": seed,
            "generated_at": manifest["snapshot"]["generated_at"],
            "sha256": manifest["files"]["json"]["sha256"],
            "source": manifest["source"],
            "row_count": len(members),
            "family_count": len({row.get("pfam_id") for row in members}),
            "local_source": f"datasets/{members_json.name}",
            "local_manifest": f"datasets/{members_json.stem}.manifest.json",
        }
        extra_artifacts[f"datasets/{members_json.name}"] = members_json.read_bytes().decode("utf-8")
        extra_artifacts[f"datasets/{members_json.stem}.manifest.json"] = members_json.with_suffix(
            ".manifest.json"
        ).read_bytes().decode("utf-8")
        if "tsv" in manifest["files"]:
            tsv_name = manifest["files"]["tsv"]["path"]
            if Path(tsv_name).name != tsv_name:
                raise ReportError("member TSV manifest path must be a filename")
            provenance["members"]["local_tsv"] = f"datasets/{tsv_name}"
            extra_artifacts[f"datasets/{tsv_name}"] = (members_json.parent / tsv_name).read_bytes().decode("utf-8")
    render_site(
        [dict(row) for row in worklist_rows], [dict(row) for row in score_rows],
        input_ids=input_ids, out_dir=out_dir, cross_mech_rows=cross_mech_rows,
        cross_mech_sources=cross_mech_sources, cross_mech_unscanned=unscanned,
        family_metadata=metadata,
        member_rows=members, provenance=provenance, extra_artifacts=extra_artifacts,
    )


def diff_trees(expected: Path, actual: Path) -> list[str]:
    """Return deterministic relative paths that differ between two trees."""
    if actual.is_symlink() or not actual.is_dir():
        return ["."]
    left = {path.relative_to(expected): path for path in expected.rglob("*")}
    right = {path.relative_to(actual): path for path in actual.rglob("*")}
    diffs = []
    for name in sorted(left.keys() | right.keys()):
        a, b = left.get(name), right.get(name)
        if a is None or b is None or a.is_symlink() or b.is_symlink():
            diffs.append(name.as_posix())
        elif a.is_dir() and b.is_dir():
            continue
        elif not a.is_file() or not b.is_file() or a.read_bytes() != b.read_bytes():
            diffs.append(name.as_posix())
    return diffs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render the offline DUFMech family website.")
    parser.add_argument("--out", type=Path, default=PAGES_DIR)
    parser.add_argument("--worklists-dir", type=Path, default=WORKLISTS_DIR)
    parser.add_argument("--worklist-json", type=Path)
    parser.add_argument("--score-json", type=Path)
    parser.add_argument("--members-json", type=Path, help="optional verified member-range snapshot")
    parser.add_argument("--records-root", type=Path, help="repository with curated family projections")
    parser.add_argument("--check", action="store_true", help="fail if --out is stale")
    args = parser.parse_args(argv)
    inputs = {"worklists_dir": args.worklists_dir, "worklist_json": args.worklist_json,
              "score_json": args.score_json,
              "members_json": args.members_json, "records_root": args.records_root}
    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            render_from_paths(out_dir=Path(tmp), **inputs)
            if not args.out.exists():
                parser.exit(1, f"{args.out} does not exist; run `just render`\n")
            diffs = diff_trees(Path(tmp), args.out)
        if diffs:
            parser.exit(1, f"{args.out} is stale ({len(diffs)} file(s) differ), "
                        f"including {', '.join(diffs[:5])}; run `just render`\n")
        print(f"{args.out} is current")
        return 0
    render_from_paths(out_dir=args.out, **inputs)
    print(f"rendered DUFMech site under {args.out}")
    return 0


def check_member_seed(
    members: list[dict[str, Any]], seed: Any, worklist_rows: list[Any],
    worklist_id: str, lineage_dir: Path,
) -> None:
    """Accept members seeded on the selected worklist or a metadata-preserving ancestor.

    Members seeded on an ancestor still apply when every derivation since kept the
    families' metadata and every member family is still in the worklist.
    """
    if seed == worklist_id:
        return
    if seed not in iter_metadata_preserving_ancestors(lineage_dir, worklist_id):
        raise ReportError(f"member snapshot was seeded against {seed}, not {worklist_id}")
    catalogue = {row["pfam_id"] for row in worklist_rows}
    if {row.get("pfam_id") for row in members} - catalogue:
        raise ReportError("member snapshot names families absent from the worklist")


def _attach_cross_mech(
    families: list[dict[str, Any]], rows: list[dict[str, Any]], unscanned: set[str] = frozenset(),
) -> dict[str, int]:
    known = {family["pfam_id"] for family in families}
    extra = {row["pfam_id"] for row in rows if row.get("pfam_id")} - known
    if extra:
        raise ReportError(f"cross-Mech families absent from worklist: {', '.join(sorted(extra))}")
    by_pfam: dict[str, dict[str, Any]] = {}
    for row in rows:
        pfam_id = row.get("pfam_id") or ""
        if not pfam_id:
            continue
        entry = by_pfam.setdefault(pfam_id, {"mechs": {}, "proteins": set(), "trait": False})
        if row["source_mech"] == PROTEIN_TRAITS_MECH and row["source_section"] == "trait_identifier":
            entry["trait"] = True
            continue
        entry["mechs"].setdefault(row["source_mech"], set()).add(row["source_path"])
        if row.get("uniprot_accession"):
            entry["proteins"].add(row["uniprot_accession"])
    for family in families:
        entry = by_pfam.get(family["pfam_id"], {"mechs": {}, "proteins": set(), "trait": False})
        family["cross_mech"] = {
            "records_by_mech": {mech: len(paths) for mech, paths in sorted(entry["mechs"].items())},
            "example_proteins": len(entry["proteins"]), "protein_traits_record": entry["trait"],
            # False: the cross-Mech scan never searched this family, so missing links are
            # not evidence of absence.
            "scanned": family["pfam_id"] not in unscanned,
        }
    return {"rows": len(rows), "families": sum(1 for entry in by_pfam.values() if entry["mechs"]),
            "proteins": len({row["uniprot_accession"] for row in rows if row.get("uniprot_accession")}),
            "unscanned_families": len(unscanned & {family["pfam_id"] for family in families})}


if __name__ == "__main__":
    raise SystemExit(main())
