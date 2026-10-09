"""Translate the shared review contract to DUFMech's retained metadata API."""

from __future__ import annotations

import importlib.util
from functools import lru_cache
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = "CultureBotAI/DUFMech"
DIGEST_ALGORITHM = "dufmech-record-content-v1"
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


def metadata(review: dict) -> dict:
    """Project a validated common observation; never assert current source freshness."""
    from dufmech.reviews import PFAM, actual_text, token

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
    native = metadata(review)
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
    return common().save_review(root, review)
