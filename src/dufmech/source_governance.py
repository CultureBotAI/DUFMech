"""Offline source, queue and multi-format writer inventory checks.

The catalogue and queue retain CLAW's shared field names and vocabularies.
The writer inventory is deliberately separate from CLAW's YAML-only audit:
call-site evidence is not proof of validation order or transaction safety.
"""

from __future__ import annotations

import argparse
import ast
import csv
import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

import yaml

from dufmech.provenance import check_manifest

CORE_COLUMNS = (
    "source_id", "name", "closes_gap", "use", "redistribution", "access",
    "priority", "status", "verified_on", "url", "rationale",
)
QUEUE_EXTENSIONS = (
    "implementation", "reviewed_on", "review_basis", "script", "artifacts", "license_url",
)
REQUIRED_WHEN_ADOPTED = ("script", "artifacts", "license_url", "review_basis")
CATALOGUE_STATUSES = {"seeded", "candidate", "deferred", "rejected", "superseded", "enrichment"}
QUEUE_STATUSES = {"CANDIDATE", "EVALUATING", "ADOPTED", "BLOCKED", "REJECTED"}
REDISTRIBUTION = {"CC0_OK", "ATTRIBUTION", "SHARE_ALIKE", "NONCOMMERCIAL", "RESTRICTED", "UNVERIFIED"}
ACCESS = {"BULK", "API", "BOTH", "MANUAL", "UNVERIFIED"}
USE = {"SEED", "CURATE_ONLY", "REFERENCE", "LINK_ONLY"}
LICENSE_CLASSES = {
    "CC0-1.0": "CC0_OK", "CC-BY-4.0": "ATTRIBUTION",
    "CC-BY-SA-4.0": "SHARE_ALIKE", "CC-BY-NC-4.0": "NONCOMMERCIAL",
}


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    subject: str
    detail: str

    def render(self) -> str:
        return f"{self.severity.upper()} {self.code} [{self.subject}]: {self.detail}"


