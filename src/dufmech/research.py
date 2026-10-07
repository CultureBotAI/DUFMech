"""Offline DUF research planning; never a provider runner or scientific finding."""

from __future__ import annotations

import argparse
import base64
import importlib
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

PROFILE = Path("conf/deep_research_provider.yaml")
SIMULATION = "OFFLINE SIMULATION ONLY: dummy availability; no provider verified or called"


def _shared():
    try:
        return importlib.import_module("kg_microbe_research")
    except ImportError as exc:
        raise RuntimeError(
            "Shared research dependency unavailable. Set CLAW_SRC to the approved CLAW src "
            "directory and PYTHONPATH=src:$CLAW_SRC; no local substitute is used."
        ) from exc


def _context(simulate: bool) -> dict[str, Any]:
    shared = _shared()
    # Empty environment and injected probes never inspect credentials or local tools.
    return {
        "environ": {},
        "probe": shared.StaticProbe(executables=frozenset({"claude"}) if simulate else frozenset()),
        "availability": shared.StaticAvailability({"claude_code": ("available", SIMULATION)})
        if simulate else None,
    }


def profile(root: Path):
    shared = _shared()
    result = shared.load_profile(Path(root) / PROFILE)
    if result.mech != "DUFMech":
        raise shared.ProfileError("This adapter requires a DUFMech profile")
    return result


def triage(root: Path, *, focus=None, allow=None, no_paid=False, simulate=False):
    """Rank the canonical catalogue offline; simulation is an explicit rehearsal."""
    shared = _shared()
    loaded = profile(root)
    report = shared.build_report(
        loaded, focus, allow=allow, no_paid=no_paid, **_context(simulate)
    )
    report.update({
        "execution_enabled": False, "simulation": simulate,
        "scope": SIMULATION if simulate else "Offline ranking; provider availability not checked",
        "profile_sha256": loaded.source_sha256,
        "provider_catalogue_sha256": shared.PROVIDER_CATALOGUE_SHA256,
        "triage_contract_sha256": shared.TRIAGE_CONTRACT_SHA256,
    })
    if no_paid:
        from kg_microbe_research.__main__ import no_paid_unsatisfiable_note

        note = no_paid_unsatisfiable_note()
        if note:
            report["no_paid_unsatisfiable"] = note
    return report


def authorize(
    root: Path, *, stage: str, focus=None, allow=None, no_paid=False, simulate=False,
    provider=None, apply=False, acknowledge_usage=False, max_cost=None, override_reason=None,
):
    """Evaluate the shared dry-run gate, while refusing all live authorization."""
    shared = _shared()
    if apply:
        raise shared.PolicyError("DUFMech provider execution is disabled, including simulations")
    plan = shared.plan_stage(
        profile(root), stage, focus=focus, allow=allow, no_paid=no_paid, **_context(simulate)
    )
    decision = shared.authorize(
        plan, provider=provider, apply=False, acknowledge_usage=acknowledge_usage,
        max_cost=max_cost, override_reason=override_reason,
    )
    return {
        **decision.as_dict(), "execution_authorized": False, "simulation": simulate,
        "scope": SIMULATION if simulate else "Offline policy evaluation only",
    }


def scaffold_result(
    root: Path, *, pfam_id: str, question: str, focus=None, allow=None, no_paid=False,
    simulate=False,
):
    """Build a checksum-bound dummy DRY_RUN with no findings and no file writes."""
    shared = _shared()
    if not simulate:
        raise shared.PolicyError("Scaffolding requires explicit --simulate; no availability is verified")
    if not re.fullmatch(r"PF[0-9]{5}", pfam_id):
        raise ValueError("--pfam-id must be a Pfam accession such as PF04149")
    if not question.strip():
        raise ValueError("--question must not be blank")
    root = Path(root).resolve(strict=True)
    profile(root)
    result = shared.build_dry_run_result(
        repository_root=root, profile_path=root / PROFILE,
        target_path=root / "data" / "families" / f"{pfam_id}.yaml",
        target_id=pfam_id, target_label=pfam_id, target_type="DUFMech FamilyRecord snapshot",
        question=f"{SIMULATION}. This is not research findings.\n{question.strip()}",
        focus_name=focus, allow=allow, no_paid=no_paid, **_context(True),
    )
    # Check the retained bytes, not a second read that could disagree with the plan.
    artifact = next(item for item in result["artifacts"] if item["role"] == "TARGET_SNAPSHOT")
    target = yaml.safe_load(base64.b64decode(artifact["content_base64"]))
    if not isinstance(target, dict) or target.get("pfam_id") != pfam_id:
        raise ValueError("Retained target snapshot does not identify the requested Pfam family")
    return result


