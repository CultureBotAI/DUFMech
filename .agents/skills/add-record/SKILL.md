---
name: add-record
description: Discover, review, and onboard new DUF, UPF, or EX_DUF Pfam family records in DUFMech from InterPro/Pfam snapshots or literature curation, preserving provenance, history, and validation gates.
---

# Add or Onboard DUFMech Family Records

Use this skill inside DUFMech when asked to check for and add new DUF/UPF/EX_DUF
Pfam family records from upstream InterPro/Pfam releases, reconcile the retained
worklist against `data/families/PF*.yaml`, or onboard a newly curated family
overlay in `curation/families/PF*.yaml`.

Read the [record contract](../../../docs/records.md),
[sources contract](../../../docs/sources.md),
[history contract](../../../docs/history.md), and the authoritative
[LinkML schema](../../../src/dufmech/schema/dufmech.yaml) before editing. When
onboarding a literature-backed overlay for an existing or newly added `PFxxxxx`
family, also follow [curate-yaml-record](../curate-yaml-record/SKILL.md) and its
[review checklist](../curate-yaml-record/references/review-checklist.md).

## 1. Upstream DUF Discovery and Bounded-Frontier Reconciliation

Before creating or modifying any worklist or family record, pin the candidate
source frontier and exact search scope, then check whether any new DUF, UPF, or
historical unknown-name (`EX_DUF`) Pfam families exist within that frontier
relative to the latest retained worklist snapshot:

1. **Pin local baseline and search ignored/hidden files**:
   - Inspect the latest retained worklist snapshot in
     `data/worklists/interpro-pfam-duf-*.json`, its companion `.manifest.json`,
     and the historical rename table in
     `data/worklists/pfam-previous-unknown-names-*.json` (plus its `.manifest.json`).
   - Search ignored and hidden files (`rg --no-ignore --hidden`), aliases
     (`short_name`, `previous_unknown_names`, `previous_ids`),
     `curation/families/PF*.yaml` overlays, `data/families/PF*.yaml`
     projections, and prior `FALSE_POSITIVE_TEXT_HIT` decisions recorded in
     worklist `.manifest.json` files before declaring any candidate absent.
   - Confirm that every included `PFxxxxx` entry in the latest worklist snapshot
     (`UNKNOWN_CANDIDATE`, `KNOWN_HISTORICAL_DUF`, and `EX_DUF`) has a generated
     canonical projection in `data/families/PFxxxxx.yaml` and is listed in
     `data/families/manifest.json`.
2. **Query live InterPro and EBI Pfam within the bounded frontier**:
   - Query the InterPro Pfam endpoint
     `https://www.ebi.ac.uk/interpro/api/entry/pfam/?search=DUF&page_size=200`
     (including tail pages past the highest retained `PFxxxxx` accession) and
     compare the total entry count and accessions against the latest retained
     `data/worklists/interpro-pfam-duf-*.json` snapshot.
   - Check EBI Pfam FTP (`https://ftp.ebi.ac.uk/pub/databases/Pfam/releases/`)
     for any newer `Pfam*.*/Pfam-A.seed.gz` or `pfamA.txt.gz` release than the
     release recorded in `data/worklists/pfam-previous-unknown-names-*.json`.
   - Run a dry-run reconciliation via `scripts/migrate_exduf_worklist.py`
     (dry-run is the default when `--apply` is omitted):
     ```bash
     uv run --locked python scripts/migrate_exduf_worklist.py \
       --parent-json data/worklists/interpro-pfam-duf-YYYY-MM-DD.json \
       --previous-names-json data/worklists/pfam-previous-unknown-names-YYYY-MM-DD.json \
       --snapshot-date YYYY-MM-DD
     ```
3. **Assign explicit per-candidate dispositions and re-run frontier**:
   - Record an explicit disposition for every evaluated candidate in the
     bounded frontier: `added`, `already_present`, `rejected_with_evidence`
     (such as `FALSE_POSITIVE_TEXT_HIT` lexical matches where neither current
     nor historical Pfam names are `DUF*`/`UPF*`), or `blocked` (when a source
     or prerequisite is unavailable).
   - After any additions, re-run the bounded frontier search to verify that no
     further admissible candidates remain.
   - Report "no new admissible candidate found" strictly within the recorded
     frontier and search scope—never claim global exhaustion of science.
4. **No-op rule when zero new DUFs exist**:
   - If upstream InterPro and EBI Pfam contain zero new DUF/UPF/EX_DUF entries
     (`0 reclassified, 0 added`) and every worklist family already has a matching
     `data/families/PFxxxxx.yaml` projection, **do not write a redundant date-stamped
     worklist snapshot**. Writing a no-op snapshot would invalidate
     `conf/site_source_pins.json` and release-snapshot regression tests without
     adding any scientific or catalog content. Report the exact upstream counts,
     highest `PFxxxxx` accession, per-category dispositions, and zero-diff
     verification result.

## 2. Adding New Seed Family Records from an Upstream Release

When a new InterPro/Pfam release introduces genuinely new `DUF*`, `UPF*`, or
`EX_DUF` (`PFxxxxx`) families not yet present in `data/families/PF*.yaml`:

