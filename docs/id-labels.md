# Offline Pfam ID/Label Validation

The label index is **derived reference data**, not a new ontology or an
independent scientific authority. Its authority is the verified, frozen
InterPro/Pfam worklist identified by the retained source hashes. It contains
only Pfam identifiers and their verbatim source names. It adds no relationships,
functional assertions, synonyms, or ontology mappings. Generated or curated
family records never supply its labels.

`conf/id_labels/pfam.obo` is a real local OBO index consumed by OAK's
`simpleobo` adapter. `conf/id_labels/provenance.json` records the source JSON
and manifest hashes, source identity, index hash, entity count and scope.
Generation selects the same latest dated worklist as the native record pipeline
and verifies its JSON, TSV and companion manifest through `load_score_input`.
It sorts identifiers and introduces no wall-clock timestamps. Reproduction
must match both generated files byte for byte.

## Commands

DUF and OAK intentionally use **separate locked runtimes**. DUF's native ShEx
parser and OAK's transitive dependencies require incompatible `chardet` versions.
Do not lower the native ShEx pins or override incompatible dependencies. The
native generator has no OAK import. Use a published CLAW checkout with its own
locked dependencies installed; `CLAW_ROOT` must identify that checkout.
For standalone commands below, set `DUF_ROOT` to DUF's absolute repository path.

Run from the DUF repository root:

```bash
uv run --locked python -m dufmech.id_labels --apply
uv run --locked python -m dufmech.id_labels --check-index
uv run --locked python -m dufmech.id_labels --check --claw-root "$CLAW_ROOT"
```

`--apply` only regenerates the two derived reference files. It never edits
family records, overlays, evidence, reviews or history. Default operation and
`--check` are read-only for DUF inputs. The isolated `uv` invocation may synchronize
CLAW's environment from its lock, offline. `--check-index` returns
`REFERENCE_VERIFIED`, never an OAK PASS. Regenerate after adopting a newer verified
snapshot; the check refuses an index from an older source.

The helper copies the exact captured inputs into a private temporary repository,
verifies them there, and invokes the unmodified governed CLI in enforce mode
against that copy. This binds OAK's actual reads to the verified bytes even if an
original path is temporarily replaced and restored. A direct invocation below
illustrates the isolated runtime, but is not the complete native adoption gate:

```bash
uv run --project "$CLAW_ROOT" --locked --offline python -I -B \
  "$DUF_ROOT/scripts/validate_id_label_correspondence.py" \
  -c "$DUF_ROOT/conf/id_label_targets.yaml"
```

The absolute script path determines the shared validator's repository root;
there is no shared `--repo-root` option. `-I` isolates Python imports from DUF's
native package and `PYTHONPATH`; no DUF LinkML code runs inside OAK's process.
That script loads the real OAK adapter and reads all family
YAML files with `pairs: [[id, name]]`, canonical-label policy and error severity.
No Pfam prefix is ignored and no label waiver is allowed. `interpro_id` is not
paired with a Pfam label: it is a separate identifier without a corresponding
InterPro label in the native schema.

All captured inputs use descriptor-confined, nonblocking regular-file reads,
limited to 64 MiB per file; symlinks and FIFOs are rejected. The native source
verifier also receives private copies of its captured JSON/TSV/manifest companions.
Before invocation the helper verifies the generated index and provenance,
the complete frozen-source record inventory and root record identifiers.
After invocation it requires exactly
one `OK_CANONICAL` result per expected family, with no skips or other verdicts,
and checks both private snapshot and original input bytes/inventory for changes.
The receipt includes the snapshot fingerprint, actual temporary command/cwd and
original repository root. The private copy is removed afterward; its recorded
command is an audit trail, not a persistent path to rerun.
Bad labels, missing or empty references, missing records and skipped pairs
fail. Counts are derived from the verified snapshot, not hard-coded to 6,532.

The shared script alone permits `SKIPPED_EMPTY_ADAPTER` with exit zero, and its
`--report` mode is diagnostic-only and always exits zero. Therefore neither
bare exit zero nor a report-mode run is this repository's adoption gate. Use
the helper for the complete gate. The normal vendored-sync check separately
verifies the shared script's authority; do not edit its governed copy.

These checks establish correspondence to a retained snapshot. They do not
check the current live Pfam catalogue, validate unmodeled ontology groundings,
prove a biological function, or promote a `SEEDED` record to scientific review.
Native record/schema/provenance and review/history checks remain necessary.

## Separate Runtime Regression

Native tests need no OAK installation. They exercise deterministic reproduction,
hash/provenance checks, inventory checks and rejection of empty/skipped results.
The separate regression is mandatory for OAK adoption, not a skipped native test:

```bash
uv run --locked python -m pytest tests/test_id_labels.py -q
uv run --project "$CLAW_ROOT" --locked --offline python -I -B \
  "$DUF_ROOT/tests/test_id_labels.py" --oak-regression --repo-root "$DUF_ROOT"
```

The standalone harness imports no DUF modules, verifies exact entity/label
round trips through genuine OAK, runs the unchanged CLI against the complete
retained corpus, and tests mismatch, missing ID, missing/empty label, missing
target and empty adapter behavior on disposable copies. Its validator children
install a network-denying audit hook. The helper rejects the shared CLI's
permitted empty-adapter skip rather than treating it as success.

## Future Scientific Capabilities

METPO proposals and causal coverage remain disabled: the current seeded corpus
does not supply curated phenotype proposals or directed causal mechanisms.
A real METPO proposal
needs a curated microbial phenotype or mechanism claim, a demonstrated gap
against the retained release and pending proposals, justified parents,
definitions and citations, and a nonempty reviewed ROBOT cohort under the
existing shared proposal contract. Pfam family names alone are not proposals.

Causal coverage needs explicitly curated directed endpoints, predicates,
scoped evidence and native schema/validation support for the shared
`graph_list` shape. Similarity, membership, source citations and research-plan
links are not causal mechanisms. Empty graph slots or proposal templates do
not establish adoption. These capabilities are pending scientific need and
implementation, not permanently inapplicable to DUF mechanism curation.
