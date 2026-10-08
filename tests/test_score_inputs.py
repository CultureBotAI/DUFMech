from __future__ import annotations

import copy
import hashlib
import json
from collections import Counter
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path

import pytest

from dufmech import score_inputs as inputs
from dufmech.reclassify import prepare_reclassification, reclassify_snapshot
from dufmech.scoring_cli import load_json_rows, main
from dufmech.scoring_snapshot import write_score_snapshot
from dufmech.worklist import DufFamilyRow
from tests.test_alphafold_snapshot import alphafold_row
from tests.test_cath_snapshot import cath_row
from tests.test_cdsearch_snapshot import cdsearch_row
from tests.test_efi_gnt_snapshot import efi_gnt_row
from tests.test_eggnog_snapshot import eggnog_row
from tests.test_jgi_img_snapshot import jgi_img_row
from tests.test_member_snapshot import joined_row
from tests.test_mgnify_snapshot import mgnify_row
from tests.test_ncbifam_snapshot import ncbifam_row
from tests.test_pdbe_kb_snapshot import pdbe_row
from tests.test_quickgo_snapshot import quickgo_row
from tests.test_rcsb_snapshot import rcsb_row
from tests.test_rhea_snapshot import rhea_row
from tests.test_scoring_snapshot import score_row
from tests.test_stringdb_snapshot import stringdb_row
from tests.test_threedbeacons_snapshot import threedbeacons_row

DATE = "2026-10-01"
NOW = datetime(2026, 10, 1, tzinfo=timezone.utc)


def seed(pfam="PF01519"):
    return DufFamilyRow(
        pfam_id=pfam, short_name="DUF16", name="Domain of unknown function DUF16",
        interpro_id="IPR002862", unknown_status="UNKNOWN_CANDIDATE",
        candidate_reasons=("short_name_matches_duf",), proteins=1, matches=1, proteomes=1,
        taxa=1, structures=0, alphafold_models=1, domain_architectures=1,
        description="Fixture seed for input-integrity tests.",
    )


PRODUCERS = [
    ("worklist", inputs.worklist.write_worklist_snapshot, seed),
    ("members", inputs.members.write_member_uniref_snapshot, joined_row),
    ("alphafold", inputs.af.write_alphafold_snapshot, alphafold_row),
    ("cath", inputs.cath.write_cath_snapshot, cath_row),
    ("cdsearch", inputs.cdd.write_cdsearch_snapshot, cdsearch_row),
    ("efi_gnt", inputs.efi.write_efi_gnt_snapshot, efi_gnt_row),
    ("eggnog", inputs.egg.write_eggnog_snapshot, eggnog_row),
    ("jgi_img", inputs.img.write_jgi_img_snapshot, jgi_img_row),
    ("mgnify", inputs.mg.write_mgnify_snapshot, mgnify_row),
    ("ncbifam", inputs.ncb.write_ncbifam_snapshot, ncbifam_row),
    ("pdbe_kb", inputs.pdbe.write_pdbe_kb_snapshot, pdbe_row),
    ("quickgo", inputs.go.write_quickgo_snapshot, quickgo_row),
    ("rcsb", inputs.rcsb.write_rcsb_snapshot, rcsb_row),
    ("rhea", inputs.rhea.write_rhea_snapshot, rhea_row),
    ("stringdb", inputs.string.write_stringdb_snapshot, stringdb_row),
    ("threedbeacons", inputs.beacons.write_threedbeacons_snapshot, threedbeacons_row),
]


def freeze(writer, rows, directory):
    manifest = writer(rows, directory, snapshot_date=DATE, generated_at=NOW)
    return directory / manifest["files"]["json"]["path"]


def frozen_seed(directory):
    return freeze(inputs.worklist.write_worklist_snapshot, [seed()], directory)


def rewrite_manifest(path, change):
    manifest_path = path.with_suffix(".manifest.json")
    manifest = json.loads(manifest_path.read_text())
    change(manifest)
    manifest_path.write_text(json.dumps(manifest))


