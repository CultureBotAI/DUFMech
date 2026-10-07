"""Deterministic, closed-schema family projections over verified frozen inputs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import secrets
from collections import defaultdict
from contextlib import ExitStack, contextmanager
from functools import lru_cache
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml.generators.pythongen import PythonGenerator

from dufmech.report import family_index, load_latest_rows, verified_manifest
from dufmech.score_inputs import load_score_input, require_verified_score_worklist

SCHEMA = Path(__file__).parent / "schema" / "dufmech.yaml"
COUNTERS = ("proteins", "matches", "proteomes", "taxa", "structures",
            "alphafold_models", "domain_architectures")
OVERLAY_FIELDS = ("curation_status", "review_id", "curation_history", "assertions", "discussions", "datasets",
                  "cross_corpus_links")


class RecordError(ValueError):
    """A record, evidence cache, or generated projection is unsafe or inconsistent."""


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject silent YAML key replacement."""


def _mapping(loader: UniqueKeyLoader, node: yaml.MappingNode) -> dict:
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in result:
            raise RecordError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node)
    return result


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def safe_path(root: Path, relative: str) -> Path:
    """Constrain reads/writes lexically and reject symlinks at every component."""
    rel = Path(relative)
    if rel.is_absolute() or not rel.parts or any(p in (".", "..") for p in rel.parts):
        raise RecordError(f"unsafe relative path: {relative}")
    root = root.absolute()
    current = Path(root.anchor)
    for part in (*root.parts[1:], *rel.parts):
        current /= part
        if current.is_symlink():
            raise RecordError(f"symlink not allowed: {current}")
    return root / rel


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        value = yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
    except (OSError, yaml.YAMLError, TypeError) as exc:
        raise RecordError(f"cannot read record {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise RecordError(f"expected an object: {path}")
    return value


@lru_cache(maxsize=2)
def generated_schema(target: str = "FamilyRecord") -> dict:
    if target not in ("FamilyRecord", "FamilyCuration"):
        raise RecordError(f"unsupported schema class: {target}")
    return json.loads(JsonSchemaGenerator(
        SCHEMA, top_class=target, not_closed=False, include_null=False
    ).serialize())


@lru_cache(maxsize=2)
def validator(target: str = "FamilyRecord") -> Draft202012Validator:
    schema = generated_schema(target)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def validate_record(record: dict, root: Path, *, target: str = "FamilyRecord") -> None:
    """Validate content and independently replay any generated history index."""
    _validate_family_record(record, root, target=target)


def _validate_family_record(
    record: dict, root: Path, *, target: str = "FamilyRecord",
    history_events: list[dict] | None = None,
) -> None:
    errors = sorted(validator(target).iter_errors(record), key=lambda e: str(list(e.path)))
    if errors:
        raise RecordError("; ".join(f"{list(e.path)}: {e.message}" for e in errors))
    if target == "FamilyRecord" and record["id"] != f"Pfam:{record['pfam_id']}":
        raise RecordError("id does not match pfam_id")
    if target == "FamilyRecord":
        from dufmech.history import project_curation_events

        try:
            expected_events = (project_curation_events(root, record["pfam_id"])
                               if history_events is None else history_events)
        except (ValueError, OSError) as exc:
            raise RecordError(str(exc)) from exc
        if record.get("curation_events", []) != expected_events:
            raise RecordError("curation_events differ from canonical history; regenerate records")
    if record.get("curation_status") == "REVIEWED":
        if not record.get("review_id"):
            raise RecordError("REVIEWED requires a retained review_id")
        if target == "FamilyRecord":
            from dufmech.reviews import require_completed_review

            try:
                require_completed_review(root, record["pfam_id"], record["review_id"], record)
            except (ValueError, OSError) as exc:
                raise RecordError(str(exc)) from exc
    curated = record["curation_status"] != "SEEDED" or any(
        record.get(key) for key in ("assertions", "discussions", "datasets", "cross_corpus_links")
    )
    if target == "FamilyRecord" and (curated or record.get("curation_history")):
        if not record.get("curation_history"):
            raise RecordError("curated records require curation_history")
        from dufmech.history import require_record_history

        try:
            require_record_history(root, record["pfam_id"], record["curation_history"])
        except (ValueError, OSError) as exc:
            raise RecordError(str(exc)) from exc
    assertions = record.get("assertions", [])
    identifiers = [item["assertion_id"] for item in assertions]
    if len(set(identifiers)) != len(identifiers):
        raise RecordError("duplicate assertion_id")
    for assertion in assertions:
        if not assertion["statement"].strip() or not assertion["scope"].strip():
            raise RecordError("assertions require nonempty statement and scope")
        for evidence in assertion["evidence"]:
            url = urlsplit(evidence["source_url"])
            if url.scheme != "https" or not url.netloc or url.username or url.password:
                raise RecordError("evidence source_url must be an HTTPS source URL")
            path = safe_path(root, evidence["cache_path"])
            try:
                raw = path.read_bytes()
                content = raw.decode("utf-8")
            except (OSError, UnicodeError) as exc:
                raise RecordError(f"unreadable evidence cache: {path}") from exc
            if hashlib.sha256(raw).hexdigest() != evidence["cache_sha256"]:
                raise RecordError(f"evidence cache hash mismatch: {path}")
            snippet = " ".join(evidence["snippet"].split())
            if not snippet or snippet not in " ".join(content.split()):
                raise RecordError(f"evidence quotation not present: {path}")
            if not evidence["explanation"].strip():
                raise RecordError("evidence requires an explanation of support")


def build_records(root: Path) -> dict[str, dict]:
    """Project source identity unchanged and merge only explicitly curated fields."""
    from dufmech.history import _project_curation_events, load_history_metadata

    worklists = safe_path(root, "data/worklists")
    rows, scores, inputs = load_latest_rows(worklists)
    source = safe_path(root, f"data/worklists/{inputs['worklist']}.json")
    source_bytes = source.read_bytes()
    verified_rows = load_score_input(source, "worklist", payload_bytes=source_bytes).rows
    if list(verified_rows) != rows:
        raise RecordError("worklist changed during record construction")
    provenance = snapshot_provenance(source, root, payload_bytes=source_bytes)
    score_provenance = None
    if inputs.get("scores"):
        score_path = safe_path(root, f"data/worklists/{inputs['scores']}.json")
        score_bytes = score_path.read_bytes()
        if json.loads(score_bytes) != scores:
            raise RecordError("scores changed during record construction")
        score_provenance = snapshot_provenance(score_path, root, payload_bytes=score_bytes)
        require_verified_score_worklist(verified_manifest(score_path), source,
                                       worklist_bytes=source_bytes)
    overlays = safe_path(root, "curation/families")
    identities = {}
    for row in rows:
        for key in ("pfam_id", "name", "short_name", "interpro_id", "description", "source_url"):
            if not isinstance(row.get(key), str):
                raise RecordError(f"{row.get('pfam_id')}: source {key} must be a string")
        identities[row["pfam_id"]] = row
    seen = set()
    result = {}
    history_by_family = defaultdict(list)
    for event in load_history_metadata(root):
        if event["target"]["kind"] == "record":
            history_by_family[event["target"]["slug"]].append(event)
    history_events = {pfam: _project_curation_events(events)
                      for pfam, events in history_by_family.items()}
    for family in family_index(rows, scores):
        pfam = family["pfam_id"]
        if pfam not in identities:
            raise RecordError(f"source Pfam identity must not require normalization: {pfam}")
        identity = identities[pfam]
        record = {
            "id": f"Pfam:{pfam}", "pfam_id": pfam, "name": identity["name"],
            "short_name": identity["short_name"], "seed_status": family["unknown_status"],
            "characterization_status": family["characterization_status"] or "UNSCORED",
            "curation_status": "SEEDED", "source_url": identity["source_url"],
            "counters": {key: family[key] for key in COUNTERS if family[key] is not None},
            "provenance": dict(provenance),
        }
        if identity["interpro_id"]:
            record["interpro_id"] = f"InterPro:{identity['interpro_id']}"
        if score_provenance and family["characterization_status"]:
            record["score_provenance"] = dict(score_provenance)
        if identity["description"]:
            record["description"] = identity["description"]
        overlay = safe_path(root, f"curation/families/{pfam}.yaml")
        if overlay.exists():
            curated = load_yaml(overlay)
            validate_record(curated, root, target="FamilyCuration")
            if curated["pfam_id"] != pfam:
                raise RecordError(f"overlay filename/identity mismatch: {overlay}")
            record.update({key: curated[key] for key in OVERLAY_FIELDS if key in curated})
            seen.add(overlay.name)
        events = history_events.get(pfam, [])
        if events:
            record["curation_events"] = events
        _validate_family_record(record, root, history_events=events)
        result[f"{pfam}.yaml"] = record
    if overlays.exists():
        unknown = {p.name for p in overlays.iterdir()} - seen
        if unknown:
            raise RecordError(f"unrecognized or orphan curation files: {sorted(unknown)}")
    return dict(sorted(result.items()))


def snapshot_provenance(path: Path, root: Path, *, payload_bytes: bytes | None = None) -> dict:
    manifest = verified_manifest(path)
    payload = path.read_bytes() if payload_bytes is None else payload_bytes
    digest = hashlib.sha256(payload).hexdigest()
    if (manifest["files"]["json"]["sha256"] != digest
            or manifest["files"]["json"]["bytes"] != len(payload)):
        raise RecordError(f"snapshot changed during record construction: {path}")
    result = {
        "snapshot_id": manifest["snapshot"]["id"],
        "path": path.relative_to(root).as_posix(),
        "sha256": digest,
        "generated_at": manifest["snapshot"]["generated_at"],
    }
    if manifest.get("source", {}).get("url"):
        result["source_url"] = manifest["source"]["url"]
    return result


def load_records(root: Path) -> list[dict]:
    """Serve only schema-validated projections matching verified source/curation inputs."""
    records = build_records(root)
    write_records(root, records, check=True)
    return list(records.values())


def _encoded(record: dict) -> bytes:
    return yaml.safe_dump(record, sort_keys=False, allow_unicode=True, width=100).encode()


@contextmanager
def _directory_fd(root: Path, relative: Path):
    """Pin each real directory so a concurrent symlink swap cannot redirect writes."""
    if relative.is_absolute() or ".." in relative.parts:
        raise RecordError(f"unsafe directory: {relative}")
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    fd = os.open(root.anchor, flags)
    try:
        for part in root.parts[1:]:
            child = os.open(part, flags, dir_fd=fd)
            os.close(fd)
            fd = child
        for part in relative.parts:
            try:
                os.mkdir(part, dir_fd=fd)
            except FileExistsError:
                pass
            child = os.open(part, flags, dir_fd=fd)
            os.close(fd)
            fd = child
        yield fd
    finally:
        os.close(fd)


def _stage_file(directory: int, payload: bytes) -> str:
    name = f".dufmech-{secrets.token_hex(16)}"
    fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                 0o644, dir_fd=directory)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
    except BaseException:
        os.unlink(name, dir_fd=directory)
        raise
    return name


