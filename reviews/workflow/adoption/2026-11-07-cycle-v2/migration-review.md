# DUFMech cycle-v2 candidate review

Prepared 2026-11-07 for [adoption #399](https://github.com/CultureBotAI/DUFMech/issues/399).
This is the implementation's scoped source and migration assessment. Independent
final-head PR review is a separate required gate; this file does not claim it
has already happened or grant runtime activation authority.

The candidate uses Claw release `mech-cycle-v2.0.0`, commit `c26f3a0906916f9641a5f82b004b5541ae5fbe52`, parent
v2.0.0. It depends on approved merge of [Claw #924](https://github.com/CultureBotAI/culturebotai-claw/pull/924)
before this DUFMech PR may merge. The other 13 Mechs retain the common baseline.
`inputs.json` binds the actual profile, parent/schema, local skills, historical
profile, CI runtime pin, dated backlog context and preparation helper by SHA-256.
The reviewed previous profile came from DUFMech `5642a645349854802748ae387c0e2df121c5e83f` and is retained
byte-for-byte at `workflow/legacy/mech-workflow-v1.yaml`. Old stage keys, goals, skill bindings and applicability
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
