"""Capture and verify the exact source bytes used by characterization scoring.

Each payload, manifest, and TSV is read once. Validation and parsing use those
buffers, so a later filesystem replacement cannot change what was scored.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import stat
from collections import Counter
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

import dufmech.alphafold_snapshot as af
import dufmech.cath_snapshot as cath
import dufmech.cdsearch_snapshot as cdd
import dufmech.efi_gnt_snapshot as efi
import dufmech.eggnog_snapshot as egg
import dufmech.jgi_img_snapshot as img
import dufmech.member_snapshot as members
import dufmech.mgnify_snapshot as mg
import dufmech.ncbifam_snapshot as ncb
import dufmech.pdbe_kb_snapshot as pdbe
import dufmech.quickgo_snapshot as go
import dufmech.rcsb_snapshot as rcsb
import dufmech.rhea_snapshot as rhea
import dufmech.snapshot as worklist
import dufmech.stringdb_snapshot as string
import dufmech.threedbeacons_snapshot as beacons
from dufmech.worklist import (
    CLASSIFIER_POLICY,
    EX_DUF,
    MIGRATED_SOURCE,
    MIGRATION_NOTE,
    MIGRATION_POLICY,
    MIGRATION_PROFILE,
    MIGRATION_REFRESH_NOTE,
    PREVIOUS_UNKNOWN_NAME_REASON,
)

RECLASSIFIED_SOURCE = "Reclassification of frozen InterPro Pfam API metadata"
RECLASSIFICATION_NOTE = (
    "No new API retrieval; all names, descriptions, identifiers and counters "
    "are copied unchanged from the source snapshot."
)
LEGACY_RECLASSIFICATION_POLICY = (
    "Recognize explicit unknown-function names and family/families descriptions; "
    "seed status is a metadata classification, not experimental evidence."
)


class ScoreInputError(ValueError):
    """A scoring input or its retained provenance is missing, malformed, or inconsistent."""


@dataclass(frozen=True)
class InputSpec:
    stem: str
    fields: list[str]
    identity: tuple[str, ...]
    source: Mapping[str, str]
    version_field: str | None = None
    json_only_fields: tuple[str, ...] = ()


# Reuse the producers' headers, URL constants, and stems. Evidence identities
# identify an annotation, not just its protein; full annotation content is kept.
INPUT_SPECS = {
    "worklist": InputSpec(worklist.WORKLIST_STEM, worklist.TSV_FIELDNAMES, ("pfam_id",),
                          {"name": "InterPro Pfam API", "url": worklist.INTERPRO_PFAM_URL}),
    "members": InputSpec(members.MEMBER_UNIREF_STEM, members.MEMBER_UNIREF_TSV_FIELDNAMES,
                         ("pfam_id", "uniprot_accession"), {
                             "interpro_pfam_proteins_url": members.INTERPRO_PFAM_PROTEINS_URL,
                             "uniprotkb_search_url": members.UNIPROTKB_SEARCH_URL,
                             "uniprot_id_mapping_url": members.UNIPROT_ID_MAPPING_URL,
                         }, "uniref_target"),
    "alphafold": InputSpec(af.ALPHAFOLD_STEM, af.ALPHAFOLD_TSV_FIELDNAMES,
                           ("uniprot_accession", "model_entity_id"),
                           {"name": "AlphaFold DB API", "prediction_url": af.ALPHAFOLD_PREDICTION_URL}),
    "cath": InputSpec(cath.CATH_STEM, cath.CATH_TSV_FIELDNAMES,
                      ("uniprot_accession", "superfamily_id", "funfam_number"),
                      {"name": "CATH-Gene3D UniProt to FunFam API",
                       "api_url": cath.CATH_UNIPROT_TO_FUNFAM_URL}, "cath_version", ("cath_version",)),
    "cdsearch": InputSpec(cdd.CDSEARCH_STEM, cdd.CDSEARCH_TSV_FIELDNAMES,
                          ("uniprot_accession", "cdd_accession", "hit_type"),
                          {"name": "NCBI Batch CD-Search", "url": cdd.CDSEARCH_URL}),
    "efi_gnt": InputSpec(efi.EFI_GNT_STEM, efi.EFI_GNT_TSV_FIELDNAMES,
                         ("query_id", "neighbor_id", "neighbor_pfam"),
                         {"name": "EFI-GNT Pfam Neighbor Mapping Table", "url": efi.EFI_GNT_URL}),
    "eggnog": InputSpec(egg.EGGNOG_STEM, egg.EGGNOG_TSV_FIELDNAMES,
                        ("query_id",),
                        {"name": "eggNOG-mapper annotations", "url": egg.EGGNOG_MAPPER_URL}),
    "jgi_img": InputSpec(img.JGI_IMG_STEM, img.JGI_IMG_TSV_FIELDNAMES,
                         ("query_id", "neighbor_gene_oid", "neighbor_pfam"),
                         {"name": "JGI IMG gene-neighborhood table", "url": img.JGI_IMG_URL}),
    "mgnify": InputSpec(mg.MGNIFY_STEM, mg.MGNIFY_TSV_FIELDNAMES, ("pfam_id", "mgyp"),
                        {"name": "MGnify Proteins API", "search_url": mg.MGNIFY_PROTEIN_SEARCH_URL}),
    "ncbifam": InputSpec(ncb.NCBIFAM_STEM, ncb.NCBIFAM_TSV_FIELDNAMES,
                         ("query_id", "ncbifam_accession"),
                         {"name": "NCBI Protein Family Model HMMs", "url": ncb.NCBIFAM_HMM_FTP_URL}),
    "pdbe_kb": InputSpec(pdbe.PDBE_KB_STEM, pdbe.PDBE_KB_TSV_FIELDNAMES,
                         ("seed_uniprot_accession", "pdb_id", "entity_id", "endpoint"),
                         {"name": "PDBe API entity annotation endpoints", "base_url": pdbe.PDBE_KB_BASE_URL}),
    "quickgo": InputSpec(go.QUICKGO_STEM, go.QUICKGO_TSV_FIELDNAMES,
                         ("uniprot_accession", "go_id"),
                         {"name": "QuickGO annotation search API", "url": go.QUICKGO_ANNOTATION_URL}),
    "rcsb": InputSpec(rcsb.RCSB_STEM, rcsb.RCSB_TSV_FIELDNAMES, ("uniprot_accession", "pdb_id"),
                      {"name": "RCSB PDB Search and Data APIs", "search_url": rcsb.RCSB_SEARCH_URL,
                       "graphql_url": rcsb.RCSB_GRAPHQL_URL}),
    "rhea": InputSpec(rhea.RHEA_STEM, rhea.RHEA_TSV_FIELDNAMES, ("uniprot_accession", "rhea_id"),
                      {"name": "Rhea REST API", "url": rhea.RHEA_URL}),
    "stringdb": InputSpec(string.STRINGDB_STEM, string.STRING_TSV_FIELDNAMES,
                          ("uniprot_accession", "partner_string_id"),
                          {"name": "STRING v12.0 API", "api_url": string.STRING_API_URL}),
    "threedbeacons": InputSpec(beacons.THREEDBEACONS_STEM, beacons.THREEDBEACONS_TSV_FIELDNAMES,
                              ("uniprot_accession", "model_identifier"),
                              {"name": "3D-Beacons Network UniProt summary API",
                               "api_url": beacons.THREEDBEACONS_API_URL}),
}


@dataclass(frozen=True)
class ScoreInput:
    rows: tuple[dict[str, Any], ...]
    provenance: dict[str, Any]


def _read_bytes(path: Path) -> bytes:
    descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
    with os.fdopen(descriptor, "rb") as handle:
        if not stat.S_ISREG(os.fstat(handle.fileno()).st_mode):
            raise ScoreInputError(f"input must be a regular file: {path}")
        return handle.read()


def _object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ScoreInputError(f"duplicate JSON object key: {key}")
        result[key] = value
    return result


def _constant(value: str) -> None:
    raise ScoreInputError(f"non-finite JSON value: {value}")


def _json(raw: bytes, path: Path) -> Any:
    try:
        return json.loads(raw.decode("utf-8"), object_pairs_hook=_object, parse_constant=_constant)
    except (ValueError, UnicodeError) as exc:
        raise ScoreInputError(f"invalid JSON in {path}: {exc}") from exc


def _digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _mapping(value: Any, label: str) -> dict:
    if not isinstance(value, dict):
        raise ScoreInputError(f"{label} must be an object")
    return value


def _timestamp(value: Any) -> datetime:
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError("missing timezone")
        return parsed
    except ValueError as exc:
        raise ScoreInputError("reclassification timestamp must include a timezone") from exc


def _source_identity(
    role: str, snapshot_id: str, source: dict, fields: Any, lineage: Any = None,
) -> None:
    spec = INPUT_SPECS[role]
    if fields != spec.fields:
        raise ScoreInputError(f"{role}: manifest header does not match source role")
    expected = spec.source
    if role == "worklist" and source.get("name") == RECLASSIFIED_SOURCE:
        expected = {**expected, "name": RECLASSIFIED_SOURCE, "note": RECLASSIFICATION_NOTE}
        _timestamp(source.get("original_generated_at"))
        if lineage is None:
            raise ScoreInputError("reclassification source requires native lineage provenance")
    if role == "worklist" and source.get("name") == MIGRATED_SOURCE:
        # A migrated worklist, or a later text reclassification of one (derivation-v2),
        # which copies its parent's source block.
        if lineage is None or lineage.get("profile") not in {MIGRATION_PROFILE, "derivation-v2"}:
            raise ScoreInputError("EX_DUF migration source requires migration lineage provenance")
        if lineage.get("profile") == MIGRATION_PROFILE:
            note = MIGRATION_REFRESH_NOTE if lineage.get("refresh") else MIGRATION_NOTE
        else:
            note = source.get("note") if source.get("note") in {
                MIGRATION_NOTE, MIGRATION_REFRESH_NOTE} else MIGRATION_NOTE
        expected = {**expected, "name": MIGRATED_SOURCE, "note": note}
        _timestamp(source.get("original_generated_at"))
    if any(source.get(key) != value for key, value in expected.items()):
        raise ScoreInputError(f"{role}: manifest source identity does not match source role")
    prefix = spec.stem
    if spec.version_field:
        version = source.get(spec.version_field)
        if not isinstance(version, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", version):
            raise ScoreInputError(f"{role}: invalid source version/target")
        if role == "members":
            if version not in {"UniRef50", "UniRef90", "UniRef100"}:
                raise ScoreInputError("members: unsupported UniRef target")
            version = version.lower()
        prefix += f"-{version}"
    if not re.fullmatch(re.escape(prefix) + r"-\d{4}-\d{2}-\d{2}", snapshot_id):
        raise ScoreInputError(f"{role}: snapshot stem does not match source role")
    try:
        date.fromisoformat(snapshot_id[-10:])
    except ValueError as exc:
        raise ScoreInputError(f"{role}: invalid snapshot date") from exc
    if lineage is not None:
        lineage = _mapping(lineage, "worklist reclassification provenance")
        if role != "worklist":
            raise ScoreInputError("reclassification provenance is only valid for worklists")
        parent = lineage.get("input_snapshot_id")
        if not isinstance(parent, str) or not re.fullmatch(
            re.escape(worklist.WORKLIST_STEM) + r"-\d{4}-\d{2}-\d{2}", parent
        ):
            raise ScoreInputError("reclassification parent must be a worklist snapshot")
        try:
            if date.fromisoformat(parent[-10:]) >= date.fromisoformat(snapshot_id[-10:]):
                raise ValueError("parent must be older")
        except ValueError as exc:
            raise ScoreInputError("reclassification parent date must be valid and older") from exc
        policies = {"reclassification-v1": LEGACY_RECLASSIFICATION_POLICY,
                    "derivation-v2": CLASSIFIER_POLICY,
                    MIGRATION_PROFILE: MIGRATION_POLICY}
        if lineage.get("profile") not in policies or lineage.get("policy") != policies[lineage["profile"]]:
            raise ScoreInputError("unsupported native reclassification profile/policy")
        digest = lineage.get("input_json_sha256")
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ScoreInputError("reclassification parent SHA-256 is required")
        _timestamp(lineage.get("input_generated_at"))


def _worklist_lineage(manifest: dict, rows: tuple[dict[str, Any], ...]) -> dict | None:
    """Recognize the retained v1 summary and the current v2 native derivation.

    Keep only the lineage summary in score provenance; the complete change log
    remains bound by the companion manifest hash.
    """
    kinds = [key for key in ("reclassification", "derivation") if key in manifest]
    if not kinds:
        return None
    if len(kinds) != 1:
        raise ScoreInputError("ambiguous reclassification profile")
    snapshot, source = manifest["snapshot"], manifest["source"]
    parents = _mapping(snapshot.get("input_snapshot_ids"), "reclassification input snapshots")
    info = _mapping(manifest[kinds[0]], "reclassification metadata")
    if kinds[0] == "derivation" and info.get("method") == "exduf_migration":
        return _migration_lineage(manifest, rows, parents, info)
    if set(parents) != {"worklist"}:
        raise ScoreInputError("reclassification requires exactly one worklist parent")
    parent = parents["worklist"]
    if kinds[0] == "reclassification":
        if (source.get("name") != RECLASSIFIED_SOURCE or info.get("source_snapshot") != parent
                or type(info.get("rows")) is not int or info["rows"] != len(rows)
                or info.get("by_unknown_status") != dict(Counter(row["unknown_status"] for row in rows))):
            raise ScoreInputError("reclassification summary does not match worklist")
        changes = info.get("changes")
        indexed = {row["pfam_id"]: row for row in rows}
        seen = set()
        if not isinstance(changes, list):
            raise ScoreInputError("reclassification changes must be a list")
        for change in changes:
            change = _mapping(change, "reclassification change")
            pfam = change.get("pfam_id")
            if (not isinstance(pfam, str) or pfam not in indexed or pfam in seen
                    or change.get("after") != indexed[pfam]["unknown_status"]
                    or change.get("after_reasons") != indexed[pfam]["candidate_reasons"]
                    or not isinstance(change.get("before"), str)
                    or not isinstance(change.get("before_reasons"), list)
                    or any(not isinstance(reason, str) for reason in change["before_reasons"])):
                raise ScoreInputError("reclassification change does not match worklist")
            seen.add(pfam)
        if (type(info.get("changed_statuses")) is not int
                or info["changed_statuses"] != sum(c["before"] != c["after"] for c in changes)):
            raise ScoreInputError("reclassification changed-status count mismatch")
        lineage = {"profile": "reclassification-v1", "input_snapshot_id": parent,
                   "input_json_sha256": info.get("source_sha256"), "policy": info.get("policy"),
                   "input_generated_at": source.get("original_generated_at")}
    else:
        if (info.get("method") != "reclassify_saved_worklist" or info.get("fetched_live") is not False
                or info.get("changed_fields") != ["unknown_status", "candidate_reasons"]):
            raise ScoreInputError("unsupported native reclassification derivation")
        files = _mapping(info.get("input_files"), "reclassification input files")
        if set(files) != {"json", "tsv", "manifest"}:
            raise ScoreInputError("reclassification requires parent JSON, TSV and manifest provenance")
        for kind, suffix in (("json", "json"), ("tsv", "tsv"), ("manifest", "manifest.json")):
            entry = _mapping(files[kind], "reclassification parent file")
            if (entry.get("path") != f"{parent}.{suffix}"
                    or type(entry.get("bytes")) is not int or entry["bytes"] <= 0
                    or not isinstance(entry.get("sha256"), str)
                    or not re.fullmatch(r"[0-9a-f]{64}", entry["sha256"])):
                raise ScoreInputError("invalid reclassification parent file provenance")
        lineage = {"profile": "derivation-v2", "input_snapshot_id": parent,
                   "input_json_sha256": files["json"]["sha256"], "policy": info.get("classifier_policy"),
                   "input_generated_at": info.get("input_snapshot_generated_at")}
    if _timestamp(lineage["input_generated_at"]) > _timestamp(snapshot["generated_at"]):
        raise ScoreInputError("reclassification parent timestamp is later than its output")
    return lineage


def _migration_lineage(
    manifest: dict, rows: tuple[dict[str, Any], ...], parents: dict, info: dict,
) -> dict:
    """Validate an EX_DUF migration: parents, parent file hashes, and the change log.

    The set of EX_DUF rows must equal the rows logged as changed to EX_DUF plus the
    added, carried and retained EX_DUF families, and only EX_DUF rows may carry the
    migration reason. The full parent rows stay bound by the recorded hashes.
    """
    allowed = {"worklist", "pfam_previous_names", "live_worklist"}
    if not {"worklist", "pfam_previous_names"} <= set(parents) <= allowed:
        raise ScoreInputError("EX_DUF migration requires worklist and pfam_previous_names parents")
    if manifest["source"].get("name") != MIGRATED_SOURCE:
        raise ScoreInputError("EX_DUF migration lineage requires the migration source identity")
    if (info.get("profile") != MIGRATION_PROFILE or info.get("migration_policy") != MIGRATION_POLICY
            or info.get("changed_fields") != ["unknown_status", "candidate_reasons"]
            or not isinstance(info.get("fetched_live"), bool)):
        raise ScoreInputError("unsupported EX_DUF migration derivation")
    parent = parents["worklist"]
    checks = [("input_files", parent), ("previous_names_files", parents["pfam_previous_names"])]
    if "live_worklist" in parents:
        checks.append(("live_worklist_files", parents["live_worklist"]))
    elif "live_worklist_files" in info:
        raise ScoreInputError("live worklist files recorded without a live_worklist parent")
    for key, name in checks:
        files = _mapping(info.get(key), f"migration {key}")
        if not {"json", "manifest"} <= set(files):
            raise ScoreInputError(f"migration {key} requires JSON and manifest provenance")
        for kind, suffix in (("json", "json"), ("manifest", "manifest.json")):
            entry = _mapping(files[kind], "migration parent file")
            if (entry.get("path") != f"{name}.{suffix}"
                    or type(entry.get("bytes")) is not int or entry["bytes"] <= 0
                    or not isinstance(entry.get("sha256"), str)
                    or not re.fullmatch(r"[0-9a-f]{64}", entry["sha256"])):
                raise ScoreInputError("invalid EX_DUF migration parent file provenance")
    indexed = {row["pfam_id"]: row for row in rows}
    lists = {}
    for key in ("added_pfam_ids", "carried_pfam_ids", "retained_ex_duf_pfam_ids",
                "refreshed_pfam_ids", "live_new_pfam_ids", "not_found_in_interpro", "changes"):
        value = info.get(key)
        if not isinstance(value, list):
            raise ScoreInputError(f"EX_DUF migration {key} must be a list")
        lists[key] = value
    for key in ("added_pfam_ids", "carried_pfam_ids", "retained_ex_duf_pfam_ids",
                "refreshed_pfam_ids", "live_new_pfam_ids"):
        if any(not isinstance(pfam, str) or pfam not in indexed for pfam in lists[key]):
            raise ScoreInputError(f"EX_DUF migration {key} lists families absent from the worklist")
    fetched = bool(lists["added_pfam_ids"] or lists["carried_pfam_ids"]
                   or lists["not_found_in_interpro"])
    if fetched and not info["fetched_live"]:
        raise ScoreInputError("EX_DUF migration fetched families but reports no live fetch")
    changed_to_ex = set()
    seen = set()
    for change in lists["changes"]:
        change = _mapping(change, "migration change")
        pfam = change.get("pfam_id")
        if (pfam not in indexed or pfam in seen
                or not isinstance(change.get("before"), str)
                or not isinstance(change.get("before_reasons"), list)
                or change.get("after") != indexed[pfam]["unknown_status"]
                or change.get("after_reasons") != indexed[pfam]["candidate_reasons"]):
            raise ScoreInputError("EX_DUF migration change does not match worklist")
        seen.add(pfam)
        if change["after"] == EX_DUF:
            changed_to_ex.add(pfam)
    ex_rows = set()
    for row in rows:
        migrated = PREVIOUS_UNKNOWN_NAME_REASON in row["candidate_reasons"]
        if migrated != (row["unknown_status"] == EX_DUF):
            raise ScoreInputError(f"{row['pfam_id']}: EX_DUF status and migration reason disagree")
        if migrated:
            ex_rows.add(row["pfam_id"])
    accounted = (changed_to_ex | set(lists["added_pfam_ids"]) | set(lists["carried_pfam_ids"])
                 | set(lists["retained_ex_duf_pfam_ids"]))
    if ex_rows != accounted:
        raise ScoreInputError("EX_DUF rows are not all accounted for by the migration log")
    transitions = Counter(
        f"{change['before']} -> {change['after']}"
        for change in lists["changes"] if change["before"] != change["after"]
    )
    if dict(sorted(transitions.items())) != info.get("status_transitions"):
        raise ScoreInputError("EX_DUF migration status transitions do not match its changes")
    lineage = {"profile": MIGRATION_PROFILE, "input_snapshot_id": parent,
               "input_json_sha256": info["input_files"]["json"]["sha256"],
               "policy": info.get("migration_policy"),
               "input_generated_at": info.get("input_snapshot_generated_at"),
               "refresh": "live_worklist" in parents}
    if _timestamp(lineage["input_generated_at"]) > _timestamp(manifest["snapshot"]["generated_at"]):
        raise ScoreInputError("EX_DUF migration parent timestamp is later than its output")
    return lineage


def _rows(raw: bytes, path: Path, role: str, *, frozen: bool) -> tuple[dict[str, Any], ...]:
    payload = _json(raw, path)
    if not isinstance(payload, list) or any(not isinstance(row, dict) for row in payload):
        raise ScoreInputError(f"{path}: every data input must be a JSON list of objects")
    spec = INPUT_SPECS[role]
    seen = set()
    for number, row in enumerate(payload, 1):
        if frozen and set(row) != set(spec.fields) | set(spec.json_only_fields):
            raise ScoreInputError(f"{path}: row {number} fields do not match the {role} header")
        if any(not isinstance(row.get(key), str) or not row[key].strip() for key in spec.identity):
            raise ScoreInputError(f"{path}: row {number} requires {role} identity fields {spec.identity}")
        if "pfam_id" in spec.identity and not re.fullmatch(r"PF\d{5}", row["pfam_id"]):
            raise ScoreInputError(f"{path}: row {number} has an invalid Pfam identity")
        identity = tuple(row[key] for key in spec.identity)
        # Evidence can repeat a subject/term with different references, providers,
        # coordinates, or qualifiers. Reject only identical full annotations.
        if role not in {"worklist", "members"}:
            identity += (json.dumps(row, sort_keys=True, separators=(",", ":")),)
        if identity in seen:
            raise ScoreInputError(f"{path}: duplicate {role} identity at row {number}")
        seen.add(identity)
    return tuple(payload)


def _file_entry(entry: Any, filename: str, raw: bytes) -> None:
    entry = _mapping(entry, f"file entry for {filename}")
    if entry.get("path") != filename:
        raise ScoreInputError(f"manifest path must be the matching filename {filename}")
    if type(entry.get("bytes")) is not int or entry["bytes"] != len(raw):
        raise ScoreInputError(f"manifest byte size mismatch for {filename}")
    if entry.get("sha256") != _digest(raw):
        raise ScoreInputError(f"manifest SHA-256 mismatch for {filename}")


def load_score_input(
    path: Path, role: str, *, allow_ad_hoc: bool = False, payload_bytes: bytes | None = None,
) -> ScoreInput:
    """Load a verified snapshot, or explicitly allow a JSON file lacking a manifest.

    Existing bad manifests are always errors. ``payload_bytes`` lets a caller
    validate the same immutable buffer it used elsewhere instead of reopening it.
    """
    if role not in INPUT_SPECS:
        raise ScoreInputError(f"unsupported scoring input role: {role}")
    if path.suffix != ".json" or path.name.endswith(".manifest.json"):
        raise ScoreInputError("scoring input must be a JSON data file")
    if path.is_symlink():
        raise ScoreInputError(f"input must not be a symlink: {path}")
    raw = _read_bytes(path) if payload_bytes is None else payload_bytes
    if not isinstance(raw, bytes):
        raise TypeError("payload_bytes must be an immutable byte buffer")
    manifest_path = path.with_suffix(".manifest.json")
    try:
        manifest_raw = _read_bytes(manifest_path)
    except FileNotFoundError:
        if not allow_ad_hoc:
            raise ScoreInputError(
                f"missing companion manifest {manifest_path}; use --allow-ad-hoc-inputs explicitly"
            ) from None
        rows = _rows(raw, path, role, frozen=False)
        return ScoreInput(rows, {
            "role": role, "path": path.name, "snapshot_id": path.stem,
            "bytes": len(raw), "sha256": _digest(raw), "rows": len(rows),
            "manifest_path": None, "manifest_bytes": None, "manifest_sha256": None,
            "source": {"name": "ad hoc JSON", "declared_role": role},
            "tsv_fieldnames": None, "validation_state": "ad_hoc",
        })
    manifest = _mapping(_json(manifest_raw, manifest_path), "manifest")
    snapshot = _mapping(manifest.get("snapshot"), "manifest.snapshot")
    if snapshot.get("id") != path.stem or snapshot.get("date") != path.stem[-10:]:
        raise ScoreInputError("manifest snapshot identity/date does not match input filename")
    try:
        generated = datetime.fromisoformat(str(snapshot.get("generated_at", "")).replace("Z", "+00:00"))
        if generated.tzinfo is None:
            raise ValueError("missing timezone")
    except ValueError as exc:
        raise ScoreInputError("manifest generated_at must include a timezone") from exc
    source = _mapping(manifest.get("source"), "manifest.source")
    fields = _mapping(manifest.get("schema"), "manifest.schema").get("tsv_fieldnames")
    files = _mapping(manifest.get("files"), "manifest.files")
    if set(files) != {"json", "tsv"}:
        raise ScoreInputError("frozen scoring inputs require JSON and TSV companion file entries")
    _file_entry(files["json"], path.name, raw)
    tsv_path = path.with_suffix(".tsv")
    tsv_raw = _read_bytes(tsv_path)
    _file_entry(files["tsv"], tsv_path.name, tsv_raw)
    rows = _rows(raw, path, role, frozen=True)
    if role == "cath" and any(row["cath_version"] != source["cath_version"] for row in rows):
        raise ScoreInputError("CATH row version does not match manifest source version")
    total = _mapping(manifest.get("rows"), "manifest.rows").get("total")
    if type(total) is not int or total != len(rows):
        raise ScoreInputError("JSON row count does not match manifest rows.total")
    lineage = _worklist_lineage(manifest, rows) if role == "worklist" else None
    _source_identity(role, path.stem, source, fields, lineage)
    try:
        reader = csv.reader(io.StringIO(tsv_raw.decode("utf-8"), newline=""), delimiter="\t", strict=True)
        if next(reader, None) != fields:
            raise ScoreInputError("TSV header does not match manifest/source role")
        count = 0
        for tsv_row in reader:
            if len(tsv_row) != len(fields):
                raise ScoreInputError("TSV row width does not match source header")
            count += 1
        if count != total:
            raise ScoreInputError("TSV row count does not match manifest rows.total")
    except (csv.Error, UnicodeError) as exc:
        raise ScoreInputError(f"invalid TSV companion: {tsv_path}") from exc
    return ScoreInput(rows, {
        "role": role, "path": path.name, "snapshot_id": path.stem,
        "bytes": len(raw), "sha256": _digest(raw), "rows": len(rows),
        "manifest_path": manifest_path.name, "manifest_bytes": len(manifest_raw),
        "manifest_sha256": _digest(manifest_raw), "source": source,
        "tsv_fieldnames": fields, "validation_state": "verified",
        **({"worklist_reclassification": lineage} if lineage is not None else {}),
    })


def score_input_validation(
    input_snapshot_ids: Mapping[str, str], input_provenance: Mapping[str, Any],
) -> str:
    """Validate supplied provenance structure and return its honest aggregate state."""
    if not input_provenance:
        return "unverified"
    if "worklist" not in input_provenance or set(input_snapshot_ids) != set(input_provenance):
        raise ScoreInputError("input provenance roles must exactly match input_snapshot_ids, including worklist")
    states = []
    for role, value in input_provenance.items():
        if role not in INPUT_SPECS:
            raise ScoreInputError(f"unsupported input provenance role: {role}")
        item = _mapping(value, f"input_provenance.{role}")
        if item.get("role") != role or item.get("snapshot_id") != input_snapshot_ids[role]:
            raise ScoreInputError("input provenance source role/snapshot identity mismatch")
        if (not isinstance(item.get("path"), str) or Path(item["path"]).name != item["path"]
                or item["path"] != f"{item['snapshot_id']}.json"):
            raise ScoreInputError("input provenance path must match its snapshot filename")
        for key in ("bytes", "rows"):
            if type(item.get(key)) is not int or item[key] < 0:
                raise ScoreInputError(f"input provenance {key} must be a nonnegative integer")
        if not isinstance(item.get("sha256"), str) or not re.fullmatch(r"[0-9a-f]{64}", item["sha256"]):
            raise ScoreInputError("input provenance SHA-256 is required")
        state = item.get("validation_state")
        if state == "verified":
            _source_identity(role, item["snapshot_id"], _mapping(item.get("source"), "source"),
                             item.get("tsv_fieldnames"), item.get("worklist_reclassification"))
            if (item.get("manifest_path") != f"{item['snapshot_id']}.manifest.json"
                    or type(item.get("manifest_bytes")) is not int or item["manifest_bytes"] <= 0
                    or not isinstance(item.get("manifest_sha256"), str)
                    or not re.fullmatch(r"[0-9a-f]{64}", item["manifest_sha256"])):
                raise ScoreInputError("verified input requires companion manifest provenance")
        elif state == "ad_hoc":
            if any(item.get(key) is not None for key in ("manifest_path", "manifest_bytes", "manifest_sha256")):
                raise ScoreInputError("ad hoc input must not declare a companion manifest")
        else:
            raise ScoreInputError("unsupported input validation state")
        states.append(state)
    return "verified" if all(state == "verified" for state in states) else "ad_hoc"


def require_verified_score_worklist(
    score_manifest: Mapping[str, Any], worklist_path: Path, *, worklist_bytes: bytes | None = None,
) -> dict[str, Any]:
    """Publication gate: all score inputs verified, and this exact worklist captured.

    Historical reports may still read legacy scores. Curated family publication
    must call this gate before using scores; a filename stem alone is insufficient.
    """
    snapshot = _mapping(score_manifest.get("snapshot"), "score snapshot")
    ids = _mapping(snapshot.get("input_snapshot_ids"), "score input_snapshot_ids")
    provenance = _mapping(score_manifest.get("input_provenance"), "score input_provenance")
    if (score_manifest.get("input_provenance_version") != 1
            or score_manifest.get("input_validation") != "verified"
            or score_input_validation(ids, provenance) != "verified"):
        raise ScoreInputError("curated publication requires verified score inputs; legacy/ad hoc scores are not eligible")
    actual = load_score_input(worklist_path, "worklist", payload_bytes=worklist_bytes).provenance
    if provenance["worklist"] != actual:
        raise ScoreInputError("score input worklist provenance differs from the exact verified worklist bytes/manifest")
    return actual