def refresh_file_entry(path, suffix):
    raw = path.with_suffix("." + suffix).read_bytes()
    rewrite_manifest(path, lambda m: m["files"][suffix].update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest()))


@pytest.mark.parametrize("role,writer,row", PRODUCERS, ids=[p[0] for p in PRODUCERS])
def test_each_native_producer_matches_its_verified_role(tmp_path, role, writer, row):
    path = freeze(writer, [row()], tmp_path)
    loaded = inputs.load_score_input(path, role)
    assert len(loaded.rows) == 1
    assert loaded.provenance["validation_state"] == "verified"
    assert loaded.provenance["sha256"] == hashlib.sha256(path.read_bytes()).hexdigest()
    assert loaded.provenance["bytes"] == path.stat().st_size
    manifest = path.with_suffix(".manifest.json")
    assert loaded.provenance["manifest_sha256"] == hashlib.sha256(manifest.read_bytes()).hexdigest()
    assert loaded.provenance["manifest_bytes"] == manifest.stat().st_size


def test_valid_multisource_fixture_preserves_scores_and_all_input_provenance(tmp_path):
    source = tmp_path / "sources"
    worklist = frozen_seed(source)
    members = freeze(inputs.members.write_member_uniref_snapshot, [joined_row("P08159")], source)
    reactions = freeze(inputs.rhea.write_rhea_snapshot, [rhea_row(), rhea_row("RHEA:46988")], source)
    annotations = freeze(inputs.go.write_quickgo_snapshot,
                         [quickgo_row("annotation-a"), quickgo_row("annotation-b")], source)
    output = tmp_path / "scores"
    assert main(["--worklist-json", str(worklist), "--member-json", str(members),
                 "--rhea-json", str(reactions), "--quickgo-json", str(annotations),
                 "--out-dir", str(output), "--snapshot-date", DATE]) == 0
    result = json.loads((output / f"duf-characterization-scores-{DATE}.json").read_text())[0]
    assert result["pfam_id"] == "PF01519"
    assert result["member_count"] == 1
    assert result["rhea_reaction_count"] == 2
    assert result["experimental_go_mf_count"] == 1
    assert result["known_evidence_count"] == 3
    assert result["characterization_status"] == "KNOWN_HISTORICAL_DUF"
    manifest = json.loads((output / f"duf-characterization-scores-{DATE}.manifest.json").read_text())
    assert manifest["input_validation"] == "verified"
    assert set(manifest["input_provenance"]) == {"worklist", "members", "rhea", "quickgo"}
    assert manifest["input_provenance"]["quickgo"]["rows"] == 2
    assert inputs.require_verified_score_worklist(manifest, worklist) == manifest["input_provenance"]["worklist"]


@pytest.mark.parametrize("change,match", [
    (lambda m: m["snapshot"].update(id="wrong"), "identity"),
    (lambda m: m["snapshot"].update(date="2026-09-30"), "identity"),
    (lambda m: m["snapshot"].update(generated_at="yesterday"), "timezone"),
    (lambda m: m["rows"].update(total=2), "row count"),
    (lambda m: m["rows"].update(total=True), "row count"),
    (lambda m: m["source"].update(name="Rhea REST API"), "source identity"),
    (lambda m: m["source"].update(url="https://example.invalid"), "source identity"),
    (lambda m: m["schema"].update(tsv_fieldnames=["pfam_id"]), "header"),
    (lambda m: m["files"]["json"].update(sha256="0" * 64), "SHA-256"),
    (lambda m: m["files"]["json"].update(bytes=0), "byte size"),
    (lambda m: m["files"]["json"].update(path="../escape.json"), "filename"),
    (lambda m: m["files"].pop("tsv"), "companion"),
])
def test_bad_existing_manifest_is_never_bypassed(tmp_path, change, match):
    path = frozen_seed(tmp_path)
    rewrite_manifest(path, change)
    for allow in (False, True):
        with pytest.raises(inputs.ScoreInputError, match=match):
            inputs.load_score_input(path, "worklist", allow_ad_hoc=allow)


