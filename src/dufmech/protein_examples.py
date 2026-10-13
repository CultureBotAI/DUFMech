"""Freeze sequence-bearing DUF examples without promoting functional claims."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import subprocess
import time
from collections import Counter, defaultdict
from datetime import date, datetime, timezone
from pathlib import Path

import httpx
import yaml

from dufmech.cross_mech import MechSource, iter_mech_records
from dufmech.cross_mech_snapshot import cross_mech_unscanned, load_cross_mech_snapshot
from dufmech.report import ReportError, load_json_rows, verified_manifest
from dufmech.site_data import source_link
from dufmech.uniprotkb import row_from_uniprotkb_entry

STEM = "duf-protein-examples"
URL = "https://rest.uniprot.org/uniprotkb/search"
FIELDS = ("accession,reviewed,protein_name,organism_name,organism_id,sequence,length,"
          "sequence_version,xref_pfam")
ACCESSION = re.compile(r"(?:[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})")
REGISTRY = "data/grounding/protein_registry.jsonl"
TSV_FIELDS = ["pfam_id", "short_name", "status", "candidate_count", "example_count",
              "accessions", "unresolved_accessions"]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sequence_valid(row: dict) -> None:
    sequence = row.get("sequence")
    if not isinstance(sequence, str) or not re.fullmatch(r"[ACDEFGHIKLMNPQRSTVWYBXZJUO]+", sequence):
        raise ValueError("invalid amino acid sequence")
    if type(row.get("sequence_length")) is not int or row["sequence_length"] != len(sequence):
        raise ValueError("sequence length mismatch")
    if row.get("sequence_sha256") != digest(sequence.encode("ascii")):
        raise ValueError("sequence checksum mismatch")
    if type(row.get("sequence_version")) is not int or row["sequence_version"] < 1:
        raise ValueError("missing sequence version")
    if not re.fullmatch(r"\d{4}_\d{2}", row.get("uniprot_release", "")):
        raise ValueError("missing UniProt release")


def normalize_entry(entry: dict, release: str) -> dict:
    metadata = row_from_uniprotkb_entry(entry)
    if metadata is None or not ACCESSION.fullmatch(metadata.uniprot_accession):
        raise ValueError("invalid primary UniProt accession")
    seq = entry.get("sequence", {})
    value = seq.get("value", "")
    row = {
        "uniprot_accession": metadata.uniprot_accession,
        "protein_name": metadata.protein_name, "reviewed": metadata.reviewed,
        "taxon_id": metadata.taxon_id, "organism": metadata.organism,
        "sequence": value, "sequence_length": seq.get("length"),
        "sequence_sha256": digest(value.encode("ascii")),
        "sequence_version": entry.get("entryAudit", {}).get("sequenceVersion"),
        "uniprot_release": release,
        "pfam_ids": sorted({ref["id"] for ref in entry.get("uniProtKBCrossReferences", [])
                            if ref.get("database") == "Pfam"}),
        "source_url": f"https://rest.uniprot.org/uniprotkb/{metadata.uniprot_accession}.json",
    }
    sequence_valid(row)
    return row


def acquire(accessions: list[str], checkpoint: Path, *, offline: bool = False,
            transport: httpx.BaseTransport | None = None) -> dict[str, dict | None]:
    """Resume exact-primary lookups. Missing/merged/isoform IDs are never substituted."""
    known, releases = {}, set()
    if checkpoint.is_symlink():
        raise ValueError("checkpoint must not be a symlink")
    if checkpoint.exists():
        for line in checkpoint.read_text().splitlines():
            batch = json.loads(line)
            if batch.get("fields") != FIELDS or batch.get("url") != URL:
                raise ValueError("checkpoint query contract differs")
            if not re.fullmatch(r"\d{4}_\d{2}", batch.get("release", "")):
                raise ValueError("checkpoint has no release")
            releases.add(batch["release"])
            if len(releases) > 1:
                raise ValueError("mixed UniProt releases in checkpoint")
            for accession, entry in batch["results"].items():
                if accession in known:
                    raise ValueError("duplicate checkpoint accession")
                if entry is not None:
                    sequence_valid(entry)
                    if entry["uniprot_accession"] != accession:
                        raise ValueError("checkpoint substituted an accession")
                    if entry["uniprot_release"] != batch["release"]:
                        raise ValueError("checkpoint entry release mismatch")
                known[accession] = entry
    wanted = sorted(set(accessions))
    missing = [a for a in wanted if a not in known and ACCESSION.fullmatch(a)]
    if offline and missing:
        raise ValueError(f"offline checkpoint lacks {len(missing)} accessions")
    with httpx.Client(timeout=60, transport=transport) as client:
        for start in range(0, len(missing), 100):
            batch = missing[start:start + 100]
            params = {"query": " OR ".join(f"accession:{a}" for a in batch),
                      "fields": FIELDS, "format": "json", "size": "500"}
            for attempt in range(4):
                try:
                    response = client.get(URL, params=params)
                    response.raise_for_status()
                    break
                except httpx.HTTPError:
                    if attempt == 3:
                        raise
                    time.sleep(2 ** attempt)
            release = response.headers.get("x-uniprot-release", "")
            if not re.fullmatch(r"\d{4}_\d{2}", release):
                raise ValueError("UniProt response has no release")
            releases.add(release)
            if len(releases) != 1:
                raise ValueError("UniProt release changed; start a new checkpoint")
            if response.links.get("next"):
                raise ValueError("unexpected pagination; reduce the accession batch size")
            entries = response.json().get("results")
            if not isinstance(entries, list):
                raise TypeError("UniProt response lacks results")
            current = dict.fromkeys(batch)
            for entry in entries:
                accession = entry.get("primaryAccession")
                if accession in current:
                    if current[accession] is not None:
                        raise ValueError("duplicate UniProt result")
                    current[accession] = normalize_entry(entry, release)
            observation = {"fields": FIELDS, "url": URL, "release": release,
                           "fetched_at": datetime.now(timezone.utc).isoformat(),
                           "results": current}
            checkpoint.parent.mkdir(parents=True, exist_ok=True)
            with checkpoint.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(observation, sort_keys=True) + "\n")
            known.update(current)
            print(f"sequence lookups: {min(start + 100, len(missing))}/{len(missing)}", flush=True)
    return {a: known.get(a) for a in wanted}


def read_registry(repo: Path, pin: dict) -> tuple[dict, dict]:
    commit = pin["commit"]
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("registry requires an immutable commit")
    content = subprocess.check_output(["git", "-C", str(repo), "show", f"{commit}:{REGISTRY}"])
    rows = {}
    for line in content.splitlines():
        row = json.loads(line)
        accession = row["protein_id"].removeprefix("UniProtKB:")
        sequence_valid(row)
        if accession in rows:
            raise ValueError("duplicate registry accession")
        rows[accession] = row
    return rows, {"commit": commit, "path": REGISTRY, "sha256": digest(content),
                  "repository": pin["repository"],
                  "url": source_link(pin["repository"], commit, REGISTRY)}


def direct_family_candidates(repo: Path, pin: dict, candidates: list[dict]) -> tuple[list, dict]:
    """Read Pfam-owned examples too: qualified PTM entries may omit legacy classifications."""
    targets = {r["source_path"]: r for r in candidates
               if r["source_mech"] == "ProteinTraitsMech"
               and r["source_section"] == "trait_identifier"
               and r["source_record_id"] == f"Pfam:{r['pfam_id']}"}
    commit, records = iter_mech_records(
        repo.parent, MechSource(repo.name, pin["data_dir"]), ref=pin["commit"], paths=set(targets))
    rows, seen, statuses = [], set(), Counter()
    for record in records:
        template = targets[record.path]
        payload = yaml.load(record.text, Loader=yaml.CSafeLoader)
        if payload.get("identifier") != template["source_record_id"]:
            raise ValueError("PTM family identity differs from pinned discovery")
        seen.add(record.path)
        for example in payload.get("canonical_examples", []):
            accession = example.get("protein_id", "").removeprefix("UniProtKB:")
            if not accession:
                continue
            status = example.get("qualification_status", "LEGACY_OR_UNSPECIFIED")
            statuses[status] += 1
            rows.append({**template, "uniprot_accession": accession,
                         "source_section": "canonical_examples",
                         "link_basis": ["ptm_own_pfam_record_example"],
                         "qualification_status": status,
                         "cited_uniprot_accession": ""})
    if seen != targets.keys():
        raise ValueError("some pinned PTM family records could not be inspected")
    return rows, {"commit": commit, "records_inspected": len(seen), "examples": len(rows),
                  "qualification_statuses": dict(statuses)}


def registry_candidates(registry: dict, entries: dict, families: list[dict]) -> tuple[list, dict]:
    """Discover target-family carriers across the entire PTM sequence registry."""
    catalogue = {r["pfam_id"] for r in families}
    rows, unavailable, without_family = [], [], []
    for accession in sorted(registry):
        current = entries.get(accession)
        if current is None:
            unavailable.append(accession)
            continue
        pfams = sorted(catalogue.intersection(current["pfam_ids"]))
        if not pfams:
            without_family.append(accession)
        for pfam in pfams:
            rows.append({"pfam_id": pfam, "uniprot_accession": accession,
                         "source_mech": "ProteinTraitsMech", "source_path": REGISTRY,
                         "source_record_id": f"UniProtKB:{accession}",
                         "source_section": "protein_registry",
                         "link_basis": ["ptm_registry_exact_uniprot_pfam_xref"],
                         "qualification_status": "NOT_ASSESSED_FOR_THIS_FAMILY"})
    return rows, {"proteins_checked": len(registry), "family_protein_pairs": len(rows),
                  "no_exact_current_entry": unavailable,
                  "without_target_family_count": len(without_family)}


def build_rows(families: list[dict], candidates: list[dict], sources: dict,
               entries: dict, registry: dict, registry_source: dict,
               *, unscanned: set[str] = frozenset()) -> list[dict]:
    """Every family is accounted for; only current Pfam-confirmed sequences are examples."""
    by_family = defaultdict(lambda: defaultdict(list))
    catalogue = {r["pfam_id"] for r in families}
    for row in candidates:
        accession, pfam = row.get("uniprot_accession"), row.get("pfam_id")
        if not accession or not pfam:
            continue
        if pfam not in catalogue:
            raise ValueError("candidate family is outside the worklist")
        source = sources[row["source_mech"]]
        url = source_link(source["repository"], source["commit"], row["source_path"])
        if not url:
            raise ValueError("candidate lacks pinned source")
        origin = {"mech": row["source_mech"], "record_id": row["source_record_id"],
                  "path": row["source_path"], "section": row["source_section"],
                  "commit": source["commit"], "url": url,
                  "link_basis": list(row["link_basis"]),
                  "qualification_status": row.get("qualification_status", "NOT_ASSESSED"),
                  "cited_uniprot_accession": row.get("cited_uniprot_accession", "")}
        previous = next((o for o in by_family[pfam][accession] if all(
            o[key] == origin[key] for key in ("mech", "path", "section", "cited_uniprot_accession"))), None)
        if previous is None:
            by_family[pfam][accession].append(origin)
        else:
            previous["link_basis"] = sorted(set(previous["link_basis"] + origin["link_basis"]))
            if origin["qualification_status"] != "NOT_ASSESSED":
                previous["qualification_status"] = origin["qualification_status"]
    output = []
    for family in sorted(families, key=lambda row: row["pfam_id"]):
        pfam = family["pfam_id"]
        examples, unresolved = [], []
        for accession, origins in sorted(by_family[pfam].items()):
            current = entries.get(accession)
            reason = ("ISOFORM_OR_INVALID_ACCESSION" if not ACCESSION.fullmatch(accession) else
                      "RESOLVED_ACCESSION_REQUIRES_REVIEW" if all(
                          o["cited_uniprot_accession"] not in ("", accession) for o in origins) else
                      "NO_EXACT_CURRENT_ENTRY" if current is None else
                      "PFAM_NOT_IN_CURRENT_ENTRY" if pfam not in current["pfam_ids"] else "")
            if reason:
                unresolved.append({"uniprot_accession": accession, "reason": reason,
                                   "origins": origins})
                continue
            sequence_valid(current)
            if current["uniprot_accession"] != accession:
                raise ValueError("entry accession mismatch")
            mirror = registry.get(accession)
            match = (mirror is not None and mirror["sequence_sha256"] == current["sequence_sha256"]
                     and mirror["sequence_version"] == current["sequence_version"])
            example = {**current, "origins": origins,
                       "evidence_scope": "FAMILY_MEMBERSHIP_NOT_FUNCTION",
                       "sequence_origin": "PTM_REGISTRY_MIRROR" if match else "UNIPROT_FETCH",
                       "registry_status": "EXACT_SEQUENCE_VERSION_MATCH" if match else
                       "DIFFERENT_SEQUENCE_OR_VERSION" if mirror else "NOT_IN_REGISTRY"}
            if mirror:
                example["registry_source"] = {
                    **registry_source, "uniprot_release": mirror["uniprot_release"],
                    "sequence_sha256": mirror["sequence_sha256"],
                    "sequence_version": mirror["sequence_version"],
                }
            if match:
                example["sequence"] = mirror["sequence"]
            examples.append(example)
        output.append({"pfam_id": pfam, "short_name": family["short_name"],
                       "discovery_scanned": pfam not in unscanned,
                       "status": "HAS_SEQUENCE_EXAMPLE" if examples else
                       "UNRESOLVED_CANDIDATES" if unresolved else
                       "NOT_SCANNED" if pfam in unscanned else "NO_SIBLING_CANDIDATE",
                       "candidate_count": len(by_family[pfam]), "example_count": len(examples),
                       "examples": examples, "unresolved": unresolved})
    return output


def validate_rows(rows: list[dict], families: list[dict]) -> None:
    expected = {r["pfam_id"]: r["short_name"] for r in families}
    if len(rows) != len(expected) or {r["pfam_id"] for r in rows} != expected.keys():
        raise ValueError("example coverage must account for every worklist family exactly once")
    for row in rows:
        pfam = row["pfam_id"]
        if row["short_name"] != expected[pfam]:
            raise ValueError("example family label differs from the worklist")
        examples, unresolved = row["examples"], row["unresolved"]
        if type(row["discovery_scanned"]) is not bool:
            raise ValueError("discovery coverage must be an explicit boolean")
        if any(type(row[key]) is not int for key in ("candidate_count", "example_count")):
            raise ValueError("example counts must be integers")
        ids = [e["uniprot_accession"] for e in examples + unresolved]
        if len(ids) != len(set(ids)) or len(ids) != row["candidate_count"]:
            raise ValueError("duplicate or inconsistent candidate accounting")
        if row["example_count"] != len(examples):
            raise ValueError("example count mismatch")
        status = ("HAS_SEQUENCE_EXAMPLE" if examples else
                  "UNRESOLVED_CANDIDATES" if unresolved else
                  "NO_SIBLING_CANDIDATE" if row["discovery_scanned"] else "NOT_SCANNED")
        if row["status"] != status:
            raise ValueError("example coverage status mismatch")
        for example in examples:
            sequence_valid(example)
            if not ACCESSION.fullmatch(example["uniprot_accession"]):
                raise ValueError("invalid example accession")
            if pfam not in example["pfam_ids"]:
                raise ValueError("example lacks exact family membership")
            if example["evidence_scope"] != "FAMILY_MEMBERSHIP_NOT_FUNCTION":
                raise ValueError("unsupported functional promotion")
            if not example["origins"]:
                raise ValueError("example lacks sibling provenance")
            if example["sequence_origin"] == "PTM_REGISTRY_MIRROR":
                registry = example.get("registry_source", {})
                if any(registry.get(key) != example[key]
                       for key in ("sequence_sha256", "sequence_version")):
                    raise ValueError("mirrored sequence differs from registry provenance")


def coverage_counts(rows: list[dict]) -> dict:
    return {"total": len(rows), "by_status": dict(Counter(r["status"] for r in rows)),
            "examples": sum(r["example_count"] for r in rows),
            "proteins": len({e["uniprot_accession"] for r in rows for e in r["examples"]})}


def write_snapshot(rows: list[dict], out_dir: Path, *, families: list[dict],
                   snapshot_date: str, worklist_id: str, source: dict,
                   checkpoint: bytes | None = None) -> Path:
    validate_rows(rows, families)
    snapshot_date = date.fromisoformat(snapshot_date).isoformat()
    stem = f"{STEM}-{snapshot_date}"
    if any(p.is_symlink() for p in (out_dir, *out_dir.absolute().parents)):
        raise ValueError("snapshot directory must not traverse symlinks")
    out_dir.mkdir(parents=True, exist_ok=True)
    tsv = io.StringIO()
    writer = csv.DictWriter(tsv, TSV_FIELDS, dialect="excel-tab", lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({**{k: row[k] for k in TSV_FIELDS[:5]},
                         "accessions": ";".join(e["uniprot_accession"] for e in row["examples"]),
                         "unresolved_accessions": ";".join(e["uniprot_accession"]
                                                          for e in row["unresolved"])})
    payloads = {"json": (json.dumps(rows, indent=2, sort_keys=True) + "\n").encode(),
                "tsv": tsv.getvalue().encode()}
    if checkpoint is not None:
        payloads["queries.jsonl"] = checkpoint
    manifest = {
        "snapshot": {"id": stem, "date": snapshot_date,
                     "generated_at": datetime.now(timezone.utc).isoformat(),
                     "input_snapshot_ids": {"worklist": worklist_id}},
        "source": source, "schema": {"tsv_fieldnames": TSV_FIELDS},
        "rows": coverage_counts(rows),
        "files": {ext: {"path": f"{stem}.{ext}", "bytes": len(data), "sha256": digest(data)}
                  for ext, data in payloads.items()},
    }
    payloads["manifest.json"] = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    paths = {ext: out_dir / f"{stem}.{ext}" for ext in payloads}
    if any(p.exists() or p.is_symlink() for p in paths.values()):
        raise FileExistsError(f"snapshot already exists: {stem}")
    created = []
    try:
        for ext, data in payloads.items():
            with paths[ext].open("xb") as handle:
                created.append(paths[ext])
                handle.write(data)
        verified_manifest(paths["json"])
    except Exception:
        for path in reversed(created):
            path.unlink()
        raise
    return paths["json"]


def load_snapshot(path: Path, families: list[dict], worklist_id: str) -> tuple[list[dict], dict]:
    manifest = verified_manifest(path)
    if manifest["snapshot"].get("input_snapshot_ids", {}).get("worklist") != worklist_id:
        raise ReportError("protein examples use a different worklist")
    rows = list(load_json_rows(path))
    validate_rows(rows, families)
    if manifest["rows"] != coverage_counts(rows):
        raise ValueError("protein-example manifest coverage differs from actual rows")
    return rows, manifest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--worklist-json", type=Path, required=True)
    parser.add_argument("--cross-mech-json", type=Path, required=True)
    parser.add_argument("--ptm-repo", type=Path, required=True)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, default=Path("data/protein_examples"))
    parser.add_argument("--snapshot-date", required=True)
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--registry-scope", choices=("all", "referenced"), default="all",
                        help="all checks the entire PTM registry; referenced reproduces the pilot")
    args = parser.parse_args(argv)
    stem = f"{STEM}-{date.fromisoformat(args.snapshot_date).isoformat()}"
    if any((args.out_dir / f"{stem}.{ext}").exists()
           or (args.out_dir / f"{stem}.{ext}").is_symlink()
           for ext in ("json", "tsv", "manifest.json", "queries.jsonl")):
        raise FileExistsError(f"snapshot already exists: {stem}")
    worklist = verified_manifest(args.worklist_json)
    families = list(load_json_rows(args.worklist_json))
    worklist_id = worklist["snapshot"]["id"]
    candidates, cross = load_cross_mech_snapshot(
        args.cross_mech_json, worklist_rows=families, worklist_snapshot_id=worklist_id)
    sources = cross["source"]["mechs"]
    registry, registry_source = read_registry(args.ptm_repo, sources["ProteinTraitsMech"])
    direct, direct_scope = direct_family_candidates(
        args.ptm_repo, sources["ProteinTraitsMech"], candidates)
    candidates.extend(direct)
    registry_accessions = list(registry) if args.registry_scope == "all" else []
    entries = acquire([*registry_accessions, *(r["uniprot_accession"] for r in candidates
                       if r.get("pfam_id") and r.get("uniprot_accession"))],
                      args.checkpoint, offline=args.offline)
    registry_scope = {"mode": args.registry_scope}
    if args.registry_scope == "all":
        registry_rows, registry_counts = registry_candidates(registry, entries, families)
        registry_scope.update(registry_counts)
        candidates.extend(registry_rows)
    rows = build_rows(families, candidates, sources, entries, registry, registry_source,
                      unscanned=cross_mech_unscanned(cross))
    observations = [json.loads(line) for line in args.checkpoint.read_text().splitlines()]
    fetched = sorted(batch["fetched_at"] for batch in observations)
    source = {
        "name": "UniProt Consortium; sibling Mech accession references and PTM sequence registry",
        "url": URL, "license": "CC-BY-4.0 (UniProt sequences and metadata)",
        "license_url": "https://rest.uniprot.org/help/license",
        "cross_mech_snapshot": cross["snapshot"]["id"],
        "cross_mech_sha256": digest(args.cross_mech_json.read_bytes()),
        "mechs": sources, "registry": registry_source,
        "ptm_direct_family_examples": direct_scope,
        "ptm_registry_discovery": registry_scope,
        "checkpoint_sha256": digest(args.checkpoint.read_bytes()),
        "acquisition_started_at": fetched[0], "acquisition_finished_at": fetched[-1],
        "uniprot_releases": sorted({e["uniprot_release"] for e in entries.values() if e}),
        "limitations": ["Family membership is not experimental functional evidence.",
                        "No domain coordinates are inferred from whole-protein sequences.",
                        "No sibling candidate does not mean UniProt has no family members.",
                        "Inactive, merged and isoform accessions are not silently substituted.",
                        "Coverage is limited to the named source repositories and pinned commits."],
    }
    path = write_snapshot(rows, args.out_dir, families=families, snapshot_date=args.snapshot_date,
                          worklist_id=worklist_id, source=source,
                          checkpoint=args.checkpoint.read_bytes())
    print(f"wrote {path}: {dict(Counter(r['status'] for r in rows))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
