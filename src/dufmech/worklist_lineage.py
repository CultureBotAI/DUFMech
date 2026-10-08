"""Compare derived worklists with locally available, hash-bound parent rows."""

from __future__ import annotations

import hashlib
import json
import os
import re
import stat
from collections import Counter
from collections.abc import Mapping, Sequence
from datetime import date
from pathlib import Path
from typing import Any

CLASSIFICATION_FIELDS = {"unknown_status", "candidate_reasons"}


def _index(rows: object) -> dict[str, dict[str, Any]]:
    if not isinstance(rows, (list, tuple)):
        raise ValueError("worklist parent comparison requires a list of rows")  # noqa: TRY004
    result = {}
    for row in rows:
        if not isinstance(row, dict) or not re.fullmatch(r"PF[0-9]{5}", str(row.get("pfam_id"))):
            raise ValueError("worklist parent comparison requires valid Pfam IDs")
        pfam = row["pfam_id"]
        if pfam in result or not CLASSIFICATION_FIELDS <= row.keys():
            raise ValueError("worklist parent comparison found duplicate or incomplete rows")
        result[pfam] = row
    return result


def _parent(
    directory: Path, snapshot_id: object, files: object,
) -> dict[str, dict[str, Any]] | None:
    if not isinstance(snapshot_id, str) or not re.fullmatch(
        r"interpro-pfam-duf-[0-9]{4}-[0-9]{2}-[0-9]{2}", snapshot_id
    ):
        raise ValueError("invalid worklist parent snapshot ID")
    date.fromisoformat(snapshot_id[-10:])
    entry = files.get("json") if isinstance(files, Mapping) else None
    if (not isinstance(entry, Mapping) or entry.get("path") != f"{snapshot_id}.json"
            or type(entry.get("bytes")) is not int or entry["bytes"] <= 0
            or not re.fullmatch(r"[0-9a-f]{64}", str(entry.get("sha256")))):
        raise ValueError("invalid worklist parent JSON provenance")
    path = directory / entry["path"]
    try:
        # Do not follow symlinks or block on a FIFO masquerading as a parent.
        fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
        with os.fdopen(fd, "rb") as handle:
            if not stat.S_ISREG(os.fstat(handle.fileno()).st_mode):
                raise ValueError(f"{path.name}: worklist parent must be a regular file")
            raw = handle.read()
    except FileNotFoundError:
        return None  # Portable snapshot sets need not bundle their ancestors.
    except OSError as exc:
        raise ValueError(f"{path.name}: could not read worklist parent: {exc}") from exc
    if len(raw) != entry["bytes"] or hashlib.sha256(raw).hexdigest() != entry["sha256"]:
        raise ValueError(f"{path.name}: content differs from recorded parent hash or byte size")
    return _index(json.loads(raw))


def _metadata(row: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in row.items() if key not in CLASSIFICATION_FIELDS}


def _same_metadata(child: Mapping, parent: Mapping, pfams: set[str]) -> None:
    for pfam in sorted(pfams):
        if _metadata(child[pfam]) != _metadata(parent[pfam]):
            raise ValueError(f"{pfam}: derived metadata differs from its recorded parent")


def _ids(info: Mapping, key: str, child: Mapping) -> set[str]:
    values = info.get(key)
    if (not isinstance(values, list) or any(not isinstance(p, str) for p in values)
            or len(values) != len(set(values)) or not set(values) <= child.keys()):
        raise ValueError(f"migration {key} must name unique families in the derived worklist")
    return set(values)


def verify_worklist_parent_rows(
    manifest_path: Path, manifest: Mapping[str, Any], rows: Sequence[Mapping[str, Any]],
) -> None:
    """Verify direct parents when present, without recursively requiring ancestors.

    Hash and comparison use the same captured parent bytes. This supplements the
    child's own manifest validation; it does not replay scientific classification.
    """
    info = manifest.get("derivation")
    snapshot = manifest.get("snapshot", {})
    if (not isinstance(snapshot, Mapping)
            or not str(snapshot.get("id", "")).startswith("interpro-pfam-duf-")
            or not isinstance(info, Mapping)):
        return
    method = info.get("method")
    if not isinstance(method, str):
        raise ValueError("worklist derivation method must be a string")  # noqa: TRY004
    if method not in {"reclassify_saved_worklist", "exduf_migration"}:
        return
    inputs = snapshot.get("input_snapshot_ids", {})
    if not isinstance(inputs, Mapping):
        raise ValueError("worklist parent snapshot IDs must be an object")  # noqa: TRY004
    parent = _parent(manifest_path.parent, inputs.get("worklist"), info.get("input_files"))
    child = _index(rows)
    if info["method"] == "reclassify_saved_worklist":
        if parent is None:
            return
        if child.keys() != parent.keys():
            raise ValueError("reclassification membership differs from its recorded parent")
        _same_metadata(child, parent, set(parent))
        transitions = Counter(
            f"{parent[p]['unknown_status']} -> {row['unknown_status']}"
            for p, row in child.items() if row["unknown_status"] != parent[p]["unknown_status"]
        )
        reasons = sum(row["candidate_reasons"] != parent[p]["candidate_reasons"]
                      for p, row in child.items())
        if (info.get("status_transitions") != dict(transitions)
                or info.get("changed_status_rows") != sum(transitions.values())
                or info.get("changed_reason_rows") != reasons):
            raise ValueError("reclassification change summary differs from its recorded parent")
        return

    added = _ids(info, "added_pfam_ids", child)
    carried = _ids(info, "carried_pfam_ids", child)
    refreshed = _ids(info, "refreshed_pfam_ids", child)
    live_new = _ids(info, "live_new_pfam_ids", child)
    live = None
    if "live_worklist" in inputs:
        live = _parent(manifest_path.parent, inputs["live_worklist"], info.get("live_worklist_files"))
    elif carried or refreshed or live_new:
        raise ValueError("migration refresh bookkeeping requires a live worklist parent")
    if added & (carried | refreshed | live_new) or carried & (refreshed | live_new):
        raise ValueError("migration membership lists overlap")
    if live is not None:
        if not live.keys() <= child.keys() or (added | carried) & live.keys():
            raise ValueError("migration membership differs from its live worklist parent")
        _same_metadata(child, live, set(live))
    if parent is None:
        return
    if (not parent.keys() <= child.keys() or (added | live_new) & parent.keys()
            or not (carried | refreshed) <= parent.keys()
            or child.keys() - parent.keys() != added | live_new):
        raise ValueError("migration membership differs from its recorded parent")
    if live is not None:
        expected_refresh = {p for p in parent.keys() & live.keys()
                            if _metadata(parent[p]) != _metadata(live[p])}
        if (carried != parent.keys() - live.keys() or live_new != live.keys() - parent.keys()
                or refreshed != expected_refresh):
            raise ValueError("migration refresh bookkeeping differs from its recorded parents")
    _same_metadata(child, parent, parent.keys() - carried - refreshed)
    # Fetched additions and carried rows are not in the producer's change log.
    changes = []
    for pfam in sorted(child.keys() - added - carried):
        old = parent.get(pfam, {"unknown_status": "ABSENT", "candidate_reasons": []})
        row = child[pfam]
        if any(old[key] != row[key] for key in CLASSIFICATION_FIELDS):
            changes.append({"pfam_id": pfam, "before": old["unknown_status"],
                            "before_reasons": old["candidate_reasons"],
                            "after": row["unknown_status"],
                            "after_reasons": row["candidate_reasons"]})
    if info.get("changes") != changes:
        raise ValueError("migration change log differs from its recorded parent")
