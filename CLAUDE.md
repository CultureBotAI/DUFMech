# DUFMech Working Agreements

DUFMech curates protein/domain family identity and evidence, not disease records.
Read `docs/records.md`, `docs/reviews.md`, `docs/history.md` and `docs/sources.md`.

- Preserve immutable `data/worklists/` snapshots and their provenance manifests.
- Generated `data/families/` records are rebuilt with `just records --apply`.
  Edit human-owned `curation/families/` overlays, not generated projections.
- Keep seed classification, evidence scoring and reviewed functional claims distinct.
  Missing evidence is not negative evidence; computational or contextual support
  is not an experimental demonstration. Scope assertions to the tested proteins.
- Every curated record needs a canonical history event via `just new-history`.
  Record/category/repository review skills must retain timestamped reports.
- Run `just qc` before publication. Offline checks do not certify live provider
  availability, current upstream taxonomy or source licenses not yet verified.
- Use isolated worktrees for changes. Preserve unrelated work and require fresh
  checks and adversarial review before merging PRs; never bypass a failing gate.
- Shared schemas, validators and governance workflows are synchronized from an
  immutable published CLAW revision. Never edit vendored copies or invent pins.
- Searches proving absence include ignored/hidden files (`rg --no-ignore --hidden`).

Provider-specific research, scientific adoption and source downloads are explicit
actions, not side effects of opening a repository or validating records. Never
commit credentials or restricted full text. Cite primary sources and retain only
the minimal appropriately licensed extract needed to check each assertion.
