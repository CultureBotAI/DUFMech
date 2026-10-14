"""Discover sequence examples for the verified sibling scan's remaining DUF gaps."""

from __future__ import annotations

import argparse
import copy
import fcntl
import json
import math
import os
import re
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from datetime import date, datetime, timezone
from pathlib import Path

import httpx

from dufmech.example_candidates import UniProtExampleClient
from dufmech.protein_examples import FIELDS, STEM, URL, digest, load_snapshot, normalize_entry
from dufmech.report import load_json_rows, verified_manifest

DIRECT_STEM = f"{STEM}-direct"
KIND = "UNIPROT_FAMILY_SEARCH"
SOURCE_KIND = "DIRECT_UNIPROT_GAP_DISCOVERY"
DIRECT_FIELDS = f"{FIELDS},annotation_score"


def query_settings(per_family: int = 3) -> dict:
    if type(per_family) is not int:
        raise TypeError("per_family must be an integer")
    return UniProtExampleClient(per_family=per_family, fields=DIRECT_FIELDS).settings


def query_url(pfam: str, settings: dict) -> str:
    return str(httpx.URL(URL, params={
        "query": settings["query"].format(pfam_id=pfam), "fields": settings["fields"],
        "sort": settings["sort"], "size": str(settings["per_family"]), "format": "json",
    }))


def validate_search_metadata(observation: dict, settings: dict) -> None:
    if (type(settings.get("per_family")) is not int
            or settings != query_settings(settings["per_family"])):
        raise ValueError("unsupported direct discovery settings")
    pfam = observation.get("pfam_id", "")
    if not re.fullmatch(r"PF\d{5}", pfam):
        raise ValueError("invalid discovery family")
    if observation.get("settings") != settings or observation.get("url") != query_url(pfam, settings):
        raise ValueError("direct discovery query contract differs")
    release = observation.get("release", "")
    if not re.fullmatch(r"\d{4}_\d{2}", release):
        raise ValueError("direct discovery lacks UniProt release")
    fetched = datetime.fromisoformat(observation.get("fetched_at", ""))
    if fetched.utcoffset() is None:
        raise ValueError("discovery timestamp lacks timezone")
    total = observation.get("total")
    if type(total) is not int or total < 0:
        raise ValueError("discovery requires explicit nonnegative total")


def validate_observation(observation: dict, settings: dict) -> list[dict]:
    validate_search_metadata(observation, settings)
    pfam, release, total = (observation[key] for key in ("pfam_id", "release", "total"))
    raw = observation.get("results")
    if not isinstance(raw, list):
        raise TypeError("discovery requires explicit results")
    if len(raw) != min(total, settings["per_family"]):
        raise ValueError("incomplete ranked discovery response")
    examples, order = [], []
    for rank, entry in enumerate(raw, 1):
        normalized = normalize_entry(entry, release)
        if pfam not in normalized["pfam_ids"]:
            raise ValueError("direct result lacks queried Pfam membership")
        score = entry.get("annotationScore")
        if type(score) not in (float, int) or not math.isfinite(score) or not 0 <= score <= 5:
            raise ValueError("invalid discovery annotation score")
        order.append((-score, normalized["uniprot_accession"]))
        examples.append({**normalized, "evidence_scope": "FAMILY_MEMBERSHIP_NOT_FUNCTION",
                         "sequence_origin": "UNIPROT_FETCH", "registry_status": "NOT_CHECKED",
                         "origins": [{"kind": KIND, "url": observation["url"],
                                      "rank": rank, "annotation_score": score,
                                      "uniprot_release": release,
                                      "fetched_at": observation["fetched_at"]}]})
    if order != sorted(order) or len({a for _, a in order}) != len(order):
        raise ValueError("duplicate or incorrectly ranked discovery results")
    return examples