def _result_path(root: Path, value: str) -> Path:
    relative = Path(value)
    if (relative.is_absolute() or ".." in relative.parts
            or relative.parts[:2] != ("research", "runs") or relative.suffix != ".yaml"):
        raise ValueError("Result path must be repository-relative research/runs/.../*.yaml")
    path = root / relative
    cursor = root
    for part in relative.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise ValueError("Result paths must not traverse symlinks")
    return path


def retain_result(root: Path, result: dict, *, output: str | None = None) -> Path:
    """Append one shared-schema-validated simulation; never overwrite a record."""
    shared = _shared()
    root = Path(root).resolve(strict=True)
    if (result.get("status") != "DRY_RUN"
            or not result.get("plan", {}).get("question", {}).get("text", "").startswith(SIMULATION)):
        raise ValueError("Only explicitly labelled dummy DRY_RUN results may be retained here")
    path = _result_path(root, output) if output else shared.new_result_path(
        root, target_id=result["plan"]["question"]["target"]["target_id"],
        result_id=result["result_id"],
    )
    return shared.write_result(path, result, repository_root=root)


def validate_result(root: Path, result: str, *, verify_snapshots=False):
    root = Path(root).resolve(strict=True)
    return _shared().load_result(
        _result_path(root, result), repository_root=root,
        verify_artifacts=True, verify_snapshots=verify_snapshots,
    )


class _Parser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        self.exit(1, f"{self.prog}: error: {message}\n")


def main(argv: list[str] | None = None) -> int:
    parser = _Parser(description=__doc__, allow_abbrev=False)
    commands = parser.add_subparsers(dest="command", required=True, parser_class=_Parser)
    for command in ("check", "triage", "authorize", "scaffold-result", "validate-result"):
        sub = commands.add_parser(command, allow_abbrev=False)
        sub.add_argument("--root", type=Path, default=Path.cwd())
        if command in {"triage", "authorize", "scaffold-result"}:
            sub.add_argument("--focus")
            sub.add_argument("--allow", action="append")
            sub.add_argument("--no-paid", action="store_true")
            sub.add_argument("--simulate", action="store_true", help=SIMULATION)
        if command == "authorize":
            sub.add_argument("--stage", required=True)
            sub.add_argument("--provider")
            sub.add_argument("--apply", action="store_true", help="Always refused: execution disabled")
            sub.add_argument("--acknowledge-usage", action="store_true")
            sub.add_argument("--max-cost")
            sub.add_argument("--override-reason")
        if command == "scaffold-result":
            sub.add_argument("--pfam-id", required=True)
            sub.add_argument("--question", required=True)
            sub.add_argument("--retain", action="store_true", help="Append the dummy result bundle")
            sub.add_argument("--output", help="Optional repository-relative research/runs YAML")
        if command == "validate-result":
            sub.add_argument("result")
            sub.add_argument("--verify-snapshots", action="store_true")
    args = parser.parse_args(argv)
    shared = None
    try:
        shared = _shared()
        root = args.root.resolve(strict=True)
        common = (
            {key: getattr(args, key) for key in ("focus", "allow", "no_paid", "simulate")}
            if args.command not in {"check", "validate-result"} else {}
        )
        if args.command == "check":
            loaded = profile(root)
            result = {"mech": loaded.mech, "profile_sha256": loaded.source_sha256,
                      "focuses": {name: list(value.stages) for name, value in loaded.focuses.items()},
                      "execution_enabled": False}
        elif args.command == "triage":
            result = triage(root, **common)
        elif args.command == "authorize":
            result = authorize(root, **common, **{
                key: getattr(args, key) for key in (
                    "stage", "provider", "apply", "acknowledge_usage", "max_cost", "override_reason"
                )
            })
        elif args.command == "scaffold-result":
            if args.output and not args.retain:
                raise ValueError("--output requires --retain; default scaffolding writes nothing")
            result = scaffold_result(root, pfam_id=args.pfam_id, question=args.question, **common)
            if args.retain:
                path = retain_result(root, result, output=args.output)
                result = {"path": str(path), "status": "DRY_RUN", "scope": SIMULATION,
                          "execution_authorized": False}
        else:
            checked = validate_result(root, args.result, verify_snapshots=args.verify_snapshots)
            result = {"valid": True, "status": checked["status"], "execution_enabled": False}
        print(json.dumps(result, indent=2))
        if "no_paid_unsatisfiable" in result:
            return 1
        return 3 if args.command == "authorize" else 0
    except (OSError, ValueError, RuntimeError, yaml.YAMLError) as exc:
        print(json.dumps({"error": str(exc), "execution_authorized": False}))
        return 2 if shared is not None and isinstance(exc, shared.PolicyError) else 1


if __name__ == "__main__":
    raise SystemExit(main())
