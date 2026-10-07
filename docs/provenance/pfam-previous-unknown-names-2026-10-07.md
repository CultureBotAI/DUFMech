# Pfam previous unknown-function names, 2026-10-07

`pfam-previous-unknown-names-2026-10-07` lists every Pfam 38.2 family whose previous
identifiers (`#=GF PI`) include a DUF or UPF name. It answers issue #78: names that
sibling Mechs cite, such as DUF1998 or DUF4393, no longer match DUFMech's worklist
because Pfam renamed those families after characterization.

```bash
uv run python scripts/freeze_pfam_previous_names.py \
  --pfam-release 38.2 --out-dir data/worklists --snapshot-date 2026-10-07
```

The script streamed the pinned release file
`https://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam38.2/Pfam-A.seed.gz`
(194,369,799 bytes, `Last-Modified: Thu, 22 Jan 2026 16:03:00 GMT`, SHA-256
`c53a1397f6741c3501f21db2179ad7810d98ddf9f3b3172257bd71ca07ba8c3b`). It kept only
the `#=GF ID`, `AC`, `DE` and `PI` header lines; no alignment was retained.
A canary run of the same command to a scratch directory produced identical rows
before this artifact was written.

| Measure | Count |
| --- | ---: |
| Families scanned | 30,134 |
| Families with any previous identifier | 4,687 |
| Families with a previous DUF/UPF name (rows) | 1,832 |
| Rows whose current name is no longer DUF/UPF | 1,798 |
| Distinct previous DUF/UPF names | 1,840 |
| Rows already in `interpro-pfam-duf-2026-10-05` | 67 |
| Rows outside the worklist | 1,765 |

All eight DUF names in issue #78 resolve:

| Previous name | Current family |
| --- | --- |
| DUF1814 | PF08843 AbiEii |
| DUF1998 | PF09369 MZB |
| DUF262 | PF03235 GmrSD_N |
| DUF4201 | PF13870 CCDC113_CCDC96_CC |
| DUF4263 | PF14082 SduA_C |
| DUF4297 | PF14130 Cap4_nuclease |
| DUF4338 | PF14236 DruA |
| DUF4393 | PF14337 Abi_alpha |

UPF0014, UPF0018, UPF0037 and UPF0265 do not occur: UPF names are UniProt family
nomenclature, not Pfam identifiers.

## Interpretation limits

A former DUF/UPF name records Pfam naming history. A rename usually follows
published characterization of some members, but it is not, by itself, evidence of
function for a family or any particular protein, and this snapshot makes no scoring
or seed-status change. The 1,765 families outside the worklist are candidates for a
separate, explicitly reviewed worklist decision; they are not added here.

## Terms

[InterPro's license page](https://interpro-documentation.readthedocs.io/en/latest/license.html),
checked on 2026-10-07, states that all InterPro, Pfam, PRINTS and SFLD downloadable
data are available under CC0 1.0. Please cite Pfam and InterPro when reusing it.
