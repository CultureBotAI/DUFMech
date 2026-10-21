# Stage 6 Dependency-Aware Infrastructure Implementation Plan (`mech-goal-sequence-20261019`, Cycle 1)

## 1. Frozen Intake Scope & Cutoff

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: Cycle `1`, Stage `6` (`infrastructure`), Revision `1` (`revision-0001`)
- **Supervisor-Frozen Cutoff (`scope_frozen_at`)**: `2026-10-21T18:40:51Z`
- **Source Revision at Freeze (`main`)**: `1795e5229d2d91cfdc34abe9e44838716587c1d8`
- **Frozen Ledger Snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/infra_snapshot.md` (`sha256: a7cbce24f42eff092037df92a8541f651a8eff8e0a184e474b04613a616c9e3e`)
- **Actionable Tasks in Frozen Intake**: `1` (`dufmech-infra-0001`)

| Task ID | Issue | Frozen Status | Priority | Dependencies | Target Disposition |
| --- | --- | --- | --- | --- | --- |
| `dufmech-infra-0001` | [CultureBotAI/DUFMech#333](https://github.com/CultureBotAI/DUFMech/issues/333) | `open` | Medium | None | `resolved` |

## 2. Issue Deduplication & Grouping Audit

Before planning implementation, all open and closed issues in `CultureBotAI/DUFMech` were audited:
- Issue [#333](https://github.com/CultureBotAI/DUFMech/issues/333) (`[infra] Include curated FamilyCuration UniProtKB accessions in protein_examples snapshots and FamilyRecord projection`) already tracks `dufmech-infra-0001` 1-to-1.
- The remaining 40 open issues (`#96` through `#279`) are family-specific curation queue trackers (`PF01886`, `PF01909`, `PF01947`, `PF01954`, `PF01957`, `PF01958`, `PF01976`, `PF02621`, `PF20352`, etc.), not infrastructure tasks in the frozen `INFRA_TASKS.md` intake.

## 3. Dependency-Aware Implementation Plan for `dufmech-infra-0001`

### 3.1 Root Cause & Technical Analysis

1. **Harvesting Curated `FamilyCuration` Accessions (`src/dufmech/protein_examples.py`)**:
   - `dufmech.protein_examples` previously harvested candidate `UniProtKB` accessions only from sibling-Mech cross-references (`data/cross_mech/`), `ProteinTraitsMech` direct family records (`direct_family_candidates`), and `ProteinTraitsMech` sequence registry entries (`registry_candidates`).
   - Meanwhile, `curation/families/PF*.yaml` (`141` overlays at `1795e5229d2d91cfdc34abe9e44838716587c1d8`) contains `262` unique `UniProtKB` accessions across `138` families in `causal_graphs.family_mapping`, `causal_graphs.nodes.grounding`, `assertions`, `assertions.evidence`, `discussions`, and `discussions.evidence`.
   - Crucially, `causal_graphs.nodes.grounding` grounds both target-family carriers (e.g., `UniProtKB:P69423` TatC in `PF00902`, `UniProtKB:P0AAT6` RsfS in `PF02410`) and interacting non-member partner proteins (e.g., `UniProtKB:P37528` PdxT `PF01174` in `PF01680` PdxS; `UniProtKB:Q9Y3I0` RTCB `PF01139` in `PF01951` Archease).
   - Therefore, harvesting from `curation/families/PF*.yaml` must distinguish explicit target-family claims (`causal_graphs.family_mapping` and member-specific `/entry/pfam/PFxxxxx` URLs) from general node/context groundings (`causal_graphs.nodes.grounding`, `assertions`, `discussions`):
     - Confirmed target-family members (`pfam_id in current["pfam_ids"]`) are promoted as `CURATED_MECHANISM_OVERLAY` candidates with immutable `DUFMech` commit/blob provenance (`https://github.com/CultureBotAI/DUFMech/blob/<commit>/curation/families/PFxxxxx.yaml`).
     - Invalid/isoform accessions (`not ACCESSION.fullmatch(accession)`), missing/merged UniProt entries (`current is None`), and mismatched explicit `family_mapping` / Pfam-identity claims are emitted as candidates so `build_rows` surfaces them in `unresolved` (`ISOFORM_OR_INVALID_ACCESSION`, `NO_EXACT_CURRENT_ENTRY`, or `PFAM_NOT_IN_CURRENT_ENTRY`).
     - Valid current UniProt entries grounded only as interacting partner nodes (`current is not None`, `pfam_id not in current["pfam_ids"]`, and not claimed in `family_mapping`) are skipped from target-family candidates and counted in `partner_or_non_member_pairs_skipped`.

2. **Evaluation of `FamilyRecord` (`src/dufmech/schema/dufmech.yaml`) vs Site/JSON Projection Boundary**:
   - `FamilyRecord` (`data/families/PF*.yaml`) is a source-derived projection of `data/worklists/` (`SnapshotProvenance.path` pattern `^data/worklists/[A-Za-z0-9_-]+[.]json$`) combined with human-curated `curation/families/PF*.yaml` overlays.
   - `dufmech.pages.render_site` (`src/dufmech/pages.py`) and `dufmech.site` (`src/dufmech/site.py`) already join the latest verified `data/protein_examples/` snapshot with `FamilyRecord` at site-render time to emit `protein_examples` in `pages/families/PF*.json`, `pages/families/PF*.html`, and `pages/families/PF*.fasta` while enforcing `evidence_scope: FAMILY_MEMBERSHIP_NOT_FUNCTION`.
   - Keeping `data/protein_examples/` joined at the `pages/families/PF*.json` projection layer rather than embedding sequence examples into `data/families/PF*.yaml` avoids rewriting all `8,296` `data/families/PF*.yaml` files whenever a `protein_examples` snapshot refreshes and preserves the strict separation between Pfam family worklist provenance and sequence-example snapshots.

### 3.2 Implementation Steps & Acceptance Criteria

1. **`src/dufmech/protein_examples.py`**:
   - Add `curation_overlay_mentions(repo, pin, families)` to read `curation/families/PF*.yaml` from a pinned 40-hex `DUFMech` commit via `iter_mech_records` and extract `UniProtKB` accessions with section and `family_member_claim` metadata.
   - Add `curation_overlay_candidates(mentions, entries)` to partition harvested mentions into target-family candidates (`confirmed_family_member_pairs` + `unresolved_member_or_lookup_pairs`) vs `partner_or_non_member_pairs_skipped`.
   - Add optional `--dufmech-repo`, `--dufmech-commit`, and `--dufmech-repository-url` flags to `dufmech.protein_examples.main()` and record `dufmech_curation_overlays` scope statistics in snapshot manifests.
2. **`tests/test_protein_examples.py`**:
   - Add unit tests verifying `curation_overlay_mentions` and `curation_overlay_candidates` across confirmed target-family members, skipped partner node groundings, mismatched `family_mapping` claims, `build_rows` / `validate_rows` immutable provenance checks, and non-40-hex commit / out-of-worklist rejection.
3. **`INFRA_TASKS.md` & Workflow Evidence**:
   - Update `dufmech-infra-0001` in `INFRA_TASKS.md` to `status: resolved` with full disposition and evidence paths.
   - Record validation outputs in `validation.md` and `evidence.yaml` (`InfrastructurePlan`), and close Issue `#333` upon PR review and verification.