@pytest.mark.parametrize("suffix", ["json", "tsv"])
def test_tampered_bytes_fail_even_with_ad_hoc_flag(tmp_path, suffix):
    path = frozen_seed(tmp_path)
    target = path.with_suffix("." + suffix)
    target.write_bytes(target.read_bytes() + b"\n")
    with pytest.raises(inputs.ScoreInputError, match="mismatch"):
        inputs.load_score_input(path, "worklist", allow_ad_hoc=True)


@pytest.mark.parametrize("change,match", [
    (lambda text: text.replace("pfam_id", "wrong_column", 1), "header"),
    (lambda text: text + text.splitlines(keepends=True)[1], "row count"),
    (lambda text: text + "x\n", "row width"),
])
def test_self_consistent_tsv_hash_still_requires_header_count_and_width(tmp_path, change, match):
    path = frozen_seed(tmp_path)
    tsv = path.with_suffix(".tsv")
    tsv.write_text(change(tsv.read_text()))
    refresh_file_entry(path, "tsv")
    with pytest.raises(inputs.ScoreInputError, match=match):
        inputs.load_score_input(path, "worklist")


def test_role_cannot_be_relabelled_by_changing_only_manifest_source_and_header(tmp_path):
    path = freeze(inputs.rhea.write_rhea_snapshot, [], tmp_path)
    rewrite_manifest(path, lambda m: (m.update(source=dict(inputs.INPUT_SPECS["worklist"].source)),
                                      m["schema"].update(tsv_fieldnames=inputs.INPUT_SPECS["worklist"].fields)))
    with pytest.raises(inputs.ScoreInputError, match="stem"):
        inputs.load_score_input(path, "worklist")


@pytest.mark.parametrize("payload", ["{}", '[{"pfam_id":"PF01519"},"discard me"]',
                                      '[{"pfam_id":"PF01519"},null]', '[{"pfam_id":null}]',
                                      '[{"pfam_id":"invalid"}]'])
def test_malformed_rows_cannot_vanish_in_explicit_ad_hoc_mode(tmp_path, payload):
    path = tmp_path / "ad-hoc.json"
    path.write_text(payload)
    with pytest.raises(inputs.ScoreInputError):
        load_json_rows(path, allow_ad_hoc=True)


def test_duplicate_seed_and_member_identities_are_rejected(tmp_path):
    path = freeze(inputs.worklist.write_worklist_snapshot, [seed(), seed()], tmp_path)
    with pytest.raises(inputs.ScoreInputError, match="duplicate worklist identity"):
        inputs.load_score_input(path, "worklist")
    member = freeze(inputs.members.write_member_uniref_snapshot, [joined_row(), joined_row()], tmp_path)
    with pytest.raises(inputs.ScoreInputError, match="duplicate members identity"):
        inputs.load_score_input(member, "members")


def test_one_protein_in_multiple_families_and_distinct_evidence_are_retained(tmp_path):
    member = freeze(inputs.members.write_member_uniref_snapshot,
                    [joined_row(), replace(joined_row(), pfam_id="PF00002")], tmp_path)
    assert len(inputs.load_score_input(member, "members").rows) == 2
    go = freeze(inputs.go.write_quickgo_snapshot, [quickgo_row("a"), quickgo_row("b")], tmp_path)
    assert len(inputs.load_score_input(go, "quickgo").rows) == 2
    cath = freeze(inputs.cath.write_cath_snapshot, [cath_row("protein/1-10"), cath_row("protein/40-50")], tmp_path)
    assert len(inputs.load_score_input(cath, "cath").rows) == 2
    egg = freeze(inputs.egg.write_eggnog_snapshot, [replace(eggnog_row(), seed_ortholog="")], tmp_path)
    assert len(inputs.load_score_input(egg, "eggnog").rows) == 1


