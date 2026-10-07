"""Offline KGX and SSSOM projections of verified Pfam/InterPro associations."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import os
import stat
import sys
from contextlib import ExitStack
from pathlib import Path

import yaml

from dufmech.records import (
    RecordError,
    _directory_fd,
    _stage_file,
    load_records,
    safe_path,
)
from dufmech.report import ReportError
from dufmech.reviews import read_source_bytes

REPOSITORY = "https://github.com/CultureBotAI/DUFMech"
PFAM_SOURCE = "https://www.ebi.ac.uk/interpro/entry/pfam/"
INTERPRO_SOURCE = "https://www.ebi.ac.uk/interpro/entry/InterPro/"
KGX_NODES = "exports/kgx/nodes.tsv"
KGX_EDGES = "exports/kgx/edges.tsv"
SSSOM = "exports/sssom/dufmech.sssom.tsv"
PROVENANCE_COLUMNS = (
    "source_snapshot_id", "source_snapshot_path", "source_snapshot_sha256",
    "source_snapshot_generated_at",
)
NODE_COLUMNS = (
    "id", "category", "name", "description", "provided_by", "source_url",
    "seed_status", "characterization_status", "curation_status", *PROVENANCE_COLUMNS,
)
EDGE_COLUMNS = (
    "id", "subject", "predicate", "object", "provided_by", "source_url",
    "source_record", "source_field", *PROVENANCE_COLUMNS,
)
SSSOM_COLUMNS = (
    "subject_id", "subject_label", "predicate_id", "object_id", "object_label",
    "mapping_justification", "confidence", "comment", "mapping_provider",
    "subject_source", "object_source",
)
ASSOCIATION_NOTE = (
    "Frozen Pfam integrated InterPro association only; neither equivalence nor "
    "functional characterization. InterPro label, per-association matching method "
    "and confidence are not recorded."
)


class ExportError(ValueError):
    """An export cannot be constructed or safely published."""


def _cell(value: str) -> str:
    """Escape reversibly without CSV quoting or physical field/line delimiters."""
    if not isinstance(value, str):
        raise ExportError("TSV values must be strings")
    escaped = {"\\": "\\\\", '"': "\\u0022", "\t": "\\t", "\n": "\\n", "\r": "\\r"}
    return "".join(
        escaped.get(char, f"\\u{ord(char):04x}")
        if char in escaped or ord(char) < 32 or ord(char) in (127, 133, 8232, 8233)
        else char
        for char in value
    )


def _table(columns: tuple[str, ...], rows: list[dict[str, str]]) -> str:
    lines = ["\t".join(columns)]
    lines.extend("\t".join(_cell(row.get(column, "")) for column in columns) for row in rows)
    text = "\n".join(lines) + "\n"
    literal = [line.split("\t") for line in text.splitlines()]
    if list(csv.reader(io.StringIO(text), delimiter="\t")) != literal:
        raise ExportError("CSV and literal TSV readers disagree")
    return text


def _provenance(record: dict) -> dict[str, str]:
    source = record["provenance"]
    return dict(zip(PROVENANCE_COLUMNS, (
        source["snapshot_id"], source["path"], source["sha256"], source["generated_at"],
    )))


def build_exports(root: Path) -> dict[str, bytes]:
    """Validate native inputs and stored projections, then render without writing."""
    records = load_records(root.absolute())
    if not records:
        raise ExportError("no verified family records to export")
    nodes: dict[str, dict[str, str]] = {}
    edges = []
    mappings = []
    for record in sorted(records, key=lambda item: item["id"]):
        subject = record["id"]
        provenance = _provenance(record)
        nodes[subject] = {
            "id": subject, "category": "biolink:NamedThing", "name": record["name"],
            "description": record.get("description", ""), "provided_by": REPOSITORY,
            "source_url": record["source_url"], "seed_status": record["seed_status"],
            "characterization_status": record["characterization_status"],
            "curation_status": record["curation_status"], **provenance,
        }
        obj = record.get("interpro_id")
        if not obj:
            continue
        # The snapshot gives an accession, but no InterPro name or entry type.
        nodes.setdefault(obj, {
            "id": obj, "category": "biolink:NamedThing", "provided_by": REPOSITORY,
            "source_url": INTERPRO_SOURCE + obj.split(":", 1)[1], **provenance,
        })
        locator = f"data/families/{record['pfam_id']}.yaml"
        edge_key = "\n".join((subject, "biolink:related_to", obj, provenance["source_snapshot_sha256"]))
        edges.append({
            "id": "dufmech:association-" + hashlib.sha256(edge_key.encode()).hexdigest(),
            "subject": subject, "predicate": "biolink:related_to", "object": obj,
            "provided_by": REPOSITORY, "source_url": record["source_url"],
            "source_record": locator, "source_field": "interpro_id", **provenance,
        })
        details = {
            **provenance, "source_record": locator, "source_field": "interpro_id",
            "curation_status": record["curation_status"],
        }
        mappings.append({
            "subject_id": subject, "subject_label": record["name"],
            "predicate_id": "skos:relatedMatch", "object_id": obj,
            "mapping_justification": "semapv:UnspecifiedMatching",
            "comment": ASSOCIATION_NOTE + " " + "; ".join(
                f"{key}={value}" for key, value in details.items()
            ),
            "mapping_provider": record["source_url"],
            "subject_source": PFAM_SOURCE, "object_source": INTERPRO_SOURCE,
        })
    if not mappings:
        raise ExportError("no verified Pfam/InterPro associations to export")
    metadata = {
        "mapping_set_id": f"{REPOSITORY}/blob/main/{SSSOM}",
        "mapping_set_title": "DUFMech frozen Pfam/InterPro associations",
        "mapping_set_description": ASSOCIATION_NOTE,
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "mapping_tool": f"{REPOSITORY}/blob/main/src/dufmech/exports.py",
        "curie_map": {
            "Pfam": PFAM_SOURCE, "InterPro": INTERPRO_SOURCE,
            "skos": "http://www.w3.org/2004/02/skos/core#",
            "semapv": "https://w3id.org/semapv/vocab/",
        },
    }
    preamble = "".join(
        "# " + line + "\n"
        for line in yaml.safe_dump(metadata, sort_keys=False, width=1000).splitlines()
    )
    return {
        KGX_NODES: _table(NODE_COLUMNS, [nodes[key] for key in sorted(nodes)]).encode(),
        KGX_EDGES: _table(EDGE_COLUMNS, edges).encode(),
        SSSOM: (preamble + _table(SSSOM_COLUMNS, mappings)).encode(),
    }


def _existing(root: Path, relative: str) -> bytes | None:
    try:
        return read_source_bytes(root, relative)
    except FileNotFoundError:
        return None
    except ValueError as exc:
        raise ExportError(str(exc)) from exc


def _existing_at(directory: int, name: str) -> bytes | None:
    try:
        descriptor = os.open(
            name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=directory,
        )
    except FileNotFoundError:
        return None
    try:
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise ExportError(f"export destination must be a regular file: {name}")
        with os.fdopen(descriptor, "rb", closefd=False) as stream:
            return stream.read()
    finally:
        os.close(descriptor)


def write_exports(root: Path, *, apply: bool = False, check: bool = False) -> list[str]:
    """Dry run by default; stage the batch, then atomically replace each changed file."""
    if apply and check:
        raise ExportError("apply and check are mutually exclusive")
    root = root.absolute()
    artifacts = build_exports(root)
    paths = {name: safe_path(root, name) for name in artifacts}
    observed = {name: _existing(root, name) for name in paths}
    changed = [name for name, payload in artifacts.items() if observed[name] != payload]
    if check and changed:
        raise ExportError(f"stale or missing exports: {', '.join(changed)}")
    if not apply or not changed:
        return changed
    with ExitStack() as stack:
        directories = {
            parent: stack.enter_context(_directory_fd(root, parent))
            for parent in sorted({paths[name].parent.relative_to(root) for name in changed})
        }
        staged = []
        try:
            for name in changed:
                fd = directories[paths[name].parent.relative_to(root)]
                staged.append((name, fd, _stage_file(fd, artifacts[name])))
            # Compare the actual publication destinations, not fresh pathname lookups.
            for name, fd, _ in staged:
                if _existing_at(fd, paths[name].name) != observed[name]:
                    raise ExportError(f"export changed during staging: {name}")
            for name, fd, temporary in staged:
                os.replace(temporary, paths[name].name, src_dir_fd=fd, dst_dir_fd=fd)
        finally:
            for _, fd, temporary in staged:
                try:
                    os.unlink(temporary, dir_fd=fd)
                except FileNotFoundError:
                    pass
    return changed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        changed = write_exports(args.root, apply=args.apply, check=args.check)
    except (ExportError, RecordError, ReportError, ValueError, OSError) as exc:
        print(f"export error: {exc}", file=sys.stderr)
        return 1
    print("exports current" if not changed else "\n".join(changed))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
