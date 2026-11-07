"""Prepare the reviewed DUFMech cycle-v2 candidate; issue #399, 2026-11-07.

Purpose: retain a reproducible, dry-run-first workflow adoption, not run a goal.
Issues #400/#401: reject concurrent edits; read immutable release assets.
Inputs: exact published CLAW release, original DUF base, dated issue/PR context.
Outputs: profile, parent snapshots, skills, migration review and hash manifest.
Requires the reviewed CLAW environment. Governance pin-coupling and native sync
must already have completed. No research, host/session input, commit or merge.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import stat
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

RELEASE = "c26f3a0906916f9641a5f82b004b5541ae5fbe52"
BASE = "5642a645349854802748ae387c0e2df121c5e83f"
BRANCH = "feat/cycle-v2-canary-20261107"
REVIEW = "reviews/workflow/adoption/2026-11-07-cycle-v2"
PROFILE = "workflow/mech-workflow.yaml"
LEGACY = "workflow/legacy/mech-workflow-v1.yaml"
ADAPTATION = ".claude/skills/dufmech-evolve-workflow/SKILL.md"
TRIAGE = ".claude/skills/triage-and-resolve-issues/SKILL.md"
GOAL = (
    "Use triage-and-resolve-issues on DUFMech's supervisor-frozen open-issue inventory. "
    "Read every member's evidence, comments and linked open work before grouping family/member/"
    "construct claims, worklist and sequence provenance, and browser/accessibility defects or "
    "proposals. Coordinate with existing curation and infrastructure PRs; do not duplicate them. "
    "Assign one severity:critical/high/medium/low label with reasons and retain stable groups, "
    "plans and every disposition. Resolve all critical/high issues or hold on their blocking "
    "prerequisites; then work the one or two largest eligible remaining groups within the "
    "primary and secondary's single shared four-hour wall-clock budget. Preserve DUF/UPF/EX_DUF "
    "identity, exact protein/construct/residue scope, source rights and uncertainty; a family "
    "assignment or model is not experimental function. Use native maintained writers and "
    "validation, retain the five required evidence outputs, finish the full authorized commit "
    "sequence, and stop for supervisor closure."
)


def digest(content: str | bytes) -> str:
    return hashlib.sha256(content.encode() if isinstance(content, str) else content).hexdigest()


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


OUTPUT_PATHS = (
    PROFILE, LEGACY, "workflow/parent/mech-cycle.yaml", "workflow/parent/workflow.yaml",
    ADAPTATION, TRIAGE, ".github/workflows/validate.yaml",
    f"{REVIEW}/backlog-context.json", f"{REVIEW}/inputs.json", f"{REVIEW}/migration-review.md",
)
INPUT_PATHS = (*OUTPUT_PATHS, "scripts/.vendored_canon_ref",
               "scripts/adhoc/prepare_cycle_v2_canary.py")


def release_blob(claw: Path, relative: str) -> str:
    """Read canonical bytes from the exact release object, never mutable files."""
    return subprocess.check_output(["git", "show", f"{RELEASE}:{relative}"], cwd=claw).decode()


def verify_target(root: Path) -> None:
    from plugins.repository_settings import RepositorySettings

    target = RepositorySettings.from_environment(
        config={"repositories": {"dufmech": str(root)}}, environ={},
    ).get_target("dufmech")
    target.open()
    if target.path != root or git(root, "rev-parse", "HEAD") != BASE:
        raise RuntimeError("Preparation target or base changed")
    if git(root, "branch", "--show-current") != BRANCH:
        raise RuntimeError("Preparation branch changed")


def snapshot_inputs(root: Path, paths: tuple[str, ...]) -> dict[str, bytes | None]:
    """Capture every input/destination, including absence; reject symlink paths."""
    result = {}
    for relative in paths:
        path = root / relative
        for part in (path, *path.parents):
            if part == root:
                break
            if part.is_symlink():
                raise RuntimeError(f"Preparation path is a symlink: {relative}")
        try:
            mode = path.lstat().st_mode
        except FileNotFoundError:
            result[relative] = None
            continue
        if not stat.S_ISREG(mode):
            raise RuntimeError(f"Preparation input is not a regular file: {relative}")
        result[relative] = path.read_bytes()
    return result


def verify_unchanged(root: Path, expected: dict[str, bytes | None]) -> None:
    current = snapshot_inputs(root, tuple(expected))
    changed = [relative for relative in expected if current[relative] != expected[relative]]
    if changed:
        raise RuntimeError("Concurrent preparation input change: " + ", ".join(changed))


def prepare(args: argparse.Namespace) -> dict[str, str]:
    claw = args.claw_root.resolve(strict=True)
    root = args.target_root.resolve(strict=True)
    sys.path.insert(0, str(claw))
    from kg_microbe_skills.catalogue import canonical_regions, render_adapter
    from plugins.repository_settings import RepositoryTarget

    RepositoryTarget("claw", claw, "CultureBotAI/culturebotai-claw").open()
    verify_target(root)
    assert git(claw, "rev-parse", "HEAD") == RELEASE
    if git(claw, "status", "--porcelain=v1"):
        raise RuntimeError("The released CLAW source checkout must be clean")
    assert (root / "scripts/.vendored_canon_ref").read_text().strip() == RELEASE

    original = subprocess.check_output(["git", "show", f"{BASE}:{PROFILE}"], cwd=root).decode()
    old = yaml.safe_load(original)
    profile = yaml.safe_load(original)
    assert old["parent"]["version"] == "1.0.0" and len(old["stages"]) == 6
    parent_source = "src/kg_microbe_workflows/templates/mech-cycle.yaml"
    schema_source = "src/kg_microbe_workflows/schema/workflow.yaml"
    parent = release_blob(claw, parent_source)
    schema = release_blob(claw, schema_source)
    profile.update(schema_version="2.0.0", profile_version="2.0.0")
    profile["parent"].update(version="2.0.0", revision=RELEASE,
                             sha256=digest(parent), schema_sha256=digest(schema))
    for stage in profile["stages"]:
        stage["stage"] += 1
    profile["stages"].insert(0, {
        "stage": 1, "key": "open_issue_triage", "goal_text": GOAL,
        "skill_paths": [ADAPTATION, TRIAGE], "applicability": "enabled",
    })
    for before, after in zip(old["stages"], profile["stages"][1:], strict=True):
        assert {k: v for k, v in before.items() if k != "stage"} == {
            k: v for k, v in after.items() if k != "stage"}

    canonical_adaptation = release_blob(claw, "src/kg_microbe_skills/canonical/evolve-mech-workflow.md")
    existing = (root / ADAPTATION).read_text()
    adaptation = render_adapter(canonical_adaptation, "dufmech", existing=existing)
    adaptation = adaptation.replace("  version: 1.0.0\n", "  version: 2.0.0\n", 1)
    assert canonical_regions(adaptation) == canonical_regions(
        render_adapter(canonical_adaptation, "dufmech"))
    canonical_triage = release_blob(claw, "src/kg_microbe_skills/canonical/triage-and-resolve-issues.md")
    triage = render_adapter(canonical_triage, "dufmech")
    triage += (
        "\n## DUFMech scope\n\n"
        "Read docs/records.md, docs/reviews.md, docs/history.md and docs/sources.md. "
        "Use curation/families overlays and maintained source/freezer code; generated "
        "data/families records are projections. Keep experimental, computational and "
        "contextual evidence distinct, including exact member, construct, sequence-coordinate "
        "and family-domain scope. Missing original-source evidence remains a named gap.\n\n"
        f"The dated adoption context under {REVIEW} is preparation evidence, not the "
        "supervisor's future issue inventory. Use only the actual issue_scope freeze for "
        "membership; reconcile linked PRs and their owners before implementing a group. "
        "Publication authorization, human-review gates and provider-credit permissions "
        "remain explicit.\n"
    )
    issues = json.loads(args.issue_context.read_text())
    prs = json.loads(args.pr_context.read_text())
    assert len(issues["data"]) == 65 and len(prs["data"]) == 47
    context = {
        "purpose": "Dated candidate-design context, never the future stage-1 frozen inventory",
        "issues_observed_at": issues["observed_at"], "prs_observed_at": prs["observed_at"],
        "issues": [{k: issue[k] for k in ("number", "title", "url", "updatedAt", "labels")}
                   for issue in sorted(issues["data"], key=lambda row: row["number"])],
        "open_prs": [{k: pr[k] for k in ("number", "title", "url", "headRefOid")}
                     for pr in sorted(prs["data"], key=lambda row: row["number"])],
    }
    workflow = (root / ".github/workflows/validate.yaml").read_text()
    old_runtime = "adce6ce0d1720635f11268465003cf78f35b2acf"
    assert (workflow.count(old_runtime), workflow.count(RELEASE)) in ((1, 0), (0, 1))
    workflow = workflow.replace(old_runtime, RELEASE)
    desired = {
        PROFILE: yaml.safe_dump(profile, sort_keys=False, allow_unicode=True, width=100),
        LEGACY: original,
        "workflow/parent/mech-cycle.yaml": parent,
        "workflow/parent/workflow.yaml": schema,
        ADAPTATION: adaptation,
        TRIAGE: triage,
        ".github/workflows/validate.yaml": workflow,
        f"{REVIEW}/backlog-context.json": json.dumps(context, indent=2) + "\n",
    }
    inputs = {
        "schema_version": "1.0.0", "prepared_on": "2026-11-07",
        "adoption_issue": "https://github.com/CultureBotAI/DUFMech/issues/399",
        "lane_pr": "https://github.com/CultureBotAI/culturebotai-claw/pull/924",
        "release": {"commit": RELEASE, "tag": "mech-cycle-v2.0.0", "parent_version": "2.0.0"},
        "previous_profile": {"revision": BASE, "path": PROFILE, "sha256": digest(original)},
        "candidate_inputs": {p: digest(text) for p, text in desired.items()},
        "helper": {"path": "scripts/adhoc/prepare_cycle_v2_canary.py",
                   "sha256": digest(Path(__file__).read_bytes())},
        "runtime_activation": "NOT PERFORMED",
        "intel_effective_hashes": "Must be computed and reviewed on the deployment host",
    }
    desired[f"{REVIEW}/inputs.json"] = json.dumps(inputs, indent=2) + "\n"
    desired[f"{REVIEW}/migration-review.md"] = f"""# DUFMech cycle-v2 candidate review