def test_missing_manifest_requires_flag_and_changed_bytes_change_provenance(tmp_path):
    path = tmp_path / "arbitrary-name.json"
    row = {"pfam_id": "PF01519", "short_name": "DUF16", "unknown_status": "UNKNOWN_CANDIDATE"}
    path.write_text(json.dumps([row]))
    assert main(["--worklist-json", str(path), "--out-dir", str(tmp_path / "blocked")]) == 1
    assert not (tmp_path / "blocked").exists()
    results = []
    for n in (1, 2):
        if n == 2:
            path.write_text(json.dumps([row, {**row, "pfam_id": "PF00002"}]))
        out = tmp_path / str(n)
        assert main(["--worklist-json", str(path), "--allow-ad-hoc-inputs", "--out-dir", str(out),
                     "--snapshot-date", DATE]) == 0
        result = json.loads((out / f"duf-characterization-scores-{DATE}.manifest.json").read_text())
        assert result["input_validation"] == "ad_hoc"
        assert result["input_provenance"]["worklist"]["manifest_sha256"] is None
        results.append(result)
    assert results[0]["snapshot"]["input_snapshot_ids"] == results[1]["snapshot"]["input_snapshot_ids"]
    assert results[0]["input_provenance"]["worklist"]["sha256"] != results[1]["input_provenance"]["worklist"]["sha256"]
    assert results[0]["input_provenance"]["worklist"]["bytes"] != results[1]["input_provenance"]["worklist"]["bytes"]


def test_each_file_is_captured_once_and_later_replacements_cannot_change_parsed_rows(tmp_path, monkeypatch):
    path = frozen_seed(tmp_path)
    originals = {candidate: candidate.read_bytes() for candidate in tmp_path.iterdir()}
    original_read = inputs._read_bytes
    reads = Counter()

    def capture_and_replace(candidate):
        reads[candidate] += 1
        raw = original_read(candidate)
        if candidate == path:
            candidate.write_text('[{"pfam_id":"PF99999"}]')
        elif candidate == path.with_suffix(".manifest.json"):
            candidate.write_text('{"source":"replaced after capture"}')
        return raw

    monkeypatch.setattr(inputs, "_read_bytes", capture_and_replace)
    loaded = inputs.load_score_input(path, "worklist")
    assert loaded.rows[0]["pfam_id"] == "PF01519"
    assert reads == Counter({candidate: 1 for candidate in originals})
    assert loaded.provenance["sha256"] == hashlib.sha256(originals[path]).hexdigest()
    assert loaded.provenance["manifest_sha256"] == hashlib.sha256(originals[path.with_suffix(".manifest.json")]).hexdigest()


def test_publication_gate_binds_worklist_bytes_and_rejects_all_unverified_roles(tmp_path):
    path = frozen_seed(tmp_path / "source")
    loaded = inputs.load_score_input(path, "worklist")
    manifest = write_score_snapshot([score_row()], tmp_path / "scores", snapshot_date=DATE,
                                    input_snapshot_ids={"worklist": path.stem},
                                    input_provenance={"worklist": loaded.provenance})
    assert inputs.require_verified_score_worklist(manifest, path, worklist_bytes=path.read_bytes())
    for altered in ({}, {**manifest, "input_validation": "ad_hoc"},
                    {**manifest, "input_provenance": {}},
                    {**manifest, "input_provenance_version": 0}):
        with pytest.raises(inputs.ScoreInputError):
            inputs.require_verified_score_worklist(altered, path)
    ad_hoc = tmp_path / "rhea.json"
    ad_hoc.write_text('[{"uniprot_accession":"P08159","rhea_id":"RHEA:10012"}]')
    mixed = copy.deepcopy(manifest)
    mixed["snapshot"]["input_snapshot_ids"]["rhea"] = ad_hoc.stem
    mixed["input_provenance"]["rhea"] = inputs.load_score_input(ad_hoc, "rhea", allow_ad_hoc=True).provenance
    with pytest.raises(inputs.ScoreInputError, match="requires verified"):
        inputs.require_verified_score_worklist(mixed, path)
    path.write_bytes(path.read_bytes() + b"\n")
    refresh_file_entry(path, "json")
    assert inputs.load_score_input(path, "worklist").provenance["sha256"] != loaded.provenance["sha256"]
    with pytest.raises(inputs.ScoreInputError, match="exact verified worklist bytes"):
        inputs.require_verified_score_worklist(manifest, path)