def validate_direct_row(row: dict) -> None:
    metadata = row["direct_discovery"]
    validate_search_metadata(metadata, metadata["settings"])
    if metadata["pfam_id"] != row["pfam_id"] or not row["discovery_scanned"] or row["unresolved"]:
        raise ValueError("inconsistent direct discovery family scope")
    if len(row["examples"]) != min(metadata["total"], metadata["settings"]["per_family"]):
        raise ValueError("direct discovery sample size differs from query")
    order = []
    for rank, example in enumerate(row["examples"], 1):
        origins = example["origins"]
        if len(origins) != 1:
            raise ValueError("direct discovery must retain its one query origin")
        origin = origins[0]
        score = origin.get("annotation_score")
        if type(score) not in (int, float) or not math.isfinite(score) or not 0 <= score <= 5:
            raise ValueError("invalid direct discovery annotation score")
        expected = {"kind": KIND, "url": metadata["url"], "rank": rank,
                    "annotation_score": score, "uniprot_release": metadata["release"],
                    "fetched_at": metadata["fetched_at"]}
        if (origin != expected or type(origin["rank"]) is not int
                or example["uniprot_release"] != metadata["release"]
                or example["registry_status"] != "NOT_CHECKED"
                or example["source_url"] != f"https://rest.uniprot.org/uniprotkb/{example['uniprot_accession']}.json"):
            raise ValueError("inconsistent direct query provenance")
        order.append((-score, example["uniprot_accession"]))
    if order != sorted(order):
        raise ValueError("incorrectly ranked direct examples")


def parse_checkpoint(content: str, settings: dict) -> dict[str, dict]:
    observations, releases = {}, set()
    if content and not content.endswith("\n"):
        raise ValueError("checkpoint has an incomplete final line; preserve it and use a repaired staging copy")
    for line in content.splitlines():
        observation = json.loads(line)
        validate_observation(observation, settings)
        pfam = observation["pfam_id"]
        if pfam in observations:
            raise ValueError("duplicate discovery checkpoint family")
        observations[pfam] = observation
        releases.add(observation["release"])
        if len(releases) > 1:
            raise ValueError("mixed UniProt releases in discovery checkpoint")
    return observations


def discover(targets: set[str], checkpoint: Path, *, per_family: int = 3,
             workers: int = 2, offline: bool = False,
             transport: httpx.BaseTransport | None = None) -> dict[str, dict]:
    """Append only validated responses, with bounded requests and an exclusive writer."""
    if type(workers) is not int or not 1 <= workers <= 4:
        raise ValueError("workers must be between one and four")
    settings = query_settings(per_family)
    adapter = UniProtExampleClient(per_family=per_family, fields=DIRECT_FIELDS, transport=transport)
    if any(not re.fullmatch(r"PF\d{5}", pfam) for pfam in targets):
        raise ValueError("invalid discovery target")
    if any(p.is_symlink() for p in (checkpoint, *checkpoint.absolute().parents)):
        raise ValueError("checkpoint must not traverse symlinks")
    existing = parse_checkpoint(checkpoint.read_text() if checkpoint.exists() else "", settings)
    if existing.keys() - targets:
        raise ValueError("checkpoint contains families outside the target cohort")
    missing = sorted(targets - existing.keys())
    if offline:
        if missing:
            raise ValueError(f"offline discovery checkpoint lacks {len(missing)} families")
        return existing
    if not missing:
        return existing
    if checkpoint.exists() and checkpoint.stat().st_nlink != 1:
        raise ValueError("writable discovery checkpoint must not have hard-link aliases")
    for manifest in checkpoint.parent.glob("*.manifest.json"):
        if any(item.get("path") == checkpoint.name
               for item in json.loads(manifest.read_text()).get("files", {}).values()):
            raise ValueError("checkpoint belongs to an immutable snapshot; use a staging copy")
    checkpoint.parent.mkdir(parents=True, exist_ok=True)
    with checkpoint.open("a+", encoding="utf-8") as sink:
        fcntl.flock(sink, fcntl.LOCK_EX | fcntl.LOCK_NB)
        sink.seek(0)
        if parse_checkpoint(sink.read(), settings) != existing:
            raise ValueError("checkpoint changed while acquiring writer lock")
        sink.seek(0, 2)
        releases = {row["release"] for row in existing.values()}
        with httpx.Client(timeout=adapter.timeout, transport=transport,
                          headers={"User-Agent": "DUFMech/1.0 (https://github.com/CultureBotAI/DUFMech)"}) as client:
            def fetch(pfam: str) -> dict:
                payload, headers = adapter._get(client, pfam)
                try:
                    total = int(headers.get("x-total-results", ""))
                except ValueError as exc:
                    raise ValueError(f"UniProt search for {pfam} lacks an explicit result count") from exc
                result = {"pfam_id": pfam, "settings": settings, "url": query_url(pfam, settings),
                          "fetched_at": datetime.now(timezone.utc).isoformat(),
                          "release": headers.get("x-uniprot-release", ""),
                          "total": total, "results": payload.get("results")}
                return result

            # Keep only a handful of requests in flight, including on fail-closed exit.
            remaining = iter(missing)
            with ThreadPoolExecutor(max_workers=workers) as pool:
                pending = {pool.submit(fetch, pfam) for pfam in
                           [next(remaining, None) for _ in range(workers)] if pfam is not None}
                while pending:
                    completed, pending = wait(pending, return_when=FIRST_COMPLETED)
                    for future in completed:
                        observation = future.result()
                        validate_observation(observation, settings)
                        releases.add(observation["release"])
                        if len(releases) > 1:
                            raise ValueError("UniProt release changed; start a fresh discovery checkpoint")
                        sink.write(json.dumps(observation, sort_keys=True) + "\n")
                        sink.flush()
                        os.fsync(sink.fileno())
                        existing[observation["pfam_id"]] = observation
                        if len(existing) % 100 == 0 or len(existing) == len(targets):
                            print(f"direct discovery: {len(existing)}/{len(targets)} families", flush=True)
                        pfam = next(remaining, None)
                        if pfam is not None:
                            pending.add(pool.submit(fetch, pfam))
    return existing


