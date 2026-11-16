# Retained review queue consolidation, 2026-11-16

This inventory and helper support [CI issue #459](https://github.com/CultureBotAI/DUFMech/issues/459)
and [queue issue #460](https://github.com/CultureBotAI/DUFMech/issues/460).
They preserve the original bytes of 950 review bundles from 95 review-only PRs:
1,900 YAML/Markdown files totaling 43,580,615 bytes. They do not reassess the
reviews, promote records, close research gaps or change scientific claims.

The [public source index](review-queue-20261116.json) records each PR number,
exact head, observed base, computed merge base, and every added file's Git mode,
blob identifier, SHA-256 and byte count. Each source PR's complete Git delta is
exactly its 20 indexed additions. The inventory contains no local machine paths
or private operational history. All original review timestamps, source references,
scope, verdicts and scientific-review declarations remain unchanged.

## Reproduce or verify

Use a separately authorized, isolated DUFMech worktree with the source commit
objects available. Resolve and validate the repository through CLAW's
`RepositorySettings`, inspect local changes and hold the `dufmech`
`LockManager` lease for application. The helper itself checks Git identity and
the public inventory; it does not centrally enforce authorization or acquire a
second lock.

From the worktree, set `REVIEW_ROOT` to its explicit absolute path:

```bash
uv run --locked python scripts/adhoc/consolidate_review_queue_20261116.py \
  --root "$REVIEW_ROOT" --inventory docs/provenance/review-queue-20261116.json
uv run --locked python scripts/adhoc/consolidate_review_queue_20261116.py \
  --root "$REVIEW_ROOT" --inventory docs/provenance/review-queue-20261116.json --apply
uv run --locked python scripts/adhoc/consolidate_review_queue_20261116.py \
  --root "$REVIEW_ROOT" --inventory docs/provenance/review-queue-20261116.json --verify
```

The default command validates every source and destination without writing.
`--apply` validates the complete set, stages all missing bytes under the
repository's ignored `.temp/`, and exclusively creates only indexed files.
Existing identical files are accepted; different bytes, executable destinations,
symlinks, incomplete pairs, duplicate paths and unexpected PR changes are refused.
A failed creation rolls back only its own unchanged files; it never removes an
unrelated destination. Empty directories may remain after a failed attempt.
Application is idempotent and `--verify` requires all 1,900 persisted files to
match their original Git blobs. The JSON receipt binds the exact inventory hash
and reports byte/file counts; retain it with the actual run evidence.

No YAML parser or serializer touches the reviews. The helper performs no network
access, research, Git commit/tag/merge, source-pin capture, Pages rendering or
deployment. Keep every source head and referenced historical object available.

## Publication boundary

Consolidation is preparation. Native review validation, independent adversarial
review and complete QC remain necessary. The site source inventory must bind a
real retained checkpoint, followed by native capture and rendering. An unchanged
historical review is not an independently completed new scientific review. The
scientific PRs #280 and #385, website PR #368 and freshness draft #457 are outside
this 95-PR inventory. No merge, release, deployment or runtime adoption follows
from this helper or its receipt.