def _text(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""


def _iso_date(value: object) -> bool:
    try:
        return date.fromisoformat(value).isoformat() == value
    except (ValueError, TypeError):
        return False


def _url(value: object) -> bool:
    try:
        parsed = urlsplit(_text(value))
        return parsed.scheme in {"https", "http", "ftp"} and bool(parsed.netloc)
    except ValueError:
        return False


def _local_file(root: Path, value: object) -> Path | None:
    text = _text(value)
    path = root / text
    if not text or Path(text).is_absolute() or ".." in Path(text).parts:
        return None
    current = root
    for part in Path(text).parts:
        current = current / part
        if current.is_symlink():
            return None
    if not path.resolve().is_relative_to(root.resolve()):
        return None
    return path if path.is_file() else None


def _load_yaml(path: Path) -> object:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def check_sources(root: Path) -> list[Finding]:
    """Check declared sources against files and queue provenance; never fetch."""
    root = Path(root)
    findings: list[Finding] = []

    def error(code: str, subject: str, detail: str) -> None:
        findings.append(Finding("error", code, subject, detail))

    try:
        blocks = _load_yaml(root / "download.yaml")
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return [Finding("error", "CATALOGUE_READ", "download.yaml", str(exc))]
    if not isinstance(blocks, list) or not blocks:
        return [Finding("error", "CATALOGUE_SHAPE", "download.yaml", "expected a nonempty list")]
    sources: dict[str, dict] = {}
    manifests: set[str] = set()
    adapters: set[str] = set()
    for number, block in enumerate(blocks, 1):
        if not isinstance(block, dict):
            error("CATALOGUE_SHAPE", str(number), "source block must be a mapping")
            continue
        source = _text(block.get("source")) or f"block:{number}"
        for key in (
            "source", "name", "url", "status", "license", "redistribution", "access",
            "license_note", "access_note", "adapter", "writer", "seeder", "review_basis",
        ):
            if not _text(block.get(key)):
                error("MISSING_FIELD", source, key)
        if source in sources:
            error("DUPLICATE_SOURCE", source, "DUFMech uses one block per pipeline")
        sources[source] = block
        for key, allowed in (
            ("status", CATALOGUE_STATUSES), ("redistribution", REDISTRIBUTION), ("access", ACCESS),
        ):
            if _text(block.get(key)) not in allowed:
                error("UNKNOWN_VALUE", source, f"{key}={block.get(key)!r}")
        if not _url(block.get("url")):
            error("BAD_URL", source, "url must be an absolute provider URL")
        if not _iso_date(block.get("reviewed_on")):
            error("BAD_REVIEW_DATE", source, "reviewed_on must be YYYY-MM-DD")
        if block.get("implementation") != "IMPLEMENTED":
            error("IMPLEMENTATION", source, "this catalogue inventories implemented pipelines")
        for key in ("adapter", "review_basis"):
            if not _local_file(root, block.get(key)):
                error("MISSING_ARTIFACT", source, f"{key}: {block.get(key)!r}")
        adapter = _text(block.get("adapter"))
        adapters.add(adapter)
        path = _local_file(root, adapter)
        if path:
            try:
                tree = ast.parse(path.read_text("utf-8"))
                functions = {n.name for n in tree.body if isinstance(n, ast.FunctionDef)}
                if _text(block.get("writer")) not in functions:
                    error("MISSING_WRITER", source, f"{block.get('writer')!r} is not in {adapter}")
            except (OSError, SyntaxError, UnicodeError) as exc:
                error("ADAPTER_READ", source, str(exc))
        script = _text(block.get("seeder"))
        if not re.fullmatch(r"[A-Za-z0-9_][A-Za-z0-9_.-]*\.py", script):
            error("BAD_SEEDER", source, "seeder must be a bare Python filename")
        elif not _local_file(root, f"scripts/{script}"):
            error("MISSING_ARTIFACT", source, f"scripts/{script}")
        terms = _text(block.get("redistribution"))
        license_id = _text(block.get("license"))
        verified = block.get("license_verified_on")
        if terms != "UNVERIFIED":
            if not _iso_date(verified) or not _url(block.get("license_url")):
                error("LICENSE_PROVENANCE", source, "verified terms need a date and primary URL")
            if terms != "RESTRICTED" and LICENSE_CLASSES.get(license_id) != terms:
                error("LICENSE_CLASS", source, f"{license_id!r} does not support {terms!r}")
        elif verified:
            error("LICENSE_PROVENANCE", source, "unverified terms must not carry a verification date")
        if terms in {"UNVERIFIED", "RESTRICTED", "NONCOMMERCIAL"}:
            findings.append(Finding("warning", "LICENSE_REVIEW", source, block.get("license_note", "")))
        artifacts = block.get("artifacts")
        if not isinstance(artifacts, list) or any(not _text(item) for item in artifacts):
            error("ARTIFACT_LIST", source, "artifacts must list manifest paths, or be []")
            artifacts = []
        if _text(block.get("status")) in {"seeded", "enrichment"} and not artifacts:
            error("MISSING_ARTIFACT", source, "in-use source has no declared snapshot manifests")
        for artifact in artifacts:
            path = _local_file(root, artifact)
            if not path or not artifact.endswith(".manifest.json"):
                error("MISSING_ARTIFACT", source, artifact)
                continue
            manifests.add(artifact)
            for issue in check_manifest(path):
                error("MANIFEST_INVALID", source, issue.render())
            if terms == "UNVERIFIED":
                findings.append(Finding("warning", "LEGACY_TERMS_UNRESOLVED", source, artifact))

    # Path.rglob includes ignored files and hidden files, unlike default rg/git inventories.
    expected_adapters = {
        str(p.relative_to(root)) for p in (root / "src/dufmech").glob("*_snapshot.py")
        if p.name != "scoring_snapshot.py"
    }
    if (root / "src/dufmech/snapshot.py").is_file():
        expected_adapters.add("src/dufmech/snapshot.py")
    for adapter in sorted(expected_adapters - adapters):
        error("UNCATALOGUED_ADAPTER", adapter, "freeze adapter is absent from download.yaml")
    for directory in ("data/worklists", "data/cross_mech"):
        for path in sorted((root / directory).rglob("*.manifest.json")):
            relative = str(path.relative_to(root))
            if relative not in manifests and not path.name.startswith("duf-characterization-scores-"):
                error("UNCATALOGUED_ARTIFACT", relative, "snapshot has no source catalogue provenance")

    findings.extend(_check_queue(root, sources))
    return findings


def _check_queue(root: Path, sources: dict[str, dict]) -> list[Finding]:
    findings: list[Finding] = []

    def error(code: str, source: str, detail: str) -> None:
        findings.append(Finding("error", code, source, detail))

    try:
        with (root / "curation/source_queue.tsv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.reader(handle, delimiter="\t", strict=True))
    except (OSError, UnicodeError, csv.Error) as exc:
        return [Finding("error", "QUEUE_READ", "source_queue.tsv", str(exc))]
    columns = rows[0] if rows else []
    required = set(CORE_COLUMNS + QUEUE_EXTENSIONS)
    if len(columns) != len(set(columns)) or set(columns) != required:
        error("QUEUE_COLUMNS", "source_queue.tsv", "expected unique shared and declared columns")
        return findings
    if len(rows) == 1:
        error("EMPTY_QUEUE", "source_queue.tsv", "no source rows")
    seen: set[str] = set()
    for number, values in enumerate(rows[1:], 2):
        if len(values) != len(columns):
            error("BAD_ROW_WIDTH", str(number), f"expected {len(columns)}, got {len(values)}")
            continue
        row = dict(zip(columns, values))
        source = row["source_id"]
        if source in seen:
            error("DUPLICATE_SOURCE_ID", source, f"row {number}")
        seen.add(source)
        for key in required - {"verified_on", "artifacts", "license_url"}:
            if not row[key].strip():
                error("MISSING_FIELD", source, key)
        for key, allowed in (
            ("status", QUEUE_STATUSES), ("redistribution", REDISTRIBUTION),
            ("access", ACCESS), ("use", USE), ("priority", {"1", "2", "3", "4", "5"}),
        ):
            if row[key] not in allowed:
                error("UNKNOWN_VALUE", source, f"{key}={row[key]!r}")
        for key in ("verified_on", "reviewed_on"):
            if row[key] and not _iso_date(row[key]):
                error("BAD_DATE", source, f"{key} must be YYYY-MM-DD")
        block = sources.get(source)
        if not block:
            error("UNCATALOGUED_SOURCE", source, "queue entry has no catalogue block")
            continue
        for queue_key, catalog_key in (
            ("name", "name"), ("redistribution", "redistribution"), ("access", "access"),
            ("url", "url"), ("implementation", "implementation"), ("reviewed_on", "reviewed_on"),
            ("review_basis", "review_basis"), ("verified_on", "license_verified_on"),
            ("license_url", "license_url"),
        ):
            if row[queue_key] != _text(block.get(catalog_key)):
                error("QUEUE_CATALOGUE_MISMATCH", source, queue_key)
        if row["script"] != f"scripts/{block.get('seeder')}":
            error("QUEUE_CATALOGUE_MISMATCH", source, "script")
        artifacts = block.get("artifacts")
        if (isinstance(artifacts, list) and all(isinstance(p, str) for p in artifacts)
                and row["artifacts"].split(";") != artifacts and (row["artifacts"] or artifacts)):
            error("QUEUE_CATALOGUE_MISMATCH", source, "artifacts")
        if row["status"] == "ADOPTED":
            if row["redistribution"] == "UNVERIFIED":
                error("ADOPTED_BUT_UNVERIFIED", source, "terms have not been verified")
            if not row["verified_on"]:
                error("ADOPTED_WITHOUT_A_DATE", source, "missing license verification date")
            for key in REQUIRED_WHEN_ADOPTED:
                if not row[key]:
                    error("ADOPTION_PROVENANCE", source, f"missing {key}")
            if _text(block.get("status")) not in {"seeded", "enrichment"}:
                error("ADOPTION_PROVENANCE", source, "catalogue does not mark source in use")
            if row["use"] == "SEED" and row["redistribution"] in {
                "UNVERIFIED", "RESTRICTED", "NONCOMMERCIAL",
            }:
                error("SEED_UNDER_TERMS_THAT_FORBID_IT", source, row["redistribution"])
        if block.get("status") == "seeded" and row["status"] != "ADOPTED":
            error("ADOPTION_PROVENANCE", source, "seeded catalogue needs adopted queue row")
    for source in sorted(sources.keys() - seen):
        error("MISSING_QUEUE_SOURCE", source, "catalogue source absent from queue")
    return findings


def _call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return _call_name(node.value) + "." + node.attr
    return ""


def _scope_calls(node: ast.AST) -> list[ast.Call]:
    calls: list[ast.Call] = []

    def visit(item: ast.AST) -> None:
        if item is not node and isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            return
        if isinstance(item, ast.Call):
            calls.append(item)
        for child in ast.iter_child_nodes(item):
            visit(child)

    visit(node)
    return calls


def writer_inventory(root: Path) -> tuple[list[dict], list[Finding]]:
    """Inventory AST write sites, including ignored/untracked Python in owned trees.

    Configured helpers are checked against real definitions. Guard evidence is
    reported as calls, never promoted to a claim that execution is safe.
    """
    root = Path(root)
    config = _load_yaml(root / "conf/writer_audit.yaml")
    if not isinstance(config, dict) or config.get("version") != 1:
        raise ValueError("writer_audit.yaml must be a version: 1 mapping")
    helpers = config.get("helpers")
    if not isinstance(helpers, dict) or not helpers:
        raise ValueError("writer audit requires explicit helpers")
    findings: list[Finding] = []
    for name, declaration in helpers.items():
        if (not isinstance(name, str) or not isinstance(declaration, dict)
                or not _text(declaration.get("path")) or not _text(declaration.get("policy"))
                or not isinstance(declaration.get("formats"), list)
                or not declaration["formats"]
                or any(not _text(f) for f in declaration["formats"])):
            raise ValueError(f"invalid writer declaration: {name!r}")
        tests = declaration.get("tests")
        if not isinstance(tests, list) or not tests:
            findings.append(Finding("error", "WRITER_POLICY_PROVENANCE", name, "no policy tests"))
        else:
            for test in tests:
                if not _local_file(root, test):
                    findings.append(Finding("error", "WRITER_POLICY_PROVENANCE", name, str(test)))
    definitions: set[tuple[str, str]] = set()
    rows: list[dict] = []
    for directory in ("src/dufmech", "scripts"):
        for path in sorted((root / directory).rglob("*.py")):
            relative = str(path.relative_to(root))
            tree = ast.parse(path.read_text("utf-8"), filename=relative)
            aliases: dict[str, str] = {}
            for node in ast.walk(tree):
                if isinstance(node, (ast.ImportFrom, ast.Import)):
                    for alias in node.names:
                        aliases[alias.asname or alias.name] = alias.name
            scopes = [tree, *(n for n in ast.walk(tree)
                             if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)))]
            for node in scopes:
                function = getattr(node, "name", "<module>")
                definitions.add((relative, function))
                calls = _scope_calls(node)
                call_names = {aliases.get(_call_name(n.func).rsplit(".", 1)[-1],
                                          _call_name(n.func).rsplit(".", 1)[-1]) for n in calls}
                declaration = helpers.get(function, {})
                if declaration.get("path") != relative:
                    declaration = {}
                missing_calls = set(declaration.get("required_calls", [])) - call_names
                if missing_calls:
                    findings.append(Finding("error", "WRITER_VALIDATION_MISSING", function,
                                            ", ".join(sorted(missing_calls))))
                if declaration.get("apply_default") is False:
                    parameters = list(zip(node.args.kwonlyargs, node.args.kw_defaults))
                    default = next((value for arg, value in parameters if arg.arg == "apply"), None)
                    if not isinstance(default, ast.Constant) or default.value is not False:
                        findings.append(Finding("error", "WRITER_DEFAULT", function,
                                                "keyword-only apply must default to False"))
                evidence: set[str] = set()
                formats: set[str] = set()
                for call in calls:
                    name = _call_name(call.func)
                    leaf = name.rsplit(".", 1)[-1]
                    resolved = aliases.get(leaf, leaf)
                    if resolved in helpers:
                        evidence.add(f"helper:{resolved}")
                        formats.update(helpers[resolved]["formats"])
                    if leaf in {"write_text", "write_bytes", "writerow", "writerows", "write"}:
                        evidence.add(f"call:{leaf}")
                    if name in {"os.replace", "os.rename", "os.link", "shutil.copyfile", "shutil.copy2"}:
                        evidence.add(f"call:{name}")
                    if leaf in {"open", "fdopen"}:
                        mode_args = call.args if name in {"open", "os.fdopen"} else [None, *call.args]
                        mode = mode_args[1] if len(mode_args) > 1 else None
                        mode = next((k.value for k in call.keywords if k.arg == "mode"), mode)
                        if (isinstance(mode, ast.Constant) and isinstance(mode.value, str)
                                and any(c in mode.value for c in "wax+")):
                            evidence.add(f"open:{mode.value}")
                        if name == "os.open" and len(call.args) > 1:
                            flags = {_call_name(n) for n in ast.walk(call.args[1])}
                            if flags & {"os.O_WRONLY", "os.O_RDWR", "os.O_CREAT", "os.O_TRUNC"}:
                                evidence.add("open:os-write-flags")
                    prefix = name.split(".", 1)[0]
                    if (aliases.get(prefix, prefix) in {"json", "yaml"}
                            and leaf in {"dump", "safe_dump"}
                            and (len(call.args) >= 2
                                 or any(k.arg in {"fp", "stream"} for k in call.keywords))):
                        evidence.add(f"serialize:{aliases.get(prefix, prefix)}")
                        formats.add(aliases.get(prefix, prefix))
                if not evidence:
                    continue
                if declaration.get("path") == relative:
                    formats.update(declaration["formats"])
                rows.append({
                    "path": relative, "function": function, "line": getattr(node, "lineno", 1),
                    "formats": sorted(formats) or ["unspecified"],
                    "write_evidence": sorted(evidence),
                    "validation_calls": sorted(call_names & set(config.get("validators", []))),
                    "history_calls": sorted(call_names & set(config.get("history_helpers", []))),
                    "policy": declaration.get("policy", "unclassified"),
                    "policy_tests": declaration.get("tests", []),
                })
    for name, declaration in helpers.items():
        if (declaration["path"], name) not in definitions:
            findings.append(Finding("error", "MISSING_WRITER_HELPER", name, declaration["path"]))
    return rows, findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check DUFMech source governance offline.")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--writers", action="store_true", help="emit JSON inventory; diagnostics on stderr")
    mode.add_argument("--sources-only", action="store_true", help="check catalogue and queue only")
    args = parser.parse_args(argv)
    findings = check_sources(args.root)
    if not args.sources_only:
        try:
            rows, writer_findings = writer_inventory(args.root)
            findings.extend(writer_findings)
            if args.writers:
                print(json.dumps(rows, indent=2, sort_keys=True))
        except (OSError, ValueError, KeyError, TypeError, SyntaxError, yaml.YAMLError) as exc:
            findings.append(Finding("error", "WRITER_AUDIT", "conf/writer_audit.yaml", str(exc)))
    stream = sys.stderr if args.writers else sys.stdout
    for finding in findings:
        print(finding.render(), file=stream)
    errors = sum(f.severity == "error" for f in findings)
    print(f"Source governance (offline): {errors} errors, {len(findings) - errors} warnings", file=stream)
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
