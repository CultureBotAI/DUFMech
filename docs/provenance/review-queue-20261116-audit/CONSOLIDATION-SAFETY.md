# Read-only consolidation safety review

Date: 2026-11-16. Published main: `a030cca0dae2771e961ae12474c24c47a32b1363`.

The existing 99 captured open PRs are independent payloads. None has even one
changed path byte-identically represented by main or another captured open PR
head. No captured PR head is an ancestor of another target. There is no existing
superseded PR closure candidate.

The 95 review-only PRs add 1,900 distinct files: 950 authoritative YAML reviews
and 950 derived Markdown partners. Their path sets are disjoint, so an exact
additive consolidation on published main is structurally feasible. A new,
durably pushed and validated consolidation would create the preservation basis;
closure messages must call the originals consolidated, not already superseded
or merged. Preserve original remote branches and original commit receipts.

All 950 review IDs are unique and match their directory names. All declare
`scientific_review: false`; 925 retain `seed_only`/`SEED_ONLY` and 25 retain
`needs_curation`/`NEEDS_FOLLOWUP`. All 950 target projection input hashes still
match main. Their seven source revisions are ancestors of published main.
13,311 of 13,312 declared inputs match their recorded source Git blobs. The sole
exception is the #289 correction's prior-review input, created in the recorded
working tree after its base commit: its SHA-256 is exactly preserved in the same
PR payload (`0a72480d392c3228f31aaee43c88307b3c5976d19551851271c47a94a0322109`).
This is not missing review evidence. 1,882 historical context inputs differ from
current main; retain their original source identity and metadata, never restamp
currentness or claim a new scientific assessment.

Consolidation gates:

1. Recheck exact live source heads before copying; use these captured heads as
   immutable provenance and compare all 1,900 destination modes/blobs and hashes.
2. Preserve existing main source/data/schema/history bytes and all original
   review YAML/Markdown bytes. Keep the four non-batch PRs separate.
3. Add only honestly generated checkpoint/provenance artifacts using native
   commands, with their actual capture context. Run full required validators.
4. Independently review the final diff and final head, verify hosted checks and
   exact durable remote head, then close originals as consolidated only once
   their complete content is preserved. No merge or promotion is implied.
5. Leave the other native checkout, untracked review directories, immutable
   ledgers and runtime session untouched. None supplies closure evidence here.

Non-batch PRs #280 and #385 contain distinct scientific overlays and shared
generated export paths, so they cannot be automatically combined or called
superseded. #368 retains unique site source/tests and 8,649 actual changed paths;
the initial GitHub `files` snapshot has only 100, explicitly recorded as partial.
#457 retains four unique inert freshness candidate files and remains outside
scientific review consolidation and runtime adoption.

No structural blocker to the proposed exact-addition consolidation was found.
Native schema/review/checkpoint validation and final-head adversarial review
remain necessary; this inventory does not certify scientific claims or green CI.

The audit enumerates complete committed Git trees independent of gitignore.
It does not infer absence of valuable ignored/untracked local work. All helpers
are read-only with respect to repositories and GitHub. No issue is filed by this
read-only reviewer; no actual code defect was established in this preservation
analysis.