@pytest.mark.parametrize("suffix", [".json", ".manifest.json", ".tsv"])
def test_symlink_input_or_companion_is_not_accepted_as_ad_hoc(tmp_path, suffix):
    path = frozen_seed(tmp_path)
    target = path.with_suffix(suffix)
    saved = target.with_name(target.name + ".original")
    target.rename(saved)
    target.symlink_to(saved)
    with pytest.raises((inputs.ScoreInputError, OSError)):
        inputs.load_score_input(path, "worklist", allow_ad_hoc=True)


def test_duplicate_json_keys_and_nonfinite_values_are_not_valid_inputs(tmp_path):
    path = tmp_path / "ad-hoc.json"
    for text in ('[{"pfam_id":"PF01519","pfam_id":"PF00002"}]',
                 '[{"pfam_id":"PF01519","proteins":NaN}]'):
        path.write_text(text)
        with pytest.raises(inputs.ScoreInputError, match="invalid JSON"):
            inputs.load_score_input(path, "worklist", allow_ad_hoc=True)


def reclassified_seed(directory, *, legacy=False):
    parent = frozen_seed(directory)
    prepared = prepare_reclassification(
        parent, snapshot_date="2026-10-05", generated_at=datetime(2026, 10, 5, tzinfo=timezone.utc),
    )
    inputs.worklist.write_snapshot_artifacts(directory, prepared.artifacts)
    path = directory / prepared.manifest["files"]["json"]["path"]
    if legacy:
        def legacy_profile(manifest):
            derivation = manifest.pop("derivation")
            manifest["source"].update(
                name=inputs.RECLASSIFIED_SOURCE, note=inputs.RECLASSIFICATION_NOTE,
                original_generated_at=derivation["input_snapshot_generated_at"],
            )
            manifest["reclassification"] = {
                **prepared.summary, "policy": inputs.LEGACY_RECLASSIFICATION_POLICY,
            }
        rewrite_manifest(path, legacy_profile)
    return path


@pytest.mark.parametrize("legacy", [False, True])
def test_native_reclassification_profiles_and_inherited_source_are_verified(tmp_path, legacy):
    path = reclassified_seed(tmp_path, legacy=legacy)
    loaded = inputs.load_score_input(path, "worklist")
    assert loaded.provenance["worklist_reclassification"]["profile"] == (
        "reclassification-v1" if legacy else "derivation-v2"
    )
    manifest = write_score_snapshot(
        [score_row()], tmp_path / "scores", snapshot_date=DATE,
        input_snapshot_ids={"worklist": path.stem}, input_provenance={"worklist": loaded.provenance},
    )
    assert inputs.require_verified_score_worklist(manifest, path) == loaded.provenance
    newer = reclassify_snapshot(path, tmp_path, snapshot_date="2026-10-06")
    inherited = inputs.load_score_input(tmp_path / newer["files"]["json"]["path"], "worklist")
    assert inherited.provenance["worklist_reclassification"]["profile"] == "derivation-v2"
    assert inherited.provenance["source"] == loaded.provenance["source"]


@pytest.mark.parametrize("change", [
    lambda m: m.pop("reclassification"),
    lambda m: m["source"].update(name="Unrecognized reclassification"),
    lambda m: m["source"].update(url="https://example.invalid"),
    lambda m: m["source"].update(note="Fetched live"),
    lambda m: m["source"].update(original_generated_at="2026-10-01"),
    lambda m: m["source"].update(original_generated_at="2026-10-07T00:00:00Z"),
    lambda m: m["schema"].update(tsv_fieldnames=["pfam_id"]),
    lambda m: m["snapshot"].update(input_snapshot_ids={"worklist": m["snapshot"]["id"]}),
    lambda m: m["reclassification"].update(source_snapshot="rhea-2026-10-01"),
    lambda m: m["reclassification"].update(source_sha256="bad"),
    lambda m: m["reclassification"].update(policy="anything"),
    lambda m: m["reclassification"].update(rows=0),
    lambda m: m["reclassification"].update(by_unknown_status={}),
    lambda m: m["reclassification"].update(changed_statuses=True),
    lambda m: m["reclassification"]["changes"][0].update(after="incorrect"),
])
def test_reclassification_label_cannot_bypass_native_profile_validation(tmp_path, change):
    path = reclassified_seed(tmp_path, legacy=True)
    rewrite_manifest(path, change)
    for allow in (False, True):
        with pytest.raises(inputs.ScoreInputError):
            inputs.load_score_input(path, "worklist", allow_ad_hoc=allow)