def enrich_rows(parent: list[dict], observations: dict[str, dict]) -> list[dict]:
    targets = {row["pfam_id"] for row in parent if row["status"] == "NO_SIBLING_CANDIDATE"}
    if observations.keys() != targets:
        raise ValueError("discovery must account for exactly the parent's uncovered families")
    output = copy.deepcopy(parent)
    for row in output:
        if row["pfam_id"] not in targets:
            continue
        observation = observations[row["pfam_id"]]
        examples = validate_observation(observation, observation["settings"])
        row.update(examples=examples, candidate_count=len(examples), example_count=len(examples),
                   status="HAS_SEQUENCE_EXAMPLE" if examples else "NO_UNIPROT_MEMBERS",
                   direct_discovery={key: value for key, value in observation.items() if key != "results"})
    return output


def parent_path(path: Path, source: dict) -> Path:
    name = source["parent"]["path"]
    if not re.fullmatch(rf"{STEM}-\d{{4}}-\d{{2}}-\d{{2}}\.json", name):
        raise ValueError("direct discovery requires an immutable sibling snapshot parent")
    return path.parent / name


def verify_derivation(path: Path, rows: list[dict], manifest: dict,
                      families: list[dict], worklist_id: str) -> None:
    source = manifest["source"]
    parent_json = parent_path(path, source)
    parent_manifest = parent_json.with_suffix(".manifest.json")
    pin = source["parent"]
    if (digest(parent_json.read_bytes()) != pin["sha256"]
            or digest(parent_manifest.read_bytes()) != pin["manifest_sha256"]):
        raise ValueError("direct discovery parent checksum differs")
    parent, parent_meta = load_snapshot(parent_json, families, worklist_id)
    if pin["snapshot_id"] != parent_meta["snapshot"]["id"]:
        raise ValueError("direct discovery parent identity differs")
    content = (path.parent / manifest["files"]["queries.jsonl"]["path"]).read_bytes()
    if digest(content) != source["checkpoint_sha256"]:
        raise ValueError("direct discovery checkpoint checksum differs")
    observations = parse_checkpoint(content.decode(), source["settings"])
    if enrich_rows(parent, observations) != rows:
        raise ValueError("direct discovery does not reproduce from parent and raw responses")
    fetched = sorted(row["fetched_at"] for row in observations.values())
    if (source["families_queried"] != len(observations)
            or source["uniprot_releases"] != sorted({r["release"] for r in observations.values()})
            or source["acquisition_started_at"] != fetched[0]
            or source["acquisition_finished_at"] != fetched[-1]):
        raise ValueError("direct discovery acquisition accounting differs")


