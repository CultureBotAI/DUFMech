"""Translate the shared review contract to DUFMech's retained metadata API."""

from __future__ import annotations

import importlib.util
from copy import deepcopy
from functools import lru_cache
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = "CultureBotAI/DUFMech"
DIGEST_ALGORITHM = "dufmech-record-content-v1"
PROJECTION_BINDING = "dufmech-reviewed-projection-v1"
MAX_PROJECTION_BYTES = 32 * 1024 * 1024
NATIVE_VERDICTS = {
    "PASS": {"pass"},
    "SEED_ONLY": {"seed_only"},
    "NEEDS_FOLLOWUP": {"needs_curation", "pass_with_limitations", "not_assessed"},
    "BLOCKED": {"blocked", "not_assessed"},
    "FAIL": {"needs_curation"},
}


@lru_cache(maxsize=1)
def common():
    """Load the byte-identical shared payload from this installed checkout."""
    spec = importlib.util.spec_from_file_location(
        "dufmech_shared_record_review", ROOT / "scripts/record_review.py",
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def inspected_fields(context: dict) -> dict:
    """Expose source/target fields without inventing any assessment or verdict."""
    targets = []
    for target in context["targets"]:
        pfam = target["id"]
        path, _, selector = target["locator"].partition("#")
        item: dict[str, Any] = {
            "target_id": pfam, "path": path, "label": pfam,
            "kind": "source" if context["kind"] == "repo" else (
                "snapshot_row" if selector else "generated"
            ),
        }
        if selector:
            item["selector"] = selector
        if context["kind"] == "repo":
            item["ownership_note"] = (
                "Inspect the selected source's ownership before proposing an edit."
            )
        else:
            item["record_class"] = "FamilyRecord" if not selector else "DufFamilyRow"
            item["owner_paths"] = [
                {"repository": REPOSITORY, "path": f"curation/families/{pfam}.yaml",
                 "role": "Maintained scientific overlay; create only with authorized curation."},
                {"repository": REPOSITORY, "path": "src/dufmech/records.py",
                 "role": "Projection generator; frozen snapshot identity is not hand-edited."},
            ]
        if pfam in context["record_digests"]:
            item["semantic_digest"] = {
                "algorithm": DIGEST_ALGORITHM,
                "sha256": context["record_digests"][pfam],
                "description": (
                    "Canonical JSON SHA-256 of effective FamilyRecord excluding only "
                    "curation_status, review_id and curation_events."
                ),
            }
        targets.append(item)
    target_paths = {item["path"] for item in targets}
    return {
        "repository": REPOSITORY,
        "kind": "repository" if context["kind"] == "repo" else context["kind"],
        "source": {
            "git_revision": context["source_revision"], "state": context["source_state"],
            "snapshot_id": context["snapshot_id"],
            "inputs": [{"path": path, "sha256": sha,
                        "role": "target" if path in target_paths else "context"}
                       for path, sha in context["source_files"].items()],
        },
        "targets": targets,
    }


def _reviewed_projection(root: Path, review: dict, path: str) -> bytes:
    """Recover the inspected bytes, never substitute a merely current semantic digest."""
    from dufmech.reviews import read_source_bytes

    shared = common()
    expected = next(item["sha256"] for item in review["source"]["inputs"]
                    if item["path"] == path)
    retained = [item for item in review["evidence"]
                if item.get("locator") == PROJECTION_BINDING and item["reference"] == path]
    if retained:
        if len(retained) != 1:
            raise ValueError(f"ambiguous retained projection binding: {path}")
        item = retained[0]
        raw = item.get("quote", "").encode("utf-8")
        if (item["kind"] != "record_content" or item.get("snapshot_sha256") != expected
                or len(raw) > MAX_PROJECTION_BYTES or shared.content_sha256(raw) != expected):
            raise ValueError(f"retained projection bytes disagree with reviewed input: {path}")
        return raw
    try:
        raw = read_source_bytes(root, path, max_bytes=MAX_PROJECTION_BYTES)
    except FileNotFoundError:
        raw = None
    if raw is not None and shared.content_sha256(raw) == expected:
        return raw
    # Committed reviews can remain verifiable after the projection is regenerated.
    revision = review["source"]["git_revision"]
    try:
        mode = shared._git(root, "ls-tree", "--format=%(objectmode)", revision, "--", path)
        if mode.strip() in {b"100644", b"100755"}:
            object_name = f"{revision}:{path}"
            size = int(shared._git(root, "cat-file", "-s", object_name).strip())
            if size <= MAX_PROJECTION_BYTES:
                raw = shared._git(root, "cat-file", "blob", object_name)
                if shared.content_sha256(raw) == expected:
                    return raw
    except (OSError, ValueError):
        pass
    raise ValueError(f"cannot verify reviewed projection bytes: {path}")


def metadata(root: Path, review: dict, *, projection_bytes: dict | None = None) -> dict:
    """Project a validated observation with source-bound native semantic digests."""
    from dufmech.reviews import PFAM, actual_text, read_yaml, record_content_digest, token

    shared = common()
    shared.validate_review(review)
    if review["repository"].lower() != REPOSITORY.lower():
        raise ValueError("structured review belongs to another repository")
    native = review.get("native_verdict")
    if native is not None and (
        native not in NATIVE_VERDICTS or review["verdict"] not in NATIVE_VERDICTS[native]
    ):
        raise ValueError("native verdict disagrees with the common verdict")
    for label, value in (
        ("summary", review["summary"]), ("reviewer", review["reviewer"]["identity"]),
        ("review_scope", review["scope"]["description"]),
    ):
        actual_text(value, label)
    for assessment in review["assessments"]:
        actual_text(assessment["summary"], "assessment summary")
        if "details" in assessment:
            actual_text(assessment["details"], "assessment details")
    kind = "repo" if review["kind"] == "repository" else review["kind"]
    snapshot_id = review["source"].get("snapshot_id", "")
    if snapshot_id:
        token(snapshot_id, "snapshot_id")
    members, targets, digests = [], [], {}
    for item in review["targets"]:
        identity, path = item["target_id"], item["path"]
        selector = item.get("selector")
        if kind != "repo":
            if not PFAM.fullmatch(identity):
                raise ValueError("DUF record/category/batch targets require exact Pfam IDs")
            members.append(identity)
            if item["kind"] == "generated":
                if path != f"data/families/{identity}.yaml" or selector:
                    raise ValueError("generated review target must be the exact family projection")
                digest = item.get("semantic_digest", {})
                if digest:
                    if digest["algorithm"] != DIGEST_ALGORITHM:
                        raise ValueError("unknown native record semantic digest algorithm")
                    raw = _reviewed_projection(root, review, path)
                    projection = read_yaml(raw.decode("utf-8"))
                    if (not isinstance(projection, dict) or projection.get("pfam_id") != identity
                            or projection.get("id") != f"Pfam:{identity}"
                            or record_content_digest(projection) != digest["sha256"]):
                        raise ValueError("review target or semantic digest differs from reviewed projection")
                    if projection_bytes is not None:
                        projection_bytes[path] = raw
                    # A generic review without frozen-source provenance cannot qualify REVIEWED.
                    if snapshot_id:
                        digests[identity] = digest["sha256"]
            elif item["kind"] == "snapshot_row":
                if (not snapshot_id or path != f"data/worklists/{snapshot_id}.json"
                        or selector != f"pfam_id={identity}"):
                    raise ValueError("snapshot row requires its exact frozen Pfam selector")
                if item.get("semantic_digest"):
                    raise ValueError("snapshot rows cannot claim a projection semantic digest")
            elif path != f"curation/families/{identity}.yaml" or selector:
                raise ValueError("maintained family review target must identify its overlay")
        targets.append({"id": identity, "locator": path + (f"#{selector}" if selector else "")})
    scope = review["scope"]
    return {
        "review_version": 2, "status": "saved",
        "started_utc": review["started_at"], "finished_utc": review["finished_at"],
        "verdict": native or review["verdict"],
        "native_verdict": native, "common_verdict": review["verdict"],
        "completion": review["completion"], "coverage": scope["coverage"],
        "reviewer": review["reviewer"]["identity"],
        "scientific_review": review["scientific_review"],
        "review_scope": scope["description"],
        "context": {
            "kind": kind, "slug": members[0] if kind == "record" else review["review_id"],
            "source_revision": review["source"]["git_revision"],
            "source_state": review["source"]["state"], "snapshot_id": snapshot_id,
            "source_files": {item["path"]: item["sha256"] for item in review["source"]["inputs"]},
            "targets": targets, "members": sorted(members),
            "selection": scope["selection"] if kind in {"category", "batch"} else "",
            "scope_paths": sorted(item["path"] for item in review["targets"]) if kind == "repo" else [],
            "record_digests": digests,
        },
    }


def save(root: Path, review: dict) -> Path:
    """Recheck native snapshot/projection context, then use the common atomic saver."""
    from dufmech.reviews import inspect_review

    if not isinstance(review, dict) or "schema_version" not in review:
        raise ValueError("new saves require the structured contract in docs/record-reviews.md")
    projection_bytes: dict[str, bytes] = {}
    native = metadata(root, review, projection_bytes=projection_bytes)
    context = native["context"]
    if not context["snapshot_id"] or context["source_state"] != "working_tree":
        raise ValueError("native saves require an inspected working-tree snapshot")
    kind = "category" if context["kind"] == "batch" else context["kind"]
    current = inspect_review(
        root, kind, context["slug"], members=context["members"],
        selection=context["selection"], snapshot_id=context["snapshot_id"],
        scope_paths=context["scope_paths"],
    )["structured"]
    # Additional hashed evidence/rubric inputs are allowed; none of the native inputs
    # or digest bindings may disappear when the reviewer constructs the common record.
    supplied = {item["path"]: item["sha256"] for item in review["source"]["inputs"]}
    if (current["source"]["git_revision"] != review["source"]["git_revision"]
            or any(supplied.get(item["path"]) != item["sha256"]
                   for item in current["source"]["inputs"])):
        raise ValueError("review input context changed; inspect again and reassess before saving")
    def binding(item):
        return (item["target_id"], item["path"], item.get("selector"), item["kind"],
                item.get("semantic_digest", {}).get("algorithm"),
                item.get("semantic_digest", {}).get("sha256"))
    if sorted(map(binding, current["targets"])) != sorted(map(binding, review["targets"])):
        raise ValueError("review target or semantic digest differs from native inspection")
    # Retain byte-exact source evidence inside the atomic pair. Bookkeeping can
    # change the projection file hash after promotion, but not this checked binding.
    retained = deepcopy(review)
    evidence_ids = {item["evidence_id"] for item in retained["evidence"]}
    for path, raw in projection_bytes.items():
        if any(item.get("locator") == PROJECTION_BINDING and item["reference"] == path
               for item in retained["evidence"]):
            continue
        stem = f"duf-projection-{Path(path).stem.lower()}"
        evidence_id = stem
        suffix = 1
        while evidence_id in evidence_ids:
            evidence_id = f"{stem}-{suffix}"
            suffix += 1
        evidence_ids.add(evidence_id)
        retained["evidence"].append({
            "evidence_id": evidence_id, "kind": "record_content", "reference": path,
            "locator": PROJECTION_BINDING,
            # This retains the source attested by the finished review; saving
            # is not a new scientific evidence-access event.
            "accessed_at": review["finished_at"],
            "support": "context_only", "snapshot_sha256": common().content_sha256(raw),
            "quote": raw.decode("utf-8"),
            "summary": "Byte-exact projection retained at save for digest verification, not scientific assessment.",
        })
    return common().save_review(root, retained)
