from __future__ import annotations

import hashlib
import json
from dataclasses import replace
from datetime import datetime, timezone

import pytest

from dufmech import pages
from dufmech.member_snapshot import write_member_uniref_snapshot
from dufmech.provenance import check_manifest
from dufmech.report import ReportError
from dufmech.scoring_snapshot import write_score_snapshot
from tests.test_member_snapshot import joined_row
from tests.test_report import freeze_worklist
from tests.test_scoring_snapshot import score_row
from tests.test_site import soup


@pytest.fixture
def native(tmp_path, monkeypatch):
    root = tmp_path / "repository"
    directory = root / "data/worklists"
    worklist = freeze_worklist(directory, pfam_id="PF01519")
    monkeypatch.setattr(pages, "REPO_ROOT", root)
    return directory, worklist, tmp_path / "site"


def freeze_members(directory, seed, *, date="2026-10-07", target="UniRef90", row=None):
    write_member_uniref_snapshot(
        [row or joined_row()], directory, snapshot_date=date, seed_snapshot_id=seed,
        uniref_target=target, generated_at=datetime(2026, 10, 7, tzinfo=timezone.utc),
    )
    return directory / f"pfam-uniprot-{target.lower()}-{date}.json"


def render(directory, out, **kwargs):
    pages.render_from_paths(
        worklists_dir=directory, out_dir=out, cross_mech_dir=directory / "no-cross", **kwargs,
    )
    return json.loads((out / "index.json").read_text())


def test_native_discovery_uses_latest_default_target_and_preserves_evidence(native, tmp_path):
    directory, worklist, out = native
    freeze_members(directory, worklist.stem, date="2026-10-06", row=joined_row("OLD123"))
    latest = freeze_members(directory, worklist.stem)
    freeze_members(directory, "different-seed", date="2026-10-08", target="UniRef50")
    payload = render(directory, out)
    assert payload["inputs"] == {"worklist": worklist.stem, "members": latest.stem}
    assert not payload["families"][0]["characterization_status"]
    dataset = payload["provenance"]["members"]
    assert dataset["seed_snapshot_id"] == worklist.stem
    assert dataset["row_count"] == dataset["family_count"] == 1
    for key in ("local_source", "local_manifest", "local_tsv"):
        published = out / dataset[key]
        assert published.read_bytes() == (directory / published.name).read_bytes()
    assert check_manifest(out / dataset["local_manifest"]) == []
    sources = soup(out, "sources.html").select_one("#member-dataset")
    assert dataset["sha256"] in sources.get_text()
    assert "UniProt Consortium" in sources.get_text()
    assert sources.select_one('a[href="https://rest.uniprot.org/help/license"]')
    assert sources.select_one('a[href="https://interpro-documentation.readthedocs.io/en/latest/license.html"]')
    assert soup(out).select_one('a[href="families/PF01519.html#domain-matches"]')
    record = soup(out, "families/PF01519.html")
    assert "39-154 of 163" in record.select_one(".domain-track")["aria-label"]
    assert "OLD123" not in record.get_text()
    assert record.select_one('a[href="../sources.html#member-dataset"]')
    exported = json.loads((out / "families/PF01519.json").read_text())
    assert exported["members"][0]["ranges"] == [[39, 154]]
    second = tmp_path / "second"
    render(directory, second)
    assert pages.diff_trees(out, second) == []


def test_native_discovery_without_members_keeps_explicit_absence(native):
    directory, worklist, out = native
    payload = render(directory, out)
    assert payload["inputs"] == {"worklist": worklist.stem}
    assert "No residue-level domain match evidence" in soup(out, "families/PF01519.html").get_text()
    assert not soup(out, "sources.html").select_one("#member-dataset")


def test_native_discovery_does_not_fall_back_past_wrong_seed(native):
    directory, worklist, out = native
    freeze_members(directory, worklist.stem, date="2026-10-06")
    freeze_members(directory, "interpro-pfam-duf-2026-09-30")
    with pytest.raises(ReportError, match="member snapshot was seeded against"):
        render(directory, out)
    assert not out.exists()


@pytest.mark.parametrize("mode", ["explicit-worklist", "explicit-score", "custom-directory"])
def test_custom_inputs_never_implicitly_adopt_native_members(native, monkeypatch, tmp_path, mode):
    directory, worklist, out = native
    freeze_members(directory, "mismatching-seed")
    kwargs = {}
    if mode == "explicit-worklist":
        kwargs["worklist_json"] = worklist
    elif mode == "explicit-score":
        write_score_snapshot([score_row("PF01519")], directory, snapshot_date="2026-10-02",
                             input_snapshot_ids={"worklist": worklist.stem})
        kwargs["score_json"] = directory / "duf-characterization-scores-2026-10-02.json"
    else:
        monkeypatch.setattr(pages, "REPO_ROOT", tmp_path / "another-repository")
    payload = render(directory, out, **kwargs)
    assert "members" not in payload["inputs"]
    assert not soup(out, "families/PF01519.html").select_one(".domain-track")


def test_explicit_member_selection_is_verified_and_old_datasets_are_pruned(native):
    directory, worklist, out = native
    member = freeze_members(directory, worklist.stem)
    render(directory, out, worklist_json=worklist, members_json=member)
    assert (out / "datasets" / member.name).is_file()
    render(directory, out, worklist_json=worklist)
    assert not (out / "datasets").exists()
    freeze_members(directory, "wrong-seed")
    with pytest.raises(ReportError, match="member snapshot was seeded against"):
        render(directory, out, worklist_json=worklist, members_json=member)


@pytest.mark.parametrize("damage", ["hash", "range", "family"])
def test_native_member_validation_precedes_any_output(native, damage):
    directory, worklist, out = native
    row = joined_row()
    if damage == "range":
        row = replace(row, match_ranges=("1-999",))
    elif damage == "family":
        row = replace(row, pfam_id="PF99999")
    member = freeze_members(directory, worklist.stem, row=row)
    if damage == "hash":
        member.write_text(member.read_text() + " ")
    with pytest.raises(ReportError, match={
        "hash": "sha256 differs", "range": "invalid member match range",
        "family": "member family absent from worklist",
    }[damage]):
        render(directory, out)
    assert not out.exists()


def test_published_member_bundle_preserves_verified_line_endings(native):
    directory, worklist, out = native
    member = freeze_members(directory, worklist.stem)
    manifest_path = member.with_suffix(".manifest.json")
    manifest = json.loads(manifest_path.read_text())
    for extension in ("json", "tsv"):
        path = member.with_suffix(f".{extension}")
        content = path.read_bytes().replace(b"\n", b"\r\n")
        path.write_bytes(content)
        manifest["files"][extension]["bytes"] = len(content)
        manifest["files"][extension]["sha256"] = hashlib.sha256(content).hexdigest()
    manifest_path.write_bytes((json.dumps(manifest, indent=2) + "\n").replace("\n", "\r\n").encode())
    render(directory, out)
    assert check_manifest(out / "datasets" / manifest_path.name) == []
    for path in (member, member.with_suffix(".tsv"), manifest_path):
        assert (out / "datasets" / path.name).read_bytes() == path.read_bytes()
