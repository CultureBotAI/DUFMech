# Cross-Mech seed-label update, 2026-10-06

`cross-mech-duf-examples-2026-10-06` derives from the October 5 cross-Mech
snapshot and the corrected `interpro-pfam-duf-2026-10-05` worklist introduced
in PR #93. It performs no new Mech scan or UniProt retrieval.

All 16,298 rows retain their family identifiers, source records, proteins,
link bases, and biological metadata. Only `unknown_status` changes: 2,479
rows now carry the corrected worklist's `UNKNOWN_CANDIDATE` seed label.
This propagates the name-based classification correction; it does not add
experimental evidence. The 22 unmatched-name rows remain unchanged.

The October 5 JSON and TSV remain byte-identical to the handoff. The new
manifest records the source snapshot, original worklist, source commit,
source JSON and manifest checksums, target worklist checksum, and changed
row count. Source Mech commits and UniProt lookup times remain those of
the original evidence acquisition.

The derivation replaces each resolved row's `unknown_status` with the value
for its `pfam_id` in the corrected worklist, then writes a new dated artifact
set with `write_cross_mech_snapshot`. Before derivation, both worklist
manifests and the source cross-Mech manifest were verified; the two worklists
were checked to differ only in classification fields. A regression test
compares every source/derived row, verifies the recorded checksums, and
checks every derived seed label against the corrected worklist.

The current report and dashboard select this new snapshot. The October 5
report remains available against its original October 1 worklist.