@pytest.mark.parametrize("change", [
    lambda m: m["derivation"].update(method="unknown"),
    lambda m: m["derivation"].update(classifier_policy="unknown"),
    lambda m: m["derivation"].update(fetched_live=True),
    lambda m: m["derivation"].update(changed_fields=["name"]),
    lambda m: m["derivation"].update(input_snapshot_generated_at="invalid"),
    lambda m: m["derivation"]["input_files"].pop("manifest"),
    lambda m: m["derivation"]["input_files"]["json"].update(path="../escape.json"),
])
def test_current_native_derivation_requires_its_declared_provenance(tmp_path, change):
    path = reclassified_seed(tmp_path)
    rewrite_manifest(path, change)
    with pytest.raises(inputs.ScoreInputError):
        inputs.load_score_input(path, "worklist", allow_ad_hoc=True)


@pytest.mark.parametrize("policy", inputs.CLASSIFIER_POLICIES)
def test_versioned_classifier_derivations_stay_loadable(tmp_path, policy):
    parent = frozen_seed(tmp_path)
    manifest = reclassify_snapshot(
        parent, tmp_path, snapshot_date="2026-10-05", classifier_policy=policy,
    )
    loaded = inputs.load_score_input(tmp_path / manifest["files"]["json"]["path"], "worklist")
    assert loaded.provenance["worklist_reclassification"]["policy"] == policy


def test_retained_october_worklist_and_live_members_score_with_verified_provenance(tmp_path):
    retained = Path(__file__).resolve().parents[1] / "data" / "worklists"
    worklist = retained / "interpro-pfam-duf-2026-10-05.json"
    members = retained / "pfam-uniprot-uniref90-2026-10-07.json"
    captured = worklist.read_bytes()
    loaded = inputs.load_score_input(worklist, "worklist", payload_bytes=captured)
    assert len(loaded.rows) == len({row["pfam_id"] for row in loaded.rows}) == 6532
    lineage = loaded.provenance["worklist_reclassification"]
    assert lineage["profile"] == "reclassification-v1"
    assert lineage["input_json_sha256"] == hashlib.sha256(
        (retained / "interpro-pfam-duf-2026-10-01.json").read_bytes()
    ).hexdigest()
    live = inputs.load_score_input(members, "members")
    assert len(live.rows) == 2
    assert {row["pfam_id"] for row in live.rows} == {"PF04149"}
    assert live.provenance["validation_state"] == "verified"
    assert main(["--worklist-json", str(worklist), "--member-json", str(members),
                 "--out-dir", str(tmp_path), "--snapshot-date", "2026-10-07"]) == 0
    scores = json.loads((tmp_path / "duf-characterization-scores-2026-10-07.json").read_text())
    assert len(scores) == 6532
    assert next(row for row in scores if row["pfam_id"] == "PF04149")["member_count"] == 2
    manifest = json.loads((tmp_path / "duf-characterization-scores-2026-10-07.manifest.json").read_text())
    assert manifest["input_validation"] == "verified"
    assert inputs.require_verified_score_worklist(
        manifest, worklist, worklist_bytes=captured,
    ) == loaded.provenance
    manifest["input_provenance"]["worklist"].pop("worklist_reclassification")
    with pytest.raises(inputs.ScoreInputError, match="requires native lineage"):
        inputs.require_verified_score_worklist(manifest, worklist, worklist_bytes=captured)