1. **Refresh the worklist and protein-example snapshots**:
   - Generate the new date-stamped worklist snapshot under `data/worklists/`
     using `scripts/migrate_exduf_worklist.py --apply` (or the worklist
     harvesting workflow in [docs/sources.md](../../../docs/sources.md)) so new
     `PFxxxxx` `DufFamilyRow` entries receive validated `pfam_id`, `short_name`,
     `name`, `interpro_id`, `unknown_status`, `candidate_reasons`,
     `uniprot_protein_count`, `reviewed_protein_count`,
     `unreviewed_protein_count`, `alphafold_count`, `structure_count`,
     `taxonomy_id`, `taxonomy_name`, `description`, `source_url`, and optional
     `previous_unknown_names` fields, while explicit text-search false positives
     (`FALSE_POSITIVE_TEXT_HIT`) are filtered out and recorded in the companion
     `.manifest.json`.
   - If representative proteins or cross-mech mappings changed, refresh
     `data/protein_examples/` and `data/cross_mech/` accordingly.
2. **Project canonical family records**:
   - Run:
     ```bash
     uv run --locked python -m dufmech.records --apply
     ```
   - Confirm that each new `PFxxxxx` family is projected into
     `data/families/PFxxxxx.yaml` and recorded in `data/families/manifest.json`.
   - Never hand-edit `data/families/PFxxxxx.yaml`; it is always generated from
     the worklist, supporting snapshots, history, reviews, and any human overlay
     in `curation/families/PFxxxxx.yaml`.

## 3. Onboarding a New Curated Family Overlay (`curation/families/PFxxxxx.yaml`)

When adding a new curated overlay for a `PFxxxxx` family (promoting a
seed-only record or curating a newly added DUF):

1. **Verify identifier and scope**:
   - Confirm the target `PFxxxxx` accession exists in the latest
     `data/worklists/interpro-pfam-duf-*.json` snapshot and `data/families/PFxxxxx.yaml`.
   - Verify Pfam `short_name`, InterPro entry (`interpro_id`), experimentally
     tested `UniProtKB` accession, and `NCBITaxon` identifier (`taxon`) against
     local snapshots and primary literature. Preserve experimentally tested
     protein and taxon scope: sequence availability and family membership do not
     prove experimentally characterized function.
2. **Author `curation/families/PFxxxxx.yaml` (`FamilyCuration`)**:
   - `FamilyCuration` is validated with a closed schema
     ([src/dufmech/schema/dufmech.yaml](../../../src/dufmech/schema/dufmech.yaml)).
     Use only its allowed top-level slots:
     - `pfam_id` (required, `PF\d{5}`)
     - `curation_status` (required: `UNCURATED`, `IN_PROGRESS`, `REVIEWED`, or `SUPERSEDED`)
     - `review_id` (only when `curation_status: REVIEWED`)
     - `curation_history`
     - `assertions` (list of `FamilyAssertion` objects carrying `function_summary`,
       `mechanism_summary`, `confidence`, `go_terms`, `tested_proteins`,
       `representative_structures`, and `evidence` items with `pmid`/`doi` and
       verbatim `snippet`)
     - `causal_graphs`
     - `discussions`
     - `datasets`
     - `cross_corpus_links`
   - **Enforce the `IN_PROGRESS` vs `REVIEWED` status gate**: New or edited
     curation overlays must use `curation_status: IN_PROGRESS` unless a
     completed review report (`reviews/PFxxxxx.md` or
     `reviews/structured/PFxxxxx.yaml`), `review_id`, and matching `REVIEW`
     history event targeting `data/families/PFxxxxx.yaml` already exist. Never
     auto-promote a record to `REVIEWED` without an independent review artifact.
   - Ground gene or protein nodes in `causal_graphs` with verified
     `UniProtKB:...` accessions matching the experimental organism (`taxon`),
     without grounding non-protein assay readouts or oligonucleotide knockdown
     reagents as proteins.
3. **Record canonical curation history**:
   - Create a real history event under `history/records/PFxxxxx/` using
     `uv run --locked python -m dufmech.history new` (`just new-history`):
     ```bash
     uv run --locked python -m dufmech.history new \
       --kind record \
       --slug PFxxxxx \
       --path curation/families/PFxxxxx.yaml \
       --timestamp YYYY-MM-DDTHH:MM:SSZ \
       --summary "Create PFxxxxx curation overlay" \
       --details "Detailed provenance and evidence summary" \
       --actor-name "Actor Name" \
       --actor-type human \
       --event CREATE \
       --outcome changed
     ```
     (Use `--event EDIT` when updating an existing overlay, and supply `--model`
     and `--agent-tool` when `--actor-type ai_agent`.)
4. **Regenerate projections, causal-graph inventory, and source pins**:
   - Run:
     ```bash
     uv run --locked python -m dufmech.records --apply
     uv run --locked python -m dufmech.causal_graphs --apply
     ```
   - When tracked source roots under `conf/site_source_pins.json` change, follow
     the committed-source workflow in `curate-yaml-record` (`uv run --locked python -m dufmech.site_sources capture --commit FULL_SHA` and `just render`).

## 4. Validation Gates

Run the repository validation suite before finishing:

```bash
uv run --locked python -m dufmech.records --check
uv run --locked python -m dufmech.causal_graphs --check
uv run --locked python -m dufmech.history check
uv run --locked python -m dufmech.reviews check
uv run --locked python -m dufmech.site_sources check
uv run --locked pytest
```
