# Bounded CI successor to the cycle-v2 preparation receipt

Prepared 2026-11-16 for [#466](https://github.com/CultureBotAI/DUFMech/issues/466)
and [#467](https://github.com/CultureBotAI/DUFMech/issues/467).

The original 2026-11-07 inputs and migration assessment remain unchanged.
Published source `a030cca0dae2771e961ae12474c24c47a32b1363` retains all eight
original candidate inputs and the preparation helper. This append-only assessment
permits one exact CI successor from already published, reviewed source
`397a28bfd597a1142feb1cf23c0cf3c69bc1b323`: `.github/workflows/validate.yaml`
changes from SHA-256 `2c014c50fc76025d6349db367d58df63c0ca85d38f692e5d045b36dfe7c51f15`
to `a34bd89df2b77d653a761ac9dc406b093d92117ce2163572de3b27d17bbded3e`.

The reviewed commit is retained by annotated
`refs/tags/source/dufmech-review-queue-ci-20261116`, object
`0f567927303e5a69f2bb069986b4308c5a9b5a09`, pointing directly to commit
`397a28bfd597a1142feb1cf23c0cf3c69bc1b323`. The exact tag type, object and target
are checked offline, so source retention survives ordinary branch cleanup.
This tag retains source only; it grants no merge or activation authority.

That source adds a durable validation scratch step before validation. It exports
TMPDIR, TMP, TEMP and a separate pytest basetemp below the runner's existing home,
with distinct run and retry identities outside the source checkout. It changes
neither the CLAW checkout pin nor job permissions, events, validation commands
or source/journal guards. The executable regression exercises the actual shell
step and real pytest journal fixtures, including paths containing spaces.

An independent read-only review of the exact #466 source hashes reported 31
passing focused tests, inspected the configured shell and local instructions,
and verified fresh-process controls for the old configuration, checkout-local
scratch and missing pytest export. That scoped review found no remaining defect
in the scratch repair. It did not certify an unchanged adoption receipt against
changed workflow bytes. Hosted run
[43953198684](https://github.com/CultureBotAI/DUFMech/actions/runs/43953198684)
then passed 1,566 tests and failed the old current-byte receipt assertion.
This successor records that narrow provenance transition rather than rewriting
the earlier observation or claiming the hosted run succeeded.

The companion receipt and tests bind the original receipt and migration review
to their historical Git bytes, replay all eight original candidate hashes,
require the other seven current inputs and preparation helper to remain exact,
and bind the sole changed workflow to the reviewed Git blob and new hash.
Extra or missing successor fields or paths, changed revisions, rewritten prior
evidence, unrelated drift and activation claims are rejected. Existing actual
runtime repository/ref, profile, parent/schema and effective-workflow checks
remain required. Future changes need their own reviewed assessment.

`dufmech-infra-0004`, the original migration hold and adoption issue
[#399](https://github.com/CultureBotAI/DUFMech/issues/399) are unchanged.
No activation, native goal input, runtime pin edit, scientific adoption, merge
or deployment was performed by this assessment. Final independent review,
full local QC and a new exact-head hosted canary remain separate validation
steps; this document does not claim they have already completed.