def freeze_discovery(parent_json: Path, checkpoint: Path, out_dir: Path, *,
                     families: list[dict], worklist_id: str, snapshot_date: str,
                     per_family: int = 3) -> Path:
    from dufmech.protein_examples import write_snapshot

    parent, manifest = load_snapshot(parent_json, families, worklist_id)
    if not re.fullmatch(rf"{STEM}-\d{{4}}-\d{{2}}-\d{{2}}\.json", parent_json.name):
        raise ValueError("direct discovery requires an immutable sibling snapshot parent")
    content = checkpoint.read_bytes()
    observations = parse_checkpoint(content.decode(), query_settings(per_family))
    rows = enrich_rows(parent, observations)
    if not observations:
        raise ValueError("no direct discovery targets")
    fetched = sorted(row["fetched_at"] for row in observations.values())
    source = {
        "kind": SOURCE_KIND, "name": "UniProt Consortium; direct Pfam family searches",
        "url": URL, "license": "CC-BY-4.0 (UniProt sequences and metadata)",
        "license_url": "https://rest.uniprot.org/help/license",
        "parent": {"path": parent_json.name, "snapshot_id": manifest["snapshot"]["id"],
                   "sha256": digest(parent_json.read_bytes()),
                   "manifest_sha256": digest(parent_json.with_suffix(".manifest.json").read_bytes())},
        "settings": query_settings(per_family), "families_queried": len(observations),
        "checkpoint_sha256": digest(content),
        "uniprot_releases": sorted({row["release"] for row in observations.values()}),
        "acquisition_started_at": fetched[0], "acquisition_finished_at": fetched[-1],
        "limitations": ["Only the parent's NO_SIBLING_CANDIDATE families were queried.",
                        "Ranked samples are not exhaustive or taxonomically representative.",
                        "Annotation score is not experimental evidence or a reviewed-only filter.",
                        "A successful empty query describes this release, not biological absence.",
                        "Full-protein Pfam membership does not establish domain boundaries or function.",
                        "New direct examples have not been compared with the PTM sequence registry.",
                        "Previously covered families and rejected sibling pairings are unchanged."],
    }
    # Portable successors retain their parent beside them; do not silently copy or repin it.
    retained_parent = out_dir / parent_json.name
    if (not retained_parent.exists() or retained_parent.read_bytes() != parent_json.read_bytes()
            or not retained_parent.with_suffix(".manifest.json").exists()
            or retained_parent.with_suffix(".manifest.json").read_bytes()
            != parent_json.with_suffix(".manifest.json").read_bytes()):
        raise ValueError("retain the unchanged parent artifact set in the output directory first")
    load_snapshot(retained_parent, families, worklist_id)
    return write_snapshot(rows, out_dir, families=families, snapshot_date=snapshot_date,
                          worklist_id=worklist_id, source=source, checkpoint=content, stem=DIRECT_STEM)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--worklist-json", type=Path, required=True)
    parser.add_argument("--parent-json", type=Path, required=True)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--per-family", type=int, default=3)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--acquire-only", action="store_true")
    parser.add_argument("--out-dir", type=Path, default=Path("data/protein_examples"))
    parser.add_argument("--snapshot-date", default=datetime.now(timezone.utc).date().isoformat())
    args = parser.parse_args(argv)
    snapshot_date = date.fromisoformat(args.snapshot_date).isoformat()
    if not args.acquire_only:
        stem = f"{DIRECT_STEM}-{snapshot_date}"
        if any((args.out_dir / f"{stem}.{ext}").exists()
               or (args.out_dir / f"{stem}.{ext}").is_symlink()
               for ext in ("json", "tsv", "manifest.json", "queries.jsonl")):
            raise FileExistsError(f"snapshot already exists: {stem}")
    worklist = verified_manifest(args.worklist_json)
    families = list(load_json_rows(args.worklist_json))
    worklist_id = worklist["snapshot"]["id"]
    parent, _ = load_snapshot(args.parent_json, families, worklist_id)
    targets = {row["pfam_id"] for row in parent if row["status"] == "NO_SIBLING_CANDIDATE"}
    if not targets:
        raise ValueError("parent snapshot has no sibling-discovery gaps")
    observations = discover(targets, args.checkpoint, per_family=args.per_family,
                            workers=args.workers, offline=args.offline)
    if args.acquire_only:
        print(f"validated {len(observations)} family searches in {args.checkpoint}")
        return 0
    path = freeze_discovery(args.parent_json, args.checkpoint, args.out_dir, families=families,
                            worklist_id=worklist_id, snapshot_date=snapshot_date,
                            per_family=args.per_family)
    _, manifest = load_snapshot(path, families, worklist_id)
    print(f"wrote {path}: {manifest['rows']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
