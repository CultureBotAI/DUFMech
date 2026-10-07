# Offline Research Planning

DUFMech's `conf/deep_research_provider.yaml` defines two domain-owned focuses:
`identity_provenance` and `functional_evidence`. Each has discovery, synthesis
and verification stages. These are questions and priorities for a future review,
not completed research or biological assertions.

`python -m dufmech.research` reuses the published CLAW `kg_microbe_research`
profile validator, provider catalogue, deterministic ranking, immutable plan,
authorization policy, LinkML result schema, provenance replay and append-only
result writer. It does not fork those contracts. The initial adapter was tested
against CLAW `b81580f150d5334841f3eb16434575701607bc81`.
The independently vendored `scripts/deep_research_contract.py` remains unchanged.

## Setup

Use an approved CLAW source checkout and the DUFMech environment. No implicit
sibling-checkout search, dependency installation, credential discovery or network
access occurs. `CLAW_SRC` identifies its `src` directory, not the checkout root.

```bash
export CLAW_SRC=/path/to/approved/culturebotai-claw/src
export PYTHONPATH="$PWD/src:$CLAW_SRC"
export PYTHONDONTWRITEBYTECODE=1
python -m dufmech.research check
python -m dufmech.research triage --focus identity_provenance
python -m pytest tests/test_research.py -q -p no:cacheprovider
```

Every subcommand accepts `--root PATH` **after** the command; it defaults to the
current directory. Profile location is fixed beneath that root. Unknown options,
abbreviated options and missing arguments fail. CLI arguments are passed directly
to argparse, without shell joining or evaluation. Output is JSON.

## Planning Is Not Execution

Normal triage passes an empty credential environment and an empty `StaticProbe`
to the shared library. It ranks every catalogue provider at every stage but does
not claim an available provider. Ambient credentials or installed CLIs do not
change the result. No secret file, dotenv, provider subprocess, billing endpoint,
health probe or PR-shepherd dispatch is used.

The shared b815 result validator independently replays ranking with an empty
credential environment. Unlike planning, that upstream replay performs a local
`shutil.which('claude')` lookup; Cyberian is blocked before its module lookup in
b815. This does not execute a tool or probe its health. Only static fit and order are compared, not
the current machine's availability. This adapter does not replace or monkeypatch
that shared validation behavior.

An explicit `--simulate` supplies a **dummy** ephemeral `claude_code` configuration
and availability view only to exercise the shared planning and dry-run policy
contracts. The reason is labelled `OFFLINE SIMULATION ONLY`; it does not attest
that Claude or any other provider exists, works or is authorized. The catalogue's
`mock` remains a non-executable stub and is not falsely made routable.

```bash
python -m dufmech.research triage --simulate --focus functional_evidence
python -m dufmech.research authorize --simulate --stage discovery
# Exit 3 means permitted dummy dry run, never permission to call a provider.
```

`authorize --apply` is always refused, even with simulation, acknowledgements,
cost ceilings or override reasons. The shared policy still enforces allowlists,
blocked providers, no-paid exclusions, cost ceilings and plan agreement for dry
runs. `--no-paid` is unsatisfiable with the current shared catalogue, not evidence
that a DUF question lacks answers. Repeated `--allow` values use shared alias and
allowlist semantics.

Exit codes: 0 successful check/triage/scaffold/validation, 1 malformed input or
validation failure, 2 policy refusal, 3 permitted offline authorization dry run.
There is no successful live-authorization exit from this adapter. Schema-valid
results are not authorization tokens; the shared plan remains `audit_only`.

## Retained Dummy Results

Preview without writing:

```bash
python -m dufmech.research scaffold-result --simulate --pfam-id PF04149 \
  --question 'Which retained identity and source-provenance checks should be planned?'
```

For an authorized retained rehearsal, add `--retain`. Repository mutations must
be coordinated with CLAW's verified `RepositorySettings` target and the original
`LockManager` `dufmech` lease. The native helper supplies append-only validated
publication, not cross-repository orchestration or user authorization.

```bash
python -m dufmech.research scaffold-result --simulate --retain --pfam-id PF04149 \
  --question 'Which retained identity and source-provenance checks should be planned?'
python -m dufmech.research validate-result research/runs/PF04149/RESULT.yaml \
  --verify-snapshots
```

The first command prints the actual collision-resistant result path. An optional
`--output research/runs/.../NAME.yaml` also requires `--retain`; it never overwrites.
Paths outside `research/runs/`, traversal and symlink publication are refused.
The only target input is `data/families/PFxxxxx.yaml`; its retained `pfam_id` must
match the requested accession. No record, overlay, review or history is changed.

The canonical `DRY_RUN` / `NOT_ASSESSED` bundle embeds exact profile and target
bytes with SHA-256, per-stage rendered questions and query hashes, canonical
catalogue/triage fingerprints, every provider evaluation, and dummy stage
assignments. Every run has `provider_called: false`, `live_authorized: false`
and no usage authorization. The question and simulated status reasons explicitly
label the dummy scope. There are no findings, scientific citations or curated
assertions. `--verify-snapshots` additionally compares current input files;
without it, historically retained bytes remain independently verifiable after
the source files change.

Retaining a bundle does not promote SEEDED/UNSCORED records, verify source licenses,
perform research, or enable provider execution. The existing fleet capability is
`deep_research`, not a new profile/execution pair. Keep it disabled for actual
execution and update its absence reason only through a separately reviewed
canonical change after the adapter is published. No capability flag is changed
by this module.