def _publish(root: Path, path: Path, payload: bytes) -> None:
    """Replace one validated generated file atomically; never modify an overlay."""
    with _directory_fd(root, path.parent.relative_to(root)) as directory:
        temporary = _stage_file(directory, payload)
        try:
            os.replace(temporary, path.name, src_dir_fd=directory, dst_dir_fd=directory)
        finally:
            try:
                os.unlink(temporary, dir_fd=directory)
            except FileNotFoundError:
                pass


@contextmanager
def _writer_lock(root: Path):
    """Coordinate native writers; external edits are additionally retained below."""
    import fcntl

    lock = safe_path(root, ".dufmech/records.lock")
    with _directory_fd(root, lock.parent.relative_to(root)) as directory:
        fd = os.open(lock.name, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW,
                     0o600, dir_fd=directory)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX)
            yield
        finally:
            os.close(fd)


def _publish_projection(root: Path, path: Path, payload: bytes,
                        expected: bytes | None) -> None:
    """Retain the actually displaced inode, then publish with exclusive creation.

    Renaming first preserves edits even from an already-open editor handle. If
    another writer creates the destination during the brief gap, never replace it.
    Recovery copies are deliberately retained, not silently garbage-collected.
    """
    safe_path(root, path.relative_to(root).as_posix())
    with ExitStack() as stack:
        directory = stack.enter_context(_directory_fd(root, path.parent.relative_to(root)))
        temporary = _stage_file(directory, payload)
        backup = None
        backup_fd = None
        try:
            if expected is not None:
                recovery = Path(".dufmech/record-recovery")
                recovery_fd = stack.enter_context(_directory_fd(root, recovery))
                slot = f"prior-{secrets.token_hex(16)}"
                os.mkdir(slot, dir_fd=recovery_fd)
                backup_fd = os.open(slot, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                                    dir_fd=recovery_fd)
                stack.callback(os.close, backup_fd)
                backup = root / recovery / slot / path.name
                os.rename(path.name, path.name, src_dir_fd=directory, dst_dir_fd=backup_fd)
                fd = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=backup_fd)
                with os.fdopen(fd, "rb") as stream:
                    if stream.read() != expected:
                        raise RecordError(f"concurrent edit preserved at {backup}")
            os.link(temporary, path.name, src_dir_fd=directory, dst_dir_fd=directory,
                    follow_symlinks=False)
        except BaseException as exc:
            # Inspect the recovery inode: cancellation may arrive immediately after rename.
            moved = False
            if backup_fd is not None:
                try:
                    os.stat(path.name, dir_fd=backup_fd, follow_symlinks=False)
                    moved = True
                except FileNotFoundError:
                    pass
            if moved:
                try:
                    os.link(path.name, path.name, src_dir_fd=backup_fd, dst_dir_fd=directory,
                            follow_symlinks=False)
                except FileExistsError:
                    pass
                except OSError as restore_error:
                    if isinstance(exc, (KeyboardInterrupt, SystemExit)):
                        raise exc
                    raise RecordError(f"restore failed at {path}; recovery: {backup}") from restore_error
            if isinstance(exc, OSError):
                raise RecordError(f"publication conflict at {path}; recovery: {backup}") from exc
            raise
        finally:
            os.unlink(temporary, dir_fd=directory)


