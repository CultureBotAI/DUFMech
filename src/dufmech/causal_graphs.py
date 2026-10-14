"""Native graph integrity checks and a whole-corpus inventory, not a scientific review."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from contextlib import nullcontext
from graphlib import CycleError, TopologicalSorter
from pathlib import Path

INVENTORY_PATH = "reports/causal_graphs/inventory.json"


def validate_graphs(graphs: list[dict]) -> None:
    """Check references and semantics after closed-schema validation."""
    graph_ids = [graph["graph_id"] for graph in graphs]
    if len(set(graph_ids)) != len(graph_ids):
        raise ValueError("duplicate graph_id")
    for graph in graphs:
        for key in ("title", "scope", "context", "family_mapping", "limitations"):
            if not graph[key].strip():
                raise ValueError(f"causal graph requires nonempty {key}")
        nodes = [node["node_id"] for node in graph["nodes"]]
        if len(nodes) != len(set(nodes)):
            raise ValueError("duplicate node_id in causal graph")
        if any(not node["label"].strip() for node in graph["nodes"]):
            raise ValueError("causal node requires nonempty label")
        edges = graph["edges"]
        edge_ids = [edge["edge_id"] for edge in edges]
        if len(edge_ids) != len(set(edge_ids)):
            raise ValueError("duplicate edge_id in causal graph")
        relations = [(e["subject"], e["predicate"], e["object"]) for e in edges]
        if len(relations) != len(set(relations)):
            raise ValueError("duplicate causal relation in a single graph context")
        used = set()
        topology = TopologicalSorter()
        for edge in edges:
            if edge["subject"] not in nodes or edge["object"] not in nodes:
                raise ValueError("dangling causal edge endpoint")
            used.update((edge["subject"], edge["object"]))
            topology.add(edge["object"], edge["subject"])
            if not edge["mechanism"].strip():
                raise ValueError("causal edge requires nonempty mechanism")
            if edge["support"] == "OBSERVED" and edge["evidence_kind"] != "EXPERIMENTAL":
                raise ValueError("OBSERVED causal effects require EXPERIMENTAL evidence")
        if used != set(nodes):
            raise ValueError("orphan causal node without an edge")
        try:
            topology.prepare()
        except CycleError as exc:
            if not graph.get("feedback_explanation", "").strip():
                raise ValueError("cyclic causal graph requires feedback_explanation") from exc
        observed = [e for e in edges if e["support"] == "OBSERVED"]
        if graph["scope_status"] == "MECHANISTIC" and not any(
            edge["directness"] == "DIRECT" for edge in observed
        ):
            raise ValueError("MECHANISTIC graph requires a directly observed experimental step")
        if graph["scope_status"] == "PHENOTYPIC" and not observed:
            raise ValueError("PHENOTYPIC graph requires an observed experimental effect")
        if graph["scope_status"] == "HYPOTHETICAL" and observed:
            raise ValueError("HYPOTHETICAL graph cannot conceal observed effects")


def inventory(records: list[dict]) -> dict:
    """Account for every validated family without equating graph presence with review."""
    from dufmech.reviews import record_content_digest

    rows = []
    for record in sorted(records, key=lambda item: item["pfam_id"]):
        graphs = record.get("causal_graphs", [])
        rows.append({
            "pfam_id": record["pfam_id"], "name": record["short_name"],
            "record_digest": record_content_digest(record),
            "graph_count": len(graphs),
            "edge_count": sum(len(g["edges"]) for g in graphs),
            "scope_statuses": sorted({g["scope_status"] for g in graphs}),
            "curation_status": record["curation_status"],
            "graph_state": "PRESENT" if graphs else "ABSENT",
        })
    ids = [row["pfam_id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate Pfam family in causal inventory")
    return {
        "kind": "structural_inventory_not_scientific_review",
        "records": len(rows),
        "graph_states": dict(sorted(Counter(row["graph_state"] for row in rows).items())),
        "families": rows,
    }


def write_inventory(root: Path, *, apply: bool = False, check: bool = False) -> dict:
    """Check or explicitly refresh the derived inventory without changing records."""
    from dufmech.records import _publish_projection, _writer_lock, load_records, safe_path

    if apply and check:
        raise ValueError("--apply and --check are mutually exclusive")
    root = root.absolute()
    with _writer_lock(root) if apply else nullcontext():
        path = safe_path(root, INVENTORY_PATH)
        if path.exists() and not path.is_file():
            raise ValueError("causal inventory must be a regular file")
        previous = path.read_bytes() if path.exists() else None
        result = inventory(load_records(root))
        payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
        if previous != payload:
            if check:
                raise ValueError(f"stale or missing {INVENTORY_PATH}; run just causal-graphs --apply")
            if apply:
                _publish_projection(root, path, payload, previous)
    return result


def main(argv: list[str] | None = None) -> int:

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="reject retained inventory drift")
    mode.add_argument("--apply", action="store_true", help="refresh the retained inventory")
    args = parser.parse_args(argv)
    try:
        result = write_inventory(args.root, apply=args.apply, check=args.check)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"causal-graphs: {exc}\n")
    if args.check or args.apply:
        print(f"{'Verified' if args.check else 'Refreshed'} {result['records']} family inventory rows")
    else:
        print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
