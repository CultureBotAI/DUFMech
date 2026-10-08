"""Migrate families Pfam renamed away from DUF/UPF names into the EX_DUF seed category.

The migration derives a new worklist snapshot from:

- the latest verified worklist (the parent),
- a Pfam previous-identifier snapshot (``pfam-previous-unknown-names-*``), and
- optionally a fresh live worklist from the InterPro DUF search (a refresh).

Rules, applied in order:

1. A family in the base worklist whose Pfam previous identifiers include a DUF/UPF
   name, and whose current short name is no longer one, becomes EX_DUF.
2. A family already EX_DUF stays EX_DUF; text reclassification never undoes it.
3. With a live refresh, a parent family missing from the new search is carried
   forward as EX_DUF when Pfam renamed it (or it was already EX_DUF), with metadata
   re-fetched from the InterPro entry API. Any other missing family stops the
   migration and is named: families are never dropped silently.
4. Renamed families outside the worklist are added as EX_DUF with metadata fetched
   from the InterPro entry API.

Seed status is metadata classification. A former DUF name records Pfam naming
history; it is not experimental evidence of function.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from collections import Counter
from collections.abc import Callable, Iterable, Mapping, Sequence
from dataclasses import dataclass, field, fields
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import httpx

from dufmech.provenance import check_manifest
from dufmech.report import ReportError
from dufmech.snapshot import WORKLIST_STEM, build_worklist_manifest, write_snapshot_artifacts
from dufmech.worklist import (
    CLASSIFIER_POLICY,
    EX_DUF,
    INTERPRO_PFAM_URL,
    MIGRATED_SOURCE,
    MIGRATION_NOTE,
    MIGRATION_POLICY,
    MIGRATION_PROFILE,
    PFAM_RE,
    STATUS_ORDER,
    DufFamilyRow,
    entry_from_interpro_detail,
    mark_ex_duf,
    render_json,
    render_tsv,
    row_from_interpro_entry,
)

MIGRATION_METHOD = "exduf_migration"
PREVIOUS_NAMES_STEM = "pfam-previous-unknown-names"


class MigrationError(RuntimeError):
    """Raised when inputs are inconsistent or a family would be dropped silently."""


@dataclass
class MigrationPlan:
    """The migrated rows and an auditable account of every change."""

    rows: list[DufFamilyRow]
    reclassified: list[dict[str, Any]] = field(default_factory=list)
    added: list[str] = field(default_factory=list)
    carried: list[str] = field(default_factory=list)
    not_found: list[str] = field(default_factory=list)
    # Families a dry run would fetch from InterPro (only set when ``fetch`` is None).
    to_fetch: list[str] = field(default_factory=list)


Fetcher = Callable[[Sequence[str]], Mapping[str, Mapping[str, Any] | None]]


def plan_migration(
    parent_rows: Sequence[DufFamilyRow],
    previous_names: Iterable[Mapping[str, Any]],
    *,
    fetch: Fetcher | None,
    live_rows: Sequence[DufFamilyRow] | None = None,
) -> MigrationPlan:
    """Apply the EX_DUF rules; ``fetch`` returns InterPro entry payloads by Pfam ID.

    With ``fetch=None`` (a dry run) nothing is fetched; ``to_fetch`` lists the
    families that would be added or carried.
    """

    renamed = {
        row["pfam_id"]
        for row in previous_names
        if row.get("previous_unknown_names") and not row.get("currently_unknown_name")
    }
    base = list(live_rows) if live_rows is not None else list(parent_rows)
    by_id = {row.pfam_id: row for row in base}
    if len(by_id) != len(base):
        raise MigrationError("worklist rows repeat a Pfam ID")
    parent_status = {row.pfam_id: row for row in parent_rows}

    carry: list[str] = []
    if live_rows is not None:
        dropped = [row for row in parent_rows if row.pfam_id not in by_id]
        unexplained = [
            row.pfam_id for row in dropped
            if row.pfam_id not in renamed and row.unknown_status != EX_DUF
        ]
        if unexplained:
            raise MigrationError(
                "families left the DUF search without Pfam rename evidence; review before "
                f"migrating: {', '.join(sorted(unexplained))}"
            )
        carry = sorted(row.pfam_id for row in dropped)

    plan = MigrationPlan(rows=[])
    for pfam_id, row in sorted(by_id.items()):
        was_ex = parent_status.get(pfam_id) is not None and parent_status[pfam_id].unknown_status == EX_DUF
        if pfam_id in renamed or was_ex or row.unknown_status == EX_DUF:
            migrated = mark_ex_duf(row)
            if migrated != row:
                plan.reclassified.append({
                    "pfam_id": pfam_id,
                    "before": row.unknown_status,
                    "after": migrated.unknown_status,
                    "before_reasons": list(row.candidate_reasons),
                    "after_reasons": list(migrated.candidate_reasons),
                })
            row = migrated
        plan.rows.append(row)

    wanted = sorted({*carry, *(renamed - by_id.keys())})
    if fetch is None:
        plan.to_fetch = wanted
        return plan
    payloads = fetch(wanted) if wanted else {}
    for pfam_id in wanted:
        payload = payloads.get(pfam_id)
        row = row_from_interpro_entry(entry_from_interpro_detail(payload)) if payload else None
        if row is None or row.pfam_id != pfam_id:
            plan.not_found.append(pfam_id)
            continue
        plan.rows.append(mark_ex_duf(row))
        (plan.carried if pfam_id in carry else plan.added).append(pfam_id)
    if any(pfam_id in carry for pfam_id in plan.not_found):
        missing = sorted(set(carry) & set(plan.not_found))
        raise MigrationError(f"carried families missing from InterPro: {', '.join(missing)}")
    return plan


class InterProEntryClient:
    """Fetch single Pfam entries from the InterPro API, anonymously, with retries."""

    def __init__(
        self,
        *,
        timeout: float = 60.0,
        transport: httpx.BaseTransport | None = None,
        retries: int = 5,
        backoff: float = 2.0,
        sleep: Callable[[float], None] = time.sleep,
        progress: Callable[[int, int], None] | None = None,
    ) -> None:
        self.timeout = timeout
        self.transport = transport
        self.retries = retries
        self.backoff = backoff
        self.sleep = sleep
        self.progress = progress

    def __call__(self, pfam_ids: Sequence[str]) -> dict[str, Mapping[str, Any] | None]:
        found: dict[str, Mapping[str, Any] | None] = {}
        with httpx.Client(
            timeout=self.timeout, follow_redirects=True, transport=self.transport
        ) as client:
            for index, pfam_id in enumerate(pfam_ids, start=1):
                if not PFAM_RE.fullmatch(pfam_id):
                    raise MigrationError(f"not a Pfam family ID: {pfam_id!r}")
                found[pfam_id] = self._get(client, pfam_id)
                if self.progress is not None:
                    self.progress(index, len(pfam_ids))
        return found

    def _get(self, client: httpx.Client, pfam_id: str) -> Mapping[str, Any] | None:
        url = f"{INTERPRO_PFAM_URL}{pfam_id}/"
        for attempt in range(self.retries + 1):
            try:
                response = client.get(url)
                if response.status_code in {404, 204}:
                    return None
                if response.status_code in {408, 429, 500, 502, 503, 504} and attempt < self.retries:
                    self.sleep(self.backoff * 2**attempt)
                    continue
                response.raise_for_status()
                payload = response.json()
            except (httpx.TransportError, ValueError) as exc:
                if attempt < self.retries:
                    self.sleep(self.backoff * 2**attempt)
                    continue
                raise MigrationError(f"could not fetch {url}") from exc
            except httpx.HTTPStatusError as exc:
                raise MigrationError(f"InterPro request failed for {url}") from exc
            if not isinstance(payload, Mapping):
                raise MigrationError(f"{url} did not return an object")
            return payload
        raise MigrationError(f"could not fetch {url}")


@dataclass(frozen=True)
class PreparedMigration:
    """Verified migration artifacts and a summary, with no files written."""

    manifest: dict[str, Any]
    artifacts: dict[str, str]
    plan: MigrationPlan


def prepare_migration(
    parent_json: Path,
    previous_names_json: Path,
    *,
    snapshot_date: str,
    fetch: Fetcher | None,
    live_json: Path | None = None,
    generated_at: datetime | None = None,
) -> PreparedMigration:
    """Verify inputs, plan the migration and build complete provenance without writing."""

    parent, parent_manifest, parent_files = _verified(parent_json, WORKLIST_STEM)
    _, names_manifest, names_files = _verified(previous_names_json, PREVIOUS_NAMES_STEM)
    day = date.fromisoformat(snapshot_date)
    if day <= date.fromisoformat(parent_manifest["snapshot"]["date"]):
        raise MigrationError("migration needs a snapshot date later than the parent worklist")
    parent_rows = _worklist_rows(parent)
    live_rows = None
    live_files: dict[str, Any] = {}
    live_id = ""
    if live_json is not None:
        live, live_manifest, live_files = _verified(live_json, WORKLIST_STEM)
        live_rows = _worklist_rows(live)
        live_id = live_manifest["snapshot"]["id"]
    previous = json.loads(previous_names_json.read_bytes())
    fetched_at = generated_at or datetime.now(timezone.utc)
    plan = plan_migration(parent_rows, previous, fetch=fetch, live_rows=live_rows)
    rows = sorted(plan.rows, key=lambda row: (_status_rank(row), -(row.proteins or 0), row.pfam_id))

    snapshot_id = f"{WORKLIST_STEM}-{day.isoformat()}"
    texts = {
        f"{snapshot_id}.json": render_json(rows) + "\n",
        f"{snapshot_id}.tsv": render_tsv(rows) + "\n",
    }
    manifest = build_worklist_manifest(
        rows,
        snapshot_id=snapshot_id,
        snapshot_date=day.isoformat(),
        generated_at=fetched_at,
        json_path=Path(f"{snapshot_id}.json"),
        json_text=texts[f"{snapshot_id}.json"],
        tsv_path=Path(f"{snapshot_id}.tsv"),
        tsv_text=texts[f"{snapshot_id}.tsv"],
    )
    parent_source = parent_manifest["source"]
    manifest["source"] = {
        "name": MIGRATED_SOURCE,
        "url": INTERPRO_PFAM_URL,
        "entry_url": f"{INTERPRO_PFAM_URL}<PFAM_ID>/",
        "note": MIGRATION_NOTE,
        "original_generated_at": parent_source.get("original_generated_at")
        or parent_manifest["snapshot"]["generated_at"],
    }
    inputs = {
        "worklist": parent_manifest["snapshot"]["id"],
        "pfam_previous_names": names_manifest["snapshot"]["id"],
    }
    if live_id:
        inputs["live_worklist"] = live_id
    manifest["snapshot"]["input_snapshot_ids"] = inputs
    transitions = Counter(
        f"{c['before']} -> {c['after']}" for c in plan.reclassified if c["before"] != c["after"]
    )
    manifest["derivation"] = {
        "method": MIGRATION_METHOD,
        "profile": MIGRATION_PROFILE,
        "classifier_policy": CLASSIFIER_POLICY,
        "migration_policy": MIGRATION_POLICY,
        "input_snapshot_generated_at": parent_manifest["snapshot"]["generated_at"],
        "input_files": parent_files,
        "previous_names_files": names_files,
        **({"live_worklist_files": live_files} if live_files else {}),
        "changed_fields": ["unknown_status", "candidate_reasons"],
        "status_transitions": dict(sorted(transitions.items())),
        "changes": plan.reclassified,
        "added_pfam_ids": sorted(plan.added),
        "carried_pfam_ids": sorted(plan.carried),
        "not_found_in_interpro": sorted(plan.not_found),
        "fetched_live": bool(plan.added or plan.carried),
        "fetched_at": _datetime_text(fetched_at) if (plan.added or plan.carried) else None,
    }
    texts[f"{snapshot_id}.manifest.json"] = json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    return PreparedMigration(manifest, texts, plan)


def _verified(path: Path, stem: str) -> tuple[Any, dict[str, Any], dict[str, Any]]:
    manifest_path = path.with_suffix(".manifest.json")
    issues = check_manifest(manifest_path)
    if issues:
        raise MigrationError("; ".join(issue.render() for issue in issues))
    manifest_bytes = manifest_path.read_bytes()
    manifest = json.loads(manifest_bytes)
    if not manifest["snapshot"]["id"].startswith(f"{stem}-"):
        raise MigrationError(f"{path.name} is not a {stem} snapshot")
    if path.name != manifest["files"]["json"]["path"]:
        raise MigrationError("input must be the JSON artifact declared by its manifest")
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != manifest["files"]["json"]["sha256"]:
        raise MigrationError(f"{path.name} changed after manifest validation")
    files = {
        **manifest["files"],
        "manifest": {
            "path": manifest_path.name,
            "bytes": len(manifest_bytes),
            "sha256": hashlib.sha256(manifest_bytes).hexdigest(),
        },
    }
    return json.loads(raw), manifest, files


def _worklist_rows(payload: Any) -> list[DufFamilyRow]:
    names = {item.name for item in fields(DufFamilyRow)}
    rows = []
    for item in payload:
        if set(item) != names | {"source_url"}:
            raise MigrationError(f"{item.get('pfam_id')}: unexpected or missing worklist fields")
        row = DufFamilyRow(**{
            key: tuple(item[key]) if key == "candidate_reasons" else item[key] for key in names
        })
        if item["source_url"] != row.source_url:
            raise MigrationError(f"{row.pfam_id}: cannot preserve a noncanonical source_url")
        rows.append(row)
    return rows


def _status_rank(row: DufFamilyRow) -> int:
    return STATUS_ORDER.get(row.unknown_status, 99)


def _datetime_text(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--parent-json", type=Path, required=True, help="latest verified worklist")
    parser.add_argument("--previous-names-json", type=Path, required=True)
    parser.add_argument(
        "--live-json", type=Path, help="fresh InterPro DUF-search worklist (refresh mode)"
    )
    parser.add_argument("--snapshot-date", required=True, help="new ISO date, later than the parent")
    parser.add_argument("--out-dir", type=Path, default=Path("data/worklists"))
    parser.add_argument("--apply", action="store_true", help="write the snapshot (default: dry run)")
    args = parser.parse_args(argv)

    def progress(done: int, total: int) -> None:
        if done == total or done % 250 == 0:
            print(f"fetched {done}/{total} InterPro entries", file=sys.stderr, flush=True)

    try:
        prepared = prepare_migration(
            args.parent_json,
            args.previous_names_json,
            snapshot_date=args.snapshot_date,
            fetch=InterProEntryClient(progress=progress) if args.apply else None,
            live_json=args.live_json,
        )
        if args.apply:
            write_snapshot_artifacts(args.out_dir, prepared.artifacts)
    except (MigrationError, ReportError, OSError, ValueError) as exc:
        parser.exit(1, f"EX_DUF migration failed: {exc}\n")
    plan, rows = prepared.plan, prepared.manifest["rows"]
    print(
        f"{'wrote' if args.apply else 'dry run:'} {prepared.manifest['snapshot']['id']}: "
        f"{rows['total']} families; {len(plan.reclassified)} reclassified, "
        f"{len(plan.added)} added, {len(plan.carried)} carried, "
        f"{len(plan.not_found)} not found in InterPro"
        + (f", {len(plan.to_fetch)} to fetch on --apply" if plan.to_fetch else "")
        + f"; by status {rows['by_unknown_status']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