def write_records(root: Path, records: dict[str, dict], *, apply: bool = False,
                  check: bool = False) -> list[str]:
    """Dry-run by default. Only replace files whose previous ownership hash agrees."""
    if apply:
        with _writer_lock(root):
            return _write_records(root, records, apply=apply, check=check)
    return _write_records(root, records, apply=apply, check=check)


def _write_records(root: Path, records: dict[str, dict], *, apply: bool,
                   check: bool) -> list[str]:
    directory = safe_path(root, "data/families")
    owner = safe_path(root, "data/families/manifest.json")
    previous_bytes = owner.read_bytes() if owner.exists() else None
    previous = json.loads(previous_bytes) if previous_bytes is not None else {}
    if not isinstance(previous, dict) or any(not isinstance(v, str) for v in previous.values()):
        raise RecordError("invalid projection ownership manifest")
    payloads = {}
    for name, record in records.items():
        if name != f"{record['pfam_id']}.yaml":
            raise RecordError(f"record filename/identity mismatch: {name}")
        validate_record(record, root)
        safe_path(root, f"data/families/{name}")
        payloads[name] = _encoded(record)
    existing = {p.name for p in directory.iterdir()} - {"manifest.json"} if directory.exists() else set()
    if existing - payloads.keys():
        raise RecordError(f"refusing to delete unrecognized/stale files: {sorted(existing - payloads.keys())}")
    changed = []
    observed = {}
    for name, payload in payloads.items():
        path = safe_path(root, f"data/families/{name}")
        if path.exists():
            old = path.read_bytes()
            observed[name] = old
            if old == payload:
                continue
            if hashlib.sha256(old).hexdigest() != previous.get(name):
                raise RecordError(f"refusing to overwrite edited/unowned projection: {path}")
        changed.append(name)
    ownership = {name: hashlib.sha256(payload).hexdigest() for name, payload in payloads.items()}
    manifest_bytes = (json.dumps(ownership, indent=2, sort_keys=True) + "\n").encode()
    if not owner.exists() or owner.read_bytes() != manifest_bytes:
        changed.append("manifest.json")
    if check and changed:
        raise RecordError(f"stale generated family projections: {len(changed)} files")
    if apply:
        for name in changed:
            if name != "manifest.json":
                _publish_projection(root, safe_path(root, f"data/families/{name}"),
                                    payloads[name], observed.get(name))
        if "manifest.json" in changed:
            _publish_projection(root, owner, manifest_bytes, previous_bytes)
    return changed