Prepared 2026-11-07 for [adoption #399](https://github.com/CultureBotAI/DUFMech/issues/399).
This is the implementation's scoped source and migration assessment. Independent
final-head PR review is a separate required gate; this file does not claim it
has already happened or grant runtime activation authority.

The candidate uses Claw release `mech-cycle-v2.0.0`, commit `{RELEASE}`, parent
v2.0.0. It depends on approved merge of [Claw #924](https://github.com/CultureBotAI/culturebotai-claw/pull/924)
before this DUFMech PR may merge. The other 13 Mechs retain the common baseline.
`inputs.json` binds the actual profile, parent/schema, local skills, historical
profile, CI runtime pin, dated backlog context and preparation helper by SHA-256.
The reviewed previous profile came from DUFMech `{BASE}` and is retained
byte-for-byte at `{LEGACY}`. Old stage keys, goals, skill bindings and applicability
are unchanged; only their candidate numbers move from 1–6 to 2–7. Infrastructure
policy is unchanged. New stage 1 uses the canonical triage policy without overrides.

## Backlog-derived scope

The preparation snapshot contains 65 open issues and 47 open PRs, before creation
of adoption issue #399. It is dated context, not a claim about future queue size
and not an executable or supervisor-frozen inventory. The actual stage 1 must use
its own complete `issue_scope` freeze, including whatever issues are open then.

Observed themes that inform the local goal are exact-family/member/construct and
mechanistic source limits (issues #204–279), worklist and sequence-example lineage
(#96, #143, #145, #154, #353), and browser/accessibility/claim presentation
(#369–397). These ranges name context, not a frozen group membership or severity
decision. The source snapshot gives the exact members. Existing PRs, including
the queued review batches, site PR #368 and infrastructure PR #387, must be
reconciled by ownership and published evidence before planning overlapping work.
No issue severity, disposition or scientific result is fabricated by adoption.

The new goal requires one evidence-backed severity label per frozen issue,
critical/high resolution first (a real blocker holds the goal), stable groups and
plans, then one shared four-hour wall-clock window for the one or two largest
eligible remaining groups. Exact DUF/UPF/EX_DUF, protein, construct, residue and
source-rights boundaries remain native scientific constraints. No record, source
download, research provider or generated site is changed by this PR.

## Activation and preservation review

The supplied operator observation is cycle 3, v1 stage 5, waiting, with PR #387
held for the user's merge. No Intel runtime was accessed to independently verify
that observation. A PR merge alone is not goal closure. Preserve the active v1
effective snapshot, native goal, six-stage numbering, receipts and evidence.
Only after v1 stages 5 and 6 close verified may the existing supervisor activate
cycle 4 under parent v2 and dispatch `open_issue_triage` as stage 1.

Before any approved activation, Intel must run the reviewed v2 supervisor and
compatible progress readers/publisher. Configure only DUFMech's reviewed
`workflow_next_profile_path`, `workflow_next_parent_path` and
`workflow_next_schema_path`. Other Mechs retain explicit v1 candidate inputs.
Retained byte-identical v1 parent/schema assets in Claw allow the active cycle to
continue while candidate repository paths change. Do not edit the runtime pin.

The operator must compute the old pinned and candidate effective hashes on Intel
and bind them in `workflow_parent_migration`, with reviewer, rationale and this
committed review artifact/hash. Effective objects include source paths, so no
M5 hash is substituted for Intel runtime authority. The candidate profile,
parent/schema and this review artifact must be committed at the verified final
infrastructure closure head. Merely appearing on unrelated newer main is not
sufficient; if final closure lacks them, stop and reconcile through reviewed work.

Before activation, rollback means selecting the retained reviewed v1 candidate
with compatible Claw code, preserving all current evidence. After v2 history or
progress publication, use a reviewed v2-compatible forward fix; never renumber
history, restore stale ledgers or downgrade readers that cannot interpret v2.

## Remaining gates

This PR must pass native `just qc`, exact-release governance/profile validation,
independent adversarial review and required CI. Its merge, the lane merge, Intel
deployment and DUFMech stage-1 execution remain separate approvals. Adoption #399
stays open until stage 1 closes verified with inventory, groups, plans,
dispositions and validation. No other adoption issues or pins advance before that
verified result. This preparation has not run a goal or deployed a supervisor.
"""
    return desired


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--claw-root", type=Path, required=True)
    parser.add_argument("--target-root", type=Path, required=True)
    parser.add_argument("--issue-context", type=Path, required=True)
    parser.add_argument("--pr-context", type=Path, required=True)
    parser.add_argument("--report-dir", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = args.target_root.resolve(strict=True)
    sys.path.insert(0, str(args.claw_root.resolve(strict=True)))
    verify_target(root)
    expected = snapshot_inputs(root, INPUT_PATHS)
    desired = prepare(args)
    if set(desired) != set(OUTPUT_PATHS):
        raise RuntimeError("Preparation output set differs from guarded paths")
    from kg_microbe_skills.catalogue import canonical_regions
    from kg_microbe_workflows import load_effective_workflow
    from kg_microbe_write import ValidatedWriteTransaction
    from plugins.lock_manager import LockManager

    args.report_dir.mkdir(parents=True, exist_ok=True)
    stage = args.report_dir / "candidate-staging"
    for relative, text in desired.items():
        destination = stage / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text)
    effective = load_effective_workflow(stage / "workflow/parent/mech-cycle.yaml", stage / PROFILE,
        "dufmech", schema_path=stage / "workflow/parent/workflow.yaml")
    for item in effective["stages"]:
        for skill in item["skill_paths"]:
            assert (stage / skill).is_file() or (root / skill).is_file(), skill
    assert canonical_regions(desired[TRIAGE])
    transaction = ValidatedWriteTransaction(root, journal_dir=args.report_dir / "write-journal")
    for relative, text in desired.items():
        transaction.stage(relative, text)
    preview = transaction.commit(apply=False)
    (args.report_dir / "profile-preview.diff").write_text(transaction.diff())
    if args.apply:
        with LockManager().lock("dufmech", "cycle-v2-workflow-candidate", timeout=120):
            verify_target(root)
            verify_unchanged(root, expected)
            transaction.commit(apply=True)
    receipt = {
        "created_at": datetime.now(timezone.utc).isoformat(), "applied": args.apply,
        "release": RELEASE, "base": BASE, "profile_version": effective["profile_version"],
        "paths": sorted(desired), "changed": len(preview.changed), "created": len(preview.created),
        "stage_keys": [stage["key"] for stage in effective["stages"]],
        "runtime_activation": "NOT PERFORMED",
    }
    (args.report_dir / "profile-preparation.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
