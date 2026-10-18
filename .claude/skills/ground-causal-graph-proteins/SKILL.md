---
name: ground-causal-graph-proteins
description: Review DUFMech family records and ground gene or protein elements of causal graphs with verified UniProtKB protein accessions, preserving provenance, history, and validation gates.
---

# Ground Causal Graph Proteins and UniProt Examples

Use this skill inside DUFMech to review curated family records (`curation/families/PF*.yaml`),
audit protein example coverage (`data/protein_examples/`), and ground gene or protein
elements in `causal_graphs` with verified `UniProtKB:...` accessions.

Read the [record contract](../../../docs/records.md),
[history contract](../../../docs/history.md), and the authoritative
[LinkML schema](../../../src/dufmech/schema/dufmech.yaml) before editing.

## 1. Scope and Audit

1. Inspect all family curation overlays (`curation/families/PF*.yaml`), generated family
   projections (`data/families/PF*.yaml`), and retained protein example snapshots
   (`data/protein_examples/`).
2. For each family overlay:
   - Check whether tested family members and discussion examples cite verified
     `UniProtKB:...` accessions consistent with `evidence/PFxxxxx/`, `data/worklists/`,
     and `data/protein_examples/`.
   - Inspect every causal graph in `causal_graphs` (`id`, `taxon`, `family_mapping`,
     `scope`, `context`, `limitations`, `evidence`, and `nodes`).
3. Identify causal graph nodes representing specific genes, proteins, constructs,
   protein complexes, or enzymatic/binding activities that lack `UniProtKB:...`
   entries in `grounding`:
   - `PERTURBATION` nodes: gene knockouts, deletions, transposon insertions,
     RNAi/CRISPR knockdowns, complementation/rescue constructs, point mutants,
     truncations, or purified protein additions/omissions.
   - `ACTIVITY` nodes: catalytic, binding, transport, or regulatory activities
     of the tested DUF protein or a specific named partner/target enzyme.
   - `STATE` nodes: abundance, localization, complex assembly, stability, or
     post-translational modification state of a specific protein or protein complex.
   - `PROCESS` or `PHENOTYPE` nodes: only when the node specifically denotes
     synthesis, translation, maturation, or turnover of a named protein product
     (for example, mitochondrial translation of a specific subunit).

## 2. Verification Rules for UniProtKB Grounding

Every `UniProtKB:...` grounding added to a causal graph node must be verified
against the graph's exact experimental system:

1. **Match the graph's organism (`taxon`) and strain**:
   - Confirm that the `UniProtKB` entry belongs to the exact `NCBITaxon:...` declared
     on the causal graph (or to the explicitly stated heterologous source organism when
     a node represents an exogenous/complementation protein construct from another
     taxon, such as human `TACO1` complementing a mouse model or an *E. coli* library
     host expressing a bacteriophage or metagenomic protein).
2. **Use authoritative local and upstream sources**:
   - First check the graph's own `family_mapping`, `scope`, `context`, and sibling
     graphs in the same `curation/families/PFxxxxx.yaml` overlay.
   - Check retained evidence extracts in `evidence/PFxxxxx/` (such as
     `uniprot-*-identity.txt` and paper extracts) and `data/protein_examples/`.
   - When a named partner, substrate, target, or co-perturbed gene/protein in the
     paper does not yet have its accession listed in the overlay, verify the exact
     gene symbol, locus tag, organism, and protein identity against UniProtKB before
     adding `UniProtKB:<accession>`.
3. **Respect explicit boundaries and negative evidence**:
   - Never guess or fabricate a `UniProtKB` accession.
   - Do not assign `UniProtKB:...` when the protein sequence exists only in `UniParc`
     or `NCBIProtein` and has no active UniProtKB entry (keep `NCBIProtein:...` and
     `UniParc:...` groundings instead).
   - Do not collapse unspecified paralogs, polyclonal antibody targets (for example,
     generic "soluble actin" or "tubulin" when `family_mapping` or `limitations`
     explicitly state no single isoform accession was identified), or commercial
     reagents from uncharacterized sources into a guessed accession.
   - When a node represents a multi-gene perturbation (such as a double knockout)
     or a defined multi-protein complex, include all verified component `UniProtKB:...`
     accessions alongside any existing complex/process terms.
   - Pure chemical entities (`CHEBI:...`), generic cellular processes (`GO:...`),
     and organismal/clinical phenotypes without a specific single-protein identity
     should retain their ontology groundings without forcing a protein accession.

## 3. Authoring, History, and Projection Workflow

1. **Edit only human-owned overlays**:
   - Apply narrow, text-preserving edits to `curation/families/PFxxxxx.yaml`.
   - Preserve all existing `grounding` CURIEs (`GO:...`, `CHEBI:...`, `EC:...`,
     `Pfam:...`, `InterPro:...`, `NCBITaxon:...`, `WormBase:...`, `NCBIProtein:...`,
     `UniParc:...`, `PDB:...`, etc.) and append verified `UniProtKB:...` CURIEs
     without duplicates.
   - Never hand-edit `data/families/PFxxxxx.yaml`, `curation_events`, or
     `reports/causal_graphs/inventory.json`.
2. **Append canonical curation history**:
   - For every modified `curation/families/PFxxxxx.yaml` overlay, record a real
     `EDIT` event in `history/records/PFxxxxx/` using `just new-history`
     (`uv run --locked python -m dufmech.history new`) with the actual UTC start
     timestamp, agent/model metadata, target `curation/families/PFxxxxx.yaml`,
     `--event EDIT`, `--outcome changed`, and a clear summary of the added
     `UniProtKB` causal-graph node groundings.
3. **Regenerate projections and inventories**:
   - Run `uv run --locked python -m dufmech.records --apply` (`just records --apply`)
     to regenerate `data/families/PFxxxxx.yaml` and update `.records-manifest.json`.
   - Run `uv run --locked python -m dufmech.causal_graphs --apply`
     (`just causal-graphs --apply`) to refresh `reports/causal_graphs/inventory.json`.

## 4. Validation Gates

After updating overlays, history, projections, and the causal graph inventory, run:

```bash
uv run --locked python -m dufmech.records --check
uv run --locked python -m dufmech.causal_graphs --check
uv run --locked python -m dufmech.history check
uv run --locked python -m dufmech.reviews check
uv run --locked pytest
```

Report the number of families reviewed, overlays updated, causal graphs and nodes
newly grounded with `UniProtKB:...` accessions, history events recorded, and any
nodes intentionally left without `UniProtKB` grounding due to UniParc-only status
or unverified isoform identity.