def schema_artifacts() -> dict[str, bytes]:
    artifacts = {f"schema/{name}.schema.json": (json.dumps(generated_schema(name),
                 indent=2, sort_keys=True) + "\n").encode()
                 for name in ("FamilyRecord", "FamilyCuration")}
    python_model = PythonGenerator(SCHEMA, metadata=False).serialize()
    compile(python_model, "dufmech.py", "exec")
    artifacts["src/dufmech/datamodel/dufmech.py"] = python_model.encode()
    schema = yaml.safe_load(SCHEMA.read_text())
    lines = ["# DUFMech Schema", "", "Generated from `src/dufmech/schema/dufmech.yaml`.", ""]
    for name, definition in schema["classes"].items():
        lines.extend([f"## {name}", "", definition.get("description", ""), "",
                      "| Field | Type | Required |", "| --- | --- | --- |"])
        for key, field in definition.get("attributes", {}).items():
            lines.append(f"| {key} | {field.get('range', 'string')} | {field.get('required', False)} |")
        lines.append("")
    artifacts["docs/schema.md"] = ("\n".join(lines).rstrip() + "\n").encode()
    return artifacts


def write_schema_artifacts(root: Path, *, apply: bool = False, check: bool = False) -> list[str]:
    changed = []
    for relative, payload in schema_artifacts().items():
        path = safe_path(root, relative)
        if not path.exists() or path.read_bytes() != payload:
            changed.append(relative)
            if apply:
                _publish(root, path, payload)
    if check and changed:
        raise RecordError(f"stale generated schema artifacts: {changed}")
    return changed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--schema-only", action="store_true")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        root = args.root.absolute()
        records = {} if args.schema_only else build_records(root)
        changes = [] if args.schema_only else write_records(
            root, records, apply=args.apply, check=args.check
        )
        changes += write_schema_artifacts(root, apply=args.apply, check=args.check)
    except (RecordError, OSError, ValueError) as exc:
        parser.exit(1, f"records: {exc}\n")
    print(f"{len(records)} schema-valid records; {len(changes)} generated files differ"
          + (" (applied)" if args.apply else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
